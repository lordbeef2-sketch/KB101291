# NI DOCUMENT BUNDLE: veristand-net-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-net-api-ref start=1751 end=2000 -->
<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-double-double.html language=enus -->
## TOPIC 01751: Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, double, double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-double-double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-alarmpriority-alarmstate-basenode-double-basenode-basenode-double-double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses constants to specify the UpperLimit and LowerLimit values within which AlarmChannel must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefi

### Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, double, double)

Initializes a new instance of [Alarming](nationalinstruments-veristand-systemdefinitionapi-alarming.html) with the specified name, description, and configuration. This constructor uses constants to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmChannel*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarming(string Name, string Description, AlarmPriority Priority, AlarmState DefaultState, BaseNode Alarm, double Delay, BaseNode Procedure, BaseNode AlarmChannel, double UpperLimit, double LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarming step. |
| Description | string | The description of the Alarming step. |
| Priority | AlarmPriority | The AlarmPriority level (Low, Medium, or High). |
| DefaultState | AlarmState | The default AlarmState (Enabled or Disabled). |
| Alarm | BaseNode | The Alarm to configure. If this is null, use the tripped alarm which triggered the procedure. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| Procedure | BaseNode | The Procedure to initiate when the alarm occurs. |
| AlarmChannel | BaseNode | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-uint-alarmstate-basenode-double-basenode-basenode-valuesource-valuesource.html language=enus -->
## TOPIC 01752: Alarming(string, string, uint, AlarmState, BaseNode, double, BaseNode, BaseNode, ValueSource, ValueSource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-uint-alarmstate-basenode-double-basenode-basenode-valuesource-valuesource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-alarming__string-string-uint-alarmstate-basenode-double-basenode-basenode-valuesource-valuesource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alarming with the specified name, description, and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarming(string Name, string Description, uint PriorityNumber, AlarmState DefaultState, BaseNode Alarm, double Delay, BaseNode Proc

### Alarming(string, string, uint, AlarmState, BaseNode, double, BaseNode, BaseNode, ValueSource, ValueSource)

Initializes a new instance of [Alarming](nationalinstruments-veristand-systemdefinitionapi-alarming.html) with the specified name, description, and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alarming(string Name, string Description, uint PriorityNumber, AlarmState DefaultState, BaseNode Alarm, double Delay, BaseNode Procedure, BaseNode AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarming step. |
| Description | string | The description of the Alarming step. |
| PriorityNumber | uint | The priority of the alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| DefaultState | AlarmState | The default AlarmState. |
| Alarm | BaseNode | The Alarm to configure. If this is null, use the tripped alarm which triggered the procedure. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| Procedure | BaseNode | The Procedure to initiate when the alarm occurs. |
| AlarmSource | BaseNode | The channel to monitor for alarm conditions. |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-defaultstate.html language=enus -->
## TOPIC 01753: DefaultState

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-defaultstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-defaultstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the default state (Disabled or Enabled) of the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmState DefaultState { get; set; }ReturnsAn enumeration value of AlarmState.

### DefaultState

Gets or sets the default state (Disabled or Enabled) of the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmState](nationalinstruments-veristand-systemdefinitionapi-alarmstate.html) DefaultState { get; set; }

#### Returns

An enumeration value of [AlarmState](nationalinstruments-veristand-systemdefinitionapi-alarmstate.html).

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-delay.html language=enus -->
## TOPIC 01754: Delay

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-delay.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-delay.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the amount of time to wait before triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double Delay { get; set; }ReturnsThe delay duration, in seconds.

### Delay

Gets or sets the amount of time to wait before triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double Delay { get; set; }

#### Returns

The delay duration, in seconds.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-function.html language=enus -->
## TOPIC 01755: Function

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-function.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-function.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the function that the Alarming step performs on the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmingStepFunction Function { get; set; }ReturnsAn enumeration value of AlarmingStepFunction.

### Function

Gets or sets the function that the [Alarming](nationalinstruments-veristand-systemdefinitionapi-alarming.html) step performs on the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmingStepFunction](nationalinstruments-veristand-systemdefinitionapi-alarmingstepfunction.html) Function { get; set; }

#### Returns

An enumeration value of [AlarmingStepFunction](nationalinstruments-veristand-systemdefinitionapi-alarmingstepfunction.html).

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitchannel.html language=enus -->
## TOPIC 01756: LowerLimitChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that determines the lower limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode LowerLimitChannel { get; }ReturnsA BaseNode reference to the lower limit

### LowerLimitChannel

Gets the channel that determines the lower limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) falls below this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) LowerLimitChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the lower limit channel.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitconstant.html language=enus -->
## TOPIC 01757: LowerLimitConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double LowerLimitConstant { get; }ReturnsThe constant lower limit value.

### LowerLimitConstant

Gets the constant that determines the low limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) falls below this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double LowerLimitConstant { get; }

#### Returns

The constant lower limit value.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitisconstant.html language=enus -->
## TOPIC 01758: LowerLimitIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-lowerlimitisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets information about whether the low limit value of the alarm is determined by a channel or by a constant. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool LowerLimitIsConstant { get; }Returnstrue if the lower limit is specified by a constant. false if the lower limit

### LowerLimitIsConstant

Gets information about whether the low limit value of the alarm is determined by a channel or by a constant.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool LowerLimitIsConstant { get; }

#### Returns

true if the lower limit is specified by a constant. false if the lower limit is specified by a channel.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-priority.html language=enus -->
## TOPIC 01759: Priority

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-priority.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-priority.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This property is deprecated in NI VeriStand 2011 and later. Use the PriorityNumber property instead. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmPriority Priority { get; set; }RemarksSetting this property to Low, Medium, or High automatically sets the PriorityNumber

### Priority

This property is deprecated in NI VeriStand 2011 and later. Use the [PriorityNumber](nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html) property instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmPriority](nationalinstruments-veristand-systemdefinitionapi-alarmpriority.html) Priority { get; set; }

#### Remarks

Setting this property to Low, Medium, or High automatically sets the [PriorityNumber](nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html) to 25, 15, or 5, respectively.

#### Returns

An enumeration value of [AlarmPriority](nationalinstruments-veristand-systemdefinitionapi-alarmpriority.html).

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-prioritynumber.html language=enus -->
## TOPIC 01760: PriorityNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-prioritynumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-prioritynumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint PriorityNumber { get; set; }ReturnsThe alarm priority number.

### PriorityNumber

Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint PriorityNumber { get; set; }

#### Returns

The alarm priority number.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-procedure.html language=enus -->
## TOPIC 01761: Procedure

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-procedure.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-procedure.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the procedure to initiate when the alarm conditions are met. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Procedure { get; set; }ReturnsA BaseNode reference to the procedure.

### Procedure

