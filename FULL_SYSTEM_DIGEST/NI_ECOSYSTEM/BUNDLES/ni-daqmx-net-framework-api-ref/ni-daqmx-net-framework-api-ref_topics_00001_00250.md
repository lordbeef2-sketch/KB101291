# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancecompleteeventpulsepolarity.html language=enus -->
## TOPIC 00001: AdvanceCompleteEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancecompleteeventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancecompleteeventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of the exported Advance Complete Event. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AdvanceCompleteEventPulsePolarityRemarksSpecifies the polarity of the exported Advance Complete Event. Use this enumeration to get or set the value of AdvanceCompleteEventPulsePolarit

### AdvanceCompleteEventPulsePolarity Enumeration

Specifies the polarity of the exported Advance Complete Event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AdvanceCompleteEventPulsePolarity

#### Remarks

Specifies the polarity of the exported Advance Complete Event. Use this enumeration to get or set the value of [AdvanceCompleteEventPulsePolarity](nationalinstruments-daqmx-exportsignals-advancecompleteeventpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger-configuredigitaledgetrigger__string-digitaledgeadvancetriggeredge.html language=enus -->
## TOPIC 00002: ConfigureDigitalEdgeTrigger(string, DigitalEdgeAdvanceTriggerEdge)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger-configuredigitaledgetrigger__string-digitaledgeadvancetriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger-configuredigitaledgetrigger__string-digitaledgeadvancetriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a task to advance to the next entry in a scan list upon a rising or falling edge of a digital signal. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeAdvanceTriggerEdge edge)RemarksThe NI-DAQmx driver does not determine if the re

### ConfigureDigitalEdgeTrigger(string, DigitalEdgeAdvanceTriggerEdge)

Configures a task to advance to the next entry in a scan list upon a [rising or falling edge of a digital signal](/csh?context=nidaqmx_mxcncpts_digtrigger).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeAdvanceTriggerEdge edge)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalEdgeTrigger(string, DigitalEdgeAdvanceTriggerEdge) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The terminal of the trigger signal. |
| edge | DigitalEdgeAdvanceTriggerEdge | The edge of the trigger signal that causes an advance trigger to occur. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger-configurenone.html language=enus -->
## TOPIC 00003: ConfigureNone()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger-configurenone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger-configurenone.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables advance triggering for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureNone()RemarksThe NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does not throw an exception for parameter values that are not

### ConfigureNone()

Disables [advance triggering](/csh?context=nidaqmx_mxcncpts_adtrig) for the task.

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

AdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger-configuresoftwaretrigger.html language=enus -->
## TOPIC 00004: ConfigureSoftwareTrigger()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger-configuresoftwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger-configuresoftwaretrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a task to advance to the next entry in a scan list upon a software trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureSoftwareTrigger()RemarksThe NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureSoftwareTri

### ConfigureSoftwareTrigger()

Configures a task to advance to the next entry in a scan list upon a software trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureSoftwareTrigger()

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureSoftwareTrigger does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

Parent topic:

AdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger-digitaledge.html language=enus -->
## TOPIC 00005: DigitalEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger-digitaledge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalEdgeAdvanceTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeAdvanceTrigger DigitalEdge { get; }RemarksThe DigitalEdgeAdvanceTrigger.

### DigitalEdge

Gets the [DigitalEdgeAdvanceTrigger](nationalinstruments-daqmx-digitaledgeadvancetrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeAdvanceTrigger](nationalinstruments-daqmx-digitaledgeadvancetrigger.html) DigitalEdge { get; }

#### Remarks

The [DigitalEdgeAdvanceTrigger](nationalinstruments-daqmx-digitaledgeadvancetrigger.html).

Parent topic:

AdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger-sendsoftwaretrigger.html language=enus -->
## TOPIC 00006: SendSoftwareTrigger()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger-sendsoftwaretrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger-sendsoftwaretrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a notification to the hardware from the running program to advance to the next entry in the switch scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic void SendSoftwareTrigger()ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SendSoftwareTrigger()

Sends a notification to the hardware from the running program to advance to the next entry in the switch scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void SendSoftwareTrigger()

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger-tostring.html language=enus -->
## TOPIC 00007: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger-tostring.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string representation of the object. SyntaxNamespace: NationalInstruments.DAQmxpublic override string ToString()RemarksOverrides ToString.ReturnsA string representation of the object.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

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

AdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger-type.html language=enus -->
## TOPIC 00008: Type

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger-type.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This property is obsolete. Will warn if used (Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic AdvanceTriggerType Type { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExc

### Type

**Obsolete: This property is obsolete. Will warn if used** 
(Deprecated) Specifies the [type](/csh?context=nidaqmx_mxcncpts_analogtriggering) of trigger to use to advance to the next entry in a switch scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AdvanceTriggerType](nationalinstruments-daqmx-advancetriggertype.html) Type { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AdvanceTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetrigger.html language=enus -->
## TOPIC 00009: AdvanceTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods that configure how the switch task advances to the next entry in the scan list and causes the switch to advance programmatically. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AdvanceTrigger : MarshalByRefO

### AdvanceTrigger Class

Contains properties and methods that configure how the [switch task advances to the next entry in the scan list](/csh?context=nidaqmx_mxcncpts_adtrig) and causes the switch to advance programmatically.

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AdvanceTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DigitalEdgeAdvanceTrigger. |
| Type | Obsolete: This property is obsolete. Will warn if used(Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureDigitalEdgeTrigger(string, DigitalEdgeAdvanceTriggerEdge) | Configures a task to advance to the next entry in a scan list upon a rising or falling edge of a digital signal. |
| ConfigureNone() | Disables advance triggering for the task. |
| ConfigureSoftwareTrigger() | Configures a task to advance to the next entry in a scan list upon a software trigger. |
| SendSoftwareTrigger() | Sends a notification to the hardware from the running program to advance to the next entry in the switch scan list. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Triggers
- AdvanceTrigger

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetriggerpulsepolarity.html language=enus -->
## TOPIC 00010: AdvanceTriggerPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetriggerpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetriggerpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the polarity of the exported Advance Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AdvanceTriggerPulsePolarityRemarksIndicates the polarity of the exported Advance Trigger. Use this enumeration to get or set the value of AdvanceTriggerPulsePolarity.MembersNameValueDescript

### AdvanceTriggerPulsePolarity Enumeration

Indicates the polarity of the exported Advance Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AdvanceTriggerPulsePolarity

#### Remarks

Indicates the polarity of the exported Advance Trigger. Use this enumeration to get or set the value of [AdvanceTriggerPulsePolarity](nationalinstruments-daqmx-exportsignals-advancetriggerpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetriggerpulsewidthunits.html language=enus -->
## TOPIC 00011: AdvanceTriggerPulseWidthUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetriggerpulsewidthunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetriggerpulsewidthunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AdvanceTriggerPulseWidth. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AdvanceTriggerPulseWidthUnitsRemarksSpecifies the units of AdvanceTriggerPulseWidth. Use this enumeration to get or set the value of AdvanceTriggerPulseWidthUnits.MembersNameValueDescriptionSeconds

### AdvanceTriggerPulseWidthUnits Enumeration

Specifies the units of [AdvanceTriggerPulseWidth](nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidth.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AdvanceTriggerPulseWidthUnits

#### Remarks

Specifies the units of [AdvanceTriggerPulseWidth](nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidth.html). Use this enumeration to get or set the value of [AdvanceTriggerPulseWidthUnits](nationalinstruments-daqmx-exportsignals-advancetriggerpulsewidthunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 10364 | Seconds. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-advancetriggertype.html language=enus -->
## TOPIC 00012: AdvanceTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-advancetriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-advancetriggertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Obsolete: This enum is obsolete. Will warn if used (Deprecated) Specifies the type of trigger to use to advance to the next entry in a switch scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AdvanceTriggerTypeRemarks(Deprecated) Specifies the type of trigger to use to advance to the

### AdvanceTriggerType Enumeration

**Obsolete: This enum is obsolete. Will warn if used** 
(Deprecated) Specifies the [type](/csh?context=nidaqmx_mxcncpts_analogtriggering) of trigger to use to advance to the next entry in a switch scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AdvanceTriggerType

#### Remarks

(Deprecated) Specifies the [type](/csh?context=nidaqmx_mxcncpts_analogtriggering) of trigger to use to advance to the next entry in a switch scan list. Use this enumeration to get or set the value of [Type](nationalinstruments-daqmx-advancetrigger-type.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DigitalEdge | 10150 | Advance to the next entry in a scan list on the rising or falling edge of a digital signal. |
| Software | 10292 | Advance to the next entry in a scan list when you call sending a software trigger. |
| None | 10230 | Advance through all entries in the scan list as fast as possible. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiaccelerationchargesensitivityunits.html language=enus -->
## TOPIC 00013: AIAccelerationChargeSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiaccelerationchargesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiaccelerationchargesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AI.Accel.Charge.Sensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIAccelerationChargeSensitivityUnitsRemarksSpecifies the units of AI.Accel.Charge.Sensitivity. Use this enumeration to get or set the value of AccelerationChargeSensitivityUnits.MembersNameValue

### AIAccelerationChargeSensitivityUnits Enumeration

Specifies the units of AI.Accel.Charge.Sensitivity.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIAccelerationChargeSensitivityUnits

#### Remarks

Specifies the units of AI.Accel.Charge.Sensitivity. Use this enumeration to get or set the value of [AccelerationChargeSensitivityUnits](nationalinstruments-daqmx-aichannel-accelerationchargesensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| PicoCoulombsPerG | 16099 | PicoCoulombs per g. |
| PicoCoulombsPerMetersPerSecondSquared | 16100 | PicoCoulombs per m/s^2. |
| PicoCoulombsPerInchesPerSecondSquared | 16101 | PicoCoulombs per in/s^2. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiaccelerationfourwiredcvoltagesensitivityunits.html language=enus -->
## TOPIC 00014: AIAccelerationFourWireDCVoltageSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiaccelerationfourwiredcvoltagesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiaccelerationfourwiredcvoltagesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIAccelerationFourWireDCVoltageSensitivityUnitsRemarksSpecifies the units of AI.Accel.4WireDCVoltage.Sensitivity. Use this enumeration to get or set the value of AccelerationFourWireDCVo

### AIAccelerationFourWireDCVoltageSensitivityUnits Enumeration

Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIAccelerationFourWireDCVoltageSensitivityUnits

#### Remarks

Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity. Use this enumeration to get or set the value of [AccelerationFourWireDCVoltageSensitivityUnits](nationalinstruments-daqmx-aichannel-accelerationfourwiredcvoltagesensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MillivoltsPerG | 12509 | mVolts/g. |
| VoltsPerG | 12510 | Volts/g. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiaccelerationunits.html language=enus -->
## TOPIC 00015: AIAccelerationUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiaccelerationunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiaccelerationunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return acceleration measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIAccelerationUnitsRemarksSpecifies the units to use to return acceleration measurements from the channel. Use this enumeration to get or set the value of Accelerati

### AIAccelerationUnits Enumeration

Specifies the units to use to return acceleration measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIAccelerationUnits

#### Remarks

Specifies the units to use to return acceleration measurements from the channel. Use this enumeration to get or set the value of [AccelerationUnits](nationalinstruments-daqmx-aichannel-accelerationunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| G | 10186 | 1 g is approximately equal to 9.81 m/s/s. |
| MetersPerSecondSquared | 12470 | Meters per second per second. |
| InchesPerSecondSquared | 12471 | Inches per second per second. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiaccelerometersensitivityunits.html language=enus -->
## TOPIC 00016: AIAccelerometerSensitivityUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiaccelerometersensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiaccelerometersensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AccelerometerSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIAccelerometerSensitivityUnitsRemarksSpecifies the units of AccelerometerSensitivity. Use this enumeration to get or set the value of AccelerometerSensitivityUnits.MembersNameValueDescriptionMilli

### AIAccelerometerSensitivityUnits Enumeration

Specifies the units of [AccelerometerSensitivity](nationalinstruments-daqmx-aichannel-accelerometersensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIAccelerometerSensitivityUnits

#### Remarks

Specifies the units of [AccelerometerSensitivity](nationalinstruments-daqmx-aichannel-accelerometersensitivity.html). Use this enumeration to get or set the value of [AccelerometerSensitivityUnits](nationalinstruments-daqmx-aichannel-accelerometersensitivityunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| MillivoltsPerG | 12509 | mVolts/g. |
| VoltsPerG | 12510 | Volts/g. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiacexcitationwiremode.html language=enus -->
## TOPIC 00017: AIACExcitationWireMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiacexcitationwiremode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiacexcitationwiremode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIACExcitationWireModeRemarksSpecifies the number of

### AIACExcitationWireMode Enumeration

Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIACExcitationWireMode

#### Remarks

Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information. Use this enumeration to get or set the value of [ACExcitationWireMode](nationalinstruments-daqmx-aichannel-acexcitationwiremode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FourWire | 4 | 4-wire. |
| FiveWire | 5 | 5-wire. |
| SixWire | 6 | 6-wire. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiadctimingmode.html language=enus -->
## TOPIC 00018: AIAdcTimingMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiadctimingmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiadctimingmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ADC timing mode, controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for AIConvertRate. You must use the sa

### AIAdcTimingMode Enumeration

Specifies the [ADC timing mode](/csh?context=nidaqmx_mxdevconsid_configadctiming), controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for [AIConvertRate](nationalinstruments-daqmx-timing-aiconvertrate.html). You must use the same ADC timing mode for all channels on a device, but you can use different ADC timing modes for different devices in the same task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIAdcTimingMode

#### Remarks

Specifies the [ADC timing mode](/csh?context=nidaqmx_mxdevconsid_configadctiming), controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for [AIConvertRate](nationalinstruments-daqmx-timing-aiconvertrate.html). You must use the same ADC timing mode for all channels on a device, but you can use different ADC timing modes for different devices in the same task. Use this enumeration to get or set the value of [AdcTimingMode](nationalinstruments-daqmx-aichannel-adctimingmode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Automatic | 16097 | Uses the most appropriate supported timing mode based on the Sample Clock Rate. |
| HighResolution | 10195 | Increases resolution and noise rejection while decreasing conversion rate. |
| HighSpeed | 14712 | Increases conversion rate while decreasing resolution. |
| Best50HzRejection | 14713 | Improves 50 Hz noise rejection while decreasing noise rejection at other frequencies. |
| Best60HzRejection | 14714 | Improves 60 Hz noise rejection while decreasing noise rejection at other frequencies. |
| Custom | 10137 | Use AdcCustomTimingMode to specify a custom value controlling the tradeoff between speed and resolution. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aiautozeromode.html language=enus -->
## TOPIC 00019: AIAutoZeroMode Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aiautozeromode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aiautozeromode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIAutoZeroModeRemarksSpecifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample. Use this enumer

### AIAutoZeroMode Enumeration

Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIAutoZeroMode

#### Remarks

Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample. Use this enumeration to get or set the value of [AutoZeroMode](nationalinstruments-daqmx-aichannel-autozeromode.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 10230 | Do not perform an autozero. |
| Once | 10244 | Perform an auto zero at the beginning of the acquisition. This auto zero task might not run if you have used DAQmx Control Task previously in your task. |
| EverySample | 10164 | Perform an auto zero at every sample of the acquisition. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aibridgeconfiguration.html language=enus -->
## TOPIC 00020: AIBridgeConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aibridgeconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aibridgeconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of Wheatstone bridge connected to the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIBridgeConfigurationRemarksSpecifies the type of Wheatstone bridge connected to the channel. Use this enumeration to get or set the value of BridgeConfiguration.MembersNameValueDe

### AIBridgeConfiguration Enumeration

Specifies the type of Wheatstone bridge connected to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIBridgeConfiguration

#### Remarks

Specifies the type of Wheatstone bridge connected to the channel. Use this enumeration to get or set the value of [BridgeConfiguration](nationalinstruments-daqmx-aichannel-bridgeconfiguration.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FullBridge | 10182 | Sensor is a full bridge. If you set UseExcitationForScaling to true, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
| HalfBridge | 10187 | Sensor is a half bridge. If you set UseExcitationForScaling to true, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
| QuarterBridge | 10270 | Sensor is a quarter bridge. If you set UseExcitationForScaling to true, NI-DAQmx divides the measurement by the excitation value. Many sensors scale data to native units using scaling of volts per excitation. |
| NoBridge | 10228 | Sensor is not a Wheatstone bridge. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aibridgeconfiguration11637.html language=enus -->
## TOPIC 00021: AIBridgeConfiguration11637 Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aibridgeconfiguration11637.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aibridgeconfiguration11637.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of Wheatstone bridge connected to the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIBridgeConfiguration11637MembersNameValueDescriptionFullBridge10182Sensor connected to the FD-11637 is a full bridge. HalfBridge10187Sensor connected to the FD-11637 is a half bri

### AIBridgeConfiguration11637 Enumeration

Specifies the type of Wheatstone bridge connected to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIBridgeConfiguration11637

#### Members

| Name | Value | Description |
| --- | --- | --- |
| FullBridge | 10182 | Sensor connected to the FD-11637 is a full bridge. |
| HalfBridge | 10187 | Sensor connected to the FD-11637 is a half bridge. |
| QuarterBridge350OhmCompletionResistor | 16164 | Sensor connected to the FD-11637 is a quarter bridge with the resistance of 350 Ohms. |
| QuarterBridge120OhmCompletionResistor | 16163 | Sensor connected to the FD-11637 is a quarter bridge with the resistance of 120 Ohms. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aibridgeelectricalunits.html language=enus -->
## TOPIC 00022: AIBridgeElectricalUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aibridgeelectricalunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aibridgeelectricalunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIBridgeElectricalUnitsRemarksSpecifies from which electrical unit to scale data. Select th

### AIBridgeElectricalUnits Enumeration

Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIBridgeElectricalUnits

#### Remarks

Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. Use this enumeration to get or set the value of [BridgeElectricalUnits](nationalinstruments-daqmx-aichannel-bridgeelectricalunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| VoltsPerVolt | 15896 | Volts per volt. |
| MillivoltsPerVolt | 15897 | Millivolts per volt. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aibridgephysicalunits.html language=enus -->
## TOPIC 00023: AIBridgePhysicalUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aibridgephysicalunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aibridgephysicalunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIBridgePhysicalUnitsRemarksSpecifies to which physical unit to scale electrical data.

### AIBridgePhysicalUnits Enumeration

Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIBridgePhysicalUnits

#### Remarks

Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. Use this enumeration to get or set the value of [BridgePhysicalUnits](nationalinstruments-daqmx-aichannel-bridgephysicalunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Newtons | 15875 | Newtons. |
| Pounds | 15876 | Pounds. |
| KilogramForce | 15877 | kilograms-force. |
| Pascals | 10081 | Pascals. |
| PoundsPerSquareInch | 15879 | Pounds per square inch. |
| Bar | 15880 | Bar. |
| NewtonMeters | 15881 | Newton metres. |
| InchOunces | 15882 | Ounce-inches. |
| InchPounds | 15883 | Pound-inches. |
| FootPounds | 15884 | Pound-feet. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aibridgescaletype.html language=enus -->
## TOPIC 00024: AIBridgeScaleType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aibridgescaletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aibridgescaletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the scaling type to use when scaling electrical values from the sensor to physical units. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIBridgeScaleTypeRemarksSpecifies the scaling type to use when scaling electrical values from the sensor to physical units. Use this enumeration t

### AIBridgeScaleType Enumeration

Specifies the [scaling type](/csh?context=nidaqmx_measfunds_bridgescalingtypes) to use when scaling electrical values from the sensor to physical units.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIBridgeScaleType

#### Remarks

Specifies the [scaling type](/csh?context=nidaqmx_measfunds_bridgescalingtypes) to use when scaling electrical values from the sensor to physical units. Use this enumeration to get or set the value of [BridgeScaleType](nationalinstruments-daqmx-aichannel-bridgescaletype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| None | 10230 | Do not scale electrical values to physical units. |
| TwoPointLinear | 15898 | You provide two pairs of electrical values and their corresponding physical values. NI-DAQmx uses those values to calculate the slope and y-intercept of a linear equation and uses that equation to scale electrical values to physical values. |
| Table | 10450 | Map an array of electrical values to an array of corresponding physical values, with all other values scaled proportionally. If you specify this scaling type, Maximum and Minimum must be within the smallest and largest physical values. For any data outside those endpoints, NI-DAQmx coerces that data to the endpoints. |
| Polynomial | 10449 | Scale values by using an Nth order polynomial equation. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aibridgeshuntcalibrationselect.html language=enus -->
## TOPIC 00025: AIBridgeShuntCalibrationSelect Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aibridgeshuntcalibrationselect.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aibridgeshuntcalibrationselect.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which shunt calibration switch(es) to enable. Use BridgeShuntCalibrationEnable to enable the switch(es) you specify with this property. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIBridgeShuntCalibrationSelectRemarksSpecifies which shunt calibration switch(es) to enable. Use Bri

### AIBridgeShuntCalibrationSelect Enumeration

Specifies which shunt calibration switch(es) to enable. Use [BridgeShuntCalibrationEnable](nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationenable.html) to enable the switch(es) you specify with this property.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIBridgeShuntCalibrationSelect

#### Remarks

Specifies which shunt calibration switch(es) to enable. Use [BridgeShuntCalibrationEnable](nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationenable.html) to enable the switch(es) you specify with this property. Use this enumeration to get or set the value of [BridgeShuntCalibrationSelect](nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationselect.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| A | 12513 | Switch A. |
| B | 12514 | Switch B. |
| AAndB | 12515 | Switches A and B. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aibridgeunits.html language=enus -->
## TOPIC 00026: AIBridgeUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aibridgeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aibridgeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return voltage ratios from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AIBridgeUnitsRemarksSpecifies in which unit to return voltage ratios from the channel. Use this enumeration to get or set the value of BridgeUnits.MembersNameValueDescriptionVolts

### AIBridgeUnits Enumeration

Specifies in which unit to return [voltage ratios](/csh?context=nidaqmx_measfunds_bridgescaling) from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AIBridgeUnits

#### Remarks

Specifies in which unit to return [voltage ratios](/csh?context=nidaqmx_measfunds_bridgescaling) from the channel. Use this enumeration to get or set the value of [BridgeUnits](nationalinstruments-daqmx-aichannel-bridgeunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| VoltsPerVolt | 15896 | Volts per volt. |
| MillivoltsPerVolt | 15897 | Millivolts per volt. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |
| FromTeds | 12516 | Units defined by TEDS information associated with the channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerationchargesensitivity.html language=enus -->
## TOPIC 00027: AccelerationChargeSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerationchargesensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerationchargesensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the charge acceleration sensor connected to the channel. This value is the units you specify with AI.Accel.Charge.SensitivityUnits. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double AccelerationChargeSensit

### AccelerationChargeSensitivity

Specifies the sensitivity of the charge acceleration sensor connected to the channel. This value is the units you specify with AI.Accel.Charge.SensitivityUnits. Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AccelerationChargeSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerationchargesensitivityunits.html language=enus -->
## TOPIC 00028: AccelerationChargeSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerationchargesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerationchargesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AI.Accel.Charge.Sensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AIAccelerationChargeSensitivityUnits AccelerationChargeSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AccelerationChargeSensitivityUnits

Specifies the units of AI.Accel.Charge.Sensitivity.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIAccelerationChargeSensitivityUnits](nationalinstruments-daqmx-aiaccelerationchargesensitivityunits.html) AccelerationChargeSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerationdecibelreference.html language=enus -->
## TOPIC 00029: AccelerationDecibelReference

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerationdecibelreference.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerationdecibelreference.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. SyntaxNamespace: NationalInstruments.DAQmxpublic double AccelerationDecibelReference { get; set; }ExceptionsTypeDescriptionNatio

### AccelerationDecibelReference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AccelerationDecibelReference { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerationfourwiredcvoltagesensitivity.html language=enus -->
## TOPIC 00030: AccelerationFourWireDCVoltageSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerationfourwiredcvoltagesensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerationfourwiredcvoltagesensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the 4 wire DC voltage acceleration sensor connected to the channel. This value is the units you specify with AI.Accel.4WireDCVoltage.SensitivityUnits. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double Accel

### AccelerationFourWireDCVoltageSensitivity

Specifies the sensitivity of the 4 wire DC voltage acceleration sensor connected to the channel. This value is the units you specify with AI.Accel.4WireDCVoltage.SensitivityUnits. Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AccelerationFourWireDCVoltageSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerationfourwiredcvoltagesensitivityunits.html language=enus -->
## TOPIC 00031: AccelerationFourWireDCVoltageSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerationfourwiredcvoltagesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerationfourwiredcvoltagesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AIAccelerationFourWireDCVoltageSensitivityUnits AccelerationFourWireDCVoltageSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver r

### AccelerationFourWireDCVoltageSensitivityUnits

Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIAccelerationFourWireDCVoltageSensitivityUnits](nationalinstruments-daqmx-aiaccelerationfourwiredcvoltagesensitivityunits.html) AccelerationFourWireDCVoltageSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerationunits.html language=enus -->
## TOPIC 00032: AccelerationUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerationunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerationunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return acceleration measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIAccelerationUnits AccelerationUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AccelerationUnits

Specifies the units to use to return acceleration measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIAccelerationUnits](nationalinstruments-daqmx-aiaccelerationunits.html) AccelerationUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerometersensitivity.html language=enus -->
## TOPIC 00033: AccelerometerSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerometersensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerometersensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the accelerometer. This value is in the units you specify with AccelerometerSensitivityUnits. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double AccelerometerSensitivity { get; set; }ExceptionsTypeDescriptio

### AccelerometerSensitivity

Specifies the sensitivity of the [accelerometer](/csh?context=nidaqmx_measfunds_accelerometers). This value is in the units you specify with [AccelerometerSensitivityUnits](nationalinstruments-daqmx-aichannel-accelerometersensitivityunits.html). Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AccelerometerSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-accelerometersensitivityunits.html language=enus -->
## TOPIC 00034: AccelerometerSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-accelerometersensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-accelerometersensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of AccelerometerSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AIAccelerometerSensitivityUnits AccelerometerSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AccelerometerSensitivityUnits

Specifies the units of [AccelerometerSensitivity](nationalinstruments-daqmx-aichannel-accelerometersensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIAccelerometerSensitivityUnits](nationalinstruments-daqmx-aiaccelerometersensitivityunits.html) AccelerometerSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-acexcitationfrequency.html language=enus -->
## TOPIC 00035: ACExcitationFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-acexcitationfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-acexcitationfrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the AC excitation frequency in Hertz. SyntaxNamespace: NationalInstruments.DAQmxpublic double ACExcitationFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ACExcitationFrequency

Specifies the AC excitation frequency in Hertz.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ACExcitationFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-acexcitationsyncenable.html language=enus -->
## TOPIC 00036: ACExcitationSyncEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-acexcitationsyncenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-acexcitationsyncenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize the AC excitation source of the channel to that of another channel. Synchronize the excitation sources of multiple channels to use multichannel sensors. Set this property to false for the master channel and to true for the slave channels. SyntaxNamespace: NationalIns

### ACExcitationSyncEnable

Specifies whether to synchronize the AC excitation source of the channel to that of another channel. Synchronize the excitation sources of multiple channels to use multichannel sensors. Set this property to false for the master channel and to true for the slave channels.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ACExcitationSyncEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-acexcitationwiremode.html language=enus -->
## TOPIC 00037: ACExcitationWireMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-acexcitationwiremode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-acexcitationwiremode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information. SyntaxNamespace: NationalInstruments.DAQmxpublic AIACExcitationWireMode ACExcitationWireMode { get; set; }

### ACExcitationWireMode

Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIACExcitationWireMode](nationalinstruments-daqmx-aiacexcitationwiremode.html) ACExcitationWireMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-adccustomtimingmode.html language=enus -->
## TOPIC 00038: AdcCustomTimingMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-adccustomtimingmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-adccustomtimingmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the timing mode of the ADC when AdcTimingMode is Custom. SyntaxNamespace: NationalInstruments.DAQmxpublic long AdcCustomTimingMode { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AdcCustomTimingMode

Specifies the [timing mode of the ADC](/csh?context=nidaqmx_mxdevconsid_configadctiming) when [AdcTimingMode](nationalinstruments-daqmx-aichannel-adctimingmode.html) is [Custom](nationalinstruments-daqmx-aiadctimingmode.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AdcCustomTimingMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-adctimingmode.html language=enus -->
## TOPIC 00039: AdcTimingMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-adctimingmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-adctimingmode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ADC timing mode, controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for AIConvertRate. You must use the sa

### AdcTimingMode

Specifies the [ADC timing mode](/csh?context=nidaqmx_mxdevconsid_configadctiming), controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for [AIConvertRate](nationalinstruments-daqmx-timing-aiconvertrate.html). You must use the same ADC timing mode for all channels on a device, but you can use different ADC timing modes for different devices in the same task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIAdcTimingMode](nationalinstruments-daqmx-aiadctimingmode.html) AdcTimingMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-attenuation.html language=enus -->
## TOPIC 00040: Attenuation

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-attenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-attenuation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of attenuation to use. SyntaxNamespace: NationalInstruments.DAQmxpublic double Attenuation { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Attenuation

Specifies the amount of attenuation to use.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Attenuation { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-autozeromode.html language=enus -->
## TOPIC 00041: AutoZeroMode

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-autozeromode.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-autozeromode.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample. SyntaxNamespace: NationalInstruments.DAQmxpublic AIAutoZeroMode AutoZeroMode { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AutoZeroMode

Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIAutoZeroMode](nationalinstruments-daqmx-aiautozeromode.html) AutoZeroMode { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-averagingwindowsize.html language=enus -->
## TOPIC 00042: AveragingWindowSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-averagingwindowsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-averagingwindowsize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples to average while acquiring data. Increasing the number of samples to average reduces noise in your measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic long AveragingWindowSize { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI

### AveragingWindowSize

Specifies the number of samples to average while acquiring data. Increasing the number of samples to average reduces noise in your measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AveragingWindowSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgebalancecoarsepot.html language=enus -->
## TOPIC 00043: BridgeBalanceCoarsePot

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgebalancecoarsepot.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgebalancecoarsepot.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies by how much to compensate for offset in the signal. This value can be between 0 and 127. SyntaxNamespace: NationalInstruments.DAQmxpublic int BridgeBalanceCoarsePot { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeBalanceCoarsePot

Specifies by how much to compensate for offset in the signal. This value can be between 0 and 127.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int BridgeBalanceCoarsePot { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgebalancefinepot.html language=enus -->
## TOPIC 00044: BridgeBalanceFinePot

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgebalancefinepot.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgebalancefinepot.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies by how much to compensate for offset in the signal. This value can be between 0 and 4095. SyntaxNamespace: NationalInstruments.DAQmxpublic int BridgeBalanceFinePot { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeBalanceFinePot

Specifies by how much to compensate for offset in the signal. This value can be between 0 and 4095.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int BridgeBalanceFinePot { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeconfiguration.html language=enus -->
## TOPIC 00045: BridgeConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of Wheatstone bridge connected to the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIBridgeConfiguration BridgeConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeConfiguration

Specifies the type of Wheatstone bridge connected to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIBridgeConfiguration](nationalinstruments-daqmx-aibridgeconfiguration.html) BridgeConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeelectricalunits.html language=enus -->
## TOPIC 00046: BridgeElectricalUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeelectricalunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeelectricalunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. SyntaxNamespace: NationalInstruments.DAQmxpublic AIBridgeElectricalUnits BridgeElectricalUnits { get; set; }ExceptionsTypeDescriptionNationalInst

### BridgeElectricalUnits

Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIBridgeElectricalUnits](nationalinstruments-daqmx-aibridgeelectricalunits.html) BridgeElectricalUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeinitialratio.html language=enus -->
## TOPIC 00047: BridgeInitialRatio

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeinitialratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeinitialratio.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in volts per volt the ratio of output voltage from the bridge to excitation voltage supplied to the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set BridgeInitialVoltage, NI-DAQmx coerces this property to BridgeI

### BridgeInitialRatio

Specifies in volts per volt the ratio of output voltage from the bridge to excitation voltage supplied to the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set [BridgeInitialVoltage](nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html), NI-DAQmx coerces this property to [BridgeInitialVoltage](nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html) divided by [ExcitationActualValue](nationalinstruments-daqmx-aichannel-excitationactualvalue.html). If you set this property, NI-DAQmx coerces [BridgeInitialVoltage](nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html) to the value of this property times [ExcitationActualValue](nationalinstruments-daqmx-aichannel-excitationactualvalue.html). If you set both this property and [BridgeInitialVoltage](nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html), and their values conflict, NI-DAQmx returns an error. To avoid this error, reset one property to its default value before setting the other.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeInitialRatio { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html language=enus -->
## TOPIC 00048: BridgeInitialVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in volts the output voltage of the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set BridgeInitialRatio, NI-DAQmx coerces this property to BridgeInitialRatio times ExcitationActualValue. This property is set by DA

### BridgeInitialVoltage

Specifies in volts the output voltage of the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set [BridgeInitialRatio](nationalinstruments-daqmx-aichannel-bridgeinitialratio.html), NI-DAQmx coerces this property to [BridgeInitialRatio](nationalinstruments-daqmx-aichannel-bridgeinitialratio.html) times [ExcitationActualValue](nationalinstruments-daqmx-aichannel-excitationactualvalue.html). This property is set by [DAQmx](nationalinstruments-daqmx.html) Perform Bridge Offset Nulling Calibration. If you set this property, NI-DAQmx coerces [BridgeInitialRatio](nationalinstruments-daqmx-aichannel-bridgeinitialratio.html) to the value of this property divided by [ExcitationActualValue](nationalinstruments-daqmx-aichannel-excitationactualvalue.html). If you set both this property and [BridgeInitialRatio](nationalinstruments-daqmx-aichannel-bridgeinitialratio.html), and their values conflict, NI-DAQmx returns an error. To avoid this error, reset one property to its default value before setting the other.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeInitialVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgenominalresistance.html language=enus -->
## TOPIC 00049: BridgeNominalResistance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgenominalresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgenominalresistance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the resistance of the bridge while not under load. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeNominalResistance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeNominalResistance

Specifies in ohms the resistance of the bridge while not under load.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeNominalResistance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgephysicalunits.html language=enus -->
## TOPIC 00050: BridgePhysicalUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgephysicalunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgephysicalunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. SyntaxNamespace: NationalInstruments.DAQmxpublic AIBridgePhysicalUnits BridgePhysicalUnits { get; set; }ExceptionsTypeDescriptionNationalIns

### BridgePhysicalUnits

Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIBridgePhysicalUnits](nationalinstruments-daqmx-aibridgephysicalunits.html) BridgePhysicalUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgepolynomialforwardcoefficients.html language=enus -->
## TOPIC 00051: BridgePolynomialForwardCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgepolynomialforwardcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgepolynomialforwardcoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of coefficients for the polynomial that converts electrical values to physical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. SyntaxNamespace: NationalInstruments.DAQm

### BridgePolynomialForwardCoefficients

Specifies an array of coefficients for the polynomial that converts electrical values to physical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] BridgePolynomialForwardCoefficients { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgepolynomialreversecoefficients.html language=enus -->
## TOPIC 00052: BridgePolynomialReverseCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgepolynomialreversecoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgepolynomialreversecoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of coefficients for the polynomial that converts physical values to electrical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. SyntaxNamespace: NationalInstruments.DAQm

### BridgePolynomialReverseCoefficients

Specifies an array of coefficients for the polynomial that converts physical values to electrical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] BridgePolynomialReverseCoefficients { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgescaletype.html language=enus -->
## TOPIC 00053: BridgeScaleType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgescaletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgescaletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the scaling type to use when scaling electrical values from the sensor to physical units. SyntaxNamespace: NationalInstruments.DAQmxpublic AIBridgeScaleType BridgeScaleType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeScaleType

Specifies the [scaling type](/csh?context=nidaqmx_measfunds_bridgescalingtypes) to use when scaling electrical values from the sensor to physical units.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIBridgeScaleType](nationalinstruments-daqmx-aibridgescaletype.html) BridgeScaleType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationaactualresistance.html language=enus -->
## TOPIC 00054: BridgeShuntCalibrationAActualResistance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationaactualresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationaactualresistance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the actual value of the internal shunt calibration A resistor. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeShuntCalibrationAActualResistance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeShuntCalibrationAActualResistance

Specifies in ohms the actual value of the internal shunt calibration A resistor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeShuntCalibrationAActualResistance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationaresistance.html language=enus -->
## TOPIC 00055: BridgeShuntCalibrationAResistance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationaresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationaresistance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the desired value of the internal shunt calibration A resistor. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeShuntCalibrationAResistance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeShuntCalibrationAResistance

Specifies in ohms the desired value of the internal shunt calibration A resistor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeShuntCalibrationAResistance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationasource.html language=enus -->
## TOPIC 00056: BridgeShuntCalibrationASource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationasource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationasource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use internal or external shunt when Shunt Cal A is selected. SyntaxNamespace: NationalInstruments.DAQmxpublic BridgeShuntCalibrationSource BridgeShuntCalibrationASource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an er

### BridgeShuntCalibrationASource

Specifies whether to use internal or external shunt when Shunt Cal A is selected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [BridgeShuntCalibrationSource](nationalinstruments-daqmx-bridgeshuntcalibrationsource.html) BridgeShuntCalibrationASource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationbactualresistance.html language=enus -->
## TOPIC 00057: BridgeShuntCalibrationBActualResistance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationbactualresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationbactualresistance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the actual value of the internal shunt calibration B resistor. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeShuntCalibrationBActualResistance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeShuntCalibrationBActualResistance

Specifies in ohms the actual value of the internal shunt calibration B resistor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeShuntCalibrationBActualResistance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationbresistance.html language=enus -->
## TOPIC 00058: BridgeShuntCalibrationBResistance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationbresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationbresistance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the desired value of the internal shunt calibration B resistor. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeShuntCalibrationBResistance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeShuntCalibrationBResistance

Specifies in ohms the desired value of the internal shunt calibration B resistor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeShuntCalibrationBResistance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationenable.html language=enus -->
## TOPIC 00059: BridgeShuntCalibrationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable a shunt calibration switch. Use BridgeShuntCalibrationSelect to select the switch(es) to enable. SyntaxNamespace: NationalInstruments.DAQmxpublic bool BridgeShuntCalibrationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx dri

### BridgeShuntCalibrationEnable

Specifies whether to enable a shunt calibration switch. Use [BridgeShuntCalibrationSelect](nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationselect.html) to select the switch(es) to enable.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool BridgeShuntCalibrationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationgainadjust.html language=enus -->
## TOPIC 00060: BridgeShuntCalibrationGainAdjust

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationgainadjust.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationgainadjust.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the result of a shunt calibration. This property is set by DAQmx Perform Shunt Calibration. NI-DAQmx multiplies data read from the channel by the value of this property. This value should be close to 1.0. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeShuntCalibrationGainAdj

### BridgeShuntCalibrationGainAdjust

Specifies the result of a shunt calibration. This property is set by [DAQmx](nationalinstruments-daqmx.html) Perform Shunt Calibration. NI-DAQmx multiplies data read from the channel by the value of this property. This value should be close to 1.0.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeShuntCalibrationGainAdjust { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationselect.html language=enus -->
## TOPIC 00061: BridgeShuntCalibrationSelect

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationselect.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationselect.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which shunt calibration switch(es) to enable. Use BridgeShuntCalibrationEnable to enable the switch(es) you specify with this property. SyntaxNamespace: NationalInstruments.DAQmxpublic AIBridgeShuntCalibrationSelect BridgeShuntCalibrationSelect { get; set; }ExceptionsTypeDescriptionNationa

### BridgeShuntCalibrationSelect

Specifies which shunt calibration switch(es) to enable. Use [BridgeShuntCalibrationEnable](nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationenable.html) to enable the switch(es) you specify with this property.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIBridgeShuntCalibrationSelect](nationalinstruments-daqmx-aibridgeshuntcalibrationselect.html) BridgeShuntCalibrationSelect { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgetableelectricalvalues.html language=enus -->
## TOPIC 00062: BridgeTableElectricalValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgetableelectricalvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgetableelectricalvalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of electrical values that map to the values in BridgeTablePhysicalValues. Specify this value in the unit indicated by BridgeElectricalUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] BridgeTableElectricalValues { get; set; }RemarksThis property returns a copy of t

### BridgeTableElectricalValues

Specifies the array of electrical values that map to the values in [BridgeTablePhysicalValues](nationalinstruments-daqmx-aichannel-bridgetablephysicalvalues.html). Specify this value in the unit indicated by [BridgeElectricalUnits](nationalinstruments-daqmx-aichannel-bridgeelectricalunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] BridgeTableElectricalValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgetablephysicalvalues.html language=enus -->
## TOPIC 00063: BridgeTablePhysicalValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgetablephysicalvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgetablephysicalvalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of physical values that map to the values in BridgeTableElectricalValues. Specify this value in the unit indicated by BridgePhysicalUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] BridgeTablePhysicalValues { get; set; }RemarksThis property returns a copy of the a

### BridgeTablePhysicalValues

Specifies the array of physical values that map to the values in [BridgeTableElectricalValues](nationalinstruments-daqmx-aichannel-bridgetableelectricalvalues.html). Specify this value in the unit indicated by [BridgePhysicalUnits](nationalinstruments-daqmx-aichannel-bridgephysicalunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] BridgeTablePhysicalValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstelectricalvalue.html language=enus -->
## TOPIC 00064: BridgeTwoPointLinearFirstElectricalValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstelectricalvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstelectricalvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the first electrical value, corresponding to BridgeTwoPointLinearFirstPhysicalValue. Specify this value in the unit indicated by BridgeElectricalUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeTwoPointLinearFirstElectricalValue { get; set; }ExceptionsTypeDescriptionNat

### BridgeTwoPointLinearFirstElectricalValue

Specifies the first electrical value, corresponding to [BridgeTwoPointLinearFirstPhysicalValue](nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstphysicalvalue.html). Specify this value in the unit indicated by [BridgeElectricalUnits](nationalinstruments-daqmx-aichannel-bridgeelectricalunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeTwoPointLinearFirstElectricalValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstphysicalvalue.html language=enus -->
## TOPIC 00065: BridgeTwoPointLinearFirstPhysicalValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstphysicalvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstphysicalvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the first physical value, corresponding to BridgeTwoPointLinearFirstElectricalValue. Specify this value in the unit indicated by BridgePhysicalUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeTwoPointLinearFirstPhysicalValue { get; set; }ExceptionsTypeDescriptionNationa

### BridgeTwoPointLinearFirstPhysicalValue

Specifies the first physical value, corresponding to [BridgeTwoPointLinearFirstElectricalValue](nationalinstruments-daqmx-aichannel-bridgetwopointlinearfirstelectricalvalue.html). Specify this value in the unit indicated by [BridgePhysicalUnits](nationalinstruments-daqmx-aichannel-bridgephysicalunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeTwoPointLinearFirstPhysicalValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondelectricalvalue.html language=enus -->
## TOPIC 00066: BridgeTwoPointLinearSecondElectricalValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondelectricalvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondelectricalvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the second electrical value, corresponding to BridgeTwoPointLinearSecondPhysicalValue. Specify this value in the unit indicated by BridgeElectricalUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeTwoPointLinearSecondElectricalValue { get; set; }ExceptionsTypeDescription

### BridgeTwoPointLinearSecondElectricalValue

Specifies the second electrical value, corresponding to [BridgeTwoPointLinearSecondPhysicalValue](nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondphysicalvalue.html). Specify this value in the unit indicated by [BridgeElectricalUnits](nationalinstruments-daqmx-aichannel-bridgeelectricalunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeTwoPointLinearSecondElectricalValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondphysicalvalue.html language=enus -->
## TOPIC 00067: BridgeTwoPointLinearSecondPhysicalValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondphysicalvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondphysicalvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the second physical value, corresponding to BridgeTwoPointLinearSecondElectricalValue. Specify this value in the unit indicated by BridgePhysicalUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double BridgeTwoPointLinearSecondPhysicalValue { get; set; }ExceptionsTypeDescriptionNati

### BridgeTwoPointLinearSecondPhysicalValue

Specifies the second physical value, corresponding to [BridgeTwoPointLinearSecondElectricalValue](nationalinstruments-daqmx-aichannel-bridgetwopointlinearsecondelectricalvalue.html). Specify this value in the unit indicated by [BridgePhysicalUnits](nationalinstruments-daqmx-aichannel-bridgephysicalunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double BridgeTwoPointLinearSecondPhysicalValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-bridgeunits.html language=enus -->
## TOPIC 00068: BridgeUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-bridgeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-bridgeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return voltage ratios from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIBridgeUnits BridgeUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### BridgeUnits

Specifies in which unit to return [voltage ratios](/csh?context=nidaqmx_measfunds_bridgescaling) from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIBridgeUnits](nationalinstruments-daqmx-aibridgeunits.html) BridgeUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calculatedpowercurrentmaximum.html language=enus -->
## TOPIC 00069: CalculatedPowerCurrentMaximum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calculatedpowercurrentmaximum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calculatedpowercurrentmaximum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced current maximum value that the device can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic

### CalculatedPowerCurrentMaximum

Specifies the current maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced current maximum value that the device can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CalculatedPowerCurrentMaximum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calculatedpowercurrentminimum.html language=enus -->
## TOPIC 00070: CalculatedPowerCurrentMinimum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calculatedpowercurrentminimum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calculatedpowercurrentminimum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the current minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced current minimum value that the device can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic

### CalculatedPowerCurrentMinimum

Specifies the current minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced current minimum value that the device can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CalculatedPowerCurrentMinimum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calculatedpowerunits.html language=enus -->
## TOPIC 00071: CalculatedPowerUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calculatedpowerunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calculatedpowerunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return power measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPowerUnits CalculatedPowerUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CalculatedPowerUnits

Specifies the units to use to return power measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPowerUnits](nationalinstruments-daqmx-aipowerunits.html) CalculatedPowerUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calculatedpowervoltagemaximum.html language=enus -->
## TOPIC 00072: CalculatedPowerVoltageMaximum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calculatedpowervoltagemaximum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calculatedpowervoltagemaximum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced voltage maximum value that the device can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic

### CalculatedPowerVoltageMaximum

Specifies the voltage maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced voltage maximum value that the device can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CalculatedPowerVoltageMaximum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calculatedpowervoltageminimum.html language=enus -->
## TOPIC 00073: CalculatedPowerVoltageMinimum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calculatedpowervoltageminimum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calculatedpowervoltageminimum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced voltage minimum value that the device can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic

### CalculatedPowerVoltageMinimum

Specifies the voltage minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced voltage minimum value that the device can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CalculatedPowerVoltageMinimum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationapplyifexpired.html language=enus -->
## TOPIC 00074: CalibrationApplyIfExpired

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationapplyifexpired.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationapplyifexpired.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the channel calibration to the channel after the expiration date has passed. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CalibrationApplyIfExpired { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CalibrationApplyIfExpired

Specifies whether to apply the channel calibration to the channel after the expiration date has passed.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CalibrationApplyIfExpired { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationdate.html language=enus -->
## TOPIC 00075: CalibrationDate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationdate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationdate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the last date and time that the channel underwent a channel calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic DateTime CalibrationDate { get; set; }RemarksThe last date and time that the channel underwent a channel calibration.ExceptionsTypeDescriptionNationalInstruments.DAQ

### CalibrationDate

Gets or sets the last date and time that the channel underwent a channel calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DateTime CalibrationDate { get; set; }

#### Remarks

The last date and time that the channel underwent a channel calibration.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationdescription.html language=enus -->
## TOPIC 00076: CalibrationDescription

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationdescription.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationdescription.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the description entered for the calibration of the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string CalibrationDescription { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CalibrationDescription

Specifies the description entered for the calibration of the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CalibrationDescription { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationenable.html language=enus -->
## TOPIC 00077: CalibrationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the channel calibration associated with the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CalibrationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CalibrationEnable

Specifies whether to enable the channel calibration associated with the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CalibrationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationexpirationdate.html language=enus -->
## TOPIC 00078: CalibrationExpirationDate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationexpirationdate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationexpirationdate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the date and time that the channel calibration expires. SyntaxNamespace: NationalInstruments.DAQmxpublic DateTime CalibrationExpirationDate { get; set; }RemarksThe date and time that the channel calibration expires.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DA

### CalibrationExpirationDate

Gets or sets the date and time that the channel calibration expires.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public DateTime CalibrationExpirationDate { get; set; }

#### Remarks

The date and time that the channel calibration expires.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationhasvalidinfo.html language=enus -->
## TOPIC 00079: CalibrationHasValidInfo

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationhasvalidinfo.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationhasvalidinfo.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the channel has calibration information. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CalibrationHasValidInfo { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CalibrationHasValidInfo

Indicates if the channel has calibration information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CalibrationHasValidInfo { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationoperatorname.html language=enus -->
## TOPIC 00080: CalibrationOperatorName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationoperatorname.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationoperatorname.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the operator who performed the channel calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic string CalibrationOperatorName { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CalibrationOperatorName

Specifies the name of the operator who performed the channel calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CalibrationOperatorName { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationpolynomialforwardcoefficients.html language=enus -->
## TOPIC 00081: CalibrationPolynomialForwardCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationpolynomialforwardcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationpolynomialforwardcoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the forward polynomial values used for calibrating the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] CalibrationPolynomialForwardCoefficients { get; set; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it

### CalibrationPolynomialForwardCoefficients

Specifies the forward polynomial values used for calibrating the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] CalibrationPolynomialForwardCoefficients { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationpolynomialreversecoefficients.html language=enus -->
## TOPIC 00082: CalibrationPolynomialReverseCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationpolynomialreversecoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationpolynomialreversecoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reverse polynomial values used for calibrating the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] CalibrationPolynomialReverseCoefficients { get; set; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it

### CalibrationPolynomialReverseCoefficients

Specifies the reverse polynomial values used for calibrating the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] CalibrationPolynomialReverseCoefficients { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationscaletype.html language=enus -->
## TOPIC 00083: CalibrationScaleType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationscaletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationscaletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method or equation form that the calibration scale uses. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChannelCalibrationScaleType CalibrationScaleType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CalibrationScaleType

Specifies the method or equation form that the calibration scale uses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChannelCalibrationScaleType](nationalinstruments-daqmx-aichannelcalibrationscaletype.html) CalibrationScaleType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationtableprescaledvalues.html language=enus -->
## TOPIC 00084: CalibrationTablePreScaledValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationtableprescaledvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationtableprescaledvalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference values collected when calibrating the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] CalibrationTablePreScaledValues { get; set; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a co

### CalibrationTablePreScaledValues

Specifies the reference values collected when calibrating the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] CalibrationTablePreScaledValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationtablescaledvalues.html language=enus -->
## TOPIC 00085: CalibrationTableScaledValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationtablescaledvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationtablescaledvalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquired values collected when calibrating the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] CalibrationTableScaledValues { get; set; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy f

### CalibrationTableScaledValues

Specifies the acquired values collected when calibrating the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] CalibrationTableScaledValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationverificationacquiredvalues.html language=enus -->
## TOPIC 00086: CalibrationVerificationAcquiredValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationverificationacquiredvalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationverificationacquiredvalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquired values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] CalibrationVerificationAcquiredValues { get; set; }RemarksT

### CalibrationVerificationAcquiredValues

Specifies the acquired values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] CalibrationVerificationAcquiredValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-calibrationverificationreferencevalues.html language=enus -->
## TOPIC 00087: CalibrationVerificationReferenceValues

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-calibrationverificationreferencevalues.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-calibrationverificationreferencevalues.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] CalibrationVerificationReferenceValues { get; set; }Remark

### CalibrationVerificationReferenceValues

Specifies the reference values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] CalibrationVerificationReferenceValues { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-chargeunits.html language=enus -->
## TOPIC 00088: ChargeUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-chargeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-chargeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return charge measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIChargeUnits ChargeUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ChargeUnits

Specifies the units to use to return charge measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIChargeUnits](nationalinstruments-daqmx-aichargeunits.html) ChargeUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-chopenable.html language=enus -->
## TOPIC 00089: ChopEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-chopenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-chopenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device will chop its inputs. Chopping removes offset voltages and other low frequency errors. SyntaxNamespace: NationalInstruments.DAQmxpublic bool ChopEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ChopEnable

Specifies whether the device will chop its inputs. Chopping removes offset voltages and other low frequency errors.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ChopEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-coupling.html language=enus -->
## TOPIC 00090: Coupling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-coupling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-coupling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the coupling for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AICoupling Coupling { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Coupling

Specifies the coupling for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AICoupling](nationalinstruments-daqmx-aicoupling.html) Coupling { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-currentacrmsunits.html language=enus -->
## TOPIC 00091: CurrentAcrmsUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-currentacrmsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-currentacrmsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return current RMS measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AICurrentAcrmsUnits CurrentAcrmsUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CurrentAcrmsUnits

Specifies the units to use to return current RMS measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AICurrentAcrmsUnits](nationalinstruments-daqmx-aicurrentacrmsunits.html) CurrentAcrmsUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-currentshuntlocation.html language=enus -->
## TOPIC 00092: CurrentShuntLocation

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-currentshuntlocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-currentshuntlocation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shunt resistor location for current measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic AICurrentShuntLocation CurrentShuntLocation { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CurrentShuntLocation

Specifies the shunt resistor location for current measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AICurrentShuntLocation](nationalinstruments-daqmx-aicurrentshuntlocation.html) CurrentShuntLocation { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-currentshuntresistance.html language=enus -->
## TOPIC 00093: CurrentShuntResistance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-currentshuntresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-currentshuntresistance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the external shunt resistance for current measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic double CurrentShuntResistance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CurrentShuntResistance

Specifies in ohms the external shunt resistance for current measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CurrentShuntResistance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-currentunits.html language=enus -->
## TOPIC 00094: CurrentUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-currentunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-currentunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return current measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AICurrentUnits CurrentUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CurrentUnits

Specifies the units to use to return current measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AICurrentUnits](nationalinstruments-daqmx-aicurrentunits.html) CurrentUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-customscalename.html language=enus -->
## TOPIC 00095: CustomScaleName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-customscalename.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-customscalename.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of a custom scale for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string CustomScaleName { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CustomScaleName

Specifies the name of a [custom scale](/csh?context=nidaqmx_mxcncpts_customscales) for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CustomScaleName { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-datatransfercustomthreshold.html language=enus -->
## TOPIC 00096: DataTransferCustomThreshold

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-datatransfercustomthreshold.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-datatransfercustomthreshold.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of samples that must be in the FIFO to transfer data from the device if DataTransferRequestCondition is OnBoardMemoryCustomThreshold. SyntaxNamespace: NationalInstruments.DAQmxpublic long DataTransferCustomThreshold { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx

### DataTransferCustomThreshold

Specifies the number of samples that must be in the FIFO to transfer data from the device if [DataTransferRequestCondition](nationalinstruments-daqmx-aichannel-datatransferrequestcondition.html) is [OnBoardMemoryCustomThreshold](nationalinstruments-daqmx-aidatatransferrequestcondition.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DataTransferCustomThreshold { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-datatransfermaximumrate.html language=enus -->
## TOPIC 00097: DataTransferMaximumRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-datatransfermaximumrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-datatransfermaximumrate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the rate in B/s to transfer data from the device. If this value is not set, then the device will transfer data at a rate based on the bus detected. Modify this value to affect performance under different combinations of operating system, configuration, and device. SyntaxNamespace: National

### DataTransferMaximumRate

Specifies the rate in B/s to transfer data from the device. If this value is not set, then the device will transfer data at a rate based on the bus detected. Modify this value to affect performance under different combinations of operating system, configuration, and device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DataTransferMaximumRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-datatransfermechanism.html language=enus -->
## TOPIC 00098: DataTransferMechanism

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-datatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-datatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AIDataTransferMechanism DataTransferMechanism { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DataTransferMechanism

Specifies the data transfer mode for the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIDataTransferMechanism](nationalinstruments-daqmx-aidatatransfermechanism.html) DataTransferMechanism { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-datatransferrequestcondition.html language=enus -->
## TOPIC 00099: DataTransferRequestCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-datatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-datatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the onboard memory of the device to the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic AIDataTransferRequestCondition DataTransferRequestCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### DataTransferRequestCondition

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIDataTransferRequestCondition](nationalinstruments-daqmx-aidatatransferrequestcondition.html) DataTransferRequestCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-dcoffset.html language=enus -->
## TOPIC 00100: DCOffset

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-dcoffset.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-dcoffset.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DC value to add to the input range of the device. Use RangeHigh and RangeLow to specify the input range. This offset is in the native units of the device . SyntaxNamespace: NationalInstruments.DAQmxpublic double DCOffset { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.D

### DCOffset

Specifies the DC value to add to the input range of the device. Use [RangeHigh](nationalinstruments-daqmx-aichannel-rangehigh.html) and [RangeLow](nationalinstruments-daqmx-aichannel-rangelow.html) to specify the input range. This offset is in the native units of the device .

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DCOffset { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-devicescalingcoefficients.html language=enus -->
## TOPIC 00101: DeviceScalingCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-devicescalingcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-devicescalingcoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the coefficients of a polynomial equation that NI-DAQmx uses to scale values from the native format of the device to volts. Each element of the array corresponds to a term of the equation. For example, if index two of the array is 4, the third term of the equation is 4x^2. Scaling coeffici

### DeviceScalingCoefficients

Indicates the coefficients of a polynomial equation that NI-DAQmx uses to scale values from the native format of the device to volts. Each element of the array corresponds to a term of the equation. For example, if index two of the array is 4, the third term of the equation is 4x^2. Scaling coefficients do not account for any custom scales or sensors contained by the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] DeviceScalingCoefficients { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilterbandpasscenterfrequency.html language=enus -->
## TOPIC 00102: DigitalFilterBandpassCenterFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilterbandpasscenterfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilterbandpasscenterfrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the center frequency of the passband for the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterBandpassCenterFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterBandpassCenterFrequency

Specifies the center frequency of the passband for the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterBandpassCenterFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilterbandpasswidth.html language=enus -->
## TOPIC 00103: DigitalFilterBandpassWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilterbandpasswidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilterbandpasswidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the passband centered around the center frequency for the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterBandpassWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterBandpassWidth

Specifies the width of the passband centered around the center frequency for the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterBandpassWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfiltercoefficients.html language=enus -->
## TOPIC 00104: DigitalFilterCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfiltercoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfiltercoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital filter coefficients. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] DigitalFilterCoefficients { get; set; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop.

### DigitalFilterCoefficients

Specifies the digital filter coefficients.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] DigitalFilterCoefficients { get; set; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilterenabled.html language=enus -->
## TOPIC 00105: DigitalFilterEnabled

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilterenabled.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the digital filter is enabled or disabled. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DigitalFilterEnabled { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterEnabled

Specifies whether the digital filter is enabled or disabled.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DigitalFilterEnabled { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilterhighpasscutofffrequency.html language=enus -->
## TOPIC 00106: DigitalFilterHighpassCutoffFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilterhighpasscutofffrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilterhighpasscutofffrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the highpass cutoff frequency of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterHighpassCutoffFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterHighpassCutoffFrequency

Specifies the highpass cutoff frequency of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterHighpassCutoffFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilterlowpasscutofffrequency.html language=enus -->
## TOPIC 00107: DigitalFilterLowpassCutoffFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilterlowpasscutofffrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilterlowpasscutofffrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lowpass cutoff frequency of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterLowpassCutoffFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterLowpassCutoffFrequency

Specifies the lowpass cutoff frequency of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterLowpassCutoffFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilternotchcenterfrequency.html language=enus -->
## TOPIC 00108: DigitalFilterNotchCenterFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilternotchcenterfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilternotchcenterfrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the center frequency of the stopband for the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterNotchCenterFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterNotchCenterFrequency

Specifies the center frequency of the stopband for the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterNotchCenterFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilternotchwidth.html language=enus -->
## TOPIC 00109: DigitalFilterNotchWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilternotchwidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilternotchwidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the width of the stopband centered around the center frequency for the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DigitalFilterNotchWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterNotchWidth

Specifies the width of the stopband centered around the center frequency for the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DigitalFilterNotchWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilterorder.html language=enus -->
## TOPIC 00110: DigitalFilterOrder

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilterorder.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilterorder.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the order of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic long DigitalFilterOrder { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterOrder

Specifies the order of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long DigitalFilterOrder { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfilterresponse.html language=enus -->
## TOPIC 00111: DigitalFilterResponse

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfilterresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfilterresponse.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital filter response. SyntaxNamespace: NationalInstruments.DAQmxpublic FilterResponse DigitalFilterResponse { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterResponse

Specifies the digital filter response.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [FilterResponse](nationalinstruments-daqmx-filterresponse.html) DigitalFilterResponse { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-digitalfiltertype.html language=enus -->
## TOPIC 00112: DigitalFilterType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-digitalfiltertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-digitalfiltertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital filter type. SyntaxNamespace: NationalInstruments.DAQmxpublic FilterType DigitalFilterType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DigitalFilterType

Specifies the digital filter type.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [FilterType](nationalinstruments-daqmx-filtertype.html) DigitalFilterType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-ditherenable.html language=enus -->
## TOPIC 00113: DitherEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-ditherenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-ditherenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable dithering. Dithering adds Gaussian noise to the input signal. You can use dithering to achieve higher resolution measurements by over sampling the input signal and averaging the results. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DitherEnable { get; set; }Excep

### DitherEnable

Specifies whether to enable dithering. Dithering adds Gaussian noise to the input signal. You can use dithering to achieve higher resolution measurements by over sampling the input signal and averaging the results.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DitherEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivity.html language=enus -->
## TOPIC 00114: EddyCurrentProximityProbeSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the eddy current proximity probe . This value is in the units you specify with EddyCurrentProximityProbeSensitivityUnits. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double EddyCurrentProximityProbeSensitivi

### EddyCurrentProximityProbeSensitivity

Specifies the sensitivity of the [eddy current proximity probe](/csh?context=nidaqmx_measfunds_eddycurrentproximityprobe) . This value is in the units you specify with [EddyCurrentProximityProbeSensitivityUnits](nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivityunits.html). Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EddyCurrentProximityProbeSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivityunits.html language=enus -->
## TOPIC 00115: EddyCurrentProximityProbeSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of EddyCurrentProximityProbeSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AIEddyCurrentProximityProbeSensitivityUnits EddyCurrentProximityProbeSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned

### EddyCurrentProximityProbeSensitivityUnits

Specifies the units of [EddyCurrentProximityProbeSensitivity](nationalinstruments-daqmx-aichannel-eddycurrentproximityprobesensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIEddyCurrentProximityProbeSensitivityUnits](nationalinstruments-daqmx-aieddycurrentproximityprobesensitivityunits.html) EddyCurrentProximityProbeSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-eddycurrentproximityprobeunits.html language=enus -->
## TOPIC 00116: EddyCurrentProximityProbeUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-eddycurrentproximityprobeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-eddycurrentproximityprobeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return proximity measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIEddyCurrentProximityProbeUnits EddyCurrentProximityProbeUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an e

### EddyCurrentProximityProbeUnits

Specifies the units to use to return proximity measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIEddyCurrentProximityProbeUnits](nationalinstruments-daqmx-aieddycurrentproximityprobeunits.html) EddyCurrentProximityProbeUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-enhancedaliasrejectionenable.html language=enus -->
## TOPIC 00117: EnhancedAliasRejectionEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-enhancedaliasrejectionenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-enhancedaliasrejectionenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable enhanced alias rejection. Leave this property set to the default value for most applications. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EnhancedAliasRejectionEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver

### EnhancedAliasRejectionEnable

Specifies whether to enable [enhanced alias rejection](/csh?context=nidaqmx_mxdevconsid_enhancedaliasrej). Leave this property set to the default value for most applications.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EnhancedAliasRejectionEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-excitationactualvalue.html language=enus -->
## TOPIC 00118: ExcitationActualValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-excitationactualvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-excitationactualvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the actual amount of excitation supplied by an internal excitation source. If you read an internal excitation source more precisely with an external device, set this property to the value you read. NI-DAQmx ignores this value for external excitation. When performing shunt calibration, some

### ExcitationActualValue

Specifies the actual amount of excitation supplied by an internal excitation source. If you read an internal excitation source more precisely with an external device, set this property to the value you read. NI-DAQmx ignores this value for external excitation. When performing shunt calibration, some devices set this property automatically.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ExcitationActualValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-excitationdcorac.html language=enus -->
## TOPIC 00119: ExcitationDCOrAC

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-excitationdcorac.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-excitationdcorac.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the excitation supply is DC or AC. SyntaxNamespace: NationalInstruments.DAQmxpublic AIExcitationDCOrAC ExcitationDCOrAC { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ExcitationDCOrAC

Specifies if the excitation supply is DC or AC.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIExcitationDCOrAC](nationalinstruments-daqmx-aiexcitationdcorac.html) ExcitationDCOrAC { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-excitationidleoutputbehavior.html language=enus -->
## TOPIC 00120: ExcitationIdleOutputBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-excitationidleoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-excitationidleoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit. SyntaxNamespace: NationalInstruments.DAQmx

### ExcitationIdleOutputBehavior

Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ExcitationIdleOutputBehavior](nationalinstruments-daqmx-excitationidleoutputbehavior.html) ExcitationIdleOutputBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-excitationsense.html language=enus -->
## TOPIC 00121: ExcitationSense

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-excitationsense.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-excitationsense.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use local or remote sense to sense excitation. SyntaxNamespace: NationalInstruments.DAQmxpublic AIExcitationSense ExcitationSense { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ExcitationSense

Specifies whether to use local or remote sense to sense excitation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIExcitationSense](nationalinstruments-daqmx-aiexcitationsense.html) ExcitationSense { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-excitationsource.html language=enus -->
## TOPIC 00122: ExcitationSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-excitationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-excitationsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of excitation. SyntaxNamespace: NationalInstruments.DAQmxpublic AIExcitationSource ExcitationSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ExcitationSource

Specifies the source of excitation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIExcitationSource](nationalinstruments-daqmx-aiexcitationsource.html) ExcitationSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-excitationvalue.html language=enus -->
## TOPIC 00123: ExcitationValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-excitationvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-excitationvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of excitation that the sensor requires. If ExcitationVoltageOrCurrent is Voltage, this value is in volts. If ExcitationVoltageOrCurrent is Current, this value is in amperes. SyntaxNamespace: NationalInstruments.DAQmxpublic double ExcitationValue { get; set; }ExceptionsTypeDescri

### ExcitationValue

Specifies the amount of excitation that the sensor requires. If [ExcitationVoltageOrCurrent](nationalinstruments-daqmx-aichannel-excitationvoltageorcurrent.html) is [Voltage](nationalinstruments-daqmx-aiexcitationvoltageorcurrent.html), this value is in volts. If [ExcitationVoltageOrCurrent](nationalinstruments-daqmx-aichannel-excitationvoltageorcurrent.html) is [Current](nationalinstruments-daqmx-aiexcitationvoltageorcurrent.html), this value is in amperes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ExcitationValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-excitationvoltageorcurrent.html language=enus -->
## TOPIC 00124: ExcitationVoltageOrCurrent

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-excitationvoltageorcurrent.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-excitationvoltageorcurrent.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the channel uses current or voltage excitation. SyntaxNamespace: NationalInstruments.DAQmxpublic AIExcitationVoltageOrCurrent ExcitationVoltageOrCurrent { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ExcitationVoltageOrCurrent

Specifies if the channel uses current or voltage excitation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIExcitationVoltageOrCurrent](nationalinstruments-daqmx-aiexcitationvoltageorcurrent.html) ExcitationVoltageOrCurrent { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-filterdelay.html language=enus -->
## TOPIC 00125: FilterDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-filterdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-filterdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the amount of time between when the ADC samples data and when the sample is read by the host device. This value is in the units you specify with FilterDelayUnits. You can adjust this amount of time using FilterDelayAdjustment. SyntaxNamespace: NationalInstruments.DAQmxpublic double FilterD

### FilterDelay

Indicates the amount of time between when the ADC samples data and when the sample is read by the host device. This value is in the units you specify with [FilterDelayUnits](nationalinstruments-daqmx-aichannel-filterdelayunits.html). You can adjust this amount of time using [FilterDelayAdjustment](nationalinstruments-daqmx-aichannel-filterdelayadjustment.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FilterDelay { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-filterdelayadjustment.html language=enus -->
## TOPIC 00126: FilterDelayAdjustment

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-filterdelayadjustment.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-filterdelayadjustment.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of filter delay that gets removed if RemoveFilterDelay is enabled. This delay adjustment is in addition to the value indicated by FilterDelay. This delay adjustment is in the units you specify with FilterDelayUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double FilterD

### FilterDelayAdjustment

Specifies the amount of filter delay that gets removed if [RemoveFilterDelay](nationalinstruments-daqmx-aichannel-removefilterdelay.html) is enabled. This delay adjustment is in addition to the value indicated by [FilterDelay](nationalinstruments-daqmx-aichannel-filterdelay.html). This delay adjustment is in the units you specify with [FilterDelayUnits](nationalinstruments-daqmx-aichannel-filterdelayunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FilterDelayAdjustment { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-filterdelayunits.html language=enus -->
## TOPIC 00127: FilterDelayUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-filterdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-filterdelayunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of FilterDelay and FilterDelayAdjustment. SyntaxNamespace: NationalInstruments.DAQmxpublic AIFilterDelayUnits FilterDelayUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterDelayUnits

Specifies the units of [FilterDelay](nationalinstruments-daqmx-aichannel-filterdelay.html) and [FilterDelayAdjustment](nationalinstruments-daqmx-aichannel-filterdelayadjustment.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIFilterDelayUnits](nationalinstruments-daqmx-aifilterdelayunits.html) FilterDelayUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-filterenabled.html language=enus -->
## TOPIC 00128: FilterEnabled

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-filterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-filterenabled.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the corresponding filter enable/disable state. SyntaxNamespace: NationalInstruments.DAQmxpublic bool FilterEnabled { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterEnabled

Specifies the corresponding filter enable/disable state.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool FilterEnabled { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-filterfrequency.html language=enus -->
## TOPIC 00129: FilterFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-filterfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-filterfrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the corresponding filter frequency (cutoff or center) of the filter response. SyntaxNamespace: NationalInstruments.DAQmxpublic double FilterFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterFrequency

Specifies the corresponding filter frequency (cutoff or center) of the filter response.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FilterFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-filterorder.html language=enus -->
## TOPIC 00130: FilterOrder

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-filterorder.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-filterorder.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the corresponding filter order and defines the slope of the filter response. SyntaxNamespace: NationalInstruments.DAQmxpublic long FilterOrder { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterOrder

Specifies the corresponding filter order and defines the slope of the filter response.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long FilterOrder { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-filterresponse.html language=enus -->
## TOPIC 00131: FilterResponse

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-filterresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-filterresponse.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the corresponding filter response and defines the shape of the filter response. SyntaxNamespace: NationalInstruments.DAQmxpublic AIFilterResponse FilterResponse { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterResponse

Specifies the corresponding filter response and defines the shape of the filter response.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIFilterResponse](nationalinstruments-daqmx-aifilterresponse.html) FilterResponse { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-forceiepesensorsensitivity.html language=enus -->
## TOPIC 00132: ForceIepeSensorSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-forceiepesensorsensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-forceiepesensorsensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the IEPE force sensor connected to the channel. Specify this value in the unit indicated by ForceIepeSensorSensitivityUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double ForceIepeSensorSensitivity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx

### ForceIepeSensorSensitivity

Specifies the sensitivity of the IEPE force sensor connected to the channel. Specify this value in the unit indicated by [ForceIepeSensorSensitivityUnits](nationalinstruments-daqmx-aichannel-forceiepesensorsensitivityunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ForceIepeSensorSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-forceiepesensorsensitivityunits.html language=enus -->
## TOPIC 00133: ForceIepeSensorSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-forceiepesensorsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-forceiepesensorsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for ForceIepeSensorSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AIForceIepeSensorSensitivityUnits ForceIepeSensorSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ForceIepeSensorSensitivityUnits

Specifies the units for [ForceIepeSensorSensitivity](nationalinstruments-daqmx-aichannel-forceiepesensorsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIForceIepeSensorSensitivityUnits](nationalinstruments-daqmx-aiforceiepesensorsensitivityunits.html) ForceIepeSensorSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-forcereadfromchannel.html language=enus -->
## TOPIC 00134: ForceReadFromChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-forcereadfromchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-forcereadfromchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to read from the channel if it is a cold-junction compensation channel. By default, reading from the task does not return data from cold-junction compensation channels. Setting this property to true forces read operations to return the cold-junction compensation channel data with t

### ForceReadFromChannel

Specifies whether to read from the channel if it is a [cold-junction compensation](/csh?context=nidaqmx_measfunds_sigcontherm) channel. By default, reading from the task does not return data from cold-junction compensation channels. Setting this property to true forces read operations to return the cold-junction compensation channel data with the other channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ForceReadFromChannel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-forcereadfromstrainchannel.html language=enus -->
## TOPIC 00135: ForceReadFromStrainChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-forcereadfromstrainchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-forcereadfromstrainchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the data is returned by reading from the task when set on a raw strain channel that is part of a rosette configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic bool ForceReadFromStrainChannel { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe N

### ForceReadFromStrainChannel

Specifies whether the data is returned by reading from the task when set on a raw strain channel that is part of a rosette configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ForceReadFromStrainChannel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-forceunits.html language=enus -->
## TOPIC 00136: ForceUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-forceunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-forceunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return force or load measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIForceUnits ForceUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ForceUnits

Specifies in which unit to return force or load measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIForceUnits](nationalinstruments-daqmx-aiforceunits.html) ForceUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-frequencyhysteresis.html language=enus -->
## TOPIC 00137: FrequencyHysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-frequencyhysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-frequencyhysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in volts a window below FrequencyThresholdVoltage. The input voltage must pass below FrequencyThresholdVoltage minus this value before NI-DAQmx recognizes a waveform repetition at FrequencyThresholdVoltage. Hysteresis can improve the measurement accuracy when the signal contains noise or j

### FrequencyHysteresis

Specifies in volts a window below [FrequencyThresholdVoltage](nationalinstruments-daqmx-aichannel-frequencythresholdvoltage.html). The input voltage must pass below [FrequencyThresholdVoltage](nationalinstruments-daqmx-aichannel-frequencythresholdvoltage.html) minus this value before NI-DAQmx recognizes a waveform repetition at [FrequencyThresholdVoltage](nationalinstruments-daqmx-aichannel-frequencythresholdvoltage.html). Hysteresis can improve the measurement accuracy when the signal contains noise or jitter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FrequencyHysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-frequencythresholdvoltage.html language=enus -->
## TOPIC 00138: FrequencyThresholdVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-frequencythresholdvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-frequencythresholdvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. SyntaxNamespace: NationalInstruments.DAQmxpubl

### FrequencyThresholdVoltage

Specifies the voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FrequencyThresholdVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-frequencyunits.html language=enus -->
## TOPIC 00139: FrequencyUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-frequencyunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-frequencyunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return frequency measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIFrequencyUnits FrequencyUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyUnits

Specifies the units to use to return frequency measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIFrequencyUnits](nationalinstruments-daqmx-aifrequencyunits.html) FrequencyUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-gain.html language=enus -->
## TOPIC 00140: Gain

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-gain.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-gain.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a gain factor to apply to the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double Gain { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Gain

Specifies a gain factor to apply to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Gain { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-impedance.html language=enus -->
## TOPIC 00141: Impedance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-impedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-impedance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input impedance of the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic double Impedance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Impedance

Specifies the input impedance of the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Impedance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectenable.html language=enus -->
## TOPIC 00142: InputLimitsFaultDetectEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable input limits fault detection. SyntaxNamespace: NationalInstruments.DAQmxpublic bool InputLimitsFaultDetectEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### InputLimitsFaultDetectEnable

Specifies whether to enable input limits fault detection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool InputLimitsFaultDetectEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectlowerlimit.html language=enus -->
## TOPIC 00143: InputLimitsFaultDetectLowerLimit

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectlowerlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectlowerlimit.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the level of the lower limit for input limits detection. An input sample outside the upper and lower bounds causes a fault. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a

### InputLimitsFaultDetectLowerLimit

Specifies the level of the lower limit for input limits detection. An input sample outside the upper and lower bounds causes a fault. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double InputLimitsFaultDetectLowerLimit { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectupperlimit.html language=enus -->
## TOPIC 00144: InputLimitsFaultDetectUpperLimit

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectupperlimit.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-inputlimitsfaultdetectupperlimit.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the level of the upper limit for input limits detection. An input sample outside the upper and lower bounds causes a fault. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a

### InputLimitsFaultDetectUpperLimit

Specifies the level of the upper limit for input limits detection. An input sample outside the upper and lower bounds causes a fault. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double InputLimitsFaultDetectUpperLimit { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-inputsource.html language=enus -->
## TOPIC 00145: InputSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-inputsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-inputsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the channel. You can use the signal from the I/O connector or one of several calibration signals. Certain devices have a single calibration signal bus. For these devices, you must specify the same calibration signal for all channels you connect to a calibration signal. Syntax

### InputSource

Specifies the source of the channel. You can use the signal from the I/O connector or one of several calibration signals. Certain devices have a single calibration signal bus. For these devices, you must specify the same calibration signal for all channels you connect to a calibration signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string InputSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-isteds.html language=enus -->
## TOPIC 00146: IsTeds

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-isteds.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-isteds.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the virtual channel was initialized using a TEDS bitstream from the corresponding physical channel. SyntaxNamespace: NationalInstruments.DAQmxpublic bool IsTeds { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### IsTeds

Indicates if the virtual channel was initialized using a TEDS bitstream from the corresponding physical channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsTeds { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-leadwireresistance.html language=enus -->
## TOPIC 00147: LeadWireResistance

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-leadwireresistance.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-leadwireresistance.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the resistance of the wires that lead to the sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic double LeadWireResistance { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LeadWireResistance

Specifies in ohms the resistance of the wires that lead to the sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LeadWireResistance { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lossylsbremovalcompressedsamplesize.html language=enus -->
## TOPIC 00148: LossyLsbRemovalCompressedSampleSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lossylsbremovalcompressedsamplesize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lossylsbremovalcompressedsamplesize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of bits to return in a raw sample when RawDataCompressionType is set to LossyLsbRemoval. SyntaxNamespace: NationalInstruments.DAQmxpublic long LossyLsbRemovalCompressedSampleSize { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retu

### LossyLsbRemovalCompressedSampleSize

Specifies the number of bits to return in a [raw sample](/csh?context=nidaqmx_mxcncpts_rawdata) when [RawDataCompressionType](nationalinstruments-daqmx-aichannel-rawdatacompressiontype.html) is set to [LossyLsbRemoval](nationalinstruments-daqmx-airawdatacompressiontype.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long LossyLsbRemovalCompressedSampleSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lowpasscutofffrequency.html language=enus -->
## TOPIC 00149: LowpassCutoffFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lowpasscutofffrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lowpasscutofffrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency in Hertz that corresponds to the -3dB cutoff of the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double LowpassCutoffFrequency { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LowpassCutoffFrequency

Specifies the frequency in Hertz that corresponds to the -3dB cutoff of the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LowpassCutoffFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lowpassenable.html language=enus -->
## TOPIC 00150: LowpassEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lowpassenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lowpassenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the lowpass filter of the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic bool LowpassEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LowpassEnable

Specifies whether to enable the lowpass filter of the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool LowpassEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorclocksource.html language=enus -->
## TOPIC 00151: LowpassSwitchedCapacitorClockSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorclocksource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information. SyntaxNamespace: NationalInstruments.DAQmxpublic AILowpassSwitchedCapacitorClockSo

### LowpassSwitchedCapacitorClockSource

Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AILowpassSwitchedCapacitorClockSource](nationalinstruments-daqmx-ailowpassswitchedcapacitorclocksource.html) LowpassSwitchedCapacitorClockSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorexternalclockdivisor.html language=enus -->
## TOPIC 00152: LowpassSwitchedCapacitorExternalClockDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorexternalclockdivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorexternalclockdivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the divisor for the external clock when you set LowpassSwitchedCapacitorClockSource to External. On the SCXI-1141, SCXI-1142, and SCXI-1143, NI-DAQmx determines the filter cutoff by using the equation f/(100*n), where f is the external frequency, and n is the external clock divisor. Refer

### LowpassSwitchedCapacitorExternalClockDivisor

Specifies the divisor for the external clock when you set [LowpassSwitchedCapacitorClockSource](nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorclocksource.html) to [External](nationalinstruments-daqmx-ailowpassswitchedcapacitorclocksource.html). On the SCXI-1141, SCXI-1142, and SCXI-1143, NI-DAQmx determines the filter cutoff by using the equation f/(100*n), where f is the external frequency, and n is the external clock divisor. Refer to the SCXI-1141/1142/1143 User Manual for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long LowpassSwitchedCapacitorExternalClockDivisor { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorexternalclockfrequency.html language=enus -->
## TOPIC 00153: LowpassSwitchedCapacitorExternalClockFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorexternalclockfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorexternalclockfrequency.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the external clock when you set LowpassSwitchedCapacitorClockSource to External. NI-DAQmx uses this frequency to set the pre- and post- filters on the SCXI-1141, SCXI-1142, and SCXI-1143. On those devices, NI-DAQmx determines the filter cutoff by using the equation f/(100*

### LowpassSwitchedCapacitorExternalClockFrequency

Specifies the frequency of the external clock when you set [LowpassSwitchedCapacitorClockSource](nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitorclocksource.html) to [External](nationalinstruments-daqmx-ailowpassswitchedcapacitorclocksource.html). NI-DAQmx uses this frequency to set the pre- and post- filters on the SCXI-1141, SCXI-1142, and SCXI-1143. On those devices, NI-DAQmx determines the filter cutoff by using the equation f/(100*n), where f is the external frequency, and n is the external clock divisor. Refer to the SCXI-1141/1142/1143 User Manual for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LowpassSwitchedCapacitorExternalClockFrequency { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitoroutputclockdivisor.html language=enus -->
## TOPIC 00154: LowpassSwitchedCapacitorOutputClockDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitoroutputclockdivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lowpassswitchedcapacitoroutputclockdivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the divisor for the output clock. NI-DAQmx uses the cutoff frequency to determine the output clock frequency. Refer to the SCXI-1141/1142/1143 User Manual for more information. SyntaxNamespace: NationalInstruments.DAQmxpublic long LowpassSwitchedCapacitorOutputClockDivisor { get; set; }Exc

### LowpassSwitchedCapacitorOutputClockDivisor

Specifies the divisor for the output clock. NI-DAQmx uses the cutoff frequency to determine the output clock frequency. Refer to the SCXI-1141/1142/1143 User Manual for more information.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long LowpassSwitchedCapacitorOutputClockDivisor { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lvdtsensitivity.html language=enus -->
## TOPIC 00155: LvdtSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lvdtsensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lvdtsensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the LVDT. This value is in the units you specify with LvdtSensitivityUnits. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double LvdtSensitivity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.

### LvdtSensitivity

Specifies the sensitivity of the [LVDT](/csh?context=nidaqmx_measfunds_lvdts). This value is in the units you specify with [LvdtSensitivityUnits](nationalinstruments-daqmx-aichannel-lvdtsensitivityunits.html). Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LvdtSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lvdtsensitivityunits.html language=enus -->
## TOPIC 00156: LvdtSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lvdtsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lvdtsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of LvdtSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AILvdtSensitivityUnits LvdtSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LvdtSensitivityUnits

Specifies the units of [LvdtSensitivity](nationalinstruments-daqmx-aichannel-lvdtsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AILvdtSensitivityUnits](nationalinstruments-daqmx-ailvdtsensitivityunits.html) LvdtSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-lvdtunits.html language=enus -->
## TOPIC 00157: LvdtUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-lvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-lvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return linear position measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AILvdtUnits LvdtUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LvdtUnits

Specifies the units to use to return linear position measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AILvdtUnits](nationalinstruments-daqmx-ailvdtunits.html) LvdtUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-maximum.html language=enus -->
## TOPIC 00158: Maximum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-maximum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-maximum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the device can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic double Maximum {

### Maximum

Specifies the [maximum value](/csh?context=nidaqmx_measfunds_limitsettings) you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the [coerced](/csh?context=nidaqmx_mxcncpts_inputlimitcoercion) maximum value that the device can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Maximum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-maximumsoundpressurelevel.html language=enus -->
## TOPIC 00159: MaximumSoundPressureLevel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-maximumsoundpressurelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-maximumsoundpressurelevel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values in pascals for Maximum and Minimum for the channel. SyntaxNamespace: NationalInstruments.DAQmxp

### MaximumSoundPressureLevel

Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values in pascals for [Maximum](nationalinstruments-daqmx-aichannel-maximum.html) and [Minimum](nationalinstruments-daqmx-aichannel-minimum.html) for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaximumSoundPressureLevel { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-measurementtype.html language=enus -->
## TOPIC 00160: MeasurementType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-measurementtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-measurementtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use. SyntaxNamespace: NationalInstruments.DAQmxpublic AIMeasurementType MeasurementType { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI

### MeasurementType

Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIMeasurementType](nationalinstruments-daqmx-aimeasurementtype.html) MeasurementType { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-memorymappingenable.html language=enus -->
## TOPIC 00161: MemoryMappingEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-memorymappingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-memorymappingenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application ac

### MemoryMappingEnable

Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool MemoryMappingEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-microphonesensitivity.html language=enus -->
## TOPIC 00162: MicrophoneSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-microphonesensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-microphonesensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the microphone. This value is in mV/Pa. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double MicrophoneSensitivity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx drive

### MicrophoneSensitivity

Specifies the sensitivity of the [microphone](/csh?context=nidaqmx_measfunds_microphones). This value is in mV/Pa. Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MicrophoneSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-minimum.html language=enus -->
## TOPIC 00163: Minimum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-minimum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-minimum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the device can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic double Minimum {

### Minimum

Specifies the [minimum value](/csh?context=nidaqmx_measfunds_limitsettings) you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the [coerced](/csh?context=nidaqmx_mxcncpts_inputlimitcoercion) minimum value that the device can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Minimum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-openchanneldetectenable.html language=enus -->
## TOPIC 00164: OpenChannelDetectEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-openchanneldetectenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-openchanneldetectenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable open channel detection. SyntaxNamespace: NationalInstruments.DAQmxpublic bool OpenChannelDetectEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OpenChannelDetectEnable

Specifies whether to enable open channel detection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool OpenChannelDetectEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-openthermocoupledetectenable.html language=enus -->
## TOPIC 00165: OpenThermocoupleDetectEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-openthermocoupledetectenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-openthermocoupledetectenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the open thermocouple detection bias voltage to the channel. Changing the value of this property on a channel may require settling time before the data returned is valid. To compensate for this settling time, discard unsettled data or add a delay between committing and sta

### OpenThermocoupleDetectEnable

Specifies whether to apply the [open thermocouple detection bias voltage](/csh?context=nidaqmx_mxdevconsid_openthermdet) to the channel. Changing the value of this property on a channel may require settling time before the data returned is valid. To compensate for this settling time, discard unsettled data or add a delay between committing and starting the task. Refer to your device specifications for the required settling time. When open thermocouple detection is enabled, use [OpenThermocoupleChannelsExist](nationalinstruments-daqmx-daqstream-openthermocouplechannelsexist.html) to determine if any channels were open.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool OpenThermocoupleDetectEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-overcurrentdetectenable.html language=enus -->
## TOPIC 00166: OvercurrentDetectEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-overcurrentdetectenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-overcurrentdetectenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable overcurrent detection. SyntaxNamespace: NationalInstruments.DAQmxpublic bool OvercurrentDetectEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OvercurrentDetectEnable

Specifies whether to enable overcurrent detection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool OvercurrentDetectEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performbridgeoffsetnullingcalibration.html language=enus -->
## TOPIC 00167: PerformBridgeOffsetNullingCalibration()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performbridgeoffsetnullingcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performbridgeoffsetnullingcalibration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a bridge offset nulling calibration on the virtual channels in the task. An error will occur if not all virtual channels in the task support this operation. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformBridgeOffsetNullingCalibration()RemarksThis method adjusts the BridgeBala

### PerformBridgeOffsetNullingCalibration()

Performs a bridge offset nulling calibration on the virtual channels in the task. An error will occur if not all virtual channels in the task support this operation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformBridgeOffsetNullingCalibration()

#### Remarks

This method adjusts the [BridgeBalanceCoarsePot](nationalinstruments-daqmx-aichannel-bridgebalancecoarsepot.html), [BridgeBalanceFinePot](nationalinstruments-daqmx-aichannel-bridgebalancefinepot.html), and [BridgeInitialVoltage](nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html) properties to eliminate voltage offset in the virtual channel. If the acquisition device does not have a built-in potentiometer, only the initial bridge voltage attribute is adjusted.

The task must not be reserved, committed, or started. All virtual channel configurations must be complete prior to calling this method. The physical channel must remain in the state at which you expect to read 0 V from the bridge while the method executes.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performbridgeoffsetnullingcalibration__bool.html language=enus -->
## TOPIC 00168: PerformBridgeOffsetNullingCalibration(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performbridgeoffsetnullingcalibration__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performbridgeoffsetnullingcalibration__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs a bridge offset nulling calibration on the virtual channels in the task. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformBridgeOffsetNullingCalibration([MarshalAs(UnmanagedType.U1)] bool skipUnsupportedChannels)RemarksThis method adjusts the BridgeBalanceCoarsePot, BridgeBalanc

### PerformBridgeOffsetNullingCalibration(bool)

Performs a bridge offset nulling calibration on the virtual channels in the task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformBridgeOffsetNullingCalibration([MarshalAs(UnmanagedType.U1)] bool skipUnsupportedChannels)

#### Remarks

This method adjusts the [BridgeBalanceCoarsePot](nationalinstruments-daqmx-aichannel-bridgebalancecoarsepot.html), [BridgeBalanceFinePot](nationalinstruments-daqmx-aichannel-bridgebalancefinepot.html), and [BridgeInitialVoltage](nationalinstruments-daqmx-aichannel-bridgeinitialvoltage.html) properties to eliminate voltage offset in the virtual channel. If the acquisition device does not have a built-in potentiometer, only the initial bridge voltage attribute is adjusted.

The task must not be reserved, committed, or started. All virtual channel configurations must be complete prior to calling this method. The physical channel must remain in the state at which you expect to read 0 V from the bridge while the method executes.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| skipUnsupportedChannels | bool | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is true, shunt calibration will be performed only on supported virtual channels in the task. If false, shunt calibration will be performed on all virtual channels in the task, which may result in an error if not all channels support shunt calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-bool.html language=enus -->
## TOPIC 00169: PerformBridgeShuntCalibration(double, ShuntElementLocation, double, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the virtual channels in the task using a bridge sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, double bridgeResistance, [MarshalAs(UnmanagedType.U1)] boo

### PerformBridgeShuntCalibration(double, ShuntElementLocation, double, bool)

Performs shunt calibration for the virtual channels in the task using a bridge sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, double bridgeResistance, [MarshalAs(UnmanagedType.U1)] bool skipUnsupportedChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | Specifies the shunt resistance, in ohms. |
| shuntResistorLocation | ShuntElementLocation | Specifies the location of the shunt resistor. |
| bridgeResistance | double | Specifies the bridge resistance, in ohms. |
| skipUnsupportedChannels | bool | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is true, shunt calibration will be performed only on supported virtual channels in the task. If false, shunt calibration will be performed on all virtual channels in the task, which may result in an error if not all channels support shunt calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-shuntcalibrationselect-shuntresistorsource-bool.html language=enus -->
## TOPIC 00170: PerformBridgeShuntCalibration(double, ShuntElementLocation, double, ShuntCalibrationSelect, ShuntResistorSource, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-shuntcalibrationselect-shuntresistorsource-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-shuntcalibrationselect-shuntresistorsource-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the specified channels using a bridge sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, double bridgeResistance, ShuntCalibrationSelect shuntResistorSelect,

### PerformBridgeShuntCalibration(double, ShuntElementLocation, double, ShuntCalibrationSelect, ShuntResistorSource, bool)

Performs shunt calibration for the specified channels using a bridge sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, double bridgeResistance, ShuntCalibrationSelect shuntResistorSelect, ShuntResistorSource shuntResistorSource, [MarshalAs(UnmanagedType.U1)] bool skipUnsupportedChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | The resistance, in ohms, of the shunt resistor. |
| shuntResistorLocation | ShuntElementLocation | The location of the shunt resistor. |
| bridgeResistance | double | The resistance, in ohms, of the bridge sensor. |
| shuntResistorSelect | ShuntCalibrationSelect | The shunt calibration switch to use. |
| shuntResistorSource | ShuntResistorSource | The shunt resistor to use. |
| skipUnsupportedChannels | bool | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is true, shunt calibration is performed only on supported channels. If false, shunt calibration is performed on channels specified by channelNames . The default is false. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-shuntcalibrationselect-shuntresistorsource.html language=enus -->
## TOPIC 00171: PerformBridgeShuntCalibration(double, ShuntElementLocation, double, ShuntCalibrationSelect, ShuntResistorSource)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-shuntcalibrationselect-shuntresistorsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double-shuntcalibrationselect-shuntresistorsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the specified channels using a bridge sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, double bridgeResistance, ShuntCalibrationSelect shuntResistorSelect,

### PerformBridgeShuntCalibration(double, ShuntElementLocation, double, ShuntCalibrationSelect, ShuntResistorSource)

Performs shunt calibration for the specified channels using a bridge sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, double bridgeResistance, ShuntCalibrationSelect shuntResistorSelect, ShuntResistorSource shuntResistorSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | The resistance, in ohms, of the shunt resistor. |
| shuntResistorLocation | ShuntElementLocation | The location of the shunt resistor. |
| bridgeResistance | double | The resistance, in ohms, of the bridge sensor. |
| shuntResistorSelect | ShuntCalibrationSelect | The shunt calibration switch to use. |
| shuntResistorSource | ShuntResistorSource | The shunt resistor to use. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double.html language=enus -->
## TOPIC 00172: PerformBridgeShuntCalibration(double, ShuntElementLocation, double)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performbridgeshuntcalibration__double-shuntelementlocation-double.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the virtual channels in the task using a bridge sensor. An error will occur if not all virtual channels in the task support this operation. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocati

### PerformBridgeShuntCalibration(double, ShuntElementLocation, double)

Performs shunt calibration for the virtual channels in the task using a bridge sensor. An error will occur if not all virtual channels in the task support this operation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformBridgeShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, double bridgeResistance)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | Specifies the shunt resistance, in ohms. |
| shuntResistorLocation | ShuntElementLocation | Specifies the location of the shunt resistor. |
| bridgeResistance | double | Specifies the bridge resistance, in ohms. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-bool.html language=enus -->
## TOPIC 00173: PerformStrainShuntCalibration(double, ShuntElementLocation, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the virtual channels in the task using a strain gage sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, [MarshalAs(UnmanagedType.U1)] bool skipUnsupportedCha

### PerformStrainShuntCalibration(double, ShuntElementLocation, bool)

Performs shunt calibration for the virtual channels in the task using a strain gage sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, [MarshalAs(UnmanagedType.U1)] bool skipUnsupportedChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | Specifies the shunt resistance, in ohms. |
| shuntResistorLocation | ShuntElementLocation | Specifies the location of the shunt resistor. |
| skipUnsupportedChannels | bool | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is true, shunt calibration will be performed only on supported virtual channels in the task. If false, shunt calibration will be performed on all virtual channels in the task, which may result in an error if not all channels support shunt calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-shuntcalibrationselect-shuntresistorsource-bool.html language=enus -->
## TOPIC 00174: PerformStrainShuntCalibration(double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource, bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-shuntcalibrationselect-shuntresistorsource-bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-shuntcalibrationselect-shuntresistorsource-bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the specified channels using a strain gage sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, ShuntCalibrationSelect shuntResistorSelect, ShuntResistorSource

### PerformStrainShuntCalibration(double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource, bool)

Performs shunt calibration for the specified channels using a strain gage sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, ShuntCalibrationSelect shuntResistorSelect, ShuntResistorSource shuntResistorSource, [MarshalAs(UnmanagedType.U1)] bool skipUnsupportedChannels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | The resistance, in ohms, of the shunt resistor. |
| shuntResistorLocation | ShuntElementLocation | The location of the shunt resistor. |
| shuntResistorSelect | ShuntCalibrationSelect | The shunt calibration switch to use. |
| shuntResistorSource | ShuntResistorSource | The shunt resistor to use. |
| skipUnsupportedChannels | bool | Specifies whether or not to skip channels that do not support shunt calibration. If skipUnsupportedChannels is true, shunt calibration is performed only on supported channels. If false, shunt calibration is performed on channels specified by channelNames . The default is false. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-shuntcalibrationselect-shuntresistorsource.html language=enus -->
## TOPIC 00175: PerformStrainShuntCalibration(double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-shuntcalibrationselect-shuntresistorsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation-shuntcalibrationselect-shuntresistorsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the specified channels using a strain gage sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, ShuntCalibrationSelect shuntResistorSelect, ShuntResistorSource

### PerformStrainShuntCalibration(double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource)

Performs shunt calibration for the specified channels using a strain gage sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation, ShuntCalibrationSelect shuntResistorSelect, ShuntResistorSource shuntResistorSource)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | The resistance, in ohms, of the shunt resistor. |
| shuntResistorLocation | ShuntElementLocation | The location of the shunt resistor. |
| shuntResistorSelect | ShuntCalibrationSelect | The shunt calibration switch to use. |
| shuntResistorSource | ShuntResistorSource | The shunt resistor to use. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation.html language=enus -->
## TOPIC 00176: PerformStrainShuntCalibration(double, ShuntElementLocation)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performstrainshuntcalibration__double-shuntelementlocation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs shunt calibration for the virtual channels in the task using a strain gage sensor. An error will occur if not all virtual channels in the task support this operation. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementL

### PerformStrainShuntCalibration(double, ShuntElementLocation)

Performs shunt calibration for the virtual channels in the task using a strain gage sensor. An error will occur if not all virtual channels in the task support this operation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformStrainShuntCalibration(double shuntResistorValue, ShuntElementLocation shuntResistorLocation)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| shuntResistorValue | double | Specifies the shunt resistance, in ohms. |
| shuntResistorLocation | ShuntElementLocation | Specifies the location of the shunt resistor. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performthermocoupleleadoffsetnullingcalibration.html language=enus -->
## TOPIC 00177: PerformThermocoupleLeadOffsetNullingCalibration()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performthermocoupleleadoffsetnullingcalibration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performthermocoupleleadoffsetnullingcalibration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. An error will occur if not all virtual channels in the task support this operation. SyntaxNamespace: NationalInstruments.DAQmxpublic void PerformTher

### PerformThermocoupleLeadOffsetNullingCalibration()

Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. An error will occur if not all virtual channels in the task support this operation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformThermocoupleLeadOffsetNullingCalibration()

#### Remarks

Keep the measured temperature as constant as possible while performing this adjustment.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-performthermocoupleleadoffsetnullingcalibration__bool.html language=enus -->
## TOPIC 00178: PerformThermocoupleLeadOffsetNullingCalibration(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-performthermocoupleleadoffsetnullingcalibration__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-performthermocoupleleadoffsetnullingcalibration__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Use this method to specify whether or not to skip channels that do not support calibration. SyntaxNamespace: NationalInstruments.DAQmxpublic void Per

### PerformThermocoupleLeadOffsetNullingCalibration(bool)

Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Use this method to specify whether or not to skip channels that do not support calibration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void PerformThermocoupleLeadOffsetNullingCalibration([MarshalAs(UnmanagedType.U1)] bool skipUnsupportedChannels)

#### Remarks

Keep the measured temperature as constant as possible while performing this adjustment.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| skipUnsupportedChannels | bool | Specifies whether or not to skip channels that do not support calibration. If skipUnsupportedChannels is true, calibration will be performed only on supported virtual channels in the task. If false, calibration will be performed on all virtual channels in the task, which may result in an error if not all channels support calibration. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-powercurrentscalingcoefficients.html language=enus -->
## TOPIC 00179: PowerCurrentScalingCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-powercurrentscalingcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-powercurrentscalingcoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the coefficients of the polynomial equation that NI-DAQmx uses to scale values from the native format of the device to amperes. Can be read at any time during a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] PowerCurrentScalingCoefficients { get; }RemarksThis property retu

### PowerCurrentScalingCoefficients

Indicates the coefficients of the polynomial equation that NI-DAQmx uses to scale values from the native format of the device to amperes. Can be read at any time during a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] PowerCurrentScalingCoefficients { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-powercurrentsetpoint.html language=enus -->
## TOPIC 00180: PowerCurrentSetpoint

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-powercurrentsetpoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-powercurrentsetpoint.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output current, in amperes. If the load draws current greater than the specified value, the device will operate in Constant Current mode. SyntaxNamespace: NationalInstruments.DAQmxpublic double PowerCurrentSetpoint { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExce

### PowerCurrentSetpoint

Specifies the output current, in amperes. If the load draws current greater than the specified value, the device will operate in Constant Current mode.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PowerCurrentSetpoint { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-poweridleoutputbehavior.html language=enus -->
## TOPIC 00181: PowerIdleOutputBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-poweridleoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-poweridleoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to disable the output or maintain the existing value after the task is uncommitted. SyntaxNamespace: NationalInstruments.DAQmxpublic PowerIdleOutputBehavior PowerIdleOutputBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retur

### PowerIdleOutputBehavior

Specifies whether to disable the output or maintain the existing value after the task is uncommitted.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [PowerIdleOutputBehavior](nationalinstruments-daqmx-poweridleoutputbehavior.html) PowerIdleOutputBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-poweroutputenable.html language=enus -->
## TOPIC 00182: PowerOutputEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-poweroutputenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-poweroutputenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable or disable power module output. Can be set while a task is running. Can be read at any time during a task. When a task is running, the output is enabled immediately. Otherwise, the output is not enabled until the task enters the Committed state. SyntaxNamespace: NationalI

### PowerOutputEnable

Specifies whether to enable or disable power module output. Can be set while a task is running. Can be read at any time during a task. When a task is running, the output is enabled immediately. Otherwise, the output is not enabled until the task enters the Committed state.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PowerOutputEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-poweroutputstate.html language=enus -->
## TOPIC 00183: PowerOutputState

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-poweroutputstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-poweroutputstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates power channel operating state. Can be read at any time during a task. SyntaxNamespace: NationalInstruments.DAQmxpublic PowerOutputState PowerOutputState { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PowerOutputState

Indicates power channel operating state. Can be read at any time during a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [PowerOutputState](nationalinstruments-daqmx-poweroutputstate.html) PowerOutputState { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-powerremotesense.html language=enus -->
## TOPIC 00184: PowerRemoteSense

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-powerremotesense.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-powerremotesense.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use local or remote sense to sense the output voltage. DAQmx Read (Power Supply) will return remote or local voltage based on the Remote Sense attribute value. Reading this property will return the user-defined value. SyntaxNamespace: NationalInstruments.DAQmxpublic Sense PowerR

### PowerRemoteSense

Specifies whether to use local or remote sense to sense the output voltage. [DAQmx](nationalinstruments-daqmx.html) Read (Power Supply) will return remote or local voltage based on the Remote Sense attribute value. Reading this property will return the user-defined value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [Sense](nationalinstruments-daqmx-sense.html) PowerRemoteSense { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-powersupplyfaultdetectenable.html language=enus -->
## TOPIC 00185: PowerSupplyFaultDetectEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-powersupplyfaultdetectenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-powersupplyfaultdetectenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable power supply fault detection. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PowerSupplyFaultDetectEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PowerSupplyFaultDetectEnable

Specifies whether to enable power supply fault detection.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PowerSupplyFaultDetectEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-powervoltagescalingcoefficients.html language=enus -->
## TOPIC 00186: PowerVoltageScalingCoefficients

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-powervoltagescalingcoefficients.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-powervoltagescalingcoefficients.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the coefficients of the polynomial equation that NI-DAQmx uses to scale values from the native format of the device to volts. Can be read at any time during a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double[] PowerVoltageScalingCoefficients { get; }RemarksThis property return

### PowerVoltageScalingCoefficients

Indicates the coefficients of the polynomial equation that NI-DAQmx uses to scale values from the native format of the device to volts. Can be read at any time during a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double[] PowerVoltageScalingCoefficients { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-powervoltagesetpoint.html language=enus -->
## TOPIC 00187: PowerVoltageSetpoint

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-powervoltagesetpoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-powervoltagesetpoint.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the constant output voltage, in volts. Can be set while a task is running. Can be read at any time during a task. SyntaxNamespace: NationalInstruments.DAQmxpublic double PowerVoltageSetpoint { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver ret

### PowerVoltageSetpoint

Specifies the constant output voltage, in volts. Can be set while a task is running. Can be read at any time during a task.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PowerVoltageSetpoint { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-pressureunits.html language=enus -->
## TOPIC 00188: PressureUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-pressureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-pressureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return pressure measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIPressureUnits PressureUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PressureUnits

Specifies in which unit to return pressure measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIPressureUnits](nationalinstruments-daqmx-aipressureunits.html) PressureUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-probeattenuation.html language=enus -->
## TOPIC 00189: ProbeAttenuation

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-probeattenuation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-probeattenuation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the amount of attenuation provided by the probe connected to the channel. Specify this attenuation as a ratio. SyntaxNamespace: NationalInstruments.DAQmxpublic double ProbeAttenuation { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned a

### ProbeAttenuation

Specifies the amount of attenuation provided by the probe connected to the channel. Specify this attenuation as a ratio.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ProbeAttenuation { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rangehigh.html language=enus -->
## TOPIC 00190: RangeHigh

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rangehigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rangehigh.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the upper limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. SyntaxNamespace: NationalInstruments.DAQmxpublic double RangeHigh { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.

### RangeHigh

Specifies the upper limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RangeHigh { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rangelow.html language=enus -->
## TOPIC 00191: RangeLow

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rangelow.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rangelow.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lower limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. SyntaxNamespace: NationalInstruments.DAQmxpublic double RangeLow { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.D

### RangeLow

Specifies the lower limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RangeLow { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rawdatacompressiontype.html language=enus -->
## TOPIC 00192: RawDataCompressionType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rawdatacompressiontype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rawdatacompressiontype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of compression to apply to raw samples returned from the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AIRawDataCompressionType RawDataCompressionType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RawDataCompressionType

Specifies the type of compression to apply to [raw samples](/csh?context=nidaqmx_mxcncpts_rawdata) returned from the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIRawDataCompressionType](nationalinstruments-daqmx-airawdatacompressiontype.html) RawDataCompressionType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rawsamplejustification.html language=enus -->
## TOPIC 00193: RawSampleJustification

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rawsamplejustification.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rawsamplejustification.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the justification of a raw sample from the device. SyntaxNamespace: NationalInstruments.DAQmxpublic AIRawSampleJustification RawSampleJustification { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RawSampleJustification

Indicates the justification of a [raw sample](/csh?context=nidaqmx_mxcncpts_rawdata) from the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIRawSampleJustification](nationalinstruments-daqmx-airawsamplejustification.html) RawSampleJustification { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rawsamplesize.html language=enus -->
## TOPIC 00194: RawSampleSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rawsamplesize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rawsamplesize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates in bits the size of a raw sample from the device. SyntaxNamespace: NationalInstruments.DAQmxpublic long RawSampleSize { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RawSampleSize

Indicates in bits the size of a [raw sample](/csh?context=nidaqmx_mxcncpts_rawdata) from the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long RawSampleSize { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-readopenchannels.html language=enus -->
## TOPIC 00195: ReadOpenChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-readopenchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-readopenchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of names of any open virtual channels. You must read ReadOpenChannelsExist before you read this property. Otherwise you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] ReadOpenChannels { get; }RemarksThis property returns a copy of the actual array.

### ReadOpenChannels

Indicates a list of names of any open virtual channels. You must read [ReadOpenChannelsExist](nationalinstruments-daqmx-aichannel-readopenchannelsexist.html) before you read this property. Otherwise you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadOpenChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-readopenchannelsdetails.html language=enus -->
## TOPIC 00196: ReadOpenChannelsDetails

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-readopenchannelsdetails.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-readopenchannelsdetails.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates a list of details of any open virtual channels. You must read ReadOpenChannelsExist before you read this property. Otherwise you will receive an error. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] ReadOpenChannelsDetails { get; }RemarksThis property returns a copy of the actua

### ReadOpenChannelsDetails

Indicates a list of details of any open virtual channels. You must read [ReadOpenChannelsExist](nationalinstruments-daqmx-aichannel-readopenchannelsexist.html) before you read this property. Otherwise you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] ReadOpenChannelsDetails { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-readopenchannelsexist.html language=enus -->
## TOPIC 00197: ReadOpenChannelsExist

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-readopenchannelsexist.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-readopenchannelsexist.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before you read ReadOpenChannels. Otherwise, you will receive an error. SyntaxName

### ReadOpenChannelsExist

Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before you read [ReadOpenChannels](nationalinstruments-daqmx-aichannel-readopenchannels.html). Otherwise, you will receive an error.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool ReadOpenChannelsExist { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-removefilterdelay.html language=enus -->
## TOPIC 00198: RemoveFilterDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-removefilterdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-removefilterdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if filter delay removal is enabled on the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool RemoveFilterDelay { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RemoveFilterDelay

Specifies if filter delay removal is enabled on the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool RemoveFilterDelay { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-resistanceconfiguration.html language=enus -->
## TOPIC 00199: ResistanceConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-resistanceconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-resistanceconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD. SyntaxNamespace: NationalInstruments.DAQmxpublic AIResistanceConfiguration ResistanceConfiguration { get; set; }Excepti

### ResistanceConfiguration

Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIResistanceConfiguration](nationalinstruments-daqmx-airesistanceconfiguration.html) ResistanceConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-resistanceunits.html language=enus -->
## TOPIC 00200: ResistanceUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-resistanceunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-resistanceunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return resistance measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic AIResistanceUnits ResistanceUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ResistanceUnits

Specifies the units to use to return resistance measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIResistanceUnits](nationalinstruments-daqmx-airesistanceunits.html) ResistanceUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-resolution.html language=enus -->
## TOPIC 00201: Resolution

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-resolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-resolution.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the resolution of the analog-to-digital converter of the channel. This value is in the units you specify with ResolutionUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double Resolution { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver retur

### Resolution

Indicates the resolution of the analog-to-digital converter of the channel. This value is in the units you specify with [ResolutionUnits](nationalinstruments-daqmx-aichannel-resolutionunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Resolution { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-resolutionunits.html language=enus -->
## TOPIC 00202: ResolutionUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-resolutionunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-resolutionunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the units of Resolution. SyntaxNamespace: NationalInstruments.DAQmxpublic AIResolutionUnits ResolutionUnits { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ResolutionUnits

Indicates the units of [Resolution](nationalinstruments-daqmx-aichannel-resolution.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIResolutionUnits](nationalinstruments-daqmx-airesolutionunits.html) ResolutionUnits { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rosettemeasurementtype.html language=enus -->
## TOPIC 00203: RosetteMeasurementType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rosettemeasurementtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rosettemeasurementtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of rosette measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic AIRosetteMeasurementType RosetteMeasurementType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RosetteMeasurementType

Specifies the type of rosette measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIRosetteMeasurementType](nationalinstruments-daqmx-airosettemeasurementtype.html) RosetteMeasurementType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rosettestrainchannels.html language=enus -->
## TOPIC 00204: RosetteStrainChannels

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rosettestrainchannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rosettestrainchannels.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the raw strain channels that comprise the strain rosette. SyntaxNamespace: NationalInstruments.DAQmxpublic string[] RosetteStrainChannels { get; }RemarksThis property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iterat

### RosetteStrainChannels

Indicates the raw strain channels that comprise the strain rosette.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string[] RosetteStrainChannels { get; }

#### Remarks

This property returns a copy of the actual array. Avoid calling this property within a for loop because it creates a copy for each iteration of the loop. Avoid using an indexer to set a member of the array because the indexer returns a copy of the object and has no effect on the actual object.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rosettestraingageorientation.html language=enus -->
## TOPIC 00205: RosetteStrainGageOrientation

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rosettestraingageorientation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rosettestraingageorientation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies gage orientation in degrees with respect to the X axis. SyntaxNamespace: NationalInstruments.DAQmxpublic double RosetteStrainGageOrientation { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RosetteStrainGageOrientation

Specifies gage orientation in degrees with respect to the X axis.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RosetteStrainGageOrientation { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rosettetype.html language=enus -->
## TOPIC 00206: RosetteType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rosettetype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rosettetype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the type of rosette gage. SyntaxNamespace: NationalInstruments.DAQmxpublic AIRosetteType RosetteType { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RosetteType

Indicates the type of rosette gage.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIRosetteType](nationalinstruments-daqmx-airosettetype.html) RosetteType { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rtda.html language=enus -->
## TOPIC 00207: RtdA

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rtda.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rtda.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 'A' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD. SyntaxNamespace: NationalInstruments.DAQmxpublic double RtdA { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RtdA

Specifies the 'A' constant of the [Callendar-Van Dusen equation](/csh?context=nidaqmx_measfunds_callendarvandusen). NI-DAQmx requires this value when you use a custom RTD.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RtdA { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rtdb.html language=enus -->
## TOPIC 00208: RtdB

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rtdb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rtdb.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 'B' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD. SyntaxNamespace: NationalInstruments.DAQmxpublic double RtdB { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RtdB

Specifies the 'B' constant of the [Callendar-Van Dusen equation](/csh?context=nidaqmx_measfunds_callendarvandusen). NI-DAQmx requires this value when you use a custom RTD.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RtdB { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rtdc.html language=enus -->
## TOPIC 00209: RtdC

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rtdc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rtdc.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 'C' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD. SyntaxNamespace: NationalInstruments.DAQmxpublic double RtdC { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RtdC

Specifies the 'C' constant of the [Callendar-Van Dusen equation](/csh?context=nidaqmx_measfunds_callendarvandusen). NI-DAQmx requires this value when you use a custom RTD.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RtdC { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rtdr0.html language=enus -->
## TOPIC 00210: RtdR0

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rtdr0.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rtdr0.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the sensor resistance at 0 deg C. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double RtdR0 { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExcept

### RtdR0

Specifies in ohms the sensor resistance at 0 deg C. The [Callendar-Van Dusen equation](/csh?context=nidaqmx_measfunds_callendarvandusen) requires this value. Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RtdR0 { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rtdtype.html language=enus -->
## TOPIC 00211: RtdType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rtdtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rtdtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of RTD connected to the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIRtdType RtdType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RtdType

Specifies the [type](/csh?context=nidaqmx_measfunds_rtd) of RTD connected to the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIRtdType](nationalinstruments-daqmx-airtdtype.html) RtdType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rvdtsensitivity.html language=enus -->
## TOPIC 00212: RvdtSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rvdtsensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rvdtsensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the RVDT. This value is in the units you specify with RvdtSensitivityUnits. Refer to the sensor documentation to determine this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double RvdtSensitivity { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.

### RvdtSensitivity

Specifies the sensitivity of the [RVDT](/csh?context=nidaqmx_measfunds_rvdts). This value is in the units you specify with [RvdtSensitivityUnits](nationalinstruments-daqmx-aichannel-rvdtsensitivityunits.html). Refer to the sensor documentation to determine this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double RvdtSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rvdtsensitivityunits.html language=enus -->
## TOPIC 00213: RvdtSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rvdtsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rvdtsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of RvdtSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AIRvdtSensitivityUnits RvdtSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RvdtSensitivityUnits

Specifies the units of [RvdtSensitivity](nationalinstruments-daqmx-aichannel-rvdtsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIRvdtSensitivityUnits](nationalinstruments-daqmx-airvdtsensitivityunits.html) RvdtSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-rvdtunits.html language=enus -->
## TOPIC 00214: RvdtUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-rvdtunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-rvdtunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return angular position measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIRvdtUnits RvdtUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### RvdtUnits

Specifies the units to use to return angular position measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIRvdtUnits](nationalinstruments-daqmx-airvdtunits.html) RvdtUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-sampleandholdenable.html language=enus -->
## TOPIC 00215: SampleAndHoldEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-sampleandholdenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-sampleandholdenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the sample and hold circuitry of the device. When you disable sample and hold circuitry, a small voltage offset might be introduced into the signal. You can eliminate this offset by using AutoZeroMode to perform an auto zero on the channel. SyntaxNamespace: NationalInstru

### SampleAndHoldEnable

Specifies whether to enable the sample and hold circuitry of the device. When you disable sample and hold circuitry, a small voltage offset might be introduced into the signal. You can eliminate this offset by using [AutoZeroMode](nationalinstruments-daqmx-aichannel-autozeromode.html) to perform an auto zero on the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SampleAndHoldEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-sensorpowerconfiguration.html language=enus -->
## TOPIC 00216: SensorPowerConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-sensorpowerconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-sensorpowerconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged. SyntaxNamespace: NationalInstruments.DAQmxpublic AISensorPowerConfiguration SensorPowerConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### SensorPowerConfiguration

Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AISensorPowerConfiguration](nationalinstruments-daqmx-aisensorpowerconfiguration.html) SensorPowerConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-sensorpowertype.html language=enus -->
## TOPIC 00217: SensorPowerType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-sensorpowertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-sensorpowertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of power supplied to the sensor. SyntaxNamespace: NationalInstruments.DAQmxpublic AISensorPowerType SensorPowerType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SensorPowerType

Specifies the type of power supplied to the sensor.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AISensorPowerType](nationalinstruments-daqmx-aisensorpowertype.html) SensorPowerType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-sensorpowervoltage.html language=enus -->
## TOPIC 00218: SensorPowerVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-sensorpowervoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-sensorpowervoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level for the sensor's power supply. SyntaxNamespace: NationalInstruments.DAQmxpublic double SensorPowerVoltage { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SensorPowerVoltage

Specifies the voltage level for the sensor's power supply.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SensorPowerVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-soundpressuredecibelreference.html language=enus -->
## TOPIC 00219: SoundPressureDecibelReference

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-soundpressuredecibelreference.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-soundpressuredecibelreference.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. NI-DAQmx also uses the decibel reference level when converting MaximumSoundPressureLevel to a voltage level. SyntaxNamespace: Na

### SoundPressureDecibelReference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. NI-DAQmx also uses the decibel reference level when converting [MaximumSoundPressureLevel](nationalinstruments-daqmx-aichannel-maximumsoundpressurelevel.html) to a voltage level.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SoundPressureDecibelReference { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-soundpressureunits.html language=enus -->
## TOPIC 00220: SoundPressureUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-soundpressureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-soundpressureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return sound pressure measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AISoundPressureUnits SoundPressureUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SoundPressureUnits

Specifies the units to use to return sound pressure measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AISoundPressureUnits](nationalinstruments-daqmx-aisoundpressureunits.html) SoundPressureUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-straingageconfiguration.html language=enus -->
## TOPIC 00221: StrainGageConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-straingageconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-straingageconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bridge configuration of the strain gages. SyntaxNamespace: NationalInstruments.DAQmxpublic AIStrainGageConfiguration StrainGageConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### StrainGageConfiguration

Specifies the [bridge configuration](/csh?context=nidaqmx_measfunds_bridgeconfig) of the strain gages.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIStrainGageConfiguration](nationalinstruments-daqmx-aistraingageconfiguration.html) StrainGageConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-straingagegagefactor.html language=enus -->
## TOPIC 00222: StrainGageGageFactor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-straingagegagefactor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-straingagegagefactor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the strain gage. Gage factor relates the change in electrical resistance to the change in strain. Refer to the sensor documentation for this value. SyntaxNamespace: NationalInstruments.DAQmxpublic double StrainGageGageFactor { get; set; }ExceptionsTypeDescriptionNational

### StrainGageGageFactor

Specifies the sensitivity of the strain gage. Gage factor relates the change in electrical resistance to the change in strain. Refer to the sensor documentation for this value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double StrainGageGageFactor { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-straingagepoissonratio.html language=enus -->
## TOPIC 00223: StrainGagePoissonRatio

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-straingagepoissonratio.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-straingagepoissonratio.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of lateral strain to axial strain in the material you are measuring. SyntaxNamespace: NationalInstruments.DAQmxpublic double StrainGagePoissonRatio { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### StrainGagePoissonRatio

Specifies the ratio of lateral strain to axial strain in the material you are measuring.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double StrainGagePoissonRatio { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-strainunits.html language=enus -->
## TOPIC 00224: StrainUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-strainunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-strainunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return strain measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIStrainUnits StrainUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### StrainUnits

Specifies the units to use to return strain measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIStrainUnits](nationalinstruments-daqmx-aistrainunits.html) StrainUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-tedsunits.html language=enus -->
## TOPIC 00225: TedsUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-tedsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-tedsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the units defined by TEDS information associated with the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string TedsUnits { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TedsUnits

Indicates the units defined by TEDS information associated with the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string TedsUnits { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-temperatureunits.html language=enus -->
## TOPIC 00226: TemperatureUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-temperatureunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-temperatureunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return temperature measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AITemperatureUnits TemperatureUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TemperatureUnits

Specifies the units to use to return temperature measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AITemperatureUnits](nationalinstruments-daqmx-aitemperatureunits.html) TemperatureUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-terminalconfiguration.html language=enus -->
## TOPIC 00227: TerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-terminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-terminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal configuration for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AITerminalConfiguration TerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TerminalConfiguration

Specifies the terminal configuration for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AITerminalConfiguration](nationalinstruments-daqmx-aiterminalconfiguration.html) TerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermistora.html language=enus -->
## TOPIC 00228: ThermistorA

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermistora.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermistora.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 'A' constant of the Steinhart-Hart thermistor equation. SyntaxNamespace: NationalInstruments.DAQmxpublic double ThermistorA { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ThermistorA

Specifies the 'A' constant of the [Steinhart-Hart thermistor equation](/csh?context=nidaqmx_measfunds_thermistors).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ThermistorA { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermistorb.html language=enus -->
## TOPIC 00229: ThermistorB

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermistorb.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermistorb.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 'B' constant of the Steinhart-Hart thermistor equation. SyntaxNamespace: NationalInstruments.DAQmxpublic double ThermistorB { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ThermistorB

Specifies the 'B' constant of the [Steinhart-Hart thermistor equation](/csh?context=nidaqmx_measfunds_thermistors).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ThermistorB { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermistorc.html language=enus -->
## TOPIC 00230: ThermistorC

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermistorc.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermistorc.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 'C' constant of the Steinhart-Hart thermistor equation. SyntaxNamespace: NationalInstruments.DAQmxpublic double ThermistorC { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ThermistorC

Specifies the 'C' constant of the [Steinhart-Hart thermistor equation](/csh?context=nidaqmx_measfunds_thermistors).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ThermistorC { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermistorr1.html language=enus -->
## TOPIC 00231: ThermistorR1

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermistorr1.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermistorr1.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in ohms the value of the reference resistor for the thermistor if you use voltage excitation. NI-DAQmx ignores this value for current excitation. SyntaxNamespace: NationalInstruments.DAQmxpublic double ThermistorR1 { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptio

### ThermistorR1

Specifies in ohms the value of the reference resistor for the [thermistor](/csh?context=nidaqmx_measfunds_thermistors) if you use voltage excitation. NI-DAQmx ignores this value for current excitation.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ThermistorR1 { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermocouplecjcchannel.html language=enus -->
## TOPIC 00232: ThermocoupleCjcChannel

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermocouplecjcchannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermocouplecjcchannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the channel that acquires the temperature of the cold junction if ThermocoupleCjcSource is Channel. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom sca

### ThermocoupleCjcChannel

Indicates the channel that acquires the temperature of the [cold junction](/csh?context=nidaqmx_measfunds_sigcontherm) if [ThermocoupleCjcSource](nationalinstruments-daqmx-aichannel-thermocouplecjcsource.html) is [Channel](nationalinstruments-daqmx-aithermocouplecjcsource.html). If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string ThermocoupleCjcChannel { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermocouplecjcsource.html language=enus -->
## TOPIC 00233: ThermocoupleCjcSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermocouplecjcsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermocouplecjcsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the source of cold-junction compensation. SyntaxNamespace: NationalInstruments.DAQmxpublic AIThermocoupleCjcSource ThermocoupleCjcSource { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ThermocoupleCjcSource

Indicates the source of [cold-junction compensation](/csh?context=nidaqmx_measfunds_sigcontherm).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIThermocoupleCjcSource](nationalinstruments-daqmx-aithermocouplecjcsource.html) ThermocoupleCjcSource { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermocouplecjcvalue.html language=enus -->
## TOPIC 00234: ThermocoupleCjcValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermocouplecjcvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermocouplecjcvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature of the cold junction if ThermocoupleCjcSource is ConstantValue. Specify this value in the units of the measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic double ThermocoupleCjcValue { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe N

### ThermocoupleCjcValue

Specifies the temperature of the [cold junction](/csh?context=nidaqmx_measfunds_sigcontherm) if [ThermocoupleCjcSource](nationalinstruments-daqmx-aichannel-thermocouplecjcsource.html) is [ConstantValue](nationalinstruments-daqmx-aithermocouplecjcsource.html). Specify this value in the units of the measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ThermocoupleCjcValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermocoupleleadoffsetvoltage.html language=enus -->
## TOPIC 00235: ThermocoupleLeadOffsetVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermocoupleleadoffsetvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermocoupleleadoffsetvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lead offset nulling voltage to subtract from measurements on a device. This property is ignored if open thermocouple detection is disabled. SyntaxNamespace: NationalInstruments.DAQmxpublic double ThermocoupleLeadOffsetVoltage { get; set; }ExceptionsTypeDescriptionNationalInstruments.DA

### ThermocoupleLeadOffsetVoltage

Specifies the [lead offset nulling](/csh?context=nidaqmx_mxdevconsid_openthermdet) voltage to subtract from measurements on a device. This property is ignored if open thermocouple detection is disabled.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double ThermocoupleLeadOffsetVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermocouplescaletype.html language=enus -->
## TOPIC 00236: ThermocoupleScaleType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermocouplescaletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermocouplescaletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method or equation form that the thermocouple scale uses. SyntaxNamespace: NationalInstruments.DAQmxpublic AIThermocoupleScaleType ThermocoupleScaleType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### ThermocoupleScaleType

Specifies the method or equation form that the thermocouple scale uses.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIThermocoupleScaleType](nationalinstruments-daqmx-aithermocouplescaletype.html) ThermocoupleScaleType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-thermocoupletype.html language=enus -->
## TOPIC 00237: ThermocoupleType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-thermocoupletype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-thermocoupletype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. SyntaxNamespace: NationalInstruments.DAQmxpublic AIThermocoupleType ThermocoupleType { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### ThermocoupleType

Specifies the [type](/csh?context=nidaqmx_measfunds_thermocouples) of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIThermocoupleType](nationalinstruments-daqmx-aithermocoupletype.html) ThermocoupleType { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-torqueunits.html language=enus -->
## TOPIC 00238: TorqueUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-torqueunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-torqueunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return torque measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AITorqueUnits TorqueUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TorqueUnits

Specifies in which unit to return torque measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AITorqueUnits](nationalinstruments-daqmx-aitorqueunits.html) TorqueUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-usbtransferrequestcount.html language=enus -->
## TOPIC 00239: UsbTransferRequestCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-usbtransferrequestcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-usbtransferrequestcount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. SyntaxNamespace: NationalInstruments.DAQmxpublic long UsbTransferRequestCount { get; set; }ExceptionsTypeDescriptionNat

### UsbTransferRequestCount

Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long UsbTransferRequestCount { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-usbtransferrequestsize.html language=enus -->
## TOPIC 00240: UsbTransferRequestSize

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-usbtransferrequestsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-usbtransferrequestsize.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. SyntaxNamespace: NationalInstruments.DAQmxpublic long UsbTransferRequestSize { get; set; }ExceptionsTypeDescriptionNationalInstruments.D

### UsbTransferRequestSize

Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long UsbTransferRequestSize { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-useexcitationforscaling.html language=enus -->
## TOPIC 00241: UseExcitationForScaling

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-useexcitationforscaling.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-useexcitationforscaling.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set this property to true for ratiometric transducers. If you set this property to true, set Maximum and Minimum to reflect the scaling. SyntaxNamespace: NationalInstruments.DAQmxpublic bool UseExcitationForScaling

### UseExcitationForScaling

Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set this property to true for ratiometric transducers. If you set this property to true, set [Maximum](nationalinstruments-daqmx-aichannel-maximum.html) and [Minimum](nationalinstruments-daqmx-aichannel-minimum.html) to reflect the scaling.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool UseExcitationForScaling { get; set; }

#### Remarks

For example, if you expect to acquire a voltage between -5 and 5, and you use an excitation of .10 volts to scale the measurement, set [Minimum](nationalinstruments-daqmx-aichannel-minimum.html) to -50 and set [Maximum](nationalinstruments-daqmx-aichannel-maximum.html) to 50. If you set [BridgeConfiguration](nationalinstruments-daqmx-aichannel-bridgeconfiguration.html) to [NoBridge](nationalinstruments-daqmx-aibridgeconfiguration.html), this property has no effect on the measurement.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-usemultiplexedexcitation.html language=enus -->
## TOPIC 00242: UseMultiplexedExcitation

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-usemultiplexedexcitation.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-usemultiplexedexcitation.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the SCXI-1122 multiplexes the excitation to the upper half of the channels as it advances through the scan list. SyntaxNamespace: NationalInstruments.DAQmxpublic bool UseMultiplexedExcitation { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver

### UseMultiplexedExcitation

Specifies if the SCXI-1122 multiplexes the excitation to the upper half of the channels as it advances through the scan list.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool UseMultiplexedExcitation { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-velocityiepesensordecibelreference.html language=enus -->
## TOPIC 00243: VelocityIepeSensorDecibelReference

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-velocityiepesensordecibelreference.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-velocityiepesensordecibelreference.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. SyntaxNamespace: NationalInstruments.DAQmxpublic double VelocityIepeSensorDecibelReference { get; set; }ExceptionsTypeDescriptio

### VelocityIepeSensorDecibelReference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double VelocityIepeSensorDecibelReference { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivity.html language=enus -->
## TOPIC 00244: VelocityIepeSensorSensitivity

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sensitivity of the IEPE velocity sensor connected to the channel. Specify this value in the unit indicated by VelocityIepeSensorSensitivityUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double VelocityIepeSensorSensitivity { get; set; }ExceptionsTypeDescriptionNationalInstrume

### VelocityIepeSensorSensitivity

Specifies the sensitivity of the IEPE velocity sensor connected to the channel. Specify this value in the unit indicated by [VelocityIepeSensorSensitivityUnits](nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivityunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double VelocityIepeSensorSensitivity { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivityunits.html language=enus -->
## TOPIC 00245: VelocityIepeSensorSensitivityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for VelocityIepeSensorSensitivity. SyntaxNamespace: NationalInstruments.DAQmxpublic AIVelocityIepeSensorSensitivityUnits VelocityIepeSensorSensitivityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### VelocityIepeSensorSensitivityUnits

Specifies the units for [VelocityIepeSensorSensitivity](nationalinstruments-daqmx-aichannel-velocityiepesensorsensitivity.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIVelocityIepeSensorSensitivityUnits](nationalinstruments-daqmx-aivelocityiepesensorsensitivityunits.html) VelocityIepeSensorSensitivityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-velocityunits.html language=enus -->
## TOPIC 00246: VelocityUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-velocityunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-velocityunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in which unit to return velocity measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIVelocityUnits VelocityUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### VelocityUnits

Specifies in which unit to return velocity measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIVelocityUnits](nationalinstruments-daqmx-aivelocityunits.html) VelocityUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-voltageacrmsunits.html language=enus -->
## TOPIC 00247: VoltageAcrmsUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-voltageacrmsunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-voltageacrmsunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return voltage RMS measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIVoltageAcrmsUnits VoltageAcrmsUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### VoltageAcrmsUnits

Specifies the units to use to return voltage RMS measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIVoltageAcrmsUnits](nationalinstruments-daqmx-aivoltageacrmsunits.html) VoltageAcrmsUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-voltagedecibelreference.html language=enus -->
## TOPIC 00248: VoltageDecibelReference

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-voltagedecibelreference.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-voltagedecibelreference.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. SyntaxNamespace: NationalInstruments.DAQmxpublic double VoltageDecibelReference { get; set; }ExceptionsTypeDescriptionNationalIn

### VoltageDecibelReference

Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double VoltageDecibelReference { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel-voltageunits.html language=enus -->
## TOPIC 00249: VoltageUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel-voltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel-voltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return voltage measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic AIVoltageUnits VoltageUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### VoltageUnits

Specifies the units to use to return voltage measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [AIVoltageUnits](nationalinstruments-daqmx-aivoltageunits.html) VoltageUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

AIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aichannel.html language=enus -->
## TOPIC 00250: AIChannel Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aichannel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aichannel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Encapsulates one or more analog input virtual channels and the properties for an analog input virtual channel. Derives fromChannelIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class AIChannel : Channel, IFilteredTypeDescriptorRemarksUse the AIChannels property to create or

### AIChannel Class

Encapsulates one or more analog input virtual channels and the properties for an analog input virtual channel.

#### Derives from

- Channel
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class AIChannel : Channel, IFilteredTypeDescriptor

#### Remarks

AIChannels

AIChannel

AIChannel

AIChannels

AIChannelCollection

AIChannel

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| AccelerationChargeSensitivity | Specifies the sensitivity of the charge acceleration sensor connected to the channel. This value is the units you specify with AI.Accel.Charge.SensitivityUnits. Refer to the sensor documentation to determine this value. |
| AccelerationChargeSensitivityUnits | Specifies the units of AI.Accel.Charge.Sensitivity. |
| AccelerationDecibelReference | Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. |
| AccelerationFourWireDCVoltageSensitivity | Specifies the sensitivity of the 4 wire DC voltage acceleration sensor connected to the channel. This value is the units you specify with AI.Accel.4WireDCVoltage.SensitivityUnits. Refer to the sensor documentation to determine this value. |
| AccelerationFourWireDCVoltageSensitivityUnits | Specifies the units of AI.Accel.4WireDCVoltage.Sensitivity. |
| AccelerationUnits | Specifies the units to use to return acceleration measurements from the channel. |
| AccelerometerSensitivity | Specifies the sensitivity of the accelerometer. This value is in the units you specify with AccelerometerSensitivityUnits. Refer to the sensor documentation to determine this value. |
| AccelerometerSensitivityUnits | Specifies the units of AccelerometerSensitivity. |
| ACExcitationFrequency | Specifies the AC excitation frequency in Hertz. |
| ACExcitationSyncEnable | Specifies whether to synchronize the AC excitation source of the channel to that of another channel. Synchronize the excitation sources of multiple channels to use multichannel sensors. Set this property to false for the master channel and to true for the slave channels. |
| ACExcitationWireMode | Specifies the number of leads on the LVDT or RVDT. Some sensors require you to tie leads together to create a four- or five- wire sensor. Refer to the sensor documentation for more information. |
| AdcCustomTimingMode | Specifies the timing mode of the ADC when AdcTimingMode is Custom. |
| AdcTimingMode | Specifies the ADC timing mode, controlling the tradeoff between speed and effective resolution. Some ADC timing modes provide increased powerline noise rejection. On devices that have an AI Convert clock, this setting affects both the maximum and default values for AIConvertRate. You must use the same ADC timing mode for all channels on a device, but you can use different ADC timing modes for different devices in the same task. |
| Attenuation | Specifies the amount of attenuation to use. |
| AutoZeroMode | Specifies how often to measure ground. NI-DAQmx subtracts the measured ground voltage from every sample. |
| AveragingWindowSize | Specifies the number of samples to average while acquiring data. Increasing the number of samples to average reduces noise in your measurement. |
| BridgeBalanceCoarsePot | Specifies by how much to compensate for offset in the signal. This value can be between 0 and 127. |
| BridgeBalanceFinePot | Specifies by how much to compensate for offset in the signal. This value can be between 0 and 4095. |
| BridgeConfiguration | Specifies the type of Wheatstone bridge connected to the channel. |
| BridgeElectricalUnits | Specifies from which electrical unit to scale data. Select the same unit that the sensor data sheet or calibration certificate uses for electrical values. |
| BridgeInitialRatio | Specifies in volts per volt the ratio of output voltage from the bridge to excitation voltage supplied to the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set BridgeInitialVoltage, NI-DAQmx coerces this property to BridgeInitialVoltage divided by ExcitationActualValue. If you set this property, NI-DAQmx coerces BridgeInitialVoltage to the value of this property times ExcitationActualValue. If you set both this property and BridgeInitialVoltage, and their values conflict, NI-DAQmx returns an error. To avoid this error, reset one property to its default value before setting the other. |
| BridgeInitialVoltage | Specifies in volts the output voltage of the bridge while not under load. NI-DAQmx subtracts this value from any measurements before applying scaling equations. If you set BridgeInitialRatio, NI-DAQmx coerces this property to BridgeInitialRatio times ExcitationActualValue. This property is set by DAQmx Perform Bridge Offset Nulling Calibration. If you set this property, NI-DAQmx coerces BridgeInitialRatio to the value of this property divided by ExcitationActualValue. If you set both this property and BridgeInitialRatio, and their values conflict, NI-DAQmx returns an error. To avoid this error, reset one property to its default value before setting the other. |
| BridgeNominalResistance | Specifies in ohms the resistance of the bridge while not under load. |
| BridgePhysicalUnits | Specifies to which physical unit to scale electrical data. Select the same unit that the sensor data sheet or calibration certificate uses for physical values. |
| BridgePolynomialForwardCoefficients | Specifies an array of coefficients for the polynomial that converts electrical values to physical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. |
| BridgePolynomialReverseCoefficients | Specifies an array of coefficients for the polynomial that converts physical values to electrical values. Each element of the array corresponds to a term of the equation. For example, if index three of the array is 9, the fourth term of the equation is 9x^3. |
| BridgeScaleType | Specifies the scaling type to use when scaling electrical values from the sensor to physical units. |
| BridgeShuntCalibrationAActualResistance | Specifies in ohms the actual value of the internal shunt calibration A resistor. |
| BridgeShuntCalibrationAResistance | Specifies in ohms the desired value of the internal shunt calibration A resistor. |
| BridgeShuntCalibrationASource | Specifies whether to use internal or external shunt when Shunt Cal A is selected. |
| BridgeShuntCalibrationBActualResistance | Specifies in ohms the actual value of the internal shunt calibration B resistor. |
| BridgeShuntCalibrationBResistance | Specifies in ohms the desired value of the internal shunt calibration B resistor. |
| BridgeShuntCalibrationEnable | Specifies whether to enable a shunt calibration switch. Use BridgeShuntCalibrationSelect to select the switch(es) to enable. |
| BridgeShuntCalibrationGainAdjust | Specifies the result of a shunt calibration. This property is set by DAQmx Perform Shunt Calibration. NI-DAQmx multiplies data read from the channel by the value of this property. This value should be close to 1.0. |
| BridgeShuntCalibrationSelect | Specifies which shunt calibration switch(es) to enable. Use BridgeShuntCalibrationEnable to enable the switch(es) you specify with this property. |
| BridgeTableElectricalValues | Specifies the array of electrical values that map to the values in BridgeTablePhysicalValues. Specify this value in the unit indicated by BridgeElectricalUnits. |
| BridgeTablePhysicalValues | Specifies the array of physical values that map to the values in BridgeTableElectricalValues. Specify this value in the unit indicated by BridgePhysicalUnits. |
| BridgeTwoPointLinearFirstElectricalValue | Specifies the first electrical value, corresponding to BridgeTwoPointLinearFirstPhysicalValue. Specify this value in the unit indicated by BridgeElectricalUnits. |
| BridgeTwoPointLinearFirstPhysicalValue | Specifies the first physical value, corresponding to BridgeTwoPointLinearFirstElectricalValue. Specify this value in the unit indicated by BridgePhysicalUnits. |
| BridgeTwoPointLinearSecondElectricalValue | Specifies the second electrical value, corresponding to BridgeTwoPointLinearSecondPhysicalValue. Specify this value in the unit indicated by BridgeElectricalUnits. |
| BridgeTwoPointLinearSecondPhysicalValue | Specifies the second physical value, corresponding to BridgeTwoPointLinearSecondElectricalValue. Specify this value in the unit indicated by BridgePhysicalUnits. |
| BridgeUnits | Specifies in which unit to return voltage ratios from the channel. |
| CalculatedPowerCurrentMaximum | Specifies the current maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced current maximum value that the device can measure with the current settings. |
| CalculatedPowerCurrentMinimum | Specifies the current minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced current minimum value that the device can measure with the current settings. |
| CalculatedPowerUnits | Specifies the units to use to return power measurements from the channel. |
| CalculatedPowerVoltageMaximum | Specifies the voltage maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced voltage maximum value that the device can measure with the current settings. |
| CalculatedPowerVoltageMinimum | Specifies the voltage minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced voltage minimum value that the device can measure with the current settings. |
| CalibrationApplyIfExpired | Specifies whether to apply the channel calibration to the channel after the expiration date has passed. |
| CalibrationDate | Gets or sets the last date and time that the channel underwent a channel calibration. |
| CalibrationDescription | Specifies the description entered for the calibration of the channel. |
| CalibrationEnable | Specifies whether to enable the channel calibration associated with the channel. |
| CalibrationExpirationDate | Gets or sets the date and time that the channel calibration expires. |
| CalibrationHasValidInfo | Indicates if the channel has calibration information. |
| CalibrationOperatorName | Specifies the name of the operator who performed the channel calibration. |
| CalibrationPolynomialForwardCoefficients | Specifies the forward polynomial values used for calibrating the channel. |
| CalibrationPolynomialReverseCoefficients | Specifies the reverse polynomial values used for calibrating the channel. |
| CalibrationScaleType | Specifies the method or equation form that the calibration scale uses. |
| CalibrationTablePreScaledValues | Specifies the reference values collected when calibrating the channel. |
| CalibrationTableScaledValues | Specifies the acquired values collected when calibrating the channel. |
| CalibrationVerificationAcquiredValues | Specifies the acquired values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process. |
| CalibrationVerificationReferenceValues | Specifies the reference values collected when verifying the calibration. NI-DAQmx stores these values as a record of calibration accuracy and does not use them in the scaling process. |
| ChargeUnits | Specifies the units to use to return charge measurements from the channel. |
| ChopEnable | Specifies whether the device will chop its inputs. Chopping removes offset voltages and other low frequency errors. |
| Coupling | Specifies the coupling for the channel. |
| CurrentAcrmsUnits | Specifies the units to use to return current RMS measurements from the channel. |
| CurrentShuntLocation | Specifies the shunt resistor location for current measurements. |
| CurrentShuntResistance | Specifies in ohms the external shunt resistance for current measurements. |
| CurrentUnits | Specifies the units to use to return current measurements from the channel. |
| CustomScaleName | Specifies the name of a custom scale for the channel. |
| DataTransferCustomThreshold | Specifies the number of samples that must be in the FIFO to transfer data from the device if DataTransferRequestCondition is OnBoardMemoryCustomThreshold. |
| DataTransferMaximumRate | Specifies the rate in B/s to transfer data from the device. If this value is not set, then the device will transfer data at a rate based on the bus detected. Modify this value to affect performance under different combinations of operating system, configuration, and device. |
| DataTransferMechanism | Specifies the data transfer mode for the device. |
| DataTransferRequestCondition | Specifies under what condition to transfer data from the onboard memory of the device to the buffer. |
| DCOffset | Specifies the DC value to add to the input range of the device. Use RangeHigh and RangeLow to specify the input range. This offset is in the native units of the device . |
| DeviceScalingCoefficients | Indicates the coefficients of a polynomial equation that NI-DAQmx uses to scale values from the native format of the device to volts. Each element of the array corresponds to a term of the equation. For example, if index two of the array is 4, the third term of the equation is 4x^2. Scaling coefficients do not account for any custom scales or sensors contained by the channel. |
| DigitalFilterBandpassCenterFrequency | Specifies the center frequency of the passband for the digital filter. |
| DigitalFilterBandpassWidth | Specifies the width of the passband centered around the center frequency for the digital filter. |
| DigitalFilterCoefficients | Specifies the digital filter coefficients. |
| DigitalFilterEnabled | Specifies whether the digital filter is enabled or disabled. |
| DigitalFilterHighpassCutoffFrequency | Specifies the highpass cutoff frequency of the digital filter. |
| DigitalFilterLowpassCutoffFrequency | Specifies the lowpass cutoff frequency of the digital filter. |
| DigitalFilterNotchCenterFrequency | Specifies the center frequency of the stopband for the digital filter. |
| DigitalFilterNotchWidth | Specifies the width of the stopband centered around the center frequency for the digital filter. |
| DigitalFilterOrder | Specifies the order of the digital filter. |
| DigitalFilterResponse | Specifies the digital filter response. |
| DigitalFilterType | Specifies the digital filter type. |
| DitherEnable | Specifies whether to enable dithering. Dithering adds Gaussian noise to the input signal. You can use dithering to achieve higher resolution measurements by over sampling the input signal and averaging the results. |
| EddyCurrentProximityProbeSensitivity | Specifies the sensitivity of the eddy current proximity probe . This value is in the units you specify with EddyCurrentProximityProbeSensitivityUnits. Refer to the sensor documentation to determine this value. |
| EddyCurrentProximityProbeSensitivityUnits | Specifies the units of EddyCurrentProximityProbeSensitivity. |
| EddyCurrentProximityProbeUnits | Specifies the units to use to return proximity measurements from the channel. |
| EnhancedAliasRejectionEnable | Specifies whether to enable enhanced alias rejection. Leave this property set to the default value for most applications. |
| ExcitationActualValue | Specifies the actual amount of excitation supplied by an internal excitation source. If you read an internal excitation source more precisely with an external device, set this property to the value you read. NI-DAQmx ignores this value for external excitation. When performing shunt calibration, some devices set this property automatically. |
| ExcitationDCOrAC | Specifies if the excitation supply is DC or AC. |
| ExcitationIdleOutputBehavior | Specifies whether this channel will disable excitation after the task is uncommitted. Setting this to Zero Volts or Amps disables excitation after task uncommit. Setting this attribute to Maintain Existing Value leaves the excitation on after task uncommit. |
| ExcitationSense | Specifies whether to use local or remote sense to sense excitation. |
| ExcitationSource | Specifies the source of excitation. |
| ExcitationValue | Specifies the amount of excitation that the sensor requires. If ExcitationVoltageOrCurrent is Voltage, this value is in volts. If ExcitationVoltageOrCurrent is Current, this value is in amperes. |
| ExcitationVoltageOrCurrent | Specifies if the channel uses current or voltage excitation. |
| FilterDelay | Indicates the amount of time between when the ADC samples data and when the sample is read by the host device. This value is in the units you specify with FilterDelayUnits. You can adjust this amount of time using FilterDelayAdjustment. |
| FilterDelayAdjustment | Specifies the amount of filter delay that gets removed if RemoveFilterDelay is enabled. This delay adjustment is in addition to the value indicated by FilterDelay. This delay adjustment is in the units you specify with FilterDelayUnits. |
| FilterDelayUnits | Specifies the units of FilterDelay and FilterDelayAdjustment. |
| FilterEnabled | Specifies the corresponding filter enable/disable state. |
| FilterFrequency | Specifies the corresponding filter frequency (cutoff or center) of the filter response. |
| FilterOrder | Specifies the corresponding filter order and defines the slope of the filter response. |
| FilterResponse | Specifies the corresponding filter response and defines the shape of the filter response. |
| ForceIepeSensorSensitivity | Specifies the sensitivity of the IEPE force sensor connected to the channel. Specify this value in the unit indicated by ForceIepeSensorSensitivityUnits. |
| ForceIepeSensorSensitivityUnits | Specifies the units for ForceIepeSensorSensitivity. |
| ForceReadFromChannel | Specifies whether to read from the channel if it is a cold-junction compensation channel. By default, reading from the task does not return data from cold-junction compensation channels. Setting this property to true forces read operations to return the cold-junction compensation channel data with the other channels in the task. |
| ForceReadFromStrainChannel | Specifies whether the data is returned by reading from the task when set on a raw strain channel that is part of a rosette configuration. |
| ForceUnits | Specifies in which unit to return force or load measurements from the channel. |
| FrequencyHysteresis | Specifies in volts a window below FrequencyThresholdVoltage. The input voltage must pass below FrequencyThresholdVoltage minus this value before NI-DAQmx recognizes a waveform repetition at FrequencyThresholdVoltage. Hysteresis can improve the measurement accuracy when the signal contains noise or jitter. |
| FrequencyThresholdVoltage | Specifies the voltage level at which to recognize waveform repetitions. You should select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. |
| FrequencyUnits | Specifies the units to use to return frequency measurements from the channel. |
| Gain | Specifies a gain factor to apply to the channel. |
| Impedance | Specifies the input impedance of the channel. |
| InputLimitsFaultDetectEnable | Specifies whether to enable input limits fault detection. |
| InputLimitsFaultDetectLowerLimit | Specifies the level of the lower limit for input limits detection. An input sample outside the upper and lower bounds causes a fault. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA. |
| InputLimitsFaultDetectUpperLimit | Specifies the level of the upper limit for input limits detection. An input sample outside the upper and lower bounds causes a fault. Note: Fault detection applies to both positive and negative inputs. For instance, if you specify a lower limit of 2 mA and an upper limit of 12 mA, NI-DAQmx detects a fault at 15 mA and -15 mA, but not at -6 mA because it is in the range of -12 mA to -2 mA. |
| InputSource | Specifies the source of the channel. You can use the signal from the I/O connector or one of several calibration signals. Certain devices have a single calibration signal bus. For these devices, you must specify the same calibration signal for all channels you connect to a calibration signal. |
| IsTeds | Indicates if the virtual channel was initialized using a TEDS bitstream from the corresponding physical channel. |
| LeadWireResistance | Specifies in ohms the resistance of the wires that lead to the sensor. |
| LossyLsbRemovalCompressedSampleSize | Specifies the number of bits to return in a raw sample when RawDataCompressionType is set to LossyLsbRemoval. |
| LowpassCutoffFrequency | Specifies the frequency in Hertz that corresponds to the -3dB cutoff of the filter. |
| LowpassEnable | Specifies whether to enable the lowpass filter of the channel. |
| LowpassSwitchedCapacitorClockSource | Specifies the source of the filter clock. If you need a higher resolution for the filter, you can supply an external clock to increase the resolution. Refer to the SCXI-1141/1142/1143 User Manual for more information. |
| LowpassSwitchedCapacitorExternalClockDivisor | Specifies the divisor for the external clock when you set LowpassSwitchedCapacitorClockSource to External. On the SCXI-1141, SCXI-1142, and SCXI-1143, NI-DAQmx determines the filter cutoff by using the equation f/(100*n), where f is the external frequency, and n is the external clock divisor. Refer to the SCXI-1141/1142/1143 User Manual for more information. |
| LowpassSwitchedCapacitorExternalClockFrequency | Specifies the frequency of the external clock when you set LowpassSwitchedCapacitorClockSource to External. NI-DAQmx uses this frequency to set the pre- and post- filters on the SCXI-1141, SCXI-1142, and SCXI-1143. On those devices, NI-DAQmx determines the filter cutoff by using the equation f/(100*n), where f is the external frequency, and n is the external clock divisor. Refer to the SCXI-1141/1142/1143 User Manual for more information. |
| LowpassSwitchedCapacitorOutputClockDivisor | Specifies the divisor for the output clock. NI-DAQmx uses the cutoff frequency to determine the output clock frequency. Refer to the SCXI-1141/1142/1143 User Manual for more information. |
| LvdtSensitivity | Specifies the sensitivity of the LVDT. This value is in the units you specify with LvdtSensitivityUnits. Refer to the sensor documentation to determine this value. |
| LvdtSensitivityUnits | Specifies the units of LvdtSensitivity. |
| LvdtUnits | Specifies the units to use to return linear position measurements from the channel. |
| Maximum | Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the device can measure with the current settings. |
| MaximumSoundPressureLevel | Specifies the maximum instantaneous sound pressure level you expect to measure. This value is in decibels, referenced to 20 micropascals. NI-DAQmx uses the maximum sound pressure level to calculate values in pascals for Maximum and Minimum for the channel. |
| MeasurementType | Indicates the measurement to take with the analog input channel and in some cases, such as for temperature measurements, the sensor to use. |
| MemoryMappingEnable | Specifies for NI-DAQmx to map hardware registers to the memory space of the application, if possible. Normally, NI-DAQmx maps hardware registers to memory accessible only to the kernel. Mapping the registers to the memory space of the application increases performance. However, if the application accesses the memory space mapped to the registers, it can adversely affect the operation of the device and possibly result in a system crash. |
| MicrophoneSensitivity | Specifies the sensitivity of the microphone. This value is in mV/Pa. Refer to the sensor documentation to determine this value. |
| Minimum | Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the device can measure with the current settings. |
| OpenChannelDetectEnable | Specifies whether to enable open channel detection. |
| OpenThermocoupleDetectEnable | Specifies whether to apply the open thermocouple detection bias voltage to the channel. Changing the value of this property on a channel may require settling time before the data returned is valid. To compensate for this settling time, discard unsettled data or add a delay between committing and starting the task. Refer to your device specifications for the required settling time. When open thermocouple detection is enabled, use OpenThermocoupleChannelsExist to determine if any channels were open. |
| OvercurrentDetectEnable | Specifies whether to enable overcurrent detection. |
| PowerCurrentScalingCoefficients | Indicates the coefficients of the polynomial equation that NI-DAQmx uses to scale values from the native format of the device to amperes. Can be read at any time during a task. |
| PowerCurrentSetpoint | Specifies the output current, in amperes. If the load draws current greater than the specified value, the device will operate in Constant Current mode. |
| PowerIdleOutputBehavior | Specifies whether to disable the output or maintain the existing value after the task is uncommitted. |
| PowerOutputEnable | Specifies whether to enable or disable power module output. Can be set while a task is running. Can be read at any time during a task. When a task is running, the output is enabled immediately. Otherwise, the output is not enabled until the task enters the Committed state. |
| PowerOutputState | Indicates power channel operating state. Can be read at any time during a task. |
| PowerRemoteSense | Specifies whether to use local or remote sense to sense the output voltage. DAQmx Read (Power Supply) will return remote or local voltage based on the Remote Sense attribute value. Reading this property will return the user-defined value. |
| PowerSupplyFaultDetectEnable | Specifies whether to enable power supply fault detection. |
| PowerVoltageScalingCoefficients | Indicates the coefficients of the polynomial equation that NI-DAQmx uses to scale values from the native format of the device to volts. Can be read at any time during a task. |
| PowerVoltageSetpoint | Specifies the constant output voltage, in volts. Can be set while a task is running. Can be read at any time during a task. |
| PressureUnits | Specifies in which unit to return pressure measurements from the channel. |
| ProbeAttenuation | Specifies the amount of attenuation provided by the probe connected to the channel. Specify this attenuation as a ratio. |
| RangeHigh | Specifies the upper limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |
| RangeLow | Specifies the lower limit of the input range of the device. This value is in the native units of the device. On E Series devices, for example, the native units is volts. |
| RawDataCompressionType | Specifies the type of compression to apply to raw samples returned from the device. |
| RawSampleJustification | Indicates the justification of a raw sample from the device. |
| RawSampleSize | Indicates in bits the size of a raw sample from the device. |
| ReadOpenChannels | Indicates a list of names of any open virtual channels. You must read ReadOpenChannelsExist before you read this property. Otherwise you will receive an error. |
| ReadOpenChannelsDetails | Indicates a list of details of any open virtual channels. You must read ReadOpenChannelsExist before you read this property. Otherwise you will receive an error. |
| ReadOpenChannelsExist | Indicates if the device or devices detected an open channel condition in any virtual channel in the task. Reading this property clears the open channel status for all channels in this task. You must read this property before you read ReadOpenChannels. Otherwise, you will receive an error. |
| RemoveFilterDelay | Specifies if filter delay removal is enabled on the device. |
| ResistanceConfiguration | Specifies the resistance configuration for the channel. NI-DAQmx uses this value for any resistance-based measurements, including temperature measurement using a thermistor or RTD. |
| ResistanceUnits | Specifies the units to use to return resistance measurements. |
| Resolution | Indicates the resolution of the analog-to-digital converter of the channel. This value is in the units you specify with ResolutionUnits. |
| ResolutionUnits | Indicates the units of Resolution. |
| RosetteMeasurementType | Specifies the type of rosette measurement. |
| RosetteStrainChannels | Indicates the raw strain channels that comprise the strain rosette. |
| RosetteStrainGageOrientation | Specifies gage orientation in degrees with respect to the X axis. |
| RosetteType | Indicates the type of rosette gage. |
| RtdA | Specifies the 'A' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD. |
| RtdB | Specifies the 'B' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD. |
| RtdC | Specifies the 'C' constant of the Callendar-Van Dusen equation. NI-DAQmx requires this value when you use a custom RTD. |
| RtdR0 | Specifies in ohms the sensor resistance at 0 deg C. The Callendar-Van Dusen equation requires this value. Refer to the sensor documentation to determine this value. |
| RtdType | Specifies the type of RTD connected to the channel. |
| RvdtSensitivity | Specifies the sensitivity of the RVDT. This value is in the units you specify with RvdtSensitivityUnits. Refer to the sensor documentation to determine this value. |
| RvdtSensitivityUnits | Specifies the units of RvdtSensitivity. |
| RvdtUnits | Specifies the units to use to return angular position measurements from the channel. |
| SampleAndHoldEnable | Specifies whether to enable the sample and hold circuitry of the device. When you disable sample and hold circuitry, a small voltage offset might be introduced into the signal. You can eliminate this offset by using AutoZeroMode to perform an auto zero on the channel. |
| SensorPowerConfiguration | Specifies whether to turn on the sensor's power supply or to leave the configuration unchanged. |
| SensorPowerType | Specifies the type of power supplied to the sensor. |
| SensorPowerVoltage | Specifies the voltage level for the sensor's power supply. |
| SoundPressureDecibelReference | Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. NI-DAQmx also uses the decibel reference level when converting MaximumSoundPressureLevel to a voltage level. |
| SoundPressureUnits | Specifies the units to use to return sound pressure measurements from the channel. |
| StrainGageConfiguration | Specifies the bridge configuration of the strain gages. |
| StrainGageGageFactor | Specifies the sensitivity of the strain gage. Gage factor relates the change in electrical resistance to the change in strain. Refer to the sensor documentation for this value. |
| StrainGagePoissonRatio | Specifies the ratio of lateral strain to axial strain in the material you are measuring. |
| StrainUnits | Specifies the units to use to return strain measurements from the channel. |
| TedsUnits | Indicates the units defined by TEDS information associated with the channel. |
| TemperatureUnits | Specifies the units to use to return temperature measurements from the channel. |
| TerminalConfiguration | Specifies the terminal configuration for the channel. |
| ThermistorA | Specifies the 'A' constant of the Steinhart-Hart thermistor equation. |
| ThermistorB | Specifies the 'B' constant of the Steinhart-Hart thermistor equation. |
| ThermistorC | Specifies the 'C' constant of the Steinhart-Hart thermistor equation. |
| ThermistorR1 | Specifies in ohms the value of the reference resistor for the thermistor if you use voltage excitation. NI-DAQmx ignores this value for current excitation. |
| ThermocoupleCjcChannel | Indicates the channel that acquires the temperature of the cold junction if ThermocoupleCjcSource is Channel. If the channel is a temperature channel, NI-DAQmx acquires the temperature in the correct units. Other channel types, such as a resistance channel with a custom sensor, must use a custom scale to scale values to degrees Celsius. |
| ThermocoupleCjcSource | Indicates the source of cold-junction compensation. |
| ThermocoupleCjcValue | Specifies the temperature of the cold junction if ThermocoupleCjcSource is ConstantValue. Specify this value in the units of the measurement. |
| ThermocoupleLeadOffsetVoltage | Specifies the lead offset nulling voltage to subtract from measurements on a device. This property is ignored if open thermocouple detection is disabled. |
| ThermocoupleScaleType | Specifies the method or equation form that the thermocouple scale uses. |
| ThermocoupleType | Specifies the type of thermocouple connected to the channel. Thermocouple types differ in composition and measurement range. |
| TorqueUnits | Specifies in which unit to return torque measurements from the channel. |
| UsbTransferRequestCount | Specifies the maximum number of simultaneous USB transfers used to stream data. Modify this value to affect performance under different combinations of operating system and device. |
| UsbTransferRequestSize | Specifies the maximum size of a USB transfer request in bytes. Modify this value to affect performance under different combinations of operating system and device. |
| UseExcitationForScaling | Specifies if NI-DAQmx divides the measurement by the excitation. You should typically set this property to true for ratiometric transducers. If you set this property to true, set Maximum and Minimum to reflect the scaling. |
| UseMultiplexedExcitation | Specifies if the SCXI-1122 multiplexes the excitation to the upper half of the channels as it advances through the scan list. |
| VelocityIepeSensorDecibelReference | Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. |
| VelocityIepeSensorSensitivity | Specifies the sensitivity of the IEPE velocity sensor connected to the channel. Specify this value in the unit indicated by VelocityIepeSensorSensitivityUnits. |
| VelocityIepeSensorSensitivityUnits | Specifies the units for VelocityIepeSensorSensitivity. |
| VelocityUnits | Specifies in which unit to return velocity measurements from the channel. |
| VoltageAcrmsUnits | Specifies the units to use to return voltage RMS measurements from the channel. |
| VoltageDecibelReference | Specifies the decibel reference level in the units of the channel. When you read samples as a waveform, the decibel reference level is included in the waveform attributes. |
| VoltageUnits | Specifies the units to use to return voltage measurements from the channel. |

#### Methods

| Name | Description |
| --- | --- |
| PerformBridgeOffsetNullingCalibration(bool) | Performs a bridge offset nulling calibration on the virtual channels in the task. |
| PerformBridgeOffsetNullingCalibration() | Performs a bridge offset nulling calibration on the virtual channels in the task. An error will occur if not all virtual channels in the task support this operation. |
| PerformBridgeShuntCalibration(double, ShuntElementLocation, double, ShuntCalibrationSelect, ShuntResistorSource) | Performs shunt calibration for the specified channels using a bridge sensor. |
| PerformBridgeShuntCalibration(double, ShuntElementLocation, double, ShuntCalibrationSelect, ShuntResistorSource, bool) | Performs shunt calibration for the specified channels using a bridge sensor. |
| PerformBridgeShuntCalibration(double, ShuntElementLocation, double) | Performs shunt calibration for the virtual channels in the task using a bridge sensor. An error will occur if not all virtual channels in the task support this operation. |
| PerformBridgeShuntCalibration(double, ShuntElementLocation, double, bool) | Performs shunt calibration for the virtual channels in the task using a bridge sensor. |
| PerformStrainShuntCalibration(double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource) | Performs shunt calibration for the specified channels using a strain gage sensor. |
| PerformStrainShuntCalibration(double, ShuntElementLocation, bool) | Performs shunt calibration for the virtual channels in the task using a strain gage sensor. |
| PerformStrainShuntCalibration(double, ShuntElementLocation) | Performs shunt calibration for the virtual channels in the task using a strain gage sensor. An error will occur if not all virtual channels in the task support this operation. |
| PerformStrainShuntCalibration(double, ShuntElementLocation, ShuntCalibrationSelect, ShuntResistorSource, bool) | Performs shunt calibration for the specified channels using a strain gage sensor. |
| PerformThermocoupleLeadOffsetNullingCalibration() | Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. An error will occur if not all virtual channels in the task support this operation. |
| PerformThermocoupleLeadOffsetNullingCalibration(bool) | Performs thermocouple lead offset nulling calibration on the channels in the task to compensate for offsets introduced by open thermocouple detection. Use this method to specify whether or not to skip channels that do not support calibration. |

#### See Also

- AIChannelCollection

Parent topic:

NationalInstruments.DAQmx
