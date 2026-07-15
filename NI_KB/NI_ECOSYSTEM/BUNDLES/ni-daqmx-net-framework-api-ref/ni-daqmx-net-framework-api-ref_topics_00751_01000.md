# NI DOCUMENT BUNDLE: ni-daqmx-net-framework-api-ref

<!--NI_BUNDLE_CHUNK bundle=ni-daqmx-net-framework-api-ref start=751 end=1000 -->
<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aodatatransferrequestcondition.html language=enus -->
## TOPIC 00751: AODataTransferRequestCondition Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aodatatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aodatatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the buffer to the onboard memory of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AODataTransferRequestConditionRemarksSpecifies under what condition to transfer data from the buffer to the onboard memory of the device. Use thi

### AODataTransferRequestCondition Enumeration

Specifies under what condition to transfer data from the buffer to the onboard memory of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AODataTransferRequestCondition

#### Remarks

Specifies under what condition to transfer data from the buffer to the onboard memory of the device. Use this enumeration to get or set the value of [DataTransferRequestCondition](nationalinstruments-daqmx-aochannel-datatransferrequestcondition.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OnBoardMemoryEmpty | 10235 | Transfer data to the device only when there is no data in the onboard memory of the device. |
| OnBoardMemoryHalfFullOrLess | 10239 | Transfer data to the device any time the onboard memory is less than half full. |
| OnBoardMemoryNotFull | 10242 | Transfer data to the device any time the onboard memory of the device is not full. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aofilterdelayunits.html language=enus -->
## TOPIC 00752: AOFilterDelayUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aofilterdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aofilterdelayunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of FilterDelay and FilterDelayAdjustment. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOFilterDelayUnitsRemarksSpecifies the units of FilterDelay and FilterDelayAdjustment. Use this enumeration to get or set the value of FilterDelayUnits.MembersNameValueDescriptionSecon

### AOFilterDelayUnits Enumeration

Specifies the units of [FilterDelay](nationalinstruments-daqmx-aochannel-filterdelay.html) and [FilterDelayAdjustment](nationalinstruments-daqmx-aochannel-filterdelayadjustment.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOFilterDelayUnits

#### Remarks

Specifies the units of [FilterDelay](nationalinstruments-daqmx-aochannel-filterdelay.html) and [FilterDelayAdjustment](nationalinstruments-daqmx-aochannel-filterdelayadjustment.html). Use this enumeration to get or set the value of [FilterDelayUnits](nationalinstruments-daqmx-aochannel-filterdelayunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Seconds | 10364 | Seconds. |
| SampleClockPeriods | 10286 | Sample Clock Periods. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aofunctiongenerationmodulationtype.html language=enus -->
## TOPIC 00753: AOFunctionGenerationModulationType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aofunctiongenerationmodulationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aofunctiongenerationmodulationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOFunctionGenerationModulationTypeRemarksSpecifies if the device generates a modulat

### AOFunctionGenerationModulationType Enumeration

Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOFunctionGenerationModulationType

#### Remarks

Specifies if the device generates a modulated version of the waveform using the original waveform as a carrier and input from an external terminal as the signal. Use this enumeration to get or set the value of [FunctionGenerationModulationType](nationalinstruments-daqmx-aochannel-functiongenerationmodulationtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AM | 14756 | Amplitude modulation. |
| FM | 14757 | Frequency modulation. |
| None | 10230 | No modulation. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aofunctiongenerationtype.html language=enus -->
## TOPIC 00754: AOFunctionGenerationType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aofunctiongenerationtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aofunctiongenerationtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the kind of the waveform to generate. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOFunctionGenerationTypeRemarksSpecifies the kind of the waveform to generate. Use this enumeration to get or set the value of FunctionGenerationType.MembersNameValueDescriptionSine14751Sine wave. T

### AOFunctionGenerationType Enumeration

Specifies the kind of the waveform to generate.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOFunctionGenerationType

#### Remarks

Specifies the kind of the waveform to generate. Use this enumeration to get or set the value of [FunctionGenerationType](nationalinstruments-daqmx-aochannel-functiongenerationtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Sine | 14751 | Sine wave. |
| Triangle | 14752 | Triangle wave. |
| Square | 14753 | Square wave. |
| Sawtooth | 14754 | Sawtooth wave. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aoidleoutputbehavior.html language=enus -->
## TOPIC 00755: AOIdleOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aoidleoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aoidleoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the state of the channel when no generation is in progress. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOIdleOutputBehaviorRemarksSpecifies the state of the channel when no generation is in progress. Use this enumeration to get or set the value of IdleOutputBehavior.MembersNameV

### AOIdleOutputBehavior Enumeration

Specifies the state of the channel when no generation is in progress.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOIdleOutputBehavior

#### Remarks

Specifies the state of the channel when no generation is in progress. Use this enumeration to get or set the value of [IdleOutputBehavior](nationalinstruments-daqmx-aochannel-idleoutputbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ZeroVolts | 12526 | Generate 0 V. |
| HighImpedance | 12527 | Set the channel to high-impedance, effectively disconnecting the analog output circuitry from the I/O connector. |
| MaintainExistingValue | 12528 | Continue generating the current value. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aooutputtype.html language=enus -->
## TOPIC 00756: AOOutputType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aooutputtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aooutputtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the channel generates voltage, current, or a waveform. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOOutputTypeRemarksIndicates whether the channel generates voltage, current, or a waveform. Use this enumeration to get or set the value of OutputType.MembersNameValueDescri

### AOOutputType Enumeration

Indicates whether the channel generates voltage, current, or a waveform.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOOutputType

#### Remarks

Indicates whether the channel generates voltage, current, or a waveform. Use this enumeration to get or set the value of [OutputType](nationalinstruments-daqmx-aochannel-outputtype.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 10322 | Voltage generation. |
| Current | 10134 | Current generation. |
| FunctionGeneration | 14750 | Function generation. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aopowerupoutputbehavior.html language=enus -->
## TOPIC 00757: AOPowerUpOutputBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aopowerupoutputbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aopowerupoutputbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the analog output state of the physical channels for some devices when your computer is powered on or the device is reset in NI-DAQmx. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOPowerUpOutputBehaviorRemarksFor all NI-DAQmx simulated devices, power-up states are not persisted.M

### AOPowerUpOutputBehavior Enumeration

Specifies the analog output state of the physical channels for some devices when your computer is powered on or the device is reset in NI-DAQmx.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOPowerUpOutputBehavior

#### Remarks

For all NI-DAQmx simulated devices, power-up states are not persisted.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 10322 | Voltage output. You can set voltage power-up states only for physical channels that support voltage output. |
| Current | 10134 | Current output. You can set current power-up states only for physical channels that support current output. |
| HighImpedance | 12527 | High-impedance state. You can set high-impedance power-up states only for physical channels that support high-impedance output. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aoresolutionunits.html language=enus -->
## TOPIC 00758: AOResolutionUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aoresolutionunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aoresolutionunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of Resolution. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOResolutionUnitsRemarksSpecifies the units of Resolution. Use this enumeration to get or set the value of ResolutionUnits.MembersNameValueDescriptionBits10109Bits.

### AOResolutionUnits Enumeration

Specifies the units of [Resolution](nationalinstruments-daqmx-aochannel-resolution.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOResolutionUnits

#### Remarks

Specifies the units of [Resolution](nationalinstruments-daqmx-aochannel-resolution.html). Use this enumeration to get or set the value of [ResolutionUnits](nationalinstruments-daqmx-aochannel-resolutionunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Bits | 10109 | Bits. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aoterminalconfiguration.html language=enus -->
## TOPIC 00759: AOTerminalConfiguration Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aoterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aoterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal configuration of the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOTerminalConfigurationRemarksSpecifies the terminal configuration of the channel. Use this enumeration to get or set the value of TerminalConfiguration.MembersNameValueDescriptionRse10083Refer

### AOTerminalConfiguration Enumeration

Specifies the terminal configuration of the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOTerminalConfiguration

#### Remarks

Specifies the terminal configuration of the channel. Use this enumeration to get or set the value of [TerminalConfiguration](nationalinstruments-daqmx-aochannel-terminalconfiguration.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rse | 10083 | Referenced Single-Ended. |
| Differential | 10106 | Differential. |
| Pseudodifferential | 12529 | Pseudodifferential. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-aovoltageunits.html language=enus -->
## TOPIC 00760: AOVoltageUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-aovoltageunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-aovoltageunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select. SyntaxNamespace: NationalInstruments.DAQmxpublic enum AOVoltageUnitsRemarksSpecifies in what units to generate voltage on the channel. Write data to the channel in the units you select. Use

### AOVoltageUnits Enumeration

Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum AOVoltageUnits

#### Remarks

Specifies in what units to generate voltage on the channel. Write data to the channel in the units you select. Use this enumeration to get or set the value of [VoltageUnits](nationalinstruments-daqmx-aochannel-voltageunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Volts | 10348 | Volts. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-configuredigitaledgetrigger__string-digitaledgearmstarttriggeredge.html language=enus -->
## TOPIC 00761: ConfigureDigitalEdgeTrigger(string, DigitalEdgeArmStartTriggerEdge)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-configuredigitaledgetrigger__string-digitaledgearmstarttriggeredge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-configuredigitaledgetrigger__string-digitaledgearmstarttriggeredge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures a task to arm for a start trigger upon a rising or falling edge of a digital signal. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeArmStartTriggerEdge edge)RemarksThe NI-DAQmx driver does not determine if the requested settings

### ConfigureDigitalEdgeTrigger(string, DigitalEdgeArmStartTriggerEdge)

Configures a task to [arm for a start trigger](/csh?context=nidaqmx_mxcncpts_armtrig) upon a [rising or falling edge of a digital signal](/csh?context=nidaqmx_mxcncpts_digtrigger).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public void ConfigureDigitalEdgeTrigger(string source, DigitalEdgeArmStartTriggerEdge edge)

#### Remarks

The NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureDigitalEdgeTrigger(string, DigitalEdgeArmStartTriggerEdge) does not throw an exception for parameter values that are not compatible with your hardware or other settings in your task. To determine if all of the settings for a [Task](nationalinstruments-daqmx-task.html) are valid, you must verify the task by starting the task, either with [Start](nationalinstruments-daqmx-task-start.html) or by reading from or writing to the task, or by calling [Control(TaskAction)](nationalinstruments-daqmx-task-control__taskaction.html) with [Verify](nationalinstruments-daqmx-taskaction.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| source | string | The terminal of the trigger signal. |
| edge | DigitalEdgeArmStartTriggerEdge | The edge of the trigger signal that causes the task to arm to respond to a start trigger. |

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-configurenone.html language=enus -->
## TOPIC 00762: ConfigureNone()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-configurenone.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-configurenone.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables arm start triggering for the task. SyntaxNamespace: NationalInstruments.DAQmxpublic void ConfigureNone()RemarksThe NI-DAQmx driver does not determine if the requested settings are possible until the task is verified. ConfigureNone does not throw an exception for parameter values that are no

### ConfigureNone()

Disables [arm start triggering](/csh?context=nidaqmx_mxcncpts_armtrig) for the task.

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

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-digitaledge.html language=enus -->
## TOPIC 00763: DigitalEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-digitaledge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-digitaledge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the DigitalEdgeArmStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic DigitalEdgeArmStartTrigger DigitalEdge { get; }RemarksThe DigitalEdgeArmStartTrigger.

### DigitalEdge

Gets the [DigitalEdgeArmStartTrigger](nationalinstruments-daqmx-digitaledgearmstarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [DigitalEdgeArmStartTrigger](nationalinstruments-daqmx-digitaledgearmstarttrigger.html) DigitalEdge { get; }

#### Remarks

The [DigitalEdgeArmStartTrigger](nationalinstruments-daqmx-digitaledgearmstarttrigger.html).

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-terminal.html language=enus -->
## TOPIC 00764: Terminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-terminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-terminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic string Terminal { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driv

### Terminal

Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Terminal { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-time.html language=enus -->
## TOPIC 00765: Time

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-time.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-time.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the TimeArmStartTrigger. SyntaxNamespace: NationalInstruments.DAQmxpublic TimeArmStartTrigger Time { get; }RemarksThe TimeArmStartTrigger.

### Time

Gets the [TimeArmStartTrigger](nationalinstruments-daqmx-timearmstarttrigger.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [TimeArmStartTrigger](nationalinstruments-daqmx-timearmstarttrigger.html) Time { get; }

#### Remarks

The [TimeArmStartTrigger](nationalinstruments-daqmx-timearmstarttrigger.html).

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-timestamp.html language=enus -->
## TOPIC 00766: Timestamp

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-timestamp.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-timestamp.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the arm start trigger timestamp. SyntaxNamespace: NationalInstruments.DAQmxpublic PrecisionDateTime Timestamp { get; }RemarksThe arm start trigger timestamp.The timestamp returned is expressed as a UTC time. For more information on timestamps in NI-DAQmx, see Timestamps.ExceptionsTypeDescriptio

### Timestamp

Gets the arm start trigger timestamp.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public PrecisionDateTime Timestamp { get; }

#### Remarks

The arm start trigger timestamp.

Note

The timestamp returned is expressed as a UTC time.

Timestamps

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-timestampenable.html language=enus -->
## TOPIC 00767: TimestampEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-timestampenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-timestampenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. SyntaxNamespace: NationalInstruments.DAQmxpublic bool TimestampEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqEx

### TimestampEnable

Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool TimestampEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-timestamptimescale.html language=enus -->
## TOPIC 00768: TimestampTimescale

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-timestamptimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-timestamptimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the arm start trigger timestamp timescale. SyntaxNamespace: NationalInstruments.DAQmxpublic ArmStartTriggerTimestampTimescale TimestampTimescale { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TimestampTimescale

Specifies the arm start trigger timestamp timescale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ArmStartTriggerTimestampTimescale](nationalinstruments-daqmx-armstarttriggertimestamptimescale.html) TimestampTimescale { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-tostring.html language=enus -->
## TOPIC 00769: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-tostring.html
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

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger-type.html language=enus -->
## TOPIC 00770: Type

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger-type.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic ArmStartTriggerType Type { get; set; }Except

### Type

Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ArmStartTriggerType](nationalinstruments-daqmx-armstarttriggertype.html) Type { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

ArmStartTrigger Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttrigger.html language=enus -->
## TOPIC 00771: ArmStartTrigger Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttrigger.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Contains properties and methods that configure a trigger that arms the task for a start trigger. For more information, refer to StartTrigger. Derives fromMarshalByRefObjectIFilteredTypeDescriptorSyntaxNamespace: NationalInstruments.DAQmxpublic class ArmStartTrigger : MarshalByRefObject, IFilteredTyp

### ArmStartTrigger Class

Contains properties and methods that configure a trigger that [arms the task for a start trigger](/csh?context=nidaqmx_mxcncpts_armtrig). For more information, refer to [StartTrigger](nationalinstruments-daqmx-starttrigger.html).

#### Derives from

- MarshalByRefObject
- IFilteredTypeDescriptor

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class ArmStartTrigger : MarshalByRefObject, IFilteredTypeDescriptor

#### Remarks

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| DigitalEdge | Gets the DigitalEdgeArmStartTrigger. |
| Terminal | Indicates the name of the internal Arm Start Trigger terminal for the task. This property does not return the name of the trigger source terminal. |
| Time | Gets the TimeArmStartTrigger. |
| Timestamp | Gets the arm start trigger timestamp. |
| TimestampEnable | Specifies whether the arm start trigger timestamp is enabled. If the timestamp is enabled but no resources are available, an error will be returned at run time. |
| TimestampTimescale | Specifies the arm start trigger timestamp timescale. |
| Type | Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. |

#### Methods

| Name | Description |
| --- | --- |
| ConfigureDigitalEdgeTrigger(string, DigitalEdgeArmStartTriggerEdge) | Configures a task to arm for a start trigger upon a rising or falling edge of a digital signal. |
| ConfigureNone() | Disables arm start triggering for the task. |
| ToString() | Returns a string representation of the object. |

#### See Also

- Triggers
- ArmStartTrigger

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttriggertimestamptimescale.html language=enus -->
## TOPIC 00772: ArmStartTriggerTimestampTimescale Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttriggertimestamptimescale.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttriggertimestamptimescale.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the arm start trigger timestamp timescale. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ArmStartTriggerTimestampTimescaleRemarksSpecifies the arm start trigger timestamp timescale. Use this enumeration to get or set the value of TimestampTimescale.MembersNameValueDescriptionHostTi

### ArmStartTriggerTimestampTimescale Enumeration

Specifies the arm start trigger timestamp timescale.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ArmStartTriggerTimestampTimescale

#### Remarks

Specifies the arm start trigger timestamp timescale. Use this enumeration to get or set the value of [TimestampTimescale](nationalinstruments-daqmx-armstarttrigger-timestamptimescale.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HostTime | 16126 | Use the host device. |
| IODeviceTime | 16127 | Use the I/O device. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-armstarttriggertype.html language=enus -->
## TOPIC 00773: ArmStartTriggerType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-armstarttriggertype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-armstarttriggertype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ArmStartTriggerTypeRemarksSpecifies the

### ArmStartTriggerType Enumeration

Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ArmStartTriggerType

#### Remarks

Specifies the type of trigger to use to arm the task for a Start Trigger. If you configure an Arm Start Trigger, the task does not respond to a Start Trigger until the device receives the Arm Start Trigger. Use this enumeration to get or set the value of [Type](nationalinstruments-daqmx-armstarttrigger-type.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DigitalEdge | 10150 | Trigger on a rising or falling edge of a digital signal. |
| Time | 15996 | Trigger when a specified time is reached. |
| None | 10230 | Disable the trigger. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-basictedsdataoption.html language=enus -->
## TOPIC 00774: BasicTedsDataOption Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-basictedsdataoption.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-basictedsdataoption.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to handle basic TEDS data in a TEDS bitstream. SyntaxNamespace: NationalInstruments.DAQmxpublic enum BasicTedsDataOptionMembersNameValueDescriptionWriteToEeprom12538Basic TEDS data is written to the EEPROM, even if the sensor includes a PROM. You cannot write basic TEDS data if the PRO

### BasicTedsDataOption Enumeration

Specifies how to handle [basic TEDS data](/csh?context=nidaqmx_measfunds_writingteds) in a TEDS bitstream.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum BasicTedsDataOption

#### Members

| Name | Value | Description |
| --- | --- | --- |
| WriteToEeprom | 12538 | Basic TEDS data is written to the EEPROM, even if the sensor includes a PROM. You cannot write basic TEDS data if the PROM contains data. |
| WriteToProm | 12539 | Basic TEDS data is written to the PROM. Any subsequent attempts to write basic TEDS data results in an error. |
| DoNotWrite | 12540 | Basic TEDS data is ignored. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-bridgeshuntcalibrationsource.html language=enus -->
## TOPIC 00775: BridgeShuntCalibrationSource Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-bridgeshuntcalibrationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-bridgeshuntcalibrationsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use internal or external shunt when Shunt Cal A is selected. SyntaxNamespace: NationalInstruments.DAQmxpublic enum BridgeShuntCalibrationSourceRemarksSpecifies whether to use internal or external shunt when Shunt Cal A is selected. Use this enumeration to get or set the value of

### BridgeShuntCalibrationSource Enumeration

Specifies whether to use internal or external shunt when Shunt Cal A is selected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum BridgeShuntCalibrationSource

#### Remarks

Specifies whether to use internal or external shunt when Shunt Cal A is selected. Use this enumeration to get or set the value of [BridgeShuntCalibrationASource](nationalinstruments-daqmx-aichannel-bridgeshuntcalibrationasource.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| BuiltIn | 10200 | Use the internal shunt. |
| UserProvided | 10167 | Use an external shunt. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-calibrationcoupling9775.html language=enus -->
## TOPIC 00776: CalibrationCoupling9775 Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-calibrationcoupling9775.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-calibrationcoupling9775.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the coupling of the calibration constants to be adjusted on the C Series NI 9775. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CalibrationCoupling9775RemarksUse this enumeration with Get9775AdjustmentPoints(CalibrationCoupling9775) and Adjust9775(string, double, CalibrationCoupli

### CalibrationCoupling9775 Enumeration

Represents the coupling of the calibration constants to be adjusted on the C Series NI 9775.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CalibrationCoupling9775

#### Remarks

Use this enumeration with [Get9775AdjustmentPoints(CalibrationCoupling9775)](nationalinstruments-daqmx-externalcalibrationsession-get9775adjustmentpoints__calibrationcoupling9775.html) and [Adjust9775(string, double, CalibrationCoupling9775)](nationalinstruments-daqmx-externalcalibrationsession-adjust9775__string-double-calibrationcoupling9775.html) to specify the coupling of the calibration constants to be adjusted.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| DC | 10050 | DC coupling. |
| AC | 10045 | AC coupling. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-calibrationinputterminalconfiguration4463.html language=enus -->
## TOPIC 00777: CalibrationInputTerminalConfiguration4463 Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-calibrationinputterminalconfiguration4463.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-calibrationinputterminalconfiguration4463.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration for the channel to calibrate on an NI PXIe 4463 device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CalibrationInputTerminalConfiguration4463MembersNameValueDescriptionDifferential10106A differential input terminal configuration. Pseudodifferentia

### CalibrationInputTerminalConfiguration4463 Enumeration

Specifies the input terminal configuration for the channel to calibrate on an NI PXIe 4463 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CalibrationInputTerminalConfiguration4463

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Differential | 10106 | A differential input terminal configuration. |
| Pseudodifferential | 12529 | A pseudodifferential input terminal configuration. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-calibrationinputterminalconfiguration9209.html language=enus -->
## TOPIC 00778: CalibrationInputTerminalConfiguration9209 Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-calibrationinputterminalconfiguration9209.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-calibrationinputterminalconfiguration9209.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration for the channel to calibrate on an NI 9209 device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CalibrationInputTerminalConfiguration9209MembersNameValueDescriptionRse10083A referenced single-ended input terminal configuration. Differential10106A d

### CalibrationInputTerminalConfiguration9209 Enumeration

Specifies the input terminal configuration for the channel to calibrate on an NI 9209 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CalibrationInputTerminalConfiguration9209

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Rse | 10083 | A referenced single-ended input terminal configuration. |
| Differential | 10106 | A differential input terminal configuration. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-calibrationmode4339.html language=enus -->
## TOPIC 00779: CalibrationMode4339 Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-calibrationmode4339.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-calibrationmode4339.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which measurements to use to calibrate an NI 4339 device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CalibrationMode4339MembersNameValueDescriptionVoltage10322Voltage mode. Ratiometric15908Ratiometric mode.

### CalibrationMode4339 Enumeration

Specifies which measurements to use to calibrate an NI 4339 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CalibrationMode4339

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 10322 | Voltage mode. |
| Ratiometric | 15908 | Ratiometric mode. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-calibrationmode4480.html language=enus -->
## TOPIC 00780: CalibrationMode4480 Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-calibrationmode4480.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-calibrationmode4480.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which measurements to use to calibrate an NI 4480 device. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CalibrationMode4480MembersNameValueDescriptionVoltage10322Voltage mode. Charge16105Charge mode.

### CalibrationMode4480 Enumeration

Specifies which measurements to use to calibrate an NI 4480 device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CalibrationMode4480

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Voltage | 10322 | Voltage mode. |
| Charge | 16105 | Charge mode. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-changedetectioneventpulsepolarity.html language=enus -->
## TOPIC 00781: ChangeDetectionEventPulsePolarity Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-changedetectioneventpulsepolarity.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-changedetectioneventpulsepolarity.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polarity of an exported Change Detection Event pulse. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ChangeDetectionEventPulsePolarityRemarksSpecifies the polarity of an exported Change Detection Event pulse. Use this enumeration to get or set the value of ChangeDetectionEventPu

### ChangeDetectionEventPulsePolarity Enumeration

Specifies the polarity of an exported Change Detection Event pulse.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ChangeDetectionEventPulsePolarity

#### Remarks

Specifies the polarity of an exported Change Detection Event pulse. Use this enumeration to get or set the value of [ChangeDetectionEventPulsePolarity](nationalinstruments-daqmx-exportsignals-changedetectioneventpulsepolarity.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| ActiveHigh | 10095 | High state is the active state. |
| ActiveLow | 10096 | Low state is the active state. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-description.html language=enus -->
## TOPIC 00782: Description

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-description.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-description.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a user-defined description for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string Description { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Description

Specifies a user-defined description for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string Description { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-dispose.html language=enus -->
## TOPIC 00783: Dispose()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-dispose.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-dispose.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases all resources used by Channel. SyntaxNamespace: NationalInstruments.DAQmxpublic override void Dispose()RemarksUse this method only if the application you create runs on a low memory system.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Dispose()

Releases all resources used by [Channel](nationalinstruments-daqmx-channel.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public override void Dispose()

#### Remarks

Use this method only if the application you create runs on a low memory system.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-dispose__bool.html language=enus -->
## TOPIC 00784: Dispose(bool)

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-dispose__bool.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-dispose__bool.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the managed and unmanaged resources used by Channel or optionally releases only the unmanaged resources. SyntaxNamespace: NationalInstruments.DAQmxprotected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)RemarksRefer to Cleaning Up Unmanaged Resources for more information on implementi

### Dispose(bool)

Releases the managed and unmanaged resources used by [Channel](nationalinstruments-daqmx-channel.html) or optionally releases only the unmanaged resources.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void Dispose([MarshalAs(UnmanagedType.U1)] bool A_0)

#### Remarks

Refer to [Cleaning Up Unmanaged Resources](https://#) for more information on implementing a Dispose method and using objects that implement IDisposable.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| A_0 | bool | true to release both managed and unmanaged resources used by Channel; false to release only unmanaged resources used by Channel. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-isglobal.html language=enus -->
## TOPIC 00785: IsGlobal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-isglobal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-isglobal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the channel is a global channel. SyntaxNamespace: NationalInstruments.DAQmxpublic bool IsGlobal { get; }RemarksA Boolean value that indicates whether the channel is a global channel.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### IsGlobal

Indicates whether the channel is a global channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool IsGlobal { get; }

#### Remarks

A Boolean value that indicates whether the channel is a global channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-physicalname.html language=enus -->
## TOPIC 00786: PhysicalName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-physicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-physicalname.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the physical channel upon which this virtual channel is based. SyntaxNamespace: NationalInstruments.DAQmxpublic string PhysicalName { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PhysicalName

Specifies the [name](/csh?context=nidaqmx_mxcncpts_physchannames) of the physical channel upon which this virtual channel is based.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PhysicalName { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-synchronizationunlockbehavior.html language=enus -->
## TOPIC 00787: SynchronizationUnlockBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-synchronizationunlockbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-synchronizationunlockbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take if the target loses its synchronization to the grand master. SyntaxNamespace: NationalInstruments.DAQmxpublic ChannelSynchronizationUnlockBehavior SynchronizationUnlockBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx drive

### SynchronizationUnlockBehavior

Specifies the action to take if the target loses its synchronization to the grand master.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ChannelSynchronizationUnlockBehavior](nationalinstruments-daqmx-channelsynchronizationunlockbehavior.html) SynchronizationUnlockBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-throwifdisposed.html language=enus -->
## TOPIC 00788: ThrowIfDisposed()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-throwifdisposed.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-throwifdisposed.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.DAQmxprotected void ThrowIfDisposed()

### ThrowIfDisposed()

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

protected void ThrowIfDisposed()

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-tostring.html language=enus -->
## TOPIC 00789: ToString()

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-tostring.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-tostring.html
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

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-type.html language=enus -->
## TOPIC 00790: Type

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-type.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-type.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the type of the virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic ChannelType Type { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Type

Indicates the [type](/csh?context=nidaqmx_mxcncpts_virtchantypes) of the virtual channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [ChannelType](nationalinstruments-daqmx-channeltype.html) Type { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel-virtualname.html language=enus -->
## TOPIC 00791: VirtualName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel-virtualname.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel-virtualname.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic string VirtualName { get; }RemarksA String that represents the name of the virtual channel.ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### VirtualName

Gets the name of the [virtual channel](/csh?context=nidaqmx_mxcncpts_virtchantypes).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string VirtualName { get; }

#### Remarks

A String that represents the name of the virtual channel.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channel.html language=enus -->
## TOPIC 00792: Channel Class

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channel.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channel.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a channel or a set of channels and the properties you can set on a channel. Derives fromMarshalByRefObjectIDisposableSyntaxNamespace: NationalInstruments.DAQmxpublic class Channel : MarshalByRefObject, IDisposableRemarksChannel is the base class for AIChannel, AOChannel, DIChannel, DOChan

### Channel Class

Represents a channel or a set of channels and the properties you can set on a channel.

#### Derives from

- MarshalByRefObject
- IDisposable

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public class Channel : MarshalByRefObject, IDisposable

#### Remarks

Channel

AIChannel

AOChannel

DIChannel

DOChannel

CIChannel

COChannel

Channel

Note

Example applications are located in the <*Public Documents*>\National Instruments\NI-DAQ\Examples\DotNET4.*x* directory or in the **Start** menu at **National Instruments»NI-DAQmx»NI-DAQmx Examples**.

#### Thread Safety

All members of this type are safe for multithreaded operations.

#### Properties

| Name | Description |
| --- | --- |
| Description | Specifies a user-defined description for the channel. |
| IsGlobal | Indicates whether the channel is a global channel. |
| PhysicalName | Specifies the name of the physical channel upon which this virtual channel is based. |
| SynchronizationUnlockBehavior | Specifies the action to take if the target loses its synchronization to the grand master. |
| Type | Indicates the type of the virtual channel. |
| VirtualName | Gets the name of the virtual channel. |

#### Methods

| Name | Description |
| --- | --- |
| Dispose() | Releases all resources used by Channel. |
| ToString() | Returns a string representation of the object. |
| Dispose(bool) | Releases the managed and unmanaged resources used by Channel or optionally releases only the unmanaged resources. |
| ThrowIfDisposed() |  |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channellinegrouping.html language=enus -->
## TOPIC 00793: ChannelLineGrouping Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channellinegrouping.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channellinegrouping.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to group digital lines into one or more virtual channels. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ChannelLineGroupingMembersNameValueDescriptionOneChannelForEachLine0A separate virtual channel is created for each digital line. OneChannelForAllLines1All digital lines are c

### ChannelLineGrouping Enumeration

Specifies how to group digital lines into one or more [virtual channels](/csh?context=nidaqmx_mxcncpts_virtchantypes).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ChannelLineGrouping

#### Members

| Name | Value | Description |
| --- | --- | --- |
| OneChannelForEachLine | 0 | A separate virtual channel is created for each digital line. |
| OneChannelForAllLines | 1 | All digital lines are combined into a single virtual channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channelsynchronizationunlockbehavior.html language=enus -->
## TOPIC 00794: ChannelSynchronizationUnlockBehavior Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channelsynchronizationunlockbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channelsynchronizationunlockbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the action to take if the target loses its synchronization to the grand master. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ChannelSynchronizationUnlockBehaviorRemarksSpecifies the action to take if the target loses its synchronization to the grand master. Use this enumeration to

### ChannelSynchronizationUnlockBehavior Enumeration

Specifies the action to take if the target loses its synchronization to the grand master.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ChannelSynchronizationUnlockBehavior

#### Remarks

Specifies the action to take if the target loses its synchronization to the grand master. Use this enumeration to get or set the value of [SynchronizationUnlockBehavior](nationalinstruments-daqmx-channel-synchronizationunlockbehavior.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| StopTaskAndError | 15862 | Stop task and return an error. |
| IgnoreLostSynchronizationLock | 16129 | Ignore the loss of synchronization and do nothing. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-channeltype.html language=enus -->
## TOPIC 00795: ChannelType Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-channeltype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-channeltype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the type of the virtual channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum ChannelTypeRemarksIndicates the type of the virtual channel. Use this enumeration to get or set the value of Type.MembersNameValueDescriptionAI10100Analog input channel. AO10102Analog output channel. DI1

### ChannelType Enumeration

Indicates the [type](/csh?context=nidaqmx_mxcncpts_virtchantypes) of the virtual channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum ChannelType

#### Remarks

Indicates the [type](/csh?context=nidaqmx_mxcncpts_virtchantypes) of the virtual channel. Use this enumeration to get or set the value of [Type](nationalinstruments-daqmx-channel-type.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AI | 10100 | Analog input channel. |
| AO | 10102 | Analog output channel. |
| DI | 10151 | Digital input channel. |
| DO | 10153 | Digital output channel. |
| CI | 10131 | Counter input channel. |
| CO | 10132 | Counter output channel. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-ciangularencoderunits.html language=enus -->
## TOPIC 00796: CIAngularEncoderUnits Enumeration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-ciangularencoderunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-ciangularencoderunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return angular position measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic enum CIAngularEncoderUnitsRemarksSpecifies the units to use to return angular position measurements from the channel. Use this enumeration to get or set the value of

### CIAngularEncoderUnits Enumeration

Specifies the units to use to return angular position measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public enum CIAngularEncoderUnits

#### Remarks

Specifies the units to use to return angular position measurements from the channel. Use this enumeration to get or set the value of [AngularEncoderUnits](nationalinstruments-daqmx-cichannel-angularencoderunits.html).

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Degrees | 10146 | Degrees. |
| Radians | 10273 | Radians. |
| Ticks | 10304 | Ticks. |
| FromCustomScale | 10065 | Units a custom scale specifies. If you select this value, you must specify a custom scale name. |

Parent topic:

NationalInstruments.DAQmx

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-angularencoderinitialangle.html language=enus -->
## TOPIC 00797: AngularEncoderInitialAngle

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-angularencoderinitialangle.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-angularencoderinitialangle.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting angle of the encoder. This value is in the units you specify with AngularEncoderUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double AngularEncoderInitialAngle { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### AngularEncoderInitialAngle

Specifies the starting angle of the encoder. This value is in the units you specify with [AngularEncoderUnits](nationalinstruments-daqmx-cichannel-angularencoderunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double AngularEncoderInitialAngle { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-angularencoderpulsesperrevolution.html language=enus -->
## TOPIC 00798: AngularEncoderPulsesPerRevolution

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-angularencoderpulsesperrevolution.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-angularencoderpulsesperrevolution.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B. SyntaxNamespace: NationalInstruments.DAQmxpublic long AngularEncoderPulsesPerRevolution { get; set; }E

### AngularEncoderPulsesPerRevolution

Specifies the number of pulses the encoder generates per revolution. This value is the number of pulses on either signal A or signal B, not the total number of pulses on both signal A and signal B.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long AngularEncoderPulsesPerRevolution { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-angularencoderunits.html language=enus -->
## TOPIC 00799: AngularEncoderUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-angularencoderunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-angularencoderunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return angular position measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic CIAngularEncoderUnits AngularEncoderUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### AngularEncoderUnits

Specifies the units to use to return angular position measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIAngularEncoderUnits](nationalinstruments-daqmx-ciangularencoderunits.html) AngularEncoderUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-count.html language=enus -->
## TOPIC 00800: Count

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-count.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-count.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current value of the count register. SyntaxNamespace: NationalInstruments.DAQmxpublic long Count { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### Count

Indicates the current value of the count register.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long Count { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesactiveedge.html language=enus -->
## TOPIC 00801: CountEdgesActiveEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edges to increment or decrement the counter. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesActiveEdge CountEdgesActiveEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesActiveEdge

Specifies on which edges to increment or decrement the counter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesActiveEdge](nationalinstruments-daqmx-cicountedgesactiveedge.html) CountEdgesActiveEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirection.html language=enus -->
## TOPIC 00802: CountEdgesCountDirection

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirection.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirection.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to increment or decrement the counter on each edge. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesCountDirection CountEdgesCountDirection { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountDirection

Specifies whether to increment or decrement the counter on each edge.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesCountDirection](nationalinstruments-daqmx-cicountedgescountdirection.html) CountEdgesCountDirection { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfilterenable.html language=enus -->
## TOPIC 00803: CountEdgesCountDirectionDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesCountDirectionDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountDirectionDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesCountDirectionDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00804: CountEdgesCountDirectionDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesCountDirectionDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountDirectionDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountDirectionDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfiltertimebaserate.html language=enus -->
## TOPIC 00805: CountEdgesCountDirectionDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesCountDirectionDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqEx

### CountEdgesCountDirectionDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountDirectionDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfiltertimebasesource.html language=enus -->
## TOPIC 00806: CountEdgesCountDirectionDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesCountDirectionDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver ret

### CountEdgesCountDirectionDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesCountDirectionDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalsynchronizationenable.html language=enus -->
## TOPIC 00807: CountEdgesCountDirectionDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectiondigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesCountDirectionDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recog

### CountEdgesCountDirectionDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesCountDirectionDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectionhysteresis.html language=enus -->
## TOPIC 00808: CountEdgesCountDirectionHysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectionhysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectionhysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level applied to the CountEdgesCountDirectionThresholdVoltage. The source signal must fall below CountEdgesCountDirectionThresholdVoltage minus the hysteresis before a change in count direction occurs. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesCountDire

### CountEdgesCountDirectionHysteresis

Specifies a hysteresis level applied to the [CountEdgesCountDirectionThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgescountdirectionthresholdvoltage.html). The source signal must fall below [CountEdgesCountDirectionThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgescountdirectionthresholdvoltage.html) minus the hysteresis before a change in count direction occurs.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountDirectionHysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectionlogiclevelbehavior.html language=enus -->
## TOPIC 00809: CountEdgesCountDirectionLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectionlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectionlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesCountDirectionLogicLevelBehavior CountEdgesCountDirectionLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returne

### CountEdgesCountDirectionLogicLevelBehavior

Specifies the logic level behavior on the count reset line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesCountDirectionLogicLevelBehavior](nationalinstruments-daqmx-cicountedgescountdirectionlogiclevelbehavior.html) CountEdgesCountDirectionLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectionterminal.html language=enus -->
## TOPIC 00810: CountEdgesCountDirectionTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectionterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectionterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal of the digital signal that controls the count direction if CountEdgesCountDirection is ExternallyControlled. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesCountDirectionTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExcep

### CountEdgesCountDirectionTerminal

Specifies the source [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the digital signal that controls the count direction if [CountEdgesCountDirection](nationalinstruments-daqmx-cichannel-countedgescountdirection.html) is [ExternallyControlled](nationalinstruments-daqmx-cicountedgescountdirection.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesCountDirectionTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectionterminalconfiguration.html language=enus -->
## TOPIC 00811: CountEdgesCountDirectionTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectionterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectionterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesCountDirectionTerminalConfiguration CountEdgesCountDirectionTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### CountEdgesCountDirectionTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesCountDirectionTerminalConfiguration](nationalinstruments-daqmx-cicountedgescountdirectionterminalconfiguration.html) CountEdgesCountDirectionTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountdirectionthresholdvoltage.html language=enus -->
## TOPIC 00812: CountEdgesCountDirectionThresholdVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountdirectionthresholdvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountdirectionthresholdvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level applied to the Count Direction terminal. When the signal is above this threshold, the counter counts up. When the signal is below this threshold, the counter counts down. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesCountDirectionThresholdVoltage { ge

### CountEdgesCountDirectionThresholdVoltage

Specifies the voltage level applied to the Count Direction terminal. When the signal is above this threshold, the counter counts up. When the signal is below this threshold, the counter counts down.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountDirectionThresholdVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetactiveedge.html language=enus -->
## TOPIC 00813: CountEdgesCountResetActiveEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the signal to reset the count. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesCountResetActiveEdge CountEdgesCountResetActiveEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetActiveEdge

Specifies on which edge of the signal to reset the count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesCountResetActiveEdge](nationalinstruments-daqmx-cicountedgescountresetactiveedge.html) CountEdgesCountResetActiveEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfilterenable.html language=enus -->
## TOPIC 00814: CountEdgesCountResetDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesCountResetDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetDigitalFilterEnable

Specifies whether to apply the pulse width filter to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesCountResetDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00815: CountEdgesCountResetDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesCountResetDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetDigitalFilterMinimumPulseWidth

Specifies the minimum pulse width the filter recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountResetDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfiltertimebaserate.html language=enus -->
## TOPIC 00816: CountEdgesCountResetDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesCountResetDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExcept

### CountEdgesCountResetDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountResetDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfiltertimebasesource.html language=enus -->
## TOPIC 00817: CountEdgesCountResetDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesCountResetDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an erro

### CountEdgesCountResetDigitalFilterTimebaseSource

Specifies the input of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesCountResetDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetdigitalsynchronizationenable.html language=enus -->
## TOPIC 00818: CountEdgesCountResetDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesCountResetDigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### CountEdgesCountResetDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesCountResetDigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetenable.html language=enus -->
## TOPIC 00819: CountEdgesCountResetEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to reset the count on the active edge specified with CountEdgesCountResetTerminal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesCountResetEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetEnable

Specifies whether to reset the count on the active edge specified with [CountEdgesCountResetTerminal](nationalinstruments-daqmx-cichannel-countedgescountresetterminal.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesCountResetEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresethysteresis.html language=enus -->
## TOPIC 00820: CountEdgesCountResetHysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresethysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresethysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level applied to CountEdgesCountResetThresholdVoltage. When CountEdgesCountResetActiveEdge is rising, the source signal must first fall below CountEdgesCountResetThresholdVoltage minus the hysteresis before a rising edge is detected at CountEdgesCountResetThresholdVoltage. Whe

### CountEdgesCountResetHysteresis

Specifies a hysteresis level applied to [CountEdgesCountResetThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html). When [CountEdgesCountResetActiveEdge](nationalinstruments-daqmx-cichannel-countedgescountresetactiveedge.html) is rising, the source signal must first fall below [CountEdgesCountResetThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html) minus the hysteresis before a rising edge is detected at [CountEdgesCountResetThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html). When [CountEdgesCountResetActiveEdge](nationalinstruments-daqmx-cichannel-countedgescountresetactiveedge.html) is falling, the source signal must first rise above [CountEdgesCountResetThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html) plus the hysteresis before a falling edge is detected at [CountEdgesCountResetThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountResetHysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetlogiclevelbehavior.html language=enus -->
## TOPIC 00821: CountEdgesCountResetLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesCountResetLogicLevelBehavior CountEdgesCountResetLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an err

### CountEdgesCountResetLogicLevelBehavior

Specifies the logic level behavior on the count reset line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesCountResetLogicLevelBehavior](nationalinstruments-daqmx-cicountedgescountresetlogiclevelbehavior.html) CountEdgesCountResetLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetresetcount.html language=enus -->
## TOPIC 00822: CountEdgesCountResetResetCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetresetcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetresetcount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value to reset the count to. SyntaxNamespace: NationalInstruments.DAQmxpublic long CountEdgesCountResetResetCount { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetResetCount

Specifies the value to reset the count to.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CountEdgesCountResetResetCount { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetterminal.html language=enus -->
## TOPIC 00823: CountEdgesCountResetTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to reset the count. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesCountResetTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetTerminal

Specifies the input terminal of the signal to reset the count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesCountResetTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetterminalconfiguration.html language=enus -->
## TOPIC 00824: CountEdgesCountResetTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesCountResetTerminalConfiguration CountEdgesCountResetTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesCountResetTerminalConfiguration](nationalinstruments-daqmx-cicountedgescountresetterminalconfiguration.html) CountEdgesCountResetTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html language=enus -->
## TOPIC 00825: CountEdgesCountResetThresholdVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgescountresetthresholdvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level at which to recognize the counter reset event. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesCountResetThresholdVoltage { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesCountResetThresholdVoltage

Specifies the voltage level at which to recognize the counter reset event.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesCountResetThresholdVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesdigitalfilterenable.html language=enus -->
## TOPIC 00826: CountEdgesDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00827: CountEdgesDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesdigitalfiltertimebaserate.html language=enus -->
## TOPIC 00828: CountEdgesDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### CountEdgesDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesdigitalfiltertimebasesource.html language=enus -->
## TOPIC 00829: CountEdgesDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### CountEdgesDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesdigitalsynchronizationenable.html language=enus -->
## TOPIC 00830: CountEdgesDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the d

### CountEdgesDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatedigitalfilterenable.html language=enus -->
## TOPIC 00831: CountEdgesGateDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatedigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatedigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the gate input signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesGateDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGateDigitalFilterEnable

Specifies whether to apply the pulse width filter to the gate input signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesGateDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatedigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00832: CountEdgesGateDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatedigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatedigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the digital filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesGateDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGateDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the digital filter recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesGateDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatedigitalfiltertimebaserate.html language=enus -->
## TOPIC 00833: CountEdgesGateDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatedigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatedigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesGateDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe

### CountEdgesGateDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesGateDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatedigitalfiltertimebasesource.html language=enus -->
## TOPIC 00834: CountEdgesGateDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatedigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatedigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesGateDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an e

### CountEdgesGateDigitalFilterTimebaseSource

Specifies the input terminal of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesGateDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgateenable.html language=enus -->
## TOPIC 00835: CountEdgesGateEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgateenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgateenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the functionality to gate the counter input signal for a count edges measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CountEdgesGateEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGateEnable

Specifies whether to enable the functionality to gate the counter input signal for a count edges measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CountEdgesGateEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatehysteresis.html language=enus -->
## TOPIC 00836: CountEdgesGateHysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatehysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatehysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level applied to the CountEdgesGateThresholdVoltage. When CountEdgesGatePauseState is High, the source signal must fall below CountEdgesGateThresholdVoltage minus the hysteresis before the counter resumes counting. When CountEdgesGatePauseState is Low, the source signal must r

### CountEdgesGateHysteresis

Specifies a hysteresis level applied to the [CountEdgesGateThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesgatethresholdvoltage.html). When [CountEdgesGatePauseState](nationalinstruments-daqmx-cichannel-countedgesgatepausestate.html) is High, the source signal must fall below [CountEdgesGateThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesgatethresholdvoltage.html) minus the hysteresis before the counter resumes counting. When [CountEdgesGatePauseState](nationalinstruments-daqmx-cichannel-countedgesgatepausestate.html) is Low, the source signal must rise above [CountEdgesGateThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesgatethresholdvoltage.html) plus the hysteresis before the counter resumes counting.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesGateHysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatelogiclevelbehavior.html language=enus -->
## TOPIC 00837: CountEdgesGateLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatelogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatelogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the gate input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesGateLogicLevelBehavior CountEdgesGateLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGateLogicLevelBehavior

Specifies the logic level behavior on the gate input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesGateLogicLevelBehavior](nationalinstruments-daqmx-cicountedgesgatelogiclevelbehavior.html) CountEdgesGateLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatepausestate.html language=enus -->
## TOPIC 00838: CountEdgesGatePauseState

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatepausestate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatepausestate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the counter gates input pulses while the signal is high or low. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesGatePauseState CountEdgesGatePauseState { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGatePauseState

Specifies whether the counter gates input pulses while the signal is high or low.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesGatePauseState](nationalinstruments-daqmx-cicountedgesgatepausestate.html) CountEdgesGatePauseState { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgateterminal.html language=enus -->
## TOPIC 00839: CountEdgesGateTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgateterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgateterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gate terminal. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesGateTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGateTerminal

Specifies the gate terminal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesGateTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgateterminalconfiguration.html language=enus -->
## TOPIC 00840: CountEdgesGateTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgateterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgateterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gate terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesGateTerminalConfiguration CountEdgesGateTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGateTerminalConfiguration

Specifies the gate terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesGateTerminalConfiguration](nationalinstruments-daqmx-cicountedgesgateterminalconfiguration.html) CountEdgesGateTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesgatethresholdvoltage.html language=enus -->
## TOPIC 00841: CountEdgesGateThresholdVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesgatethresholdvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesgatethresholdvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level at which to recognize the counter gate signal. SyntaxNamespace: NationalInstruments.DAQmxpublic double CountEdgesGateThresholdVoltage { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesGateThresholdVoltage

Specifies the voltage level at which to recognize the counter gate signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesGateThresholdVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgeshysteresis.html language=enus -->
## TOPIC 00842: CountEdgesHysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgeshysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgeshysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level to apply to CountEdgesThresholdVoltage. When CountEdgesActiveEdge is rising, the source signal must first fall below CountEdgesThresholdVoltage minus the hysteresis before a rising edge is detected at CountEdgesThresholdVoltage. When CountEdgesActiveEdge is falling, the

### CountEdgesHysteresis

Specifies a hysteresis level to apply to [CountEdgesThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html). When [CountEdgesActiveEdge](nationalinstruments-daqmx-cichannel-countedgesactiveedge.html) is rising, the source signal must first fall below [CountEdgesThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html) minus the hysteresis before a rising edge is detected at [CountEdgesThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html). When [CountEdgesActiveEdge](nationalinstruments-daqmx-cichannel-countedgesactiveedge.html) is falling, the source signal must first rise above [CountEdgesThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html) plus the hysteresis before a falling edge is detected at [CountEdgesThresholdVoltage](nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesHysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesinitialcount.html language=enus -->
## TOPIC 00843: CountEdgesInitialCount

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesinitialcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesinitialcount.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting value from which to count. SyntaxNamespace: NationalInstruments.DAQmxpublic long CountEdgesInitialCount { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesInitialCount

Specifies the starting value from which to count.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CountEdgesInitialCount { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgeslogiclevelbehavior.html language=enus -->
## TOPIC 00844: CountEdgesLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgeslogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgeslogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesLogicLevelBehavior CountEdgesLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesLogicLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesLogicLevelBehavior](nationalinstruments-daqmx-cicountedgeslogiclevelbehavior.html) CountEdgesLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesterminal.html language=enus -->
## TOPIC 00845: CountEdgesTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string CountEdgesTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CountEdgesTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesterminalconfiguration.html language=enus -->
## TOPIC 00846: CountEdgesTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CICountEdgesTerminalConfiguration CountEdgesTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CountEdgesTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICountEdgesTerminalConfiguration](nationalinstruments-daqmx-cicountedgesterminalconfiguration.html) CountEdgesTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html language=enus -->
## TOPIC 00847: CountEdgesThresholdVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countedgesthresholdvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. SyntaxNamespace: NationalInstruments.DAQmxpublic double C

### CountEdgesThresholdVoltage

Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CountEdgesThresholdVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebaseactiveedge.html language=enus -->
## TOPIC 00848: CounterTimebaseActiveEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebaseactiveedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebaseactiveedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge. SyntaxNamespace: NationalInstruments.DAQmxpublic CICounterTimebaseActiveEdge CounterTimebaseActiveEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx

### CounterTimebaseActiveEdge

Specifies whether a timebase cycle is from rising edge to rising edge or from falling edge to falling edge.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CICounterTimebaseActiveEdge](nationalinstruments-daqmx-cicountertimebaseactiveedge.html) CounterTimebaseActiveEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebasedigitalfilterenable.html language=enus -->
## TOPIC 00849: CounterTimebaseDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebasedigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebasedigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CounterTimebaseDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CounterTimebaseDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CounterTimebaseDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebasedigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00850: CounterTimebaseDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebasedigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebasedigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double CounterTimebaseDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### CounterTimebaseDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CounterTimebaseDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebasedigitalfiltertimebaserate.html language=enus -->
## TOPIC 00851: CounterTimebaseDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebasedigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebasedigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double CounterTimebaseDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionTh

### CounterTimebaseDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CounterTimebaseDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebasedigitalfiltertimebasesource.html language=enus -->
## TOPIC 00852: CounterTimebaseDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebasedigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebasedigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string CounterTimebaseDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an

### CounterTimebaseDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CounterTimebaseDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebasedigitalsynchronizationenable.html language=enus -->
## TOPIC 00853: CounterTimebaseDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebasedigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebasedigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool CounterTimebaseDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by

### CounterTimebaseDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool CounterTimebaseDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebasemastertimebasedivisor.html language=enus -->
## TOPIC 00854: CounterTimebaseMasterTimebaseDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebasemastertimebasedivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebasemastertimebasedivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to measure slower signals without causing the count register to roll over. SyntaxNamespace: NationalInstruments.DAQmxpublic long CounterTimebaseMasterTimebaseDivisor { get; set; }ExceptionsTypeDescri

### CounterTimebaseMasterTimebaseDivisor

Specifies the divisor for an external counter timebase. You can divide the counter timebase in order to measure slower signals without causing the count register to roll over.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long CounterTimebaseMasterTimebaseDivisor { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebaserate.html language=enus -->
## TOPIC 00855: CounterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to take measurements in terms of time or frequency rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can take measurements only in terms

### CounterTimebaseRate

Specifies in Hertz the frequency of the counter timebase. Specifying the rate of a counter timebase allows you to take measurements in terms of time or frequency rather than in ticks of the timebase. If you use an external timebase and do not specify the rate, you can take measurements only in terms of ticks of the timebase.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double CounterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-countertimebasesource.html language=enus -->
## TOPIC 00856: CounterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-countertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-countertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the timebase to use for the counter. SyntaxNamespace: NationalInstruments.DAQmxpublic string CounterTimebaseSource { get; set; }RemarksTypically, NI-DAQmx uses one of the internal counter timebases when performing counter measurements. Use this property to specify an extern

### CounterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the timebase to use for the counter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string CounterTimebaseSource { get; set; }

#### Remarks

Typically, NI-DAQmx uses one of the internal counter timebases when performing counter measurements. Use this property to specify an external timebase and produce custom measurement ranges that are not possible with the internal timebases.

You also can use this property to chain counters together. By using the output of a counter as the timebase of another counter, you can effectively widen a counter. For example, you can chain two 24 bit counters together to produce one 48 bit counter.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-customscalename.html language=enus -->
## TOPIC 00857: CustomScaleName

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-customscalename.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-customscalename.html
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

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-datatransfermechanism.html language=enus -->
## TOPIC 00858: DataTransferMechanism

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-datatransfermechanism.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-datatransfermechanism.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data transfer mode for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTransferMechanism DataTransferMechanism { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DataTransferMechanism

Specifies the data transfer mode for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTransferMechanism](nationalinstruments-daqmx-cidatatransfermechanism.html) DataTransferMechanism { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-datatransferrequestcondition.html language=enus -->
## TOPIC 00859: DataTransferRequestCondition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-datatransferrequestcondition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-datatransferrequestcondition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies under what condition to transfer data from the onboard memory of the device to the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDataTransferRequestCondition DataTransferRequestCondition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### DataTransferRequestCondition

Specifies under what condition to transfer data from the onboard memory of the device to the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDataTransferRequestCondition](nationalinstruments-daqmx-cidatatransferrequestcondition.html) DataTransferRequestCondition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-duplicatecountprevention.html language=enus -->
## TOPIC 00860: DuplicateCountPrevention

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-duplicatecountprevention.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-duplicatecountprevention.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable duplicate count prevention for the channel. Duplicate count prevention is enabled by default. Setting Prescaler disables duplicate count prevention unless you explicitly enable it. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DuplicateCountPrevention { get; set;

### DuplicateCountPrevention

Specifies whether to enable [duplicate count prevention](/csh?context=nidaqmx_mxdevconsid_dupcountprevention) for the channel. Duplicate count prevention is enabled by default. Setting [Prescaler](nationalinstruments-daqmx-cichannel-prescaler.html) disables duplicate count prevention unless you explicitly enable it.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DuplicateCountPrevention { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycycledigitalfilterenabled.html language=enus -->
## TOPIC 00861: DutyCycleDigitalFilterEnabled

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycycledigitalfilterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycycledigitalfilterenabled.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool DutyCycleDigitalFilterEnabled { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DutyCycleDigitalFilterEnabled

Specifies whether to apply the pulse width filter to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool DutyCycleDigitalFilterEnabled { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycycledigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00862: DutyCycleDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycycledigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycycledigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the digital filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double DutyCycleDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DutyCycleDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the digital filter recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DutyCycleDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycycledigitalfiltertimebaserate.html language=enus -->
## TOPIC 00863: DutyCycleDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycycledigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycycledigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double DutyCycleDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-D

### DutyCycleDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double DutyCycleDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycycledigitalfiltertimebasesource.html language=enus -->
## TOPIC 00864: DutyCycleDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycycledigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycycledigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string DutyCycleDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DutyCycleDigitalFilterTimebaseSource

Specifies the input terminal of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DutyCycleDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycyclelogiclevelbehavior.html language=enus -->
## TOPIC 00865: DutyCycleLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycyclelogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycyclelogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDutyCycleLogicLevelBehavior DutyCycleLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DutyCycleLogicLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDutyCycleLogicLevelBehavior](nationalinstruments-daqmx-cidutycyclelogiclevelbehavior.html) DutyCycleLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycyclestartingedge.html language=enus -->
## TOPIC 00866: DutyCycleStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycyclestartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycyclestartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies which edge of the input signal to begin the duty cycle measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDutyCycleStartingEdge DutyCycleStartingEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DutyCycleStartingEdge

Specifies which edge of the input signal to begin the duty cycle measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDutyCycleStartingEdge](nationalinstruments-daqmx-cidutycyclestartingedge.html) DutyCycleStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycycleterminal.html language=enus -->
## TOPIC 00867: DutyCycleTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycycleterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycycleterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string DutyCycleTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DutyCycleTerminal

Specifies the input terminal of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string DutyCycleTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-dutycycleterminalconfiguration.html language=enus -->
## TOPIC 00868: DutyCycleTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-dutycycleterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-dutycycleterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIDutyCycleTerminalConfiguration DutyCycleTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### DutyCycleTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIDutyCycleTerminalConfiguration](nationalinstruments-daqmx-cidutycycleterminalconfiguration.html) DutyCycleTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputdigitalfilterenable.html language=enus -->
## TOPIC 00869: EncoderAInputDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EncoderAInputDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderAInputDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EncoderAInputDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00870: EncoderAInputDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double EncoderAInputDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderAInputDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EncoderAInputDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputdigitalfiltertimebaserate.html language=enus -->
## TOPIC 00871: EncoderAInputDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double EncoderAInputDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe

### EncoderAInputDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EncoderAInputDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputdigitalfiltertimebasesource.html language=enus -->
## TOPIC 00872: EncoderAInputDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string EncoderAInputDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an er

### EncoderAInputDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string EncoderAInputDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputdigitalsynchronizationenable.html language=enus -->
## TOPIC 00873: EncoderAInputDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EncoderAInputDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by th

### EncoderAInputDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EncoderAInputDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputlogiclevelbehavior.html language=enus -->
## TOPIC 00874: EncoderAInputLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEncoderAInputLogicLevelBehavior EncoderAInputLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderAInputLogicLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderAInputLogicLevelBehavior](nationalinstruments-daqmx-ciencoderainputlogiclevelbehavior.html) EncoderAInputLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputterminal.html language=enus -->
## TOPIC 00875: EncoderAInputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which signal A is connected. SyntaxNamespace: NationalInstruments.DAQmxpublic string EncoderAInputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderAInputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which signal A is connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string EncoderAInputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderainputterminalconfiguration.html language=enus -->
## TOPIC 00876: EncoderAInputTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderainputterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderainputterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEncoderAInputTerminalConfiguration EncoderAInputTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderAInputTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderAInputTerminalConfiguration](nationalinstruments-daqmx-ciencoderainputterminalconfiguration.html) EncoderAInputTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputdigitalfilterenable.html language=enus -->
## TOPIC 00877: EncoderBInputDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EncoderBInputDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderBInputDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EncoderBInputDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00878: EncoderBInputDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double EncoderBInputDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderBInputDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EncoderBInputDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputdigitalfiltertimebaserate.html language=enus -->
## TOPIC 00879: EncoderBInputDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double EncoderBInputDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe

### EncoderBInputDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EncoderBInputDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputdigitalfiltertimebasesource.html language=enus -->
## TOPIC 00880: EncoderBInputDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string EncoderBInputDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an er

### EncoderBInputDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string EncoderBInputDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputdigitalsynchronizationenable.html language=enus -->
## TOPIC 00881: EncoderBInputDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EncoderBInputDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by th

### EncoderBInputDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EncoderBInputDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputlogiclevelbehavior.html language=enus -->
## TOPIC 00882: EncoderBInputLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEncoderBInputLogicLevelBehavior EncoderBInputLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderBInputLogicLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderBInputLogicLevelBehavior](nationalinstruments-daqmx-ciencoderbinputlogiclevelbehavior.html) EncoderBInputLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputterminal.html language=enus -->
## TOPIC 00883: EncoderBInputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which signal B is connected. SyntaxNamespace: NationalInstruments.DAQmxpublic string EncoderBInputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderBInputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which signal B is connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string EncoderBInputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderbinputterminalconfiguration.html language=enus -->
## TOPIC 00884: EncoderBInputTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderbinputterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderbinputterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEncoderBInputTerminalConfiguration EncoderBInputTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderBInputTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderBInputTerminalConfiguration](nationalinstruments-daqmx-ciencoderbinputterminalconfiguration.html) EncoderBInputTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderdecodingtype.html language=enus -->
## TOPIC 00885: EncoderDecodingType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderdecodingtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderdecodingtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. X1, X2, and X4 are valid for quadrature encoders only. TwoPulseCounting is valid for two-pulse encoders only. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEncoderDecodingType EncoderDecodingType { g

### EncoderDecodingType

Specifies how to count and interpret the pulses the encoder generates on signal A and signal B. [X1](nationalinstruments-daqmx-ciencoderdecodingtype.html), [X2](nationalinstruments-daqmx-ciencoderdecodingtype.html), and [X4](nationalinstruments-daqmx-ciencoderdecodingtype.html) are valid for [quadrature encoders](/csh?context=nidaqmx_measfunds_quadencoders) only. [TwoPulseCounting](nationalinstruments-daqmx-ciencoderdecodingtype.html) is valid for [two-pulse encoders](/csh?context=nidaqmx_measfunds_twopulse) only.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderDecodingType](nationalinstruments-daqmx-ciencoderdecodingtype.html) EncoderDecodingType { get; set; }

#### Remarks

X2 and X4 decoding are more sensitive to smaller changes in position than X1 encoding, with X4 being the most sensitive. However, more sensitive decoding is more likely to produce erroneous measurements if vibration exists in the encoder or other noise exists in the signals.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzindexenable.html language=enus -->
## TOPIC 00886: EncoderZIndexEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzindexenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzindexenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use Z indexing for the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EncoderZIndexEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderZIndexEnable

Specifies whether to use [Z indexing](/csh?context=nidaqmx_measfunds_zindexing) for the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EncoderZIndexEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzindexphase.html language=enus -->
## TOPIC 00887: EncoderZIndexPhase

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzindexphase.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzindexphase.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than AHighBHigh. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEnc

### EncoderZIndexPhase

Specifies the states at which signal A and signal B must be while signal Z is high for NI-DAQmx to reset the measurement. If signal Z is never high while signal A and signal B are high, for example, you must choose a phase other than [AHighBHigh](nationalinstruments-daqmx-ciencoderzindexphase.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderZIndexPhase](nationalinstruments-daqmx-ciencoderzindexphase.html) EncoderZIndexPhase { get; set; }

#### Remarks

When signal Z transitions to high and how long it stays high varies from encoder to encoder. Refer to the documentation for the encoder to determine the timing of signal Z with respect to signal A and signal B.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzindexvalue.html language=enus -->
## TOPIC 00888: EncoderZIndexValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzindexvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzindexvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value to which to reset the measurement when signal Z is high and signal A and signal B are at the states you specify with EncoderZIndexPhase. Specify this value in the units of the measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic double EncoderZIndexValue { get; set; }Exc

### EncoderZIndexValue

Specifies the value to which to reset the measurement when signal Z is high and signal A and signal B are at the states you specify with [EncoderZIndexPhase](nationalinstruments-daqmx-cichannel-encoderzindexphase.html). Specify this value in the units of the measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EncoderZIndexValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputdigitalfilterenable.html language=enus -->
## TOPIC 00889: EncoderZInputDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EncoderZInputDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderZInputDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EncoderZInputDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00890: EncoderZInputDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double EncoderZInputDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderZInputDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EncoderZInputDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputdigitalfiltertimebaserate.html language=enus -->
## TOPIC 00891: EncoderZInputDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double EncoderZInputDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe

### EncoderZInputDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double EncoderZInputDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputdigitalfiltertimebasesource.html language=enus -->
## TOPIC 00892: EncoderZInputDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string EncoderZInputDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an er

### EncoderZInputDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string EncoderZInputDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputdigitalsynchronizationenable.html language=enus -->
## TOPIC 00893: EncoderZInputDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool EncoderZInputDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by th

### EncoderZInputDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool EncoderZInputDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputlogiclevelbehavior.html language=enus -->
## TOPIC 00894: EncoderZInputLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEncoderZInputLogicLevelBehavior EncoderZInputLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderZInputLogicLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderZInputLogicLevelBehavior](nationalinstruments-daqmx-ciencoderzinputlogiclevelbehavior.html) EncoderZInputLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputterminal.html language=enus -->
## TOPIC 00895: EncoderZInputTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which signal Z is connected. SyntaxNamespace: NationalInstruments.DAQmxpublic string EncoderZInputTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderZInputTerminal

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) to which signal Z is connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string EncoderZInputTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-encoderzinputterminalconfiguration.html language=enus -->
## TOPIC 00896: EncoderZInputTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-encoderzinputterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-encoderzinputterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIEncoderZInputTerminalConfiguration EncoderZInputTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### EncoderZInputTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIEncoderZInputTerminalConfiguration](nationalinstruments-daqmx-ciencoderzinputterminalconfiguration.html) EncoderZInputTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-filterdelay.html language=enus -->
## TOPIC 00897: FilterDelay

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-filterdelay.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-filterdelay.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the amount of time between when the input signal transitions and when the filtered sample is read by the host device. This value is in the units specified with FilterDelayUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double FilterDelay { get; }ExceptionsTypeDescriptionNationalIns

### FilterDelay

Indicates the amount of time between when the input signal transitions and when the filtered sample is read by the host device. This value is in the units specified with [FilterDelayUnits](nationalinstruments-daqmx-cichannel-filterdelayunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FilterDelay { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-filterdelayunits.html language=enus -->
## TOPIC 00898: FilterDelayUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-filterdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-filterdelayunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units of FilterDelay. SyntaxNamespace: NationalInstruments.DAQmxpublic CIFilterDelayUnits FilterDelayUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterDelayUnits

Specifies the units of [FilterDelay](nationalinstruments-daqmx-cichannel-filterdelay.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIFilterDelayUnits](nationalinstruments-daqmx-cifilterdelayunits.html) FilterDelayUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-filterenabled.html language=enus -->
## TOPIC 00899: FilterEnabled

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-filterenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-filterenabled.html
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

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-filterfrequency.html language=enus -->
## TOPIC 00900: FilterFrequency

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-filterfrequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-filterfrequency.html
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

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-filterorder.html language=enus -->
## TOPIC 00901: FilterOrder

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-filterorder.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-filterorder.html
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

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-filterresponse.html language=enus -->
## TOPIC 00902: FilterResponse

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-filterresponse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-filterresponse.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the corresponding filter response and defines the shape of the filter response. SyntaxNamespace: NationalInstruments.DAQmxpublic CIFilterResponse FilterResponse { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FilterResponse

Specifies the corresponding filter response and defines the shape of the filter response.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIFilterResponse](nationalinstruments-daqmx-cifilterresponse.html) FilterResponse { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencydigitalfilterenable.html language=enus -->
## TOPIC 00903: FrequencyDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencydigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencydigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool FrequencyDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool FrequencyDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencydigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00904: FrequencyDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencydigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencydigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double FrequencyDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FrequencyDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencydigitalfiltertimebaserate.html language=enus -->
## TOPIC 00905: FrequencyDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencydigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencydigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double FrequencyDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-D

### FrequencyDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FrequencyDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencydigitalfiltertimebasesource.html language=enus -->
## TOPIC 00906: FrequencyDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencydigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencydigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string FrequencyDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string FrequencyDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencydigitalsynchronizationenable.html language=enus -->
## TOPIC 00907: FrequencyDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencydigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencydigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool FrequencyDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the de

### FrequencyDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool FrequencyDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencydivisor.html language=enus -->
## TOPIC 00908: FrequencyDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencydivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencydivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value by which to divide the input signal if FrequencyMeasurementMethod is LargeRangeTwoCounter. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement. SyntaxNamespace

### FrequencyDivisor

Specifies the value by which to divide the input signal if [FrequencyMeasurementMethod](nationalinstruments-daqmx-cichannel-frequencymeasurementmethod.html) is [LargeRangeTwoCounter](nationalinstruments-daqmx-cifrequencymeasurementmethod.html). The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long FrequencyDivisor { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencyenableaveraging.html language=enus -->
## TOPIC 00909: FrequencyEnableAveraging

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencyenableaveraging.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencyenableaveraging.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging mode for Sample Clock-timed frequency measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic bool FrequencyEnableAveraging { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyEnableAveraging

Specifies whether to enable [averaging mode](/csh?context=nidaqmx_mxcncpts_configtimemeas) for Sample Clock-timed frequency measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool FrequencyEnableAveraging { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencyhysteresis.html language=enus -->
## TOPIC 00910: FrequencyHysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencyhysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencyhysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level to apply to FrequencyThresholdVoltage. When FrequencyStartingEdge is rising, the source signal must first fall below FrequencyThresholdVoltage minus the hysteresis before a rising edge is detected at FrequencyThresholdVoltage. When FrequencyStartingEdge is falling, the s

### FrequencyHysteresis

Specifies a hysteresis level to apply to [FrequencyThresholdVoltage](nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html). When [FrequencyStartingEdge](nationalinstruments-daqmx-cichannel-frequencystartingedge.html) is rising, the source signal must first fall below [FrequencyThresholdVoltage](nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html) minus the hysteresis before a rising edge is detected at [FrequencyThresholdVoltage](nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html). When [FrequencyStartingEdge](nationalinstruments-daqmx-cichannel-frequencystartingedge.html) is falling, the source signal must first rise above [FrequencyThresholdVoltage](nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html) plus the hysteresis before a falling edge is detected at [FrequencyThresholdVoltage](nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FrequencyHysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencylogicallevelbehavior.html language=enus -->
## TOPIC 00911: FrequencyLogicalLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencylogicallevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencylogicallevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIFrequencyLogicLevelBehavior FrequencyLogicalLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyLogicalLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIFrequencyLogicLevelBehavior](nationalinstruments-daqmx-cifrequencylogiclevelbehavior.html) FrequencyLogicalLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencymeasurementmethod.html language=enus -->
## TOPIC 00912: FrequencyMeasurementMethod

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencymeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencymeasurementmethod.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method to use to measure the frequency of the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic CIFrequencyMeasurementMethod FrequencyMeasurementMethod { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyMeasurementMethod

Specifies the method to use to measure the frequency of the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIFrequencyMeasurementMethod](nationalinstruments-daqmx-cifrequencymeasurementmethod.html) FrequencyMeasurementMethod { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencymeasurementtime.html language=enus -->
## TOPIC 00913: FrequencyMeasurementTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencymeasurementtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencymeasurementtime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the length of time to measure the frequency of the signal if FrequencyMeasurementMethod is HighFrequencyTwoCounter. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, t

### FrequencyMeasurementTime

Specifies in seconds the length of time to measure the frequency of the signal if [FrequencyMeasurementMethod](nationalinstruments-daqmx-cichannel-frequencymeasurementmethod.html) is [HighFrequencyTwoCounter](nationalinstruments-daqmx-cifrequencymeasurementmethod.html). Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FrequencyMeasurementTime { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencystartingedge.html language=enus -->
## TOPIC 00914: FrequencyStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencystartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencystartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies between which edges to measure the frequency of the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic CIFrequencyStartingEdge FrequencyStartingEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyStartingEdge

Specifies between which edges to measure the frequency of the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIFrequencyStartingEdge](nationalinstruments-daqmx-cifrequencystartingedge.html) FrequencyStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencyterminal.html language=enus -->
## TOPIC 00915: FrequencyTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencyterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencyterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string FrequencyTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string FrequencyTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencyterminalconfiguration.html language=enus -->
## TOPIC 00916: FrequencyTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencyterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencyterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIFrequencyTerminalConfiguration FrequencyTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIFrequencyTerminalConfiguration](nationalinstruments-daqmx-cifrequencyterminalconfiguration.html) FrequencyTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html language=enus -->
## TOPIC 00917: FrequencyThresholdVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencythresholdvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. SyntaxNamespace: NationalInstruments.DAQmxpublic double F

### FrequencyThresholdVoltage

Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double FrequencyThresholdVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-frequencyunits.html language=enus -->
## TOPIC 00918: FrequencyUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-frequencyunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-frequencyunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return frequency measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic CIFrequencyUnits FrequencyUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### FrequencyUnits

Specifies the units to use to return frequency measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIFrequencyUnits](nationalinstruments-daqmx-cifrequencyunits.html) FrequencyUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-gpssyncmethod.html language=enus -->
## TOPIC 00919: GpsSyncMethod

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-gpssyncmethod.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-gpssyncmethod.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method to use to synchronize the counter to a GPS receiver. SyntaxNamespace: NationalInstruments.DAQmxpublic CIGpsSyncMethod GpsSyncMethod { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### GpsSyncMethod

Specifies the method to use to synchronize the counter to a GPS receiver.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIGpsSyncMethod](nationalinstruments-daqmx-cigpssyncmethod.html) GpsSyncMethod { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-gpssyncsource.html language=enus -->
## TOPIC 00920: GpsSyncSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-gpssyncsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-gpssyncsource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal to which the GPS synchronization signal is connected. SyntaxNamespace: NationalInstruments.DAQmxpublic string GpsSyncSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### GpsSyncSource

Specifies the [terminal](/csh?context=nidaqmx_daqhelp_connectcounter) to which the GPS synchronization signal is connected.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string GpsSyncSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-linearencoderdistanceperpulse.html language=enus -->
## TOPIC 00921: LinearEncoderDistancePerPulse

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-linearencoderdistanceperpulse.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-linearencoderdistanceperpulse.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify with LinearEncoderUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double LinearEncoderDistancePerPulse { get; set; }ExceptionsTypeDescriptionNationalInstrume

### LinearEncoderDistancePerPulse

Specifies the distance to measure for each pulse the encoder generates on signal A or signal B. This value is in the units you specify with [LinearEncoderUnits](nationalinstruments-daqmx-cichannel-linearencoderunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LinearEncoderDistancePerPulse { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-linearencoderinitialposition.html language=enus -->
## TOPIC 00922: LinearEncoderInitialPosition

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-linearencoderinitialposition.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-linearencoderinitialposition.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the position of the encoder when the measurement begins. This value is in the units you specify with LinearEncoderUnits. SyntaxNamespace: NationalInstruments.DAQmxpublic double LinearEncoderInitialPosition { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-D

### LinearEncoderInitialPosition

Specifies the position of the encoder when the measurement begins. This value is in the units you specify with [LinearEncoderUnits](nationalinstruments-daqmx-cichannel-linearencoderunits.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double LinearEncoderInitialPosition { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-linearencoderunits.html language=enus -->
## TOPIC 00923: LinearEncoderUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-linearencoderunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-linearencoderunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return linear encoder measurements from the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic CILinearEncoderUnits LinearEncoderUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### LinearEncoderUnits

Specifies the units to use to return linear encoder measurements from the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CILinearEncoderUnits](nationalinstruments-daqmx-cilinearencoderunits.html) LinearEncoderUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-maximum.html language=enus -->
## TOPIC 00924: Maximum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-maximum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-maximum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the hardware can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic double Maximum

### Maximum

Specifies the maximum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced maximum value that the hardware can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Maximum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-maximummeasurementperiod.html language=enus -->
## TOPIC 00925: MaximumMeasurementPeriod

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-maximummeasurementperiod.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-maximummeasurementperiod.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum period (in seconds) in which the device will recognize signals. For frequency measurements, a signal with a higher period than the one set in this property will return 0 Hz. For duty cycle, the device will return 0 or 1 depending on the state of the line during the max defined

### MaximumMeasurementPeriod

Specifies the maximum period (in seconds) in which the device will recognize signals. For frequency measurements, a signal with a higher period than the one set in this property will return 0 Hz. For duty cycle, the device will return 0 or 1 depending on the state of the line during the max defined period of time. Period measurements will return NaN. Pulse width measurement will return zero.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double MaximumMeasurementPeriod { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-measurementtype.html language=enus -->
## TOPIC 00926: MeasurementType

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-measurementtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-measurementtype.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement to take with the channel. SyntaxNamespace: NationalInstruments.DAQmxpublic CIMeasurementType MeasurementType { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### MeasurementType

Indicates the measurement to take with the channel.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIMeasurementType](nationalinstruments-daqmx-cimeasurementtype.html) MeasurementType { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-memorymappingenable.html language=enus -->
## TOPIC 00927: MemoryMappingEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-memorymappingenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-memorymappingenable.html
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

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-minimum.html language=enus -->
## TOPIC 00928: Minimum

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-minimum.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-minimum.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the hardware can measure with the current settings. SyntaxNamespace: NationalInstruments.DAQmxpublic double Minimum

### Minimum

Specifies the minimum value you expect to measure. This value is in the units you specify with a units property. When you query this property, it returns the coerced minimum value that the hardware can measure with the current settings.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double Minimum { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-numberpossiblyinvalidsamples.html language=enus -->
## TOPIC 00929: NumberPossiblyInvalidSamples

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-numberpossiblyinvalidsamples.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-numberpossiblyinvalidsamples.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the number of samples that the device might have overwritten before it could transfer them to the buffer. SyntaxNamespace: NationalInstruments.DAQmxpublic long NumberPossiblyInvalidSamples { get; }RemarksOn certain devices during finite buffered time measurements, it is not possible to det

### NumberPossiblyInvalidSamples

Indicates the number of samples that the device might have overwritten before it could transfer them to the buffer.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long NumberPossiblyInvalidSamples { get; }

#### Remarks

On certain devices during finite buffered time measurements, it is not possible to detect if the counter overwrites a value it read before the device could transfer the sample to the buffer. This uncertainty is present only when [DataTransferMechanism](nationalinstruments-daqmx-cichannel-datatransfermechanism.html) is [Dma](nationalinstruments-daqmx-cidatatransfermechanism.html) and occurs as the acquisition nears completion.

Once the acquisition completes, it is impossible to tell if the status value on the counter indicates an overwrite as a result of a true overwrite, or because the counter detected another edge of the input signal after the acquisition completed but before the counter could disarm. As a result of this behavior, higher frequency input signals are more likely to increase the number of possibly invalid samples.

To decrease the number of possibly invalid samples, read more often from the buffer. Reading from the buffer forces a check on the hardware status and ensures all data is valid up to the present point in the buffer. By default, NI-DAQmx checks the validity of data every fourth of the buffer. If you do not perform a read until after the device acquires all data, the value of this property is one-fourth of the buffer size or zero.

The value this property indicates is valid only while the task is in the running state. The value of this property while the task is in any other state is zero.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-outputstate.html language=enus -->
## TOPIC 00930: OutputState

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-outputstate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-outputstate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the current state of the out terminal of the counter. SyntaxNamespace: NationalInstruments.DAQmxpublic CIOutputState OutputState { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### OutputState

Indicates the current state of the [out terminal](/csh?context=nidaqmx_mxcncpts_counterparts) of the counter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIOutputState](nationalinstruments-daqmx-cioutputstate.html) OutputState { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-perioddigitalfilterenable.html language=enus -->
## TOPIC 00931: PeriodDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-perioddigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-perioddigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PeriodDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PeriodDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-perioddigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00932: PeriodDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-perioddigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-perioddigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double PeriodDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PeriodDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-perioddigitalfiltertimebaserate.html language=enus -->
## TOPIC 00933: PeriodDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-perioddigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-perioddigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double PeriodDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQm

### PeriodDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PeriodDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-perioddigitalfiltertimebasesource.html language=enus -->
## TOPIC 00934: PeriodDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-perioddigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-perioddigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string PeriodDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PeriodDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-perioddigitalsynchronizationenable.html language=enus -->
## TOPIC 00935: PeriodDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-perioddigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-perioddigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PeriodDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the devic

### PeriodDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PeriodDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-perioddivisor.html language=enus -->
## TOPIC 00936: PeriodDivisor

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-perioddivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-perioddivisor.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value by which to divide the input signal if PeriodMeasurementMethod is LargeRangeTwoCounter. The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement. SyntaxNamespace: N

### PeriodDivisor

Specifies the value by which to divide the input signal if [PeriodMeasurementMethod](nationalinstruments-daqmx-cichannel-periodmeasurementmethod.html) is [LargeRangeTwoCounter](nationalinstruments-daqmx-ciperiodmeasurementmethod.html). The larger the divisor, the more accurate the measurement. However, too large a value could cause the count register to roll over, which results in an incorrect measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long PeriodDivisor { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodenableaveraging.html language=enus -->
## TOPIC 00937: PeriodEnableAveraging

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodenableaveraging.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodenableaveraging.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging mode for Sample Clock-timed period measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PeriodEnableAveraging { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodEnableAveraging

Specifies whether to enable [averaging mode](/csh?context=nidaqmx_mxcncpts_configtimemeas) for Sample Clock-timed period measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PeriodEnableAveraging { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodhysteresis.html language=enus -->
## TOPIC 00938: PeriodHysteresis

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodhysteresis.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodhysteresis.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a hysteresis level to apply to PeriodThresholdVoltage. When PeriodStartingEdge is rising, the source signal must first fall below PeriodThresholdVoltage minus the hysteresis before a rising edge is detected at PeriodThresholdVoltage. When PeriodStartingEdge is falling, the source signal mu

### PeriodHysteresis

Specifies a hysteresis level to apply to [PeriodThresholdVoltage](nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html). When [PeriodStartingEdge](nationalinstruments-daqmx-cichannel-periodstartingedge.html) is rising, the source signal must first fall below [PeriodThresholdVoltage](nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html) minus the hysteresis before a rising edge is detected at [PeriodThresholdVoltage](nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html). When [PeriodStartingEdge](nationalinstruments-daqmx-cichannel-periodstartingedge.html) is falling, the source signal must first rise above [PeriodThresholdVoltage](nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html) plus the hysteresis before a falling edge is detected at [PeriodThresholdVoltage](nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PeriodHysteresis { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodlogiclevelbehavior.html language=enus -->
## TOPIC 00939: PeriodLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPeriodLogicLevelBehavior PeriodLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodLogicLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPeriodLogicLevelBehavior](nationalinstruments-daqmx-ciperiodlogiclevelbehavior.html) PeriodLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodmeasurementmethod.html language=enus -->
## TOPIC 00940: PeriodMeasurementMethod

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodmeasurementmethod.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodmeasurementmethod.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method to use to measure the period of the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPeriodMeasurementMethod PeriodMeasurementMethod { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodMeasurementMethod

Specifies the method to use to measure the period of the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPeriodMeasurementMethod](nationalinstruments-daqmx-ciperiodmeasurementmethod.html) PeriodMeasurementMethod { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodmeasurementtime.html language=enus -->
## TOPIC 00941: PeriodMeasurementTime

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodmeasurementtime.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodmeasurementtime.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the length of time to measure the period of the signal if PeriodMeasurementMethod is HighFrequencyTwoCounter. Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the cou

### PeriodMeasurementTime

Specifies in seconds the length of time to measure the period of the signal if [PeriodMeasurementMethod](nationalinstruments-daqmx-cichannel-periodmeasurementmethod.html) is [HighFrequencyTwoCounter](nationalinstruments-daqmx-ciperiodmeasurementmethod.html). Measurement accuracy increases with increased measurement time and with increased signal frequency. If you measure a high-frequency signal for too long, however, the count register could roll over, which results in an incorrect measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PeriodMeasurementTime { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodstartingedge.html language=enus -->
## TOPIC 00942: PeriodStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodstartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodstartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies between which edges to measure the period of the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPeriodStartingEdge PeriodStartingEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodStartingEdge

Specifies between which edges to measure the period of the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPeriodStartingEdge](nationalinstruments-daqmx-ciperiodstartingedge.html) PeriodStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodterminal.html language=enus -->
## TOPIC 00943: PeriodTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string PeriodTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PeriodTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodterminalconfiguration.html language=enus -->
## TOPIC 00944: PeriodTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPeriodTerminalConfiguration PeriodTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPeriodTerminalConfiguration](nationalinstruments-daqmx-ciperiodterminalconfiguration.html) PeriodTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html language=enus -->
## TOPIC 00945: PeriodThresholdVoltage

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodthresholdvoltage.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls. SyntaxNamespace: NationalInstruments.DAQmxpublic double P

### PeriodThresholdVoltage

Specifies the voltage level at which to recognize waveform repetitions. Select a voltage level that occurs only once within the entire period of a waveform. You also can select a voltage that occurs only once while the voltage rises or falls.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PeriodThresholdVoltage { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-periodunits.html language=enus -->
## TOPIC 00946: PeriodUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-periodunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-periodunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit to use to return period measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPeriodUnits PeriodUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PeriodUnits

Specifies the unit to use to return period measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPeriodUnits](nationalinstruments-daqmx-ciperiodunits.html) PeriodUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-prescaler.html language=enus -->
## TOPIC 00947: Prescaler

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-prescaler.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-prescaler.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the divisor to apply to the signal you connect to the counter source terminal. Scaled data that you read takes this setting into account. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the

### Prescaler

Specifies the divisor to apply to the signal you connect to the counter source terminal. Scaled data that you read takes this setting into account. You should use a prescaler only when you connect an external signal to the counter source terminal and when that signal has a higher frequency than the fastest onboard timebase. Setting this value disables duplicate count prevention unless you explicitly set [DuplicateCountPrevention](nationalinstruments-daqmx-cichannel-duplicatecountprevention.html) to true.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long Prescaler { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfilterenable.html language=enus -->
## TOPIC 00948: PulseFrequencyDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseFrequencyDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyDigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseFrequencyDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00949: PulseFrequencyDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseFrequencyDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseFrequencyDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfiltertimebaserate.html language=enus -->
## TOPIC 00950: PulseFrequencyDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseFrequencyDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### PulseFrequencyDigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseFrequencyDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfiltertimebasesource.html language=enus -->
## TOPIC 00951: PulseFrequencyDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencydigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseFrequencyDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyDigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseFrequencyDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencydigitalsynchronizationenable.html language=enus -->
## TOPIC 00952: PulseFrequencyDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencydigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencydigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseFrequencyDigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx

### PulseFrequencyDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseFrequencyDigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencylogiclevelbehavior.html language=enus -->
## TOPIC 00953: PulseFrequencyLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencylogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencylogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseFrequencyLogicLevelBehavior PulseFrequencyLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyLogicLevelBehavior

Specifies the logic level behavior on the count reset line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseFrequencyLogicLevelBehavior](nationalinstruments-daqmx-cipulsefrequencylogiclevelbehavior.html) PulseFrequencyLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencystartingedge.html language=enus -->
## TOPIC 00954: PulseFrequencyStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencystartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencystartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin pulse measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseFrequencyStartingEdge PulseFrequencyStartingEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyStartingEdge

Specifies on which edge of the input signal to begin pulse measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseFrequencyStartingEdge](nationalinstruments-daqmx-cipulsefrequencystartingedge.html) PulseFrequencyStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencyterminal.html language=enus -->
## TOPIC 00955: PulseFrequencyTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencyterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencyterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseFrequencyTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseFrequencyTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencyterminalconfiguration.html language=enus -->
## TOPIC 00956: PulseFrequencyTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencyterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencyterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseFrequencyTerminalConfiguration PulseFrequencyTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseFrequencyTerminalConfiguration](nationalinstruments-daqmx-cipulsefrequencyterminalconfiguration.html) PulseFrequencyTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsefrequencyunits.html language=enus -->
## TOPIC 00957: PulseFrequencyUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsefrequencyunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsefrequencyunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return pulse specifications in terms of frequency. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseFrequencyUnits PulseFrequencyUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseFrequencyUnits

Specifies the units to use to return pulse specifications in terms of frequency.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseFrequencyUnits](nationalinstruments-daqmx-cipulsefrequencyunits.html) PulseFrequencyUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksdigitalfilterenable.html language=enus -->
## TOPIC 00958: PulseTicksDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseTicksDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTicksDigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseTicksDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00959: PulseTicksDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseTicksDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTicksDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseTicksDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksdigitalfiltertimebaserate.html language=enus -->
## TOPIC 00960: PulseTicksDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseTicksDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQm

### PulseTicksDigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseTicksDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksdigitalfiltertimebasesource.html language=enus -->
## TOPIC 00961: PulseTicksDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseTicksDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTicksDigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseTicksDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksdigitalsynchronizationenable.html language=enus -->
## TOPIC 00962: PulseTicksDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseTicksDigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driv

### PulseTicksDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseTicksDigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetickslogiclevelbehavior.html language=enus -->
## TOPIC 00963: PulseTicksLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetickslogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetickslogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseTicksLogicLevelBehavior PulseTicksLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTicksLogicLevelBehavior

Specifies the logic level behavior on the count reset line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseTicksLogicLevelBehavior](nationalinstruments-daqmx-cipulsetickslogiclevelbehavior.html) PulseTicksLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksstartingedge.html language=enus -->
## TOPIC 00964: PulseTicksStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksstartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksstartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin pulse measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseTicksStartingEdge PulseTicksStartingEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTicksStartingEdge

Specifies on which edge of the input signal to begin pulse measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseTicksStartingEdge](nationalinstruments-daqmx-cipulseticksstartingedge.html) PulseTicksStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksterminal.html language=enus -->
## TOPIC 00965: PulseTicksTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseTicksTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTicksTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseTicksTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulseticksterminalconfiguration.html language=enus -->
## TOPIC 00966: PulseTicksTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulseticksterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulseticksterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseTicksTerminalConfiguration PulseTicksTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTicksTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseTicksTerminalConfiguration](nationalinstruments-daqmx-cipulseticksterminalconfiguration.html) PulseTicksTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimedigitalfilterenable.html language=enus -->
## TOPIC 00967: PulseTimeDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimedigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimedigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply a digital filter to the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseTimeDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeDigitalFilterEnable

Specifies whether to apply a digital [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseTimeDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimedigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00968: PulseTimeDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimedigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimedigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseTimeDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseTimeDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimedigitalfiltertimebaserate.html language=enus -->
## TOPIC 00969: PulseTimeDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimedigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimedigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseTimeDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx

### PulseTimeDigitalFilterTimebaseRate

Specifies in hertz the rate of the digital filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseTimeDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimedigitalfiltertimebasesource.html language=enus -->
## TOPIC 00970: PulseTimeDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimedigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimedigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the terminal of the signal to use as the timebase of the digital filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseTimeDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeDigitalFilterTimebaseSource

Specifies the [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the digital filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseTimeDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimedigitalsynchronizationenable.html language=enus -->
## TOPIC 00971: PulseTimeDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimedigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimedigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseTimeDigitalSynchronizationEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx drive

### PulseTimeDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseTimeDigitalSynchronizationEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimelogiclevelbehavior.html language=enus -->
## TOPIC 00972: PulseTimeLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimelogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimelogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseTimeLogicLevelBehavior PulseTimeLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeLogicLevelBehavior

Specifies the logic level behavior on the count reset line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseTimeLogicLevelBehavior](nationalinstruments-daqmx-cipulsetimelogiclevelbehavior.html) PulseTimeLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimestartingedge.html language=enus -->
## TOPIC 00973: PulseTimeStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimestartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimestartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin pulse measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseTimeStartingEdge PulseTimeStartingEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeStartingEdge

Specifies on which edge of the input signal to begin pulse measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseTimeStartingEdge](nationalinstruments-daqmx-cipulsetimestartingedge.html) PulseTimeStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimeterminal.html language=enus -->
## TOPIC 00974: PulseTimeTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimeterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimeterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseTimeTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseTimeTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimeterminalconfiguration.html language=enus -->
## TOPIC 00975: PulseTimeTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimeterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimeterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseTimeTerminalConfiguration PulseTimeTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseTimeTerminalConfiguration](nationalinstruments-daqmx-cipulsetimeterminalconfiguration.html) PulseTimeTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsetimeunits.html language=enus -->
## TOPIC 00976: PulseTimeUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsetimeunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsetimeunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return pulse specifications in terms of high time and low time. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseTimeUnits PulseTimeUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseTimeUnits

Specifies the units to use to return pulse specifications in terms of high time and low time.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseTimeUnits](nationalinstruments-daqmx-cipulsetimeunits.html) PulseTimeUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthdigitalfilterenable.html language=enus -->
## TOPIC 00977: PulseWidthDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthdigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthdigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseWidthDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseWidthDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseWidthDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthdigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00978: PulseWidthDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthdigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthdigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseWidthDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseWidthDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseWidthDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthdigitalfiltertimebaserate.html language=enus -->
## TOPIC 00979: PulseWidthDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthdigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthdigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double PulseWidthDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### PulseWidthDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double PulseWidthDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthdigitalfiltertimebasesource.html language=enus -->
## TOPIC 00980: PulseWidthDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthdigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthdigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseWidthDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### PulseWidthDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseWidthDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthdigitalsynchronizationenable.html language=enus -->
## TOPIC 00981: PulseWidthDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthdigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthdigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool PulseWidthDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the d

### PulseWidthDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool PulseWidthDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthlogiclevelbehavior.html language=enus -->
## TOPIC 00982: PulseWidthLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the input line. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseWidthLogicLevelBehavior PulseWidthLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseWidthLogicLevelBehavior

Specifies the logic level behavior on the input line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseWidthLogicLevelBehavior](nationalinstruments-daqmx-cipulsewidthlogiclevelbehavior.html) PulseWidthLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthstartingedge.html language=enus -->
## TOPIC 00983: PulseWidthStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthstartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthstartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin each pulse width measurement. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseWidthStartingEdge PulseWidthStartingEdge { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseWidthStartingEdge

Specifies on which edge of the input signal to begin each pulse width measurement.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseWidthStartingEdge](nationalinstruments-daqmx-cipulsewidthstartingedge.html) PulseWidthStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthterminal.html language=enus -->
## TOPIC 00984: PulseWidthTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string PulseWidthTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseWidthTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string PulseWidthTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthterminalconfiguration.html language=enus -->
## TOPIC 00985: PulseWidthTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseWidthTerminalConfiguration PulseWidthTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseWidthTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseWidthTerminalConfiguration](nationalinstruments-daqmx-cipulsewidthterminalconfiguration.html) PulseWidthTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-pulsewidthunits.html language=enus -->
## TOPIC 00986: PulseWidthUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-pulsewidthunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-pulsewidthunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return pulse width measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic CIPulseWidthUnits PulseWidthUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### PulseWidthUnits

Specifies the units to use to return pulse width measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CIPulseWidthUnits](nationalinstruments-daqmx-cipulsewidthunits.html) PulseWidthUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-sampleclockoverrunbehavior.html language=enus -->
## TOPIC 00987: SampleClockOverrunBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-sampleclockoverrunbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-sampleclockoverrunbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the counter behavior when data is read but a new value was not detected during a sample clock. SyntaxNamespace: NationalInstruments.DAQmxpublic CISampleClockOverrunBehavior SampleClockOverrunBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx d

### SampleClockOverrunBehavior

Specifies the counter behavior when data is read but a new value was not detected during a sample clock.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CISampleClockOverrunBehavior](nationalinstruments-daqmx-cisampleclockoverrunbehavior.html) SampleClockOverrunBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-sampleclockoverrunsentinelvalue.html language=enus -->
## TOPIC 00988: SampleClockOverrunSentinelValue

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-sampleclockoverrunsentinelvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-sampleclockoverrunsentinelvalue.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sentinel value returned when the No New Sample Behavior is set to Sentinel Value. SyntaxNamespace: NationalInstruments.DAQmxpublic int SampleClockOverrunSentinelValue { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SampleClockOverrunSentinelValue

Specifies the sentinel value returned when the No New Sample Behavior is set to Sentinel Value.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public int SampleClockOverrunSentinelValue { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperioddigitalfilterenable.html language=enus -->
## TOPIC 00989: SemiPeriodDigitalFilterEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperioddigitalfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperioddigitalfilterenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the pulse width filter to the signal. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SemiPeriodDigitalFilterEnable { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SemiPeriodDigitalFilterEnable

Specifies whether to apply the pulse width [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) to the signal.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SemiPeriodDigitalFilterEnable { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperioddigitalfilterminimumpulsewidth.html language=enus -->
## TOPIC 00990: SemiPeriodDigitalFilterMinimumPulseWidth

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperioddigitalfilterminimumpulsewidth.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperioddigitalfilterminimumpulsewidth.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in seconds the minimum pulse width the filter recognizes. SyntaxNamespace: NationalInstruments.DAQmxpublic double SemiPeriodDigitalFilterMinimumPulseWidth { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SemiPeriodDigitalFilterMinimumPulseWidth

Specifies in seconds the minimum pulse width the [filter](/csh?context=nidaqmx_mxdevconsid_digfiltering) recognizes.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SemiPeriodDigitalFilterMinimumPulseWidth { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperioddigitalfiltertimebaserate.html language=enus -->
## TOPIC 00991: SemiPeriodDigitalFilterTimebaseRate

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperioddigitalfiltertimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperioddigitalfiltertimebaserate.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter. SyntaxNamespace: NationalInstruments.DAQmxpublic double SemiPeriodDigitalFilterTimebaseRate { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-

### SemiPeriodDigitalFilterTimebaseRate

Specifies in hertz the rate of the pulse width filter timebase. NI-DAQmx uses this value to compute settings for the filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public double SemiPeriodDigitalFilterTimebaseRate { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperioddigitalfiltertimebasesource.html language=enus -->
## TOPIC 00992: SemiPeriodDigitalFilterTimebaseSource

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperioddigitalfiltertimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperioddigitalfiltertimebasesource.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to use as the timebase of the pulse width filter. SyntaxNamespace: NationalInstruments.DAQmxpublic string SemiPeriodDigitalFilterTimebaseSource { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error

### SemiPeriodDigitalFilterTimebaseSource

Specifies the input [terminal](/csh?context=nidaqmx_mxcncpts_terminal) of the signal to use as the timebase of the pulse width filter.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SemiPeriodDigitalFilterTimebaseSource { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperioddigitalsynchronizationenable.html language=enus -->
## TOPIC 00993: SemiPeriodDigitalSynchronizationEnable

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperioddigitalsynchronizationenable.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperioddigitalsynchronizationenable.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device. SyntaxNamespace: NationalInstruments.DAQmxpublic bool SemiPeriodDigitalSynchronizationEnable { get; set; }RemarksThis property does not affect the minimum pulse width recognized by the d

### SemiPeriodDigitalSynchronizationEnable

Specifies whether to synchronize recognition of transitions in the signal to the internal timebase of the device.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool SemiPeriodDigitalSynchronizationEnable { get; set; }

#### Remarks

This property does not affect the minimum pulse width recognized by the device, but setting this property to true does limit the speed at which the device recognizes transitions to less than the frequency of the internal timebase.

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperiodlogiclevelbehavior.html language=enus -->
## TOPIC 00994: SemiPeriodLogicLevelBehavior

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperiodlogiclevelbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperiodlogiclevelbehavior.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the logic level behavior on the count reset line. SyntaxNamespace: NationalInstruments.DAQmxpublic CISemiPeriodLogicLevelBehavior SemiPeriodLogicLevelBehavior { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SemiPeriodLogicLevelBehavior

Specifies the logic level behavior on the count reset line.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CISemiPeriodLogicLevelBehavior](nationalinstruments-daqmx-cisemiperiodlogiclevelbehavior.html) SemiPeriodLogicLevelBehavior { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperiodstartingedge.html language=enus -->
## TOPIC 00995: SemiPeriodStartingEdge

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperiodstartingedge.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperiodstartingedge.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies on which edge of the input signal to begin semi-period measurement. Semi-period measurements alternate between high time and low time, starting on this edge. SyntaxNamespace: NationalInstruments.DAQmxpublic CISemiPeriodStartingEdge SemiPeriodStartingEdge { get; set; }ExceptionsTypeDescript

### SemiPeriodStartingEdge

Specifies on which edge of the input signal to begin semi-period measurement. Semi-period measurements alternate between high time and low time, starting on this edge.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CISemiPeriodStartingEdge](nationalinstruments-daqmx-cisemiperiodstartingedge.html) SemiPeriodStartingEdge { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperiodterminal.html language=enus -->
## TOPIC 00996: SemiPeriodTerminal

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperiodterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperiodterminal.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal of the signal to measure. SyntaxNamespace: NationalInstruments.DAQmxpublic string SemiPeriodTerminal { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SemiPeriodTerminal

Specifies the [input terminal](/csh?context=nidaqmx_daqhelp_connectcounter) of the signal to measure.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public string SemiPeriodTerminal { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperiodterminalconfiguration.html language=enus -->
## TOPIC 00997: SemiPeriodTerminalConfiguration

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperiodterminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperiodterminalconfiguration.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the input terminal configuration. SyntaxNamespace: NationalInstruments.DAQmxpublic CISemiPeriodTerminalConfiguration SemiPeriodTerminalConfiguration { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SemiPeriodTerminalConfiguration

Specifies the input terminal configuration.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CISemiPeriodTerminalConfiguration](nationalinstruments-daqmx-cisemiperiodterminalconfiguration.html) SemiPeriodTerminalConfiguration { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-semiperiodunits.html language=enus -->
## TOPIC 00998: SemiPeriodUnits

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-semiperiodunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-semiperiodunits.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units to use to return semi-period measurements. SyntaxNamespace: NationalInstruments.DAQmxpublic CISemiPeriodUnits SemiPeriodUnits { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### SemiPeriodUnits

Specifies the units to use to return semi-period measurements.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public [CISemiPeriodUnits](nationalinstruments-daqmx-cisemiperiodunits.html) SemiPeriodUnits { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-terminalcountreached.html language=enus -->
## TOPIC 00999: TerminalCountReached

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-terminalcountreached.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-terminalcountreached.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the counter rolled over. When you query this property, NI-DAQmx resets it to false. SyntaxNamespace: NationalInstruments.DAQmxpublic bool TerminalCountReached { get; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQmx driver returned an error.

### TerminalCountReached

Indicates whether the counter rolled over. When you query this property, NI-DAQmx resets it to false.

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public bool TerminalCountReached { get; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class

<!--NI_TOPIC bundle=ni-daqmx-net-framework-api-ref path=nationalinstruments-daqmx-cichannel-timestampinitialseconds.html language=enus -->
## TOPIC 01000: TimestampInitialSeconds

- bundle_id: `ni-daqmx-net-framework-api-ref`
- source_path: `nationalinstruments-daqmx-cichannel-timestampinitialseconds.html`
- source_url: https://docs-be.ni.com/bundle/ni-daqmx-net-framework-api-ref/raw/resource/enus/nationalinstruments-daqmx-cichannel-timestampinitialseconds.html
- document_id: `ni-daqmx-net-framework-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of seconds that elapsed since the beginning of the current year. This value is ignored if GpsSyncMethod is IrigB. SyntaxNamespace: NationalInstruments.DAQmxpublic long TimestampInitialSeconds { get; set; }ExceptionsTypeDescriptionNationalInstruments.DAQmx.DaqExceptionThe NI-DAQm

### TimestampInitialSeconds

Specifies the number of seconds that elapsed since the beginning of the current year. This value is ignored if [GpsSyncMethod](nationalinstruments-daqmx-cichannel-gpssyncmethod.html) is [IrigB](nationalinstruments-daqmx-cigpssyncmethod.html).

#### Syntax

**Namespace:**[NationalInstruments.DAQmx](nationalinstruments-daqmx.html)

public long TimestampInitialSeconds { get; set; }

#### Exceptions

| Type | Description |
| --- | --- |
| NationalInstruments.DAQmx.DaqException | The NI-DAQmx driver returned an error. |

Parent topic:

CIChannel Class