Gets or sets the procedure to initiate when the alarm conditions are met.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Procedure { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the procedure.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__basenode.html language=enus -->
## TOPIC 01762: SetLowerLimit(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the low limit to reference the specified channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetLowerLimit(BaseNode LowerLimit)ParametersNameTypeDescriptionLowerLimitBaseNodeThe channel that determines the low limit value of the alarm.

### SetLowerLimit(BaseNode)

Sets the low limit to reference the specified channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetLowerLimit(BaseNode LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__double.html language=enus -->
## TOPIC 01763: SetLowerLimit(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the low limit to the specified constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetLowerLimit(double LowerLimit)ParametersNameTypeDescriptionLowerLimitdoubleThe constant that determines the low limit value of the alarm.

### SetLowerLimit(double)

Sets the low limit to the specified constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetLowerLimit(double LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| LowerLimit | double | The constant that determines the low limit value of the alarm. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__valuesource.html language=enus -->
## TOPIC 01764: SetLowerLimit(ValueSource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__valuesource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-setlowerlimit__valuesource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the low limit to the specified channel or constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetLowerLimit(ValueSource LowerLimit)ParametersNameTypeDescriptionLowerLimitValueSourceThe channel or constant that determines the low limit value of the alarm

### SetLowerLimit(ValueSource)

Sets the low limit to the specified channel or constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetLowerLimit(ValueSource LowerLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__basenode.html language=enus -->
## TOPIC 01765: SetUpperLimit(BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the high limit to reference the specified channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetUpperLimit(BaseNode UpperLimit)ParametersNameTypeDescriptionUpperLimitBaseNodeThe channel that determines the high limit value of the alarm.

### SetUpperLimit(BaseNode)

Sets the high limit to reference the specified channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetUpperLimit(BaseNode UpperLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__double.html language=enus -->
## TOPIC 01766: SetUpperLimit(double)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__double.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__double.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the high limit to the specified constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetUpperLimit(double UpperLimit)ParametersNameTypeDescriptionUpperLimitdoubleThe constant that determines the high limit value of the alarm.

### SetUpperLimit(double)

Sets the high limit to the specified constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetUpperLimit(double UpperLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| UpperLimit | double | The constant that determines the high limit value of the alarm. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__valuesource.html language=enus -->
## TOPIC 01767: SetUpperLimit(ValueSource)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__valuesource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-setupperlimit__valuesource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the high limit to the specified channel or constant value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetUpperLimit(ValueSource UpperLimit)ParametersNameTypeDescriptionUpperLimitValueSourceThe channel or constant that determines the high limit value of the ala

### SetUpperLimit(ValueSource)

Sets the high limit to the specified channel or constant value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetUpperLimit(ValueSource UpperLimit)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. |

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitchannel.html language=enus -->
## TOPIC 01768: UpperLimitChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the channel that determines the upper limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode UpperLimitChannel { get; }ReturnsA BaseNode reference to the upper limit chan

### UpperLimitChannel

Gets the channel that determines the upper limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) exceeds this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) UpperLimitChannel { get; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the upper limit channel.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitconstant.html language=enus -->
## TOPIC 01769: UpperLimitConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double UpperLimitConstant { get; }ReturnsThe constant upper limit value.

### UpperLimitConstant

Gets the constant that determines the high limit value of the alarm. If the value of [AlarmSource](nationalinstruments-veristand-systemdefinitionapi-alarm-alarmsource.html) exceeds this limit, the alarm is triggered.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double UpperLimitConstant { get; }

#### Returns

The constant upper limit value.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitisconstant.html language=enus -->
## TOPIC 01770: UpperLimitIsConstant

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitisconstant.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-upperlimitisconstant.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets information about whether the high limit value of the alarm is determined by a channel or by a constant. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UpperLimitIsConstant { get; }Returnstrue if the upper limit is specified by a constant. false if the upper limit

### UpperLimitIsConstant

Gets information about whether the high limit value of the alarm is determined by a channel or by a constant.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UpperLimitIsConstant { get; }

#### Returns

true if the upper limit is specified by a constant. false if the upper limit is specified by a channel.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-usetrippedalarm.html language=enus -->
## TOPIC 01771: UseTrippedAlarm()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-usetrippedalarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-usetrippedalarm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies to use the tripped alarm which triggered the procedure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void UseTrippedAlarm()

### UseTrippedAlarm()

Specifies to use the tripped alarm which triggered the procedure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void UseTrippedAlarm()

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming-usingtrippedalarm.html language=enus -->
## TOPIC 01772: UsingTrippedAlarm

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming-usingtrippedalarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming-usingtrippedalarm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets information about whether the step is using the tripped alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool UsingTrippedAlarm { get; }Returnstrue if the step is using the tripped alarm. false if the step has a specific alarm specified.

### UsingTrippedAlarm

Gets information about whether the step is using the tripped alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool UsingTrippedAlarm { get; }

#### Returns

true if the step is using the tripped alarm. false if the step has a specific alarm specified.

Parent topic:

Alarming Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarming.html language=enus -->
## TOPIC 01773: Alarming Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Alarm Command, or Alarming, step that you can add to a Procedure. This step performs the specified Function on the specified Alarm when the step executes. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Alarming : CommandRemarksUse the

### Alarming Class

Represents an **Alarm Command**, or Alarming, step that you can add to a [Procedure](nationalinstruments-veristand-systemdefinitionapi-procedure.html). This step performs the specified [Function](nationalinstruments-veristand-systemdefinitionapi-alarming-function.html) on the specified [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarming-alarm.html) when the step executes.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Alarming : Command

#### Remarks

Use the members of this class to configure the alarm that the Alarming step calls when the procedure executes.

**Accessing this Class**

- Alarming Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, double, double) | Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses constants to specify the UpperLimit and LowerLimit values within which AlarmChannel must stay to avoid triggering the alarm. |
| Alarming(string, string, AlarmingStepFunction, BaseNode) | Initializes a new instance of Alarming with the specified Name , Description , and Function . |
| Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, double, BaseNode) | Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmChannel must stay to avoid triggering the alarm. |
| Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, BaseNode, BaseNode) | Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses channels to specify the UpperLimit and LowerLimit values within which AlarmChannel must stay to avoid triggering the alarm. |
| Alarming(string, string, AlarmPriority, AlarmState, BaseNode, double, BaseNode, BaseNode, BaseNode, double) | Initializes a new instance of Alarming with the specified name, description, and configuration. This constructor uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmChannel must stay to avoid triggering the alarm. |
| Alarming(string, string, uint, AlarmState, BaseNode, double, BaseNode, BaseNode, ValueSource, ValueSource) | Initializes a new instance of Alarming with the specified name, description, and configuration. |

#### Properties

| Name | Description |
| --- | --- |
| Alarm | Gets or sets the Alarm on which to perform the step Function. |
| AlarmChannel | Gets or sets the channel to monitor for alarm conditions. |
| DefaultState | Gets or sets the default state (Disabled or Enabled) of the alarm. |
| Delay | Gets or sets the amount of time to wait before triggering the alarm. |
| Function | Gets or sets the function that the Alarming step performs on the alarm. |
| LowerLimitChannel | Gets the channel that determines the lower limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| LowerLimitConstant | Gets the constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| LowerLimitIsConstant | Gets information about whether the low limit value of the alarm is determined by a channel or by a constant. |
| Priority | This property is deprecated in NI VeriStand 2011 and later. Use the PriorityNumber property instead. |
| PriorityNumber | Gets or sets the priority of an alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| Procedure | Gets or sets the procedure to initiate when the alarm conditions are met. |
| UpperLimitChannel | Gets the channel that determines the upper limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| UpperLimitConstant | Gets the constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| UpperLimitIsConstant | Gets information about whether the high limit value of the alarm is determined by a channel or by a constant. |
| UsingTrippedAlarm | Gets information about whether the step is using the tripped alarm. |

#### Methods

| Name | Description |
| --- | --- |
| SetLowerLimit(ValueSource) | Sets the low limit to the specified channel or constant value. |
| SetLowerLimit(double) | Sets the low limit to the specified constant value. |
| SetLowerLimit(BaseNode) | Sets the low limit to reference the specified channel. |
| SetUpperLimit(double) | Sets the high limit to the specified constant value. |
| SetUpperLimit(BaseNode) | Sets the high limit to reference the specified channel. |
| SetUpperLimit(ValueSource) | Sets the high limit to the specified channel or constant value. |
| UseTrippedAlarm() | Specifies to use the tripped alarm which triggered the procedure. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmingstepfunction.html language=enus -->
## TOPIC 01774: AlarmingStepFunction Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmingstepfunction.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmingstepfunction.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The function of an alarm running on the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum AlarmingStepFunctionMembersNameValueDescriptionAdjustSettings0Allows you to configure settings for the alarm. EnableAlarm2Enables the alarm. DisableAlarm3Disables the alarm a

### AlarmingStepFunction Enumeration

The function of an alarm running on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum AlarmingStepFunction

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AdjustSettings | 0 | Allows you to configure settings for the alarm. |
| EnableAlarm | 2 | Enables the alarm. |
| DisableAlarm | 3 | Disables the alarm and continues executing the subroutine. |
| ResetAlarmExitSubroutine | 4 | Resets the alarm and exits the subroutine. |
| DisableAlarmExitSubroutine | 5 | Disables the alarm and exits the subroutine. |
| ResetAlarm | 8 | Resets the alarm and continues executing the subroutine. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmmode.html language=enus -->
## TOPIC 01775: AlarmMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The action that occurs when the alarm is triggered on the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum AlarmModeMembersNameValueDescriptionNormal0The alarm trips if the channel value exceeds the high or low limits. IndicateOnlyThe alarm only monitors and indi

### AlarmMode Enumeration

The action that occurs when the alarm is triggered on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum AlarmMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Normal | 0 | The alarm trips if the channel value exceeds the high or low limits. |
| IndicateOnly |  | The alarm only monitors and indicates the channel value. The alarm does not trip even if the channel value exceeds the high or low limits. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmpriority.html language=enus -->
## TOPIC 01776: AlarmPriority Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmpriority.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmpriority.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This enumeration is deprecated in NI VeriStand 2011 and later. Use the PriorityNumber property instead. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum AlarmPriorityRemarksSetting this enumeration to Low, Medium, or High automatically sets the PriorityNumber to 25, 15,

### AlarmPriority Enumeration

This enumeration is deprecated in NI VeriStand 2011 and later. Use the [PriorityNumber](nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html) property instead.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum AlarmPriority

#### Remarks

Setting this enumeration to Low, Medium, or High automatically sets the [PriorityNumber](nationalinstruments-veristand-systemdefinitionapi-alarm-prioritynumber.html) to 25, 15, or 5, respectively.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Low | 0 | The alarm is a low-priority alarm. |
| Medium |  | The alarm is a medium-priority alarm. |
| High |  | The alarm is a high-priority alarm. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addalarm__alarm-out.html language=enus -->
## TOPIC 01777: AddAlarm(Alarm, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addalarm__alarm-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addalarm__alarm-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alarm to the Alarms section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarm(Alarm alarm, out Error error)ParametersNameTypeDescriptionalarmAlarmThe Alarm to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error

### AddAlarm(Alarm, out Error)

Adds the specified [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarm(Alarm alarm, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alarm | Alarm | The Alarm to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addalarm__alarm.html language=enus -->
## TOPIC 01778: AddAlarm(Alarm)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addalarm__alarm.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addalarm__alarm.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alarm to the Alarms section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarm(Alarm alarm)ParametersNameTypeDescriptionalarmAlarmThe Alarm to add.Returnstrue if the Alarm was added successfully.

### AddAlarm(Alarm)

Adds the specified [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarm(Alarm alarm)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alarm | Alarm | The Alarm to add. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addalarmfolder__alarmfolder-out.html language=enus -->
## TOPIC 01779: AddAlarmFolder(AlarmFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addalarmfolder__alarmfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addalarmfolder__alarmfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AlarmFolder to the Alarms section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarmFolder(AlarmFolder folder, out Error error)ParametersNameTypeDescriptionfolderAlarmFolderThe AlarmFolder to add.errorout ErrorReturns an NationalInstruments.Ver

### AddAlarmFolder(AlarmFolder, out Error)

Adds the specified [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarmFolder(AlarmFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AlarmFolder | The AlarmFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addalarmfolder__alarmfolder.html language=enus -->
## TOPIC 01780: AddAlarmFolder(AlarmFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addalarmfolder__alarmfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addalarmfolder__alarmfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AlarmFolder to the Alarms section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlarmFolder(AlarmFolder folder)ParametersNameTypeDescriptionfolderAlarmFolderThe AlarmFolder to add.Returnstrue if the AlarmFolder was added successfully.

### AddAlarmFolder(AlarmFolder)

Adds the specified [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlarmFolder(AlarmFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AlarmFolder | The AlarmFolder to add. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html language=enus -->
## TOPIC 01781: AddNewAlarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses channels to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionA

### AddNewAlarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses channels to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) AddNewAlarm(string Name, string Description, Channel AlarmSource, BaseNode UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01782: AddNewAlarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses channels to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionA

### AddNewAlarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses channels to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarm(string Name, string Description, Channel AlarmSource, BaseNode UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html language=enus -->
## TOPIC 01783: AddNewAlarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriSta

### AddNewAlarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses a channel to specify the *UpperLimit*  and a constant to specify the *LowerLimit*  within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) AddNewAlarm(string Name, string Description, Channel AlarmSource, BaseNode UpperLimit, double LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

The new Alarm

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01784: AddNewAlarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-basenode-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriSta

### AddNewAlarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses a channel to specify the *UpperLimit*  and a constant to specify the *LowerLimit*  within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarm(string Name, string Description, Channel AlarmSource, BaseNode UpperLimit, double LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | BaseNode | The channel that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html language=enus -->
## TOPIC 01785: AddNewAlarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriSta

### AddNewAlarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses a constant to specify the *UpperLimit*  and a channel to specify the *LowerLimit*  within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) AddNewAlarm(string Name, string Description, Channel AlarmSource, double UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

the new Alarm

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01786: AddNewAlarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-basenode-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriSta

### AddNewAlarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses a constant to specify the *UpperLimit*  and a channel to specify the *LowerLimit*  within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarm(string Name, string Description, Channel AlarmSource, double UpperLimit, BaseNode LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | BaseNode | The channel that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html language=enus -->
## TOPIC 01787: AddNewAlarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinition

### AddNewAlarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses constants to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) AddNewAlarm(string Name, string Description, Channel AlarmSource, double UpperLimit, double LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html language=enus -->
## TOPIC 01788: AddNewAlarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-double-double-procedure-alarmmode-alarmstate-alarmpriority-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinition

### AddNewAlarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section. This method uses constants to specify the *UpperLimit*  and *LowerLimit*  values within which *AlarmSource*  must stay to avoid triggering the alarm.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarm(string Name, string Description, Channel AlarmSource, double UpperLimit, double LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, AlarmPriority Priority, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | double | The constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | double | The constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| Priority | AlarmPriority | The AlarmPriority level. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-out.html language=enus -->
## TOPIC 01789: AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarm AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure Alar

### AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, out Error)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, uint GroupNumber, uint PriorityNumber, double Delay, string TripMessage, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| GroupNumber | uint | The number of the group to which the Alarm belongs. |
| PriorityNumber | uint | The priority of the alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html language=enus -->
## TOPIC 01790: AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarm__string-string-channel-valuesource-valuesource-procedure-alarmmode-alarmstate-uint-uint-double-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure Alarm

### AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string)

Adds a new [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) with the specified name, description, and configuration to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarm(string Name, string Description, Channel AlarmSource, ValueSource UpperLimit, ValueSource LowerLimit, Procedure AlarmAction, AlarmMode Mode, AlarmState DefaultState, uint GroupNumber, uint PriorityNumber, double Delay, string TripMessage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alarm. |
| Description | string | The description of the Alarm. |
| AlarmSource | Channel | The channel to monitor for alarm conditions. |
| UpperLimit | ValueSource | The channel or constant that determines the high limit value of the alarm. If the value of AlarmSource exceeds this limit, the alarm is triggered. |
| LowerLimit | ValueSource | The channel or constant that determines the low limit value of the alarm. If the value of AlarmSource falls below this limit, the alarm is triggered. |
| AlarmAction | Procedure | The Procedure to initiate when the alarm occurs. |
| Mode | AlarmMode | The AlarmMode. |
| DefaultState | AlarmState | The default AlarmState. |
| GroupNumber | uint | The number of the group to which the Alarm belongs. |
| PriorityNumber | uint | The priority of the alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. |
| Delay | double | The amount of time to wait before triggering the alarm. |
| TripMessage | string | The message to display when the alarm is tripped. |

#### Returns

true if the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarmfolder__string-string-out.html language=enus -->
## TOPIC 01791: AddNewAlarmFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarmfolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarmfolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AlarmFolder with the specified name and description to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmFolder AddNewAlarmFolder(string Name, string Description, out Error error)ParametersNameTypeDescriptionNamestringThe name of the AlarmFolde

### AddNewAlarmFolder(string, string, out Error)

Adds a new [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) with the specified name and description to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) AddNewAlarmFolder(string Name, string Description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AlarmFolder. |
| Description | string | The description of the AlarmFolder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarmfolder__string-string.html language=enus -->
## TOPIC 01792: AddNewAlarmFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarmfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-addnewalarmfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AlarmFolder with the specified name and description to the AlarmFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAlarmFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the AlarmFolder.DescriptionstringThe d

### AddNewAlarmFolder(string, string)

Adds a new [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) with the specified name and description to the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAlarmFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AlarmFolder. |
| Description | string | The description of the AlarmFolder. |

#### Returns

true if the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) was added successfully.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmfolderlist.html language=enus -->
## TOPIC 01793: GetAlarmFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the AlarmFolder elements from the Alarms section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmFolder[] GetAlarmFolderList()RemarksThis method only returns folders that are direct descendants of the Alarms section. Any modification that yo

### GetAlarmFolderList()

Gets an array that contains the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html)[] GetAlarmFolderList()

#### Remarks

Alarms

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmfolderlist__bool.html language=enus -->
## TOPIC 01794: GetAlarmFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the AlarmFolder elements from Alarms. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AlarmFolder[] GetAlarmFolderList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definition. However, any

### GetAlarmFolderList(bool)

Gets an array that contains the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html)[] GetAlarmFolderList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AlarmFolder element of the Alarms section. true if the method traverses each child AlarmFolder instance to search for other AlarmFolder instances to traverse or other AlarmFolder elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) elements from the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmlist.html language=enus -->
## TOPIC 01795: GetAlarmList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Alarm elements from the Alarms section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarm[] GetAlarmList()RemarksThis method only returns alarms that are direct descendants of the Alarms section. Any modification that you make to the conte

### GetAlarmList()

Gets an array that contains the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html)[] GetAlarmList()

#### Remarks

Alarms

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmlist__bool.html language=enus -->
## TOPIC 01796: GetAlarmList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms-getalarmlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Alarm elements from the Alarms section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alarm[] GetAlarmList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definition. However, any modifi

### GetAlarmList(bool)

Gets an array that contains the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html)[] GetAlarmList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AlarmFolder element of the Alarms section. true if the method traverses each child AlarmFolder instance to search for other AlarmFolder instances to traverse or other Alarm elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) elements from the [Alarms](nationalinstruments-veristand-systemdefinitionapi-alarms.html) section.

Parent topic:

Alarms Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarms.html language=enus -->
## TOPIC 01797: Alarms Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarms.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarms.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Alarms section of a Target, which contains any configured Alarm and AlarmFolder objects. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Alarms : SectionRemarksUse the members of this class to add new or access existing alarms or alarm

### Alarms Class

Represents the **Alarms** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html), which contains any configured [Alarm](nationalinstruments-veristand-systemdefinitionapi-alarm.html) and [AlarmFolder](nationalinstruments-veristand-systemdefinitionapi-alarmfolder.html) objects.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Alarms : Section

#### Remarks

Use the members of this class to add new or access existing alarms or alarm folders.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.Target.GetAlarms

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddAlarm(Alarm, out Error) | Adds the specified Alarm to the Alarms section. |
| AddAlarm(Alarm) | Adds the specified Alarm to the Alarms section. |
| AddAlarmFolder(AlarmFolder, out Error) | Adds the specified AlarmFolder to the Alarms section. |
| AddAlarmFolder(AlarmFolder) | Adds the specified AlarmFolder to the Alarms section. |
| AddNewAlarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarm(string, string, Channel, double, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a constant to specify the UpperLimit and a channel to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses channels to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarm(string, string, Channel, BaseNode, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses a channel to specify the UpperLimit and a constant to specify the LowerLimit within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarm(string, string, Channel, BaseNode, BaseNode, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses channels to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string) | Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. |
| AddNewAlarm(string, string, Channel, ValueSource, ValueSource, Procedure, AlarmMode, AlarmState, uint, uint, double, string, out Error) | Adds a new Alarm with the specified name, description, and configuration to the AlarmFolder. |
| AddNewAlarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarm(string, string, Channel, double, double, Procedure, AlarmMode, AlarmState, AlarmPriority, double, string, out Error) | Adds a new Alarm with the specified name, description, and configuration to the Alarms section. This method uses constants to specify the UpperLimit and LowerLimit values within which AlarmSource must stay to avoid triggering the alarm. |
| AddNewAlarmFolder(string, string) | Adds a new AlarmFolder with the specified name and description to the AlarmFolder. |
| AddNewAlarmFolder(string, string, out Error) | Adds a new AlarmFolder with the specified name and description to the AlarmFolder. |
| GetAlarmFolderList() | Gets an array that contains the AlarmFolder elements from the Alarms section. |
| GetAlarmFolderList(bool) | Gets an array that contains the AlarmFolder elements from Alarms. |
| GetAlarmList() | Gets an array that contains the Alarm elements from the Alarms section. |
| GetAlarmList(bool) | Gets an array that contains the Alarm elements from the Alarms section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmstate.html language=enus -->
## TOPIC 01798: AlarmState Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmstate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmstate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The state of an alarm on the target. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum AlarmStateMembersNameValueDescriptionDisabled0The alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. EnabledThe alarm is active. The al

### AlarmState Enumeration

The state of an alarm on the target.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum AlarmState

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Disabled | 0 | The alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. |
| Enabled |  | The alarm is active. The alarm trips if the channel value exceeds the high or low limits. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alarmstatus.html language=enus -->
## TOPIC 01799: AlarmStatus Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alarmstatus.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alarmstatus.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A channel that indicates the current status of an alarm. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class AlarmStatus : Channel

### AlarmStatus Class

A channel that indicates the current status of an alarm.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class AlarmStatus : Channel

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-alias__string-string-channel.html language=enus -->
## TOPIC 01800: Alias(string, string, Channel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-alias__string-string-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-alias__string-string-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alias with the specified name, description, and channel linked by reference. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias(string Name, string Description, Channel LinkedChannelReference)ParametersNameTypeDescriptionNamestringThe name of

### Alias(string, string, Channel)

Initializes a new instance of [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by reference.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alias(string Name, string Description, Channel LinkedChannelReference)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the alias. |
| Description | string | The description of the alias. |
| LinkedChannelReference | Channel | The reference to the channel that the alias represents. |

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-alias__string-string-string.html language=enus -->
## TOPIC 01801: Alias(string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-alias__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-alias__string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Alias with the specified name, description, and channel linked by path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias(string Name, string Description, string LinkedChannelPath)ParametersNameTypeDescriptionNamestringThe name of the alias.

### Alias(string, string, string)

Initializes a new instance of [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Alias(string Name, string Description, string LinkedChannelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the alias. |
| Description | string | The description of the alias. |
| LinkedChannelPath | string | The path to the channel that alias represents. |

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-columndimensions.html language=enus -->
## TOPIC 01802: ColumnDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-columndimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-columndimensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of columns in the linked channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ColumnDimensions { get; }ReturnsThe number of columns.

### ColumnDimensions

Gets the number of columns in the linked channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ColumnDimensions { get; }

#### Returns

The number of columns.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-datasource.html language=enus -->
## TOPIC 01803: DataSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-datasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-datasource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the source channel that maps to the current channel that this alias represents and provides it data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode DataSource { get; set; }ReturnsA BaseNode reference to the source channel.

### DataSource

Gets or sets the source channel that maps to the current channel that this alias represents and provides it data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) DataSource { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the source channel.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-getvaluetable__out-out.html language=enus -->
## TOPIC 01804: GetValueTable(out string[], out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-getvaluetable__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-getvaluetable__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value table for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetValueTable(out string[] names, out double[] values)ParametersNameTypeDescriptionnamesout string[]The names for the channel value table.valuesout double[]The values for the channel v

### GetValueTable(out string[], out double[])

Gets the value table for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetValueTable(out string[] names, out double[] values)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | out string[] | The names for the channel value table. |
| values | out double[] | The values for the channel value table. |

#### Returns

Returns true if the channel value table is defined.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-isreadable.html language=enus -->
## TOPIC 01805: IsReadable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-isreadable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-isreadable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the channel is readable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsReadable { get; }

### IsReadable

Gets a value indicating whether the channel is readable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsReadable { get; }

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-iswritable.html language=enus -->
## TOPIC 01806: IsWritable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-iswritable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-iswritable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the channel is writable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsWritable { get; }

### IsWritable

Gets a value indicating whether the channel is writable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsWritable { get; }

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-linkedchannel.html language=enus -->
## TOPIC 01807: LinkedChannel

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-linkedchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-linkedchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel that the alias represents. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode LinkedChannel { get; set; }ReturnsA BaseNode reference to the channel.

### LinkedChannel

Gets or sets the channel that the alias represents.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) LinkedChannel { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-removedatasource.html language=enus -->
## TOPIC 01808: RemoveDataSource()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-removedatasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-removedatasource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the source channel that maps to the current channel that this alias represents and provides it data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveDataSource()RemarksA BaseNode reference to the source channel.

### RemoveDataSource()

Removes the source channel that maps to the current channel that this alias represents and provides it data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveDataSource()

#### Remarks

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the source channel.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-rowdimensions.html language=enus -->
## TOPIC 01809: RowDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-rowdimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-rowdimensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of rows in the linked channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int RowDimensions { get; }ReturnsThe number of rows.

### RowDimensions

Gets the number of rows in the linked channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int RowDimensions { get; }

#### Returns

The number of rows.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-scaleunits.html language=enus -->
## TOPIC 01810: ScaleUnits

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-scaleunits.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-scaleunits.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the units of the scale associated with the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ScaleUnits { get; }RemarksThe units of the scale can be any arbitrary string. If no scale exists, then this property returns the units of the channel. ReturnsRetur

### ScaleUnits

Gets the units of the scale associated with the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ScaleUnits { get; }

#### Remarks

The units of the scale can be any arbitrary string. If no scale exists, then this property returns the units of the channel.

#### Returns

Returns a string that indicates the units of the scale associated with the channel.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias-units.html language=enus -->
## TOPIC 01811: Units

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias-units.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias-units.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the units associated with the channel. This can be any arbitrary string. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Units { get; set; }ReturnsThe units.

### Units

Gets or sets the units associated with the channel. This can be any arbitrary string.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Units { get; set; }

#### Returns

The units.

Parent topic:

Alias Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-alias.html language=enus -->
## TOPIC 01812: Alias Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-alias.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-alias.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an alias, which defines an alternate name for a channel in a system definition file. You can use the alias name, rather than the full channel path, in the Workspace window and Stimulus Profile Editor. Derives fromBaseNodeIChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinit

### Alias Class

Represents an alias, which defines an alternate name for a channel in a system definition file. You can use the alias name, rather than the full channel path, in the **Workspace** window and Stimulus Profile Editor.

#### Derives from

- BaseNode
- IChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Alias : BaseNode, IChannel

#### Remarks

Use the members of this class to get information about the alias and to get or set the channel it represents.

**Accessing this Class**

- [GetAliasesList(bool)](nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliaseslist__bool.html)
- [GetAliasesList(bool)](nationalinstruments-veristand-systemdefinitionapi-aliases-getaliaseslist__bool.html)
- Alias Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Alias(string, string, Channel) | Initializes a new instance of Alias with the specified name, description, and channel linked by reference. |
| Alias(string, string, string) | Initializes a new instance of Alias with the specified name, description, and channel linked by path. |

#### Properties

| Name | Description |
| --- | --- |
| ColumnDimensions | Gets the number of columns in the linked channel value. |
| DataSource | Gets or sets the source channel that maps to the current channel that this alias represents and provides it data. |
| IsReadable | Gets a value indicating whether the channel is readable. |
| IsWritable | Gets a value indicating whether the channel is writable. |
| LinkedChannel | Gets or sets the channel that the alias represents. |
| RowDimensions | Gets the number of rows in the linked channel value. |
| ScaleUnits | Gets the units of the scale associated with the channel. |
| Units | Gets or sets the units associated with the channel. This can be any arbitrary string. |

#### Methods

| Name | Description |
| --- | --- |
| GetValueTable(out string[], out double[]) | Gets the value table for the channel. |
| RemoveDataSource() | Removes the source channel that maps to the current channel that this alias represents and provides it data. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addalias__alias-out.html language=enus -->
## TOPIC 01813: AddAlias(Alias, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addalias__alias-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addalias__alias-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alias to the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlias(Alias alias, out Error error)ParametersNameTypeDescriptionaliasAliasThe Alias to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no erro

### AddAlias(Alias, out Error)

Adds the specified [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) to the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlias(Alias alias, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alias | Alias | The Alias to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addalias__alias.html language=enus -->
## TOPIC 01814: AddAlias(Alias)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addalias__alias.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addalias__alias.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alias to the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlias(Alias alias)ParametersNameTypeDescriptionaliasAliasThe Alias to add.Returnstrue if the Alias was added successfully.

### AddAlias(Alias)

Adds the specified [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) to the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlias(Alias alias)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alias | Alias | The Alias to add. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addaliasfolder__aliasfolder-out.html language=enus -->
## TOPIC 01815: AddAliasFolder(AliasFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addaliasfolder__aliasfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addaliasfolder__aliasfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AliasFolder to the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAliasFolder(AliasFolder folder, out Error error)ParametersNameTypeDescriptionfolderAliasFolderThe AliasFolder to add.errorout ErrorReturns an NationalInstruments.Ve

### AddAliasFolder(AliasFolder, out Error)

Adds the specified [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) to the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAliasFolder(AliasFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AliasFolder | The AliasFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addaliasfolder__aliasfolder.html language=enus -->
## TOPIC 01816: AddAliasFolder(AliasFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addaliasfolder__aliasfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addaliasfolder__aliasfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AliasFolder to the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAliasFolder(AliasFolder folder)ParametersNameTypeDescriptionfolderAliasFolderThe AliasFolder to add.Returnstrue if the AliasFolder was added successfully.

### AddAliasFolder(AliasFolder)

Adds the specified [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) to the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAliasFolder(AliasFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AliasFolder | The AliasFolder to add. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbypath__string-string-string-out.html language=enus -->
## TOPIC 01817: AddNewAliasByPath(string, string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbypath__string-string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbypath__string-string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias AddNewAliasByPath(string Name, string Description, string LinkedChannelPath, out Error error)ParametersNameTypeDescriptionNamestringThe na

### AddNewAliasByPath(string, string, string, out Error)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) AddNewAliasByPath(string Name, string Description, string LinkedChannelPath, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelPath | string | The path to the channel that Alias represents. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbypath__string-string-string.html language=enus -->
## TOPIC 01818: AddNewAliasByPath(string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbypath__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbypath__string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAliasByPath(string Name, string Description, string LinkedChannelPath)ParametersNameTypeDescriptionNamestringThe name of the Alias.De

### AddNewAliasByPath(string, string, string)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAliasByPath(string Name, string Description, string LinkedChannelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelPath | string | The path to the channel that Alias represents. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbyreference__string-string-channel-out.html language=enus -->
## TOPIC 01819: AddNewAliasByReference(string, string, Channel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbyreference__string-string-channel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbyreference__string-string-channel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by reference. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference, out Error error)ParametersNameTypeDescription

### AddNewAliasByReference(string, string, Channel, out Error)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by reference.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelReference | Channel | The reference to the channel that Alias represents. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbyreference__string-string-channel.html language=enus -->
## TOPIC 01820: AddNewAliasByReference(string, string, Channel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbyreference__string-string-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasbyreference__string-string-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by reference. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference)ParametersNameTypeDescriptionNamestringThe name

### AddNewAliasByReference(string, string, Channel)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by reference.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelReference | Channel | The reference to the channel that Alias represents. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasfolder__string-string-out.html language=enus -->
## TOPIC 01821: AddNewAliasFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasfolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasfolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AliasFolder with the specified name and description to the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AliasFolder AddNewAliasFolder(string Name, string Description, out Error error)ParametersNameTypeDescriptionNamestringThe name of the AliasF

### AddNewAliasFolder(string, string, out Error)

Adds a new [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) with the specified name and description to the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) AddNewAliasFolder(string Name, string Description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AliasFolder. |
| Description | string | The description of the AliasFolder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasfolder__string-string.html language=enus -->
## TOPIC 01822: AddNewAliasFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-addnewaliasfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AliasFolder with the specified name and description to the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAliasFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the AliasFolder.DescriptionstringT

### AddNewAliasFolder(string, string)

Adds a new [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) with the specified name and description to the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAliasFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AliasFolder. |
| Description | string | The description of the AliasFolder. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-deleteunmappedaliases.html language=enus -->
## TOPIC 01823: DeleteUnmappedAliases()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-deleteunmappedaliases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-deleteunmappedaliases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all the aliases that are not linked to any channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void DeleteUnmappedAliases()

### DeleteUnmappedAliases()

Deletes all the aliases that are not linked to any channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void DeleteUnmappedAliases()

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-exportaliasestofile__string-predicate_ichannel_-predicate_basenode..html language=enus -->
## TOPIC 01824: ExportAliasesToFile(string, Predicate< IChannel >, Predicate< BaseNode >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-exportaliasestofile__string-predicate_ichannel_-predicate_basenode..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-exportaliasestofile__string-predicate_ichannel_-predicate_basenode..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Write a TSV file where each line has 2 tab separated elements. The first element is the node path of the linked channel and the second element is the node path (relative to the Aliases node) of the alias linked to that channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### ExportAliasesToFile(string, Predicate< IChannel >, Predicate< BaseNode >)

Write a TSV file where each line has 2 tab separated elements. The first element is the node path of the linked channel and the second element is the node path (relative to the Aliases node) of the alias linked to that channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ExportAliasesToFile(string filePath, Predicate< IChannel > inclusionFilter=null, Predicate< BaseNode > recursePredicate=null)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | The file in which to store the output. |
| inclusionFilter | Predicate< IChannel > | function to specify whether we should include a particular channel. Pass null to include all |
| recursePredicate | Predicate< BaseNode > | Whether we should recurse below a given node. |

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-getaliaseslist.html language=enus -->
## TOPIC 01825: GetAliasesList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-getaliaseslist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-getaliaseslist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains Alias elements from the Aliases section. This method only returns aliases that are direct descendants of the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias[] GetAliasesList()RemarksAny modification that you make to the cont

### GetAliasesList()

Gets an array that contains [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section. This method only returns aliases that are direct descendants of the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html)[] GetAliasesList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-getaliaseslist__bool.html language=enus -->
## TOPIC 01826: GetAliasesList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-getaliaseslist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-getaliaseslist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Alias elements from the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias[] GetAliasesList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definition. However, any mod

### GetAliasesList(bool)

Gets an array that contains the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html)[] GetAliasesList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AliasFolder element of the Aliases section. true if the method traverses each child AliasFolder instance to search for other AliasFolder instances to traverse or other Alias elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-getaliasfolderlist.html language=enus -->
## TOPIC 01827: GetAliasFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-getaliasfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-getaliasfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the AliasFolder elements from the Aliases section. This method only returns folders that are direct descendants of the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AliasFolder[] GetAliasFolderList()RemarksAny modification that

### GetAliasFolderList()

Gets an array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section. This method only returns folders that are direct descendants of the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html)[] GetAliasFolderList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-getaliasfolderlist__bool.html language=enus -->
## TOPIC 01828: GetAliasFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-getaliasfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-getaliasfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the AliasFolder elements from the Aliases section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AliasFolder[] GetAliasFolderList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definition.

### GetAliasFolderList(bool)

Gets an array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html)[] GetAliasFolderList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AliasFolder element of the Aliases section. true if the method traverses each child AliasFolder instance to search for other AliasFolder instances to traverse or other AliasFolder elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section.

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases-importaliasesfromfile__string-predicate_string..html language=enus -->
## TOPIC 01829: ImportAliasesFromFile(string, Predicate< string >)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases-importaliasesfromfile__string-predicate_string..html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases-importaliasesfromfile__string-predicate_string..html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Imports aliases from a file. Each line contains an aliasable channel in the system definition. If an alias exists, it follows the channel path after a tab. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void ImportAliasesFromFile(string filePath, Predicate< string > inclusi

### ImportAliasesFromFile(string, Predicate< string >)

Imports aliases from a file. Each line contains an aliasable channel in the system definition. If an alias exists, it follows the channel path after a tab.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void ImportAliasesFromFile(string filePath, Predicate< string > inclusionFilter=null)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| filePath | string | string filePath |
| inclusionFilter | Predicate< string > | function to specify whether we should include an alias at a particular NodePath. Pass null to include all. |

Parent topic:

Aliases Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliases.html language=enus -->
## TOPIC 01830: Aliases Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliases.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliases.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Aliases section of the system definition, which contains Alias objects that define names you can use in place of full channel paths. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Aliases : SectionRemarksUse the members of this class

### Aliases Class

Represents the **Aliases** section of the system definition, which contains [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) objects that define names you can use in place of full channel paths.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Aliases : Section

#### Remarks

Use the members of this class to add a new or access an existing alias or [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

**Accessing this Class**

- [GetAliases](nationalinstruments-veristand-systemdefinitionapi-root-getaliases.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddAlias(Alias) | Adds the specified Alias to the Aliases section. |
| AddAlias(Alias, out Error) | Adds the specified Alias to the Aliases section. |
| AddAliasFolder(AliasFolder) | Adds the specified AliasFolder to the Aliases section. |
| AddAliasFolder(AliasFolder, out Error) | Adds the specified AliasFolder to the Aliases section. |
| AddNewAliasByPath(string, string, string) | Adds a new Alias with the specified name, description, and channel linked by path. |
| AddNewAliasByPath(string, string, string, out Error) | Adds a new Alias with the specified name, description, and channel linked by path. |
| AddNewAliasByReference(string, string, Channel) | Adds a new Alias with the specified name, description, and channel linked by reference. |
| AddNewAliasByReference(string, string, Channel, out Error) | Adds a new Alias with the specified name, description, and channel linked by reference. |
| AddNewAliasFolder(string, string) | Adds a new AliasFolder with the specified name and description to the Aliases section. |
| AddNewAliasFolder(string, string, out Error) | Adds a new AliasFolder with the specified name and description to the Aliases section. |
| DeleteUnmappedAliases() | Deletes all the aliases that are not linked to any channel. |
| ExportAliasesToFile(string, Predicate< IChannel >, Predicate< BaseNode >) | Write a TSV file where each line has 2 tab separated elements. The first element is the node path of the linked channel and the second element is the node path (relative to the Aliases node) of the alias linked to that channel. |
| GetAliasesList(bool) | Gets an array that contains the Alias elements from the Aliases section. |
| GetAliasesList() | Gets an array that contains Alias elements from the Aliases section. This method only returns aliases that are direct descendants of the Aliases section. |
| GetAliasFolderList() | Gets an array that contains the AliasFolder elements from the Aliases section. This method only returns folders that are direct descendants of the Aliases section. |
| GetAliasFolderList(bool) | Gets an array that contains the AliasFolder elements from the Aliases section. |
| ImportAliasesFromFile(string, Predicate< string >) | Imports aliases from a file. Each line contains an aliasable channel in the system definition. If an alias exists, it follows the channel path after a tab. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addalias__alias-out.html language=enus -->
## TOPIC 01831: AddAlias(Alias, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addalias__alias-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addalias__alias-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alias to the AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlias(Alias alias, out Error error)ParametersNameTypeDescriptionaliasAliasThe Alias to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error oc

### AddAlias(Alias, out Error)

Adds the specified [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) to the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlias(Alias alias, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alias | Alias | The Alias to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addalias__alias.html language=enus -->
## TOPIC 01832: AddAlias(Alias)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addalias__alias.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addalias__alias.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified Alias to the AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAlias(Alias alias)ParametersNameTypeDescriptionaliasAliasThe Alias to add.Returnstrue if the Alias was added successfully.

### AddAlias(Alias)

Adds the specified [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) to the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAlias(Alias alias)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| alias | Alias | The Alias to add. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addaliasfolder__aliasfolder-out.html language=enus -->
## TOPIC 01833: AddAliasFolder(AliasFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addaliasfolder__aliasfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addaliasfolder__aliasfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AliasFolder to the AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAliasFolder(AliasFolder folder, out Error error)ParametersNameTypeDescriptionfolderAliasFolderThe AliasFolder to add.errorout ErrorReturns an NationalInstruments.VeriSt

### AddAliasFolder(AliasFolder, out Error)

Adds the specified [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) to the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAliasFolder(AliasFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AliasFolder | The AliasFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addaliasfolder__aliasfolder.html language=enus -->
## TOPIC 01834: AddAliasFolder(AliasFolder)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addaliasfolder__aliasfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addaliasfolder__aliasfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified AliasFolder to the AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAliasFolder(AliasFolder folder)ParametersNameTypeDescriptionfolderAliasFolderThe AliasFolder to add.Returnstrue if the AliasFolder was added successfully.

### AddAliasFolder(AliasFolder)

Adds the specified [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) to the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAliasFolder(AliasFolder folder)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | AliasFolder | The AliasFolder to add. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbypath__string-string-string-out.html language=enus -->
## TOPIC 01835: AddNewAliasByPath(string, string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbypath__string-string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbypath__string-string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias AddNewAliasByPath(string Name, string Description, string LinkedChannelPath, out Error error)ParametersNameTypeDescriptionNamestringThe na

### AddNewAliasByPath(string, string, string, out Error)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) AddNewAliasByPath(string Name, string Description, string LinkedChannelPath, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelPath | string | The path to the channel that Alias represents. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbypath__string-string-string.html language=enus -->
## TOPIC 01836: AddNewAliasByPath(string, string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbypath__string-string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbypath__string-string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAliasByPath(string Name, string Description, string LinkedChannelPath)ParametersNameTypeDescriptionNamestringThe name of the Alias.De

### AddNewAliasByPath(string, string, string)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAliasByPath(string Name, string Description, string LinkedChannelPath)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelPath | string | The path to the channel that Alias represents. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbyreference__string-string-channel-out.html language=enus -->
## TOPIC 01837: AddNewAliasByReference(string, string, Channel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbyreference__string-string-channel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbyreference__string-string-channel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by reference. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference, out Error error)ParametersNameTypeDescription

### AddNewAliasByReference(string, string, Channel, out Error)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by reference.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelReference | Channel | The reference to the channel that Alias represents. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbyreference__string-string-channel.html language=enus -->
## TOPIC 01838: AddNewAliasByReference(string, string, Channel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbyreference__string-string-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasbyreference__string-string-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Alias with the specified name, description, and channel linked by reference. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference)ParametersNameTypeDescriptionNamestringThe name

### AddNewAliasByReference(string, string, Channel)

Adds a new [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) with the specified name, description, and channel linked by reference.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAliasByReference(string Name, string Description, Channel LinkedChannelReference)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Alias. |
| Description | string | The description of the Alias. |
| LinkedChannelReference | Channel | The reference to the channel that Alias represents. |

#### Returns

true if the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasfolder__string-string-out.html language=enus -->
## TOPIC 01839: AddNewAliasFolder(string, string, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasfolder__string-string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasfolder__string-string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AliasFolder with the specified name and description to the AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AliasFolder AddNewAliasFolder(string Name, string Description, out Error error)ParametersNameTypeDescriptionNamestringThe name of the AliasFolde

### AddNewAliasFolder(string, string, out Error)

Adds a new [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) with the specified name and description to the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) AddNewAliasFolder(string Name, string Description, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AliasFolder. |
| Description | string | The description of the AliasFolder. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasfolder__string-string.html language=enus -->
## TOPIC 01840: AddNewAliasFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-addnewaliasfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new AliasFolder with the specified name and description to the AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddNewAliasFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the AliasFolder.DescriptionstringThe d

### AddNewAliasFolder(string, string)

Adds a new [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) with the specified name and description to the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddNewAliasFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AliasFolder. |
| Description | string | The description of the AliasFolder. |

#### Returns

true if the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) was added successfully.

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-aliasfolder__string-string.html language=enus -->
## TOPIC 01841: AliasFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-aliasfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-aliasfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of AliasFolder with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AliasFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the AliasFolder.DescriptionstringThe description

### AliasFolder(string, string)

Initializes a new instance of [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public AliasFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the AliasFolder. |
| Description | string | The description of the AliasFolder. |

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliaseslist.html language=enus -->
## TOPIC 01842: GetAliasesList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliaseslist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliaseslist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Alias elements from the current AliasFolder. This method only returns aliases that are direct descendants of the current AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias[] GetAliasesList()RemarksAny modification that you make

### GetAliasesList()

Gets an array that contains the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html). This method only returns aliases that are direct descendants of the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html)[] GetAliasesList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliaseslist__bool.html language=enus -->
## TOPIC 01843: GetAliasesList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliaseslist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliaseslist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the Alias elements from the current AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Alias[] GetAliasesList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definition. However, any

### GetAliasesList(bool)

Gets an array that contains the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html)[] GetAliasesList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AliasFolder element of the AliasFolder instance. true if the method traverses each child AliasFolder instance to search for other AliasFolder instances to traverse or other Alias elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the [Alias](nationalinstruments-veristand-systemdefinitionapi-alias.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliasfolderlist.html language=enus -->
## TOPIC 01844: GetAliasFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliasfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliasfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the AliasFolder elements from the current AliasFolder. This method only returns folders that are direct descendants of the current AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AliasFolder[] GetAliasFolderList()RemarksAny modificati

### GetAliasFolderList()

Gets an array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html). This method only returns folders that are direct descendants of the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html)[] GetAliasFolderList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliasfolderlist__bool.html language=enus -->
## TOPIC 01845: GetAliasFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliasfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliasfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the AliasFolder elements from the current AliasFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic AliasFolder[] GetAliasFolderList(bool deep)RemarksAny modification that you make to the contents of this array also apply to the system definiti

### GetAliasFolderList(bool)

Gets an array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html)[] GetAliasFolderList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child AliasFolder element of the AliasFolder instance. true if the method traverses each child AliasFolder instance to search for other AliasFolder instances to traverse or other AliasFolder elements to add to the result list; otherwise false. |

#### Returns

An array that contains the [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html) elements from the current [AliasFolder](nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html).

Parent topic:

AliasFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html language=enus -->
## TOPIC 01846: AliasFolder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-aliasfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a folder under the Aliases section of the system definition. Folders simply organize aliases into logical groups. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class AliasFolder : SectionRemarksUse the members of this class to add a new or acc

### AliasFolder Class

Represents a folder under the [Aliases](nationalinstruments-veristand-systemdefinitionapi-aliases.html) section of the system definition. Folders simply organize aliases into logical groups.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class AliasFolder : Section

#### Remarks

Use the members of this class to add a new or access an existing alias or subfolder within the current alias folder.

**Accessing this Class**

- [GetAliasFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-aliases-getaliasfolderlist__bool.html)
- [GetAliasFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-aliasfolder-getaliasfolderlist__bool.html)
- AliasFolder Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| AliasFolder(string, string) | Initializes a new instance of AliasFolder with the specified name and description. |

#### Methods

| Name | Description |
| --- | --- |
| AddAlias(Alias) | Adds the specified Alias to the AliasFolder. |
| AddAlias(Alias, out Error) | Adds the specified Alias to the AliasFolder. |
| AddAliasFolder(AliasFolder, out Error) | Adds the specified AliasFolder to the AliasFolder. |
| AddAliasFolder(AliasFolder) | Adds the specified AliasFolder to the AliasFolder. |
| AddNewAliasByPath(string, string, string, out Error) | Adds a new Alias with the specified name, description, and channel linked by path. |
| AddNewAliasByPath(string, string, string) | Adds a new Alias with the specified name, description, and channel linked by path. |
| AddNewAliasByReference(string, string, Channel, out Error) | Adds a new Alias with the specified name, description, and channel linked by reference. |
| AddNewAliasByReference(string, string, Channel) | Adds a new Alias with the specified name, description, and channel linked by reference. |
| AddNewAliasFolder(string, string) | Adds a new AliasFolder with the specified name and description to the AliasFolder. |
| AddNewAliasFolder(string, string, out Error) | Adds a new AliasFolder with the specified name and description to the AliasFolder. |
| GetAliasesList() | Gets an array that contains the Alias elements from the current AliasFolder. This method only returns aliases that are direct descendants of the current AliasFolder. |
| GetAliasesList(bool) | Gets an array that contains the Alias elements from the current AliasFolder. |
| GetAliasFolderList() | Gets an array that contains the AliasFolder elements from the current AliasFolder. This method only returns folders that are direct descendants of the current AliasFolder. |
| GetAliasFolderList(bool) | Gets an array that contains the AliasFolder elements from the current AliasFolder. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcounter.html language=enus -->
## TOPIC 01847: GetCounter()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcounter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcounter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Counter channel under an AutomaticFrameProcessing section of an outgoing NI-XNET CAN frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Counter GetCounter()ReturnsA Counter object.

### GetCounter()

Gets the [Counter](nationalinstruments-veristand-systemdefinitionapi-counter.html) channel under an [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section of an outgoing NI-XNET CAN frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Counter](nationalinstruments-veristand-systemdefinitionapi-counter.html) GetCounter()

#### Returns

A [Counter](nationalinstruments-veristand-systemdefinitionapi-counter.html) object.

Parent topic:

AutomaticFrameProcessing Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcrc.html language=enus -->
## TOPIC 01848: GetCRC()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcrc.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing-getcrc.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CRC (cyclic redundancy check) channel under an AutomaticFrameProcessing section of an outgoing NI-XNET CAN frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CRC GetCRC()ReturnsA CRC object.

### GetCRC()

Gets the [CRC](nationalinstruments-veristand-systemdefinitionapi-crc.html) (cyclic redundancy check) channel under an [AutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html) section of an outgoing NI-XNET CAN frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CRC](nationalinstruments-veristand-systemdefinitionapi-crc.html) GetCRC()

#### Returns

A [CRC](nationalinstruments-veristand-systemdefinitionapi-crc.html) object.

Parent topic:

AutomaticFrameProcessing Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html language=enus -->
## TOPIC 01849: AutomaticFrameProcessing Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-automaticframeprocessing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents an Automatic Frame Processing section under an outgoing frame of an NI-XNET CAN port. The Automatic Frame Processing section contains CRC and Counter channels. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class AutomaticFrameProcessing : Sect

### AutomaticFrameProcessing Class

Represents an **Automatic Frame Processing** section under an outgoing frame of an NI-XNET CAN port. The **Automatic Frame Processing** section contains [CRC](nationalinstruments-veristand-systemdefinitionapi-crc.html) and [Counter](nationalinstruments-veristand-systemdefinitionapi-counter.html) channels.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class AutomaticFrameProcessing : Section

#### Remarks

Use the members of this class to access [CRC](nationalinstruments-veristand-systemdefinitionapi-crc.html) and [Counter](nationalinstruments-veristand-systemdefinitionapi-counter.html) channels.

**Accessing this Class**

- [CreateAutomaticFrameProcessing(out Error)](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe-createautomaticframeprocessing__out.1.html)
- [GetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-rawdatabasedframe-getautomaticframeprocessing.html)
- [CreateAutomaticFrameProcessing(out Error)](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-createautomaticframeprocessing__out.1.html)
- [GetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-signalbasedframe-getautomaticframeprocessing.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| GetCounter() | Gets the Counter channel under an AutomaticFrameProcessing section of an outgoing NI-XNET CAN frame. |
| GetCRC() | Gets the CRC (cyclic redundancy check) channel under an AutomaticFrameProcessing section of an outgoing NI-XNET CAN frame. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-average-average__string-string-uint-channel.html language=enus -->
## TOPIC 01850: Average(string, string, uint, Channel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-average-average__string-string-uint-channel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-average-average__string-string-uint-channel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Average with the specified name, description, and configuration. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Average(string Name, string Description, uint NumberOfPoints, Channel ChannelToAverage)ParametersNameTypeDescriptionNamestringThe na

### Average(string, string, uint, Channel)

Initializes a new instance of [Average](nationalinstruments-veristand-systemdefinitionapi-average.html) with the specified name, description, and configuration.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Average(string Name, string Description, uint NumberOfPoints, Channel ChannelToAverage)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the Average calculated channel. |
| Description | string | The description of the Average calculated channel. |
| NumberOfPoints | uint | The number of points of data you want to include in the average. |
| ChannelToAverage | Channel | The channel for which you want to calculate the average value. |

Parent topic:

Average Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-average-channeltoaverage.html language=enus -->
## TOPIC 01851: ChannelToAverage

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-average-channeltoaverage.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-average-channeltoaverage.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the channel for which to calculate the average value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode ChannelToAverage { get; set; }ReturnsA BaseNode reference to the channel.

### ChannelToAverage

Gets or sets the channel for which to calculate the average value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) ChannelToAverage { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the channel.

Parent topic:

Average Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-average-numberofpoints.html language=enus -->
## TOPIC 01852: NumberOfPoints

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-average-numberofpoints.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-average-numberofpoints.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the number of points of data to include in the average. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint NumberOfPoints { get; set; }ReturnsThe number of points to include in the average.

### NumberOfPoints

Gets or sets the number of points of data to include in the average.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint NumberOfPoints { get; set; }

#### Returns

The number of points to include in the average.

Parent topic:

Average Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-average.html language=enus -->
## TOPIC 01853: Average Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-average.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-average.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a calculated channel with the average function. The average function calculates the average value of the channel you specify every n points. Derives fromCalculatedChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class Average : CalculatedChannelRemarksUse th

### Average Class

Represents a calculated channel with the average function. The average function calculates the average value of the channel you specify every *n* points.

#### Derives from

- CalculatedChannel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class Average : CalculatedChannel

#### Remarks

Use the members of this class to get or set the averaged channel and the number of points used to perform the averaging.

**Accessing this Class**

- Average Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| Average(string, string, uint, Channel) | Initializes a new instance of Average with the specified name, description, and configuration. |

#### Properties

| Name | Description |
| --- | --- |
| ChannelToAverage | Gets or sets the channel for which to calculate the average value. |
| NumberOfPoints | Gets or sets the number of points of data to include in the average. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-basenodetype.html language=enus -->
## TOPIC 01854: BaseNodeType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a reference to the internal representation of this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNodeType BaseNodeType { get; }ReturnsA reference to the internal representation of the node.

### BaseNodeType

Gets a reference to the internal representation of this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public BaseNodeType BaseNodeType { get; }

#### Returns

A reference to the internal representation of the node.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-description.html language=enus -->
## TOPIC 01855: Description

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-description.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-description.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the description of this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Description { get; set; }ReturnsThe description of the node.

### Description

Gets or sets the description of this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Description { get; set; }

#### Returns

The description of the node.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-equals__object.html language=enus -->
## TOPIC 01856: Equals(object)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-equals__object.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-equals__object.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override bool Equals(object obj)

### Equals(object)

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override bool Equals(object obj)

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-findchildrenbyguid__string.html language=enus -->
## TOPIC 01857: FindChildrenByGUID(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-findchildrenbyguid__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-findchildrenbyguid__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode[] FindChildrenByGUID(string TypeGUID)RemarksModifications you make to the contents of this list apply to t

### FindChildrenByGUID(string)

Gets an array that contains the child [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) elements of the current node that match the specified *TypeGUID* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html)[] FindChildrenByGUID(string TypeGUID)

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| TypeGUID | string | The GUID to find. |

#### Returns

An array that contains the child [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) elements of the current node.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-findfirstchildwithname__string-out-bool.html language=enus -->
## TOPIC 01858: FindFirstChildWithName(string, out BaseNode, bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-findfirstchildwithname__string-out-bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-findfirstchildwithname__string-out-bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the first child node with the specified name. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool FindFirstChildWithName(string Name, out BaseNode Child, bool DeepHierarchy)ParametersNameTypeDescriptionNamestringThe name of the node to find.Childout BaseNodeUpon return

### FindFirstChildWithName(string, out BaseNode, bool)

Gets the first child node with the specified name.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool FindFirstChildWithName(string Name, out BaseNode Child, bool DeepHierarchy)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the node to find. |
| Child | out BaseNode | Upon return, contains the child node, or null if not found. |
| DeepHierarchy | bool | true to search the entire hierarchy beneath this node. FALSE to search only the children of this node. |

#### Returns

true if a child node with the specified name was found successfully.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-findnodebypath__string-out.html language=enus -->
## TOPIC 01859: FindNodeByPath(string, out BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-findnodebypath__string-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-findnodebypath__string-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a node using the specified path. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool FindNodeByPath(string nodepath, out BaseNode Node)ParametersNameTypeDescriptionnodepathstringThe path to the node. The path is relative to path of this node.Nodeout BaseNodeUpon return

### FindNodeByPath(string, out BaseNode)

Gets a node using the specified path.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool FindNodeByPath(string nodepath, out BaseNode Node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| nodepath | string | The path to the node. The path is relative to path of this node. |
| Node | out BaseNode | Upon return, contains the node with the specified nodepath , or null if not found. |

#### Returns

true if a node with the specified path was found successfully.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-getchildren.html language=enus -->
## TOPIC 01860: GetChildren()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-getchildren.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-getchildren.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the child BaseNode elements of the current node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode[] GetChildren()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications you make to

### GetChildren()

Gets an array that contains the child [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) elements of the current node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html)[] GetChildren()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the child [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) elements of the current node.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-getdocumentpath.html language=enus -->
## TOPIC 01861: GetDocumentPath()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-getdocumentpath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-getdocumentpath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the system definition file that owns this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string GetDocumentPath()ReturnsThe path to the system definition file on disk.

### GetDocumentPath()

Gets the path to the system definition file that owns this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string GetDocumentPath()

#### Returns

The path to the system definition file on disk.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-getdocumentroot.html language=enus -->
## TOPIC 01862: GetDocumentRoot()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-getdocumentroot.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-getdocumentroot.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Root node of the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Root GetDocumentRoot()ReturnsThe Root of this node, or null if not found.

### GetDocumentRoot()

Gets the [Root](nationalinstruments-veristand-systemdefinitionapi-root.html) node of the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Root](nationalinstruments-veristand-systemdefinitionapi-root.html) GetDocumentRoot()

#### Returns

The [Root](nationalinstruments-veristand-systemdefinitionapi-root.html) of this node, or null if not found.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-gethashcode.html language=enus -->
## TOPIC 01863: GetHashCode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-gethashcode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-gethashcode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic override int GetHashCode()

### GetHashCode()

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public override int GetHashCode()

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-getnodeerrors.html language=enus -->
## TOPIC 01864: GetNodeErrors()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-getnodeerrors.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-getnodeerrors.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets all the reported errors for this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic IEnumerable< Error > GetNodeErrors()ReturnsA collection of errors.

### GetNodeErrors()

Gets all the reported errors for this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public IEnumerable< Error > GetNodeErrors()

#### Returns

A collection of errors.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-getparent__out.html language=enus -->
## TOPIC 01865: GetParent(out BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-getparent__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-getparent__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the parent node of this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetParent(out BaseNode Parent)ParametersNameTypeDescriptionParentout BaseNodeThe parent node, or null if not found.Returnstrue if the parent node was found successfully.

### GetParent(out BaseNode)

Gets the parent node of this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetParent(out BaseNode Parent)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Parent | out BaseNode | The parent node, or null if not found. |

#### Returns

true if the parent node was found successfully.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-logfileproducer.html language=enus -->
## TOPIC 01866: LogFileProducer

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-logfileproducer.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-logfileproducer.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the node is a log file producer. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool LogFileProducer { get; set; }

### LogFileProducer

Gets a value indicating whether the node is a log file producer.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool LogFileProducer { get; set; }

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-name.html language=enus -->
## TOPIC 01867: Name

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-name.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-name.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of this node. To rename a node, use the RenameNode(string) method. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string Name { get; }ReturnsThe name of the node.

### Name

Gets the name of this node. To rename a node, use the [RenameNode(string)](nationalinstruments-veristand-systemdefinitionapi-basenode-renamenode__string.html) method.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string Name { get; }

#### Returns

The name of the node.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-nodeid.html language=enus -->
## TOPIC 01868: NodeID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-nodeid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-nodeid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the ID of this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ulong NodeID { get; }ReturnsThe node ID.

### NodeID

Gets the ID of this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong NodeID { get; }

#### Returns

The node ID.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-nodepath.html language=enus -->
## TOPIC 01869: NodePath

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-nodepath.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-nodepath.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the path to the node within the system definition file. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string NodePath { get; }ReturnsThe path to the node.

### NodePath

Gets the path to the node within the system definition file.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string NodePath { get; }

#### Returns

The path to the node.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-operator_eq__basenode-basenode.html language=enus -->
## TOPIC 01870: operator==(BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-operator_eq__basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-operator_eq__basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compare two items for equality. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool operator==(BaseNode left, BaseNode right)ParametersNameTypeDescriptionleftBaseNodeThe left itemrightBaseNodeThe right itemReturnsTrue if the items are equal

### operator==(BaseNode, BaseNode)

Compare two items for equality.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool operator==(BaseNode left, BaseNode right)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| left | BaseNode | The left item |
| right | BaseNode | The right item |

#### Returns

True if the items are equal

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-operator_neq__basenode-basenode.html language=enus -->
## TOPIC 01871: operator!=(BaseNode, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-operator_neq__basenode-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-operator_neq__basenode-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Compare two items for inequality. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static bool operator!=(BaseNode left, BaseNode right)ParametersNameTypeDescriptionleftBaseNodeThe left itemrightBaseNodeThe right itemReturnsTrue if the items are not equal

### operator!=(BaseNode, BaseNode)

Compare two items for inequality.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static bool operator!=(BaseNode left, BaseNode right)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| left | BaseNode | The left item |
| right | BaseNode | The right item |

#### Returns

True if the items are not equal

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-removenode.html language=enus -->
## TOPIC 01872: RemoveNode()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-removenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-removenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes this node from the hierarchy, if the node can be removed. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool RemoveNode()Returnstrue if the node was removed successfully.

### RemoveNode()

Removes this node from the hierarchy, if the node can be removed.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool RemoveNode()

#### Returns

true if the node was removed successfully.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-renamenode__string.html language=enus -->
## TOPIC 01873: RenameNode(string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-renamenode__string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-renamenode__string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool RenameNode(string NewName)ParametersNameTypeDescriptionNewNamestringThe nam

### RenameNode(string)

Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool RenameNode(string NewName)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| NewName | string | The name of the node. |

#### Returns

true if the node was renamed successfully.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode-typeguid.html language=enus -->
## TOPIC 01874: TypeGUID

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode-typeguid.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode-typeguid.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string TypeGUID { get; set; }ReturnsThe node GUID.

### TypeGUID

Gets the GUID associated with the node. Attempts to set the GUID of a [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) will generate an exception.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string TypeGUID { get; set; }

#### Returns

The node GUID.

Parent topic:

BaseNode Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-basenode.html language=enus -->
## TOPIC 01875: BaseNode Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents generic nodes in the system definition and provides access to options and configuration settings that all nodes support. Derives fromobjectSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class BaseNode : objectRemarksYou can use the members of this class to get pr

### BaseNode Class

Represents generic nodes in the system definition and provides access to options and configuration settings that all nodes support.

#### Derives from

- object

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class BaseNode : object

#### Remarks

You can use the members of this class to get properties of a node such as its name, ID, and associated GUID, to rename or remove a node, and to traverse the system definition tree.

**Accessing this Class**

- [IDToBaseNode](nationalinstruments-veristand-systemdefinitionapi-nodeidutil-idtobasenode__ulong.html)

Note

You can access this class from almost any other class that represents a node in the system definition.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Properties

| Name | Description |
| --- | --- |
| BaseNodeType | Gets a reference to the internal representation of this node. |
| Description | Gets or sets the description of this node. |
| LogFileProducer | Gets a value indicating whether the node is a log file producer. |
| Name | Gets the name of this node. To rename a node, use the RenameNode(string) method. |
| NodeID | Gets the ID of this node. |
| NodePath | Gets the path to the node within the system definition file. |
| TypeGUID | Gets the GUID associated with the node. Attempts to set the GUID of a BaseNode will generate an exception. |

#### Methods

| Name | Description |
| --- | --- |
| Equals(object) |  |
| FindChildrenByGUID(string) | Gets an array that contains the child BaseNode elements of the current node that match the specified TypeGUID . |
| FindFirstChildWithName(string, out BaseNode, bool) | Gets the first child node with the specified name. |
| FindNodeByPath(string, out BaseNode) | Gets a node using the specified path. |
| GetChildren() | Gets an array that contains the child BaseNode elements of the current node. |
| GetDocumentPath() | Gets the path to the system definition file that owns this node. |
| GetDocumentRoot() | Gets the Root node of the system definition file. |
| GetHashCode() |  |
| GetNodeErrors() | Gets all the reported errors for this node. |
| GetParent(out BaseNode) | Gets the parent node of this node. |
| RemoveNode() | Removes this node from the hierarchy, if the node can be removed. |
| RenameNode(string) | Renames this node to the name you specify, if the node can be renamed and if the name you specify is not already in use by a sibling of this node. |

#### Operators

| Name | Description |
| --- | --- |
| operator!=(BaseNode, BaseNode) | Compare two items for inequality. |
| operator==(BaseNode, BaseNode) | Compare two items for equality. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-acceleration.html language=enus -->
## TOPIC 01876: Acceleration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-acceleration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-acceleration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The acceleration function calculates the acceleration and velocity of the channel you specify. The calculated channel stores the acceleration value. The channel you specify when you configure the calculated channel stores the velocity. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionA

### Acceleration

The acceleration function calculates the acceleration and velocity of the channel you specify. The calculated channel stores the acceleration value. The channel you specify when you configure the calculated channel stores the velocity.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Acceleration

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-average.html language=enus -->
## TOPIC 01877: Average

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-average.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-average.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The average function calculates the average value of the channel you specify every n points. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Average

### Average

The average function calculates the average value of the channel you specify every *n* points.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Average

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-calculatedchanneltype.html language=enus -->
## TOPIC 01878: CalculatedChannelType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-calculatedchanneltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-calculatedchanneltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type of the calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ushort CalculatedChannelType { get; }ReturnsAn integer representing the channel type.

### CalculatedChannelType

Gets the type of the calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ushort CalculatedChannelType { get; }

#### Returns

An integer representing the channel type.

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-conditional.html language=enus -->
## TOPIC 01879: Conditional

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-conditional.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-conditional.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Conditional

### Conditional

The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Conditional

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-downcast.html language=enus -->
## TOPIC 01880: Downcast()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-downcast.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-downcast.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Casts CalculatedChannel to a more specific type. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannel Downcast()ReturnsA downcast CalculatedChannel object.

### Downcast()

Casts [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) to a more specific type.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) Downcast()

#### Returns

A downcast [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) object.

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-formula.html language=enus -->
## TOPIC 01881: Formula

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-formula.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-formula.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The formula function calculates the result of the formula you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Formula

### Formula

The formula function calculates the result of the formula you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Formula

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-lowpassfilter.html language=enus -->
## TOPIC 01882: LowpassFilter

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-lowpassfilter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-lowpassfilter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The lowpass filter function applies a lowpass Butterworth filter to the value of the channel you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort LowpassFilter

### LowpassFilter

The lowpass filter function applies a lowpass Butterworth filter to the value of the channel you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort LowpassFilter

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-maximum.html language=enus -->
## TOPIC 01883: Maximum

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-maximum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-maximum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The maximum function compares two values and returns the larger value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Maximum

### Maximum

The maximum function compares two values and returns the larger value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Maximum

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-minimum.html language=enus -->
## TOPIC 01884: Minimum

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-minimum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-minimum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The minimum function compares two values and returns the smaller value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic const ushort Minimum

### Minimum

The minimum function compares two values and returns the smaller value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort Minimum

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-peakandvalley.html language=enus -->
## TOPIC 01885: PeakAndValley

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-peakandvalley.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel-peakandvalley.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The peak and valley function calculates the peak, valley, and offset of a cyclical waveform on the channel you specify. The calculated channel stores the peak value. The channels you specify when you configure the calculated channel store the valley and offset values. SyntaxNamespace: NationalInstru

### PeakAndValley

The peak and valley function calculates the peak, valley, and offset of a cyclical waveform on the channel you specify. The calculated channel stores the peak value. The channels you specify when you configure the calculated channel store the valley and offset values.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public const ushort PeakAndValley

Parent topic:

CalculatedChannel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html language=enus -->
## TOPIC 01886: CalculatedChannel Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a calculated channel, which produces new values based on calculations performed on other channels in the system definition. Derives fromChannelSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CalculatedChannel : ChannelRemarksUse the members of this class to

### CalculatedChannel Class

Represents a calculated channel, which produces new values based on calculations performed on other channels in the system definition.

#### Derives from

- Channel

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CalculatedChannel : Channel

#### Remarks

Use the members of this class to get the type of a calculated channel or to downcast the type to a more specific type.

**Accessing this Class**

- [GetCalculatedChannelList](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannellist.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Fields

| Name | Description |
| --- | --- |
| Acceleration | The acceleration function calculates the acceleration and velocity of the channel you specify. The calculated channel stores the acceleration value. The channel you specify when you configure the calculated channel stores the velocity. |
| Average | The average function calculates the average value of the channel you specify every n points. |
| Conditional | The conditional function uses an if/else statement to check the channel you specify for the condition you specify and return the appropriate value. |
| Formula | The formula function calculates the result of the formula you specify. |
| LowpassFilter | The lowpass filter function applies a lowpass Butterworth filter to the value of the channel you specify. |
| Maximum | The maximum function compares two values and returns the larger value. |
| Minimum | The minimum function compares two values and returns the smaller value. |
| PeakAndValley | The peak and valley function calculates the peak, valley, and offset of a cyclical waveform on the channel you specify. The calculated channel stores the peak value. The channels you specify when you configure the calculated channel store the valley and offset values. |

#### Properties

| Name | Description |
| --- | --- |
| CalculatedChannelType | Gets the type of the calculated channel. |

#### Methods

| Name | Description |
| --- | --- |
| Downcast() | Casts CalculatedChannel to a more specific type. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-addcalculatedchannel__calculatedchannel-out.html language=enus -->
## TOPIC 01887: AddCalculatedChannel(CalculatedChannel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-addcalculatedchannel__calculatedchannel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-addcalculatedchannel__calculatedchannel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified CalculatedChannel to the CalculatedChannelFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCalculatedChannel(CalculatedChannel calculatedChannel, out Error error)ParametersNameTypeDescriptioncalculatedChannelCalculatedChannelThe CalculatedCh

### AddCalculatedChannel(CalculatedChannel, out Error)

Adds the specified [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) to the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCalculatedChannel(CalculatedChannel calculatedChannel, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| calculatedChannel | CalculatedChannel | The CalculatedChannel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) was added successfully.

Parent topic:

CalculatedChannelFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-addcalculatedchannelfolder__calculatedchannelfolder-out.html language=enus -->
## TOPIC 01888: AddCalculatedChannelFolder(CalculatedChannelFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-addcalculatedchannelfolder__calculatedchannelfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-addcalculatedchannelfolder__calculatedchannelfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified CalculatedChannelFolder to the CalculatedChannelFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCalculatedChannelFolder(CalculatedChannelFolder folder, out Error error)ParametersNameTypeDescriptionfolderCalculatedChannelFolderThe Calculated

### AddCalculatedChannelFolder(CalculatedChannelFolder, out Error)

Adds the specified [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) to the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCalculatedChannelFolder(CalculatedChannelFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | CalculatedChannelFolder | The CalculatedChannelFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) was added successfully.

Parent topic:

CalculatedChannelFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-calculatedchannelfolder__string-string.html language=enus -->
## TOPIC 01889: CalculatedChannelFolder(string, string)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-calculatedchannelfolder__string-string.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-calculatedchannelfolder__string-string.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CalculatedChannelFolder with the specified name and description. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannelFolder(string Name, string Description)ParametersNameTypeDescriptionNamestringThe name of the CalculatedChannelFold

### CalculatedChannelFolder(string, string)

Initializes a new instance of [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) with the specified name and description.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CalculatedChannelFolder(string Name, string Description)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the CalculatedChannelFolder. |
| Description | string | The description of the CalculatedChannelFolder. |

Parent topic:

CalculatedChannelFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelfolderlist.html language=enus -->
## TOPIC 01890: GetCalculatedChannelFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannelFolder. This method only returns folders that are direct descendants of the current CalculatedChannelFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannelFo

### GetCalculatedChannelFolderList()

Gets an array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html). This method only returns folders that are direct descendants of the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html)[] GetCalculatedChannelFolderList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

Parent topic:

CalculatedChannelFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelfolderlist__bool.html language=enus -->
## TOPIC 01891: GetCalculatedChannelFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannelFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannelFolder[] GetCalculatedChannelFolderList(bool deep)RemarksAny modification that you make to the contents

### GetCalculatedChannelFolderList(bool)

Gets an array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html)[] GetCalculatedChannelFolderList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child CalculatedChannelFolder element of the CalculatedChannelFolder instance. true if the method traverses each child CalculatedChannelFolder instance to search for other CalculatedChannelFolder instances to traverse or other CalculatedChannelFolder elements to add to the result list; otherwise false. |

#### Returns

An array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

Parent topic:

CalculatedChannelFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelslist.html language=enus -->
## TOPIC 01892: GetCalculatedChannelsList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelslist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelslist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannel elements from the current CalculatedChannelFolder. This method only returns CalculatedChannels that are direct descendants of the current CalculatedChannelFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChan

### GetCalculatedChannelsList()

Gets an array that contains the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html). This method only returns CalculatedChannels that are direct descendants of the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html)[] GetCalculatedChannelsList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

