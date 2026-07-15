# NOMAGIC DOCUMENTATION SPACE: Validation Rules

<!--NOMAGIC_SPACE key=VR chunk=1 -->

<!--NOMAGIC_PAGE id=17684360 space=VR version=9 -->
## PAGE 00001: Action Behavior is not allocated

- page_id: `17684360`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684360/Action+Behavior+is+not+allocated
- version_number: 9
- version_date: `2021-02-11T09:51:26.025+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Allocations
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ActionBehavior

**Description**

This rule checks to see if the action or behavior is allocated to the Allocated Activity Partition when the swimlane's**Allocation Mode**is**Usage**.

**Severity**

warning****

**Constrained Element**

Action****

**Solvers**

**Allocate Action**- sets the same element in the **Allocated To** property value as defined in the Allocated Activity Partition.

**Example**

**[IMAGE alt='' src='']**

###### *Receive the regulator request* Action is allocated to *tr* Part Property.****

****

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ActionBehavior</p><p><strong>Description</strong></p><p>This rule checks to see if the action or behavior is allocated to the Allocated Activity Partition when the <span>swimlane's </span><strong>Allocation Mode</strong><span> is </span><strong>Usage</strong><span>.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Action<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Allocate Action </strong>- sets the same element in the <strong>Allocated To</strong> property value as defined in the Allocated Activity Partition.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="behavior_is_not_allocated.png" /></ac:image></strong></p><h6 style="text-align: center;"><em>Receive the regulator request</em> Action is allocated to <em>tr</em> Part Property.<strong><br /></strong></h6><p><strong><br /></strong></p><p><strong><br /></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985492 space=VR version=1 -->
## PAGE 00002: Active correctness validation rules

- page_id: `228985492`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985492/Active+correctness+validation+rules
- version_number: 1
- version_date: `2024-01-30T13:55:10.071+01:00`
- ancestors: Validation Rules > UAF validation rules
- labels: []

### NORMALIZED CONTENT

Active Validation instantly checks the accuracy, completeness, and correctness of a model, displays errors in the model, and suggests solutions.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Active Validation instantly checks the accuracy, completeness, and correctness of a model, displays errors in the model, and suggests solutions.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d1b96020-4e18-45b7-a9f8-84323172b748" /></p>
````

<!--NOMAGIC_PAGE id=243969479 space=VR version=1 -->
## PAGE 00003: Actor and Usecase

- page_id: `243969479`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969479/Actor+and+Usecase
- version_number: 1
- version_date: `2025-07-31T10:51:30.101+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ActorUsecase

**Description**

This validation rule checks if an Actor is associated with at least one Use Case.

**Severity**

info

**Constrained Element**

Actor

**Solvers**

- To fix this, make sure an Actor is associated with at least one Use Case.

**Example**

[IMAGE alt='' src='']

###### The Actor *User* is not associated with any Use Case. 
The error is resolved by drawing an Association relationship between the Actor and the Use Case *Provide comfortable temperature*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ActorUsecase</p><p><strong>Description</strong></p><p>This validation rule checks if an Actor is associated with at least one Use Case.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained Element</strong></p><p>Actor</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure an Actor is associated with at least one Use Case.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Actor_and_Usecase.png" /></ac:image></p><h6 style="text-align: center;">The Actor <em>User</em> is not associated with any Use Case. <br />The error is resolved by drawing an Association relationship between the Actor and the Use Case <em>Provide comfortable temperature</em>.</h6>
````

<!--NOMAGIC_PAGE id=64973742 space=VR version=35 -->
## PAGE 00004: AdjunctProperty

- page_id: `64973742`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/64973742/AdjunctProperty
- version_number: 35
- version_date: `2021-01-13T12:13:13.474+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ADJUNCT_SYNC

**Description**

This validation rule checks if property to which «adjunct»stereotype is applied meet the following constraints:

- Has the same name as the principal.
- Is owned by an element that owns the principal.
- If the principal is a Connector or CallAction, the Adjunct Property have to be composite.

**Severity**

warning****

**Constrained****element**

Property

**Solvers**

- Synchronize - synchronizes the Adjunct property to match its type, multiplicity, aggregation and NamdElement name.
- Set Principal - opens the Select Principal dialog to choose the principal for the Adjunct Property.

**Example**

**[IMAGE alt='' src='']**

###### The Adjunct Property name is the same as principal's.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ADJUNCT_SYNC</p><p><strong>Description</strong></p><p>This validation rule checks if property to which <span style="color: rgb(51,51,51);letter-spacing: 0.0px;">«</span>adjunct<span style="color: rgb(51,51,51);letter-spacing: 0.0px;">» </span>stereotype is applied meet the following constraints:</p><ul><li>Has the same name as the principal.</li><li>Is owned by an element that owns the principal.</li><li>If the principal is a Connector or CallAction, the Adjunct Property have to be composite.</li></ul><p><br /></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained</strong><strong> element</strong></p><p>Property</p><p><strong>Solvers</strong></p><ul><li><strong style="letter-spacing: 0.0px;">Synchronize</strong> - synchronizes the Adjunct property to match its type, multiplicity, aggregation and NamdElement name. </li><li><strong>Set Principal</strong> - opens the <strong>Select Principal</strong> dialog to choose the principal for the Adjunct Property.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="adjunctproperty.png" /></ac:image></strong></p><h6 style="text-align: center;">The Adjunct Property name is the same as principal's.</h6>
````

<!--NOMAGIC_PAGE id=64973744 space=VR version=13 -->
## PAGE 00005: BoundReference

- page_id: `64973744`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/64973744/BoundReference
- version_number: 13
- version_date: `2021-01-06T06:39:53.021+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

BOUND_SYNC

**Description**

This rule checks if property stereotyped by the «boundReference» is the role of the connector end of at least one binding connector, or generalized by such a property through redefinition. The roles of the connector ends are specified in the **Bound End** property value. The value of boundEnd is a connector end of a binding connector.

**Severity**

warning****

**Constrained****element**

Property

**Solvers**

- Synchronize - synchronizes the Bound Reference property by setting a role of the connector end in the Bound End property value.

**Example**

[IMAGE alt='' src='']

###### The *chs.rb* role of the connector end is specified for the *rb* Bound Reference property.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>BOUND_SYNC</p><p><strong>Description</strong></p><p>This rule checks if property stereotyped by the «boundReference» is the role of the connector end of at least one binding connector, or generalized by such a property through redefinition. The roles of the connector ends are specified in the <strong>Bound End</strong> property value. The value of boundEnd is a connector end of a binding connector.</p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained</strong><strong> element</strong></p><p>Property</p><p><strong>Solvers</strong></p><ul><li><strong>Synchronize</strong> - synchronizes the Bound Reference property by setting a role of the connector end in the <strong>Bound End</strong> property value.</li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="BOUND_SYNC.png" /></ac:image></p><h6 style="text-align: center;">The <em>chs.rb</em> role of the connector end is specified for the <em>rb</em> Bound Reference property.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17673183 space=VR version=12 -->
## PAGE 00006: BPMN validation rules

- page_id: `17673183`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17673183/BPMN+validation+rules
- version_number: 12
- version_date: `2025-08-18T18:19:16.646+02:00`
- ancestors: Validation Rules
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler has the functionality to check if a created BPMN model corresponds to the most important modeling rules defined in the Business Process Modeling and Notation (BPMN) standard. 
Cameo Business Modeler provides the following three validation suites to validate BPMN models:

BPMN2 Correctness, Completeness, and BPMN2 Export Completeness validation rules are available only in the Architect edition.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler has the functionality to check if a created BPMN model corresponds to the most important modeling rules defined in the Business Process Modeling and Notation (BPMN) standard. <br />Cameo Business Modeler provides the following three validation suites to validate BPMN models:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="4a241300-2262-45ad-a7e0-037516dfee1f" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cb66d723-1363-4c9d-bf03-b169c63763c4"><ac:rich-text-body>BPMN2 Correctness, Completeness, and BPMN2 Export Completeness validation rules are available only in the Architect edition.</ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=17675649 space=VR version=1 -->
## PAGE 00007: BPMN2 Completeness Validation Rules

- page_id: `17675649`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17675649/BPMN2+Completeness+Validation+Rules
- version_number: 1
- version_date: `2017-05-25T13:30:25.636+02:00`
- ancestors: Validation Rules > BPMN validation rules
- labels: []

### NORMALIZED CONTENT

The BPMN2 validation rules included in the BPMN2 Completeness validation rules suite are described in the table.

| Validation rule | Severity |
| --- | --- |
| An Intermediate Boundary Event should have an outgoing Sequence Flow. | Info |
| An Intermediate Event should have an incoming or outgoing Sequence Flow. | Info |
| An Error Code should be specified for an Error End Event. | Info |
| An Event-Based Gateway should have two or more outgoing Sequence Flows. | Info |
| An Event SubProcess will have one Start Event. | Warning |
| A Start Event shall have at least one outgoing Sequence Flow. | Warning |
| An Intermediate Event can have either an incoming or outgoing Message Flow. It cannot contain both. | Warning |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The BPMN2 validation rules included in the BPMN2 Completeness validation rules suite are described in the table.</p><table><colgroup><col /><col /></colgroup><tbody><tr><th>Validation rule </th><th><p>Severity</p></th></tr><tr><td><p>An Intermediate Boundary Event should have an outgoing Sequence Flow.</p></td><td><p>Info</p></td></tr><tr><td><span>An Intermediate Event should have an incoming or outgoing Sequence Flow. </span></td><td><span>Info</span></td></tr><tr><td><span>An Error Code should be specified for an Error End Event. </span></td><td><span>Info</span></td></tr><tr><td><span>An Event-Based Gateway should have two or more outgoing Sequence Flows. </span></td><td><span>Info</span></td></tr><tr><td><span>An Event SubProcess will have one Start Event. </span></td><td><p>Warning</p></td></tr><tr><td><span>A Start Event shall have at least one outgoing Sequence Flow. </span></td><td><span>Warning</span></td></tr><tr><td colspan="1"><span>An Intermediate Event can have either an incoming or outgoing Message Flow. It cannot contain </span><span>both.</span></td><td colspan="1"><span>Warning</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17675632 space=VR version=1 -->
## PAGE 00008: BPMN2 Correctness (Active) Validation Rules

- page_id: `17675632`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17675632/BPMN2+Correctness+Active+Validation+Rules
- version_number: 1
- version_date: `2017-05-25T13:07:22.710+02:00`
- ancestors: Validation Rules > BPMN validation rules
- labels: []

### NORMALIZED CONTENT

The BPMN correctness (active) validation rules defined in Cameo Business Modeler for BPMN2 projects are described in the table.

| Validation rule | Severity |
| --- | --- |
| A Sequence Flow cannot connect the elements inside a SubProcess to the elements outside the SubProcess. | Error |
| A Message Flow must connect two separate Pools or elements in separate pools. | Error |
| A Conversation Link can be from a Participant to a Communication, a SubConversation, or to a CallConversation. It can also be from a Communication, a SubConversation, or a CallConversation to a Participant. | Error |
| An Ad Hoc SubProcess may not have a Start Event. An Ad Hoc SubProcess may not have an End Event. | Warning |
| A Message Start Event cannot be used in a Choreography diagram. | Warning |
| An Error Start Event cannot be used in a Choreography diagram. | Error |
| An Error Boundary Event cannot be used in a Choreography diagram. | Error |
| A Message End Event cannot be used in a Choreography diagram. | Error |
| An Error End Event cannot be used in a Choreography diagram. | Error |
| An Escalation End Event cannot be used in a Choreography diagram. | Error |
| A Cancel End Event cannot be used in a Choreography diagram. | Error |
| A Signal End Event cannot be used in a Choreography diagram. | Error |
| A Multiple End Event cannot be used in a Choreography diagram. | Error |
| A Compensation End Event cannot be used in a Choreography diagram. | Error |
| A Sequence Flow cannot cross the Pool Boundary. | Error |
| A BPMN Process Diagram should be owned by BPMN Process or SubProcess. | Error |
| A BPMN Process diagram should be owned by a BPMN Process or SubProcess. | Error |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The BPMN correctness (active) validation rules defined in Cameo Business Modeler for BPMN2 projects are described in the table.</p><table class="relative-table" style="width: 75.5962%;"><colgroup><col style="width: 84.4211%;" /><col style="width: 15.5789%;" /></colgroup><tbody><tr><th>Validation rule </th><th><p>Severity</p></th></tr><tr><td><p>A Sequence Flow cannot connect the elements inside a SubProcess to the elements outside the SubProcess.</p></td><td>Error</td></tr><tr><td><span>A Message Flow must connect two separate Pools or elements in separate pools.</span></td><td>Error</td></tr><tr><td><p>A Conversation Link can be from a Participant to a Communication, a SubConversation, or to a CallConversation. It can also be from a Communication, a SubConversation, or a CallConversation to a Participant.</p></td><td>Error</td></tr><tr><td>An Ad Hoc SubProcess may not have a Start Event. An Ad Hoc SubProcess may not have an End Event.</td><td><p>Warning</p></td></tr><tr><td><span>A Message Start Event cannot be used in a Choreography diagram. </span></td><td><p>Warning</p></td></tr><tr><td><span>An Error Start Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td><span>An Error Boundary Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td><span>A Message End Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td><span>An Error End Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td><span>An Escalation End Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td><span>A Cancel End Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td><span>A Signal End Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td><span>A Multiple End Event cannot be used in a Choreography diagram. </span></td><td>Error</td></tr><tr><td>A Compensation End Event cannot be used in a Choreography diagram.</td><td><span>Error</span></td></tr><tr><td><span>A Sequence Flow cannot cross the Pool Boundary. </span></td><td><span>Error</span></td></tr><tr><td colspan="1"><span>A BPMN Process Diagram should be owned by BPMN Process or SubProcess.</span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A BPMN Process diagram should be owned by a BPMN Process or SubProcess. </span></td><td colspan="1"><span>Error</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17675635 space=VR version=1 -->
## PAGE 00009: BPMN2 Correctness Validation Rules

- page_id: `17675635`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17675635/BPMN2+Correctness+Validation+Rules
- version_number: 1
- version_date: `2017-05-25T13:26:57.567+02:00`
- ancestors: Validation Rules > BPMN validation rules
- labels: []

### NORMALIZED CONTENT

The BPMN2 validation rules included in the BPMN2 Correctness validation rules suite are described in the table.

| Validation rule | Severity |
| --- | --- |
| An Event SubProcess cannot have any incoming or outgoing Sequence Flows. | Warning |
| An Ad Hoc SubProcess cannot have a SubChoreography. | Warning |
| An Ad Hoc SubProcess cannot have Conversations. | Warning |
| A Converging Gateway should not have more than one outgoing Sequence Flow. | Info |
| A Diverging Gateway should not have more than one incoming Sequence Flow. | Info |
| A Participant’s multiplicity minimum value must be 0 for an unspecified multiplicity or >=2 when the multiplicity minimum value is specified. | Warning |
| A Participant’s multiplicity maximum value must be 0 for an unspecified multiplicity or >=2 when the multiplicity maximum value is specified. | Warning |
| The beginning quantity of an Activity should be one (1) or greater. | Warning |
| The ending quantity of an Activity should be one (1) or greater. | Warning |
| A Data Input cannot have an incoming Data Association. | Warning |
| A Data Output cannot have an outgoing Data Association. | Warning |
| A Condition cannot be specified for an outgoing Sequence Flow from a Start Event. | Info |
| Only Messages and Multiple Start Events can have incoming Message Flows. | Warning |
| Only Multiple Start Events can have multiple incoming Message Flows. | Warning |
| A Cancel Event can only be attached to a Transaction SubProcess boundary. | Warning |
| An Intermediate Boundary Event cannot have an incoming Sequence Flow. | Warning |
| A Compensation Boundary Event cannot have an outgoing Sequence Flow. | Warning |
| A Link Intermediate Event can have either an incoming or outgoing Sequence Flow. It cannot contain both. | Warning |
| A Compensation Start Event should not be used with a top-level Process. | Info |
| A Cancel End Event can only be used within a Transaction SubProcess. | Warning |
| A None Start Event cannot be used with an Event SubProcess. | Warning |
| A default Sequence Flow should not have a conditionExpression. | Warning |
| A Sequence Flow outgoing from an Event Gateway should not have a conditionExpression. | Info |
| A Non-Interrupting Start Event can only be used inside an Event SubProcess. | Warning |
| A CallActivity cannot be displayed in the Choreography Diagram. | Error |
| A CallChoreography cannot be displayed in the BPMN Process Diagram. | Error |
| A CallConversation cannot be displayed in the BPMN Process Diagram. | Error |
| A Conversation cannot be displayed in the BPMN Process Diagram. | Error |
| A SubChoreography cannot be displayed in the BPMN Process Diagram. | Error |
| A SubConversation cannot be displayed in the BPMN Process Diagram. | Error |
| A SubProcess cannot be displayed in the Choreography Diagram. | Error |
| A Task cannot be displayed in the Choreography Diagram. | Error |
| A Data Association should not be connected between Data Object and Gateway. | Warning |
| A ChoreographyTask cannot be displayed in the BPMN Process Diagram. | Error |
| A Compensation Activity cannot have any incoming Sequence Flows. | Warning |
| An Escalation Start Event cannot be used with a top-level Process. | Error |
| An Error Start Event cannot be used with a top-level Process. | Info |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The BPMN2 validation rules included in the BPMN2 Correctness validation rules suite are described in the table.</p><table class="relative-table" style="width: 79.1339%;"><colgroup><col style="width: 82.8685%;" /><col style="width: 17.1315%;" /></colgroup><tbody><tr><th>Validation rule </th><th><p>Severity</p></th></tr><tr><td><p>An Event SubProcess cannot have any incoming or outgoing Sequence Flows.</p></td><td><p>Warning</p></td></tr><tr><td><p>An Ad Hoc SubProcess cannot have a SubChoreography.</p></td><td><p>Warning</p></td></tr><tr><td><p>An Ad Hoc SubProcess cannot have Conversations.</p></td><td><span>Warning</span></td></tr><tr><td><p>A Converging Gateway should not have more than one outgoing Sequence Flow.</p></td><td><p>Info</p></td></tr><tr><td><p>A Diverging Gateway should not have more than one incoming Sequence Flow.</p></td><td><span>Info</span></td></tr><tr><td colspan="1"><span>A Participant’s multiplicity minimum value must be 0 for an unspecified multiplicity or &gt;=2 when </span><span>the multiplicity minimum value is specified.</span></td><td colspan="1"><span>Warning</span></td></tr><tr><td><p>A Participant’s multiplicity maximum value must be 0 for an unspecified multiplicity or &gt;=2 when the multiplicity maximum value is specified.</p></td><td><span>Warning</span></td></tr><tr><td><p>The beginning quantity of an Activity should be one (1) or greater.</p></td><td><span>Warning</span></td></tr><tr><td><p>The ending quantity of an Activity should be one (1) or greater.</p></td><td><span>Warning</span></td></tr><tr><td><p>A Data Input cannot have an incoming Data Association.</p></td><td><span>Warning</span></td></tr><tr><td><p>A Data Output cannot have an outgoing Data Association.</p></td><td><span>Warning</span></td></tr><tr><td><p>A Condition cannot be specified for an outgoing Sequence Flow from a Start Event.</p></td><td><span>Info</span></td></tr><tr><td><p>Only Messages and Multiple Start Events can have incoming Message Flows.</p></td><td><span>Warning</span></td></tr><tr><td><p>Only Multiple Start Events can have multiple incoming Message Flows.</p></td><td><span>Warning</span></td></tr><tr><td><p>A Cancel Event can only be attached to a Transaction SubProcess boundary.</p></td><td><span>Warning</span></td></tr><tr><td><p>An Intermediate Boundary Event cannot have an incoming Sequence Flow.</p></td><td><span>Warning</span></td></tr><tr><td><p>A Compensation Boundary Event cannot have an outgoing Sequence Flow.</p></td><td><span>Warning</span></td></tr><tr><td colspan="1"><p>A Link Intermediate Event can have either an incoming or outgoing Sequence Flow. It cannot contain both.</p></td><td colspan="1"><span>Warning</span></td></tr><tr><td colspan="1"><span>A Compensation Start Event should not be used with a top-level Process. </span></td><td colspan="1"><span>Info</span></td></tr><tr><td colspan="1"><span>A Cancel End Event can only be used within a Transaction SubProcess. </span></td><td colspan="1"><span>Warning</span></td></tr><tr><td colspan="1"><span>A None Start Event cannot be used with an Event SubProcess. </span></td><td colspan="1"><span>Warning</span></td></tr><tr><td colspan="1"><span>A default Sequence Flow should not have a conditionExpression. </span></td><td colspan="1"><span>Warning</span></td></tr><tr><td colspan="1"><span>A Sequence Flow outgoing from an Event Gateway should not have a conditionExpression. </span></td><td colspan="1"><span>Info</span></td></tr><tr><td colspan="1"><span>A Non-Interrupting Start Event can only be used inside an Event SubProcess. </span></td><td colspan="1"><span>Warning</span></td></tr><tr><td colspan="1"><span>A CallActivity cannot be displayed in the Choreography Diagram.</span></td><td colspan="1"><p>Error</p></td></tr><tr><td colspan="1"><span>A CallChoreography cannot be displayed in the BPMN Process Diagram. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A CallConversation cannot be displayed in the BPMN Process Diagram.</span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1">A Conversation cannot be displayed in the BPMN Process Diagram.  </td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A SubChoreography cannot be displayed in the BPMN Process Diagram. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A SubConversation cannot be displayed in the BPMN Process Diagram. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1">A SubProcess cannot be displayed in the Choreography Diagram.</td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A Task cannot be displayed in the Choreography Diagram. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A Data Association should not be connected between Data Object and Gateway. </span></td><td colspan="1"><span>Warning</span></td></tr><tr><td colspan="1"><span>A ChoreographyTask cannot be displayed in the BPMN Process Diagram.</span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A Compensation Activity cannot have any incoming Sequence Flows. </span></td><td colspan="1"><span>Warning</span></td></tr><tr><td colspan="1"><span>An Escalation Start Event cannot be used with a top-level Process. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>An Error Start Event cannot be used with a top-level Process.</span></td><td colspan="1"><span>Info</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17675651 space=VR version=1 -->
## PAGE 00010: BPMN2 Export Completeness Validation Rules

- page_id: `17675651`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17675651/BPMN2+Export+Completeness+Validation+Rules
- version_number: 1
- version_date: `2017-05-25T13:35:31.069+02:00`
- ancestors: Validation Rules > BPMN validation rules
- labels: []

### NORMALIZED CONTENT

The BPMN2 validation rules included in the BPMN2 Export Completeness validation rules suite are described in the table.

| Validation rule | Severity |
| --- | --- |
| An Assignment should have a from value. | Error |
| An Assignment should have a to value. | Error |
| A ChoreograhpyActivity should have an initiatingParticipantRef value. | Error |
| A ChoreograhpyTask should have a messageFlow value. | Error |
| A ComplexBehaviorDefinition should have a condition value. | Error |
| A ConversationAssociation should have an innerConversationNodeRef value. | Error |
| A ConversationAssociation should have an outerConversationNodeRef value. | Error |
| A CorrelationProperty should have a CorrelationPropertyRetrievalExpression at least one. | Error |
| A CorrelationPropertyBinding should have a correlationPropertyRef value. | Error |
| A CorrelationPropertyBinding should have a dataPathBody value. | Error |
| A CorrelationPropertyRetrievalExpression should have a messagePathBody value. | Error |
| A CorrelationPropertyRetrievalExpression should have a messageRef value. | Error |
| A CorrelationSubscription should have a correlationKeyRef value. | Error |
| A Definitions should have a targetNamespace value. | Error |
| A BPMNImport should have an importType value. | Error |
| A BPMNImport should have a location value. | Error |
| A BPMNImport should have a namespace value. | Error |
| A BPMNInterface should have a name value. | Error |
| A BPMNInterface should have an operation at least one. | Error |
| An InputOutputSpecification should have an inputSets value. | Error |
| An InputOutputSpecification should have an outputSets value. | Error |
| A LinkCatchIntermediateEvent should have a name value. | Error |
| A LinkThrowIntermediateEvent should have a name value. | Error |
| An Operation should have an inMessageRef value. | Error |
| An Operation should have a name value. | Error |
| A Resource should have a name value. | Error |
| A ResourceAssignmentExpression should have an expression value. | Error |
| A ResourceParameterBinding should have an expression value. | Error |
| A ResourceParameterBinding should have a parameterRef value. | Error |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The BPMN2 validation rules included in the BPMN2 Export Completeness validation rules suite are described in the table.</p><table><colgroup><col /><col /></colgroup><tbody><tr><th>Validation rule </th><th><p>Severity</p></th></tr><tr><td>An Assignment should have a from value.  </td><td>Error</td></tr><tr><td><span>An Assignment should have a to value. </span></td><td><span>Error</span></td></tr><tr><td><span>A ChoreograhpyActivity should have an initiatingParticipantRef value. </span></td><td><span>Error</span></td></tr><tr><td colspan="1"><span>A ChoreograhpyTask should have a messageFlow value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A ComplexBehaviorDefinition should have a condition value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A ConversationAssociation should have an innerConversationNodeRef value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A ConversationAssociation should have an outerConversationNodeRef value.</span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1">A CorrelationProperty should have a CorrelationPropertyRetrievalExpression at least one.  </td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A CorrelationPropertyBinding should have a correlationPropertyRef value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A CorrelationPropertyBinding should have a dataPathBody value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A CorrelationPropertyRetrievalExpression should have a messagePathBody value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A CorrelationPropertyRetrievalExpression  should have a messageRef value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A CorrelationSubscription should have a correlationKeyRef value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A Definitions should have a targetNamespace value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A BPMNImport should have an importType value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A BPMNImport should have a location value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A BPMNImport should have a namespace value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A BPMNInterface should have a name value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A BPMNInterface should have an operation at least one. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>An InputOutputSpecification should have an inputSets value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>An InputOutputSpecification should have an outputSets value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A LinkCatchIntermediateEvent should have a name value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A LinkThrowIntermediateEvent should have a name value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>An Operation should have an inMessageRef value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>An Operation should have a name value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A Resource should have a name value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A ResourceAssignmentExpression should have an expression value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A ResourceParameterBinding should have an expression value. </span></td><td colspan="1"><span>Error</span></td></tr><tr><td colspan="1"><span>A ResourceParameterBinding should have a parameterRef value.</span></td><td colspan="1"><span>Error</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=64973746 space=VR version=18 -->
## PAGE 00011: ClassifierBehavior

- page_id: `64973746`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/64973746/ClassifierBehavior
- version_number: 18
- version_date: `2021-01-06T06:41:32.218+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

CLASSIFIER_BEHAVIOR_SYNC

**Description**

This validation rule checks if property to which«classifierBehavior»stereotype is applied meet the following constraints:

- Is only applied to properties owned (not inherited) by Blocks that have classifier behaviors.
- Is composite.
- Is typed by the classifier behavior of their owning Block or a generalization of the classifier behavior.

**Severity**

warning****

**Constrained****element**

Property

**Solvers**

To fix this error, check if Classifier Behavior Property:

- Is Typed by the Activity.
- Aggregation property value set as composite .
- Have Name .
- Is owner by Blocks that have classifier behaviors.

**Example**

[IMAGE alt='' src='']

###### The **Aggregation******property value set to**composite** for the *Integrator1* Classifier Behavior.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>CLASSIFIER_BEHAVIOR_SYNC</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">This validation rule checks if property to which </span><span style="color: rgb(51,51,51);">«c<span style="color: rgb(62,63,64);">lassifierBehavior</span></span><span style="color: rgb(51,51,51);">» </span><span style="color: rgb(62,63,64);">stereotype is applied meet the following constraints:</span></span></p><ul><li><span style="color: rgb(62,63,64);">Is only applied to properties owned (not inherited) by Blocks that have classifier behaviors.</span></li><li><span style="color: rgb(62,63,64);">Is composite.</span></li><li><span style="color: rgb(62,63,64);">Is typed by the classifier behavior of their owning Block or a generalization of the classifier behavior.<br class="_mce_tagged_br" /></span></li></ul><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained</strong><strong> element</strong></p><p>Property</p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this error, check if Classifier Behavior Property:</span></p><ul><li>Is<strong> Typed </strong>by the Activity.</li><li><strong>Aggregation</strong> property value set as <strong>composite</strong>.</li><li>Have <strong>Name</strong>.</li><li>Is owner <span style="color: rgb(62,63,64);">by Blocks that have classifier behaviors.</span></li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="CLASSIFIER_BEHAVIOR_SYNC.png" /></ac:image></p><h6 style="text-align: center;">The <strong>Aggregation</strong><span style="letter-spacing: 0.0px;"><strong> </strong>property value set to </span><strong>composite</strong> for the <em>Integrator1</em> Classifier Behavior.</h6><p><br /></p><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985557 space=VR version=1 -->
## PAGE 00012: COM2001

- page_id: `228985557`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985557/COM2001
- version_number: 1
- version_date: `2018-04-11T06:31:06.769+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2001

**Message**

Actual Project is not linked to Actual Organizational Resource.

**Description**

Actual Project should have the Actual Organizational Resource assigned.

**Severity**

Info

**Context element**

Project

**Solvers**

- Select Actual Organizational Resources - the Actual Organizational Resource is selected.
- Create Actual Organizational Resource - the Actual Organizational Resource is created.

**Example**

[IMAGE alt='' src='']

###### Actual Organizational Resource is selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2001</p><p><strong>Message</strong></p><p>Actual Project is not linked to Actual Organizational Resource.</p><p><strong>Description</strong></p><p>Actual Project should have the Actual Organizational Resource assigned.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Project</p><p><strong>Solvers</strong></p><ul><li><strong>Select Actual Organizational Resources</strong> - the Actual Organizational Resource is selected.</li><li><strong>Create Actual Organizational Resource</strong> - the Actual Organizational Resource is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2001.png" /></ac:image></p><h6>Actual Organizational Resource is selected</h6>
````

<!--NOMAGIC_PAGE id=228985559 space=VR version=1 -->
## PAGE 00013: COM2002

- page_id: `228985559`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985559/COM2002
- version_number: 1
- version_date: `2018-04-11T07:06:33.267+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2002

**Message**

Actual Project Milestone Start Date is undefined.

**Description**

A date of the Actual Project Milestone should be defined.

**Severity**

Info

**Context element**

Actual Project Milestone

**Solvers**

- Specify Date - the Date and Time Setting dialog opens. Specify the Actual Project Milestone date.

**Example**

[IMAGE alt='' src='']

###### Actual Project Milestone date is defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2002</p><p><strong>Message</strong></p><p>Actual Project Milestone Start Date is undefined.</p><p><strong>Description</strong></p><p>A date of the Actual Project Milestone should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Actual Project Milestone</p><p><strong>Solvers</strong></p><ul><li><strong>Specify Date</strong> - the Date and Time Setting dialog opens. Specify the Actual Project Milestone date.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2002.png" /></ac:image></p><h6>Actual Project Milestone date is defined</h6>
````

<!--NOMAGIC_PAGE id=228985561 space=VR version=1 -->
## PAGE 00014: COM2003

- page_id: `228985561`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985561/COM2003
- version_number: 1
- version_date: `2018-04-11T08:01:56.619+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2003

**Message**

Actual Project Milestone does not have Resources assigned

**Description**

Actual Project Milestone should have the System Resource assigned.

**Severity**

Info

**Context element**

Actual Project Milestone

**Solvers**

- Select System Resources - the System Resource is selected.
- Create System Resource - the System Resource is created.

**Example**

[IMAGE alt='' src='']

###### Actual Resource for Actual Project Milestone is assigned

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2003</p><p><strong>Message</strong></p><p>Actual Project Milestone does not have Resources assigned</p><p><strong>Description</strong></p><p>Actual Project Milestone should have the System Resource assigned.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Actual Project Milestone</p><p><strong>Solvers</strong></p><ul><li><strong>Select System Resources</strong> - the System Resource is selected.</li><li><strong>Create System Resource</strong> - the System Resource is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2003.png" /></ac:image></p><h6>Actual Resource for Actual Project Milestone is assigned</h6>
````

<!--NOMAGIC_PAGE id=228985563 space=VR version=1 -->
## PAGE 00015: COM2004

- page_id: `228985563`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985563/COM2004
- version_number: 1
- version_date: `2018-04-12T07:04:39.741+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2004

**Message**

Actual Project Milestone is not associated with Actual Project.

**Description**

Actual Project Milestone should have the Actual Project assigned.

**Severity**

Info

**Context element**

Actual Project Milestone

**Solvers**

- Select Actual Project - the Actual Project is selected.
- Create Actual Project - the Actual Project is created.

**Example**

[IMAGE alt='' src='']

###### Actual Project is selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2004</p><p><strong>Message</strong></p><p>Actual Project Milestone is not associated with Actual Project.</p><p><strong>Description</strong></p><p>Actual Project Milestone should have the Actual Project assigned.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Actual Project Milestone</p><p><strong>Solvers</strong></p><ul><li><strong>Select Actual Project</strong> - the Actual Project is selected.</li><li><strong>Create Actual Project</strong> - the Actual Project is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2004.png" /></ac:image></p><h6>Actual Project is selected</h6>
````

<!--NOMAGIC_PAGE id=228985565 space=VR version=1 -->
## PAGE 00016: COM2005

- page_id: `228985565`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985565/COM2005
- version_number: 1
- version_date: `2018-04-13T04:55:25.612+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2005

**Message**

Actual Project Start Date is undefined.

**Description**

Start Date of the Actual Project should be defined.

**Severity**

Info

**Context element**

Actual Project

**Solvers**

- Specify Start Date - the Date and Time Settings dialog opens. You can specify the date the project should start.

**Example**

[IMAGE alt='' src='']

###### Start date of Project is specified

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2005</p><p><strong>Message</strong></p><p>Actual Project Start Date is undefined.</p><p><strong>Description</strong></p><p>Start Date of the Actual Project should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Actual Project</p><p><strong>Solvers</strong></p><ul><li><strong>Specify Start Date</strong> - the Date and Time Settings dialog opens. You can specify the date the project should start.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2005.png" /></ac:image></p><h6>Start date of Project is specified</h6>
````

<!--NOMAGIC_PAGE id=228985567 space=VR version=1 -->
## PAGE 00017: COM2006

- page_id: `228985567`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985567/COM2006
- version_number: 1
- version_date: `2018-04-13T06:56:01.341+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2006

**Message**

Alias is not annotating any Element

**Description**

Alias should be associated with the UAF Element.

**Severity**

Info

**Context element**

Alias

**Solvers**

- Select UAF Element - select any UAF element, which might need alias to be defined.
- Create UAF Element - create any UAF element, which might need alias to be defined.

**Example**

[IMAGE alt='' src='']

###### Alias is annotating High Level Operational Concept element

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2006</p><p><strong>Message</strong></p><p>Alias is not annotating any Element</p><p><strong>Description</strong></p><p>Alias should be associated with the UAF Element.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Alias</p><p><strong>Solvers</strong></p><ul><li><strong>Select UAF Element</strong> - select any UAF element, which might need alias to be defined.</li><li><strong>Create UAF Element</strong> - create any UAF element, which might need alias to be defined.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2006.png" /></ac:image></p><h6>Alias is annotating High Level Operational Concept element</h6>
````

<!--NOMAGIC_PAGE id=228985569 space=VR version=1 -->
## PAGE 00018: COM2007

- page_id: `228985569`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985569/COM2007
- version_number: 1
- version_date: `2018-04-13T06:38:12.014+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2007

**Message**

Definition has no authors defined.

**Description**

Author of the Definition should be defined.

**Severity**

Info

**Context element**

Definition

**Solvers**

- Add Author - the text editor opens. Type the author.

**Example**

[IMAGE alt='' src='']

###### Author is added

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2007</p><p><strong>Message</strong></p><p>Definition has no authors defined.</p><p><strong>Description</strong></p><p>Author of the Definition should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Definition</p><p><strong>Solvers</strong></p><ul><li> <strong>Add </strong> <strong>Author</strong> - the text editor opens. Type the author.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2007.png" /></ac:image></p><h6>Author is added</h6>
````

<!--NOMAGIC_PAGE id=228985571 space=VR version=1 -->
## PAGE 00019: COM2008

- page_id: `228985571`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985571/COM2008
- version_number: 1
- version_date: `2018-04-13T06:54:57.054+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2008

**Message**

Definition is not annotating Element.

**Description**

Definition should be associated with the UAF Element.

**Severity**

Info

**Context element**

Definition

**Solvers**

- Select UAF Element - select any UAF element, which might need alias to be defined.
- Create UAF Element - create any UAF element, which might need alias to be defined.

**Example**

[IMAGE alt='' src='']

###### Definition is annotating Whole Life Enterprise

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2008</p><p><strong>Message</strong></p><p>Definition is not annotating Element.</p><p><strong>Description</strong></p><p>Definition should be associated with the UAF Element.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Definition</p><p><strong>Solvers</strong></p><ul><li><strong>Select UAF Element</strong> - select any UAF element, which might need alias to be defined.</li><li><strong>Create UAF Element</strong> - create any UAF element, which might need alias to be defined.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2008.png" /></ac:image></p><h6>Definition is annotating Whole Life Enterprise</h6>
````

<!--NOMAGIC_PAGE id=228985573 space=VR version=1 -->
## PAGE 00020: COM2009

- page_id: `228985573`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985573/COM2009
- version_number: 1
- version_date: `2018-04-23T11:09:23.774+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2009

**Message**

Natural Resource is not Conveyed.

**Description**

Natural Resource element should be used as the Conveyed element for either Operational Exchange or Resource Exchange.

**Severity**

Info

**Context element**

Natural Resource

**Solvers**

- Drag the Natural Resource onto the exchange. The element becomes conveyed.

**Example**

[IMAGE alt='' src='']

###### Energy is dragged onto the exchange

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2009</p><p><strong>Message</strong></p><p>Natural Resource is not Conveyed.</p><p><strong>Description</strong></p><p>Natural Resource element should be used as the Conveyed element for either Operational Exchange or Resource Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Natural Resource</p><p><strong>Solvers</strong></p><ul><li>Drag the Natural Resource onto the exchange. The element becomes conveyed.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2009.png" /></ac:image></p><h6>Energy is dragged onto the exchange</h6>
````

<!--NOMAGIC_PAGE id=228985575 space=VR version=1 -->
## PAGE 00021: COM2010

- page_id: `228985575`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985575/COM2010
- version_number: 1
- version_date: `2018-04-09T13:58:41.678+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2010

**Message**

Information Element is not Conveyed

**Description**

Information element should be used as the Conveyed element for either Operational Exchange.

**Severity**

Info

**Context element**

Information Element

**Solvers**

- Select Operational Exchanges - the Operational Exchanges are selected.
- Create Operational Exchange - the Operational Exchange is created.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2010</p><p><strong>Message</strong></p><p>Information Element is not Conveyed</p><p><strong>Description</strong></p><p>Information element should be used as the Conveyed element for either Operational Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Information Element</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Exchanges</strong> - the Operational Exchanges are selected.</li><li><strong>Create Operational Exchange</strong> - the Operational Exchange is created.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="2010.png" /></ac:image><br /></strong></p><p> </p>
````

<!--NOMAGIC_PAGE id=228985577 space=VR version=1 -->
## PAGE 00022: COM2012

- page_id: `228985577`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985577/COM2012
- version_number: 1
- version_date: `2022-12-16T13:20:52.054+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2012

**Message**

Geo Political Extent Type is not Conveyed

**Description**

Geo Political Extent Type should be used as either the Conveyed element for the Operational Exchange or Resource Exchange.

**Severity**

Info

**Context element**

Geo Political Extent Type

**Solvers**

- Select Operational Exchanges and Resource Exchange - the Operational Exchange or Resource Exchange is selected.
- Create Operational Exchange - the Operational Exchange is created.
- Create Resource Exchange - the Resource Exchange is created.

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2012</p><p><strong>Message</strong></p><p>Geo Political Extent Type is not Conveyed</p><p><strong>Description</strong></p><p>Geo Political Extent Type should be used as either the Conveyed element for the Operational Exchange or Resource Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Geo Political Extent Type</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Exchanges and Resource Exchange</strong> - the Operational Exchange or Resource Exchange is selected.</li><li><strong>Create Operational Exchange</strong> - the Operational Exchange is created.</li><li><strong>Create Resource Exchange</strong> - the Resource Exchange is created.</li></ul><p><strong>Example</strong></p><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985578 space=VR version=1 -->
## PAGE 00023: COM2014

- page_id: `228985578`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985578/COM2014
- version_number: 1
- version_date: `2018-04-13T10:44:25.688+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2014

**Message**

Measurement Set has no Measurements defined.

**Description**

Measurement Set should have at least one Measurement defined as its owned attribute.

**Severity**

Info

**Context element**

Measurement Set

**Solvers**

- Create Measurement - Created Measurement specification window opens with the focus on the name property.

**Example**

[IMAGE alt='' src='']

###### Measurement is created

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2014</p><p><strong>Message</strong></p><p>Measurement Set has no Measurements defined.</p><p><strong>Description</strong></p><p>Measurement Set should have at least one Measurement defined as its owned attribute.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Measurement Set</p><p><strong>Solvers</strong></p><ul><li><strong>Create Measurement</strong> - Created Measurement specification window opens with the focus on the name property.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2014.png" /></ac:image></p><h6>Measurement is created</h6>
````

<!--NOMAGIC_PAGE id=228985580 space=VR version=1 -->
## PAGE 00024: COM2015

- page_id: `228985580`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985580/COM2015
- version_number: 1
- version_date: `2018-04-13T10:51:23.601+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2015

**Message**

Metadata Name is undefined.

**Description**

Name of the Metadata should be defined.

**Severity**

Info

**Context element**

Metadata

**Solvers**

- Add Name - text editor opens. Type the name.

**Example**

[IMAGE alt='' src='']

###### Metadata name is set

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2015</p><p><strong>Message</strong></p><p>Metadata Name is undefined.</p><p><strong>Description</strong></p><p>Name of the Metadata should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Metadata</p><p><strong>Solvers</strong></p><ul><li><strong>Add Name</strong> - text editor opens. Type the name.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2015.png" /></ac:image></p><h6>Metadata name is set</h6>
````

<!--NOMAGIC_PAGE id=228985582 space=VR version=1 -->
## PAGE 00025: COM2016

- page_id: `228985582`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985582/COM2016
- version_number: 1
- version_date: `2018-04-13T10:52:48.747+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2016

**Message**

Create Pins correspondingly to Operational Ports owned by Operational Performer Capable to Perform Activity

**Description**

If the Operational Performer has the Operational Ports and the Operational Performer is associated with the Operational Activity using Is Capable To Perform relationship, then the Operation Activity Action should have the Pins that are synchronized with the Operational Ports. The Behavior of the Operational Activity Action is the particular Operational Activity.

**Severity**

Info

**Context element**

Operational Activity Action

**Solvers**

- Synchronize Pins with Operational Ports - the Input and Output Pins are created for the Operational Activity Action.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2016</p><p><strong>Message</strong></p><p>Create Pins correspondingly to Operational Ports owned by Operational Performer Capable to Perform Activity</p><p><strong>Description</strong></p><p>If the Operational Performer has the Operational Ports and the Operational Performer is associated with the Operational Activity using Is Capable To Perform relationship, then the Operation Activity Action should have the Pins that are synchronized with the Operational Ports. The Behavior of the Operational Activity Action is the particular Operational Activity.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Operational Activity Action</p><p><strong>Solvers</strong></p><ul><li><strong>Synchronize Pins with Operational Ports</strong> - the Input and Output Pins are created for the Operational Activity Action.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="2016.png" /></ac:image><br /></strong></p><p> </p>
````

<!--NOMAGIC_PAGE id=228985584 space=VR version=1 -->
## PAGE 00026: COM2018

- page_id: `228985584`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985584/COM2018
- version_number: 1
- version_date: `2024-02-28T12:29:25.484+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2018

**Message**

Operational Agent is not a source or target for Operational Exchange.

**Description**

Operational Agent should be set as a source or target for the Operational Exchange.

**Severity**

Info

**Constrained element**

Operational Agent

**Solvers**

- Create Outgoing Operational Exchange - the Realized Operational Exchange wizard opens where you can create an Outgoing Operational Exchange.
- Create Incoming Operational Exchange - the Realized Operational Exchange wizard opens where you can create an Incoming Operational Exchange.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2018</p><p><strong>Message</strong> </p><p>Operational Agent is not a source or target for Operational Exchange.</p><p><strong>Description</strong></p><p>Operational Agent should be set as a source or target for the Operational Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Constrained element</strong></p><p>Operational Agent</p><p><strong>Solvers</strong></p><ul><li><strong>Create Outgoing Operational Exchange</strong> - the Realized Operational Exchange wizard opens where you can create an Outgoing Operational Exchange.</li><li><strong>Create Incoming Operational Exchange</strong> - the Realized Operational Exchange wizard opens where you can create an Incoming Operational Exchange.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:title="An Outgoing Operational Exchange is created" ac:alt="An Outgoing Operational Exchange is created"><ri:attachment ri:filename="COM2018.png" /></ac:image><br /></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985586 space=VR version=1 -->
## PAGE 00027: COM2019

- page_id: `228985586`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985586/COM2019
- version_number: 1
- version_date: `2024-03-07T09:26:44.347+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2019

**Message**

Operational Agent is not Capable to Perform Operational Activity.

**Description**

Operational Agent should be associated with the Operational Activity using the Is Capable To Perform relationship.

**Severity**

Info

**Constrained element**

Operational Agent

**Solvers**

- Select Operational Activities - the Operational Activity is selected and the Is Capable To Perform relationship is created.
- Create Operational Activity - the Operational Activity is created together with the Is Capable To Perform relationship.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2019</p><p><strong>Message</strong></p><p>Operational Agent is not Capable to Perform Operational Activity.</p><p><strong>Description</strong></p><p>Operational Agent should be associated with the Operational Activity using the Is Capable To Perform relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Constrained element</strong></p><p>Operational Agent</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Activities</strong> - the Operational Activity is selected and the Is Capable To Perform relationship is created.</li><li><strong>Create Operational Activity</strong> - the Operational Activity is created together with the Is Capable To Perform relationship.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:title="Operational Activity is selected" ac:alt="Operational Activity is selected"><ri:attachment ri:filename="COM2019.png" /></ac:image><br /></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985588 space=VR version=1 -->
## PAGE 00028: COM2020

- page_id: `228985588`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985588/COM2020
- version_number: 1
- version_date: `2018-04-09T13:54:45.288+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2020

**Message**

Operational Performer is not Exhibiting Capability.

**Description**

Operational Performer should be associated with the Capability using the Exhibits relationship.

**Severity**

Info

**Context element**

Operational Performer

**Solvers**

- Select Capabilities - the Capability is selected.
- Create Capability - the Capability is created.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2020</p><p><strong>Message</strong></p><p>Operational Performer is not Exhibiting Capability.</p><p><strong>Description</strong></p><p>Operational Performer should be associated with the Capability using the Exhibits relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Operational Performer</p><p><strong>Solvers</strong></p><ul><li><strong>Select Capabilities</strong> - the Capability is selected.</li><li><strong>Create Capability</strong> - the Capability is created.</li></ul><p><strong>Example</strong></p><p><ac:image ac:title="Node exhibits Capability" ac:alt="Node exhibits Capability"><ri:attachment ri:filename="COM2020.png" /></ac:image></p><p> </p>
````

<!--NOMAGIC_PAGE id=228985590 space=VR version=1 -->
## PAGE 00029: COM2021

- page_id: `228985590`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985590/COM2021
- version_number: 1
- version_date: `2018-04-13T14:01:01.091+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2021

**Message**

Operational Performer is not Implemented by Resource Performer.

**Description**

Operational Performer should be associated with the Resource Performer using the Implements relationship.

**Severity**

Info

**Context element**

Node

**Solvers**

- Select Resource Performer - the Resource Performer is selected.
- Create Resource Performer - the Resource Performer is created.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2021</p><p><strong>Message</strong></p><p>Operational Performer is not Implemented by Resource Performer.</p><p><strong>Description</strong></p><p>Operational Performer should be associated with the Resource Performer using the Implements relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Node</p><p><strong>Solvers</strong></p><ul><li><strong>Select Resource Performer</strong> - the Resource Performer is selected.</li><li><strong>Create Resource Performer</strong> - the Resource Performer is created.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COM2021.png" /></ac:image><br /></strong></p><p> </p>
````

<!--NOMAGIC_PAGE id=228985592 space=VR version=1 -->
## PAGE 00030: COM2022

- page_id: `228985592`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985592/COM2022
- version_number: 1
- version_date: `2018-04-16T08:10:05.915+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2022

**Message**

Operational Role is not performing Operational Activity Action.

**Description**

Operational Role should perform the Operational Activity Action in the specific context using Performs In Context relationship.

**Severity**

Info

**Context element**

Node Role

**Solvers**

- Select Operational Activity Action - the Operational Activity Action is selected.
- Create Operational Activity Action - the Operational Activity Action is created.

A behavior of the Operational Activity Action is displayed in Is Capable To Perform Operational Activity property.

**Example**

[IMAGE alt='' src='']

###### Operational Activity Action is selected to be performed by Operational Role

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2022</p><p><strong>Message</strong></p><p>Operational Role is not performing Operational Activity Action.</p><p><strong>Description</strong></p><p>Operational Role should perform the Operational Activity Action in the specific context using <span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);">Performs In Context</span></span> relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Node Role</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Activity Action</strong> - the Operational Activity Action is selected.</li><li><strong>Create Operational Activity Action</strong> - the Operational Activity Action is created.</li></ul><p>A behavior of the Operational Activity Action is displayed in Is Capable To Perform Operational Activity property.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2022.png" /></ac:image></p><h6>Operational Activity Action is selected to be performed by Operational Role</h6>
````

<!--NOMAGIC_PAGE id=228985594 space=VR version=1 -->
## PAGE 00031: COM2023

- page_id: `228985594`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985594/COM2023
- version_number: 1
- version_date: `2018-04-16T09:06:12.323+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2023

**Message**

Operational Activity is not Implemented by Function.

**Description**

Operational Activity should be associated with the Function using the Implements relationship.

**Severity**

Info

**Context element**

Operational Activity

**Solvers**

- Select Functions - the Function is selected.
- Create Function - the Function is created.

**Example**

[IMAGE alt='' src='']

###### Operational Activity is implemented by Function

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2023</p><p><strong>Message</strong></p><p>Operational Activity is not Implemented by Function.</p><p><strong>Description</strong></p><p>Operational Activity should be associated with the Function using the Implements relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Operational Activity</p><p><strong>Solvers</strong></p><ul><li><strong>Select Functions</strong> - the Function is selected.</li><li><strong>Create Function</strong> - the Function is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2023.png" /></ac:image></p><h6>Operational Activity is implemented by Function</h6>
````

<!--NOMAGIC_PAGE id=228985596 space=VR version=1 -->
## PAGE 00032: COM2024

- page_id: `228985596`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985596/COM2024
- version_number: 1
- version_date: `2024-02-28T09:41:27.539+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2024

**Message**

Operational Activity is not Performed by Operational Agent.

**Description**

Operational Activity should be associated with the Operational Agent using the Is Capable To Perform relationship.

**Severity**

Info

**Constrained element**

Operational Activity

**Solvers**

- Select Operational Agent - the S elect Element dialog opens where you can select one of the existing Operational Agent specializations.
- Create Operational Agent - the Select Element dialog opens where you can create the needed Operational Agent specialization.

**Example**

**[IMAGE alt='' src='']**

###### Operational Activity is performed by Operational Performer****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2024</p><p><strong>Message</strong></p><p>Operational Activity is not Performed by Operational Agent.</p><p><strong>Description</strong></p><p><span style="color: rgb(23,43,77);">Operational Activity should be associated with the Operational Agent using the Is Capable To Perform relationship.</span></p><p><strong>Severity</strong></p><p>Info</p><p><strong>Constrained element</strong></p><p>Operational Activity</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Agent </strong>- the S<span style="color: rgb(23,43,77);">elect Element dialog opens where you can select one of the existing<span> </span></span>Operational Agent<span style="color: rgb(23,43,77);"><span> </span>specializations.</span></li><li><strong>Create Operational Agent </strong>- the <span style="color: rgb(23,43,77);">Select Element dialog opens where you can create the needed<span> </span></span>Operational Agent<span style="color: rgb(23,43,77);"><span> </span>specialization.</span></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:title="Operational Activity is performed by Node" ac:alt="Operational Activity is performed by Node"><ri:attachment ri:filename="COM2024.png" /></ac:image></strong></p><h6>Operational Activity is performed by Operational Performer<strong><br /></strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985598 space=VR version=1 -->
## PAGE 00033: COM2025

- page_id: `228985598`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985598/COM2025
- version_number: 1
- version_date: `2018-04-16T10:54:54.412+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2025

**Message**

Operational Constraint is not constraining Element.

**Description**

Constraining Element should be defined for the Operational Constraint.

**Severity**

Info

**Context element**

Operational Constraint

**Solvers**

- Select Subjects for Operational Constraint - the Constraining Element is selected.
- Create Subject for Operational Constraint - the Constraining Element is created.

**Example**

[IMAGE alt='' src='']

###### Constrained Element is selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2025</p><p><strong>Message</strong></p><p>Operational Constraint is not constraining Element.</p><p><strong>Description</strong></p><p>Constraining Element should be defined for the Operational Constraint.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Operational Constraint</p><p><strong>Solvers</strong></p><ul><li><strong>Select Subjects for Operational Constraint</strong> - the Constraining Element is selected.</li><li><strong>Create Subject for Operational Constraint</strong> - the Constraining Element is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2025.png" /></ac:image></p><h6>Constrained Element is selected</h6>
````

<!--NOMAGIC_PAGE id=228985600 space=VR version=1 -->
## PAGE 00034: COM2026

- page_id: `228985600`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985600/COM2026
- version_number: 1
- version_date: `2018-04-16T11:37:35.559+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2026

**Message**

Operational Exchange is not Implemented by Resource Exchange

**Description**

Operational Exchange should be associated with the Resource Exchange using the Implements relationship.

**Severity**

Info

**Context element**

Operational Exchange

**Solvers**

- Select Resource Exchange - the Resource Exchange is selected.
- Create Resource Exchange - the Resource Exchange is created.
- Sync Operational Exchange with Resource **Exchange** - the Operational Exchange is synchronized with the Resource Exchange.

**Example**

[IMAGE alt='' src='']

###### Resource Exchange implements Operational Exchange

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2026</p><p><strong>Message</strong></p><p>Operational Exchange is not Implemented by Resource Exchange</p><p><strong>Description</strong></p><p>Operational Exchange should be associated with the Resource Exchange using the Implements relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Operational Exchange</p><p><strong>Solvers</strong></p><ul><li><strong>Select Resource Exchange</strong> - the Resource Exchange is selected.</li><li><strong>Create Resource Exchange</strong> - the Resource Exchange is created.</li><li><strong>Sync Operational Exchange with Resource <strong>Exchange</strong></strong> - the Operational Exchange is synchronized with the Resource Exchange.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2026.png" /></ac:image></p><h6>Resource Exchange implements Operational Exchange</h6>
````

<!--NOMAGIC_PAGE id=228985602 space=VR version=1 -->
## PAGE 00035: COM2027

- page_id: `228985602`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985602/COM2027
- version_number: 1
- version_date: `2018-04-16T12:27:06.198+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2027

**Message**

Producing and Consuming Activities are not defined for Operational Exchange.

**Description**

Operational Activities should be set as a Producing or Consuming Activities for the Operational Exchange.

**Severity**

Info

**Context element**

Operational Exchange

**Solvers**

- Set Producing / Consuming Activities - the Producing and Consuming Activities are set.

**Example**

[IMAGE alt='' src='']

###### Producing and Consuming activities are defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2027</p><p><strong>Message</strong></p><p>Producing and Consuming Activities are not defined for Operational Exchange.</p><p><strong>Description</strong></p><p>Operational Activities should be set as a Producing or Consuming Activities for the Operational Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Operational Exchange</p><p><strong>Solvers</strong></p><ul><li><strong>Set Producing / Consuming Activities</strong> - the Producing and Consuming Activities are set.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2027.png" /></ac:image></p><h6>Producing and Consuming activities are defined</h6>
````

<!--NOMAGIC_PAGE id=228985604 space=VR version=1 -->
## PAGE 00036: COM2028

- page_id: `228985604`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985604/COM2028
- version_number: 1
- version_date: `2024-03-15T14:54:11.884+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2028

**Message**

The Operational Exchange is not realized.

**Description**

The Operational Exchange existing in the model is not realized.

**Severity**

warning

**Context element**

Operational Exchange

**Solvers**

- Remove from Model - the Operational Exchange will be removed from the model.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2028</p><p><strong>Message</strong></p><p>The Operational Exchange is not realized.</p><p><strong>Description</strong></p><p>The Operational Exchange existing in the model is not realized.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Context element</strong></p><p>Operational Exchange </p><p><strong>Solvers</strong></p><ul><li><strong><span style="color: rgb(23,43,77);">Remove from Model</span></strong><span style="color: rgb(23,43,77);"> - the Operational Exchange will be removed from the model.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2028.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985606 space=VR version=1 -->
## PAGE 00037: COM2029

- page_id: `228985606`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985606/COM2029
- version_number: 1
- version_date: `2024-03-15T15:02:31.344+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2029

**Message**

The Resource Exchange existingin the model is not realized.

**Description**

Not Realized Resource Exchange.

**Severity**

warning

**Context element**

Resource Exchange

**Solvers**

- Remove from Model - the Resource Exchange will be removed from the model.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2029</p><p><strong>Message</strong></p><p>The Resource Exchange existing<span style="color: rgb(23,43,77);"> in the model is not realized</span>.</p><p><strong>Description</strong></p><p>Not Realized Resource Exchange.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Context element</strong></p><p>Resource Exchange </p><p><strong>Solvers</strong></p><ul><li><strong><span style="color: rgb(23,43,77);">Remove from Model</span></strong><span style="color: rgb(23,43,77);"> - the Resource Exchange will be removed from the model.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2029.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985608 space=VR version=1 -->
## PAGE 00038: COM2030

- page_id: `228985608`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985608/COM2030
- version_number: 1
- version_date: `2024-03-15T14:59:12.449+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2030

**Message**

The Service Exchange existingin the model is not realized.

**Description**

Not Realized Service Exchange.

**Severity**

warning

**Context element**

Service Exchange

**Solvers**

- Remove from Model - the Service Exchange will be removed from the model.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2030</p><p><strong>Message</strong></p><p>The Service Exchange <span style="color: rgb(23,43,77);">existing</span><span style="color: rgb(23,43,77);"> in the model is not realized</span><span style="color: rgb(23,43,77);">.</span></p><p><strong>Description</strong></p><p>Not Realized Service Exchange.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Context element</strong></p><p>Service Exchange </p><p><strong>Solvers</strong></p><ul><li><strong><span style="color: rgb(23,43,77);">Remove from Model</span></strong><span style="color: rgb(23,43,77);"><span> </span>- the Service Exchange will be removed from the model.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2030.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985610 space=VR version=1 -->
## PAGE 00039: COM2031

- page_id: `228985610`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985610/COM2031
- version_number: 1
- version_date: `2018-04-17T07:01:02.601+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2031

**Message**

Service Policy is not constraining Service Specification.

**Description**

Service Interface should be defined as the Constraint Element of the Service Policy.

**Severity**

Info

**Context element**

Service Policy

**Solvers**

- Select Service Interfaces - the Service Interface is selected.
- Create Service Interface - the Service Interface is created.

**Example**

[IMAGE alt='' src='']

###### Constrained Element is selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2031</p><p><strong>Message</strong></p><p>Service Policy is not constraining Service Specification.</p><p><strong>Description</strong></p><p>Service Interface should be defined as the Constraint Element of the Service Policy.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Service Policy</p><p><strong>Solvers</strong></p><ul><li><strong>Select Service Interfaces</strong> - the Service Interface is selected.</li><li><strong>Create Service Interface</strong> - the Service Interface is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2031.png" /></ac:image></p><h6>Constrained Element is selected</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985612 space=VR version=1 -->
## PAGE 00040: COM2032

- page_id: `228985612`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985612/COM2032
- version_number: 1
- version_date: `2023-10-12T11:37:15.684+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2032

**Message**

Benefits are not defined.

**Description**

Benefits of the Enterprise Goal should be defined.

**Severity**

Info

**Context element**

Enterprise Goal

**Solvers**

- Select Value Item - select an existing Value Item or its specialization.
- Create Value Item - create a new Value Item or its specialization.

**Example**

[IMAGE alt='' src='']

###### Benefit with the Value Item is defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2032</p><p><strong>Message</strong></p><p>Benefits are not defined.</p><p><strong>Description</strong></p><p>Benefits of the Enterprise Goal should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Enterprise Goal</p><p><strong>Solvers</strong></p><ul><li><strong>Select Value Item </strong>- select an existing Value Item or its specialization.</li><li><strong>Create Value Item</strong> - create a new Value Item or its specialization.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2032.png" /></ac:image></p><h6>Benefit with the Value Item is defined</h6>
````

<!--NOMAGIC_PAGE id=228985614 space=VR version=1 -->
## PAGE 00041: COM2033

- page_id: `228985614`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985614/COM2033
- version_number: 1
- version_date: `2018-04-17T10:06:22.910+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2033

**Message**

Capability is not Exhibited by Capability Configuration.

**Description**

Capability should be exhibited by the Capability Configuration using Exhibits relationship.

**Severity**

Info

**Context element**

Capability

**Solvers**

- Select Capability Configurations - the Capability Configuration is selected.
- Create Capability Configuration - the Capability Configuration is created.

**Example**

[IMAGE alt='' src='']

###### Capability Configuration exhibits Capability

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2033</p><p><strong>Message</strong></p><p>Capability is not Exhibited by Capability Configuration.</p><p><strong>Description</strong></p><p>Capability should be exhibited by the Capability Configuration using Exhibits relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Capability</p><p><strong>Solvers</strong></p><ul><li><strong>Select Capability Configurations</strong> - the Capability Configuration is selected.</li><li><strong>Create Capability Configuration</strong> - the Capability Configuration is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2033.png" /></ac:image></p><h6>Capability Configuration exhibits Capability</h6>
````

<!--NOMAGIC_PAGE id=228985616 space=VR version=1 -->
## PAGE 00042: COM2034

- page_id: `228985616`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985616/COM2034
- version_number: 1
- version_date: `2018-04-17T10:25:07.084+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2034

**Message**

Capability is not Exhibited by Operational Performer.

**Description**

Capability should be exhibited by the Operational Performer using Exhibits relationship.

**Severity**

Info

**Context element**

Capability

**Solvers**

- Select Operational Performers - the Operational Performers are selected.
- Create **Operational Performers** - the Operational Performers are created.

**Example**

[IMAGE alt='' src='']

###### Operational Performer exhibits Capability

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2034</p><p><strong>Message</strong></p><p>Capability is not Exhibited by Operational Performer.</p><p><strong>Description</strong></p><p>Capability should be exhibited by the Operational Performer using Exhibits relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Capability</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Performers </strong>- the Operational Performers are selected.</li><li><strong>Create <strong>Operational Performers</strong></strong> - the Operational Performers are created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2034.png" /></ac:image></p><h6>Operational Performer exhibits Capability</h6>
````

<!--NOMAGIC_PAGE id=228985618 space=VR version=1 -->
## PAGE 00043: COM2035

- page_id: `228985618`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985618/COM2035
- version_number: 1
- version_date: `2018-04-17T10:38:08.020+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2035

**Message**

Capability is not Mapped to Operational Activity.

**Description**

Capability should be mapped with the Operational Activity using Activity Part of Capability or Maps to Capability relationship.

**Severity**

Info

**Context element**

Capability

**Solvers**

- Select Operational Activities - the Operational Activity is selected.
- Create Operational Activity - the Operational Activity is created.

**Example**

[IMAGE alt='' src='']

###### Capability is mapped to Operational Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2035</p><p><strong>Message</strong></p><p>Capability is not Mapped to Operational Activity.</p><p><strong>Description</strong></p><p>Capability should be mapped with the Operational Activity using Activity Part of Capability or Maps to Capability relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Capability</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Activities</strong> - the Operational Activity is selected.</li><li><strong>Create Operational Activity</strong> - the Operational Activity is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2035.png" /></ac:image></p><h6>Capability is mapped to Operational Activity</h6>
````

<!--NOMAGIC_PAGE id=228985620 space=VR version=1 -->
## PAGE 00044: COM2036

- page_id: `228985620`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985620/COM2036
- version_number: 1
- version_date: `2023-10-12T08:40:37.103+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2036

**Message**

Enterprise Goal is not linked to Actual Strategic Phase or its specializations.

**Description**

Enterprise Goal should be set as a goal for the Actual Strategic Phase or its specializations.

**Severity**

Info

**Constrained element**

Enterprise Goal

**Solvers**

- Select Actual Strategic Phases - select an existing Actual Strategic Phase. The Phases relationship is created between Enterprise Goal and the selected Actual Strategic Phase or its specialization.
- Create Actual Strategic Phase - create Actual Strategic Phase that will be linked with the Enterprise Goal. The Phases relationship is created between Enterprise Goal and the created Actual Strategic Phase or its specialization.

**Example**

[IMAGE alt='' src='']

###### Enterprise Goal is linked to Actual Strategic Phase

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2036</p><p><strong>Message</strong></p><p>Enterprise Goal is not linked to Actual Strategic Phase or its specializations.</p><p><strong>Description</strong></p><p>Enterprise Goal should be set as a goal for the Actual Strategic Phase or its specializations.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Constrained element</strong></p><p>Enterprise Goal</p><p><strong>Solvers</strong></p><ul><li><strong>Select Actual Strategic Phases</strong> - select an existing Actual Strategic Phase. The Phases relationship is created between Enterprise Goal and the selected Actual Strategic Phase or its specialization.</li><li><strong>Create Actual Strategic Phase</strong> - create Actual Strategic Phase that will be linked with the Enterprise Goal. The Phases relationship is created between Enterprise Goal and the created Actual Strategic Phase or its specialization.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2036.png" /></ac:image></p><h6>Enterprise Goal is linked to Actual Strategic Phase</h6>
````

<!--NOMAGIC_PAGE id=228985622 space=VR version=1 -->
## PAGE 00045: COM2037

- page_id: `228985622`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985622/COM2037
- version_number: 1
- version_date: `2023-10-12T08:11:51.228+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2037

**Message**

Actual Strategic Phase or its specialization does not have Vision defined.

**Description**

Actual Strategic Phase or its specialization should have the Vision assigned.

**Severity**

Info

**Constrained element**

Actual Strategic Phase

**Solvers**

- Select Vision - the Vision is selected, and P hases relationship is created between the Actual Strategic Phase or its specialization and the selected Enterprise Vision.
- Create Vision - the Vision is created, and P hases relationship is created between the Actual Strategic Phase or its specialization and the created Enterprise Vision.

**Example**

**[IMAGE alt='' src='']**

###### Vision is defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2037</p><p><strong>Message</strong></p><p>Actual Strategic Phase or its specialization does not have Vision defined.</p><p><strong>Description</strong></p><p>Actual Strategic Phase or its specialization should have the Vision assigned.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Constrained element</strong></p><p>Actual Strategic Phase</p><p><strong>Solvers</strong></p><ul><li><strong>Select Vision</strong> - the Vision is selected, and <span style="color: rgb(23,43,77);"><span> P</span></span>hases<span style="color: rgb(23,43,77);"><span> </span>relationship is created between the Actual Strategic Phase or its specialization and the selected Enterprise Vision.</span></li><li><strong>Create Vision</strong> - the Vision is created, and <span style="color: rgb(23,43,77);"><span> P</span></span>hases<span style="color: rgb(23,43,77);"><span> </span>relationship is created between the Actual Strategic Phase or its specialization and the created Enterprise Vision.</span></li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COM2037.png" /></ac:image><br /></strong></p><h6> Vision is defined</h6>
````

<!--NOMAGIC_PAGE id=228985624 space=VR version=1 -->
## PAGE 00046: COM2038

- page_id: `228985624`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985624/COM2038
- version_number: 1
- version_date: `2023-10-12T12:00:33.191+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2038

**Message**

Actual Strategic Phase or its specialization End Date is undefined.

**Description**

End Date of the Actual Strategic Phase or its specialization should be defined.

**Severity**

Info

**Context element**

Actual Strategic Phase

**Solvers**

- Specify End Date - The [CONFLUENCE_PAGE title='Date and Time Settings dialog' space='UAF13PTWRT'] dialog opens. Specify the end date for the Actual Strategic Phase or its specialization.

**Example**

**[IMAGE alt='' src='']**

###### End date is defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p><strong>Abbreviation</strong></p><p>COM2038</p><p><strong>Message</strong></p><p>Actual Strategic Phase or its specialization End Date is undefined.</p><p><strong>Description</strong></p><p>End Date of the Actual Strategic Phase or its specialization should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Actual Strategic Phase</p><p><strong>Solvers</strong></p><ul><li><strong>Specify End Date</strong> - The <strong><ac:link><ri:page ri:space-key="UAF13PTWRT" ri:content-title="Date and Time Settings dialog" /><ac:plain-text-link-body><![CDATA[Date and Time Settings]]></ac:plain-text-link-body></ac:link></strong> dialog opens. Specify the end date for the Actual Strategic Phase or its specialization.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COM2038.png" /></ac:image></strong></p><h6>End date is defined</h6>
````

<!--NOMAGIC_PAGE id=228985626 space=VR version=1 -->
## PAGE 00047: COM2039

- page_id: `228985626`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985626/COM2039
- version_number: 1
- version_date: `2023-10-12T07:47:50.014+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2039

**Message**

Actual Strategic Phaseor its specializationhas no Enterprise Goals defined.

**Description**

Actual Strategic Phaseor its specialization should have the Enterprise Goals assigned.

**Severity**

Info

**Constrained element**

Actual Strategic Phase

**Solvers**

- Select Enterprise Goals - the Enterprise Goal is selected, and Phases relationship is created between the Actual Strategic Phase or its specialization and the selected Enterprise Goal.
- Create Enterprise Goal - the Enterprise Goal is created, and Phases relationship is created between the Actual Strategic Phase or its specialization and the selected Enterprise Goal.

**Example**

[IMAGE alt='' src='']

###### Enterprise Goal is defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2039</p><p><strong>Message</strong></p><p>Actual Strategic Phase<span style="color: rgb(23,43,77);"><span> </span>or its specialization </span>has no Enterprise Goals defined.</p><p><strong>Description</strong></p><p>Actual Strategic Phase<span style="color: rgb(23,43,77);"><span> </span>or its specialization</span> should have the Enterprise Goals assigned.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Constrained element</strong></p><p>Actual Strategic Phase</p><p><strong>Solvers</strong></p><ul><li><strong>Select Enterprise Goals</strong> - the Enterprise Goal is selected, and Phases relationship is created between the Actual Strategic Phase <span style="color: rgb(23,43,77);"><span> </span>or its specialization and the selected Enterprise Goal.</span></li><li><strong>Create Enterprise Goal</strong> - the Enterprise Goal is created, and Phases relationship is created between the Actual Strategic Phase <span style="color: rgb(23,43,77);"><span> </span>or its specialization and the selected Enterprise Goal.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2039.png" /></ac:image></p><h6><span style="color: rgb(112,112,112);">Enterprise Goal is defined</span></h6>
````

<!--NOMAGIC_PAGE id=228985628 space=VR version=1 -->
## PAGE 00048: COM2041

- page_id: `228985628`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985628/COM2041
- version_number: 1
- version_date: `2023-10-12T12:18:05.432+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2041

**Message**

Actual Strategic Phase is not Phasing Phaseable Element

**Description**

Actual Strategic Phase should exhibit the Capability using the Exhibits relationship.

**Severity**

Info

**Context element**

Actual Strategic Phase

**Solvers**

- Create Phaseable Element - create a needed phaseable element. The Phases relationship is also created.
- Select Phaseable Element - select an existing phaseable element. The Phases relationship is also created.

**Example**

**[IMAGE alt='' src='']**

###### Actual Enterprise Phase phasing the Capability

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2041</p><p><strong>Message</strong></p><p>Actual Strategic Phase is not Phasing Phaseable Element</p><p><strong>Description</strong></p><p>Actual Strategic Phase should exhibit the Capability using the Exhibits relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Actual Strategic Phase</p><p><strong>Solvers</strong></p><ul><li><strong>Create Phaseable Element</strong> - create a needed phaseable element. The Phases relationship is also created.</li><li><strong>Select Phaseable Element</strong> - select an existing phaseable element. The Phases relationship is also created.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:title="Actual Enterprise Phase exhibiting Capability" ac:alt="Actual Enterprise Phase exhibiting Capability"><ri:attachment ri:filename="COM2041.png" /></ac:image><br /></strong></p><h6> Actual Enterprise Phase phasing the Capability</h6>
````

<!--NOMAGIC_PAGE id=228985630 space=VR version=1 -->
## PAGE 00049: COM2042

- page_id: `228985630`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985630/COM2042
- version_number: 1
- version_date: `2023-10-12T12:19:58.115+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2042

**Message**

Actual Strategic Phase or its specialization Start Date is undefined.

**Description**

Start Date of the Actual Strategic Phase or its specialization should be defined.

**Severity**

Info

**Context element**

Actual Strategic Phase

**Solvers**

- Specify Start Date - the [CONFLUENCE_PAGE title='Date and Time Settings dialog' space='UAF13PTWRT']**Date and Time Settings** dialog opens. Specify the start date.

**Example**

**[IMAGE alt='' src='']**

###### The start date for Actual Enterprise Phase is defined.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2042</p><p><strong>Message</strong></p><p>Actual Strategic Phase or its specialization Start Date is undefined.</p><p><strong>Description</strong></p><p>Start Date of the Actual Strategic Phase or its specialization should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Actual Strategic Phase</p><p><strong>Solvers</strong></p><ul><li><strong>Specify Start Date</strong> - the <ac:link><ri:page ri:space-key="UAF13PTWRT" ri:content-title="Date and Time Settings dialog" /><ac:link-body><strong>Date and Time Settings</strong></ac:link-body></ac:link> dialog opens. Specify the start date.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COM2042.png" /></ac:image><br /></strong></p><h6> The start date for Actual Enterprise Phase is defined.</h6>
````

<!--NOMAGIC_PAGE id=228985632 space=VR version=1 -->
## PAGE 00050: COM2043

- page_id: `228985632`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985632/COM2043
- version_number: 1
- version_date: `2023-10-12T11:58:24.727+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2043

**Message**

Enterprise Vision is not linked to Actual Strategic Phase or its specializations.

**Description**

Enterprise Vision should be assigned to the Actual Strategic Phase or its specializations.

**Severity**

Info

**Constrained element**

Enterprise Vision

**Solvers**

- Select Actual Strategic Phase - select an existing Actual Strategic Phase. The Phases relationship is created between Enterprise Vision and the selected Actual Strategic Phase or its specializations.
- Create Actual Strategic Phase - create an Actual Strategic Phase. The Phases relationship is created between Enterprise Vision and the created Actual Strategic Phase or its specializations.

**Example**

[IMAGE alt='' src='']

###### Dragging the Actual Strategic Phase onto the Enterprise Vision assigns the Enterprise Vision and creates the Phases relationship.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2043</p><p><strong>Message</strong></p><p>Enterprise Vision is not linked to Actual Strategic Phase or its specializations.</p><p><strong>Description</strong></p><p>Enterprise Vision should be assigned to the Actual Strategic Phase or its specializations.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Constrained element</strong></p><p>Enterprise Vision</p><p><strong>Solvers</strong></p><ul><li><strong>Select Actual Strategic Phase</strong> - select an existing Actual Strategic Phase. The Phases relationship is created between Enterprise Vision and the selected Actual Strategic Phase or its specializations.</li><li><strong>Create Actual Strategic Phase</strong> - create an Actual Strategic Phase. The Phases relationship is created between Enterprise Vision and the created Actual Strategic Phase or its specializations.</li></ul><p><strong>Example</strong></p><p><ac:image ac:title="Enterprise Vision is linked with Actual Enterprise Phase" ac:alt="Enterprise Vision is linked with Actual Enterprise Phase"><ri:attachment ri:filename="COM2043.png" /></ac:image></p><h6>Dragging the Actual Strategic Phase onto the Enterprise Vision assigns the Enterprise Vision and creates the Phases relationship.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985634 space=VR version=1 -->
## PAGE 00051: COM2044

- page_id: `228985634`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985634/COM2044
- version_number: 1
- version_date: `2018-04-19T08:40:22.408+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2044

**Message**

Vision Statement is not defined.

**Description**

Statement of the Vision should be defined.

**Severity**

Info

**Context element**

Vision

**Solvers**

- Select Vision Statements - the Vision Statement is selected.
- Create Vision Statement - the Vision Statement is created.

**Example**

[IMAGE alt='' src='']

###### Vision statement is defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2044</p><p><strong>Message</strong></p><p>Vision Statement is not defined.</p><p><strong>Description</strong></p><p>Statement of the Vision should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Vision</p><p><strong>Solvers</strong></p><ul><li><strong>Select Vision Statements</strong> - the Vision Statement is selected.</li><li><strong>Create Vision Statement</strong> - the Vision Statement is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2044.png" /></ac:image></p><h6>Vision statement is defined</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985636 space=VR version=1 -->
## PAGE 00052: COM2045

- page_id: `228985636`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985636/COM2045
- version_number: 1
- version_date: `2018-04-19T10:57:36.659+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2045

**Message**

Capability Configuration has no doctrine defined.

**Description**

Doctrine of the Capability Configuration should be defined.

**Severity**

Info

**Context element**

Capability Configuration

**Solvers**

- Select Doctrines - the Resource Constraint is selected.
- Create Doctrine - the Resource Constraint is created.

**Example**

[IMAGE alt='' src='']

###### Doctrine is defined for Capability Configuration

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2045</p><p><strong>Message</strong></p><p>Capability Configuration has no doctrine defined.</p><p><strong>Description</strong></p><p>Doctrine of the Capability Configuration should be defined.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Capability Configuration</p><p><strong>Solvers</strong></p><ul><li><strong>Select Doctrines</strong> - the Resource Constraint is selected.</li><li><strong>Create Doctrine</strong> - the Resource Constraint is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2045.png" /></ac:image></p><h6>Doctrine is defined for Capability Configuration</h6>
````

<!--NOMAGIC_PAGE id=228985638 space=VR version=1 -->
## PAGE 00053: COM2046

- page_id: `228985638`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985638/COM2046
- version_number: 1
- version_date: `2018-04-20T07:13:19.811+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2046

**Message**

If the Resource Performer has the Resource Ports and the Resource Performer is associated with the Function using Is Capable of Performing relationship, then the Function Action should have the Pins that are synchronized with the Resource Ports. The Behavior of the Function Action is the particular Function.

**Description**

If the System Resource has the Resource Ports and the System Resource is associated with the Function using Activity Performed by Performer or Is Capable of Performing relationship, then the Function Action should have the Pins that are synchronized with the Resource Ports. The Behavior of the Function Action is the particular Function.

**Severity**

Info

**Context element**

Function Action

**Solvers**

- Synchronize Pins with Resource Ports - the Input and Output Pins are created for the Function Action.

**Example**

[IMAGE alt='' src='']

###### Input and Output pins are created

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2046</p><p><strong>Message</strong></p><p>If the Resource Performer has the Resource Ports and the Resource Performer is associated with the Function using Is Capable of Performing relationship, then the Function Action should have the Pins that are synchronized with the Resource Ports. The Behavior of the Function Action is the particular Function.</p><p><strong>Description</strong></p><p>If the System Resource has the Resource Ports and the System Resource is associated with the Function using Activity Performed by Performer or Is Capable of Performing relationship, then the Function Action should have the Pins that are synchronized with the Resource Ports. The Behavior of the Function Action is the particular Function.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Function Action</p><p><strong>Solvers</strong></p><ul><li><strong>Synchronize Pins with Resource Ports</strong> - the Input and Output Pins are created for the Function Action.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2046.png" /></ac:image></p><h6>Input and Output pins are created</h6>
````

<!--NOMAGIC_PAGE id=228985640 space=VR version=1 -->
## PAGE 00054: COM2048

- page_id: `228985640`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985640/COM2048
- version_number: 1
- version_date: `2018-04-20T07:21:51.321+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2048

**Message**

Function should be performed by the Resource Performer using the Is Capable of Performing relationship.

**Description**

Function should be performed by the System Resource using the Is Capable To Perform relationship.

**Severity**

Info

**Context element**

Function

**Solvers**

- SelectSystem Resources - the System Resource is selected.
- Create System Resource - the System Resource is created.

**Example**

**[IMAGE alt='' src='']**

###### Function is performed by System

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2048</p><p><strong>Message</strong></p><p>Function should be performed by the Resource Performer using the Is Capable of Performing relationship.</p><p><strong>Description</strong></p><p>Function should be performed by the System Resource using the Is Capable To Perform <span style="color: rgb(51,51,51);">relationship.</span></p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Function</p><p><strong>Solvers</strong></p><ul><li><strong>Select<span style="color: rgb(51,51,51);"> System Resources</span></strong> - the <span style="color: rgb(51,51,51);">System Resource</span> is selected.</li><li><strong>Create <span style="color: rgb(51,51,51);">System Resource</span></strong> - the<span style="color: rgb(51,51,51);"> System Resource</span> is created.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="2048.png" /></ac:image><br /></strong></p><h6>Function is performed by System</h6>
````

<!--NOMAGIC_PAGE id=228985642 space=VR version=1 -->
## PAGE 00055: COM2049

- page_id: `228985642`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985642/COM2049
- version_number: 1
- version_date: `2022-12-16T13:20:23.667+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2049

**Message**

Producing and Consuming Functions are not defined for Resource Exchange.

**Description**

Functions should be set as Producing or Consuming Functions for the Resource Exchange.

**Severity**

Info

**Context element**

Resource Exchange

**Solvers**

- Set Producing and Consuming Functions - the Producing and Consuming Functions are set.

**Example**

[IMAGE alt='' src='']

###### Producing and Consuming functions are defined

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2049</p><p><strong>Message</strong></p><p>Producing and Consuming Functions are not defined for Resource Exchange.</p><p><strong>Description</strong></p><p>Functions should be set as Producing or Consuming Functions for the Resource Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Resource Exchange</p><p><strong>Solvers</strong></p><ul><li><strong>Set Producing and Consuming Functions</strong> - the Producing and Consuming Functions are set.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2049.png" /></ac:image></p><h6>Producing and Consuming functions are defined</h6>
````

<!--NOMAGIC_PAGE id=228985644 space=VR version=1 -->
## PAGE 00056: COM2050

- page_id: `228985644`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985644/COM2050
- version_number: 1
- version_date: `2018-04-21T07:33:12.594+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2050

**Message**

Resource Constraint is not constraining Element.

**Description**

Constraining Element should be defined for the Resource Constraint.

**Severity**

Info

**Context element**

Resource Constraint

**Solvers**

- Select Subjects for Resource Constraint - the Constrained Element is selected.
- Create Subject for Resource Constraint - the Constrained Element is created.

**Example**

[IMAGE alt='' src='']

###### Constrained Element is selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2050</p><p><strong>Message</strong></p><p>Resource Constraint is not constraining Element.</p><p><strong>Description</strong></p><p>Constraining Element should be defined for the Resource Constraint.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Resource Constraint</p><p><strong>Solvers</strong></p><ul><li><strong>Select Subjects for Resource Constraint</strong> - the Constrained Element is selected.</li><li><strong>Create Subject for Resource Constraint</strong> - the Constrained Element is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2050.png" /></ac:image></p><h6>Constrained Element is selected</h6>
````

<!--NOMAGIC_PAGE id=228985646 space=VR version=1 -->
## PAGE 00057: COM2051

- page_id: `228985646`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985646/COM2051
- version_number: 1
- version_date: `2018-04-21T07:57:08.270+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2051

**Message**

Resource Exchange is not Implementing Operational Exchange

**Description**

Resource Exchange should be associated with the Operational Exchange using the Implements relationship.

**Severity**

Info

**Context element**

Resource Exchange

**Solvers**

- Select Operational Exchanges - the Operational Exchange is selected.
- Create Operational Exchange - the Operational Exchange is created.
- Sync Resource Exchange with Operational Exchange - the Resource Exchange is synchronized with Operational Exchange.

**Example**

[IMAGE alt='' src='']

###### Resource Excanhge implements Operational Exchange

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2051</p><p><strong>Message</strong></p><p>Resource Exchange is not Implementing Operational Exchange</p><p><strong>Description</strong></p><p>Resource Exchange should be associated with the Operational Exchange using the Implements relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Resource Exchange</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Exchanges</strong> - the Operational Exchange is selected.</li><li><strong>Create Operational Exchange</strong> - the Operational Exchange is created.</li><li><strong>Sync Resource Exchange with Operational Exchange</strong> - the Resource Exchange is synchronized with Operational Exchange.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2051.png" /></ac:image></p><h6>Resource Excanhge implements Operational Exchange</h6>
````

<!--NOMAGIC_PAGE id=228985648 space=VR version=1 -->
## PAGE 00058: COM2052

- page_id: `228985648`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985648/COM2052
- version_number: 1
- version_date: `2018-04-21T08:28:49.956+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2052

**Message**

Resource Role is not performing Function Action.

**Description**

Resource Role should perform the Function in the specific context.

**Severity**

Info

**Context element**

Resource Role

**Solution**

1. Create a swimlane with Resource Role as representer in the SV-4 diagram.
2. Create or add a Function Action to that swimlane.

A behavior of the Function Action is displayed in Performs in Context property.

**Example**

[IMAGE alt='' src='']

###### Resource Role performs Function

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2052</p><p><strong>Message</strong></p><p>Resource Role is not performing Function Action.</p><p><strong>Description</strong></p><p>Resource Role should perform the Function in the specific context.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Resource Role</p><p><strong>Solution</strong></p><ol><li>Create a swimlane with Resource Role as representer in the SV-4 diagram.</li><li>Create or add a Function Action to that swimlane.</li></ol><p>A behavior of the Function Action is displayed in Performs in Context property.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2052.png" /></ac:image></p><h6>Resource Role performs Function</h6>
````

<!--NOMAGIC_PAGE id=228985650 space=VR version=1 -->
## PAGE 00059: COM2054

- page_id: `228985650`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985650/COM2054
- version_number: 1
- version_date: `2018-04-21T09:07:05.643+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2054

**Message**

Resource Performer is not a source or target for Resource Exchange.

**Description**

System Resource should be set as a source or target for the Resource Exchange.

**Severity**

Info

**Context element**

System Resource

**Solvers**

- Create Outgoing Resource Exchange - the Resource Exchange Creation Wizard opens. The Sending System Resource will be set.
- Create Incoming Resource Exchange - the Resource Exchange Creation Wizard opens. The Receiving System Resource will be set.

**Example**

[IMAGE alt='' src='']

###### Distress Beacon System is set as target for Resource Exchange

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2054</p><p><strong>Message</strong></p><p>Resource Performer is not a source or target for Resource Exchange.</p><p><strong>Description</strong></p><p>System Resource should be set as a source or target for the Resource Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>System Resource</p><p><strong>Solvers</strong></p><ul><li><strong>Create Outgoing Resource Exchange </strong>- the Resource Exchange Creation Wizard opens. The Sending System Resource will be set.</li><li><strong>Create Incoming Resource Exchange </strong>- the Resource Exchange Creation Wizard opens. The Receiving System Resource will be set.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2054.png" /></ac:image></p><h6>Distress Beacon System is set as target for Resource Exchange</h6>
````

<!--NOMAGIC_PAGE id=228985652 space=VR version=1 -->
## PAGE 00060: COM2055

- page_id: `228985652`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985652/COM2055
- version_number: 1
- version_date: `2024-03-07T09:27:34.346+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2055

**Message**

Resource Performer should be associated with the Function using Is Capable To Perform relationship

**Description**

Resource Performer should be associated with the Function using the Is Capable To Perform relationship.

**Severity**

Info

**Context element**

Resource Performer

**Solvers**

- Select Functions - the Function is selected and the Is Capable To Perform relationship is created .
- Create Function - the Function is created together with the Is Capable To Perform relationship .

**Example**

**[IMAGE alt='' src='']**

###### System performs Function

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2055</p><p><strong>Message</strong></p><p>Resource Performer should be associated with the Function using Is Capable To Perform relationship</p><p><strong>Description</strong></p><p>Resource Performer should be associated with the Function using the Is Capable To Perform relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Resource Performer</p><p><strong>Solvers</strong></p><ul><li><strong>Select Functions</strong> - the Function is selected <span style="color: rgb(23,43,77);">and the Is Capable To Perform relationship is created</span>.</li><li><strong>Create Function</strong> - the Function is created together<span style="color: rgb(23,43,77);"> with the Is Capable To Perform relationship</span>.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="2055.png" /></ac:image><br /></strong></p><h6> System performs Function</h6>
````

<!--NOMAGIC_PAGE id=228985654 space=VR version=1 -->
## PAGE 00061: COM2056

- page_id: `228985654`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985654/COM2056
- version_number: 1
- version_date: `2018-04-21T09:18:06.671+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2056

**Message**

Resource Performer is not Exhibiting Capability

**Description**

Resource Performer should exhibit the Capability using Exhibits relationship.

**Severity**

Info

**Context element**

Resource Performer

**Solvers**

- Select Capabilities - the Capability is selected.
- Create Capability - the Capability is created.

**Example**

[IMAGE alt='' src='']

###### System exhibits Capability

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2056</p><p><strong>Message</strong></p><p>Resource Performer is not Exhibiting Capability</p><p><strong>Description</strong></p><p>Resource Performer should exhibit the Capability using Exhibits relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Resource Performer</p><p><strong>Solvers</strong></p><ul><li><strong>Select Capabilities</strong> - the Capability is selected.</li><li><strong>Create Capability</strong> - the Capability is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2056.png" /></ac:image></p><h6>System exhibits Capability</h6>
````

<!--NOMAGIC_PAGE id=228985656 space=VR version=1 -->
## PAGE 00062: COM2057

- page_id: `228985656`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985656/COM2057
- version_number: 1
- version_date: `2018-04-21T09:25:35.207+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2057

**Message**

Resource Performer is not Implementing Operational Performer.

**Description**

Resource Performer should implement the Operational Performer using the Implements relationship.

**Severity**

Info

**Context element**

Resource Performer

**Solvers**

- Select Operational Performers - the Operational Performer is selected.
- Create Operational Performer - the Operational Performer is created.

**Example**

[IMAGE alt='' src='']

###### System implements Operational Performer

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2057</p><p><strong>Message</strong></p><p>Resource Performer is not Implementing Operational Performer.</p><p><strong>Description</strong></p><p>Resource Performer should implement the Operational Performer using the Implements relationship.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Resource Performer</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Performers</strong> - the Operational Performer is selected.</li><li><strong>Create Operational Performer</strong> - the Operational Performer is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="com2057.png" /></ac:image></p><h6>System implements Operational Performer</h6>
````

<!--NOMAGIC_PAGE id=228985658 space=VR version=1 -->
## PAGE 00063: COM2059

- page_id: `228985658`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985658/COM2059
- version_number: 1
- version_date: `2018-04-21T09:27:25.385+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2059

**Message**

Data Element is not conveyed by any Resource Exchange.

**Description**

Data element should be used as the Conveyed element for either Resource Exchange.

**Severity**

Info

**Context element**

Data Element

**Solvers**

- Select Resource Exchanges - the Resource Exchanges are selected.
- Create Resource Exchange - the Resource Exchange is created.

**Example**

[IMAGE alt='' src='']

###### Data Element is conveyed

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2059</p><p><strong>Message</strong></p><p>Data Element is not conveyed by any Resource Exchange.</p><p><strong>Description</strong></p><p>Data element should be used as the Conveyed element for either Resource Exchange.</p><p><strong>Severity</strong></p><p>Info</p><p><strong>Context element</strong></p><p>Data Element</p><p><strong>Solvers</strong></p><ul><li><strong>Select Resource Exchanges</strong> - the Resource Exchanges are selected.</li><li><strong>Create Resource Exchange</strong> - the Resource Exchange is created.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="2059.png" /></ac:image></p><h6>Data Element is conveyed</h6><p> </p>
````

<!--NOMAGIC_PAGE id=228985660 space=VR version=1 -->
## PAGE 00064: COM2060

- page_id: `228985660`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985660/COM2060
- version_number: 1
- version_date: `2024-06-21T09:39:44.706+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2060

**Message**

Service is not a source or target for Service Exchange

**Description**

Service must be a Source or Target for Service Exchange.

**Severity**

info

**Constrained Element**

Service

**Solvers**

- Create Outgoing Service Exchange - the Realized Service Exchange wizard opens, where you need to select a receiving Service. When you click Finish, the appropriate Service Exchange is created.
- Create Incoming Service Exchange - the Realized Service Exchange wizard opens, where you need to select a sending Service. When you click Finish, the appropriate Service Exchange is created.

**Sample**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2060</p><p><strong>Message</strong></p><p>Service is not a source or target for Service Exchange </p><p><strong>Description</strong></p><p>Service must be a Source or Target for Service Exchange.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained Element</strong></p><p>Service </p><p><strong>Solvers</strong></p><ul><li><strong>Create Outgoing Service Exchange</strong> - the Realized Service Exchange wizard opens, where you need to select a receiving Service. When you click Finish, the appropriate Service Exchange is created.</li><li><strong>Create Incoming Service Exchange</strong> - the Realized Service Exchange wizard opens, where you need to select a sending Service. When you click Finish, the appropriate Service Exchange is created.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="COM2060.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985662 space=VR version=1 -->
## PAGE 00065: COM2061

- page_id: `228985662`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985662/COM2061
- version_number: 1
- version_date: `2024-06-21T10:43:30.093+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2061

**Message**

Producing and Consuming Functions are not defined for Service Exchange

**Description**

The Producing and Consuming Functions are not defined.

**Severity**

info

**Constrained Element**

Service Exchange

**Solvers**

- There are no automatic solvers. Extend your model manually by creating Producing and Consuming Functions.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2061</p><p><strong>Message</strong></p><p>Producing and Consuming Functions are not defined for Service Exchange</p><p><strong>Description</strong></p><p>The Producing and Consuming Functions are not defined.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained Element</strong></p><p>Service Exchange</p><p><strong>Solvers</strong></p><ul><li>There are no automatic solvers. Extend your model manually by creating Producing and Consuming Functions.</li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985663 space=VR version=1 -->
## PAGE 00066: COM2062

- page_id: `228985663`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985663/COM2062
- version_number: 1
- version_date: `2024-06-12T13:13:59.083+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2062

**Message**

Function is not Implementing Service Function or Operational Activity

**Description**

The Function is not Implementing Service Function or Operational Activity.

**Severity**

info

**Constrained element**

Function

**Solvers**

- ********Create**Operational Activity****** or Service Function - the Selec Element dialog opens, where in Creation Mode, you can create a new Operational Activity or Service Function.
- Select Operational Activity or Service Function - the Selec Element dialog opens, where you can select an existing Operational Activity or Service Function.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2062</p><p><strong>Message</strong></p><p>Function is not Implementing Service Function or Operational Activity</p><p><strong>Description</strong></p><p>The Function is not Implementing Service Function or Operational Activity.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Function</p><p><strong>Solvers</strong></p><ul><li><strong><strong><strong><strong><strong>Create </strong>Operational Activity</strong></strong></strong> or Service Function</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Operational Activity or Service Function.<span> </span></span></li><li><strong>Select Operational Activity or Service Function</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Operational Activity or Service Function.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2062.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985665 space=VR version=1 -->
## PAGE 00067: COM2063

- page_id: `228985665`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985665/COM2063
- version_number: 1
- version_date: `2024-06-12T13:24:10.677+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2063

**Message**

Service Function is not Implemented by Function

**Description**

The Service Function is not Implemented by Function.

**Severity**

info

**Constrained element**

Service Function

**Solvers**

- Create Function - the Selec Element dialog opens, where in Creation Mode, you can create a new Function.
- Select Function - the Selec Element dialog opens, where you can select an existing Function.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Abbreviation</strong></p><p style="">COM2063</p><p style=""><strong>Message</strong></p><p style="">Service Function is not Implemented by Function</p><p style=""><strong>Description</strong></p><p style="">The Service Function is not Implemented by Function.</p><p style=""><strong>Severity</strong></p><p style="">info</p><p style=""><strong>Constrained element</strong></p><p style="">Service Function</p><p style=""><strong>Solvers</strong></p><ul style=""><li><strong>Create Function</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Function.<span> </span></span></li><li><strong>Select Function</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Function.</li></ul><p style=""><strong>Example</strong></p><p style=""><ac:image><ri:attachment ri:filename="COM2063.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985667 space=VR version=1 -->
## PAGE 00068: COM2065

- page_id: `228985667`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985667/COM2065
- version_number: 1
- version_date: `2024-06-04T14:52:03.364+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2065

**Message**

Resource Interface is not Implementing Service Interface or Operational Interface.

**Description**

The Resource Interface is not implementing a Service Interface or Operational Interface.

**Severity**

info

**Constrained element**

Resource Interface

**Solvers**

- Create Operational Interface or Service Interface - the Selec Element dialog opens, where in Creation Mode, you can create a new Service Interface or Operational Interface.
- Select Operational Interface or Service Interface - the Selec Element dialog opens, where you can select an existing Service Interface or Operational Interface.

**Example**

[IMAGE alt='' src='']

###### The Service Interface was selected.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2065</p><p><strong>Message</strong></p><p>Resource Interface is not Implementing Service Interface or Operational Interface.</p><p><strong>Description</strong></p><p>The Resource Interface is not implementing a Service Interface or Operational Interface.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Resource Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Create Operational Interface or Service Interface</strong> - the <strong>Selec Element</strong> dialog opens, where in Creation Mode, you can create a new Service Interface or Operational Interface.</li><li><strong>Select Operational Interface or Service Interface</strong> - the <strong>Selec Element</strong> dialog opens, where you can select an existing Service Interface or Operational Interface.</li></ul><p><strong>Example</strong></p><p><ac:image ac:height="207"><ri:attachment ri:filename="COM2065.png" /></ac:image></p><h6>The Service Interface was selected.</h6>
````

<!--NOMAGIC_PAGE id=228985669 space=VR version=1 -->
## PAGE 00069: COM2066

- page_id: `228985669`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985669/COM2066
- version_number: 1
- version_date: `2024-06-05T11:43:26.252+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2066

**Message**

Service Interface is not Implemented by Resource Interface.

**Description**

The Service Interface is not implemented by a Resource Interface.

**Severity**

info

**Constrained element**

Service Interface

**Solvers**

- Create Resource Interface - the Selec Element dialog opens, where in Creation Mode, you can create a new Resource Interface.
- Select Resource Interface - the Selec Element dialog opens, where you can select an existing Resource Interface.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2066</p><p><strong>Message</strong></p><p>Service Interface is not Implemented by Resource Interface.</p><p><strong>Description</strong></p><p>The Service Interface is not implemented by a Resource Interface.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Service Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Create Resource Interface</strong> - <span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Resource Interface.</span></li><li><strong>Select Resource Interface</strong> - <span style="color: rgb(23,43,77);">the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where you can select an existing Resource Interface.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2066.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985671 space=VR version=1 -->
## PAGE 00070: COM2067

- page_id: `228985671`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985671/COM2067
- version_number: 1
- version_date: `2024-06-05T13:01:04.687+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2067

**Message**

Operational Interface is not Implemented by Resource Interface

**Description**

The Operational Interface is not Implemented by Resource Interface

**Severity**

info

**Constrained element**

Operational Interface

**Solvers**

- Create Resource Interface - the Selec Element dialog opens, where in Creation Mode, you can create a new Resource Interface.
- Select Resource Interface - the Selec Element dialog opens, where you can select an existing Resource Interface.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2067</p><p><strong>Message</strong></p><p>Operational Interface is not Implemented by Resource Interface</p><p><strong>Description</strong></p><p>The Operational Interface is not Implemented by Resource Interface</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Operational Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Create Resource Interface</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where in Creation Mode, you can create a new Resource Interface.</li><li><strong>Select Resource  Interface</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Resource Interface.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2067.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985673 space=VR version=1 -->
## PAGE 00071: COM2068

- page_id: `228985673`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985673/COM2068
- version_number: 1
- version_date: `2024-06-12T14:45:31.293+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2068

**Message**

Service Interface is not Implementing Operational Interface

**Description**

The Service Interface is not Implementing an Operational Interface.

**Severity**

info

**Constrained element**

Service Interface

**Solvers**

- Create Operational Interface - the Selec Element dialog opens, where in Creation Mode, you can create a new Operational Interface.
- Select Operational Interface - the Selec Element dialog opens, where you can select an existing Operational Interface.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Abbreviation</strong></p><p style="">COM2068</p><p style=""><strong>Message</strong></p><p style="">Service Interface is not Implementing Operational Interface</p><p style=""><strong>Description</strong></p><p style="">The Service Interface is not Implementing an Operational Interface.</p><p style=""><strong>Severity</strong></p><p style="">info</p><p style=""><strong>Constrained element</strong></p><p style="">Service Interface</p><p style=""><strong>Solvers</strong></p><ul style=""><li><strong>Create Operational Interface </strong>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Operational Interface.<span> </span></span></li><li><strong>Select Operational Interface</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Operational Interface.</li></ul><p style=""><strong>Example</strong></p><p style=""><ac:image><ri:attachment ri:filename="COM2068.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985675 space=VR version=1 -->
## PAGE 00072: COM2069

- page_id: `228985675`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985675/COM2069
- version_number: 1
- version_date: `2024-06-12T14:57:03.810+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2069

**Message**

Operational Interface is not Implemented by Service Interface

**Description**

The Operational Interface is not Implemented by Service Interface.

**Severity**

info

**Constrained element**

Operational Interface

**Solvers**

- Create Service Interface - the Selec Element dialog opens, where in Creation Mode, you can create a new Service Interface.
- Select Service Interface - the Selec Element dialog opens, where you can select an existing Service Interface.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Abbreviation</strong></p><p style="">COM2069</p><p style=""><strong>Message</strong></p><p style="">Operational Interface is not Implemented by Service Interface</p><p style=""><strong>Description</strong></p><p style="">The Operational Interface is not Implemented by Service Interface.</p><p style=""><strong>Severity</strong></p><p style="">info</p><p style=""><strong>Constrained element</strong></p><p style="">Operational Interface</p><p style=""><strong>Solvers</strong></p><ul style=""><li><strong>Create Service Interface </strong>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Service Interface.<span> </span></span></li><li><strong>Select Service Interface</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Service Interface.</li></ul><p style=""><strong>Example</strong></p><p style=""><ac:image><ri:attachment ri:filename="COM2069.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985677 space=VR version=1 -->
## PAGE 00073: COM2070

- page_id: `228985677`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985677/COM2070
- version_number: 1
- version_date: `2024-06-05T13:40:57.041+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2070

**Message**

Resource Connector is not Implementing Operational Connector or Resource Connector

**Description**

Resource Connector is not Implementing Operational Connector or Resource Connector

**Severity**

info

**Constrained element**

Resource Connector

**Solvers**

- Select Operational Connector or Resource Connector - in the open Select Element dialog, choose an existing Operational Connector or Resource Connector.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2070</p><p><strong>Message</strong></p><p>Resource Connector is not Implementing Operational Connector or Resource Connector</p><p><strong>Description</strong></p><p>Resource Connector is not Implementing Operational Connector or Resource Connector</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Resource Connector</p><p><strong>Solvers</strong></p><ul><li><strong>Select Operational Connector or Resource Connector </strong>- in the open <strong>Select Element</strong> dialog, choose an existing Operational Connector or Resource Connector.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2070.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985679 space=VR version=1 -->
## PAGE 00074: COM2071

- page_id: `228985679`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985679/COM2071
- version_number: 1
- version_date: `2024-06-05T14:25:53.926+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2071

**Message**

Operational Connector is not Implemented by Resource Connector

**Description**

The Operational Connector is not Implemented by Resource Connector

**Severity**

info

**Constrained element**

Operational Connector

**Solvers**

- Select Resource Connector - the Selec Element dialog opens, where you can select an existing Resource Connector.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2071</p><p><strong>Message</strong></p><p>Operational Connector is not Implemented by Resource Connector</p><p><strong>Description</strong></p><p>The Operational Connector is not Implemented by Resource Connector</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Operational Connector</p><p><strong>Solvers</strong></p><ul><li><strong>Select Resource Connector</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Resource Connector.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2071.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985681 space=VR version=1 -->
## PAGE 00075: COM2072

- page_id: `228985681`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985681/COM2072
- version_number: 1
- version_date: `2024-06-07T12:09:50.411+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2072

**Message**

Resource Connector is not Implemented by Resource Connector

**Description**

The Resource Connector is not Implemented by Resource Connector.

**Severity**

info

**Constrained element**

Resource Connector

**Solvers**

- Select Resource Connector - the Selec Element dialog opens, where you can select an existing Resource Connector.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2072</p><p><strong>Message</strong></p><p>Resource Connector is not Implemented by Resource Connector</p><p><strong>Description</strong></p><p>The Resource Connector is not Implemented by Resource Connector.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Resource Connector</p><p><strong>Solvers</strong></p><ul><li><strong>Select Resource Connector</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Resource Connector.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2072.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985683 space=VR version=1 -->
## PAGE 00076: COM2073

- page_id: `228985683`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985683/COM2073
- version_number: 1
- version_date: `2024-06-07T14:10:22.606+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2073

**Message**

Resource Role is not Implementing Operational Role

**Description**

The Resource Role is not Implementing the Operational Role.

**Severity**

info

**Constrained element**

Resource Role

**Solvers**

- Create Operational Role - the Selec Element dialog opens, where in Creation Mode, you can create a new Operational Role.
- Select Operational Role - the Selec Element dialog opens, where you can select an existing Operational Role.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2073</p><p><strong>Message</strong></p><p>Resource Role is not Implementing Operational Role</p><p><strong>Description</strong></p><p>The Resource Role is not Implementing the Operational Role.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Resource Role</p><p><strong>Solvers</strong></p><ul><li><strong>Create Operational Role</strong> -<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Operational Role.<span> </span></span><strong> </strong></li><li><strong>Select Operational Role</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Operational Role.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2073.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985685 space=VR version=1 -->
## PAGE 00077: COM2074

- page_id: `228985685`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985685/COM2074
- version_number: 1
- version_date: `2024-06-07T15:43:32.613+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2074

**Message**

Operational Role is not Implemented by Resource Role

**Description**

The Operational Role is not Implemented by a Resource Role.

**Severity**

info

**Constrained element**

Operational Role

**Solvers**

- Create Resource Role - the Selec Element dialog opens, where in Creation Mode, you can create a new Resource Role.
- Select Resource Role - the Selec Element dialog opens, where you can select an existing Resource Role.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2074</p><p><strong>Message</strong></p><p>Operational Role is not Implemented by Resource Role</p><p><strong>Description</strong></p><p>The Operational Role is not Implemented by a Resource Role.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Operational Role</p><p><strong>Solvers</strong></p><ul><li><strong>Create Resource Role</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Resource Role.<span> </span></span></li><li><strong>Select Resource Role</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Resource Role.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2074.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985687 space=VR version=1 -->
## PAGE 00078: COM2075

- page_id: `228985687`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985687/COM2075
- version_number: 1
- version_date: `2024-06-10T07:29:59.165+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2075

**Message**

Resource Information is not Implementing Operational Information

**Description**

Resource Information is not Implementing Operational Information

**Severity**

info

**Constrained element**

Resource Information

**Solvers**

- Create Operational Information - the Selec Element dialog opens, where in Creation Mode, you can create a new Operational Information.
- Select Operational Information - the Selec Element dialog opens, where you can select an existing Operational Information.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2075</p><p><strong>Message</strong></p><p>Resource Information is not Implementing Operational Information</p><p><strong>Description</strong></p><p>Resource Information is not Implementing Operational Information</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Resource Information</p><p><strong>Solvers</strong></p><ul><li><strong>Create Operational Information</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Operational Information.<span> </span></span></li><li><strong>Select Operational Information</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Operational Information.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2075.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985689 space=VR version=1 -->
## PAGE 00079: COM2076

- page_id: `228985689`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985689/COM2076
- version_number: 1
- version_date: `2024-06-10T09:31:08.242+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2076

**Message**

Operational Information is not Implemented by Resource Information

**Description**

Operational Information is not Implemented by Resource Information

**Severity**

info

**Constrained element**

Operational Information

**Solvers**

- Create Resource Information - the Selec Element dialog opens, where in Creation Mode, you can create a new Resource Information.
- Select Resource Information - the Selec Element dialog opens, where you can select an existing Resource Information.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2076</p><p><strong>Message</strong></p><p>Operational Information is not Implemented by Resource Information</p><p><strong>Description</strong></p><p>Operational Information is not Implemented by Resource Information</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Operational Information</p><p><strong>Solvers</strong></p><ul><li><strong>Create Resource Information</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Resource Information.<span> </span></span></li><li><strong>Select Resource Information</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Resource Information.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2076.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985691 space=VR version=1 -->
## PAGE 00080: COM2077

- page_id: `228985691`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985691/COM2077
- version_number: 1
- version_date: `2024-06-10T09:59:04.978+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2077

**Message**

Operational Information is not Implementing Strategic Information

**Description**

Operational Information is not Implementing Strategic Information.

**Severity**

info

**Constrained element**

Operational Information

**Solvers**

- Create Strategic Information - the Selec Element dialog opens, where in Creation Mode, you can create a new Strategic Information.
- Select Strategic Information - the Selec Element dialog opens, where you can select an existing Strategic Information.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2077</p><p><strong>Message</strong></p><p>Operational Information is not Implementing Strategic Information</p><p><strong>Description</strong></p><p>Operational Information is not Implementing Strategic Information.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Operational Information</p><p><strong>Solvers</strong></p><ul><li><strong>Create Strategic Information</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Strategic Information.<span> </span></span></li><li><strong>Select Strategic Information</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Strategic Information.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2077.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985693 space=VR version=1 -->
## PAGE 00081: COM2078

- page_id: `228985693`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985693/COM2078
- version_number: 1
- version_date: `2024-06-10T10:16:03.873+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2078

**Message**

Strategic Information is not Implemented by Operational Information

**Description**

Strategic Information is not Implemented by Operational Information

**Severity**

info

**Constrained element**

Strategic Information

**Solvers**

- Create Operational Information - the Selec Element dialog opens, where in Creation Mode, you can create a new Operational Information.
- Select Operational Information - the Selec Element dialog opens, where you can select an existing Operational Information.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2078</p><p><strong>Message</strong></p><p>Strategic Information is not Implemented by Operational Information</p><p><strong>Description</strong></p><p>Strategic Information is not Implemented by Operational Information</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Strategic Information</p><p><strong>Solvers</strong></p><ul><li><strong>Create Operational Information</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Operational Information.<span> </span></span></li><li><strong>Select Operational Information</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Operational Information.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2078.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985695 space=VR version=1 -->
## PAGE 00082: COM2079

- page_id: `228985695`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985695/COM2079
- version_number: 1
- version_date: `2024-06-12T07:45:20.009+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2079

**Message**

Resource Service is not Implementing Service

**Description**

Resource Service is not Implementing Service.

**Severity**

info

**Constrained element**

Resource Service

**Solvers**

- Create Service - the Selec Element dialog opens, where in Creation Mode, you can create a new Service.
- Select Service - the Selec Element dialog opens, where you can select an existing Service.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2079</p><p><strong>Message</strong></p><p>Resource Service is not Implementing Service</p><p><strong>Description</strong></p><p>Resource Service is not Implementing Service.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Resource Service</p><p><strong>Solvers</strong></p><ul><li><strong>Create Service</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Service.<span> </span></span></li><li><strong>Select Service</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Service.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2079.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985697 space=VR version=1 -->
## PAGE 00083: COM2080

- page_id: `228985697`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985697/COM2080
- version_number: 1
- version_date: `2024-06-12T07:39:47.919+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2080

**Message**

Service is not Implemented by Resource Service

**Description**

The Service is not Implemented by Resource Service.

**Severity**

info

**Constrained element**

Service

**Solvers**

- Create Resource Service - the Selec Element dialog opens, where in Creation Mode, you can create a new Resource Service.
- Select Resource Service - the Selec Element dialog opens, where you can select an existing Resource Service.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2080</p><p><strong>Message</strong></p><p>Service is not Implemented by Resource Service</p><p><strong>Description</strong></p><p>The Service is not Implemented by Resource Service.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Service</p><p><strong>Solvers</strong></p><ul><li><strong>Create Resource Service</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Resource Service.<span> </span></span></li><li><strong>Select Resource Service</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Resource Service.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2080.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985699 space=VR version=1 -->
## PAGE 00084: COM2081

- page_id: `228985699`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985699/COM2081
- version_number: 1
- version_date: `2024-06-12T11:01:32.427+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2081

**Message**

Architecture is not Implementing Actual Strategic Phase

**Description**

Architecture is not Implementing Actual Strategic Phase.

**Severity**

info

**Constrained element**

Architecture

**Solvers**

- Create Actual Strategic Phase - the Selec Element dialog opens, where in Creation Mode, you can create a new Actual Strategic Phase.
- Select Actual Strategic Phase - the Selec Element dialog opens, where you can select an existing Actual Strategic Phase.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Abbreviation</strong></p><p style="">COM2081</p><p style=""><strong>Message</strong></p><p style="">Architecture is not Implementing Actual Strategic Phase</p><p style=""><strong>Description</strong></p><p style="">Architecture is not Implementing Actual Strategic Phase.</p><p style=""><strong>Severity</strong></p><p style="">info</p><p style=""><strong>Constrained element</strong></p><p style="">Architecture</p><p style=""><strong>Solvers</strong></p><ul style=""><li><strong>Create Actual Strategic Phase</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Actual Strategic Phase.<span> </span></span></li><li><strong>Select Actual Strategic Phase</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Actual Strategic Phase.</li></ul><p style=""><strong>Example</strong></p><p style=""><ac:image><ri:attachment ri:filename="COM2081.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985701 space=VR version=1 -->
## PAGE 00085: COM2082

- page_id: `228985701`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985701/COM2082
- version_number: 1
- version_date: `2024-06-12T11:51:41.435+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2082

**Message**

Operational Activity is not Implementing Actual Strategic Phase

**Description**

Operational Activity is not Implementing Actual Strategic Phase.

**Severity**

info

**Constrained element**

Operational Activity

**Solvers**

- Create Actual Strategic Phase - the Selec Element dialog opens, where in Creation Mode, you can create a new Actual Strategic Phase.
- Select Actual Strategic Phase - the Selec Element dialog opens, where you can select an existing Actual Strategic Phase.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Abbreviation</strong></p><p style="">COM2082</p><p style=""><strong>Message</strong></p><p style="">Operational Activity is not Implementing Actual Strategic Phase</p><p style=""><strong>Description</strong></p><p style="">Operational Activity is not Implementing Actual Strategic Phase.</p><p style=""><strong>Severity</strong></p><p style="">info</p><p style=""><strong>Constrained element</strong></p><p style="">Operational Activity</p><p style=""><strong>Solvers</strong></p><ul style=""><li><strong>Create Actual Strategic Phase</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Actual Strategic Phase.<span> </span></span></li><li><strong>Select Actual Strategic Phase</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Actual Strategic Phase.</li></ul><p style=""><strong>Example</strong></p><p style=""><ac:image><ri:attachment ri:filename="COM2082.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985703 space=VR version=1 -->
## PAGE 00086: COM2083

- page_id: `228985703`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985703/COM2083
- version_number: 1
- version_date: `2024-06-12T12:07:14.910+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2083

**Message**

Actual Strategic Phase is not Implemented by Architecture or Operational Activity

**Description**

The Actual Strategic Phase is not Implemented by Architecture or Operational Activity.

**Severity**

info

**Constrained element**

Actual Strategic Phase

**Solvers**

- Create Architecture or Operational Activity - the Selec Element dialog opens, where in Creation Mode, you can create a new Architecture or Operational Activity.
- Select Architecture or Operational Activity - the Selec Element dialog opens, where you can select an existing Architecture or Operational Activity.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2083</p><p><strong>Message</strong></p><p>Actual Strategic Phase is not Implemented by Architecture or Operational Activity</p><p><strong>Description</strong></p><p>The Actual Strategic Phase is not Implemented by Architecture or Operational Activity.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained element</strong></p><p>Actual Strategic Phase</p><p><strong>Solvers</strong></p><ul><li><strong>Create Architecture or Operational Activity</strong><span> </span>-<span style="color: rgb(23,43,77);"><span> </span>the<span> </span></span><strong style="text-align: left;">Selec Element</strong><span style="color: rgb(23,43,77);"><span> </span>dialog opens, where in Creation Mode, you can create a new Architecture or Operational Activity.<span> </span></span></li><li><strong>Select Architecture or Operational Activity</strong><span> </span>- the<span> </span><strong>Selec Element</strong><span> </span>dialog opens, where you can select an existing Architecture or Operational Activity.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2083.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985705 space=VR version=1 -->
## PAGE 00087: COM2084

- page_id: `228985705`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985705/COM2084
- version_number: 1
- version_date: `2024-03-08T08:05:45.996+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2084

**Message**

The Operational Exchange has no Conveyed Items.

**Description**

The Operational Exchange has no Conveyed Items.

**Severity**

warning

**Constrained element**

Operational Exchange

**Solvers**

- Select Conveyed Item - the opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style=""><strong>Abbreviation</strong></p><p style="">COM2084</p><p style=""><strong>Message</strong></p><p style="">The Operational Exchange has no Conveyed Items.</p><p style=""><strong>Description</strong></p><p style="">The Operational Exchange has no Conveyed Items.</p><p style=""><strong>Severity</strong></p><p style="">warning</p><p style=""><strong>Constrained element</strong></p><p style="">Operational Exchange</p><p style=""><strong>Solvers</strong></p><ul><li style=""><strong><span style="color: rgb(23,43,77);">Select Conveyed Item -</span></strong><span style="color: rgb(23,43,77);"> the</span><strong><span style="color: rgb(23,43,77);"> </span></strong><span style="color: rgb(23,43,77);">opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.</span></li></ul><p style=""><strong>Example</strong></p><p style=""><ac:image><ri:attachment ri:filename="COM2084.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985707 space=VR version=1 -->
## PAGE 00088: COM2085

- page_id: `228985707`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985707/COM2085
- version_number: 1
- version_date: `2024-03-08T10:06:26.126+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2085

**Message**

The Service Exchange has no Conveyed Items.

**Description**

The Service Exchange has no Conveyed Items.

**Severity**

warning

**Constrained element**

Service Exchange

**Solvers**

- Select Conveyed Item - the opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2085</p><p><strong>Message</strong></p><p>The Service Exchange has no Conveyed Items.</p><p><strong>Description</strong></p><p>The Service Exchange has no Conveyed Items.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained element</strong></p><p>Service Exchange</p><p><strong>Solvers</strong></p><ul><li><strong><span style="color: rgb(23,43,77);">Select Conveyed Item -</span></strong><span style="color: rgb(23,43,77);"><span> </span>the</span><strong><span style="color: rgb(23,43,77);"><span> </span></span></strong><span style="color: rgb(23,43,77);">opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2085.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985709 space=VR version=1 -->
## PAGE 00089: COM2086

- page_id: `228985709`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985709/COM2086
- version_number: 1
- version_date: `2024-03-08T10:54:56.906+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2086

**Message**

The Resource Exchange has no Conveyed Items.

**Description**

The Resource Exchange has no Conveyed Items.

**Severity**

warning

**Constrained element**

Resource Exchange

**Solvers**

- Select Conveyed Item - the opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2086</p><p><strong>Message</strong></p><p>The Resource Exchange has no Conveyed Items.</p><p><strong>Description</strong></p><p>The Resource Exchange has no Conveyed Items.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained element</strong></p><p>Resource Exchange</p><p><strong>Solvers</strong></p><ul><li><strong><span style="color: rgb(23,43,77);">Select Conveyed Item -</span></strong><span style="color: rgb(23,43,77);"><span> </span>the</span><strong><span style="color: rgb(23,43,77);"><span> </span></span></strong><span style="color: rgb(23,43,77);">opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2086.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985711 space=VR version=1 -->
## PAGE 00090: COM2087

- page_id: `228985711`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985711/COM2087
- version_number: 1
- version_date: `2024-03-08T13:49:29.168+01:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2087

**Message**

The Strategic Exchange has no Conveyed Items.

**Description**

The Strategic Exchange has no Conveyed Items.

**Severity**

warning

**Constrained element**

Strategic Exchange

**Solvers**

- Select Conveyed Item - the opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2087</p><p><strong>Message</strong></p><p>The Strategic Exchange has no Conveyed Items.</p><p><strong>Description</strong></p><p>The Strategic Exchange has no Conveyed Items.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained element</strong></p><p>Strategic Exchange</p><p><strong>Solvers</strong></p><ul><li><strong><span style="color: rgb(23,43,77);">Select Conveyed Item -</span></strong><span style="color: rgb(23,43,77);"><span> </span>the</span><strong><span style="color: rgb(23,43,77);"><span> </span></span></strong><span style="color: rgb(23,43,77);">opens Select Element dialog opens where you can choose Conveyed Item for the validated exchange.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2087.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985713 space=VR version=1 -->
## PAGE 00091: COM2088

- page_id: `228985713`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985713/COM2088
- version_number: 1
- version_date: `2024-04-09T14:28:34.484+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2088

**Message**

Realized <exchang name> Exchange has no Conveyed Items.

**Description**

The realized <exchange name> Exchange has no Conveyed Items.

**Severity**

warning

**Constrained element**

Operational Connector, Association, Operational Activity Edge, Operational Message

**Solvers**

- Select Conveyed Item - the Select Element dialog opens where you can choose the Conveyed Item for the validated exchange.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2088</p><p><strong>Message</strong></p><p>Realized &lt;exchang name&gt; Exchange has no Conveyed Items.</p><p><strong>Description</strong></p><p>The realized &lt;exchange name&gt; Exchange has no Conveyed Items.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained element</strong></p><p>Operational Connector, Association, Operational Activity Edge, Operational Message</p><p><strong>Solvers</strong></p><ul><li><strong>Select Conveyed Item - </strong>the <strong>Select Element</strong> dialog opens where you can choose the Conveyed Item for the validated exchange.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2088.png" /></ac:image></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985715 space=VR version=1 -->
## PAGE 00092: COM2089

- page_id: `228985715`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985715/COM2089
- version_number: 1
- version_date: `2024-04-09T14:28:52.029+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2089

**Message**

Realized <exchang name> Service Exchange has no Conveyed Items.

**Description**

The realized <exchang name> Service Exchange has no Conveyed Items.

**Severity**

warning

**Constrained element**

Service Function Edge, Service Message, Service Connector, Association

**Solvers**

- **Select Conveyed Item** - the Select Element dialog opens where you can choose the Conveyed Item for the validated exchange.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2089</p><p><strong>Message</strong></p><p>Realized &lt;exchang name&gt; Service Exchange has no Conveyed Items.</p><p><strong>Description</strong></p><p>The realized &lt;exchang name&gt; Service Exchange has no Conveyed Items.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained element</strong></p><p>Service Function Edge, Service Message, Service Connector, Association</p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Select Conveyed Item</strong> - the Select Element dialog opens where you can choose the Conveyed Item for the validated exchange.</span></li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COM2089.png" /></ac:image></strong></p>
````

<!--NOMAGIC_PAGE id=228985717 space=VR version=1 -->
## PAGE 00093: COM2090

- page_id: `228985717`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985717/COM2090
- version_number: 1
- version_date: `2024-04-09T14:29:11.832+02:00`
- ancestors: Validation Rules > UAF validation rules > Completeness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COM2090

**Message**

Realized <exchang name> Resource Exchange has no Conveyed Items.

**Description**

The realized <exchang name> Resource Exchange has no Conveyed Items.

**Severity**

warning

**Constrained element**

Function Edge, Resource Message, Resource Connector, Association

**Solvers**

- **Select Conveyed Item**- the Select Element dialog opens where you can choose the Conveyed Item for the validated exchange.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COM2090</p><p><strong>Message</strong></p><p>Realized &lt;exchang name&gt; Resource Exchange has no Conveyed Items.</p><p><strong>Description</strong></p><p>The realized &lt;exchang name&gt; Resource Exchange has no Conveyed Items.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained element</strong></p><p>Function Edge, Resource Message, Resource Connector, Association</p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Select Conveyed Item</strong><span> </span>- the Select Element dialog opens where you can choose the Conveyed Item for the validated exchange.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COM2090.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985556 space=VR version=1 -->
## PAGE 00094: Completeness validation rules

- page_id: `228985556`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985556/Completeness+validation+rules
- version_number: 1
- version_date: `2016-02-23T09:32:26.069+01:00`
- ancestors: Validation Rules > UAF validation rules
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f3e8608d-7a8c-4ec7-b16b-9cd51b4bc687" /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=64948430 space=VR version=16 -->
## PAGE 00095: Connector Property

- page_id: `64948430`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/64948430/Connector+Property
- version_number: 16
- version_date: `2021-01-12T13:11:48.468+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ConnectorProperty

**Description**

This validation rule checks if the Connector Property is connected with the matching Connector.

**Severity**

warning****

**Constrained Element**

Connector Property****

**Solvers**

- Synchronize - reconnects the Connector Property to matching Connector in the model.

**Example**

**[IMAGE alt='' src='']**

###### The *Shower Water Delivery* Connector Property is synchronized with the*shawerWaterDelivery* Connector.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ConnectorProperty</p><p><strong>Description</strong></p><p>This validation rule checks if the Connector Property is connected with the matching Connector. </p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Connector Property<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Synchronize </strong>- <ac:inline-comment-marker ac:ref="599961ec-d644-4e98-bf3b-51e251f5d5cf">reconnects the Connector Property to matching Connector in the model.</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="599961ec-d644-4e98-bf3b-51e251f5d5cf"><br /></ac:inline-comment-marker></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="ConnectorProperty.png" /></ac:image></strong></p><h6 style="text-align: center;">The <em>Shower Water Delivery</em> Connector Property is synchronized with the<em> shawerWaterDelivery</em> Connector.</h6>
````

<!--NOMAGIC_PAGE id=228985493 space=VR version=1 -->
## PAGE 00096: COR2001

- page_id: `228985493`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985493/COR2001
- version_number: 1
- version_date: `2018-03-29T07:23:27.385+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2001

**Message**

Actual Project Milestone date exceeds Actual Project time period

**Description**

Actual Project Milestone date cannot exceed the Actual Project time period (start date - end date).

**Severity**

Error

**Context element**

Instance Specification

**Solvers**

You can select one of the following solvers:

- Autocorrect - automatically fix Actual Project Milestone Date to Actual Projects start Date.
- Edit Actual Project Milestone Date - the UPDM Time Dialog is opened where you can set the new Actual Project Milestone date.

**Example**

[IMAGE alt='' src='']

###### StartPhase milestone date changed to start date of project using Autocorrect solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2001</p><p><strong>Message</strong></p><p>Actual Project Milestone date exceeds Actual Project time period</p><p><strong>Description</strong></p><p>Actual Project Milestone date cannot exceed the Actual Project time period (start date - end date).</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Instance Specification</p><p><strong>Solvers</strong></p><p>You can select one of the following solvers:</p><ul><li><strong>Autocorrect</strong> - automatically fix Actual Project Milestone Date to Actual Projects start Date.</li><li><strong>Edit Actual Project Milestone Date</strong> - the UPDM Time Dialog is opened where you can set the new Actual Project Milestone date.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2001.png" /></ac:image></p><h6>StartPhase milestone date changed to start date of project using Autocorrect solver</h6>
````

<!--NOMAGIC_PAGE id=228985495 space=VR version=1 -->
## PAGE 00097: COR2002

- page_id: `228985495`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985495/COR2002
- version_number: 1
- version_date: `2019-04-15T08:58:50.774+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2002

**Message**

Incorrect Actual Project Milestone nesting

**Description**

If Actual Milestone is Nested in the Project but it is not set in Project's milestones property, it should be fixed.

**Severity**

Error

**Context element**

Nested Actual Project

**Solvers**

You can use one of the following solvers:

- Remove this Shape - remove Nested Actual Project Milestone from Diagram.
- Move Element Here - update ownedMilestones property for Nesting Actual Project to the Nested Actual Project Milestone.
- De-nest this Shape - de-Nest Nested Actual Project Milestone.

**Example**

**[IMAGE alt='' src='']**

###### Property ownedMilestone updated using Move Element Here solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2002</p><p><strong>Message</strong></p><p>Incorrect Actual Project Milestone nesting</p><p><strong>Description</strong></p><p>If Actual Milestone is Nested in the Project but it is not set in Project's milestones property, it should be fixed.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Nested Actual Project</p><p><strong>Solvers</strong></p><p>You can use one of the following solvers:</p><ul><li><strong>Remove this Shape</strong> - remove Nested Actual Project Milestone from Diagram.</li><li><strong>Move Element Here</strong> - update ownedMilestones property for Nesting Actual Project to the Nested Actual Project Milestone.</li><li><strong>De-nest this Shape</strong> - de-Nest Nested Actual Project Milestone.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="cor2002.png" /></ac:image></strong></p><h6>Property ownedMilestone updated using Move Element Here solver</h6>
````

<!--NOMAGIC_PAGE id=228985497 space=VR version=1 -->
## PAGE 00098: COR2003

- page_id: `228985497`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985497/COR2003
- version_number: 1
- version_date: `2018-03-29T08:30:08.435+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2003

**Message**

Incorrect Actual Project nesting

**Description**

If Actual Project is Nested but its whole property is not set or incorrect, it should be set.

**Severity**

Error

**Context element**

Nested Actual Project

**Solvers**

You can use one of the following solvers:

- Remove this Shape - remove Nested Actual Project from Diagram.
- Move Element Here - change whole property for Nested Actual Project to the Nesting Actual Project.
- De-nest this Shape - de-Nest Nested Actual Project.

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2003</p><p><strong>Message</strong></p><p>Incorrect Actual Project nesting</p><p><strong>Description</strong></p><p>If Actual Project is Nested but its whole property is not set or incorrect, it should be set.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Nested Actual Project</p><p><strong>Solvers</strong></p><p>You can use one of the following solvers:</p><ul><li><strong>Remove this Shape</strong> - remove Nested Actual Project from Diagram.</li><li><strong>Move Element Here</strong> - change whole property for Nested Actual Project to the Nesting Actual Project.</li><li><strong>De-nest this Shape</strong> - de-Nest Nested Actual Project.</li></ul><p><strong>Example</strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=296124827 space=VR version=1 -->
## PAGE 00099: COR2004

- page_id: `296124827`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/296124827/COR2004
- version_number: 1
- version_date: `2026-03-23T09:54:52.042+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

#### WARNING: Deprecated

Deprecated

This validation rule is deprecated stating with the 2026x version.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="51951212-3720-49b8-a5d7-36b07c932f56"><ac:parameter ac:name="title">Deprecated</ac:parameter><ac:rich-text-body><p>This validation rule is deprecated stating with the 2026x version.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=228985498 space=VR version=1 -->
## PAGE 00100: COR2005

- page_id: `228985498`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985498/COR2005
- version_number: 1
- version_date: `2018-03-29T08:31:38.809+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2005

**Message**

Order of Actual Project dates is incorrect in a project sequence

**Description**

Actual Project Dates should correspond to their sequence.

**Severity**

Error

**Context element**

Dependency

**Solvers**

You can use one of the following solvers:

- Autocorrect - change Project Sequence Project To start Date to be equal to Project From start Date.
- Edit From Project Start Date - open Date Dialog to specify Project Milestone's Project From Start Date.
- Edit To Project Start Date - open Date Dialog to specify Project Sequences Project To Start Date.
- Remove Project Sequence - remove Project Sequence from Model.
- Change Project Sequence Direction - change Direction of Project Sequence.

**Example**

[IMAGE alt='' src='']

###### Changed Project dates using Edit To Project Start Date solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2005</p><p><strong>Message</strong></p><p>Order of Actual Project dates is incorrect in a project sequence</p><p><strong>Description</strong></p><p>Actual Project Dates should correspond to their sequence.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Dependency</p><p><strong>Solvers</strong></p><p>You can use one of the following solvers:</p><ul><li><strong>Autocorrect</strong> - change Project Sequence Project To start Date to be equal to Project From start Date.</li><li><strong>Edit From Project Start Date</strong> - open Date Dialog to specify Project Milestone's Project From Start Date.</li><li><strong>Edit To Project Start Date</strong> - open Date Dialog to specify Project Sequences Project To Start Date.</li><li><strong>Remove Project Sequence</strong> - remove Project Sequence from Model.</li><li><strong>Change Project Sequence Direction</strong> - change Direction of Project Sequence.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2005.png" /></ac:image></p><h6>Changed Project dates using Edit To Project Start Date solver</h6>
````

<!--NOMAGIC_PAGE id=228985500 space=VR version=1 -->
## PAGE 00101: COR2006

- page_id: `228985500`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985500/COR2006
- version_number: 1
- version_date: `2018-03-30T13:31:43.911+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2006

**Message**

Non Measurable elements cannot have Actual Measurement Set assigned

**Description**

All UAF Elements have property called Measurement Set. It is filled in with the Measurement Sets and marks that the element is measurable. Actual Measurement Set instantiated from these Measurement Sets contains actual Measurements of the particular element. Only measurable UAF elements can be measured by Actual Measurements. This rule should mark UAF elements that are Measured by Actual Measurements, but do not have Measurement Sets defined (is not measurable).

**Severity**

Error

**Context element**

UAF Element with Actual Measurement Set assigned.

**Solvers**

You can use one of the following solvers:

- Remove Measurement Set - removes Current Actual Measurement Set from UAF Element actual Measurements property.
- Make Element Measurable - if Actual Measurement Set has Classifier defined (Measurement Set), assigns it to the Measurement Sets property of the same UAF element. Otherwise Creates new Measurement Set under the same owner Actual Measurement Set is and sets it as its Classifier. Also sets the Measurement Set as Measurement Sets property value for the same UAF Element Actual Measurement Set is assigned to.

**Example**

[IMAGE alt='' src='']

###### Specified Property Set using Make Element Measurable solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2006</p><p><strong>Message</strong></p><p>Non Measurable elements cannot have Actual Measurement Set assigned</p><p><strong>Description</strong></p><p>All UAF Elements have property called Measurement Set. It is filled in with the Measurement Sets and marks that the element is measurable. Actual Measurement Set instantiated from these Measurement Sets contains actual Measurements of the particular element. Only measurable UAF elements can be measured by Actual Measurements. This rule should mark UAF elements that are Measured by Actual Measurements, but do not have Measurement Sets defined (is not measurable).</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>UAF Element with Actual Measurement Set assigned.</p><p><strong>Solvers</strong></p><p>You can use one of the following solvers:</p><ul><li><strong>Remove Measurement Set</strong> - removes Current Actual Measurement Set from UAF Element actual Measurements property.</li><li><strong>Make Element Measurable</strong> - if Actual Measurement Set has Classifier defined (Measurement Set), assigns it to the Measurement Sets property of the same UAF element. Otherwise Creates new Measurement Set under the same owner Actual Measurement Set is and sets it as its Classifier. Also sets the Measurement Set as Measurement Sets property value for the same UAF Element Actual Measurement Set is assigned to.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2006.png" /></ac:image></p><h6>Specified Property Set using Make Element Measurable solver</h6>
````

<!--NOMAGIC_PAGE id=228985502 space=VR version=1 -->
## PAGE 00102: COR2007

- page_id: `228985502`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985502/COR2007
- version_number: 1
- version_date: `2018-03-29T07:28:46.636+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2007

**Message**

Exchange from and/or to elements do not match Swimlane representation

**Description**

Requirements for validation rule for detecting exchanges violating Swimlane representatives in activity diagrams. The representation of the Swimlane of the operational activity and the performing node should match.

**Severity**

Warning

**Context element**

Activity Edge

**Solvers**

- Remove Realization of the Operational Exchange - removes the realization of the Operational Exchange.
- Remove Operational Activity Action[s] from the Swimlanes - removes the Operational Activity Action from the Swimlane.

**Example**

[IMAGE alt='' src='']

###### Swimlane representation is changed to Search Node according to the structural model

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2007</p><p><strong>Message</strong></p><p>Exchange from and/or to elements do not match Swimlane representation</p><p><strong>Description</strong></p><p>Requirements for validation rule for detecting exchanges violating Swimlane representatives in activity diagrams. The representation of the Swimlane of the operational activity and the performing node should match.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Remove Realization of the Operational Exchange</strong> - removes the realization of the Operational Exchange.</li><li><strong>Remove Operational Activity Action[s] from the Swimlanes</strong> - removes the Operational Activity Action from the Swimlane.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2007.png" /></ac:image></p><h6>Swimlane representation is changed to Search Node according to the structural model</h6>
````

<!--NOMAGIC_PAGE id=228985504 space=VR version=1 -->
## PAGE 00103: COR2008

- page_id: `228985504`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985504/COR2008
- version_number: 1
- version_date: `2018-03-29T09:27:25.503+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2008

**Message**

Element's End Date is earlier than the Start Date

**Description**

Requirements for validation rule for End Date property should not be earlier than Start Date property validation rule.

**Severity**

Warning

**Context element**

Fill Posts, Enterprise Phase, Forecast, Actual Project

**Solvers**

- Change Start Date - open Date Dialog to specify the new Start Date.
- Change End Date - open Date Dialog to specify the new End Date.

**Example**

[IMAGE alt='' src='']

###### End date changed using Change End Date solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2008</p><p><strong>Message</strong></p><p>Element's End Date is earlier than the Start Date</p><p><strong>Description</strong></p><p>Requirements for validation rule for End Date property should not be earlier than Start Date property validation rule.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Fill Posts, Enterprise Phase, Forecast, Actual Project</p><p><strong>Solvers</strong></p><ul><li><strong>Change Start Date</strong> - open Date Dialog to specify the new Start Date.</li><li><strong>Change End Date</strong> - open Date Dialog to specify the new End Date.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2008.png" /></ac:image></p><h6>End date changed using Change End Date solver</h6>
````

<!--NOMAGIC_PAGE id=228985506 space=VR version=1 -->
## PAGE 00104: COR2009

- page_id: `228985506`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985506/COR2009
- version_number: 1
- version_date: `2025-01-17T09:35:06.526+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2009

**Message**

Operational Connector end Role Owners should match Information Source and Target of realized Operational Exchange.

**Description**

The incorrect Operational Exchange realization by Operational Connector between Operational Ports.

**Severity**

Error

**Context element**

Connector

**Solvers**

- Correct Realization - the realization is corrected.
- Remove Realization - the realization is removed. The excess realization is identified according to the Realizing Connector property of the Operational Exchange.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2009</p><p><strong>Message</strong></p><p>Operational Connector end Role Owners should match Information Source and Target of realized Operational Exchange.</p><p><strong>Description</strong></p><p>The incorrect Operational Exchange realization by Operational Connector between Operational Ports.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Connector</p><p><strong>Solvers</strong></p><ul><li><strong>Correct Realization</strong> - the realization is corrected.</li><li><strong>Remove Realization</strong> - the realization is removed. The excess realization is identified according to the Realizing Connector property of the Operational Exchange.</li></ul>
````

<!--NOMAGIC_PAGE id=228985507 space=VR version=1 -->
## PAGE 00105: COR2010

- page_id: `228985507`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985507/COR2010
- version_number: 1
- version_date: `2018-04-06T14:06:11.784+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2010

**Message**

Operational Connector Operational Role Types should match Information Source and Target of realized Operational Exchange.

**Description**

The Source and Target of the realized Operational Exchange do not match Role Types of the Operational Exchange.

**Severity**

Error

**Context element**

Connector

**Solvers**

- Correct Realization - the realization is corrected. The types of the Node Roles are changed according to the target and Source of the Operational Exchange.
- Remove Realization - the realization is removed. The excess realization is identified according to the Realizing Connector property of the Operational Exchange.

**Example**

[IMAGE alt='' src='']

###### Incorrect Operational Connector is removed using Remove Realization solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2010</p><p><strong>Message</strong></p><p>Operational Connector Operational Role Types should match Information Source and Target of realized Operational Exchange.</p><p><strong>Description</strong></p><p>The Source and Target of the realized Operational Exchange do not match Role Types of the Operational Exchange.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Connector</p><p><strong>Solvers</strong></p><ul><li><strong>Correct Realization</strong> - the realization is corrected. The types of the Node Roles are changed according to the target and Source of the Operational Exchange.</li><li><strong>Remove Realization</strong> - the realization is removed. The excess realization is identified according to the Realizing Connector property of the Operational Exchange.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2010.png" /></ac:image></p><h6>Incorrect Operational Connector is removed using Remove Realization solver</h6>
````

<!--NOMAGIC_PAGE id=228985509 space=VR version=1 -->
## PAGE 00106: COR2011

- page_id: `228985509`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985509/COR2011
- version_number: 1
- version_date: `2018-04-04T13:15:05.856+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2011

**Message**

Information Source and Target of Operational Exchange should perform Operational Activities that are behaviors of Operational Activity Actions connected by Operational Activity Edge.

**Description**

Operational Activity Actions are connected by Operational Activity Edge that realizes the Operational Exchange. The Source and Target of the Operational Exchange do not perform Operational Activities that are behaviors of Operational Activity Actions. The inconsistency should be fixed.

**Severity**

Error

**Context element**

Activity Edge

**Solvers**

- Correct Realization - exchange realization by activity edge is corrected.
- Remove Realization - the realization is removed.

**Example**

[IMAGE alt='' src='']

###### Exchange realization is changed using Correct Realization solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2011</p><p><strong>Message</strong></p><p>Information Source and Target of Operational Exchange should perform Operational Activities that are behaviors of Operational Activity Actions connected by Operational Activity Edge.</p><p><strong>Description</strong></p><p>Operational Activity Actions are connected by Operational Activity Edge that realizes the Operational Exchange. The Source and Target of the Operational Exchange do not perform Operational Activities that are behaviors of Operational Activity Actions. The inconsistency should be fixed.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Correct Realization</strong> - exchange realization by activity edge is corrected.</li><li><strong>Remove Realization</strong> - the realization is removed.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2011.png" /></ac:image></p><h6>Exchange realization is changed using Correct Realization solver</h6>
````

<!--NOMAGIC_PAGE id=228985511 space=VR version=1 -->
## PAGE 00107: COR2012

- page_id: `228985511`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985511/COR2012
- version_number: 1
- version_date: `2023-03-20T14:08:51.732+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2012

**Message**

Realized Operational Exchange should convey one and only one Operational Exchange Item.

**Description**

Activity Edge connecting Pins or Activity Parameters can realize Information Flows that convey only one Exchange Item.

**Severity**

Warning

**Context element**

Activity Edge

**Solvers**

- Add / Remove Conveyed Item - add a conveyed item if it is missing or select which conveyed item should be removed.
- Remove Operational Exchange Realization - all realized Operational Exchange Items are deselected in the Operational Exchange Manager.

**Example**

[IMAGE alt='' src='']

###### Message conveyed item is removed from the Operational Exchange specification

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2012</p><p><strong>Message</strong></p><p>Realized Operational Exchange should convey one and only one Operational Exchange Item.</p><p><strong>Description</strong></p><p>Activity Edge connecting Pins or Activity Parameters can realize Information Flows that convey only one Exchange Item.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Add / Remove Conveyed Item</strong> - add a conveyed item if it is missing or select which conveyed item should be removed.</li><li><strong>Remove Operational Exchange Realization</strong> - all realized Operational Exchange Items are deselected in the Operational Exchange Manager.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2012.png" /></ac:image></p><h6>Message conveyed item is removed from the Operational Exchange specification</h6>
````

<!--NOMAGIC_PAGE id=228985513 space=VR version=1 -->
## PAGE 00108: COR2013

- page_id: `228985513`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985513/COR2013
- version_number: 1
- version_date: `2018-04-03T14:27:48.904+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2013

**Message**

Operational Activity Action behavior is not defined or is incorrect.

**Description**

Operational Activity Action behavior property should be set to any of Operational Activities.

**Severity**

Error

**Context element**

Call Behavior Action

**Solvers**

- Select Behavior - select a behavior from your model.
- Create Behavior - create a behavior.

**Example**

[IMAGE alt='' src='']

###### Behavior of Operational Activity Action is specified using Select Behavior solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2013</p><p><strong>Message</strong></p><p>Operational Activity Action behavior is not defined or is incorrect.</p><p><strong>Description</strong></p><p>Operational Activity Action behavior property should be set to any of Operational Activities.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Call Behavior Action</p><p><strong>Solvers</strong></p><ul><li><strong>Select Behavior</strong> - select a behavior from your model.</li><li><strong>Create Behavior</strong> - create a behavior.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2013.png" /></ac:image></p><h6>Behavior of Operational Activity Action is specified using Select Behavior solver</h6>
````

<!--NOMAGIC_PAGE id=228985515 space=VR version=1 -->
## PAGE 00109: COR2014

- page_id: `228985515`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985515/COR2014
- version_number: 1
- version_date: `2018-04-04T11:43:44.142+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2014

**Message**

Operational Message connected lifelines represent incorrect Parts.

**Description**

Operational Message connects Lifelines that are of incompatible types.

**Severity**

Error

**Context element**

Lifeline

**Solvers**

- Convert to Operational Role - opens the Select Operational Performer dialog where you can select the required Operational Performer.

**Example**

[IMAGE alt='' src='']

###### Representation of Lifeline is changed using Convert To Operational Role solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2014</p><p><strong>Message</strong></p><p>Operational Message connected lifelines represent incorrect Parts.</p><p><strong>Description</strong></p><p>Operational Message connects Lifelines that are of incompatible types.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Lifeline</p><p><strong>Solvers</strong></p><ul><li><strong>Convert to Operational Role</strong> - opens the <strong>Select Operational Performer</strong> dialog where you can select the required Operational Performer.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2014.png" /></ac:image></p><h6>Representation of Lifeline is changed using Convert To Operational Role solver</h6>
````

<!--NOMAGIC_PAGE id=228985517 space=VR version=1 -->
## PAGE 00110: COR2015

- page_id: `228985517`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985517/COR2015
- version_number: 1
- version_date: `2018-04-04T13:16:20.832+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2015

**Message**

Directions of realizing relationship and realized Operational Exchange do not match.

**Description**

The direction of the realizing relationship and the realized Operational Exchange differs. The inconsistency should be fixed.

**Severity**

Warning

**Context element**

Activity Edge, Message

**Solvers**

- Remove Operational Exchange - the Operational Exchange is removed.

**Example**

[IMAGE alt='' src='']

###### Direction of realizing relationship is changed

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2015</p><p><strong>Message</strong></p><p>Directions of realizing relationship and realized Operational Exchange do not match.</p><p><strong>Description</strong></p><p>The direction of the realizing relationship and the realized Operational Exchange differs. The inconsistency should be fixed.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Activity Edge, Message</p><p><strong>Solvers</strong></p><ul><li><strong>Remove Operational Exchange</strong> - the Operational Exchange is removed.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2015.png" /></ac:image></p><h6>Direction of realizing relationship is changed</h6>
````

<!--NOMAGIC_PAGE id=228985519 space=VR version=1 -->
## PAGE 00111: COR2016

- page_id: `228985519`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985519/COR2016
- version_number: 1
- version_date: `2018-04-04T13:47:54.569+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2016

**Message**

Conveyed Operational Exchange Item and Object Nodes Types should be synchronized.

**Description**

The Supplier and Client of Object Nodes of the Activity Edge are not of Type of the Exchange Item conveyed by flow realized by the Activity edge. The inconsistency should be fixed.

**Severity**

Warning

**Context element**

Activity Edge

**Solvers**

- Change Object Node Types - the Object Node Type is changed.
- Change Conveyed Information Item - the Conveyed Information Item is changed.
- Remove Operational Exchange - the Operational Exchange is removed.

**Example**

[IMAGE alt='' src='']

###### Conveyed Operational Exchange Item is changed using Change Conveyed Information Item solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2016</p><p><strong>Message</strong></p><p>Conveyed Operational Exchange Item and Object Nodes Types should be synchronized.</p><p><strong>Description</strong></p><p>The Supplier and Client of Object Nodes of the Activity Edge are not of Type of the Exchange Item conveyed by flow realized by the Activity edge. The inconsistency should be fixed.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Change Object Node Types</strong> - the Object Node Type is changed.</li><li><strong>Change Conveyed Information Item</strong> - the Conveyed Information Item is changed.</li><li><strong>Remove Operational Exchange</strong> - the Operational Exchange is removed.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2016.png" /></ac:image></p><h6>Conveyed Operational Exchange Item is changed using Change Conveyed Information Item solver</h6>
````

<!--NOMAGIC_PAGE id=228985720 space=VR version=1 -->
## PAGE 00112: COR2017

- page_id: `228985720`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985720/COR2017
- version_number: 1
- version_date: `2020-04-08T06:25:35.570+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2017

**Message**

Directions of realizing relationship and realized Operational Exchange do not match.

**Description**

Relationship and Realized Operational Exchange does not have same direction.

**Severity**

Warning

**Context element**

Operational Association

**Solvers**

No automatic solvers for this validation rule. To solve this warning, you need to align directions.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2017</p><p><strong>Message</strong></p><p>Directions of realizing relationship and realized Operational Exchange do not match.</p><p><strong>Description</strong></p><p>Relationship and Realized Operational Exchange does not have same direction.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Operational Association</p><p><strong>Solvers</strong></p><p>No automatic solvers for this validation rule. To solve this warning, you need to align directions.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="2017.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985722 space=VR version=1 -->
## PAGE 00113: COR2019

- page_id: `228985722`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985722/COR2019
- version_number: 1
- version_date: `2024-04-09T14:40:02.301+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2019

**Message**

<viewpoint specific>* Ports typed by Conjugated Interface cannot be owned by Conjugated <viewpoint specific>* Ports and vice versa. Conflicts with at least '<port name>'.

**Description**

Two conjugation mechanisms are mixed.

**Severity**

Warning

**Context element**

Operational Port, Resource Port, Service Port

**Solver**

- There is no automatic solver for this validation rule. You can only select the conflicting port in the Containment tree and solve it manually.

**Example**

[IMAGE alt='' src='']

###### Operational Port type was changed into not conjugated interface

*******<viewpoint specific>** -Operational, Resource, Service.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2019</p><p><strong>Message</strong></p><p>&lt;viewpoint specific&gt;* Ports typed by Conjugated Interface cannot be owned by Conjugated &lt;viewpoint specific&gt;* Ports and vice versa. Conflicts with at least '&lt;port name&gt;'.</p><p><strong>Description</strong></p><p><span style="color: rgb(23,43,77);">Two conjugation mechanisms are mixed.</span></p><p><strong>Severity</strong></p><p><span style="color: rgb(23,43,77);">Warning</span></p><p><strong>Context element</strong></p><p><span style="color: rgb(23,43,77);">Operational Port, Resource Port, Service Port</span></p><p><strong><span style="color: rgb(23,43,77);">Solver</span></strong></p><ul><li><span style="color: rgb(23,43,77);">There is no automatic solver for this validation rule. You can only select the conflicting port in the Containment tree and solve it manually.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2019.png" /></ac:image></p><h6>Operational Port type was changed into not conjugated interface</h6><hr /><p><strong>*</strong><span style="color: rgb(23,43,77);"><strong>&lt;viewpoint specific&gt;</strong> - </span>Operational, Resource, Service.</p>
````

<!--NOMAGIC_PAGE id=228985521 space=VR version=1 -->
## PAGE 00114: COR2020

- page_id: `228985521`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985521/COR2020
- version_number: 1
- version_date: `2018-04-04T14:22:55.497+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2020

**Message**

Service Function Action behavior must be Service Function or its specializations.

**Description**

Service Function behavior property should be set to any of Service Function.

**Severity**

Error

**Context element**

Call Behavior Action

**Solvers**

- Select Behavior - select a behavior from the model.
- Create Behavior - create a behavior.

**Example**

[IMAGE alt='' src='']

###### Behavior of Service Function Action is specified using Select Behavior solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2020</p><p><strong>Message</strong></p><p>Service Function Action behavior must be Service Function or its specializations.</p><p><strong>Description</strong></p><p>Service Function behavior property should be set to any of Service Function.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Call Behavior Action</p><p><strong>Solvers</strong></p><ul><li><strong>Select Behavior</strong> - select a behavior from the model.</li><li><strong>Create Behavior</strong> - create a behavior.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2020.png" /></ac:image></p><h6>Behavior of Service Function Action is specified using Select Behavior solver</h6>
````

<!--NOMAGIC_PAGE id=228985523 space=VR version=4 -->
## PAGE 00115: COR2021

- page_id: `228985523`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985523/COR2021
- version_number: 4
- version_date: `2026-03-23T09:44:34.646+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

#### WARNING: Deprecated

Deprecated

This validation rule is deprecated stating with the 2026x version.

**Abbreviation**

COR2021

**Message**

Actual Enterprise Phase Start and End Date must fall within the enclosing Actual Enterprise Phase having this Actual Enterprise Phase set as a value for a slot.

**Description**

Incorrect Actual Enterprise Phase dates

**Severity**

Error

**Constrained Element**

Actual Enterprise Phase

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="51951212-3720-49b8-a5d7-36b07c932f56"><ac:parameter ac:name="title">Deprecated</ac:parameter><ac:rich-text-body><p>This validation rule is deprecated stating with the 2026x version.</p></ac:rich-text-body></ac:structured-macro><p><strong>Abbreviation</strong></p><p>COR2021</p><p><strong>Message</strong></p><p>Actual Enterprise Phase Start and End Date must fall within the enclosing Actual Enterprise Phase having this Actual Enterprise Phase set as a value for a slot.</p><p><strong>Description</strong></p><p>Incorrect Actual Enterprise Phase dates</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained Element</strong></p><p>Actual Enterprise Phase</p><p><strong>Solvers</strong></p><p><br /></p><p><strong>Example</strong></p>
````

<!--NOMAGIC_PAGE id=228985524 space=VR version=1 -->
## PAGE 00116: COR2022

- page_id: `228985524`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985524/COR2022
- version_number: 1
- version_date: `2018-04-05T11:38:13.731+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2022

**Message**

The client and supplier are not the same specialization of "Subject Of Forecast" (e.g. Software to Software, Resource Artifact to Resource Artifact, Capability Configuration to Capability Configuration) and etc.

**Description**

The client and supplier are not stereotyped by the same specialization of "Subject Of Forecast" (e.g. Software to Software, Resource Artifact to Resource Artifact, Capability Configuration to Capability Configuration, System to System, Systems Node to Systems Node, Post to Post, Organization to Organization, Standard to Standard, Capability to Capability, Competence to Competence).

**Severity**

Error

**Context element**

Dependency

**Solvers**

- Change To Forecast Element - opens the dialog to select the correct forecast element.
- Change From Technology Element - opens the dialog to select the correct technology element.
- Remove Forecast - removes the Forecast relationship.

Example

[IMAGE alt='' src='']

###### Natural Resource element is changed to Capability Configuration element using Change To Forecast Element solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2022</p><p><strong>Message</strong></p><p>The client and supplier are not the same specialization of &quot;Subject Of Forecast&quot; (e.g. Software to Software, Resource Artifact to Resource Artifact, Capability Configuration to Capability Configuration) and etc.</p><p><strong>Description</strong></p><p>The client and supplier are not stereotyped by the same specialization of &quot;Subject Of Forecast&quot; (e.g. Software to Software, Resource Artifact to Resource Artifact, Capability Configuration to Capability Configuration, System to System, Systems Node to Systems Node, Post to Post, Organization to Organization, Standard to Standard, Capability to Capability, Competence to Competence).</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Dependency</p><p><strong>Solvers</strong></p><ul><li><strong>Change To Forecast Element</strong> - opens the dialog to select the correct forecast element.</li><li><strong>Change From Technology Element</strong> - opens the dialog to select the correct technology element.</li><li><strong>Remove Forecast</strong> - removes the Forecast relationship.</li></ul><p>Example</p><p><ac:image><ri:attachment ri:filename="cor2022.png" /></ac:image></p><h6>Natural Resource element is changed to Capability Configuration element using Change To Forecast Element solver</h6>
````

<!--NOMAGIC_PAGE id=228985526 space=VR version=1 -->
## PAGE 00117: COR2023

- page_id: `228985526`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985526/COR2023
- version_number: 1
- version_date: `2019-06-05T12:59:15.666+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2023

**Message**

Function Action behavior must be Function or its specializations.

**Description**

Function Action behavior property should be set to any of Functions

**Severity**

Error

**Context element**

Call Behavior Action

**Solvers**

- Select Behavior - select a behavior from the model.
- Create Behavior - create a behavior.

**Example**

[IMAGE alt='' src='']

###### Behavior of Function Action is specified using Select Behavior solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2023</p><p><strong>Message</strong></p><p>Function Action behavior must be Function or its specializations.</p><p><strong>Description</strong></p><p>Function Action behavior property should be set to any of Functions</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Call Behavior Action</p><p><strong>Solvers</strong></p><ul><li><strong>Select Behavior</strong> - select a behavior from the model.</li><li><strong>Create Behavior</strong> - create a behavior.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2023.png" /></ac:image></p><h6>Behavior of Function Action is specified using Select Behavior solver</h6>
````

<!--NOMAGIC_PAGE id=228985528 space=VR version=1 -->
## PAGE 00118: COR2024

- page_id: `228985528`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985528/COR2024
- version_number: 1
- version_date: `2018-04-05T07:40:59.373+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2024

**Message**

Resource element is not implementing the Operational element.

**Description**

The couple associated with the Implementation relationship is not correct. The Supplier can be such as Node, Operational Exchange, Operational Activity, and Function. The Client can be such as System Resource, Resource Interaction, Function, and Service Function.

**Severity**

Error

**Context element**

Abstraction

**Solvers**

- Change Operational Element - opens the dialog to select the correct operational element.
- Change Systems Element - opens the dialog to select the correct system element.
- Remove Implements Operational Relationship - removes the Implements relationship.

**Example**

[IMAGE alt='' src='']

###### Operational Performer is changed to Operational Activity using Change Operational Element solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2024</p><p><strong>Message</strong></p><p>Resource element is not implementing the Operational element. </p><p><strong>Description</strong></p><p>The couple associated with the Implementation relationship is not correct. The Supplier can be such as Node, Operational Exchange, Operational Activity, and Function. The Client can be such as System Resource, Resource Interaction, Function, and Service Function.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Abstraction</p><p><strong>Solvers</strong></p><ul><li><strong>Change Operational Element</strong> - opens the dialog to select the correct operational element.</li><li><strong>Change Systems Element</strong> - opens the dialog to select the correct system element.</li><li><strong>Remove Implements Operational Relationship</strong> - removes the Implements relationship.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2024.png" /></ac:image></p><h6>Operational Performer is changed to Operational Activity using Change Operational Element solver</h6>
````

<!--NOMAGIC_PAGE id=228985530 space=VR version=1 -->
## PAGE 00119: COR2025

- page_id: `228985530`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985530/COR2025
- version_number: 1
- version_date: `2022-12-16T10:10:39.104+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2025

**Message**

The Information Source and Target of Resource Exchange should perform Functions that are behaviors of Function Actions connected by Function Edge.

**Description**

Function Actions are connected by Function Edge that realizes the Resource Exchange. The Source and Target of the Resource Exchange do not perform Functions that are behaviors of Function Actions. The inconsistency should be fixed.

**Severity**

Error

**Context element**

Activity Edge

**Solvers**

- Correct Realization - the realization is corrected.
- Remove Realization - the realization is removed.

**Example**

[IMAGE alt='' src='']

###### Realization is changed using Correct Realization solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2025</p><p><strong>Message</strong></p><p>The Information Source and Target of Resource Exchange should perform Functions that are behaviors of Function Actions connected by Function Edge.</p><p><strong>Description</strong></p><p>Function Actions are connected by Function Edge that realizes the Resource Exchange. The Source and Target of the Resource Exchange do not perform Functions that are behaviors of Function Actions. The inconsistency should be fixed.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Correct Realization</strong> - the realization is corrected.</li><li><strong>Remove Realization</strong> - the realization is removed.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2025.png" /></ac:image></p><h6>Realization is changed using Correct Realization solver</h6>
````

<!--NOMAGIC_PAGE id=228985532 space=VR version=1 -->
## PAGE 00120: COR2026

- page_id: `228985532`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985532/COR2026
- version_number: 1
- version_date: `2022-12-16T13:18:46.287+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2026

**Message**

Resource Connector end Role Owner should match the Information Source and Target of realized Resource Exchange.

**Description**

The Source and Target of the realized Resource Exchange do not match the Role Owners of the Resource Connector ends.

**Severity**

Error

**Context element**

Connector

**Solvers**

- Correct Realization - the realization is corrected.
- Remove Realization - the realization is removed.

**Example**

[IMAGE alt='' src='']

###### Incorrect Resource Connector is removed using Remove Realization solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2026</p><p><strong>Message</strong></p><p>Resource Connector end Role Owner should match the Information Source and Target of realized Resource Exchange.</p><p><strong>Description</strong></p><p>The Source and Target of the realized Resource Exchange do not match the Role Owners of the Resource Connector ends.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Connector</p><p><strong>Solvers</strong></p><ul><li><strong>Correct Realization</strong> - the realization is corrected.</li><li><strong>Remove Realization</strong> - the realization is removed.</li></ul><p><strong>Example</strong></p><p><br /></p><p><ac:image><ri:attachment ri:filename="cor2026.png" /></ac:image></p><h6>Incorrect Resource Connector is removed using Remove Realization solver</h6>
````

<!--NOMAGIC_PAGE id=228985534 space=VR version=1 -->
## PAGE 00121: COR2029

- page_id: `228985534`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985534/COR2029
- version_number: 1
- version_date: `2018-04-05T14:30:39.009+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2029

**Message**

Resource Role kind is incorrect according to its type and owner.

**Description**

The Role Kind of a Resource Role is incompatible with the type of Owner of the Resource Role.

**Severity**

Error

**Context element**

Resource Role

**Solvers**

- Sets Resource Role’s Kind Value To Other - other Resource Role kind value is set.
- Sets Resource Role’s Kind Value To - you can select Platform, Systems, or Component as a Resource Role kind value.

**Example**

[IMAGE alt='' src='']

###### Resource Role Kind changed using Sets Resource Role’s Kind Value To... solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2029</p><p><strong>Message</strong></p><p>Resource Role kind is incorrect according to its type and owner. </p><p><strong>Description</strong></p><p>The Role Kind of a Resource Role is incompatible with the type of Owner of the Resource Role.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Resource Role</p><p><strong>Solvers</strong></p><ul><li><strong>Sets Resource Role’s Kind Value To Other</strong> - other Resource Role kind value is set.</li><li><strong>Sets Resource Role’s Kind Value To</strong> - you can select Platform, Systems, or Component as a Resource Role kind value.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2029.png" /></ac:image></p><h6>Resource Role Kind changed using Sets Resource Role’s Kind Value To... solver</h6>
````

<!--NOMAGIC_PAGE id=228985536 space=VR version=1 -->
## PAGE 00122: COR2030

- page_id: `228985536`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985536/COR2030
- version_number: 1
- version_date: `2023-03-20T14:09:42.366+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2030

**Message**

Realized Resource Exchange should convey one and only one Resource Exchange Item.

**Description**

Function Edge connecting Pins or Activity Parameters can realize Information Flows that convey only one Exchange Item.

**Severity**

Warning

**Context element**

Activity Edge

**Solvers**

- Add / Remove Conveyed Item - add a conveyed item if it is missing or select which conveyed item should be removed.
- Remove Resource Exchange realization - all realized Resource Exchange Items are deselected in the Resource Exchange Manager.

**Example**

[IMAGE alt='' src='']

###### The reported Location conveyed item is removed from the Resource Exchange specification

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2030</p><p><strong>Message</strong></p><p>Realized Resource Exchange should convey one and only one Resource Exchange Item.</p><p><strong>Description</strong></p><p>Function Edge connecting Pins or Activity Parameters can realize Information Flows that convey only one Exchange Item.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Add / Remove Conveyed Item</strong> - <span style="color: rgb(62,63,64);">add a conveyed item if it is missing or select which conveyed item should be removed.</span></li><li><strong>Remove Resource Exchange realization</strong> - <span style="color: rgb(62,63,64);">all realized Resource Exchange Items are deselected in the Resource Exchange Manager.</span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2030.png" /></ac:image></p><h6>The reported Location conveyed item is removed from the Resource Exchange specification</h6>
````

<!--NOMAGIC_PAGE id=228985538 space=VR version=1 -->
## PAGE 00123: COR2031

- page_id: `228985538`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985538/COR2031
- version_number: 1
- version_date: `2022-12-16T13:19:13.819+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2031

**Message**

Conveyed Resource Exchange Item and Object Nodes Types should be synchronized.

**Description**

The Supplier and Client of Object Nodes of the Activity Edge are not of Type of the Exchange Item conveyed by flow realized by the Activity edge. The inconsistency should be fixed.

**Severity**

Warning

**Context element**

Activity Edge

**Solvers**

- Change Object Node Types - the Object Node type is changed.
- Change Conveyed Information Item - the Conveyed Information Item is changed.
- Delete selected Resource Exchange from model - the Resource Exchange is removed from the model.

**Example**

[IMAGE alt='' src='']

###### Conveyed Resource Exchange Item is changed using Change Conveyed Information Item solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2031</p><p><strong>Message</strong></p><p>Conveyed Resource Exchange Item and Object Nodes Types should be synchronized.</p><p><strong>Description</strong></p><p>The Supplier and Client of Object Nodes of the Activity Edge are not of Type of the Exchange Item conveyed by flow realized by the Activity edge. The inconsistency should be fixed.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Change Object Node Types</strong> - the Object Node type is changed.</li><li><strong>Change Conveyed Information Item</strong> - the Conveyed Information Item is changed.</li><li><strong>Delete selected Resource Exchange from model</strong> - the Resource Exchange is removed from the model.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2031.png" /></ac:image></p><h6>Conveyed Resource Exchange Item is changed using Change Conveyed Information Item solver</h6>
````

<!--NOMAGIC_PAGE id=228985540 space=VR version=1 -->
## PAGE 00124: COR2032

- page_id: `228985540`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985540/COR2032
- version_number: 1
- version_date: `2018-04-06T06:59:03.519+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2032

**Message**

Resource Message Connected Lifelines represent incorrect Parts.

**Description**

Resource Message connects Lifelines that are of incompatible types.

**Severity**

Error

**Context element**

Lifeline

**Solvers**

- Convert to Resource Role - the incorrect part is converted to the selected Resource Role.

**Example**

[IMAGE alt='' src='']

###### Representation of Lifeline is changed using Convert To Resource Role solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2032</p><p><strong>Message</strong></p><p>Resource Message Connected Lifelines represent incorrect Parts.</p><p><strong>Description</strong></p><p>Resource Message connects Lifelines that are of incompatible types.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Lifeline</p><p><strong>Solvers</strong></p><ul><li><strong>Convert to Resource Role</strong> - the incorrect part is converted to the selected Resource Role.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2032.png" /></ac:image></p><h6>Representation of Lifeline is changed using Convert To Resource Role solver</h6>
````

<!--NOMAGIC_PAGE id=228985724 space=VR version=1 -->
## PAGE 00125: COR2033

- page_id: `228985724`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985724/COR2033
- version_number: 1
- version_date: `2022-12-16T13:21:08.459+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2033

**Message**

Directions of realizing relationship and realized Resource Exchange do not match.

**Description**

The direction of the realizing relationship and the realized Resource Exchange differs.

**Severity**

Warning

**Context element**

Resource Association

**Solvers**

No automatic solvers for this validation rule. To solve this warning, you need to align directions.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2033</p><p><strong>Message</strong></p><p>Directions of realizing relationship and realized Resource Exchange do not match.</p><p><strong>Description</strong></p><p>The direction of the realizing relationship and the realized Resource Exchange differs.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Resource Association</p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">No automatic solvers for this validation rule. To solve this warning, you need to align directions.</span></p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="cor2033.png" /></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=228985726 space=VR version=1 -->
## PAGE 00126: COR2049

- page_id: `228985726`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985726/COR2049
- version_number: 1
- version_date: `2023-05-19T07:08:28.064+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2049

**Message**

Project Milestone owned attribute must be Project Theme, Property, Measurement or their specializations.

**Description**

The owned attribute of the Project Milestone can be Project Theme, Property, Measurement, or their specialization.

**Severity**

Error

**Context element**

Property

**Example**

**[IMAGE alt='' src='']**

###### The Capability Role was changed to Project Theme

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2049</p><p><strong>Message</strong></p><p>Project Milestone owned attribute must be Project Theme, Property, Measurement or their specializations.</p><p><strong>Description</strong></p><p style="text-align: left;">The owned attribute of the Project Milestone can be Project Theme, Property, Measurement, or their specialization.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Property</p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="cor2049.png" /></ac:image></strong></p><h6>The Capability Role was changed to Project Theme</h6>
````

<!--NOMAGIC_PAGE id=228985728 space=VR version=1 -->
## PAGE 00127: COR2051

- page_id: `228985728`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985728/COR2051
- version_number: 1
- version_date: `2023-03-16T13:28:04.280+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2051

**Description**

Project owned attribute must be Project Role or Project Milestone Role.

**Severity**

Error

**Context element**

Project

**Solvers**

An automatic solvers are not available, please solve it manually by changing the Project type to Project Role or Project Milestone Role.****

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2051</p><p><strong>Description</strong></p><p>Project owned attribute must be Project Role or Project Milestone Role.</p><p><strong>Severity</strong></p><p> Error</p><p><strong>Context element</strong></p><p>Project</p><p><strong>Solvers</strong></p><p>An automatic solvers are not available, please solve it manually by changing the Project type to Project Role or Project Milestone Role.<strong><br /></strong></p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="2051.png" /></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=228985730 space=VR version=1 -->
## PAGE 00128: COR2085

- page_id: `228985730`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985730/COR2085
- version_number: 1
- version_date: `2024-03-05T16:30:08.735+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2085

**Message**

Information Source for Operational Exchange must be Operational Agent or its specializations.

**Description**

Source value of Operational Exchange must be*Operational Agents*or its specializations.

**Severity**

Error

**Constrained element**

Operational Exchange

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong><span> </span></p><p>COR2085</p><p><strong>Message</strong></p><p>Information Source for Operational Exchange must be Operational Agent or its specializations.</p><p><strong>Description</strong></p><p>Source value of Operational Exchange must be<span> </span><em>Operational Agents</em><span> </span>or its specializations.</p><p><strong>Severity</strong><span> </span></p><p>Error</p><p><strong>Constrained element</strong></p><p>Operational Exchange</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2085.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985732 space=VR version=1 -->
## PAGE 00129: COR2087

- page_id: `228985732`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985732/COR2087
- version_number: 1
- version_date: `2024-03-05T14:13:10.720+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2087

**Message**

Information Target for Operational Exchange must be Operational Agent or its specializations.

**Description**

Target value of Operational Exchange must be*Operational Agents*or its specializations.

**Severity**

Error

**Constrained element**

Operational Exchange

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong><span> </span></p><p>COR2087</p><p><strong>Message</strong></p><p>Information Target for Operational Exchange must be Operational Agent or its specializations.</p><p><strong>Description</strong><span> </span></p><p>Target value of Operational Exchange must be<span> </span><em>Operational Agents</em><span> </span>or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained element</strong><span> </span></p><p>Operational Exchange</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2087.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985734 space=VR version=1 -->
## PAGE 00130: COR2103

- page_id: `228985734`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985734/COR2103
- version_number: 1
- version_date: `2025-01-10T15:12:49.295+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2103

**Message**

Conveyed Operational Exchange Item must be subtype of Operational Exchange Item.

**Description**

The type of conveyed property of Operational Exchange is incorrect.

**Severity**

Error

**Constrained element**

Operational Exchange

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2103</p><p><strong>Message</strong></p><p>Conveyed Operational Exchange Item must be subtype of Operational Exchange Item.</p><p><strong>Description</strong></p><p>The type of conveyed property of Operational Exchange is incorrect.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained element</strong></p><p>Operational Exchange</p><p><strong>Example</strong></p><p><strong> <ac:image><ri:attachment ri:filename="cor2103.png" /></ac:image></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985736 space=VR version=1 -->
## PAGE 00131: COR2108

- page_id: `228985736`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985736/COR2108
- version_number: 1
- version_date: `2023-03-16T13:26:47.305+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2108

**Description**

The owned Port of the Operational Performer must be the Operational Port.

**Severity**

error

**Context element**

Operational Port

**Solvers**

An automatic solvers are not available, please solve it manually**:**

- Delete Port: select the Port shape and press Delete .
- Change Port Type: right-click the Port shape and select: Refactor > Convert To > More Elements > Operational Port.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2108</p><p><strong>Description</strong></p><p>The owned Port of the Operational Performer must be the Operational Port.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Context element</strong></p><p><span style="color: rgb(255,0,0);"> </span>Operational Port</p><p><strong>Solvers</strong></p><p>An automatic solvers are not available, please solve it manually<strong>:</strong></p><ul><li>Delete Port: select the Port shape and press <strong>Delete</strong>.</li><li>Change Port Type: right-click the Port shape and select: <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Elements</strong> &gt; Operational Port.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="2108.png" /></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=228985738 space=VR version=1 -->
## PAGE 00132: COR2109

- page_id: `228985738`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985738/COR2109
- version_number: 1
- version_date: `2023-03-16T13:27:36.155+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2109

**Description**

Type of Service Port must be Service Interface or its specializations.

**Severity**

error

**Context element**

Service Port

**Solvers**

An automatic solvers are not available, please solve it manually by changing the Service Port type.****

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2109</p><p><strong>Description</strong></p><p>Type of Service Port must be Service Interface or its specializations.</p><p><strong>Severity</strong></p><p> error</p><p><strong>Context element</strong></p><p>Service Port</p><p><strong>Solvers</strong></p><p>An automatic solvers are not available, please solve it manually by changing the Service Port type.<strong><br /></strong></p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="2109.png" /></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=228985740 space=VR version=1 -->
## PAGE 00133: COR2126

- page_id: `228985740`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985740/COR2126
- version_number: 1
- version_date: `2024-04-09T13:35:25.373+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2126

**Message**

Broken synchronization between '<conjugated interface name>' Operational Interface and '<original interface name>' original interfaces.

**Description**

Incorrect synchronization between Conjugated Operational Interface and Original Interface.

**Severity**

Warning

**Constrained element**

- Operational Interface

**Solver**

- Synchronize Conjugated Operational Interface with Original Interface :
  - set the opposite Flow Property directions of the Conjugated Operational Interface.
  - delete any unmatched and/or duplicated Flow Properties in the Conjugated Operational Interface.
  - create a matching Flow Property for the Conjugated Operational Interface but in the opposite direction of the Original Interface.

**Example**

[IMAGE alt='' src='']

###### Using the solver, the missing flow property was added

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><strong>Abbreviation</strong></p><p style="text-align: left;">COR2126</p><p style="text-align: left;"><strong>Message</strong></p><p style="text-align: left;">Broken synchronization between '&lt;conjugated interface name&gt;' Operational Interface and '&lt;original interface name&gt;' original interfaces.</p><p style="text-align: left;"><strong>Description</strong></p><p style="text-align: left;">Incorrect synchronization between Conjugated Operational Interface and Original Interface.</p><p style="text-align: left;"><strong>Severity</strong></p><p style="text-align: left;">Warning</p><p style="text-align: left;"><strong>Constrained element</strong></p><ul><li style="text-align: left;">Operational Interface</li></ul><p style="text-align: left;"><strong>Solver</strong></p><ul style="text-align: left;"><li><strong>Synchronize Conjugated Operational Interface with Original Interface</strong>:<ul style="text-align: left;"><li>set the opposite Flow Property directions of the Conjugated Operational Interface.</li><li>delete any unmatched and/or duplicated Flow Properties in the Conjugated Operational Interface.</li><li>create a matching Flow Property for the Conjugated Operational Interface but in the opposite direction of the Original Interface. </li></ul></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2126.png" /></ac:image></p><h6>Using the solver, the missing flow property was added</h6>
````

<!--NOMAGIC_PAGE id=228985742 space=VR version=1 -->
## PAGE 00134: COR2127

- page_id: `228985742`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985742/COR2127
- version_number: 1
- version_date: `2024-04-09T13:36:14.043+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2127

**Message**

Broken synchronization between '<conjugated interface name>' Resource Interface and '<original interface name>' original interfaces.

**Description**

Incorrect synchronization between Conjugated Resource Interface and Original Interface

**Severity**

Warning

**Context element**

Resource Interface

**Solvers**

- Synchronize Conjugated Resource Interface with Original Interface:
  - set the opposite Flow Property directions of the Conjugated Resource Interface.
  - delete any unmatched and/or duplicated Flow Properties in the Conjugated Resource Interface.
  - create a matching Flow Property for the Conjugated Resource Interface but in the opposite direction of the Original Interface.

**Example**

[IMAGE alt='' src='']

###### Using the solver, the missing flow property was added

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2127</p><p><strong>Message</strong></p><p>Broken synchronization between '&lt;conjugated interface name&gt;' Resource Interface and '&lt;original interface name&gt;' original interfaces.</p><p><strong>Description</strong></p><p>Incorrect synchronization between Conjugated Resource Interface and Original Interface</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Resource Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Synchronize Conjugated Resource Interface with Original Interface:</strong><ul><li>set the opposite Flow Property directions of the Conjugated Resource Interface.</li><li>delete any unmatched and/or duplicated Flow Properties in the Conjugated Resource Interface.</li><li>create a matching Flow Property for the Conjugated Resource Interface but in the opposite direction of the Original Interface. </li></ul></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2127.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">Using the solver, the missing flow property was added</span></h6>
````

<!--NOMAGIC_PAGE id=228985744 space=VR version=1 -->
## PAGE 00135: COR2128

- page_id: `228985744`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985744/COR2128
- version_number: 1
- version_date: `2024-04-09T14:15:13.370+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2128

**Message**

Broken synchronization between '<conjugated interface name>' Service Interface and '<original interface name>' original interfaces.

**Description**

Incorrect synchronization between Conjugated Service Interface and Original Interface

**Severity**

Warning

**Context element**

Service Interface

**Solvers**

- Synchronize Conjugated Service Interface with Original Interface:
  - set the opposite Flow Property directions of the Conjugated Service Interface.
  - delete any unmatched and/or duplicated Flow Properties in the Conjugated Service Interface.
  - create a matching Flow Property for the Conjugated Service Interface but in the opposite direction of the Original Interface.

**Example**

[IMAGE alt='' src='']

###### Using the solver, the missing flow property was added

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2128</p><p><strong>Message</strong></p><p>Broken synchronization between '&lt;conjugated interface name&gt;' Service Interface and '&lt;original interface name&gt;' original interfaces.</p><p><strong>Description</strong></p><p>Incorrect synchronization between Conjugated Service Interface and Original Interface</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Service Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Synchronize Conjugated Service Interface with Original Interface:</strong><ul><li>set the opposite Flow Property directions of the Conjugated Service Interface.</li><li>delete any unmatched and/or duplicated Flow Properties in the Conjugated Service Interface.</li><li>create a matching Flow Property for the Conjugated Service Interface but in the opposite direction of the Original Interface. </li></ul></li></ul><p><strong>Example</strong></p><p style="text-align: left;"><ac:image><ri:attachment ri:filename="COR2128.png" /></ac:image></p><h6>Using the solver, the missing flow property was added</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985746 space=VR version=1 -->
## PAGE 00136: COR2140

- page_id: `228985746`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985746/COR2140
- version_number: 1
- version_date: `2025-01-10T15:12:04.069+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2140

**Message**

Client for the Exhibits must be Capable Element or its specializations

**Description**

The supplier must be Capable Element or its specializations.

**Severity**

Error

**Constrained element**

Exhibits

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2140</p><p><strong>Message</strong></p><p>Client for the Exhibits must be Capable Element or its specializations</p><p><strong>Description</strong></p><p>The supplier must be Capable Element or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained element</strong></p><p>Exhibits</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2140.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985748 space=VR version=1 -->
## PAGE 00137: COR2142

- page_id: `228985748`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985748/COR2142
- version_number: 1
- version_date: `2025-01-10T15:12:29.669+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2142

**Message**

Supplier for Desires must be Actual State or its specializations

**Description**

Supplier is incorrect for Desires. The supplier must be an Actual State or its specializations.

**Severity**

Error

**Constrained element**

Desires

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2142</p><p><strong>Message</strong></p><p>Supplier for Desires must be Actual State or its specializations</p><p><strong>Description</strong></p><p>Supplier is incorrect for Desires. The supplier must be an Actual State or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained element</strong></p><p>Desires</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2142.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985750 space=VR version=1 -->
## PAGE 00138: COR2143

- page_id: `228985750`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985750/COR2143
- version_number: 1
- version_date: `2025-01-10T15:12:15.951+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2143

**Message**

Supplier for the Exhibits must be Capability or its specializations.

**Description**

The supplier must be Capable Element.

**Severity**

Error

**Constrained element**

Exhibits

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2143</p><p><strong>Message</strong></p><p>Supplier for the Exhibits must be Capability or its specializations.</p><p><strong>Description</strong></p><p>The supplier must be Capable Element.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained element</strong></p><p>Exhibits</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2143.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985752 space=VR version=1 -->
## PAGE 00139: COR2162

- page_id: `228985752`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985752/COR2162
- version_number: 1
- version_date: `2023-03-16T13:29:04.535+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2162

**Description**

Type is incorrect for conveyed property of Resource Exchange

**Severity**

Error

**Context element**

Resource Exchange

**Solvers**

An automatic solvers are not available, please solve it manually by changing the conveyed property to Resource Exchange element.********

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2162</p><p><strong>Description</strong></p><p>Type is incorrect for conveyed property of Resource Exchange</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Resource Exchange</p><p><strong>Solvers</strong></p><p>An automatic solvers are not available, please solve it manually by changing the conveyed property to Resource Exchange element.<strong><strong><br /></strong></strong></p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COR2162.png" /></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=228985754 space=VR version=1 -->
## PAGE 00140: COR2178

- page_id: `228985754`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985754/COR2178
- version_number: 1
- version_date: `2024-04-05T14:39:10.010+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2178

**Message**

The Conjugated Operational Interface must have original interface.

**Description**

The original Operational Interface is not defined

**Severity**

Warning

**Context element**

Operational Interface

**Solvers**

- Select original Operational Interface - the Select Operational Interface dialog opens where you can choose the needed interface from the existing ones.

**Example**

[IMAGE alt='' src='']

###### An original Operational Interface was selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2178</p><p><strong>Message</strong></p><p>The Conjugated Operational Interface must have original interface.</p><p><strong>Description</strong></p><p>The original Operational Interface is not defined</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Operational Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Select original Operational Interface</strong> - the <strong>Select Operational Interface</strong> dialog opens where you can choose the needed interface from the existing ones.</li></ul><p><strong>Example</strong></p><p style="text-align: left;"><ac:image><ri:attachment ri:filename="COR2178.png" /></ac:image></p><h6 style="text-align: left;">An original Operational Interface was selected</h6>
````

<!--NOMAGIC_PAGE id=228985756 space=VR version=1 -->
## PAGE 00141: COR2179

- page_id: `228985756`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985756/COR2179
- version_number: 1
- version_date: `2024-04-05T14:44:48.851+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2179

**Message**

The Conjugated Service Interface must have original interface.

**Description**

Original Service Interface is not defined

**Severity**

Warning

**Context element**

Service Interface

**Solvers**

- Select original Service Interface - the Select Service Interface dialog opens where you can choose the needed interface from the existing ones.

**Example**

[IMAGE alt='' src='']

###### An original Service Interface was selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2179</p><p><strong>Message</strong></p><p>The Conjugated Service Interface must have original interface.</p><p><strong>Description</strong></p><p>Original Service Interface is not defined</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Service Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Select original Service Interface</strong> - the <strong>Select Service Interface</strong> dialog opens where you can choose the needed interface from the existing ones.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2179.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">An original Service Interface was selected</span></h6>
````

<!--NOMAGIC_PAGE id=228985758 space=VR version=1 -->
## PAGE 00142: COR2180

- page_id: `228985758`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985758/COR2180
- version_number: 1
- version_date: `2024-04-05T14:38:42.406+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2180

**Message**

The Conjugated Service Interface must have original interface.

**Description**

Original Service Interface is not defined

**Severity**

Warning

**Context element**

Service Interface

**Solvers**

- Select original Service Interface - the Select Resource Interface dialog opens where you can choose the needed interface from the existing ones.

**Example**

[IMAGE alt='' src='']

###### An original Resource Interface was selected

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2180</p><p><strong>Message</strong></p><p>The Conjugated Service Interface must have original interface.</p><p><strong>Description</strong></p><p>Original Service Interface is not defined</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Service Interface</p><p><strong>Solvers</strong></p><ul><li><strong>Select original Service Interface</strong> - the <strong>Select Resource Interface</strong> dialog opens where you can choose the needed interface from the existing ones.</li></ul><p><strong>Example</strong></p><p style="text-align: left;"><ac:image><ri:attachment ri:filename="COR2180.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">An original Resource Interface was selected</span></h6>
````

<!--NOMAGIC_PAGE id=228985760 space=VR version=1 -->
## PAGE 00143: COR2184

- page_id: `228985760`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985760/COR2184
- version_number: 1
- version_date: `2024-05-09T14:45:14.818+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2184

**Message**

Start and/or End dates of <Validated Actual State> must enclose dates of owned <Owned Actual State>

**Description**

An Actual State Start / End Dates do not correlate with the owned Actual Sates. If the validated element is*Actual Strategic Phase*, then <Owned Actual State> will be Actual Strategic Phase. If the validated element is*Actual Project*, then <Owned Actual State> will beActual Project.

**Severity**

Warning

**Constrained element**

Actual Project, Actual Strategic Phase

**Solvers**

- Update Start Date to Cover Owned <Owned Actual State> - if the Start Date is incorrect, choosing this solver will update the Start Date automatically to cover the dates of child elements.
- Update End Date to Cover Owned <Owned Actual State> - if the End Date is incorrect, choosing this solver will update the End Date automatically to cover the dates of child elements. If one or more child elements do not have the End Date, the End Date value will be removed for the validated parent element also.

**Update Start and End Dates to Cover Owned <Owned Actual State>** - the solvers above are merged into one solver if the parent Actual State does not cover both, start and end dates.

- Open Actual Project Assignment Wizard (in Project Roadmap) or Open Actual Strategic Phase Assignment Wizard (in Actual Strategic Phasing) - opens a wizard, where you can enter the needed dates manually.

**Example**

[IMAGE alt='' src='']

###### The **Update Start Date to Cover Owned <Owned Actual State>** solver was selected to automatically update the Start Date to the correct one.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2184</p><p><strong>Message</strong></p><p><span style="color: rgb(23,43,77);">Start and/or End dates of &lt;Validated Actual State&gt; must enclose dates of owned &lt;Owned Actual State&gt;</span></p><p><strong>Description</strong></p><p>An Actual State Start / End Dates do not correlate with the owned Actual Sates. <span style="letter-spacing: 0.0px;">If the validated element is </span><em style="letter-spacing: 0.0px;">Actual Strategic Phase</em><span style="letter-spacing: 0.0px;">, then &lt;Owned Actual State&gt; will be Actual Strategic <ac:inline-comment-marker ac:ref="47ba1303-a778-4f81-9e77-1f933f164ef7">Phase</ac:inline-comment-marker>. If the validated element is </span><em style="letter-spacing: 0.0px;">Actual Project</em><span style="letter-spacing: 0.0px;">, then <span>&lt;Owned Actual State&gt; will be </span>Actual Project.</span></p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Constrained element</strong></p><p>Actual Project, Actual Strategic Phase</p><p><strong>Solvers</strong></p><ul><li><strong>Update Start Date to Cover Owned &lt;Owned Actual State&gt;</strong> - if the Start Date is incorrect, choosing this solver will update the Start Date automatically to cover the dates of child elements. </li><li><strong>Update End Date to Cover Owned &lt;Owned Actual State&gt;</strong> - if the End Date is incorrect, choosing this solver will update the End Date automatically to cover the dates of child elements. If one or more child elements do not have the End Date, the End Date value will be removed for the validated parent element also.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4abbe50f-da8b-4ed6-aef6-64621cae1d76"><ac:rich-text-body><p><strong>Update Start and End Dates to Cover Owned &lt;Owned Actual State&gt;</strong> - the solvers above are merged into one solver if the parent Actual State does not cover both, start and end dates. </p></ac:rich-text-body></ac:structured-macro><ul><li><strong>Open Actual Project Assignment Wizard </strong>(in Project Roadmap) or <strong>Open Actual Strategic Phase Assignment Wizard</strong> (in Actual Strategic Phasing) - opens a wizard, where you can enter the needed dates manually.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2184.png" /></ac:image></p><h6>The <strong style="text-align: left;">Update Start Date to Cover Owned &lt;Owned Actual State&gt;</strong> solver was selected to automatically update the Start Date to the correct one.</h6>
````

<!--NOMAGIC_PAGE id=228985767 space=VR version=1 -->
## PAGE 00144: COR2185

- page_id: `228985767`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985767/COR2185
- version_number: 1
- version_date: `2024-05-02T10:47:14.981+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2185

**Message**

Measurement Sets are not synchronized between <Associated element> and its <Validated element>.

**Description**

Measurement Sets Are Not Synchronized between <Associated element> and its <Validated element>, where:

- <Associated element> can be the type of role, such as Operational Performer, the behavior of action, such as Operational Activity.
- <Validated element> can be Measurable Elements, such as Operational Role or Operational Action .

**Severity**

Warning

**Constrained element**

UAF Element

**Solvers**

- Select Correct Measurement Set to <Validated element> - If the Measurable Element's type is Property Set, choosing this solver the Measurement Set value is removed. If the Measurable Element's type is another Measurable Element, the Select Measurement Set dialog opens, where you can select one or more correct Measurement Sets for the validated element.
- Set Correct Measurement Set to <Associated element> - the Select Measurement Set dialog opens, where you can select one or more correct Measurement Sets for the associated element. If the Measurable Element's type is Property Set, this solver is not available.

**Example**

[IMAGE alt='' src='']

###### An example of the case when a Measurable Element's type is Property Set. The "**Select Correct Measurement Set to <Validated element>**" solver was used. The incorrect Measurement Set was removed.

[IMAGE alt='' src='']

###### An example of the case when a Measurable Element's type is another Measurable Element. The "**Set Correct Measurement Set to <Associated element>**" solver was used. The correct Measurement Sets were selected.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2185</p><p><strong>Message</strong></p><p>Measurement Sets are not synchronized between &lt;Associated element&gt; and its &lt;Validated element&gt;.</p><p><strong>Description</strong></p><p>Measurement Sets Are Not Synchronized between &lt;Associated element&gt; and its &lt;Validated element&gt;, where:</p><ul><li>&lt;Associated element&gt; can be the type of role, such as Operational Performer,<span> </span>the <ac:inline-comment-marker ac:ref="82eddc67-a0ad-41f1-a271-1da9accaf7b1">behavior</ac:inline-comment-marker> of action, such as Operational Activity.</li><li>&lt;Validated element&gt; can be Measurable Elements, such as <ac:inline-comment-marker ac:ref="cd4e6ae7-4a3e-4c86-be39-274a3c797c4d">Operational Role or Operational Action</ac:inline-comment-marker>.</li></ul><p><strong>Severity</strong></p><p>Warning</p><p><strong>Constrained element</strong></p><p>UAF Element</p><p><strong>Solvers</strong></p><ul style="text-align: left;"><li><strong><ac:inline-comment-marker ac:ref="9d787fea-e58f-40f2-94f9-0355c43a6b4d">Select Correct Measurement Set to &lt;Validated element&gt;</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="9d787fea-e58f-40f2-94f9-0355c43a6b4d"> - If the Measurable Element's type is Property Set, choosing this solver the Measurement Set value is removed. If the Measurable Element's type is another Measurable Element, the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="9d787fea-e58f-40f2-94f9-0355c43a6b4d">Select Measurement Set</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="9d787fea-e58f-40f2-94f9-0355c43a6b4d"> dialog opens, where you can select one or more correct Measurement Sets for the validated element.</ac:inline-comment-marker></li><li><strong><ac:inline-comment-marker ac:ref="74669cdd-f407-425d-97d4-af00a2113901">Set Correct Measurement Set to &lt;Associated element&gt;</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="74669cdd-f407-425d-97d4-af00a2113901"> - the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="74669cdd-f407-425d-97d4-af00a2113901">Select Measurement Set</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="74669cdd-f407-425d-97d4-af00a2113901"> dialog opens, where you can select one or more correct Measurement Sets for the associated element. If the Measurable Element's type is Property Set, this solver is not available.</ac:inline-comment-marker></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2185.png" /></ac:image></p><h6>An example of the case when a Measurable Element's type is Property Set. The &quot;<strong>Select Correct Measurement Set to &lt;Validated element&gt;</strong>&quot; solver was used. The incorrect Measurement Set was removed.</h6><p><br /></p><p><ac:image><ri:attachment ri:filename="COR2185_II.png" /></ac:image></p><h6>An example of the case when a Measurable Element's type is another Measurable Element. The &quot;<strong>Set Correct Measurement Set to &lt;Associated element&gt;</strong>&quot; solver was used. The correct Measurement Sets were selected.</h6>
````

<!--NOMAGIC_PAGE id=228985776 space=VR version=1 -->
## PAGE 00145: COR2187

- page_id: `228985776`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985776/COR2187
- version_number: 1
- version_date: `2024-03-07T12:08:13.817+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2187

**Message**

Operational Activity Performed by Operational Role and Operational Agent is not in compliance.

**Description**

Operational Role type and Operational Activity Performer shall be the same element.

**Severity**

warning

**Constrained element**

Operational Activity Action

**Solvers**

- Create Relationship between <Operational Agent name> and <Operational Activity name> - creates Is Capable To Perform Relationship between Operational Role type and Operational Activity.
- Change Behavior - the Select Element dialog opens where you can select the Operational Activity. Is Capable To Perform relationship is created between the Operational Agent and selected Operational Activity.
- Remove Operational Activity Action from Swimlane - removes the Operational Activity Action from the diagram and the model .

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong><span> </span></p><p>COR2187</p><p><strong>Message</strong><span> </span></p><p>Operational Activity Performed by Operational Role and Operational Agent is not in compliance.</p><p><strong>Description</strong><span> </span></p><p>Operational Role type and Operational Activity Performer shall be the same element.</p><p><strong>Severity</strong><span> </span></p><p>warning</p><p><strong>Constrained element</strong><span> </span></p><p>Operational Activity Action</p><p><strong>Solvers</strong></p><ul><li><strong>Create Relationship between &lt;Operational Agent name&gt; and &lt;Operational Activity name&gt;</strong> - creates Is Capable To Perform Relationship between Operational Role type and Operational Activity.</li><li><strong>Change Behavior</strong> - the <strong>Select Element</strong> dialog opens where you can select the Operational Activity. Is Capable To Perform relationship is created between the Operational Agent and selected Operational Activity.</li><li><strong>Remove Operational Activity Action from Swimlane</strong> - removes the Operational Activity Action from the diagram<span style="color: rgb(23,43,77);"> and the model</span>.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2187.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985778 space=VR version=1 -->
## PAGE 00146: COR2188

- page_id: `228985778`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985778/COR2188
- version_number: 1
- version_date: `2024-03-07T12:09:09.664+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2188

**Message**

Function Performed by Resource Role and Resource is not in compliance.

**Description**

Resource Role type and Function Performer shall be the same element.

**Severity**

warning

**Constrained element**

Function Action

**Solvers**

- Create Relationship between <Resource Performer name> and <Function name> - creates the Is Capable To Perform relationship between Resource Role type and Function.
- Change Behavior - the Select Element dialog opens where you can select the Function. Is Capable To Perform relationship is created between the Resource and selected Function.
- Remove Function Action from Swimlane - removes the Function Action from the diagram and the model .

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2188</p><p><strong>Message</strong><span> </span></p><p>Function Performed by Resource Role and Resource is not in compliance.</p><p><strong>Description</strong><span> </span></p><p>Resource Role type and Function Performer shall be the same element.</p><p><strong>Severity</strong><span> </span></p><p>warning</p><p><strong>Constrained element</strong></p><p>Function Action</p><p><strong>Solvers</strong></p><ul><li><strong>Create Relationship between &lt;Resource Performer name&gt; and &lt;Function name&gt;</strong> - creates the Is Capable To Perform relationship between Resource Role type and Function.</li><li><strong>Change Behavior </strong>- the <strong>Select Element</strong> dialog opens where you can select the Function. Is Capable To Perform relationship is created between the Resource and selected Function.</li><li><strong>Remove Function Action from Swimlane</strong> - removes the Function Action from the diagram <span style="color: rgb(23,43,77);">and the model</span>.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="COR2188.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=228985780 space=VR version=1 -->
## PAGE 00147: COR2189

- page_id: `228985780`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985780/COR2189
- version_number: 1
- version_date: `2024-03-07T12:08:24.665+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2189

**Message**

Operational Agent Is Not Performing Operational Activity.

**Description**

Operational Activity should be performed by Operational Agent or its specialization representing a swimlane.

**Severity**

warning

**Constrained element**

Operational Activity Action

**Solvers:**

- Create Relationship between <Operational Agent name> and <Operational Activity name> - creates the Is Capable To Perform relationship between Operational Agent and Operational Activity.
- Change Behavior - the Select Element dialog opens where you can select an Operational Activity. Is Capable To Perform relationship is created between the Operational Agent and selected Operational Activity.
- Remove Operational Activity Action from Swimlane - r emoves the Operational Activity Action from the diagram and the model.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong><span> </span></p><p>COR2189</p><p><strong>Message</strong><span> </span></p><p>Operational Agent Is Not Performing Operational Activity.</p><p><strong>Description</strong><span> </span></p><p>Operational Activity should be performed by Operational Agent or its specialization representing a swimlane.</p><p><strong>Severity</strong><span> </span></p><p>warning</p><p><strong>Constrained element</strong></p><p>Operational Activity Action</p><p><strong>Solvers:</strong></p><ul><li><strong>Create Relationship between &lt;Operational Agent name&gt; and &lt;Operational Activity name&gt;</strong> - creates the Is Capable To Perform relationship between Operational Agent and Operational Activity.</li><li><strong>Change Behavior</strong> - the <strong>Select Element</strong> dialog opens where you can select an Operational Activity. Is Capable To Perform relationship is created between the Operational Agent and selected Operational Activity.</li><li><strong>Remove Operational Activity Action from Swimlane</strong> - r<span style="color: rgb(23,43,77);">emoves the Operational Activity Action from the diagram and the model.</span></li></ul><p><strong><span style="color: rgb(23,43,77);">Example</span></strong></p><p><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="COR2189.png" /></ac:image></span></p>
````

<!--NOMAGIC_PAGE id=228985782 space=VR version=1 -->
## PAGE 00148: COR2190

- page_id: `228985782`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985782/COR2190
- version_number: 1
- version_date: `2024-03-07T12:08:02.094+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2190

**Message**

Resource Is Not Performing Function

**Description**

Function should be performed by Resource or its specialization representing a swimlane.

**Severity**

warning

**Constrained element**

Function Action

**Solvers**

- Create Relationship between <Resource> and <Function> - creates the Is Capable To Perform relationship between Resource and Function.
- Change Behavior - the Select Element dialog opens where you can select a Function. Is Capable To Perform relationship is created between the Resource and selected Function.
- Remove Function Action from Swimlane - r emoves the Function Action from the diagram and the model.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong><span> </span></p><p>COR2190</p><p><strong>Message</strong><span> </span></p><p>Resource Is Not Performing Function</p><p><strong>Description</strong><span> </span></p><p>Function should be performed by Resource or its specialization representing a swimlane.</p><p><strong>Severity</strong><span> </span></p><p>warning</p><p><strong>Constrained element</strong></p><p>Function Action</p><p><strong>Solvers</strong></p><ul><li><strong>Create Relationship between &lt;Resource&gt; and &lt;Function&gt;</strong> - creates the Is Capable To Perform relationship between Resource and Function.</li><li><strong>Change Behavior </strong>- the <strong>Select Element</strong> dialog opens where you can select a Function. Is Capable To Perform relationship is created between the Resource and selected Function.</li><li><strong>Remove Function Action from Swimlane</strong> - <span style="color: rgb(23,43,77);">r</span><span style="color: rgb(23,43,77);">emoves the Function Action from the diagram and the model.</span></li></ul><p><strong><span style="color: rgb(23,43,77);">Example</span></strong></p><p><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="COR2190.png" /></ac:image></span></p>
````

<!--NOMAGIC_PAGE id=228985784 space=VR version=1 -->
## PAGE 00149: COR2196

- page_id: `228985784`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985784/COR2196
- version_number: 1
- version_date: `2024-05-16T12:40:59.550+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2196

**Message**

Start date of the Actual Project Milestone precedes date of its referenced Actual Project Milestones.

**Description**

The Actual Project Milestone Date is incorrect. The rule checks if the Actual Project Milestone Start Date does not precede the Start Dates of its referenced Actual Project Milestones connected using the Milestone Dependency relationships and belong to the child Actual Projects, that are owned by the same owner as the validated Actual Project Milestone.

**Severity**

Warning

**Constrained element**

Actual Project Milestone

**Solvers**

- Update Start Date Based on Referenced Actual Project Milestones - choosing this solver updatesthe validated Actual Project Milestone Start Date to the latest date found down the Milestone Dependency chain.

**Example**

[IMAGE alt='' src='']

###### The solver updated the Start Date of *Phase 1 Available* Actual Project Milestone to match the Start Date of *Phase 2 OOS* Actual Project Milestone.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2196</p><p><strong>Message</strong></p><p>Start date of the Actual Project Milestone precedes date of its referenced Actual Project Milestones.</p><p><strong>Description</strong></p><p>The Actual Project Milestone Date is incorrect. The rule <span style="color: rgb(23,43,77);">checks if the Actual Project Milestone Start Date does not precede the <span style="color: rgb(23,43,77);">Start Dates of</span> its referenced Actual Project Milestones connected using the Milestone Dependency relationships and belong to the child Actual Projects, that are owned by the same owner as the validated Actual Project Milestone. </span></p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Constrained element</strong></p><p>Actual Project Milestone</p><p><strong>Solvers</strong></p><ul style="text-align: left;"><li><strong><span style="color: rgb(23,43,77);">Update Start Date Based on Referenced Actual Project Milestones</span></strong><span style="color: rgb(23,43,77);"> - choosing this solver updates<span style="color: rgb(23,43,77);"> the validated Actual Project Milestone Start Date to the latest date found down the Milestone Dependency chain.</span></span></li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2196.png" /></ac:image></p><h6>The solver updated the Start Date of <em>Phase 1 Available</em> Actual Project Milestone to match the Start Date of <em>Phase 2 OOS</em> Actual Project Milestone. </h6>
````

<!--NOMAGIC_PAGE id=228985787 space=VR version=1 -->
## PAGE 00150: COR2212

- page_id: `228985787`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985787/COR2212
- version_number: 1
- version_date: `2023-03-16T13:33:07.901+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2212

**Description**

Security Control Action behavior is not defined or is incorrect. The Security Control Action behavior property should be set to any of Security Controls.

**Severity**

error

**Context element**

Security Control Action

**Solvers**

- Select Behavior - select a behavior from your model.
- Create Behavior - create a behavior.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2212</p><p><strong>Description</strong></p><p>Security Control Action behavior is not defined or is incorrect. The Security Control Action behavior property should be set to any of Security Controls.</p><p><strong>Severity</strong></p><p> error</p><p><strong>Context element</strong></p><p>Security Control Action</p><p><strong>Solvers</strong></p><ul><li><strong>Select Behavior</strong> - select a behavior from your model.</li><li><strong>Create Behavior</strong> - create a behavior.</li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COR2212.png" /></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=228985789 space=VR version=1 -->
## PAGE 00151: COR2255

- page_id: `228985789`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985789/COR2255
- version_number: 1
- version_date: `2023-09-15T11:43:41.394+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2255

**Message**

Class property value of the Service Port must be Service or Service Interface or their specializations.

**Description**

The type is incorrect for the Service Port class property. The Class property value should be Service or Service Interface or their specializations.

**Severity**

Error

**Context element**

Service Port

**Example**

[IMAGE alt='' src='']

###### The incorrect Class property value Operational Interface was changed to Service Interface.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2255</p><p><strong>Message</strong></p><p>Class property value of the Service Port must be Service or Service Interface or their specializations.</p><p><strong>Description</strong></p><p>The type is incorrect for the Service Port class property. The Class property value should be Service or Service Interface or their specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Service Port</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2255.png" /></ac:image></p><h6>The incorrect Class property value Operational Interface was changed to Service Interface.</h6>
````

<!--NOMAGIC_PAGE id=228985791 space=VR version=1 -->
## PAGE 00152: COR2256

- page_id: `228985791`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985791/COR2256
- version_number: 1
- version_date: `2023-09-15T11:55:58.955+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2256

**Message**

Class property value of the Resource Port must be Resource Performer or Resource Interface or their specializations.

**Description**

The type is incorrect for the Resource Port class property. The class property type should be Resource Performer or Resource Interface or their specializations.

**Severity**

Error

**Context element**

Resource Port

**Example**

[IMAGE alt='' src='']

###### The incorrect Class property Operational Interface was changed to Resource Interface.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2256</p><p><strong>Message</strong></p><p>Class property value of the Resource Port must be Resource Performer or Resource Interface or their specializations.</p><p><strong>Description</strong></p><p>The type is incorrect for the Resource Port class property. The class property type should be Resource Performer or Resource Interface or their specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Resource Port</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2256.png" /></ac:image></p><h6>The incorrect Class property Operational Interface was changed to Resource Interface.</h6>
````

<!--NOMAGIC_PAGE id=228985793 space=VR version=1 -->
## PAGE 00153: COR2310

- page_id: `228985793`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985793/COR2310
- version_number: 1
- version_date: `2023-05-19T07:07:36.482+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2310

**Message**

Defining feature of the Project Status must be Project Theme or its specializations.

**Description**

The defining feature of Project Status must be Project Theme.

**Severity**

Error

**Context element**

Actual Project Milestone

**Example**

**[IMAGE alt='' src='']**

###### The defining feature was changed from property to Project Theme.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2310</p><p><strong>Message</strong></p><p>Defining feature of the Project Status must be Project Theme or its specializations.</p><p><strong>Description</strong></p><p><span style="color: rgb(23,43,77);">The defining feature of Project Status must be Project Theme.</span></p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Actual Project Milestone</p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="cor2310.png" /></ac:image></strong></p><h6>The defining feature was changed from property to Project Theme.</h6>
````

<!--NOMAGIC_PAGE id=228985542 space=VR version=1 -->
## PAGE 00154: COR2322

- page_id: `228985542`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985542/COR2322
- version_number: 1
- version_date: `2023-03-20T14:09:14.706+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2322

**Message**

Realized Service Exchange should convey one and only one Service Exchange Item.

**Description**

Service Function Edge connecting Pins or Activity Parameters can realize Information Flows that convey only one Service Exchange Item.

**Severity**

Warning

**Context element**

Activity Edge

**Solvers**

- Add / Remove Conveyed Item - add a conveyed item if it is missing or select which conveyed item should be removed.
- Remove Service Exchange Realization - all realized Service Exchange Items are deselected in the Service Exchange Manager.

**Example**

[IMAGE alt='' src='']

###### The message conveyed item is removed from the Service Exchange specification.

Another example illustrates the case when the Service Exchange Item is missing.

[IMAGE alt='' src='']

###### Adding the missing Conveyed Item using the solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2322</p><p><strong>Message</strong></p><p>Realized Service Exchange should convey one and only one Service Exchange Item.</p><p><strong>Description</strong></p><p>Service Function Edge connecting Pins or Activity Parameters can realize Information Flows that convey only one Service Exchange Item.</p><p><strong>Severity</strong></p><p>Warning</p><p><strong>Context element</strong></p><p>Activity Edge</p><p><strong>Solvers</strong></p><ul><li><strong>Add / Remove Conveyed Item</strong> - add a conveyed item if it is missing or select which conveyed item should be removed.</li><li><strong>Remove Service Exchange Realization</strong> - all realized Service Exchange Items are deselected in the Service Exchange Manager.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2322.png" /></ac:image></p><h6>The message conveyed item is removed from the Service Exchange specification.</h6><p>Another example illustrates the case when the Service Exchange Item is missing.</p><p><ac:image><ri:attachment ri:filename="cor2322_add.png" /></ac:image></p><h6>Adding the missing Conveyed Item using the solver.</h6>
````

<!--NOMAGIC_PAGE id=228985545 space=VR version=1 -->
## PAGE 00155: COR2325

- page_id: `228985545`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985545/COR2325
- version_number: 1
- version_date: `2024-06-21T14:05:56.282+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2325

**Message**

Operational Connector end Role Owners should match Information Source and Target of realized Operational Exchange.

**Description**

The Source and Target of the realized Operational Exchange do not match Role Owners of the Operational Connector.

**Severity**

Error

**Context element**

Connector

**Solvers**

- Correct Realization - the incorrect needline is removed.
- Remove Realization - the realization is removed. The excess realization is identified according to the Realizing Connector property of the Operational Exchange.

**Sample**

[IMAGE alt='' src='']

###### Conveyed Service Exchange Item is changed using Change Conveyed Information Item solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2325</p><p><strong>Message</strong></p><p>Operational Connector end Role Owners should match Information Source and Target of realized Operational Exchange.</p><p><strong>Description</strong></p><p>The Source and Target of the realized Operational Exchange do not match Role Owners of the Operational Connector.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Connector</p><p><strong>Solvers</strong></p><ul><li><strong>Correct Realization</strong><span> </span>- the incorrect needline is removed.</li><li><strong>Remove Realization</strong><span> </span>- the realization is removed. The excess realization is identified according to the Realizing Connector property of the Operational Exchange.</li></ul><p><strong>Sample</strong></p><p><ac:image><ri:attachment ri:filename="COR2325.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">Conveyed Service Exchange Item is changed using Change Conveyed Information Item solver</span></h6>
````

<!--NOMAGIC_PAGE id=228985547 space=VR version=1 -->
## PAGE 00156: COR2330

- page_id: `228985547`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985547/COR2330
- version_number: 1
- version_date: `2024-06-21T12:10:33.445+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2330

**Message**

Conveyed Service Exchange Item and Service Nodes Types should be synchronized

**Description**

The Supplier and Client of Object Nodes of the Activity Edge are not of Type of the Exchange Item conveyed by flow realized by the Activity edge. The inconsistency should be fixed.

**Severity**

Error

**Constrained Element**

Service Object Flow

**Solvers**

- Change Object Node Types - the Object Node type is changed.
- Change Conveyed Information Item - the Conveyed Information Item is changed.
- Remove Service Exchange realization - the Service Exchange is removed from the model.

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2330</p><p><strong>Message</strong></p><p>Conveyed Service Exchange Item and Service Nodes Types should be synchronized</p><p><strong>Description</strong></p><p><span style="color: rgb(23,43,77);">The Supplier and Client of Object Nodes of the Activity Edge are not of Type of the Exchange Item conveyed by flow realized by the Activity edge. The inconsistency should be fixed.</span></p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained Element</strong></p><p>Service Object Flow</p><p><strong>Solvers</strong></p><ul><li><strong>Change Object Node Types</strong> - <span style="color: rgb(23,43,77);">the Object Node type is changed.</span></li><li><strong>Change Conveyed Information Item</strong> - <span style="color: rgb(23,43,77);">the Conveyed Information Item is changed.</span></li><li><strong>Remove Service Exchange realization</strong> - <span style="color: rgb(23,43,77);">the Service Exchange is removed from the model.</span></li></ul><p><strong>Example</strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985795 space=VR version=1 -->
## PAGE 00157: COR2332

- page_id: `228985795`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985795/COR2332
- version_number: 1
- version_date: `2023-10-13T13:36:20.422+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2332

**Message**

Realizing Activity Edge of Service Exchange must be Service Activity Edge or its specializations.

**Description**

The type for realizing the Activity Edge property of Service Exchange is incorrect. The type must be Service Activity Edge or its specializations.

**Severity**

Error

**Constrained Element**

Service Exchange

**Sample**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2332</p><p><strong>Message</strong></p><p>Realizing Activity Edge of Service Exchange must be Service Activity Edge or its specializations.</p><p><strong>Description</strong></p><p>The type for realizing the Activity Edge property of Service Exchange is incorrect. The type must be Service Activity Edge or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained Element</strong></p><p>Service Exchange</p><p><strong>Sample</strong></p>
````

<!--NOMAGIC_PAGE id=228985796 space=VR version=1 -->
## PAGE 00158: COR2335

- page_id: `228985796`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985796/COR2335
- version_number: 1
- version_date: `2023-05-19T07:05:49.598+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2335

**Message**

Supplier for the Implements should be Actual Strategic Phase if Client is Architecture or its specializations.

**Description**

When the client is Operational Architecture, Resource Architecture, or Service Architecture, the supplier must be Actual Enterprise Phase, Actual Enduring Task, Value Stream, Whole Life Enterprise, or Enterprise Mission.

**Severity**

Error

**Context element**

Implements

**Example**

[IMAGE alt='' src='']

###### Actual Organization was changed to Actual Enduring Task to resolve the validation

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2335</p><p><strong>Message</strong></p><p>Supplier for the Implements should be Actual Strategic Phase if Client is Architecture or its specializations.</p><p><strong>Description</strong></p><p>When the client is Operational Architecture, Resource Architecture, or Service Architecture, the supplier must be Actual Enterprise Phase, Actual Enduring Task, Value Stream, Whole Life Enterprise, or Enterprise Mission.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Implements</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2335.png" /></ac:image></p><h6>Actual Organization was changed to Actual Enduring Task to resolve the validation</h6>
````

<!--NOMAGIC_PAGE id=228985798 space=VR version=1 -->
## PAGE 00159: COR2343

- page_id: `228985798`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985798/COR2343
- version_number: 1
- version_date: `2023-05-19T07:06:33.132+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2343

**Message**

Client for the Implements should be Service Interface if Supplier is Operational Interface or its specializations.

**Description**

The couple associated with the Implementation relationship is not correct. The Client must be Service Interface when the Supplier is Operational Interface or its specializations.

**Severity**

Error

**Context element**

Implements

**Example**

[IMAGE alt='' src='']

###### Resource Artifact was changed to Service Interface to resolve this validation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2343</p><p><strong>Message</strong></p><p>Client for the Implements should be Service Interface if Supplier is Operational Interface or its specializations.</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">The couple associated with the Implementation relationship is not correct. The Client must be Service Interface when the Supplier is Operational Interface or its specializations.</span></p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Implements</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2343.png" /></ac:image></p><h6>Resource Artifact was changed to Service Interface to resolve this validation.</h6>
````

<!--NOMAGIC_PAGE id=228985800 space=VR version=1 -->
## PAGE 00160: COR2344

- page_id: `228985800`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985800/COR2344
- version_number: 1
- version_date: `2023-05-19T07:06:16.124+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2344

**Message**

Supplier for the Implements should be Operational Interface if Client is Service Interface or its specializations.

**Description**

The couple associated with the Implementation relationship is not correct. The Supplier must be an Operational Interface when the Supplier is Service Interface or its specializations.

**Severity**

Error

**Context element**

Implements

**Example**

[IMAGE alt='' src='']

###### Resource Interface was changed to Operational Interface to resolve this validation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p><strong>Abbreviation</strong></p><p>COR2344</p><p><strong>Message</strong></p><p>Supplier for the Implements should be Operational Interface if Client is Service Interface or its specializations.</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">The couple associated with the Implementation relationship is not correct. The Supplier must be an Operational Interface when the Supplier is Service Interface or its specializations.</span></p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Implements</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2344.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">Resource Interface was changed to Operational Interface to resolve this validation.</span></h6>
````

<!--NOMAGIC_PAGE id=228985548 space=VR version=1 -->
## PAGE 00161: COR2345

- page_id: `228985548`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985548/COR2345
- version_number: 1
- version_date: `2023-05-17T12:11:21.212+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2345

**Message**

Service Message connected Lifelines represent incorrect Parts.

**Description**

Service Message connects Lifelines that are of incompatible types.

**Severity**

Error

**Context element**

Lifeline

**Solver**

**Convert to Service Role** - opens the**Select Service**dialog where you can select the required Service Role.

**Example**

[IMAGE alt='' src='']

###### Representation of Lifeline is changed using Convert To Service Role solver

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2345</p><p><strong>Message</strong></p><p><span style="color: rgb(23,43,77);">Service Message connected Lifelines represent incorrect Parts.</span></p><p><strong>Description</strong></p><p style="text-align: left;"><span style="color: rgb(62,63,64);">Service Message connects Lifelines that are of incompatible types.</span></p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Lifeline</p><p><strong>Solver</strong></p><p><strong style="text-align: left;">Convert to Service Role</strong> - <span style="color: rgb(62,63,64);">opens the<span> </span></span><strong style="text-align: left;">Select Service </strong><span style="color: rgb(62,63,64);">dialog where you can select the required Service Role.</span></p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2345.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">Representation of Lifeline is changed using Convert To Service Role solver</span></h6>
````

<!--NOMAGIC_PAGE id=228985550 space=VR version=1 -->
## PAGE 00162: COR2346

- page_id: `228985550`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985550/COR2346
- version_number: 1
- version_date: `2023-02-13T13:57:09.199+01:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2346

**Message**

Project Sequence type/kind is not valid for Project Sequence.

**Description**

The Project Sequence relationship connects Actual Projects, one or both of which have no end date.

**Severity**

Error

**Context element**

Project Sequence

**Solvers**

- **Change Project Sequence type to "Start-to-Start"** - none of the Actual Projects or only the source Actual Project has end dates.
- **Change Project Sequence type to "Start-to-Finish"**- the source Actual Project has no ends date, but the target Actual Project has.
- **Change Project Sequence type to "Finish-to-Start"** - the source Actual Project has an end date, but the target Actual Project does not have an end date.
- **Remove Project Sequence from Model**- the Project Sequence is deleted from the model.

**Example**

**[IMAGE alt='' src='']**

###### The Project Sequence type was changed to Start-to-Start

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2346</p><p><strong>Message</strong></p><p><span style="color: rgb(23,43,77);">Project Sequence type/kind is not valid for Project Sequence.</span></p><p><strong>Description</strong></p><p><span style="color: rgb(23,43,77);">The Project Sequence relationship connects Actual Projects, one or both of which have no end date.</span></p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Project Sequence</p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Change Project Sequence type to &quot;Start-to-Start&quot;</strong> - none of the Actual Projects or only the source Actual Project has end dates.</span></li><li><span style="color: rgb(23,43,77);"><strong>Change Project Sequence type to &quot;Start-to-Finish&quot;</strong><span> - the source Actual Project has no ends date, but the target Actual Project has.</span></span></li><li><span style="color: rgb(23,43,77);"><strong>Change Project Sequence type to &quot;Finish-to-Start&quot;</strong> - the source Actual Project has an end date, but the target Actual Project does not have an end date.</span></li><li><span style="color: rgb(23,43,77);"><strong>Remove Project Sequence from Model </strong>- the Project Sequence is deleted from the model.</span></li></ul><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="COR2346.png" /></ac:image></strong></p><h6>The Project Sequence type was changed to Start-to-Start</h6>
````

<!--NOMAGIC_PAGE id=228985552 space=VR version=1 -->
## PAGE 00163: COR2347

- page_id: `228985552`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985552/COR2347
- version_number: 1
- version_date: `2023-09-15T09:06:28.923+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2347

**Message**

The client and supplier connected with the Impacted By relationship are paired incorrectly.

**Description**

Incorrect Impacted By coupling. Either the client or the supplier of the Impacted By relationship is incorrect.

**Severity**

Error

**Context element**

Impacted By

**Solvers**

- Change Impacted By Supplier Element - the Select <element> dialog opens. Choose the appropriate element.
- Change Impacted By Client Element - the Select <element> dialog opens. Choose the needed the appropriate element.
- Remove Impacted By Relationship - the relationship is removed.

**Example**

[IMAGE alt='' src='']

###### An example of an incorrect coupling where the supplier for the client Opportunity is incorrect.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2347</p><p><strong>Message</strong></p><p>The client and supplier connected with the Impacted By relationship are paired incorrectly.</p><p><strong>Description</strong></p><p>Incorrect Impacted By coupling. Either the client or the supplier of the Impacted By relationship is incorrect.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Solvers</strong></p><ul><li><strong>Change Impacted By Supplier Element</strong><span> </span>- the<span> </span><strong>Select &lt;element&gt;</strong><span> </span>dialog opens. Choose the appropriate element.</li><li><strong>Change Impacted By Client Element</strong><span> </span>- the<span> </span><strong>Select &lt;element&gt;</strong><span> </span>dialog opens. Choose the needed the appropriate element.</li><li><strong>Remove Impacted By Relationship</strong><span> </span>- the relationship is removed.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2347.png" /></ac:image></p><h6>An example of an incorrect coupling where the supplier for the client Opportunity is incorrect.</h6>
````

<!--NOMAGIC_PAGE id=228985802 space=VR version=1 -->
## PAGE 00164: COR2348

- page_id: `228985802`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985802/COR2348
- version_number: 1
- version_date: `2023-09-15T09:30:32.535+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2348

**Message**

Supplier for the Impacted By should be Opportunity or its specializations

**Description**

Supplier is incorrect for Impacted By client Capability. The supplier for the Capability should be Opportunity or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### The incorrect supplier Challenge was replaced with the correct supplier Opportunity.

###### .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2348</p><p><strong>Message</strong></p><p>Supplier for the Impacted By should be Opportunity or its specializations</p><p><strong>Description</strong></p><p>Supplier is incorrect for Impacted By client Capability. The supplier for the  Capability should be Opportunity or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2348.png" /></ac:image></p><h6>The incorrect supplier Challenge was replaced with the correct supplier Opportunity.</h6><h6>.</h6>
````

<!--NOMAGIC_PAGE id=228985804 space=VR version=1 -->
## PAGE 00165: COR2349

- page_id: `228985804`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985804/COR2349
- version_number: 1
- version_date: `2023-09-15T09:20:02.911+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2349

**Message**

Supplier for the Impacted By should be Enterprise Goal or its specializations.

**Description**

The supplier is incorrect for the Impacted By client Actual Outcome. The supplier for the Actual Outcome should be Enterprise Goal or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### The incorrect supplier Opportunity was replaced with the correct supplier Enterprise Goal.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2349</p><p><strong>Message</strong></p><p>Supplier for the Impacted By should be Enterprise Goal or its specializations.</p><p><strong>Description</strong></p><p>The supplier is incorrect for the Impacted By client Actual Outcome. The supplier for the  Actual Outcome should be Enterprise Goal or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image ac:height="177"><ri:attachment ri:filename="cor2347.png" /></ac:image></p><h6>The incorrect supplier Opportunity was replaced with the correct supplier Enterprise Goal.</h6>
````

<!--NOMAGIC_PAGE id=228985806 space=VR version=1 -->
## PAGE 00166: COR2350

- page_id: `228985806`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985806/COR2350
- version_number: 1
- version_date: `2023-09-15T10:09:15.034+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2350

**Message**

Supplier for the Impacted By should be Challenge or its specializations.

**Description**

The supplier is incorrect for Impacted By client Architecture. The supplier for the Architecture should be Challenge or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### An example where the incorrect supplier Opportunity for the client Operational Architecture was replaced with the correct supplier Challenge.

###### .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2350</p><p><strong>Message</strong></p><p>Supplier for the Impacted By should be Challenge or its specializations.</p><p><strong>Description</strong></p><p>The supplier is incorrect for Impacted By client Architecture. The supplier for the Architecture should be Challenge or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2350.png" /></ac:image></p><h6>An example where the incorrect supplier Opportunity for the client Operational Architecture was replaced with the correct supplier Challenge.</h6><h6>.</h6>
````

<!--NOMAGIC_PAGE id=228985808 space=VR version=1 -->
## PAGE 00167: COR2351

- page_id: `228985808`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985808/COR2351
- version_number: 1
- version_date: `2023-09-15T10:07:52.428+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2351

**Message**

Supplier for the Impacted By should be Challenge or its specializations.

**Description**

The supplier is incorrect for Impacted By client Operational Activity. The supplier for the Operational Activity should be Challenge or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### The incorrect supplier Driver was replaced with the correct supplier Chanllenge.

###### .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2351</p><p><strong>Message</strong></p><p>Supplier for the Impacted By should be Challenge or its specializations.</p><p><strong>Description</strong></p><p>The supplier is incorrect for Impacted By client Operational Activity. The supplier for the Operational Activity should be Challenge or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2351.png" /></ac:image></p><h6>The incorrect supplier Driver was replaced with the correct supplier Chanllenge.</h6><h6>.</h6>
````

<!--NOMAGIC_PAGE id=228985810 space=VR version=1 -->
## PAGE 00168: COR2352

- page_id: `228985810`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985810/COR2352
- version_number: 1
- version_date: `2023-09-15T10:14:07.521+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2352

**Message**

Supplier for the Impacted By should be Challenge or its specializations.

**Description**

The supplier is incorrect for Impacted By client Actual Strategic Phase. The supplier for the Actual Strategic Phase should be Challenge or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### The incorrect supplier Driver was replaced with the correct supplier Challenge.

###### .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2352</p><p><strong>Message</strong></p><p>Supplier for the Impacted By should be Challenge or its specializations.</p><p><strong>Description</strong></p><p>The supplier is incorrect for Impacted By client Actual Strategic Phase. The supplier for the Actual Strategic Phase should be Challenge or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2352.png" /></ac:image></p><h6>The incorrect supplier Driver was replaced with the correct supplier Challenge.</h6><h6>.</h6>
````

<!--NOMAGIC_PAGE id=228985812 space=VR version=1 -->
## PAGE 00169: COR2353

- page_id: `228985812`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985812/COR2353
- version_number: 1
- version_date: `2023-09-15T10:19:43.809+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2353

**Message**

Client for the Impacted By should be Actual Outcome or its specializations.

**Description**

The client is incorrect for Impacted By supplier Enterprise Goal. The client for the Enterprise Goal should be Actual Outcome or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### The incorrect client Actual Effect was replaced with the correct client Actual Outcome.

###### .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2353</p><p><strong>Message</strong></p><p>Client for the Impacted By should be Actual Outcome or its specializations.</p><p><strong>Description</strong></p><p>The client is incorrect for Impacted By supplier Enterprise Goal. The client for the Enterprise Goal should be Actual Outcome or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2353.png" /></ac:image></p><h6>The incorrect client Actual Effect was replaced with the correct client Actual Outcome.</h6><h6>.</h6>
````

<!--NOMAGIC_PAGE id=228985814 space=VR version=1 -->
## PAGE 00170: COR2354

- page_id: `228985814`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985814/COR2354
- version_number: 1
- version_date: `2023-09-15T10:21:20.450+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2354

**Message**

Client for the Impacted By should be Capability or its specializations.

**Description**

The client is incorrect for Impacted By supplier Opportunity. The client for the Opportunity should be Capability or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### The incorrect client Challenge was replaced with the correct client Capability.

###### .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2354</p><p><strong>Message</strong></p><p>Client for the Impacted By should be Capability or its specializations.</p><p><strong>Description</strong></p><p>The client is incorrect for Impacted By supplier Opportunity. The client for the Opportunity should be Capability or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2354.png" /></ac:image></p><h6>The incorrect client Challenge was replaced with the correct client Capability.</h6><h6>.</h6>
````

<!--NOMAGIC_PAGE id=228985816 space=VR version=1 -->
## PAGE 00171: COR2355

- page_id: `228985816`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985816/COR2355
- version_number: 1
- version_date: `2023-09-15T10:38:24.297+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2355

**Message**

Client for the Impacted By should be specialization of Architecture or Actual Strategic Phase, or Operational Activity or its specializations.

**Description**

The client is incorrect for Impacted By supplier Challenge. The client for the Challenge should be a specialization of Architecture or Actual Strategic Phase, or Operational Activity or its specializations.

**Severity**

Error

**Context element**

Impacted By

**Example**

[IMAGE alt='' src='']

###### An example of the incorrect client Function was replaced with the correct client Operational Activity.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2355</p><p><strong>Message</strong></p><p>Client for the Impacted By should be specialization of Architecture or Actual Strategic Phase, or Operational Activity or its specializations.</p><p><strong>Description</strong></p><p>The client is incorrect for Impacted By supplier Challenge. The client for the Challenge should be a specialization of Architecture or Actual Strategic Phase, or Operational Activity or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Impacted By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2355.png" /></ac:image></p><h6>An example of the incorrect client Function was replaced with the correct client Operational Activity.</h6>
````

<!--NOMAGIC_PAGE id=228985554 space=VR version=1 -->
## PAGE 00172: COR2356

- page_id: `228985554`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985554/COR2356
- version_number: 1
- version_date: `2023-09-15T07:44:50.912+02:00`
- ancestors: Validation Rules > UAF validation rules > Active correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2356

**Message**

The client and supplier connected with the Motivated By relationship are paired incorrectly.

**Description**

Incorrect Motivated By coupling. Either the client or the supplier of the Motivated By relationship is incorrect.

**Severity**

Error

**Context element**

Motivated By

**Solvers**

- Change Motivated By Supplier Element - the Select <element> dialog opens. Choose the appropriate element.
- Change Motivated By Client Element - the Select <element> dialog opens. Choose the needed the appropriate element.
- Remove Motivated By Relationship - the relationship is removed.

**Example**

[IMAGE alt='' src='']

###### An example of an incorrect coupling where the supplier for the client Opportunity is incorrect.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2356</p><p><strong>Message</strong></p><p>The client and supplier connected with the Motivated By relationship are paired incorrectly.</p><p><strong>Description</strong></p><p>Incorrect Motivated By coupling. Either the client or the supplier of the Motivated By relationship is incorrect.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Motivated By</p><p><strong>Solvers</strong></p><ul><li><strong>Change Motivated By Supplier Element</strong> - the <strong>Select &lt;element&gt;</strong> dialog opens. Choose the appropriate element.</li><li><strong>Change Motivated By Client Element</strong> - the <strong>Select &lt;element&gt;</strong> dialog opens. Choose the needed the appropriate element.</li><li><strong>Remove Motivated By Relationship</strong> - the relationship is removed.</li></ul><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2360.png" /></ac:image></p><h6>An example of an incorrect coupling where the supplier for the client Opportunity is incorrect.</h6>
````

<!--NOMAGIC_PAGE id=228985818 space=VR version=1 -->
## PAGE 00173: COR2357

- page_id: `228985818`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985818/COR2357
- version_number: 1
- version_date: `2023-09-15T07:41:10.390+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2357

**Message**

Client for the Motivated By should be Opportunity or its specializations.

**Description**

The client is incorrect for Motivated By supplier Challenge. The client for the Challenge should be Opportunity or its specializations.

**Severity**

Error

**Context element**

Motivated By

**Example**

[IMAGE alt='' src='']

###### The incorrect client Enterprise Goal was replaced with the correct client Opportunity.

###### .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2357</p><p><strong>Message</strong></p><p>Client for the Motivated By should be Opportunity or its specializations.</p><p><strong>Description</strong></p><p>The client is incorrect for Motivated By supplier Challenge. The client for the Challenge should be Opportunity or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Motivated By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2357.png" /></ac:image></p><h6>The incorrect client Enterprise Goal was replaced with the correct client Opportunity.</h6><h6>.</h6>
````

<!--NOMAGIC_PAGE id=228985820 space=VR version=1 -->
## PAGE 00174: COR2358

- page_id: `228985820`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985820/COR2358
- version_number: 1
- version_date: `2023-09-15T07:41:22.938+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2358

**Message**

Client for the Motivated By should be Enterprise Goal or its specializations.

**Description**

The client is incorrect for Motivated By supplier Driver. The client for the Driver should be Enterprise Goal or its specializations.

**Severity**

Error

**Context element**

Motivated By

**Example**

[IMAGE alt='' src='']

###### The incorrect client Opportunity was replaced with the correct client Enterprise Goal.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2358</p><p><strong>Message</strong></p><p>Client for the Motivated By should be Enterprise Goal or its specializations.</p><p><strong>Description</strong></p><p>The client is incorrect for Motivated By supplier Driver. The client for the Driver should be Enterprise Goal or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Motivated By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2358.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">The incorrect client Opportunity was replaced with the correct client Enterprise Goal.</span></h6>
````

<!--NOMAGIC_PAGE id=228985822 space=VR version=1 -->
## PAGE 00175: COR2359

- page_id: `228985822`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985822/COR2359
- version_number: 1
- version_date: `2023-09-15T07:41:41.277+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2359

**Message**

Supplier for the Motivated By should be Driver or its specializations.

**Description**

The supplier is incorrect for the Motivated By client Enterprise Goal. The supplier for the Enterprise Goal should be Driver or its specializations.

**Severity**

Error

**Context element**

Motivated By

**Example**

[IMAGE alt='' src='']

###### The incorrect supplier Opportunity was replaced with the correct supplier Driver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2359</p><p><strong>Message</strong></p><p>Supplier for the Motivated By should be Driver or its specializations.</p><p><strong>Description</strong></p><p>The supplier is incorrect for the Motivated By client Enterprise Goal. The supplier for the Enterprise Goal should be Driver or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Motivated By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2359.png" /></ac:image></p><h6><span style="color: rgb(128,128,128);">The incorrect supplier Opportunity was replaced with the correct supplier Driver.</span></h6>
````

<!--NOMAGIC_PAGE id=228985824 space=VR version=1 -->
## PAGE 00176: COR2360

- page_id: `228985824`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985824/COR2360
- version_number: 1
- version_date: `2023-09-15T07:41:56.185+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2360

**Message**

Supplier for the Motivated By should be Challenge or its specializations.

**Description**

The supplier is incorrect for Motivated By client Opportunity. The supplier for the Opportunity should be Challenge or its specializations.

**Severity**

Error

**Context element**

Motivated By

**Example**

[IMAGE alt='' src='']

###### The incorrect supplier Driver was replaced with the correct supplier Challenge.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2360</p><p><strong>Message</strong></p><p>Supplier for the Motivated By should be Challenge or its specializations.</p><p><strong>Description</strong></p><p>The supplier is incorrect for Motivated By client Opportunity. The supplier for the Opportunity should be Challenge or its specializations.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Motivated By</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2360.png" /></ac:image></p><h6>The incorrect supplier Driver was replaced with the correct supplier Challenge.</h6>
````

<!--NOMAGIC_PAGE id=228985826 space=VR version=1 -->
## PAGE 00177: COR2361

- page_id: `228985826`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985826/COR2361
- version_number: 1
- version_date: `2023-09-15T11:44:02.822+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2361

**Message**

Class property value of the Operational Port must be Operational Agent or Operational Interface or their specializations.

**Description**

The type is incorrect for the Operational Port class property. The Class property value should be Operational Agent, Operational Interface, or one of these specializations.

**Severity**

Error

**Context element**

Operational Port

**Example**

[IMAGE alt='' src='']

###### The incorrect Class property value Resource Interface was changed to the Operational Interface.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>COR2361</p><p><strong>Message</strong></p><p>Class property value of the Operational Port must be Operational Agent or Operational Interface or their specializations.</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">The type is incorrect for the Operational Port class property. The Class property value should be Operational Agent, Operational Interface, or one of these specializations.</span></p><p><strong>Severity</strong></p><p>Error</p><p><strong>Context element</strong></p><p>Operational Port</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="cor2361.png" /></ac:image></p><h6>The incorrect Class property value Resource Interface was changed to the Operational Interface.</h6>
````

<!--NOMAGIC_PAGE id=228985828 space=VR version=3 -->
## PAGE 00178: COR2362

- page_id: `228985828`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985828/COR2362
- version_number: 3
- version_date: `2025-11-24T11:13:24.338+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

COR2362

**Message**

Capability Provision's actual start/end dates do not align with the Capability Provision's consolidated start/end dates

**Description**

The Capability Provision's actual and consolidated start and/or end dates do not match.

**Severity**

Warning

**Constrained element**

Resource Performer

**Solver**

- Change Capability Provision actual start/end dates to match Capability Provision consolidated start/end dates - the dates will be updated to match the Capability Provision start and end dates.
- Change Capability Provision actual start date to match Capability Provision consolidated start date - the date will be updated to match the Capability Provision start date.
- Change Capability Provision actual end date to match Capability Provision consolidated end date - the date will be updated to match the Capability Provision end date.

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><strong>Abbreviation</strong></p><p style="text-align: left;">COR2362</p><p style="text-align: left;"><strong>Message</strong></p><p style="text-align: left;">Capability Provision's actual start/end dates do not align with the Capability Provision's consolidated start/end dates</p><p style="text-align: left;"><strong>Description</strong></p><p style="text-align: left;">The Capability Provision's actual and consolidated start and/or end dates do not match.</p><p style="text-align: left;"><strong>Severity</strong></p><p style="text-align: left;">Warning</p><p style="text-align: left;"><strong>Constrained element</strong></p><p style="text-align: left;">Resource Performer</p><p style="text-align: left;"><strong>Solver</strong></p><ul><li style="text-align: left;"><strong>Change Capability Provision actual start/end dates to match Capability Provision consolidated start/end dates</strong> - the dates will be updated to match the Capability Provision start and end dates.</li><li><strong>Change Capability Provision actual start date to match Capability Provision consolidated start date </strong>- the date will be updated to match the Capability Provision start date.</li><li><strong>Change Capability Provision actual end date to match Capability Provision consolidated end date</strong> - the date will be updated to match the Capability Provision end date.</li></ul><p><strong>Example</strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985719 space=VR version=1 -->
## PAGE 00179: Correctness validation rules

- page_id: `228985719`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985719/Correctness+validation+rules
- version_number: 1
- version_date: `2016-02-23T09:27:51.358+01:00`
- ancestors: Validation Rules > UAF validation rules
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="afe097db-5de1-45ad-917c-c44b2140cb5a" /></p>
````

<!--NOMAGIC_PAGE id=243969473 space=VR version=1 -->
## PAGE 00180: Deprecated JavaScript

- page_id: `243969473`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969473/Deprecated+JavaScript
- version_number: 1
- version_date: `2025-07-31T10:51:29.923+02:00`
- ancestors: Validation Rules > UML validation rules > Deprecated JavaScript rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

JS

**Description**

This validation rule checks if the specified expression does not use Javascript Nashorn scripting language that is deprecated.

**Severity**

error

**Constrained Element**

Element

**Solvers**

- Change to JavaScript Rhino - changes the Javascript Nashorn scripting language to JavaScript Rhino.

**Example**

[IMAGE alt='' src='']

###### The *Parameter Direction and Type*Generic Table has a custom Column *Parameter Direction and Type using StringConcat* that implements a Javascript Nashorn script. 
The error is resolved by changing the scripting language to JavaScript Rhino via the **Change to JavaScript Rhino** solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>JS</p><p><strong>Description</strong></p><p>This validation rule checks if the specified expression does not use Javascript Nashorn scripting language that is deprecated.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Element</p><p><strong>Solvers</strong></p><ul><li><strong>Change to JavaScript Rhino</strong> - changes the Javascript Nashorn scripting language to JavaScript Rhino.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Deprecated JavaScript.png" /></ac:image></p><h6 style="text-align: center;">The <em>Parameter Direction and Type </em>Generic Table has a custom Column <em>Parameter Direction and Type using StringConcat</em> that implements a Javascript Nashorn script.<br />The error is resolved by changing the scripting language to JavaScript Rhino via the <strong>Change to JavaScript Rhino</strong> solver.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969472 space=VR version=1 -->
## PAGE 00181: Deprecated JavaScript rules

- page_id: `243969472`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969472/Deprecated+JavaScript+rules
- version_number: 1
- version_date: `2025-07-31T10:51:29.854+02:00`
- ancestors: Validation Rules > UML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides detailed descriptions of all validation rules that belong to the **Deprecated JavaScript** validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section provides detailed descriptions of all validation rules that belong to the <strong>Deprecated JavaScript</strong> validation suite.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="bff74fbd-b19e-4d14-80e5-6ac8392fa9de" /></p>
````

<!--NOMAGIC_PAGE id=17684449 space=VR version=17 -->
## PAGE 00182: DesignConstraint satisfied by an invalid element

- page_id: `17684449`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684449/DesignConstraint+satisfied+by+an+invalid+element
- version_number: 17
- version_date: `2021-01-12T12:02:40.145+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

designConstraint[1]****

**Description**

This validation rule checks if the Design Constraint is satisfied by a Block or Part Property.****

**Severity**

warning****

**Constrained Element**

designConstraint****

**Solvers**

- Remove invalid Satisfy relationship(s) - Deletes not valid Satisfy relationship from the model.

#### NOTE: Manual Solver

Manual Solver

Reconnect existing or create new satisfy relationship from Part Property or Block to Design Constraint.

**Example**

**[IMAGE alt='' src='']**

###### The*VCCS Sensors* Design Constraint is satisfied by a *sensorSystem* Part Property.

****

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>designConstraint[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the Design Constraint is satisfied by a Block or Part Property.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>designConstraint<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Remove invalid Satisfy relationship(s)</strong> - Deletes not valid Satisfy relationship from the model.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0d4c0fcb-c23a-414f-8a76-59d16ea1a160"><ac:parameter ac:name="title">Manual Solver</ac:parameter><ac:rich-text-body><p>Reconnect existing or create new satisfy relationship from Part Property or Block to Design Constraint.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="designConstraint_val_rule.png" /></ac:image></strong></p><h6 style="text-align: center;">The<em style="font-weight: bold;"> VCCS Sensors</em> Design Constraint is satisfied by a <em style="font-weight: bold;">sensorSystem</em> Part Property.</h6><p><strong><br /></strong></p><p><strong><br /></strong></p>
````

<!--NOMAGIC_PAGE id=243969481 space=VR version=1 -->
## PAGE 00183: Element not in diagram

- page_id: `243969481`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969481/Element+not+in+diagram
- version_number: 1
- version_date: `2025-07-31T10:51:30.200+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Element(s) not in diagram

**Description**

This validation rule checks if the element is displayed on the diagram pane when that element and the diagram have the same owner (behavior context). This rule applies to Sequence, Activity, State Machine, and Communication diagrams.

**Severity**

warning

**Constrained Element**

Diagram

**Solvers**

- Display Inner Elements - displays the element that is not displayed in the diagram that belongs to the same owner as the element.
- Remove Element - removes the element that is not displayed in any of the diagrams that belong to the same owner as the element from the Model.

**Example**

[IMAGE alt='' src='']

###### Activity Parameter Node *: Hot Air* and the diagram *Cool Down Cabin Air*belong to the same owner, Activity *Cool Down Cabin Air*, but the Activity Parameter Node *: Hot Air* is not displayed on the diagram *Cool Down Cabin Air*. 
The error is resolved by displaying the Activity Parameter Node *: Hot Air*via the **Display Inner Elements**solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>Element(s) not in diagram</p><p><strong>Description</strong></p><p>This validation rule checks if the element is displayed on the diagram pane when that element and the diagram have the same owner (behavior context). This rule applies to Sequence, Activity, State Machine, and Communication diagrams.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Diagram</p><p><strong>Solvers</strong></p><ul><li><strong>Display Inner Elements </strong>- displays the element that is not displayed in the diagram that belongs to the same owner as the element.</li><li><strong>Remove Element</strong> - removes the element that is not displayed in any of the diagrams that belong to the same owner as the element from the Model.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Element_not_in_diagram.png" /></ac:image></p><h6 style="text-align: center;">Activity Parameter Node <em>: Hot Air</em> and the diagram <em>Cool Down Cabin Air </em>belong to the same owner, Activity <em>Cool Down Cabin Air</em>, but the Activity Parameter Node <em>: Hot Air</em> is not displayed on the diagram <em>Cool Down Cabin Air</em>. <br />The error is resolved by displaying the Activity Parameter Node <em>: Hot Air </em>via the <strong>Display Inner Elements </strong>solver.</h6>
````

<!--NOMAGIC_PAGE id=17684827 space=VR version=5 -->
## PAGE 00184: Encapsulation of the Block

- page_id: `17684827`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684827/Encapsulation+of+the+Block
- version_number: 5
- version_date: `2021-02-11T09:49:12.016+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Block[A]****

**Description**

This validation rule checks If **isEncapsulated**property value of a Block is set to *true*, then the Block is treated as a black box: a Part Property typed by this black box can only be connected via its ports or directly to its outer boundary.****

**Severity**

warning****

**Constrained Element**

Connector****

**Solvers**

To fix this, connect nested part that are typed by encapsulated Block via ports or outer boundary.

**Example**

**[IMAGE alt='' src='']**

###### The Brake Block is encapsulated and nested Part Properties typed by it are connected via Proxy Ports.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>Block[A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks If <strong><ac:inline-comment-marker ac:ref="69f79cf1-05de-4c44-beb5-f1982924d439">isEncapsulated</ac:inline-comment-marker> </strong>property value of a Block is set to <em>true</em>, then the Block is treated as a black box: a Part Property typed by this black box can only be connected via its ports or directly to its outer boundary.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Connector<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, connect nested part that are typed by encapsulated Block via ports or outer boundary.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="isEncapsulated.png" /></ac:image></strong></p><h6 style="text-align: center;">The Brake Block is encapsulated and nested Part Properties typed by it are connected via Proxy Ports.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969483 space=VR version=1 -->
## PAGE 00185: Flows on decision

- page_id: `243969483`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969483/Flows+on+decision
- version_number: 1
- version_date: `2025-07-31T10:51:30.303+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

DecisionOut

**Description**

This validation rule checks if a Decision Node has more than one Outgoing Edge.

**Severity**

warning

**Constrained Element**

DecisionNode

**Solvers**

- To fix this, make sure a Decision Node has more than one Outgoing Edge.

**Example**

[IMAGE alt='' src='']

###### The Decision Node has only one Outgoing Edge. The error is resolved by creating a second Outgoing Edge.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>DecisionOut</p><p><strong>Description</strong></p><p>This validation rule checks if a Decision Node has more than one Outgoing Edge.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>DecisionNode</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure a Decision Node has more than one Outgoing Edge.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Flows_on_decision.png" /></ac:image></p><h6 style="text-align: center;">The Decision Node has only one Outgoing Edge. The error is resolved by creating a second Outgoing Edge.</h6>
````

<!--NOMAGIC_PAGE id=17684454 space=VR version=13 -->
## PAGE 00186: FunctionalRequirement satisfied by an invalid element

- page_id: `17684454`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684454/FunctionalRequirement+satisfied+by+an+invalid+element
- version_number: 13
- version_date: `2021-01-13T12:09:06.855+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

functionalRequirement[1]****

**Description**

This validation rulechecks if the Functional Requirement is satisfied by an Operation, Action, State or Behavior. ****

**Severity**

warning****

**Constrained Element**

Functional Requirement****

**Solvers**

- **Remove invalid Satisfy relationship(s)** - Deletes not valid Satisfy relationship from the model. Manual SolverReconnect existing or create new satisfy relationship from Operation, Action, State or Behavior to Functional Requirement.

**Example**

[IMAGE alt='' src='']

###### The*Break Functional Requirements*Functional Requirementis satisfied by a *Break***Activity.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>functionalRequirement[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks if the Functional Requirement is s</span>atisfied by an Operation, Action, State or Behavior. <strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Functional Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><p class="auto-cursor-target"><strong>Remove invalid Satisfy relationship(s)</strong> - Deletes not valid Satisfy relationship from the model.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="34bd3ce6-f85b-4ad8-8ffd-66087a099605"><ac:parameter ac:name="title">Manual Solver</ac:parameter><ac:rich-text-body><p>Reconnect existing or create new satisfy relationship from Operation, Action, State or Behavior to <span style="color: rgb(62,63,64);">Functional Requirement</span>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="functional Req.png" /></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(94,108,132);">The</span><em> Break Functional Requirements </em>Functional Requirement<span style="color: rgb(94,108,132);"> is satisfied by a <em>Break</em></span><span style="color: rgb(94,108,132);"><em> </em>Activity.</span></h6>
````

<!--NOMAGIC_PAGE id=243969485 space=VR version=1 -->
## PAGE 00187: Guard on decision

- page_id: `243969485`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969485/Guard+on+decision
- version_number: 1
- version_date: `2025-07-31T10:51:30.399+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

DecisionGuar

**Description**

This validation rule checks if a Flow from a Decision Node has a Guard specified.

**Severity**

warning

**Constrained Element**

ActivityEdge

**Solvers**

- To fix this, make sure to specify a Guard for a Flow from a Decision Node.

**Example**

[IMAGE alt='' src='']

###### The Decision Node has two outgoing Object Flows, one of which has no Guard. The error is resolved by specifying the Guard for the second Flow.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>DecisionGuar</p><p><strong>Description</strong></p><p>This validation rule checks if a Flow from a Decision Node has a Guard specified.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>ActivityEdge</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure to specify a Guard for a Flow from a Decision Node.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Guard_on_decision.png" /></ac:image></p><h6 style="text-align: center;">The Decision Node has two outgoing Object Flows, one of which has no Guard. The error is resolved by specifying the Guard for the second Flow.</h6>
````

<!--NOMAGIC_PAGE id=243969487 space=VR version=1 -->
## PAGE 00188: Implemented Operations

- page_id: `243969487`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969487/Implemented+Operations
- version_number: 1
- version_date: `2025-07-31T10:51:30.511+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ImplOp

**Description**

This validation rule checks if all operations of realized interfaces are implemented.

**Severity**

warning

**Constrained Element**

Class

**Solvers**

- To fix this, make sure all operations of realized interfaces are implemented.

**Example**

[IMAGE alt='' src='']

###### The realized interface *Air Control*contains the *CoolAir*operation that is not implemented. The error is resolved by implementing the operation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ImplOp</p><p><strong>Description</strong></p><p>This validation rule checks if all operations of realized interfaces are implemented.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Class</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure all operations of realized interfaces are implemented.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Implemented_Operations.png" /></ac:image></p><h6 style="text-align: center;">The realized interface <em>Air Control </em>contains the <em>CoolAir </em>operation that is not implemented. The error is resolved by implementing the operation. </h6>
````

<!--NOMAGIC_PAGE id=267026811 space=VR version=8 -->
## PAGE 00189: InconsistentSpecializingPropertyType

- page_id: `267026811`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/267026811/InconsistentSpecializingPropertyType
- version_number: 8
- version_date: `2025-10-30T12:49:43.245+01:00`
- ancestors: Validation Rules > Systems Cybersecurity Designer validation rules
- labels: []

### NORMALIZED CONTENT

All ISO 21434 valueProperties must be typed by a specific Enumeration as defined in the ISO 21434 Profile. If an improper type or no type is set for such a valueProperty, a validation error will appear. The validation rule will have the abbreviation **ISPT** and a message describing the problem. The validation rule provides a solver whereby the valueProperty’s type will be reset to the appropriate Enumeration. Below is a table showing the abstract class and property from the profile, along with the enumeration that must be the type of that property.

**Abbreviation**

ISPT

**Message**

Invalid type for property '<Property Name>': '<Property Type>'

**Severity**

error

**Context element**

The following table shows the appropriate abstract class, property from the profile, and the correct enumeration.****

| AbstractClass | Property | Enumeration |
| --- | --- | --- |
| AbstractCybersecurityAsset | Confidentiality | HiMedLoValuation |
| AbstractCybersecurityAsset | Integrity | HiMedLoValuation |
| AbstractCybersecurityAsset | Availability | HiMedLoValuation |
| AbstractEffectWithImpact | SafetyImpact | ImpactRating |
| AbstractEffectWithImpact | FinancialImpact | ImpactRating |
| AbstractEffectWithImpact | OperationalImpact | ImpactRating |
| AbstractEffectWithImpact | PrivacyImpact | ImpactRating |
| AbstractManualAttackPath | AttackFeasibilityRating | HiMedLoFeasibility |
| AbstractAttackPathISO18045 | Elapsed Time | ElapsedTime |
| AbstractAttackPathISO18045 | Equipment | Equipment |
| AbstractAttackPathISO18045 | Expertise | Expertise |
| AbstractAttackPathISO18045 | Knowledge of TOE | Knowledge of TOE |
| AbstractAttackPathISO18045 | Window of Opportunity | Window of Opportunity |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>All ISO 21434 valueProperties must be typed by a specific Enumeration as defined in the ISO 21434 Profile.  If an improper type or no type is set for such a valueProperty, a validation error will appear.  The validation rule will have the abbreviation <strong>ISPT</strong> and a message describing the problem.  The validation rule provides a solver whereby the valueProperty’s type will be reset to the appropriate Enumeration.  Below is a table showing the abstract class and property from the profile, along with the enumeration that must be the type of that property.</p><p style="text-align: left;"><strong>Abbreviation</strong></p><p style="text-align: left;">ISPT</p><p style="text-align: left;"><strong>Message</strong></p><p style="text-align: left;">Invalid type for property '&lt;Property Name&gt;': '&lt;Property Type&gt;'</p><p style="text-align: left;"><strong>Severity</strong></p><p style="text-align: left;">error</p><p style="text-align: left;"><strong>Context element</strong></p><p style="text-align: left;">The following table shows the appropriate abstract class, property from the profile, and the correct enumeration.<strong><br /><br /></strong></p><table><tbody><tr><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>AbstractClass</strong></p></td><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>Property</strong></p></td><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>Enumeration</strong></p></td></tr><tr><td><p>AbstractCybersecurityAsset</p></td><td><p>Confidentiality</p></td><td><p>HiMedLoValuation</p></td></tr><tr><td><p>AbstractCybersecurityAsset</p></td><td><p>Integrity</p></td><td><p>HiMedLoValuation</p></td></tr><tr><td><p>AbstractCybersecurityAsset</p></td><td><p>Availability</p></td><td><p>HiMedLoValuation</p></td></tr><tr><td><p>AbstractEffectWithImpact</p></td><td><p>SafetyImpact</p></td><td><p>ImpactRating</p></td></tr><tr><td><p>AbstractEffectWithImpact</p></td><td><p>FinancialImpact</p></td><td><p>ImpactRating</p></td></tr><tr><td><p>AbstractEffectWithImpact</p></td><td><p>OperationalImpact</p></td><td><p>ImpactRating</p></td></tr><tr><td><p>AbstractEffectWithImpact</p></td><td><p>PrivacyImpact</p></td><td><p>ImpactRating</p></td></tr><tr><td><p>AbstractManualAttackPath</p></td><td><p>AttackFeasibilityRating</p></td><td><p>HiMedLoFeasibility</p></td></tr><tr><td><p>AbstractAttackPathISO18045</p></td><td><p>Elapsed Time</p></td><td><p>ElapsedTime</p></td></tr><tr><td><p>AbstractAttackPathISO18045</p></td><td><p>Equipment</p></td><td><p>Equipment</p></td></tr><tr><td><p>AbstractAttackPathISO18045</p></td><td><p>Expertise</p></td><td><p>Expertise</p></td></tr><tr><td><p>AbstractAttackPathISO18045</p></td><td><p>Knowledge of TOE</p></td><td><p>Knowledge of TOE</p></td></tr><tr><td><p>AbstractAttackPathISO18045</p></td><td><p>Window of Opportunity</p></td><td><p>Window of Opportunity</p></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=267026814 space=VR version=8 -->
## PAGE 00190: InconsistentStereotypeAndAbstractClass

- page_id: `267026814`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/267026814/InconsistentStereotypeAndAbstractClass
- version_number: 8
- version_date: `2025-10-30T12:49:31.055+01:00`
- ancestors: Validation Rules > Systems Cybersecurity Designer validation rules
- labels: []

### NORMALIZED CONTENT

Most elements (see below) in an ISO 21434 project have a stereotype and general classifier pair. If the general classifier of such an element is removed, or an element is created and given only a stereotype listed below, a validation error will appear. The validation rule provides a solver whereby the appropriate general classifier can be applied to the element by selecting the solver option. That validation error will have the abbreviation **ISAC** and a message describing the problem.

**Abbreviation**

ISAC

**Message**

'<Element Name>' has applied stereotype '<Stereotype Name>' but has no generalization to '<AbstractElementType Name>'

**Severity**

error

**Context element**

This table shows the appropriate stereotype and the corresponding abstract class.

| Stereotype | AbstractClass |
| --- | --- |
| AttackPotentialBasedAttackPath | AbstractAttackPotentialBasedAttackPath |
| CybersecurityAsset | AbstractCybersecurityAsset |
| DamageScenario | AbstractDamageScenario |
| ManualAttackPath | AbstractManualAttackPath |
| ThreatScenario | AbstractThreatScenario |
| CybersecurityAssuranceLevel | AbstractCybersecurityAssuranceLevel |
| Weakness | Weakness (from RAMML) |

**Solvers**

You can select the **Add generalization to ‘<AbstractElementType>'**command.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Most elements (see below) in an ISO 21434 project have a stereotype and general classifier pair.  If the general classifier of such an element is removed, or an element is created and given only a stereotype listed below, a validation error will appear. The validation rule provides a solver whereby the appropriate general classifier can be applied to the element by selecting the solver option. That validation error will have the abbreviation <strong>ISAC</strong> and a message describing the problem. </p><p style="text-align: left;"><strong>Abbreviation</strong></p><p style="text-align: left;">ISAC</p><p style="text-align: left;"><strong>Message</strong></p><p style="text-align: left;">'&lt;Element Name&gt;' has applied stereotype '&lt;Stereotype Name&gt;' but has no generalization to '&lt;AbstractElementType Name&gt;'</p><p style="text-align: left;"><strong>Severity</strong></p><p style="text-align: left;">error</p><p style="text-align: left;"><strong>Context element</strong></p><p>This table shows the appropriate stereotype and the corresponding abstract class.<br /><br /></p><table class="wrapped"><tbody><tr><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>Stereotype</strong></p></td><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>AbstractClass</strong></p></td></tr><tr><td><p>AttackPotentialBasedAttackPath</p></td><td><p>AbstractAttackPotentialBasedAttackPath</p></td></tr><tr><td><p>CybersecurityAsset</p></td><td><p>AbstractCybersecurityAsset</p></td></tr><tr><td><p>DamageScenario</p></td><td><p>AbstractDamageScenario</p></td></tr><tr><td><p>ManualAttackPath</p></td><td><p>AbstractManualAttackPath</p></td></tr><tr><td><p>ThreatScenario</p></td><td><p>AbstractThreatScenario</p></td></tr><tr><td><p>CybersecurityAssuranceLevel</p></td><td><p>AbstractCybersecurityAssuranceLevel</p></td></tr><tr><td><p>Weakness</p></td><td><p>Weakness (from RAMML)</p></td></tr></tbody></table><p><strong style="text-align: left;"><br />Solvers</strong></p><p>You can select the <strong>Add generalization to ‘&lt;AbstractElementType&gt;' </strong>command.</p>
````

<!--NOMAGIC_PAGE id=243969489 space=VR version=1 -->
## PAGE 00191: Information Flow has no Conveyed Information

- page_id: `243969489`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969489/Information+Flow+has+no+Conveyed+Information
- version_number: 1
- version_date: `2025-07-31T10:51:30.641+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

IFHNCI[1]

**Description**

This validation rule checks if there are any Information Flows without Conveyed Information.

**Severity**

warning

**Constrained Element**

Information Flow

**Solvers**

- **Select Conveyed Information** - opens the Select Conveyed Information dialog where you can choose the Conveyed Information for the validated Information Flow.

**Example**

[IMAGE alt='' src='']

###### An Information Flow has no Conveyed Information. The error is resolved by specifying Conveyed Information via the **Select Conveyed Information**solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p><span style="color: rgb(23,43,77);">IFHNCI</span><span class="error" style="color: rgb(23,43,77);">[1]</span></p><p><strong>Description</strong></p><p>This validation rule checks if there are any <span style="color: rgb(23,43,77);">Information Flows without Conveyed Information.</span></p><p><strong>Severity</strong></p><p><span style="color: rgb(23,43,77);">warning</span></p><p><strong>Constrained Element</strong></p><p><span style="color: rgb(23,43,77);">Information Flow</span></p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Select Conveyed Information</strong> - <span style="color: rgb(23,43,77);">opens the Select Conveyed Information dialog where you can choose the Conveyed Information for the validated Information Flow.</span></span></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Information_Flow_has_no_Conveyed_Information.png" /></ac:image></p><h6 style="text-align: center;">An Information Flow has no Conveyed Information. The error is resolved by specifying Conveyed Information via the <strong>Select Conveyed Information </strong>solver.</h6>
````

<!--NOMAGIC_PAGE id=17684457 space=VR version=6 -->
## PAGE 00192: InterfaceRequirement satisfied by an invalid element

- page_id: `17684457`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684457/InterfaceRequirement+satisfied+by+an+invalid+element
- version_number: 6
- version_date: `2021-01-06T06:50:37.255+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

interfaceRequirement[1]****

**Description**

This rulechecks if Interface Requiement is satisfied by a port, Connector, Item Flow, and/or Constraint Property.****

**Severity**

warning****

**Constrained Element**

Interface Requirement****

**Solvers**

- **Remove invalid Satisfy relationship(s)** - deletes not valid Satisfy relationship from the model.

**Example**

**[IMAGE alt='' src='']**

###### The *Display Check Money Status* Interface Requirement s satisfied by *Check Money* Item Flow.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>interfaceRequirement[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule </span><span style="color: rgb(62,63,64);">checks if Interface Requiement is s</span>atisfied by a port, Connector, Item Flow, and/or Constraint Property.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Interface Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong><strong>Remove invalid Satisfy relationship(s)</strong></strong><span style="color: rgb(62,63,64);"> - deletes not valid Satisfy relationship from the model.</span></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="interface_req_val_rule.png" /></ac:image></strong></p><h6 style="text-align: center;">The <em>Display Check Money Status</em> Interface Requirement s satisfied by <em>Check Money</em> Item Flow.</h6></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684800 space=VR version=8 -->
## PAGE 00193: Invalid Activity Edge source

- page_id: `17684800`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684800/Invalid+Activity+Edge+source
- version_number: 8
- version_date: `2021-01-12T15:00:29.556+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Probability[1]****

**Description**

This validation rule checks to see if the «probability» stereotype is only applied to activity edges that have decision nodes or object nodes as sources.****

**Severity**

warning****

**Constrained Element**

Activity Edge, Parameter Set****

**Solvers**

To fix this, apply the «probability» stereotype to all activity edges that have decision nodes or object nodes as sources.

**Example**

**[IMAGE alt='' src='']**

###### The «probability» stereotype is applied to activity edges that have decision node as a source.

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Probability[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks to see if the «probability» stereotype is only applied to a<ac:inline-comment-marker ac:ref="82b26356-6568-4a07-b9bf-460bf0ba58ea">ctivity edges</ac:inline-comment-marker> that have decision nodes or object nodes as sources.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity Edge, Parameter Set<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, apply the «probability» stereotype to all activity edges that have decision nodes or object nodes as sources.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_activity_edge_source.png" /></ac:image></strong></p><h6 style="text-align: center;">The «probability» stereotype is applied to activity edges that have decision node as a source.</h6><p><strong><br /></strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684924 space=VR version=9 -->
## PAGE 00194: Invalid Aggregation

- page_id: `17684924`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684924/Invalid+Aggregation
- version_number: 9
- version_date: `2021-02-11T09:49:26.232+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ParticipantProperty[3]****

**Description**

This validation rule checks if the **Aggregation** property value of a Property stereotyped by «ParticipantProperty» is set to *none*. ****

**Severity**

warning****

**Constrained Element**

Participant Property****

**Solvers**

- **Change Aggregation Kind to none -**sets the **Aggregation** property value to *none*.

**Example**

**[IMAGE alt='' src='']**

###### The Aggregation property value is set to none for the *suppliedByInLink* Participant Property.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ParticipantProperty[3]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the <strong>Aggregation</strong> property value of a Property stereotyped by <span style="color: rgb(62,63,64);">«P</span>articipantProperty<span style="color: rgb(62,63,64);">»</span> <ac:inline-comment-marker ac:ref="890fb80b-5b85-4749-9801-d61d0b675501">is set to <em>none</em>.</ac:inline-comment-marker> <span style="color: rgb(62,63,64);"> </span><span style="color: rgb(62,63,64);"> </span><strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Participant Property<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><p><strong>Change Aggregation Kind to none - </strong><span style="color: rgb(62,63,64);">sets the <strong>Aggregation</strong> property value to <em>none</em>.</span></p></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="ParticipantProperty_aggregation.png" /></ac:image><br /></strong></p><h6 style="text-align: center;">The Aggregation property value is set to none for the <em>suppliedByInLink</em> Participant Property.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684829 space=VR version=9 -->
## PAGE 00195: Invalid Association ends name

- page_id: `17684829`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684829/Invalid+Association+ends+name
- version_number: 9
- version_date: `2021-01-12T13:41:04.426+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Block[3]****

**Description**

This validation rule checks if the Property that is typed by a Block and is owned by an Association (which kind is Aggregation or Composition) does not have a name and is not defined as a navigable end of the Association.****

**Severity**

warning****

**Constrained Element**

Property****

**Solvers**

To fix this, delete the name of the Property that s typed by a Block and is owned by an Association end which is not navigable.

**Example**

###### **[IMAGE alt='' src='']**The Property typed by the*Regulation Loop Principle* Block and is owned by Association has no name.

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>Block[3]<strong><br /></strong></p><p><strong>Description</strong></p><p><ac:inline-comment-marker ac:ref="e2349768-c09b-467a-835c-ea0d7d5f6357">This validation rule checks if the Property</ac:inline-comment-marker> that is typed by a Block and is owned by an Association (which kind is Aggregation or Composition) does not have a name and is not defined as a navigable end of the Association.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Property<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, delete the name of the Property that s typed by a Block and is owned by an <ac:inline-comment-marker ac:ref="7302dfaa-6bcd-472b-99f6-fba8ab0969a9">Association <span style="color: rgb(62,63,64);">end which is not navigable</span></ac:inline-comment-marker>.</p><p><strong>Example</strong></p><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_association_ends_name.png" /></ac:image></strong>The Property typed by the<em> Regulation Loop Principle</em> Block and is owned by Association has no name.</h6><p><strong><br /></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684374 space=VR version=12 -->
## PAGE 00196: Invalid Connector

- page_id: `17684374`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684374/Invalid+Connector
- version_number: 12
- version_date: `2024-04-15T18:34:31.611+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

InvConnector****

**Description**

This validation rule checks if the owner of the Connector is correct or the Connector ends specified in the model are not changed.

**Severity**

error****

**Constrained Element**

Connector, Property****

**Solvers**

- Update Connector Ends - sets the same owner for the Binding Connector as specified for its ends.
- Delete from Diagram - removes Binding Connector from the diagram.
- Delete from Model - removes Binding Connector from the model.

**Example**

**[IMAGE alt='' src='']**

###### The correct owner is selected for the Binding Connector.

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>InvConnector<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the owner of the Connector is correct or the Connector ends specified in the model are not changed.</p><p><strong>Severity</strong></p><p>error<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Connector, Property<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Update Connector Ends </strong>- sets the same owner for the Binding Connector as specified for its ends.</li><li><strong>Delete from Diagram</strong> - removes Binding Connector from the diagram.</li><li><strong>Delete from Model</strong> - removes Binding Connector from the model.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="InvConnector.png" /></ac:image></strong></p><h6 style="text-align: center;">The correct owner is selected for the Binding Connector.</h6><p><strong> </strong></p>
````

<!--NOMAGIC_PAGE id=166396640 space=VR version=4 -->
## PAGE 00197: Invalid Connector (UML Correctness)

- page_id: `166396640`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/166396640/Invalid+Connector+UML+Correctness
- version_number: 4
- version_date: `2024-04-15T20:02:23.532+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Other validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

InvConnector

**Description**

This validation rule checks if the Connector's owner is wrong or if the Connector Ends specified in the model are changed.

**Severity**

error

**Constrained Element**

Connector, Connector End, Diagram

**Solvers**

- Update Connector Ends - updates the Connector Ends to the correct ones and/or moves the Connector to the correct owner.
- Redefine and Replace Connector - redefines the inherited Connector and replaces it with the redefining one if one of the inherited Connector's Ends is redefined.
- Replace with Redefining - replaces the inherited Connector with the redefining one if one of the inherited Connector's Ends is redefined and the Connector is already redefined in the same context.
- Delete from Diagram - deletes the Connector from the Diagram.
- Delete from Model - deletes the Connector from the Model.

**Example**

###### **[IMAGE alt='' src='']**Part Properties typed by *VCCU* and *Cabin*are under the owner Block *Vehicle in Use*. The Connector between these Part Properties is under a different owner *Vehicle in Maintenance*, which causes an error. 
The error is resolved via the **Update Connector Ends**solver, which moves the Connector under the Block *Vehicle in Use*, making it the owner.****

###### **[IMAGE alt='' src='']**One of the inherited Connector's Ends is redefined while the Connector itself is inherited, causing the validation error. 
The error is resolved via the **Redefine and Replace Connector** solver, which redefines the inherited Connector and replaces it with the redefining one.

###### **[IMAGE alt='' src='']**One of the inherited Connector's Ends is redefined while the Connector itself is inherited, causing the validation error. 
The error is resolved via the **Replace with Redefining** solver, which replaces the inherited Connector with the redefining Connector that already exists in the same context.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>InvConnector</p><p><strong>Description</strong></p><p>This validation rule checks if the <span>Connector's owner is wrong or if the Connector Ends specified in the model are changed.</span></p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Connector, Connector End, Diagram</p><p><strong>Solvers</strong></p><ul><li><strong>Update Connector Ends</strong> - updates the Connector Ends to the correct ones and/or moves the Connector to the correct owner. </li><li><strong>Redefine and Replace Connector</strong> - redefines the inherited Connector and replaces it with the redefining one if one of the inherited Connector's Ends is redefined.</li><li><strong>Replace with Redefining</strong> - replaces the inherited Connector with the redefining one if one of the inherited Connector's Ends is redefined and the Connector is already redefined in the same context.</li><li><strong>Delete from Diagram </strong>- deletes the Connector from the Diagram.</li><li><strong>Delete from Model </strong>- deletes the Connector from the Model.</li></ul><p><strong>Example</strong></p><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="Invalid Connector.png" /></ac:image></strong>Part Properties typed by <em>VCCU</em> and <em>Cabin </em>are under the owner Block <em>Vehicle in Use</em>. The Connector between these Part Properties is under a different owner <em>Vehicle in Maintenance</em>, which causes an error.<br />The error is resolved via the <strong>Update Connector Ends </strong>solver, which moves the Connector under the Block <em>Vehicle in Use</em>, making it the owner.<strong> </strong></h6><hr /><h6 style="text-align: center;">                  </h6><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="Invalid Connector_Redefine and Replace Connector.png" /></ac:image></strong>One of the inherited Connector's Ends is redefined while the Connector itself is inherited, causing the validation error. <br />The error is resolved via the <strong>Redefine and Replace Connector</strong> solver, which redefines the inherited Connector and replaces it with the redefining one.</h6><hr /><h6 style="text-align: center;">                  </h6><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="Invalid Connector_Replace with Redefining.png" /></ac:image></strong>One of the inherited Connector's Ends is redefined while the Connector itself is inherited, causing the validation error. <br />The error is resolved via the <strong>Replace with Redefining</strong> solver, which replaces the inherited Connector with the redefining Connector that already exists in the same context.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=20845934 space=VR version=1 -->
## PAGE 00198: Invalid Copy of requirement

- page_id: `20845934`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845934/Invalid+Copy+of+requirement
- version_number: 1
- version_date: `2017-08-21T11:34:15.300+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Copy[A]****

**Description**

A requirement can’t copy more than one requirement.****

**Severity**

warning****

**Context element**

Copy****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Copy[A]<strong><br /></strong></p><p><strong>Description</strong></p><p>A requirement can’t copy more than one requirement.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Copy<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684366 space=VR version=10 -->
## PAGE 00199: Invalid ends type compatibility

- page_id: `17684366`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684366/Invalid+ends+type+compatibility
- version_number: 10
- version_date: `2021-02-11T09:46:58.710+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

BindingConnector[1]****

**Description**

This validation rule checks if the two ends of a Binding Connector must have either the same type or types that are compatible so that equality of their values can be defined.

**Severity**

warning****

**Constrained Element**

Connector****

**Solvers**

- Convert types of Binding Connector ends to be type of <parameter name> - specifies the same type for both ends of Binding Connector.

**Example**

**[IMAGE alt='' src='']**

###### The types of Parameters *o* and *i* are the same Value Property Real.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>BindingConnector[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule checks if t</span>he two ends of a Binding Connector must have either the same type or types that are compatible so that equality of their values can be defined.</p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Connector<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Convert types of Binding Connector ends to be type of &lt;parameter name&gt;</strong> - specifies the same type for both ends of Binding Connector.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="binding_connector_ends_type.png" /></ac:image></strong></p><h6 style="text-align: center;">The types of Parameters <em>o</em> and <em>i</em> are the same Value Property Real.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=20845951 space=VR version=1 -->
## PAGE 00200: Invalid generalization of Requirement

- page_id: `20845951`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845951/Invalid+generalization+of+Requirement
- version_number: 1
- version_date: `2017-08-21T11:46:05.509+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Requirement[4]****

**Description**

Classes stereotyped by «requirement» may not participate in generalizations.****

**Severity**

warning****

**Context element**

Generalization****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Requirement[4]<strong><br /></strong></p><p><strong>Description</strong></p><p>Classes stereotyped by «requirement» may not participate in generalizations.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Generalization<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684776 space=VR version=12 -->
## PAGE 00201: Invalid isControlType tag

- page_id: `17684776`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684776/Invalid+isControlType+tag
- version_number: 12
- version_date: `2021-01-12T14:25:46.859+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ControlValue[1]****

**Description**

This validation rulechecks to see ifthe **I****s Control Type** property value is *true* for object nodes with the type ControlValueKind.****

**Severity**

warning****

**Constrained Element**

Object Node****

**Solvers**

To fix this, in the Object Node's Specification window, set the**Is****Control Type** property value to *true*. To find this property, switch the**All**property mode in the Specification window.

**Example**

**[IMAGE alt='' src='']**

###### The object node typed by ControlValueKind must be set asisControlType.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;"><strong>Abbreviation</strong></p><p>ControlValue[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks to see if</span><span style="color: rgb(62,63,64);"> the <strong>I</strong></span><strong>s Control Type</strong> property value is <em>true</em> for object nodes with the type ControlValueKind.<strong> <br /> </strong></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Object Node<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p>To fix this, in the Object Node's Specification window, set the<span style="color: rgb(62,63,64);"> <strong>Is</strong> </span><strong>Control Type</strong> property value to <em>true</em>. To find this property, switch <span>the </span><strong>All</strong><span> property mode in the Specification window.</span></p><p><span><strong>Example</strong><br /></span></p><p><strong style="letter-spacing: 0.0px;"><br /><ac:image ac:align="center"><ri:attachment ri:filename="isControlType.png" /></ac:image></strong></p><p><br /></p><h6 style="text-align: center;">The object node typed by ControlValueKind must be set as<span> </span>isControlType.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684804 space=VR version=8 -->
## PAGE 00202: Invalid isStream tag

- page_id: `17684804`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684804/Invalid+isStream+tag
- version_number: 8
- version_date: `2021-02-11T09:54:58.747+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Rate[1]****

**Description**

This validation rule checks to see if a parameter is streaming when the «rate» stereotype is applied to it.****

**Severity**

warning****

**Constrained Element**

Activity Edge, Object Node, Parameter****

**Solvers**

To fix this, in the Parameter's Specification window, set the**Is Stream** property value to *true*. To find this property, switchthe**All**property mode in the Specification window.

****

**Example**

**[IMAGE alt='' src='']**

###### The output Parameter must be streaming if it is stereotyped by «rate».

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Rate[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks to see if a parameter is streaming when the «rate» stereotype is applied to it.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity Edge, Object Node, Parameter<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, in the Parameter's Specification window, set the<span style="color: rgb(62,63,64);"> <strong>Is Stream</strong></span> property value to <em>true</em>. <span style="color: rgb(62,63,64);">To find this property, switch </span><span style="color: rgb(62,63,64);">the </span><strong>All</strong><span style="color: rgb(62,63,64);"> property mode in the Specification window.</span></p><p><strong><br /></strong></p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="rate_stereotype_on_streaming_parameter.png" /></ac:image></strong></p><h6 style="text-align: center;">The output Parameter must be streaming if it is stereotyped by «rate».</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684382 space=VR version=8 -->
## PAGE 00203: Invalid Matching Unit and QuantityKind

- page_id: `17684382`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684382/Invalid+Matching+Unit+and+QuantityKind
- version_number: 8
- version_date: `2021-02-02T13:51:26.676+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ValueType[A]****

**Description**

This validation rule checks if a value is present for the unit attribute, the quantity kind attribute must be equal to the quantity kind property of the referenced unit.

**Severity**

info****

**Constrained Element**

Value Type****

**Solvers**

To fix this, make sure the quantity kind set for the Value Type matches with the quantity kind set for the unit for the same Value Type.

**Example**

**[IMAGE alt='' src='']**

###### The *pascal* Unit quantity kind *pressure* matches with the quantity kind set for the *pressure* Value Type.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ValueType[A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if a value is present for the unit attribute, the quantity kind attribute must be equal to the quantity kind property of the referenced unit.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Value Type<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, make sure the quantity kind set for the Value Type matches with the quantity kind set for the unit for the same Value Type.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_matching_unit_and_QuantityKind.png" /></ac:image><br /></strong></p><h6 style="text-align: center;">The <em>pascal</em> Unit quantity kind <em>pressure</em> matches with the quantity kind set for the <em>pressure</em> Value Type.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684796 space=VR version=11 -->
## PAGE 00204: Invalid No Optional lower multiplicity

- page_id: `17684796`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684796/Invalid+No+Optional+lower+multiplicity
- version_number: 11
- version_date: `2021-02-11T09:54:17.335+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Optional[1]****

**Description**

This validation rule checks to see if the parameter's (without the «optional» stereotype applied) lower value of multiplicityisgreater than zero.

**Severity**

warning****

**Constrained Element**

Parameter****

**Solvers**

To fix this, open the Parameter's Specification window and set the**Multiplicity******property's lower value to greater than zero. ****

**Example**

**[IMAGE alt='' src='']**

###### The *recovered* Parameter multiplicity must be lower be greater than zero. ****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Optional[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule checks to see if the parameter's (<span style="color: rgb(62,63,64);">without the «optional» stereotype applied</span>) lower value of multiplicity </span><span style="color: rgb(62,63,64);">is</span><span style="color: rgb(62,63,64);"> greater than zero.</span></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Parameter<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, open the Parameter's Specification window and set the </span><strong>Multiplicity</strong><span style="color: rgb(62,63,64);"><strong> </strong>property's lower value to greater than zero.</span> <strong> <br /> </strong></p><p><strong>Example</strong></p><p><strong> <ac:image ac:align="center"><ri:attachment ri:filename="parameter_multiplicity.png" /></ac:image> </strong></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">The </span> <em style="text-align: center;">recovered</em> <span> Parameter multiplicity must be <span>lower be greater than zero</span>.</span> <strong> <br /> </strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684798 space=VR version=10 -->
## PAGE 00205: Invalid Optional lower multiplicity

- page_id: `17684798`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684798/Invalid+Optional+lower+multiplicity
- version_number: 10
- version_date: `2021-01-12T14:59:44.272+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Optional[1]****

**Description**

This validation rule checks to see if a parameter's (stereotyped by the «optional») lower value of multiplicityisequal to zero.This means the parameter may not have a value for the activity or any behavior to begin or end execution.

**Severity**

warning****

**Constrained Element**

Parameter****

**Solvers**

To fix this, open the Parameter's Specification window and select the **Multiplicity** property's lower value - equal to zero.

**Example**

[IMAGE alt='' src='']

###### The *recovered* Parameter multiplicity must be lower or equal to zero.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p><strong>Abbreviation</strong></p><p>Optional[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule checks to see if a parameter's (<span style="color: rgb(62,63,64);">stereotyped by the «optional»</span>) lower value of multiplicity </span><span style="color: rgb(62,63,64);">is</span><span style="color: rgb(62,63,64);"> equal to zero. </span>This means the parameter may not have a value for the activity or any behavior to begin or end execution.</p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Parameter<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, open the Parameter's Specification window and select the <strong>Multiplicity</strong> property's lower value - equal to zero.</p><p><strong>Example</strong></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="optional_parameter_multiplicity.png" /></ac:image></p><h6 style="text-align: center;">The <em>recovered</em> Parameter multiplicity must be lower or equal to zero.</h6>
````

<!--NOMAGIC_PAGE id=20845953 space=VR version=1 -->
## PAGE 00206: Invalid owned attribute of Requirement

- page_id: `20845953`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845953/Invalid+owned+attribute+of+Requirement
- version_number: 1
- version_date: `2017-08-21T11:46:57.201+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Requirement[2]****

**Description**

The property owned Attribute must be empty.****

**Severity**

warning****

**Context element**

Requirement****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Requirement[2]<strong><br /></strong></p><p><strong>Description</strong></p><p>The property owned Attribute must be empty.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Requirement<strong> <br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=20845955 space=VR version=1 -->
## PAGE 00207: Invalid owned operation of Requirement

- page_id: `20845955`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845955/Invalid+owned+operation+of+Requirement
- version_number: 1
- version_date: `2017-08-21T11:47:45.916+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Requirement[1]****

**Description**

The property owned Operation must be empty.****

**Severity**

warning****

**Context element**

Requirement****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Requirement[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>The property owned Operation must be empty.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684926 space=VR version=8 -->
## PAGE 00208: Invalid Owner

- page_id: `17684926`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684926/Invalid+Owner
- version_number: 8
- version_date: `2021-02-11T09:49:38.128+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ParticipantProperty[1]****

**Description**

This validation rule checks if only Blocks own properties with «ParticipantProperty»stereotype applied.****

**Severity**

warning****

**Constrained Element**

Participant Property****

**Solvers**

To fix this, apply a «Block»stereotype for the owner of the Participant Property.

**Example**

###### **[IMAGE alt='' src='']**

###### The owner of the Participant Properties is an Association Block.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>ParticipantProperty[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule checks if only Blocks own properties with <span style="color: rgb(62,63,64);">«P</span><span style="color: rgb(62,63,64);">articipantProperty</span><span style="color: rgb(62,63,64);">» </span>stereotype applied.</span><strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Participant Property<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, apply a <span style="color: rgb(62,63,64);">«</span>Block<span style="color: rgb(62,63,64);">» </span>stereotype for the owner of the <span style="color: rgb(62,63,64);">P</span><span style="color: rgb(62,63,64);">articipant Property</span>.</p><p><strong style="letter-spacing: 0.0px;">Example</strong></p><h6><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalidOwner.png" /></ac:image></strong></h6><h6 style="text-align: center;">The owner of the Participant Properties is an Association Block.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684378 space=VR version=8 -->
## PAGE 00209: Invalid owner of DistributedProperty

- page_id: `17684378`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684378/Invalid+owner+of+DistributedProperty
- version_number: 8
- version_date: `2021-02-11T09:48:28.220+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

DistributedProperty[1]****

**Description**

This validation rule checks if the «DistributedProperty» stereotype (and its subtypes) is applied only to properties of classifiers stereotyped by Block or Value Type.****

**Severity**

warning****

**Constrained Element**

Property****

**Solvers**

- Apply «Block» to the owner of this property - applies the « Block » stereotype for the owner of property stereotyped by « DistributedProperty ».
- Apply «ValueType» to the owner of this property - applies the « ValueType » stereotype for the owner of property stereotyped by « DistributedProperty ».

**Example**

**[IMAGE alt='' src='']**

###### The *powerSupply* Part Property is stereotyped by «DistributedProperty» and must be owned by a *Computer* Block but not *Computer* Class.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>DistributedProperty[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the <span style="color: rgb(62,63,64);">«</span>DistributedProperty<span style="color: rgb(62,63,64);">»</span> stereotype (and its subtypes) is applied only to properties of classifiers stereotyped by Block or Value Type.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Property<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Apply <span style="color: rgb(62,63,64);">«</span>Block<span style="color: rgb(62,63,64);">»</span> to the owner of this property </strong>- applies the <span style="color: rgb(62,63,64);">«</span>Block<span style="color: rgb(62,63,64);">»</span> stereotype for the owner of property stereotyped by <span style="color: rgb(62,63,64);">«</span>DistributedProperty<span style="color: rgb(62,63,64);">».</span></li><li><strong>Apply <span style="color: rgb(62,63,64);">«</span>ValueType<span style="color: rgb(62,63,64);">»</span> to the owner of this property </strong>- applies the <span style="color: rgb(62,63,64);">«</span>ValueType<span style="color: rgb(62,63,64);">»</span> stereotype for the owner of property stereotyped by <span style="color: rgb(62,63,64);">«</span>DistributedProperty<span style="color: rgb(62,63,64);">».</span><br /><span style="color: rgb(62,63,64);"><br /></span></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="distributedProperty.png" /></ac:image></strong></p><h6 style="text-align: center;">The <em>powerSupply</em> Part Property is stereotyped by <span style="color: rgb(62,63,64);">«</span>DistributedProperty<span style="color: rgb(62,63,64);">» and must be owned by a <em>Computer</em> Block but not <em>Computer</em> Class.</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684933 space=VR version=9 -->
## PAGE 00210: Invalid Owner Type

- page_id: `17684933`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684933/Invalid+Owner+Type
- version_number: 9
- version_date: `2021-02-02T13:39:05.320+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

PropertySpecificType [B]****

**Description**

This validation rule checks if the property which is typed by the PropertySpecificType is owned by Block or subtypes of Block.

**Severity**

info****

**Constrained Element**

Property****

**Solvers**

To fix this, make sure the property typed by the PropertySpecificTypeis owned by a Block or subtypes of Block.

**Example**

**[IMAGE alt='' src='']**

###### The *arbiter* property is typed by the PropertySpecificType is owned by the *StopWatchTest* Block.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>PropertySpecificType [B]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the property which is typed by the PropertySpecificType is owned by Block or subtypes of Block.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Property<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, make sure the property typed by the PropertySpecificType<span style="color: rgb(62,63,64);"> is owned by a Block or subtypes of Block.</span></p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_owner_type.png" /></ac:image></strong></p><h6 style="text-align: center;">The <em>arbiter</em> property is typed by the PropertySpecificType is owned by the <em>StopWatchTest</em> Block.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684772 space=VR version=13 -->
## PAGE 00211: Invalid parameter type

- page_id: `17684772`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684772/Invalid+parameter+type
- version_number: 13
- version_date: `2021-02-11T09:52:28.889+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ControlOperator[1]****

**Description**

This validationrule checks to see if the behavior or operation has the «ControlOperator» stereotype applied. If yes, thatbehavior or operation must also have at least one parameter typed by the ControlValueKind enumeration.

**Severity**

warning****

**Constrained Element**

Behavior, Operation****

**Solvers**

To fix this, do one of the following:

- Change the type to the ControlValueKind enumeration for the parameter.
- Create a new parameter typed by the ControlValueKind enumeration.

****

**Example**

**[IMAGE alt='' src='']**

###### The getTime behavior and operation with «ControlOperator» stereotype applied have parameters that type must be ControlValueKind enumeration.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>ControlOperator[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This <span style="color: rgb(62,63,64);">validation </span>rule checks to see if the behavior or operation has the «ControlOperator» stereotype applied. If yes, that<span style="color: rgb(62,63,64);"> behavior or operation</span> must also have at least one parameter typed by the ControlValueKind enumeration.</span></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Behavior, Operation<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p>To fix this, do one of the following:</p><ul><li><span style="color: rgb(62,63,64);">Change the type to the ControlValueKind enumeration for the parameter.</span></li><li>Create a new parameter typed by the ControlValueKind enumeration.</li></ul><p><strong><br /> </strong></p><p><strong>Example</strong></p><p><strong> <ac:image ac:align="center"><ri:attachment ri:filename="invalid_parameter_type.png" /></ac:image> </strong></p><h6 style="text-align: center;">The getTime behavior and operation with «ControlOperator» stereotype applied have parameters that type must be ControlValueKind enumeration.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684766 space=VR version=32 -->
## PAGE 00212: Invalid parameter type of Behavior

- page_id: `17684766`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684766/Invalid+parameter+type+of+Behavior
- version_number: 32
- version_date: `2021-01-25T15:07:20.296+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ControlOperator[1]****

**Description**

This validation rule checks if the behavior has the «ControlOperator»stereotype applied. If yes, that behavioralso must have at least one parameter typed by the ControlValueKind enumeration and vice versa.

**Severity**

warning****

**Constrained Element**

Behavior****

**Solvers**

To fix this, do one of the following:

- The behavior which is not typed by the «ControlOperator» stereotype but has a parameter typed by ControlValueKind enumeration:
  - Apply the «ControlOperator» stereotype for the behavior.
  - Delete parameter typed by ControlValueKind enumeration from behavior.
- If the behavior is stereotyped by «ControlOperator» which does not have the parameter typed by ControlValueKind enumeration:
  - Change the type of parameter to ControlValueKind enumeration.
  - Create a new parameter typed by the ControlValueKind enumeration.
  - Remove the «ControlOperator» stereotype from the behavior.

**Example**

[IMAGE alt='' src='']

###### The *out* Parameter type is ControlValueKind enumeration and its *Paint* Activity must be stereotyped by «ControlOperator».

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p><strong>Abbreviation</strong></p><p>ControlOperator[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">This validation rule checks if the behavior has the <span style="color: rgb(62,63,64);">«ControlOperator» </span>stereotype applied. If yes, <span style="color: rgb(62,63,64);">that <span style="color: rgb(62,63,64);">behavior </span></span>also must have at least one parameter typed by the ControlValueKind enumeration and vice versa.</span><br /></span></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Behavior<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><ac:inline-comment-marker ac:ref="c9f72e5b-c2fb-4033-84f6-2f6b3ff5ef38">To fix this, do one of the following:</ac:inline-comment-marker></p><ul><li>The behavior which is not typed by the «ControlOperator» stereotype but has a parameter typed by ControlValueKind enumeration: <ul><li>Apply the «ControlOperator» stereotype for the behavior.</li><li>Delete parameter typed by ControlValueKind enumeration from behavior.</li></ul></li><li> If the behavior is stereotyped by «ControlOperator» which does not have the parameter typed by ControlValueKind enumeration:<ul><li>Change the type of parameter to ControlValueKind enumeration.</li><li>Create a new parameter typed by the ControlValueKind enumeration.</li><li>Remove the «ControlOperator» stereotype from the behavior.<br /><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);"><br /></span></span></li></ul></li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="controlOperator.png" /></ac:image></p><h6 style="text-align: center;">The <em>out</em> Parameter type is <span>ControlValueKind enumeration and its <em>Paint</em> Activity must be stereotyped by <span>«ControlOperator».</span> </span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684770 space=VR version=15 -->
## PAGE 00213: Invalid parameter type of Operation

- page_id: `17684770`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684770/Invalid+parameter+type+of+Operation
- version_number: 15
- version_date: `2021-02-11T09:52:45.481+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ControlOperator[1]****

**Description**

This validation rule checks to if the operation has the «ControlOperator»stereotype applied. If yes,that operationalso must have at least one parameter typed by the ControlValueKind enumeration.****

**Severity**

warning****

**Constrained Element**

Operation****

**Solvers**

To fix this, do one of the following:

- Apply the «ControlOperator» stereotype for the operation that has a parameter typed by the ControlValueKind enumeration.
- Delete the parameter from the Activity (behavior).
- Change the type to the ControlValueKind enumeration for the parameter.
- Create a new parameter typed by the ControlValueKind enumeration.

****

**Example**

**[IMAGE alt='' src='']**

###### The*return*parameter type isControlValueKind enumeration and its *getTime*Operation must be stereotyped by «ControlOperator».****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>ControlOperator[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule checks to if the operation has the <span style="color: rgb(62,63,64);">«ControlOperator» </span>stereotype applied. If yes, </span><span style="color: rgb(62,63,64);">that operation </span><span style="color: rgb(62,63,64);">also must have at least one parameter typed by the ControlValueKind enumeration.</span><strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Operation<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, do one of the following:</p><ul><li>Apply the <span style="color: rgb(62,63,64);">«ControlOperator» stereotype for the operation that has a parameter typed by the ControlValueKind enumeration.</span></li><li>Delete the parameter from the Activity (behavior).</li><li>Change the type to the ControlValueKind enumeration for the parameter.</li><li>Create a new parameter typed by the ControlValueKind enumeration.</li></ul><p><strong><br /></strong></p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="operation_with_controlOperator_stereotype.png" /></ac:image></strong></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">The </span><span style="color: rgb(128,128,128);"><em>return </em></span><span style="color: rgb(128,128,128);">parameter type is </span><span style="color: rgb(128,128,128);">ControlValueKind enumeration and its <em>getTime </em>Operation must be stereotyped by «ControlOperator».</span><strong><br /></strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684929 space=VR version=6 -->
## PAGE 00214: Invalid Part Property type

- page_id: `17684929`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684929/Invalid+Part+Property+type
- version_number: 6
- version_date: `2021-02-11T09:49:53.052+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

PartProperty[A]****

**Description**

This validation rule checks if the type of a Part Property is a Block.****

**Severity**

warning****

**Constrained Element**

Part Property

**Solvers**

To fix this, make sure the type of Part Property is a Block.

**Example**

[IMAGE alt='' src='']

###### The type of Part Property is a Block.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>PartProperty[A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the type of a Part Property is a Block.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Part Property</p><p><strong>Solvers</strong></p><p>To fix this, make sure the type of Part Property is a Block.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="invalid_part_property_type.png" /></ac:image></p><h6 style="text-align: center;">The type of Part Property is a Block.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684935 space=VR version=6 -->
## PAGE 00215: Invalid PropertySpecificType Name

- page_id: `17684935`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684935/Invalid+PropertySpecificType+Name
- version_number: 6
- version_date: `2021-02-11T09:50:13.006+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

PropertySpecificType [2]****

**Description**

This validation rule checks if a classifier stereotyped by the «PropertySpecificType» is unnamed. ****

**Severity**

info****

**Constrained Element**

Classifier****

**Solvers**

To fix this, delete the name of the classifier.

**Example**

**[IMAGE alt='' src='']**

###### The Block stereotyped by the «PropertySpecificType» is unnamed.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>PropertySpecificType [2]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if a classifier stereotyped by the <span style="color: rgb(62,63,64);">«</span><span style="color: rgb(62,63,64);">PropertySpecificType</span><span style="color: rgb(62,63,64);">»</span> is unnamed. <strong><br /></strong></p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Classifier<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, delete the name of the classifier.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="PropertySpecificType_must_be_unnamed.png" /></ac:image></strong></p><h6 style="text-align: center;">The Block stereotyped by the <span style="color: rgb(62,63,64);">«</span><span style="color: rgb(62,63,64);">PropertySpecificType</span><span style="color: rgb(62,63,64);">» is unnamed.</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684939 space=VR version=10 -->
## PAGE 00216: Invalid PropertySpecificType Owner

- page_id: `17684939`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684939/Invalid+PropertySpecificType+Owner
- version_number: 10
- version_date: `2021-02-02T14:14:35.719+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

PropertySpecificType [A]****

**Description**

This validation rule checks if a classifiers with the «PropertySpecificType» («pst») stereotype are owned by the Block which owns the property which is typed by the Property Specific Type.

**Severity**

info****

**Constrained Element**

Property Specific Type****

**Solvers**

To fix this, make sure the classifiers stereotyped by the«PropertySpecificType»(«pst»)is under the same owner as the property which is typed by this classifier.

**Example**

**[IMAGE alt='' src='']**

###### The Block stereotyped by «pst» is owned by the Block which owns the *arbiter* Part Property which is typed by the Property Specific Type.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>PropertySpecificType [A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if a classifiers with the <span style="color: rgb(62,63,64);">«</span><span style="color: rgb(62,63,64);">PropertySpecificType</span><span style="color: rgb(62,63,64);">»</span> («pst») stereotype are owned by the Block which owns the property which is typed by the Property Specific Type. </p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Property Specific Type<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, make sure <span style="color: rgb(62,63,64);">the classifiers stereotyped by the </span><span style="color: rgb(62,63,64);">«</span><span style="color: rgb(62,63,64);">PropertySpecificType</span><span style="color: rgb(62,63,64);">»</span><span style="color: rgb(62,63,64);"> («pst») </span>is under the same owner as the property which is typed by <span style="color: rgb(62,63,64);">this classifier</span>.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_pst_owner.png" /></ac:image></strong></p><h6 style="text-align: center;">The Block stereotyped by «pst» is owned by the Block which owns the <em>arbiter</em> Part Property which is typed by the Property Specific Type.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969540 space=VR version=1 -->
## PAGE 00217: Invalid Redefinition

- page_id: `243969540`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969540/Invalid+Redefinition
- version_number: 1
- version_date: `2025-07-31T10:51:32.171+02:00`
- ancestors: Validation Rules > UML validation rules > UML correctness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

InvRdf****

**Description**

This validation rule checks if a property redefines the inherited property of the owner classifier.

**Severity**

Error

**Constrained Element**

Property, Operation

**Solvers**

To fix this, do one of the following:

- Change the Redefined Property value to the appropriate one that is inherited, not owned.
- Remove Element solver - removes the invalid redefining property from the model.

**Example**

###### [IMAGE alt='' src=''] 
The element *Car* owns two attributes, *wheel* and *type*. The attribute*wheel*redefines the attribute *type*, causing the validation error. 
The error is resolved by changing the *wheel*attribute's **Redefined Property**value to the appropriate one, which is the *wheel*attribute, inherited from the element *Transport*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>InvRdf<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if a property redefines the inherited property of the owner classifier.</p><p><strong>Severity</strong></p><p>Error</p><p><strong>Constrained Element</strong></p><p>Property, Operation</p><p><strong>Solvers</strong></p><p>To fix this, do one of the following:</p><ul><li>Change the <strong>Redefined Property </strong>value to the appropriate one that is inherited, not owned.</li><li><strong>Remove Element</strong> solver -  removes the invalid redefining property from the model.</li></ul><p><strong>Example</strong></p><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="invalid_redefinition.png" /></ac:image><br /><span style="color: rgb(94,108,132);">The element <em>Car</em> owns two attributes, <em>wheel</em> and <em>type</em>. The attribute </span><span style="color: rgb(94,108,132);"><em>wheel</em> </span><span style="color: rgb(94,108,132);">redefines the attribute <em>type</em>, causing the validation error.<br />The error is resolved by changing the <em>wheel </em>attribute's <strong>Redefined Property </strong>value to the appropriate one, which is the <em>wheel </em>attribute, inherited from the element <em>Transport</em></span><span style="color: rgb(94,108,132);">.</span></h6>
````

<!--NOMAGIC_PAGE id=17684947 space=VR version=7 -->
## PAGE 00218: Invalid Reference Property type

- page_id: `17684947`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684947/Invalid+Reference+Property+type
- version_number: 7
- version_date: `2021-02-11T09:50:42.770+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ReferenceProperty[A]****

**Description**

This validation rule checks if the type of a Reference Property is a Block.****

**Severity**

warning****

**Constrained Element**

Reference Property****

**Solvers**

To fix this, specify the Block as a type of the Reference Property.

**Example**

**[IMAGE alt='' src='']**

###### The*cyl* Reference Property is typed by the *Cylinder* Block.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ReferenceProperty[A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the type of a Reference Property is a Block.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Reference Property<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, specify the Block as a type of the Reference Property.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_reference_property_type.png" /></ac:image></strong></p><h6 style="text-align: center;">The<em> cyl</em> Reference Property is typed by the <em>Cylinder</em> Block.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684362 space=VR version=9 -->
## PAGE 00219: Invalid represented element of the activity partition

- page_id: `17684362`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684362/Invalid+represented+element+of+the+activity+partition
- version_number: 9
- version_date: `2021-02-11T09:51:44.095+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Allocations
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

AllocateActivityPartition[B]****

**Description**

This validation rule checks to see if the represented element of the activity partition which is stereotyped «AllocateActivityPartition» is the property**.**

**Severity**

info****

**Constrained Element**

Activity Partition ****

**Solvers**

To fix this, open the Allocate Activity Partition's Specification window and change the **Represents**property value to a property.

**Example**

**[IMAGE alt='' src='']**

###### The represented element of the activity partition with the «AllocateActivityPartition» stereotype applied is the Part Property typed by *Space Telescope* Block.****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>AllocateActivityPartition[B]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks to see if the represented element of the activity partition which is stereotyped «AllocateActivityPartition» is the property<strong>.<br /></strong></p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity Partition <strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, open the Allocate Activity Partition's Specification window and change the <strong>Represents </strong>property value to a property.</p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="AllocatedActivityPartition_property.png" /></ac:image></strong></p><h6 style="text-align: center;">The represented element of the activity partition with the «AllocateActivityPartition» stereotype applied is the Part Property typed by <em>Space Telescope</em> Block.<strong><br /></strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=20845942 space=VR version=1 -->
## PAGE 00220: Invalid return parameter type

- page_id: `20845942`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845942/Invalid+return+parameter+type
- version_number: 1
- version_date: `2017-08-21T11:39:21.863+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

TestCase[1]****

**Description**

The type of return parameter of the stereotyped model element must be VerdictKind. (note: this is consistent with the UML Testing Profile).****

**Severity**

warning****

**Context element**

Behavior****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>TestCase[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>The type of return parameter of the stereotyped model element must be VerdictKind. (note: this is consistent with the UML Testing Profile).<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Behavior<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684965 space=VR version=8 -->
## PAGE 00221: Invalid Shared Property type

- page_id: `17684965`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684965/Invalid+Shared+Property+type
- version_number: 8
- version_date: `2021-02-11T09:51:00.380+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

SharedProperty[A]****

**Description**

This validation rule checks if the type of a Shared Property is a Block.****

**Severity**

warning****

**Constrained Element**

Shared Property

**Solvers**

To fix this, specify the Block as a type of the Shared Property.****

**Example**

###### **[IMAGE alt='' src='']**

###### The type of *powerSupply* Shared Property is a *DC Power Supply* Block.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>SharedProperty[A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the type of a Shared Property is a Block.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Shared Property</p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, specify the Block as a type of the Shared Property.</span><strong><br /></strong></p><p><strong>Example</strong></p><h6><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_shared_property_type.png" /></ac:image></strong></h6><h6 style="text-align: center;">The type of <em>powerSupply</em> Shared Property is a <em>DC Power Supply</em> Block.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=20845936 space=VR version=1 -->
## PAGE 00222: Invalid Slave Requirement text

- page_id: `20845936`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845936/Invalid+Slave+Requirement+text
- version_number: 1
- version_date: `2017-08-21T11:35:14.795+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Copy[2]****

**Description**

The text property of the client requirement is constrained to be a copy of the text property of the supplier requirement.****

**Severity**

warning****

**Context element**

Copy****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Copy[2]<strong><br /></strong></p><p><strong>Description</strong></p><p>The text property of the client requirement is constrained to be a copy of the text property of the supplier requirement.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Copy<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=20845949 space=VR version=1 -->
## PAGE 00223: Invalid source or target of DeriveReqt

- page_id: `20845949`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845949/Invalid+source+or+target+of+DeriveReqt
- version_number: 1
- version_date: `2017-08-21T11:45:04.022+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

DeriveReqt[1] and DeriveReqt[2]****

**Description**

A DeriveReqt dependency may only be created between two classes that have the "requirement" stereotype, or a sub-type of the "requirement" stereotype applied.****

**Severity**

warning****

**Context element**

Derive Requirement****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>DeriveReqt[1] and DeriveReqt[2]<strong><br /></strong></p><p><strong>Description</strong></p><p>A DeriveReqt dependency may only be created between two classes that have the &quot;requirement&quot; stereotype, or a sub-type of the &quot;requirement&quot; stereotype applied.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Derive Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=20845939 space=VR version=1 -->
## PAGE 00224: Invalid stereotype(s) of client/supplier of Copy

- page_id: `20845939`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845939/Invalid+stereotype+s+of+client+supplier+of+Copy
- version_number: 1
- version_date: `2017-08-21T11:36:01.761+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Copy[1]****

**Description**

A Copy dependency may only be created between two classes that have the “requirement” stereotype, or a subtype of the “requirement” stereotype applied.****

**Severity**

warning****

**Context element**

Copy****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Copy[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>A Copy dependency may only be created between two classes that have the “requirement” stereotype, or a subtype of the “requirement” stereotype applied.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Copy<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684415 space=VR version=11 -->
## PAGE 00225: Invalid streaming parameter

- page_id: `17684415`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684415/Invalid+streaming+parameter
- version_number: 11
- version_date: `2021-01-06T06:48:07.815+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

nonStreaming[1]****

**Description**

This validation rulechecks if the Activity stereotyped by «nonStreaming»owns streaming parameters.

**Severity**

warning****

**Constrained Element**

Activity****

**Solvers**

To fix this warning, in the parameters Specification window set the**Is Stream**property value to*false*.

**Example**

**[IMAGE alt='' src='']**

###### The *Paint* non streaming Activity owns *out* non streaming Parameter.

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><p><br /></p><p><strong>Abbreviation</strong></p><p>nonStreaming[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule</span><span style="color: rgb(62,63,64);"> checks if t</span>he Activity stereotyped by <span style="color: rgb(51,51,51);">«</span>nonStreaming<span style="color: rgb(51,51,51);">»</span><span style="color: rgb(62,63,64);"> owns streaming parameters.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this warning, in the <span style="letter-spacing: 0.0px;">parameters Specification window set the </span><strong style="letter-spacing: 0.0px;">Is Stream</strong><span style="letter-spacing: 0.0px;"> property value to </span><em style="letter-spacing: 0.0px;">false</em><span style="letter-spacing: 0.0px;">.</span></p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="nonStreaming_val_rule.png" /></ac:image></strong></p><h6 style="text-align: center;">The <em>Paint</em> non streaming Activity owns <em>out</em> non streaming Parameter.</h6><p><strong><br /></strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684944 space=VR version=9 -->
## PAGE 00226: Invalid typed properties size

- page_id: `17684944`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684944/Invalid+typed+properties+size
- version_number: 9
- version_date: `2021-02-11T09:50:32.947+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

PropertySpecificType [1]****

**Description**

This validation rule checks if a classifier to which the «PropertySpecificType»stereotype is applied is referenced as the type of only one property.****

**Severity**

warning****

**Constrained Element**

Property****

**Solvers**

To fix this, make sure that only one property exists in the model typed by the classifier with «pst» stereotype.

**Example**

**[IMAGE alt='' src='']**

###### Only one property exists in the model typed by the Block with «pst» stereotype.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>PropertySpecificType [1]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if a classifier to which the <span style="color: rgb(62,63,64);">«</span><span style="color: rgb(62,63,64);">PropertySpecificType</span><span style="color: rgb(62,63,64);">» </span>stereotype is applied is referenced as the type of only one property.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Property<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, make sure that only one property exists in the model typed by the classifier with <span style="color: rgb(62,63,64);">«</span>pst<span style="color: rgb(62,63,64);">»</span> stereotype.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="Invalid_typed_properties_size.png" /></ac:image></strong></p><h6 style="text-align: center;">Only one property exists in the model typed by the Block with <span style="color: rgb(62,63,64);">«</span>pst<span style="color: rgb(62,63,64);">»</span> stereotype.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684380 space=VR version=8 -->
## PAGE 00227: Invalid Value Property type

- page_id: `17684380`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684380/Invalid+Value+Property+type
- version_number: 8
- version_date: `2021-02-11T09:48:40.755+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ValueProperty[A]****

**Description**

This validation rule checks if the type of a Value Property is a Value Type.****

**Severity**

warning****

**Constrained Element**

Value Property****

**Solvers**

- Remove ValueProperty stereotype - removes the «ValueProperty » stereotype.
- Change Data Type to Value Type - applies the «ValueType » stereotype for the Data Type that is selected as Value Property type.

**Example**

**[IMAGE alt='' src='']**

###### The*i* Value Property is typed by Value Type instead of Data Type.

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>ValueProperty[A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if the type of a Value Property is a Value Type.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Value Property<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Remove ValueProperty stereotype</strong> - removes the <span style="color: rgb(62,63,64);">«ValueProperty</span><span style="color: rgb(62,63,64);">» </span>stereotype.</li><li><strong>Change Data Type to Value Type</strong> - applies the <span style="color: rgb(62,63,64);">«ValueType</span><span style="color: rgb(62,63,64);">»</span> stereotype for the <span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="d87bac7d-a50b-4c81-9c1f-9383cd3860bc">Data Type</ac:inline-comment-marker></span> that is selected as Value Property type.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="invalid_valueProperty_type.png" /></ac:image></strong></p><h6 style="text-align: center;">The<em> i</em> Value Property is typed by Value Type instead of Data Type.</h6><p><strong><br /></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=267026818 space=VR version=7 -->
## PAGE 00228: InvalidPropertyOwnership

- page_id: `267026818`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/267026818/InvalidPropertyOwnership
- version_number: 7
- version_date: `2025-10-30T12:49:15.407+01:00`
- ancestors: Validation Rules > Systems Cybersecurity Designer validation rules
- labels: []

### NORMALIZED CONTENT

Most properties in an ISO 21434 project can only be owned by certain types of elements. If such a property is inadvertently owned by an element other than the appropriate type, a validation error will appear. That validation error will have the abbreviation **IPO** and a 6a message describing the problem.

**Abbreviation**

IPO

**Message**

'<Element Name>' is not an appropriate owner of the property '<Property Name>'

**Severity**

error

**Context element**

This table shows the appropriate abstract class that owns each such property.

| Abstract | Property |
| --- | --- |
| AbstractCybersecurityAsset | Confidentiality |
| AbstractCybersecurityAsset | Integrity |
| AbstractCybersecurityAsset | Availability |
| AbstractDamageScenario | effect |
| AbstractDamageScenario | failure |
| AbstractDamageScenario | operationalSituation |
| AbstractEffectWithImpact | Safety |
| AbstractEffectWithImpact | Financial |
| AbstractEffectWithImpact | Operational |
| AbstractEffectWithImpact | Privacy |
| AbstractManualAttackPath | AttackFeasibilityRating |
| AbstractThreatScenario | attackPath |
| AbstractThreatScenario | failure |
| AbstractThreatScenario | ResidualSafetyRiskValue |
| AbstractThreatScenario | ResidualFinancialRiskValue |
| AbstractThreatScenario | Residual OperationalRiskValue |
| AbstractThreatScenario | ResidualPrivacyRiskValue |
| AbstractAttackPathISO18045 | Elapsed Time |
| AbstractAttackPathISO18045 | Equipment |
| AbstractAttackPathISO18045 | Expertise |
| AbstractAttackPathISO18045 | Knowledge of TOE |
| AbstractAttackPathISO18045 | Window of Opportunity |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Most properties in an ISO 21434 project can only be owned by certain types of elements.  If such a property is inadvertently owned by an element other than the appropriate type, a validation error will appear.  That validation error will have the abbreviation <strong>IPO</strong> and a 6a message describing the problem. </p><p style="text-align: left;"><strong>Abbreviation</strong></p><p style="text-align: left;">IPO</p><p style="text-align: left;"><strong>Message</strong></p><p style="text-align: left;">'&lt;Element Name&gt;' is not an appropriate owner of the property '&lt;Property Name&gt;'</p><p style="text-align: left;"><strong>Severity</strong></p><p style="text-align: left;">error</p><p style="text-align: left;"><strong>Context element</strong></p><p style="text-align: left;">This table shows the appropriate abstract class that owns each such property.<br /><br /></p><table><tbody class=""><tr class=""><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>Abstract</strong></p></td><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>Property</strong></p></td></tr><tr class=""><td><p>AbstractCybersecurityAsset</p></td><td><p>Confidentiality</p></td></tr><tr class=""><td><p>AbstractCybersecurityAsset</p></td><td><p>Integrity</p></td></tr><tr class=""><td><p>AbstractCybersecurityAsset</p></td><td><p>Availability</p></td></tr><tr class=""><td><p>AbstractDamageScenario</p></td><td><p>effect</p></td></tr><tr class=""><td><p>AbstractDamageScenario</p></td><td><p>failure</p></td></tr><tr class=""><td><p>AbstractDamageScenario</p></td><td><p>operationalSituation</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>Safety</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>Financial</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>Operational</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>Privacy</p></td></tr><tr class=""><td><p>AbstractManualAttackPath</p></td><td><p>AttackFeasibilityRating</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>attackPath</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>failure</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>ResidualSafetyRiskValue</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>ResidualFinancialRiskValue</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>Residual OperationalRiskValue</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>ResidualPrivacyRiskValue</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Elapsed Time</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Equipment</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Expertise</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Knowledge of TOE</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Window of Opportunity</p></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=267026822 space=VR version=9 -->
## PAGE 00229: InvalidValue

- page_id: `267026822`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/267026822/InvalidValue
- version_number: 9
- version_date: `2025-10-30T12:48:57.291+01:00`
- ancestors: Validation Rules > Systems Cybersecurity Designer validation rules
- labels: []

### NORMALIZED CONTENT

Many properties in an ISO 21434 Project must have a specific Value type. If the Value of such a property is not an element of the appropriate type or an enumeration literal of the appropriate enumeration, a validation error will appear. That validation error will have abbreviation **IVV** and a message describing the problem.

**Abbreviation**

IVV

**Message**

Invalid value for '<Property Name>':<Property Value>

**Severity**

error

**Context element**

The following table shows the appropriate Type or Enumeration of the value for each abstract class and property pair.

| AbstractClass | Property | Type of value |
| --- | --- | --- |
| AbstractCybersecurityAsset | Confidentiality | HiMedLoValuation |
| AbstractCybersecurityAsset | Integrity | HiMedLoValuation |
| AbstractCybersecurityAsset | Availability | HiMedLoValuation |
| AbstractDamageScenario | operationalSituation | AbstractOperationalSituation |
| AbstractDamageScenario | failure | UndesiredState |
| AbstractDamageScenario | effect | AutomotiveEffect |
| AbstractEffectWithImpact | SafetyImpact | ImpactRating |
| AbstractEffectWithImpact | FinancialImpact | ImpactRating |
| AbstractEffectWithImpact | OperationalImpact | ImpactRating |
| AbstractEffectWithImpact | PrivacyImpact | ImpactRating |
| AbstractManualAttackPath | AttackFeasibilityRating | HiMedLoFeasibility |
| AbstractThreatScenario | attackPath | AbstractAttackPath |
| AbstractThreatScenario | failure | UndesiredState |
| AbstractThreatScenario | ResidualSafetyRiskValue | Real |
| AbstractThreatScenario | ResidualFinancialRiskValue | Real |
| AbstractThreatScenario | ResidualOperationalRiskValue | Real |
| AbstractThreatScenario | ResidualPrivacyRiskValue | Real |
| AbstractAttackPathISO18045 | Elapsed Time | ElapsedTime |
| AbstractAttackPathISO18045 | Equipment | Equipment |
| AbstractAttackPathISO18045 | Expertise | Expertise |
| AbstractAttackPathISO18045 | Knowledge of TOE | Knowledge of TOE |
| AbstractAttackPathISO18045 | Window of Opportunity | Window of Opportunity |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Many properties in an ISO 21434 Project must have a specific Value type.  If the Value of such a property is not an element of the appropriate type or an enumeration literal of the appropriate enumeration, a validation error will appear. That validation error will have abbreviation <strong>IVV</strong> and a message describing the problem. </p><p style="text-align: left;"><strong>Abbreviation</strong></p><p style="text-align: left;">IVV</p><p style="text-align: left;"><strong>Message</strong></p><p style="text-align: left;">Invalid value for '&lt;Property Name&gt;':&lt;Property Value&gt;</p><p style="text-align: left;"><strong>Severity</strong></p><p style="text-align: left;">error</p><p style="text-align: left;"><strong>Context element</strong></p><p>The following table shows the appropriate Type or Enumeration of the value for each abstract class and property pair.<br /><br /></p><table><tbody class=""><tr class=""><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>AbstractClass</strong></p></td><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>Property</strong></p></td><td class="highlight-#f4f5f7" data-highlight-colour="#f4f5f7"><p title=""><strong>Type of value</strong></p></td></tr><tr class=""><td><p>AbstractCybersecurityAsset</p></td><td><p>Confidentiality</p></td><td><p>HiMedLoValuation</p></td></tr><tr class=""><td><p>AbstractCybersecurityAsset</p></td><td><p>Integrity</p></td><td><p>HiMedLoValuation</p></td></tr><tr class=""><td><p>AbstractCybersecurityAsset</p></td><td><p>Availability</p></td><td><p>HiMedLoValuation</p></td></tr><tr class=""><td><p>AbstractDamageScenario</p></td><td><p>operationalSituation</p></td><td><p>AbstractOperationalSituation</p></td></tr><tr class=""><td><p>AbstractDamageScenario</p></td><td><p>failure</p></td><td><p>UndesiredState</p></td></tr><tr class=""><td><p>AbstractDamageScenario</p></td><td><p>effect</p></td><td><p>AutomotiveEffect</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>SafetyImpact</p></td><td><p>ImpactRating</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>FinancialImpact</p></td><td><p>ImpactRating</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>OperationalImpact</p></td><td><p>ImpactRating</p></td></tr><tr class=""><td><p>AbstractEffectWithImpact</p></td><td><p>PrivacyImpact</p></td><td><p>ImpactRating</p></td></tr><tr class=""><td><p>AbstractManualAttackPath</p></td><td><p>AttackFeasibilityRating</p></td><td><p>HiMedLoFeasibility</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>attackPath</p></td><td><p>AbstractAttackPath</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>failure</p></td><td><p>UndesiredState</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>ResidualSafetyRiskValue</p></td><td><p>Real</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>ResidualFinancialRiskValue</p></td><td><p>Real</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>ResidualOperationalRiskValue</p></td><td><p>Real</p></td></tr><tr class=""><td><p>AbstractThreatScenario</p></td><td><p>ResidualPrivacyRiskValue</p></td><td><p>Real</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Elapsed Time</p></td><td><p>ElapsedTime</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Equipment</p></td><td><p>Equipment</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Expertise</p></td><td><p>Expertise</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Knowledge of TOE</p></td><td><p>Knowledge of TOE</p></td></tr><tr class=""><td><p>AbstractAttackPathISO18045</p></td><td><p>Window of Opportunity</p></td><td><p>Window of Opportunity</p></td></tr></tbody></table>
````

<!--NOMAGIC_PAGE id=165249328 space=VR version=2 -->
## PAGE 00230: Item Flow has no Conveyed Items

- page_id: `165249328`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/165249328/Item+Flow+has+no+Conveyed+Items
- version_number: 2
- version_date: `2024-04-18T17:03:04.454+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Ports and Flows
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

IFHNCI[2]

**Description**

This validation rule checks if there are anyItem Flows without Conveyed Items.

**Severity**

warning****

**Constrained Element**

Item Flow

**Solvers**

- **Select Conveyed Item** - opens the Select Conveyed Information dialog where you can choose the Conveyed Item for the validated Item Flow.

**Example**

**[IMAGE alt='' src='']**

###### An Item Flow has no Conveyed Item. The error is resolved by specifying a Conveyed Item via the **Select Conveyed Item**solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p><span style="color: rgb(23,43,77);">IFHNCI</span><span class="error" style="color: rgb(23,43,77);">[2]</span></p><p><strong>Description</strong></p><p>This validation rule checks if <span style="letter-spacing: 0.0px;">there are any </span><span style="color: rgb(23,43,77);">Item Flows without Conveyed Items.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Item Flow</p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Select Conveyed Item</strong> - <span style="color: rgb(23,43,77);">opens the Select Conveyed Information dialog where you can choose the Conveyed Item for the validated Item Flow.</span></span></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><strong><ac:image><ri:attachment ri:filename="Item_Flow_has_no_Conveyed_Items.png" /></ac:image><br /></strong></p><h6 style="text-align: center;">An Item Flow has no Conveyed Item. The error is resolved by specifying a Conveyed Item via the <strong>Select Conveyed Item </strong>solver.</h6>
````

<!--NOMAGIC_PAGE id=243969492 space=VR version=1 -->
## PAGE 00231: Mandatory Tagged Value

- page_id: `243969492`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969492/Mandatory+Tagged+Value
- version_number: 1
- version_date: `2025-07-31T10:51:30.758+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

LackOfTagVal

**Description**

This validation rule checks that if the stereotype's tag definition multiplicity is 1, only one value to a slot is allowed.

**Severity**

warning

**Constrained Element**

Element

**Solvers**

- To fix this, make sure the tag has exactly 1 value.

**Example**

[IMAGE alt='' src='']

###### The *Car*stereotype contains a tag definition *gearTransmission*with the multiplicity set to one. The class *Sedan*with the applied stereotype *Car*does not have the *gearTransmission*tag specified with a value, which causes an error. 
The error is resolved by specifying the *gearTransmission*tag with a value.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>LackOfTagVal</p><p><strong>Description</strong></p><p>This validation rule checks that if the stereotype's <ac:inline-comment-marker ac:ref="3e14238d-efa6-4400-84e7-8fcaa3e3a05b">tag definition</ac:inline-comment-marker> multiplicity is 1, only one value to a slot is allowed.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Element</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the tag has exactly 1 value.<strong> </strong></li></ul><p><strong><ac:inline-comment-marker ac:ref="96d08a8d-61b6-4fb5-9ed4-dd630b18b829">Example</ac:inline-comment-marker></strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Mandatory Tagged Value.png" /></ac:image></p><h6 style="text-align: center;">The <em>Car </em>stereotype contains a tag definition <em>gearTransmission </em>with the multiplicity set to one. The class <em>Sedan </em>with the applied stereotype <em>Car </em>does not have the <em>gearTransmission </em>tag specified with a value, which causes an error.<br />The error is resolved by specifying the <em>gearTransmission </em>tag with a value.</h6>
````

<!--NOMAGIC_PAGE id=243969496 space=VR version=1 -->
## PAGE 00232: Metamodel Reference

- page_id: `243969496`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969496/Metamodel+Reference
- version_number: 1
- version_date: `2025-07-31T10:51:30.880+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ProfMeta

**Description**

This validation rule checks if a Profile has a metamodel reference.

**Severity**

warning

**Constrained Element**

Profile

**Solvers**

- To fix this, recreate the Profile to make sure it has a metamodel reference.

**Example**

[IMAGE alt='' src='']

###### The Profile *Prototype* does not have a metamodel reference. The error is resolved by recreating the Profile.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ProfMeta</p><p><strong>Description</strong></p><p>This validation rule checks if a Profile has a metamodel reference.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Profile</p><p><strong>Solvers</strong></p><ul><li><ac:inline-comment-marker ac:ref="571b51b2-3012-4df4-991a-e44744e60ccb">To fix this, recreate the Profile to make sure it has a metamodel reference.</ac:inline-comment-marker> </li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Metamodel_Reference.png" /></ac:image></p><h6 style="text-align: center;">The Profile <em>Prototype</em> does not have a metamodel reference. The error is resolved by recreating the Profile.</h6>
````

<!--NOMAGIC_PAGE id=17684364 space=VR version=7 -->
## PAGE 00233: Missing allocation dependency

- page_id: `17684364`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684364/Missing+allocation+dependency
- version_number: 7
- version_date: `2021-02-11T09:51:55.051+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Allocations
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

AllocateActivityPartition [A]****

**Description**

This rule checks to see if an Action appearing in an Allocate Activity Partition is the client (from) an end of an Allocate relationship. Also, it checks to see if the element that represents the Allocate Activity Partition is the supplier (to) end of the same Allocate relationship.

**Severity**

info****

**Constrained Element**

Action****

**Solvers**

To fix this, do one of the following:

- Open the Action's Specification window, click the Relations property group and create an outgoing Allocate relationship with the element that represents the Allocate Activity Partition.
- Open the Part Property's or Block's (the element that represents the Allocate Activity Partition) Specification window, click the Relations property group, and create an incoming Allocate relationship with the Action.

**Example**

**[IMAGE alt='' src='']**

###### The Allocate relationship is created between *Take photos* Action and Part Property typed by Space Telescope that represents the Allocate Activity Partition.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>AllocateActivityPartition [A]<strong><br /></strong></p><p><strong>Description</strong></p><p>This rule checks to see if an Action appearing in an Allocate Activity Partition is the client (from) an end of an Allocate relationship. Also, it checks to see if the element that represents the Allocate Activity Partition is the supplier (to) end of the same Allocate relationship.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Action<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, do one of the following:</p><ul><li>Open the Action's Specification window, click the <strong>Relations</strong> property group and create an outgoing Allocate relationship with the element that represents the Allocate Activity Partition.</li><li>Open the Part Property's or Block's (the element that represents the Allocate Activity Partition) Specification window, click the <strong>Relations</strong> property group, and create an incoming Allocate relationship with the Action.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="allocate_dependency.png" /></ac:image></strong></p><h6 style="text-align: center;">The Allocate relationship is created between <em>Take photos</em> Action and Part Property typed by Space Telescope that represents the Allocate Activity Partition.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684368 space=VR version=6 -->
## PAGE 00234: Missing Block stereotype

- page_id: `17684368`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684368/Missing+Block+stereotype
- version_number: 6
- version_date: `2021-01-11T10:24:37.456+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Block[8]****

**Description**

This validation rule checks if a classifier which specializes a Block is also have the «Block»stereotype or one of its specializations applied.

**Severity**

info****

**Constrained Element**

Class****

**Solvers**

To fix this, do one of the following:

- Apply «Block»stereotype for an element which base classifier is stereotyped by a «Block».
- Open element's Specification window and in the Base Classifier property select any element except a Block or leave it empty.

**Example**

**[IMAGE alt='' src='']**

###### The Block stereotype must be applied for a *Wheel* since its base classifier is stereotyped by a Block.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Block[8]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if a classifier which specializes a Block is also have the <span style="color: rgb(62,63,64);">«Block</span><span style="color: rgb(62,63,64);">» </span>stereotype or one of its specializations applied.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Class<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, do one of the following:</p><ul><li><p>Apply <span style="color: rgb(62,63,64);">«Block</span><span style="color: rgb(62,63,64);">» </span>stereotype for an element which base classifier is stereotyped by a <span style="color: rgb(62,63,64);">«Block</span><span style="color: rgb(62,63,64);">»</span>.</p></li><li>Open element's Specification window and in the <strong>Base Classifier</strong> property select any element except a Block or leave it empty.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="missing_block_stereotype.png" /></ac:image></strong></p><h6 style="text-align: center;">The Block stereotype must be applied for a <em>Wheel</em> since its base classifier is stereotyped by a Block.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684774 space=VR version=11 -->
## PAGE 00235: Missing ControlOperator stereotype

- page_id: `17684774`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684774/Missing+ControlOperator+stereotype
- version_number: 11
- version_date: `2021-02-11T09:53:07.811+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ControlOperator[2]****

**Description**

This validation rule checks to see if: 1) a behavior has the «ControlOperator» stereotype applied; 2) that it is set as a method for an operation, which is typed by that behavior; and 3) is also stereotyped bythe «ControlOperator».

**Severity**

warning****

**Constrained Element**

Behavior, Operation****

**Solvers**

To fix this, applythe «ControlOperator» stereotype for the behavior that is set as a method of an operation with the «ControlOperator» stereotype applied. ****

**Example**

[IMAGE alt='' src='']

###### The *getTime* Activity is a method of operation that is stereotyped by «ControlOperator».

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>ControlOperator[2]<strong> <br /> </strong></p><p><strong>Description</strong></p><p>This validation rule checks to see if: 1) a behavior has the «ControlOperator» stereotype applied; 2) that it is set as a method for an <span style="color: rgb(62,63,64);">operation, which is typed by that behavior; and 3) is also stereotyped by </span><span class="ic-current-selection" style="color: rgb(62,63,64);">the «ControlOperator».</span></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Behavior, Operation<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, apply </span>the <span style="color: rgb(62,63,64);">«ControlOperator» stereotype for the behavior that is set as a method of an operation with the «ControlOperator» stereotype applied.</span> <strong> <br /> </strong></p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="method.png" /></ac:image></p><h6 style="text-align: center;">The <em>getTime</em> Activity is a method of operation that is stereotyped by <span>«ControlOperator».</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684802 space=VR version=7 -->
## PAGE 00236: Missing Probability stereotype

- page_id: `17684802`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684802/Missing+Probability+stereotype
- version_number: 7
- version_date: `2021-02-11T09:54:46.167+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Probability[2]****

**Description**

This validation rule checks to see if the «probability» stereotype is applied to all edges coming out of the same source when the «probability» stereotype is applied to an activity edge.****

**Severity**

warning****

**Constrained Element**

Activity Edge****

**Solvers**

To fix this, apply the «probability» stereotype to all edges coming out of the same source.

**Example**

**[IMAGE alt='' src='']**

###### Both Control Flows that come out of the same source must be stereotyped by the «probability».

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Probability[2]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks to see if the «probability» stereotype is applied to all edges coming out of the same source when the «probability» stereotype is applied to an activity edge.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity Edge<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, apply the «probability» stereotype to all edges coming out of the same source.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="probability_on_activity_edge.png" /></ac:image></strong></p><h6 style="text-align: center;">Both Control Flows that come out of the same source must be stereotyped by the  «probability».</h6><p><strong><br /></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=20845945 space=VR version=1 -->
## PAGE 00237: Missing Recursive copy of sub-requirement

- page_id: `20845945`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845945/Missing+Recursive+copy+of+sub-requirement
- version_number: 1
- version_date: `2017-08-21T11:41:22.969+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Copy[C]****

**Description**

If the supplier requirement has sub requirements, copies of the sub requirements are made recursively in the context of the client requirement and Copy dependencies are created between each sub requirement and the associated copy.****

**Severity**

info****

**Context element**

Copy****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Copy[C]<strong><br /></strong></p><p><strong>Description</strong></p><p>If the supplier requirement has sub requirements, copies of the sub requirements are made recursively in the context of the client requirement and Copy dependencies are created between each sub requirement and the associated copy.<strong><br /></strong></p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Context element</strong></p><p>Copy<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=20845957 space=VR version=1 -->
## PAGE 00238: Missing requirement stereotype

- page_id: `20845957`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845957/Missing+requirement+stereotype
- version_number: 1
- version_date: `2017-08-21T11:48:39.150+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Requirement[5]****

**Description**

A nested classifier of a class stereotyped by «requirement» must also be stereotyped by «requirement».****

**Severity**

warning****

**Context element**

Classifier****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Requirement[5]<strong><br /></strong></p><p><strong>Description</strong></p><p>A nested classifier of a class stereotyped by «requirement» must also be stereotyped by «requirement».<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Classifier<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684417 space=VR version=7 -->
## PAGE 00239: Missing streaming parameter

- page_id: `17684417`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684417/Missing+streaming+parameter
- version_number: 7
- version_date: `2021-01-06T12:10:14.385+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

streaming[1]****

**Description**

This validation rulechecks if the Activity stereotyped by«streaming»owns at least one parameter that is streaming.

**Severity**

warning****

**Constrained Element**

Activity****

**Solvers**

To fix this warning, do one of the following:

- If the parameter is created for the streaming Activity, in the parameters Specification window set the Is Stream property value to true .
- If any of parameters are not created for the streaming Activity, create it.

**Example**

**[IMAGE alt='' src='']**

###### The streaming *dry part* Activity owns streaming *in* Parameter.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>streaming[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks if t</span><span style="color: rgb(62,63,64);">he Activity stereotyped by </span><span style="color: rgb(51,51,51);">«s</span><span style="color: rgb(62,63,64);">treaming</span><span style="color: rgb(51,51,51);">»</span><span style="color: rgb(62,63,64);"> owns at least one parameter that is streaming.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity<strong><br /></strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this warning, do one of the following:</span></p><ul><li><span style="color: rgb(62,63,64);">If the parameter is created <span style="color: rgb(62,63,64);">for the streaming Activity</span>, in the </span><span style="color: rgb(62,63,64);">parameters Specification window set the </span><strong>Is Stream</strong><span style="color: rgb(62,63,64);"> property value to </span><em>true</em><span style="color: rgb(62,63,64);">.</span><strong><br class="_mce_tagged_br" /></strong></li><li><span style="color: rgb(62,63,64);">If any of parameters are not created for the streaming Activity, create it.</span></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="missing_streaming_parameter.png" /></ac:image></strong></p><h6 style="text-align: center;">The streaming <em>dry part</em> Activity owns streaming <em>in</em> Parameter.</h6></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684385 space=VR version=10 -->
## PAGE 00240: Missing Value Type stereotype

- page_id: `17684385`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684385/Missing+Value+Type+stereotype
- version_number: 10
- version_date: `2021-02-11T09:49:00.236+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Blocks
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ValueType[1]****

**Description**

This validation rule checks if any classifier which specializes (has generalization relationship to) a Value Type also have the «ValueType» stereotype applied.****

**Severity**

warning****

**Constrained Element**

DataType****

**Solvers**

- Apply the corresponding Value Type stereotype and/or its subtype(s) to itself - applies the «V alueType » stereotype.

**Example**

**[IMAGE alt='' src='']**

###### The *Actions* Data Type must be stereotyped by «valueType».

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>ValueType[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><ac:inline-comment-marker ac:ref="b3284607-8ae2-46ca-ab29-e9fd17388612">This validation rule checks if any classifier which specializes (has generalization relationship to) a Value Type</ac:inline-comment-marker> also have the <span style="color: rgb(62,63,64);">«V</span>alueType<span style="color: rgb(62,63,64);">»</span> stereotype applied.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><ac:inline-comment-marker ac:ref="2bb6e78c-ac21-4c40-b625-49466d0bb9b0">DataType</ac:inline-comment-marker><strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Apply the corresponding Value Type stereotype and/or its subtype(s) to itself</strong> - applies the <span style="color: rgb(62,63,64);">«V</span>alueType<span style="color: rgb(62,63,64);">»</span> stereotype.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="missing_value_type_stereotype.png" /></ac:image></strong></p><h6 style="text-align: center;">The <em>Actions</em> Data Type must be stereotyped by <span style="color: rgb(62,63,64);">«</span>valueType<span style="color: rgb(62,63,64);">».</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969498 space=VR version=1 -->
## PAGE 00241: Multiple Slot Values

- page_id: `243969498`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969498/Multiple+Slot+Values
- version_number: 1
- version_date: `2025-07-31T10:51:31.003+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

SlotValAccMult

**Description**

This validation rule checks if more than one Slot Value is defined. If the Defining Feature multiplicity is 1, only one value for the Slot is allowed.

**Severity**

warning

**Constrained Element**

Slot

**Solvers**

- To fix this, make sure the Slot has only one value.

**Example**

[IMAGE alt='' src='']

###### The Enumeration element *Car Models* has the *Doors*property with the multiplicity set to 1 and Enumeration Literals that inherit that property as a Slot Value. The Enumeration Literal *Coupe* has the Slot *Doors* specified with 2 values (4 and 2), which causes an error since the property *Doors* has the multiplicity of 1, allowing it to have only one value for the Slot. 
The error is resolved by removing one of the Slot Values.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>SlotValAccMult</p><p><strong>Description</strong></p><p>This validation rule checks if more than one Slot Value is defined. If the Defining Feature multiplicity is 1, only one value for the Slot is allowed.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Slot</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the Slot has only one value.<strong> </strong></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Multiple_Slot_Values.png" /></ac:image></p><h6 style="text-align: center;">The Enumeration element <em>Car Models</em> has the <em>Doors </em>property with the multiplicity set to 1 and Enumeration Literals that inherit that property as a Slot Value. The Enumeration Literal <em>Coupe</em> has the Slot <em>Doors</em> specified with 2 values (4 and 2), which causes an error since the property <em>Doors</em> has the multiplicity of 1, allowing it to have only one value for the Slot. <br />The error is resolved by removing one of the Slot Values. </h6>
````

<!--NOMAGIC_PAGE id=243969500 space=VR version=1 -->
## PAGE 00242: Multiple Tagged Values

- page_id: `243969500`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969500/Multiple+Tagged+Values
- version_number: 1
- version_date: `2025-07-31T10:51:31.050+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

TagValAccMult

**Description**

This validation rule checks if a tag has more than one value defined. If the stereotype's tag definition multiplicity is 1, only one value is allowed for a Tagged Value.

**Severity**

warning

**Constrained Element**

TaggedValue

**Solvers**

- To fix this, make sure the number of values defined for a tag does not exceed the number defined for the stereotype's tag definition multiplicity.

**Example**

[IMAGE alt='' src='']

###### The *Car*stereotype contains a tag definition *gearTransmission*with the multiplicity set to one. The class *Sedan*with the applied stereotype *Car*has the *gearTransmission*tag specified with two values, which causes an error.The error is resolved by removing one of the values.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>TagValAccMult</p><p><strong>Description</strong></p><p>This validation rule checks if a tag has more than one value defined. If the <ac:inline-comment-marker ac:ref="ce60265f-6d2e-45ab-beef-aad73eae34fa">stereotype's tag definition</ac:inline-comment-marker> multiplicity is 1, only one value is allowed for a Tagged Value.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>TaggedValue</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the number of values defined for a tag does not exceed the number defined for the stereotype's tag definition multiplicity.</li></ul><p><strong><ac:inline-comment-marker ac:ref="ba8c4c6d-7086-428a-b609-d167f6f6b768">Example</ac:inline-comment-marker></strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Multiple Tagged Values.png" /></ac:image></p><h6 style="text-align: center;">The <em>Car </em>stereotype contains a tag definition <em>gearTransmission </em>with the multiplicity set to one. The class <em>Sedan </em>with the applied stereotype <em>Car </em>has the <em style="letter-spacing: 0.0px;">gearTransmission</em><span style="letter-spacing: 0.0px;"> tag specified with two values, which causes an error.<br /></span>The error is resolved by removing one of the values.</h6>
````

<!--NOMAGIC_PAGE id=243969503 space=VR version=1 -->
## PAGE 00243: Nameless Actor

- page_id: `243969503`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969503/Nameless+Actor
- version_number: 1
- version_date: `2025-07-31T10:51:31.104+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ActNmIsDef

**Description**

This validation rule checks if Actors are named.

**Severity**

error

**Constrained Element**

Actor

**Solvers**

- To fix this, make sure Actors are named.

**Example**

[IMAGE alt='' src='']

###### The diagram contains a nameless Actor. The error is resolved by naming the Actor.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ActNmIsDef</p><p><strong>Description</strong></p><p>This validation rule checks if Actors are named.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Actor</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure Actors are named.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Nameless_Actor.png" /></ac:image></p><h6 style="text-align: center;">The diagram contains a nameless Actor. The error is resolved by naming the Actor.</h6>
````

<!--NOMAGIC_PAGE id=243969505 space=VR version=1 -->
## PAGE 00244: Nameless Attribute

- page_id: `243969505`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969505/Nameless+Attribute
- version_number: 1
- version_date: `2025-07-31T10:51:31.145+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

AtrNmIsDef

**Description**

This validation rule checks if Attributes are named.

**Severity**

info

**Constrained Element**

Property

**Solvers**

- To fix this, make sure the Attributes are named.

**Example**

[IMAGE alt='' src='']

###### The Part Property typed by the Block *VCCU* is nameless. The error is resolved by naming the Part Property.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>AtrNmIsDef</p><p><strong>Description</strong></p><p>This validation rule checks if Attributes are named.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained Element</strong></p><p>Property</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the Attributes are named.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Nameless_Attribute.png" /></ac:image></p><h6 style="text-align: center;">The Part Property typed by the Block <em>VCCU</em> is nameless. The error is resolved by naming the Part Property.</h6>
````

<!--NOMAGIC_PAGE id=243969507 space=VR version=1 -->
## PAGE 00245: Nameless Class

- page_id: `243969507`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969507/Nameless+Class
- version_number: 1
- version_date: `2025-07-31T10:51:31.187+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ClsNmIsDef

**Description**

This validation rule checks if Classes are named.

**Severity**

error

**Constrained Element**

Class

**Solvers**

- To fix this, make sure the Classes are named.

**Example**

[IMAGE alt='' src='']

###### The diagram contains three Classes, one of which is nameless. The error is resolved by naming the Class.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ClsNmIsDef</p><p><strong>Description</strong></p><p>This validation rule checks if Classes are named.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Class</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the Classes are named.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Nameless_Class.png" /></ac:image></p><h6 style="text-align: center;">The diagram contains three Classes, one of which is nameless. The error is resolved by naming the Class.</h6>
````

<!--NOMAGIC_PAGE id=243969509 space=VR version=1 -->
## PAGE 00246: Nameless Operation

- page_id: `243969509`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969509/Nameless+Operation
- version_number: 1
- version_date: `2025-07-31T10:51:31.234+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

OpNmIsDef

**Description**

This validation rule checks if Operations are named.

**Severity**

error

**Constrained Element**

Operation

**Solvers**

- To fix this, make sure Operations are named.

**Example**

[IMAGE alt='' src='']

###### Block *Cooling*has a nameless Operation. The error is resolved by naming the Operation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>OpNmIsDef</p><p><strong>Description</strong></p><p>This validation rule checks if Operations are named.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Operation</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure Operations are named.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Nameless_Operation.png" /></ac:image></p><h6 style="text-align: center;">Block <em>Cooling </em>has a nameless Operation. The error is resolved by naming the Operation.</h6>
````

<!--NOMAGIC_PAGE id=243969511 space=VR version=1 -->
## PAGE 00247: No Activity Incoming Edge

- page_id: `243969511`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969511/No+Activity+Incoming+Edge
- version_number: 1
- version_date: `2025-07-31T10:51:31.290+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ActIncEdg

**Description**

This validation rule checks if an Activity should have Incoming Edges: Control Flows or Object Flows.

**Severity**

warning

**Constrained Element**

ActivityNode

**Solvers**

- To fix this, make sure an Activity has Incoming Edges: Control Flows or Object Flows.

**Example**

[IMAGE alt='' src='']

###### Activity Final Node has no Incoming Edge. The error is resolved by creating a Control Flow between the Call Behavior Action and the Activity Final Node.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ActIncEdg</p><p><strong>Description</strong></p><p>This validation rule checks if an Activity should have Incoming Edges: Control Flows or Object Flows.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>ActivityNode</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure an Activity has Incoming Edges: Control Flows or Object Flows.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Activity_Incoming_Edge.png" /></ac:image></p><h6 style="text-align: center;">Activity Final Node has no Incoming Edge. The error is resolved by creating a Control Flow between the Call Behavior Action and the Activity Final Node.</h6>
````

<!--NOMAGIC_PAGE id=243969513 space=VR version=1 -->
## PAGE 00248: No Activity Outgoing Edge

- page_id: `243969513`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969513/No+Activity+Outgoing+Edge
- version_number: 1
- version_date: `2025-07-31T10:51:31.339+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ActOutEdg

**Description**

This validation rule checks if an Activity should have Outgoing Edges: Control Flows or Object Flows.

**Severity**

warning

**Constrained Element**

ActivityNode

**Solvers**

- To fix this, make sure an Activity has Outgoing Edges: Control Flows or Object Flows.

**Example**

[IMAGE alt='' src='']

###### Call Behavior Action has no Outgoing Edge. The error is resolved by creating a Control Flow between the Call Behavior Action and the Activity Final Node.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ActOutEdg</p><p><strong>Description</strong></p><p>This validation rule checks if an Activity should have Outgoing Edges: Control Flows or Object Flows.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>ActivityNode</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure an Activity has Outgoing Edges: Control Flows or Object Flows.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Activity_Outgoing_Edge.png" /></ac:image></p><h6 style="text-align: center;">Call Behavior Action has no Outgoing Edge. The error is resolved by creating a Control Flow between the Call Behavior Action and the Activity Final Node.</h6>
````

<!--NOMAGIC_PAGE id=243969515 space=VR version=1 -->
## PAGE 00249: No Association Multiplicity

- page_id: `243969515`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969515/No+Association+Multiplicity
- version_number: 1
- version_date: `2025-07-31T10:51:31.390+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

MltIsDef

**Description**

This validation rule checks if the multiplicity for the ends of an Association is not specified. The default one (if unspecified) is 1.

**Severity**

info

**Constrained Element**

Association

**Solvers**

- To fix this, make sure the multiplicity for the ends of an Association is specified.

**Example**

[IMAGE alt='' src='']

###### The Association ends between the Block *VCCU* and the Block *Heating*does not have its multiplicity specified. The error is resolved by specifying the multiplicity for the ends of an Association.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>MltIsDef</p><p><strong>Description</strong></p><p>This validation rule checks if the <span style="color: rgb(62,63,64);">multiplicity for the ends of an Association</span> is not specified. The default one (if unspecified) is 1.</p><p><strong>Severity</strong></p><p>info</p><p><strong>Constrained Element</strong></p><p>Association</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the multiplicity for the ends of an Association is specified.<strong> </strong></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Association_Multiplicity.png" /></ac:image></p><h6 style="text-align: center;">The Association ends between the Block <em>VCCU</em> and the Block <em>Heating </em>does not have its multiplicity specified. The error is resolved by specifying the multiplicity for the ends of an Association.</h6>
````

<!--NOMAGIC_PAGE id=243969517 space=VR version=1 -->
## PAGE 00250: No Classifier for Instance

- page_id: `243969517`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969517/No+Classifier+for+Instance
- version_number: 1
- version_date: `2025-07-31T10:51:31.446+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

InstClsfIsDef

**Description**

This validation rule checks if Instances have the Classifier specified.

**Severity**

error

**Constrained Element**

Instance Specification

**Solvers**

- To fix this, make sure that Instances have the Classifier specified.

**Example**

[IMAGE alt='' src='']

###### The Instance Specification *SUV_R* does not have a Classifier specified. The error is resolved by specifying the Classifier.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>InstClsfIsDef</p><p><strong>Description</strong></p><p>This validation rule checks if Instances have the Classifier specified.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Instance Specification</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure that Instances have the Classifier specified.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Classifier_for_Instance.png" /></ac:image></p><h6 style="text-align: center;">The Instance Specification <em>SUV_R</em> does not have a Classifier specified. The error is resolved by specifying the Classifier.</h6>
````

<!--NOMAGIC_PAGE id=81100899 space=VR version=17 -->
## PAGE 00251: No compatible Connector

- page_id: `81100899`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/81100899/No+compatible+Connector
- version_number: 17
- version_date: `2021-09-14T13:14:15.169+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Behavior to Structure Synchronization
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

BehaviorToStructureSync[2]

**Description**

This validation rule checks to see if the Connector exists between the two compatible Proxy Ports that can exchange flowing items found in Activities.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

**Create Connector** - creates a missing Connector between the two compatible Proxy Ports.

**Example**

**[IMAGE alt='' src='']**

###### Creating a Connector that is missing in the Internal Block Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>BehaviorToStructureSync[2]</p><p><strong>Description</strong></p><p>This validation rule checks to see if the Connector exists between the two compatible Proxy Ports that can exchange flowing items found in Activities. </p><p><strong style="letter-spacing: 0.0px;">Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Create Connector</strong> - creates a missing Connector between the two compatible Proxy Ports. </p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="btos_2nd_validation_rule.png" /></ac:image></strong></p><h6 style="text-align: center;">Creating a Connector that is missing in the Internal Block Diagram.</h6>
````

<!--NOMAGIC_PAGE id=70390264 space=VR version=17 -->
## PAGE 00252: No compatible Interface

- page_id: `70390264`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/70390264/No+compatible+Interface
- version_number: 17
- version_date: `2021-09-10T09:56:42.390+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Behavior to Structure Synchronization
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

BehaviorToStructureSync[1]

**Description**

This validation rule detects the Part Properties or containing Blocks of Part Properties having incompatible interfaces in accordance with the flowing items specified in Activities.****

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Create Port - creates a new Proxy Port typed by a compatible Interface Block.
- Choose Compatible Interface Block - changes an already existing Proxy Port type to a compatible Interface Block.
- Add Missing Flow Property - adds a new Flow Property to an Interface Block that types a Proxy Port.
- Reverse Direction of Port - changes the Proxy Port direction, thus changing the Flow Property direction of an Interface Block that types a Proxy Port.

**Example**

**[IMAGE alt='' src='']**

###### Part Property*: Power* and the enclosing Block*Wireless Earbuds* after using Behavior to Structure Synchronization solvers.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>BehaviorToStructureSync[1]</p><p><strong><ac:inline-comment-marker ac:ref="7216feb7-efde-4071-86ed-30df4d49b0fe">Description</ac:inline-comment-marker></strong></p><p>This validation rule detects the Part Properties or containing Blocks of Part Properties having incompatible interfaces in accordance with the flowing items specified in Activities.<strong><br class="_mce_tagged_br" /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><ac:inline-comment-marker ac:ref="d88639d5-40f1-443d-8985-e8e9b51ab799">Diagram</ac:inline-comment-marker><strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Create Port </strong>- creates a new Proxy Port typed by a compatible Interface Block.</li><li><strong>Choose Compatible Interface Block </strong>- changes an already existing Proxy Port type to a compatible Interface Block.</li><li><strong>Add Missing Flow Property </strong>- adds a new Flow Property to an Interface Block that types a Proxy Port.</li><li><strong style="letter-spacing: 0.0px;">Reverse Direction of Port </strong>- changes the Proxy Port direction, thus changing the Flow Property direction of an Interface Block that types a Proxy Port.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="BehaviorToStructureSync_validtion_rule.png" /></ac:image></strong></p><h6 style="text-align: center;">Part Property<em> : Power</em> and the <ac:inline-comment-marker ac:ref="a06bd8af-81ef-40cf-aa5c-9863cef18b57">enclosing Block </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="a06bd8af-81ef-40cf-aa5c-9863cef18b57">Wireless Earbuds</ac:inline-comment-marker></em> after using Behavior to Structure Synchronization solvers.</h6>
````

<!--NOMAGIC_PAGE id=81101367 space=VR version=10 -->
## PAGE 00253: No compatible Item Flow realization

- page_id: `81101367`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/81101367/No+compatible+Item+Flow+realization
- version_number: 10
- version_date: `2021-09-14T11:58:12.915+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Behavior to Structure Synchronization
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

BehaviorToStructureSync[3]

**Description**

This validation rule checks if Part Properties with correctly typed Proxy Ports and Connectors in the Internal Block Diagrams have compatible Item Flows realized on Connectors.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Realize Missing Item Flow - creates a new compatible Item Flow or reuses an existing one and then realizes it on the Connector.
- Open Item Flow Manager - opens the Item Flow Manager dialog.
- Change Item Flow Realization Compatibility Checking - opens the Project Options dialog to turn on/turn off the Item Flow realization checking.

**Example**

[IMAGE alt='' src='']

###### Realizing a missing Item Flow on the Connector in the Internal Block Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>BehaviorToStructureSync[3]</p><p><strong>Description</strong></p><p>This validation rule checks if Part Properties with correctly typed Proxy Ports and Connectors in the Internal Block Diagrams have compatible Item Flows realized on Connectors.</p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Realize Missing Item Flow</strong> - <span style="color: rgb(62,63,64);">creates a new compatible Item Flow or reuses an existing one and then realizes it on the Connector.</span></li><li><strong>Open Item Flow Manager</strong> - opens the <strong>Item Flow Manager</strong> dialog.</li><li><strong>Change Item Flow Realization Compatibility Checking</strong> - opens the <strong>Project Options</strong> dialog to turn on/turn off the Item Flow realization checking. </li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="btos_third_validation_rule.png" /></ac:image></p><h6 style="text-align: center;">Realizing a missing Item Flow on the Connector in the Internal Block Diagram.</h6>
````

<!--NOMAGIC_PAGE id=17684325 space=VR version=11 -->
## PAGE 00254: No discrete with continuous Activity Edge

- page_id: `17684325`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684325/No+discrete+with+continuous+Activity+Edge
- version_number: 11
- version_date: `2021-02-11T09:53:52.669+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Discrete[1]****

**Description**

This validation rule checks to make sure that the «discrete» and «continuous» stereotypes are not applied to the same Activity Edge at the same time.****

**Severity**

warning****

**Constrained Element**

Activity Edge****

**Solvers**

To fix this, leave only one«discrete» or «continuous» stereotype applied for the Control Flow or Object Flow.****

**Example**

###### **[IMAGE alt='' src='']**The*of8*Object Flow can have only one «discrete» or «continuous» stereotype applied at the same time.****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>Discrete[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks to make sure that the «discrete» and «continuous» stereotypes are not applied to the same Activity Edge at the same time.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity Edge<strong><br /></strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, leave only one </span><span style="color: rgb(62,63,64);">«discrete» or «continuous» stereotype applied for the Control Flow or Object Flow.</span><strong><br /></strong></p><p><strong>Example</strong></p><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="activityEdge.png" /></ac:image></strong><span style="color: rgb(128,128,128);">The</span><em style="text-align: center;"> of8</em><span style="color: rgb(128,128,128);"> Object Flow can have only one «discrete» or «continuous» stereotype applied at the same time.</span><strong><br /></strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684333 space=VR version=14 -->
## PAGE 00255: No discrete with continuous Object Node

- page_id: `17684333`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684333/No+discrete+with+continuous+Object+Node
- version_number: 14
- version_date: `2021-02-11T09:53:20.183+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Discrete[1]****

**Description**

This validation rulechecks to see if the «discrete» and «continuous» stereotypes are applied to the same Object Node at the same time.****

**Severity**

warning****

**Constrained Element**

Object Node****

**Solvers**

To fix this, leave only one «discrete» or «continuous» stereotype applied for the same Object Node at the same time.

**Example**

**[IMAGE alt='' src='']**

###### The*cold dirty* Activity Parameter Node can have only one «discrete» or «continuous» stereotype applied at the same time.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Discrete[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks to see if t</span>he «discrete» and «continuous» stereotypes are applied to the same Object Node at the same time.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Object Node<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, leave only one «discrete» or «continuous» stereotype applied for the same Object Node at the same time.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="continiuos_discrete.png" /></ac:image></strong></p><h6 style="text-align: center;">The<em> cold dirty</em> Activity Parameter Node can have only one «discrete» or «continuous» stereotype applied at the same time.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684337 space=VR version=9 -->
## PAGE 00256: No discrete with continuous Parameter

- page_id: `17684337`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684337/No+discrete+with+continuous+Parameter
- version_number: 9
- version_date: `2021-02-11T09:54:04.294+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Discrete[1]****

**Description**

This validation rule checks to make sure the «discrete» and «continuous» stereotypes are not applied to the same Parameterat the same time.****

**Severity**

warning****

**Constrained Element**

Parameter****

**Solvers**

To fix this, leave only one«discrete» or «continuous» stereotype applied for the same Parameter at the same time. ****

**Example**

**[IMAGE alt='' src='']**

###### The *recovered* Parameter can have only one «discrete» or «continuous» stereotype applied at the same time. ****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Discrete[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p>This validation rule checks to make sure the «discrete» and «continuous» stereotypes are not applied to the same <span style="color: rgb(62,63,64);">Parameter </span>at the same time.<strong> <br /> </strong></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Parameter<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, leave only one </span><span style="color: rgb(62,63,64);">«discrete» or «continuous» stereotype applied for the same Parameter at the same time.</span> <strong> <br /> </strong></p><p><strong>Example</strong></p><p><strong> <ac:image ac:align="center"><ri:attachment ri:filename="parameter_continuous.png" /></ac:image> </strong></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">The</span> <em style="text-align: center;"> recovered</em> <span> Parameter can have only one «discrete» or «continuous» stereotype applied at the same time.</span> <strong> <br /> </strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969519 space=VR version=1 -->
## PAGE 00257: No Incoming Transitions

- page_id: `243969519`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969519/No+Incoming+Transitions
- version_number: 1
- version_date: `2025-07-31T10:51:31.504+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

StatIncTrns

**Description**

This validation rule checks if a State is without Incoming Transitions.

**Severity**

warning

**Constrained Element**

Vertex

**Solvers**

- To fix this, make sure a State has Incoming Transitions.

**Example**

[IMAGE alt='' src='']

###### The State *Initializing* does not have any Incoming Transitions. The error is resolved by creating a Transition between the State *Initializing* and the Initial Pseudo State.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>StatIncTrns</p><p><strong>Description</strong></p><p>This validation rule checks if a State is without Incoming Transitions.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Vertex</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure a State has Incoming Transitions.<strong><br /></strong></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Incoming_Transitions.png" /></ac:image></p><h6 style="text-align: center;">The State <em>Initializing</em> does not have any Incoming Transitions. The error is resolved by creating a Transition between the State <em>Initializing</em> and the Initial Pseudo State.</h6>
````

<!--NOMAGIC_PAGE id=243969521 space=VR version=1 -->
## PAGE 00258: No Operation for Call Message

- page_id: `243969521`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969521/No+Operation+for+Call+Message
- version_number: 1
- version_date: `2025-07-31T10:51:31.565+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

CllMsgWithOp

**Description**

This validation rule checks if a Call Message has an Operation assigned.

**Severity**

error

**Constrained Element**

Message

**Solvers**

- To fix this, make sure a Call Message has an Operation assigned.

**Example**

[IMAGE alt='' src='']

###### Call Message *No.2*does not have an Operation assigned. The error is resolved by assigning an Operation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>CllMsgWithOp</p><p><strong>Description</strong></p><p>This validation rule checks if a Call Message has an Operation assigned.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Message</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure a Call Message has an Operation assigned.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Operation_for_Call_Message.png" /></ac:image></p><h6 style="text-align: center;">Call Message <em>No.2 </em>does not have an Operation assigned. The error is resolved by assigning an Operation. </h6>
````

<!--NOMAGIC_PAGE id=243969523 space=VR version=1 -->
## PAGE 00259: No Outgoing Transitions

- page_id: `243969523`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969523/No+Outgoing+Transitions
- version_number: 1
- version_date: `2025-07-31T10:51:31.631+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

StatOutTrns

**Description**

This validation rule checks if a State is without Outgoing Transitions.

**Severity**

warning

**Constrained Element**

Vertex

**Solvers**

- To fix this, make sure a State has Outgoing Transitions.

**Example**

[IMAGE alt='' src='']

###### The Initial Pseudo State does not have any Outgoing Transitions. The error is resolved by creating a Transition between the Initial Pseudo State and the State *Off*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>StatOutTrns</p><p><strong>Description</strong></p><p>This validation rule checks if a State is without Outgoing Transitions.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Vertex</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure a State has Outgoing Transitions.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Outgoing_Transitions.png" /></ac:image></p><h6 style="text-align: center;">The Initial Pseudo State does not have any Outgoing Transitions. The error is resolved by creating a Transition between the Initial Pseudo State and the State <em>Off</em>.</h6>
````

<!--NOMAGIC_PAGE id=17684351 space=VR version=9 -->
## PAGE 00260: No Overwrite with noBuffer of Object Node

- page_id: `17684351`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684351/No+Overwrite+with+noBuffer+of+Object+Node
- version_number: 9
- version_date: `2021-02-11T09:53:38.111+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

noBuffer[1]-Overwrite[1]****

**Description**

This validation rule checks to make sure the «nobuffer» and «overwrite» stereotypes are not applied to the same Object Nodeat the same time.****

**Severity**

warning****

**Constrained Element**

Object Node****

**Solvers**

To fix this, leave only one «nobuffer» or «overwrite» stereotype applied for the same Object Node****at the same time.****

**Example**

###### **[IMAGE alt='' src='']**

###### The *pure* Activity Parameter Node can have only one «nobuffer» or «overwrite» stereotype applied at the same time. ****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>noBuffer[1]-Overwrite[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p>This validation rule checks to make sure the «nobuffer» and «overwrite» stereotypes are not applied to the same <span style="color: rgb(62,63,64);">Object Node </span>at the same time.<strong> <br /> </strong></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Object Node<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, leave only one</span> <span style="color: rgb(62,63,64);">«nobuffer» or «overwrite»  stereotype applied for the same Object Node<strong> </strong>at the same time.</span><strong><br /> </strong></p><p><strong>Example</strong></p><h6><strong> <ac:image ac:align="center"><ri:attachment ri:filename="nobuffer_overwrite.png" /></ac:image> </strong></h6><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">The</span> <em style="text-align: center;"> pure</em> <span> Activity Parameter Node can have only one <span>«nobuffer» or «overwrite»</span> stereotype applied at the same time.</span> <strong> <br /> </strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969525 space=VR version=1 -->
## PAGE 00261: No Stereotype Metaclass

- page_id: `243969525`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969525/No+Stereotype+Metaclass
- version_number: 1
- version_date: `2025-07-31T10:51:31.698+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

MtClsForStr

**Description**

This validation rule checks if a Stereotype has a Metaclass.

**Severity**

error

**Constrained Element**

Stereotype

**Solvers**

- To fix this, make sure a Stereotype has a Metaclass.

**Example**

[IMAGE alt='' src='']

###### Stereotype *Activation* does not have a Metaclass specified. The error is resolved by specifying a Metaclass.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>MtClsForStr</p><p><strong>Description</strong></p><p>This validation rule checks if a Stereotype has a Metaclass.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Stereotype</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure a Stereotype has a Metaclass.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Stereotype_Metaclass.png" /></ac:image></p><h6 style="text-align: center;">Stereotype <em>Activation</em> does not have a Metaclass specified. The error is resolved by specifying a Metaclass.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=17684419 space=VR version=9 -->
## PAGE 00262: No streaming with nonStreaming

- page_id: `17684419`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684419/No+streaming+with+nonStreaming
- version_number: 9
- version_date: `2021-01-06T12:18:50.421+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

streaming[A]-nonStreaming[A]****

**Description**

This validation rulechecks if t he Activity is not stereotyped by «s treaming » and «nons treaming » at the same time.****

**Severity**

warning****

**Constrained Element**

Activity****

**Solvers**

To fix this, keep only one «streaming » or «nonstreaming » stereotype applied for the same Activity.

**Example**

**[IMAGE alt='' src='']**

###### Only «streaming» stereotype is applied for the *dry part* Activity.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>streaming[A]-nonStreaming[A]<strong> <br /> </strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule</span><span style="color: rgb(62,63,64);"> checks if t</span> <span style="color: rgb(62,63,64);">he Activity is not stereotyped by</span> <span style="color: rgb(51,51,51);">«s</span> <span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> and <span style="color: rgb(51,51,51);">«nons</span> <span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> at the same time.<strong> <br /> </strong></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Activity<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, keep only one <span style="color: rgb(51,51,51);">«s</span><span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> or <span style="color: rgb(51,51,51);">«nons</span><span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> stereotype applied for the same Activity.</span></p><p><strong>Example</strong></p><p><strong> <ac:image ac:align="center"><ri:attachment ri:filename="streaming_nonStreaming_val_rule.png" /></ac:image> </strong></p><h6 style="text-align: center;">Only «streaming» stereotype is applied for the <em>dry part</em> Activity.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969527 space=VR version=1 -->
## PAGE 00263: No Type for Parameter

- page_id: `243969527`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969527/No+Type+for+Parameter
- version_number: 1
- version_date: `2025-07-31T10:51:31.764+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

PrmTpIsDef

**Description**

This validation rule checks if parameter types for an Operation are specified.

**Severity**

error

**Constrained Element**

Operation

**Solvers**

- To fix this, make sure parameter types for an Operation are specified.

**Example**

[IMAGE alt='' src='']

###### The *Process Data*Operation has a parameter *input*that does not have a type. The error is resolved by specifying a type for the parameter.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>PrmTpIsDef</p><p><strong>Description</strong></p><p>This validation rule checks if parameter types for an Operation are specified.</p><p><strong>Severity</strong></p><p>error</p><p><strong>Constrained Element</strong></p><p>Operation</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure parameter types for an Operation are specified.</li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="No_Type_for_Parameter.png" /></ac:image></p><h6 style="text-align: center;">The <em>Process Data </em>Operation has a parameter <em>input </em>that does not have a type. The error is resolved by specifying a type for the parameter.</h6>
````

<!--NOMAGIC_PAGE id=92217275 space=VR version=3 -->
## PAGE 00264: Not Realized Item Flow

- page_id: `92217275`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/92217275/Not+Realized+Item+Flow
- version_number: 3
- version_date: `2022-05-25T14:50:29.827+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Ports and Flows
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

NRIF****

**Description**

This validation rule checks if there are any Item Flows in the model that are not realized. ****

**Severity**

warning****

**Constrained Element**

Item Flow

**Solvers**

- Remove from Model - removes the not realized Item Flow from the model .

**Example**

**[IMAGE alt='' src='']**

###### The Item Flow from the *Human-Machine Interaction* block to the *VCCU* block is not realized as it does not contain any realizing elements. 
The error is resolved via the **Remove from Model** solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>NRIF<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if there are any Item Flows in the model that are not realized. <strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Item Flow</p><p><strong>Solvers</strong></p><ul><li><strong>Remove from Model </strong>- removes the <span style="color: rgb(62,63,64);">not realized Item Flow from the model</span>.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="Not Realized Item Flow.png" /></ac:image></strong></p><h6 style="text-align: center;">The Item Flow from the <em>Human-Machine Interaction</em> block to the <em>VCCU</em> block is not realized as it does not contain any realizing elements. <br />The error is resolved via the <strong>Remove from Model</strong> solver.</h6>
````

<!--NOMAGIC_PAGE id=17684429 space=VR version=7 -->
## PAGE 00265: Obsolete Quantity Kind for QUDV

- page_id: `17684429`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684429/Obsolete+Quantity+Kind+for+QUDV
- version_number: 7
- version_date: `2020-12-07T07:28:39.542+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

QUDV[B]****

**Description**

This rulechecks if each QUDV Quantity Kind's base classifier is an Instance Specification, instead of a DataType.

**Severity**

info****

**Constrained Element**

DataType

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>QUDV[B]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule</span><span style="color: rgb(62,63,64);"> checks if e</span>ach QUDV Quantity Kind's base classifier is an Instance Specification, instead of a DataType.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>DataType</p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684433 space=VR version=8 -->
## PAGE 00266: Obsolete Quantity Kind used in Unit for QUDV

- page_id: `17684433`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684433/Obsolete+Quantity+Kind+used+in+Unit+for+QUDV
- version_number: 8
- version_date: `2020-12-07T07:28:51.136+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

QUDV[D]****

**Description**

This rulechecks if the Quantity Kind defined in the Unit is not obsolete in the context of QUDV.

**Severity**

info****

**Constrained Element**

Instance Specification

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>QUDV[D]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule </span><span style="color: rgb(62,63,64);">checks if t</span>he Quantity Kind defined in the Unit is not obsolete in the context of QUDV.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Instance Specification</p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684437 space=VR version=5 -->
## PAGE 00267: Obsolete Quantity Kind used in Value Type for QUDV

- page_id: `17684437`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684437/Obsolete+Quantity+Kind+used+in+Value+Type+for+QUDV
- version_number: 5
- version_date: `2020-12-07T07:29:01.528+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

QUDV[E]****

**Description**

This rulechecks if the Quantity Kind defined in the Value Type is not obsolete in the context of QUDV.

**Severity**

info****

**Constrained Element**

Data Type

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>QUDV[E]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule </span><span style="color: rgb(62,63,64);">checks if t</span>he Quantity Kind defined in the Value Type is not obsolete in the context of QUDV.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Data Type</p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684442 space=VR version=5 -->
## PAGE 00268: Obsolete Unit for QUDV

- page_id: `17684442`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684442/Obsolete+Unit+for+QUDV
- version_number: 5
- version_date: `2020-12-07T07:29:12.233+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

QUDV[A]****

**Description**

This rulechecks if each QUDV Unit's base classifier is an Instance Specification, instead of a DataType.

**Severity**

info****

**Constrained Element**

DataType

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>QUDV[A]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule</span><span style="color: rgb(62,63,64);"> checks if e</span>ach QUDV Unit's base classifier is an Instance Specification, instead of a DataType.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>DataType</p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=17684446 space=VR version=5 -->
## PAGE 00269: Obsolete Unit used in Value Type for QUDV

- page_id: `17684446`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684446/Obsolete+Unit+used+in+Value+Type+for+QUDV
- version_number: 5
- version_date: `2020-12-07T07:29:25.498+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

QUDV[C]****

**Description**

This rulechecks if the Unit defined in the ValueType is not obsolete in the context of QUDV.

**Severity**

info****

**Constrained Element**

DataType

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>QUDV[C]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule </span><span style="color: rgb(62,63,64);">checks if t</span>he Unit defined in the ValueType is not obsolete in the context of QUDV.</p><p><strong>Severity</strong></p><p>info<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>DataType</p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228985830 space=VR version=1 -->
## PAGE 00270: OperationalBToSSync 1

- page_id: `228985830`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985830/OperationalBToSSync+1
- version_number: 1
- version_date: `2023-04-26T07:54:37.561+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

**Abbreviation**

OperationalBToSSync[1]

**Description**

No compatible Operational Interface. Thisvalidation rule checks whether Operational Ports and Operational Interfaces are compatible with flows between the Operational Roles. The missing Ports and Interfaces can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Create Operational Port - creates a new Operational Port typed by a compatible Operational Interface.
- Choose Compatible Operational Interface - changes an existing Operational Port type to a compatible Operational Interface.
- Add Missing Flow Property - adds a new Flow Property to an Operational Interface that types an Operational Port.
- Reverse Direction of Operational Port - changes the Operational Port direction, thus changing the Flow Property direction of an Operational Interface that types an Operational Port.

**Example**

**[IMAGE alt='' src='']**

###### The Operational Port *iMedical care request* is created using Behavior to Structure Synchronization solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>OperationalBToSSync[1]</p><p><strong><ac:inline-comment-marker ac:ref="7216feb7-efde-4071-86ed-30df4d49b0fe">Description</ac:inline-comment-marker></strong></p><p><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="0cab6c11-8f7d-467f-bb0d-2f7ed7ce8a0a">No compatible Operational Interface</ac:inline-comment-marker>. This </span><span style="color: rgb(62,63,64);">validation rule checks whether Operational Ports and Operational Interfaces are compatible with flows between the Operational Roles. The missing Ports and Interfaces can be handled automatically using solvers.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><ac:inline-comment-marker ac:ref="d88639d5-40f1-443d-8985-e8e9b51ab799">Diagram</ac:inline-comment-marker><strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Create Operational Port </strong>- creates a new Operational Port typed by a compatible Operational Interface.</li><li><strong>Choose Compatible Operational Interface </strong>- changes an existing Operational Port type to a compatible Operational Interface.</li><li><strong>Add Missing Flow Property </strong>- adds a new Flow Property to an Operational Interface that types an Operational Port.</li><li><strong style="letter-spacing: 0.0px;">Reverse Direction of Operational Port </strong>- changes the Operational Port direction, thus changing the Flow Property direction of an Operational Interface that types an Operational Port.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="UAF_behavior_to_structure_operational_ports_and_interfaces_validation_rule_process.png" /></ac:image></strong></p><h6 style="text-align: center;">The Operational Port <em>iMedical care request</em> is created using Behavior to Structure Synchronization solver.</h6>
````

<!--NOMAGIC_PAGE id=228985834 space=VR version=1 -->
## PAGE 00271: OperationalBToSSync 2

- page_id: `228985834`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985834/OperationalBToSSync+2
- version_number: 1
- version_date: `2023-04-26T08:00:00.003+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

OperationalBToSSync[2]

**Description**

No compatible Operational Connector.The second validation rule checks whether an Operational Connector exists between the two compatible Operational Ports owned by the Operational Roles. The missing Operational Connectors can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

**Create Operational Connector** - creates a missing Operational Connector between the two compatible Operational Ports.

**Example**

###### **[IMAGE alt='' src='']**Creating an Operational Connector that is missing in the Operational Internal Connectivity Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>OperationalBToSSync[2]</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="a0500637-79af-47bc-8229-8ac16e656b3c">No compatible Operational Connector.</ac:inline-comment-marker><span> </span></span><span style="color: rgb(62,63,64);">The second validation rule checks whether an Operational Connector exists between the two compatible Operational Ports owned by the Operational Roles. The missing Operational Connectors can be handled automatically using solvers.</span></p><p><strong style="letter-spacing: 0.0px;">Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Create Operational Connector</strong> - creates a missing Operational Connector between the two compatible Operational Ports. </p><p><strong>Example</strong></p><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="UAF_behavior_to_structure_operational_connectors_validation_rule_process.png" /></ac:image></strong>Creating an Operational Connector that is missing in the Operational Internal Connectivity Diagram.</h6>
````

<!--NOMAGIC_PAGE id=228985838 space=VR version=1 -->
## PAGE 00272: OperationalBToSSync 3

- page_id: `228985838`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985838/OperationalBToSSync+3
- version_number: 1
- version_date: `2024-01-08T14:00:21.104+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

**Abbreviation**

OperationalBToSSync[3]

**Description**

No compatible Operational Exchange realization. The third validation rule checks realized Operational Exchanges in Activities and help to ensure the correct Operational Exchanges are realized on Operational Connectors that connect Operational Ports typed by compatible Operational Interface.Themissing Exchanges can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Realize Missing Operational Exchange - realizes existing compatible Operational Exchange found in the behavior model on the Operational Connector.
- Open Operational Exchange Manager - opens the Operational Exchange Manager dialog.
- Change Exchange Realization Compatibility Checking - opens the Project Options dialog to turn on/off the Exchange realization checking.

**Example**

[IMAGE alt='' src='']

###### Realizing a missing Operational Exchange on the Connector in the Operational Internal Connectivity Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>OperationalBToSSync[3]</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="9ff0abfe-f10c-4db0-a28c-130842d00ba0">No compatible Operational Exchange realization.</ac:inline-comment-marker> The third validation rule checks realized Operational Exchanges in Activities and help to ensure the correct Operational Exchanges are realized on Operationa<ac:inline-comment-marker ac:ref="bb0881e4-6236-4d84-b81c-3005736dc329">l C</ac:inline-comment-marker>onnectors that connect Operational Ports typed by compatible Operationa<ac:inline-comment-marker ac:ref="60b25f69-a771-4e52-9a21-4361ac38e1e4">l I</ac:inline-comment-marker>nterface.<span> </span></span>The<span style="color: rgb(62,63,64);"><span> </span>missing Exchanges can be handled automatically using solvers.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Realize Missing Operational Exchange</strong> - realizes existing compatible Operational Exchange found in the behavior model on the Operational Connector.</li><li><strong>Open Operational Exchange Manager</strong> - opens the <strong>Operational Exchange</strong><strong> Manager</strong> dialog.</li><li><strong>Change Exchange Realization Compatibility Checking</strong> - <span style="color: rgb(62,63,64);">opens the<span> </span></span><strong style="text-align: left;">Project Options</strong><span style="color: rgb(62,63,64);"><span> </span>dialog to turn on/off the Exchange realization checking. </span> </li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="UAF_behavior_to_structure_operational_exchanges_validation_rule_process.png" /></ac:image></p><h6 style="text-align: center;">Realizing a missing Operational Exchange on the Connector in the Operational Internal Connectivity Diagram.</h6>
````

<!--NOMAGIC_PAGE id=166396638 space=VR version=1 -->
## PAGE 00273: Other validation rules

- page_id: `166396638`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/166396638/Other+validation+rules
- version_number: 1
- version_date: `2024-04-15T18:36:43.587+02:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="98c37cb9-5859-4a44-8c02-78085dafb48b" /></p>
````

<!--NOMAGIC_PAGE id=17684460 space=VR version=6 -->
## PAGE 00274: PerformanceRequirement satisfied by an invalid element

- page_id: `17684460`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684460/PerformanceRequirement+satisfied+by+an+invalid+element
- version_number: 6
- version_date: `2021-01-06T12:24:33.014+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

performanceRequirement[1]****

**Description**

This validation rulechecks if the Performance Requirement is satisfied by a Value Property.****

**Severity**

warning****

**Constrained Element**

Performance Requirement****

**Solvers**

- **Remove invalid Satisfy relationship(s)** - deletes not valid Satisfy relationship from the model.

**Example**

**[IMAGE alt='' src='']**

###### The *Pad Thickness* Performance Requirement is satisfied by *thickness* Value Property.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>performanceRequirement[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks if the Performance <ac:inline-comment-marker ac:ref="e99f472b-03e9-46d1-bbfe-264d3f54a2e0">Requirement</ac:inline-comment-marker> is s</span>atisfied by a Value Property.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Performance Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong><strong>Remove invalid Satisfy relationship(s) </strong></strong><span style="color: rgb(62,63,64);">- deletes not valid Satisfy relationship from the model.</span><strong><br class="_mce_tagged_br" /></strong></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="perform_req_val_rule.png" /></ac:image></strong></p><h6 style="text-align: center;">The <em>Pad Thickness</em> Performance Requirement is satisfied by <em>thickness</em> Value Property.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969529 space=VR version=1 -->
## PAGE 00275: Realized Information Flow has no Conveyed Information

- page_id: `243969529`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969529/Realized+Information+Flow+has+no+Conveyed+Information
- version_number: 1
- version_date: `2025-07-31T10:51:31.829+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

RIFHNCI[1]

**Description**

This validation rule checks if there are any realized Information Flows without Conveyed Information.

**Severity**

warning

**Constrained Element**

Connector, Association, ActivityEdge, Message

**Solvers**

- **Select Conveyed Information** - opens the Select Conveyed Information dialog where you can choose the Conveyed Information for the validated Information Flow.

**Example**

[IMAGE alt='' src='']

###### An Information Flow has no Conveyed Information. The error is resolved by specifying Conveyed Information via the **Select Conveyed Information**solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p><span style="color: rgb(23,43,77);">RIFHNCI</span><span class="error" style="color: rgb(23,43,77);">[1]</span></p><p><strong>Description</strong></p><p>This validation rule checks if <span style="letter-spacing: 0.0px;">there are any r</span><span style="color: rgb(23,43,77);">ealized Information Flows without Conveyed Information.</span></p><p><strong>Severity</strong></p><p><span style="color: rgb(23,43,77);">warning</span></p><p><strong>Constrained Element</strong></p><p><span style="color: rgb(23,43,77);">Connector, Association, ActivityEdge, Message</span></p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Select Conveyed Information</strong> - opens the Select Conveyed Information dialog where you can choose the Conveyed Information for the validated Information Flow.</span></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Realized_Information_Flow_has_no_Conveyed_Information.png" /></ac:image></p><h6 style="text-align: center;">An Information Flow has no Conveyed Information. The error is resolved by specifying Conveyed Information via the <strong>Select Conveyed Information </strong>solver.</h6>
````

<!--NOMAGIC_PAGE id=165249329 space=VR version=2 -->
## PAGE 00276: Realized Item Flow has no Conveyed Items

- page_id: `165249329`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/165249329/Realized+Item+Flow+has+no+Conveyed+Items
- version_number: 2
- version_date: `2024-04-18T17:02:51.748+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Ports and Flows
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

RIFHNCI[2]

**Description**

This validation rule checks if there are any realized Item Flows without Conveyed Items.****

**Severity**

warning****

**Constrained Element**

Connector, Association, ActivityEdge, Message

**Solvers**

- **Select Conveyed Item** - opens the Select Conveyed Information dialog where you can choose theConveyed Item for the validated Item Flow.

**Example**

**[IMAGE alt='' src='']**

###### An Item Flow has no Conveyed Item. The error is resolved by specifying a Conveyed Item via the **Select Conveyed Item**solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p><span style="color: rgb(23,43,77);">RIFHNCI</span><span class="error" style="color: rgb(23,43,77);">[2]</span></p><p><strong>Description</strong></p><p>This validation rule checks if there are any r<span style="color: rgb(23,43,77);">ealized Item Flows without Conveyed Items.</span><strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><span style="color: rgb(23,43,77);">Connector, Association, ActivityEdge, Message</span></p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Select Conveyed Item</strong> - opens the Select Conveyed Information dialog <span style="color: rgb(23,43,77);">where you can choose the </span>Conveyed Item for the validated Item Flow.</span></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><strong><ac:image><ri:attachment ri:filename="Realized_Item_Flow_has_no_Conveyed_Items.png" /></ac:image><br /></strong></p><h6 style="text-align: center;">An Item Flow has no Conveyed Item. The error is resolved by specifying a Conveyed Item via the <strong>Select Conveyed Item </strong>solver.</h6>
````

<!--NOMAGIC_PAGE id=20845947 space=VR version=1 -->
## PAGE 00277: Recursive loop of Copy dependencies

- page_id: `20845947`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845947/Recursive+loop+of+Copy+dependencies
- version_number: 1
- version_date: `2017-08-21T11:42:59.008+02:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

Copy[B]****

**Description**

Copy dependencies should not from a cyclic graph.****

**Severity**

warning****

**Context element**

Copy****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>Copy[B]<strong><br /></strong></p><p><strong>Description</strong></p><p>Copy dependencies should not from a cyclic graph.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Copy<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=44907318 space=VR version=11 -->
## PAGE 00278: Relationship and its ends differ in context

- page_id: `44907318`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/44907318/Relationship+and+its+ends+differ+in+context
- version_number: 11
- version_date: `2022-09-20T08:12:38.548+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Contextual Relationships
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

DifferInContext

**Description**

The context of the relationship does not match the context the connected property is displayed in.

**Severity**

error

**Constrained Element**

Diagram

**Solvers**

You can use one of the following solvers:

- Update Context of Relationship - updates the actual path of the connected property.
- Decontextualize - removes the relationship context.
- Remove from Diagram - removes the symbol from the diagram.
- Delete from Model - deletes the element from the model.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p><ac:inline-comment-marker ac:ref="2e406f54-d801-4fbb-b8c0-1bb02eef418e">DifferInContext</ac:inline-comment-marker></p><p><strong>Description</strong></p><p>The context of the relationship does not match the context the connected property is displayed in.</p><p><strong>Severity</strong></p><p><ac:inline-comment-marker ac:ref="18d31d91-e86f-446c-af30-4a3414317881">error</ac:inline-comment-marker></p><p><strong><ac:inline-comment-marker ac:ref="4faf89ff-d147-4f4e-a5ce-4838b8b7af97">Constrained Element</ac:inline-comment-marker></strong></p><p>Diagram</p><p><strong>Solvers</strong></p><p>You can use one of the following solvers:</p><ul><li><strong>Update Context of Relationship</strong> - updates the actual path of the connected property.</li><li><strong>Decontextualize</strong> - removes the relationship context. </li><li><strong>Remove from Diagram</strong> - removes the symbol from the diagram.</li><li><strong><ac:inline-comment-marker ac:ref="e6658119-aa99-46ba-8404-ff01f8f4e220">Delete from Model</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="e6658119-aa99-46ba-8404-ff01f8f4e220">  - deletes the element from the model.</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="e6658119-aa99-46ba-8404-ff01f8f4e220"><br /></ac:inline-comment-marker></li></ul><p><strong><ac:inline-comment-marker ac:ref="4bed668a-0532-459a-a992-a1888cb7a7e0">Example</ac:inline-comment-marker></strong></p><p><strong><ac:image ac:height="137" ac:width="517"><ri:attachment ri:filename="validatation_contextual_relationships.png" /></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=20845930 space=VR version=6 -->
## PAGE 00279: Requirements validation rules

- page_id: `20845930`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845930/Requirements+validation+rules
- version_number: 6
- version_date: `2024-01-30T08:14:17.709+01:00`
- ancestors: Validation Rules
- labels: []

### NORMALIZED CONTENT

This page contains all constraints for the Requirements implemented in the tool as validation rules.

The Requirements validation suites and active validation suites include the following validation rules:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This page contains all constraints for the Requirements implemented in the tool as validation rules.</p><p>The Requirements validation suites and active validation suites include the following validation rules:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="298da124-da67-492d-864e-2e00e31dec66" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=228985843 space=VR version=1 -->
## PAGE 00280: ResourcesBToSSync 1

- page_id: `228985843`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985843/ResourcesBToSSync+1
- version_number: 1
- version_date: `2023-04-26T07:57:41.487+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

**Abbreviation**

ResourcesBToSSync[1]

**Description**

No compatible Resource Interface. Thisvalidation rule checks whether Resource Ports and Resource Interfaces are compatible with flows between the Resource Roles. The missing Ports and Interfaces can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Create Resource Port - creates a new Resource Port typed by a compatible Resource Interface.
- Choose Compatible Resource Interface - changes an existing Resource Port type to a compatible Resource Interface.
- Add Missing Flow Property - adds a new Flow Property to a Resource Interface that types a Resource Port.
- Reverse Direction of ResourcePort - changes the Resource Port direction, thus changing the Flow Property direction of a Resource Interface that types a Resource Port.

**Example**

**[IMAGE alt='' src='']**

###### The Resource Port*iTriage*is created using Behavior to Structure Synchronization solvers.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ResourcesBToSSync[1]</p><p><strong><ac:inline-comment-marker ac:ref="7216feb7-efde-4071-86ed-30df4d49b0fe">Description</ac:inline-comment-marker></strong></p><p><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="63e12ed2-ff4d-407b-9819-9808bb8dd540">No compatible Resource Interface</ac:inline-comment-marker>. This </span><span style="color: rgb(62,63,64);">validation rule checks whether Resource Ports and Resource Interfaces are compatible with flows between the Resource Roles. The missing Ports and Interfaces can be handled automatically using solvers.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><ac:inline-comment-marker ac:ref="d88639d5-40f1-443d-8985-e8e9b51ab799">Diagram</ac:inline-comment-marker><strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Create Resource Port </strong>- creates a new Resource Port typed by a compatible Resource Interface.</li><li><strong>Choose Compatible Resource Interface </strong>- changes an existing Resource Port type to a compatible Resource Interface.</li><li><strong>Add Missing Flow Property </strong>- adds a new Flow Property to a Resource Interface that types a Resource Port.</li><li><strong style="letter-spacing: 0.0px;">Reverse Direction <ac:inline-comment-marker ac:ref="70f0e072-f1d9-4655-a463-9a4400f792a0">of <span style="color: rgb(62,63,64);">Resource </span>Port</ac:inline-comment-marker> </strong>- changes the Resource Port direction, thus changing the Flow Property direction of a Resource Interface that types a Resource Port.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="UAF_behavior_to_structure_resources_ports_and_interfaces_validation_rule_process.png" /></ac:image></strong></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">The Resource Port<span> </span></span><em style="text-align: center;">iTriage</em><span style="color: rgb(128,128,128);"><span> </span>is created</span> using Behavior to Structure Synchronization solvers.</h6>
````

<!--NOMAGIC_PAGE id=228985848 space=VR version=1 -->
## PAGE 00281: ResourcesBToSSync 2

- page_id: `228985848`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985848/ResourcesBToSSync+2
- version_number: 1
- version_date: `2023-04-26T07:58:36.053+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ResourcesBToSSync[2]

**Description**

No compatible Resource Connector.The second validation rule checks whether a Resources Connector exists between the two compatible Resources Ports owned by the Resource Roles. The missing Resources Connectors can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

**Create ResourcesConnector** - creates a missing ResourcesConnector between the two compatible ResourcesPorts.

**Example**

###### **[IMAGE alt='' src='']**Creating a Resources Connector that is missing in the Resources Internal Connectivity Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ResourcesBToSSync[2]</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="a0ee347f-f6f4-4407-9928-dc6c9d15ed05">No compatible Resource Connector</ac:inline-comment-marker>.<span> </span></span><span style="color: rgb(62,63,64);">The second validation rule checks whether a Resources Connector exists between the two compatible Resources Ports owned by the Resource <ac:inline-comment-marker ac:ref="045f01d7-539d-408c-89eb-3a42e10e96f3">Roles</ac:inline-comment-marker>. The missing Resources Connectors can be handled automatically using solvers.</span></p><p><strong style="letter-spacing: 0.0px;">Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Create <span style="color: rgb(62,63,64);">Resources </span>Connector</strong> - creates a missing <span style="color: rgb(62,63,64);">Resources </span>Connector between the two compatible <span style="color: rgb(62,63,64);">Resources </span>Ports. </p><p><strong>Example</strong></p><h6 style="text-align: center;"><strong><ac:image><ri:attachment ri:filename="UAF_behavior_to_structure_resources_connectors_validation_rule_process.png" /></ac:image><br /></strong><span style="color: rgb(128,128,128);">Creating a Resources Connector that is missing in the Resources Internal Connectivity Diagram.</span></h6>
````

<!--NOMAGIC_PAGE id=228985852 space=VR version=1 -->
## PAGE 00282: ResourcesBToSSync 3

- page_id: `228985852`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985852/ResourcesBToSSync+3
- version_number: 1
- version_date: `2024-01-15T15:46:01.942+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ResourcesBToSSync[3]

**Description**

No compatible Resource Exchange realization. The third validation rule checks realized Resources Exchanges in Activities and help to ensure the correct Resources Exchanges are realized on Resources Connectors that connect Resources Ports typed by compatible Resources Interface.Themissing Exchanges can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Realize Missing Resource Exchange - r ealizes existing compatible Resource Exchange found in the behavior model on the Resources Connector .
- Open Resource Exchange Manager - opens the Resource Exchange Manager dialog.
- Change Exchange Realization Compatibility Checking - opens the Project Options dialog to turn on/turn off the Exchange realization checking.

**Example**

[IMAGE alt='' src='']

###### Realizing a missing Resource Exchange on the Connector in the Resources Internal Connectivity Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ResourcesBToSSync[3]</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">No compatible Resource Exchange realization. The third validation rule checks realized Resources Exchanges in Activities and help to ensure the correct Resources Exchanges are realized on Resources Connectors that connect Resources Ports typed by compatible Resources Interface.<span> </span></span><span style="color: rgb(62,63,64);">The</span><span style="color: rgb(62,63,64);"><span> </span>missing Exchanges can be handled automatically using solvers.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Realize Missing Resource Exchange</strong> - <span style="color: rgb(62,63,64);">r</span><span style="color: rgb(23,43,77);">ealizes existing compatible Resource Exchange found in the behavior model on the Resources Connector</span><span style="color: rgb(62,63,64);">. </span></li><li><strong>Open <ac:inline-comment-marker ac:ref="51a81ba7-c982-4882-ba93-f54dfb5d2fc8">Resource Exchange Manager</ac:inline-comment-marker></strong> - opens the <strong>Resource Exchange Manager</strong> dialog.</li><li><strong>Change Exchange Realization Compatibility Checking</strong> - opens the <strong>Project Options</strong> dialog to turn on/turn off the Exchange realization checking. </li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="UAF_behavior_to_structure_resources_connectors_validation_rule_process (1).png" /></ac:image></p><h6 style="text-align: center;"><ac:inline-comment-marker ac:ref="4d386544-5508-408a-99c2-114155023b62">Realizing a missing Resource Exchange on the Connector in the Resources Internal Connectivity Diagram.</ac:inline-comment-marker></h6>
````

<!--NOMAGIC_PAGE id=228985857 space=VR version=1 -->
## PAGE 00283: ServicesBToSSync 1

- page_id: `228985857`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985857/ServicesBToSSync+1
- version_number: 1
- version_date: `2023-04-26T07:47:11.549+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ServicesBToSSync[1]

**Description**

No compatible Service Interface. Thisvalidation rule checks whether Service Ports and Service Interfaces are compatible with flows between the Service Roles. The missing Ports and Interfaces can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Create Service Port - creates a new Service Port typed by a compatible Service Interface.
- Choose Compatible ServiceInterface - changes an existing Service Port type to a compatible Service Interface.
- Add Missing Flow Property - adds a new Flow Property to a Service Interface that types a Service Port.
- Reverse Direction of Service Port - changes the Service Port direction, thus changing the Flow Property direction of a Service Interface that types a Service Port.

**Example**

###### **[IMAGE alt='' src='']**The Service Port*iPayment*is created using Behavior to Structure Synchronization solver.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ServicesBToSSync[1]</p><p><strong><ac:inline-comment-marker ac:ref="7216feb7-efde-4071-86ed-30df4d49b0fe">Description</ac:inline-comment-marker></strong></p><p><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="9024090c-41c0-49d6-a323-a9b586b9b0f5">No compatible Service Interface.</ac:inline-comment-marker> This </span><span style="color: rgb(62,63,64);">validation rule checks whether Service Ports and Service Interfaces are compatible with flows between the Service Roles. The missing Ports and Interfaces can be handled automatically using solvers.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><ac:inline-comment-marker ac:ref="d88639d5-40f1-443d-8985-e8e9b51ab799">Diagram</ac:inline-comment-marker><strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Create Service Port </strong>- creates a new Service Port typed by a compatible <span style="color: rgb(62,63,64);">Service </span>Interface.</li><li><strong>Choose Compatible <span style="color: rgb(62,63,64);">Service </span>Interface </strong>- changes an existing <span style="color: rgb(62,63,64);">Service </span>Port type to a compatible <span style="color: rgb(62,63,64);">Service </span>Interface.</li><li><strong>Add Missing Flow Property </strong>- adds a new Flow Property to a <span style="color: rgb(62,63,64);">Service </span>Interface that types a <span style="color: rgb(62,63,64);">Service </span>Port.</li><li><strong style="letter-spacing: 0.0px;">Reverse Direction of Service Port </strong>- changes the <span style="color: rgb(62,63,64);">Service </span>Port direction, thus changing the Flow Property direction of a <span style="color: rgb(62,63,64);">Service </span>Interface that types a <span style="color: rgb(62,63,64);">Service </span>Port.</li></ul><p><strong>Example</strong></p><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="UAF_behavior_to_structure_services_ports_and_interfaces_validation_rule_process.png" /></ac:image></strong><span style="color: rgb(128,128,128);"><ac:inline-comment-marker ac:ref="e0cf8396-b271-4626-b8be-080047f2cc69">The Service Port</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="e0cf8396-b271-4626-b8be-080047f2cc69"> </ac:inline-comment-marker></span></span><em style="text-align: center;"><ac:inline-comment-marker ac:ref="e0cf8396-b271-4626-b8be-080047f2cc69">iPayment</ac:inline-comment-marker></em><span style="color: rgb(128,128,128);"><span><ac:inline-comment-marker ac:ref="e0cf8396-b271-4626-b8be-080047f2cc69"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="e0cf8396-b271-4626-b8be-080047f2cc69">is created using Behavior to Structure Synchronization solver.</ac:inline-comment-marker></span></h6>
````

<!--NOMAGIC_PAGE id=228985862 space=VR version=1 -->
## PAGE 00284: ServicesBToSSync 2

- page_id: `228985862`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985862/ServicesBToSSync+2
- version_number: 1
- version_date: `2023-04-26T07:59:20.924+02:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

ServicesBToSSync[2]

**Description**

No compatible ServiceConnector. The second validation rule checks whether a Service Connector exists between the two compatible Service Ports owned by the Asset Roles. The missing Service Connectors can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

**Create Service Connector** - creates a missing Service Connector between the two compatible Service Ports.

**Example**

**[IMAGE alt='' src='']**

###### Creating a Service Connector that is missing in the Service Internal Connectivity Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ServicesBToSSync[2]</p><p><strong>Description</strong></p><p><ac:inline-comment-marker ac:ref="670a3714-f597-460c-a0cf-5e4db118a57a">No compatible <span style="color: rgb(62,63,64);">Service </span>Connector.</ac:inline-comment-marker> <span style="color: rgb(62,63,64);">The second validation rule checks whether a Service Connector exists between the two compatible Service Ports owned by the <ac:inline-comment-marker ac:ref="f87fe1a4-f757-4797-b21d-b5fc6535cdee">Asset</ac:inline-comment-marker> Roles. The missing Service Connectors can be handled automatically using solvers.</span></p><p><strong style="letter-spacing: 0.0px;">Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Create Service Connector</strong> - creates a missing Service Connector between the two compatible Service Ports. </p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="UAF_behavior_to_structure_services_connectors_validation_rule_process.png" /></ac:image></strong></p><h6 style="text-align: center;">Creating a Service Connector that is missing in the Service Internal Connectivity Diagram.</h6>
````

<!--NOMAGIC_PAGE id=228985866 space=VR version=1 -->
## PAGE 00285: ServicesBToSSync 3

- page_id: `228985866`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985866/ServicesBToSSync+3
- version_number: 1
- version_date: `2024-01-08T14:06:24.922+01:00`
- ancestors: Validation Rules > UAF validation rules > Correctness validation rules
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

**Abbreviation**

ServicesBToSSync[3]

**Description**

No compatible Service Exchange realization. The third validation rule checks realized Service Exchanges in Activities and help to ensure the correct Service Exchanges are realized on Service Connectors that connect Service Ports typed by compatible Service Interface.Themissing Exchanges can be handled automatically using solvers.

**Severity**

warning****

**Constrained Element**

Diagram****

**Solvers**

- Realize Missing Service Exchange - r ealizes existing compatible Service Exchange found in the behavior model on the Service Connector .
- Open Service Exchange Manager - opens the Service Exchange Manager dialog.
- Change Exchange Realization Compatibility Checking - opens the Project Options dialog to turn on/off the Exchange realization checking.

**Example**

[IMAGE alt='' src='']

###### Realizing a missing Operational Exchange on the Connector in the Operational Internal Connectivity Diagram.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>ServicesBToSSync[3]</p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">No compatible Service Exchange realization. The third validation rule checks realized Service Exchanges in Activities and help to ensure the correct Service Exchanges are realized on Service Connectors that connect Service Ports typed by compatible Service Interface.<span> </span></span><span style="color: rgb(62,63,64);">The</span><span style="color: rgb(62,63,64);"><span> </span>missing Exchanges can be handled automatically using solvers.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Realize Missing Service Exchange</strong> - <span style="color: rgb(62,63,64);">r</span><span style="color: rgb(23,43,77);">ealizes existing compatible Service Exchange found in the behavior model on the Service Connector</span><span style="color: rgb(62,63,64);">.</span></li><li><strong>Open Service Exchange Manager</strong> - opens the <strong>Service Exchange</strong><strong> Manager</strong> dialog.</li><li><strong>Change Exchange Realization Compatibility Checking</strong> - <span style="color: rgb(62,63,64);">opens the<span> </span></span><strong style="text-align: left;">Project Options</strong><span style="color: rgb(62,63,64);"><span> </span>dialog to turn on/off the Exchange realization checking. </span> <span style="letter-spacing: 0.0px;"> </span></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="UAF_behavior_to_structure_services_exchanges_validation_rule_process.png" /></ac:image></p><h6 style="text-align: center;"><ac:inline-comment-marker ac:ref="5d5b7f9e-ce01-4e9c-a49f-30f4811c5bec">Realizing a missing Operational Exchange on the Connector in the Operational Internal Connectivity Diagram.</ac:inline-comment-marker></h6>
````

<!--NOMAGIC_PAGE id=85766738 space=VR version=8 -->
## PAGE 00286: Signal incompatible with Proxy Port

- page_id: `85766738`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/85766738/Signal+incompatible+with+Proxy+Port
- version_number: 8
- version_date: `2022-03-30T10:36:50.141+02:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Activities
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

SignalIncWithProxyPort

**Description**

This validation rule checks if:

- The Send Signal Action uses a compatible Proxy Port in the On Port property to transmit the Signal.
- The Accept Event Action uses a compatible Proxy Port in the Port property to transmit the Signal.

The validation rule checks each Proxy Port's flow property type, direction, and evaluates isConjugated value to determine if the specified Proxy Port is capable of transmitting the Signal.

**Severity**

warning****

**Constrained Element**

SendSignalAction, AcceptEventAction

**Solvers**

To fix this, select the Action with the failed validation, click the warning icon in the smart manipulator toolbar and select one of the following:

- Remove '<Port>' Port - removes the incompatible port from the On Port/Port property.
- Replace '<Port>' Port with Compatible - removes the incompatible port from the On Port/Port property and provides a list of compatible Proxy Ports for replacing the incompatible port.

**Example**

[IMAGE alt='' src='']

###### The *Sys not Ok* Send Signal Action should use Proxy Port *out p2* instead of *in p1*. The *Stop* Accept Event Action should use Proxy Port *in p1* instead of *out p2*.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>SignalIncWithProxyPort</p><p><strong>Description</strong></p><p>This validation rule checks if:</p><ul><li>The Send Signal Action uses a compatible Proxy Port in the On Port property to transmit the Signal.</li><li>The Accept Event Action uses a compatible Proxy Port in the Port property to transmit the Signal.</li></ul><p>The validation rule checks each Proxy Port's flow property type, direction, and evaluates isConjugated value to determine if the specified Proxy Port is capable of transmitting the Signal. </p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>SendSignalAction, AcceptEventAction</p><p><strong>Solvers</strong></p><p>To fix this, select the Action with the failed validation, click the warning icon in the <span style="color: rgb(62,63,64);">smart manipulator toolbar</span> and select one of the following:</p><ul><li><strong>Remove '&lt;Port&gt;' Port </strong>- removes the incompatible port from the On Port/Port property.</li><li><strong>Replace '&lt;Port&gt;' Port with Compatible </strong>- removes the incompatible port from the On Port/Port property and provides a list of compatible Proxy Ports for replacing the incompatible port.</li></ul><p><strong>Example</strong></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Send Signal and Accept Event Action On Port and Port property incompatible with Proxy Port.png" /></ac:image></p><h6 style="text-align: center;">The <em>Sys not Ok</em> Send Signal Action should use Proxy Port <em>out p2</em> instead of <em>in p1</em>. The <em>Stop</em> Accept Event Action should use Proxy Port <em>in p1</em> instead of <em>out p2</em>.</h6>
````

<!--NOMAGIC_PAGE id=243969533 space=VR version=1 -->
## PAGE 00287: Slot multiplicity 2

- page_id: `243969533`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969533/Slot+multiplicity+2
- version_number: 1
- version_date: `2025-07-31T10:51:31.913+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

SlotMult2

**Description**

This validation rule checks if the number of Slot Values is in the multiplicity range. The validation rule is triggered if there are fewer values than the set multiplicity range.

**Severity**

warning

**Constrained Element**

Slot

**Solvers**

- To fix this, make sure the number of Slot Values is not lower than the specified multiplicity range.

**Example**

**[IMAGE alt='' src='']**

###### The Instance Specification *car Models* is typed by the Class *Car Models*, which as an attribute *Sedan*typed by an Enumeration *Airbag Types*with the multiplicity set to four. The Instance Specification's Slot *Sedan*is specified with one value instead of four causing the error. 
The error is resolved by specifying the Slot with four values.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>SlotMult2</p><p><strong>Description</strong></p><p>This validation rule checks if the number of Slot Values is in the multiplicity range. The validation rule is triggered if there are fewer values than the set multiplicity range.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>Slot</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the number of Slot Values is not lower than the specified multiplicity range.</li></ul><p><strong><ac:inline-comment-marker ac:ref="de566b2c-e1e7-4c85-9936-881513af3bb7">Example</ac:inline-comment-marker></strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="Slot multiplicity 2.png" /></ac:image></strong></p><h6 style="text-align: center;">The Instance Specification <em>car Models</em> is typed by the Class <em>Car Models</em>, which as an attribute <em>Sedan </em>typed by an Enumeration <em>Airbag Types </em>with the multiplicity set to four. The Instance Specification's Slot <em>Sedan </em>is specified with one value instead of four causing the error.<br />The error is resolved by specifying the Slot with four values.</h6>
````

<!--NOMAGIC_PAGE id=20845959 space=VR version=4 -->
## PAGE 00288: Suspect Unlinked Requirement

- page_id: `20845959`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/20845959/Suspect+Unlinked+Requirement
- version_number: 4
- version_date: `2022-10-31T08:42:31.366+01:00`
- ancestors: Validation Rules > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

UnlinkReq****

**Description**

This validation rule checks if there are any unlinked elements.****

**Severity**

warning****

**Context element**

Abstract Requirement****

**Solvers**

- To fix this, make sure the requirement has a Satisfy, Verify, Refine, or deriveReq relationship with the corresponding element.

**Example**

[IMAGE alt='' src='']

###### The Requirement *Vehicle's battery energy consumption* is unlinked from the *energyConsumption* Value Property of the *High-voltage Battery* Block. 
The error is resolved by re-creating the Satisfy relationship between the Requirement and the Value Property.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>UnlinkReq<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if there are any unlinked elements.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Abstract Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><ac:inline-comment-marker ac:ref="6d6f2f5f-2850-4c0b-82af-14679ece1447">To fix this, make sure the requirement has a Satisfy, Verify, Refine, or deriveReq relationship with the corresponding element.</ac:inline-comment-marker></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Suspect_Unlinked_Requirement.png" /></ac:image></p><h6 style="text-align: center;">The Requirement <em>Vehicle's battery energy consumption</em> is unlinked from the <em>energyConsumption</em> Value Property of the <em>High-voltage Battery</em> Block. <br />The error is resolved by re-creating the Satisfy relationship between the Requirement and the Value Property.</h6>
````

<!--NOMAGIC_PAGE id=249004904 space=VR version=2 -->
## PAGE 00289: SysML v1 validation rules

- page_id: `249004904`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/249004904/SysML+v1+validation+rules
- version_number: 2
- version_date: `2025-08-25T12:26:58.901+02:00`
- ancestors: Validation Rules
- labels: []

### NORMALIZED CONTENT

This page contains all SysML constraints implemented in the tool as validation rules. You can find the rules in the validation suite ([CONFLUENCE_PAGE title='SysML validation suites' space='SYSMLPTWRT']) and active validation suite ([CONFLUENCE_PAGE title='SysML active validation suites' space='SYSMLPTWRT']) Packages stored under the **Auxiliary Resources** > **MD Customization for SysML** > **SysML constraints**.

The SysML validation suites and active validation suites include the following validation rules:

The list below displays only a few SysML v1 validation rules.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This page contains all SysML constraints implemented in the tool as validation rules. You can find the rules in the validation suite (<ac:link><ri:page ri:space-key="SYSMLPTWRT" ri:content-title="SysML validation suites" /><ac:plain-text-link-body><![CDATA[SysML ValSuite]]></ac:plain-text-link-body></ac:link>) and active validation suite (<ac:link><ri:page ri:space-key="SYSMLPTWRT" ri:content-title="SysML active validation suites" /><ac:plain-text-link-body><![CDATA[SysML activeValSuite]]></ac:plain-text-link-body></ac:link>) Packages stored under the <strong>Auxiliary Resources</strong> &gt; <strong>MD Customization for SysML</strong> &gt; <strong>SysML constraints</strong>.</p><p>The SysML validation suites and active validation suites include the following validation rules:</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="733f4481-2f2a-40f1-a1f4-cb11f89284db"><ac:rich-text-body><p>The list below displays only a few SysML v1 validation rules.</p></ac:rich-text-body></ac:structured-macro><p><br /><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f0b2b1e4-0a26-4fd4-b6b6-18c0e7620364" /></p>
````

<!--NOMAGIC_PAGE id=267026804 space=VR version=3 -->
## PAGE 00290: Systems Cybersecurity Designer validation rules

- page_id: `267026804`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/267026804/Systems+Cybersecurity+Designer+validation+rules
- version_number: 3
- version_date: `2025-10-29T09:47:53.716+01:00`
- ancestors: Validation Rules
- labels: []

### NORMALIZED CONTENT

To learn more about the Systems Cybersecurity Designer validation rules, refer to the following pages:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To learn more about the Systems Cybersecurity Designer validation rules, refer to the following pages:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="631e4d22-6d87-48b9-b0f0-237ebcda54fc" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969536 space=VR version=1 -->
## PAGE 00291: Tags multiplicity 2

- page_id: `243969536`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969536/Tags+multiplicity+2
- version_number: 1
- version_date: `2025-07-31T10:51:32.009+02:00`
- ancestors: Validation Rules > UML validation rules > UML completeness constraints rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

TagMult2

**Description**

This validation rule checks if the number of tag values is in the multiplicity range. The validation rule is triggered if there are fewer values than the set multiplicity range.

**Severity**

warning

**Constrained Element**

TaggedValue

**Solvers**

- To fix this, make sure the number of tag values is not lower than the specified multiplicity range.

**Example**

###### **[IMAGE alt='' src='']**The Stereotype *Car* has a tag definition *airbags* with a multiplicity of two or more. The class *Car Model 1*with the applied stereotype *Car*has the *airbags*tag specified with only one value, which causes an error. 
The error is resolved by specifying two values.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Abbreviation</strong></p><p>TagMult2</p><p><strong>Description</strong></p><p>This validation rule checks if the number of tag values is in the multiplicity range. The validation rule is triggered if there are fewer values than the set multiplicity range.</p><p><strong>Severity</strong></p><p>warning</p><p><strong>Constrained Element</strong></p><p>TaggedValue</p><p><strong>Solvers</strong></p><ul><li>To fix this, make sure the number of tag values is not lower than the specified multiplicity range.</li></ul><p><strong><ac:inline-comment-marker ac:ref="844f9cdb-b9ab-4de6-af39-8d12da834add">Example</ac:inline-comment-marker></strong></p><h6 style="text-align: center;"><strong><ac:image><ri:attachment ri:filename="Tags multiplicity 2.png" /></ac:image><br /></strong>The Stereotype <em>Car</em> has a tag definition <em>airbags</em> with a multiplicity of two or more. The class <em>Car Model 1 </em>with the applied stereotype <em>Car </em>has the <em>airbags </em>tag specified with only one value, which causes an error.<br />The error is resolved by specifying two values.</h6>
````

<!--NOMAGIC_PAGE id=17684421 space=VR version=7 -->
## PAGE 00292: Testcase Verdict

- page_id: `17684421`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/17684421/Testcase+Verdict
- version_number: 7
- version_date: `2020-12-07T07:29:48.526+01:00`
- ancestors: Validation Rules > SysML v1 validation rules > Validation rules of Non-normative Extensions
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

NoVerdict****

**Description**

This rulechecks if theTestcase returns a parameter typed by the VerdictKind.

**Severity**

warning****

**Constrained Element**

Behavior, Operation****

**Solvers**

**Create Verdict** - creates return parameter typed by the VerdictKind.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>NoVerdict<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule </span><span style="color: rgb(62,63,64);">checks if t</span><span style="color: rgb(62,63,64);">he </span>Testcase returns a parameter typed by the VerdictKind.</p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Behavior, Operation<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Create Verdict</strong> - creates return parameter typed by the VerdictKind.</p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="testCase_verdict.png" /></ac:image><br /></strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=228985491 space=VR version=2 -->
## PAGE 00293: UAF validation rules

- page_id: `228985491`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/228985491/UAF+validation+rules
- version_number: 2
- version_date: `2025-08-14T14:53:15.722+02:00`
- ancestors: Validation Rules
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="dcf71292-afec-448d-b8b0-4307e6dd448a" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=243969478 space=VR version=1 -->
## PAGE 00294: UML completeness constraints rules

- page_id: `243969478`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969478/UML+completeness+constraints+rules
- version_number: 1
- version_date: `2025-07-31T10:51:30.032+02:00`
- ancestors: Validation Rules > UML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides detailed descriptions of all validation rules that belong to the**UML completeness constraints**validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section provides detailed descriptions of all validation rules that belong to the<span> <strong>UML completeness constraints</strong></span><span> </span>validation suite.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5a634fd5-42f6-4367-a790-84f17531ca06" /></p>
````

<!--NOMAGIC_PAGE id=243969539 space=VR version=1 -->
## PAGE 00295: UML correctness constraints rules

- page_id: `243969539`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969539/UML+correctness+constraints+rules
- version_number: 1
- version_date: `2025-07-31T10:51:32.103+02:00`
- ancestors: Validation Rules > UML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belong to the **UML correctness constraints** validation suite.

The list below displays only a few UML validation rules. The rest are under construction.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section provides the detailed descriptions of all validation rules that belong to the <strong>UML correctness constraints</strong> validation suite.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="733f4481-2f2a-40f1-a1f4-cb11f89284db"><ac:rich-text-body><p>The list below displays only a few UML validation rules. The rest are under construction.</p></ac:rich-text-body></ac:structured-macro><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f80edc37-da91-4f89-9f90-b0c1d5a66411" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=243969471 space=VR version=3 -->
## PAGE 00296: UML validation rules

- page_id: `243969471`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243969471/UML+validation+rules
- version_number: 3
- version_date: `2025-08-14T16:34:50.199+02:00`
- ancestors: Validation Rules
- labels: []

### NORMALIZED CONTENT

This page contains all the UML constraints implemented in the tool as validation rules. You can find the rules in the [CONFLUENCE_PAGE title='Predefined validation suites' space='MT'] and the [CONFLUENCE_PAGE title='Active validation suites' space='MT'] packages stored under the **Auxiliary Resources** > **UML Standard Profile** > **Validation Profile**. The UML predefined validation suites and active validation suites include the following validation rules:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This page contains all the UML constraints implemented in the tool as validation rules. You can find the rules in the <ac:link><ri:page ri:space-key="MT" ri:content-title="Predefined validation suites" /><ac:plain-text-link-body><![CDATA[predefined validation suites]]></ac:plain-text-link-body></ac:link> and the <ac:link><ri:page ri:space-key="MT" ri:content-title="Active validation suites" /><ac:plain-text-link-body><![CDATA[active validation suites]]></ac:plain-text-link-body></ac:link> packages stored under the <strong style="letter-spacing: 0.0px;">Auxiliary Resources</strong> &gt; <strong style="letter-spacing: 0.0px;">UML Standard Profile</strong> &gt; <strong style="letter-spacing: 0.0px;">Validation Profile</strong>. The UML predefined validation suites and active validation suites include the following validation rules:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7b5ca5d7-8ac3-4da1-a496-2062a37e065a" /></p>
````

<!--NOMAGIC_PAGE id=243971673 space=VR version=4 -->
## PAGE 00297: Validation Rules

- page_id: `243971673`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/243971673/Validation+Rules
- version_number: 4
- version_date: `2025-11-25T16:45:30.048+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

This guide describes SysML v1, UAF, and UML validation rules. To learn more, see the following topics:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#172b4d);">This guide describes SysML v1, UAF, and UML validation rules. To learn more, see the following topics:</span></p><p><span style="color:var(--ds-text,#172b4d);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9c3c62ba-5e38-4155-b54d-fa8ea926fc49" /></span></p>
````

<!--NOMAGIC_PAGE id=68526119 space=VR version=8 -->
## PAGE 00298: Validation rules of Activities

- page_id: `68526119`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/68526119/Validation+rules+of+Activities
- version_number: 8
- version_date: `2024-01-29T12:10:53.332+01:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belong to active and passive*Activites*validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belong to active and passive </span><em>Activites</em><span style="color: rgb(62,63,64);"> validation suite.</span></p><p><span style="color: rgb(62,63,64);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8b218e6c-0974-402c-8d53-a799fccf94f9" /></span></p>
````

<!--NOMAGIC_PAGE id=68526121 space=VR version=6 -->
## PAGE 00299: Validation rules of Allocations

- page_id: `68526121`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/68526121/Validation+rules+of+Allocations
- version_number: 6
- version_date: `2024-01-29T11:22:37.737+01:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Allocations***validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Allocations</em></span><span style="color: rgb(62,63,64);"><em> </em>validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="231e3b0d-f393-4be4-baaf-36c4da9a2ad1" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=70390262 space=VR version=5 -->
## PAGE 00300: Validation rules of Behavior to Structure Synchronization

- page_id: `70390262`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/70390262/Validation+rules+of+Behavior+to+Structure+Synchronization
- version_number: 5
- version_date: `2024-01-29T09:35:53.667+01:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belong to the passive Behavior to Structure Synchronization**validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belong to <ac:inline-comment-marker ac:ref="b3a26d4c-e766-4621-9600-30ab00191223">the passive</ac:inline-comment-marker> Behavior to Structure Synchronization</span><span style="color: rgb(62,63,64);"><em> </em></span><span style="color: rgb(62,63,64);">validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d95b5232-42b2-4a7b-b9e2-6f35266387dc" /></p>
````

<!--NOMAGIC_PAGE id=68526123 space=VR version=5 -->
## PAGE 00301: Validation rules of Blocks

- page_id: `68526123`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/68526123/Validation+rules+of+Blocks
- version_number: 5
- version_date: `2024-01-29T11:41:16.563+01:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Blocks***validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Blocks</em></span><span style="color: rgb(62,63,64);"><em> </em>validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="6672bfd9-d612-40b7-a913-8d33bdf79a0c" /></p>
````

<!--NOMAGIC_PAGE id=68526125 space=VR version=4 -->
## PAGE 00302: Validation rules of Contextual Relationships

- page_id: `68526125`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/68526125/Validation+rules+of+Contextual+Relationships
- version_number: 4
- version_date: `2021-01-01T08:29:28.840+01:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Contextual Relationships***validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Contextual Relationships</em></span><span style="color: rgb(62,63,64);"><em> </em>validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="911a68ce-172a-45e2-b479-369ea5733e9d" /></p>
````

<!--NOMAGIC_PAGE id=64973669 space=VR version=8 -->
## PAGE 00303: Validation rules of Non-normative Extensions

- page_id: `64973669`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/64973669/Validation+rules+of+Non-normative+Extensions
- version_number: 8
- version_date: `2024-01-29T11:46:49.322+01:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Non-normative Extensions* validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Non-normative Extensions</em> validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e46f07c5-69de-43d0-9777-938fcd3fad23" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=100207360 space=VR version=5 -->
## PAGE 00304: Validation rules of Ports and Flows

- page_id: `100207360`
- space_key: `VR`
- source_url: https://docs.nomagic.com/spaces/VR/pages/100207360/Validation+rules+of+Ports+and+Flows
- version_number: 5
- version_date: `2025-08-25T09:59:17.310+02:00`
- ancestors: Validation Rules > SysML v1 validation rules
- labels: []

### NORMALIZED CONTENT

This section provides detailed descriptions of all validation rules that belong to the active and passive*Ports and Flows*validation suites.

The list below displays only a few SysML validation rules.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color:var(--ds-text,#333333);">This section provides detailed descriptions of all validation rules that belong to the active and passive </span><em>Ports and Flows</em><span style="color:var(--ds-text,#333333);"> validation suites.</span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="733f4481-2f2a-40f1-a1f4-cb11f89284db"><ac:rich-text-body><p>The list below displays only a few SysML validation rules. </p></ac:rich-text-body></ac:structured-macro><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="fdcdea8c-a1b3-400e-bacb-d833a3065ebe" /></p>
````
