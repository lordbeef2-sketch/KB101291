# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=3751 end=4000 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-singlepoint-addsignalbasedframe__signalbasedframe.html language=enus -->
## TOPIC 03751: AddSignalBasedFrame(SignalBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-singlepoint-addsignalbasedframe__signalbasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-singlepoint-addsignalbasedframe__signalbasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signalBasedFrame to the Single-Point section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)RemarksFor example code and more information about this method, refer to one of the following help topi

### AddSignalBasedFrame(SignalBasedFrame)

Adds the specified *signalBasedFrame*  to the **Single-Point** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The signal format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-singlepoint-getrawdatabasedframelist.html language=enus -->
## TOPIC 03752: GetRawDataBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-singlepoint-getrawdatabasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-singlepoint-getrawdatabasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the RawDataBasedFrame elements of the current SinglePoint section. This method gets all the incoming single-point, raw data format frames under the current port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RawDataBasedFrame[] GetRawDataBasedFr

### GetRawDataBasedFrameList()

Gets an array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements of the current [SinglePoint](nationalinstruments-veristand-systemdefinitionapi-singlepoint.html) section. This method gets all the incoming single-point, raw data format frames under the current port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html)[] GetRawDataBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements of the current [SinglePoint](nationalinstruments-veristand-systemdefinitionapi-singlepoint.html) section.

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-singlepoint-getsignalbasedframelist.html language=enus -->
## TOPIC 03753: GetSignalBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-singlepoint-getsignalbasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-singlepoint-getsignalbasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SignalBasedFrame elements from the current SinglePoint section. This method gets all the incoming single-point, signal format frames under the current port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedFrame[] GetSignalBasedFrame

### GetSignalBasedFrameList()

Gets an array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [SinglePoint](nationalinstruments-veristand-systemdefinitionapi-singlepoint.html) section. This method gets all the incoming single-point, signal format frames under the current port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html)[] GetSignalBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [SinglePoint](nationalinstruments-veristand-systemdefinitionapi-singlepoint.html) section.

Parent topic:

SinglePoint Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-singlepoint.html language=enus -->
## TOPIC 03754: SinglePoint Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-singlepoint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-singlepoint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Single-Point section under an Incoming section of an NI-XNET CAN, LIN, or FlexRay port. When you import single-point frames, NI VeriStand reads the most recent value received for the frame. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic cla

### SinglePoint Class

Represents the **Single-Point** section under an [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) section of an NI-XNET CAN, LIN, or FlexRay port. When you import single-point frames, NI VeriStand reads the most recent value received for the frame.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SinglePoint : Section

#### Remarks

Use the members of this class to add new or access existing single-point frames.

**Accessing this Class**

- [GetSinglePoint](nationalinstruments-veristand-systemdefinitionapi-incoming-getsinglepoint.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddRawDataBasedFrame(RawDataBasedFrame) | Adds the specified rawDataBasedFrame to the Single-Point section. |
| AddRawDataBasedFrame(RawDataBasedFrame, out Error) | Adds the specified rawDataBasedFrame to the Single-Point section. |
| AddSignalBasedFrame(SignalBasedFrame, out Error) | Adds the specified signalBasedFrame to the Single-Point section. |
| AddSignalBasedFrame(SignalBasedFrame) | Adds the specified signalBasedFrame to the Single-Point section. |
| GetRawDataBasedFrameList() | Gets an array that contains the RawDataBasedFrame elements of the current SinglePoint section. This method gets all the incoming single-point, raw data format frames under the current port. |
| GetSignalBasedFrameList() | Gets an array that contains the SignalBasedFrame elements from the current SinglePoint section. This method gets all the incoming single-point, signal format frames under the current port. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-skipncycles.html language=enus -->
## TOPIC 03755: SkipNCycles

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-skipncycles.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-skipncycles.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume. SyntaxNamespace: NationalInstruments.VeriSta

### SkipNCycles

Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double SkipNCycles { get; set; }

#### Returns

The number of cycles to skip.

Parent topic:

SkipCyclicFrames Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-triggerchannel.html language=enus -->
## TOPIC 03756: TriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-triggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-triggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by SkipNCycles decrements to zero. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Tri

### TriggerChannel

Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by [SkipNCycles](nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-skipncycles.html) decrements to zero.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) TriggerChannel { get; set; }

#### Remarks

Note

This channel is not automatically reset when [SkipNCycles](nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes-skipncycles.html) decrements to zero.

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the trigger channel.

Parent topic:

SkipCyclicFrames Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html language=enus -->
## TOPIC 03757: SkipCyclicFrames Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-skipcyclicframes.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Skip Cyclic Frames channel under the FrameFaulting section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies to skip transmission of a specified number of cyclic frames across the CAN bus when a specified trigger channel has a non-zero value. Derives fromChann

### SkipCyclicFrames Class

