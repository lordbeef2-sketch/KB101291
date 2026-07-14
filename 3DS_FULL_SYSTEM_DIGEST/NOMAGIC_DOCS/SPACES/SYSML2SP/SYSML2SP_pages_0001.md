# NOMAGIC DOCUMENTATION SPACE: SysML v2 Simulation

<!--NOMAGIC_SPACE key=SYSML2SP chunk=1 -->

<!--NOMAGIC_PAGE id=308314185 space=SYSML2SP version=7 -->
## PAGE 00001: (2026x Refresh1) Displaying simulation information

- page_id: `308314185`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314185/2026x+Refresh1+Displaying+simulation+information
- version_number: 7
- version_date: `2026-06-22T12:54:46.703+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Simulation information in views
- labels: []

### NORMALIZED CONTENT

During simulation, views can display runtime information associated with model elements. This information is dynamically updated during the simulation and reflects the current state of the simulated system. Observing runtime values, execution indicators, and requirement statuses directly on views makes it easier to understand how the system evolves over time.

##### Simulation annotations in views

During simulation, behavior concepts (e.g., states) or ports and connections (e.g., payloads flowing through connections) displayed in views are annotated to indicate the execution flow.

Simulation annotations are displayed for a state when a**State Usage**is placed inside a**Part Usage**in a view and that view is located within the**Root Simulation Target**hierarchy.

If the view displays the**Root****Simulation** **Target**, the view does not need to be located within the Root Simulation Target hierarchy and may be placed anywhere while still displaying the simulation annotations.

Simulation annotations mark symbols as:

- Active (default color [IMAGE alt='' src='']) - the symbol that is currently being executed during the simulation.
- Visited (default color [IMAGE alt='' src='']) - the symbols that have already been executed.
- Last Visited (default color [IMAGE alt='' src='']) - the symbol that has been executed most recently.

[IMAGE alt='' src='']

###### Annotations of the flashlight system simulation

###### Configuring annotation colors

To change the colors used for simulation annotations

1. In the main menu, select Options > Project .
2. In the Project Options dialog, select the Simulation option group. [ATTACHMENT filename='simulation_project_options.png']
3. On the right side of the dialog, select the value cell you want to change and click [ATTACHMENT filename='edit_value.png'] .
4. In the open dialog, select a new color and click OK .
5. Click OK to close the Project Options dialog.

##### Displaying runtime values

In views, runtime values are displayed in blue. During simulation, these runtime values replace the default values and are displayed next to:

- Attributes
- References
- Satisfy requirements

Attributes or references that contain expressions may display calculated values during simulation. These values appear directly in the view near the element names and update continuously as the simulation progresses.

When a simulation is running, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability during execution.

You can also [CONFLUENCE_PAGE title='(2026x Refresh1) Manipulating simulation information' space=''] directly in views and change simulation results in real-time.

[IMAGE alt='' src='']

###### A sample view displaying runtime values during model simulation.

###### Supported data types

Runtime values can be displayed in views only for the following data types:

- Primitive:
  - Integer
  - Real
  - Boolean
  - String
- Enumeration

If a property has a different data type, its runtime value is not displayed directly in the view.

#### TIP: Resizing shapes to fit runtime values

Resizing shapes to fit runtime values

If a runtime value does not fit inside a shape and is cut off, resize the shape as described below:

1. Select the shape you want to resize.
2. Do one of the following:
  - Click [ATTACHMENT filename='resize_icon.png'] on the shape.
  - Click [IMAGE alt='' src=''] in the view toolbar.

###### Automated requirement verification

Model simulation supports automated requirement verification. Runtime values on part, attribute, and reference shapes are highlighted in green or red to indicate whether the related requirement is satisfied. The verification result on the satisfy requirement shape is also highlighted in green or red, respectively.

In addition, a tooltip containing the text of the unsatisfied requirement appears when you hover the mouse pointer over a failing part, attribute, reference, or satisfy requirement shape.

[IMAGE alt='' src='']

###### View fragments showing failing attributes and the related satisfy requirement.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">During simulation, views can display runtime information associated with model elements. This information is dynamically updated during the simulation and reflects the current state of the simulated system. Observing runtime values, execution indicators, and requirement statuses directly on views makes it easier to understand how the system evolves over time.</p><h3 style="text-align: left;">Simulation annotations in views</h3><p style="text-align: left;">During simulation, behavior concepts (e.g., states) or ports and connections (e.g., payloads flowing through connections) displayed in views are annotated to indicate the execution flow.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1640a5b1-c4c8-45c7-a651-efc80673183e"><ac:rich-text-body><p>Simulation annotations are displayed for a state when a<span> </span><strong>State Usage</strong><span> </span>is placed inside a<span> </span><strong>Part Usage</strong><span> </span>in a view and that view is located within the<span> </span><strong>Root Simulation Target</strong><span> </span>hierarchy.</p><p>If the view displays the<span> </span><strong>Root</strong><span> </span><strong>Simulation</strong> <strong>Target</strong>, the view does not need to be located within the Root Simulation Target hierarchy and may be placed anywhere while still displaying the simulation annotations.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">Simulation annotations mark symbols as:</p><ul style="text-align: left;"><li data-uuid="6e5843ad-360d-4129-80ad-66a709c9ea37"><strong>Active</strong><span> (default color <ac:image><ri:attachment ri:filename="active_color.png" /></ac:image>) </span>- the symbol that is currently being executed during the simulation.</li><li data-uuid="bc219784-e5c9-4616-b7b4-1021a3c2f002"><strong>Visited</strong><span> (default color <ac:image><ri:attachment ri:filename="visited_color.png" /></ac:image>) </span>- the symbols that have already been executed.</li><li data-uuid="44b8cf90-8876-42e1-8e39-1bd3a739eec6"><strong>Last Visited</strong><span> (default color <ac:image><ri:attachment ri:filename="last_visited_color.png" /></ac:image>)</span>- the symbol that has been executed most recently.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="simulation_annotations.png" /></ac:image></p><h6 style="text-align: center;">Annotations of the flashlight system simulation</h6><p><br /></p><h4>Configuring annotation colors</h4><p>To change the colors used for simulation annotations</p><hr /><ol><li data-uuid="b576d7f7-6332-42b9-8cf8-934ba9a80522">In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="d6abdf92-d45c-487d-81d3-6758d0fc5a66">In the <strong>Project Options</strong> dialog, select the <strong>Simulation</strong> option group.<br /><ac:image><ri:attachment ri:filename="simulation_project_options.png" /></ac:image></li><li data-uuid="47028fe1-48fd-4519-8249-23e0d1ed57e5">On the right side of the dialog, select the value cell you want to change and click <ac:image><ri:attachment ri:filename="edit_value.png" /></ac:image>.</li><li data-uuid="0260722c-0926-4e77-bb04-bb3725fd58e5">In the open dialog, select a new color and click <strong>OK</strong>.</li><li data-uuid="038b1e53-3a2b-4372-85e9-47ce740fc3ab">Click <strong>OK</strong> to close the <strong>Project Options</strong> dialog.</li></ol><h3 style="text-align: left;">Displaying runtime values</h3><p>In views, runtime values are displayed in blue. During simulation, these runtime values replace the default values and are displayed next to:</p><ul><li data-uuid="4c764c77-655d-4b12-90da-a6d0e43d70f2">Attributes</li><li data-uuid="7a6375fc-fe9c-49a1-9208-a39703fd0450">References</li><li data-uuid="0c557862-e97b-4f33-830c-11d2bdb179ce">Satisfy requirements</li></ul><p>Attributes or references that contain expressions may display calculated values during simulation. These values appear directly in the view near the element names and update continuously as the simulation progresses.</p><p>When a simulation is running, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability during execution.</p><p>You can also <ac:link><ri:page ri:content-title="(2026x Refresh1) Manipulating simulation information" /><ac:plain-text-link-body><![CDATA[modify runtime values]]></ac:plain-text-link-body></ac:link> directly in views and change simulation results in real-time.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="runtime_values_in_views.png" /></ac:image></p><h6 style="text-align: center;">A sample view displaying runtime values during model simulation.</h6><h4 style="text-align: left;">Supported data types</h4><p style="text-align: left;">Runtime values can be displayed in views only for the following data types:</p><ul style="text-align: left;"><li data-uuid="ead3d827-a142-4a7e-b80e-a02fdcb92de0">Primitive:<ul><li>Integer</li><li>Real</li><li>Boolean</li><li>String</li></ul></li><li data-uuid="2fcf634a-5a42-4f66-be8d-a75dbf35d594">Enumeration</li></ul><p style="text-align: left;">If a property has a different data type, its runtime value is not displayed directly in the view.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="65dd4694-e5f8-465c-9e2f-355fcad37925"><ac:parameter ac:name="title">Resizing shapes to fit runtime values</ac:parameter><ac:rich-text-body><p>If a runtime value does not fit inside a shape and is cut off, resize the shape as described below:</p><ol><li data-uuid="b98a04b2-4802-4f66-b891-c2d1de526e90">Select the shape you want to resize.</li><li data-uuid="c4a443aa-1168-4817-bdad-845028f0ba22">Do one of the following:<ul><li data-uuid="1b67b46f-c3e2-40a7-b278-855a4b259526">Click <ac:image><ri:attachment ri:filename="resize_icon.png" /></ac:image> on the shape.</li><li data-uuid="48e8d067-405c-4c21-bf16-456895c3439e">Click<span> <ac:image ac:thumbnail="true" ac:height="10"><ri:attachment ri:filename="resize_icon_in_toolbar.png" /></ac:image></span><span> </span>in the view toolbar.</li></ul></li></ol></ac:rich-text-body></ac:structured-macro><h4>Automated requirement verification</h4><p>Model simulation supports automated requirement verification. Runtime values on part, attribute, and reference shapes are highlighted in green or red to indicate whether the related requirement is satisfied. The verification result on the satisfy requirement shape is also highlighted in green or red, respectively.</p><p>In addition, a tooltip containing the text of the unsatisfied requirement appears when you hover the mouse pointer over a failing part, attribute, reference, or satisfy requirement shape.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="requirement_verification.png" /></ac:image></p><h6 style="text-align: center;">View fragments showing failing attributes and the related satisfy requirement.</h6>
````

<!--NOMAGIC_PAGE id=308314182 space=SYSML2SP version=1 -->
## PAGE 00002: (2026x Refresh1) Exporting simulation data to CSV

- page_id: `308314182`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314182/2026x+Refresh1+Exporting+simulation+data+to+CSV
- version_number: 1
- version_date: `2026-05-19T10:23:37.317+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) SyML v2 Simulation window
- labels: []

### NORMALIZED CONTENT

You can export the simulation data from the **Variables** panel for further analysis outside the modeling tool environment.Exported data is saved in CSV format, which can be opened using spreadsheet or data analysis tools.

Only the variables with the following data types are exported:

- Primitive data types
  - Integer
  - Real
  - String
  - Boolean
- Enumeration values

To export the simulation data

1. In the **Variables** panel, select the variables you want to export. If no variables are selected, all variables of the supported data types are exported.If a part usage or port usage is selected, all nested primitive feature values and enumeration values are exported recursively.
2. In the panel toolbar, click [ATTACHMENT filename='export_to_csv.png'] .
3. In the open dialog, select the directory where you want to save the file.
4. Click the **Save** button.