Parent topic:

CalculatedChannelFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelslist__bool.html language=enus -->
## TOPIC 01893: GetCalculatedChannelsList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelslist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelslist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannel elements from the current CalculatedChannelFolder. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannel[] GetCalculatedChannelsList(bool deep)RemarksAny modification that you make to the contents of this array al

### GetCalculatedChannelsList(bool)

Gets an array that contains the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html)[] GetCalculatedChannelsList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child CalculatedChannelFolder element of the CalculatedChannelFolder instance. true if the method traverses each child CalculatedChannelFolder instance to search for other CalculatedChannelFolder instances to traverse or other CalculatedChannel elements to add to the result list; otherwise false. |

#### Returns

Returns an array that contains the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) elements from the current [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html).

Parent topic:

CalculatedChannelFolder Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html language=enus -->
## TOPIC 01894: CalculatedChannelFolder Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a folder under the CalculatedChannels section of the system definition. Folders simply organize CalculatedChannels into logical groups. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CalculatedChannelFolder : SectionRemarksUse the members

### CalculatedChannelFolder Class

Represents a folder under the [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) section of the system definition. Folders simply organize CalculatedChannels into logical groups.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CalculatedChannelFolder : Section

#### Remarks

Use the members of this class to add a new or access an existing CalculatedChannel or subfolder within the current CalculatedChannel folder.