Represents the **Skip Cyclic Frames** channel under the [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies to skip transmission of a specified number of cyclic frames across the CAN bus when a specified trigger channel has a non-zero value.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SkipCyclicFrames : Channel

#### Remarks

Use the members of this class to configure the channel and to get or set the trigger channel and the number of cyclic frames to skip.

**Accessing this Class**

- [GetSkipCyclicFrames](nationalinstruments-veristand-systemdefinitionapi-framefaulting-getskipcyclicframes.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| SkipNCycles | Gets or sets the number cycles for which to skip transmission of the frame across the bus. For each skipped cycle, a frame value is dequeued and the skip count is decremented. When the skip count decrements to zero, subsequent cyclic transmissions resume. |
| TriggerChannel | Gets or sets the trigger channel to watch for a non-zero value. Skipping frame transmission begins when this channel value becomes non-zero and stops when the skip count specified by SkipNCycles decrements to zero. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sleepmode-sleepmode__string-string.html language=enus -->
## TOPIC 03758: SleepMode(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sleepmode-sleepmode__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sleepmode-sleepmode__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SleepMode class and creates a Transceiver State, or Sleep Mode, channel with the specified Name and associated triggerNode . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SleepMode(string Name, string triggerNode)ParametersNameTypeDescript

### SleepMode(string, string)

Initializes a new instance of the [SleepMode](nationalinstruments-veristand-systemdefinitionapi-sleepmode.html) class and creates a **Transceiver State**, or Sleep Mode, channel with the specified *Name*  and associated *triggerNode* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SleepMode(string Name, string triggerNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the sleep mode channel. |
| triggerNode | string | The fully qualified path to the node that represents the TriggerChannel in the system definition. Sleep mode is enabled when the value of this channel is non-zero. |

Parent topic:

SleepMode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sleepmode-sleepmode__string.html language=enus -->
## TOPIC 03759: SleepMode(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sleepmode-sleepmode__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sleepmode-sleepmode__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SleepMode class and creates a Transceiver State, or Sleep Mode, channel with the specified triggerNode . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SleepMode(string triggerNode)ParametersNameTypeDescriptiontriggerNodestringThe fully qua

### SleepMode(string)

Initializes a new instance of the [SleepMode](nationalinstruments-veristand-systemdefinitionapi-sleepmode.html) class and creates a **Transceiver State**, or Sleep Mode, channel with the specified *triggerNode* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SleepMode(string triggerNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| triggerNode | string | The fully qualified path to the node that represents the TriggerChannel in the system definition. Sleep mode is enabled when the value of this channel is non-zero. |

Parent topic:

SleepMode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sleepmode-triggerchannel.html language=enus -->
## TOPIC 03760: TriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sleepmode-triggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sleepmode-triggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode TriggerChannel { get; set; }Retur

### TriggerChannel

Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) TriggerChannel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the trigger channel.

Parent topic:

SleepMode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sleepmode.html language=enus -->
## TOPIC 03761: SleepMode Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sleepmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sleepmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Transceiver State, or Sleep Mode, channel under the CANInterfaceChannels section of an NI-XNET CAN port. This channel controls the sleep mode option on the CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame. De

### SleepMode Class

Represents a **Transceiver State**, or Sleep Mode, channel under the [CANInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html) section of an NI-XNET CAN port. This channel controls the sleep mode option on the CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SleepMode : Channel

#### Remarks

**Accessing this Class**

- [GetSleepModeChannel](nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getsleepmodechannel.html)
- SleepMode Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SleepMode(string, string) | Initializes a new instance of the SleepMode class and creates a Transceiver State, or Sleep Mode, channel with the specified Name and associated triggerNode . |
| SleepMode(string) | Initializes a new instance of the SleepMode class and creates a Transceiver State, or Sleep Mode, channel with the specified triggerNode . |

#### Properties

| Name | Description |
| --- | --- |
| TriggerChannel | Gets or sets the channel that triggers sleep mode on an NI-XNET CAN port. If the value of this channel is non-zero, sleep mode is enabled. If the value is zero, sleep mode is disabled. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slsc-addslscchassis__slscchassis-out.html language=enus -->
## TOPIC 03762: AddSLSCChassis(SLSCChassis, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slsc-addslscchassis__slscchassis-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slsc-addslscchassis__slscchassis-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SLSCChassis to the SLSC section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void AddSLSCChassis(SLSCChassis slscChassis, out Error error)ParametersNameTypeDescriptionslscChassisSLSCChassisThe SLSC chassis to add.errorout ErrorReturns an NationalInstru

### AddSLSCChassis(SLSCChassis, out Error)

Adds the specified [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html) to the **SLSC** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void AddSLSCChassis(SLSCChassis slscChassis, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| slscChassis | SLSCChassis | The SLSC chassis to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

SLSC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slsc-exportconfiguration__string-out.html language=enus -->
## TOPIC 03763: ExportConfiguration(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slsc-exportconfiguration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slsc-exportconfiguration__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the SLSC chassis configuration to the file you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ExportConfiguration(string filepath, out Error error)ParametersNameTypeDescriptionfilepathstringThe file to save the SLSC chassis configuration to.errorout Erro

### ExportConfiguration(string, out Error)

Saves the SLSC chassis configuration to the file you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ExportConfiguration(string filepath, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | The file to save the SLSC chassis configuration to. |
| error | out Error | The error output. |

Parent topic:

SLSC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slsc-getslscchassislist.html language=enus -->
## TOPIC 03764: GetSLSCChassisList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slsc-getslscchassislist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slsc-getslscchassislist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SLSCChassis elements from the SLSC section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCChassis[] GetSLSCChassisList()ReturnsAn array that contains the SLSCChassis elements from the SLSC section.

### GetSLSCChassisList()

Gets an array that contains the [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html) elements from the [SLSC](nationalinstruments-veristand-systemdefinitionapi-slsc.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html)[] GetSLSCChassisList()

#### Returns

An array that contains the [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html) elements from the [SLSC](nationalinstruments-veristand-systemdefinitionapi-slsc.html) section.

Parent topic:

SLSC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slsc-importconfigurations__string-out.html language=enus -->
## TOPIC 03765: ImportConfigurations(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slsc-importconfigurations__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slsc-importconfigurations__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the SLSC chassis configuration from the file you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ImportConfigurations(string filepath, out Error error)ParametersNameTypeDescriptionfilepathstringThe file to load the SLSC chassis configuration from.errorout

### ImportConfigurations(string, out Error)

Loads the SLSC chassis configuration from the file you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ImportConfigurations(string filepath, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | The file to load the SLSC chassis configuration from. |
| error | out Error | The error output. |

Parent topic:

SLSC Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slsc.html language=enus -->
## TOPIC 03766: SLSC Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slsc.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slsc.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SLSC section of a Hardware. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SLSC : SectionRemarksUse the members of this class to add a new SLSC chassis or get a list of existing SLSC chassis. MethodsNameDescriptionAddSLSCChassis(SLSCC

### SLSC Class

Represents the **SLSC** section of a [Hardware](nationalinstruments-veristand-systemdefinitionapi-hardware.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SLSC : Section

#### Remarks

Use the members of this class to add a new SLSC chassis or get a list of existing SLSC chassis.

#### Methods

| Name | Description |
| --- | --- |
| AddSLSCChassis(SLSCChassis, out Error) | Adds the specified SLSCChassis to the SLSC section. |
| ExportConfiguration(string, out Error) | Saves the SLSC chassis configuration to the file you specify. |
| GetSLSCChassisList() | Gets an array that contains the SLSCChassis elements from the SLSC section. |
| ImportConfigurations(string, out Error) | Loads the SLSC chassis configuration from the file you specify. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassisid.html language=enus -->
## TOPIC 03767: ChassisID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassisid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassisid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name or the IP address of the SLSCChassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ChassisID { get; set; }ReturnsThe IP address.

### ChassisID

Gets or sets the name or the IP address of the SLSCChassis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ChassisID { get; set; }

#### Returns

The IP address.

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassisidtype.html language=enus -->
## TOPIC 03768: ChassisIDType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassisidtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassisidtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the mode how the cahssis is defined. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCChassisIDType ChassisIDType { get; set; }ReturnsAn enumerable value represents a chassis name or an IP address(hostname)

### ChassisIDType

Gets or sets the mode how the cahssis is defined.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSCChassisIDType](nationalinstruments-veristand-systemdefinitionapi-slscchassis-slscchassisidtype.html) ChassisIDType { get; set; }

#### Returns

An enumerable value represents a chassis name or an IP address(hostname)

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassistype.html language=enus -->
## TOPIC 03769: ChassisType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassistype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-chassistype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of the SLSCChassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ChassisType { get; private set; }ReturnsThe type of the SLSCChassis.

### ChassisType

Gets the type of the SLSCChassis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ChassisType { get; private set; }

#### Returns

The type of the SLSCChassis.

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-exportconfiguration__string-out.html language=enus -->
## TOPIC 03770: ExportConfiguration(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-exportconfiguration__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-exportconfiguration__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the SLSC chassis configuration to the file you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ExportConfiguration(string filepath, out Error error)ParametersNameTypeDescriptionfilepathstringThe file to save the SLSC chassis configuration to.errorout Erro

### ExportConfiguration(string, out Error)

Saves the SLSC chassis configuration to the file you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ExportConfiguration(string filepath, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | The file to save the SLSC chassis configuration to. |
| error | out Error | The Error output. |

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-getchassischannelssection.html language=enus -->
## TOPIC 03771: GetChassisChannelsSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-getchassischannelssection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-getchassischannelssection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get the SLSCChassisChannels element under the SLSCChassis section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCChassisChannels GetChassisChannelsSection()ReturnsA SLSCChassisChannels object.

### GetChassisChannelsSection()

Get the [SLSCChassisChannels](nationalinstruments-veristand-systemdefinitionapi-slscchassischannels.html) element under the [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSCChassisChannels](nationalinstruments-veristand-systemdefinitionapi-slscchassischannels.html) GetChassisChannelsSection()

#### Returns

A [SLSCChassisChannels](nationalinstruments-veristand-systemdefinitionapi-slscchassischannels.html) object.

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-getmodulessection.html language=enus -->
## TOPIC 03772: GetModulesSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-getmodulessection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-getmodulessection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SLSCModules section under the SLSC Chassis, which contains all the SLSCModuleCustomDevices. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCModules GetModulesSection()ReturnsA SLSCModules object.

### GetModulesSection()

Gets the [SLSCModules](nationalinstruments-veristand-systemdefinitionapi-slscmodules.html) section under the SLSC Chassis, which contains all the [SLSCModuleCustomDevice](nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html)s.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSCModules](nationalinstruments-veristand-systemdefinitionapi-slscmodules.html) GetModulesSection()

#### Returns

A [SLSCModules](nationalinstruments-veristand-systemdefinitionapi-slscmodules.html) object.

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-password.html language=enus -->
## TOPIC 03773: Password

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-password.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-password.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the password for the SLSCChassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Password { get; set; }ReturnsThe password.

### Password

Gets or sets the password for the SLSCChassis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Password { get; set; }

#### Returns

The password.

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-slscchassis__string-slscchassistype.html language=enus -->
## TOPIC 03774: SLSCChassis(string, SLSCChassisType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-slscchassis__string-slscchassistype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-slscchassis__string-slscchassistype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SLSCChassis class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCChassis(string name, SLSCChassisType chassisType)ParametersNameTypeDescriptionnamestringThe name of the SLSCChassis.chassisTypeSLSCChassisTypeThe type of a defined SLSC c

### SLSCChassis(string, SLSCChassisType)

Initializes a new instance of the [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SLSCChassis(string name, SLSCChassisType chassisType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the SLSCChassis. |
| chassisType | SLSCChassisType | The type of a defined SLSC chassis. |

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis-username.html language=enus -->
## TOPIC 03775: Username

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis-username.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis-username.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the username for the SLSCChassis. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Username { get; set; }ReturnsThe username.

### Username

Gets or sets the username for the SLSCChassis.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Username { get; set; }

#### Returns

The username.

Parent topic:

SLSCChassis Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassis.html language=enus -->
## TOPIC 03776: SLSCChassis Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassis.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassis.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SLSCChassis section of the SLSC. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SLSCChassis : SectionConstructorsNameDescriptionSLSCChassis(string, SLSCChassisType)Initializes a new instance of the SLSCChassis class. PropertiesNameDes

### SLSCChassis Class

Represents the **SLSCChassis** section of the [SLSC](nationalinstruments-veristand-systemdefinitionapi-slsc.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SLSCChassis : Section

#### Constructors

| Name | Description |
| --- | --- |
| SLSCChassis(string, SLSCChassisType) | Initializes a new instance of the SLSCChassis class. |

#### Properties

| Name | Description |
| --- | --- |
| ChassisID | Gets or sets the name or the IP address of the SLSCChassis. |
| ChassisIDType | Gets or sets the mode how the cahssis is defined. |
| ChassisType | Gets the type of the SLSCChassis. |
| Password | Gets or sets the password for the SLSCChassis. |
| Username | Gets or sets the username for the SLSCChassis. |

#### Methods

| Name | Description |
| --- | --- |
| ExportConfiguration(string, out Error) | Saves the SLSC chassis configuration to the file you specify. |
| GetChassisChannelsSection() | Get the SLSCChassisChannels element under the SLSCChassis section. |
| GetModulesSection() | Gets the SLSCModules section under the SLSC Chassis, which contains all the SLSCModuleCustomDevices. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassischannel.html language=enus -->
## TOPIC 03777: SLSCChassisChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassischannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassischannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SLSC chassis channel node of a SLSCChassisChannelSection. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SLSCChassisChannel : Channel

### SLSCChassisChannel Class

Represents the **SLSC chassis channel** node of a [SLSCChassisChannelSection](nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection.html).

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SLSCChassisChannel : Channel

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassischannels-getchassischannelsections.html language=enus -->
## TOPIC 03778: GetChassisChannelSections()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassischannels-getchassischannelsections.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassischannels-getchassischannelsections.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the list of SLSC physical channels saved in SLSCChassisChannelSection array. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCChassisChannelSection[] GetChassisChannelSections()ReturnsArray of SLSCChassisChannelSection.

### GetChassisChannelSections()

Gets the list of SLSC physical channels saved in SLSCChassisChannelSection array.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSCChassisChannelSection](nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection.html)[] GetChassisChannelSections()

#### Returns

Array of SLSCChassisChannelSection.

Parent topic:

SLSCChassisChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassischannels.html language=enus -->
## TOPIC 03779: SLSCChassisChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassischannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassischannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SLSCChassisChannels section of the SLSCChassis. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SLSCChassisChannels : SectionMethodsNameDescriptionGetChassisChannelSections()Gets the list of SLSC physical channels saved in SLSCChassisC

### SLSCChassisChannels Class

Represents the **SLSCChassisChannels** section of the [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SLSCChassisChannels : Section

#### Methods

| Name | Description |
| --- | --- |
| GetChassisChannelSections() | Gets the list of SLSC physical channels saved in SLSCChassisChannelSection array. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection-getslscchassischannellist.html language=enus -->
## TOPIC 03780: GetSLSCChassisChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection-getslscchassischannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection-getslscchassischannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SLSCChassisChannel elements from the SLSCChassisChannelSection section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCChassisChannel[] GetSLSCChassisChannelList()ReturnsAn array that contains the SLSCChassisChannel elements from the SLSC

### GetSLSCChassisChannelList()

Gets an array that contains the [SLSCChassisChannel](nationalinstruments-veristand-systemdefinitionapi-slscchassischannel.html) elements from the [SLSCChassisChannelSection](nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSCChassisChannel](nationalinstruments-veristand-systemdefinitionapi-slscchassischannel.html)[] GetSLSCChassisChannelList()

#### Returns

An array that contains the [SLSCChassisChannel](nationalinstruments-veristand-systemdefinitionapi-slscchassischannel.html) elements from the [SLSCChassisChannelSection](nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection.html) section.

Parent topic:

SLSCChassisChannelSection Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection.html language=enus -->
## TOPIC 03781: SLSCChassisChannelSection Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscchassischannelsection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SLSC chassis channel category section of an SLSCChassis. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SLSCChassisChannelSection : SectionRemarksUse the members of this class to add a new SLSC chassis channel section or get a list of

### SLSCChassisChannelSection Class

Represents the **SLSC chassis channel category** section of an [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SLSCChassisChannelSection : Section

#### Remarks

Use the members of this class to add a new SLSC chassis channel section or get a list of existing SLSC chassis channel sections.

#### Methods

| Name | Description |
| --- | --- |
| GetSLSCChassisChannelList() | Gets an array that contains the SLSCChassisChannel elements from the SLSCChassisChannelSection section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-removenode.html language=enus -->
## TOPIC 03782: RemoveNode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-removenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-removenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes this node from the hierarchy, if the node can be removed. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override bool RemoveNode()Returnstrue if the node was removed successfully.

### RemoveNode()

Removes this node from the hierarchy, if the node can be removed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override bool RemoveNode()

#### Returns

true if the node was removed successfully.

Parent topic:

SLSCModuleCustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-slotnumber.html language=enus -->
## TOPIC 03783: SlotNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-slotnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-slotnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The slot number of the SLSC chassis with which the custom device is associated. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int SlotNumber { get; set; }

### SlotNumber

The slot number of the SLSC chassis with which the custom device is associated.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int SlotNumber { get; set; }

Parent topic:

SLSCModuleCustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-slscmodulecustomdevice__string-string-int.html language=enus -->
## TOPIC 03784: SLSCModuleCustomDevice(string, string, int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-slscmodulecustomdevice__string-string-int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice-slscmodulecustomdevice__string-string-int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the SLSCModuleCustomDevice class. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCModuleCustomDevice(string name, string guid, int slotNumber)ParametersNameTypeDescriptionnamestringThe name associated with the custom device, as specified in

### SLSCModuleCustomDevice(string, string, int)

Initializes a new instance of the [SLSCModuleCustomDevice](nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html) class.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SLSCModuleCustomDevice(string name, string guid, int slotNumber)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name associated with the custom device, as specified in the Custom Device XML file. |
| guid | string | The GUID associated with the custom device, as specified in the Custom Device XML file. |
| slotNumber | int | The slot number of the SLSC module in the chassis. |

Parent topic:

SLSCModuleCustomDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html language=enus -->
## TOPIC 03785: SLSCModuleCustomDevice Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an SLSC module custom device. Derives fromCustomDeviceSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SLSCModuleCustomDevice : CustomDeviceConstructorsNameDescriptionSLSCModuleCustomDevice(string, string, int)Initializes a new instance of the SLSCModuleCusto

### SLSCModuleCustomDevice Class

Represents an SLSC module custom device.

#### Derives from

- CustomDevice

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SLSCModuleCustomDevice : CustomDevice

#### Constructors

| Name | Description |
| --- | --- |
| SLSCModuleCustomDevice(string, string, int) | Initializes a new instance of the SLSCModuleCustomDevice class. |

#### Properties

| Name | Description |
| --- | --- |
| SlotNumber | The slot number of the SLSC chassis with which the custom device is associated. |

#### Methods

| Name | Description |
| --- | --- |
| RemoveNode() | Removes this node from the hierarchy, if the node can be removed. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscmodules-getmodule__int-out.html language=enus -->
## TOPIC 03786: GetModule(int, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscmodules-getmodule__int-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscmodules-getmodule__int-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SLSCModuleCustomDevice for the specified slot number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SLSCModuleCustomDevice GetModule(int slotNumber, out Error error)ParametersNameTypeDescriptionslotNumberintThe 1-indexed slot number of the module.errorout ErrorRet

### GetModule(int, out Error)

Gets the [SLSCModuleCustomDevice](nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html) for the specified slot number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SLSCModuleCustomDevice](nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html) GetModule(int slotNumber, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| slotNumber | int | The 1-indexed slot number of the module. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The custom device associated with the specified slot, or null if the slot is empty.

Parent topic:

SLSCModules Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscmodules-setmodule__int-slscmodulecustomdevice-out.html language=enus -->
## TOPIC 03787: SetModule(int, SLSCModuleCustomDevice, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscmodules-setmodule__int-slscmodulecustomdevice-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscmodules-setmodule__int-slscmodulecustomdevice-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the SLSCModuleCustomDevice for the specified slot number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetModule(int slotNumber, SLSCModuleCustomDevice customDevice, out Error error)ParametersNameTypeDescriptionslotNumberintThe 1-indexed slot number of the modul

### SetModule(int, SLSCModuleCustomDevice, out Error)

Sets the [SLSCModuleCustomDevice](nationalinstruments-veristand-systemdefinitionapi-slscmodulecustomdevice.html) for the specified slot number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetModule(int slotNumber, SLSCModuleCustomDevice customDevice, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| slotNumber | int | The 1-indexed slot number of the module. |
| customDevice | SLSCModuleCustomDevice | The custom device to use for the module. If null, the slot will be set to empty. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

SLSCModules Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-slscmodules.html language=enus -->
## TOPIC 03788: SLSCModules Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-slscmodules.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-slscmodules.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the SLSCModules section of the SLSCChassis. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SLSCModules : SectionMethodsNameDescriptionGetModule(int, out Error)Gets the SLSCModuleCustomDevice for the specified slot number. SetModule(int, S

### SLSCModules Class

Represents the **SLSCModules** section of the [SLSCChassis](nationalinstruments-veristand-systemdefinitionapi-slscchassis.html).

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SLSCModules : Section

#### Methods

| Name | Description |
| --- | --- |
| GetModule(int, out Error) | Gets the SLSCModuleCustomDevice for the specified slot number. |
| SetModule(int, SLSCModuleCustomDevice, out Error) | Sets the SLSCModuleCustomDevice for the specified slot number. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sporadic-addrawdatabasedframe__rawdatabasedframe-out.html language=enus -->
## TOPIC 03789: AddRawDataBasedFrame(RawDataBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sporadic-addrawdatabasedframe__rawdatabasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sporadic-addrawdatabasedframe__rawdatabasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified rawDataBasedFrame to the Sporadic section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe raw data format fra

### AddRawDataBasedFrame(RawDataBasedFrame, out Error)

Adds the specified *rawDataBasedFrame*  to the **Sporadic** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The raw data format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

Sporadic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sporadic-addrawdatabasedframe__rawdatabasedframe.html language=enus -->
## TOPIC 03790: AddRawDataBasedFrame(RawDataBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sporadic-addrawdatabasedframe__rawdatabasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sporadic-addrawdatabasedframe__rawdatabasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified rawDataBasedFrame to the Sporadic section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe raw data format frame to add. Return

### AddRawDataBasedFrame(RawDataBasedFrame)

Adds the specified *rawDataBasedFrame*  to the **Sporadic** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The raw data format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

Sporadic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sporadic-addsignalbasedframe__signalbasedframe-out.html language=enus -->
## TOPIC 03791: AddSignalBasedFrame(SignalBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sporadic-addsignalbasedframe__signalbasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sporadic-addsignalbasedframe__signalbasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signalBasedFrame to the Sporadic section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)RemarksFor example code and more information about this method, refer to one of the follow

### AddSignalBasedFrame(SignalBasedFrame, out Error)

Adds the specified *signalBasedFrame*  to the **Sporadic** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The signal format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

Sporadic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sporadic-addsignalbasedframe__signalbasedframe.html language=enus -->
## TOPIC 03792: AddSignalBasedFrame(SignalBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sporadic-addsignalbasedframe__signalbasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sporadic-addsignalbasedframe__signalbasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signalBasedFrame to the Sporadic section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)RemarksFor example code and more information about this method, refer to one of the following help topics:

### AddSignalBasedFrame(SignalBasedFrame)

Adds the specified *signalBasedFrame*  to the **Sporadic** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The signal format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

Sporadic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sporadic-getrawdatabasedframelist.html language=enus -->
## TOPIC 03793: GetRawDataBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sporadic-getrawdatabasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sporadic-getrawdatabasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the RawDataBasedFrame elements of the current Sporadic section. This method gets all the incoming sporadic, raw data format frames under the current port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RawDataBasedFrame[] GetRawDataBasedFrameList

### GetRawDataBasedFrameList()

Gets an array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements of the current [Sporadic](nationalinstruments-veristand-systemdefinitionapi-sporadic.html) section. This method gets all the incoming sporadic, raw data format frames under the current port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html)[] GetRawDataBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements of the current [Sporadic](nationalinstruments-veristand-systemdefinitionapi-sporadic.html) section.

Parent topic:

Sporadic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sporadic-getsignalbasedframelist.html language=enus -->
## TOPIC 03794: GetSignalBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sporadic-getsignalbasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sporadic-getsignalbasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SignalBasedFrame elements from the current Sporadic section. This method gets all the incoming sporadic, signal format frames under the current port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedFrame[] GetSignalBasedFrameList()R

### GetSignalBasedFrameList()

Gets an array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [Sporadic](nationalinstruments-veristand-systemdefinitionapi-sporadic.html) section. This method gets all the incoming sporadic, signal format frames under the current port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html)[] GetSignalBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [Sporadic](nationalinstruments-veristand-systemdefinitionapi-sporadic.html) section.

Parent topic:

Sporadic Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-sporadic.html language=enus -->
## TOPIC 03795: Sporadic Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-sporadic.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-sporadic.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Sporadic section that contains outgoing, sporadic frames under an NI-XNET LIN port. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Sporadic : SectionRemarksUse the members of this class to add or access sporadic frames. Sporadic frame

### Sporadic Class

Represents the **Sporadic** section that contains outgoing, sporadic frames under an NI-XNET LIN port.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Sporadic : Section

#### Remarks

Use the members of this class to add or access sporadic frames.

Sporadic frames attempt to provide dynamic behavior to LIN. Sporadic frames always carry signals (data), and their IDs are 0 – 59 (0x3B). Only the slave task associated with the master node can send sporadic frames. The header of a sporadic frame is sent in its frame slot only when the master task knows that a data value (signal) within the frame has been updated. If multiple unconditional frames associated with a sporadic slot have updated data, the master transmits only the highest priority frame, which the order that the frames appear in the sporadic frame list determines.

**Accessing this Class**

- [GetSporadic](nationalinstruments-veristand-systemdefinitionapi-outgoing-getsporadic.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddRawDataBasedFrame(RawDataBasedFrame) | Adds the specified rawDataBasedFrame to the Sporadic section. |
| AddRawDataBasedFrame(RawDataBasedFrame, out Error) | Adds the specified rawDataBasedFrame to the Sporadic section. |
| AddSignalBasedFrame(SignalBasedFrame, out Error) | Adds the specified signalBasedFrame to the Sporadic section. |
| AddSignalBasedFrame(SignalBasedFrame) | Adds the specified signalBasedFrame to the Sporadic section. |
| GetRawDataBasedFrameList() | Gets an array that contains the RawDataBasedFrame elements of the current Sporadic section. This method gets all the incoming sporadic, raw data format frames under the current port. |
| GetSignalBasedFrameList() | Gets an array that contains the SignalBasedFrame elements from the current Sporadic section. This method gets all the incoming sporadic, signal format frames under the current port. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus-analysisbuffersize.html language=enus -->
## TOPIC 03796: AnalysisBufferSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus-analysisbuffersize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus-analysisbuffersize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpubli

### AnalysisBufferSize

Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int AnalysisBufferSize { get; set; }

#### Remarks

Note

This property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Returns

The analysis buffer size.

Parent topic:

Stimulus Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus-analysisresultsize.html language=enus -->
## TOPIC 03797: AnalysisResultSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus-analysisresultsize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus-analysisresultsize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test. SyntaxNamespace: NationalInstruments.Ver

### AnalysisResultSize

Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int AnalysisResultSize { get; set; }

#### Remarks

Note

This property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Returns

The analysis failure result buffer size.

Parent topic:

Stimulus Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus-auxilliarybuffersize.html language=enus -->
## TOPIC 03798: AuxilliaryBufferSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus-auxilliarybuffersize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus-auxilliarybuffersize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by

### AuxilliaryBufferSize

Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int AuxilliaryBufferSize { get; set; }

#### Remarks

Note

This property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Returns

The auxiliary buffer size.

Parent topic:

Stimulus Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus-getgeneratorlist.html language=enus -->
## TOPIC 03799: GetGeneratorList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus-getgeneratorlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus-getgeneratorlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Generator elements from the Stimulus section. This method gets a list of existing stimulus generators in the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Generator[] GetGeneratorList()RemarksThis method is obsolete in NI

### GetGeneratorList()

Gets an array that contains the [Generator](nationalinstruments-veristand-systemdefinitionapi-generator.html) elements from the [Stimulus](nationalinstruments-veristand-systemdefinitionapi-stimulus.html) section. This method gets a list of existing stimulus generators in the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Generator](nationalinstruments-veristand-systemdefinitionapi-generator.html)[] GetGeneratorList()

#### Remarks

Note

This method is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [Generator](nationalinstruments-veristand-systemdefinitionapi-generator.html) elements from the [Stimulus](nationalinstruments-veristand-systemdefinitionapi-stimulus.html) section.

Parent topic:

Stimulus Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus-maxgenmaps.html language=enus -->
## TOPIC 03800: MaxGenMaps

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus-maxgenmaps.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus-maxgenmaps.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum number of stimulus generator mappings across the entire system. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int MaxGenMaps { get; set; }RemarksThis property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version

### MaxGenMaps

Gets or sets the maximum number of stimulus generator mappings across the entire system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int MaxGenMaps { get; set; }

#### Remarks

Note

This property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Returns

The maximum number of stimulus generator mappings.

Parent topic:

Stimulus Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus-maxsteps.html language=enus -->
## TOPIC 03801: MaxSteps

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus-maxsteps.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus-maxsteps.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int MaxSteps { get; set; }RemarksThis property is ob

### MaxSteps

Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int MaxSteps { get; set; }

#### Remarks

Note

This property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Returns

The maximum number of steps a generator can contain.

Parent topic:

Stimulus Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus-setgeneratorcount__int.html language=enus -->
## TOPIC 03802: SetGeneratorCount(int)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus-setgeneratorcount__int.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus-setgeneratorcount__int.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the number of stimulus generators in the system. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetGeneratorCount(int Count)RemarksThis method is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor.

### SetGeneratorCount(int)

Sets the number of stimulus generators in the system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetGeneratorCount(int Count)

#### Remarks

Note

This method is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Count | int | The number of generators. |

#### Returns

true if the number of generators was set successfully.

Parent topic:

Stimulus Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimulus.html language=enus -->
## TOPIC 03803: Stimulus Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimulus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimulus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Stimulus section of a Target, which contains the stimulus generators available in the Legacy Stimulus Profile Editor. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Stimulus : SectionRemarksThis class is obsolete in NI VeriStand 2011

### Stimulus Class

Represents the **Stimulus** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html), which contains the stimulus generators available in the Legacy Stimulus Profile Editor.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Stimulus : Section

#### Remarks

Note

This class is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

**Accessing this Class**

- [GetStimulus](nationalinstruments-veristand-systemdefinitionapi-target-getstimulus.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| AnalysisBufferSize | Gets or sets the size of the analysis buffer. The analysis buffer stores the expected result values for a table test. Set this value to a number that matches or exceeds the number of expected result values in a given table test. |
| AnalysisResultSize | Gets or sets the size of the analysis failure result buffer. The analysis failure result buffer stores the failure results for a table test. Set this value to a number that meets or exceeds the maximum number of failures you expect to occur in the table test. |
| AuxilliaryBufferSize | Gets or sets the size of the auxiliary buffer. The auxiliary buffer stores multi-point playback data in comma-separated value (CSV), files. Set this buffer size to a number that matches or exceeds the number of data points in the CSV file you want to play back. The auxiliary buffer size is shared by all active stimulus generators, so all generators can have up to Auxiliary Buffer Size total in data points for playback. |
| MaxGenMaps | Gets or sets the maximum number of stimulus generator mappings across the entire system. |
| MaxSteps | Gets or sets the maximum number of steps a stimulus generator can contain. Set this value to a number that is larger than the number of steps in the longest generator script. |

#### Methods

| Name | Description |
| --- | --- |
| GetGeneratorList() | Gets an array that contains the Generator elements from the Stimulus section. This method gets a list of existing stimulus generators in the system definition. |
| SetGeneratorCount(int) | Sets the number of stimulus generators in the system. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimuluschannel-units.html language=enus -->
## TOPIC 03804: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimuluschannel-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimuluschannel-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units associated with the stimulus channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override string Units { get; }RemarksThis property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Us

### Units

Gets the units associated with the stimulus channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override string Units { get; }

#### Remarks

Note

This property is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Returns

The units associated with the channel.

Parent topic:

StimulusChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-stimuluschannel.html language=enus -->
## TOPIC 03805: StimulusChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-stimuluschannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-stimuluschannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a stimulus channel of a Generator. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class StimulusChannel : ChannelRemarksThis class is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile

### StimulusChannel Class

Represents a stimulus channel of a [Generator](nationalinstruments-veristand-systemdefinitionapi-generator.html).

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class StimulusChannel : Channel

#### Remarks

Note

This class is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

**Accessing this Class**

- [GetStimulusChannelList](nationalinstruments-veristand-systemdefinitionapi-generator-getstimuluschannellist.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Units | Gets the units associated with the stimulus channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemchannel-units.html language=enus -->
## TOPIC 03806: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemchannel-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemchannel-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units associated with the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override string Units { get; }ReturnsThe units associated with the channel.

### Units

Gets the units associated with the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override string Units { get; }

#### Returns

The units associated with the channel.

Parent topic:

SystemChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemchannel.html language=enus -->
## TOPIC 03807: SystemChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a system channel under the SystemChannels section. System channels monitor the state and condition of various aspects of the system. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SystemChannel : ChannelRemarksUse the members of this clas

### SystemChannel Class

Represents a system channel under the [SystemChannels](nationalinstruments-veristand-systemdefinitionapi-systemchannels.html) section. System channels monitor the state and condition of various aspects of the system.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SystemChannel : Channel

#### Remarks

Use the members of this class to get the units associated with the channel.

**Accessing this Class**

- [GetSystemChannels](nationalinstruments-veristand-systemdefinitionapi-systemchannels-getsystemchannels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| Units | Gets the units associated with the channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemchannels-getsystemchannels.html language=enus -->
## TOPIC 03808: GetSystemChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemchannels-getsystemchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemchannels-getsystemchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SystemChannel elements from the SystemChannels section. This method gets the individual system channels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SystemChannel[] GetSystemChannels()RemarksModifications you make to the contents of this l

### GetSystemChannels()

Gets an array that contains the [SystemChannel](nationalinstruments-veristand-systemdefinitionapi-systemchannel.html) elements from the [SystemChannels](nationalinstruments-veristand-systemdefinitionapi-systemchannels.html) section. This method gets the individual system channels.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SystemChannel](nationalinstruments-veristand-systemdefinitionapi-systemchannel.html)[] GetSystemChannels()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SystemChannel](nationalinstruments-veristand-systemdefinitionapi-systemchannel.html) elements from the [SystemChannels](nationalinstruments-veristand-systemdefinitionapi-systemchannels.html) section.

Parent topic:

SystemChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemchannels.html language=enus -->
## TOPIC 03809: SystemChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the System Channels section of a Target, which contains a variety of channels that monitor the state and condition of various aspects of the system. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SystemChannels : SectionRemarksUse the mem

### SystemChannels Class

Represents the **System Channels** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html), which contains a variety of channels that monitor the state and condition of various aspects of the system.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SystemChannels : Section

#### Remarks

Use the members of this class to access the system channels.

**Accessing this Class**

- [GetSystemChannels](nationalinstruments-veristand-systemdefinitionapi-target-getsystemchannels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetSystemChannels() | Gets an array that contains the SystemChannel elements from the SystemChannels section. This method gets the individual system channels. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition-documenttype.html language=enus -->
## TOPIC 03810: DocumentType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition-documenttype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition-documenttype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The DocumentType for this SystemDefinition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DocumentType DocumentType { get; }

### DocumentType

The DocumentType for this SystemDefinition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public DocumentType DocumentType { get; }

Parent topic:

SystemDefinition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition-root.html language=enus -->
## TOPIC 03811: Root

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition-root.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition-root.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Root node of the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Root Root { get; }RemarksFor example code and more information about this property, refer to one of the following help topics: LabVIEW Walkthrough: Modifying a System Definition

### Root

Gets the [Root](nationalinstruments-veristand-systemdefinitionapi-root.html) node of the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Root](nationalinstruments-veristand-systemdefinitionapi-root.html) Root { get; }

#### Remarks

For example code and more information about this property, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

A [Root](nationalinstruments-veristand-systemdefinitionapi-root.html) object.

Parent topic:

SystemDefinition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition-savesystemdefinitionfile__out.html language=enus -->
## TOPIC 03812: SaveSystemDefinitionFile(out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition-savesystemdefinitionfile__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition-savesystemdefinitionfile__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SaveSystemDefinitionFile(out string error)RemarksThis method saves the file to the location specified by the file path stored within the class instance. ParametersNameTypeDescriptionerroro

### SaveSystemDefinitionFile(out string)

Saves the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SaveSystemDefinitionFile(out string error)

#### Remarks

This method saves the file to the location specified by the file path stored within the class instance.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out string | Upon return, contains the error that caused the system definition file not to be saved. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the system definition file was saved successfully.

Parent topic:

SystemDefinition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition-savesystemdefinitionfile__string-out.html language=enus -->
## TOPIC 03813: SaveSystemDefinitionFile(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition-savesystemdefinitionfile__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition-savesystemdefinitionfile__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves the system definition file to the specified location. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SaveSystemDefinitionFile(string filepath, out string error)RemarksThis method updates the file path stored with the class instance to the specified filepath . Par

### SaveSystemDefinitionFile(string, out string)

Saves the system definition file to the specified location.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SaveSystemDefinitionFile(string filepath, out string error)

#### Remarks

This method updates the file path stored with the class instance to the specified *filepath* .

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | The location to save the system definition file. |
| error | out string | Upon return, contains the error that caused the system definition file not to be saved. If no error occurs, this parameter contains an empty string. |

#### Returns

true if the system definition file was saved successfully.

Parent topic:

SystemDefinition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition-systemdefinition__string-string-string-string-string-string-string.html language=enus -->
## TOPIC 03814: SystemDefinition(string, string, string, string, string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition-systemdefinition__string-string-string-string-string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition-systemdefinition__string-string-string-string-string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SystemDefinition with the specified configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SystemDefinition(string Name, string Description, string Creator, string Version, string TargetName, string TargetType, string filepath)Parameters

### SystemDefinition(string, string, string, string, string, string, string)

Initializes a new instance of [SystemDefinition](nationalinstruments-veristand-systemdefinitionapi-systemdefinition.html) with the specified configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SystemDefinition(string Name, string Description, string Creator, string Version, string TargetName, string TargetType, string filepath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the system definition. |
| Description | string | The description of the system definition. |
| Creator | string | The user account name of the system definition file creator. |
| Version | string | The file format version of the system definition file. |
| TargetName | string | The name of the default target. |
| TargetType | string | The operating system of the default target. Valid values are: Windows, PharLap, or VxWorks. |
| filepath | string | The path to the system definition file on disk. |

Parent topic:

SystemDefinition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition-systemdefinition__string.html language=enus -->
## TOPIC 03815: SystemDefinition(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition-systemdefinition__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition-systemdefinition__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of SystemDefinition with the specified file path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SystemDefinition(string nivssdfFile)RemarksFor example code and more information about this method, refer to one of the following help topics: LabVIEW

### SystemDefinition(string)

Initializes a new instance of [SystemDefinition](nationalinstruments-veristand-systemdefinitionapi-systemdefinition.html) with the specified file path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public SystemDefinition(string nivssdfFile)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nivssdfFile | string | The path to the system definition file. |

Parent topic:

SystemDefinition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition-version.html language=enus -->
## TOPIC 03816: Version

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition-version.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition-version.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the version number of the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Version Version { get; }ReturnsThe file version.

### Version

Gets the version number of the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Version Version { get; }

#### Returns

The file version.

Parent topic:

SystemDefinition Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinition.html language=enus -->
## TOPIC 03817: SystemDefinition Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinition.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinition.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a system definition file, which contains configuration settings for the VeriStand Engine. This class is the base class for configuring system definitions through this API. Derives fromobjectSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SystemDefinition : o

### SystemDefinition Class

Represents a system definition file, which contains configuration settings for the VeriStand Engine. This class is the base class for configuring system definitions through this API.

#### Derives from

- object

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SystemDefinition : object

#### Remarks

Use the members of this class to create and save the system definition file, and to get its version information and [Root](nationalinstruments-veristand-systemdefinitionapi-root.html) node.

**Accessing this Class**

- SystemDefinition Constructor

For example code and more information about this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| SystemDefinition(string, string, string, string, string, string, string) | Initializes a new instance of SystemDefinition with the specified configuration. |
| SystemDefinition(string) | Initializes a new instance of SystemDefinition with the specified file path. |

#### Properties

| Name | Description |
| --- | --- |
| DocumentType | The DocumentType for this SystemDefinition. |
| Root | Gets the Root node of the system definition file. |
| Version | Gets the version number of the system definition file. |

#### Methods

| Name | Description |
| --- | --- |
| SaveSystemDefinitionFile(string, out string) | Saves the system definition file to the specified location. |
| SaveSystemDefinitionFile(out string) | Saves the system definition file. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_basenodetype..html language=enus -->
## TOPIC 03818: GetDescendantChannels(this BaseNodeType, Predicate< BaseNodeType >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_basenodetype..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_basenodetype..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< BaseNodeType > GetDescendantChannels(this BaseNodeType baseNodeType, Predicate< BaseNodeType > inclusionFilter)

### GetDescendantChannels(this BaseNodeType, Predicate< BaseNodeType >)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< BaseNodeType > GetDescendantChannels(this BaseNodeType baseNodeType, Predicate< BaseNodeType > inclusionFilter)

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_basenodetype_-predicate_basenodetype..html language=enus -->
## TOPIC 03819: GetDescendantChannels(this BaseNodeType, Predicate< BaseNodeType >, Predicate< BaseNodeType >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_basenodetype_-predicate_basenodetype..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_basenodetype_-predicate_basenodetype..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get all channels a BaseNodeType has beneath it (or just itself, if it is a channel). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< BaseNodeType > GetDescendantChannels(this BaseNodeType baseNodeType, Predicate< BaseNodeType > inclusionFilter, Predicate<

### GetDescendantChannels(this BaseNodeType, Predicate< BaseNodeType >, Predicate< BaseNodeType >)

Get all channels a BaseNodeType has beneath it (or just itself, if it is a channel).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< BaseNodeType > GetDescendantChannels(this BaseNodeType baseNodeType, Predicate< BaseNodeType > inclusionFilter, Predicate< BaseNodeType > recursePredicate)

#### Remarks

This is much higher performance than the BaseNode version if you can avoid converting all outputs back to BaseNode

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNodeType | this BaseNodeType | The baseNodeType we are searching for child channels |
| inclusionFilter | Predicate< BaseNodeType > | function to specify whether we should include a particular channel. Pass null to include all |
| recursePredicate | Predicate< BaseNodeType > | Whether we should recurse below a given node. |

#### Returns

Enumeration of child channels

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel..1.html language=enus -->
## TOPIC 03820: GetDescendantChannels(this IEnumerable< BaseNode >, Predicate< IChannel >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel..1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel..1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get all channels a list of BaseNodes have beneath it (or just itself, if it is a channel) SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< BaseNode > GetDescendantChannels(this IEnumerable< BaseNode > baseNodes, Predicate< IChannel > inclusionFilter)Parame

### GetDescendantChannels(this IEnumerable< BaseNode >, Predicate< IChannel >)

Get all channels a list of BaseNodes have beneath it (or just itself, if it is a channel)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) > GetDescendantChannels(this IEnumerable< BaseNode > baseNodes, Predicate< IChannel > inclusionFilter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNodes | this IEnumerable< BaseNode > | The baseNodes we are searching for child channels |
| inclusionFilter | Predicate< IChannel > | function to specify whether we should include a particular channel. Pass null to include all |

#### Returns

Deep enumeration of channels

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel..html language=enus -->
## TOPIC 03821: GetDescendantChannels(this BaseNode, Predicate< IChannel >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< BaseNode > GetDescendantChannels(this BaseNode baseNode, Predicate< IChannel > inclusionFilter)

### GetDescendantChannels(this BaseNode, Predicate< IChannel >)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) > GetDescendantChannels(this BaseNode baseNode, Predicate< IChannel > inclusionFilter)

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel_-predicate_basenode..html language=enus -->
## TOPIC 03822: GetDescendantChannels(this BaseNode, Predicate< IChannel >, Predicate< BaseNode >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel_-predicate_basenode..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this-predicate_ichannel_-predicate_basenode..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get all channels a BaseNode has beneath it (or just itself, if it is a channel) SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< BaseNode > GetDescendantChannels(this BaseNode baseNode, Predicate< IChannel > inclusionFilter, Predicate< BaseNode > recursePr

### GetDescendantChannels(this BaseNode, Predicate< IChannel >, Predicate< BaseNode >)

Get all channels a BaseNode has beneath it (or just itself, if it is a channel)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) > GetDescendantChannels(this BaseNode baseNode, Predicate< IChannel > inclusionFilter, Predicate< BaseNode > recursePredicate)

#### Remarks

For higher performance, use the BaseNodeType version

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNode | this BaseNode | The baseNode we are searching for child channels |
| inclusionFilter | Predicate< IChannel > | function to specify whether we should include a particular channel. Pass null to include all |
| recursePredicate | Predicate< BaseNode > | Whether we should recurse below a given node. |

#### Returns

Enumeration of child channels

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this.html language=enus -->
## TOPIC 03823: GetDescendantChannels(this BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getdescendantchannels__this.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Get all channels a BaseNode has beneath it (or just itself, if it is a channel) SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< BaseNode > GetDescendantChannels(this BaseNode baseNode)ParametersNameTypeDescriptionbaseNodethis BaseNodeThe baseNode we are s

### GetDescendantChannels(this BaseNode)

Get all channels a BaseNode has beneath it (or just itself, if it is a channel)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) > GetDescendantChannels(this BaseNode baseNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNode | this BaseNode | The baseNode we are searching for child channels |

#### Returns

Enumeration of child channels

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getfirstancestoroftype_t___this.html language=enus -->
## TOPIC 03824: GetFirstAncestorOfType< T >(this BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getfirstancestoroftype_t___this.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getfirstancestoroftype_t___this.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Wrapper for GetParent that is easier to use with LINQ. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static T GetFirstAncestorOfType< T >(this BaseNode baseNode)ParametersNameTypeDescriptionbaseNodethis BaseNodeBaseNode to get parent ofReturnsParent BaseNode, or null if we

### GetFirstAncestorOfType< T >(this BaseNode)

Wrapper for GetParent that is easier to use with LINQ.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static [T](nationalinstruments-veristand-systemdefinitionapi-thermocoupletype.html) GetFirstAncestorOfType< T >(this BaseNode baseNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNode | this BaseNode | BaseNode to get parent of |

#### Returns

Parent BaseNode, or null if we don't have one.

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getparent__this.1.html language=enus -->
## TOPIC 03825: GetParent(this BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getparent__this.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getparent__this.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Wrapper for GetParent that is easier to use with LINQ. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static BaseNode GetParent(this BaseNode baseNode)ParametersNameTypeDescriptionbaseNodethis BaseNodeBaseNode to get parent ofReturnsParent BaseNode, or null if we don't have

### GetParent(this BaseNode)

Wrapper for GetParent that is easier to use with LINQ.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) GetParent(this BaseNode baseNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNode | this BaseNode | BaseNode to get parent of |

#### Returns

Parent BaseNode, or null if we don't have one.

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getparent__this.html language=enus -->
## TOPIC 03826: GetParent(this BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getparent__this.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-getparent__this.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Wrapper for GetParent that is easier to use with LINQ. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static BaseNodeType GetParent(this BaseNodeType baseNodeType)ParametersNameTypeDescriptionbaseNodeTypethis BaseNodeTypeBaseNodeType to get parent ofReturnsParent BaseNodeTy

### GetParent(this BaseNodeType)

Wrapper for GetParent that is easier to use with LINQ.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static BaseNodeType GetParent(this BaseNodeType baseNodeType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNodeType | this BaseNodeType | BaseNodeType to get parent of |

#### Returns

Parent BaseNodeType, or null if we don't have one.

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isdeprecated__this.1.html language=enus -->
## TOPIC 03827: IsDeprecated(this BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isdeprecated__this.1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isdeprecated__this.1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Check if a node is deprecated. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool IsDeprecated(this BaseNode node)ParametersNameTypeDescriptionnodethis BaseNodeBaseNode to checkReturnsTrue if the node is deprecated

### IsDeprecated(this BaseNode)

Check if a node is deprecated.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool IsDeprecated(this BaseNode node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | this BaseNode | BaseNode to check |

#### Returns

True if the node is deprecated

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isdeprecated__this.html language=enus -->
## TOPIC 03828: IsDeprecated(this BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isdeprecated__this.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isdeprecated__this.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Check if a node is deprecated. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool IsDeprecated(this BaseNodeType baseNodeType)ParametersNameTypeDescriptionbaseNodeTypethis BaseNodeTypeBaseNodeType to checkReturnsTrue if the node is deprecated

### IsDeprecated(this BaseNodeType)

Check if a node is deprecated.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool IsDeprecated(this BaseNodeType baseNodeType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNodeType | this BaseNodeType | BaseNodeType to check |

#### Returns

True if the node is deprecated

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isselforancestorof__this-basenode.html language=enus -->
## TOPIC 03829: IsSelfOrAncestorOf(this BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isselforancestorof__this-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isselforancestorof__this-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Check if baseNode is an ancestor of potential child. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool IsSelfOrAncestorOf(this BaseNode baseNode, BaseNode potentialChild)ParametersNameTypeDescriptionbaseNodethis BaseNodeexpected ancestorpotentialChildBaseNodepotent

### IsSelfOrAncestorOf(this BaseNode, BaseNode)

Check if baseNode is an ancestor of potential child.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool IsSelfOrAncestorOf(this BaseNode baseNode, BaseNode potentialChild)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNode | this BaseNode | expected ancestor |
| potentialChild | BaseNode | potential child |

#### Returns

true if baseNode is potentialChild or an ancestor of it

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isselforancestorof__this-basenodetype.html language=enus -->
## TOPIC 03830: IsSelfOrAncestorOf(this BaseNodeType, BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isselforancestorof__this-basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions-isselforancestorof__this-basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Check if baseNodeType is an ancestor of potential child. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool IsSelfOrAncestorOf(this BaseNodeType baseNodeType, BaseNodeType potentialChild)ParametersNameTypeDescriptionbaseNodeTypethis BaseNodeTypeexpected ancestorpote

### IsSelfOrAncestorOf(this BaseNodeType, BaseNodeType)

Check if baseNodeType is an ancestor of potential child.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool IsSelfOrAncestorOf(this BaseNodeType baseNodeType, BaseNodeType potentialChild)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNodeType | this BaseNodeType | expected ancestor |
| potentialChild | BaseNodeType | potential child |

#### Returns

true if baseNodeType is potentialChild or an ancestor of it

Parent topic:

SystemDefinitionExtensions Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions.html language=enus -->
## TOPIC 03831: SystemDefinitionExtensions Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemdefinitionextensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Extension methods to assist with manipulating the SystemDefinition. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SystemDefinitionExtensionsMethodsNameDescriptionGetDescendantChannels(this IEnumerable< BaseNode >, Predicate< IChannel >)Get all channel

### SystemDefinitionExtensions Class

Extension methods to assist with manipulating the SystemDefinition.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SystemDefinitionExtensions

#### Methods

| Name | Description |
| --- | --- |
| GetDescendantChannels(this IEnumerable< BaseNode >, Predicate< IChannel >) | Get all channels a list of BaseNodes have beneath it (or just itself, if it is a channel) |
| GetDescendantChannels(this BaseNode, Predicate< IChannel >, Predicate< BaseNode >) | Get all channels a BaseNode has beneath it (or just itself, if it is a channel) |
| GetDescendantChannels(this BaseNode, Predicate< IChannel >) |  |
| GetDescendantChannels(this BaseNodeType, Predicate< BaseNodeType >, Predicate< BaseNodeType >) | Get all channels a BaseNodeType has beneath it (or just itself, if it is a channel). |
| GetDescendantChannels(this BaseNodeType, Predicate< BaseNodeType >) |  |
| GetDescendantChannels(this BaseNode) | Get all channels a BaseNode has beneath it (or just itself, if it is a channel) |
| GetFirstAncestorOfType< T >(this BaseNode) | Wrapper for GetParent that is easier to use with LINQ. |
| GetParent(this BaseNode) | Wrapper for GetParent that is easier to use with LINQ. |
| GetParent(this BaseNodeType) | Wrapper for GetParent that is easier to use with LINQ. |
| IsDeprecated(this BaseNode) | Check if a node is deprecated. |
| IsDeprecated(this BaseNodeType) | Check if a node is deprecated. |
| IsSelfOrAncestorOf(this BaseNodeType, BaseNodeType) | Check if baseNodeType is an ancestor of potential child. |
| IsSelfOrAncestorOf(this BaseNode, BaseNode) | Check if baseNode is an ancestor of potential child. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systeminitialization-autostart.html language=enus -->
## TOPIC 03832: AutoStart

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systeminitialization-autostart.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systeminitialization-autostart.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AutoStart { get; set; }Returnstrue if the system runs the system definition fil

### AutoStart

Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AutoStart { get; set; }

#### Returns

true if the system runs the system definition file automatically. false if a user must redeploy.

Parent topic:

SystemInitialization Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systeminitialization.html language=enus -->
## TOPIC 03833: SystemInitialization Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systeminitialization.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systeminitialization.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the System Initialization section of the system definition, which contains information about the order that multiple targets deploy relative to each other. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class SystemInitialization : SectionRemar

### SystemInitialization Class

Represents the **System Initialization** section of the system definition, which contains information about the order that multiple targets deploy relative to each other.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SystemInitialization : Section

#### Remarks

Use the members of this class to get or set whether the system definition automatically runs after a target reboots.

**Accessing this Class**

- [GetSystemInitialization](nationalinstruments-veristand-systemdefinitionapi-root-getsysteminitialization.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| AutoStart | Gets or sets whether the system runs the system definition file automatically after a target reboots or waits for a user to redeploy the file. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-systemmappings.html language=enus -->
## TOPIC 03834: SystemMappings Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-systemmappings.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-systemmappings.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the System Mappings section of the system definition, which stores information about how source channels within the system definition map to destination channels. Destination channels store the mapping information. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDe

### SystemMappings Class

Represents the **System Mappings** section of the system definition, which stores information about how source channels within the system definition map to destination channels. Destination channels store the mapping information.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class SystemMappings : Section

#### Remarks

**Accessing this Class**

- [GetSystemMappings](nationalinstruments-veristand-systemdefinitionapi-root-getsystemmappings.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html language=enus -->
## TOPIC 03835: ControlLoopTimingSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the timing source for the Primary Control Loop. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TargetControlLoopTimingSource ControlLoopTimingSource { get; }ReturnsAn enumeration value of TargetControlLoopTimingSource.

### ControlLoopTimingSource

Gets the timing source for the Primary Control Loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TargetControlLoopTimingSource](nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html) ControlLoopTimingSource { get; }

#### Returns

An enumeration value of [TargetControlLoopTimingSource](nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html).

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-customtimingdevice.html language=enus -->
## TOPIC 03836: CustomTimingDevice

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-customtimingdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-customtimingdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the custom device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if ControlLoopTimingSource is CustomDeviceTiming. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CustomDevice CustomTimingDevice { get; set; }Retu

### CustomTimingDevice

Gets or sets the custom device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if [ControlLoopTimingSource](nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html) is [CustomDeviceTiming](nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) CustomTimingDevice { get; set; }

#### Returns

The [CustomDevice](nationalinstruments-veristand-systemdefinitionapi-customdevice.html) that is the PCL timing source.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-daqdigitallinesdecimation.html language=enus -->
## TOPIC 03837: DAQDigitalLinesDecimation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-daqdigitallinesdecimation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-daqdigitallinesdecimation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher

### DAQDigitalLinesDecimation

Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint DAQDigitalLinesDecimation { get; set; }

#### Returns

The decimation applied to PCL execution.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-daqdigitallinesrate.html language=enus -->
## TOPIC 03838: DAQDigitalLinesRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-daqdigitallinesrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-daqdigitallinesrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionA

### DAQDigitalLinesRate

Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double DAQDigitalLinesRate { get; set; }

#### Returns

The frequency (in Hz) at which the PCL reads and writes DAQ digital line values.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-daqtimeout.html language=enus -->
## TOPIC 03839: DAQTimeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-daqtimeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-daqtimeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the amount of time to wait for a DAQ device to transfer data before timing out. This property is only valid of the ControlLoopTimingSource is DAQTiming. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint DAQTimeout { get; }ReturnsThe DAQ timeout, in microseconds.

### DAQTimeout

Gets the amount of time to wait for a DAQ device to transfer data before timing out. This property is only valid of the [ControlLoopTimingSource](nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html) is [DAQTiming](nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint DAQTimeout { get; }

#### Returns

The DAQ timeout, in microseconds.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-daqtimingdevice.html language=enus -->
## TOPIC 03840: DAQTimingDevice

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-daqtimingdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-daqtimingdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the DAQ device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if ControlLoopTimingSource is DAQTiming. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DAQDevice DAQTimingDevice { get; set; }ReturnsThe DAQDevice t

### DAQTimingDevice

Gets or sets the DAQ device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if [ControlLoopTimingSource](nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html) is [DAQTiming](nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) DAQTimingDevice { get; set; }

#### Returns

The [DAQDevice](nationalinstruments-veristand-systemdefinitionapi-daqdevice.html) that is the PCL timing source.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-dataprocessingloopdecimation.html language=enus -->
## TOPIC 03841: DataProcessingLoopDecimation

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-dataprocessingloopdecimation.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-dataprocessingloopdecimation.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution. SyntaxNamespace: NationalI

### DataProcessingLoopDecimation

Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int DataProcessingLoopDecimation { get; set; }

#### Returns

The execution rate of the DPL.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-dataprocessingloopprocessor.html language=enus -->
## TOPIC 03842: DataProcessingLoopProcessor

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-dataprocessingloopprocessor.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-dataprocessingloopprocessor.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int DataProcessingLoopProcessor {

### DataProcessingLoopProcessor

Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int DataProcessingLoopProcessor { get; set; }

#### Returns

The processor on which the Data Processing Loop executes.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-datarate.html language=enus -->
## TOPIC 03843: DataRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-datarate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-datarate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the rate for updating channel values in the Send Communication Loop. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double DataRate { get; set; }ReturnsThe channel value update rate.

### DataRate

Gets or sets the rate for updating channel values in the Send Communication Loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double DataRate { get; set; }

#### Returns

The channel value update rate.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-deploymentgroup.html language=enus -->
## TOPIC 03844: DeploymentGroup

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-deploymentgroup.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-deploymentgroup.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the deployment group to which a target belongs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int DeploymentGroup { get; set; }ReturnsThe deployment group.

### DeploymentGroup

Gets or sets the deployment group to which a target belongs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int DeploymentGroup { get; set; }

#### Returns

The deployment group.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-disabletarget.html language=enus -->
## TOPIC 03845: DisableTarget

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-disabletarget.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-disabletarget.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the Boolean flag indicating whether a target is disabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool DisableTarget { get; set; }Returnstrue if the target is disabled.

### DisableTarget

Gets or sets the Boolean flag indicating whether a target is disabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool DisableTarget { get; set; }

#### Returns

true if the target is disabled.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-executionmode.html language=enus -->
## TOPIC 03846: ExecutionMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-executionmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-executionmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TargetExecutionMode ExecutionMode { get; set; }ReturnsAn enumeration value of TargetExecutionMode.

### ExecutionMode

Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TargetExecutionMode](nationalinstruments-veristand-systemdefinitionapi-targetexecutionmode.html) ExecutionMode { get; set; }

#### Returns

An enumeration value of [TargetExecutionMode](nationalinstruments-veristand-systemdefinitionapi-targetexecutionmode.html).

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-filterdaqerrors.html language=enus -->
## TOPIC 03847: FilterDAQErrors

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-filterdaqerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-filterdaqerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to true if you do not want the system to shut down when an NI-DAQ device reports an error. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool FilterDAQErrors { get; set; }Returnstrue if D

### FilterDAQErrors

Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to true if you do not want the system to shut down when an NI-DAQ device reports an error.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool FilterDAQErrors { get; set; }

#### Returns

true if DAQ errors are filtered.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-filterwatchdogerrors.html language=enus -->
## TOPIC 03848: FilterWatchdogErrors

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-filterwatchdogerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-filterwatchdogerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Co

### FilterWatchdogErrors

Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to true if you want NI VeriStand to ignore these errors.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool FilterWatchdogErrors { get; set; }

#### Returns

true if watchdog errors are filtered.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-fpgascaninterfacemode.html language=enus -->
## TOPIC 03849: FPGAScanInterfaceMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-fpgascaninterfacemode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-fpgascaninterfacemode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. (Windows) This setting has no effect on Windows targets. SyntaxNam

### FPGAScanInterfaceMode

Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. **(Windows)** This setting has no effect on Windows targets.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ushort FPGAScanInterfaceMode { get; set; }

#### Remarks

| Value | Mode |
| --- | --- |
| 0 | Use current — Uses the currently configured NI Scan Engine interface mode. NI VeriStand does not override any settings. |
| 1 | FPGA Mode — Sets the NI Scan Engine to LabVIEW FPGA Interface mode. |
| 2 | Scan Interface Mode — Sets the NI Scan Engine to Scan Interface mode.Note Most NI C series hardware supports this mode, but a few backplanes, controllers, and modules do not. Refer to your hardware documentation to confirm Scan Interface Mode support. |

#### Returns

The interface mode of the target. Valid values include:

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getalarms.html language=enus -->
## TOPIC 03850: GetAlarms()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getalarms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getalarms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Alarms section under the target, which contains any alarms you configure to notify the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a procedure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinit

### GetAlarms()

Gets the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section under the target, which contains any alarms you configure to notify the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a procedure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) GetAlarms()

#### Returns

An [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getcalculatedchannels.html language=enus -->
## TOPIC 03851: GetCalculatedChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getcalculatedchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getcalculatedchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CalculatedChannels section under the target, which contains any calculated channels you configure. These channels produce new values based on calculations performed on other channels in the system. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannels G

### GetCalculatedChannels()

Gets the [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) section under the target, which contains any calculated channels you configure. These channels produce new values based on calculations performed on other channels in the system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) GetCalculatedChannels()

#### Returns

A [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getcustomdevices.html language=enus -->
## TOPIC 03852: GetCustomDevices()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getcustomdevices.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getcustomdevices.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CustomDevices section under the target, which contains any custom devices you configure. Custom devices enable you to customize and extend the functionality of NI VeriStand by packaging LabVIEW code, or any code you can call from LabVIEW, into a device that you can add to an NI VeriStand sy

### GetCustomDevices()

Gets the [CustomDevices](nationalinstruments-veristand-systemdefinitionapi-customdevices.html) section under the target, which contains any custom devices you configure. Custom devices enable you to customize and extend the functionality of NI VeriStand by packaging LabVIEW code, or any code you can call from LabVIEW, into a device that you can add to an NI VeriStand system definition file and deploy to a target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CustomDevices](nationalinstruments-veristand-systemdefinitionapi-customdevices.html) GetCustomDevices()

#### Returns

A [CustomDevices](nationalinstruments-veristand-systemdefinitionapi-customdevices.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-gethardware.html language=enus -->
## TOPIC 03853: GetHardware()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-gethardware.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-gethardware.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Hardware section under the target, which contains all the Chassis you configure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Hardware GetHardware()RemarksFor example code and more information about this method, refer to one of the following help topics: LabVIEW

### GetHardware()

Gets the [Hardware](nationalinstruments-veristand-systemdefinitionapi-hardware.html) section under the target, which contains all the [Chassis](nationalinstruments-veristand-systemdefinitionapi-chassis.html) you configure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Hardware](nationalinstruments-veristand-systemdefinitionapi-hardware.html) GetHardware()

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

A [Hardware](nationalinstruments-veristand-systemdefinitionapi-hardware.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getprocedures.html language=enus -->
## TOPIC 03854: GetProcedures()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getprocedures.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getprocedures.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Procedures section under the target, which contains any procedures you add. Procedures specify sets of actions that the VeriStand Engine executes in response to an event, such as an alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Procedures GetProcedures()Ret

### GetProcedures()

Gets the [Procedures](nationalinstruments-veristand-systemdefinitionapi-procedures.html) section under the target, which contains any procedures you add. Procedures specify sets of actions that the VeriStand Engine executes in response to an event, such as an alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Procedures](nationalinstruments-veristand-systemdefinitionapi-procedures.html) GetProcedures()

#### Returns

A [Procedures](nationalinstruments-veristand-systemdefinitionapi-procedures.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getsimulationmodels.html language=enus -->
## TOPIC 03855: GetSimulationModels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getsimulationmodels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getsimulationmodels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SimulationModels section under the target, which contains any models you import into the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SimulationModels GetSimulationModels()ReturnsA SimulationModels object.

### GetSimulationModels()

Gets the [SimulationModels](nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html) section under the target, which contains any models you import into the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SimulationModels](nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html) GetSimulationModels()

#### Returns

A [SimulationModels](nationalinstruments-veristand-systemdefinitionapi-simulationmodels.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getstimulus.html language=enus -->
## TOPIC 03856: GetStimulus()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getstimulus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getstimulus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Stimulus section, which contains the stimulus generators available in the Legacy Stimulus Profile Editor. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Stimulus GetStimulus()RemarksThis method is obsolete in NI VeriStand 2011 and later and does not interact with t

### GetStimulus()

Gets the [Stimulus](nationalinstruments-veristand-systemdefinitionapi-stimulus.html) section, which contains the stimulus generators available in the Legacy Stimulus Profile Editor.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Stimulus](nationalinstruments-veristand-systemdefinitionapi-stimulus.html) GetStimulus()

#### Remarks

Note

This method is obsolete in NI VeriStand 2011 and later and does not interact with the latest version of the Stimulus Profile Editor. Use the Stimulus Profile API, in NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi.dll to interact with the current Stimulus Profile Editor.

#### Returns

A [Stimulus](nationalinstruments-veristand-systemdefinitionapi-stimulus.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getsystemchannels.html language=enus -->
## TOPIC 03857: GetSystemChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getsystemchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getsystemchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the SystemChannels section under the target, which contains a variety of channels that monitor the state and condition of various aspects of the system. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SystemChannels GetSystemChannels()ReturnsA SystemChannels object.

### GetSystemChannels()

Gets the [SystemChannels](nationalinstruments-veristand-systemdefinitionapi-systemchannels.html) section under the target, which contains a variety of channels that monitor the state and condition of various aspects of the system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SystemChannels](nationalinstruments-veristand-systemdefinitionapi-systemchannels.html) GetSystemChannels()

#### Returns

A [SystemChannels](nationalinstruments-veristand-systemdefinitionapi-systemchannels.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getuserchannels.html language=enus -->
## TOPIC 03858: GetUserChannels()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getuserchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getuserchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the UserChannels section under the target, which contains and user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannels GetUserChannels(

### GetUserChannels()

Gets the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section under the target, which contains and user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) GetUserChannels()

#### Returns

A [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-getxnetdatabases.html language=enus -->
## TOPIC 03859: GetXNETDatabases()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-getxnetdatabases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-getxnetdatabases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the XNETDatabases section of the target, which contains any XNET Databases you add to the system definition to run XNET devices. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic XNETDatabases GetXNETDatabases()ReturnsAn XNETDatabases object.

### GetXNETDatabases()

Gets the [XNETDatabases](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html) section of the target, which contains any XNET Databases you add to the system definition to run [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) devices.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [XNETDatabases](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html) GetXNETDatabases()

#### Returns

An [XNETDatabases](nationalinstruments-veristand-systemdefinitionapi-xnetdatabases.html) object.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-ipaddress.html language=enus -->
## TOPIC 03860: IPAddress

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-ipaddress.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-ipaddress.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the IP address of the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string IPAddress { get; set; }ReturnsThe IP address.

### IPAddress

Gets or sets the IP address of the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string IPAddress { get; set; }

#### Returns

The IP address.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-maximumstreamedchannels.html language=enus -->
## TOPIC 03861: MaximumStreamedChannels

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-maximumstreamedchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-maximumstreamedchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int MaximumStreamedChannels { get; set; }ReturnsThe maximum number of streamed channels.

### MaximumStreamedChannels

Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int MaximumStreamedChannels { get; set; }

#### Returns

The maximum number of streamed channels.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-operatingsystem.html language=enus -->
## TOPIC 03862: OperatingSystem

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-operatingsystem.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-operatingsystem.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the operating system of the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string OperatingSystem { get; set; }ReturnsThe operating system. Valid values are PharLap, VxWorks, or Windows.

### OperatingSystem

Gets or sets the operating system of the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string OperatingSystem { get; set; }

#### Returns

The operating system. Valid values are PharLap, VxWorks, or Windows.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-password.html language=enus -->
## TOPIC 03863: Password

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-password.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-password.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the password for the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Password { get; set; }

### Password

Gets or sets the password for the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Password { get; set; }

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-passwordpropertystring.html language=enus -->
## TOPIC 03864: PasswordPropertyString

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-passwordpropertystring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-passwordpropertystring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Name of the property holding the password. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const string PasswordPropertyString

### PasswordPropertyString

Name of the property holding the password.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const string PasswordPropertyString

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-primarycontrolloopprocessor.html language=enus -->
## TOPIC 03865: PrimaryControlLoopProcessor

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-primarycontrolloopprocessor.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-primarycontrolloopprocessor.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processor on which to execute the Primary Control Loop (PCL). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int PrimaryControlLoopProcessor { get; set; }RemarksIf you specify an invalid processor, the PCL executes on the first available processor. ReturnsT

### PrimaryControlLoopProcessor

Gets or sets the processor on which to execute the Primary Control Loop (PCL).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int PrimaryControlLoopProcessor { get; set; }

#### Remarks

If you specify an invalid processor, the PCL executes on the first available processor.

#### Returns

The processor on which the PCL executes. -2 specifies any available processor.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetoautomatic.html language=enus -->
## TOPIC 03866: SetControlLoopTimingSourceToAutomatic()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetoautomatic.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetoautomatic.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Primary Control Loop timing source to automatic. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetControlLoopTimingSourceToAutomatic()Returnstrue if the timing source was set successfully.

### SetControlLoopTimingSourceToAutomatic()

Sets the Primary Control Loop timing source to automatic.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetControlLoopTimingSourceToAutomatic()

#### Returns

true if the timing source was set successfully.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetoautomatic__out.html language=enus -->
## TOPIC 03867: SetControlLoopTimingSourceToAutomatic(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetoautomatic__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetoautomatic__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Primary Control Loop timing source to automatic. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetControlLoopTimingSourceToAutomatic(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error

### SetControlLoopTimingSourceToAutomatic(out Error)

Sets the Primary Control Loop timing source to automatic.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetControlLoopTimingSourceToAutomatic(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the timing source was set successfully.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetocustomdevice__string-out.html language=enus -->
## TOPIC 03868: SetControlLoopTimingSourceToCustomDevice(string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetocustomdevice__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetocustomdevice__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Primary Control Loop timing source to the specified custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetControlLoopTimingSourceToCustomDevice(string CustomDeviceName, out Error error)ParametersNameTypeDescriptionCustomDeviceNamestringThe name of t

### SetControlLoopTimingSourceToCustomDevice(string, out Error)

Sets the Primary Control Loop timing source to the specified custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetControlLoopTimingSourceToCustomDevice(string CustomDeviceName, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| CustomDeviceName | string | The name of the custom device to set as the timing source. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the timing source was set successfully. false if the custom device is an invalid timing source.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetocustomdevice__string.html language=enus -->
## TOPIC 03869: SetControlLoopTimingSourceToCustomDevice(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetocustomdevice__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetocustomdevice__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Primary Control Loop timing source to the specified custom device. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetControlLoopTimingSourceToCustomDevice(string CustomDeviceName)ParametersNameTypeDescriptionCustomDeviceNamestringThe name of the custom device

### SetControlLoopTimingSourceToCustomDevice(string)

Sets the Primary Control Loop timing source to the specified custom device.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetControlLoopTimingSourceToCustomDevice(string CustomDeviceName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| CustomDeviceName | string | The name of the custom device to set as the timing source. |

#### Returns

true if the timing source was set successfully. false if the custom device is an invalid timing source.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetodaq__string-uint-uint-out.html language=enus -->
## TOPIC 03870: SetControlLoopTimingSourceToDAQ(string, uint, uint, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetodaq__string-uint-uint-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetodaq__string-uint-uint-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Primary Control Loop timing source to the DAQ device with the specified name and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetControlLoopTimingSourceToDAQ(string DAQDeviceName, uint DAQTimeout, uint TimedLoopSleepTime, out Error error)Param

### SetControlLoopTimingSourceToDAQ(string, uint, uint, out Error)

Sets the Primary Control Loop timing source to the DAQ device with the specified name and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetControlLoopTimingSourceToDAQ(string DAQDeviceName, uint DAQTimeout, uint TimedLoopSleepTime, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| DAQDeviceName | string | The name of the DAQ device to set as the timing source. |
| DAQTimeout | uint | The amount of time in milliseconds to wait for the DAQ device to transfer data before timing out. |
| TimedLoopSleepTime | uint | The amount of time in microseconds the Primary Control Loop sleeps after each tick. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the timing source was set successfully. false if the DAQ device is an invalid timing source.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetodaq__string-uint-uint.html language=enus -->
## TOPIC 03871: SetControlLoopTimingSourceToDAQ(string, uint, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetodaq__string-uint-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-setcontrollooptimingsourcetodaq__string-uint-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Primary Control Loop timing source to the DAQ device with the specified name and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool SetControlLoopTimingSourceToDAQ(string DAQDeviceName, uint DAQTimeout, uint TimedLoopSleepTime)ParametersNameTypeDesc

### SetControlLoopTimingSourceToDAQ(string, uint, uint)

Sets the Primary Control Loop timing source to the DAQ device with the specified name and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool SetControlLoopTimingSourceToDAQ(string DAQDeviceName, uint DAQTimeout, uint TimedLoopSleepTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| DAQDeviceName | string | The name of the DAQ device to set as the timing source. |
| DAQTimeout | uint | The amount of time in milliseconds to wait for the DAQ device to transfer data before timing out. |
| TimedLoopSleepTime | uint | The amount of time in microseconds the Primary Control Loop sleeps after each tick. |

#### Returns

true if the timing source was set successfully. false if the DAQ device is an invalid timing source.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-target__string-string.html language=enus -->
## TOPIC 03872: Target(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-target__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-target__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Target with the specified name and target type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Target(string Name, string TargetType)ParametersNameTypeDescriptionNamestringThe name of the Target.TargetTypestringThe operating system of the targe

### Target(string, string)

Initializes a new instance of [Target](nationalinstruments-veristand-systemdefinitionapi-target.html) with the specified name and target type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Target(string Name, string TargetType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Target. |
| TargetType | string | The operating system of the target. Valid values are PharLap, VxWorks, or Windows. |

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-targetrate.html language=enus -->
## TOPIC 03873: TargetRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-targetrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-targetrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the execution rate of the target in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double TargetRate { get; set; }ReturnsThe target execution rate, in hertz.

### TargetRate

Gets or sets the execution rate of the target in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double TargetRate { get; set; }

#### Returns

The target execution rate, in hertz.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-targettimingmode.html language=enus -->
## TOPIC 03874: TargetTimingMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-targettimingmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-targettimingmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the timing mode for the target. When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TargetTimingMode TargetTimingMode { get; set; }

### TargetTimingMode

Gets or sets the timing mode for the target. When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TargetTimingMode](nationalinstruments-veristand-systemdefinitionapi-targettimingmode.html) TargetTimingMode { get; set; }

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-timedloopsleeptime.html language=enus -->
## TOPIC 03875: TimedLoopSleepTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-timedloopsleeptime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-timedloopsleeptime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the amount of time in microseconds the Primary Control Loop (PCL) sleeps after each tick. NI VeriStand ignores this value if the master timing device has an external timing source. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint TimedLoopSleepTime { get; }ReturnsTh

### TimedLoopSleepTime

Gets the amount of time in microseconds the Primary Control Loop (PCL) sleeps after each tick. NI VeriStand ignores this value if the master timing device has an external timing source.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint TimedLoopSleepTime { get; }

#### Returns

The amount of time the PCL sleeps after each tick, in microseconds.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-timeout.html language=enus -->
## TOPIC 03876: Timeout

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-timeout.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-timeout.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the ControlLoopTimingSource is DAQTiming. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Timeout { get; set; }ReturnsThe timeout, in seco

### Timeout

Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the [ControlLoopTimingSource](nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html) is [DAQTiming](nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Timeout { get; set; }

#### Returns

The timeout, in seconds.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-timingsourcedaqsettings.html language=enus -->
## TOPIC 03877: TimingSourceDAQSettings

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-timingsourcedaqsettings.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-timingsourcedaqsettings.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if ControlLoopTimingSource is DAQTiming. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TimingSourceSettingsOptions TimingSourceDAQSettings { get;

### TimingSourceDAQSettings

Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if [ControlLoopTimingSource](nationalinstruments-veristand-systemdefinitionapi-target-controllooptimingsource.html) is [DAQTiming](nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TimingSourceSettingsOptions](nationalinstruments-veristand-systemdefinitionapi-timingsourcesettingsoptions.html) TimingSourceDAQSettings { get; set; }

#### Returns

An enumeration value of [TimingSourceSettingsOptions](nationalinstruments-veristand-systemdefinitionapi-timingsourcesettingsoptions.html).

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-username.html language=enus -->
## TOPIC 03878: Username

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-username.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-username.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the username for the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Username { get; set; }

### Username

Gets or sets the username for the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Username { get; set; }

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-usernamepropertystring.html language=enus -->
## TOPIC 03879: UsernamePropertyString

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-usernamepropertystring.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-usernamepropertystring.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Name of the property holding the username. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const string UsernamePropertyString

### UsernamePropertyString

Name of the property holding the username.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const string UsernamePropertyString

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target-warmuptime_ms.html language=enus -->
## TOPIC 03880: WarmupTime_ms

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target-warmuptime_ms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target-warmuptime_ms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint WarmupTime_ms { get; set; }ReturnsThe warm-up time, in mi

### WarmupTime_ms

Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint WarmupTime_ms { get; set; }

#### Returns

The warm-up time, in microseconds.

Parent topic:

Target Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-target.html language=enus -->
## TOPIC 03881: Target Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a target in the system definition. Derives fromBaseNodeBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Target : BaseNode, BaseNodeRemarksUse the members of this class to specify configuration settings for the target, such as its name, operating syste

### Target Class

Represents a target in the system definition.

#### Derives from

- BaseNode
- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Target : BaseNode, BaseNode

#### Remarks

Use the members of this class to specify configuration settings for the target, such as its name, operating system, timing source, processor assignments, and so on.

**Accessing this Class**

- [GetTargetList](nationalinstruments-veristand-systemdefinitionapi-targets-gettargetlist.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Target(string, string) | Initializes a new instance of Target with the specified name and target type. |

#### Fields

| Name | Description |
| --- | --- |
| PasswordPropertyString | Name of the property holding the password. |
| UsernamePropertyString | Name of the property holding the username. |

#### Properties

| Name | Description |
| --- | --- |
| ControlLoopTimingSource | Gets the timing source for the Primary Control Loop. |
| CustomTimingDevice | Gets or sets the custom device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if ControlLoopTimingSource is CustomDeviceTiming. |
| DAQDigitalLinesDecimation | Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at a rate of 100Hz. If you set the PCL to execute at a rate faster than 100Hz, use this property to specify a higher decimation value and reduce the frequency with which the PCL reads and writes the digital line values. |
| DAQDigitalLinesRate | Gets or sets how frequently the Primary Control Loop (PCL) reads and writes DAQ digital line values. The DIO Loop, which receives and sends these values from and to the PCL, executes at this rate and cannot be faster than the PCL loop. |
| DAQTimeout | Gets the amount of time to wait for a DAQ device to transfer data before timing out. This property is only valid of the ControlLoopTimingSource is DAQTiming. |
| DAQTimingDevice | Gets or sets the DAQ device that serves as the timing source for the Primary Control Loop (PCL). This property is only valid if ControlLoopTimingSource is DAQTiming. |
| DataProcessingLoopDecimation | Gets or sets the execution rate of the Data Processing Loop (DPL). A value of 1 specifies that the DPL reads values on every iteration of the Primary Control Loop (PCL). You can specify a value higher than 1 to read PCL values less frequently and increase system execution. |
| DataProcessingLoopProcessor | Gets or sets the processor on which to execute the Data Processing Loop. -2 is any available processor. If you specify an invalid processor, the loop executes on the first available processor. |
| DataRate | Gets or sets the rate for updating channel values in the Send Communication Loop. |
| DeploymentGroup | Gets or sets the deployment group to which a target belongs. |
| DisableTarget | Gets or sets the Boolean flag indicating whether a target is disabled. |
| ExecutionMode | Gets or sets the execution mode (parallel or low latency) of the loops of the VeriStand Engine. |
| FilterDAQErrors | Gets or sets whether to filter errors from NI-DAQmx function calls. Set this property to true if you do not want the system to shut down when an NI-DAQ device reports an error. |
| FilterWatchdogErrors | Gets or sets whether to filter errors reported by the timing watchdog. For example, if you set the Primary Control Loop to execute at a high rate and your system contains large or complex models, the watchdog reports an error if the models cannot execute quickly enough to keep up with the Primary Control Loop. Set this property to true if you want NI VeriStand to ignore these errors. |
| FPGAScanInterfaceMode | Gets or sets the interface mode for the NI Scan Engine on RT targets. You can use this property to override the current settings of the NI Scan Engine, which can be useful for certain C Series modules, such as NI 986x series devices. (Windows) This setting has no effect on Windows targets. |
| IPAddress | Gets or sets the IP address of the target. |
| MaximumStreamedChannels | Gets or sets the maximum number of channels that the VeriStand Engine can stream to the host. |
| OperatingSystem | Gets or sets the operating system of the target. |
| Password | Gets or sets the password for the target. |
| PrimaryControlLoopProcessor | Gets or sets the processor on which to execute the Primary Control Loop (PCL). |
| TargetRate | Gets or sets the execution rate of the target in hertz. |
| TargetTimingMode | Gets or sets the timing mode for the target. When an FPGA serves as the Primary Control Loop timing source, the mode affects certain performance characteristics of the system. |
| TimedLoopSleepTime | Gets the amount of time in microseconds the Primary Control Loop (PCL) sleeps after each tick. NI VeriStand ignores this value if the master timing device has an external timing source. |
| Timeout | Gets or sets the amount of time to wait for a start trigger from the DAQ device before timing out. This property is only valid if the ControlLoopTimingSource is DAQTiming. |
| TimingSourceDAQSettings | Gets or sets the timing source setting for the DAQ device that is timing the Primary Control Loop. This property is only valid if ControlLoopTimingSource is DAQTiming. |
| Username | Gets or sets the username for the target. |
| WarmupTime_ms | Gets or sets the amount of time the system waits before considering late flags. You can set a warm-up time to give the system time to allocate and manage resources. |

#### Methods

| Name | Description |
| --- | --- |
| GetAlarms() | Gets the Alarms section under the target, which contains any alarms you configure to notify the user that the value of a particular channel has gone outside a specified range of values. Alarms also can trigger the execution of a procedure. |
| GetCalculatedChannels() | Gets the CalculatedChannels section under the target, which contains any calculated channels you configure. These channels produce new values based on calculations performed on other channels in the system. |
| GetCustomDevices() | Gets the CustomDevices section under the target, which contains any custom devices you configure. Custom devices enable you to customize and extend the functionality of NI VeriStand by packaging LabVIEW code, or any code you can call from LabVIEW, into a device that you can add to an NI VeriStand system definition file and deploy to a target. |
| GetHardware() | Gets the Hardware section under the target, which contains all the Chassis you configure. |
| GetProcedures() | Gets the Procedures section under the target, which contains any procedures you add. Procedures specify sets of actions that the VeriStand Engine executes in response to an event, such as an alarm. |
| GetSimulationModels() | Gets the SimulationModels section under the target, which contains any models you import into the system definition. |
| GetStimulus() | Gets the Stimulus section, which contains the stimulus generators available in the Legacy Stimulus Profile Editor. |
| GetSystemChannels() | Gets the SystemChannels section under the target, which contains a variety of channels that monitor the state and condition of various aspects of the system. |
| GetUserChannels() | Gets the UserChannels section under the target, which contains and user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on. |
| GetXNETDatabases() | Gets the XNETDatabases section of the target, which contains any XNET Databases you add to the system definition to run XNET devices. |
| SetControlLoopTimingSourceToAutomatic() | Sets the Primary Control Loop timing source to automatic. |
| SetControlLoopTimingSourceToAutomatic(out Error) | Sets the Primary Control Loop timing source to automatic. |
| SetControlLoopTimingSourceToCustomDevice(string) | Sets the Primary Control Loop timing source to the specified custom device. |
| SetControlLoopTimingSourceToCustomDevice(string, out Error) | Sets the Primary Control Loop timing source to the specified custom device. |
| SetControlLoopTimingSourceToDAQ(string, uint, uint) | Sets the Primary Control Loop timing source to the DAQ device with the specified name and configuration. |
| SetControlLoopTimingSourceToDAQ(string, uint, uint, out Error) | Sets the Primary Control Loop timing source to the DAQ device with the specified name and configuration. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html language=enus -->
## TOPIC 03882: TargetControlLoopTimingSource Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-targetcontrollooptimingsource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timing source for the system. The timing source times the system by sending ticks to the Primary Control Loop. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum TargetControlLoopTimingSourceMembersNameValueDescriptionAutomaticTiming0NI VeriStand determines t

### TargetControlLoopTimingSource Enumeration

Specifies the timing source for the system. The timing source times the system by sending ticks to the Primary Control Loop.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum TargetControlLoopTimingSource

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AutomaticTiming | 0 | NI VeriStand determines the timing source to use. |
| DAQTiming | 1 | NI VeriStand uses an NI-DAQ device in the system as the timing source. |
| CustomDeviceTiming | 2 | NI VeriStand uses the custom device you specify as the timing source. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-targetexecutionmode.html language=enus -->
## TOPIC 03883: TargetExecutionMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-targetexecutionmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-targetexecutionmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the execution mode for the loops of the VeriStand Engine. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum TargetExecutionModeMembersNameValueDescriptionParallel0Executes all the loops of the VeriStand Engine in parallel. In this mode, the system does not write

### TargetExecutionMode Enumeration

Specifies the execution mode for the loops of the VeriStand Engine.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum TargetExecutionMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Parallel | 0 | Executes all the loops of the VeriStand Engine in parallel. In this mode, the system does not write values to or execute the Model Execution Loop(s) on the first iteration of the system, but it does read values from the loop(s). This causes a one-cycle delay on executing your model, but increases the execution speed of the entire system. |
| LowLatency | 1 | Executes all the loops of the VeriStand Engine in parallel, but writes values to, executes, and reads values from the Model Execution Loop(s) at every iteration of the system, including the first. National Instruments recommends you select this mode only if you need to minimize your CPU usage because waiting for the Model Execution Loop(s) to read, execute, and write on each iteration can significantly slow the execution speed of the system. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-targets-addtarget__target-out.html language=enus -->
## TOPIC 03884: AddTarget(Target, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-targets-addtarget__target-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-targets-addtarget__target-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Target to the Targets section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddTarget(Target target, out Error error)ParametersNameTypeDescriptiontargetTargetThe target to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If

### AddTarget(Target, out Error)

Adds the specified [Target](nationalinstruments-veristand-systemdefinitionapi-target.html) to the [Targets](nationalinstruments-veristand-systemdefinitionapi-targets.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddTarget(Target target, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | Target | The target to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the target was added successfully.

Parent topic:

Targets Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-targets-addtarget__target.html language=enus -->
## TOPIC 03885: AddTarget(Target)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-targets-addtarget__target.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-targets-addtarget__target.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Target to the Targets section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddTarget(Target target)ParametersNameTypeDescriptiontargetTargetThe target to add.Returnstrue if the target was added successfully.

### AddTarget(Target)

Adds the specified [Target](nationalinstruments-veristand-systemdefinitionapi-target.html) to the [Targets](nationalinstruments-veristand-systemdefinitionapi-targets.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddTarget(Target target)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| target | Target | The target to add. |

#### Returns

true if the target was added successfully.

Parent topic:

Targets Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-targets-gettargetlist.html language=enus -->
## TOPIC 03886: GetTargetList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-targets-gettargetlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-targets-gettargetlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Target elements from the Targets section. This method gets a list of existing targets in the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Target[] GetTargetList()RemarksModifications you make to the contents of this list

### GetTargetList()

Gets an array that contains the [Target](nationalinstruments-veristand-systemdefinitionapi-target.html) elements from the [Targets](nationalinstruments-veristand-systemdefinitionapi-targets.html) section. This method gets a list of existing targets in the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Target](nationalinstruments-veristand-systemdefinitionapi-target.html)[] GetTargetList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

An array that contains the [Target](nationalinstruments-veristand-systemdefinitionapi-target.html) elements from the [Targets](nationalinstruments-veristand-systemdefinitionapi-targets.html) section.

Parent topic:

Targets Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-targets.html language=enus -->
## TOPIC 03887: Targets Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-targets.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-targets.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Targets section of the system definition, which contains all the targets you configure. Derives fromBaseNodeSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Targets : BaseNodeRemarksUse the members of this class to add a target or get a list of existing t

### Targets Class

Represents the **Targets** section of the system definition, which contains all the targets you configure.

#### Derives from

- BaseNode

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Targets : BaseNode

#### Remarks

Use the members of this class to add a target or get a list of existing targets.

**Accessing this Class**

- [GetTargets](nationalinstruments-veristand-systemdefinitionapi-root-gettargets.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddTarget(Target, out Error) | Adds the specified Target to the Targets section. |
| AddTarget(Target) | Adds the specified Target to the Targets section. |
| GetTargetList() | Gets an array that contains the Target elements from the Targets section. This method gets a list of existing targets in the system definition. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-targettimingmode.html language=enus -->
## TOPIC 03888: TargetTimingMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-targettimingmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-targettimingmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The timing mode of the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum TargetTimingModeMembersNameValueDescriptionAuto0NI VeriStand will attempt to determine the best option for the target. WaitOnInterrupt1NI VeriStand uses interrupts to synchronize with the RIO

### TargetTimingMode Enumeration

The timing mode of the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum TargetTimingMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Auto | 0 | NI VeriStand will attempt to determine the best option for the target. |
| WaitOnInterrupt | 1 | NI VeriStand uses interrupts to synchronize with the RIO master timing source. |
| WaitOnDmaRead | 2 | NI VeriStand uses the FPGA DMA to synchronize with the RIO master timing source. This offers maximum loop rates at the cost of CPU usage. This mode is not supported on single-core targets. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-tasktype.html language=enus -->
## TOPIC 03889: TaskType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-tasktype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-tasktype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This enumeration is used to select the Task Type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum TaskTypeMembersNameValueDescriptionAnalogInput0An Analog Input Task.

### TaskType Enumeration

This enumeration is used to select the Task Type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum TaskType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AnalogInput | 0 | An Analog Input Task. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-temperatureunit.html language=enus -->
## TOPIC 03890: TemperatureUnit Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-temperatureunit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-temperatureunit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the Temperature Unit of the thermocouple. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum TemperatureUnitMembersNameValueDescriptionCelsius0Unit is celsius. FahrenheitUnit is fahrenheit. KelvinUnit is kelvin. RankineUnit is Rankine.

### TemperatureUnit Enumeration

Defines the Temperature Unit of the thermocouple.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum TemperatureUnit

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Celsius | 0 | Unit is celsius. |
| Fahrenheit |  | Unit is fahrenheit. |
| Kelvin |  | Unit is kelvin. |
| Rankine |  | Unit is Rankine. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplecjctype.html language=enus -->
## TOPIC 03891: ThermocoupleCJCType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplecjctype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplecjctype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the CJC type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ThermocoupleCJCTypeMembersNameValueDescriptionICSensor0CJC type is IC Sensor. ThermistorCJC type is Thermistor. TemperatureCJC type is Temperature (deg C). NI9211CJC type is NI 9211 Calibrated. NI9213

### ThermocoupleCJCType Enumeration

Defines the CJC type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ThermocoupleCJCType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ICSensor | 0 | CJC type is IC Sensor. |
| Thermistor |  | CJC type is Thermistor. |
| Temperature |  | CJC type is Temperature (deg C). |
| NI9211 |  | CJC type is NI 9211 Calibrated. |
| NI9213 |  | CJC type is NI 9213 Calibrated. |
| NI9219 |  | CJC type is NI 9219 Calibrated. |
| NI9214 |  | CJC type is NI 9214 Calibrated. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-temperatureunit.html language=enus -->
## TOPIC 03892: TemperatureUnit

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-temperatureunit.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-temperatureunit.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TemperatureUnit TemperatureUnit { get; set; }ReturnsAn enumeration of TemperatureUnit.

### TemperatureUnit

Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TemperatureUnit](nationalinstruments-veristand-systemdefinitionapi-temperatureunit.html) TemperatureUnit { get; set; }

#### Returns

An enumeration of [TemperatureUnit](nationalinstruments-veristand-systemdefinitionapi-temperatureunit.html).

Parent topic:

ThermocoupleScale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplecjcsource.html language=enus -->
## TOPIC 03893: ThermocoupleCJCSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplecjcsource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplecjcsource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode ThermocoupleCJCSource { get; set; }ReturnsA BaseNode reference to the channel that serves as the source of col

### ThermocoupleCJCSource

Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) ThermocoupleCJCSource { get; set; }

#### Returns

A BaseNode reference to the channel that serves as the source of cold-junction compensation.

Parent topic:

ThermocoupleScale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplecjctype.html language=enus -->
## TOPIC 03894: ThermocoupleCJCType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplecjctype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplecjctype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of device the thermocouple uses to perform cold-junction compensation. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ThermocoupleCJCType ThermocoupleCJCType { get; set; }ReturnsAn enumeration of ThermocoupleCJCType.

### ThermocoupleCJCType

Gets or sets the type of device the thermocouple uses to perform cold-junction compensation.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ThermocoupleCJCType](nationalinstruments-veristand-systemdefinitionapi-thermocouplecjctype.html) ThermocoupleCJCType { get; set; }

#### Returns

An enumeration of [ThermocoupleCJCType](nationalinstruments-veristand-systemdefinitionapi-thermocouplecjctype.html).

Parent topic:

ThermocoupleScale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplescale__string-thermocoupletype-thermocouplecjctype-temperatureunit-basenode.html language=enus -->
## TOPIC 03895: ThermocoupleScale(string, ThermocoupleType, ThermocoupleCJCType, TemperatureUnit, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplescale__string-thermocoupletype-thermocouplecjctype-temperatureunit-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplescale__string-thermocoupletype-thermocouplecjctype-temperatureunit-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ThermocoupleScale class with the specified name and properties. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ThermocoupleScale(string name, ThermocoupleType thermocoupleType, ThermocoupleCJCType thermocoupleCJCType, TemperatureUnit temper

### ThermocoupleScale(string, ThermocoupleType, ThermocoupleCJCType, TemperatureUnit, BaseNode)

Initializes a new instance of the ThermocoupleScale class with the specified name and properties.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ThermocoupleScale(string name, ThermocoupleType thermocoupleType, ThermocoupleCJCType thermocoupleCJCType, TemperatureUnit temperatureUnit, BaseNode thermocoupleCJCSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the ThermocoupleScale instance. |
| thermocoupleType | ThermocoupleType | The type of thermocouple connected to the channel. |
| thermocoupleCJCType | ThermocoupleCJCType | The type of device the thermocouple uses to perform cold-junction compensation. |
| temperatureUnit | TemperatureUnit | The temperature unit. |
| thermocoupleCJCSource | BaseNode | The channel that serves as the source of cold-junction compensation. |

Parent topic:

ThermocoupleScale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplescale__string.html language=enus -->
## TOPIC 03896: ThermocoupleScale(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplescale__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocouplescale__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the ThermocoupleScale class with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ThermocoupleScale(string name)RemarksThis constructor sets scaleUnit to Celsius, thermocoupleType to B, thermocoupleCJCType to ICSensor, thermoc

### ThermocoupleScale(string)

Initializes a new instance of the ThermocoupleScale class with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ThermocoupleScale(string name)

#### Remarks

This constructor sets *scaleUnit* to Celsius, *thermocoupleType* to B, *thermocoupleCJCType* to ICSensor, *thermocoupleCJCSource* to null, and *temperatureUnit* to Celsius.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the ThermocoupleScale instance. |

Parent topic:

ThermocoupleScale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocoupletype.html language=enus -->
## TOPIC 03897: ThermocoupleType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplescale-thermocoupletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the type of thermocouple in use. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ThermocoupleType ThermocoupleType { get; set; }ReturnsAn enumeration of ThermocoupleType.

### ThermocoupleType

Gets or sets the type of thermocouple in use.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [ThermocoupleType](nationalinstruments-veristand-systemdefinitionapi-thermocoupletype.html) ThermocoupleType { get; set; }

#### Returns

An enumeration of [ThermocoupleType](nationalinstruments-veristand-systemdefinitionapi-thermocoupletype.html).

Parent topic:

ThermocoupleScale Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocouplescale.html language=enus -->
## TOPIC 03898: ThermocoupleScale Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocouplescale.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocouplescale.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a thermocouple Scale, which converts raw values from a thermocouple to Kelvins or degrees Celsius, Fahrenheit, or Rankine. Derives fromScaleSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class ThermocoupleScale : ScaleConstructorsNameDescriptionThermocoupleScale(

### ThermocoupleScale Class

Represents a thermocouple [Scale](nationalinstruments-veristand-systemdefinitionapi-scale.html), which converts raw values from a thermocouple to Kelvins or degrees Celsius, Fahrenheit, or Rankine.

#### Derives from

- Scale

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class ThermocoupleScale : Scale

#### Constructors

| Name | Description |
| --- | --- |
| ThermocoupleScale(string, ThermocoupleType, ThermocoupleCJCType, TemperatureUnit, BaseNode) | Initializes a new instance of the ThermocoupleScale class with the specified name and properties. |
| ThermocoupleScale(string) | Initializes a new instance of the ThermocoupleScale class with the specified name. |

#### Properties

| Name | Description |
| --- | --- |
| TemperatureUnit | Gets or sets the units of the scaled temperature values: Kelvins or degrees Celsius, Fahrenheit, or Rankine. |
| ThermocoupleCJCSource | Gets or sets the channel that serves as the source of cold-junction compensation for the ThermocoupleScale. |
| ThermocoupleCJCType | Gets or sets the type of device the thermocouple uses to perform cold-junction compensation. |
| ThermocoupleType | Gets or sets the type of thermocouple in use. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-thermocoupletype.html language=enus -->
## TOPIC 03899: ThermocoupleType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-thermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-thermocoupletype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the thermocouple type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum ThermocoupleTypeMembersNameValueDescriptionB0B type thermocouple. EE type thermocouple. JJ type thermocouple. KK type thermocouple. RR type thermocouple. SS type thermocouple. TT type thermoc

### ThermocoupleType Enumeration

Defines the thermocouple type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum ThermocoupleType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| B | 0 | B type thermocouple. |
| E |  | E type thermocouple. |
| J |  | J type thermocouple. |
| K |  | K type thermocouple. |
| R |  | R type thermocouple. |
| S |  | S type thermocouple. |
| T |  | T type thermocouple. |
| N |  | N type thermocouple. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timedifference-initialvalue.html language=enus -->
## TOPIC 03900: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timedifference-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timedifference-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the Time Difference channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InitialValue { get; set; }ReturnsT

### InitialValue

Gets or sets the initial value of the **Time Difference** channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InitialValue { get; set; }

#### Returns

The initial value of the channel.

Parent topic:

TimeDifference Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timedifference.html language=enus -->
## TOPIC 03901: TimeDifference Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timedifference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timedifference.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Time Difference channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel stores the difference between the two most recent ReceiveTime timestamps. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class TimeDifference : Channel

### TimeDifference Class

Represents the **Time Difference** channel for an incoming NI-XNET CAN, LIN, or FlexRay frame. This channel stores the difference between the two most recent [ReceiveTime](nationalinstruments-veristand-systemdefinitionapi-receivetime.html) timestamps.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class TimeDifference : Channel

#### Remarks

You can use the members of this class to configure the Time Difference channel and, and to set a dedicated start value, if required.

**Accessing this Class**

- [GetTimeDifference](nationalinstruments-veristand-systemdefinitionapi-frameinformation-gettimedifference.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| InitialValue | Gets or sets the initial value of the Time Difference channel. This property only represents an initial value for the channel, and does not actually enhance or delay frame transmission. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timestepduration.html language=enus -->
## TOPIC 03902: TimeStepDuration Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timestepduration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timestepduration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Time Step Duration channel, which you can use to get information about the duration, in microseconds, of the last time step of the model running on the target. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class TimeStepDuration : Channel

### TimeStepDuration Class

Represents a **Time Step Duration** channel, which you can use to get information about the duration, in microseconds, of the last time step of the model running on the target.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class TimeStepDuration : Channel

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingandsync-addtimingandsyncdevice__timingandsyncdevice-out.html language=enus -->
## TOPIC 03903: AddTimingAndSyncDevice(TimingAndSyncDevice, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingandsync-addtimingandsyncdevice__timingandsyncdevice-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingandsync-addtimingandsyncdevice__timingandsyncdevice-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified timingAndSyncDevice to the Timing and Sync section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddTimingAndSyncDevice(TimingAndSyncDevice timingAndSyncDevice, out Error error)ParametersNameTypeDescriptiontimingAndSyncDeviceTimingAndSyncDeviceThe

### AddTimingAndSyncDevice(TimingAndSyncDevice, out Error)

Adds the specified *timingAndSyncDevice*  to the **Timing and Sync** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddTimingAndSyncDevice(TimingAndSyncDevice timingAndSyncDevice, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timingAndSyncDevice | TimingAndSyncDevice | The timing and sync device to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the timing and sync device was added successfully.

Parent topic:

TimingAndSync Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingandsync-addtimingandsyncdevice__timingandsyncdevice.html language=enus -->
## TOPIC 03904: AddTimingAndSyncDevice(TimingAndSyncDevice)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingandsync-addtimingandsyncdevice__timingandsyncdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingandsync-addtimingandsyncdevice__timingandsyncdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified timingAndSyncDevice to the Timing and Sync section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddTimingAndSyncDevice(TimingAndSyncDevice timingAndSyncDevice)ParametersNameTypeDescriptiontimingAndSyncDeviceTimingAndSyncDeviceThe timing and sync d

### AddTimingAndSyncDevice(TimingAndSyncDevice)

Adds the specified *timingAndSyncDevice*  to the **Timing and Sync** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddTimingAndSyncDevice(TimingAndSyncDevice timingAndSyncDevice)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| timingAndSyncDevice | TimingAndSyncDevice | The timing and sync device to add. |

#### Returns

true if the timing and sync device was added successfully.

Parent topic:

TimingAndSync Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingandsync-gettimingandsyncdevicelist.html language=enus -->
## TOPIC 03905: GetTimingAndSyncDeviceList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingandsync-gettimingandsyncdevicelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingandsync-gettimingandsyncdevicelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the TimingAndSyncDevice elements from the TimingAndSync section. This method gets the existing timing and sync devices in the system definition. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TimingAndSyncDevice[] GetTimingAndSyncDeviceList()Rema

### GetTimingAndSyncDeviceList()

Gets an array that contains the [TimingAndSyncDevice](nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html) elements from the [TimingAndSync](nationalinstruments-veristand-systemdefinitionapi-timingandsync.html) section. This method gets the existing timing and sync devices in the system definition.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [TimingAndSyncDevice](nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html)[] GetTimingAndSyncDeviceList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [TimingAndSyncDevice](nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html) elements from the [TimingAndSync](nationalinstruments-veristand-systemdefinitionapi-timingandsync.html) section.

Parent topic:

TimingAndSync Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingandsync.html language=enus -->
## TOPIC 03906: TimingAndSync Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingandsync.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingandsync.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Timing and Sync section of the system definition, which contains all configured timing and sync devices. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class TimingAndSync : SectionRemarksUse the members of this class to add a new timing an

### TimingAndSync Class

Represents the **Timing and Sync** section of the system definition, which contains all configured timing and sync devices.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class TimingAndSync : Section

#### Remarks

Use the members of this class to add a new timing and sync device or get a list of existing devices.

**Accessing this Class**

- [GetTimingAndSync](nationalinstruments-veristand-systemdefinitionapi-chassis-gettimingandsync.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddTimingAndSyncDevice(TimingAndSyncDevice, out Error) | Adds the specified timingAndSyncDevice to the Timing and Sync section. |
| AddTimingAndSyncDevice(TimingAndSyncDevice) | Adds the specified timingAndSyncDevice to the Timing and Sync section. |
| GetTimingAndSyncDeviceList() | Gets an array that contains the TimingAndSyncDevice elements from the TimingAndSync section. This method gets the existing timing and sync devices in the system definition. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice-isrtsi0capable.html language=enus -->
## TOPIC 03907: IsRTSI0Capable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice-isrtsi0capable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice-isrtsi0capable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsRTSI0Capable { get; set;

### IsRTSI0Capable

Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsRTSI0Capable { get; set; }

#### Remarks

A device that can drive the RTSI 0 line can act as the chassis master hardware synchronization device for the system, meaning it cam control the synchronization of all hardware in a chassis.

#### Returns

true if the device can drive the RTSI 0 line.

Parent topic:

TimingAndSyncDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice-timingandsyncdevice__string-string.html language=enus -->
## TOPIC 03908: TimingAndSyncDevice(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice-timingandsyncdevice__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice-timingandsyncdevice__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the TimingAndSyncDevice class for the timing and sync device specified by Name and GUID . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic TimingAndSyncDevice(string Name, string GUID)ParametersNameTypeDescriptionNamestringThe name of the timing

### TimingAndSyncDevice(string, string)

Initializes a new instance of the [TimingAndSyncDevice](nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html) class for the timing and sync device specified by *Name*  and *GUID* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public TimingAndSyncDevice(string Name, string GUID)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the timing and sync device to access. |
| GUID | string | The associated GUID of the timing and sync device to access, as it appears in the Custom Device XML file for the timing and sync device. |

Parent topic:

TimingAndSyncDevice Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html language=enus -->
## TOPIC 03909: TimingAndSyncDevice Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingandsyncdevice.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a timing and sync device, which is a custom device that can drive the RTSI 0 line and synchronize all the hardware I/O devices in the system. Derives fromCustomDeviceSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class TimingAndSyncDevice : CustomDeviceRemarksUse

### TimingAndSyncDevice Class

Represents a timing and sync device, which is a custom device that can drive the RTSI 0 line and synchronize all the hardware I/O devices in the system.

#### Derives from

- CustomDevice

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class TimingAndSyncDevice : CustomDevice

#### Remarks

Use the members of this class to add sections and channels to a device, get and set device item property values, and get or set whether the device can drive the RTSI 0 line.

**Accessing this Class**

- [AddTimingAndSyncDevice(TimingAndSyncDevice, out Error)](nationalinstruments-veristand-systemdefinitionapi-timingandsync-addtimingandsyncdevice__timingandsyncdevice-out.html)
- [GetTimingAndSyncDeviceList](nationalinstruments-veristand-systemdefinitionapi-timingandsync-gettimingandsyncdevicelist.html)
- TimingAndSyncDevice Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| TimingAndSyncDevice(string, string) | Initializes a new instance of the TimingAndSyncDevice class for the timing and sync device specified by Name and GUID . |

#### Properties

| Name | Description |
| --- | --- |
| IsRTSI0Capable | Gets or sets whether the timing and sync device is capable of driving the RTSI 0 line, which is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-timingsourcesettingsoptions.html language=enus -->
## TOPIC 03910: TimingSourceSettingsOptions Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-timingsourcesettingsoptions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-timingsourcesettingsoptions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DAQ timing source setting for the Primary Control Loop when the PCL timing source is set to DAQ. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum TimingSourceSettingsOptionsMembersNameValueDescriptionControlLoopFromTask0The timing source uses a combination

### TimingSourceSettingsOptions Enumeration

Specifies the DAQ timing source setting for the Primary Control Loop when the PCL timing source is set to DAQ.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum TimingSourceSettingsOptions

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ControlLoopFromTask | 0 | The timing source uses a combination of the sample clock and the sleep time to determine when to send ticks to the Primary Control Loop. |
| SignalFromTask_SampleComplete | 1 | The timing source sends a tick to the Primary Control Loop each time a sample completes. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-transmittime-removetriggerchannel.html language=enus -->
## TOPIC 03911: RemoveTriggerChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-transmittime-removetriggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-transmittime-removetriggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes a TriggerChannel that you previously set on the Transmit Time channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveTriggerChannel()

### RemoveTriggerChannel()

Removes a [TriggerChannel](nationalinstruments-veristand-systemdefinitionapi-transmittime-triggerchannel.html) that you previously set on the Transmit Time channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveTriggerChannel()

Parent topic:

TransmitTime Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-transmittime-settriggerchannel__basenode.html language=enus -->
## TOPIC 03912: SetTriggerChannel(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-transmittime-settriggerchannel__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-transmittime-settriggerchannel__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a trigger channel to use to get the transmit time value for a Transmit Time channel. The value of this channel is used as the transmit time value, in seconds. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetTriggerChannel(BaseNode TriggerChannel)ParametersNameTy

### SetTriggerChannel(BaseNode)

Sets a trigger channel to use to get the transmit time value for a **Transmit Time** channel. The value of this channel is used as the transmit time value, in seconds.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetTriggerChannel(BaseNode TriggerChannel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| TriggerChannel | BaseNode | The channel to monitor for the transmit time value. |

Parent topic:

TransmitTime Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-transmittime-transmittimevalue.html language=enus -->
## TOPIC 03913: TransmitTimeValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-transmittime-transmittimevalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-transmittime-transmittimevalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the constant value to use as the transmit time, in seconds. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double TransmitTimeValue { get; set; }ReturnsThe transmit time, in seconds.

### TransmitTimeValue

Gets or sets the constant value to use as the transmit time, in seconds.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double TransmitTimeValue { get; set; }

#### Returns

The transmit time, in seconds.

Parent topic:

TransmitTime Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-transmittime-triggerchannel.html language=enus -->
## TOPIC 03914: TriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-transmittime-triggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-transmittime-triggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the trigger channel the Transmit Time channel is using to get its value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode TriggerChannel { get; }ReturnsA BaseNode reference to the trigger channel.

### TriggerChannel

Gets a reference to the trigger channel the **Transmit Time** channel is using to get its value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) TriggerChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the trigger channel.

Parent topic:

TransmitTime Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-transmittime-usetriggerchannel.html language=enus -->
## TOPIC 03915: UseTriggerChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-transmittime-usetriggerchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-transmittime-usetriggerchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets whether the Transmit Time channel is using a trigger channel to get the transmit time value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UseTriggerChannel { get; }Returnstrue if the Transmit Time channel is using a trigger channel value for the transmit time va

### UseTriggerChannel

Gets whether the **Transmit Time** channel is using a trigger channel to get the transmit time value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UseTriggerChannel { get; }

#### Returns

true if the **Transmit Time** channel is using a trigger channel value for the transmit time value.

Parent topic:

TransmitTime Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-transmittime.html language=enus -->
## TOPIC 03916: TransmitTime Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-transmittime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-transmittime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Transmit Time under the FrameFaulting section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies the amount of time that must elapse between subsequent transmissions of the cyclic frame. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefi

### TransmitTime Class

Represents a **Transmit Time** under the [FrameFaulting](nationalinstruments-veristand-systemdefinitionapi-framefaulting.html) section of an outgoing cyclic frame of an NI-XNET CAN port. This channel specifies the amount of time that must elapse between subsequent transmissions of the cyclic frame.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class TransmitTime : Channel

#### Remarks

Use the members of this class to configure the channel and to get or set the constant transmit time or the trigger channel to monitor for the transmit time.

**Accessing this Class**

- [GetTransmitTime](nationalinstruments-veristand-systemdefinitionapi-framefaulting-gettransmittime.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| TransmitTimeValue | Gets or sets the constant value to use as the transmit time, in seconds. |
| TriggerChannel | Gets a reference to the trigger channel the Transmit Time channel is using to get its value. |
| UseTriggerChannel | Gets whether the Transmit Time channel is using a trigger channel to get the transmit time value. |

#### Methods

| Name | Description |
| --- | --- |
| RemoveTriggerChannel() | Removes a TriggerChannel that you previously set on the Transmit Time channel. |
| SetTriggerChannel(BaseNode) | Sets a trigger channel to use to get the transmit time value for a Transmit Time channel. The value of this channel is used as the transmit time value, in seconds. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-triggertype.html language=enus -->
## TOPIC 03917: TriggerType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-triggertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-triggertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the type of a DAQTrigger. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum TriggerTypeMembersNameValueDescriptionNone0No trigger. AnalogEdgeAn analog edge trigger. AnalogWindowAn analog window trigger. DigitalEdgeA digital edge trigger. SoftwareA software trigger

### TriggerType Enumeration

Defines the type of a [DAQTrigger](nationalinstruments-veristand-systemdefinitionapi-daqtrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum TriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 0 | No trigger. |
| AnalogEdge |  | An analog edge trigger. |
| AnalogWindow |  | An analog window trigger. |
| DigitalEdge |  | A digital edge trigger. |
| Software |  | A software trigger. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-unconditional-addrawdatabasedframe__rawdatabasedframe-out.html language=enus -->
## TOPIC 03918: AddRawDataBasedFrame(RawDataBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-unconditional-addrawdatabasedframe__rawdatabasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-unconditional-addrawdatabasedframe__rawdatabasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified rawDataBasedFrame to the Unconditional section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe raw data forma

### AddRawDataBasedFrame(RawDataBasedFrame, out Error)

Adds the specified *rawDataBasedFrame*  to the **Unconditional** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The raw data format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

Unconditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-unconditional-addrawdatabasedframe__rawdatabasedframe.html language=enus -->
## TOPIC 03919: AddRawDataBasedFrame(RawDataBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-unconditional-addrawdatabasedframe__rawdatabasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-unconditional-addrawdatabasedframe__rawdatabasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified rawDataBasedFrame to the Unconditional section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)ParametersNameTypeDescriptionrawDataBasedFrameRawDataBasedFrameThe raw data format frame to add. R

### AddRawDataBasedFrame(RawDataBasedFrame)

Adds the specified *rawDataBasedFrame*  to the **Unconditional** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddRawDataBasedFrame(RawDataBasedFrame rawDataBasedFrame)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| rawDataBasedFrame | RawDataBasedFrame | The raw data format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

Unconditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-unconditional-addsignalbasedframe__signalbasedframe-out.html language=enus -->
## TOPIC 03920: AddSignalBasedFrame(SignalBasedFrame, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-unconditional-addsignalbasedframe__signalbasedframe-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-unconditional-addsignalbasedframe__signalbasedframe-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signalBasedFrame to the Unconditional section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)RemarksFor example code and more information about this method, refer to one of the f

### AddSignalBasedFrame(SignalBasedFrame, out Error)

Adds the specified *signalBasedFrame*  to the **Unconditional** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame, out Error error)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The signal format frame to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the frame was added successfully.

Parent topic:

Unconditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-unconditional-addsignalbasedframe__signalbasedframe.html language=enus -->
## TOPIC 03921: AddSignalBasedFrame(SignalBasedFrame)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-unconditional-addsignalbasedframe__signalbasedframe.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-unconditional-addsignalbasedframe__signalbasedframe.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified signalBasedFrame to the Unconditional section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)RemarksFor example code and more information about this method, refer to one of the following help top

### AddSignalBasedFrame(SignalBasedFrame)

Adds the specified *signalBasedFrame*  to the **Unconditional** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSignalBasedFrame(SignalBasedFrame signalBasedFrame)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| signalBasedFrame | SignalBasedFrame | The signal format frame to add. |

#### Returns

true if the frame was added successfully.

Parent topic:

Unconditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-unconditional-getrawdatabasedframelist.html language=enus -->
## TOPIC 03922: GetRawDataBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-unconditional-getrawdatabasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-unconditional-getrawdatabasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the RawDataBasedFrame elements from the current Unconditional section. This method gets all the outgoing unconditional, raw data format frames under the current port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic RawDataBasedFrame[] GetRawDataBa

### GetRawDataBasedFrameList()

Gets an array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [Unconditional](nationalinstruments-veristand-systemdefinitionapi-unconditional.html) section. This method gets all the outgoing unconditional, raw data format frames under the current port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html)[] GetRawDataBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [RawDataBasedFrame](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe.html) elements from the current [Unconditional](nationalinstruments-veristand-systemdefinitionapi-unconditional.html) section.

Parent topic:

Unconditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-unconditional-getsignalbasedframelist.html language=enus -->
## TOPIC 03923: GetSignalBasedFrameList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-unconditional-getsignalbasedframelist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-unconditional-getsignalbasedframelist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the SignalBasedFrame elements from the current Unconditional section. This method gets all the outgoing unconditional, signal format frames under the current port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic SignalBasedFrame[] GetSignalBasedFr

### GetSignalBasedFrameList()

Gets an array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [Unconditional](nationalinstruments-veristand-systemdefinitionapi-unconditional.html) section. This method gets all the outgoing unconditional, signal format frames under the current port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html)[] GetSignalBasedFrameList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [SignalBasedFrame](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe.html) elements from the current [Unconditional](nationalinstruments-veristand-systemdefinitionapi-unconditional.html) section.

Parent topic:

Unconditional Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-unconditional.html language=enus -->
## TOPIC 03924: Unconditional Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-unconditional.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-unconditional.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Unconditional section that contains outgoing, unconditional frames under an NI-XNET LIN port. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Unconditional : SectionRemarksUnconditional frames are the most common type of outgoing LIN f

### Unconditional Class

Represents the **Unconditional** section that contains outgoing, unconditional frames under an NI-XNET LIN port.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Unconditional : Section

#### Remarks

Unconditional frames are the most common type of outgoing LIN frame and carry signals, or data. Unconditional frames have identifiers from 0 – 59 (0x3B). Use the members of this class to add or access unconditional frames.

**Accessing this Class**

- [GetUnconditional](nationalinstruments-veristand-systemdefinitionapi-outgoing-getunconditional.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddRawDataBasedFrame(RawDataBasedFrame) | Adds the specified rawDataBasedFrame to the Unconditional section. |
| AddRawDataBasedFrame(RawDataBasedFrame, out Error) | Adds the specified rawDataBasedFrame to the Unconditional section. |
| AddSignalBasedFrame(SignalBasedFrame, out Error) | Adds the specified signalBasedFrame to the Unconditional section. |
| AddSignalBasedFrame(SignalBasedFrame) | Adds the specified signalBasedFrame to the Unconditional section. |
| GetRawDataBasedFrameList() | Gets an array that contains the RawDataBasedFrame elements from the current Unconditional section. This method gets all the outgoing unconditional, raw data format frames under the current port. |
| GetSignalBasedFrameList() | Gets an array that contains the SignalBasedFrame elements from the current Unconditional section. This method gets all the outgoing unconditional, signal format frames under the current port. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannel-initialvalue.html language=enus -->
## TOPIC 03925: InitialValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannel-initialvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannel-initialvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the initial value of the user channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InitialValue { get; set; }ReturnsThe initial value of the channel.

### InitialValue

Gets or sets the initial value of the user channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InitialValue { get; set; }

#### Returns

The initial value of the channel.

Parent topic:

UserChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannel-userchannel__string-string-string-double.html language=enus -->
## TOPIC 03926: UserChannel(string, string, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannel-userchannel__string-string-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannel-userchannel__string-string-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of UserChannel with the specified name, description, units, and default value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannel(string Name, string Description, string Units, double DefaultValue)ParametersNameTypeDescriptionNamestringThe

### UserChannel(string, string, string, double)

Initializes a new instance of [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) with the specified name, description, units, and default value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public UserChannel(string Name, string Description, string Units, double DefaultValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channel. |
| Description | string | The description of the user channel. |
| Units | string | The units to associate with the user channel. |
| DefaultValue | double | The default value of the user channel. |

Parent topic:

UserChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannel.html language=enus -->
## TOPIC 03927: UserChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a user channel, which stores a single value. You can use user channels as variables in procedures, stimulus profiles, and so on. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class UserChannel : ChannelRemarksUse the members of this class to c

### UserChannel Class

Represents a user channel, which stores a single value. You can use user channels as variables in procedures, stimulus profiles, and so on.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class UserChannel : Channel

#### Remarks

Use the members of this class to configure the channel and get or set its initial value.

**Accessing this Class**

- [GetUserChannelList(bool)](nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannellist__bool.html)
- [GetUserChannelList(bool)](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannellist__bool.html)
- UserChannel Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| UserChannel(string, string, string, double) | Initializes a new instance of UserChannel with the specified name, description, units, and default value. |

#### Properties

| Name | Description |
| --- | --- |
| InitialValue | Gets or sets the initial value of the user channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannel__string-string-string-double-out.html language=enus -->
## TOPIC 03928: AddNewUserChannel(string, string, string, double, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannel__string-string-string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannel__string-string-string-double-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannel with the specified name, description, units, and default value to the User Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannel AddNewUserChannel(string Name, string Description, string Units, double DefaultValue, out Error err

### AddNewUserChannel(string, string, string, double, out Error)

Adds a new [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) with the specified name, description, units, and default value to the **User Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) AddNewUserChannel(string Name, string Description, string Units, double DefaultValue, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channel. |
| Description | string | The description of the user channel. |
| Units | string | The units to associate with the user channel. |
| DefaultValue | double | The default value of the user channel. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The newly created UserChannel

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannel__string-string-string-double.html language=enus -->
## TOPIC 03929: AddNewUserChannel(string, string, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannel__string-string-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannel__string-string-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannel with the specified name, description, units, and default value to the User Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewUserChannel(string Name, string Description, string Units, double DefaultValue)ParametersNameTypeDes

### AddNewUserChannel(string, string, string, double)

Adds a new [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) with the specified name, description, units, and default value to the **User Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewUserChannel(string Name, string Description, string Units, double DefaultValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channel. |
| Description | string | The description of the user channel. |
| Units | string | The units to associate with the user channel. |
| DefaultValue | double | The default value of the user channel. |

#### Returns

true if the user channel was added successfully.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannelsfolder__string-string-out.html language=enus -->
## TOPIC 03930: AddNewUserChannelsFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannelsfolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannelsfolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannelsFolder with the specified name and description to the User Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannelsFolder AddNewUserChannelsFolder(string Name, string Description, out Error error)ParametersNameTypeDescriptionNames

### AddNewUserChannelsFolder(string, string, out Error)

Adds a new [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) with the specified name and description to the **User Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) AddNewUserChannelsFolder(string Name, string Description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channels folder. |
| Description | string | The description of the user channels folder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The newly created UserChannelsFolder

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannelsfolder__string-string.html language=enus -->
## TOPIC 03931: AddNewUserChannelsFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannelsfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-addnewuserchannelsfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannelsFolder with the specified name and description to the User Channels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewUserChannelsFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the user chann

### AddNewUserChannelsFolder(string, string)

Adds a new [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) with the specified name and description to the **User Channels** section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewUserChannelsFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channels folder. |
| Description | string | The description of the user channels folder. |

#### Returns

true if the folder was added successfully.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannel__userchannel-out.html language=enus -->
## TOPIC 03932: AddUserChannel(UserChannel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannel__userchannel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannel__userchannel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannel to the User Channels section.. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannel(UserChannel channel, out Error error)ParametersNameTypeDescriptionchannelUserChannelThe user channel to add.errorout ErrorReturns an NationalInst

### AddUserChannel(UserChannel, out Error)

Adds the specified [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) to the **User Channels** section..

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannel(UserChannel channel, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | UserChannel | The user channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the user channel was added successfully.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannel__userchannel.html language=enus -->
## TOPIC 03933: AddUserChannel(UserChannel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannel__userchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannel__userchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannel to the User Channels section.. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannel(UserChannel channel)ParametersNameTypeDescriptionchannelUserChannelThe user channel to add.Returnstrue if the user channel was added successfully

### AddUserChannel(UserChannel)

Adds the specified [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) to the **User Channels** section..

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannel(UserChannel channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | UserChannel | The user channel to add. |

#### Returns

true if the user channel was added successfully.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannelsfolder__userchannelsfolder-out.html language=enus -->
## TOPIC 03934: AddUserChannelsFolder(UserChannelsFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannelsfolder__userchannelsfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannelsfolder__userchannelsfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannelsFolder to the User Channels section.. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannelsFolder(UserChannelsFolder folder, out Error error)ParametersNameTypeDescriptionfolderUserChannelsFolderThe user channel folder to add.erro

### AddUserChannelsFolder(UserChannelsFolder, out Error)

Adds the specified [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) to the **User Channels** section..

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannelsFolder(UserChannelsFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | UserChannelsFolder | The user channel folder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the folder was added successfully.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannelsfolder__userchannelsfolder.html language=enus -->
## TOPIC 03935: AddUserChannelsFolder(UserChannelsFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannelsfolder__userchannelsfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-adduserchannelsfolder__userchannelsfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannelsFolder to the User Channels section.. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannelsFolder(UserChannelsFolder folder)ParametersNameTypeDescriptionfolderUserChannelsFolderThe user channel folder to add.Returnstrue if the fo

### AddUserChannelsFolder(UserChannelsFolder)

Adds the specified [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) to the **User Channels** section..

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannelsFolder(UserChannelsFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | UserChannelsFolder | The user channel folder to add. |

#### Returns

true if the folder was added successfully.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannelfolderlist.html language=enus -->
## TOPIC 03936: GetUserChannelFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannelfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannelfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannelsFolder elements from the UserChannels section. This method only returns folders that are direct descendants of the UserChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannelsFolder[] GetUserChannelFolderList(

### GetUserChannelFolderList()

Gets an array that contains the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section. This method only returns folders that are direct descendants of the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html)[] GetUserChannelFolderList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannelfolderlist__bool.html language=enus -->
## TOPIC 03937: GetUserChannelFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannelfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannelfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannelsFolder elements from the UserChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannelsFolder[] GetUserChannelFolderList(bool deep)RemarksModifications you make to the contents of this list apply to the system d

### GetUserChannelFolderList(bool)

Gets an array that contains the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html)[] GetUserChannelFolderList(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child UserChannelsFolder element of the UserChannels section. true if the method traverses each child UserChannelsFolder instance to search for other UserChannelsFolder instances to traverse or other UserChannelsFolder elements to add to the result list; otherwise false. |

#### Returns

An array that contains the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannellist.html language=enus -->
## TOPIC 03938: GetUserChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannel elements from the UserChannels section. This method only returns user channels that are direct descendants of the UserChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannel[] GetUserChannelList()RemarksModifi

### GetUserChannelList()

Gets an array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section. This method only returns user channels that are direct descendants of the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html)[] GetUserChannelList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannellist__bool.html language=enus -->
## TOPIC 03939: GetUserChannelList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannellist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannellist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannel elements from the UserChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannel[] GetUserChannelList(bool deep)RemarksModifications you make to the contents of this list apply to the system definition. However,

### GetUserChannelList(bool)

Gets an array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html)[] GetUserChannelList(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child UserChannelsFolder element of the UserChannels section. true if the method traverses each child UserChannelsFolder instance to search for other UserChannelsFolder instances to traverse or other UserChannel elements to add to the result list; otherwise false. |

#### Returns

An array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section.

Parent topic:

UserChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannels.html language=enus -->
## TOPIC 03940: UserChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the User Channels section of a Target, which contains any user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Us

### UserChannels Class

Represents the **User Channels** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html), which contains any user channels you configure. User channels store a single value, and can be variables in procedures, stimulus profiles, and so on.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class UserChannels : Section

#### Remarks

Use the members of this class to add a new or existing [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) or [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html), or to get a list of existing channels or folders.

**Accessing this Class**

- [GetUserChannels](nationalinstruments-veristand-systemdefinitionapi-target-getuserchannels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddNewUserChannel(string, string, string, double) | Adds a new UserChannel with the specified name, description, units, and default value to the User Channels section. |
| AddNewUserChannel(string, string, string, double, out Error) | Adds a new UserChannel with the specified name, description, units, and default value to the User Channels section. |
| AddNewUserChannelsFolder(string, string, out Error) | Adds a new UserChannelsFolder with the specified name and description to the User Channels section. |
| AddNewUserChannelsFolder(string, string) | Adds a new UserChannelsFolder with the specified name and description to the User Channels section. |
| AddUserChannel(UserChannel, out Error) | Adds the specified UserChannel to the User Channels section.. |
| AddUserChannel(UserChannel) | Adds the specified UserChannel to the User Channels section.. |
| AddUserChannelsFolder(UserChannelsFolder, out Error) | Adds the specified UserChannelsFolder to the User Channels section.. |
| AddUserChannelsFolder(UserChannelsFolder) | Adds the specified UserChannelsFolder to the User Channels section.. |
| GetUserChannelFolderList() | Gets an array that contains the UserChannelsFolder elements from the UserChannels section. This method only returns folders that are direct descendants of the UserChannels section. |
| GetUserChannelFolderList(bool) | Gets an array that contains the UserChannelsFolder elements from the UserChannels section. |
| GetUserChannelList() | Gets an array that contains the UserChannel elements from the UserChannels section. This method only returns user channels that are direct descendants of the UserChannels section. |
| GetUserChannelList(bool) | Gets an array that contains the UserChannel elements from the UserChannels section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannel__string-string-string-double-out.html language=enus -->
## TOPIC 03941: AddNewUserChannel(string, string, string, double, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannel__string-string-string-double-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannel__string-string-string-double-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannel with the specified name, description, units, and default value to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannel AddNewUserChannel(string Name, string Description, string Units, double DefaultValue, out Error error)

### AddNewUserChannel(string, string, string, double, out Error)

Adds a new [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) with the specified name, description, units, and default value to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) AddNewUserChannel(string Name, string Description, string Units, double DefaultValue, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channel. |
| Description | string | The description of the user channel. |
| Units | string | The units to associate with the user channel. |
| DefaultValue | double | The default value of the user channel. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The newly created UserChannel

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannel__string-string-string-double.html language=enus -->
## TOPIC 03942: AddNewUserChannel(string, string, string, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannel__string-string-string-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannel__string-string-string-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannel with the specified name, description, units, and default value to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewUserChannel(string Name, string Description, string Units, double DefaultValue)ParametersNameTypeDescri

### AddNewUserChannel(string, string, string, double)

Adds a new [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) with the specified name, description, units, and default value to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewUserChannel(string Name, string Description, string Units, double DefaultValue)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channel. |
| Description | string | The description of the user channel. |
| Units | string | The units to associate with the user channel. |
| DefaultValue | double | The default value of the user channel. |

#### Returns

true if the user channel was added successfully.

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannelsfolder__string-string-out.html language=enus -->
## TOPIC 03943: AddNewUserChannelsFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannelsfolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannelsfolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannelsFolder with the specified name and description to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannelsFolder AddNewUserChannelsFolder(string Name, string Description, out Error error)ParametersNameTypeDescriptionNamestri

### AddNewUserChannelsFolder(string, string, out Error)

Adds a new [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) with the specified name and description to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) AddNewUserChannelsFolder(string Name, string Description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channels folder. |
| Description | string | The description of the user channels folder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The newly created UserChannelsFolder

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannelsfolder__string-string.html language=enus -->
## TOPIC 03944: AddNewUserChannelsFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannelsfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-addnewuserchannelsfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new UserChannelsFolder with the specified name and description to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewUserChannelsFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the user channels

### AddNewUserChannelsFolder(string, string)

Adds a new [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) with the specified name and description to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewUserChannelsFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the user channels folder. |
| Description | string | The description of the user channels folder. |

#### Returns

true if the folder was added successfully.

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannel__userchannel-out.html language=enus -->
## TOPIC 03945: AddUserChannel(UserChannel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannel__userchannel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannel__userchannel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannel to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannel(UserChannel channel, out Error error)ParametersNameTypeDescriptionchannelUserChannelThe user channel to add.errorout ErrorReturns an NationalInstrume

### AddUserChannel(UserChannel, out Error)

Adds the specified [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannel(UserChannel channel, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | UserChannel | The user channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the user channel was added successfully.

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannel__userchannel.html language=enus -->
## TOPIC 03946: AddUserChannel(UserChannel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannel__userchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannel__userchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannel to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannel(UserChannel channel)ParametersNameTypeDescriptionchannelUserChannelThe user channel to add.Returnstrue if the user channel was added successfully.

### AddUserChannel(UserChannel)

Adds the specified [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannel(UserChannel channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channel | UserChannel | The user channel to add. |

#### Returns

true if the user channel was added successfully.

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannelsfolder__userchannelsfolder-out.html language=enus -->
## TOPIC 03947: AddUserChannelsFolder(UserChannelsFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannelsfolder__userchannelsfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannelsfolder__userchannelsfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannelsFolder to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannelsFolder(UserChannelsFolder folder, out Error error)ParametersNameTypeDescriptionfolderUserChannelsFolderThe user channel folder to add.errorout

### AddUserChannelsFolder(UserChannelsFolder, out Error)

Adds the specified [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannelsFolder(UserChannelsFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | UserChannelsFolder | The user channel folder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the folder was added successfully.

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannelsfolder__userchannelsfolder.html language=enus -->
## TOPIC 03948: AddUserChannelsFolder(UserChannelsFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannelsfolder__userchannelsfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-adduserchannelsfolder__userchannelsfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified UserChannelsFolder to the UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddUserChannelsFolder(UserChannelsFolder folder)ParametersNameTypeDescriptionfolderUserChannelsFolderThe user channel folder to add.Returnstrue if the folder

### AddUserChannelsFolder(UserChannelsFolder)

Adds the specified [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) to the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddUserChannelsFolder(UserChannelsFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | UserChannelsFolder | The user channel folder to add. |

#### Returns

true if the folder was added successfully.

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannelfolderlist.html language=enus -->
## TOPIC 03949: GetUserChannelFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannelfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannelfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannel elements from the current UserChannelsFolder. This method only returns folders that are direct descendants of the current UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannelsFolder[] GetUserChannelFolder

### GetUserChannelFolderList()

Gets an array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html). This method only returns folders that are direct descendants of the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html)[] GetUserChannelFolderList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannelfolderlist__bool.html language=enus -->
## TOPIC 03950: GetUserChannelFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannelfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannelfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannel elements from the current UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannelsFolder[] GetUserChannelFolderList(bool deep)RemarksModifications you make to the contents of this list apply to the system de

### GetUserChannelFolderList(bool)

Gets an array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html)[] GetUserChannelFolderList(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child UserChannelsFolder element of the UserChannelsFolder instance. true if the method traverses each child UserChannelsFolder instance to search for other UserChannelsFolder instances to traverse or other UserChannelsFolder elements to add to the result list; otherwise false. |

#### Returns

An array that contains the [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannellist.html language=enus -->
## TOPIC 03951: GetUserChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannel elements from the current UserChannelsFolder. This method only returns user channels that are direct descendants of the current UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannel[] GetUserChannelList()R

### GetUserChannelList()

Gets an array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html). This method only returns user channels that are direct descendants of the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html)[] GetUserChannelList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannellist__bool.html language=enus -->
## TOPIC 03952: GetUserChannelList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannellist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannellist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the UserChannel elements from the current UserChannelsFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannel[] GetUserChannelList(bool deep)RemarksModifications you make to the contents of this list apply to the system definition. How

### GetUserChannelList(bool)

Gets an array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html)[] GetUserChannelList(bool deep)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child UserChannelsFolder element of the UserChannelsFolder instance. true if the method traverses each child UserChannelsFolder instance to search for other UserChannelsFolder instances to traverse or other UserChannel elements to add to the result list; otherwise false. |

#### Returns

An array that contains the [UserChannel](nationalinstruments-veristand-systemdefinitionapi-userchannel.html) elements from the current [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html).

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-userchannelsfolder__string-string.html language=enus -->
## TOPIC 03953: UserChannelsFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-userchannelsfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-userchannelsfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of UserChannelsFolder with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic UserChannelsFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the folder.DescriptionstringThe des

### UserChannelsFolder(string, string)

Initializes a new instance of [UserChannelsFolder](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html) with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public UserChannelsFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the folder. |
| Description | string | The description of the folder. |

Parent topic:

UserChannelsFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html language=enus -->
## TOPIC 03954: UserChannelsFolder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a folder under the UserChannels section of a target. Folders simply organize user channels into logical groups. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class UserChannelsFolder : SectionRemarksUse the members of this class to add a new o

### UserChannelsFolder Class

Represents a folder under the [UserChannels](nationalinstruments-veristand-systemdefinitionapi-userchannels.html) section of a target. Folders simply organize user channels into logical groups.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class UserChannelsFolder : Section

#### Remarks

Use the members of this class to add a new or existing user channel or user channels folder to the current folder, or to get a list of existing channels or sub-folders.

**Accessing this Class**

- [GetUserChannelFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-userchannels-getuserchannelfolderlist__bool.html)
- [GetUserChannelFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-userchannelsfolder-getuserchannelfolderlist__bool.html)
- UserChannelsFolder Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| UserChannelsFolder(string, string) | Initializes a new instance of UserChannelsFolder with the specified name and description. |

#### Methods

| Name | Description |
| --- | --- |
| AddNewUserChannel(string, string, string, double) | Adds a new UserChannel with the specified name, description, units, and default value to the UserChannelsFolder. |
| AddNewUserChannel(string, string, string, double, out Error) | Adds a new UserChannel with the specified name, description, units, and default value to the UserChannelsFolder. |
| AddNewUserChannelsFolder(string, string, out Error) | Adds a new UserChannelsFolder with the specified name and description to the UserChannelsFolder. |
| AddNewUserChannelsFolder(string, string) | Adds a new UserChannelsFolder with the specified name and description to the UserChannelsFolder. |
| AddUserChannel(UserChannel, out Error) | Adds the specified UserChannel to the UserChannelsFolder. |
| AddUserChannel(UserChannel) | Adds the specified UserChannel to the UserChannelsFolder. |
| AddUserChannelsFolder(UserChannelsFolder, out Error) | Adds the specified UserChannelsFolder to the UserChannelsFolder. |
| AddUserChannelsFolder(UserChannelsFolder) | Adds the specified UserChannelsFolder to the UserChannelsFolder. |
| GetUserChannelFolderList() | Gets an array that contains the UserChannel elements from the current UserChannelsFolder. This method only returns folders that are direct descendants of the current UserChannelsFolder. |
| GetUserChannelFolderList(bool) | Gets an array that contains the UserChannel elements from the current UserChannelsFolder. |
| GetUserChannelList() | Gets an array that contains the UserChannel elements from the current UserChannelsFolder. This method only returns user channels that are direct descendants of the current UserChannelsFolder. |
| GetUserChannelList(bool) | Gets an array that contains the UserChannel elements from the current UserChannelsFolder. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-addmapping__channel-channel.html language=enus -->
## TOPIC 03955: AddMapping(Channel, Channel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-addmapping__channel-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-addmapping__channel-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a channel mapping to the system. The source channel maps to the destination channel, but the destination channel stores the mapping information. This method overwrites any pre-existing mapping information on the destination channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitio

### AddMapping(Channel, Channel)

Adds a channel mapping to the system. The source channel maps to the destination channel, but the destination channel stores the mapping information. This method overwrites any pre-existing mapping information on the destination channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static void AddMapping(Channel Source, Channel Destination)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Source | Channel | The source channel. |
| Destination | Channel | The destination channel. |

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-afprtpath.html language=enus -->
## TOPIC 03956: AfpRtPath()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-afprtpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-afprtpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the binary automatic frame processing (.ini) file on an RT target for which automatic frame processing is enabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string AfpRtPath()ReturnsThe path to the .ini file.

### AfpRtPath()

Gets the path to the binary automatic frame processing (.ini) file on an RT target for which automatic frame processing is enabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string AfpRtPath()

#### Returns

The path to the .ini file.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string..html language=enus -->
## TOPIC 03957: AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< KeyValuePair< IChannel, IChannel > > AutoMapChannels(BaseNode sourceNode, BaseNode destinationNode, IEqualityComparer< string > comparer)

### AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< KeyValuePair< [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html), [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html) > > AutoMapChannels(BaseNode sourceNode, BaseNode destinationNode, IEqualityComparer< string > comparer)

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string_-predicate_ichannel..html language=enus -->
## TOPIC 03958: AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >, Predicate< IChannel >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string_-predicate_ichannel..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string_-predicate_ichannel..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< KeyValuePair< IChannel, IChannel > > AutoMapChannels(BaseNode sourceNode, BaseNode destinationNode, IEqualityComparer< string > comparer, Predicate< IChannel > inclusionFilter)

### AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >, Predicate< IChannel >)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< KeyValuePair< [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html), [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html) > > AutoMapChannels(BaseNode sourceNode, BaseNode destinationNode, IEqualityComparer< string > comparer, Predicate< IChannel > inclusionFilter)

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string_-predicate_ichannel_-predicate_basenode..html language=enus -->
## TOPIC 03959: AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >, Predicate< IChannel >, Predicate< BaseNode >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string_-predicate_ichannel_-predicate_basenode..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode-iequalitycomparer_string_-predicate_ichannel_-predicate_basenode..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find name matches between the source and destination channels and maps them If there are multiple names that match in either collection, we will only return the first as a match. This is done to improve performance for large channel count. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinit

### AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >, Predicate< IChannel >, Predicate< BaseNode >)

Find name matches between the source and destination channels and maps them If there are multiple names that match in either collection, we will only return the first as a match. This is done to improve performance for large channel count.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< KeyValuePair< [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html), [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html) > > AutoMapChannels(BaseNode sourceNode, BaseNode destinationNode, IEqualityComparer< string > comparer, Predicate< IChannel > inclusionFilter, Predicate< BaseNode > recursePredicate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceNode | BaseNode | Source node to attempt name matching with it's descendant channels |
| destinationNode | BaseNode | Destination node to attempt name matching with it's descendant channels |
| comparer | IEqualityComparer< string > | Comparison algorithm. Passing null will yield default |
| inclusionFilter | Predicate< IChannel > | Inclusion filter for channels beneath each node. Passing null will yield the default behavior |
| recursePredicate | Predicate< BaseNode > | Whether we should recurse below a given node. Passing null will yield default results(skip some builtin channels) |

#### Returns

list of mappings that were created - Source to Destination

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode.html language=enus -->
## TOPIC 03960: AutoMapChannels(BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-automapchannels__basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static IEnumerable< KeyValuePair< IChannel, IChannel > > AutoMapChannels(BaseNode sourceNode, BaseNode destinationNode)

### AutoMapChannels(BaseNode, BaseNode)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< KeyValuePair< [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html), [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html) > > AutoMapChannels(BaseNode sourceNode, BaseNode destinationNode)

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-buildpath__string-string.html language=enus -->
## TOPIC 03961: BuildPath(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-buildpath__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-buildpath__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new path by appending a name (or relative path) to an existing path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string BuildPath(string path, string relative)ParametersNameTypeDescriptionpathstringThe base path to which to append relative .relativestrin

### BuildPath(string, string)

Creates a new path by appending a name (or relative path) to an existing path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string BuildPath(string path, string relative)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The base path to which to append relative . |
| relative | string | The new path component to append to path . |

#### Returns

The resulting path.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-clearmapping__channel.html language=enus -->
## TOPIC 03962: ClearMapping(Channel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-clearmapping__channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-clearmapping__channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the channel mapping for the specified destination channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static void ClearMapping(Channel Destination)ParametersNameTypeDescriptionDestinationChannelThe destination channel whose source channel mapping you want to remo

### ClearMapping(Channel)

Clears the channel mapping for the specified destination channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static void ClearMapping(Channel Destination)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Destination | Channel | The destination channel whose source channel mapping you want to remove. |

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-createbasenodefromsystemstoragenode__basenodetype.html language=enus -->
## TOPIC 03963: CreateBaseNodeFromSystemStorageNode(BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-createbasenodefromsystemstoragenode__basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-createbasenodefromsystemstoragenode__basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a SystemDefinitionAPI BaseNode from a SystemStorage BaseNodeType. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static BaseNode CreateBaseNodeFromSystemStorageNode(BaseNodeType storageNode)ParametersNameTypeDescriptionstorageNodeBaseNodeTypeThe SystemStorage BaseNo

### CreateBaseNodeFromSystemStorageNode(BaseNodeType)

Creates a SystemDefinitionAPI [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) from a SystemStorage BaseNodeType.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) CreateBaseNodeFromSystemStorageNode(BaseNodeType storageNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| storageNode | BaseNodeType | The SystemStorage BaseNodeType from which to create the BaseNode. |

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) object that contains the *storageNode* .

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-currentversion.html language=enus -->
## TOPIC 03964: CurrentVersion

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-currentversion.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-currentversion.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the current version information for the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static SystemStorage.VersionType CurrentVersion { get; }Remarks object reference. ReturnsA VersionType reference. Use the VersionTypeToVersion method to conve

### CurrentVersion

Gets the current version information for the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static SystemStorage.VersionType CurrentVersion { get; }

#### Remarks

object reference.

#### Returns

A VersionType reference. Use the [VersionTypeToVersion](nationalinstruments-veristand-systemdefinitionapi-utilities-versiontypetoversion__systemstorage.versiontype.html) method to convert this reference to a System.Version

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-datareplayrtpath.html language=enus -->
## TOPIC 03965: DataReplayRTPath()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-datareplayrtpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-datareplayrtpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path on the RT target to the folder where NI-XNET DataFileReplay files are stored. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string DataReplayRTPath()ReturnsThe path to the folder where DataFileReplay files are stored.

### DataReplayRTPath()

Gets the path on the RT target to the folder where NI-XNET [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html) files are stored.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string DataReplayRTPath()

#### Returns

The path to the folder where [DataFileReplay](nationalinstruments-veristand-systemdefinitionapi-datafilereplay.html) files are stored.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-datetimetodouble__datetime.html language=enus -->
## TOPIC 03966: DateTimeToDouble(DateTime)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-datetimetodouble__datetime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-datetimetodouble__datetime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the time stamp specified by dateTime to a double-precision, floating-point number. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static double DateTimeToDouble(DateTime dateTime)ParametersNameTypeDescriptiondateTimeDateTimeThe time stamp to convert.ReturnsThe date

### DateTimeToDouble(DateTime)

Converts the time stamp specified by *dateTime*  to a double-precision, floating-point number.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static double DateTimeToDouble(DateTime dateTime)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| dateTime | DateTime | The time stamp to convert. |

#### Returns

The *dateTime*  in double representation, as a total number of seconds.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-defaultautomaprecursionfilter__basenode.html language=enus -->
## TOPIC 03967: DefaultAutoMapRecursionFilter(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-defaultautomaprecursionfilter__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-defaultautomaprecursionfilter__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Default recursion filter for automap. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool DefaultAutoMapRecursionFilter(BaseNode node)ParametersNameTypeDescriptionnodeBaseNodeBaseNode to considerReturnstrue if the baseNode and it's children should be considered for A

### DefaultAutoMapRecursionFilter(BaseNode)

Default recursion filter for automap.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool DefaultAutoMapRecursionFilter(BaseNode node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BaseNode | BaseNode to consider |

#### Returns

true if the baseNode and it's children should be considered for AutoMap. False otherwise.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-deserializeslsc__string-out-basenodetype.html language=enus -->
## TOPIC 03968: DeserializeSLSC(string, out Error, BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-deserializeslsc__string-out-basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-deserializeslsc__string-out-basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deserialize SLSC node from file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static void DeserializeSLSC(string filepath, out Error error, BaseNodeType baseNode)ParametersNameTypeDescriptionfilepathstringThe path to the file to deserialize from.errorout ErrorThe error ou

### DeserializeSLSC(string, out Error, BaseNodeType)

Deserialize SLSC node from file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static void DeserializeSLSC(string filepath, out Error error, BaseNodeType baseNode)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | The path to the file to deserialize from. |
| error | out Error | The error output string. |
| baseNode | BaseNodeType | The SLSC node to add the chassis under. |

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-doubletodatetime__double.html language=enus -->
## TOPIC 03969: DoubleToDateTime(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-doubletodatetime__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-doubletodatetime__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts the double-precision, floating-point number specified by totalSeconds to a time stamp. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static DateTime DoubleToDateTime(double totalSeconds)ParametersNameTypeDescriptiontotalSecondsdoubleThe number to convert to a time

### DoubleToDateTime(double)

Converts the double-precision, floating-point number specified by *totalSeconds*  to a time stamp.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static DateTime DoubleToDateTime(double totalSeconds)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| totalSeconds | double | The number to convert to a time stamp. This value must represent a number of seconds. |

#### Returns

The *totalSeconds*  as a time stamp.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-findnamematches__ienumerable_ichannel_-ienumerable_ichannel_-iequalitycomparer_string..html language=enus -->
## TOPIC 03970: FindNameMatches(IEnumerable< IChannel >, IEnumerable< IChannel >, IEqualityComparer< string >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-findnamematches__ienumerable_ichannel_-ienumerable_ichannel_-iequalitycomparer_string..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-findnamematches__ienumerable_ichannel_-ienumerable_ichannel_-iequalitycomparer_string..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Find name matches between the source and destination channels. If there are multiple names that match in either collection, we will only return the first as a match. This is done to improve performance for large channel count. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### FindNameMatches(IEnumerable< IChannel >, IEnumerable< IChannel >, IEqualityComparer< string >)

Find name matches between the source and destination channels. If there are multiple names that match in either collection, we will only return the first as a match. This is done to improve performance for large channel count.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static IEnumerable< KeyValuePair< [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html), [IChannel](nationalinstruments-veristand-systemdefinitionapi-ichannel.html) > > FindNameMatches(IEnumerable< IChannel > sourceChannels, IEnumerable< IChannel > destinationChannels, IEqualityComparer< string > comparer)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sourceChannels | IEnumerable< IChannel > | source channels |
| destinationChannels | IEnumerable< IChannel > | destination channels |
| comparer | IEqualityComparer< string > | Comparison algorithm. Passing null will yield default |

#### Returns

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-getfilename__string.html language=enus -->
## TOPIC 03971: GetFilename(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-getfilename__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-getfilename__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the file at the specified path . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string GetFilename(string path)ParametersNameTypeDescriptionpathstringThe path to the file whose name you want to return.ReturnsThe filename.

### GetFilename(string)

Gets the name of the file at the specified *path* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string GetFilename(string path)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The path to the file whose name you want to return. |

#### Returns

The filename.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-getlocalizednamebyguid__string.html language=enus -->
## TOPIC 03972: GetLocalizedNameByGUID(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-getlocalizednamebyguid__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-getlocalizednamebyguid__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the localized name of the node associated with the specified GUID . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string GetLocalizedNameByGUID(string GUID)RemarksThis method searches all page declarations within the system. ParametersNameTypeDescriptionGUIDstr

### GetLocalizedNameByGUID(string)

Gets the localized name of the node associated with the specified *GUID* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string GetLocalizedNameByGUID(string GUID)

#### Remarks

This method searches all page declarations within the system.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| GUID | string | The GUID of the node. |

#### Returns

The node name.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-pathtypepairtoabsolutepath__string-dependentfilepropertytype-string.html language=enus -->
## TOPIC 03973: PathTypePairToAbsolutePath(string, DependentFilePropertyType, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-pathtypepairtoabsolutepath__string-dependentfilepropertytype-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-pathtypepairtoabsolutepath__string-dependentfilepropertytype-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares the path and type parameters and builds an absolute path. If type is Relative, this method appends path to basePath . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string PathTypePairToAbsolutePath(string path, DependentFilePropertyType type, string basePat

### PathTypePairToAbsolutePath(string, DependentFilePropertyType, string)

Compares the *path*  and *type*  parameters and builds an absolute path. If *type*  is [Relative](nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html), this method appends *path*  to *basePath* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string PathTypePairToAbsolutePath(string path, DependentFilePropertyType type, string basePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The path to convert to an absolute path. |
| type | DependentFilePropertyType | The type of path . |
| basePath | string | The base path to append path to if type is Relative. |

#### Returns

The absolute path.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-pathtypepairtoabsolutepath__string-veristand.customdevice.pathtype.html language=enus -->
## TOPIC 03974: PathTypePairToAbsolutePath(string, VeriStand.CustomDevice.PathType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-pathtypepairtoabsolutepath__string-veristand.customdevice.pathtype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-pathtypepairtoabsolutepath__string-veristand.customdevice.pathtype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares the path and type parameters and builds an absolute path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string PathTypePairToAbsolutePath(string path, VeriStand.CustomDevice.PathType type)ParametersNameTypeDescriptionpathstringThe path to convert to an abso

### PathTypePairToAbsolutePath(string, VeriStand.CustomDevice.PathType)

Compares the *path*  and *type*  parameters and builds an absolute path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string PathTypePairToAbsolutePath(string path, VeriStand.CustomDevice.PathType type)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The path to convert to an absolute path. |
| type | VeriStand.CustomDevice.PathType | The type of path . |

#### Returns

The absolute path.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-relativeafpinipath.html language=enus -->
## TOPIC 03975: RelativeAfpIniPath()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-relativeafpinipath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-relativeafpinipath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the relative path to the binary automatic frame processing (.ini) file on a CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string RelativeAfpIniPath()ReturnsThe relative path to the .ini file.

### RelativeAfpIniPath()

Gets the relative path to the binary automatic frame processing (.ini) file on a CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string RelativeAfpIniPath()

#### Returns

The relative path to the .ini file.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-resetallidentifiers__basenodetype.html language=enus -->
## TOPIC 03976: ResetAllIdentifiers(BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-resetallidentifiers__basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-resetallidentifiers__basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the identifiers for the specified BaseNodeType and all its descendants. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static void ResetAllIdentifiers(BaseNodeType baseNodeType)ParametersNameTypeDescriptionbaseNodeTypeBaseNodeTypeThe node to reset identifiers for.

### ResetAllIdentifiers(BaseNodeType)

Resets the identifiers for the specified BaseNodeType and all its descendants.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static void ResetAllIdentifiers(BaseNodeType baseNodeType)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| baseNodeType | BaseNodeType | The node to reset identifiers for. |

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-resolvepathtype__string-ref.html language=enus -->
## TOPIC 03977: ResolvePathType(string, ref string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-resolvepathtype__string-ref.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-resolvepathtype__string-ref.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compares the RootPath and relative FilePath to determine the DependentFileType of the FilePath . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static DependentFileType ResolvePathType(string RootPath, ref string FilePath)ParametersNameTypeDescriptionRootPathstringThe root

### ResolvePathType(string, ref string)

Compares the *RootPath*  and relative *FilePath*  to determine the [DependentFileType](nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html) of the *FilePath* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static [DependentFileType](nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html) ResolvePathType(string RootPath, ref string FilePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| RootPath | string | The root path to which any relative paths are relative. |
| FilePath | ref string | The file path for which to determine the DependentFileType. This path can be relative or absolute. |

#### Returns

An enumeration value of [DependentFileType](nationalinstruments-veristand-systemdefinitionapi-dependentfiletype.html).

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-rtmainpath.html language=enus -->
## TOPIC 03978: RtMainPath()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-rtmainpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-rtmainpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the main destination path for the system definition on the RT target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string RtMainPath()ReturnsThe destination path.

### RtMainPath()

Gets the main destination path for the system definition on the RT target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string RtMainPath()

#### Returns

The destination path.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-serializeslsc__string-out-basenodetype.html language=enus -->
## TOPIC 03979: SerializeSLSC(string, out Error, BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-serializeslsc__string-out-basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-serializeslsc__string-out-basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Serializes one or multiple SLSC Chassis into a given file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static void SerializeSLSC(string filepath, out Error error, BaseNodeType node)ParametersNameTypeDescriptionfilepathstringThe path to the file on disk.errorout ErrorThe

### SerializeSLSC(string, out Error, BaseNodeType)

Serializes one or multiple SLSC Chassis into a given file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static void SerializeSLSC(string filepath, out Error error, BaseNodeType node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filepath | string | The path to the file on disk. |
| error | out Error | The error output string. |
| node | BaseNodeType | The SLSC/SLSCChassis node to serialize. |

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-strippath__string-out.html language=enus -->
## TOPIC 03980: StripPath(string, out string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-strippath__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-strippath__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Strips the last component from the specified path and returns both the component and the stripped path, without the component. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string StripPath(string path, out string relative)ParametersNameTypeDescriptionpathstringThe

### StripPath(string, out string)

Strips the last component from the specified *path*  and returns both the component and the stripped path, without the component.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string StripPath(string path, out string relative)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The path to strip. |
| relative | out string | The stripped path, without the component. |

#### Returns

The last component of *path* .

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-strippath__string.html language=enus -->
## TOPIC 03981: StripPath(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-strippath__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-strippath__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Strips the last component from the specified path . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string StripPath(string path)ParametersNameTypeDescriptionpathstringThe path to strip.ReturnsThe last component of path .

### StripPath(string)

Strips the last component from the specified *path* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string StripPath(string path)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| path | string | The path to strip. |

#### Returns

The last component of *path* .

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-strippathifinllb__string.html language=enus -->
## TOPIC 03982: StripPathIfInLLB(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-strippathifinllb__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-strippathifinllb__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Strips the last component from the specified filePath if the path is to an LLB. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static string StripPathIfInLLB(string filePath)ParametersNameTypeDescriptionfilePathstringThe path to strip.ReturnsIf filePath is to an LLB, the la

### StripPathIfInLLB(string)

Strips the last component from the specified *filePath*  if the path is to an LLB.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static string StripPathIfInLLB(string filePath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The path to strip. |

#### Returns

If *filePath*  is to an LLB, the last component of *filePath* .

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities-versiontypetoversion__systemstorage.versiontype.html language=enus -->
## TOPIC 03983: VersionTypeToVersion(SystemStorage.VersionType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities-versiontypetoversion__systemstorage.versiontype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities-versiontypetoversion__systemstorage.versiontype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts versiontype to a System.Version object. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static Version VersionTypeToVersion(SystemStorage.VersionType versiontype)ParametersNameTypeDescriptionversiontypeSystemStorage.VersionTypeThe version type to convert. Use the Cu

### VersionTypeToVersion(SystemStorage.VersionType)

Converts *versiontype*  to a System.Version object.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static Version VersionTypeToVersion(SystemStorage.VersionType versiontype)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| versiontype | SystemStorage.VersionType | The version type to convert. Use the CurrentVersion property to get this reference. |

#### Returns

A System.Version object.

Parent topic:

Utilities Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-utilities.html language=enus -->
## TOPIC 03984: Utilities Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-utilities.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-utilities.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Class that provides a way to perform various common operations within the system definition, such as stripping paths, converting data types, and creating channel mappings. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class UtilitiesRemarksNot static as it

### Utilities Class

Class that provides a way to perform various common operations within the system definition, such as stripping paths, converting data types, and creating channel mappings.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Utilities

#### Remarks

Not static as it has been that way for 10+ years and we weren't sure of the impact on LV code that might call constructor.

#### Properties

| Name | Description |
| --- | --- |
| CurrentVersion | Gets the current version information for the system definition file. |

#### Methods

| Name | Description |
| --- | --- |
| AddMapping(Channel, Channel) | Adds a channel mapping to the system. The source channel maps to the destination channel, but the destination channel stores the mapping information. This method overwrites any pre-existing mapping information on the destination channel. |
| AfpRtPath() | Gets the path to the binary automatic frame processing (.ini) file on an RT target for which automatic frame processing is enabled. |
| AutoMapChannels(BaseNode, BaseNode) |  |
| AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >) |  |
| AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >, Predicate< IChannel >, Predicate< BaseNode >) | Find name matches between the source and destination channels and maps them If there are multiple names that match in either collection, we will only return the first as a match. This is done to improve performance for large channel count. |
| AutoMapChannels(BaseNode, BaseNode, IEqualityComparer< string >, Predicate< IChannel >) |  |
| BuildPath(string, string) | Creates a new path by appending a name (or relative path) to an existing path. |
| ClearMapping(Channel) | Clears the channel mapping for the specified destination channel. |
| CreateBaseNodeFromSystemStorageNode(BaseNodeType) | Creates a SystemDefinitionAPI BaseNode from a SystemStorage BaseNodeType. |
| DataReplayRTPath() | Gets the path on the RT target to the folder where NI-XNET DataFileReplay files are stored. |
| DateTimeToDouble(DateTime) | Converts the time stamp specified by dateTime to a double-precision, floating-point number. |
| DefaultAutoMapRecursionFilter(BaseNode) | Default recursion filter for automap. |
| DeserializeSLSC(string, out Error, BaseNodeType) | Deserialize SLSC node from file. |
| DoubleToDateTime(double) | Converts the double-precision, floating-point number specified by totalSeconds to a time stamp. |
| FindNameMatches(IEnumerable< IChannel >, IEnumerable< IChannel >, IEqualityComparer< string >) | Find name matches between the source and destination channels. If there are multiple names that match in either collection, we will only return the first as a match. This is done to improve performance for large channel count. |
| GetFilename(string) | Gets the name of the file at the specified path . |
| GetLocalizedNameByGUID(string) | Gets the localized name of the node associated with the specified GUID . |
| PathTypePairToAbsolutePath(string, VeriStand.CustomDevice.PathType) | Compares the path and type parameters and builds an absolute path. |
| PathTypePairToAbsolutePath(string, DependentFilePropertyType, string) | Compares the path and type parameters and builds an absolute path. If type is Relative, this method appends path to basePath . |
| RelativeAfpIniPath() | Gets the relative path to the binary automatic frame processing (.ini) file on a CAN port. |
| ResetAllIdentifiers(BaseNodeType) | Resets the identifiers for the specified BaseNodeType and all its descendants. |
| ResolvePathType(string, ref string) | Compares the RootPath and relative FilePath to determine the DependentFileType of the FilePath . |
| RtMainPath() | Gets the main destination path for the system definition on the RT target. |
| SerializeSLSC(string, out Error, BaseNodeType) | Serializes one or multiple SLSC Chassis into a given file. |
| StripPath(string) | Strips the last component from the specified path . |
| StripPath(string, out string) | Strips the last component from the specified path and returns both the component and the stripped path, without the component. |
| StripPathIfInLLB(string) | Strips the last component from the specified filePath if the path is to an LLB. |
| VersionTypeToVersion(SystemStorage.VersionType) | Converts versiontype to a System.Version object. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-valuesource-channel.html language=enus -->
## TOPIC 03985: Channel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-valuesource-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-valuesource-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The channel that determines the value of another channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic readonly BaseNode Channel

### Channel

The channel that determines the value of another channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public readonly [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Channel

Parent topic:

ValueSource Data Structure

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-valuesource-constant.html language=enus -->
## TOPIC 03986: Constant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-valuesource-constant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-valuesource-constant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The constant that determines the value of a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic readonly double Constant

### Constant

The constant that determines the value of a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public readonly double Constant

Parent topic:

ValueSource Data Structure

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-valuesource-isconstant.html language=enus -->
## TOPIC 03987: isConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-valuesource-isconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-valuesource-isconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a channel value is determined by a constant or by a channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic readonly bool isConstant

### isConstant

Specifies whether a channel value is determined by a constant or by a channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public readonly bool isConstant

Parent topic:

ValueSource Data Structure

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-valuesource-valuesource__basenode.html language=enus -->
## TOPIC 03988: ValueSource(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-valuesource-valuesource__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-valuesource-valuesource__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ValueSource where a channel value determines the source. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ValueSource(BaseNode Channel)ParametersNameTypeDescriptionChannelBaseNodeThe channel that determines the value of another channel.

### ValueSource(BaseNode)

Initializes a new instance of [ValueSource](nationalinstruments-veristand-systemdefinitionapi-valuesource.html) where a channel value determines the source.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ValueSource(BaseNode Channel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Channel | BaseNode | The channel that determines the value of another channel. |

Parent topic:

ValueSource Data Structure

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-valuesource-valuesource__double.html language=enus -->
## TOPIC 03989: ValueSource(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-valuesource-valuesource__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-valuesource-valuesource__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of ValueSource where a constant value determines the source. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ValueSource(double Constant)ParametersNameTypeDescriptionConstantdoubleThe constant that determines the value of a channel.

### ValueSource(double)

Initializes a new instance of [ValueSource](nationalinstruments-veristand-systemdefinitionapi-valuesource.html) where a constant value determines the source.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ValueSource(double Constant)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Constant | double | The constant that determines the value of a channel. |

Parent topic:

ValueSource Data Structure

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-valuesource.html language=enus -->
## TOPIC 03990: ValueSource Data Structure

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-valuesource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-valuesource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the source of a channel value as a constant or a channel. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic struct ValueSourceRemarksAccessing this StructureValueSource Constructor Thread SafetyAny members of this type are not guaranteed to be thread

### ValueSource Data Structure

Represents the source of a channel value as a constant or a channel.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public struct ValueSource

#### Remarks

**Accessing this Structure**

- ValueSource Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| ValueSource(BaseNode) | Initializes a new instance of ValueSource where a channel value determines the source. |
| ValueSource(double) | Initializes a new instance of ValueSource where a constant value determines the source. |

#### Fields

| Name | Description |
| --- | --- |
| Channel | The channel that determines the value of another channel. |
| Constant | The constant that determines the value of a channel. |
| isConstant | Specifies whether a channel value is determined by a constant or by a channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-variant-data.html language=enus -->
## TOPIC 03991: Data

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-variant-data.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-variant-data.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The data bytes of the variant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic byte[] Data { get; set; }

### Data

The data bytes of the variant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public byte[] Data { get; set; }

Parent topic:

Variant Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-variant-type.html language=enus -->
## TOPIC 03992: Type

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-variant-type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-variant-type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The type descriptor of the variant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic byte[] Type { get; set; }

### Type

The type descriptor of the variant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public byte[] Type { get; set; }

Parent topic:

Variant Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-variant-variant__byte_arr1-byte_arr1.html language=enus -->
## TOPIC 03993: Variant(byte[], byte[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-variant-variant__byte_arr1-byte_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-variant-variant__byte_arr1-byte_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the Variant with the specified type and value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Variant(byte[] type, byte[] data)ParametersNameTypeDescriptiontypebyte[]The type descriptor of the variant value.databyte[]The data bytes of the varia

### Variant(byte[], byte[])

Initializes a new instance of the [Variant](nationalinstruments-veristand-systemdefinitionapi-variant.html) with the specified type and value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Variant(byte[] type, byte[] data)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| type | byte[] | The type descriptor of the variant value. |
| data | byte[] | The data bytes of the variant value. |

Parent topic:

Variant Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-variant.html language=enus -->
## TOPIC 03994: Variant Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-variant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-variant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a variant value that encapsulates the type descriptor and data bytes. Derives fromNoneSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class VariantConstructorsNameDescriptionVariant(byte[], byte[])Initializes a new instance of the Variant with the specified type a

### Variant Class

Represents a variant value that encapsulates the type descriptor and data bytes.

#### Derives from

None

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Variant

#### Constructors

| Name | Description |
| --- | --- |
| Variant(byte[], byte[]) | Initializes a new instance of the Variant with the specified type and value. |

#### Properties

| Name | Description |
| --- | --- |
| Data | The data bytes of the variant value. |
| Type | The type descriptor of the variant value. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-bool.html language=enus -->
## TOPIC 03995: VirtualECU(string, string, string, int, int, ushort, bool, bool, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of VirtualECU. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic VirtualECU(string name, string description, string virtualECUPath, int processor, int decimation, ushort initialState, bool segmentVectors, bool importParameters, bool importSignals)Par

### VirtualECU(string, string, string, int, int, ushort, bool, bool, bool)

Initializes a new instance of [VirtualECU](nationalinstruments-veristand-systemdefinitionapi-virtualecu.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public VirtualECU(string name, string description, string virtualECUPath, int processor, int decimation, ushort initialState, bool segmentVectors, bool importParameters, bool importSignals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the virtual ECU. |
| description | string | The description of the virtual ECU. |
| virtualECUPath | string | The path to the virtual ECU. |
| processor | int | The processor on which the virtual ECU runs. |
| decimation | int | The decimation of the virtual ECU. |
| initialState | ushort | The initial execution state of the virtual ECU. 0: Running. 1: Paused. |
| segmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the virtual ECU is loaded. |
| importParameters | bool | true to import parameters. |
| importSignals | bool | true to import signals. |

Parent topic:

VirtualECU Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool.html language=enus -->
## TOPIC 03996: VirtualECU(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-string-bool-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of VirtualECU and filters the imported parameters and signals according to the conditions you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic VirtualECU(string name, string description, string virtualECUPath, int processor, int decimation,

### VirtualECU(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool)

Initializes a new instance of [VirtualECU](nationalinstruments-veristand-systemdefinitionapi-virtualecu.html) and filters the imported parameters and signals according to the conditions you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public VirtualECU(string name, string description, string virtualECUPath, int processor, int decimation, ushort initialState, bool segmentVectors, bool importParameters, string parameterRegularExpression, bool importSignals, string signalRegularExpression, bool importOnlyNamedSignals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the virtual ECU. |
| description | string | The description of the virtual ECU. |
| virtualECUPath | string | The path to the virtual ECU. |
| processor | int | The processor on which the virtual ECU runs. |
| decimation | int | The decimation of the virtual ECU. |
| initialState | ushort | The initial execution state of the virtual ECU. 0: Running. 1: Paused. |
| segmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the virtual ECU is loaded. |
| importParameters | bool | true to import parameters. |
| parameterRegularExpression | string | The regular expression to use to filter parameters. Parameters that match the regular expression are imported. |
| importSignals | bool | true to import signals. |
| signalRegularExpression | string | The regular expression to use to filter signals. Signals that match the regular expression are imported. |
| importOnlyNamedSignals | bool | true to import only named signals. |

Parent topic:

VirtualECU Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-string-globalparameterscopes-bool-string-bool.html language=enus -->
## TOPIC 03997: VirtualECU(string, string, string, int, int, ushort, bool, bool, string, GlobalParameterScopes, bool, string, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-string-globalparameterscopes-bool-string-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-virtualecu-virtualecu__string-string-string-int-int-ushort-bool-bool-string-globalparameterscopes-bool-string-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of VirtualECU and filters the imported parameters and signals according to the conditions you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic VirtualECU(string name, string description, string virtualECUPath, int processor, int decimation,

### VirtualECU(string, string, string, int, int, ushort, bool, bool, string, GlobalParameterScopes, bool, string, bool)

Initializes a new instance of [VirtualECU](nationalinstruments-veristand-systemdefinitionapi-virtualecu.html) and filters the imported parameters and signals according to the conditions you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public VirtualECU(string name, string description, string virtualECUPath, int processor, int decimation, ushort initialState, bool segmentVectors, bool importParameters, string parameterRegularExpression, GlobalParameterScopes globalParameterScope, bool importSignals, string signalRegularExpression, bool importOnlyNamedSignals)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| name | string | The name of the virtual ECU. |
| description | string | The description of the virtual ECU. |
| virtualECUPath | string | The path to the virtual ECU. |
| processor | int | The processor on which the virtual ECU runs. |
| decimation | int | The decimation of the virtual ECU. |
| initialState | ushort | The initial execution state of the virtual ECU. 0: Running. 1: Paused. |
| segmentVectors | bool | true to split up vector inputs, outputs, parameters, and signals into scalar channels when the virtual ECU is loaded. |
| importParameters | bool | true to import parameters. |
| parameterRegularExpression | string | The regular expression to use to filter parameters. Parameters that match the regular expression are imported. |
| globalParameterScope | GlobalParameterScopes | The scope of the global parameters. They can be either target or virtual ECU scoped. |
| importSignals | bool | true to import signals. |
| signalRegularExpression | string | The regular expression to use to filter signals. Signals that match the regular expression are imported. |
| importOnlyNamedSignals | bool | true to import only named signals. |

Parent topic:

VirtualECU Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-virtualecu.html language=enus -->
## TOPIC 03998: VirtualECU Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-virtualecu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-virtualecu.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a virtual ECU as a specialized type of Model and inherits all the capabilities of Model. Virtual ECUs within the same network cluster are automatically connected to each other and to real ECUs via an XNET interface. Derives fromModelSyntaxNamespace: NationalInstruments.VeriStand.SystemDef

### VirtualECU Class

Represents a virtual ECU as a specialized type of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html) and inherits all the capabilities of [Model](nationalinstruments-veristand-systemdefinitionapi-model.html). Virtual ECUs within the same network cluster are automatically connected to each other and to real ECUs via an XNET interface.

#### Derives from

- Model

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class VirtualECU : Model

#### Remarks

Use the members of this class to retrieve information about, set the decimation for, or reload a virtual ECU. Refer to [ECUNetworkCluster](nationalinstruments-veristand-systemdefinitionapi-ecunetworkcluster.html) to configure an ECU network cluster.

#### Constructors

| Name | Description |
| --- | --- |
| VirtualECU(string, string, string, int, int, ushort, bool, bool, string, GlobalParameterScopes, bool, string, bool) | Initializes a new instance of VirtualECU and filters the imported parameters and signals according to the conditions you specify. |
| VirtualECU(string, string, string, int, int, ushort, bool, bool, string, bool, string, bool) | Initializes a new instance of VirtualECU and filters the imported parameters and signals according to the conditions you specify. |
| VirtualECU(string, string, string, int, int, ushort, bool, bool, bool) | Initializes a new instance of VirtualECU. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html language=enus -->
## TOPIC 03999: VirtualECUToolchain Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-virtualecutoolchain.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Toolchain that was used to build virtual ECUs. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum VirtualECUToolchainMembersNameValueDescriptionSilver0Silver®, virtual ECU platform from Synopsys®.

### VirtualECUToolchain Enumeration

Toolchain that was used to build virtual ECUs.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum VirtualECUToolchain

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Silver | 0 | Silver®, virtual ECU platform from Synopsys®. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-waveform-datatype.html language=enus -->
## TOPIC 04000: DataType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-waveform-datatype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-waveform-datatype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the data type associated with the waveform. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic WaveformTypeDataType DataType { get; set; }ReturnsThe data type.

### DataType

Gets or sets the data type associated with the waveform.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public WaveformTypeDataType DataType { get; set; }

#### Returns

The data type.

Parent topic:

Waveform Class