The CSV file with the recorded values is downloaded to your selected location.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">You can export the simulation data from the <strong>Variables</strong> panel for further analysis outside the modeling tool environment. </span><span style="color:var(--ds-text,#172b4d);">Exported data is saved in CSV format, which can be opened using spreadsheet or data analysis tools.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Only the variables with the following data types are exported:</span></p><ul style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="a2d8641a-aeed-4b82-8b4e-33ea6b1c55bd"><span style="color:var(--ds-text,#172b4d);">Primitive data types</span><ul><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">Integer</span></li><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">Real</span></li><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">String</span></li><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">Boolean</span></li></ul></li><li style="color:var(--ds-text,#172b4d);" data-uuid="70657c65-28e2-421b-90f0-d6338e8c7e90"><span style="color:var(--ds-text,#172b4d);">Enumeration values</span></li></ul><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To export the simulation data</span></p><hr /><ol style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="0fc6db49-b400-4e6f-9fe2-bf6732c32a20"><span style="color:var(--ds-text,#172b4d);">In the <strong>Variables</strong> panel, select the variables you want to export.<br /></span><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="a7fb7938-43f0-40ee-ab02-48090540ce61"><ac:rich-text-body><ul><li>If no variables are selected, all variables of the supported data types are exported.</li><li><span style="color:var(--ds-text,#172b4d);">If a part usage or port usage is selected, all nested primitive feature values and enumeration values are exported recursively.</span></li></ul></ac:rich-text-body></ac:structured-macro></li><li style="color:var(--ds-text,#172b4d);" data-uuid="256cf81e-85f7-4ac8-b503-b8decae26e4d">In the panel toolbar, click <ac:image><ri:attachment ri:filename="export_to_csv.png"><ri:page ri:content-title="(2026x Refresh1) Exporting simulation data to CSV" /></ri:attachment></ac:image>.</li><li style="color:var(--ds-text,#172b4d);" data-uuid="85bc4fac-7b81-4fda-9358-2147a61bef1c"><span style="color:var(--ds-text,#172b4d);">In the open dialog, select the directory where you want to save the file.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="17ef7cb1-b8a5-4710-82ac-fd4fe514721a"><span style="color:var(--ds-text,#172b4d);">Click the <strong>Save</strong> button.</span></li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The CSV file with the recorded values is downloaded to your selected location.</span></p>
````

<!--NOMAGIC_PAGE id=308314198 space=SYSML2SP version=3 -->
## PAGE 00003: (2026x Refresh1) Manipulating simulation information

- page_id: `308314198`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314198/2026x+Refresh1+Manipulating+simulation+information
- version_number: 3
- version_date: `2026-06-22T13:06:12.339+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Simulation information in views
- labels: []

### NORMALIZED CONTENT

You can interact with the simulation data displayed in views to improve understanding and analysis of system behavior during execution. Simulation views allow inspection and modification of runtime information without interrupting the simulation.Manipulating simulation data provides a practical way to observe how a model responds to changing conditions, supporting both debugging and behavioral analysis.

##### Changing Runtime Values

During simulation, initial runtime values (indicated by “:=”) can be changed directly in the views. This allows you to observe how the system’s behavior responds to changing values while the simulation is running.

To change runtime values on element shapes

1. During model simulation, select a part, attribute, or reference shape in a view.
2. Select the initial runtime value (indicated by ":=") you want to change.
3. Do one of the following depending on the value type:
  - For a numerical runtime value, type a new value. [ATTACHMENT filename='changing_numerical_value.png']
  - For an enumeration runtime value, click the value and select a new value from the drop-down list. [ATTACHMENT filename='changing_enumeration_value.png']
  - For a Boolean value, click the value several times until the desired value is set. [ATTACHMENT filename='changing_boolean_value.png']
4. Press Enter to save the change.

When runtime values are changed, the simulation data is automatically updated.

##### Sending a Payload

A payload can be sent directly from a state transition in a view during model simulation. If sending a payload is supported for a transition, a smart manipulator icon appears next to the selected transition symbol.

To send a payload from a transition symbol

1. Select the transition symbol that has the payload you want to send.
2. Click the Fire Transition icon. [ATTACHMENT filename='firing_transition.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="isSelectedEnd"><span>You can interact with the simulation data displayed in views to improve understanding and analysis of system behavior during execution. Simulation views allow inspection and modification of runtime information without interrupting the simulation. </span><span>Manipulating simulation data provides a practical way to observe how a model responds to changing conditions, supporting both debugging and behavioral analysis.</span></p><h3 style="text-align: left;">Changing Runtime Values</h3><p style="text-align: left;">During simulation, initial runtime values (indicated by “:=”) can be changed directly in the views. This allows you to observe how the system’s behavior responds to changing values while the simulation is running.</p><p style="text-align: left;">To change runtime values on element shapes</p><hr /><ol style="text-align: left;"><li data-uuid="12d69495-b30f-4ab1-8136-ed097e7fc1c0">During model simulation, select a part, attribute, or reference shape in a view.</li><li data-uuid="4865dbf1-176e-4b01-8170-791786554a5a">Select the<span> </span>initial runtime value (indicated by &quot;:=&quot;) you want to change.</li><li data-uuid="5dbc7164-e50c-4750-bd5b-bc5378b18734">Do one of the following depending on the value type:<ul style="text-align: left;"><li>For a numerical runtime value, type a new value.<br /><ac:image ac:height="116"><ri:attachment ri:filename="changing_numerical_value.png" /></ac:image></li><li>For an enumeration runtime value, click the value and select a new value from the drop-down list.<br /><ac:image><ri:attachment ri:filename="changing_enumeration_value.png" /></ac:image></li><li>For a Boolean value, click the value several times until the desired value is set.<br /><ac:image><ri:attachment ri:filename="changing_boolean_value.png" /></ac:image></li></ul></li><li data-uuid="057f4811-0e9c-4076-8404-8c3618dcfe2c">Press Enter to save the change.</li></ol><p style="text-align: left;">When runtime values are changed, the simulation data is automatically updated. </p><h3 style="text-align: left;">Sending a Payload</h3><p style="text-align: left;">A payload can be sent directly from a state transition in a view during model simulation. If sending a payload is supported for a transition, a smart manipulator icon appears next to the selected transition symbol.</p><p style="text-align: left;">To send a payload from a transition symbol</p><hr /><ol style="text-align: left;"><li data-uuid="2dbcdec5-3010-4b20-91d9-9c7906778145">Select the transition symbol that has the payload you want to send.</li><li data-uuid="4d2baade-2fc1-447a-b146-29344ad7be99">Click the<span> </span><strong>Fire Transition</strong><span> </span>icon. <br /><ac:image><ri:attachment ri:filename="firing_transition.png" /></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=309365941 space=SYSML2SP version=1 -->
## PAGE 00004: (2026x Refresh1) Modeling states for simulation

- page_id: `309365941`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365941/2026x+Refresh1+Modeling+states+for+simulation
- version_number: 1
- version_date: `2026-06-03T12:57:39.291+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Simulating states
- labels: []

### NORMALIZED CONTENT

This section provides guidelines for modeling states to ensure correct execution during simulation.

A state defines the dynamic behavior of a system by specifying the states, transitions, and actions that occur in response to events or conditions. When modeling states for simulation, it is essential to structure the model so that the simulation engine can correctly evaluate:

- State activation - which states are currently active
- Transition triggers - events or conditions that cause state changes
- Guard conditions - logical rules that enable or block transitions
- Behavioral actions - activities performed within states or during transitions
- Payload (signal) communication - how data or events are passed between elements

The following sections describe the key modeling elements required to create executable states and ensure accurate simulation results.

#### Initial state

An initial state represents the starting point of a state. It defines which state becomes active when execution begins.

An initial state does not represent an actual system condition. Instead, it is used to determine the first active state when the simulation starts.

The initial state is determined by either:

- the start node, or
- a state with no incoming transitions

If multiple states satisfy this condition, the simulation engine selects the first one based on model order.

#### PANEL: Example

Example

exhibitstateOperating_STM{ 
stateOff; 
stateStarting; 
stateRunning; 
transitionfirststartthenOff; 
transitionfirstOffthenStarting; 
transitionfirstStartingthenRunning; 
}

In the above example, the simulation starts at**start**, the transition leads to**Off**, and **Off**becomes the first active state.

#### Entry, do, and exit actions

States can define behaviors that are executed during different phases of state activation.

Entry, do, and exit actions allow the model to describe:

- Entry - initialization logic executed when entering a state.
- Do - behavior executed while the state remains active.
- Exit - cleanup or signaling executed when leaving a state

#### PANEL: Example

Example

stateOff{ 
entry{ 
assignlevel :=1; 
} 
do{ 
sendnewStatusUpdate() 
} 
exit{ 
sendnewStop() 
} 
}

Simulation behavior in the example above:

1. When Off becomes active, the entry action runs.
2. While Off is active, the do action runs.
3. When leaving Off , the exit action runs.

#### NOTE: Example

Only the following action types are currently supported:

- Assignment action
- Send action
- Composite actions (multiple actions executed sequentially) Exampleentry{ 
level :=1 
sendnewStart() 
}

#### Sending payloads using the send action

Payloads (signals) can be sent using thesendaction. Several optional parameters may be defined when sending a payload.

##### Sending a payload without attributes, a sender, or receiver

A payload can be sent without specifying attributes, sender, or receiver. In this case, the payload is sent to the state itself. If theitem definitionincludes attributes with default values, these defaults are included in the payload when it is sent.

#### PANEL: Example

Example

itemdefStart;stateOff{ 
entrysendnewStart(); 
}

##### Sending a payload with attributes

Payloads may contain attributes. Attribute values can be provided when sending the payload.

#### NOTE: Limitation

Limitation

and

#### PANEL: Example

Example

itemdefDataSignal 
{attributereading:Real; 
attributeisUrgent:Boolean 
}stateOff{ 
entrysendnewDataSignal(reading=150,isUrgent=false); 
}

##### Sending a payload via the sender

A payload can be sent through a**port usage** (sender). If multiple Connections or interface usages exist, the payload is delivered toall connected receivers, unless a specific receiver is defined.

#### PANEL: Example

Example

ItemdefStart;stateOff{ 
entrysendnewStart()viabuttonPort; 
}

##### Sending a payload to the receiver

A payload can be sent to a**part usage**(receiver)*.*

#### PANEL: Example

Example

ItemdefStart;stateOff{ 
entrysendnewStart()toButton; 
}

##### Sending a payload via the sender to the receiver

A payload can also be sent via a**port usage**(sender) to a**part usage**(receiver). In this scenario, the payload is transmitted from the specified sender port to the defined receiver part. This approach is useful when you want to limit delivery to specific receivers connected to that port.

#### PANEL: Example

Example

ItemdefStart;stateOff{ 
entrysendnewStart()viabuttonPorttoButton; 
}

#### Triggers on transitions

Atriggerspecifies the event that causes a transition to become eligible for execution. Without triggers, transitions would occur immediately whenever their source state is active. Triggers ensure transitions occur only when specific events happen.

A transition is executed when:

- Its trigger occurs.
- Any guard condition evaluates to true .

##### Types of supported triggers

###### Payload (signal) trigger

A payload trigger is triggered when a specific payload (signal) is received.

**Examples:**

transitionfirstOffacceptStartthenStarting;

transitionfirstOffacceptStartviaoutPortthenStarting;

The transition fires when the**Start**signal is received. If a port is defined, the payload will only be received if it arrives through the**specified port**.

Payloads can be defined using:

- Item definition
- Item usage

###### Change trigger

A change trigger is triggered when a Boolean expression changes from*false* to *true*, or when it evaluates to*true* during its first evaluation.

#### PANEL: Example

Example

transitionfirstIdleacceptwhenengine.temperature >100thenActive;

The transition fires when the expression becomes *true*.

###### Time trigger

A time trigger is triggered based on the simulation time.

Two types of time triggers are supported:

- Absolute time ExampletransitionfirstOffacceptat5[s]thenStarting; The transition fires when the simulation time reaches 5 seconds.
- Relative time ExampletransitionfirstOffacceptafter10[s]thenStarting; The transition fires when the simulation time reaches 10 seconds.

#### NOTE: Example

- Expressions referencing model values are supported. ExampletransitionfirstOffacceptaftertargetTime [s]thenStarting;
- The simulation engine does not interpret time units. All time values are executed in seconds by default.

#### Using guards on transitions

Aguard is a Boolean expression that must evaluate to*true*for a transition to occur. They add an additional condition that must be satisfied after the trigger is received. Therefore, guards allow modelingdecision logic within a state.

Guards are commonly used to:

- Check system parameters
- Filter incoming events
- Ensure transitions occur only in valid conditions

Without guards, transitions would be triggered whenever their events occur.

#### PANEL: Example

Example

transitionfirstOffacceptStartiflevel >1thenStarting;

Simulation behavior in the example above:

1. A Start signal is received.
2. The guard level > 1 is evaluated.
3. The transition executes only if the guard evaluates to true .

#### Using effects on transitions

A transition effectis an action that is executed when a transition occurs. Effects define behavior that happens during the transition between two states.

Effects allow the model to perform operations that logically belong to the transition itself, such as:

- Sending payloads
- Updating variables

This helps separatethe**state behavior** fromthe**transition behavior**.

**Execution order**

When a transition occurs, execution proceeds in the following order:

1. Exit action of the source state
2. Transition effect
3. Entry action of the target state

#### PANEL: Example

Example

transitionfirstOffacceptStartdosendnewStart()thenStarting;

Simulation behavior in the above example:

1. The exit action of Off executes.
2. The transition effect sends Start .
3. The entry action of Starting executes.

#### NOTE: Example

#### PANEL: Example

Example

transitionfirstOffacceptStartdo 
sendnewStart(); 
assignlevel; 
thenStarting;

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section provides guidelines for modeling states to ensure correct execution during simulation.</p><p>A state defines the dynamic behavior of a system by specifying the states, transitions, and actions that occur in response to events or conditions. When modeling states for simulation, it is essential to structure the model so that the simulation engine can correctly evaluate:</p><ul><li data-uuid="0b28f3d8-f81f-4034-9de8-13b1d9b88f80"><strong>State activation</strong> - which states are currently active</li><li data-uuid="50458a3a-ef21-43a9-a86b-0c4df8504359"><strong>Transition triggers</strong> - events or conditions that cause state changes</li><li data-uuid="aae5a99f-5b9c-40ef-9eec-f5b32edbdc29"><strong>Guard conditions</strong> - logical rules that enable or block transitions</li><li data-uuid="6f302b08-8bf3-4099-bdc4-70d209cb40a2"><strong>Behavioral actions</strong> - activities performed within states or during transitions</li><li data-uuid="c2b1be6a-498d-49b8-8207-d18ffa962d31"><strong>Payload (signal) communication</strong> - how data or events are passed between elements</li></ul><p>The following sections describe the key modeling elements required to create executable states and ensure accurate simulation results.</p><h2 style="text-align: left;">Initial state</h2><p>An initial state represents the starting point of a state. It defines which state becomes active when execution begins.</p><p>An initial state does not represent an actual system condition. Instead, it is used to determine the first active state when the simulation starts.</p><p>The initial state is determined by either:</p><ul><li data-uuid="290afc43-4823-46bb-8ea7-18d1bd80537b">the start node, or</li><li data-uuid="1dcdd111-0d3d-4bbb-bce1-16d5040face2">a state with no incoming transitions</li></ul><p>If multiple states satisfy this condition, the simulation engine selects the first one based on model order.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4d300c30-78eb-43b7-bce0-0209ef667fc3"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">exhibit</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Operating_STM</span><span style="color:var(--ds-text,#000000);"> {<br /></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Running</span><span style="color:var(--ds-text,#000000);">;<br /></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Running</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    }</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">In the above example, the simulation starts at<span> </span><strong>start</strong>, the transition leads to<span> </span><strong>Off</strong>, and <strong>Off</strong><span> </span>becomes the first active state.</p><h2 style="text-align: left;">Entry, do, and exit actions</h2><p style="text-align: left;">States can define behaviors that are executed during different phases of state activation.</p><p style="text-align: left;">Entry, do, and exit actions allow the model to describe:</p><ul><li data-uuid="058da20a-c305-469f-a142-a6b09d47c5dd"><strong>Entry</strong> - initialization logic executed when entering a state.</li><li data-uuid="1daac322-0f70-4973-b4b1-33ef1fb4beaa"><strong>Do</strong> - behavior executed while the state remains active.</li><li data-uuid="32473065-9a44-4a33-a950-da80e3097339"><strong>Exit</strong> - cleanup or signaling executed when leaving a state</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="da2b31a0-cd4e-4d9f-a836-8bbccea047ff"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">assign</span><span style="color:var(--ds-text,#000000);"> level := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">   }</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">do</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> StatusUpdate()</span><br /><span style="color:var(--ds-text,#000000);">   }</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">exit</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Stop()</span><br /><span style="color:var(--ds-text,#000000);">   }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">Simulation behavior in the example above:</p><ol style="text-align: left;"><li data-uuid="7030280c-7bea-43b9-b0d3-b715a1a7e6f7">When<span> </span><strong>Off</strong><span> </span>becomes active, the<span> </span><strong>entry</strong> action runs.</li><li data-uuid="6fa1c0b3-a35a-4da8-bb2a-29d3bff90de8">While<span> </span><strong>Off</strong><span> </span>is active, the<span> </span><strong>do</strong> action runs.</li><li data-uuid="5a6d5e72-906b-43ab-9378-3b8f764ecb5a">When leaving<span> </span><strong>Off</strong>, the<strong> </strong><strong>exit </strong>action runs.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="df4458f7-3c46-47f5-a860-eea15e354451"><ac:rich-text-body><p>Only the following action types are currently supported:</p><ul><li data-uuid="0f4640cb-a4b2-4827-b786-5d242edefbef">Assignment action</li><li data-uuid="40564044-4987-4966-82e8-8daa4d540f41">Send action</li><li data-uuid="c1230362-1939-4124-b274-099e26bc2f5b">Composite actions (multiple actions executed sequentially)<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3607b330-3abf-4954-b706-84f2bd982e5a"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">   level := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Start()</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></li></ul></ac:rich-text-body></ac:structured-macro><h2>Sending payloads using the send action</h2><p>Payloads (signals) can be sent using the<span> </span>send<span> </span>action. Several optional parameters may be defined when sending a payload.</p><h3>Sending a payload without attributes, a sender, or receiver</h3><p>A payload can be sent without specifying attributes, sender, or receiver. In this case, the payload is sent to the state itself. If the<span> </span>item definition<span> </span>includes attributes with default values, these defaults are included in the payload when it is sent.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="eed94ba3-ceb3-48f5-8837-276d9a41d87c"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">item</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Start</span><span style="color:var(--ds-text,#000000);">();</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload with attributes</h3><p>Payloads may contain attributes. Attribute values can be provided when sending the payload.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a5468b6e-4422-4e87-b797-dca796792e11"><ac:parameter ac:name="title">Limitation</ac:parameter><ac:rich-text-body>Attributes can only be defined for<span> </span>primitive<span> and </span>enumeration<span> </span>types.</ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="980e8ee4-844e-4e85-b72d-c2c3f131003a"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">item</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">DataSignal</span><br /><span style="color:var(--ds-text,#000000);">{ </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">reading</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">isUrgent</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Boolean</span><span style="color:var(--ds-text,#000000);"> </span><br /><span style="color:var(--ds-text,#000000);">}<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">DataSignal</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">reading</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">150</span><span style="color:var(--ds-text,#000000);">, </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">isUrgent</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue,#0055cc);">false</span><span style="color:var(--ds-text,#000000);">);</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload via the sender</h3><p>A payload can be sent through a<span> </span><strong>port usage</strong> (sender). If multiple Connections or interface usages exist, the payload is delivered to<span> </span>all connected receivers, unless a specific receiver is defined.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e8bc354e-3dd3-49e0-9c80-ab633dba5c2b"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">Item </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">via</span><span style="color:var(--ds-text,#000000);"> buttonPort;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload to the receiver</h3><p>A payload can be sent to a<span> <strong>part usage</strong> </span>(receiver)<em>.</em></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10b53614-dfee-4732-afb1-bd641ebdd44b"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">Item </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> Button;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload via the sender to the receiver</h3><p>A payload can also be sent via a<span> <strong>port usage</strong></span><span> </span>(sender) to a<span> <strong>part usage</strong> </span>(receiver). In this scenario, the payload is transmitted from the specified sender port to the defined receiver part. This approach is useful when you want to limit delivery to specific receivers connected to that port.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3f321aba-91a2-498b-a566-dc4cdb426944"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">Item </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">via</span><span style="color:var(--ds-text,#000000);"> buttonPort </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> Button;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h2 class="code-java">Triggers on transitions</h2><p style="text-align: left;">A<span> </span>trigger<span> </span>specifies the event that causes a transition to become eligible for execution. Without triggers, transitions would occur immediately whenever their source state is active. Triggers ensure transitions occur only when specific events happen.</p><p style="text-align: left;">A transition is executed when:</p><ul style="text-align: left;"><li data-uuid="98466f7d-f999-414c-a502-e980e20d4009">Its trigger occurs.</li><li data-uuid="2c261f9d-1cdd-4e43-af87-c2d793c3f9f2">Any guard condition evaluates to <em>true</em>.</li></ul><h3 style="text-align: left;">Types of supported triggers</h3><h4 style="text-align: left;">Payload (signal) trigger</h4><p style="text-align: left;">A payload trigger is triggered when a specific payload (signal) is received.</p><p style="text-align: left;"><strong>Examples:</strong></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b6baf7f4-fdcc-494b-be07-3f4521551a94"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e751214a-70a3-4b84-ac84-3a7251603d8c"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">via</span><span style="color:var(--ds-text,#000000);"> outPort </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">The transition fires when the<span> </span><strong>Start</strong><span> </span>signal is received. If a port is defined, the payload will only be received if it arrives through the<span> </span><strong>specified port</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7c9a8090-868b-4d78-843e-fe7137208ed0"><ac:rich-text-body><p>Payloads can be defined using:</p><ul><li data-uuid="ab972ab2-c719-441b-9a4c-1b6906e7cf58">Item definition</li><li data-uuid="508c62aa-ea9b-4903-8cf2-49af0c26bf23">Item usage</li></ul></ac:rich-text-body></ac:structured-macro><h4>Change trigger</h4><p style="text-align: left;">A change trigger is triggered when a Boolean expression changes from<span> </span><em>false</em> to <em>true</em>, or when it evaluates to<span> </span><em>true</em> during its first evaluation.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="31f0c11f-d650-4cd3-abf8-e5dadf5e1ae1"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> Idle </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">when</span><span style="color:var(--ds-text,#000000);"> engine.temperature &gt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Active</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">The transition fires when the expression becomes <em>true</em>.</p><h4 style="text-align: left;">Time trigger</h4><p style="text-align: left;">A time trigger is triggered based on the simulation time.</p><p style="text-align: left;">Two types of time triggers are supported:</p><ul><li style="text-align: left;" data-uuid="36c69654-fafe-4509-a0d4-7964fdb9c7fe"><strong>Absolute time</strong><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="548fb61f-8717-46bd-b72b-9f879f4b590f"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">at</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">5</span><span style="color:var(--ds-text,#000000);"> [s] </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro>The transition fires when the simulation time reaches<span> </span>5 seconds.</li><li style="text-align: left;" data-uuid="e97d9909-d2da-4924-927b-63a6e3956d75"><strong>Relative time</strong><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="941c96ee-ba51-46c7-b0b0-510486b878dc"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">after</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">10</span><span style="color:var(--ds-text,#000000);"> [s] </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro>The transition fires when the simulation time reaches<span> </span>10 seconds.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="983ab964-c19a-4121-b68a-a7ebc2bbc0f4"><ac:rich-text-body><ul><li data-uuid="3f43bb8e-bc2d-446b-a168-1afff29c8696">Expressions referencing model values are supported.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10afd8d5-9a05-47f6-9196-70e73d6eb1e0"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> Off </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">after</span><span style="color:var(--ds-text,#000000);"> targetTime [s] </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="0ed8c1b3-2765-42eb-b908-5fc601816d30">The simulation engine<span> </span>does not interpret time units. All time values are executed in<span> </span>seconds by default.</li></ul></ac:rich-text-body></ac:structured-macro><h2 class="code-java">Using guards on transitions</h2><p style="text-align: left;">A<span> </span>guard is a Boolean expression that must evaluate to<span> </span><em>true</em><span> </span>for a transition to occur. They add an additional condition that must be satisfied after the trigger is received. Therefore, guards allow modeling<span> </span>decision logic within a state.</p><p style="text-align: left;">Guards are commonly used to:</p><ul style="text-align: left;"><li data-uuid="d2e3c98d-5949-4b90-9e3e-f9fdc32a513e">Check system parameters</li><li data-uuid="255a7bae-53aa-4569-a91d-708d4ac928ae">Filter incoming events</li><li data-uuid="879be7b3-c3cc-4671-8eb2-6408f0777bbb">Ensure transitions occur only in valid conditions</li></ul><p style="text-align: left;">Without guards, transitions would be triggered whenever their events occur.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9286e644-1983-482b-b815-4accd9e922f2"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">if</span><span style="color:var(--ds-text,#000000);"> level &gt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">Simulation behavior in the example above:</p><ol style="text-align: left;"><li data-uuid="4a86395f-5907-4ebb-8471-97a54e245e08">A<span> </span><strong>Start</strong><span> </span>signal is received.</li><li data-uuid="07c7437d-ecc7-4a58-889b-9ef7893ac7bf">The guard<span> </span>level &gt; 1<span> </span>is evaluated.</li><li data-uuid="9b7d4704-5a49-47af-885d-23c8b9509882">The transition executes<span> </span>only if the guard evaluates to <em>true</em>.</li></ol><h2 style="text-align: left;">Using effects on transitions</h2><p style="text-align: left;">A transition effect<span> </span>is an action that is executed when a transition occurs. Effects define behavior that happens during the transition between two states.</p><p style="text-align: left;">Effects allow the model to perform operations that logically belong to the transition itself, such as:</p><ul style="text-align: left;"><li data-uuid="279c3de4-f7c0-45f4-8d98-64876075fcc3">Sending payloads</li><li data-uuid="42f0dbb9-a877-4551-9495-53c792c645cc">Updating variables</li></ul><p style="text-align: left;">This helps separate<span> the </span><strong>state behavior</strong> from<span> the </span><strong>transition behavior</strong>.</p><p style="text-align: left;"><strong>Execution order</strong></p><p style="text-align: left;">When a transition occurs, execution proceeds in the following order:</p><ol style="text-align: left;"><li data-uuid="ee25645f-faf6-4150-b9df-0d48ae4b7c55">Exit action<span> </span>of the source state</li><li data-uuid="31ed7db3-aa9d-442a-9604-fd0c698e1761">Transition<span> </span>effect</li><li data-uuid="d89aef34-e580-4919-8388-1f40bc1bbd54">Entry action<span> </span>of the target state</li></ol><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e361fa99-b885-4f23-b4e7-b68a981b7359"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">do</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Start() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">Simulation behavior in the above example:</p><ol style="text-align: left;"><li data-uuid="fe00f8b2-07e5-47ab-aa02-4e2311477bdf">The exit action of<span> </span><strong>Off</strong><span> </span>executes.</li><li data-uuid="3eb5aaed-cfa2-4ac7-a472-28fd60fe4c7d">The transition effect sends<span> </span><strong>Start</strong>.</li><li data-uuid="a9940bb9-a76c-447d-ac20-4661dddbc892">The entry action of<span> </span><strong>Starting</strong><span> </span>executes.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="20889c99-8651-4890-a7e8-b9d28cfc75a0"><ac:rich-text-body>Effects may include multiple actions. These actions are executed in the order defined.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1b0e4a1c-def1-4a3c-ade6-fcaf01ab7532"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> Off </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">do</span><br /><span style="color:var(--ds-text,#000000);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Start();</span><br /><span style="color:var(--ds-text,#000000);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">assign</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">level</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=308314148 space=SYSML2SP version=1 -->
## PAGE 00005: (2026x Refresh1) Prerequisites

- page_id: `308314148`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314148/2026x+Refresh1+Prerequisites
- version_number: 1
- version_date: `2026-05-19T10:23:36.818+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

To work with all of the SysML v2 simulation features, the following software should be [installed](https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&version=latest):

- One of the following CATIA Magic/No Magic modeling tools:
  - Cameo Systems Modeler (Enterprise Edition only)
  - Cameo Enterprise Architecture
  - Magic Cyber Systems Engineer
  - Magic Systems of Systems Architect
- SysML v1 Plugin.
- Cameo Requirements Modeler.
- Cameo Simulation Toolkit or Magic Model Analyst.
- SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.
- SysML v2 Simulation Plugin. It enables execution of SysML v2 models (state machine simulations, mathematical calculations, and requirements verification).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">To work with all of the SysML v2 simulation features, the following software should be <a href="https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&amp;version=latest">installed</a>:</p><ul style="text-align: left;"><li data-uuid="34fec4e7-ad39-45f6-8615-0a3ea8277051">One of the following CATIA Magic/No Magic modeling tools:<ul><li>Cameo Systems Modeler (Enterprise Edition only)</li><li>Cameo Enterprise Architecture</li><li>Magic Cyber Systems Engineer</li><li>Magic Systems of Systems Architect</li></ul></li><li data-uuid="4d8f8ae9-1b0d-4142-9b1e-06cd6790e2d1">SysML v1 Plugin.</li><li data-uuid="2090e25b-4471-446c-98b8-3950634ee8a0">Cameo Requirements Modeler.</li><li data-uuid="75a80510-7ecf-4758-a004-5d3ef8fa48f6">Cameo Simulation Toolkit or Magic Model Analyst.</li><li data-uuid="8cf4e403-0608-4b30-bf35-0aac0af7e487">SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.</li><li data-uuid="b8263519-1d0c-49a9-853b-b04fb72718fe">SysML v2 Simulation Plugin. It enables execution of SysML v2 models (state machine simulations, mathematical calculations, and requirements verification).</li></ul>
````

<!--NOMAGIC_PAGE id=309365943 space=SYSML2SP version=1 -->
## PAGE 00006: (2026x Refresh1) Running the state simulation

- page_id: `309365943`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365943/2026x+Refresh1+Running+the+state+simulation
- version_number: 1
- version_date: `2026-06-03T12:57:39.452+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Simulating states
- labels: []

### NORMALIZED CONTENT

The SysML v2 simulation engine performs a state simulation when one of the following elements is selected for simulation:

- State
- Exhibit state
- Part usage that owns an **e** xhibit state

##### Starting state simulation

To start the state simulation

1. Simulate a s tate, exhibit state, or part usage that owns an exhibit state.
2. In the SysML v2 Simulation window, click [IMAGE alt='' src=''].

The simulation runs until it is manually stopped.

##### Terminating state simulation

You can terminate the simulation by clicking**Terminate**(**[IMAGE alt='' src='']**)from one of the following locations:

- Diagram toolbar
- SysML v2 Simulation window
- Context menu of the simulated element

##### Sending payloads during simulation

During a simulation, payloads can be sent interactively using thesmart manipulator of a transition symbol displayed in views.

To send a payload from a transition symbol

1. Select the transition symbol that defines the payload you want to send.
2. Click Fire Transition .

If no element consumes a payload, it is automatically removed from the event pool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The SysML v2 simulation engine performs a state simulation when one of the following elements is selected for simulation:</p><ul style="text-align: left;"><li data-uuid="280bcaf4-3861-4dd2-aae1-1af30d0e0d61"><strong>State</strong></li><li data-uuid="21c1f7a3-3fab-4119-878c-cd99f13cd850"><strong>Exhibit state</strong></li><li data-uuid="860c5cf2-9f0e-48df-83c5-b57c7f6e9c0e"><strong>Part usage</strong><span> </span>that owns an<span> <strong>e</strong></span><strong>xhibit state</strong></li></ul><h3 style="text-align: left;">Starting state simulation</h3><p style="text-align: left;">To start the state simulation</p><hr /><ol style="text-align: left;"><li data-uuid="a77afb1d-7ba7-48fd-9c6e-a4bedeb72c9b">Simulate a<span> s</span>tate, exhibit state, or part usage that owns an exhibit state.</li><li data-uuid="929aaf13-0187-4e3a-a8a4-eea59637245a">In the <strong>SysML v2 Simulation</strong> window, click <strong><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="start.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Running the state simulation" /></ri:attachment></ac:image>.</strong></li></ol><p style="text-align: left;">The simulation runs until it is manually stopped.</p><h3 style="text-align: left;">Terminating state simulation</h3><p style="text-align: left;">You can terminate the simulation by clicking<span> </span><strong>Terminate</strong><span> (<strong><ac:image><ri:attachment ri:filename="terminate.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Running the state simulation" /></ri:attachment></ac:image></strong>) </span>from one of the following locations:</p><ul style="text-align: left;"><li data-uuid="df4b2e7f-c7e0-4a9a-86aa-f7d9bb9b3298">Diagram toolbar</li><li data-uuid="ef6974b6-e252-418d-8d6c-5f1a1985ab4b"><strong>SysML v2 Simulation</strong> window</li><li data-uuid="0a110057-fd2a-43f8-b3a2-a52b90097ae9">Context menu of the simulated element</li></ul><h3 style="text-align: left;">Sending payloads during simulation</h3><p style="text-align: left;">During a simulation, payloads can be sent interactively using the<span> </span>smart manipulator of a transition symbol displayed in views.</p><p>To send a payload from a transition symbol</p><hr /><ol style="text-align: left;"><li data-uuid="895a31c9-e9f2-48d4-a500-2a2aa7cf4c13">Select the transition<span> </span>symbol that defines the payload you want to send.</li><li data-uuid="6c14a175-7c4c-475a-9b7a-17b88ca34c94">Click<span> </span><strong>Fire Transition</strong>. </li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c663d930-3dc0-4109-8220-bae07e575384"><ac:rich-text-body>If no element consumes a payload, it is automatically removed from the event pool.</ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=308314150 space=SYSML2SP version=1 -->
## PAGE 00007: (2026x Refresh1) Samples and libraries

- page_id: `308314150`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314150/2026x+Refresh1+Samples+and+libraries
- version_number: 1
- version_date: `2026-05-19T10:23:36.850+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

##### Samples

You can review the SysML v2 project samples provided with the installation, found at:

- <modeling tool installation directory>\samples\SysML v2\SysML v2 Simulation Overview.mdszip

##### Libraries

Each SysML v2 project is automatically loaded with the following used projects:

- Standard Libraries. It contains standard SysML v2 libraries.
- 3DS SysML Customization. It contains concepts designed for view creation and symbol style customization.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Samples</h3><p style="text-align: left;">You can review the SysML v2 project samples provided with the installation, found at:</p><ul style="text-align: left;"><li data-uuid="3b534de1-52a0-47ab-8228-870773d3c79e"><em>&lt;modeling tool installation directory&gt;\samples\SysML v2\SysML v2 Simulation Overview.mdszip</em></li></ul><h3 style="text-align: left;">Libraries</h3><p style="text-align: left;">Each SysML v2 project is automatically loaded with the following used projects:</p><ul style="text-align: left;"><li data-uuid="3d73af8a-9f6a-4afc-b376-0a94305086c4"><em>Standard Libraries.</em><span> </span>It contains standard SysML v2 libraries.</li><li data-uuid="70a874e7-d705-425d-a85e-387875955662"><em>3DS SysML Customization.</em><span> </span>It contains concepts designed for view creation and symbol style customization.</li></ul>
````

<!--NOMAGIC_PAGE id=309365934 space=SYSML2SP version=1 -->
## PAGE 00008: (2026x Refresh1) Simulating states

- page_id: `309365934`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365934/2026x+Refresh1+Simulating+states
- version_number: 1
- version_date: `2026-06-03T12:57:39.069+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

Simulating states allows you to execute and visualize the behaviors they define. Using the SysML v2 Simulation plugin, you can run SysML v2 states directly from the model and observe how states, transitions, triggers, and actions behave during execution.

Simulation enables you to:

- Validate system behavior early in the design process
- Verify state transitions and guard logic
- Observe how payloads and events propagate between elements
- Identify issues in behavioral models before implementation
- Demonstrate system behavior interactively

During simulation, active states are annotated, and transitions are executed according to the semantics defined in the model, allowing you to explore system dynamics in real time.

For more information, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Simulating states allows you to execute and visualize the behaviors they define. Using the SysML v2 Simulation plugin, you can run SysML v2 states directly from the model and observe how states, transitions, triggers, and actions behave during execution.</p><p data-start="1409" data-end="1439">Simulation enables you to:</p><ul data-start="1444" data-end="1715"><li data-section-id="i51o6b" data-start="1444" data-end="1498" data-uuid="2d36acf2-f4dd-4cc3-9a68-6d26cdc4a358">Validate system behavior early in the design process</li><li data-section-id="9et9kk" data-start="1501" data-end="1543" data-uuid="88e4cc05-28c7-4a63-8ad8-bf5a98fd01d0">Verify state transitions and guard logic</li><li data-section-id="1orl4vb" data-start="1546" data-end="1606" data-uuid="0e1d6af3-1ff4-4ac3-9a67-953751b82fb5">Observe how payloads and events propagate between elements</li><li data-section-id="80z2bb" data-start="1609" data-end="1669" data-uuid="23c9d399-e7d9-4043-b55a-843d232e9a13">Identify issues in behavioral models before implementation</li><li data-section-id="6z70tw" data-start="1672" data-end="1715" data-uuid="5764b3af-704f-429b-9577-8f4166243a73">Demonstrate system behavior interactively</li></ul><p style="text-align: left;">During simulation, active states are annotated, and transitions are executed according to the semantics defined in the model, allowing you to explore system dynamics in real time.</p><p style="text-align: left;">For more information, see the following topics:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="48540b48-a3eb-4863-9827-768a42255091" /></p>
````

<!--NOMAGIC_PAGE id=308314171 space=SYSML2SP version=2 -->
## PAGE 00009: (2026x Refresh1) Simulation information in views

- page_id: `308314171`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314171/2026x+Refresh1+Simulation+information+in+views
- version_number: 2
- version_date: `2026-05-28T14:19:44.924+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

During simulation, model views can display runtime information that reflects the current state of the simulated system. This allows observing variable values, execution states, and calculated data directly within views.

Simulation data visualization helps analyze system behavior without leaving the modeling environment. Runtime information can be displayed, updated, and manipulated while the simulation is running.

For more information, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">During simulation, model views can display runtime information that reflects the current state of the simulated system. This allows observing variable values, execution states, and calculated data directly within views.</p><p style="text-align: left;">Simulation data visualization helps analyze system behavior without leaving the modeling environment. Runtime information can be displayed, updated, and manipulated while the simulation is running.</p><p style="text-align: left;">For more information, see the following topics:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b5751640-0630-41cf-8356-848f2ffa0594" /></p>
````

<!--NOMAGIC_PAGE id=309365936 space=SYSML2SP version=1 -->
## PAGE 00010: (2026x Refresh1) Supported elements

- page_id: `309365936`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365936/2026x+Refresh1+Supported+elements
- version_number: 1
- version_date: `2026-06-03T12:57:39.141+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) Simulating states
- labels: []

### NORMALIZED CONTENT

The tables below list the SysML v2 state elements supported by the simulation engine.

In the **Executable** column, the following symbols mark whether elements are supported or not:

- [ATTACHMENT filename='supported.png'] - Supported elements
- [ATTACHMENT filename='partialy_supported.png'] - Partially supported elements
- [ATTACHMENT filename='unsupported.png'] - Unsupported elements

##### States

| SysML v2 Concept | Specification details | Executable |
| --- | --- | --- |
| State Def | State Def |  |
| stateDef :> stateDef |  |  |
| abstract stateDef |  |  |
| State Usage | State Usage |  |
| Exhibit State Usage |  |  |
| Composite State |  |  |
| Parallel State |  |  |
| stateUsage : stateDef |  |  |
| stateUsage :> stateUsage |  |  |
| stateUsage :>> stateUsage |  |  |
| ref stateUsage:StateDef |  |  |
| stateUsage references stateUsage |  |  |
| stateUsage_1 = stateUsage_2 |  |  |
| stateUsage : StateDef [1..*] ordered nonunique |  |  |
| Control Nodes | Start (Initial) Node |  |
| Done (Final) Node |  |  |
| Terminate Node |  |  |
| Entry Action | entry action assign x:=1; |  |
| entry action InitialAssign { *assign* controller.valve:=1; *send* new Terminate() via ButtonPort; } |  |  |
| entry action actionUsage:actionDef:; |  |  |
| entry actionUsage; |  |  |
| Do Action | do action assign x:=1; |  |
| do action InitialAssign { *assign* controller.valve:=1; *send* new Terminate() via ButtonPort; } |  |  |
| do action actionUsage:actionDef:; |  |  |
| do actionUsage; |  |  |
| Exit Action | exit action assign x:=1; |  |
| exit action InitialAssign { *assign* controller.valve:=1; *send* new Terminate() via ButtonPort; } |  |  |
| exit action actionUsage:actionDef:; |  |  |
| exit actionUsage; |  |  |
| Transitions | Transition |  |
| Self Transition |  |  |
| Completion Transition |  |  |
| Accepter(Transition)Accept Action | Accept Payload Trigger accept Start;accept Start via TimerPort; |  |
| Change Trigger accept when waterTank.level <= minlevel |  |  |
| Time Trigger (Absolute) accept at 5 [s]accept at operationTime |  |  |
| Time Trigger (Relative) accept after 2 [s]accept after simTime>10 |  |  |
| Guard(Transition) | if waterTank.level <= minlevel |  |
| if not waterTank.level <= minlevel |  |  |
| if payload.targetSpeed>0 |  |  |
| Effect(Transition) | do action assign x:=1; |  |
| do action InitialAssign { *assign* x:=1; *assign* y:=1; } |  |  |
| do action actionUsage:actionDef:; |  |  |
| do actionUsage; |  |  |
| do action assign speed :=payload.targetSpeed; |  |  |
| Conditional Succession | state def OperationalStates { entry action initial { out attribute isStarting : Boolean; } if not initial.isStarting then off; if initial.isStarting then starting; state off; state starting; state on; } |  |