**Accessing this Class**

- [GetCalculatedChannelFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannelfolderlist__bool.html)
- [GetCalculatedChannelFolderList(bool)](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder-getcalculatedchannelfolderlist__bool.html)
- CalculatedChannelFolder Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CalculatedChannelFolder(string, string) | Initializes a new instance of CalculatedChannelFolder with the specified name and description. |

#### Methods

| Name | Description |
| --- | --- |
| AddCalculatedChannel(CalculatedChannel, out Error) | Adds the specified CalculatedChannel to the CalculatedChannelFolder. |
| AddCalculatedChannelFolder(CalculatedChannelFolder, out Error) | Adds the specified CalculatedChannelFolder to the CalculatedChannelFolder. |
| GetCalculatedChannelFolderList() | Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannelFolder. This method only returns folders that are direct descendants of the current CalculatedChannelFolder. |
| GetCalculatedChannelFolderList(bool) | Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannelFolder. |
| GetCalculatedChannelsList(bool) | Gets an array that contains the CalculatedChannel elements from the current CalculatedChannelFolder. |
| GetCalculatedChannelsList() | Gets an array that contains the CalculatedChannel elements from the current CalculatedChannelFolder. This method only returns CalculatedChannels that are direct descendants of the current CalculatedChannelFolder. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addacceleration__acceleration-out.html language=enus -->
## TOPIC 01895: AddAcceleration(Acceleration, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addacceleration__acceleration-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addacceleration__acceleration-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an Acceleration calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAcceleration(Acceleration acceleration, out Error error)ParametersNameTypeDescriptionaccelerationAccelerationThe Acceleration calculated channel to add.errorout ErrorReturns an N