##### Actions

#### NOTE: Limitation

Limitation

The usage is restricted to entry/do/exit actions or transition effects within a state.

| SysML v2 Concept | Specification details | Status |
| --- | --- | --- |
| Assignment action | assign x:=1; |  |
| assign x:= 1+y*54; |  |  |
| assign x:= telecom.antenna.mass; |  |  |
| assign telecom.antenna.mass:=2; |  |  |
| Send action | send new Start(); |  |
| send new Start() to timer; |  |  |
| send new Start() via outPort; |  |  |
| send new Start() via outPort totimer; |  |  |
| send new Start() to vehicle.engine |  |  |
| send new Start(limit=10, mass=129) |  |  |
| send itemUsage; |  |  |
| Accept action | accept Start |  |
| accept Start via inPort |  |  |
| accept after 2accept after simTime>10(Relative time trigger) |  |  |
| accept at 5accept at operationTime(Absolute time trigger) |  |  |
| accept when x>1(Change trigger) |  |  |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The tables below list the SysML v2 state elements supported by the simulation engine.</p><p style="text-align: left;">In the <strong>Executable</strong> column, the following symbols mark whether elements are supported or not:</p><ul><li data-uuid="7cb1bd3a-d732-402f-8f3f-4efad33d55c8"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image> - Supported elements</li><li data-uuid="bae86dee-597f-4f47-9519-816a76bed450"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image> - Partially supported elements</li><li data-uuid="4cc9b194-da82-465d-b977-b805de577469"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image> - Unsupported elements</li></ul><h3 style="text-align: left;">States</h3><table class="wrapped"><tbody class=""><tr class=""><th style="text-align: center;">SysML v2 Concept</th><th style="text-align: center;">Specification details</th><th style="text-align: center;">Executable</th></tr><tr class=""><td rowspan="3"><strong>State Def</strong></td><td>State Def</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>stateDef<span> </span><strong>:&gt;</strong><span> </span>stateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>abstract</strong><span> </span>stateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="11"><strong>State Usage</strong></td><td>State Usage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Exhibit State Usage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Composite State</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Parallel State</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>:</strong><span> </span>stateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>:&gt;</strong><span> </span>stateUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>:&gt;&gt;</strong><span> </span>stateUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>ref</strong><span> </span>stateUsage:StateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>references</strong><span> </span>stateUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>stateUsage_1<span> </span><strong>=</strong><span> </span>stateUsage_2</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>stateUsage : StateDef<span> </span><strong><span class="error">[1..*]</span><span> </span>ordered nonunique</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="3"><strong>Control Nodes</strong></td><td>Start (Initial) Node</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Done (Final) Node</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Terminate Node</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Entry Action</strong></td><td><strong>entry</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>entry</strong><span> </span><strong>action</strong><span> </span>InitialAssign {       *assign* controller.valve:=1;       *send* new Terminate() via ButtonPort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>entry</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>entry</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Do Action</strong></td><td><strong>do</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>InitialAssign {     *assign* controller.valve:=1;     *send* new Terminate() via ButtonPort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Exit Action</strong></td><td><strong>exit</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>exit</strong><span> </span><strong>action</strong><span> </span>InitialAssign {       *assign* controller.valve:=1;       *send* new Terminate() via ButtonPort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>exit</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>exit</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="3"><strong>Transitions</strong></td><td>Transition</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Self Transition</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Completion Transition</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Accepter</strong><br /><strong>(Transition)</strong><br /><strong>Accept Action</strong></td><td>Accept Payload Trigger<br /> <br /><em>accept Start;</em><br /><em>accept Start via TimerPort;</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Change Trigger<br /> <br /><em>accept when waterTank.level &lt;= minlevel</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Time Trigger (Absolute)<br /> <br /><em>accept at 5<span> </span><span class="error">[s]</span></em><br />accept at operationTime</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td>Time Trigger (Relative)<br /> <br /><em>accept after 2<span> </span><span class="error">[s]</span></em><br />accept after simTime&gt;10</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="3"><strong>Guard</strong><br /><strong>(Transition)</strong></td><td><strong>if</strong><span> </span><em>waterTank.level &lt;= minlevel</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><em><strong>if</strong><span> </span><strong>not</strong><span> </span>waterTank.level &lt;= minlevel</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>if</strong><span> </span><strong>payload</strong>.targetSpeed&gt;0</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="5"><strong>Effect</strong><br /><strong>(Transition)</strong></td><td><strong>do</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>InitialAssign {       *assign* x:=1;       *assign* y:=1; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>do action assign</strong><span> </span>speed<span> </span><strong>:=</strong><strong>payload</strong>.targetSpeed;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>Conditional Succession</strong></td><td><pre class="code-java">state def OperationalStates {
entry action initial { out attribute isStarting : <span class="code-object" style="color:var(--ds-text-accent-blue-bolder,#09326c);">Boolean</span>; }
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">if</span> not initial.isStarting then off;
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">if</span> initial.isStarting then starting;
state off;
state starting;
state on; }</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr></tbody></table><h3 style="text-align: left;">Actions</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3ead4032-c783-435c-96cd-a6f746fffb12"><ac:parameter ac:name="title">Limitation</ac:parameter><ac:rich-text-body>The usage is restricted to entry/do/exit actions or transition effects within a state.</ac:rich-text-body></ac:structured-macro><table class="wrapped relative-table" style="letter-spacing: 0.0px;width: 51.6164%;"><colgroup><col style="width: 18.7035%;" /><col style="width: 69.9256%;" /><col style="width: 11.3709%;" /></colgroup><tbody class=""><tr class=""><th style="text-align: center;">SysML v2 Concept</th><th style="text-align: center;">Specification details</th><th style="text-align: center;">Status</th></tr><tr class=""><td rowspan="4"><strong>Assignment action</strong></td><td><strong>assign</strong> x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>assign</strong> x:= 1+y*54;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>assign</strong> x:= telecom.antenna.mass;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>assign</strong> telecom.antenna.mass:=2;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="7"><strong>Send action</strong></td><td><strong>send</strong> <strong>new</strong> Start();</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>to</strong> timer;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>via</strong> outPort;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>via</strong> outPort <strong>to</strong>timer;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>to</strong> vehicle.engine</td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p><p><br /></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start(limit=10, mass=129)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> itemUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td rowspan="5"><strong>Accept action</strong></td><td><strong>accept</strong> Start</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> Start via inPort</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> <strong>after</strong> 2<br /><strong>accept</strong> <strong>after</strong> simTime&gt;10<br />(Relative time trigger)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> <strong>at</strong> 5<br /><strong>accept</strong> <strong>at</strong> operationTime<br />(Absolute time trigger)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> <strong>when</strong> x&gt;1<br />(Change trigger)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png"><ri:page ri:space-key="SYSML2SP" ri:content-title="(2026x Refresh1) Supported elements" /></ri:attachment></ac:image></p></div></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=308314154 space=SYSML2SP version=5 -->
## PAGE 00011: (2026x Refresh1) Supported structural and connectivity elements

- page_id: `308314154`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314154/2026x+Refresh1+Supported+structural+and+connectivity+elements
- version_number: 5
- version_date: `2026-06-22T14:55:41.611+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

This chapter defines thestructure concepts and connectivitysupported by the simulation engine. It outlines how SysML v2 architectural elements are transformed from static definitions into dynamic, executable models, focusing on data propagation, interface contracts, and runtime validation.

##### Supported elements

The simulation engine supports execution of the SysML v2 structure elements listed in the table below.

In the **Executable** column, the following symbols mark whether elements are supported or not:

- [ATTACHMENT filename='supported.png'] - Supported elements
- [ATTACHMENT filename='partialy_supported.png'] - Partially supported elements
- [ATTACHMENT filename='unsupported.png'] - Unsupported elements

| SysML v2 Concept | Specification details | Executable | Notes |
| --- | --- | --- | --- |
| Part Def | PartDef |  |  |
| Part Usage | Part Usage |  |  |
| partUsage : PartDef |  |  |  |
| partUsage :>> partUsage |  |  |  |
| partUsage :> partUsage |  |  |  |
| partUsage [1..*] ordered nonunique |  |  |  |
| ref partUsage : PartDef |  |  |  |
| partUsage_1 = partUsage_2 |  |  |  |
| Port Def | port def FuelingPort { attribute flowRate : Real; out fuelOut : Fuel; in fuelReturn : Fuel; } |  | The simulation does not check the direction of a directed Feature, meaning the payload is transferred without verifying if it complies with the port definition |
| Port Usage | portUsage : PortDef |  |  |
| portUsage : ~PortDef |  |  |  |
| Nested portsport p0 : PortDef { port p1 : PortDef; port p2 : PortDef; port p3 : PortDef;} |  |  |  |
| Connection Def | connection defConnectionDef1 {end part end1 : Part1;end part end2 : Part2;} |  |  |
| Connection Usage | connection connection1 :ConnectionDef1connect part1.port to part2.port; |  | All ConnectionUsage functions as delegation. |
| Connection (n-ary{}with 3 ends)connection connection1 : ConnectionDef1connect (part1,part2, part3); |  |  |  |
| Binding Connection | binding bind attributeUsage = attributeUsage; |  | Binding works only between attribute usages of primitive types. |
| Interface Def | interface def ControlToTankInterface { endp1 : ~ValvePort; endp2 :ValvePort; } |  | If a flow is specified between attribute usages of primitive types, the value flows according to the specification. |
| Interface Usage | interface : ControlToTankInterface connect controller.valvePort to waterTank.valvePort; |  | All InterfaceUsage functions as a delegation. |
| Flow | interface def ControlToTankInterface { endp1 : ~:ValvePort; endp2 :ValvePort; flow from p1.valve to p2.valve; } |  | Flows are supported only when specified in the Interface Definition |
| Attribute Def | attribute def Dimensions { attributelength :Real; attributewidth :Real; attributeheight :Real; } |  |  |
| Attribute Usage | attributeUsage:ScalarValues::Real |  | Only primitive type (Integer, Real, String, Boolean)Units are not supported. |
| attributeUsage : EnumerationDef |  |  |  |
| attributeUsage:mass |  | Units are not supported. |  |
| attributeUsage = expression |  |  |  |
| attributeUsage := expression |  |  |  |
| attribute:AttributeDef |  |  |  |
| attribute:AttributeDef [1..*] |  |  |  |
| Enumeration | enum def EnumerationDef1 { enum enum1; enum enum2; } |  |  |
| enum def EnumerationDef1 { enum = value1[unit1]; enum = value2[unit2]; } |  |  |  |

##### Connectivity

Connectivity in SysML v2 simulation moves beyond static structural definitions to specify how elementsdynamically interact during execution. The simulation engine enforces strict rules for data exchange, payload routing, and state synchronization to ensure model fidelity.

###### Interfaces

Interfaces serve as the formal contract between structural parts. They define the structured interaction points where data, energy, or material (modeled asflowUsages) cross system boundaries.

Key Applications:

- Component Decoupling Define how components interact (ports and flows) without being dependent on their internal state machine logic or private behaviors.
- Automated Data Propagation Ensure that a value change in a source component is automatically reflected in the connected target component.
- Payload Routing Facilitate the movement of discrete messages or physical items through defined ports.

[IMAGE alt='' src='']

###### Simulation of the *FlashingLightSystem* part usage.

#### PANEL: Syntax example

Syntax example

interfacedefButtonToTimerInterface{ 
endp1:ButtonPort; 
endp2:TimerInPort; 
flowofStartfromp1.starttop2.start; 
flowofStopfromp1.starttop2.start; 
}// Usage in a system contextinterface:ButtonToTimerInterfaceconnectbutton.buttonOuttotimer.timerIn;

Payloads can also be transferred using a connection usage.

###### Flows

The simulation engine executesflow usagesdefined within aninterface definition. The behavior of these flows follows specific operational semantics:

- Data Transfer (Non-Destructive) By default, transfers are executed as a copy operation. The source value remains intact while an identical instance is propagated to the target (isMove = false).
- Propagation Trigger (Push) Value transfer is reactive. It is initiated immediately upon an update to the source property (isPush = true).

[IMAGE alt='' src='']

###### Simulation of the *WaterTankSystem* part usage.

#### PANEL: Syntax example

Syntax example

interfacedefControlToTankInterface{ 
endp1: ~PortDefs::ValvePort;// Conjugated port (source) 
endp2:PortDefs::ValvePort;// Standard port (target) 
flowfromp1.valvetop2.valve;// flow 
} 
 
// Usage in a system contextinterface:ControlToTankInterfaceconnectcontroller.valvePorttowaterTank.valvePort;

###### Binding connections

Binding connectorsare utilized to map specific primitive FeatureValues directly to one another. This ensures that two features always share the same value throughout the simulation lifecycle.

#### PANEL: Syntax example

Syntax example

partdefVehicle{ 
attributemass;partengine{ 
attributeengineMass;}// Binding the engine's mass attribute to a local featurebindengine.engineMass=mass;

###### Runtime error handling

To ensure model integrity, the execution engine enforces strict rules during value assignments. Violations result in informative messages in the Simulation Console

| Condition | Engine Action | Console Info Message |
| --- | --- | --- |
| Bound Value | Assignment skipped | [Feature] := [Value] - failed because the value is bound. |
| Incompatible Type | Assignment skipped | [Feature] := [Value] - failed due to incompatible types. |
| Real to Integer | Value is trimmed at the "." | [Feature] := [Value] - value changed from Real to Integer. |

###### Visual Execution Tracing

The simulation provides real-time visual feedback to help users trace the path of payloads and data.

- Visited/Last Visited When a payload is transferred via a port usage, the entire path—from the source port, through the c onnection/interface, to the destination—is highlighted.
- Handling Ambiguity If a port has multiple outgoing connections/interfaces and the specific target is not pre-defined, the engine annotates all possible paths and connectors to signify potential interaction routes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">This chapter defines the<span> </span>structure concepts and connectivity<span> </span>supported by the simulation engine. It outlines how SysML v2 architectural elements are transformed from static definitions into dynamic, executable models, focusing on data propagation, interface contracts, and runtime validation. </p><h3 style="text-align: left;">Supported elements</h3><p style="text-align: left;">The simulation engine supports execution of the SysML v2 structure elements listed in the table below.</p><p style="text-align: left;">In the <strong>Executable</strong> column, the following symbols mark whether elements are supported or not:</p><ul><li style="text-align: left;" data-uuid="f22aecdb-8efc-4be9-9f08-07baecaaf569"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image> - Supported elements</li><li style="text-align: left;" data-uuid="91838cec-2477-405c-bc81-11bdc339d666"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image> - Partially supported elements</li><li style="text-align: left;" data-uuid="53e24025-7013-4575-81cc-6f1a57cc3f85"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image> - Unsupported elements</li></ul><table class="relative-table wrapped" style="width: 69.863%;"><colgroup><col style="width: 12.245%;" /><col style="width: 33.0459%;" /><col style="width: 8.79132%;" /><col style="width: 45.9189%;" /></colgroup><tbody><tr><th style="text-align: center;" scope="row">SysML v2 Concept</th><th style="text-align: center;" scope="col">Specification details</th><th style="text-align: center;" scope="col">Executable</th><th style="text-align: center;" scope="col">Notes</th></tr><tr><th scope="row">Part Def</th><td>PartDef</td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p><p><br /></p></div></td><td><br /></td></tr><tr><th rowspan="7" scope="rowgroup">Part Usage</th><td>Part Usage</td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p><p><br /></p></div></td><td><br /></td></tr><tr><td>partUsage<span> </span><strong>:</strong><span> </span>PartDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage :&gt;&gt; partUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage :&gt; partUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage<span> </span><strong><span class="error">[1..*]</span><span> </span>ordered nonunique</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td><strong>ref</strong><span> </span>partUsage : PartDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage_1<span> </span><strong>=</strong><span> </span>partUsage_2</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th scope="row">Port Def</th><td><pre class="code-java">port def FuelingPort {
attribute flowRate : Real;
out fuelOut : Fuel;
in fuelReturn : Fuel;
}</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p><p><br /></p></div></td><td>The simulation does not check the direction of a directed Feature, meaning the payload is transferred without verifying if it complies with the port definition</td></tr><tr><th rowspan="3" scope="rowgroup">Port Usage</th><td>portUsage : PortDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>portUsage : ~PortDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>Nested ports<pre class="code-java">port p0 : PortDef {
 port p1 : PortDef;
 port p2 : PortDef;
 port p3 : PortDef;} </pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th scope="row">Connection Def</th><td><em>connection def</em><br /><em>ConnectionDef1 {</em><br /><em>end part end1 : Part1;</em><br /><em>end part end2 : Part2;</em><br /><em>}</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th rowspan="2" scope="rowgroup">Connection Usage</th><td><em>connection connection1 :</em><em>ConnectionDef1</em><br /><em>connect part1.port to</em><span> </span><em>part2.port;</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td>All ConnectionUsage functions as delegation.</td></tr><tr><td>Connection (n-ary<em>{</em>}with 3 ends)<br /><em>connection connection1 :</em><span> </span><em>ConnectionDef1</em><br /><em>connect (part1,</em><em>part2, part3);</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th scope="row">Binding Connection</th><td><em>binding bind attributeUsage = attributeUsage;</em><br /> </td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Binding works only between attribute usages of primitive types.</td></tr><tr><th scope="row">Interface Def</th><td>interface def ControlToTankInterface { endp1 : ~ValvePort; endp2 :ValvePort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td>If a flow is specified between attribute usages of primitive types, the value flows according to the specification.</td></tr><tr><th scope="row">Interface Usage</th><td>interface : ControlToTankInterface connect controller.valvePort to waterTank.valvePort;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td>All InterfaceUsage functions as a delegation.</td></tr><tr><th scope="row">Flow</th><td>interface def ControlToTankInterface { endp1 : ~:ValvePort; endp2 :ValvePort; flow from p1.valve to p2.valve; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Flows are supported only when specified in the Interface Definition</td></tr><tr><th scope="row">Attribute Def</th><td>attribute def Dimensions { attributelength :Real; attributewidth :Real; attributeheight :Real; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th rowspan="7" scope="rowgroup">Attribute Usage</th><td>attributeUsage:ScalarValues::Real</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Only primitive type (Integer, Real, String, Boolean)<br />Units are not supported.</td></tr><tr><td>attributeUsage : EnumerationDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attributeUsage:mass</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Units are not supported.</td></tr><tr><td>attributeUsage = expression</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attributeUsage := expression</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attribute:AttributeDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attribute:AttributeDef<span> </span><span class="error">[1..*]</span></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th rowspan="2" scope="rowgroup">Enumeration</th><td><pre class="code-java"><span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> def EnumerationDef1
{
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> enum1;
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> enum2;
}
</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td><pre class="code-java"><span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> def EnumerationDef1
{
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> = value1[unit1];
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> = value2[unit2];
}
</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr></tbody></table><h3 style="text-align: left;">Connectivity</h3><p style="text-align: left;">Connectivity in SysML v2 simulation moves beyond static structural definitions to specify how elements<span> </span>dynamically interact during execution. The simulation engine enforces strict rules for data exchange, payload routing, and state synchronization to ensure model fidelity.</p><h4>Interfaces</h4><p style="text-align: left;">Interfaces serve as the formal contract between structural parts. They define the structured interaction points where data, energy, or material (modeled as<span> </span>flowUsages) cross system boundaries.</p><p style="text-align: left;">Key Applications:</p><ul style="text-align: left;"><li data-uuid="2e5d92b7-1ed2-42e4-a147-e5733c736655"><strong>Component Decoupling<br /></strong>Define<span> </span><em>how</em><span> </span>components interact (ports and flows) without being dependent on their internal state machine logic or private behaviors.</li><li data-uuid="e8526512-9a86-467a-ad39-13bcf054e1e1"><strong>Automated Data Propagation<br /></strong>Ensure that a value change in a source component is automatically reflected in the connected target component.</li><li data-uuid="634d2a10-4fc7-40d9-90cf-97d1f33290e9"><strong>Payload Routing<br /></strong>Facilitate the movement of discrete messages or physical items through defined ports.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="simulation_of_interconnection_view.png" /></ac:image></p><h6 style="text-align: center;">Simulation of the <em>FlashingLightSystem</em> part usage.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d7dd4c17-3106-4fec-ad62-9b8dce29e288"><ac:parameter ac:name="title">Syntax example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">ButtonToTimerInterface</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">ButtonPort</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">TimerInPort</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">flow</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">of</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">from</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">flow</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">of</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Stop</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">from</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    }<br /><br /></span><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Usage in a system context</span><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-chart-gray-bold,#8590a2);">  </span><span style="color:var(--ds-text,#000000);">:  </span><span style="color:var(--ds-text-accent-teal,#206a83);">ButtonToTimerInterface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">connect</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">button</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">buttonOut</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">timer</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">timerIn</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2ed2d87e-6ea2-444d-80d1-10e98cde3e92"><ac:rich-text-body>Payloads can also be transferred using a connection usage.</ac:rich-text-body></ac:structured-macro><h4>Flows</h4><p style="text-align: left;">The simulation engine executes<span> flow usages </span>defined within an<span> i</span>nterface definition. The behavior of these flows follows specific operational semantics:</p><ul style="text-align: left;"><li data-uuid="36ed582c-0d05-4c7f-b1d0-9411a1bae7a0"><strong>Data Transfer (Non-Destructive)<br /></strong>By default, transfers are executed as a<span> </span><strong>copy</strong><span> </span>operation. The source value remains intact while an identical instance is propagated to the target (isMove = false).</li><li data-uuid="eb18560c-1259-4ca9-8063-95d490e618d3"><strong>Propagation Trigger (Push)<br /></strong>Value transfer is reactive. It is initiated immediately upon an update to the source property (isPush = true).</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="simulation_of_part_usage.png" /></ac:image></p><h6 style="text-align: center;">Simulation of the <em>WaterTankSystem</em> part usage.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a486f46f-9ef6-4908-8bcf-158acafffe86"><ac:parameter ac:name="title">Syntax example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">ControlToTankInterface</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);"> : ~</span><span style="color:var(--ds-text-accent-teal,#206a83);">PortDefs::ValvePort</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Conjugated port (source)</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">PortDefs::ValvePort</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Standard port (target)</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">flow</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">from</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valve</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valve</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// flow</span><br /><span style="color:var(--ds-text,#000000);">    }<br /><br /><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Usage in a system context<br /></span></span><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text,#000000);"> :  </span><span style="color:var(--ds-text-accent-teal,#206a83);">ControlToTankInterface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">connect</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">controller</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valvePort</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">waterTank</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valvePort</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><h4 class="code-java">Binding connections</h4><p style="text-align: left;">Binding connectors<span> </span>are utilized to map specific primitive FeatureValues directly to one another. This ensures that two features always share the same value throughout the simulation lifecycle.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="07effaab-9da3-41ea-8c0a-4ad3030ce28a"><ac:parameter ac:name="title">Syntax example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Vehicle</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">                </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">mass</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">                part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engine</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">                        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engineMass;<span style="color:var(--ds-text,#000000);"><br />                }<br /><br /></span></span><span class="code-comment" style="color:var(--ds-background-accent-gray-bolder,#626f86);">                <span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Binding the engine's mass attribute to a local feature</span><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">                bind</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engine</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engineMass</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">mass</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><h4>Runtime error handling</h4><p style="text-align: left;">To ensure model integrity, the execution engine enforces strict rules during value assignments. Violations result in informative messages in the Simulation Console</p><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th scope="col">Condition</th><th scope="col">Engine Action</th><th scope="col">Console Info Message</th></tr><tr><td><strong>Bound Value</strong></td><td>Assignment skipped</td><td> <span class="error">[Feature]</span><span> </span>:=<span> </span><span class="error">[Value]</span><span> </span>- failed because the value is bound.</td></tr><tr><td><strong>Incompatible Type</strong></td><td>Assignment skipped</td><td> <span class="error">[Feature]</span><span> </span>:=<span> </span><span class="error">[Value]</span><span> </span>- failed due to incompatible types.</td></tr><tr><td><strong>Real to Integer</strong></td><td>Value is trimmed at the &quot;.&quot;</td><td> <span class="error">[Feature]</span><span> </span>:=<span> </span><span class="error">[Value]</span><span> </span>- value changed from Real to Integer.</td></tr></tbody></table><h4>Visual Execution Tracing</h4><p style="text-align: left;">The simulation provides real-time visual feedback to help users trace the path of payloads and data.</p><ul style="text-align: left;"><li data-uuid="b664ae19-f563-4ae0-88af-00eee24af2cb"><strong>Visited/Last Visited<br /></strong>When a payload is transferred via a<span> </span>port usage, the entire path—from the source port, through the<span> c</span>onnection/interface, to the destination—is highlighted.</li><li data-uuid="470bca55-7124-4029-ab8a-25c4385cc509"><strong>Handling Ambiguity<br /></strong>If a port has multiple outgoing connections/interfaces and the specific target is not pre-defined, the engine annotates<span> </span><em>all</em><span> </span>possible paths and connectors to signify potential interaction routes.</li></ul>
````

<!--NOMAGIC_PAGE id=308314162 space=SYSML2SP version=1 -->
## PAGE 00012: (2026x Refresh1) SyML v2 Simulation window

- page_id: `308314162`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314162/2026x+Refresh1+SyML+v2+Simulation+window
- version_number: 1
- version_date: `2026-05-19T10:23:37.080+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

The**SysML v2****Simulation** window is the primary interface for controlling and monitoring simulation execution. It provides access to runtime values, execution logs, charts, and data export functionality.

The window appears automatically when the simulation starts and remains active until the simulation is terminated.

[IMAGE alt='' src='']

###### SysML v2 Simulation window

The **SysML v2 Simulation** window contains the following panels that allow you to observe and manage simulation execution:

- Console Panel - Displays simulation messages and logs, including informational messages, warnings, and errors generated during simulation execution.
- Variables Panel - Displays runtime values of model variables. Values are updated dynamically as the simulation progresses.

##### Console panel

The**Console**panel displays messages generated during simulation execution. These messages provide information about simulation events, warnings, and errors that occur during the simulation. You can use the **Console** panel to monitor simulation behavior and diagnose issues in the model.

The following table describes the types of messages displayed in the **Console** panel.

| Message Type | Description |
| --- | --- |
| Information | Provide general information about simulation progress and execution events. |
| Warnings | Indicate potential modeling issues that may affect the simulation behavior. |
| Errors | Indicate problems that prevent the simulation from continuing correctly. |

The **Console** panel is useful for diagnosing simulation issues. When troubleshooting simulation problems, the console should be the first place to check for diagnostic information.

Use the panel to monitor execution logs to:

- Track simulation events
- Detect modeling errors
- Identify the requirement verification results
- Understand simulation behavior

##### Variables panel

The**Variables** panel displays runtime values of model elements during simulation. It allows you to observe how values change during the simulation.

Variables are organized in a hierarchical tree structure that reflects the structure of the simulated model. Each node represents a model element such as a part, attribute, reference, or port.

You can expand or collapse nodes to explore nested elements and monitor specific runtime values.

The **Variables** panel can display the following runtime elements:

- Part usages
- Attribute usages
- Reference usages
- Port usages
- Satisfy requirements

You can also use the Variables panel to open a [CONFLUENCE_PAGE title='(2026x Refresh1) Time Series Chart' space=''] and [CONFLUENCE_PAGE title='(2026x Refresh1) Exporting simulation data to CSV' space=''].

##### Simulation controls

The **SysML v2 Simulation** window toolbar provides the following controls for managing the simulation execution.

| Control | Icon | Description |
| --- | --- | --- |
| Start |  | Begins the simulation execution. |
| Pause |  | Temporarily suspends the simulation execution. |
| Resume |  | Continues the simulation execution after pausing. |
| Step |  | Executes a single simulation time step. |
| Terminate |  | Terminates the current simulation. |
| Speed Slider |  | Adjusts the simulation execution speed. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The<span> <strong>SysML v2 </strong></span><strong>Simulation</strong> window is the primary interface for controlling and monitoring simulation execution. It provides access to runtime values, execution logs, charts, and data export functionality.</p><p style="text-align: left;">The window appears automatically when the simulation starts and remains active until the simulation is terminated.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="sysml_v2_simulation_window.png"><ri:page ri:content-title="(2026x Refresh1) SyML v2 Simulation window" /></ri:attachment></ac:image></p><h6 style="text-align: center;">SysML v2 Simulation window</h6><p style="text-align: left;">The <strong>SysML v2 Simulation</strong> window contains the following panels that allow you to observe and manage simulation execution:</p><ul style="text-align: left;"><li data-uuid="50733de9-b896-459a-abea-3de6f521ebf9"><strong>Console Panel</strong><span> </span>- Displays simulation messages and logs, including informational messages, warnings, and errors generated during simulation execution.</li><li data-uuid="7ea510ab-1e47-42ee-8088-96d9c4c82601"><strong>Variables Panel</strong><span> </span>- Displays runtime values of model variables. Values are updated dynamically as the simulation progresses.</li></ul><h3>Console panel</h3><p style="text-align: left;">The<span> </span><strong>Console </strong>panel displays messages generated during simulation execution. These messages provide information about simulation events, warnings, and errors that occur during the simulation. You can use the <strong>Console</strong> panel to monitor simulation behavior and diagnose issues in the model.</p><p style="text-align: left;">The following table describes the types of messages displayed in the <strong>Console</strong> panel.</p><table class="wrapped"><tbody class=""><tr class=""><th style="text-align: center;">Message Type</th><th style="text-align: center;">Description</th></tr><tr class=""><td><strong>Information</strong></td><td>Provide general information about simulation progress and execution events.</td></tr><tr class=""><td><strong>Warnings</strong></td><td>Indicate potential modeling issues that may affect the simulation behavior.</td></tr><tr class=""><td><strong>Errors</strong></td><td>Indicate problems that prevent the simulation from continuing correctly.</td></tr></tbody></table><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="d0284f6f-2f40-47f5-b759-f5878dac59c2"><ac:rich-text-body><p>The <strong>Console</strong> panel is useful for diagnosing simulation issues. When troubleshooting simulation problems, the console should be the first place to check for diagnostic information.</p><p>Use the panel to monitor execution logs to:</p><ul><li data-uuid="b052858f-634f-4ab4-b817-0aacabfcc34d">Track simulation events</li><li data-uuid="5435d369-f9d2-4127-9dc1-8e194f757fd6">Detect modeling errors</li><li data-uuid="68f94f54-937b-4ec7-b8de-1957872e5753">Identify the requirement verification results</li><li data-uuid="aa62e112-6fd9-4052-a8fc-18752f161ce0">Understand simulation behavior</li></ul></ac:rich-text-body></ac:structured-macro><h3 style="text-align: left;">Variables panel</h3><p style="text-align: left;">The<span> </span><strong>Variables</strong> panel displays runtime values of model elements during simulation. It allows you to observe how values change during the simulation.</p><p style="text-align: left;">Variables are organized in a hierarchical tree structure that reflects the structure of the simulated model. Each node represents a model element such as a part, attribute, reference, or port.</p><p style="text-align: left;">You can expand or collapse nodes to explore nested elements and monitor specific runtime values.</p><p style="text-align: left;">The <strong>Variables</strong> panel can display the following runtime elements:</p><ul style="text-align: left;"><li data-uuid="3314e180-3de0-4e3f-bb5c-bc218178ce42">Part usages</li><li data-uuid="c1ee549b-58e4-461a-8250-c82c335e8e8d">Attribute usages</li><li data-uuid="da2791da-be9b-478f-b881-d0ade0389c89">Reference usages</li><li data-uuid="42ae10ea-ceee-4954-8dbf-9f25edb821b8">Port usages</li><li data-uuid="1760def3-8428-48b6-a6ce-6f7a24293bb5">Satisfy requirements</li></ul><p>You can also use the Variables panel to open a <ac:link><ri:page ri:content-title="(2026x Refresh1) Time Series Chart" /></ac:link> and <ac:link><ri:page ri:content-title="(2026x Refresh1) Exporting simulation data to CSV" /><ac:plain-text-link-body><![CDATA[export simulation data to CSV]]></ac:plain-text-link-body></ac:link>.</p><h3 style="text-align: left;">Simulation controls</h3><p style="text-align: left;">The <strong>SysML v2 Simulation</strong> window toolbar provides the following controls for managing the simulation execution.</p><table class="wrapped"><tbody class=""><tr class=""><th style="text-align: center;">Control</th><th style="text-align: center;">Icon</th><th style="text-align: center;">Description</th></tr><tr class=""><td><strong>Start</strong></td><td><div class="content-wrapper"><p style="text-align: center;"><strong><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="start.png"><ri:page ri:content-title="(2026x Refresh1) SyML v2 Simulation window" /></ri:attachment></ac:image><br /></strong></p></div></td><td>Begins the simulation execution.</td></tr><tr class=""><td><strong>Pause</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="pause.png"><ri:page ri:content-title="(2026x Refresh1) SyML v2 Simulation window" /></ri:attachment></ac:image><br /></strong></p></div></td><td>Temporarily suspends the simulation execution.</td></tr><tr class=""><td><strong>Resume</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image><ri:attachment ri:filename="resume.png"><ri:page ri:content-title="(2026x Refresh1) SyML v2 Simulation window" /></ri:attachment></ac:image><br /></strong></p></div></td><td>Continues the simulation execution after pausing.</td></tr><tr class=""><td><strong>Step</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image><ri:attachment ri:filename="step.png"><ri:page ri:content-title="(2026x Refresh1) SyML v2 Simulation window" /></ri:attachment></ac:image><br /></strong></p></div></td><td>Executes a single simulation time step.</td></tr><tr class=""><td><strong>Terminate</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image><ri:attachment ri:filename="terminate.png"><ri:page ri:content-title="(2026x Refresh1) SyML v2 Simulation window" /></ri:attachment></ac:image><br /></strong></p></div></td><td>Terminates the current simulation.</td></tr><tr class=""><td><strong>Speed Slider</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="speed.png"><ri:page ri:content-title="(2026x Refresh1) SyML v2 Simulation window" /></ri:attachment></ac:image><br /></strong></p></div></td><td>Adjusts the simulation execution speed.</td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=308314146 space=SYSML2SP version=4 -->
## PAGE 00013: (2026x Refresh1) SysML v2 Simulation Plugin Documentation

- page_id: `308314146`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314146/2026x+Refresh1+SysML+v2+Simulation+Plugin+Documentation
- version_number: 4
- version_date: `2026-06-30T09:54:50.087+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

lightgrey

The SysML v2 Simulation Plugin is in the Technology Preview phase. We do not recommend using it for long-term projects because there might be future changes affecting its functionality.

The SysML v2 Simulation Plugin enables execution of SysML v2 models to validate system behavior before implementation. It supports testing design logic, verifying requirements, and analyzing dynamic system interactions within a model-based systems engineering (MBSE) environment.

##### Why is Simulation Needed?

In today’s complex system environments, static models alone are not sufficient. Simulation provides:

- Early validation of system behavior
- Detection of design gaps and logical errors
- Improved requirement verification and traceability
- Greater confidence before committing to implementation

##### Business Benefits

Adopting simulation within MBSE delivers measurable value:

- Reduced development costs through early defect detection
- Shorter development cycles and faster time to market
- Improved product quality and compliance
- Lower project risk and better stakeholder alignment

The following topics explain how to install and use the SysML v2 Simulation Plugin:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3ea9e360-7173-4f87-b85d-2c3fb48cdac4"><ac:parameter ac:name="bgColor">lightgrey</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">The SysML v2 Simulation Plugin is in the Technology Preview phase. We do not recommend using it for long-term projects because there might be future changes affecting its functionality.</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">The SysML v2 Simulation Plugin enables execution of SysML v2 models to validate system behavior before implementation. It supports testing design logic, verifying requirements, and analyzing dynamic system interactions within a model-based systems engineering (MBSE) environment.</p><h3 style="text-align: left;">Why is Simulation Needed?</h3><p style="text-align: left;">In today’s complex system environments, static models alone are not sufficient. Simulation provides:</p><ul><li style="text-align: left;" data-uuid="293db28c-656d-43c1-a2c9-cb3e576fab0d">Early validation of system behavior</li><li data-uuid="9faf20da-b1ce-42a8-9d00-6f3c82deaadd">Detection of design gaps and logical errors</li><li data-uuid="4ad43ae4-06f5-45ed-9cca-b4258bfa4fe8">Improved requirement verification and traceability</li><li data-uuid="2932948a-4c07-46ad-8d9c-00f4a8d6488d">Greater confidence before committing to implementation</li></ul><h3 style="text-align: left;">Business Benefits</h3><p style="text-align: left;">Adopting simulation within MBSE delivers measurable value:</p><ul style="text-align: left;"><li data-uuid="aeeddda1-7eb5-4559-97dc-8a8e70ba03fc">Reduced development costs through early defect detection</li><li data-uuid="e92210aa-b2e9-4d3b-9c9a-98395fc1bc77">Shorter development cycles and faster time to market</li><li data-uuid="17f4a7e5-090e-4b3c-b1e2-84e0134d2034">Improved product quality and compliance</li><li data-uuid="2104fcff-9945-42be-a6e5-e86287e934d9">Lower project risk and better stakeholder alignment</li></ul><p style="text-align: left;">The following topics explain how to install and use the SysML v2 Simulation Plugin:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="0ca80646-7181-4acd-a5e5-6af2f4a2224c" /></p>
````

<!--NOMAGIC_PAGE id=308314173 space=SYSML2SP version=3 -->
## PAGE 00014: (2026x Refresh1) Time Series Chart

- page_id: `308314173`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314173/2026x+Refresh1+Time+Series+Chart
- version_number: 3
- version_date: `2026-06-22T15:11:03.604+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide > (2026x Refresh1) SyML v2 Simulation window
- labels: []

### NORMALIZED CONTENT

The **Variables** panel allows you to visualize variable values over time using a Time Series Chart. The chart displays time-series data for numerical variables during the simulation.

[IMAGE alt='' src='']

###### Time Series Chart

##### Opening Time Series Chart

To open a Time Series Chart

1. In the **Variables** panel, select the check boxes for one or more numerical attributes or references.
2. In the panel toolbar, click [IMAGE alt='' src='']. 
[IMAGE alt='' src='']

The chart window opens and displays attribute values starting from the moment it is opened.You can open multiple Time Series Charts simultaneously.

##### Adding variables to an open chart

To add additional variables to an existing chart:

1. Select one or more **numerical attributes** or **references** using checkboxes or directly from the variable tree.
2. Right-click the selected variables.
3. Select **Insert to Chart**. 
[IMAGE alt='' src='']

The selected variable is added to the chart visualization.

##### Chart display options

You can choose from several visualization options in an open Time Series Chart for better readability and easier analysis of the chart.

To configure Time Series Chart display options

- In an open Time Series Chart, click [ATTACHMENT filename='chart_settings.png'] and select one or several of the following options:
  - **Interpolation (Linear)** - to display the chart as either a curvilinear or linear line.
  - **Show Data Points** - to show or hide data points on the chart lines.
  - **Show Values** - to show or hide numeric values in the chart.

##### Exporting chart data

You can export the data of an open Time Series Chart to multiple formats for external use.Available export formats are:PNG,JPEG,SVG,CSV, andXLS.

Exported chart data can be useful for data analysis, reports, or documetnation.

To export Time Series Chart data

1. In an open Time Series Chart, click [IMAGE alt='' src=''] and select one of the following options:
  - Download PNG image
  - Download JPEG image
  - Download SVG vector image
  - Download CSV
  - Download XLS
2. In an open window, select the directory where you want to save the file.
3. Optionally, change the file name.
4. Click the Save button.

The file is downloaded to your selected location.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The <strong>Variables</strong> panel allows you to visualize variable values over time using a Time Series Chart. The c</span><span style="color:var(--ds-text,#172b4d);">hart displays time-series data for numerical variables during the simulation.</span></p><p style="text-align: left;"><ac:image ac:align="center"><ri:attachment ri:filename="time_series_chart_window.png" /></ac:image></p><h6 style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">Time Series Chart</span></h6><h3 style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Opening Time Series Chart</span></h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To open a Time Series Chart</span></p><hr /><ol style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="0a66947c-ca5f-456d-a8e7-7cd1193f36fa"><span style="color:var(--ds-text,#172b4d);">In the <strong>Variables</strong> panel, select the check boxes for one or more numerical attributes or references.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="ec639d9a-d7e7-4c21-93ae-b7f22992a72e"><span style="color:var(--ds-text,#172b4d);">In the panel toolbar, click <ac:image><ri:attachment ri:filename="time_series_chart.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="opening_time_series_chart.png" /></ac:image></span></li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The chart window opens and displays attribute values starting from the moment it is opened. </span><span style="color:var(--ds-text,#172b4d);">You can open multiple Time Series Charts simultaneously.</span></p><h3 style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Adding variables to an open chart</span></h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To add additional variables to an existing chart:</span></p><ol style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="561739e9-f987-4a0c-a75a-201d966cc326"><span style="color:var(--ds-text,#172b4d);">Select one or more <strong>numerical attributes</strong> or <strong>references</strong> using checkboxes or directly from the variable tree.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="f76cc750-6c2a-4eb4-88f5-64b4563689b8"><span style="color:var(--ds-text,#172b4d);">Right-click the selected variables.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="70539c81-1089-4c5f-82ad-7f053e1ed242"><span style="color:var(--ds-text,#172b4d);">Select <strong>Insert to Chart</strong>.<br /><ac:image><ri:attachment ri:filename="inserting_variables_to_chart.png" /></ac:image><br /></span></li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The selected variable is added to the chart visualization.</span></p><h3 style="text-align: left;">Chart display options</h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">You can choose from several visualization options in an open Time Series Chart for better readability and easier analysis of the chart.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To configure Time Series Chart display options</span></p><hr /><ul><li data-uuid="5244d5d7-6428-4625-b4e9-5f2fea82e25b">In an open Time Series Chart, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="chart_settings.png" /></ac:image> and select one or several of the following options:<ul><li data-uuid="8197fe1f-9bf1-468d-b24e-4e1f004103e1"><span style="color:var(--ds-text,#172b4d);"><strong>Interpolation (Linear)</strong> - to display the chart as either a curvilinear or linear line.</span></li><li data-uuid="4c379191-e8b6-44a7-8ce9-7e6011f17284"><span style="color:var(--ds-text,#172b4d);"><strong>Show Data Points</strong> - to show or hide data points on the chart lines.</span></li><li data-uuid="6298fb23-d84b-426b-ae4c-5bfb5534e8fd"><span style="color:var(--ds-text,#172b4d);"><strong>Show Values</strong> - to show or hide numeric values in the chart.</span></li></ul></li></ul><h3><span style="color:var(--ds-text,#172b4d);">Exporting chart data</span></h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">You can export the data of an open Time Series Chart to multiple formats for external use. </span><span style="color:var(--ds-text,#172b4d);">Available export formats are: </span><span style="color:var(--ds-text,#172b4d);">PNG, </span><span style="color:var(--ds-text,#172b4d);">JPEG, </span><span style="color:var(--ds-text,#172b4d);">SVG, </span><span style="color:var(--ds-text,#172b4d);">CSV, and </span><span style="color:var(--ds-text,#172b4d);">XLS.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Exported chart data can be useful for data analysis, reports, or documetnation.</span></p><p style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">To export Time Series Chart data</span></p><hr /><ol><li style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">In an open Time Series Chart, click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="export_chart_data.png" /></ac:image> and select one of the following options:</span><ul><li style="text-align: left;"><strong>Download PNG image</strong></li><li style="text-align: left;font-weight: bold;" data-uuid="c81ae603-6bbe-472f-9643-67590745c8bf"><strong>Download JPEG image</strong></li><li style="text-align: left;" data-uuid="f16fdaa2-5b33-4613-b738-66aa186fde71"><strong>Download SVG vector image</strong></li><li style="text-align: left;" data-uuid="74c76e52-3140-451b-aef0-bcad0bb4291c"><strong>Download CSV</strong></li><li style="text-align: left;" data-uuid="993049a0-7ae4-4bba-a395-76b890677b27"><strong>Download XLS</strong></li></ul></li><li style="text-align: left;" data-uuid="a8c4b0e6-0973-4b84-84bc-58d00416a006">In an open window, select the directory where you want to save the file.</li><li style="text-align: left;" data-uuid="210b088c-b8d6-4bd0-848e-43a2c436b3f8">Optionally, change the file name.</li><li style="text-align: left;" data-uuid="965a630c-cf6b-4451-a419-2987a14da1f0">Click the <strong>Save</strong> button.</li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The file is downloaded to your selected location.</span></p>
````

<!--NOMAGIC_PAGE id=308314152 space=SYSML2SP version=1 -->
## PAGE 00015: (2026x Refresh1) User guide

- page_id: `308314152`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/308314152/2026x+Refresh1+User+guide
- version_number: 1
- version_date: `2026-05-19T10:23:36.882+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

The SysML v2 Simulation Plugin user guide explains how to execute SysML v2 models to validate system behavior, verify requirements, analyze dynamic scenarios, and identify design issues early in the MBSE process.

#### NOTE: SysML v2 Simulation Plugin - Technology Preview

SysML v2 Simulation Plugin - Technology Preview

The SysML v2 Simulation Plugin is provided as a technology preview. We do not recommend using it to create any long-term projects because there might be future changes affecting its functionality.

For information about generic SysML v2 modeling features, including using the textual notation, see the [SysML v2 Plugin documentation](https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&version=latest).

To learn more, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The SysML v2 Simulation Plugin user guide explains how to execute SysML v2 models to validate system behavior, verify requirements, analyze dynamic scenarios, and identify design issues early in the MBSE process.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7269f27a-a013-4360-a1a5-0dd498f6ef22"><ac:parameter ac:name="title">SysML v2 Simulation Plugin - Technology Preview</ac:parameter><ac:rich-text-body>The SysML v2 Simulation Plugin is provided as a technology preview. We do not recommend using it to create any long-term projects because there might be future changes affecting its functionality.</ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f0f8e034-bdef-4bad-9db3-36961de8057f"><ac:rich-text-body><p>For information about generic SysML v2 modeling features, including using the textual notation, see the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=latest">SysML v2 Plugin documentation</a>.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"> To learn more, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9b84f3dd-7313-4b7a-bbd3-d1b7ab506897" /></p>
````

<!--NOMAGIC_PAGE id=314180721 space=SYSML2SP version=6 -->
## PAGE 00016: (2026x Refresh1) Using expressions

- page_id: `314180721`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/314180721/2026x+Refresh1+Using+expressions
- version_number: 6
- version_date: `2026-06-19T14:49:10.362+02:00`
- ancestors: Versions of SysML v2 Simulation Plugin Documentation > (2026x Refresh1) SysML v2 Simulation Plugin Documentation > (2026x Refresh1) User guide
- labels: []

### NORMALIZED CONTENT

The SysML v2 Simulation plugin supports the evaluation of feature values defined by expressions. Expressions may calculate values using operators (for example, arithmetic or comparison operations) or derive values by referencing other features in the model. Expressions can be applied to attributes and references to define computed or derived values within a model.

During simulation, expressions are evaluated automatically. When a runtime value is changed, all dependent expressions are recalculated.

If you initiate the simulation from a model view, the results of expression evaluation are displayed on element shapes to provide immediate runtime feedback. Evaluated values of attributes and references are displayed in blue and are updated dynamically as the simulation progresses. For more information, see [CONFLUENCE_PAGE title='(2026x Refresh1) Simulation information in views' space=''].

##### Supported value types

Expressions operate on:

- Primitive types (Integer, Real, Boolean, etc.)
- Enumeration values
- Feature references
- Collections (arrays/lists)

##### Supported operators

| Type | Operators |
| --- | --- |
| Arithmetic | + |
| - |  |
| * |  |
| / |  |
| Comparison | > |
| < |  |
| >= |  |
| <= |  |
| Equality | == |
| != |  |

##### Collections and aggregation functions

In the simulation context, expressions support collections (arrays/lists), which contain multiple values of a compatible type. Each element in a collection is evaluated individually. If any element in a collection is incompatible, the entire assignment is rejected. If values are converted during evaluation, those elements are also treated as incompatible.

You can use collections with the **sum(<list>)** function, which computes the total of all numeric elements in a collection and returns a single numeric value. This function can be used in any expression context that expects a numeric result.

##### Accessing nested features

Expressions support nested feature access using dot notation. This mechanism is available wherever feature values are used in simulation, including expressions, actions, event conditions, and message targets. It allows you to navigate structured model elements and access deeply nested values in complex systems.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The SysML v2 Simulation plugin supports the evaluation of feature values defined by expressions. Expressions may calculate values using operators (for example, arithmetic or comparison operations) or derive values by referencing other features in the model. Expressions can be applied to attributes and references to define computed or derived values within a model.</p><p>During simulation, expressions are evaluated automatically. When a runtime value is changed, all dependent expressions are recalculated.</p><p>If you initiate the simulation from a model view, the results of expression evaluation are displayed on element shapes to provide immediate runtime feedback. Evaluated values of attributes and references are displayed in blue and are updated dynamically as the simulation progresses. For more information, see <ac:link><ri:page ri:content-title="(2026x Refresh1) Simulation information in views" /><ac:plain-text-link-body><![CDATA[Simulation information in views]]></ac:plain-text-link-body></ac:link>.</p><h3>Supported value types</h3><p>Expressions operate on:</p><ul><li data-uuid="d7ef360f-680c-4b3b-9795-03c05052db50">Primitive types (Integer, Real, Boolean, etc.)</li><li data-uuid="46d1ebed-7f3f-4a4a-9cbe-fcd5416d83e4">Enumeration values</li><li data-uuid="b2e96c27-6df1-4bff-8449-4a0bdf682821">Feature references</li><li data-uuid="85f6f1aa-901d-404c-9a98-7710c9010bbb">Collections (arrays/lists)</li></ul><h3>Supported operators</h3><table class="relative-table wrapped" style="width: 23.8904%;"><colgroup><col style="width: 45.0591%;" /><col style="width: 54.9445%;" /></colgroup><thead class=""><tr class=""><th>Type</th><th>Operators</th></tr></thead><tbody class=""><tr class=""><td rowspan="4">Arithmetic</td><td><code>+</code></td></tr><tr><td><code>-</code></td></tr><tr><td>*</td></tr><tr><td>/</td></tr><tr class=""><td rowspan="4">Comparison<br /><br /><br /><br /></td><td><code>&gt;</code></td></tr><tr><td>&lt;</td></tr><tr><td>&gt;=</td></tr><tr><td>&lt;=</td></tr><tr class=""><td rowspan="2">Equality</td><td><code>==</code></td></tr><tr><td>!=</td></tr></tbody></table><h3>Collections and aggregation functions</h3><p>In the simulation context, expressions support collections (arrays/lists), which contain multiple values of a compatible type. Each element in a collection is evaluated individually. If any element in a collection is incompatible, the entire assignment is rejected. If values are converted during evaluation, those elements are also treated as incompatible.</p><p>You can use collections with the <strong>sum(&lt;list&gt;)</strong> function, which computes the total of all numeric elements in a collection and returns a single numeric value. This function can be used in any expression context that expects a numeric result.</p><h3>Accessing nested features</h3><p>Expressions support nested feature access using dot notation. This mechanism is available wherever feature values are used in simulation, including expressions, actions, event conditions, and message targets. It allows you to navigate structured model elements and access deeply nested values in complex systems.</p>
````

<!--NOMAGIC_PAGE id=306283326 space=SYSML2SP version=20 -->
## PAGE 00017: Displaying simulation information

- page_id: `306283326`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/306283326/Displaying+simulation+information
- version_number: 20
- version_date: `2026-07-10T15:01:59.387+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide > Simulation information in views
- labels: []

### NORMALIZED CONTENT

During simulation, views can display runtime information associated with model elements. This information is dynamically updated during the simulation and reflects the current state of the simulated system. Observing runtime values, execution indicators, and requirement statuses directly on views makes it easier to understand how the system evolves over time.

##### Simulation annotations in views

During simulation, behavior concepts (e.g., states) or ports and connections (e.g., payloads flowing through connections) displayed in views are annotated to indicate the execution flow.

Simulation annotations mark symbols as:

- Active (default color [IMAGE alt='' src='']) - the symbol that is currently being executed during the simulation.
- Visited (default color [IMAGE alt='' src='']) - the symbols that have already been executed.
- Last Visited (default color [IMAGE alt='' src='']) - the symbol that has been executed most recently.

[IMAGE alt='' src='']

###### Annotations of the flashlight system simulation

###### Configuring annotation colors

To change the colors used for simulation annotations

1. In the main menu, select Options > Project .
2. In the Project Options dialog, select the Simulation option group. [ATTACHMENT filename='simulation_project_options.png']
3. On the right side of the dialog, select the value cell you want to change and click [ATTACHMENT filename='edit_value.png'] .
4. In the open dialog, select a new color and click OK .
5. Click OK to close the Project Options dialog.

##### Displaying runtime values

In views, runtime values are displayed in blue. During simulation, these runtime values replace the default values and are displayed next to:

- Attributes
- References
- Satisfy requirements

Attributes or references that contain expressions may display calculated values during simulation. These values appear directly in the view near the element names and update continuously as the simulation progresses.

When a simulation is running, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability during execution.

You can also [CONFLUENCE_PAGE title='Manipulating simulation information' space=''] directly in views and change simulation results in real-time.

[IMAGE alt='' src='']

###### A sample view displaying runtime values during model simulation.

###### Supported data types

Runtime values can be displayed in views only for the following data types:

- Primitive:
  - Integer
  - Real
  - Boolean
  - String
- Enumeration

If a property has a different data type, its runtime value is not displayed directly in the view.

#### TIP: Resizing shapes to fit runtime values

Resizing shapes to fit runtime values

If a runtime value does not fit inside a shape and is cut off, resize the shape as described below:

1. Select the shape you want to resize.
2. Do one of the following:
  - Click [ATTACHMENT filename='resize_icon.png'] on the shape.
  - Click [IMAGE alt='' src=''] in the view toolbar.

###### Automated requirement verification

Model simulation supports automated requirement verification. Runtime values on part, attribute, and reference shapes are highlighted in green or red to indicate whether the related requirement is satisfied. The verification result on the satisfy requirement shape is also highlighted in green or red, respectively.

In addition, a tooltip containing the text of the unsatisfied requirement appears when you hover the mouse pointer over a failing part, attribute, reference, or satisfy requirement shape.

[IMAGE alt='' src='']

###### View fragments showing failing attributes and the related satisfy requirement.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">During simulation, views can display runtime information associated with model elements. This information is dynamically updated during the simulation and reflects the current state of the simulated system. Observing runtime values, execution indicators, and requirement statuses directly on views makes it easier to understand how the system evolves over time.</p><h3 style="text-align: left;">Simulation annotations in views</h3><p style="text-align: left;">During simulation, behavior concepts (e.g., states) or ports and connections (e.g., payloads flowing through connections) displayed in views are annotated to indicate the execution flow.</p><p style="text-align: left;">Simulation annotations mark symbols as:</p><ul style="text-align: left;"><li data-uuid="6e5843ad-360d-4129-80ad-66a709c9ea37"><strong>Active</strong><span> (default color <ac:image><ri:attachment ri:filename="active_color.png" /></ac:image>) </span>- the symbol that is currently being executed during the simulation.</li><li data-uuid="bc219784-e5c9-4616-b7b4-1021a3c2f002"><strong>Visited</strong><span> (default color <ac:image><ri:attachment ri:filename="visited_color.png" /></ac:image>) </span>- the symbols that have already been executed.</li><li data-uuid="44b8cf90-8876-42e1-8e39-1bd3a739eec6"><strong>Last Visited</strong><span> (default color <ac:image><ri:attachment ri:filename="last_visited_color.png" /></ac:image>)</span>- the symbol that has been executed most recently.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="simulation_annotations.png" /></ac:image></p><h6 style="text-align: center;">Annotations of the flashlight system simulation</h6><p><br /></p><h4>Configuring annotation colors</h4><p>To change the colors used for simulation annotations</p><hr /><ol><li data-uuid="b576d7f7-6332-42b9-8cf8-934ba9a80522">In the main menu, select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li data-uuid="d6abdf92-d45c-487d-81d3-6758d0fc5a66">In the <strong>Project Options</strong> dialog, select the <strong>Simulation</strong> option group.<br /><ac:image><ri:attachment ri:filename="simulation_project_options.png" /></ac:image></li><li data-uuid="47028fe1-48fd-4519-8249-23e0d1ed57e5">On the right side of the dialog, select the value cell you want to change and click <ac:image><ri:attachment ri:filename="edit_value.png" /></ac:image>.</li><li data-uuid="0260722c-0926-4e77-bb04-bb3725fd58e5">In the open dialog, select a new color and click <strong>OK</strong>.</li><li data-uuid="038b1e53-3a2b-4372-85e9-47ce740fc3ab">Click <strong>OK</strong> to close the <strong>Project Options</strong> dialog.</li></ol><h3 style="text-align: left;">Displaying runtime values</h3><p>In views, runtime values are displayed in blue. During simulation, these runtime values replace the default values and are displayed next to:</p><ul><li data-uuid="4c764c77-655d-4b12-90da-a6d0e43d70f2">Attributes</li><li data-uuid="7a6375fc-fe9c-49a1-9208-a39703fd0450">References</li><li data-uuid="0c557862-e97b-4f33-830c-11d2bdb179ce">Satisfy requirements</li></ul><p>Attributes or references that contain expressions may display calculated values during simulation. These values appear directly in the view near the element names and update continuously as the simulation progresses.</p><p>When a simulation is running, views do not display types; only the current runtime values are shown. This reduces visual complexity and improves view readability during execution.</p><p>You can also <ac:link><ri:page ri:content-title="Manipulating simulation information" /><ac:plain-text-link-body><![CDATA[modify runtime values]]></ac:plain-text-link-body></ac:link> directly in views and change simulation results in real-time.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="runtime_values_in_views.png" /></ac:image></p><h6 style="text-align: center;">A sample view displaying runtime values during model simulation.</h6><h4 style="text-align: left;">Supported data types</h4><p style="text-align: left;">Runtime values can be displayed in views only for the following data types:</p><ul style="text-align: left;"><li data-uuid="ead3d827-a142-4a7e-b80e-a02fdcb92de0">Primitive:<ul><li>Integer</li><li>Real</li><li>Boolean</li><li>String</li></ul></li><li data-uuid="2fcf634a-5a42-4f66-be8d-a75dbf35d594">Enumeration</li></ul><p style="text-align: left;">If a property has a different data type, its runtime value is not displayed directly in the view.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="65dd4694-e5f8-465c-9e2f-355fcad37925"><ac:parameter ac:name="title">Resizing shapes to fit runtime values</ac:parameter><ac:rich-text-body><p>If a runtime value does not fit inside a shape and is cut off, resize the shape as described below:</p><ol><li data-uuid="b98a04b2-4802-4f66-b891-c2d1de526e90">Select the shape you want to resize.</li><li data-uuid="c4a443aa-1168-4817-bdad-845028f0ba22">Do one of the following:<ul><li data-uuid="1b67b46f-c3e2-40a7-b278-855a4b259526">Click <ac:image><ri:attachment ri:filename="resize_icon.png" /></ac:image> on the shape.</li><li data-uuid="48e8d067-405c-4c21-bf16-456895c3439e">Click<span> <ac:image ac:thumbnail="true" ac:height="10"><ri:attachment ri:filename="resize_icon_in_toolbar.png" /></ac:image></span><span> </span>in the view toolbar.</li></ul></li></ol></ac:rich-text-body></ac:structured-macro><h4>Automated requirement verification</h4><p>Model simulation supports automated requirement verification. Runtime values on part, attribute, and reference shapes are highlighted in green or red to indicate whether the related requirement is satisfied. The verification result on the satisfy requirement shape is also highlighted in green or red, respectively.</p><p>In addition, a tooltip containing the text of the unsatisfied requirement appears when you hover the mouse pointer over a failing part, attribute, reference, or satisfy requirement shape.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="requirement_verification.png" /></ac:image></p><h6 style="text-align: center;">View fragments showing failing attributes and the related satisfy requirement.</h6>
````

<!--NOMAGIC_PAGE id=304001312 space=SYSML2SP version=3 -->
## PAGE 00018: Exporting simulation data to CSV

- page_id: `304001312`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/304001312/Exporting+simulation+data+to+CSV
- version_number: 3
- version_date: `2026-05-14T13:16:14.779+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide > SyML v2 Simulation window
- labels: []

### NORMALIZED CONTENT

You can export the simulation data from the **Variables** panel for further analysis outside the modeling tool environment.Exported data is saved in CSV format, which can be opened using spreadsheet or data analysis tools.

Only the variables with the following data types are exported:

- Primitive data types
  - Integer
  - Real
  - String
  - Boolean
- Enumeration values

To export the simulation data

1. In the **Variables** panel, select the variables you want to export. If no variables are selected, all variables of the supported data types are exported.If a part usage or port usage is selected, all nested primitive feature values and enumeration values are exported recursively.
2. In the panel toolbar, click [ATTACHMENT filename='export_to_csv.png'] .
3. In the open dialog, select the directory where you want to save the file.
4. Click the **Save** button.

The CSV file with the recorded values is downloaded to your selected location.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">You can export the simulation data from the <strong>Variables</strong> panel for further analysis outside the modeling tool environment. </span><span style="color:var(--ds-text,#172b4d);">Exported data is saved in CSV format, which can be opened using spreadsheet or data analysis tools.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Only the variables with the following data types are exported:</span></p><ul style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="a2d8641a-aeed-4b82-8b4e-33ea6b1c55bd"><span style="color:var(--ds-text,#172b4d);">Primitive data types</span><ul><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">Integer</span></li><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">Real</span></li><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">String</span></li><li style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">Boolean</span></li></ul></li><li style="color:var(--ds-text,#172b4d);" data-uuid="70657c65-28e2-421b-90f0-d6338e8c7e90"><span style="color:var(--ds-text,#172b4d);">Enumeration values</span></li></ul><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To export the simulation data</span></p><hr /><ol style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="0fc6db49-b400-4e6f-9fe2-bf6732c32a20"><span style="color:var(--ds-text,#172b4d);">In the <strong>Variables</strong> panel, select the variables you want to export.<br /></span><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="a7fb7938-43f0-40ee-ab02-48090540ce61"><ac:rich-text-body><ul><li>If no variables are selected, all variables of the supported data types are exported.</li><li><span style="color:var(--ds-text,#172b4d);">If a part usage or port usage is selected, all nested primitive feature values and enumeration values are exported recursively.</span></li></ul></ac:rich-text-body></ac:structured-macro></li><li style="color:var(--ds-text,#172b4d);" data-uuid="256cf81e-85f7-4ac8-b503-b8decae26e4d">In the panel toolbar, click <ac:image><ri:attachment ri:filename="export_to_csv.png" /></ac:image>.</li><li style="color:var(--ds-text,#172b4d);" data-uuid="85bc4fac-7b81-4fda-9358-2147a61bef1c"><span style="color:var(--ds-text,#172b4d);">In the open dialog, select the directory where you want to save the file.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="17ef7cb1-b8a5-4710-82ac-fd4fe514721a"><span style="color:var(--ds-text,#172b4d);">Click the <strong>Save</strong> button.</span></li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The CSV file with the recorded values is downloaded to your selected location.</span></p>
````

<!--NOMAGIC_PAGE id=306283329 space=SYSML2SP version=9 -->
## PAGE 00019: Manipulating simulation information

- page_id: `306283329`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/306283329/Manipulating+simulation+information
- version_number: 9
- version_date: `2026-06-22T13:05:59.137+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide > Simulation information in views
- labels: []

### NORMALIZED CONTENT

You can interact with the simulation data displayed in views to improve understanding and analysis of system behavior during execution. Simulation views allow inspection and modification of runtime information without interrupting the simulation.Manipulating simulation data provides a practical way to observe how a model responds to changing conditions, supporting both debugging and behavioral analysis.

##### Changing Runtime Values

During simulation, initial runtime values (indicated by “:=”) can be changed directly in the views. This allows you to observe how the system’s behavior responds to changing values while the simulation is running.

To change runtime values on element shapes

1. During model simulation, select a part, attribute, or reference shape in a view.
2. Select the initial runtime value (indicated by ":=") you want to change.
3. Do one of the following depending on the value type:
  - For a numerical runtime value, type a new value. [ATTACHMENT filename='changing_numerical_value.png']
  - For an enumeration runtime value, click the value and select a new value from the drop-down list. [ATTACHMENT filename='changing_enumeration_value.png']
  - For a Boolean value, click the value several times until the desired value is set. [ATTACHMENT filename='changing_boolean_value.png']
4. Press Enter to save the change.

When runtime values are changed, the simulation data is automatically updated.

##### Sending a Payload

A payload can be sent directly from a state transition in a view during model simulation. If sending a payload is supported for a transition, a smart manipulator icon appears next to the selected transition symbol.

To send a payload from a transition symbol

1. Select the transition symbol that has the payload you want to send.
2. Click the Fire Transition icon. [ATTACHMENT filename='firing_transition.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="isSelectedEnd"><span>You can interact with the simulation data displayed in views to improve understanding and analysis of system behavior during execution. Simulation views allow inspection and modification of runtime information without interrupting the simulation. </span><span>Manipulating simulation data provides a practical way to observe how a model responds to changing conditions, supporting both debugging and behavioral analysis.</span></p><h3 style="text-align: left;">Changing Runtime Values</h3><p style="text-align: left;">During simulation, initial runtime values (indicated by “:=”) can be changed directly in the views. This allows you to observe how the system’s behavior responds to changing values while the simulation is running.</p><p style="text-align: left;">To change runtime values on element shapes</p><hr /><ol style="text-align: left;"><li data-uuid="c98645fe-4142-4e3d-8432-034e41ea04d2">During model simulation, select a part, attribute, or reference shape in a view.</li><li data-uuid="4da77d11-322c-4b1f-bbf4-d41b7a8540b7">Select the<span> </span>initial runtime value (indicated by &quot;:=&quot;) you want to change.</li><li data-uuid="6c3ec624-e8f3-4eb4-9258-2b699ec40933">Do one of the following depending on the value type:<ul style="text-align: left;"><li data-uuid="90b85f6f-aae3-496f-9c97-ef9e07fe364f">For a numerical runtime value, type a new value.<br /><ac:image ac:height="116"><ri:attachment ri:filename="changing_numerical_value.png" /></ac:image></li><li data-uuid="eeffb28e-4cc0-4f2e-b3f8-ba584444e25a">For an enumeration runtime value, click the value and select a new value from the drop-down list.<br /><ac:image><ri:attachment ri:filename="changing_enumeration_value.png" /></ac:image></li><li data-uuid="0ca06777-3c9a-4375-a89e-b8ef455fd5e6">For a Boolean value, click the value several times until the desired value is set.<br /><ac:image><ri:attachment ri:filename="changing_boolean_value.png" /></ac:image></li></ul></li><li data-uuid="d251eb5b-6dbb-446a-9662-2a5b769ebcd7">Press Enter to save the change.</li></ol><p style="text-align: left;">When runtime values are changed, the simulation data is automatically updated. </p><h3 style="text-align: left;">Sending a Payload</h3><p style="text-align: left;">A payload can be sent directly from a state transition in a view during model simulation. If sending a payload is supported for a transition, a smart manipulator icon appears next to the selected transition symbol.</p><p style="text-align: left;">To send a payload from a transition symbol</p><hr /><ol style="text-align: left;"><li data-uuid="c27addd4-48d7-49e2-9d58-187ea4f7f0cb">Select the transition symbol that has the payload you want to send.</li><li data-uuid="8736aa39-fe7b-41c2-997e-784ac03cfc37">Click the<span> </span><strong>Fire Transition</strong><span> </span>icon. <br /><ac:image><ri:attachment ri:filename="firing_transition.png" /></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=309365623 space=SYSML2SP version=20 -->
## PAGE 00020: Modeling states for simulation

- page_id: `309365623`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365623/Modeling+states+for+simulation
- version_number: 20
- version_date: `2026-06-03T12:47:01.720+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide > Simulating states
- labels: []

### NORMALIZED CONTENT

This section provides guidelines for modeling states to ensure correct execution during simulation.

A state defines the dynamic behavior of a system by specifying the states, transitions, and actions that occur in response to events or conditions. When modeling states for simulation, it is essential to structure the model so that the simulation engine can correctly evaluate:

- State activation - which states are currently active
- Transition triggers - events or conditions that cause state changes
- Guard conditions - logical rules that enable or block transitions
- Behavioral actions - activities performed within states or during transitions
- Payload (signal) communication - how data or events are passed between elements

The following sections describe the key modeling elements required to create executable states and ensure accurate simulation results.

#### Initial state

An initial state represents the starting point of a state. It defines which state becomes active when execution begins.

An initial state does not represent an actual system condition. Instead, it is used to determine the first active state when the simulation starts.

The initial state is determined by either:

- the start node, or
- a state with no incoming transitions

If multiple states satisfy this condition, the simulation engine selects the first one based on model order.

#### PANEL: Example

Example

exhibitstateOperating_STM{ 
stateOff; 
stateStarting; 
stateRunning; 
transitionfirststartthenOff; 
transitionfirstOffthenStarting; 
transitionfirstStartingthenRunning; 
}

In the above example, the simulation starts at**start**, the transition leads to**Off**, and **Off**becomes the first active state.

#### Entry, do, and exit actions

States can define behaviors that are executed during different phases of state activation.

Entry, do, and exit actions allow the model to describe:

- Entry - initialization logic executed when entering a state.
- Do - behavior executed while the state remains active.
- Exit - cleanup or signaling executed when leaving a state

#### PANEL: Example

Example

stateOff{ 
entry{ 
assignlevel :=1; 
} 
do{ 
sendnewStatusUpdate() 
} 
exit{ 
sendnewStop() 
} 
}

Simulation behavior in the example above:

1. When Off becomes active, the entry action runs.
2. While Off is active, the do action runs.
3. When leaving Off , the exit action runs.

#### NOTE: Example

Only the following action types are currently supported:

- Assignment action
- Send action
- Composite actions (multiple actions executed sequentially) Exampleentry{ 
level :=1 
sendnewStart() 
}

#### Sending payloads using the send action

Payloads (signals) can be sent using thesendaction. Several optional parameters may be defined when sending a payload.

##### Sending a payload without attributes, a sender, or receiver

A payload can be sent without specifying attributes, sender, or receiver. In this case, the payload is sent to the state itself. If theitem definitionincludes attributes with default values, these defaults are included in the payload when it is sent.

#### PANEL: Example

Example

itemdefStart;stateOff{ 
entrysendnewStart(); 
}

##### Sending a payload with attributes

Payloads may contain attributes. Attribute values can be provided when sending the payload.

#### NOTE: Limitation

Limitation

and

#### PANEL: Example

Example

itemdefDataSignal 
{attributereading:Real; 
attributeisUrgent:Boolean 
}stateOff{ 
entrysendnewDataSignal(reading=150,isUrgent=false); 
}

##### Sending a payload via the sender

A payload can be sent through a**port usage** (sender). If multiple Connections or interface usages exist, the payload is delivered toall connected receivers, unless a specific receiver is defined.

#### PANEL: Example

Example

ItemdefStart;stateOff{ 
entrysendnewStart()viabuttonPort; 
}

##### Sending a payload to the receiver

A payload can be sent to a**part usage**(receiver)*.*

#### PANEL: Example

Example

ItemdefStart;stateOff{ 
entrysendnewStart()toButton; 
}

##### Sending a payload via the sender to the receiver

A payload can also be sent via a**port usage**(sender) to a**part usage**(receiver). In this scenario, the payload is transmitted from the specified sender port to the defined receiver part. This approach is useful when you want to limit delivery to specific receivers connected to that port.

#### PANEL: Example

Example

ItemdefStart;stateOff{ 
entrysendnewStart()viabuttonPorttoButton; 
}

#### Triggers on transitions

Atriggerspecifies the event that causes a transition to become eligible for execution. Without triggers, transitions would occur immediately whenever their source state is active. Triggers ensure transitions occur only when specific events happen.

A transition is executed when:

- Its trigger occurs.
- Any guard condition evaluates to true .

##### Types of supported triggers

###### Payload (signal) trigger

A payload trigger is triggered when a specific payload (signal) is received.

**Examples:**

transitionfirstOffacceptStartthenStarting;

transitionfirstOffacceptStartviaoutPortthenStarting;

The transition fires when the**Start**signal is received. If a port is defined, the payload will only be received if it arrives through the**specified port**.

Payloads can be defined using:

- Item definition
- Item usage

###### Change trigger

A change trigger is triggered when a Boolean expression changes from*false* to *true*, or when it evaluates to*true* during its first evaluation.

#### PANEL: Example

Example

transitionfirstIdleacceptwhenengine.temperature >100thenActive;

The transition fires when the expression becomes *true*.

###### Time trigger

A time trigger is triggered based on the simulation time.

Two types of time triggers are supported:

- Absolute time ExampletransitionfirstOffacceptat5[s]thenStarting; The transition fires when the simulation time reaches 5 seconds.
- Relative time ExampletransitionfirstOffacceptafter10[s]thenStarting; The transition fires when the simulation time reaches 10 seconds.

#### NOTE: Example

- Expressions referencing model values are supported. ExampletransitionfirstOffacceptaftertargetTime [s]thenStarting;
- The simulation engine does not interpret time units. All time values are executed in seconds by default.

#### Using guards on transitions

Aguard is a Boolean expression that must evaluate to*true*for a transition to occur. They add an additional condition that must be satisfied after the trigger is received. Therefore, guards allow modelingdecision logic within a state.

Guards are commonly used to:

- Check system parameters
- Filter incoming events
- Ensure transitions occur only in valid conditions

Without guards, transitions would be triggered whenever their events occur.

#### PANEL: Example

Example

transitionfirstOffacceptStartiflevel >1thenStarting;

Simulation behavior in the example above:

1. A Start signal is received.
2. The guard level > 1 is evaluated.
3. The transition executes only if the guard evaluates to true .

#### Using effects on transitions

A transition effectis an action that is executed when a transition occurs. Effects define behavior that happens during the transition between two states.

Effects allow the model to perform operations that logically belong to the transition itself, such as:

- Sending payloads
- Updating variables

This helps separatethe**state behavior** fromthe**transition behavior**.

**Execution order**

When a transition occurs, execution proceeds in the following order:

1. Exit action of the source state
2. Transition effect
3. Entry action of the target state

#### PANEL: Example

Example

transitionfirstOffacceptStartdosendnewStart()thenStarting;

Simulation behavior in the above example:

1. The exit action of Off executes.
2. The transition effect sends Start .
3. The entry action of Starting executes.

#### NOTE: Example

#### PANEL: Example

Example

transitionfirstOffacceptStartdo 
sendnewStart(); 
assignlevel; 
thenStarting;

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section provides guidelines for modeling states to ensure correct execution during simulation.</p><p>A state defines the dynamic behavior of a system by specifying the states, transitions, and actions that occur in response to events or conditions. When modeling states for simulation, it is essential to structure the model so that the simulation engine can correctly evaluate:</p><ul><li data-uuid="0b28f3d8-f81f-4034-9de8-13b1d9b88f80"><strong>State activation</strong> - which states are currently active</li><li data-uuid="50458a3a-ef21-43a9-a86b-0c4df8504359"><strong>Transition triggers</strong> - events or conditions that cause state changes</li><li data-uuid="aae5a99f-5b9c-40ef-9eec-f5b32edbdc29"><strong>Guard conditions</strong> - logical rules that enable or block transitions</li><li data-uuid="6f302b08-8bf3-4099-bdc4-70d209cb40a2"><strong>Behavioral actions</strong> - activities performed within states or during transitions</li><li data-uuid="c2b1be6a-498d-49b8-8207-d18ffa962d31"><strong>Payload (signal) communication</strong> - how data or events are passed between elements</li></ul><p>The following sections describe the key modeling elements required to create executable states and ensure accurate simulation results.</p><h2 style="text-align: left;">Initial state</h2><p>An initial state represents the starting point of a state. It defines which state becomes active when execution begins.</p><p>An initial state does not represent an actual system condition. Instead, it is used to determine the first active state when the simulation starts.</p><p>The initial state is determined by either:</p><ul><li data-uuid="290afc43-4823-46bb-8ea7-18d1bd80537b">the start node, or</li><li data-uuid="1dcdd111-0d3d-4bbb-bce1-16d5040face2">a state with no incoming transitions</li></ul><p>If multiple states satisfy this condition, the simulation engine selects the first one based on model order.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4d300c30-78eb-43b7-bce0-0209ef667fc3"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">exhibit</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Operating_STM</span><span style="color:var(--ds-text,#000000);"> {<br /></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Running</span><span style="color:var(--ds-text,#000000);">;<br /></span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Running</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    }</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">In the above example, the simulation starts at<span> </span><strong>start</strong>, the transition leads to<span> </span><strong>Off</strong>, and <strong>Off</strong><span> </span>becomes the first active state.</p><h2 style="text-align: left;">Entry, do, and exit actions</h2><p style="text-align: left;">States can define behaviors that are executed during different phases of state activation.</p><p style="text-align: left;">Entry, do, and exit actions allow the model to describe:</p><ul><li data-uuid="058da20a-c305-469f-a142-a6b09d47c5dd"><strong>Entry</strong> - initialization logic executed when entering a state.</li><li data-uuid="1daac322-0f70-4973-b4b1-33ef1fb4beaa"><strong>Do</strong> - behavior executed while the state remains active.</li><li data-uuid="32473065-9a44-4a33-a950-da80e3097339"><strong>Exit</strong> - cleanup or signaling executed when leaving a state</li></ul><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="da2b31a0-cd4e-4d9f-a836-8bbccea047ff"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">assign</span><span style="color:var(--ds-text,#000000);"> level := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">   }</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">do</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> StatusUpdate()</span><br /><span style="color:var(--ds-text,#000000);">   }</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">exit</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">      </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Stop()</span><br /><span style="color:var(--ds-text,#000000);">   }</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">Simulation behavior in the example above:</p><ol style="text-align: left;"><li data-uuid="7030280c-7bea-43b9-b0d3-b715a1a7e6f7">When<span> </span><strong>Off</strong><span> </span>becomes active, the<span> </span><strong>entry</strong> action runs.</li><li data-uuid="6fa1c0b3-a35a-4da8-bb2a-29d3bff90de8">While<span> </span><strong>Off</strong><span> </span>is active, the<span> </span><strong>do</strong> action runs.</li><li data-uuid="5a6d5e72-906b-43ab-9378-3b8f764ecb5a">When leaving<span> </span><strong>Off</strong>, the<strong> </strong><strong>exit </strong>action runs.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="df4458f7-3c46-47f5-a860-eea15e354451"><ac:rich-text-body><p>Only the following action types are currently supported:</p><ul><li data-uuid="0f4640cb-a4b2-4827-b786-5d242edefbef">Assignment action</li><li data-uuid="40564044-4987-4966-82e8-8daa4d540f41">Send action</li><li data-uuid="c1230362-1939-4124-b274-099e26bc2f5b">Composite actions (multiple actions executed sequentially)<ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3607b330-3abf-4954-b706-84f2bd982e5a"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">   level := </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><br /><span style="color:var(--ds-text,#000000);">   </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Start()</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro></li></ul></ac:rich-text-body></ac:structured-macro><h2>Sending payloads using the send action</h2><p>Payloads (signals) can be sent using the<span> </span>send<span> </span>action. Several optional parameters may be defined when sending a payload.</p><h3>Sending a payload without attributes, a sender, or receiver</h3><p>A payload can be sent without specifying attributes, sender, or receiver. In this case, the payload is sent to the state itself. If the<span> </span>item definition<span> </span>includes attributes with default values, these defaults are included in the payload when it is sent.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="eed94ba3-ceb3-48f5-8837-276d9a41d87c"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">item</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">            </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Start</span><span style="color:var(--ds-text,#000000);">();</span><br /><span style="color:var(--ds-text,#000000);">        }</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload with attributes</h3><p>Payloads may contain attributes. Attribute values can be provided when sending the payload.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a5468b6e-4422-4e87-b797-dca796792e11"><ac:parameter ac:name="title">Limitation</ac:parameter><ac:rich-text-body>Attributes can only be defined for<span> </span>primitive<span> and </span>enumeration<span> </span>types.</ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="980e8ee4-844e-4e85-b72d-c2c3f131003a"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">item</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">DataSignal</span><br /><span style="color:var(--ds-text,#000000);">{ </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">reading</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Real</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">isUrgent</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">Boolean</span><span style="color:var(--ds-text,#000000);"> </span><br /><span style="color:var(--ds-text,#000000);">}<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">DataSignal</span><span style="color:var(--ds-text,#000000);">(</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">reading</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">150</span><span style="color:var(--ds-text,#000000);">, </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">isUrgent</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue,#0055cc);">false</span><span style="color:var(--ds-text,#000000);">);</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload via the sender</h3><p>A payload can be sent through a<span> </span><strong>port usage</strong> (sender). If multiple Connections or interface usages exist, the payload is delivered to<span> </span>all connected receivers, unless a specific receiver is defined.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e8bc354e-3dd3-49e0-9c80-ab633dba5c2b"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">Item </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">via</span><span style="color:var(--ds-text,#000000);"> buttonPort;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload to the receiver</h3><p>A payload can be sent to a<span> <strong>part usage</strong> </span>(receiver)<em>.</em></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10b53614-dfee-4732-afb1-bd641ebdd44b"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">Item </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> Button;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h3 class="code-java">Sending a payload via the sender to the receiver</h3><p>A payload can also be sent via a<span> <strong>port usage</strong></span><span> </span>(sender) to a<span> <strong>part usage</strong> </span>(receiver). In this scenario, the payload is transmitted from the specified sender port to the defined receiver part. This approach is useful when you want to limit delivery to specific receivers connected to that port.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3f321aba-91a2-498b-a566-dc4cdb426944"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#000000);">Item </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">state</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);">{</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">entry</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Start</span><span style="color:var(--ds-text,#000000);">() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">via</span><span style="color:var(--ds-text,#000000);"> buttonPort </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> Button;</span><br /><span style="color:var(--ds-text,#000000);">}</span></p></ac:rich-text-body></ac:structured-macro><h2 class="code-java">Triggers on transitions</h2><p style="text-align: left;">A<span> </span>trigger<span> </span>specifies the event that causes a transition to become eligible for execution. Without triggers, transitions would occur immediately whenever their source state is active. Triggers ensure transitions occur only when specific events happen.</p><p style="text-align: left;">A transition is executed when:</p><ul style="text-align: left;"><li data-uuid="98466f7d-f999-414c-a502-e980e20d4009">Its trigger occurs.</li><li data-uuid="2c261f9d-1cdd-4e43-af87-c2d793c3f9f2">Any guard condition evaluates to <em>true</em>.</li></ul><h3 style="text-align: left;">Types of supported triggers</h3><h4 style="text-align: left;">Payload (signal) trigger</h4><p style="text-align: left;">A payload trigger is triggered when a specific payload (signal) is received.</p><p style="text-align: left;"><strong>Examples:</strong></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b6baf7f4-fdcc-494b-be07-3f4521551a94"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e751214a-70a3-4b84-ac84-3a7251603d8c"><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">via</span><span style="color:var(--ds-text,#000000);"> outPort </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">The transition fires when the<span> </span><strong>Start</strong><span> </span>signal is received. If a port is defined, the payload will only be received if it arrives through the<span> </span><strong>specified port</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7c9a8090-868b-4d78-843e-fe7137208ed0"><ac:rich-text-body><p>Payloads can be defined using:</p><ul><li data-uuid="ab972ab2-c719-441b-9a4c-1b6906e7cf58">Item definition</li><li data-uuid="508c62aa-ea9b-4903-8cf2-49af0c26bf23">Item usage</li></ul></ac:rich-text-body></ac:structured-macro><h4>Change trigger</h4><p style="text-align: left;">A change trigger is triggered when a Boolean expression changes from<span> </span><em>false</em> to <em>true</em>, or when it evaluates to<span> </span><em>true</em> during its first evaluation.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="31f0c11f-d650-4cd3-abf8-e5dadf5e1ae1"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> Idle </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">when</span><span style="color:var(--ds-text,#000000);"> engine.temperature &gt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">100</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Active</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">The transition fires when the expression becomes <em>true</em>.</p><h4 style="text-align: left;">Time trigger</h4><p style="text-align: left;">A time trigger is triggered based on the simulation time.</p><p style="text-align: left;">Two types of time triggers are supported:</p><ul><li style="text-align: left;" data-uuid="36c69654-fafe-4509-a0d4-7964fdb9c7fe"><strong>Absolute time</strong><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="548fb61f-8717-46bd-b72b-9f879f4b590f"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">at</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">5</span><span style="color:var(--ds-text,#000000);"> [s] </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro>The transition fires when the simulation time reaches<span> </span>5 seconds.</li><li style="text-align: left;" data-uuid="e97d9909-d2da-4924-927b-63a6e3956d75"><strong>Relative time</strong><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="941c96ee-ba51-46c7-b0b0-510486b878dc"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">after</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">10</span><span style="color:var(--ds-text,#000000);"> [s] </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro>The transition fires when the simulation time reaches<span> </span>10 seconds.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="983ab964-c19a-4121-b68a-a7ebc2bbc0f4"><ac:rich-text-body><ul><li data-uuid="3f43bb8e-bc2d-446b-a168-1afff29c8696">Expressions referencing model values are supported.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="10afd8d5-9a05-47f6-9196-70e73d6eb1e0"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> Off </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">after</span><span style="color:var(--ds-text,#000000);"> targetTime [s] </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro></li><li data-uuid="0ed8c1b3-2765-42eb-b908-5fc601816d30">The simulation engine<span> </span>does not interpret time units. All time values are executed in<span> </span>seconds by default.</li></ul></ac:rich-text-body></ac:structured-macro><h2 class="code-java">Using guards on transitions</h2><p style="text-align: left;">A<span> </span>guard is a Boolean expression that must evaluate to<span> </span><em>true</em><span> </span>for a transition to occur. They add an additional condition that must be satisfied after the trigger is received. Therefore, guards allow modeling<span> </span>decision logic within a state.</p><p style="text-align: left;">Guards are commonly used to:</p><ul style="text-align: left;"><li data-uuid="d2e3c98d-5949-4b90-9e3e-f9fdc32a513e">Check system parameters</li><li data-uuid="255a7bae-53aa-4569-a91d-708d4ac928ae">Filter incoming events</li><li data-uuid="879be7b3-c3cc-4671-8eb2-6408f0777bbb">Ensure transitions occur only in valid conditions</li></ul><p style="text-align: left;">Without guards, transitions would be triggered whenever their events occur.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="9286e644-1983-482b-b815-4accd9e922f2"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">if</span><span style="color:var(--ds-text,#000000);"> level &gt; </span><span style="color:var(--ds-background-accent-green-bolder,#1f845a);">1</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">Simulation behavior in the example above:</p><ol style="text-align: left;"><li data-uuid="4a86395f-5907-4ebb-8471-97a54e245e08">A<span> </span><strong>Start</strong><span> </span>signal is received.</li><li data-uuid="07c7437d-ecc7-4a58-889b-9ef7893ac7bf">The guard<span> </span>level &gt; 1<span> </span>is evaluated.</li><li data-uuid="9b7d4704-5a49-47af-885d-23c8b9509882">The transition executes<span> </span>only if the guard evaluates to <em>true</em>.</li></ol><h2 style="text-align: left;">Using effects on transitions</h2><p style="text-align: left;">A transition effect<span> </span>is an action that is executed when a transition occurs. Effects define behavior that happens during the transition between two states.</p><p style="text-align: left;">Effects allow the model to perform operations that logically belong to the transition itself, such as:</p><ul style="text-align: left;"><li data-uuid="279c3de4-f7c0-45f4-8d98-64876075fcc3">Sending payloads</li><li data-uuid="42f0dbb9-a877-4551-9495-53c792c645cc">Updating variables</li></ul><p style="text-align: left;">This helps separate<span> the </span><strong>state behavior</strong> from<span> the </span><strong>transition behavior</strong>.</p><p style="text-align: left;"><strong>Execution order</strong></p><p style="text-align: left;">When a transition occurs, execution proceeds in the following order:</p><ol style="text-align: left;"><li data-uuid="ee25645f-faf6-4150-b9df-0d48ae4b7c55">Exit action<span> </span>of the source state</li><li data-uuid="31ed7db3-aa9d-442a-9604-fd0c698e1761">Transition<span> </span>effect</li><li data-uuid="d89aef34-e580-4919-8388-1f40bc1bbd54">Entry action<span> </span>of the target state</li></ol><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e361fa99-b885-4f23-b4e7-b68a981b7359"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Off</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">do</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Start() </span><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><p class="code-java">Simulation behavior in the above example:</p><ol style="text-align: left;"><li data-uuid="fe00f8b2-07e5-47ab-aa02-4e2311477bdf">The exit action of<span> </span><strong>Off</strong><span> </span>executes.</li><li data-uuid="3eb5aaed-cfa2-4ac7-a472-28fd60fe4c7d">The transition effect sends<span> </span><strong>Start</strong>.</li><li data-uuid="a9940bb9-a76c-447d-ac20-4661dddbc892">The entry action of<span> </span><strong>Starting</strong><span> </span>executes.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="20889c99-8651-4890-a7e8-b9d28cfc75a0"><ac:rich-text-body>Effects may include multiple actions. These actions are executed in the order defined.<br /><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="1b0e4a1c-def1-4a3c-ade6-fcaf01ab7532"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">transition</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">first</span><span style="color:var(--ds-text,#000000);"> Off </span><span style="color:var(--ds-text-accent-blue,#0055cc);">accept</span><span style="color:var(--ds-text,#000000);"> Start </span><span style="color:var(--ds-text-accent-blue,#0055cc);">do</span><br /><span style="color:var(--ds-text,#000000);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">send</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">new</span><span style="color:var(--ds-text,#000000);"> Start();</span><br /><span style="color:var(--ds-text,#000000);">  </span><span style="color:var(--ds-text-accent-blue,#0055cc);">assign</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">level</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text-accent-blue,#0055cc);">then</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">Starting</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=298094585 space=SYSML2SP version=2 -->
## PAGE 00021: Prerequisites

- page_id: `298094585`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/298094585/Prerequisites
- version_number: 2
- version_date: `2026-04-01T12:24:43.681+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

To work with all of the SysML v2 simulation features, the following software should be [installed](https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&version=latest):

- One of the following CATIA Magic/No Magic modeling tools:
  - Cameo Systems Modeler (Enterprise Edition only)
  - Cameo Enterprise Architecture
  - Magic Cyber Systems Engineer
  - Magic Systems of Systems Architect
- SysML v1 Plugin.
- Cameo Requirements Modeler.
- Cameo Simulation Toolkit or Magic Model Analyst.
- SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.
- SysML v2 Simulation Plugin. It enables execution of SysML v2 models (state machine simulations, mathematical calculations, and requirements verification).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">To work with all of the SysML v2 simulation features, the following software should be <a href="https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&amp;version=latest">installed</a>:</p><ul style="text-align: left;"><li data-uuid="34fec4e7-ad39-45f6-8615-0a3ea8277051">One of the following CATIA Magic/No Magic modeling tools:<ul><li>Cameo Systems Modeler (Enterprise Edition only)</li><li>Cameo Enterprise Architecture</li><li>Magic Cyber Systems Engineer</li><li>Magic Systems of Systems Architect</li></ul></li><li data-uuid="4d8f8ae9-1b0d-4142-9b1e-06cd6790e2d1">SysML v1 Plugin.</li><li data-uuid="2090e25b-4471-446c-98b8-3950634ee8a0">Cameo Requirements Modeler.</li><li data-uuid="75a80510-7ecf-4758-a004-5d3ef8fa48f6">Cameo Simulation Toolkit or Magic Model Analyst.</li><li data-uuid="8cf4e403-0608-4b30-bf35-0aac0af7e487">SysML v2 Plugin. It provides the majority of the SysML v2 features, including the Textual Editor.</li><li data-uuid="b8263519-1d0c-49a9-853b-b04fb72718fe">SysML v2 Simulation Plugin. It enables execution of SysML v2 models (state machine simulations, mathematical calculations, and requirements verification).</li></ul>
````

<!--NOMAGIC_PAGE id=309365638 space=SYSML2SP version=6 -->
## PAGE 00022: Running the state simulation

- page_id: `309365638`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365638/Running+the+state+simulation
- version_number: 6
- version_date: `2026-06-03T12:56:02.527+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide > Simulating states
- labels: []

### NORMALIZED CONTENT

The SysML v2 simulation engine performs a state simulation when one of the following elements is selected for simulation:

- State
- Exhibit state
- Part usage that owns an **e** xhibit state

##### Starting state simulation

To start the state simulation

1. Simulate a s tate, exhibit state, or part usage that owns an exhibit state.
2. In the SysML v2 Simulation window, click [IMAGE alt='' src=''].

The simulation runs until it is manually stopped.

##### Terminating state simulation

You can terminate the simulation by clicking**Terminate**(**[IMAGE alt='' src='']**)from one of the following locations:

- Diagram toolbar
- SysML v2 Simulation window
- Context menu of the simulated element

##### Sending payloads during simulation

During a simulation, payloads can be sent interactively using thesmart manipulator of a transition symbol displayed in views.

To send a payload from a transition symbol

1. Select the transition symbol that defines the payload you want to send.
2. Click Fire Transition .

If no element consumes a payload, it is automatically removed from the event pool.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The SysML v2 simulation engine performs a state simulation when one of the following elements is selected for simulation:</p><ul style="text-align: left;"><li data-uuid="280bcaf4-3861-4dd2-aae1-1af30d0e0d61"><strong>State</strong></li><li data-uuid="21c1f7a3-3fab-4119-878c-cd99f13cd850"><strong>Exhibit state</strong></li><li data-uuid="860c5cf2-9f0e-48df-83c5-b57c7f6e9c0e"><strong>Part usage</strong><span> </span>that owns an<span> <strong>e</strong></span><strong>xhibit state</strong></li></ul><h3 style="text-align: left;">Starting state simulation</h3><p style="text-align: left;">To start the state simulation</p><hr /><ol style="text-align: left;"><li data-uuid="a77afb1d-7ba7-48fd-9c6e-a4bedeb72c9b">Simulate a<span> s</span>tate, exhibit state, or part usage that owns an exhibit state.</li><li data-uuid="929aaf13-0187-4e3a-a8a4-eea59637245a">In the <strong>SysML v2 Simulation</strong> window, click <strong><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="start.png" /></ac:image>.</strong></li></ol><p style="text-align: left;">The simulation runs until it is manually stopped.</p><h3 style="text-align: left;">Terminating state simulation</h3><p style="text-align: left;">You can terminate the simulation by clicking<span> </span><strong>Terminate</strong><span> (<strong><ac:image><ri:attachment ri:filename="terminate.png" /></ac:image></strong>) </span>from one of the following locations:</p><ul style="text-align: left;"><li data-uuid="df4b2e7f-c7e0-4a9a-86aa-f7d9bb9b3298">Diagram toolbar</li><li data-uuid="ef6974b6-e252-418d-8d6c-5f1a1985ab4b"><strong>SysML v2 Simulation</strong> window</li><li data-uuid="0a110057-fd2a-43f8-b3a2-a52b90097ae9">Context menu of the simulated element</li></ul><h3 style="text-align: left;">Sending payloads during simulation</h3><p style="text-align: left;">During a simulation, payloads can be sent interactively using the<span> </span>smart manipulator of a transition symbol displayed in views.</p><p>To send a payload from a transition symbol</p><hr /><ol style="text-align: left;"><li data-uuid="895a31c9-e9f2-48d4-a500-2a2aa7cf4c13">Select the transition<span> </span>symbol that defines the payload you want to send.</li><li data-uuid="6c14a175-7c4c-475a-9b7a-17b88ca34c94">Click<span> </span><strong>Fire Transition</strong>. </li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c663d930-3dc0-4109-8220-bae07e575384"><ac:rich-text-body>If no element consumes a payload, it is automatically removed from the event pool.</ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=298094594 space=SYSML2SP version=2 -->
## PAGE 00023: Samples and libraries

- page_id: `298094594`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/298094594/Samples+and+libraries
- version_number: 2
- version_date: `2026-04-10T18:02:19.723+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

##### Samples

You can review the SysML v2 project samples provided with the installation, found at:

- <modeling tool installation directory>\samples\SysML v2\SysML v2 Simulation Overview.mdszip

##### Libraries

Each SysML v2 project is automatically loaded with the following used projects:

- Standard Libraries. It contains standard SysML v2 libraries.
- 3DS SysML Customization. It contains concepts designed for view creation and symbol style customization.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Samples</h3><p style="text-align: left;">You can review the SysML v2 project samples provided with the installation, found at:</p><ul style="text-align: left;"><li data-uuid="3b534de1-52a0-47ab-8228-870773d3c79e"><em>&lt;modeling tool installation directory&gt;\samples\SysML v2\SysML v2 Simulation Overview.mdszip</em></li></ul><h3 style="text-align: left;">Libraries</h3><p style="text-align: left;">Each SysML v2 project is automatically loaded with the following used projects:</p><ul style="text-align: left;"><li data-uuid="3d73af8a-9f6a-4afc-b376-0a94305086c4"><em>Standard Libraries.</em><span> </span>It contains standard SysML v2 libraries.</li><li data-uuid="70a874e7-d705-425d-a85e-387875955662"><em>3DS SysML Customization.</em><span> </span>It contains concepts designed for view creation and symbol style customization.</li></ul>
````

<!--NOMAGIC_PAGE id=309365617 space=SYSML2SP version=2 -->
## PAGE 00024: Simulating states

- page_id: `309365617`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365617/Simulating+states
- version_number: 2
- version_date: `2026-06-03T09:40:04.625+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

Simulating states allows you to execute and visualize the behaviors they define. Using the SysML v2 Simulation plugin, you can run SysML v2 states directly from the model and observe how states, transitions, triggers, and actions behave during execution.

Simulation enables you to:

- Validate system behavior early in the design process
- Verify state transitions and guard logic
- Observe how payloads and events propagate between elements
- Identify issues in behavioral models before implementation
- Demonstrate system behavior interactively

During simulation, active states are annotated, and transitions are executed according to the semantics defined in the model, allowing you to explore system dynamics in real time.

For more information, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Simulating states allows you to execute and visualize the behaviors they define. Using the SysML v2 Simulation plugin, you can run SysML v2 states directly from the model and observe how states, transitions, triggers, and actions behave during execution.</p><p data-start="1409" data-end="1439">Simulation enables you to:</p><ul data-start="1444" data-end="1715"><li data-section-id="i51o6b" data-start="1444" data-end="1498" data-uuid="2d36acf2-f4dd-4cc3-9a68-6d26cdc4a358">Validate system behavior early in the design process</li><li data-section-id="9et9kk" data-start="1501" data-end="1543" data-uuid="88e4cc05-28c7-4a63-8ad8-bf5a98fd01d0">Verify state transitions and guard logic</li><li data-section-id="1orl4vb" data-start="1546" data-end="1606" data-uuid="0e1d6af3-1ff4-4ac3-9a67-953751b82fb5">Observe how payloads and events propagate between elements</li><li data-section-id="80z2bb" data-start="1609" data-end="1669" data-uuid="23c9d399-e7d9-4043-b55a-843d232e9a13">Identify issues in behavioral models before implementation</li><li data-section-id="6z70tw" data-start="1672" data-end="1715" data-uuid="5764b3af-704f-429b-9577-8f4166243a73">Demonstrate system behavior interactively</li></ul><p style="text-align: left;">During simulation, active states are annotated, and transitions are executed according to the semantics defined in the model, allowing you to explore system dynamics in real time.</p><p style="text-align: left;">For more information, see the following topics:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="48540b48-a3eb-4863-9827-768a42255091" /></p>
````

<!--NOMAGIC_PAGE id=306283322 space=SYSML2SP version=3 -->
## PAGE 00025: Simulation information in views

- page_id: `306283322`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/306283322/Simulation+information+in+views
- version_number: 3
- version_date: `2026-05-28T14:19:22.757+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

During simulation, model views can display runtime information that reflects the current state of the simulated system. This allows observing variable values, execution states, and calculated data directly within views.

Simulation data visualization helps analyze system behavior without leaving the modeling environment. Runtime information can be displayed, updated, and manipulated while the simulation is running.

For more information, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">During simulation, model views can display runtime information that reflects the current state of the simulated system. This allows observing variable values, execution states, and calculated data directly within views.</p><p style="text-align: left;">Simulation data visualization helps analyze system behavior without leaving the modeling environment. Runtime information can be displayed, updated, and manipulated while the simulation is running.</p><p style="text-align: left;">For more information, see the following topics:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b5751640-0630-41cf-8356-848f2ffa0594" /></p>
````

<!--NOMAGIC_PAGE id=309365620 space=SYSML2SP version=2 -->
## PAGE 00026: Supported elements

- page_id: `309365620`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/309365620/Supported+elements
- version_number: 2
- version_date: `2026-06-03T09:54:26.342+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide > Simulating states
- labels: []

### NORMALIZED CONTENT

The tables below list the SysML v2 state elements supported by the simulation engine.

In the **Executable** column, the following symbols mark whether elements are supported or not:

- [ATTACHMENT filename='supported.png'] - Supported elements
- [ATTACHMENT filename='partialy_supported.png'] - Partially supported elements
- [ATTACHMENT filename='unsupported.png'] - Unsupported elements

##### States

| SysML v2 Concept | Specification details | Executable |
| --- | --- | --- |
| State Def | State Def |  |
| stateDef :> stateDef |  |  |
| abstract stateDef |  |  |
| State Usage | State Usage |  |
| Exhibit State Usage |  |  |
| Composite State |  |  |
| Parallel State |  |  |
| stateUsage : stateDef |  |  |
| stateUsage :> stateUsage |  |  |
| stateUsage :>> stateUsage |  |  |
| ref stateUsage:StateDef |  |  |
| stateUsage references stateUsage |  |  |
| stateUsage_1 = stateUsage_2 |  |  |
| stateUsage : StateDef [1..*] ordered nonunique |  |  |
| Control Nodes | Start (Initial) Node |  |
| Done (Final) Node |  |  |
| Terminate Node |  |  |
| Entry Action | entry action assign x:=1; |  |
| entry action InitialAssign { *assign* controller.valve:=1; *send* new Terminate() via ButtonPort; } |  |  |
| entry action actionUsage:actionDef:; |  |  |
| entry actionUsage; |  |  |
| Do Action | do action assign x:=1; |  |
| do action InitialAssign { *assign* controller.valve:=1; *send* new Terminate() via ButtonPort; } |  |  |
| do action actionUsage:actionDef:; |  |  |
| do actionUsage; |  |  |
| Exit Action | exit action assign x:=1; |  |
| exit action InitialAssign { *assign* controller.valve:=1; *send* new Terminate() via ButtonPort; } |  |  |
| exit action actionUsage:actionDef:; |  |  |
| exit actionUsage; |  |  |
| Transitions | Transition |  |
| Self Transition |  |  |
| Completion Transition |  |  |
| Accepter(Transition)Accept Action | Accept Payload Trigger accept Start;accept Start via TimerPort; |  |
| Change Trigger accept when waterTank.level <= minlevel |  |  |
| Time Trigger (Absolute) accept at 5 [s]accept at operationTime |  |  |
| Time Trigger (Relative) accept after 2 [s]accept after simTime>10 |  |  |
| Guard(Transition) | if waterTank.level <= minlevel |  |
| if not waterTank.level <= minlevel |  |  |
| if payload.targetSpeed>0 |  |  |
| Effect(Transition) | do action assign x:=1; |  |
| do action InitialAssign { *assign* x:=1; *assign* y:=1; } |  |  |
| do action actionUsage:actionDef:; |  |  |
| do actionUsage; |  |  |
| do action assign speed :=payload.targetSpeed; |  |  |
| Conditional Succession | state def OperationalStates { entry action initial { out attribute isStarting : Boolean; } if not initial.isStarting then off; if initial.isStarting then starting; state off; state starting; state on; } |  |

##### Actions

#### NOTE: Limitation

Limitation

The usage is restricted to entry/do/exit actions or transition effects within a state.

| SysML v2 Concept | Specification details | Status |
| --- | --- | --- |
| Assignment action | assign x:=1; |  |
| assign x:= 1+y*54; |  |  |
| assign x:= telecom.antenna.mass; |  |  |
| assign telecom.antenna.mass:=2; |  |  |
| Send action | send new Start(); |  |
| send new Start() to timer; |  |  |
| send new Start() via outPort; |  |  |
| send new Start() via outPort totimer; |  |  |
| send new Start() to vehicle.engine |  |  |
| send new Start(limit=10, mass=129) |  |  |
| send itemUsage; |  |  |
| Accept action | accept Start |  |
| accept Start via inPort |  |  |
| accept after 2accept after simTime>10(Relative time trigger) |  |  |
| accept at 5accept at operationTime(Absolute time trigger) |  |  |
| accept when x>1(Change trigger) |  |  |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The tables below list the SysML v2 state elements supported by the simulation engine.</p><p style="text-align: left;">In the <strong>Executable</strong> column, the following symbols mark whether elements are supported or not:</p><ul><li data-uuid="7cb1bd3a-d732-402f-8f3f-4efad33d55c8"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image> - Supported elements</li><li data-uuid="bae86dee-597f-4f47-9519-816a76bed450"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image> - Partially supported elements</li><li data-uuid="4cc9b194-da82-465d-b977-b805de577469"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image> - Unsupported elements</li></ul><h3 style="text-align: left;">States</h3><table class="wrapped"><tbody class=""><tr class=""><th style="text-align: center;">SysML v2 Concept</th><th style="text-align: center;">Specification details</th><th style="text-align: center;">Executable</th></tr><tr class=""><td rowspan="3"><strong>State Def</strong></td><td>State Def</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>stateDef<span> </span><strong>:&gt;</strong><span> </span>stateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>abstract</strong><span> </span>stateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="11"><strong>State Usage</strong></td><td>State Usage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Exhibit State Usage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Composite State</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>Parallel State</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>:</strong><span> </span>stateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>:&gt;</strong><span> </span>stateUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>:&gt;&gt;</strong><span> </span>stateUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>ref</strong><span> </span>stateUsage:StateDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>stateUsage<span> </span><strong>references</strong><span> </span>stateUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>stateUsage_1<span> </span><strong>=</strong><span> </span>stateUsage_2</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>stateUsage : StateDef<span> </span><strong><span class="error">[1..*]</span><span> </span>ordered nonunique</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="3"><strong>Control Nodes</strong></td><td>Start (Initial) Node</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Done (Final) Node</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td>Terminate Node</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Entry Action</strong></td><td><strong>entry</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>entry</strong><span> </span><strong>action</strong><span> </span>InitialAssign {       *assign* controller.valve:=1;       *send* new Terminate() via ButtonPort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>entry</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>entry</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Do Action</strong></td><td><strong>do</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>InitialAssign {     *assign* controller.valve:=1;     *send* new Terminate() via ButtonPort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Exit Action</strong></td><td><strong>exit</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>exit</strong><span> </span><strong>action</strong><span> </span>InitialAssign {       *assign* controller.valve:=1;       *send* new Terminate() via ButtonPort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>exit</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>exit</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="3"><strong>Transitions</strong></td><td>Transition</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Self Transition</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Completion Transition</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="4"><strong>Accepter</strong><br /><strong>(Transition)</strong><br /><strong>Accept Action</strong></td><td>Accept Payload Trigger<br /> <br /><em>accept Start;</em><br /><em>accept Start via TimerPort;</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Change Trigger<br /> <br /><em>accept when waterTank.level &lt;= minlevel</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Time Trigger (Absolute)<br /> <br /><em>accept at 5<span> </span><span class="error">[s]</span></em><br />accept at operationTime</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td>Time Trigger (Relative)<br /> <br /><em>accept after 2<span> </span><span class="error">[s]</span></em><br />accept after simTime&gt;10</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="3"><strong>Guard</strong><br /><strong>(Transition)</strong></td><td><strong>if</strong><span> </span><em>waterTank.level &lt;= minlevel</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><em><strong>if</strong><span> </span><strong>not</strong><span> </span>waterTank.level &lt;= minlevel</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>if</strong><span> </span><strong>payload</strong>.targetSpeed&gt;0</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="5"><strong>Effect</strong><br /><strong>(Transition)</strong></td><td><strong>do</strong><span> </span><strong>action</strong><span> </span><strong>assign</strong><span> </span>x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>InitialAssign {       *assign* x:=1;       *assign* y:=1; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span><strong>action</strong><span> </span>actionUsage:actionDef:;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>do</strong><span> </span>actionUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>do action assign</strong><span> </span>speed<span> </span><strong>:=</strong><strong>payload</strong>.targetSpeed;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>Conditional Succession</strong></td><td><pre class="code-java">state def OperationalStates {
entry action initial { out attribute isStarting : <span class="code-object" style="color:var(--ds-text-accent-blue-bolder,#09326c);">Boolean</span>; }
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">if</span> not initial.isStarting then off;
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">if</span> initial.isStarting then starting;
state off;
state starting;
state on; }</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr></tbody></table><h3 style="text-align: left;">Actions</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3ead4032-c783-435c-96cd-a6f746fffb12"><ac:parameter ac:name="title">Limitation</ac:parameter><ac:rich-text-body>The usage is restricted to entry/do/exit actions or transition effects within a state.</ac:rich-text-body></ac:structured-macro><table class="wrapped relative-table" style="letter-spacing: 0.0px;width: 51.6164%;"><colgroup><col style="width: 18.7035%;" /><col style="width: 69.9256%;" /><col style="width: 11.3709%;" /></colgroup><tbody class=""><tr class=""><th style="text-align: center;">SysML v2 Concept</th><th style="text-align: center;">Specification details</th><th style="text-align: center;">Status</th></tr><tr class=""><td rowspan="4"><strong>Assignment action</strong></td><td><strong>assign</strong> x:=1;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>assign</strong> x:= 1+y*54;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>assign</strong> x:= telecom.antenna.mass;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>assign</strong> telecom.antenna.mass:=2;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="7"><strong>Send action</strong></td><td><strong>send</strong> <strong>new</strong> Start();</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>to</strong> timer;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>via</strong> outPort;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>via</strong> outPort <strong>to</strong>timer;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start() <strong>to</strong> vehicle.engine</td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p><p><br /></p></div></td></tr><tr class=""><td><strong>send</strong> <strong>new</strong> Start(limit=10, mass=129)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>send</strong> itemUsage;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td></tr><tr class=""><td rowspan="5"><strong>Accept action</strong></td><td><strong>accept</strong> Start</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> Start via inPort</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> <strong>after</strong> 2<br /><strong>accept</strong> <strong>after</strong> simTime&gt;10<br />(Relative time trigger)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> <strong>at</strong> 5<br /><strong>accept</strong> <strong>at</strong> operationTime<br />(Absolute time trigger)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr><tr class=""><td><strong>accept</strong> <strong>when</strong> x&gt;1<br />(Change trigger)</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=298094715 space=SYSML2SP version=18 -->
## PAGE 00027: Supported structural and connectivity elements

- page_id: `298094715`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/298094715/Supported+structural+and+connectivity+elements
- version_number: 18
- version_date: `2026-06-22T14:55:22.920+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

This chapter defines thestructure concepts and connectivitysupported by the simulation engine. It outlines how SysML v2 architectural elements are transformed from static definitions into dynamic, executable models, focusing on data propagation, interface contracts, and runtime validation.

##### Supported elements

The simulation engine supports execution of the SysML v2 structure elements listed in the table below.

In the **Executable** column, the following symbols mark whether elements are supported or not:

- [ATTACHMENT filename='supported.png'] - Supported elements
- [ATTACHMENT filename='partialy_supported.png'] - Partially supported elements
- [ATTACHMENT filename='unsupported.png'] - Unsupported elements

| SysML v2 Concept | Specification details | Executable | Notes |
| --- | --- | --- | --- |
| Part Def | PartDef |  |  |
| Part Usage | Part Usage |  |  |
| partUsage : PartDef |  |  |  |
| partUsage :>> partUsage |  |  |  |
| partUsage :> partUsage |  |  |  |
| partUsage [1..*] ordered nonunique |  |  |  |
| ref partUsage : PartDef |  |  |  |
| partUsage_1 = partUsage_2 |  |  |  |
| Port Def | port def FuelingPort { attribute flowRate : Real; out fuelOut : Fuel; in fuelReturn : Fuel; } |  | The simulation does not check the direction of a directed Feature, meaning the payload is transferred without verifying if it complies with the port definition |
| Port Usage | portUsage : PortDef |  |  |
| portUsage : ~PortDef |  |  |  |
| Nested portsport p0 : PortDef { port p1 : PortDef; port p2 : PortDef; port p3 : PortDef;} |  |  |  |
| Connection Def | connection defConnectionDef1 {end part end1 : Part1;end part end2 : Part2;} |  |  |
| Connection Usage | connection connection1 :ConnectionDef1connect part1.port to part2.port; |  | All ConnectionUsage functions as delegation. |
| Connection (n-ary{}with 3 ends)connection connection1 : ConnectionDef1connect (part1,part2, part3); |  |  |  |
| Binding Connection | binding bind attributeUsage = attributeUsage; |  | Binding works only between attribute usages of primitive types. |
| Interface Def | interface def ControlToTankInterface { endp1 : ~ValvePort; endp2 :ValvePort; } |  | If a flow is specified between attribute usages of primitive types, the value flows according to the specification. |
| Interface Usage | interface : ControlToTankInterface connect controller.valvePort to waterTank.valvePort; |  | All InterfaceUsage functions as a delegation. |
| Flow | interface def ControlToTankInterface { endp1 : ~:ValvePort; endp2 :ValvePort; flow from p1.valve to p2.valve; } |  | Flows are supported only when specified in the Interface Definition |
| Attribute Def | attribute def Dimensions { attributelength :Real; attributewidth :Real; attributeheight :Real; } |  |  |
| Attribute Usage | attributeUsage:ScalarValues::Real |  | Only primitive type (Integer, Real, String, Boolean)Units are not supported. |
| attributeUsage : EnumerationDef |  |  |  |
| attributeUsage:mass |  | Units are not supported. |  |
| attributeUsage = expression |  |  |  |
| attributeUsage := expression |  |  |  |
| attribute:AttributeDef |  |  |  |
| attribute:AttributeDef [1..*] |  |  |  |
| Enumeration | enum def EnumerationDef1 { enum enum1; enum enum2; } |  |  |
| enum def EnumerationDef1 { enum = value1[unit1]; enum = value2[unit2]; } |  |  |  |

##### Connectivity

Connectivity in SysML v2 simulation moves beyond static structural definitions to specify how elementsdynamically interactduring execution. The simulation engine enforces strict rules for data exchange, payload routing, and state synchronization to ensure model fidelity.

###### Interfaces

Interfaces serve as the formal contract between structural parts. They define the structured interaction points where data, energy, or material (modeled asflowUsages) cross system boundaries.

Key Applications:

- Component Decoupling Define how components interact (ports and flows) without being dependent on their internal state machine logic or private behaviors.
- Automated Data Propagation Ensure that a value change in a source component is automatically reflected in the connected target component.
- Payload Routing Facilitate the movement of discrete messages or physical items through defined ports.

[IMAGE alt='' src='']

###### Simulation of the *FlashingLightSystem* part usage.

#### PANEL: Syntax example

Syntax example

interfacedefButtonToTimerInterface{ 
endp1:ButtonPort; 
endp2:TimerInPort; 
flowofStartfromp1.starttop2.start; 
flowofStopfromp1.starttop2.start; 
}// Usage in a system contextinterface:ButtonToTimerInterfaceconnectbutton.buttonOuttotimer.timerIn;

Payloads can also be transferred using a connection usage.

###### Flows

The simulation engine executesflow usagesdefined within aninterface definition. The behavior of these flows follows specific operational semantics:

- Data Transfer (Non-Destructive) By default, transfers are executed as a copy operation. The source value remains intact while an identical instance is propagated to the target (isMove = false).
- Propagation Trigger (Push) Value transfer is reactive. It is initiated immediately upon an update to the source property (isPush = true).

[IMAGE alt='' src='']

###### Simulation of the *WaterTankSystem* part usage.

#### PANEL: Syntax example

Syntax example

interfacedefControlToTankInterface{ 
endp1: ~PortDefs::ValvePort;// Conjugated port (source) 
endp2:PortDefs::ValvePort;// Standard port (target) 
flowfromp1.valvetop2.valve;// flow 
} 
 
// Usage in a system contextinterface:ControlToTankInterfaceconnectcontroller.valvePorttowaterTank.valvePort;

###### Binding connections

Binding connectorsare utilized to map specific primitive FeatureValues directly to one another. This ensures that two features always share the same value throughout the simulation lifecycle.

#### PANEL: Syntax example

Syntax example

partdefVehicle{ 
attributemass;partengine{ 
attributeengineMass;}// Binding the engine's mass attribute to a local featurebindengine.engineMass=mass;

###### Runtime error handling

To ensure model integrity, the execution engine enforces strict rules during value assignments. Violations result in informative messages in the Simulation Console

| Condition | Engine Action | Console Info Message |
| --- | --- | --- |
| Bound Value | Assignment skipped | [Feature] := [Value] - failed because the value is bound. |
| Incompatible Type | Assignment skipped | [Feature] := [Value] - failed due to incompatible types. |
| Real to Integer | Value is trimmed at the "." | [Feature] := [Value] - value changed from Real to Integer. |

###### Visual Execution Tracing

The simulation provides real-time visual feedback to help users trace the path of payloads and data.

- Visited/Last Visited When a payload is transferred via a port usage, the entire path—from the source port, through the c onnection/interface, to the destination—is highlighted.
- Handling Ambiguity If a port has multiple outgoing connections/interfaces and the specific target is not pre-defined, the engine annotates all possible paths and connectors to signify potential interaction routes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">This chapter defines the<span> </span>structure concepts and connectivity<span> </span>supported by the simulation engine. It outlines how SysML v2 architectural elements are transformed from static definitions into dynamic, executable models, focusing on data propagation, interface contracts, and runtime validation. </p><h3 style="text-align: left;">Supported elements</h3><p style="text-align: left;">The simulation engine supports execution of the SysML v2 structure elements listed in the table below.</p><p style="text-align: left;">In the <strong>Executable</strong> column, the following symbols mark whether elements are supported or not:</p><ul><li style="text-align: left;" data-uuid="f22aecdb-8efc-4be9-9f08-07baecaaf569"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image> - Supported elements</li><li style="text-align: left;" data-uuid="91838cec-2477-405c-bc81-11bdc339d666"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image> - Partially supported elements</li><li style="text-align: left;" data-uuid="53e24025-7013-4575-81cc-6f1a57cc3f85"><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image> - Unsupported elements</li></ul><table class="relative-table wrapped" style="width: 69.863%;"><colgroup><col style="width: 12.245%;" /><col style="width: 33.0459%;" /><col style="width: 8.79132%;" /><col style="width: 45.9189%;" /></colgroup><tbody><tr><th style="text-align: center;" scope="row">SysML v2 Concept</th><th style="text-align: center;" scope="col">Specification details</th><th style="text-align: center;" scope="col">Executable</th><th style="text-align: center;" scope="col">Notes</th></tr><tr><th scope="row">Part Def</th><td>PartDef</td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p><p><br /></p></div></td><td><br /></td></tr><tr><th rowspan="7" scope="rowgroup">Part Usage</th><td>Part Usage</td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p><p><br /></p></div></td><td><br /></td></tr><tr><td>partUsage<span> </span><strong>:</strong><span> </span>PartDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage :&gt;&gt; partUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage :&gt; partUsage</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage<span> </span><strong><span class="error">[1..*]</span><span> </span>ordered nonunique</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td><strong>ref</strong><span> </span>partUsage : PartDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>partUsage_1<span> </span><strong>=</strong><span> </span>partUsage_2</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th scope="row">Port Def</th><td><pre class="code-java">port def FuelingPort {
attribute flowRate : Real;
out fuelOut : Fuel;
in fuelReturn : Fuel;
}</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><br /></p><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p><p><br /></p></div></td><td>The simulation does not check the direction of a directed Feature, meaning the payload is transferred without verifying if it complies with the port definition</td></tr><tr><th rowspan="3" scope="rowgroup">Port Usage</th><td>portUsage : PortDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>portUsage : ~PortDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>Nested ports<pre class="code-java">port p0 : PortDef {
 port p1 : PortDef;
 port p2 : PortDef;
 port p3 : PortDef;} </pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th scope="row">Connection Def</th><td><em>connection def</em><br /><em>ConnectionDef1 {</em><br /><em>end part end1 : Part1;</em><br /><em>end part end2 : Part2;</em><br /><em>}</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th rowspan="2" scope="rowgroup">Connection Usage</th><td><em>connection connection1 :</em><em>ConnectionDef1</em><br /><em>connect part1.port to</em><span> </span><em>part2.port;</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td>All ConnectionUsage functions as delegation.</td></tr><tr><td>Connection (n-ary<em>{</em>}with 3 ends)<br /><em>connection connection1 :</em><span> </span><em>ConnectionDef1</em><br /><em>connect (part1,</em><em>part2, part3);</em></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th scope="row">Binding Connection</th><td><em>binding bind attributeUsage = attributeUsage;</em><br /> </td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Binding works only between attribute usages of primitive types.</td></tr><tr><th scope="row">Interface Def</th><td>interface def ControlToTankInterface { endp1 : ~ValvePort; endp2 :ValvePort; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td>If a flow is specified between attribute usages of primitive types, the value flows according to the specification.</td></tr><tr><th scope="row">Interface Usage</th><td>interface : ControlToTankInterface connect controller.valvePort to waterTank.valvePort;</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td>All InterfaceUsage functions as a delegation.</td></tr><tr><th scope="row">Flow</th><td>interface def ControlToTankInterface { endp1 : ~:ValvePort; endp2 :ValvePort; flow from p1.valve to p2.valve; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Flows are supported only when specified in the Interface Definition</td></tr><tr><th scope="row">Attribute Def</th><td>attribute def Dimensions { attributelength :Real; attributewidth :Real; attributeheight :Real; }</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th rowspan="7" scope="rowgroup">Attribute Usage</th><td>attributeUsage:ScalarValues::Real</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Only primitive type (Integer, Real, String, Boolean)<br />Units are not supported.</td></tr><tr><td>attributeUsage : EnumerationDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attributeUsage:mass</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="partialy_supported.png" /></ac:image></p></div></td><td>Units are not supported.</td></tr><tr><td>attributeUsage = expression</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attributeUsage := expression</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attribute:AttributeDef</td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td>attribute:AttributeDef<span> </span><span class="error">[1..*]</span></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><th rowspan="2" scope="rowgroup">Enumeration</th><td><pre class="code-java"><span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> def EnumerationDef1
{
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> enum1;
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> enum2;
}
</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="supported.png" /></ac:image></p></div></td><td><br /></td></tr><tr><td><pre class="code-java"><span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> def EnumerationDef1
{
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> = value1[unit1];
<span class="code-keyword" style="color:var(--ds-text-accent-magenta,#943d73);">enum</span> = value2[unit2];
}
</pre></td><td style="text-align: center;"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:width="16"><ri:attachment ri:filename="unsupported.png" /></ac:image></p></div></td><td><br /></td></tr></tbody></table><h3 style="text-align: left;">Connectivity</h3><p style="text-align: left;">Connectivity in SysML v2 simulation moves beyond static structural definitions to specify how elements<span> </span>dynamically interact<span> </span>during execution. The simulation engine enforces strict rules for data exchange, payload routing, and state synchronization to ensure model fidelity.</p><h4>Interfaces</h4><p style="text-align: left;">Interfaces serve as the formal contract between structural parts. They define the structured interaction points where data, energy, or material (modeled as<span> </span>flowUsages) cross system boundaries.</p><p style="text-align: left;">Key Applications:</p><ul style="text-align: left;"><li data-uuid="2e5d92b7-1ed2-42e4-a147-e5733c736655"><strong>Component Decoupling<br /></strong>Define<span> </span><em>how</em><span> </span>components interact (ports and flows) without being dependent on their internal state machine logic or private behaviors.</li><li data-uuid="e8526512-9a86-467a-ad39-13bcf054e1e1"><strong>Automated Data Propagation<br /></strong>Ensure that a value change in a source component is automatically reflected in the connected target component.</li><li data-uuid="634d2a10-4fc7-40d9-90cf-97d1f33290e9"><strong>Payload Routing<br /></strong>Facilitate the movement of discrete messages or physical items through defined ports.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="simulation_of_interconnection_view.png" /></ac:image></p><h6 style="text-align: center;">Simulation of the <em>FlashingLightSystem</em> part usage.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="d7dd4c17-3106-4fec-ad62-9b8dce29e288"><ac:parameter ac:name="title">Syntax example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">ButtonToTimerInterface</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">ButtonPort</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">TimerInPort</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">flow</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">of</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">from</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">flow</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">of</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Stop</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">from</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">start</span><span style="color:var(--ds-text,#000000);">;</span><br /><span style="color:var(--ds-text,#000000);">    }<br /><br /></span><span style="color:var(--ds-text,#000000);"><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Usage in a system context</span><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-chart-gray-bold,#8590a2);">  </span><span style="color:var(--ds-text,#000000);">:  </span><span style="color:var(--ds-text-accent-teal,#206a83);">ButtonToTimerInterface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">connect</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">button</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">buttonOut</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">timer</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">timerIn</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2ed2d87e-6ea2-444d-80d1-10e98cde3e92"><ac:rich-text-body>Payloads can also be transferred using a connection usage.</ac:rich-text-body></ac:structured-macro><h4>Flows</h4><p style="text-align: left;">The simulation engine executes<span> flow usages </span>defined within an<span> i</span>nterface definition. The behavior of these flows follows specific operational semantics:</p><ul style="text-align: left;"><li data-uuid="36ed582c-0d05-4c7f-b1d0-9411a1bae7a0"><strong>Data Transfer (Non-Destructive)<br /></strong>By default, transfers are executed as a<span> </span><strong>copy</strong><span> </span>operation. The source value remains intact while an identical instance is propagated to the target (isMove = false).</li><li data-uuid="eb18560c-1259-4ca9-8063-95d490e618d3"><strong>Propagation Trigger (Push)<br /></strong>Value transfer is reactive. It is initiated immediately upon an update to the source property (isPush = true).</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="simulation_of_part_usage.png" /></ac:image></p><h6 style="text-align: center;">Simulation of the <em>WaterTankSystem</em> part usage.</h6><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a486f46f-9ef6-4908-8bcf-158acafffe86"><ac:parameter ac:name="title">Syntax example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">ControlToTankInterface</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);"> : ~</span><span style="color:var(--ds-text-accent-teal,#206a83);">PortDefs::ValvePort</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Conjugated port (source)</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">end</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);"> : </span><span style="color:var(--ds-text-accent-teal,#206a83);">PortDefs::ValvePort</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Standard port (target)</span><br /><span style="color:var(--ds-text,#000000);">        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">flow</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">from</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p1</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valve</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">p2</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valve</span><span style="color:var(--ds-text,#000000);">; </span><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// flow</span><br /><span style="color:var(--ds-text,#000000);">    }<br /><br /><span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Usage in a system context<br /></span></span><span style="color:var(--ds-text-accent-blue,#0055cc);">interface</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text,#000000);"> :  </span><span style="color:var(--ds-text-accent-teal,#206a83);">ControlToTankInterface</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">connect</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">controller</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valvePort</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">to</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">waterTank</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">valvePort</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><h4 class="code-java">Binding connections</h4><p style="text-align: left;">Binding connectors<span> </span>are utilized to map specific primitive FeatureValues directly to one another. This ensures that two features always share the same value throughout the simulation lifecycle.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="07effaab-9da3-41ea-8c0a-4ad3030ce28a"><ac:parameter ac:name="title">Syntax example</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text-accent-blue,#0055cc);">part</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue,#0055cc);">def</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-teal,#206a83);">Vehicle</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">                </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">mass</span><span style="color:var(--ds-text,#000000);">;<br /><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">                part</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engine</span><span style="color:var(--ds-text,#000000);"> {</span><br /><span style="color:var(--ds-text,#000000);">                        </span><span style="color:var(--ds-text-accent-blue,#0055cc);">attribute</span><span style="color:var(--ds-chart-gray-bold,#8590a2);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engineMass;<span style="color:var(--ds-text,#000000);"><br />                }<br /><br /></span></span><span class="code-comment" style="color:var(--ds-background-accent-gray-bolder,#626f86);">                <span style="color:var(--ds-icon-accent-lime,#6a9a23);">// Binding the engine's mass attribute to a local feature</span><br /></span><span style="color:var(--ds-text-accent-blue,#0055cc);">                bind</span><span style="color:var(--ds-text,#000000);"> </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engine</span><span style="color:var(--ds-text,#000000);">.</span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">engineMass</span><span style="color:var(--ds-text,#000000);"> = </span><span style="color:var(--ds-text-accent-blue-bolder,#09326c);">mass</span><span style="color:var(--ds-text,#000000);">;</span></p></ac:rich-text-body></ac:structured-macro><h4>Runtime error handling</h4><p style="text-align: left;">To ensure model integrity, the execution engine enforces strict rules during value assignments. Violations result in informative messages in the Simulation Console</p><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th scope="col">Condition</th><th scope="col">Engine Action</th><th scope="col">Console Info Message</th></tr><tr><td><strong>Bound Value</strong></td><td>Assignment skipped</td><td> <span class="error">[Feature]</span><span> </span>:=<span> </span><span class="error">[Value]</span><span> </span>- failed because the value is bound.</td></tr><tr><td><strong>Incompatible Type</strong></td><td>Assignment skipped</td><td> <span class="error">[Feature]</span><span> </span>:=<span> </span><span class="error">[Value]</span><span> </span>- failed due to incompatible types.</td></tr><tr><td><strong>Real to Integer</strong></td><td>Value is trimmed at the &quot;.&quot;</td><td> <span class="error">[Feature]</span><span> </span>:=<span> </span><span class="error">[Value]</span><span> </span>- value changed from Real to Integer.</td></tr></tbody></table><h4>Visual Execution Tracing</h4><p style="text-align: left;">The simulation provides real-time visual feedback to help users trace the path of payloads and data.</p><ul style="text-align: left;"><li data-uuid="b664ae19-f563-4ae0-88af-00eee24af2cb"><strong>Visited/Last Visited<br /></strong>When a payload is transferred via a<span> </span>port usage, the entire path—from the source port, through the<span> c</span>onnection/interface, to the destination—is highlighted.</li><li data-uuid="470bca55-7124-4029-ab8a-25c4385cc509"><strong>Handling Ambiguity<br /></strong>If a port has multiple outgoing connections/interfaces and the specific target is not pre-defined, the engine annotates<span> </span><em>all</em><span> </span>possible paths and connectors to signify potential interaction routes.</li></ul>
````

<!--NOMAGIC_PAGE id=301367472 space=SYSML2SP version=13 -->
## PAGE 00028: SyML v2 Simulation window

- page_id: `301367472`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/301367472/SyML+v2+Simulation+window
- version_number: 13
- version_date: `2026-05-06T14:47:15.674+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

The**SysML v2****Simulation** window is the primary interface for controlling and monitoring simulation execution. It provides access to runtime values, execution logs, charts, and data export functionality.

The window appears automatically when the simulation starts and remains active until the simulation is terminated.

[IMAGE alt='' src='']

###### SysML v2 Simulation window

The **SysML v2 Simulation** window contains the following panels that allow you to observe and manage simulation execution:

- Console Panel - Displays simulation messages and logs, including informational messages, warnings, and errors generated during simulation execution.
- Variables Panel - Displays runtime values of model variables. Values are updated dynamically as the simulation progresses.

##### Console panel

The**Console**panel displays messages generated during simulation execution. These messages provide information about simulation events, warnings, and errors that occur during the simulation. You can use the **Console** panel to monitor simulation behavior and diagnose issues in the model.

The following table describes the types of messages displayed in the **Console** panel.

| Message Type | Description |
| --- | --- |
| Information | Provide general information about simulation progress and execution events. |
| Warnings | Indicate potential modeling issues that may affect the simulation behavior. |
| Errors | Indicate problems that prevent the simulation from continuing correctly. |

The **Console** panel is useful for diagnosing simulation issues. When troubleshooting simulation problems, the console should be the first place to check for diagnostic information.

Use the panel to monitor execution logs to:

- Track simulation events
- Detect modeling errors
- Identify the requirement verification results
- Understand simulation behavior

##### Variables panel

The**Variables** panel displays runtime values of model elements during simulation. It allows you to observe how values change during the simulation.

Variables are organized in a hierarchical tree structure that reflects the structure of the simulated model. Each node represents a model element such as a part, attribute, reference, or port.

You can expand or collapse nodes to explore nested elements and monitor specific runtime values.

The **Variables** panel can display the following runtime elements:

- Part usages
- Attribute usages
- Reference usages
- Port usages
- Satisfy requirements

You can also use the Variables panel to open a [CONFLUENCE_PAGE title='Time Series Chart' space=''] and [CONFLUENCE_PAGE title='Exporting simulation data to CSV' space=''].

##### Simulation controls

The **SysML v2 Simulation** window toolbar provides the following controls for managing the simulation execution.

| Control | Icon | Description |
| --- | --- | --- |
| Start |  | Begins the simulation execution. |
| Pause |  | Temporarily suspends the simulation execution. |
| Resume |  | Continues the simulation execution after pausing. |
| Step |  | Executes a single simulation time step. |
| Terminate |  | Terminates the current simulation. |
| Speed Slider |  | Adjusts the simulation execution speed. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The<span> <strong>SysML v2 </strong></span><strong>Simulation</strong> window is the primary interface for controlling and monitoring simulation execution. It provides access to runtime values, execution logs, charts, and data export functionality.</p><p style="text-align: left;">The window appears automatically when the simulation starts and remains active until the simulation is terminated.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="sysml_v2_simulation_window.png" /></ac:image></p><h6 style="text-align: center;">SysML v2 Simulation window</h6><p style="text-align: left;">The <strong>SysML v2 Simulation</strong> window contains the following panels that allow you to observe and manage simulation execution:</p><ul style="text-align: left;"><li data-uuid="50733de9-b896-459a-abea-3de6f521ebf9"><strong>Console Panel</strong><span> </span>- Displays simulation messages and logs, including informational messages, warnings, and errors generated during simulation execution.</li><li data-uuid="7ea510ab-1e47-42ee-8088-96d9c4c82601"><strong>Variables Panel</strong><span> </span>- Displays runtime values of model variables. Values are updated dynamically as the simulation progresses.</li></ul><h3>Console panel</h3><p style="text-align: left;">The<span> </span><strong>Console </strong>panel displays messages generated during simulation execution. These messages provide information about simulation events, warnings, and errors that occur during the simulation. You can use the <strong>Console</strong> panel to monitor simulation behavior and diagnose issues in the model.</p><p style="text-align: left;">The following table describes the types of messages displayed in the <strong>Console</strong> panel.</p><table class="wrapped"><tbody class=""><tr class=""><th style="text-align: center;">Message Type</th><th style="text-align: center;">Description</th></tr><tr class=""><td><strong>Information</strong></td><td>Provide general information about simulation progress and execution events.</td></tr><tr class=""><td><strong>Warnings</strong></td><td>Indicate potential modeling issues that may affect the simulation behavior.</td></tr><tr class=""><td><strong>Errors</strong></td><td>Indicate problems that prevent the simulation from continuing correctly.</td></tr></tbody></table><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="d0284f6f-2f40-47f5-b759-f5878dac59c2"><ac:rich-text-body><p>The <strong>Console</strong> panel is useful for diagnosing simulation issues. When troubleshooting simulation problems, the console should be the first place to check for diagnostic information.</p><p>Use the panel to monitor execution logs to:</p><ul><li data-uuid="b052858f-634f-4ab4-b817-0aacabfcc34d">Track simulation events</li><li data-uuid="5435d369-f9d2-4127-9dc1-8e194f757fd6">Detect modeling errors</li><li data-uuid="68f94f54-937b-4ec7-b8de-1957872e5753">Identify the requirement verification results</li><li data-uuid="aa62e112-6fd9-4052-a8fc-18752f161ce0">Understand simulation behavior</li></ul></ac:rich-text-body></ac:structured-macro><h3 style="text-align: left;">Variables panel</h3><p style="text-align: left;">The<span> </span><strong>Variables</strong> panel displays runtime values of model elements during simulation. It allows you to observe how values change during the simulation.</p><p style="text-align: left;">Variables are organized in a hierarchical tree structure that reflects the structure of the simulated model. Each node represents a model element such as a part, attribute, reference, or port.</p><p style="text-align: left;">You can expand or collapse nodes to explore nested elements and monitor specific runtime values.</p><p style="text-align: left;">The <strong>Variables</strong> panel can display the following runtime elements:</p><ul style="text-align: left;"><li data-uuid="3314e180-3de0-4e3f-bb5c-bc218178ce42">Part usages</li><li data-uuid="c1ee549b-58e4-461a-8250-c82c335e8e8d">Attribute usages</li><li data-uuid="da2791da-be9b-478f-b881-d0ade0389c89">Reference usages</li><li data-uuid="42ae10ea-ceee-4954-8dbf-9f25edb821b8">Port usages</li><li data-uuid="1760def3-8428-48b6-a6ce-6f7a24293bb5">Satisfy requirements</li></ul><p>You can also use the Variables panel to open a <ac:link><ri:page ri:content-title="Time Series Chart" /></ac:link> and <ac:link><ri:page ri:content-title="Exporting simulation data to CSV" /><ac:plain-text-link-body><![CDATA[export simulation data to CSV]]></ac:plain-text-link-body></ac:link>.</p><h3 style="text-align: left;">Simulation controls</h3><p style="text-align: left;">The <strong>SysML v2 Simulation</strong> window toolbar provides the following controls for managing the simulation execution.</p><table class="wrapped"><tbody class=""><tr class=""><th style="text-align: center;">Control</th><th style="text-align: center;">Icon</th><th style="text-align: center;">Description</th></tr><tr class=""><td><strong>Start</strong></td><td><div class="content-wrapper"><p style="text-align: center;"><strong><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="start.png" /></ac:image><br /></strong></p></div></td><td>Begins the simulation execution.</td></tr><tr class=""><td><strong>Pause</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="pause.png" /></ac:image><br /></strong></p></div></td><td>Temporarily suspends the simulation execution.</td></tr><tr class=""><td><strong>Resume</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image><ri:attachment ri:filename="resume.png" /></ac:image><br /></strong></p></div></td><td>Continues the simulation execution after pausing.</td></tr><tr class=""><td><strong>Step</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image><ri:attachment ri:filename="step.png" /></ac:image><br /></strong></p></div></td><td>Executes a single simulation time step.</td></tr><tr class=""><td><strong>Terminate</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image><ri:attachment ri:filename="terminate.png" /></ac:image><br /></strong></p></div></td><td>Terminates the current simulation.</td></tr><tr class=""><td><strong>Speed Slider</strong></td><td style="text-align: center;"><div class="content-wrapper"><p><strong><ac:image ac:thumbnail="true" ac:height="14"><ri:attachment ri:filename="speed.png" /></ac:image><br /></strong></p></div></td><td>Adjusts the simulation execution speed.</td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=291833503 space=SYSML2SP version=6 -->
## PAGE 00029: SysML v2 Simulation Plugin Documentation

- page_id: `291833503`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/291833503/SysML+v2+Simulation+Plugin+Documentation
- version_number: 6
- version_date: `2026-06-30T09:56:25.412+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

lightgrey

The SysML v2 Simulation Plugin is in the Technology Preview phase. We do not recommend using it for long-term projects because there might be future changes affecting its functionality.

The SysML v2 Simulation Plugin enables execution of SysML v2 models to validate system behavior before implementation. It supports testing design logic, verifying requirements, and analyzing dynamic system interactions within a model-based systems engineering (MBSE) environment.

##### Why is Simulation Needed?

In today’s complex system environments, static models alone are not sufficient. Simulation provides:

- Early validation of system behavior
- Detection of design gaps and logical errors
- Improved requirement verification and traceability
- Greater confidence before committing to implementation

##### Business Benefits

Adopting simulation within MBSE delivers measurable value:

- Reduced development costs through early defect detection
- Shorter development cycles and faster time to market
- Improved product quality and compliance
- Lower project risk and better stakeholder alignment

The following topics explain how to install and use the SysML v2 Simulation Plugin:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3ea9e360-7173-4f87-b85d-2c3fb48cdac4"><ac:parameter ac:name="bgColor">lightgrey</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">The SysML v2 Simulation Plugin is in the Technology Preview phase. We do not recommend using it for long-term projects because there might be future changes affecting its functionality.</span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;">The SysML v2 Simulation Plugin enables execution of SysML v2 models to validate system behavior before implementation. It supports testing design logic, verifying requirements, and analyzing dynamic system interactions within a model-based systems engineering (MBSE) environment.</p><h3 style="text-align: left;">Why is Simulation Needed?</h3><p style="text-align: left;">In today’s complex system environments, static models alone are not sufficient. Simulation provides:</p><ul><li style="text-align: left;" data-uuid="293db28c-656d-43c1-a2c9-cb3e576fab0d">Early validation of system behavior</li><li data-uuid="9faf20da-b1ce-42a8-9d00-6f3c82deaadd">Detection of design gaps and logical errors</li><li data-uuid="4ad43ae4-06f5-45ed-9cca-b4258bfa4fe8">Improved requirement verification and traceability</li><li data-uuid="2932948a-4c07-46ad-8d9c-00f4a8d6488d">Greater confidence before committing to implementation</li></ul><h3 style="text-align: left;">Business Benefits</h3><p style="text-align: left;">Adopting simulation within MBSE delivers measurable value:</p><ul style="text-align: left;"><li data-uuid="aeeddda1-7eb5-4559-97dc-8a8e70ba03fc">Reduced development costs through early defect detection</li><li data-uuid="e92210aa-b2e9-4d3b-9c9a-98395fc1bc77">Shorter development cycles and faster time to market</li><li data-uuid="17f4a7e5-090e-4b3c-b1e2-84e0134d2034">Improved product quality and compliance</li><li data-uuid="2104fcff-9945-42be-a6e5-e86287e934d9">Lower project risk and better stakeholder alignment</li></ul><p style="text-align: left;">The following topics explain how to install and use the SysML v2 Simulation Plugin:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="0ca80646-7181-4acd-a5e5-6af2f4a2224c" /></p>
````

<!--NOMAGIC_PAGE id=304001305 space=SYSML2SP version=14 -->
## PAGE 00030: Time Series Chart

- page_id: `304001305`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/304001305/Time+Series+Chart
- version_number: 14
- version_date: `2026-06-22T15:11:41.630+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide > SyML v2 Simulation window
- labels: []

### NORMALIZED CONTENT

The **Variables** panel allows you to visualize variable values over time using a Time Series Chart. The chart displays time-series data for numerical variables during the simulation.

[IMAGE alt='' src='']

###### Time Series Chart

##### Opening Time Series Chart

To open a Time Series Chart

1. In the **Variables** panel, select the check boxes for one or more numerical attributes or references.
2. In the panel toolbar, click [IMAGE alt='' src='']. 
[IMAGE alt='' src='']

The chart window opens and displays attribute values starting from the moment it is opened.You can open multiple Time Series Charts simultaneously.

##### Adding variables to an open chart

To add additional variables to an existing chart:

1. Select one or more **numerical attributes** or **references** using checkboxes or directly from the variable tree.
2. Right-click the selected variables.
3. Select **Insert to Chart**. 
[IMAGE alt='' src='']

The selected variable is added to the chart visualization.

##### Chart display options

You can choose from several visualization options in an open Time Series Chart for better readability and easier analysis of the chart.

To configure Time Series Chart display options

- In an open Time Series Chart, click [ATTACHMENT filename='chart_settings.png'] and select one or several of the following options:
  - **Interpolation (Linear)** - to display the chart as either a curvilinear or linear line.
  - **Show Data Points** - to show or hide data points on the chart lines.
  - **Show Values** - to show or hide numeric values in the chart.

##### Exporting chart data

You can export the data of an open Time Series Chart to multiple formats for external use.Available export formats are:PNG,JPEG,SVG,CSV, andXLS.

Exported chart data can be useful for data analysis, reports, or documetnation.

To export Time Series Chart data

1. In an open Time Series Chart, click [IMAGE alt='' src=''] and select one of the following options:
  - Download PNG image
  - Download JPEG image
  - Download SVG vector image
  - Download CSV
  - Download XLS
2. In an open window, select the directory where you want to save the file.
3. Optionally, change the file name.
4. Click the Save button.

The file is downloaded to your selected location.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The <strong>Variables</strong> panel allows you to visualize variable values over time using a Time Series Chart. The c</span><span style="color:var(--ds-text,#172b4d);">hart displays time-series data for numerical variables during the simulation.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);"><ac:image ac:align="center"><ri:attachment ri:filename="time_series_chart_window.png" /></ac:image></span></p><h6 style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">Time Series Chart</span></h6><h3 style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Opening Time Series Chart</span></h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To open a Time Series Chart</span></p><hr /><ol style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="0a66947c-ca5f-456d-a8e7-7cd1193f36fa"><span style="color:var(--ds-text,#172b4d);">In the <strong>Variables</strong> panel, select the check boxes for one or more numerical attributes or references.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="ec639d9a-d7e7-4c21-93ae-b7f22992a72e"><span style="color:var(--ds-text,#172b4d);">In the panel toolbar, click <ac:image><ri:attachment ri:filename="time_series_chart.png" /></ac:image>.<br /><ac:image><ri:attachment ri:filename="opening_time_series_chart.png" /></ac:image></span></li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The chart window opens and displays attribute values starting from the moment it is opened. </span><span style="color:var(--ds-text,#172b4d);">You can open multiple Time Series Charts simultaneously.</span></p><h3 style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Adding variables to an open chart</span></h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To add additional variables to an existing chart:</span></p><ol style="text-align: left;"><li style="color:var(--ds-text,#172b4d);" data-uuid="561739e9-f987-4a0c-a75a-201d966cc326"><span style="color:var(--ds-text,#172b4d);">Select one or more <strong>numerical attributes</strong> or <strong>references</strong> using checkboxes or directly from the variable tree.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="f76cc750-6c2a-4eb4-88f5-64b4563689b8"><span style="color:var(--ds-text,#172b4d);">Right-click the selected variables.</span></li><li style="color:var(--ds-text,#172b4d);" data-uuid="70539c81-1089-4c5f-82ad-7f053e1ed242"><span style="color:var(--ds-text,#172b4d);">Select <strong>Insert to Chart</strong>.<br /><ac:image><ri:attachment ri:filename="inserting_variables_to_chart.png" /></ac:image><br /></span></li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The selected variable is added to the chart visualization.</span></p><h3 style="text-align: left;">Chart display options</h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">You can choose from several visualization options in an open Time Series Chart for better readability and easier analysis of the chart.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">To configure Time Series Chart display options</span></p><hr /><ul><li data-uuid="5244d5d7-6428-4625-b4e9-5f2fea82e25b">In an open Time Series Chart, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="chart_settings.png" /></ac:image> and select one or several of the following options:<ul><li data-uuid="8197fe1f-9bf1-468d-b24e-4e1f004103e1"><span style="color:var(--ds-text,#172b4d);"><strong>Interpolation (Linear)</strong> - to display the chart as either a curvilinear or linear line.</span></li><li data-uuid="4c379191-e8b6-44a7-8ce9-7e6011f17284"><span style="color:var(--ds-text,#172b4d);"><strong>Show Data Points</strong> - to show or hide data points on the chart lines.</span></li><li data-uuid="6298fb23-d84b-426b-ae4c-5bfb5534e8fd"><span style="color:var(--ds-text,#172b4d);"><strong>Show Values</strong> - to show or hide numeric values in the chart.</span></li></ul></li></ul><h3><span style="color:var(--ds-text,#172b4d);">Exporting chart data</span></h3><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">You can export the data of an open Time Series Chart to multiple formats for external use. </span><span style="color:var(--ds-text,#172b4d);">Available export formats are: </span><span style="color:var(--ds-text,#172b4d);">PNG, </span><span style="color:var(--ds-text,#172b4d);">JPEG, </span><span style="color:var(--ds-text,#172b4d);">SVG, </span><span style="color:var(--ds-text,#172b4d);">CSV, and </span><span style="color:var(--ds-text,#172b4d);">XLS.</span></p><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">Exported chart data can be useful for data analysis, reports, or documetnation.</span></p><p style="color:var(--ds-text,#172b4d);"><span style="color:var(--ds-text,#172b4d);">To export Time Series Chart data</span></p><hr /><ol><li style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">In an open Time Series Chart, click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="export_chart_data.png" /></ac:image> and select one of the following options:</span><ul><li style="text-align: left;"><strong>Download PNG image</strong></li><li style="text-align: left;font-weight: bold;" data-uuid="c81ae603-6bbe-472f-9643-67590745c8bf"><strong>Download JPEG image</strong></li><li style="text-align: left;" data-uuid="f16fdaa2-5b33-4613-b738-66aa186fde71"><strong>Download SVG vector image</strong></li><li style="text-align: left;" data-uuid="74c76e52-3140-451b-aef0-bcad0bb4291c"><strong>Download CSV</strong></li><li style="text-align: left;" data-uuid="993049a0-7ae4-4bba-a395-76b890677b27"><strong>Download XLS</strong></li></ul></li><li style="text-align: left;" data-uuid="a8c4b0e6-0973-4b84-84bc-58d00416a006">In an open window, select the directory where you want to save the file.</li><li style="text-align: left;" data-uuid="210b088c-b8d6-4bd0-848e-43a2c436b3f8">Optionally, change the file name.</li><li style="text-align: left;" data-uuid="965a630c-cf6b-4451-a419-2987a14da1f0">Click the <strong>Save</strong> button.</li></ol><p style="text-align: left;"><span style="color:var(--ds-text,#172b4d);">The file is downloaded to your selected location.</span></p>
````

<!--NOMAGIC_PAGE id=298094608 space=SYSML2SP version=3 -->
## PAGE 00031: User guide

- page_id: `298094608`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/298094608/User+guide
- version_number: 3
- version_date: `2026-04-01T12:41:39.881+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation
- labels: []

### NORMALIZED CONTENT

The SysML v2 Simulation Plugin user guide explains how to execute SysML v2 models to validate system behavior, verify requirements, analyze dynamic scenarios, and identify design issues early in the MBSE process.

#### NOTE: SysML v2 Simulation Plugin - Technology Preview

SysML v2 Simulation Plugin - Technology Preview

The SysML v2 Simulation Plugin is provided as a technology preview. We do not recommend using it to create any long-term projects because there might be future changes affecting its functionality.

For information about generic SysML v2 modeling features, including using the textual notation, see the [SysML v2 Plugin documentation](https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&version=latest).

To learn more, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">The SysML v2 Simulation Plugin user guide explains how to execute SysML v2 models to validate system behavior, verify requirements, analyze dynamic scenarios, and identify design issues early in the MBSE process.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7269f27a-a013-4360-a1a5-0dd498f6ef22"><ac:parameter ac:name="title">SysML v2 Simulation Plugin - Technology Preview</ac:parameter><ac:rich-text-body>The SysML v2 Simulation Plugin is provided as a technology preview. We do not recommend using it to create any long-term projects because there might be future changes affecting its functionality.</ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f0f8e034-bdef-4bad-9db3-36961de8057f"><ac:rich-text-body><p>For information about generic SysML v2 modeling features, including using the textual notation, see the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=sysml-v2-plugin-documentation&amp;version=latest">SysML v2 Plugin documentation</a>.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"> To learn more, see the following topics:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9b84f3dd-7313-4b7a-bbd3-d1b7ab506897" /></p>
````

<!--NOMAGIC_PAGE id=314180706 space=SYSML2SP version=6 -->
## PAGE 00032: Using expressions

- page_id: `314180706`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/314180706/Using+expressions
- version_number: 6
- version_date: `2026-06-19T14:48:37.578+02:00`
- ancestors: SysML v2 Simulation Plugin Documentation > User guide
- labels: []

### NORMALIZED CONTENT

The SysML v2 Simulation plugin supports the evaluation of feature values defined by expressions. Expressions may calculate values using operators (for example, arithmetic or comparison operations) or derive values by referencing other features in the model. Expressions can be applied to attributes and references to define computed or derived values within a model.

During simulation, expressions are evaluated automatically. When a runtime value is changed, all dependent expressions are recalculated.

If you initiate the simulation from a model view, the results of expression evaluation are displayed on element shapes to provide immediate runtime feedback. Evaluated values of attributes and references are displayed in blue and are updated dynamically as the simulation progresses. For more information, see [CONFLUENCE_PAGE title='Simulation information in views' space=''].

##### Supported value types

Expressions operate on:

- Primitive types (Integer, Real, Boolean, etc.)
- Enumeration values
- Feature references
- Collections (arrays/lists)

##### Supported operators

| Type | Operators |
| --- | --- |
| Arithmetic | + |
| - |  |
| * |  |
| / |  |
| Comparison | > |
| < |  |
| >= |  |
| <= |  |
| Equality | == |
| != |  |

##### Collections and aggregation functions

In the simulation context, expressions support collections (arrays/lists), which contain multiple values of a compatible type. Each element in a collection is evaluated individually. If any element in a collection is incompatible, the entire assignment is rejected. If values are converted during evaluation, those elements are also treated as incompatible.

You can use collections with the **sum(<list>)** function, which computes the total of all numeric elements in a collection and returns a single numeric value. This function can be used in any expression context that expects a numeric result.

##### Accessing nested features

Expressions support nested feature access using dot notation. This mechanism is available wherever feature values are used in simulation, including expressions, actions, event conditions, and message targets. It allows you to navigate structured model elements and access deeply nested values in complex systems.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The SysML v2 Simulation plugin supports the evaluation of feature values defined by expressions. Expressions may calculate values using operators (for example, arithmetic or comparison operations) or derive values by referencing other features in the model. Expressions can be applied to attributes and references to define computed or derived values within a model.</p><p>During simulation, expressions are evaluated automatically. When a runtime value is changed, all dependent expressions are recalculated.</p><p>If you initiate the simulation from a model view, the results of expression evaluation are displayed on element shapes to provide immediate runtime feedback. Evaluated values of attributes and references are displayed in blue and are updated dynamically as the simulation progresses. For more information, see <ac:link><ri:page ri:content-title="Simulation information in views" /></ac:link>.</p><h3>Supported value types</h3><p>Expressions operate on:</p><ul><li data-uuid="325c129a-9a25-474a-9408-8dacd20de7a5">Primitive types (Integer, Real, Boolean, etc.)</li><li data-uuid="9a7b2892-2447-4439-9bd4-a4fda02aa033">Enumeration values</li><li data-uuid="313c2271-9168-427a-be0e-45d4dd8cc683">Feature references</li><li data-uuid="1ffbc8c9-dd67-4578-95e7-c0582bbee4fa">Collections (arrays/lists)</li></ul><h3>Supported operators</h3><table class="relative-table wrapped" style="width: 23.8904%;"><colgroup class=""><col class="" style="width: 45.0591%;" /><col class="" style="width: 54.9445%;" /></colgroup><thead class=""><tr class=""><th>Type</th><th>Operators</th></tr></thead><tbody class=""><tr class=""><td rowspan="4">Arithmetic</td><td><code>+</code></td></tr><tr class=""><td><code>-</code></td></tr><tr class=""><td>*</td></tr><tr class=""><td>/</td></tr><tr class=""><td rowspan="4">Comparison<br /><br /><br /><br /></td><td><code>&gt;</code></td></tr><tr class=""><td>&lt;</td></tr><tr class=""><td>&gt;=</td></tr><tr class=""><td>&lt;=</td></tr><tr class=""><td rowspan="2">Equality</td><td><code>==</code></td></tr><tr class=""><td>!=</td></tr></tbody></table><h3>Collections and aggregation functions</h3><p>In the simulation context, expressions support collections (arrays/lists), which contain multiple values of a compatible type. Each element in a collection is evaluated individually. If any element in a collection is incompatible, the entire assignment is rejected. If values are converted during evaluation, those elements are also treated as incompatible.</p><p>You can use collections with the <strong>sum(&lt;list&gt;)</strong> function, which computes the total of all numeric elements in a collection and returns a single numeric value. This function can be used in any expression context that expects a numeric result.</p><h3>Accessing nested features</h3><p>Expressions support nested feature access using dot notation. This mechanism is available wherever feature values are used in simulation, including expressions, actions, event conditions, and message targets. It allows you to navigate structured model elements and access deeply nested values in complex systems.</p>
````

<!--NOMAGIC_PAGE id=291833514 space=SYSML2SP version=1 -->
## PAGE 00033: Versions of SysML v2 Simulation Plugin Documentation

- page_id: `291833514`
- space_key: `SYSML2SP`
- source_url: https://docs.nomagic.com/spaces/SYSML2SP/pages/291833514/Versions+of+SysML+v2+Simulation+Plugin+Documentation
- version_number: 1
- version_date: `2026-03-04T13:34:27.428+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

e42c5df24130f5aa406cdf6d562bc81a

SysML v2 Simulation Plugin Documentation

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="464793c1-0def-4938-9b9b-9122cfa21cbd"><ac:parameter ac:name="permaId">e42c5df24130f5aa406cdf6d562bc81a</ac:parameter><ac:parameter ac:name="documentTitle">SysML v2 Simulation Plugin Documentation</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````