### AddAcceleration(Acceleration, out Error)

Adds an [Acceleration](nationalinstruments-veristand-systemdefinitionapi-acceleration.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAcceleration(Acceleration acceleration, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| acceleration | Acceleration | The Acceleration calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Acceleration](nationalinstruments-veristand-systemdefinitionapi-acceleration.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addacceleration__acceleration.html language=enus -->
## TOPIC 01896: AddAcceleration(Acceleration)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addacceleration__acceleration.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addacceleration__acceleration.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an Acceleration calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAcceleration(Acceleration acceleration)ParametersNameTypeDescriptionaccelerationAccelerationThe Acceleration calculated channel to add.Returnstrue if the Acceleration calculated

### AddAcceleration(Acceleration)

Adds an [Acceleration](nationalinstruments-veristand-systemdefinitionapi-acceleration.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAcceleration(Acceleration acceleration)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| acceleration | Acceleration | The Acceleration calculated channel to add. |

#### Returns

true if the [Acceleration](nationalinstruments-veristand-systemdefinitionapi-acceleration.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addaverage__average-out.html language=enus -->
## TOPIC 01897: AddAverage(Average, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addaverage__average-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addaverage__average-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an Average calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAverage(Average average, out Error error)ParametersNameTypeDescriptionaverageAverageThe Average calculated channel to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error

### AddAverage(Average, out Error)

Adds an [Average](nationalinstruments-veristand-systemdefinitionapi-average.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAverage(Average average, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| average | Average | The Average calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Average](nationalinstruments-veristand-systemdefinitionapi-average.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addaverage__average.html language=enus -->
## TOPIC 01898: AddAverage(Average)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addaverage__average.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addaverage__average.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an Average calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddAverage(Average average)ParametersNameTypeDescriptionaverageAverageThe Average calculated channel to add.Returnstrue if the Average calculated channel was added successfully.

### AddAverage(Average)

Adds an [Average](nationalinstruments-veristand-systemdefinitionapi-average.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddAverage(Average average)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| average | Average | The Average calculated channel to add. |

#### Returns

true if the [Average](nationalinstruments-veristand-systemdefinitionapi-average.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannel__calculatedchannel-out.html language=enus -->
## TOPIC 01899: AddCalculatedChannel(CalculatedChannel, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannel__calculatedchannel-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannel__calculatedchannel-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a CalculatedChannel of any type to the CalculatedChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCalculatedChannel(CalculatedChannel calculatedChannel, out Error error)ParametersNameTypeDescriptioncalculatedChannelCalculatedChannelThe Calculate

### AddCalculatedChannel(CalculatedChannel, out Error)

Adds a [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) of any type to the [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCalculatedChannel(CalculatedChannel calculatedChannel, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| calculatedChannel | CalculatedChannel | The CalculatedChannel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannel__calculatedchannel.html language=enus -->
## TOPIC 01900: AddCalculatedChannel(CalculatedChannel)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannel__calculatedchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannel__calculatedchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a CalculatedChannel of any type to the CalculatedChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCalculatedChannel(CalculatedChannel calculatedChannel)ParametersNameTypeDescriptioncalculatedChannelCalculatedChannelThe CalculatedChannel to add.R

### AddCalculatedChannel(CalculatedChannel)

Adds a [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) of any type to the [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCalculatedChannel(CalculatedChannel calculatedChannel)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| calculatedChannel | CalculatedChannel | The CalculatedChannel to add. |

#### Returns

true if the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannelfolder__calculatedchannelfolder-out.html language=enus -->
## TOPIC 01901: AddCalculatedChannelFolder(CalculatedChannelFolder, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannelfolder__calculatedchannelfolder-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addcalculatedchannelfolder__calculatedchannelfolder-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified CalculatedChannelFolder to the CalculatedChannels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCalculatedChannelFolder(CalculatedChannelFolder folder, out Error error)ParametersNameTypeDescriptionfolderCalculatedChannelFolderThe CalculatedChann

### AddCalculatedChannelFolder(CalculatedChannelFolder, out Error)

Adds the specified [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) to the [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCalculatedChannelFolder(CalculatedChannelFolder folder, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| folder | CalculatedChannelFolder | The CalculatedChannelFolder to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addconditional__conditional-out.html language=enus -->
## TOPIC 01902: AddConditional(Conditional, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addconditional__conditional-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addconditional__conditional-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Conditional calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddConditional(Conditional conditional, out Error error)ParametersNameTypeDescriptionconditionalConditionalThe Conditional calculated channel to add.errorout ErrorReturns an NationalI

### AddConditional(Conditional, out Error)

Adds a [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddConditional(Conditional conditional, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| conditional | Conditional | The Conditional calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addconditional__conditional.html language=enus -->
## TOPIC 01903: AddConditional(Conditional)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addconditional__conditional.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addconditional__conditional.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Conditional calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddConditional(Conditional conditional)ParametersNameTypeDescriptionconditionalConditionalThe Conditional calculated channel to add.Returnstrue if the Conditional calculated channel w

### AddConditional(Conditional)

Adds a [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddConditional(Conditional conditional)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| conditional | Conditional | The Conditional calculated channel to add. |

#### Returns

true if the [Conditional](nationalinstruments-veristand-systemdefinitionapi-conditional.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addformula__formula-out.html language=enus -->
## TOPIC 01904: AddFormula(Formula, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addformula__formula-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addformula__formula-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Formula calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFormula(Formula formula, out Error error)ParametersNameTypeDescriptionformulaFormulaThe Formula calculated channel to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error o

### AddFormula(Formula, out Error)

Adds a [Formula](nationalinstruments-veristand-systemdefinitionapi-formula.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFormula(Formula formula, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| formula | Formula | The Formula calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Formula](nationalinstruments-veristand-systemdefinitionapi-formula.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addformula__formula.html language=enus -->
## TOPIC 01905: AddFormula(Formula)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addformula__formula.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addformula__formula.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Formula calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddFormula(Formula formula)ParametersNameTypeDescriptionformulaFormulaThe Formula calculated channel to add.Returnstrue if the Formula calculated channel was added successfully.

### AddFormula(Formula)

Adds a [Formula](nationalinstruments-veristand-systemdefinitionapi-formula.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddFormula(Formula formula)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| formula | Formula | The Formula calculated channel to add. |

#### Returns

true if the [Formula](nationalinstruments-veristand-systemdefinitionapi-formula.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addlowpassfilter__lowpassfilter-out.html language=enus -->
## TOPIC 01906: AddLowpassFilter(LowpassFilter, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addlowpassfilter__lowpassfilter-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addlowpassfilter__lowpassfilter-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a LowpassFilter calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddLowpassFilter(LowpassFilter lowpassFilter, out Error error)ParametersNameTypeDescriptionlowpassFilterLowpassFilterThe LowpassFilter calculated channel to add.errorout ErrorReturn

### AddLowpassFilter(LowpassFilter, out Error)

Adds a [LowpassFilter](nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddLowpassFilter(LowpassFilter lowpassFilter, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| lowpassFilter | LowpassFilter | The LowpassFilter calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [LowpassFilter](nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addlowpassfilter__lowpassfilter.html language=enus -->
## TOPIC 01907: AddLowpassFilter(LowpassFilter)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addlowpassfilter__lowpassfilter.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addlowpassfilter__lowpassfilter.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a LowpassFilter calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddLowpassFilter(LowpassFilter lowpassFilter)ParametersNameTypeDescriptionlowpassFilterLowpassFilterThe LowpassFilter calculated channel to add.Returnstrue if the LowpassFilter calc

### AddLowpassFilter(LowpassFilter)

Adds a [LowpassFilter](nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddLowpassFilter(LowpassFilter lowpassFilter)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| lowpassFilter | LowpassFilter | The LowpassFilter calculated channel to add. |

#### Returns

true if the [LowpassFilter](nationalinstruments-veristand-systemdefinitionapi-lowpassfilter.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addmaximum__maximum-out.html language=enus -->
## TOPIC 01908: AddMaximum(Maximum, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addmaximum__maximum-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addmaximum__maximum-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Maximum calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddMaximum(Maximum maximum, out Error error)ParametersNameTypeDescriptionmaximumMaximumThe Maximum calculated channel to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error o

### AddMaximum(Maximum, out Error)

Adds a [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddMaximum(Maximum maximum, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximum | Maximum | The Maximum calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addmaximum__maximum.html language=enus -->
## TOPIC 01909: AddMaximum(Maximum)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addmaximum__maximum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addmaximum__maximum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Maximum calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddMaximum(Maximum maximum)ParametersNameTypeDescriptionmaximumMaximumThe Maximum calculated channel to add.Returnstrue if the Maximum calculated channel was added successfully.

### AddMaximum(Maximum)

Adds a [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddMaximum(Maximum maximum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| maximum | Maximum | The Maximum calculated channel to add. |

#### Returns

true if the [Maximum](nationalinstruments-veristand-systemdefinitionapi-maximum.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addminimum__minimum-out.html language=enus -->
## TOPIC 01910: AddMinimum(Minimum, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addminimum__minimum-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addminimum__minimum-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Minimum calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddMinimum(Minimum minimum, out Error error)ParametersNameTypeDescriptionminimumMinimumThe Minimum calculated channel to add.errorout ErrorReturns an NationalInstruments.VeriStand.Error o

### AddMinimum(Minimum, out Error)

Adds a [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddMinimum(Minimum minimum, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minimum | Minimum | The Minimum calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addminimum__minimum.html language=enus -->
## TOPIC 01911: AddMinimum(Minimum)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addminimum__minimum.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addminimum__minimum.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a Minimum calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddMinimum(Minimum minimum)ParametersNameTypeDescriptionminimumMinimumThe Minimum calculated channel to add.Returnstrue if the Minimum calculated channel was added successfully.

### AddMinimum(Minimum)

Adds a [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddMinimum(Minimum minimum)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| minimum | Minimum | The Minimum calculated channel to add. |

#### Returns

true if the [Minimum](nationalinstruments-veristand-systemdefinitionapi-minimum.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addpeakandvalley__peakandvalley-out.html language=enus -->
## TOPIC 01912: AddPeakAndValley(PeakAndValley, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addpeakandvalley__peakandvalley-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addpeakandvalley__peakandvalley-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a PeakAndValley calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddPeakAndValley(PeakAndValley peakAndValley, out Error error)ParametersNameTypeDescriptionpeakAndValleyPeakAndValleyThe PeakAndValley calculated channel to add.errorout ErrorReturn

### AddPeakAndValley(PeakAndValley, out Error)

Adds a [PeakAndValley](nationalinstruments-veristand-systemdefinitionapi-peakandvalley.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddPeakAndValley(PeakAndValley peakAndValley, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| peakAndValley | PeakAndValley | The PeakAndValley calculated channel to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [PeakAndValley](nationalinstruments-veristand-systemdefinitionapi-peakandvalley.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addpeakandvalley__peakandvalley.html language=enus -->
## TOPIC 01913: AddPeakAndValley(PeakAndValley)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addpeakandvalley__peakandvalley.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-addpeakandvalley__peakandvalley.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a PeakAndValley calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddPeakAndValley(PeakAndValley peakAndValley)ParametersNameTypeDescriptionpeakAndValleyPeakAndValleyThe PeakAndValley calculated channel to add.Returnstrue if the PeakAndValley calc

### AddPeakAndValley(PeakAndValley)

Adds a [PeakAndValley](nationalinstruments-veristand-systemdefinitionapi-peakandvalley.html) calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddPeakAndValley(PeakAndValley peakAndValley)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| peakAndValley | PeakAndValley | The PeakAndValley calculated channel to add. |

#### Returns

true if the [PeakAndValley](nationalinstruments-veristand-systemdefinitionapi-peakandvalley.html) calculated channel was added successfully.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannelfolderlist.html language=enus -->
## TOPIC 01914: GetCalculatedChannelFolderList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannelfolderlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannelfolderlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannels. This method only returns folders that are direct descendants of the current CalculatedChannels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannelFolder[] Get

### GetCalculatedChannelFolderList()

Gets an array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html). This method only returns folders that are direct descendants of the current [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html)[] GetCalculatedChannelFolderList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

Returns an array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html).

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannelfolderlist__bool.html language=enus -->
## TOPIC 01915: GetCalculatedChannelFolderList(bool)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannelfolderlist__bool.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannelfolderlist__bool.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannelFolder[] GetCalculatedChannelFolderList(bool deep)RemarksAny modification that you make to the contents of t

### GetCalculatedChannelFolderList(bool)

Gets an array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html)[] GetCalculatedChannelFolderList(bool deep)

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| deep | bool | Specifies whether the method traverses each child CalculatedChannelFolder element of the CalculatedChannels instance. true if the method traverses each child CalculatedChannelFolder instance to search for other CalculatedChannelFolder instances to traverse or other CalculatedChannelFolder elements to add to the result list; otherwise false. |

#### Returns

An array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements from the current [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html).

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannellist.html language=enus -->
## TOPIC 01916: GetCalculatedChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getcalculatedchannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannel elements of the CalculatedChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannel[] GetCalculatedChannelList()RemarksModifications you make to the contents of this list apply to the system definiti

### GetCalculatedChannelList()

Gets an array that contains the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) elements of the [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html)[] GetCalculatedChannelList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

#### Returns

An array that contains the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) elements of the [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html) section.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getorderedchannellist.html language=enus -->
## TOPIC 01917: GetOrderedChannelList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getorderedchannellist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-getorderedchannellist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CalculatedChannel elements, in execution order, from the current CalculatedChannels. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CalculatedChannel[] GetOrderedChannelList()RemarksAny modification that you make to the contents of this array

### GetOrderedChannelList()

Gets an array that contains the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) elements, in execution order, from the current [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html)[] GetOrderedChannelList()

#### Remarks

Note

Any modification that you make to the contents of this array also apply to the system definition. However, any modification that you make to the array container does not affect the system definition. For example, any modification that you make by calling Array.SetValue() or Array.Clear() does not affect the system definition.

#### Returns

An array that contains the [CalculatedChannelFolder](nationalinstruments-veristand-systemdefinitionapi-calculatedchannelfolder.html) elements, in execution order, from the current [CalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html).

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-reorderchannellist__calculatedchannel_arr1-out.html language=enus -->
## TOPIC 01918: ReorderChannelList(CalculatedChannel[], out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-reorderchannellist__calculatedchannel_arr1-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-reorderchannellist__calculatedchannel_arr1-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rearranges the order in which NI VeriStand reads values from each calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ReorderChannelList(CalculatedChannel[] channels, out Error error)ParametersNameTypeDescriptionchannelsCalculatedChannel[]An array of Cal

### ReorderChannelList(CalculatedChannel[], out Error)

Rearranges the order in which NI VeriStand reads values from each calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ReorderChannelList(CalculatedChannel[] channels, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channels | CalculatedChannel[] | An array of CalculatedChannel elements arranged in the order in which you want to read values. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) objects were reordered successfully. Otherwise false. This method can return false if *channels* includes an additional CalculatedChannel object, a missing CalculatedChannel object, or a CalculatedChannel object that does not match an existing CalculatedChannel.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-reorderchannellist__calculatedchannel_arr1.html language=enus -->
## TOPIC 01919: ReorderChannelList(CalculatedChannel[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-reorderchannellist__calculatedchannel_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels-reorderchannellist__calculatedchannel_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Rearranges the order in which NI VeriStand reads values from each calculated channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool ReorderChannelList(CalculatedChannel[] channels)ParametersNameTypeDescriptionchannelsCalculatedChannel[]An array of CalculatedChannel el

### ReorderChannelList(CalculatedChannel[])

Rearranges the order in which NI VeriStand reads values from each calculated channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool ReorderChannelList(CalculatedChannel[] channels)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| channels | CalculatedChannel[] | An array of CalculatedChannel elements arranged in the order in which you want to read values. |

#### Returns

true if the [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) objects were reordered successfully. Otherwise false. This method can return false if *channels* includes an additional CalculatedChannel object, a missing CalculatedChannel object, or a CalculatedChannel object that does not match an existing CalculatedChannel.

Parent topic:

CalculatedChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html language=enus -->
## TOPIC 01920: CalculatedChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-calculatedchannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Calculated Channels section of a Target. This section contains CalculatedChannel objects that perform calculations on other channels in the system. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CalculatedChannels : SectionRemarksUse

### CalculatedChannels Class

Represents the **Calculated Channels** section of a [Target](nationalinstruments-veristand-systemdefinitionapi-target.html). This section contains [CalculatedChannel](nationalinstruments-veristand-systemdefinitionapi-calculatedchannel.html) objects that perform calculations on other channels in the system.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CalculatedChannels : Section

#### Remarks

Use the members of this class to add or access calculated channels, and to reorder the list of calculated channels within the system definition file.

**Accessing this Class**

- [GetCalculatedChannels](nationalinstruments-veristand-systemdefinitionapi-target-getcalculatedchannels.html)

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddAcceleration(Acceleration, out Error) | Adds an Acceleration calculated channel. |
| AddAcceleration(Acceleration) | Adds an Acceleration calculated channel. |
| AddAverage(Average) | Adds an Average calculated channel. |
| AddAverage(Average, out Error) | Adds an Average calculated channel. |
| AddCalculatedChannel(CalculatedChannel) | Adds a CalculatedChannel of any type to the CalculatedChannels section. |
| AddCalculatedChannel(CalculatedChannel, out Error) | Adds a CalculatedChannel of any type to the CalculatedChannels section. |
| AddCalculatedChannelFolder(CalculatedChannelFolder, out Error) | Adds the specified CalculatedChannelFolder to the CalculatedChannels. |
| AddConditional(Conditional) | Adds a Conditional calculated channel. |
| AddConditional(Conditional, out Error) | Adds a Conditional calculated channel. |
| AddFormula(Formula, out Error) | Adds a Formula calculated channel. |
| AddFormula(Formula) | Adds a Formula calculated channel. |
| AddLowpassFilter(LowpassFilter) | Adds a LowpassFilter calculated channel. |
| AddLowpassFilter(LowpassFilter, out Error) | Adds a LowpassFilter calculated channel. |
| AddMaximum(Maximum) | Adds a Maximum calculated channel. |
| AddMaximum(Maximum, out Error) | Adds a Maximum calculated channel. |
| AddMinimum(Minimum) | Adds a Minimum calculated channel. |
| AddMinimum(Minimum, out Error) | Adds a Minimum calculated channel. |
| AddPeakAndValley(PeakAndValley, out Error) | Adds a PeakAndValley calculated channel. |
| AddPeakAndValley(PeakAndValley) | Adds a PeakAndValley calculated channel. |
| GetCalculatedChannelFolderList() | Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannels. This method only returns folders that are direct descendants of the current CalculatedChannels. |
| GetCalculatedChannelFolderList(bool) | Gets an array that contains the CalculatedChannelFolder elements from the current CalculatedChannels. |
| GetCalculatedChannelList() | Gets an array that contains the CalculatedChannel elements of the CalculatedChannels section. |
| GetOrderedChannelList() | Gets an array that contains the CalculatedChannel elements, in execution order, from the current CalculatedChannels. |
| ReorderChannelList(CalculatedChannel[]) | Rearranges the order in which NI VeriStand reads values from each calculated channel. |
| ReorderChannelList(CalculatedChannel[], out Error) | Rearranges the order in which NI VeriStand reads values from each calculated channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-callprocedure-callprocedure__string-string-basenode.html language=enus -->
## TOPIC 01921: CallProcedure(string, string, BaseNode)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-callprocedure-callprocedure__string-string-basenode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-callprocedure-callprocedure__string-string-basenode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of CallProcedure with the specified name, description, and procedure. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CallProcedure(string Name, string Description, BaseNode Procedure)ParametersNameTypeDescriptionNamestringThe name of the CallProce

### CallProcedure(string, string, BaseNode)

Initializes a new instance of [CallProcedure](nationalinstruments-veristand-systemdefinitionapi-callprocedure.html) with the specified name, description, and procedure.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CallProcedure(string Name, string Description, BaseNode Procedure)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the CallProcedure step. |
| Description | string | The description of the CallProcedure step. |
| Procedure | BaseNode | The BaseNode reference to the procedure to call when this step executes. |

Parent topic:

CallProcedure Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-callprocedure-procedure.html language=enus -->
## TOPIC 01922: Procedure

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-callprocedure-procedure.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-callprocedure-procedure.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the procedure to call when this step executes. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode Procedure { get; set; }ReturnsA BaseNode reference to the procedure.

### Procedure

Gets or sets the procedure to call when this step executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) Procedure { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the procedure.

Parent topic:

CallProcedure Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-callprocedure.html language=enus -->
## TOPIC 01923: CallProcedure Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-callprocedure.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-callprocedure.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a Call Procedure step that you can add to a Procedure. The Call Procedure step calls a procedure when the step executes. Derives fromCommandSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CallProcedure : CommandRemarksUse the members of this class to get or

### CallProcedure Class

Represents a **Call Procedure** step that you can add to a [Procedure](nationalinstruments-veristand-systemdefinitionapi-procedure.html). The **Call Procedure** step calls a procedure when the step executes.

#### Derives from

- Command

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CallProcedure : Command

#### Remarks

Use the members of this class to get or set the procedure to call when the step executes.

**Accessing this Class**

- CallProcedure Constructor

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CallProcedure(string, string, BaseNode) | Initializes a new instance of CallProcedure with the specified name, description, and procedure. |

#### Properties

| Name | Description |
| --- | --- |
| Procedure | Gets or sets the procedure to call when this step executes. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-can-addcanport__canport-out.html language=enus -->
## TOPIC 01924: AddCANPort(CANPort, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-can-addcanport__canport-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-can-addcanport__canport-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified CANPort to the CAN section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCANPort(CANPort canPort, out Error error)RemarksFor example code and more information about this method, refer to one of the following help topics: LabVIEW Walkthrough: Mod

### AddCANPort(CANPort, out Error)

Adds the specified [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) to the [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCANPort(CANPort canPort, out Error error)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| canPort | CANPort | The CAN port to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

#### Returns

true if the port was added successfully.

Parent topic:

CAN Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-can-addcanport__canport.html language=enus -->
## TOPIC 01925: AddCANPort(CANPort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-can-addcanport__canport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-can-addcanport__canport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified CANPort to the CAN section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddCANPort(CANPort canPort)RemarksFor example code and more information about this method, refer to one of the following help topics: LabVIEW Walkthrough: Modifying a System D

### AddCANPort(CANPort)

Adds the specified [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) to the [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddCANPort(CANPort canPort)

#### Remarks

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| canPort | CANPort | The CAN port to add. |

#### Returns

true if the port was added successfully.

Parent topic:

CAN Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-can-getcanportlist.html language=enus -->
## TOPIC 01926: GetCANPortList()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-can-getcanportlist.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-can-getcanportlist.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array that contains the CANPort elements from the current CAN section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANPort[] GetCANPortList()RemarksModifications you make to the contents of this list apply to the system definition. However, modifications you make

### GetCANPortList()

Gets an array that contains the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) elements from the current [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html)[] GetCANPortList()

#### Remarks

Note

Modifications you make to the contents of this list apply to the system definition. However, modifications you make to the array container, such as by calling Array.SetValue() or Array.Clear(), have no effect on the system definition.

For example code and more information about this method, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Returns

An array that contains the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) elements from the current [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) section.

Parent topic:

CAN Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-can.html language=enus -->
## TOPIC 01927: CAN Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-can.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-can.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the CAN section under XNET in the system definition. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CAN : SectionRemarksUse the members of this class to add a CANPort or get a list of existing CAN ports. Accessing this ClassM:NationalInst

### CAN Class

Represents the **CAN** section under [XNET](nationalinstruments-veristand-systemdefinitionapi-xnet.html) in the system definition.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CAN : Section

#### Remarks

Use the members of this class to add a [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) or get a list of existing CAN ports.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.XNET.GetCAN

For example code and more information about this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddCANPort(CANPort, out Error) | Adds the specified CANPort to the CAN section. |
| AddCANPort(CANPort) | Adds the specified CANPort to the CAN section. |
| GetCANPortList() | Gets an array that contains the CANPort elements from the current CAN section. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-addsleepmodechannel__sleepmode-out.html language=enus -->
## TOPIC 01928: AddSleepModeChannel(SleepMode, out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-addsleepmodechannel__sleepmode-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-addsleepmodechannel__sleepmode-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds the specified SleepMode to the CANInterfaceChannels section. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool AddSleepModeChannel(SleepMode sleepMode, out Error error)ParametersNameTypeDescriptionsleepModeSleepModeThe SleepMode to add.errorout ErrorReturns an Nation

### AddSleepModeChannel(SleepMode, out Error)

Adds the specified [SleepMode](nationalinstruments-veristand-systemdefinitionapi-sleepmode.html) to the [CANInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html) section.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool AddSleepModeChannel(SleepMode sleepMode, out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| sleepMode | SleepMode | The SleepMode to add. |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createcommunicationstatechannel__out.html language=enus -->
## TOPIC 01929: CreateCommunicationStateChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createcommunicationstatechannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createcommunicationstatechannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Communication State status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateCommunicationStateChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand

### CreateCommunicationStateChannel(out Error)

Creates the Communication State status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateCommunicationStateChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createfaultchannel__out.html language=enus -->
## TOPIC 01930: CreateFaultChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createfaultchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createfaultchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Fault status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateFaultChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If no error

### CreateFaultChannel(out Error)

Creates the Fault status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateFaultChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createlasterrorchannel__out.html language=enus -->
## TOPIC 01931: CreateLastErrorChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createlasterrorchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createlasterrorchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Last Error status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateLastErrorChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If

### CreateLastErrorChannel(out Error)

Creates the Last Error status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateLastErrorChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createlasterrortimestampchannel__out.html language=enus -->
## TOPIC 01932: CreateLastErrorTimestampChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createlasterrortimestampchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createlasterrortimestampchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Last Error Timestamp status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateLastErrorTimestampChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStan

### CreateLastErrorTimestampChannel(out Error)

Creates the Last Error Timestamp status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateLastErrorTimestampChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createreceiveerrorcounterchannel__out.html language=enus -->
## TOPIC 01933: CreateReceiveErrorCounterChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createreceiveerrorcounterchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createreceiveerrorcounterchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Receive Error Counter status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateReceiveErrorCounterChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriSt

### CreateReceiveErrorCounterChannel(out Error)

Creates the Receive Error Counter status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateReceiveErrorCounterChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createtransceivererrorchannel__out.html language=enus -->
## TOPIC 01934: CreateTransceiverErrorChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createtransceivererrorchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createtransceivererrorchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Transceiver Error status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateTransceiverErrorChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Err

### CreateTransceiverErrorChannel(out Error)

Creates the Transceiver Error status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateTransceiverErrorChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createtransmiterrorcounterchannel__out.html language=enus -->
## TOPIC 01935: CreateTransmitErrorCounterChannel(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createtransmiterrorcounterchannel__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-createtransmiterrorcounterchannel__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the Transmit Error Counter status channel for the interface, if it does not exist. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel CreateTransmitErrorCounterChannel(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.Veri

### CreateTransmitErrorCounterChannel(out Error)

Creates the Transmit Error Counter status channel for the interface, if it does not exist.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) CreateTransmitErrorCounterChannel(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getcommunicationstatechannel.html language=enus -->
## TOPIC 01936: GetCommunicationStateChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getcommunicationstatechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getcommunicationstatechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Communication State status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetCommunicationStateChannel()

### GetCommunicationStateChannel()

Gets the Communication State status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetCommunicationStateChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getfaultchannel.html language=enus -->
## TOPIC 01937: GetFaultChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getfaultchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getfaultchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Fault status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetFaultChannel()

### GetFaultChannel()

Gets the Fault status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetFaultChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getlasterrorchannel.html language=enus -->
## TOPIC 01938: GetLastErrorChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getlasterrorchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getlasterrorchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Last Error status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetLastErrorChannel()

### GetLastErrorChannel()

Gets the Last Error status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetLastErrorChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getlasterrortimestampchannel.html language=enus -->
## TOPIC 01939: GetLastErrorTimestampChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getlasterrortimestampchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getlasterrortimestampchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Last Error Timestamp status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetLastErrorTimestampChannel()

### GetLastErrorTimestampChannel()

Gets the Last Error Timestamp status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetLastErrorTimestampChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getreceiveerrorcounterchannel.html language=enus -->
## TOPIC 01940: GetReceiveErrorCounterChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getreceiveerrorcounterchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getreceiveerrorcounterchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Receive Error Counter status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetReceiveErrorCounterChannel()

### GetReceiveErrorCounterChannel()

Gets the Receive Error Counter status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetReceiveErrorCounterChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getsleepmodechannel.html language=enus -->
## TOPIC 01941: GetSleepModeChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getsleepmodechannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-getsleepmodechannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Transceiver State, or Sleep Mode, channel under an NI-XNET CAN port. The Sleep Mode channel controls the sleep mode option on an NI-XNET CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame. SyntaxNamespace: National

### GetSleepModeChannel()

Gets the **Transceiver State**, or Sleep Mode, channel under an NI-XNET CAN port. The Sleep Mode channel controls the sleep mode option on an NI-XNET CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [SleepMode](nationalinstruments-veristand-systemdefinitionapi-sleepmode.html) GetSleepModeChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-gettransceivererrorchannel.html language=enus -->
## TOPIC 01942: GetTransceiverErrorChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-gettransceivererrorchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-gettransceivererrorchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Transceiver Error status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetTransceiverErrorChannel()

### GetTransceiverErrorChannel()

Gets the Transceiver Error status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetTransceiverErrorChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-gettransmiterrorcounterchannel.html language=enus -->
## TOPIC 01943: GetTransmitErrorCounterChannel()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-gettransmiterrorcounterchannel.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels-gettransmiterrorcounterchannel.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Transmit Error Counter status channel for the interface. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel GetTransmitErrorCounterChannel()

### GetTransmitErrorCounterChannel()

Gets the Transmit Error Counter status channel for the interface.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) GetTransmitErrorCounterChannel()

Parent topic:

CANInterfaceChannels Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html language=enus -->
## TOPIC 01944: CANInterfaceChannels Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents the Interface section under an NI-XNET CAN port. This section contains the port-specific channel that controls the port's sleep mode and channels which provide status information. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CANInterfac

### CANInterfaceChannels Class

Represents the **Interface** section under an NI-XNET CAN port. This section contains the port-specific channel that controls the port's sleep mode and channels which provide status information.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CANInterfaceChannels : Section

#### Remarks

Use the members of this class to configure the **Interface** section and to access the [SleepMode](nationalinstruments-veristand-systemdefinitionapi-sleepmode.html) channel.

You cannot directly call this class. Use the SleepMode Constructor

constructor to access the sleep mode channel.

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Methods

| Name | Description |
| --- | --- |
| AddSleepModeChannel(SleepMode, out Error) | Adds the specified SleepMode to the CANInterfaceChannels section. |
| CreateCommunicationStateChannel(out Error) | Creates the Communication State status channel for the interface, if it does not exist. |
| CreateFaultChannel(out Error) | Creates the Fault status channel for the interface, if it does not exist. |
| CreateLastErrorChannel(out Error) | Creates the Last Error status channel for the interface, if it does not exist. |
| CreateLastErrorTimestampChannel(out Error) | Creates the Last Error Timestamp status channel for the interface, if it does not exist. |
| CreateReceiveErrorCounterChannel(out Error) | Creates the Receive Error Counter status channel for the interface, if it does not exist. |
| CreateTransceiverErrorChannel(out Error) | Creates the Transceiver Error status channel for the interface, if it does not exist. |
| CreateTransmitErrorCounterChannel(out Error) | Creates the Transmit Error Counter status channel for the interface, if it does not exist. |
| GetCommunicationStateChannel() | Gets the Communication State status channel for the interface. |
| GetFaultChannel() | Gets the Fault status channel for the interface. |
| GetLastErrorChannel() | Gets the Last Error status channel for the interface. |
| GetLastErrorTimestampChannel() | Gets the Last Error Timestamp status channel for the interface. |
| GetReceiveErrorCounterChannel() | Gets the Receive Error Counter status channel for the interface. |
| GetSleepModeChannel() | Gets the Transceiver State, or Sleep Mode, channel under an NI-XNET CAN port. The Sleep Mode channel controls the sleep mode option on an NI-XNET CAN port. A port in sleep mode does not transmit data until you release sleep mode or until the port receives an incoming frame. |
| GetTransceiverErrorChannel() | Gets the Transceiver Error status channel for the interface. |
| GetTransmitErrorCounterChannel() | Gets the Transmit Error Counter status channel for the interface. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-caniomode.html language=enus -->
## TOPIC 01945: CANIOMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-caniomode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-caniomode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: I/O Mode used by the interface when transmitting a CAN frame. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum CANIOModeMembersNameValueDescriptionStandard0Default CAN 2.0 A/B standard I/O mode with 8-byte payload. FD1CAN FD mode supporting payloads up to 64 bytes. FDBRS

### CANIOMode Enumeration

I/O Mode used by the interface when transmitting a CAN frame.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CANIOMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Standard | 0 | Default CAN 2.0 A/B standard I/O mode with 8-byte payload. |
| FD | 1 | CAN FD mode supporting payloads up to 64 bytes. |
| FDBRS | 2 | CAN FD mode with optional Baud Rate Switching for increased data transfer rates. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-afpbinaryfile.html language=enus -->
## TOPIC 01946: AFPBinaryFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-afpbinaryfile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-afpbinaryfile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the binary (.ini) file used for automatic frame processing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic DependentFile AFPBinaryFile { get; set; }RemarksYou can use the BinaryFilePath parameter of SetAutomaticFrameProcessing to set this file. ReturnsA DependentFile r

### AFPBinaryFile

Gets the binary (.ini) file used for automatic frame processing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) AFPBinaryFile { get; set; }

#### Remarks

You can use the *BinaryFilePath* parameter of [SetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-canport-setautomaticframeprocessing__string-string-uint_arr1.html) to set this file.

#### Returns

A [DependentFile](nationalinstruments-veristand-systemdefinitionapi-dependentfile.html) reference to the .ini file.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-afpglobaldata.html language=enus -->
## TOPIC 01947: AFPGlobalData

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-afpglobaldata.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-afpglobaldata.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the global data used for automatic frame processing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint[] AFPGlobalData { get; set; }ReturnsThe array specified by the GlobalData parameter of SetAutomaticFrameProcessing.

### AFPGlobalData

Gets the global data used for automatic frame processing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint[] AFPGlobalData { get; set; }

#### Returns

The array specified by the *GlobalData* parameter of [SetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-canport-setautomaticframeprocessing__string-string-uint_arr1.html).

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-afpinifile.html language=enus -->
## TOPIC 01948: AFPINIFile

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-afpinifile.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-afpinifile.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the name of the AFPBinaryFile used for automatic frame processing. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string AFPINIFile { get; set; }ReturnsThe filename specified by the IniFileName parameter of SetAutomaticFrameProcessing.

### AFPINIFile

Gets the name of the [AFPBinaryFile](nationalinstruments-veristand-systemdefinitionapi-canport-afpbinaryfile.html) used for automatic frame processing.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string AFPINIFile { get; set; }

#### Returns

The filename specified by the *IniFileName* parameter of [SetAutomaticFrameProcessing](nationalinstruments-veristand-systemdefinitionapi-canport-setautomaticframeprocessing__string-string-uint_arr1.html).

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-baudrate.html language=enus -->
## TOPIC 01949: BaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-baudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-baudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the baud rate of the CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint BaudRate { get; set; }RemarksThis rate can be 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or 1000000. Some transceiv

### BaudRate

Gets or sets the baud rate of the CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint BaudRate { get; set; }

#### Remarks

This rate can be 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or 1000000. Some transceivers may support only a subset of these values.

#### Returns

The baud rate. You can use the *BaudRate* parameter of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) constructor to specify an initial value.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-baudratebitfield.html language=enus -->
## TOPIC 01950: BaudRateBitfield

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-baudratebitfield.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-baudratebitfield.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the baud rate bitfield of the CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ulong BaudRateBitfield { get; set; }

### BaudRateBitfield

Gets or sets the baud rate bitfield of the CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong BaudRateBitfield { get; set; }

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-canbusoff.html language=enus -->
## TOPIC 01951: CANBusOff

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-canbusoff.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-canbusoff.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool CANBusOff { get; set; }Returnstrue if the bus is recovered from off mode if it switches due to a physical fault. Otherwis

### CANBusOff

Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool CANBusOff { get; set; }

#### Returns

true if the bus is recovered from off mode if it switches due to a physical fault. Otherwise false.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-canbusoffrate.html language=enus -->
## TOPIC 01952: CANBusOffRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-canbusoffrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-canbusoffrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the bit rate at which to check the state of the CAN bus (active or off). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint CANBusOffRate { get; set; }ReturnsThe bit rate at which the CAN bus state is checked.

### CANBusOffRate

Gets or sets the bit rate at which to check the state of the CAN bus (active or off).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint CANBusOffRate { get; set; }

#### Returns

The bit rate at which the CAN bus state is checked.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-canport__string-ushort-database-string-uint-uint.html language=enus -->
## TOPIC 01953: CANPort(string, ushort, Database, string, uint, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-canport__string-ushort-database-string-uint-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-canport__string-ushort-database-string-uint-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CANPort class and creates a port with the specified Name , PortNumber , LinkedDatabase , ClusterName , and BaudRate . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANPort(string Name, ushort PortNumber, Database LinkedDatabase, string Clu

### CANPort(string, ushort, Database, string, uint, uint)

Initializes a new instance of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) class and creates a port with the specified *Name* , *PortNumber* , *LinkedDatabase* , *ClusterName* , and *BaudRate* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CANPort(string Name, ushort PortNumber, Database LinkedDatabase, string ClusterName, uint BaudRate, uint FDBaudRate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the port. |
| PortNumber | ushort | The physical address of the port. |
| LinkedDatabase | Database | The XNET database associated with the port. |
| ClusterName | string | The cluster in LinkedDatabase that is associated with the port. |
| BaudRate | uint | The baud rate all cluster nodes under the port use. This rate can be 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or 1000000. Some transceivers may support only a subset of these values. |
| FDBaudRate | uint | The FD baud rate all cluster nodes under the port use. |

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-canport__string-ushort-database-string-uint.html language=enus -->
## TOPIC 01954: CANPort(string, ushort, Database, string, uint)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-canport__string-ushort-database-string-uint.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-canport__string-ushort-database-string-uint.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of the CANPort class and creates a port with the specified Name , PortNumber , LinkedDatabase , ClusterName , and BaudRate . SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANPort(string Name, ushort PortNumber, Database LinkedDatabase, string Clu

### CANPort(string, ushort, Database, string, uint)

Initializes a new instance of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) class and creates a port with the specified *Name* , *PortNumber* , *LinkedDatabase* , *ClusterName* , and *BaudRate* .

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public CANPort(string Name, ushort PortNumber, Database LinkedDatabase, string ClusterName, uint BaudRate)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| Name | string | The name of the port. |
| PortNumber | ushort | The physical address of the port. |
| LinkedDatabase | Database | The XNET database associated with the port. |
| ClusterName | string | The cluster in LinkedDatabase that is associated with the port. |
| BaudRate | uint | The baud rate all cluster nodes under the port use. This rate can be 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or 1000000. Some transceivers may support only a subset of these values. |

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-clustername.html language=enus -->
## TOPIC 01955: ClusterName

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-clustername.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-clustername.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the name of the cluster in LinkedDatabase that is associated with the CANPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic string ClusterName { get; set; }ReturnsThe cluster name. You can use the ClusterName parameter of the CANPort constructor to specify an

### ClusterName

Gets or sets the name of the cluster in [LinkedDatabase](nationalinstruments-veristand-systemdefinitionapi-canport-linkeddatabase.html) that is associated with the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public string ClusterName { get; set; }

#### Returns

The cluster name. You can use the *ClusterName* parameter of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) constructor to specify an initial value.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-createinterfacesection__out.html language=enus -->
## TOPIC 01956: CreateInterfaceSection(out Error)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-createinterfacesection__out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-createinterfacesection__out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the CANInterfaceChannels section of the current CANPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANInterfaceChannels CreateInterfaceSection(out Error error)ParametersNameTypeDescriptionerrorout ErrorReturns an NationalInstruments.VeriStand.Error object. If n

### CreateInterfaceSection(out Error)

Creates the [CANInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html) section of the current [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CANInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html) CreateInterfaceSection(out Error error)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| error | out Error | Returns an NationalInstruments.VeriStand.Error object. If no error occurs, the Code property of the Error object is 0. |

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-disabled.html language=enus -->
## TOPIC 01957: Disabled

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-disabled.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-disabled.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether the port is disabled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Disabled { get; set; }

### Disabled

Gets or sets whether the port is disabled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Disabled { get; set; }

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-echo.html language=enus -->
## TOPIC 01958: Echo

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-echo.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-echo.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool Echo { get; set

### Echo

Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool Echo { get; set; }

#### Returns

true if outgoing frames are echoed back as incoming frames. Otherwise false.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-fdbaudrate.html language=enus -->
## TOPIC 01959: FDBaudRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-fdbaudrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-fdbaudrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the FD baud rate of the CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint FDBaudRate { get; set; }RemarksThis rate can be 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or 1000000. Some tran

### FDBaudRate

Gets or sets the FD baud rate of the CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint FDBaudRate { get; set; }

#### Remarks

This rate can be 33333, 40000, 50000, 62500, 80000, 83333, 100000, 125000, 160000, 200000, 250000, 400000, 500000, 800000, or 1000000. Some transceivers may support only a subset of these values.

#### Returns

The FD baud rate. You can use the *BaudRate* parameter of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) constructor to specify an initial value.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-fdbaudratebitfield.html language=enus -->
## TOPIC 01960: FDBaudRateBitfield

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-fdbaudratebitfield.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-fdbaudratebitfield.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the FD baud rate bitfield of the CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ulong FDBaudRateBitfield { get; set; }

### FDBaudRateBitfield

Gets or sets the FD baud rate bitfield of the CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ulong FDBaudRateBitfield { get; set; }

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-fdisomode.html language=enus -->
## TOPIC 01961: FDISOMode

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-fdisomode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-fdisomode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the FD ISO mode of the CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic FDISOMode FDISOMode { get; set; }

### FDISOMode

Gets or sets the FD ISO mode of the CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [FDISOMode](nationalinstruments-veristand-systemdefinitionapi-fdisomode.html) FDISOMode { get; set; }

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-getincoming.html language=enus -->
## TOPIC 01962: GetIncoming()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-getincoming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-getincoming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the Incoming section of the current CANPort, which includes incoming single-point frames and raw frame data logging files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Incoming GetIncoming()ReturnsAn Incoming object.

### GetIncoming()

Gets the [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) section of the current [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html), which includes incoming single-point frames and raw frame data logging files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) GetIncoming()

#### Returns

An [Incoming](nationalinstruments-veristand-systemdefinitionapi-incoming.html) object.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-getinterfacesection.html language=enus -->
## TOPIC 01963: GetInterfaceSection()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-getinterfacesection.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-getinterfacesection.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the CANInterfaceChannels section of the current CANPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANInterfaceChannels GetInterfaceSection()

### GetInterfaceSection()

Gets the [CANInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html) section of the current [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CANInterfaceChannels](nationalinstruments-veristand-systemdefinitionapi-caninterfacechannels.html) GetInterfaceSection()

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-getoutgoing.html language=enus -->
## TOPIC 01964: GetOutgoing()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-getoutgoing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-getoutgoing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Accesses the Outgoing section of the current CANPort, which includes outgoing event-triggered and cyclic frames and data replay files. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Outgoing GetOutgoing()ReturnsAn Outgoing object.

### GetOutgoing()

Accesses the [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) section of the current [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html), which includes outgoing event-triggered and cyclic frames and data replay files.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) GetOutgoing()

#### Returns

An [Outgoing](nationalinstruments-veristand-systemdefinitionapi-outgoing.html) object.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-incomingrate.html language=enus -->
## TOPIC 01965: IncomingRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-incomingrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-incomingrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processing rate for incoming frames in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint IncomingRate { get; set; }RemarksIf InlineIncoming is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the incoming frame sess

### IncomingRate

Gets or sets the processing rate for incoming frames in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint IncomingRate { get; set; }

#### Remarks

If [InlineIncoming](nationalinstruments-veristand-systemdefinitionapi-canport-inlineincoming.html) is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the incoming frame session loop. For example, if the PCL execution rate is 1000 Hz, setting this rate to 100 Hz calls the frame session loop on every 10th iteration of the PCL.

#### Returns

The processing rate in hertz.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-inlineincoming.html language=enus -->
## TOPIC 01966: InlineIncoming

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-inlineincoming.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-inlineincoming.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### InlineIncoming

Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InlineIncoming { get; set; }

#### Remarks

By default, NI VeriStand runs incoming and outgoing frame sessions as asynchronous custom devices that execute in separate loops from the PCL. Therefore, there is a one-cycle delay when reading and writing channel values between the frame session loops and the rest of the system. You can inline frames to eliminate this delay by running the session loops as inline hardware interface custom devices, where NI VeriStand uses the loop rate to calculate the decimation factor for calls to the session loop.

Inlining frames is useful if you need to reduce latency when getting XNET data from your system, or if you want to correlate frame data with channel data. However, inlining frames can increase CPU usage, and if the XNET loops take too long to execute, delay the execution of the PCL.

#### Returns

true if incoming frames are processed inline with the PCL. false if they are processed asynchronously.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-inlineoutgoing.html language=enus -->
## TOPIC 01967: InlineOutgoing

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-inlineoutgoing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-inlineoutgoing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic

### InlineOutgoing

Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool InlineOutgoing { get; set; }

#### Remarks

By default, NI VeriStand runs incoming and outgoing frame sessions as asynchronous custom devices that execute in separate loops from the PCL. Therefore, there is a 1-cycle delay when reading and writing channel values between the frame session loops and the rest of the system. You can inline frames to eliminate this delay by running the session loops as inline hardware interface custom devices, where NI VeriStand uses the loop rate to calculate the decimation factor for calls to the session loop.

Inlining frames is useful if you need to reduce latency when getting XNET data from your system, or if you want to correlate frame data with channel data. However, inlining frames can increase CPU usage, and if the XNET loops take too long to execute, delay the execution of the PCL.

#### Returns

true if outgoing frames are processed inline with the PCL. false if they are processed asynchronously.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-inputstreamqueuesize.html language=enus -->
## TOPIC 01968: InputStreamQueueSize

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-inputstreamqueuesize.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-inputstreamqueuesize.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint InputStreamQueueSize { get; s

### InputStreamQueueSize

Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint InputStreamQueueSize { get; set; }

#### Returns

An integer representing the queue size.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-inputstreamreadtime.html language=enus -->
## TOPIC 01969: InputStreamReadTime

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-inputstreamreadtime.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-inputstreamreadtime.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double InputStrea

### InputStreamReadTime

Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double InputStreamReadTime { get; set; }

#### Returns

A double representing the read time in seconds.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-linkeddatabase.html language=enus -->
## TOPIC 01970: LinkedDatabase

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-linkeddatabase.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-linkeddatabase.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the XNET database associated with the CANPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode LinkedDatabase { get; set; }ReturnsA BaseNode reference to the database. You can use the LinkedDatabase parameter of the CANPort constructor to specify an ini

### LinkedDatabase

Gets or sets the XNET database associated with the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) LinkedDatabase { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the database. You can use the *LinkedDatabase* parameter of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) constructor to specify an initial value.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-outgoingrate.html language=enus -->
## TOPIC 01971: OutgoingRate

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-outgoingrate.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-outgoingrate.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the processing rate for outgoing frames in hertz. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint OutgoingRate { get; set; }RemarksIf InlineOutgoing is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the outgoing frame sess

### OutgoingRate

Gets or sets the processing rate for outgoing frames in hertz.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint OutgoingRate { get; set; }

#### Remarks

If [InlineOutgoing](nationalinstruments-veristand-systemdefinitionapi-canport-inlineoutgoing.html) is true, NI VeriStand uses this rate to calculate the decimation factor for calls to the outgoing frame session loop. For example, if the PCL execution rate is 1000 Hz, setting this rate to 100 Hz calls the frame session loop on every 10th iteration of the PCL.

#### Returns

An integer representing the processing rate in hertz.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-portnumber.html language=enus -->
## TOPIC 01972: PortNumber

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-portnumber.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-portnumber.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the physical address of the CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic ushort PortNumber { get; set; }ReturnsThe port number. You can use the PortNumber parameter of the CANPort constructor to specify an initial value.

### PortNumber

Gets or sets the physical address of the CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public ushort PortNumber { get; set; }

#### Returns

The port number. You can use the *PortNumber* parameter of the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html) constructor to specify an initial value.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-remove986xsupport.html language=enus -->
## TOPIC 01973: Remove986xSupport()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-remove986xsupport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-remove986xsupport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes support for NI CompactRIO 986x CAN modules. You can use Set986xSupport to configure support. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void Remove986xSupport()

### Remove986xSupport()

Removes support for NI CompactRIO 986*x* CAN modules. You can use [Set986xSupport](nationalinstruments-veristand-systemdefinitionapi-canport-set986xsupport__dependentfile-ushort.html) to configure support.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void Remove986xSupport()

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-removeautomaticframeprocessing.html language=enus -->
## TOPIC 01974: RemoveAutomaticFrameProcessing()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-removeautomaticframeprocessing.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-removeautomaticframeprocessing.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes automatic frame processing from the CANPort. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveAutomaticFrameProcessing()

### RemoveAutomaticFrameProcessing()

Removes automatic frame processing from the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveAutomaticFrameProcessing()

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-set986xsupport__dependentfile-ushort.html language=enus -->
## TOPIC 01975: Set986xSupport(DependentFile, ushort)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-set986xsupport__dependentfile-ushort.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-set986xsupport__dependentfile-ushort.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures support for NI CompactRIO 986x CAN modules. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void Set986xSupport(DependentFile file, ushort rioPortNumber)RemarksIf the bitfile contains configuration information for anything other than CompactRIO 986x devices, you a

### Set986xSupport(DependentFile, ushort)

Configures support for NI CompactRIO 986*x* CAN modules.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void Set986xSupport(DependentFile file, ushort rioPortNumber)

#### Remarks

Note

If the bitfile contains configuration information for anything other than CompactRIO 986*x* devices, you also must add the bitfile as a configuration file under [FPGA](nationalinstruments-veristand-systemdefinitionapi-fpga.html).

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| file | DependentFile | The reference to the bitfile for the 986x devices. |
| rioPortNumber | ushort | The port to download file to. |

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-setautomaticframeprocessing__string-string-uint_arr1.html language=enus -->
## TOPIC 01976: SetAutomaticFrameProcessing(string, string, uint[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-setautomaticframeprocessing__string-string-uint_arr1.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-setautomaticframeprocessing__string-string-uint_arr1.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets automatic frame processing on the CANPort. You must set automatic frame processing on the port if you want to configure CRCs and counters on outgoing frames under the port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void SetAutomaticFrameProcessing(string IniFileNa

### SetAutomaticFrameProcessing(string, string, uint[])

Sets automatic frame processing on the [CANPort](nationalinstruments-veristand-systemdefinitionapi-canport.html). You must set automatic frame processing on the port if you want to configure CRCs and counters on outgoing frames under the port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void SetAutomaticFrameProcessing(string IniFileName, string BinaryFilePath, uint[] GlobalData)

#### Remarks

NI VeriStand supports CRC-8 and CRC-16 length polynomials.

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| IniFileName | string | The name of the binary file to use for automatic frame processing. |
| BinaryFilePath | string | The path to the binary file to use for automatic frame processing. The CRC files installed with NI VeriStand are available in the < Application Data > \\National Instruments\\VeriStand\\System Explorer\\XNET\\AFP directory. |
| GlobalData | uint[] | An array that contains the following data:GlobalData[0] = Polynomial, or the generator polynomial for the CRC. This decimal value is converted to binary form to create the polynomial. For example, if you enter the decimal value 23, the value becomes 10111 in binary form, which translates to the following polynomial: 1x^4 + 0x^3 + 1x^2 + 1x + 1 GlobalData[1] = Initial CRC, or the initial value to use for the CRC calculation. This decimal value is converted to binary form. The value can be up to 8 bits long for CRC-8 and up to 16 bits long for CRC-16. GlobalData[2] = Final XOR, or the value to XOR with the calculated CRC. This decimal value is converted to binary form. The value can be up to 8 bits long for CRC-8 and up to 16 bits long for CRC-16. GlobalData[3] = Reflected, if a non-zero number, specifies to reverse the order of the bits in the CRC before writing the data in to the data stream. |

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-termination.html language=enus -->
## TOPIC 01977: Termination

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-termination.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-termination.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the onboard XNETTermination. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic XNETTermination Termination { get; set; }RemarksDifferent CAN hardware have different termination requirements, and the behavior of this component depends on the TransceiverType: HS — H

### Termination

Gets or sets the onboard [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) Termination { get; set; }

#### Remarks

TransceiverType

- [HS](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html) — High-Speed CAN networks are typically terminated on the bus itself, instead of within an individual CAN node. However, NI-XNET allows you to configure termination within the node to simplify testing. If your bus already has the correct amount of termination, set Termination to [Off](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html). ValueDescription[Off](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html)Termination is disabled.[On](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html)Termination is enabled (120 Ω ).
- [LS](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html) — Every node on a Low-Speed CAN network requires termination for each CAN data line. This configuration allows the Low-Speed/Fault-Tolerant CAN port to provide fault detection and recovery. In general, if the existing network has an overall network termination of 125 Ω or less, set Termination to [On](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) to enable the 4.99 k Ω option. Otherwise, select [Off](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html) for the 1.11 k Ω option. ValueDescription[Off](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html)Termination is set to 1.11k Ω .[On](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html)Termination is set to 4.99k Ω .
- [SW](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html) — The ISO standard requires Single-Wire transceivers to have a 9.09 k Ω resistor. No additional configuration is supported.

#### Returns

An enumeration value of [XNETTermination](nationalinstruments-veristand-systemdefinitionapi-xnettermination.html), indicating whether termination is On or Off.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-transceivertype.html language=enus -->
## TOPIC 01978: TransceiverType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-transceivertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-transceivertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CANTransceiverType for the port. Transceivers can be high-speed (HS), low-speed (LS), or single wire (SW). SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANTransceiverType TransceiverType { get; set; }ReturnsThe transceiver type. The default value depends

### TransceiverType

Gets or sets the [CANTransceiverType](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html) for the port. Transceivers can be high-speed (HS), low-speed (LS), or single wire (SW).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CANTransceiverType](nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html) TransceiverType { get; set; }

#### Returns

The transceiver type. The default value depends on the physical transceivers present on the CAN device.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport-transmitordertype.html language=enus -->
## TOPIC 01979: TransmitOrderType

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport-transmitordertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport-transmitordertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the CANTransmitOrderType for the port. You can transmit frames to the CAN bus AsSubmitted or ByIdentifier. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic CANTransmitOrderType TransmitOrderType { get; set; }ReturnsThe default is AsSubmitted.

### TransmitOrderType

Gets or sets the [CANTransmitOrderType](nationalinstruments-veristand-systemdefinitionapi-cantransmitordertype.html) for the port. You can transmit frames to the CAN bus AsSubmitted or ByIdentifier.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [CANTransmitOrderType](nationalinstruments-veristand-systemdefinitionapi-cantransmitordertype.html) TransmitOrderType { get; set; }

#### Returns

The default is AsSubmitted.

Parent topic:

CANPort Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-canport.html language=enus -->
## TOPIC 01980: CANPort Class

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-canport.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-canport.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Represents a port under the NI-XNET CAN section. Derives fromSectionSyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic class CANPort : SectionRemarksUse the members of this class to configure port settings, such as the port name, physical address, processing rate for incoming a

### CANPort Class

Represents a port under the NI-XNET [CAN](nationalinstruments-veristand-systemdefinitionapi-can.html) section.

#### Derives from

- Section

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public class CANPort : Section

#### Remarks

Use the members of this class to configure port settings, such as the port name, physical address, processing rate for incoming and outgoing frames.

**Accessing this Class**

- M:NationalInstruments.VeriStand.SystemDefinitionAPI.CAN.GetCANPortList
- CANPort Constructor

For example code and more information about this class, refer to one of the following help topics:

LabVIEW Walkthrough: Modifying a System Definition File

C# Walkthrough: Modifying a System Definition File

#### Thread Safety

Any members of this type are not guaranteed to be thread safe.

#### Constructors

| Name | Description |
| --- | --- |
| CANPort(string, ushort, Database, string, uint, uint) | Initializes a new instance of the CANPort class and creates a port with the specified Name , PortNumber , LinkedDatabase , ClusterName , and BaudRate . |
| CANPort(string, ushort, Database, string, uint) | Initializes a new instance of the CANPort class and creates a port with the specified Name , PortNumber , LinkedDatabase , ClusterName , and BaudRate . |

#### Properties

| Name | Description |
| --- | --- |
| AFPBinaryFile | Gets the binary (.ini) file used for automatic frame processing. |
| AFPGlobalData | Gets the global data used for automatic frame processing. |
| AFPINIFile | Gets the name of the AFPBinaryFile used for automatic frame processing. |
| BaudRate | Gets or sets the baud rate of the CAN port. |
| BaudRateBitfield | Gets or sets the baud rate bitfield of the CAN port. |
| CANBusOff | Gets or sets whether the CAN bus is recovered if it switches off due to a physical fault on the bus. |
| CANBusOffRate | Gets or sets the bit rate at which to check the state of the CAN bus (active or off). |
| ClusterName | Gets or sets the name of the cluster in LinkedDatabase that is associated with the CANPort. |
| Disabled | Gets or sets whether the port is disabled. |
| Echo | Gets or sets whether sessions contain frames that the interface transmits. If true, when frame transmission is complete for an output (outgoing) session, the frame is echoed to the input (incoming) session. |
| FDBaudRate | Gets or sets the FD baud rate of the CAN port. |
| FDBaudRateBitfield | Gets or sets the FD baud rate bitfield of the CAN port. |
| FDISOMode | Gets or sets the FD ISO mode of the CAN port. |
| IncomingRate | Gets or sets the processing rate for incoming frames in hertz. |
| InlineIncoming | Gets or sets whether to process incoming frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. |
| InlineOutgoing | Gets or sets whether to process outgoing frames inline with the VeriStand Engine's Primary Control Loop (PCL). By default, NI VeriStand runs incoming and outgoing frame sessions asynchronously, or in a parallel loop to the PCL. |
| InputStreamQueueSize | Gets or sets the queue size for the input stream. For signal I/O sessions, this is the number of signal values stored. For frame I/O sessions, this is the number of bytes of frame data stored. |
| InputStreamReadTime | Gets or sets the read time for the input stream. For signal I/O sessions, this is the timeout for the raw frame read. After this amount of time has elapsed, any frames available from the hardware will be read. |
| LinkedDatabase | Gets or sets the XNET database associated with the CANPort. |
| OutgoingRate | Gets or sets the processing rate for outgoing frames in hertz. |
| PortNumber | Gets or sets the physical address of the CAN port. |
| Termination | Gets or sets the onboard XNETTermination. |
| TransceiverType | Gets or sets the CANTransceiverType for the port. Transceivers can be high-speed (HS), low-speed (LS), or single wire (SW). |
| TransmitOrderType | Gets or sets the CANTransmitOrderType for the port. You can transmit frames to the CAN bus AsSubmitted or ByIdentifier. |

#### Methods

| Name | Description |
| --- | --- |
| CreateInterfaceSection(out Error) | Creates the CANInterfaceChannels section of the current CANPort. |
| GetIncoming() | Gets the Incoming section of the current CANPort, which includes incoming single-point frames and raw frame data logging files. |
| GetInterfaceSection() | Gets the CANInterfaceChannels section of the current CANPort. |
| GetOutgoing() | Accesses the Outgoing section of the current CANPort, which includes outgoing event-triggered and cyclic frames and data replay files. |
| Remove986xSupport() | Removes support for NI CompactRIO 986x CAN modules. You can use Set986xSupport to configure support. |
| RemoveAutomaticFrameProcessing() | Removes automatic frame processing from the CANPort. |
| Set986xSupport(DependentFile, ushort) | Configures support for NI CompactRIO 986x CAN modules. |
| SetAutomaticFrameProcessing(string, string, uint[]) | Sets automatic frame processing on the CANPort. You must set automatic frame processing on the port if you want to configure CRCs and counters on outgoing frames under the port. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html language=enus -->
## TOPIC 01981: CANTransceiverType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cantransceivertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The transceiver type of an NI-XNET CAN port. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum CANTransceiverTypeMembersNameValueDescriptionHS0High-Speed. 40kbaud - 1 Mbaud. LS1Low-Speed/Fault-Tolerant. 40 - 125kbaud. SW2Single Wire. 33.333 - 83.333 kbaud.

### CANTransceiverType Enumeration

The transceiver type of an NI-XNET CAN port.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CANTransceiverType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| HS | 0 | High-Speed. 40kbaud - 1 Mbaud. |
| LS | 1 | Low-Speed/Fault-Tolerant. 40 - 125kbaud. |
| SW | 2 | Single Wire. 33.333 - 83.333 kbaud. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cantransmitordertype.html language=enus -->
## TOPIC 01982: CANTransmitOrderType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cantransmitordertype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cantransmitordertype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The order in which the CAN interface transmits frames from the internal queue. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum CANTransmitOrderTypeMembersNameValueDescriptionAsSubmitted0Transmits frames to the CAN bus in the order that they were submitted to the queue.

### CANTransmitOrderType Enumeration

The order in which the CAN interface transmits frames from the internal queue.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CANTransmitOrderType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| AsSubmitted | 0 | Transmits frames to the CAN bus in the order that they were submitted to the queue. |
| ByIdentifier | 1 | Transmits frames to the CAN bus according to their relative priorities. Frames with a higher priority identifier (lower CAN ID value) transmit first. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cdchannel_type.html language=enus -->
## TOPIC 01983: CDChannel_Type Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cdchannel_type.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cdchannel_type.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type (Input or Output) of a custom device channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum CDChannel_TypeMembersNameValueDescriptionInput0The channel is an input channel, and is writable. OutputThe channel is an output channel.

### CDChannel_Type Enumeration

Specifies the type (Input or Output) of a custom device channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CDChannel_Type

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Input | 0 | The channel is an input channel, and is writable. |
| Output |  | The channel is an output channel. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cddriverexecmode.html language=enus -->
## TOPIC 01984: CDDriverExecMode Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cddriverexecmode.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cddriverexecmode.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the execution mode, or device type, of a custom device. The execution mode defines how the device interacts with the VeriStand Engine. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum CDDriverExecModeMembersNameValueDescriptionAsynchronous0The device executes a

### CDDriverExecMode Enumeration

Specifies the execution mode, or device type, of a custom device. The execution mode defines how the device interacts with the VeriStand Engine.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CDDriverExecMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Asynchronous | 0 | The device executes asynchronously, or in a separate, parallel loop to the VeriStand Engine's Primary Control Loop. Asynchronous custom devices use RT FIFOs to exchange channel data with the rest of the NI VeriStand system. |
| InlineHWInterface |  | The device executes inline with the VeriStand Engine's Primary Control Loop (PCL) and can read and write data from and to a hardware device. Inline custom devices contain a Case structure and execute as state machines. In inline hardware interface devices, two of the cases (Read Data from HW and Write Data to HW) are called on each iteration of the PCL. |
| InlineModelInterface |  | The device executes inline with the VeriStand Engine's Primary Control Loop (PCL). Inline model interface devices can process data acquired from hardware inputs and send the processed values to hardware outputs with no latency. Inline custom devices contain a Case structure and execute as state machines. In inline model interface devices, one case (Execute Model) is called on each iteration of the PCL. |
| InlineTimingAndSync |  | The device executes as an inline hardware interface custom device that also can function as the hardware synchronization master device, which drives the RTSI 0 line. In NI VeriStand, the device appears as a Timing and Sync device. |
| AsynchronousTimingAndSync |  | The device executes as an asynchronous custom device that also can function as the hardware synchronization master device, which drives the RTSI 0 line. In NI VeriStand, the device appears as a Timing and Sync device. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cdlooptype.html language=enus -->
## TOPIC 01985: CDLoopType Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cdlooptype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cdlooptype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of loop in which an asynchronous custom device executes. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic enum CDLoopTypeMembersNameValueDescriptionWhileLoop0The device executes in a While Loop. TimedLoopThe device executes in a Timed Loop. With this loop t

### CDLoopType Enumeration

Specifies the type of loop in which an asynchronous custom device executes.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CDLoopType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| WhileLoop | 0 | The device executes in a While Loop. |
| TimedLoop |  | The device executes in a Timed Loop. With this loop type, you can use the UseDeviceClock property to synchronize the device with the Primary Control Loop's timing source. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-cdtimelooppriority.html language=enus -->
## TOPIC 01986: CDTimeLoopPriority Enumeration

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-cdtimelooppriority.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-cdtimelooppriority.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the priority of the Timed Loop that an asynchronous custom device with a CDLoopType of TimedLoop executes in. If you want to wire this value to the input terminal of a Timed Loop in LabVIEW, you must first convert it to a positive integer between 1 and 65,535. SyntaxNamespace: NationalInst

### CDTimeLoopPriority Enumeration

Specifies the priority of the Timed Loop that an asynchronous custom device with a [CDLoopType](nationalinstruments-veristand-systemdefinitionapi-cdlooptype.html) of [TimedLoop](nationalinstruments-veristand-systemdefinitionapi-cdlooptype.html) executes in. If you want to wire this value to the input terminal of a Timed Loop in LabVIEW, you must first convert it to a positive integer between 1 and 65,535.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public enum CDTimeLoopPriority

#### Members

| Name | Value | Description |
| --- | --- | --- |
| Low | 0 | The priority is low. |
| Medium |  | The priority is medium. |
| High |  | The priority is high. |

Parent topic:

NationalInstruments.VeriStand.SystemDefinitionAPI

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-bitfields.html language=enus -->
## TOPIC 01987: BitFields

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-bitfields.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-bitfields.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a bitfield mask that is set on the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic uint BitFields { get; }RemarksIntegerValue0K_FAULTABLE1K_READABLE2K_SCALABLE3K_WRITABLE ReturnsAn integer representing the field values:

### BitFields

Gets a bitfield mask that is set on the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public uint BitFields { get; }

#### Remarks

| Integer | Value |
| --- | --- |
| 0 | K_FAULTABLE |
| 1 | K_READABLE |
| 2 | K_SCALABLE |
| 3 | K_WRITABLE |

#### Returns

An integer representing the field values:

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-channel__basenodetype.html language=enus -->
## TOPIC 01988: Channel(BaseNodeType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-channel__basenodetype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-channel__basenodetype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Channel with the object that you specify. Returns an exception if the object is not of type Channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel(BaseNodeType node)ParametersNameTypeDescriptionnodeBaseNodeTypeThe BaseNodeType object.

### Channel(BaseNodeType)

Initializes a new instance of [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) with the object that you specify. Returns an exception if the object is not of type [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html).

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Channel(BaseNodeType node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | BaseNodeType | The BaseNodeType object. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-channel__channeltype.html language=enus -->
## TOPIC 01989: Channel(ChannelType)

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-channel__channeltype.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-channel__channeltype.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initializes a new instance of Channel with the object that you specify. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic Channel(ChannelType node)ParametersNameTypeDescriptionnodeChannelTypeThe ChannelType object.

### Channel(ChannelType)

Initializes a new instance of [Channel](nationalinstruments-veristand-systemdefinitionapi-channel.html) with the object that you specify.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public Channel(ChannelType node)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| node | ChannelType | The ChannelType object. |

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-columndimensions.html language=enus -->
## TOPIC 01990: ColumnDimensions

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-columndimensions.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-columndimensions.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the number of columns in the channel value. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic int ColumnDimensions { get; }ReturnsThe number of columns.

### ColumnDimensions

Gets the number of columns in the channel value.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public int ColumnDimensions { get; }

#### Returns

The number of columns.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-datasource.html language=enus -->
## TOPIC 01991: DataSource

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-datasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-datasource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets or sets the source channel that maps to the current channel and provides it data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic BaseNode DataSource { get; set; }ReturnsA BaseNode reference to the source channel.

### DataSource

Gets or sets the source channel that maps to the current channel and provides it data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) DataSource { get; set; }

#### Returns

A [BaseNode](nationalinstruments-veristand-systemdefinitionapi-basenode.html) reference to the source channel.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-defaultvalue.html language=enus -->
## TOPIC 01992: DefaultValue

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-defaultvalue.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-defaultvalue.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the default value of the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic double[] DefaultValue { get; }ReturnsThe default value.

### DefaultValue

Gets the default value of the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public double[] DefaultValue { get; }

#### Returns

The default value.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-getvaluetable__out-out.html language=enus -->
## TOPIC 01993: GetValueTable(out string[], out double[])

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-getvaluetable__out-out.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-getvaluetable__out-out.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the value table for the channel. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool GetValueTable(out string[] names, out double[] values)ParametersNameTypeDescriptionnamesout string[]The names for the channel value table.valuesout double[]The values for the channel v

### GetValueTable(out string[], out double[])

Gets the value table for the channel.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool GetValueTable(out string[] names, out double[] values)

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| names | out string[] | The names for the channel value table. |
| values | out double[] | The values for the channel value table. |

#### Returns

Returns true if the channel value table is defined.

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-isreadable.html language=enus -->
## TOPIC 01994: IsReadable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-isreadable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-isreadable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the channel is readable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsReadable { get; }

### IsReadable

Gets a value indicating whether the channel is readable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsReadable { get; }

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-iswritable.html language=enus -->
## TOPIC 01995: IsWritable

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-iswritable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-iswritable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets a value indicating whether the channel is writable. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic bool IsWritable { get; }

### IsWritable

Gets a value indicating whether the channel is writable.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public bool IsWritable { get; }

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-k_faultable.html language=enus -->
## TOPIC 01996: K_FAULTABLE

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-k_faultable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-k_faultable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A bit flag mask specifying that the channel can be faulted. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static readonly uint K_FAULTABLE

### K_FAULTABLE

A bit flag mask specifying that the channel can be faulted.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static readonly uint K_FAULTABLE

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-k_readable.html language=enus -->
## TOPIC 01997: K_READABLE

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-k_readable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-k_readable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A bit flag mask specifying that the channel can be read from. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static readonly uint K_READABLE

### K_READABLE

A bit flag mask specifying that the channel can be read from.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static readonly uint K_READABLE

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-k_scalable.html language=enus -->
## TOPIC 01998: K_SCALABLE

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-k_scalable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-k_scalable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A bit flag mask specifying that the channel can be scaled. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static readonly uint K_SCALABLE

### K_SCALABLE

A bit flag mask specifying that the channel can be scaled.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static readonly uint K_SCALABLE

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-k_writable.html language=enus -->
## TOPIC 01999: K_WRITABLE

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-k_writable.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-k_writable.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: A bit flag mask specifying that the channel can be written to. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic static readonly uint K_WRITABLE

### K_WRITABLE

A bit flag mask specifying that the channel can be written to.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public static readonly uint K_WRITABLE

Parent topic:

Channel Class

<!--NI_TOPIC bundle=veristand-net-api-ref path=nationalinstruments-veristand-systemdefinitionapi-channel-removedatasource.html language=enus -->
## TOPIC 02000: RemoveDataSource()

- bundle_id: `veristand-net-api-ref`
- source_path: `nationalinstruments-veristand-systemdefinitionapi-channel-removedatasource.html`
- source_url: https://docs-be.ni.com/bundle/veristand-net-api-ref/raw/resource/enus/nationalinstruments-veristand-systemdefinitionapi-channel-removedatasource.html
- document_id: `veristand-net-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the source channel that maps to the current channel and provides it data. SyntaxNamespace: NationalInstruments.VeriStand.SystemDefinitionAPIpublic void RemoveDataSource()

### RemoveDataSource()

Removes the source channel that maps to the current channel and provides it data.

#### Syntax

**Namespace:**[NationalInstruments.VeriStand.SystemDefinitionAPI](nationalinstruments-veristand-systemdefinitionapi.html)

public void RemoveDataSource()

Parent topic:

Channel Class
