# NOMAGIC DOCUMENTATION SPACE: Cameo Business Modeler Plugin 2024x

<!--NOMAGIC_SPACE key=CBMP2024x chunk=1 -->

<!--NOMAGIC_PAGE id=290031677 space=CBMP2024x version=2 -->
## PAGE 00001: 2024x Version News

- page_id: `290031677`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031677/2024x+Version+News
- version_number: 2
- version_date: `2026-02-11T11:52:30.865+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation
- labels: []

### NORMALIZED CONTENT

### Cameo Business Modeler Plugin

Released on: November 10, 2023

The version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.

Check the product compatibility [CONFLUENCE_PAGE title='Product compatibility' space='NMDOC'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="line-height: 1.66667;letter-spacing: normal;text-align: center;">Cameo Business Modeler Plugin</h1><p style="text-align: center;"><span style="color:var(--ds-text,#707070);">Released on: November 10</span><span style="color:var(--ds-text,#707070);">, 2023</span></p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.</p><p>Check the product compatibility <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Product compatibility" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031708 space=CBMP2024x version=1 -->
## PAGE 00002: Activities

- page_id: `290031708`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031708/Activities
- version_number: 1
- version_date: `2026-02-09T13:51:12.105+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

An Activity is a work that is performed within a business process. An Activity can be atomic or non-atomic (compound). There are three types of Activities that are part of a Process:

If the Activity property Is For Compensation is set to true, the Activity will be used for compensation, which means that this Activity will be activated only when a Compensation Event is detected and initiated under the Compensation Event visibility scope. The Compensation indicator (marker) is displayed for all activities that are used for the compensation.

- Compensation Task with Compensation indicator [ATTACHMENT filename='task_compensation.png']
- Compensation SubProcess with Compensation indicator [ATTACHMENT filename='subprocess_compensation.png']

Activities can be repeated sequentially, essentially behaving like a loop. The presence of loop characteristics signifies that an Activity has the looping behavior. There are two types of looping characteristics defined in BPMN:

- Standard Loop. A Standard Loop indicator (marker) displayed in an Activity shape shows that the looping behavior based on a boolean condition is defined for this Activity. Additional looping characteristics can be defined, and the Activity will loop as long as the boolean condition is true. The condition is evaluated for every loop iteration and can be evaluated at the beginning or end of the iteration. In addition, a numeric cap can be optionally specified, but the number of iterations cannot exceed this cap.
  - Task with Standard Loop marker [ATTACHMENT filename='task_standard_loop.png']
  - SubProcess with Standard Loop marker [ATTACHMENT filename='subprocess_standard_loop.png']
- MultiInstance Loop. A MultiInstance Loop indicator shows that a desired number of Activity instances can be created. The instances can be executed in parallel or sequentially. Either expression is used to specify the desired number of instances or a data driven setup that can be used.
  - Task with MultiInstance Loop marker for parallel instances 
[IMAGE alt='' src='']
  - SubProcess with MultiInstance Loop marker for parallel instances 
[IMAGE alt='' src='']
  - Task with MultiInstance Loop marker for sequential instances 
[IMAGE alt='' src='']
  - SubProcess with MultiInstance Loop marker for sequential instances [ATTACHMENT filename='sun_multi_par_seq.png']

The Compensation, Multi-instance Loop, and Standard Loop indicators can be added to all types of Activities.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An Activity is a work that is performed within a business process. An Activity can be atomic or non-atomic (compound). There are three types of Activities that are part of a Process:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f66051d6-e804-413f-8aea-802e12fc6c57" /></p><p>If the Activity property Is For Compensation is set to true, the Activity will be used for compensation, which means that this Activity will be activated only when a Compensation Event is detected and initiated under the Compensation Event visibility scope. The Compensation indicator (marker) is displayed for all activities that are used for the compensation.</p><ul><li>Compensation Task with Compensation indicator<br /><ac:image><ri:attachment ri:filename="task_compensation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></li><li>Compensation SubProcess with Compensation indicator<br /><ac:image><ri:attachment ri:filename="subprocess_compensation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></li></ul><p>Activities can be repeated sequentially, essentially behaving like a loop. The presence of loop characteristics signifies that an Activity has the looping behavior. There are two types of looping characteristics defined in BPMN:</p><ul><li>Standard Loop. A Standard Loop indicator (marker) displayed in an Activity shape shows that the looping behavior based on a boolean condition is defined for this Activity. Additional looping characteristics can be defined, and the Activity will loop as long as the boolean condition is true. The condition is evaluated for every loop iteration and can be evaluated at the beginning or end of the iteration. In addition, a numeric cap can be optionally specified, but the number of iterations cannot exceed this cap.<ul><li>Task with Standard Loop marker<br /><ac:image><ri:attachment ri:filename="task_standard_loop.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></li><li>SubProcess with Standard Loop marker<br /><ac:image><ri:attachment ri:filename="subprocess_standard_loop.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></li></ul></li><li><p>MultiInstance Loop. A MultiInstance Loop indicator shows that a desired number of Activity instances can be created. The instances can be executed in parallel or sequentially. Either expression is used to specify the desired number of instances or a data driven setup that can be used.</p><ul><li><p>Task with MultiInstance Loop marker for parallel instances<br /><ac:image><ri:attachment ri:filename="task_multi_par.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></p></li><li><p>SubProcess with MultiInstance Loop marker for parallel instances<br /><ac:image><ri:attachment ri:filename="sun_multi_par.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></p></li><li><p>Task with MultiInstance Loop marker for sequential instances<br /><ac:image><ri:attachment ri:filename="task_multi_par_seq.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></p></li><li>SubProcess with MultiInstance Loop marker for sequential instances<br /><ac:image><ri:attachment ri:filename="sun_multi_par_seq.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Activities" /></ri:attachment></ac:image></li></ul></li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="78303b38-7a07-479f-9c99-d0b24fc412d5"><ac:rich-text-body><p>The Compensation, Multi-instance Loop, and Standard Loop indicators can be added to all types of Activities.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=290031738 space=CBMP2024x version=1 -->
## PAGE 00003: AdHoc SubProcess

- page_id: `290031738`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031738/AdHoc+SubProcess
- version_number: 1
- version_date: `2026-02-09T13:52:59.379+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > SubProcesses
- labels: []

### NORMALIZED CONTENT

**Description**

An AdHoc SubProcess is a specialized type of SubProcess, which is a group of activities that have no required sequence relationships. A set of activities can be defined for the process, but the sequence and number of performances for the activities are determined by the performers of the activities.

**Notation**

- Expanded [ATTACHMENT filename='expanded_adhoc.png']
- Collapsed [ATTACHMENT filename='suppressed_adhoc.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An AdHoc SubProcess is a specialized type of SubProcess, which is a group of activities that have no required sequence relationships. A set of activities can be defined for the process, but the sequence and number of performances for the activities are determined by the performers of the activities.</p><p><strong>Notation</strong></p><ul><li>Expanded<br /><ac:image><ri:attachment ri:filename="expanded_adhoc.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="AdHoc SubProcess" /></ri:attachment></ac:image></li><li>Collapsed<br /><ac:image><ri:attachment ri:filename="suppressed_adhoc.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="AdHoc SubProcess" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031694 space=CBMP2024x version=1 -->
## PAGE 00004: Anchor

- page_id: `290031694`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031694/Anchor
- version_number: 1
- version_date: `2026-02-09T13:48:29.120+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Common BPMN Elements > Artifacts
- labels: []

### NORMALIZED CONTENT

**Description**

An Anchor is used to associate a Text Annotation, Note, or Comment with the other diagram elements.

**Example**

**[IMAGE alt='' src='']**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Anchor is used to associate a Text Annotation, Note, or Comment with the other diagram elements.</p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="anchor.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Anchor" /></ri:attachment></ac:image></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031693 space=CBMP2024x version=1 -->
## PAGE 00005: Artifacts

- page_id: `290031693`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031693/Artifacts
- version_number: 1
- version_date: `2026-02-09T13:48:22.433+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Common BPMN Elements
- labels: []

### NORMALIZED CONTENT

Artifacts provide modelers with the capability to show additional information about a process.

This information is not directly related to a sequence or message flow of the process.

Types of Artifacts are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Artifacts provide modelers with the capability to show additional information about a process.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1f9fef4d-e0a1-4632-a016-fc715ae69da7"><ac:rich-text-body><p>This information is not directly related to a sequence or message flow of the process.</p></ac:rich-text-body></ac:structured-macro><p>Types of Artifacts are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="078ed980-0d83-4f43-8c1f-8ae66343a5cc" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031998 space=CBMP2024x version=1 -->
## PAGE 00006: Assessment

- page_id: `290031998`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031998/Assessment
- version_number: 1
- version_date: `2026-02-09T15:12:19.825+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Assessment Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

An Assessment is a judgment of some Influencer that affects the ability of organization to employ its Means or achieve its Ends. In other words, an Assessment expresses a logical connection or fact type between Influencers and the Ends and/or Means of the business plans. In this way, an Assessment indicates which Influencers are relevant to which Ends and/or Means.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Assessment Concepts
- Assessment Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Assessment is a judgment of some Influencer that affects the ability of organization to employ its Means or achieve its Ends. In other words, an Assessment expresses a logical connection or fact type between Influencers and the Ends and/or Means of the business plans. In this way, an Assessment indicates which Influencers are relevant to which Ends and/or Means.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="assesment.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concepts">Assessment Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concept+Relationships" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Assessment Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032004 space=CBMP2024x version=1 -->
## PAGE 00007: Assessment Concept Relationships

- page_id: `290032004`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032004/Assessment+Concept+Relationships
- version_number: 1
- version_date: `2026-02-09T15:29:26.777+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Assessment Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

The following table provides the relationships that exist between element types and their meaning.

| Relationship | Description | Example |
| --- | --- | --- |
| Identifies | This link connects to a or . Meaning that the Assessment points out some possible Potential Reward or Risk that is/are significant to that Assessment. Each possible consequence serves as an appraisal of the worth, value, or quality of some aspect of the Assessment in specific terms, types, or dimensions. |  |
| ProvidesImpetus | This link connects to a or . Meaning that the Assessment is the driving force for the Business Policy or Business Rule. |  |
| AffectsAchievements | This link connects to a , , or . Meaning that the Assessment has an impact on the End outcomes. |  |
| AffectsEmployment | This link connects to a , , , or . Meaning that the Assessment has an impact on the use of Means. |  |
| JudgementFor | This link connects to a Influencer ( or ). Meaning that the Assessment is the Influencer’s judgment that influences the organization’s ability to carry out its Means or achieve its Ends. |  |

**Related element**

- Assessment Concepts

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>The following table provides the relationships that exist between element types and their meaning.</p><table class="relative-table wrapped" style="width: 2059.95px;"><colgroup><col style="width: 210.594px;" /><col style="width: 1303.06px;" /><col style="width: 545.297px;" /></colgroup><tbody><tr><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Relationship </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Description </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);"><p style="color:var(--ds-text,#172b4d);">Example</p></th></tr><tr><td style="">Identifies</td><td style=""><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Potential Reward" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Risk" /></ac:link>. Meaning that the Assessment points out some possible Potential Reward or Risk that is/are significant to that Assessment. Each possible consequence serves as an appraisal of the worth, value, or quality of some aspect of the Assessment in specific terms, types, or dimensions.</p></td><td style=""><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="identifies.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td style=""><p>Provides<br />Impetus</p></td><td style=""><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link>. Meaning that the Assessment is the driving force for the Business Policy or Business Rule.</p></td><td style=""><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="provides_impetus.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td style=""><p>Affects<br />Achievements</p></td><td style=""><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Vision" /></ac:link>, <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Goal" /></ac:link>, or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Objective" /></ac:link>. Meaning that the Assessment has an impact on the End outcomes.</p></td><td style=""><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="affects_achievements.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td style=""><p>Affects<br />Employment</p></td><td style=""><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Mission" /></ac:link>, <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /></ac:link>, <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link>, <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link>. Meaning that the Assessment has an impact on the use of Means.</p></td><td style=""><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="affects_employment.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td style=""><p>Judgement<br />For</p></td><td style=""><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment" /></ac:link> to a Influencer (<ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="External Influencer" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Internal Influencer" /></ac:link>). Meaning that the Assessment is the Influencer’s judgment that influences the organization’s ability to carry out its Means or achieve its Ends.</p></td><td style=""><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="judgement_for.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Assessment Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr></tbody></table><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concepts">Assessment Concepts</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031997 space=CBMP2024x version=1 -->
## PAGE 00008: Assessment Concepts

- page_id: `290031997`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031997/Assessment+Concepts
- version_number: 1
- version_date: `2026-02-09T15:11:52.274+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram
- labels: []

### NORMALIZED CONTENT

The Assessment element is the Influencer's assessment of the organization ends and means including the activities, events, and data that trigger or feed business activities.

There are three types of Assessment elements:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Assessment element is the Influencer's assessment of the organization ends and means including the activities, events, and data that trigger or feed business activities.</p><p>There are three types of Assessment elements:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="99ba7d1b-c0d0-46fb-b134-ab5a57f52a35" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031698 space=CBMP2024x version=1 -->
## PAGE 00009: Association

- page_id: `290031698`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031698/Association
- version_number: 1
- version_date: `2026-02-09T13:48:45.501+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Common BPMN Elements > Artifacts
- labels: []

### NORMALIZED CONTENT

**Description**

An Association link shows that particular classes are related to each other. Association links may have names defined – names help to read diagrams. You can also specify multiplicity at the end of an association.

**Example**

###### [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Association link shows that particular classes are related to each other. Association links may have names defined – names help to read diagrams. You can also specify multiplicity at the end of an association.</p><p><strong>Example</strong></p><h6 style="letter-spacing: normal;line-height: 1.66667;color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="association (1).png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Association" /></ri:attachment></ac:image></h6><p />
````

<!--NOMAGIC_PAGE id=290031813 space=CBMP2024x version=1 -->
## PAGE 00010: Boundary Events

- page_id: `290031813`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031813/Boundary+Events
- version_number: 1
- version_date: `2026-02-09T14:34:51.581+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

A Boundary Event is an Intermediate event which can be placed on the boundary of any of the following activities:

- SubProcess, Task, or Call Activity
- SubChoreography, Choreography Task, or Call Choreography

Boundary Event indicates that while attached-to Activity is running, event is listening for the trigger signal.

Boundary Event types:

- Interrupting Boundary Event aborts Activity and Process is continued of exceptional flow. This event is drawn with a solid border.
- Non-Interrupting Boundary Event splits process to parallel flows. This event is drawn with a dashed border.

[IMAGE alt='' src='']

###### Error Boundary Event attached to SubProcess.

Types of Boundary Events are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Boundary Event is an Intermediate event which can be placed on the boundary of any of the following activities:</p><ul><li>SubProcess, Task, or Call Activity</li><li>SubChoreography, Choreography Task, or Call Choreography</li></ul><p>Boundary Event indicates that while attached-to Activity is running, event is listening for the trigger signal.</p><p>Boundary Event types:</p><ul><li>Interrupting Boundary Event aborts Activity and Process is continued of exceptional flow. This event is drawn with a solid border.</li><li>Non-Interrupting Boundary Event splits process to parallel flows. This event is drawn with a dashed border.</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="boundary_error.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Boundary Events" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Error Boundary Event attached to SubProcess.</h6><p>Types of Boundary Events are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="dd5528d2-89f7-4470-8751-3f740afa86c7" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032054 space=CBMP2024x version=1 -->
## PAGE 00011: BPMN Activities Description Table

- page_id: `290032054`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032054/BPMN+Activities+Description+Table
- version_number: 1
- version_date: `2026-02-09T15:45:24.223+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > BPMN Tables
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Activities Description table is designed to display or edit selected process activities descriptions in a table form. A BPMN Activities Description table is created for a BPMN Process.

**Example**

[IMAGE alt='' src='']

###### BPMN Activities Description table.

**Related elements**

- Activities
- BPMN Tables

**Related procedure**

- Creating a Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Activities Description table is designed to display or edit selected process activities descriptions in a table form. A BPMN Activities Description table is created for a BPMN Process.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="activities_description_table.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Activities Description Table" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Activities Description table.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Tables">BPMN Tables</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032015 space=CBMP2024x version=1 -->
## PAGE 00012: BPMN Association

- page_id: `290032015`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032015/BPMN+Association
- version_number: 1
- version_date: `2026-02-09T15:31:02.329+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Data Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Association link shows that particular classes are related to each other. BPMN Association links may have names defined – names help to read diagrams. You can also specify multiplicity at the end of a BPMN Association.

**Example**

[IMAGE alt='' src='']

###### BPMN Association between two Classes with Multiplicity at the End.

**Related element**

- Class

**Related diagram**

- Business Data Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Association link shows that particular classes are related to each other. BPMN Association links may have names defined – names help to read diagrams. You can also specify multiplicity at the end of a BPMN Association.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="association_example.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Association" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Association between two Classes with Multiplicity at the End.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Data+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Business Data Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032052 space=CBMP2024x version=1 -->
## PAGE 00013: BPMN Business Data Description Table

- page_id: `290032052`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032052/BPMN+Business+Data+Description+Table
- version_number: 1
- version_date: `2026-02-09T15:44:52.700+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > BPMN Tables
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Business Data Description table is designed to display or edit class descriptions in a table form. You can display existing classes or create new classes in this table.

**Example**

[IMAGE alt='' src='']

###### BPMN Business Data Description table.

**Related elements**

- Class
- BPMN Tables

**Related procedure**

- Creating a Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Business Data Description table is designed to display or edit class descriptions in a table form. You can display existing classes or create new classes in this table.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="business_data_description_table.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Business Data Description Table" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Business Data Description table.</h6><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Tables">BPMN Tables</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031918 space=CBMP2024x version=1 -->
## PAGE 00014: BPMN Choreography Diagram

- page_id: `290031918`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031918/BPMN+Choreography+Diagram
- version_number: 1
- version_date: `2026-02-09T14:44:23.661+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Choreography formalizes the way business participants coordinate their interactions. A Choreography is a type of process, but its purpose and behavior are different from a standard BPMN process.

A standard process defines the flow of activities of a specific partner entity or organization. In contrast, a Choreography formalizes the way business participants coordinate their interactions. The focus is not on the work performed within these participants, but rather on the information (messages) exchanged between them.

A Choreography is a definition of expected behavior, basically a procedural business contract between interacting participants. It shows the messages exchanged and their logical relations. This allows business partners to plan their business processes for inter-operation without introducing conflicts.

[IMAGE alt='' src='']

###### BPMN Choreography diagram.

A BPMN Choreography diagram is based on the UML Activity diagram and includes restrictions and extensions as defined by BPMN.

Types of Choreography elements are as follows:

**Related elements**

- Choreography
- Choreography Activities
- Error
- Intermediate Catch Event
- Intermediate Throwing Event
- Boundary Events
- End Events
- Gateways

**Related diagram**

- BPMN Process Diagram

**Related procedure**

- Using BPMN Choreography Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Choreography formalizes the way business participants coordinate their interactions. A Choreography is a type of process, but its purpose and behavior are different from a standard BPMN process.</p><p>A standard process defines the flow of activities of a specific partner entity or organization. In contrast, a Choreography formalizes the way business participants coordinate their interactions. The focus is not on the work performed within these participants, but rather on the information (messages) exchanged between them.</p><p>A Choreography is a definition of expected behavior, basically a procedural business contract between interacting participants. It shows the messages exchanged and their logical relations. This allows business partners to plan their business processes for inter-operation without introducing conflicts.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="choreography_diagram.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Choreography Diagram" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Choreography diagram.</h6><p>A BPMN Choreography diagram is based on the UML Activity diagram and includes restrictions and extensions as defined by BPMN.</p><p>Types of Choreography elements are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="4d335140-5180-4a64-b441-3516fbfd43f8" /></p><p><br /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Choreography</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Error" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Error</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Gateways">Gateways</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Choreography+Diagram">Using BPMN Choreography Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031892 space=CBMP2024x version=1 -->
## PAGE 00015: BPMN Collaboration Diagram

- page_id: `290031892`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031892/BPMN+Collaboration+Diagram
- version_number: 1
- version_date: `2026-02-09T14:38:11.156+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Collaboration represents the interactions between two or more business entities. A Collaboration diagram depicts a global point of view. It shows the interactions between participants in general.

A Collaboration contains two or more pools, representing the participants in the collaboration. Messages exchanged between the participants are shown by message flows that connect two pools together (or objects within the pools).

[IMAGE alt='' src='']

###### Collaboration diagram with two Black Box Pools.

[IMAGE alt='' src='']

###### Collaboration diagram with two Pools showing process.

A Collaboration diagram can also show distinct conversations between collaborating participants in a domain. Communications are defined by the conversations, participants, and conversation links between them.

[IMAGE alt='' src='']

###### BPMN Collaboration diagram with Conversations.

The elements of a BPMN Process diagram can be displayed on the BPMN Collaboration diagram.

**Related element**

- BPMN Process

**Related diagram**

- BPMN Process Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Collaboration represents the interactions between two or more business entities. A Collaboration diagram depicts a global point of view. It shows the interactions between participants in general.</p><p>A Collaboration contains two or more pools, representing the participants in the collaboration. Messages exchanged between the participants are shown by message flows that connect two pools together (or objects within the pools).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="collaboration_I.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Collaboration Diagram" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Collaboration diagram with two Black Box Pools.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="collaboration_II.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Collaboration Diagram" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Collaboration diagram with two Pools showing process.</h6><p>A Collaboration diagram can also show distinct conversations between collaborating participants in a domain. Communications are defined by the conversations, participants, and conversation links between them.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="collaboration_III.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Collaboration Diagram" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">BPMN Collaboration diagram with Conversations.</h6><p>The elements of a BPMN Process diagram can be displayed on the BPMN Collaboration diagram.</p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032059 space=CBMP2024x version=1 -->
## PAGE 00016: BPMN Data Usage Matrices

- page_id: `290032059`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032059/BPMN+Data+Usage+Matrices
- version_number: 1
- version_date: `2026-02-09T15:47:05.953+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > BPMN Matrices
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Data Usage Matrix shows what data classes are used in BPMN Processes and SubProcess. Data Objects represents classes in a BPMN diagram.

A BPMN Data Usage Matrix presents information about all BPMN Processes and SubProcesses in rows and Classes in columns. Each row in the matrix shows if a class is used in a BPMN Process or SubProcess diagram as a Data Object.

**Example**

[IMAGE alt='' src='']

###### BPMN Data Usage Matrix.

**Related elements**

- BPMN Process
- SubProcesses
- Class
- BPMN Matrices

**Related diagram**

- BPMN Process Diagram

**Related procedure**

- Creating a Diagram
- Dependency Matrix

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Data Usage Matrix shows what data classes are used in BPMN Processes and SubProcess. Data Objects represents classes in a BPMN diagram.</p><p>A BPMN Data Usage Matrix presents information about all BPMN Processes and SubProcesses in rows and Classes in columns. Each row in the matrix shows if a class is used in a BPMN Process or SubProcess diagram as a Data Object.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="data_usage_matrix.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Data Usage Matrices" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Data Usage Matrix.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/SubProcesses">SubProcesses</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Matrices" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Matrices</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Dependency+Matrix">Dependency Matrix</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032056 space=CBMP2024x version=1 -->
## PAGE 00017: BPMN Matrices

- page_id: `290032056`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032056/BPMN+Matrices
- version_number: 1
- version_date: `2026-02-09T15:45:49.388+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts
- labels: []

### NORMALIZED CONTENT

A BPMN matrix is designed to explore relations between different types of elements. There are two types of BPMN matrices in Cameo Business Modeler:

**Related external resource**

- Dependency Matrix

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A BPMN matrix is designed to explore relations between different types of elements. There are two types of BPMN matrices in Cameo Business Modeler:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="99cfe4f2-ae37-4816-ad03-7c0ecd2c484e" /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related external resource</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Dependency+Matrix">Dependency Matrix</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031706 space=CBMP2024x version=1 -->
## PAGE 00018: BPMN Process

- page_id: `290031706`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031706/BPMN+Process
- version_number: 1
- version_date: `2026-02-09T13:50:44.779+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Process element defines a process performed in an organization. This element is a container for the BPMN Process diagram and its elements. Process diagram describes how a process is performed.

**Notation** 
[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Process element defines a process performed in an organization. This element is a container for the BPMN Process diagram and its elements. Process diagram describes how a process is performed.</p><p><strong>Notation</strong><br /><ac:image ac:thumbnail="true" ac:width="200"><ri:attachment ri:filename="bpmn_process.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Process" /></ri:attachment></ac:image></p>
````

<!--NOMAGIC_PAGE id=290031704 space=CBMP2024x version=1 -->
## PAGE 00019: BPMN Process Diagram

- page_id: `290031704`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031704/BPMN+Process+Diagram
- version_number: 1
- version_date: `2026-02-09T13:50:37.755+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Process Diagram describes a sequence or flow of activities in an organization that shows how the business works. The diagram shows activities, events, and data that trigger or feed business activities. A BPMN Process Diagram is similar to the UML Activity diagram with a much richer set of default message types and business process styles of notations.

**Example**

[IMAGE alt='' src='']

###### BPMN Process diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Process Diagram describes a sequence or flow of activities in an organization that shows how the business works. The diagram shows activities, events, and data that trigger or feed business activities. A BPMN Process Diagram is similar to the UML Activity diagram with a much richer set of default message types and business process styles of notations.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="process_diagram.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Process Diagram" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">BPMN Process diagram</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032048 space=CBMP2024x version=1 -->
## PAGE 00020: BPMN Processes Description Table

- page_id: `290032048`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032048/BPMN+Processes+Description+Table
- version_number: 1
- version_date: `2026-02-09T15:43:51.523+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > BPMN Tables
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Processes Description table is designed to display or edit processes descriptions in a table form. You can display existing processes or create new processes in this table.

**Example**

[IMAGE alt='' src='']

###### BPMN Processes Description table.

**Related elements**

- BPMN Process
- BPMN Tables

**Related procedure**

- Creating a Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Processes Description table is designed to display or edit processes descriptions in a table form. You can display existing processes or create new processes in this table.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="process_description_table.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Processes Description Table" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Processes Description table.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Tables">BPMN Tables</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032061 space=CBMP2024x version=1 -->
## PAGE 00021: BPMN Processes Structure Map

- page_id: `290032061`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032061/BPMN+Processes+Structure+Map
- version_number: 1
- version_date: `2026-02-09T15:47:39.739+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Processes Structure Map diagram allows you to represent the structure of processes in a project. The 
processes are grouped into packages on the diagram. And each process may itself contains other processes, 
which in turn may contain other processes. The diagram makes the processes easier to understand and helps you 
analyze how they are organized.

A BPMN Processes Structure Map diagram shows packages, processes, subprocesses, and tasks from a 
selected scope.

**Example**

[IMAGE alt='' src='']

###### BPMN Processes Structure Map.

**Related elements**

- Package
- BPMN Process
- Activities

**Related diagram**

- BPMN Process Diagram

**Related external resource**

- Relation Map

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Processes Structure Map diagram allows you to represent the structure of processes in a project. The<br />processes are grouped into packages on the diagram. And each process may itself contains other processes,<br />which in turn may contain other processes. The diagram makes the processes easier to understand and helps you<br />analyze how they are organized.</p><p>A BPMN Processes Structure Map diagram shows packages, processes, subprocesses, and tasks from a<br />selected scope.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="process_structure_map.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Processes Structure Map" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Processes Structure Map.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Package">Package</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related external resource</strong></p><ul><li><a href="https://docs.nomagic.com/display/MD2024xR1/Relation+Map" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Relation Map</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032050 space=CBMP2024x version=1 -->
## PAGE 00022: BPMN Resources Description Table

- page_id: `290032050`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032050/BPMN+Resources+Description+Table
- version_number: 1
- version_date: `2026-02-09T15:44:23.320+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > BPMN Tables
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Resources Description table is designed to display or edit resources description in a table form. You can display existing Resources or create new ones in this table.

BPMN defines four types of Resources as follows:

- Resource
- Organization Unit
- Role
- Person
- Information System

You can display all of them in a BPMN Resources Description table.

**Example**

[IMAGE alt='' src='']

###### BPMN Resource Roles Description table.

**Related elements**

- Resource
- BPMN Tables

**Related procedure**

- Creating a Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Resources Description table is designed to display or edit resources description in a table form. You can display existing Resources or create new ones in this table.</p><p>BPMN defines four types of Resources as follows:</p><ul><li>Resource</li><li>Organization Unit</li><li>Role</li><li>Person</li><li>Information System</li></ul><p>You can display all of them in a BPMN Resources Description table.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="resource_description_table.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Resources Description Table" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Resource Roles Description table.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Tables">BPMN Tables</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032057 space=CBMP2024x version=1 -->
## PAGE 00023: BPMN Resources Usage Matrices

- page_id: `290032057`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032057/BPMN+Resources+Usage+Matrices
- version_number: 1
- version_date: `2026-02-09T15:46:33.599+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > BPMN Matrices
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMN Resources Usage Matrix is designed to review and edit an allocation of Resource Roles for BPMN Activities. The Resource Roles used in an Activity show a Resources property in a BPMN Activity specification dialog.

A BPMN Resources Usage Matrix presents information about BPMN Activities in rows and Resource Roles in columns. Each arrow in the matrix shows if a Resource Role is used by an Activity. 
You can define Resource Roles usage for all BPMN Activities by assigning or removing the Resource Roles to or from the Activities.

**Example**

[IMAGE alt='' src='']

###### BPMN Resource Usage Matrix.

**Related elements**

- BPMN Process
- Activities
- Resource
- Organization Unit
- Role
- Person
- Information system
- BPMN Matrices

**Related procedure**

- Creating a Diagram
- Dependency Matrix

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A BPMN Resources Usage Matrix is designed to review and edit an allocation of Resource Roles for BPMN Activities. The Resource Roles used in an Activity show a Resources property in a BPMN Activity specification dialog.</p><p>A BPMN Resources Usage Matrix presents information about BPMN Activities in rows and Resource Roles in columns. Each arrow in the matrix shows if a Resource Role is used by an Activity.<br />You can define Resource Roles usage for all BPMN Activities by assigning or removing the Resource Roles to or from the Activities.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="resource_usage_matrix.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMN Resources Usage Matrices" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">BPMN Resource Usage Matrix.</h6><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Matrices" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Matrices</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Dependency+Matrix">Dependency Matrix</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032047 space=CBMP2024x version=1 -->
## PAGE 00024: BPMN Tables

- page_id: `290032047`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032047/BPMN+Tables
- version_number: 1
- version_date: `2026-02-09T15:43:20.587+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts
- labels: []

### NORMALIZED CONTENT

BPMN tables allow the quick creation of BPMN elements as well as easy review and modification of their properties. You can review a group of elements as one set in the same place by using these tables.

Types of BPMN tables in Cameo Business Modeler are as follows:

**Related external resource**

- Generic table

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>BPMN tables allow the quick creation of BPMN elements as well as easy review and modification of their properties. You can review a group of elements as one set in the same place by using these tables.</p><p>Types of BPMN tables in Cameo Business Modeler are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="0f4ec51c-ffde-4445-902b-aa194f37e942" /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related external resource</strong></p><ul><li><a href="https://docs.nomagic.com/display/MD2024xR1/Generic+table" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Generic table</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032102 space=CBMP2024x version=1 -->
## PAGE 00025: BPMN2 Completeness Validation Rules

- page_id: `290032102`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032102/BPMN2+Completeness+Validation+Rules
- version_number: 1
- version_date: `2026-02-09T16:05:27.792+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Validation Rules
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
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The BPMN2 validation rules included in the BPMN2 Completeness validation rules suite are described in the table.</p><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Validation rule </th><th><p>Severity</p></th></tr><tr><td><p>An Intermediate Boundary Event should have an outgoing Sequence Flow.</p></td><td><p>Info</p></td></tr><tr><td><span>An Intermediate Event should have an incoming or outgoing Sequence Flow. </span></td><td><span>Info</span></td></tr><tr><td><span>An Error Code should be specified for an Error End Event. </span></td><td><span>Info</span></td></tr><tr><td><span>An Event-Based Gateway should have two or more outgoing Sequence Flows. </span></td><td><span>Info</span></td></tr><tr><td><span>An Event SubProcess will have one Start Event. </span></td><td><p>Warning</p></td></tr><tr><td><span>A Start Event shall have at least one outgoing Sequence Flow. </span></td><td><span>Warning</span></td></tr><tr><td colspan="1"><span>An Intermediate Event can have either an incoming or outgoing Message Flow. It cannot contain </span><span>both.</span></td><td colspan="1"><span>Warning</span></td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290032100 space=CBMP2024x version=1 -->
## PAGE 00026: BPMN2 Correctness (Active) Validation Rules

- page_id: `290032100`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032100/BPMN2+Correctness+Active+Validation+Rules
- version_number: 1
- version_date: `2025-05-05T10:26:49.145+02:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Validation Rules
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

<!--NOMAGIC_PAGE id=290032101 space=CBMP2024x version=1 -->
## PAGE 00027: BPMN2 Correctness Validation Rules

- page_id: `290032101`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032101/BPMN2+Correctness+Validation+Rules
- version_number: 1
- version_date: `2026-02-09T16:05:21.715+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Validation Rules
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

<!--NOMAGIC_PAGE id=290032103 space=CBMP2024x version=1 -->
## PAGE 00028: BPMN2 Export Completeness Validation Rules

- page_id: `290032103`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032103/BPMN2+Export+Completeness+Validation+Rules
- version_number: 1
- version_date: `2026-02-09T16:05:34.559+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Validation Rules
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

<!--NOMAGIC_PAGE id=290031951 space=CBMP2024x version=1 -->
## PAGE 00029: BPMN2 XML support

- page_id: `290031951`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031951/BPMN2+XML+support
- version_number: 1
- version_date: `2026-02-09T14:52:33.546+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler supports exporting BPMN2 models as BPMN2 Diagram Interchange files. The BPMN2 Diagram Interchange is a format for interchanging BPMN2 diagrams between tools. Its reduced ambiguity allows the users to exchange BPMN models between tools more conveniently. You can export a BPMN2 diagram as a BPMN2 Diagram Interchange file (BPMN2 XMI).

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Exporting Models to BPMN2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler supports exporting BPMN2 models as BPMN2 Diagram Interchange files. The BPMN2 Diagram Interchange is a format for interchanging BPMN2 diagrams between tools. Its reduced ambiguity allows the users to exchange BPMN models between tools more conveniently. You can export a BPMN2 diagram as a BPMN2 Diagram Interchange file (BPMN2 XMI).</p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Exporting+Models+to+BPMN2" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Exporting Models to BPMN2</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031906 space=CBMP2024x version=1 -->
## PAGE 00030: BPMNMessage

- page_id: `290031906`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031906/BPMNMessage
- version_number: 1
- version_date: `2026-02-09T14:39:49.012+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A BPMNMessage represents the content of communications between two participants. It is passed by a message flow and is sent or received by a message event.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Message Flow
- Choreography Task

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating and Using Message Flow
- Creating and Using Choreography Task

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Description</strong></p><p>A BPMNMessage represents the content of communications between two participants. It is passed by a message flow and is sent or received by a message event.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="message.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="BPMNMessage" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Message+Flow">Message Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Task" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Choreography Task</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Message+Flow">Creating and Using Message Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Choreography+Task" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Choreography Task</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032034 space=CBMP2024x version=1 -->
## PAGE 00031: BPMNRelationships

- page_id: `290032034`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032034/BPMNRelationships
- version_number: 1
- version_date: `2026-02-09T15:36:05.470+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Process Definition Diagram
- labels: []

### NORMALIZED CONTENT

Process Definition diagram has relationships as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Process Definition diagram has relationships as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="afb0efd8-d0a7-4fde-94c3-de7eed05251f" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290032010 space=CBMP2024x version=1 -->
## PAGE 00032: Business Data Diagram

- page_id: `290032010`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032010/Business+Data+Diagram
- version_number: 1
- version_date: `2026-02-09T15:30:06.462+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Business Data diagram provides possibilities to define what business concepts are used in business processes. The diagram shows classes that represent concepts we can identify in a business area. Therefore, it allows defining properties and relations between classes. Class elements identified in Business Data diagrams are represented by Data Object elements and can be reused later in the BPMN Process diagram.

Business Data Diagram is based on UML Class diagram. It is a simplified version of the class diagram that includes only model elements needed for business data definitions.

**Example**

[IMAGE alt='' src='']

###### Business Data Diagram showing Classes.

**Related elements**

- Class
- BPMN Association
- Generalization

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Business Data diagram provides possibilities to define what business concepts are used in business processes. The diagram shows classes that represent concepts we can identify in a business area. Therefore, it allows defining properties and relations between classes. Class elements identified in Business Data diagrams are represented by Data Object elements and can be reused later in the BPMN Process diagram.</p><p>Business Data Diagram is based on UML Class diagram. It is a simplified version of the class diagram that includes only model elements needed for business data definitions.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="business_data_diagram.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Data Diagram" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Business Data Diagram showing Classes.</h6><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Association">BPMN Association</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Generalization">Generalization</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031953 space=CBMP2024x version=1 -->
## PAGE 00033: Business Motivation Diagram

- page_id: `290031953`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031953/Business+Motivation+Diagram
- version_number: 1
- version_date: `2026-02-09T14:53:32.277+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

The Business Motivation Model designed to develop, communicate, and manage business plans. The model identifies and defines the elements of business plans, the motivating factors to establish the business plans, and how all these factors and elements are interconnected.

**Example**

[IMAGE alt='' src='']

###### Business Motivation Diagram.

**Related elements**

- Ends Concepts
- Means Concepts
- Influencer Concepts
- Assessment Concepts

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Description</strong></p><p>The Business Motivation Model designed to develop, communicate, and manage business plans. The model identifies and defines the elements of business plans, the motivating factors to establish the business plans, and how all these factors and elements are interconnected.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="business_motivation_diagram.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Motivation Diagram" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Business Motivation Diagram.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related elements</strong></p><ul class="childpages-macro"><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Ends+Concepts">Ends Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Means+Concepts">Means Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Influencer+Concepts">Influencer Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concepts">Assessment Concepts</a></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031683 space=CBMP2024x version=1 -->
## PAGE 00034: Business Motivation Model standard

- page_id: `290031683`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031683/Business+Motivation+Model+standard
- version_number: 1
- version_date: `2026-02-09T13:47:34.841+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Getting Started > Introducing Main Concepts
- labels: []

### NORMALIZED CONTENT

The Business Motivation Model (BMM) is a standard created by the Object Management Group (OMG). This standard is designed to develop, communicate, and manage business plans. The model identifies and defines the elements of business plans, the motivating factors to establish the business plans, and how all these factors and elements are interconnected.

You can find full details about BMM at [http://www.omg.org/technology/documents/br_pm_spec_catalog.htm](http://www.omg.org/technology/documents/br_pm_spec_catalog.htm)

The following diagrams are supported:

- [CONFLUENCE_PAGE title='Business Motivation Diagram' space='CBMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Business Motivation Model (BMM) is a standard created by the Object Management Group (OMG). This standard is designed to develop, communicate, and manage business plans. The model identifies and defines the elements of business plans, the motivating factors to establish the business plans, and how all these factors and elements are interconnected.</p><p>You can find full details about BMM at <a href="http://www.omg.org/technology/documents/br_pm_spec_catalog.htm">http://www.omg.org/technology/documents/br_pm_spec_catalog.htm</a></p><p>The following diagrams are supported:</p><ul><li><ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Motivation Diagram" /></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031972 space=CBMP2024x version=1 -->
## PAGE 00035: Business Policy

- page_id: `290031972`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031972/Business+Policy
- version_number: 1
- version_date: `2026-02-09T14:56:57.348+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Means Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Business Policy is a Directive that is not directly enforceable whose purpose is to govern or guide the enterprise. Business Policies provide the basis for Business Rules. Business Policies also govern Business Processes.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Means Concepts
- Mean Concept Relationships

**Related diagrams**

- Business Motivation Diagram
- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Business Policy is a Directive that is not directly enforceable whose purpose is to govern or guide the enterprise. Business Policies provide the basis for Business Rules. Business Policies also govern Business Processes.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="business_policy.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Means+Concepts">Means Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Mean+Concept+Relationships">Mean Concept Relationships</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031682 space=CBMP2024x version=1 -->
## PAGE 00036: Business Process Model and Notation (BPMN) standard

- page_id: `290031682`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031682/Business+Process+Model+and+Notation+BPMN+standard
- version_number: 1
- version_date: `2026-02-09T13:47:28.126+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Getting Started > Introducing Main Concepts
- labels: []

### NORMALIZED CONTENT

The Business Process Modeling and Notation is a standard created by the Object Management Group (OMG). BPMN provides the capability of describing internal business procedures in a graphical notation and enables organizations to communicate these procedures in a standard manner. Furthermore, the standardized graphical notation facilitates the understanding of performance collaborations and business transactions between organizations. This ensures that businesses will understand themselves and other business participants better.

The Cameo Business Modeler plugin for MagicDraw provides support for BPMN2 standard, business concepts and organization structure definition, and BMM standard support for business goals definition. It is also includes BPMN model validation, business analysis tables, matrices, relation maps, reports, manuals, samples, and imports from BPMN 1.1 models that have been created with MagicDraw.

Cameo Business Modeler provides capabilities for model exchange via XPDL files import and export, BPMN2 XMI export.

The BPMN2 standard consists of the following three major parts:

- Process, which shows business processes, events, and messages.
- Collaboration, which shows how a process is implemented among collaborators and displays details of conversations among participants.
- Choreography, which provides a view of message/information flows among participants.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Business Process Modeling and Notation is a standard created by the Object Management Group (OMG). BPMN provides the capability of describing internal business procedures in a graphical notation and enables organizations to communicate these procedures in a standard manner. Furthermore, the standardized graphical notation facilitates the understanding of performance collaborations and business transactions between organizations. This ensures that businesses will understand themselves and other business participants better.</p><p>The Cameo Business Modeler plugin for MagicDraw provides support for BPMN2 standard, business concepts and organization structure definition, and BMM standard support for business goals definition. It is also includes BPMN model validation, business analysis tables, matrices, relation maps, reports, manuals, samples, and imports from BPMN 1.1 models that have been created with MagicDraw.</p><p>Cameo Business Modeler provides capabilities for model exchange via XPDL files import and export, BPMN2 XMI export.</p><p>The BPMN2 standard consists of the following three major parts:</p><ul><li>Process, which shows business processes, events, and messages.</li><li>Collaboration, which shows how a process is implemented among collaborators and displays details of conversations among participants.</li><li>Choreography, which provides a view of message/information flows among participants.</li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031689 space=CBMP2024x version=1 -->
## PAGE 00037: Business Process Model and Notation Concepts

- page_id: `290031689`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031689/Business+Process+Model+and+Notation+Concepts
- version_number: 1
- version_date: `2026-02-09T13:48:00.696+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

The section introduces the common Business Process Model and Notation (BPMN) elements, describes the main types of BPMN diagrams, and presents the automatic numbering feature.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The section introduces the common Business Process Model and Notation (BPMN) elements, describes the main types of BPMN diagrams, and presents the automatic numbering feature.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="54286ba4-929c-4ac9-8966-7ca5454536cf" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031974 space=CBMP2024x version=1 -->
## PAGE 00038: Business Rule

- page_id: `290031974`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031974/Business+Rule
- version_number: 1
- version_date: `2026-02-09T14:57:18.055+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Means Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Business Rule is a Directive, intended to govern, guide, or influence business behavior, in support of Business Policy that has been formulated in response to an Opportunity, Threat, Strength, or Weakness. It is a single Directive that does not require additional interpretation to undertake Strategies or Tactics. Often, a Business Rule is derived from Business Policy. Business Rules guide Business Processes.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Means Concepts
- Mean Concept Relationships

**Related diagrams**

- Business Motivation Diagram
- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Business Rule is a Directive, intended to govern, guide, or influence business behavior, in support of Business Policy that has been formulated in response to an Opportunity, Threat, Strength, or Weakness. It is a single Directive that does not require additional interpretation to undertake Strategies or Tactics. Often, a Business Rule is derived from Business Policy. Business Rules guide Business Processes.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="business_rule.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Means+Concepts">Means Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Mean+Concept+Relationships">Mean Concept Relationships</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031730 space=CBMP2024x version=1 -->
## PAGE 00039: Business Rule Task

- page_id: `290031730`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031730/Business+Rule+Task
- version_number: 1
- version_date: `2026-02-09T13:52:20.785+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A Business Rule Task provides a mechanism for a process to provide inputs to a business rules engine and to get the output of calculations that the business rules engine might provide.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Business Rule Task provides a mechanism for a process to provide inputs to a business rules engine and to get the output of calculations that the business rules engine might provide.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="business_rule_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031748 space=CBMP2024x version=1 -->
## PAGE 00040: Call Activity

- page_id: `290031748`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031748/Call+Activity
- version_number: 1
- version_date: `2026-02-09T13:53:29.593+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities
- labels: []

### NORMALIZED CONTENT

**Description**

A Call Activity identifies a point in a process where a global process is used. The Call Activity acts as a wrapper for the invocation of the global process within the execution. The activation of the Call Activity results in the transfer of control to the called global process.

A Call Activity shares the same notation as a Task or SubProcess with a thick line around the boundary of its shape.

The BPMN2 Call Activity corresponds to the Reusable SubProcess of BPMN 1.2, and the BPMN2 SubProcess corresponds to the Embedded SubProcess of BPMN 1.2.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Call Activity identifies a point in a process where a global process is used. The Call Activity acts as a wrapper for the invocation of the global process within the execution. The activation of the Call Activity results in the transfer of control to the called global process.</p><p>A Call Activity shares the same notation as a Task or SubProcess with a thick line around the boundary of its shape.</p><p>The BPMN2 Call Activity corresponds to the Reusable SubProcess of BPMN 1.2, and the BPMN2 SubProcess corresponds to the Embedded SubProcess of BPMN 1.2.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="callactivity.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Call Activity" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031935 space=CBMP2024x version=1 -->
## PAGE 00041: Call Choreography

- page_id: `290031935`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031935/Call+Choreography
- version_number: 1
- version_date: `2026-02-09T14:48:20.847+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Choreography Diagram > Choreography Activities
- labels: []

### NORMALIZED CONTENT

**Description**

A Call Choreography identifies the point in a process where a global choreography is used. It acts as a place holder to include a choreography element it is calling.

A Call Choreography is with a thick border.

**Notation**

- Call Choreography [ATTACHMENT filename='call_choreography.png']
- A Call Choreography referencing another Choreography is marked with a plus (+) sign [ATTACHMENT filename='call_choreography_ref.png']

**Related elements**

- Organization Unit
- Role
- Person
- Choreography Activities
- Choreography

**Related diagram**

- BPMN Choreography Diagram

**Related procedures**

- Creating Call Choreography Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Call Choreography identifies the point in a process where a global choreography is used. It acts as a place holder to include a choreography element it is calling.</p><p>A Call Choreography is with a thick border.</p><p><strong>Notation</strong></p><ul><li>Call Choreography<br /><ac:image><ri:attachment ri:filename="call_choreography.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Call Choreography" /></ri:attachment></ac:image></li><li>A Call Choreography referencing another Choreography is marked with a plus (+) sign<br /><ac:image><ri:attachment ri:filename="call_choreography_ref.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Call Choreography" /></ri:attachment></ac:image></li></ul><p><br /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Choreography</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+Call+Choreography+Activity">Creating Call Choreography Activity</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031912 space=CBMP2024x version=1 -->
## PAGE 00042: Call Conversation

- page_id: `290031912`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031912/Call+Conversation
- version_number: 1
- version_date: `2026-02-09T14:42:46.107+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Call Conversation identifies a place in a conversation where a Conversation is used.

**Notation**

- Call Conversation that does not call any conversation [ATTACHMENT filename='call_conversation.png']
- Call Conversation calling Global Conversation [ATTACHMENT filename='call_conversation_global.png']

**Related elements**

- Collaboration
- Pool and Lane
- Conversation Link

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Process Diagram

**Related procedure**

- Creating and Using Conversation Nodes

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Call Conversation identifies a place in a conversation where a Conversation is used.</p><p><strong>Notation</strong></p><ul><li>Call Conversation that does not call any conversation<br /><ac:image><ri:attachment ri:filename="call_conversation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Call Conversation" /></ri:attachment></ac:image></li><li>Call Conversation calling Global Conversation<br /><ac:image><ri:attachment ri:filename="call_conversation_global.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Call Conversation" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Collaboration">Collaboration</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Conversation+Link">Conversation Link</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Conversation+Nodes">Creating and Using Conversation Nodes</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031676 space=CBMP2024x version=1 -->
## PAGE 00043: Cameo Business Modeler Plugin Documentation

- page_id: `290031676`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031676/Cameo+Business+Modeler+Plugin+Documentation
- version_number: 1
- version_date: `2026-01-12T14:01:21.038+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="56ff0d81-8f60-44e1-9ee4-a87efe0bb4b6"><ac:parameter ac:name="depth">2</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=290031826 space=CBMP2024x version=1 -->
## PAGE 00044: Cancel Boundary Event

- page_id: `290031826`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031826/Cancel+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:18:07.865+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Cancel Boundary Event is used within a Transaction SubProcess.

This type of Event must be attached to the boundary of a SubProcess and will be triggered if the following conditions are satisfied:

- A Cancel End Event is reached within the Transaction SubProcess.
- A Transaction Protocol Cancel message is received while a transaction is being performed.

A Cancel Boundary Event always interrupts the Activity to which it is attached. The boundary of the event is always solid.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Cancel Boundary Event is used within a Transaction SubProcess.</p><p>This type of Event must be attached to the boundary of a SubProcess and will be triggered if the following conditions are satisfied:</p><ul><li>A Cancel End Event is reached within the Transaction SubProcess.</li><li>A Transaction Protocol Cancel message is received while a transaction is being performed.</li></ul><p>A Cancel Boundary Event always interrupts the Activity to which it is attached. The boundary of the event is always solid.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="boundary_event_cancel.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Cancel Boundary Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031851 space=CBMP2024x version=1 -->
## PAGE 00045: Cancel End Event

- page_id: `290031851`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031851/Cancel+End+Event
- version_number: 1
- version_date: `2026-02-09T14:22:51.427+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Cancel End Event is used within a Transaction SubProcess. It indicates that the transaction will be canceled and a Cancel Boundary Event attached to the SubProcess boundary will be triggered. It also indicates that a Transaction Protocol Cancel message have to be sent to all entities involved in the transaction.

**Notation**

[IMAGE alt='' src='']

**Related element**

- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Cancel End Event is used within a Transaction SubProcess. It indicates that the transaction will be canceled and a Cancel Boundary Event attached to the SubProcess boundary will be triggered. It also indicates that a Transaction Protocol Cancel message have to be sent to all entities involved in the transaction.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_cancel.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Cancel End Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li>End Events</li></ul><p><strong>Related diagrams</strong></p><ul><li>BPMN Process Diagram</li><li>BPMN Collaboration Diagram</li></ul><p><strong>Related procedure</strong></p><ul><li>Creating and Using an Event</li></ul>
````

<!--NOMAGIC_PAGE id=290031920 space=CBMP2024x version=1 -->
## PAGE 00046: Choreography

- page_id: `290031920`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031920/Choreography
- version_number: 1
- version_date: `2026-02-09T14:44:51.733+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Choreography Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Choreography is a container for a BPMN Choreography diagram and its elements.

**Related diagram**

- BPMN Choreography Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Choreography is a container for a BPMN Choreography diagram and its elements.</p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagram</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031921 space=CBMP2024x version=1 -->
## PAGE 00047: Choreography Activities

- page_id: `290031921`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031921/Choreography+Activities
- version_number: 1
- version_date: `2026-02-09T14:45:50.671+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Choreography Diagram
- labels: []

### NORMALIZED CONTENT

A Choreography Activity is an abstract element. It represents a point on a choreography flow where an interaction occurs between two or more participants.

There are three types of Choreography activities defined in business process modeling:

The shape of a Choreography Task, SubChoreography, or Call Choreography consists of two or more participant compartments and one name compartment. One of the participants can be selected as an initiating participant. The color of the initiating participant compartment is the same as the color of the name compartment. The other participants compartments are gray.

[IMAGE alt='' src='']

###### Compartments on Choreography Activity shape.

The looping properties of a Choreography Activity can be specified. They can be repeated sequentially, essentially behaving like a loop. The presence of loop characteristics signifies that the Choreography Activity has looping behavior. There are two types of Looping characteristics defined in BPMN:

**Standard Loop**

A Standard Loop marker displayed on a name compartment of a Choreography Activity shape shows that the looping behavior based on a boolean condition is defined for this Activity. Additional looping characteristics can also be defined: the Activity will loop as long as the boolean condition is true. The condition is evaluated for every loop iteration and can be evaluated at the beginning or end of the iteration. In addition, a numeric cap can be optionally specified, but the number of iterations cannot exceed this cap.

- Choreography Activity with Standard Loop marker [ATTACHMENT filename='choreography_task_with_standard_loop.png']
- SubChoreography with Standard Loop marker [ATTACHMENT filename='choreography_subprocess_with_standard_loop.png']

**Multi-instance Loop**

A Multi-instance Loop marker shows that a desired number of Choreography Activity instances can be created. The instances can be executed either in parallel or sequentially and each will be identified using a different marker.

- Choreography Task with Parallel MultiInstance Loop marker [ATTACHMENT filename='choreography_task_parallel.png']
- SubChoreography with Parallel MultiInstance Loop marker [ATTACHMENT filename='choreography_subprocess_parallel.png']
- Choreography Task with sequential MultiInstance Loop marker [ATTACHMENT filename='choreography_task_parallel_is_sequential.png']
- SubChoreography with sequential MultiInstance Loop marker [ATTACHMENT filename='choreography_subprocess_parallel_is_sequential.png']

Multi-instance Loop and Standard Loop markers can be added to all types of Choreography activities.

There are circumstances when a Choreography Activity references a multi-instance participant (the minimum multiplicity property value for a participant is 2 or greater). A multi-instance participant represents a situation where there is more than one possible related participant involved in a Choreography. If this is the case, a MultiInstance marker will be displayed in the participant compartment of a Choreography Activity shape.

**Related diagram**

- BPMN Process Diagram

**Related procedure**

- Using Choreography Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Choreography Activity is an abstract element. It represents a point on a choreography flow where an interaction occurs between two or more participants.</p><p>There are three types of Choreography activities defined in business process modeling:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b3e4d655-dd0d-49cc-8824-972698b39055" /></p><p>The shape of a Choreography Task, SubChoreography, or Call Choreography consists of two or more participant compartments and one name compartment. One of the participants can be selected as an initiating participant. The color of the initiating participant compartment is the same as the color of the name compartment. The other participants compartments are gray.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="choreography_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Activities" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Compartments on Choreography Activity shape.</h6><p>The looping properties of a Choreography Activity can be specified. They can be repeated sequentially, essentially behaving like a loop. The presence of loop characteristics signifies that the Choreography Activity has looping behavior. There are two types of Looping characteristics defined in BPMN:</p><p><strong>Standard Loop</strong></p><p>A Standard Loop marker displayed on a name compartment of a Choreography Activity shape shows that the looping behavior based on a boolean condition is defined for this Activity. Additional looping characteristics can also be defined: the Activity will loop as long as the boolean condition is true. The condition is evaluated for every loop iteration and can be evaluated at the beginning or end of the iteration. In addition, a numeric cap can be optionally specified, but the number of iterations cannot exceed this cap.</p><ul><li>Choreography Activity with Standard Loop marker<br /><ac:image><ri:attachment ri:filename="choreography_task_with_standard_loop.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Activities" /></ri:attachment></ac:image></li><li>SubChoreography with Standard Loop marker<br /><ac:image><ri:attachment ri:filename="choreography_subprocess_with_standard_loop.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Activities" /></ri:attachment></ac:image></li></ul><p><strong>Multi-instance Loop</strong></p><p>A Multi-instance Loop marker shows that a desired number of Choreography Activity instances can be created. The instances can be executed either in parallel or sequentially and each will be identified using a different marker.</p><ul><li>Choreography Task with Parallel MultiInstance Loop marker<br /><ac:image><ri:attachment ri:filename="choreography_task_parallel.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Activities" /></ri:attachment></ac:image></li><li>SubChoreography with Parallel MultiInstance Loop marker<br /><ac:image><ri:attachment ri:filename="choreography_subprocess_parallel.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Activities" /></ri:attachment></ac:image></li><li>Choreography Task with sequential MultiInstance Loop marker<br /><ac:image><ri:attachment ri:filename="choreography_task_parallel_is_sequential.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Activities" /></ri:attachment></ac:image></li><li>SubChoreography with sequential MultiInstance Loop marker<br /><ac:image><ri:attachment ri:filename="choreography_subprocess_parallel_is_sequential.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Activities" /></ri:attachment></ac:image></li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="11aafcb5-2c6a-42d7-b66b-404ecfd578f0"><ac:rich-text-body><p>Multi-instance Loop and Standard Loop markers can be added to all types of Choreography activities.</p></ac:rich-text-body></ac:structured-macro><p>There are circumstances when a Choreography Activity references a multi-instance participant (the minimum multiplicity property value for a participant is 2 or greater). A multi-instance participant represents a situation where there is more than one possible related participant involved in a Choreography. If this is the case, a MultiInstance marker will be displayed in the participant compartment of a Choreography Activity shape.</p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagram</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Choreography+Activity" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using Choreography Activity</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031929 space=CBMP2024x version=1 -->
## PAGE 00048: Choreography Task

- page_id: `290031929`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031929/Choreography+Task
- version_number: 1
- version_date: `2026-02-09T14:46:42.522+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Choreography Diagram > Choreography Activities
- labels: []

### NORMALIZED CONTENT

**Description**

A Choreography Task is an atomic Activity in a choreography process. It represents one or more messages exchanged between two Participants.A Choreography Task can display messages that are defined by the referenced Message Flows. The messages connected to an Initiating Participant compartment are white and those connected to a Non-Initiating Participant compartment are gray.

**Notation**

[IMAGE alt='' src=''] 
**Example**

[IMAGE alt='' src='']

###### Choreography task corresponding to BPMN Collaboration diagram.

**Related elements**

- Organization Unit
- Role
- Person
- Choreography Activities

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating and Using Choreography Task
- Using Choreography Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="margin-top: 10.0px;"><strong>Description</strong></p><p>A Choreography Task is an atomic Activity in a choreography process. It represents one or more messages exchanged between two Participants.A Choreography Task can display messages that are defined by the referenced Message Flows. The messages connected to an Initiating Participant compartment are white and those connected to a Non-Initiating Participant compartment are gray.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="choreography_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Task" /></ri:attachment></ac:image><br /><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="choreography_example_I.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Choreography Task" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Choreography task corresponding to BPMN Collaboration diagram.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Choreography+Task" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Choreography Task</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Choreography+Activity" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using Choreography Activity</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032012 space=CBMP2024x version=1 -->
## PAGE 00049: Class

- page_id: `290032012`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032012/Class
- version_number: 1
- version_date: `2026-02-09T15:30:32.378+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Data Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Class element represents data or a concept that is related to problem area and is used by business processes. To define more information about a class, you can add class properties for the class.

**Notation**

- Class [ATTACHMENT filename='class.png']
- Class with properties [ATTACHMENT filename='class_with_properties.png']

**Related elements**

- BPMN Association
- Generalization
- Data Object

**Related diagrams**

- Business Data Diagram
- BPMN Business Data Description Table
- BPMN Data Usage Matrices

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Class element represents data or a concept that is related to problem area and is used by business processes. To define more information about a class, you can add class properties for the class.</p><p><strong>Notation</strong></p><ul><li>Class<br /><ac:image><ri:attachment ri:filename="class.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Class" /></ri:attachment></ac:image></li><li>Class with properties<br /><ac:image><ri:attachment ri:filename="class_with_properties.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Class" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Association">BPMN Association</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Generalization">Generalization</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Data+Object" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Data Object</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Data+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Business Data Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Business+Data+Description+Table">BPMN Business Data Description Table</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Data+Usage+Matrices">BPMN Data Usage Matrices</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031896 space=CBMP2024x version=1 -->
## PAGE 00050: Collaboration

- page_id: `290031896`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031896/Collaboration
- version_number: 1
- version_date: `2026-02-09T14:32:11.074+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Collaboration element provides a description of collaborations between pools. This element is a container for a BPMN Collaboration diagram and its elements.

**Related elements**

- Pool and Lane
- Participant

**Related diagram**

- BPMN Collaboration Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Collaboration element provides a description of collaborations between pools. This element is a container for a BPMN Collaboration diagram and its elements.</p><p><br /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Participant">Participant</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031690 space=CBMP2024x version=1 -->
## PAGE 00051: Common BPMN Elements

- page_id: `290031690`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031690/Common+BPMN+Elements
- version_number: 1
- version_date: `2026-02-09T13:48:08.273+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts
- labels: []

### NORMALIZED CONTENT

The following section defines the BPMN elements that can be used in several BPMN diagrams, such as Process, Collaboration, and Choreography diagrams.

Common BPMN2 elements are described in the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following section defines the BPMN elements that can be used in several BPMN diagrams, such as Process, Collaboration, and Choreography diagrams.</p><p>Common BPMN2 elements are described in the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c0416f14-ca67-4843-944d-341518f5623c" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031889 space=CBMP2024x version=1 -->
## PAGE 00052: Compensation

- page_id: `290031889`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031889/Compensation
- version_number: 1
- version_date: `2026-02-09T14:37:36.908+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Compensation in business process modeling is concerned with undoing steps that have already been successfully completed because their results and possible side effects are no longer desired and need to be reversed. If an Activity is still active, it cannot be compensated and needs to be canceled. The cancellation of a SubProcess can produce a compensation of the already successfully completed portions of an active Activity.

A Compensation is performed by a compensation handler. A compensation handler performs the steps necessary to reverse the effects of an Activity. For a SubProcess, the compensation handler will have access to the SubProcess data once they have been completed (“snapshot data”).

A compensation handler is a set of Activities that is not connected to other portions of the BPMN model. The compensation handler starts with either of the Compensation Events:

- Compensation Boundary Event
- The handler’s Start Event (in case of a Compensation Event SubProcess)

A compensation handler connected through a boundary event can only perform a “black-box” compensation of the original Activity. This compensation is modeled with a specialized Compensation Activity, which is connected to the boundary event through an association. The Compensation Activity, which can be either a Task or a SubProcess, is marked to show that it is used for compensation only and is located outside the normal flow of the Process.

[IMAGE alt='' src='']

###### Compensation handler connected through Compensation Boundary Event.

Another way to model a compensation is using a compensation handler, which starts with a Start Event of an Event SubProcess that is contained within a Process or SubProcess. Just like any other Compensation Activities, a Compensation Event SubProcess is located outside the normal flow of a process. The Event SubProcess, which is marked with a dotted line boundary, has access to data that are part of the parent, which is a snapshot at the point in time when the parent has been completed. A Compensation Event SubProcess can recursively trigger a compensation for activities contained in its parent.

**Example**

[IMAGE alt='' src='']

###### Compensation defined by Event SubProcess.

**Related elements**

- BPMN Process
- SubProcesses
- Compensation Start Event
- Escalation Throwing Intermediate Event
- Compensation Boundary Event
- Association

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Using Activities

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Compensation in business process modeling is concerned with undoing steps that have already been successfully completed because their results and possible side effects are no longer desired and need to be reversed. If an Activity is still active, it cannot be compensated and needs to be canceled. The cancellation of a SubProcess can produce a compensation of the already successfully completed portions of an active Activity.</p><p>A Compensation is performed by a compensation handler. A compensation handler performs the steps necessary to reverse the effects of an Activity. For a SubProcess, the compensation handler will have access to the SubProcess data once they have been completed (“snapshot data”).</p><p>A compensation handler is a set of Activities that is not connected to other portions of the BPMN model. The compensation handler starts with either of the Compensation Events:</p><ul><li>Compensation Boundary Event </li><li>The handler’s Start Event (in case of a Compensation Event SubProcess)</li></ul><p>A compensation handler connected through a boundary event can only perform a “black-box” compensation of the original Activity. This compensation is modeled with a specialized Compensation Activity, which is connected to the boundary event through an association. The Compensation Activity, which can be either a Task or a SubProcess, is marked to show that it is used for compensation only and is located outside the normal flow of the Process.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="compensation_handler_I.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Compensation" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Compensation handler connected through Compensation Boundary Event.</h6><p>Another way to model a compensation is using a compensation handler, which starts with a Start Event of an Event SubProcess that is contained within a Process or SubProcess. Just like any other Compensation Activities, a Compensation Event SubProcess is located outside the normal flow of a process. The Event SubProcess, which is marked with a dotted line boundary, has access to data that are part of the parent, which is a snapshot at the point in time when the parent has been completed. A Compensation Event SubProcess can recursively trigger a compensation for activities contained in its parent.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="compensation_handler_II.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Compensation" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Compensation defined by Event SubProcess.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/SubProcesses">SubProcesses</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Compensation+Start+Event">Compensation Start Event</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Escalation+Throwing+Intermediate+Event">Escalation Throwing Intermediate Event</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Compensation+Boundary+Event">Compensation Boundary Event</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Association">Association</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Activities">Using Activities</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031828 space=CBMP2024x version=1 -->
## PAGE 00053: Compensation Boundary Event

- page_id: `290031828`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031828/Compensation+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:18:30.723+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Compensation Boundary Event is used to catch a Compensation Event. The event will be triggered by a compensation event. When the event is triggered, a Compensation Activity, which is associated with it, will be performed.

The Compensation Boundary Event in this sense does not affect the interrupting or non-interrupting aspect. Compensations can only be triggered after the completion of an Activity to which they are attached. Thus, they cannot interrupt the Activity. The boundary of the event is always solid.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Boundary Events
- Activities
- Compensation

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Compensation Boundary Event is used to catch a Compensation Event. The event will be triggered by a compensation event. When the event is triggered, a Compensation Activity, which is associated with it, will be performed.</p><p>The Compensation Boundary Event in this sense does not affect the interrupting or non-interrupting aspect. Compensations can only be triggered after the completion of an Activity to which they are attached. Thus, they cannot interrupt the Activity. The boundary of the event is always solid.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="boundary_event_compensation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Compensation Boundary Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Compensation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Compensation</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031853 space=CBMP2024x version=1 -->
## PAGE 00054: Compensation End Event

- page_id: `290031853`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031853/Compensation+End+Event
- version_number: 1
- version_date: `2026-02-09T14:23:14.731+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Compensation End Event indicates that a compensation is necessary.

- If an Activity, which has successfully been completed, is identified, that Activity will be compensated.
- If no Activity is identified, all successfully completed Activities visible from the Compensation End Event will be compensated in reverse order of their sequence flows.

To be compensated, an Activity must have a Compensation Boundary Event or contain a Compensation Event SubProcess.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- End Events
- Compensation

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Compensation End Event indicates that a compensation is necessary.</p><ul><li>If an Activity, which has successfully been completed, is identified, that Activity will be compensated.</li><li>If no Activity is identified, all successfully completed Activities visible from the Compensation End Event will be compensated in reverse order of their sequence flows.</li></ul><p>To be compensated, an Activity must have a Compensation Boundary Event or contain a Compensation Event SubProcess.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_compensation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Compensation End Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Compensation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Compensation</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031763 space=CBMP2024x version=1 -->
## PAGE 00055: Compensation Start Event

- page_id: `290031763`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031763/Compensation+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:57:26.711+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Compensation Start Event triggers an in-line Compensation Event SubProcess only. The event is triggered when the compensation occurs.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Compensation Start Event triggers an in-line Compensation Event SubProcess only. The event is triggered when the compensation occurs.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="start_event_compensation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Compensation Start Event" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031807 space=CBMP2024x version=1 -->
## PAGE 00056: Compensation Throwing Intermediate Event

- page_id: `290031807`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031807/Compensation+Throwing+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:14:41.709+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Throwing Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Compensation Throwing Intermediate Event indicates that a compensation is necessary.

If an Activity, which has been successfully completed, is identified, then it will be compensated.

If no Activity is identified, all successfully completed Activities visible from a Compensation Throwing Intermediate Event will be compensated in reverse order of their sequence flows. To be compensated, the Activity must have a Boundary Compensation Event or contain a Compensation Event SubProcess.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Compensation
- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Compensation Throwing Intermediate Event indicates that a compensation is necessary.</p><p>If an Activity, which has been successfully completed, is identified, then it will be compensated.</p><p>If no Activity is identified, all successfully completed Activities visible from a Compensation Throwing Intermediate Event will be compensated in reverse order of their sequence flows. To be compensated, the Activity must have a Boundary Compensation Event or contain a Compensation Event SubProcess.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_throwing_event_compensation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Compensation Throwing Intermediate Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Compensation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Compensation</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031875 space=CBMP2024x version=1 -->
## PAGE 00057: Complex Gateway

- page_id: `290031875`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031875/Complex+Gateway
- version_number: 1
- version_date: `2026-02-09T14:36:47.445+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Gateways
- labels: []

### NORMALIZED CONTENT

**Description**

A Complex Gateway can be used to model complex synchronization behavior. An Activation Condition is the Complex Gateway’s property, which is used to describe precise behavior.

**Notation**

[IMAGE alt='' src='']

**Example**

The activation condition specifies that tokens on three out of five incoming sequence flows are needed to activate the gateway. Which token the Gateway will produce is determined by the conditions on the outgoing sequence flow as in the split behavior of an Inclusive Gateway

[IMAGE alt='' src='']

###### Complex Gateway.

**Related elements**

- Gateways
- Sequence Flow

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using a Sequence Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Complex Gateway can be used to model complex synchronization behavior. An Activation Condition is the Complex Gateway’s property, which is used to describe precise behavior.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="gateway_complex.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Complex Gateway" /></ri:attachment></ac:image></p><p><strong>Example</strong></p><p>The activation condition specifies that tokens on three out of five incoming sequence flows are needed to activate the gateway. Which token the Gateway will produce is determined by the conditions on the outgoing sequence flow as in the split behavior of an Inclusive Gateway</p><p><ac:image ac:align="center"><ri:attachment ri:filename="complex_gateway.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Complex Gateway" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Complex Gateway.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Gateways">Gateways</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Sequence+Flow">Sequence Flow</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032030 space=CBMP2024x version=1 -->
## PAGE 00058: Composition

- page_id: `290032030`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032030/Composition
- version_number: 1
- version_date: `2026-02-09T15:35:17.779+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Organization Structure Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Composition is a key relationship that shows how organization structure is composed. For example, one organization unit can be a part of a parent organization.

**Example**

[IMAGE alt='' src='']

**Related elements**

- Resource
- Organization Unit
- Role
- Person
- Information system

**Related diagrams**

- Organization Structure Diagram

**Related Procedure**

- Using Organization Structure Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Composition is a key relationship that shows how organization structure is composed. For example, one organization unit can be a part of a parent organization.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="composition.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Composition" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Structure+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Organization Structure Diagram</a></li></ul><p><strong>Related Procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Organization+Structure+Diagram">Using Organization Structure Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031830 space=CBMP2024x version=1 -->
## PAGE 00059: Conditional Boundary Event

- page_id: `290031830`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031830/Conditional+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:18:57.107+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Conditional Boundary Event is triggered when a specified condition becomes true. When the event is triggered, it will change a normal flow of a Process into an exception flow.

This event displays either of the following on a diagram:

- A Conditional Catching Intermediate Event name if the name is specified.
- A Conditional property value if the name is unspecified.

**Notation**

- Conditional Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_conditional.png']
- Non-interrupting Conditional Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_conditional_false.png']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Conditional Boundary Event is triggered when a specified condition becomes true. When the event is triggered, it will change a normal flow of a Process into an exception flow.</p><p>This event displays either of the following on a diagram:</p><ul><li>A Conditional Catching Intermediate Event name if the name is specified.</li><li>A Conditional property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><ul><li>Conditional Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_conditional.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Conditional Boundary Event" /></ri:attachment></ac:image></li><li>Non-interrupting Conditional Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_conditional_false.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Conditional Boundary Event" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031789 space=CBMP2024x version=1 -->
## PAGE 00060: Conditional Catching Intermediate Event

- page_id: `290031789`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031789/Conditional+Catching+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:00:58.395+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Conditional Catching Intermediate Event is triggered when a condition becomes true.

This event displays either of the following on a diagram:

- A Conditional Catching Intermediate Event name if the name is specified.
- A Condition property value if the name is unspecified.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Conditional Catching Intermediate Event is triggered when a condition becomes true.</p><p>This event displays either of the following on a diagram:</p><ul><li>A Conditional Catching Intermediate Event name if the name is specified.</li><li>A Condition property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event_conditional.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Conditional Catching Intermediate Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031765 space=CBMP2024x version=1 -->
## PAGE 00061: Conditional Start Event

- page_id: `290031765`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031765/Conditional+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:57:36.911+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Conditional Start Event is triggered when a condition is specified, become true. For example, “S&P 500 changes by more than 10% since opening” or “Temperature above 300C”.

A Conditional Start Event displays either of the following on a diagram:

- A Conditional Start Event name if the name is specified.
- A Condition property value if the name is unspecified.

A conditional expression of an event must become “false”, and then “true” before the event can be triggered again.

**Notation**

- Interrupting Conditional Start Event [ATTACHMENT filename='start_event_conditional_interr.png']
- Non-interrupting Conditional Start Event [ATTACHMENT filename='start_event_conditional_noninterr.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Conditional Start Event is triggered when a condition is specified, become true. For example, “S&amp;P 500 changes by more than 10% since opening” or “Temperature above 300C”.</p><p>A Conditional Start Event displays either of the following on a diagram:</p><ul><li>A Conditional Start Event name if the name is specified.</li><li>A Condition property value if the name is unspecified.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9ea91e94-3159-4200-9f08-51120fdeb9db"><ac:rich-text-body><p>A conditional expression of an event must become “false”, and then “true” before the event can be triggered again.</p></ac:rich-text-body></ac:structured-macro><p><strong>Notation</strong></p><ul><li>Interrupting Conditional Start Event<br /><ac:image><ri:attachment ri:filename="start_event_conditional_interr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Conditional Start Event" /></ri:attachment></ac:image></li><li>Non-interrupting Conditional Start Event<br /><ac:image><ri:attachment ri:filename="start_event_conditional_noninterr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Conditional Start Event" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031945 space=CBMP2024x version=1 -->
## PAGE 00062: Consecutive with Owner Number

- page_id: `290031945`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031945/Consecutive+with+Owner+Number
- version_number: 1
- version_date: `2026-02-09T14:50:41.666+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Numbering Elements > Numbering Schemas
- labels: []

### NORMALIZED CONTENT

**Description**

A Consecutive with Owner Number numbering schema provides non-multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is displayed before the element number.

**Example**

[IMAGE alt='' src='']

###### Consecutive Numbering style with element owner number.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Using BPMN Element Numbers

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Consecutive with Owner Number numbering schema provides non-multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is displayed before the element number.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="element_numbering_consecutive_I.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Consecutive with Owner Number" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Consecutive Numbering style with element owner number.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Element+Numbers" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using BPMN Element Numbers</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031947 space=CBMP2024x version=1 -->
## PAGE 00063: Consecutive without Owner Number

- page_id: `290031947`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031947/Consecutive+without+Owner+Number
- version_number: 1
- version_date: `2026-02-09T14:51:10.296+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Numbering Elements > Numbering Schemas
- labels: []

### NORMALIZED CONTENT

**Description**

A Consecutive without Owner Number numbering schema provides non-multilevel element numbering. An Element Owner (BPMN Process, BPMN Collaboration, or Choreography) number is not included in the element number.

**Example**

[IMAGE alt='' src='']

###### Consecutive numbering style without owner number.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Using BPMN Element Numbers

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Consecutive without Owner Number numbering schema provides non-multilevel element numbering. An Element Owner (BPMN Process, BPMN Collaboration, or Choreography) number is not included in the element number.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="element_numbering_consecutive_II.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Consecutive without Owner Number" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Consecutive numbering style without owner number.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Element+Numbers" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using BPMN Element Numbers</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031908 space=CBMP2024x version=1 -->
## PAGE 00064: Conversation

- page_id: `290031908`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031908/Conversation
- version_number: 1
- version_date: `2026-02-09T14:41:54.828+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Conversation is an atomic element for a BPMN Collaboration diagram. It represents a set of message flows that is grouped together.

A Conversation can involve two or more Participants. A Conversation Link path will be from a Conversation to the involved Participants (Pools).

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Pool and Lane
- Conversation Link

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using Conversation Nodes

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Conversation is an atomic element for a BPMN Collaboration diagram. It represents a set of message flows that is grouped together.</p><p>A Conversation can involve two or more Participants. A Conversation Link path will be from a Conversation to the involved Participants (Pools).</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="conversation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Conversation" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Conversation+Link">Conversation Link</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Conversation+Nodes">Creating and Using Conversation Nodes</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031915 space=CBMP2024x version=1 -->
## PAGE 00065: Conversation Link

- page_id: `290031915`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031915/Conversation+Link
- version_number: 1
- version_date: `2026-02-09T14:43:27.779+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Conversation Link is used to connect conversation nodes (Communication, SubConversation, and Call Conversation) to and from Participants (Pools).

**Example**

[IMAGE alt='' src='']

###### Conversation Link notation.

**Related elements**

- Collaboration
- SubConversation
- Call Conversation
- Conversation

**Related diagram**

- BPMN Collaboration Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Conversation Link is used to connect conversation nodes (Communication, SubConversation, and Call Conversation) to and from Participants (Pools).</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="conversation_link.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Conversation Link" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Conversation Link notation.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Collaboration">Collaboration</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/SubConversation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">SubConversation</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Call+Conversation">Call Conversation</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Conversation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Conversation</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032064 space=CBMP2024x version=1 -->
## PAGE 00066: Creating a Diagram

- page_id: `290032064`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032064/Creating+a+Diagram
- version_number: 1
- version_date: `2026-02-09T15:47:54.516+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Creating diagrams' space='MD2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="eae4f08c-e6c8-4d47-b6d5-e0142ef9ec86"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Creating diagrams" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032070 space=CBMP2024x version=1 -->
## PAGE 00067: Creating and Using a BPMNEvent

- page_id: `290032070`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032070/Creating+and+Using+a+BPMNEvent
- version_number: 1
- version_date: `2026-02-09T15:51:04.621+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

This section will describe how to create and specify Events in BPMN diagrams.

To create a BPMNEvent

- On the Process diagram palette, click a desired event button and then select a type of BPMNEvent.

To create a Boundary Event

- On the Process diagram pallete, click the Boundary Event (Message) button and then select a type of Boundary Event.
- Click an Activity or Choreography Activity in the diagram. [ATTACHMENT filename='create_boundary_event.png']

To change a BPMNEvent type

You can change an Event type for Start, Intermediate, Boundary, or End Events.

- Right-click a created BPMNEvent and select a new BPMNEvent type.

To change a Start Event to non-interrupting, do one of the following

Not all Start Event types can be non-interrupting. The command *Is Interrupting*is only available for the following Start Event types:

- Message Start Event
- Timer Start Event
- Escalation Start Event
- Conditional Start Event
- Signal Start Event
- Multiple Start Event
- Parallel Multiple Start Event

- Right-click the Start Event and on the shortcut menu click Is Interrupting > False .
- Open the Start Event Specification window. It the Is Interrupting property box, select False and click Close .

To change a Boundary Event to non-interrupting, do one of the following

Not all Boundary Event types can be non-interrupting. The command *Cancel Activity* is only available for the following Boundary Event types:

- Message Boundary Event
- Timer Boundary Event
- Escalation Boundary Event
- Conditional Boundary Event
- Signal Boundary Event
- Multiple Boundary Event
- Parallel Multiple Boundary Event

- Right-click the Boundary Event and on the shortcut menu click Cancel Activity > False .
- Open the Boundary Event Specification window. In the Cancel Activity property box, select False , and then click Close .

**Related elements**

- Start Events
- Intermediate Catch Event
- Intermediate Throwing Event
- Boundary Events
- End Events
- Activities
- Choreography Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Tasks
- Creating and Using SubProcesses
- Using Activities
- Creating and Using a Sequence Flow
- Creating and Using Data Items
- Using Common BPMN Elements
- Navigation Between BPMN Diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section will describe how to create and specify Events in BPMN diagrams.</p><p><br /></p><p>To create a  BPMNEvent</p><hr style="" /><ul><li>On the Process diagram palette, click a desired event button and then select a type of BPMNEvent.</li></ul><p><br /></p><p>To create a Boundary Event</p><hr style="" /><ul><li>On the Process diagram pallete, click the <strong>Boundary Event (Message)</strong> button and then select a type of Boundary Event.</li><li>Click an Activity or Choreography Activity in the diagram.<br /><ac:image ac:thumbnail="true" ac:height="66"><ri:attachment ri:filename="create_boundary_event.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Creating and Using a BPMNEvent" /></ri:attachment></ac:image></li></ul><p><br /></p><p>To change a BPMNEvent type</p><hr style="" /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fe3f459b-b348-42f0-a542-abe251874cbb"><ac:rich-text-body>You can change an Event type for Start, Intermediate, Boundary, or End Events.</ac:rich-text-body></ac:structured-macro><ul><li>Right-click a created BPMNEvent and select a new BPMNEvent type.</li></ul><p><br /></p><p>To change a Start Event to non-interrupting, do one of the following</p><hr style="" /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="93c7382e-fc01-40cb-90e1-92752d454711"><ac:rich-text-body><p>Not all Start Event types can be non-interrupting. The command <em>Is Interrupting </em>is only available for the following Start Event types:</p><ul><li>Message Start Event</li><li>Timer Start Event</li><li>Escalation Start Event</li><li>Conditional Start Event</li><li>Signal Start Event</li><li>Multiple Start Event</li><li>Parallel Multiple Start Event</li></ul></ac:rich-text-body></ac:structured-macro><ul><li>Right-click the Start Event and on the shortcut menu click <strong>Is Interrupting</strong> &gt; <strong>False</strong>.</li><li>Open the Start Event Specification window. It the <strong>Is Interrupting</strong> property box, select <strong>False</strong> and click <strong>Close</strong>.</li></ul><p><br /></p><p>To change a Boundary Event to non-interrupting, do one of the following</p><hr style="" /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="2b5e8584-5546-4362-b294-e7dad0e70799"><ac:rich-text-body><p>Not all Boundary Event types can be non-interrupting. The command <em>Cancel Activity</em> is only available for the following Boundary Event types:</p><ul class="_mce_tagged_br"><li>Message Boundary Event</li><li>Timer Boundary Event</li><li>Escalation Boundary Event</li><li>Conditional Boundary Event</li><li>Signal Boundary Event</li><li>Multiple Boundary Event</li><li>Parallel Multiple Boundary Event</li></ul></ac:rich-text-body></ac:structured-macro><ul><li>Right-click the Boundary Event and on the shortcut menu click <strong>Cancel Activity</strong>&gt; <strong>False</strong>.</li><li>Open the Boundary Event Specification window. In the <strong>Cancel Activity</strong> property box, select <strong>False</strong>, and then click <strong>Close</strong>.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Start+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Start Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Tasks" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Tasks</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+SubProcesses" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using SubProcesses</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Activities">Using Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Common+BPMN+Elements">Using Common BPMN Elements</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Navigation+Between+BPMN+Diagrams">Navigation Between BPMN Diagrams</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032072 space=CBMP2024x version=1 -->
## PAGE 00068: Creating and Using a Sequence Flow

- page_id: `290032072`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032072/Creating+and+Using+a+Sequence+Flow
- version_number: 1
- version_date: `2026-02-09T15:51:51.837+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

A Sequence Flow connects Activities, Choreography Activities, Events, and Gateways. A Conditional Sequence Flow has a condition expression and is drawn with a mini-diamond marker at the beginning of the Sequence Flow A default Sequence Flow is indicated with a backslash at the beginning of the Sequence Flow.

To create a Sequence Flow, do one of the following

- Click an Activity on the diagram. On the Smart Manipulators toolbar click the Sequence Flow button.
- Click the Sequence Flow button on the diagram pallet and connect appropriate shapes on the diagram pane.

To add a condition to Sequence Flow, do one of the following

- Select the created Sequence Flow, open its Specification window and enter the Condition Expression property value.
- Select the created Sequence Flow and type the condition between the brackets. [ATTACHMENT filename='sequence_flow_condition_expression.png']

A Conditional Sequence Flow outgoing from a Gateway is displayed without a mini diamond marker.

To set a default Sequence Flow

A default Sequence Flow can be specified for Activities (Tasks, Subprocesses, and Call Activities) or exclusive, inclusive, and complex Gateways.

1. Select the Sequence flow on the diagram pane.
2. On the Smart Manipulator toolbar, click the Make Default button. [ATTACHMENT filename='default_sequence_flow.png']

A default Sequence flow does not have a condition expression.

To change direction of Sequence Flow

- Right-click the Sequence Flow and from the shortcut menu, select Refactor > Reverse Direction .

**Related element**

- Sequence Flow

**Related diagrams**

- BPMN Process Diagrams
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Tasks
- Creating and Using SubProcesses
- Using Activities
- Creating and Using an Event
- Creating and Using Data Items
- Using Common BPMN Elements
- Navigation Between BPMN Diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Sequence Flow connects Activities, Choreography Activities, Events, and Gateways. A Conditional Sequence Flow has a condition expression and is drawn with a mini-diamond marker at the beginning of the Sequence Flow A default Sequence Flow is indicated with a backslash at the beginning of the Sequence Flow.</p><p><br /></p><p>To create a Sequence Flow, do one of the following</p><hr style="" /><ul><li>Click an Activity on the diagram. On the Smart Manipulators toolbar click the Sequence Flow button.</li><li>Click the <strong>Sequence Flow</strong> button on the diagram pallet and connect appropriate shapes on the diagram pane.</li></ul><p><br /></p><p>To add a condition to Sequence Flow, do one of the following</p><hr style="" /><ul><li>Select the created Sequence Flow, open its Specification window and enter the <strong>Condition Expression</strong> property value.</li><li>Select the created Sequence Flow and type the condition between the brackets.<br /><ac:image ac:height="80"><ri:attachment ri:filename="sequence_flow_condition_expression.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Creating and Using a Sequence Flow" /></ri:attachment></ac:image></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="52172a33-a14d-463d-a9c5-90450b0feecf"><ac:rich-text-body><p>A Conditional Sequence Flow outgoing from a Gateway is displayed without a mini diamond marker.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>To set a default Sequence Flow</p><hr style="" /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a56f66f9-163b-49bc-b90b-82439aa76248"><ac:rich-text-body><p>A default Sequence Flow can be specified for Activities (Tasks, Subprocesses, and Call Activities) or exclusive, inclusive, and complex Gateways.</p></ac:rich-text-body></ac:structured-macro><ol><li>Select the Sequence flow on the diagram pane.</li><li>On the Smart Manipulator toolbar, click the Make Default button.<br /><ac:image ac:thumbnail="true" ac:height="186"><ri:attachment ri:filename="default_sequence_flow.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Creating and Using a Sequence Flow" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dab14980-bc5e-4d79-bf2f-215ae73ca5e1"><ac:rich-text-body><p>A default Sequence flow does not have a condition expression.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>To change direction of Sequence Flow</p><hr style="" /><ul><li>Right-click the Sequence Flow and from the shortcut menu, select <strong>Refactor</strong> &gt; <strong>Reverse Direction</strong>.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Sequence+Flow" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Sequence Flow</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagrams</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Tasks" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Tasks</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+SubProcesses" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using SubProcesses</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Activities">Using Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Common+BPMN+Elements">Using Common BPMN Elements</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Navigation+Between+BPMN+Diagrams">Navigation Between BPMN Diagrams</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032086 space=CBMP2024x version=1 -->
## PAGE 00069: Creating and Using Choreography Task

- page_id: `290032086`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032086/Creating+and+Using+Choreography+Task
- version_number: 1
- version_date: `2026-02-09T15:59:44.336+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Choreography Diagram
- labels: []

### NORMALIZED CONTENT

A Choreography Task can have references to Message Flows, existing among referenced Resources.

To create a Choreography Task

- On the diagram pallet, click Choreography Task .

To select Message Flows referenced by a Choreography Task

1. Open the Choreography Task Specification window.
2. Select Message Flow property value cell and click the ... button. The Select Message Flows dialog opens.
3. Select the Message Flows and click OK .

If the Message Flows, which are referenced by a Choreography Task, have the Messages specified, they will be displayed and attached to the Choreography Task in the diagram.

To specify Messages for a Choreography Task

1. Create a BPMN Collaboration diagram with Pools representing Resources and Message Flows with Messages.
2. On a BPMN Choreography diagram and create Choreography Task.
3. Open the Choreography Task Specification window. Specify the Participants for the Participant Refs property and a Participant for the Initiating Participant Ref property.
4. Select the Message Flow property and click the ... button. The Select Message Flows dialog opens.
5. Select the Message Flows you have created in step 3 as the Message Flow property value and click Close .

- Initiating Messages (connected to an initiating Participant compartment) will be displayed in yellow.
- Non-initiating messages (connected to a non-initiating Participant compartment) will be displayed in gray.

To hide the Messages for a Choreography Task, do one of the following

- Right-click a Choreography Task and select Show Messages .
- Right-click a Choreography Task and click Symbol(s) Properties . The Symbol Properties dialog opens. Select Show Messages .

**Related elements**

- Choreography Task
- Resource
- Participant
- Message
- Collaboration

**Related diagram**

- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Using Choreography Activity
- Creating SubChoreography
- Creating Call Choreography Activity
- Creating and Using Pool and Lanes
- Creating and Using Message Flow
- Using Common BPMN Elements

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Choreography Task can have references to Message Flows, existing among referenced Resources.</p><p><br /></p><p>To create a Choreography Task</p><hr style="" /><ul><li>On the diagram pallet, click <strong>Choreography Task</strong>.</li></ul><p><br /></p><p>To select Message Flows referenced by a Choreography Task</p><hr style="" /><ol><li>Open the Choreography Task Specification window.</li><li>Select <strong>Message Flow</strong> property value cell and click the <strong>...</strong> button. The <strong>Select Message Flows</strong> dialog opens.</li><li>Select the Message Flows and click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="e31ec675-b98a-4793-83ee-231f334bad97"><ac:rich-text-body>If the Message Flows, which are referenced by a Choreography Task, have the Messages specified, they will be displayed and attached to the Choreography Task in the diagram.</ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p><p>To specify Messages for a Choreography Task</p><hr style="" /><ol><li>Create a BPMN Collaboration diagram with Pools representing Resources and Message Flows with Messages.</li><li>On a BPMN Choreography diagram and create Choreography Task.</li><li>Open the Choreography Task Specification window. Specify the Participants for the <strong>Participant Refs</strong> property and a Participant for the <strong>Initiating Participant Ref</strong> property.</li><li>Select the <strong>Message Flow</strong> property and click the<strong> ...</strong> button. The <strong>Select Message Flows</strong> dialog opens. </li><li>Select the Message Flows you have created in step 3 as the <strong>Message Flow</strong> property value and click <strong>Close</strong>.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cd9069ac-8fbe-474a-a3fe-9e53e99cc7b8"><ac:rich-text-body><ul><li>Initiating Messages (connected to an initiating Participant compartment) will be displayed in yellow.</li><li>Non-initiating messages (connected to a non-initiating Participant compartment) will be displayed in gray.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To hide the Messages for a Choreography Task, do one of the following</p><hr style="" /><ul><li>Right-click a Choreography Task and select <strong>Show Messages</strong>.</li><li>Right-click a Choreography Task and click <strong>Symbol(s) Properties</strong>. The <strong>Symbol Properties</strong> dialog opens. Select <strong>Show Messages</strong>.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Task" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Choreography Task</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Participant">Participant</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Message">Message</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Collaboration">Collaboration</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Choreography+Activity" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using Choreography Activity</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+SubChoreography">Creating SubChoreography</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+Call+Choreography+Activity">Creating Call Choreography Activity</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Pool+and+Lanes">Creating and Using Pool and Lanes</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Message+Flow">Creating and Using Message Flow</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Common+BPMN+Elements">Using Common BPMN Elements</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032082 space=CBMP2024x version=1 -->
## PAGE 00070: Creating and Using Conversation Nodes

- page_id: `290032082`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032082/Creating+and+Using+Conversation+Nodes
- version_number: 1
- version_date: `2026-02-09T15:57:54.393+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

A Conversation groups messages exchanged among collaboration participants.

To create a Communication between two Pools

1. Create a Conversation and Pool.
2. Create a Conversation Link from the Conversation to a Pool.
3. Draw another Conversation Link from the Conversation to another Pool.

A Pool requires a specified Representing Resource.

To select Message Flows grouped by a Conversation

1. Do one of the following: The **Select Message Flows** dialog opens. It shows all Message Flows that are grouped by a Conversation.
  - 
    - Open the Conversation shape Specification window. Select the Message Flow Refs property value cell and then click the ... button.
    - Select a Communication shape and on the Smart Manipulator toolbar, click the Message Flows button.
2. Select one or more Message Flows and click **OK**. When the Show Message Flows Related to Participants check box is selected, only the message flows that exist in a project between the Representing Participants of the pools connected by a Conversation will show. 
Click to clear the check box to see all message flows in a project.

You can also assign a Message Flow to a Conversation by dragging it from the Containment tree to a Conversation shape on the BPMN Collaboration diagram.

To create a SubConversation

- On the diagram pallet, click SubConversation .

A SubConversation can contain inner Conversation Nodes (Conversation and SubConversation).

To create a Conversation Node for a SubConversation, do one of the following

- Select SubConversation and on the Smart manipulator toolbar, click the SubConversation button.
- Open the Specification window, select Conversation Nodes in the property group list on the left. Click the Create button and select a Node type. Type the name and click Close .

A CallConversation can reference Collaboration or Global Conversation.

To create a CallConversation

- On the diagram pallet, click SubConversation .

**Related elements**

- Conversation
- SubConversation
- Call Conversation
- Message
- Message Flow
- Pool and Lane

**Related diagram**

- BPMN Collaboration Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Pool and Lanes
- Creating and Using Message Flow
- Creating and Using Participant

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Conversation groups messages exchanged among collaboration participants.</p><p><br /></p><p>To create a Communication between two Pools</p><hr style="" /><ol><li>Create a Conversation and Pool.</li><li>Create a Conversation Link from the Conversation to a Pool.</li><li>Draw another Conversation Link from the Conversation to another Pool.</li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ffb582e6-22d5-43ad-b1ca-5fcfdc4ad2c8"><ac:rich-text-body>A Pool requires a specified Representing Resource.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To select Message Flows grouped by a Conversation</p><hr style="" /><ol><li>Do one of the following:<ul><li style="list-style-type: none;background-image: none;"><ul><li>Open the Conversation shape <strong>Specification</strong> window. Select the <strong>Message Flow Refs</strong> property value cell and then click the<strong> ...</strong> button.</li><li>Select a Communication shape and on the Smart Manipulator toolbar, click the <strong>Message Flows</strong> button.</li></ul></li></ul><p>The <strong>Select Message Flows</strong> dialog opens. It shows all Message Flows that are grouped by a Conversation.</p></li><li><p class="auto-cursor-target">Select one or more Message Flows and click <strong>OK</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fddd82af-bd7b-46d3-8654-ab6d14d78a66"><ac:rich-text-body><p>When the Show Message Flows Related to Participants check box is selected, only the message flows that exist in a project between the Representing Participants of the pools connected by a Conversation will show.<br />Click to clear the check box to see all message flows in a project.</p></ac:rich-text-body></ac:structured-macro></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="11f511bc-486c-4df6-a67a-a77407248fd9"><ac:rich-text-body><p>You can also assign a Message Flow to a Conversation by dragging it from the Containment tree to a Conversation shape on the BPMN Collaboration diagram.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>To create a SubConversation</p><hr style="" /><ul><li>On the diagram pallet, click <strong>SubConversation</strong>.</li></ul><p>A SubConversation can contain inner Conversation Nodes (Conversation and SubConversation).</p><p><br /></p><p>To create a Conversation Node for a SubConversation, do one of the following</p><hr style="" /><ul><li>Select SubConversation and on the Smart manipulator toolbar, click the <strong>SubConversation</strong> button.</li><li>Open the Specification window, select <strong>Conversation Nodes</strong> in the property group list on the left. Click the <strong>Create</strong> button and select a Node type. Type the name and click <strong>Close</strong>.</li></ul><p>A CallConversation can reference Collaboration or Global Conversation.</p><p><br /></p><p>To create a CallConversation</p><hr style="" /><ul><li>On the diagram pallet, click <strong>SubConversation</strong>.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Conversation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Conversation</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/SubConversation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">SubConversation</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Call+Conversation">Call Conversation</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Message">Message</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Message+Flow">Message Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Pool+and+Lanes">Creating and Using Pool and Lanes</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Message+Flow">Creating and Using Message Flow</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Participant">Creating and Using Participant</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032075 space=CBMP2024x version=1 -->
## PAGE 00071: Creating and Using Data Items

- page_id: `290032075`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032075/Creating+and+Using+Data+Items
- version_number: 1
- version_date: `2026-02-09T15:53:59.341+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

You can create the following data items in a BPMN Process diagram:

- [CONFLUENCE_PAGE title='Data Object' space='CBMP2024x']
- [CONFLUENCE_PAGE title='Data Store' space='CBMP2024x']
- [CONFLUENCE_PAGE title='Data Input and Data Output' space='CBMP2024x']

You can mark a Data Object as a collection.

With a Data Association, you can connect a data item to other elements of the BPMN Process diagram.

To create a data item

Business Analyst perspective provide most popular SubProcess types. Full list ofSubProcesses types you can have only in Business Modeler and Full Featured perspectives.

- On the Process diagram pallet, click Data Objec t and select needed Data item.

To create a new Data Object, which is typed by a classifier

- Select the classifier in the Containment tree and drag it to a BPMN Process or BPMN Collaboration diagram.

To specify a type of Data Item, do one of the following

- In the Containment tree, select an element and drag it on the Data Item.
- Right-click the Data Item, from the shortcut menu, select Type and choose the needed type.
- Open the Specification window and select a Type.

To mark a Data Object as collection, do one of the following

- Right-click the Data Object and from the shortcut menu choose Is Collection > true .
- Open the Data Object Specification window, Is Collection property set to true.

To create a Data Association between two data items

1. On the Process diagram pallet, click the Data Association button.
2. On the diagram pane
  - Click an element, which will be the source of the Data Association.
  - Click an element, which will be the target of the Data Association.

- The source or target of a Data Association can only be a Data Object, Data Store, Data Input, or Data Output.
- The other end of the Data Association should always be an activity or event.

To display a Data Object directly connected to a Sequence Flow

A Data Object connected to a Sequence Flow is a visual shortcut of two Data Associations.In the model, the Data Associations still exist, and the Data Object connecting to the Sequence Flow will be displayed.

1. Draw a Data Association from an Activity to a Data Object.
2. Draw another Data Association from the Data Object to another Activity.
3. Draw a Sequence Flow from the first to the second Activity.
4. Right-click the Data Object and select Show Connected to Sequence Flow from the shortcut menu.

**Related element**

- Common BPMN Elements

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Tasks
- Creating and Using SubProcesses
- Using Activities
- Creating and Using an Event
- Creating and Using a Sequence Flow
- Navigation Between BPMN Diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can create the following data items in a BPMN Process diagram:</p><ul><li><ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Object" /></ac:link></li><li><ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Store" /></ac:link></li><li><ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Input and Data Output" /></ac:link></li></ul><p>You can mark a Data Object as a collection.</p><p>With a Data Association, you can connect a data item to other elements of the BPMN Process diagram.</p><p><br /></p><p>To create a data item</p><hr /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="2ae59501-80ba-47c3-81c1-6195979319dc"><ac:rich-text-body>Business Analyst perspective provide most popular SubProcess types. Full list ofSubProcesses types you can have only in Business Modeler and Full Featured perspectives.</ac:rich-text-body></ac:structured-macro><ul><li>On the <strong>Process</strong> diagram pallet, click <strong>Data Objec</strong>t and select needed Data item.</li></ul><p><br /></p><p>To create a new Data Object, which is typed by a classifier</p><hr /><ul><li>Select the classifier in the Containment tree and drag it to a BPMN Process or BPMN Collaboration diagram.</li></ul><p><br /></p><p>To specify a type of Data Item, do one of the following</p><hr /><ul><li>In the Containment tree, select an element and drag it on the Data Item.</li><li>Right-click the Data Item, from the shortcut menu, select Type and choose the needed type.</li><li>Open the Specification window and select a Type.</li></ul><p><br /></p><p>To mark a Data Object as collection, do one of the following</p><hr /><ul><li>Right-click the Data Object and from the shortcut menu choose <strong>Is Collection</strong> &gt; <strong>true</strong>.</li><li>Open the Data Object Specification window, <strong>Is Collection</strong> property set to true.</li></ul><p><br /></p><p>To create a Data Association between two data items</p><hr /><ol><li>On the Process diagram pallet, click the <strong>Data Association</strong> button.</li><li>On the diagram pane<ul><li>Click an element, which will be the source of the Data Association.</li><li>Click an element, which will be the target of the Data Association.</li></ul></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="eecd0ebf-5961-40cb-90e2-968c01a61ff2"><ac:rich-text-body><ul><li>The source or target of a Data Association can only be a Data Object, Data Store, Data Input, or Data Output.</li><li>The other end of the Data Association should always be an activity or event.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>To display a Data Object directly connected to a Sequence Flow</p><hr /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e38d3546-acb6-4895-9c34-8f7ebdcd1f27"><ac:rich-text-body>A Data Object connected to a Sequence Flow is a visual shortcut of two Data Associations.In the model, the Data Associations still exist, and the Data Object connecting to the Sequence Flow will be displayed.</ac:rich-text-body></ac:structured-macro><ol><li>Draw a Data Association from an Activity to a Data Object.</li><li>Draw another Data Association from the Data Object to another Activity.</li><li>Draw a Sequence Flow from the first to the second Activity.</li><li>Right-click the Data Object and select <strong>Show Connected to Sequence Flow</strong> from the shortcut menu.</li></ol><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Common+BPMN+Elements">Common BPMN Elements</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Tasks">Creating and Using Tasks</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+SubProcesses">Creating and Using SubProcesses</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Activities">Using Activities</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Navigation+Between+BPMN+Diagrams">Navigation Between BPMN Diagrams</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032081 space=CBMP2024x version=1 -->
## PAGE 00072: Creating and Using Message Flow

- page_id: `290032081`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032081/Creating+and+Using+Message+Flow
- version_number: 1
- version_date: `2026-02-09T15:57:28.718+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

To draw a Message Flow between two elements or Pools, do one of the following

- On the Collaboration diagram pallet, click Message Flow button and connect appropriate shapes.
- Select the Pool header and on the Smart manipulator toolbar, click the Message Flow button. A Message Flow must connect two different Pools or inner elements of different Pools.

To create a new Message for a Message Flow, which is typed by a classifier, by using drag and drop operation

- Select the classifier (Class, Input Set, Output Set, or Error) in the Containment tree and drag it to a Message Flow on a Collaboration diagram.

To create a Message for a Message Flow from the Smart Manipulator toolbar

You can create a Message in a BPMN Process, Collaboration, Choreography, or SubProcess element.

1. On the diagram pane, select a Message Flow path and on the Smart Manipulator toolbar, click the Referenced Messages button. The Select Message dialog opens.
2. Select a Collaboration where you want to create a new message and click the Creation Mode button.
3. Select a Collaboration element and click the Create button.
4. Click OK .

To change a Message display mode

- Right-click a Message Flow and from the shortcut menu select one of the following:
  - Show Message and select a message display mode.
  - Symbol(s) Properties and select the needed Show Message property value.

To change direction of Message Flow

- Right-click the Message Flow and from the shortcut menu, select Refactor > Reverse Direction .

**Related elements**

- Message
- Message Flow
- Pool and Lane

**Related diagram**

- BPMN Collaboration Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Pool and Lanes
- Creating and Using Conversation Nodes
- Creating and Using Participant

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To draw a Message Flow between two elements or Pools, do one of the following</p><hr /><ul><li>On the Collaboration diagram pallet, click <strong>Message Flow</strong> button and connect appropriate shapes.</li><li><p class="auto-cursor-target">Select the Pool header and on the Smart manipulator toolbar, click the Message Flow button.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="583a423f-dc55-4f2c-a02b-26691645c12e"><ac:rich-text-body><p>A Message Flow must connect two different Pools or inner elements of different Pools.</p></ac:rich-text-body></ac:structured-macro></li></ul><p>To create a new Message for a Message Flow, which is typed by a classifier, by using drag and drop operation</p><hr /><ul><li>Select the classifier (Class, Input Set, Output Set, or Error) in the Containment tree and drag it to a Message Flow on a Collaboration diagram.</li></ul><p><br /></p><p>To create a Message for a Message Flow from the Smart Manipulator toolbar</p><hr /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c18eee7a-dd6c-482b-b920-f484ea26ceaf"><ac:rich-text-body><p>You can create a Message in a BPMN Process, Collaboration, Choreography, or SubProcess element.</p></ac:rich-text-body></ac:structured-macro><ol><li>On the diagram pane, select a Message Flow path and on the Smart Manipulator toolbar, click the Referenced Messages button. The <strong>Select Message</strong> dialog opens.</li><li>Select a Collaboration where you want to create a new message and click the <strong>Creation Mode</strong> button.</li><li>Select a Collaboration element and click the <strong>Create</strong> button.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To change a Message display mode</p><hr /><ul><li>Right-click a Message Flow and from the shortcut menu select one of the following:<ul><li><strong>Show Message</strong> and select a message display mode.</li><li><strong>Symbol(s) Properties</strong> and select the needed <strong>Show Message</strong> property value.</li></ul></li></ul><p><br /></p><p>To change direction of Message Flow</p><hr /><ul><li>Right-click the Message Flow and from the shortcut menu, select <strong>Refactor</strong> &gt; <strong>Reverse Direction</strong>.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Message">Message</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Message+Flow">Message Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane">Pool and Lane</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Pool+and+Lanes">Creating and Using Pool and Lanes</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Conversation+Nodes">Creating and Using Conversation Nodes</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Participant">Creating and Using Participant</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032083 space=CBMP2024x version=1 -->
## PAGE 00073: Creating and Using Participant

- page_id: `290032083`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032083/Creating+and+Using+Participant
- version_number: 1
- version_date: `2026-02-09T15:58:22.457+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

To create a Participant

- Right-click the BPMN Collaboration or Choreography element in the Containment tree and from the shortcut menu, select Create Element > Participant .

To create a multi-instance Participant

1. Right-click a created Participant in the Containment tree and select Specification from the shortcut menu. The Participant Specification window opens.
2. In the Participant Specification window, under the Multiplicity category in the General property group, type the Minimum property value (“2” or greater).

The Minimum Multiplicity value of a MultiInstance participant propertymust be “2” or greater.

**Related elements**

- Participant
- Pool and Lane
- Choreography Activities

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Using BPMN Collaboration Diagram
- Using BPMN Choreography Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To create a Participant</p><hr style="" /><ul><li>Right-click the BPMN Collaboration or Choreography element in the Containment tree and from the shortcut menu, select <strong>Create Element</strong> &gt; <strong>Participant</strong>.</li></ul><p><br /></p><p>To create a multi-instance Participant</p><hr style="" /><ol><li>Right-click a created Participant in the Containment tree and select <strong>Specification</strong> from the shortcut menu. The Participant Specification window opens.</li><li>In the Participant Specification window, under the <strong>Multiplicity</strong> category in the <strong>General</strong> property group, type the <strong>Minimum property value</strong> (“2” or greater).</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="f615a87b-e7c9-4637-a4c6-c7b16c928e5b"><ac:rich-text-body>The Minimum Multiplicity value of a MultiInstance participant propertymust be “2” or greater.</ac:rich-text-body></ac:structured-macro><p style="margin-top: 0.0px;"><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Participant">Participant</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Collaboration+Diagram">Using BPMN Collaboration Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Choreography+Diagram">Using BPMN Choreography Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032080 space=CBMP2024x version=1 -->
## PAGE 00074: Creating and Using Pool and Lanes

- page_id: `290032080`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032080/Creating+and+Using+Pool+and+Lanes
- version_number: 1
- version_date: `2026-02-09T15:55:49.100+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

A Pool in a BPMN collaboration diagram represents a participant of a collaboration. A Pool can have its inner process flows defined. You can add the elements from a BPMN Process diagram to a pool. You can also hide the pool details by displaying a “black box” pool. A Pool can also have inner lanes.

To create a Pool from Diagram pallet

1. On the Collaboration Diagram pallet, click Horizontal Pool and select a needed type of Pool.
2. Select Resources and click OK .

To create a Pool with a representing Resources from the Containment tree

- Drag a Resource, Organization, Post, or Person from the Containment tree to a BPMN Collaboration diagram pane.

To create a Pool with a suppressed content

- On the Collaboration Diagram pallet, under Conversations click Participant (Pool) .

To add Lane to a Pool, do one of the following

- Right-click a Pool, point to Insert Inner Lanes or Insert Lanes and select a lane type.
- Right-click a Pool header and click to select Insert Lanes .

To open a Pool Specification window

- Right-click the Pool header and select Specification .

To specify a model element represented by a Pool or Lane, do one of the following

A Pool can represent a BPMN Resource element or UML classifier element.

- Click a Pool or Lane header on the diagram. On the Smart Manipulators toolbar click the Represents button.
- Open the Pool or Lane Specification window, click **Represents** and select the represented elements from drop down list. Any type of element you can select only from Specification window.
- Select a represented element in the Containment tree and drag it to the Pool or Lane header on the diagram.

To hide a Pool content on a diagram (to display a “black box” pool)

- Right-click a Pool header and from the shortcut menu select one of the following:
  - Suppress Pool Content
  - Symbol(s) Properties and in the open dialog set the Suppress Pool Content property value to true.

A Pool with suppressed content that references a MultiInstance Participant will be displayed with a MultiInstance marker.

To display a MultiInstance marker on a Pool

1. Open the Specification window.
2. Click **Represents** and select a represented multi-instance Participant. A MultiInstance marker can be displayed only on a Poll with suppressed contents.

To review the Pool or Lane traceability information

- Open the Specification window, click Traceability .

**Related elements**

- Resource
- Participant
- Pool and Lane
- Organization Unit
- Role
- Person
- Information system

**Related diagram**

- BPMN Collaboration Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Message Flow
- Creating and Using Conversation Nodes
- Creating and Using Participant
- Using Common BPMN Elements

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Pool in a BPMN collaboration diagram represents a participant of a collaboration. A Pool can have its inner process flows defined. You can add the elements from a BPMN Process diagram to a pool. You can also hide the pool details by displaying a “black box” pool. A Pool can also have inner lanes.</p><p><br /></p><p>To create a Pool from Diagram pallet</p><hr style="" /><ol><li>On the Collaboration Diagram pallet, click <strong>Horizontal Pool</strong> and select a needed type of Pool.</li><li>Select Resources and click <strong>OK</strong>.</li></ol><p><br /></p><p>To create a Pool with a representing Resources from the Containment tree</p><hr style="" /><ul><li>Drag a Resource, Organization, Post, or Person from the Containment tree to a BPMN Collaboration diagram pane.</li></ul><p><br /></p><p>To create a Pool with a suppressed content</p><hr style="" /><ul><li>On the Collaboration Diagram pallet, under <strong>Conversations</strong> click <strong>Participant (Pool)</strong>.</li></ul><p><br /></p><p>To add Lane to a Pool, do one of the following</p><hr style="" /><ul><li>Right-click a Pool, point to <strong>Insert Inner Lanes</strong> or <strong>Insert Lanes</strong> and select a lane type.</li><li>Right-click a Pool header and click to select <strong>Insert Lanes</strong>.</li></ul><p><br /></p><p>To open a Pool Specification window</p><hr style="" /><ul><li>Right-click the Pool header and select <strong>Specification</strong>.</li></ul><p><br /></p><p>To specify a model element represented by a Pool or Lane, do one of the following</p><hr style="" /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f77c8e05-ba6d-48e8-befc-72902e18da92"><ac:rich-text-body>A Pool can represent a BPMN Resource element or UML classifier element.</ac:rich-text-body></ac:structured-macro><ul><li>Click a Pool or Lane header on the diagram. On the Smart Manipulators toolbar click the <strong>Represents</strong> button.</li><li><p>Open the Pool or Lane Specification window, click <strong>Represents</strong> and select the represented elements from drop down list.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ec55315d-89d1-46a5-9fa6-b901b453ea55"><ac:rich-text-body><p>Any type of element you can select only from Specification window.</p></ac:rich-text-body></ac:structured-macro></li><li><p>Select a represented element in the Containment tree and drag it to the Pool or Lane header on the diagram.</p></li></ul><p><br /></p><p>To hide a Pool content on a diagram (to display a “black box” pool)</p><hr style="" /><ul><li>Right-click a Pool header and from the shortcut menu select one of the following:<ul><li><strong>Suppress Pool Content</strong></li><li><strong>Symbol(s) Properties</strong> and in the open dialog set the <strong>Suppress Pool Content</strong> property value to true.</li></ul></li></ul><p>A Pool with suppressed content that references a MultiInstance Participant will be displayed with a MultiInstance marker.</p><p><br /></p><p>To display a MultiInstance marker on a Pool</p><hr style="" /><ol><li>Open the Specification window.</li><li><p class="auto-cursor-target">Click <strong>Represents</strong> and select a represented multi-instance Participant.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="eae4f50c-0c1a-45e4-ad82-f95f45ef0cfd"><ac:rich-text-body><p>A MultiInstance marker can be displayed only on a Poll with suppressed contents.</p></ac:rich-text-body></ac:structured-macro></li></ol><p><br /></p><p>To review the Pool or Lane traceability information</p><hr style="" /><ul><li>Open the Specification window, click <strong>Traceability</strong>.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Participant">Participant</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Message+Flow">Creating and Using Message Flow</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Conversation+Nodes">Creating and Using Conversation Nodes</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Participant">Creating and Using Participant</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Common+BPMN+Elements">Using Common BPMN Elements</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032068 space=CBMP2024x version=1 -->
## PAGE 00075: Creating and Using SubProcesses

- page_id: `290032068`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032068/Creating+and+Using+SubProcesses
- version_number: 1
- version_date: `2026-02-09T15:49:36.387+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

A BPMN diagram can display subprocesses with different symbol properties. They are as follows:

- An expanded SubProcess can contain inner shapes.
- A collapsed SubProcess cannot display inner shapes. A plus sign (+) marker will be displayed for a collapsed subprocess.

If the *Is Triggered By Event* property of a SubProcess is set to true, it will call an Event SubProcess and will be drawn with a dashed border.

There are two specific types of SubProcesses:

- Transaction SubProcess. It is represented with double borders.
- AdHoc SubProcess. It is represented with an AdHoc marker on its shape.

To create a SubProcess

Business Analyst perspective provide most popular SubProcess types. Full list of SubProcesses types you can have only in Business Modeler and Full Featured perspectives.

1. Open a BPMN Process diagram.
2. On the diagram pallet, click the arrow next to the SubProcess and select the needed type of SubProcess.

To expand a SubProcess, do one of the following

- Right-click a SubProcess shape and from the shortcut menu select Symbol(s) Properties. Then, in the Symbol Properties dialog, click to clear the Suppress Content .
- Right-click a SubProcess shape and in the shortcut menu click to clear Suppress Content.

To collapse SubProcess, do one of the following

- Right-click a SubProcess shape and then on the shortcut menu click to select Suppress Content.
- Right-click a SubProcess shape and from the shortcut menu select Symbol(s) Properties. Then in the Symbol Properties dialog click to select the Suppress Content.

To mark a created SubProcess as an event SubProcess, do one of the following

- Right-click the SubProcess and on the shortcut menu click to select Triggered By Event .
- Open the SubProcess Specification window. Select the Triggered By Event check box.

To convert a SubProcess to a Transaction SubProcess or AdHoc SubProcess

- Right-click the SubProcess and from the shortcut menu select Refactor > Convert To > More Specific > AdHoc SubProcess or Transaction SubProcess .

To convert a Transaction SubProcess or AdHoc SubProcess to a SubProcess

- Right-click the Ad Hoc SubProcess or Transaction SubProcess and from shortcut menu select Refactor > Convert To > More General > SubProcess .

To display a Start Event icon on a Event SubProcess

1. Create an expanded Event SubProcess.
2. Create a Start Event to the Event SubProcess.
3. Right-click the SubProcess and click to select the Suppress Content check box.

**Related element**

- SubProcesses

**Related Diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Tasks
- Using Activities
- Creating and Using an Event
- Creating and Using a Sequence Flow
- Creating and Using Data Items
- Navigation Between BPMN Diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A BPMN diagram can display subprocesses with different symbol properties. They are as follows:</p><ul><li>An expanded SubProcess can contain inner shapes.</li><li>A collapsed SubProcess cannot display inner shapes. A plus sign (+) marker will be displayed for a collapsed subprocess.</li></ul><p>If the <em>Is Triggered By Event</em> property of a SubProcess is set to true, it will call an Event SubProcess and will be drawn with a dashed border.</p><p>There are two specific types of SubProcesses:</p><ul><li>Transaction SubProcess. It is represented with double borders.</li><li>AdHoc SubProcess. It is represented with an AdHoc marker on its shape.</li></ul><p><br /></p><p>To create a SubProcess</p><hr style="" /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="dcff3241-113d-4ad5-95e1-319a492ccf50"><ac:rich-text-body><p>Business Analyst perspective provide most popular SubProcess types. Full list of SubProcesses types you can have only in Business Modeler and Full Featured perspectives.</p></ac:rich-text-body></ac:structured-macro><ol><li>Open a BPMN Process diagram.</li><li>On the diagram pallet, click the arrow next to the SubProcess and select the needed type of SubProcess.</li></ol><p><br /></p><p>To expand a SubProcess, do one of the following</p><hr style="" /><ul><li>Right-click a SubProcess shape and from the shortcut menu select Symbol(s) Properties. Then, in the Symbol Properties dialog, click to clear the <strong>Suppress Content</strong>.</li><li>Right-click a SubProcess shape and in the shortcut menu click to clear Suppress Content.</li></ul><p><br /></p><p>To collapse SubProcess, do one of the following</p><hr style="" /><ul><li>Right-click a SubProcess shape and then on the shortcut menu click to select Suppress Content.</li><li>Right-click a SubProcess shape and from the shortcut menu select Symbol(s) Properties. Then in the Symbol Properties dialog click to select the Suppress Content.</li></ul><p><br /></p><p>To mark a created SubProcess as an event SubProcess, do one of the following</p><hr style="" /><ul><li>Right-click the SubProcess and on the shortcut menu click to select <strong>Triggered By Event</strong>.</li><li>Open the SubProcess Specification window. Select the <strong>Triggered By Event</strong> check box.</li></ul><p><br /></p><p>To convert a SubProcess to a Transaction SubProcess or AdHoc SubProcess</p><hr style="" /><ul><li>Right-click the SubProcess and from the shortcut menu select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>AdHoc SubProcess</strong> or <strong>Transaction SubProcess</strong>.</li></ul><p><br /></p><p>To convert a Transaction SubProcess or AdHoc SubProcess to a SubProcess</p><hr style="" /><ul><li>Right-click the Ad Hoc SubProcess or Transaction SubProcess and from shortcut menu select <strong>Refactor</strong> &gt;<strong> Convert To</strong> &gt;<strong> More General</strong>&gt; <strong>SubProcess</strong>.</li></ul><p><br /></p><p>To display a Start Event icon on a Event SubProcess</p><hr style="" /><ol><li>Create an expanded Event SubProcess.</li><li>Create a Start Event to the Event SubProcess.</li><li>Right-click the SubProcess and click to select the <strong>Suppress Content</strong> check box.</li></ol><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/SubProcesses">SubProcesses</a></li></ul><p><strong>Related Diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Tasks" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Tasks</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Activities">Using Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Navigation+Between+BPMN+Diagrams">Navigation Between BPMN Diagrams</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032067 space=CBMP2024x version=1 -->
## PAGE 00076: Creating and Using Tasks

- page_id: `290032067`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032067/Creating+and+Using+Tasks
- version_number: 1
- version_date: `2026-02-09T15:49:04.338+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

There are multiple types of Tasks that you can create in a BPMN Process diagram.

To create a Task

1. Open a Process diagram.
2. On the diagram pallet, click the Task button and select a type of Task you need to create.

To change a task type

- Right-click a Task and select one of the following task types:
  - Business Rule Task
  - Manual Task
  - Receive Task
  - Script Task
  - Send Task
  - Service Task
  - User Task

**Related element**

- Tasks

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using SubProcesses
- Using Activities
- Creating and Using an Event
- Creating and Using a Sequence Flow
- Creating and Using Data Items
- Navigation Between BPMN Diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>There are multiple types of Tasks that you can create in a BPMN Process diagram.</p><p><br /></p><p>To create a Task</p><hr style="" /><ol><li>Open a Process diagram.</li><li>On the diagram pallet, click the <strong>Task</strong> button and select a type of Task you need to create.</li></ol><p><br /></p><p>To change a task type</p><hr style="" /><ul><li>Right-click a Task and select one of the following task types:<ul><li>Business Rule Task</li><li>Manual Task</li><li>Receive Task</li><li>Script Task</li><li>Send Task</li><li>Service Task</li><li>User Task</li></ul></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Tasks">Tasks</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+SubProcesses" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using SubProcesses</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Activities">Using Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Navigation+Between+BPMN+Diagrams">Navigation Between BPMN Diagrams</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031686 space=CBMP2024x version=1 -->
## PAGE 00077: Creating BPMN Projects

- page_id: `290031686`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031686/Creating+BPMN+Projects
- version_number: 1
- version_date: `2026-02-09T13:47:54.059+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Getting Started
- labels: []

### NORMALIZED CONTENT

To create a new project from template, you can choose one of the following templates:

- A BPMN2 Project, which provides the workspace for business process modeling. This project is empty.
- A Business Model project, which provides workspace with predefined project structure and guidelines how to create business model.

The Cameo SOA+ plugin is discontinued. However, you can load projects created in earlier versions with this plugin in your modeling tool. SoaML diagrams will be converted to pure UML diagrams and maintenance of the SoaML profile will continue. The SoaML Profile is available through the **Resource / Plugin Manager**.

To create a new workspace for an empty project

1. Do one of the following:
  - On the main menu, click File > New Project .
  - Click the [ATTACHMENT filename='new_project.png'] button on the File toolbar.
  - Press Ctrl + N.
2. In the New Project dialog, select the project template under the Business Process Modeling domain. [ATTACHMENT filename='bpm_select.png']
3. Specify the file name in the Name box.
4. Click the ... button to define the location for storing your newly created project in your computer.
5. Click OK .

If you work not in the Business Analyst perspective, a message asking whether you want to change the perspective will open. Click Yes to switch to the Business Analyst perspective supporting business modeling diagrams.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To create a new project from template, you can choose one of the following templates:</p><ul><li>A BPMN2 Project, which provides the workspace for business process modeling. This project is empty.</li><li>A Business Model project, which provides workspace with predefined project structure and guidelines how to create business model.<br /><br /></li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="07e5988e-5c6d-461c-bbd4-02a24ba8603d"><ac:rich-text-body><p>The Cameo SOA+ plugin is discontinued. However, you can load projects created in earlier versions with this plugin in your modeling tool. SoaML diagrams will be converted to pure UML diagrams and maintenance of the SoaML profile will continue. The SoaML Profile is available through the <strong>Resource / Plugin Manager</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p>To create a new workspace for an empty project</p><hr /><ol><li>Do one of the following:<ul><li>On the main menu, click <strong>File</strong> &gt; <strong>New Project</strong>.</li><li>Click the <ac:image><ri:attachment ri:filename="new_project.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Creating BPMN Projects" /></ri:attachment></ac:image> button on the File toolbar.</li><li>Press Ctrl + N.</li></ul></li><li>In the <strong>New Project</strong> dialog, select the project template under the <strong>Business Process Modeling</strong> domain.<br /><ac:image><ri:attachment ri:filename="bpm_select.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Creating BPMN Projects" /></ri:attachment></ac:image> </li><li>Specify the file name in the Name box.</li><li>Click the <strong>...</strong> button to define the location for storing your newly created project in your computer.</li><li>Click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2406c105-99d3-4eda-8556-22f4495ff26f"><ac:rich-text-body><p>If you work not in the Business Analyst perspective, a message asking whether you want to change the perspective will open. Click Yes to switch to the Business Analyst perspective supporting business modeling diagrams.</p></ac:rich-text-body></ac:structured-macro><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032088 space=CBMP2024x version=1 -->
## PAGE 00078: Creating Call Choreography Activity

- page_id: `290032088`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032088/Creating+Call+Choreography+Activity
- version_number: 1
- version_date: `2026-02-09T16:00:34.838+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Choreography Diagram
- labels: []

### NORMALIZED CONTENT

Business Analyst perspective provide most popular Call Choreographytypes. Full list of Call Choreography types you can have only in Business Modeler and Full Featured perspectives.

A Call Choreography Activity holds a reference to a Choreography.

To create a Call Choreography Activity

1. On the diagram pallet, click Call Choreography Activity. The Select Behavior dialog opens.
2. Select a Choreography Activity .
3. Click OK .

To change the element called by a Call Choreography Activity

- Right-click a Call Choreography Activity and click Called Choreography Ref . Select a Choreography from the elements list.
- Open the Call Choreography Activity Specification window. Click Called Choreography Ref and select a Choreography as property value.

**Related element**

- Call Choreography

**Related diagram**

- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Using Choreography Activity
- Creating and Using Choreography Task
- Creating SubChoreography
- Creating Call Choreography Activity
- Using Common BPMN Elements

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="46066d2f-c6ce-4108-bf46-99d43945a4b4"><ac:rich-text-body>Business Analyst perspective provide most popular Call Choreographytypes. Full list of Call Choreography types you can have only in Business Modeler and Full Featured perspectives.</ac:rich-text-body></ac:structured-macro><p style="margin-top: 0.0px;">A Call Choreography Activity holds a reference to a Choreography.</p><p><br /></p><p>To create a Call Choreography Activity</p><hr style="" /><ol><li>On the diagram pallet, click <strong>Call Choreography</strong> Activity. The <strong>Select Behavior</strong> dialog opens.</li><li>Select a <strong>Choreography Activity</strong>.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To change the element called by a Call Choreography Activity</p><hr style="" /><ul><li>Right-click a Call Choreography Activity and click <strong>Called Choreography Ref</strong>. Select a <strong>Choreography</strong> from the elements list.</li><li>Open the Call Choreography Activity Specification window. Click <strong>Called Choreography Ref</strong> and select a <strong>Choreography</strong> as property value.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Call+Choreography" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Call Choreography</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Choreography+Activity" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using Choreography Activity</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Choreography+Task" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Choreography Task</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+SubChoreography">Creating SubChoreography</a></li><li class="current"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+Call+Choreography+Activity">Creating Call Choreography Activity</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Common+BPMN+Elements">Using Common BPMN Elements</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032087 space=CBMP2024x version=1 -->
## PAGE 00079: Creating SubChoreography

- page_id: `290032087`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032087/Creating+SubChoreography
- version_number: 1
- version_date: `2026-02-09T16:00:06.518+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Choreography Diagram
- labels: []

### NORMALIZED CONTENT

A SubChoreography can be displayed with different symbol properties:

- An Expanded SubChoreography can contain inner shapes.
- A Collapsed SubChoreography cannot display inner shapes. A plus sign (+) marker is displayed for a collapsed subprocess.

To create SubChoreography

- On the Choreography diagram pallet, click SubChoreography and select a needed SubChoreography.

To expand a SubChoreography, do one of the following

- Right-click a SubChoreography and on the shortcut menu select Suppress Content .
- Right-click a SubChoreography and select Symbol(s) Properties . The Symbol Properties dialog opens. Select or clear the Suppress Content and click OK .

To collapse a SubChoreography, do one of the following

- Right-click a SubChoreography and on the shortcut menu clear the Suppress Content .
- Right-click a SubChoreography and select Symbol(s) Properties . The Symbol Properties dialog opens. Clear the Suppress Content and click OK .

**Related element**

- SubChoreography

**Related diagram**

- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Using Choreography Activity
- Creating and Using Choreography Task
- Creating Call Choreography Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A SubChoreography can be displayed with different symbol properties:</p><ul><li>An Expanded SubChoreography can contain inner shapes.</li><li>A Collapsed SubChoreography cannot display inner shapes. A plus sign (+) marker is displayed for a collapsed subprocess.</li></ul><p><br /></p><p>To create SubChoreography</p><hr style="" /><ul><li>On the Choreography diagram pallet, click <strong>SubChoreography</strong> and select a needed SubChoreography.</li></ul><p><br /></p><p>To expand a SubChoreography, do one of the following</p><hr style="" /><ul><li>Right-click a SubChoreography and on the shortcut menu select <strong>Suppress Content</strong>.</li><li>Right-click a SubChoreography and select <strong>Symbol(s) Properties</strong>. The <strong>Symbol Properties</strong> dialog opens. Select or clear the <strong>Suppress Content</strong> and click <strong>OK</strong>.</li></ul><p><br /></p><p>To collapse a SubChoreography, do one of the following</p><hr style="" /><ul><li>Right-click a SubChoreography and on the shortcut menu clear the <strong>Suppress Content</strong>.</li><li>Right-click a SubChoreography and select <strong>Symbol(s) Properties</strong>. The<strong> Symbol Properties</strong> dialog opens. Clear the <strong>Suppress Content</strong> and click <strong>OK</strong>.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/SubChoreography">SubChoreography</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Choreography+Activity" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using Choreography Activity</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Choreography+Task" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Choreography Task</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+Call+Choreography+Activity">Creating Call Choreography Activity</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031887 space=CBMP2024x version=1 -->
## PAGE 00080: Data Association

- page_id: `290031887`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031887/Data+Association
- version_number: 1
- version_date: `2026-02-09T14:37:11.399+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Items and Data
- labels: []

### NORMALIZED CONTENT

**Description**

A Data Association is used to model how data are pushed into or pulled from item-aware elements. Tokens do not flow along a Data Association. Therefore, they have no direct effect on the flow of a process.

Alternatively, Data Objects can be directly associated with a Sequence Flow to represent the same input or output Data Associations. This is a visual shortcut that is stored in a model as two Data Associations

- from Activity to Data Object
- from Data Object to Activity

**Example**

[IMAGE alt='' src='']

###### Data Association showing flow of Data Object.

**Related elements**

- Data Object
- Data Store
- Data Input and Data Output
- Sequence Flow

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using Data Items

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p style="margin-top: 0.0px;"><strong>Description</strong></p><p>A Data Association is used to model how data are pushed into or pulled from item-aware elements. Tokens do not flow along a Data Association. Therefore, they have no direct effect on the flow of a process.</p><p>Alternatively, Data Objects can be directly associated with a Sequence Flow to represent the same input or output Data Associations. This is a visual shortcut that is stored in a model as two Data Associations</p><ul><li>from Activity to Data Object</li><li>from Data Object to Activity</li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="data_association_ flow_data_object.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Association" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Data Association showing flow of Data Object.</h6><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Data+Object">Data Object</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Data+Store">Data Store</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Data+Input+and+Data+Output">Data Input and Data Output</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Sequence+Flow">Sequence Flow</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items">Creating and Using Data Items</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031884 space=CBMP2024x version=1 -->
## PAGE 00081: Data Input and Data Output

- page_id: `290031884`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031884/Data+Input+and+Data+Output
- version_number: 1
- version_date: `2026-02-09T14:30:06.088+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Items and Data
- labels: []

### NORMALIZED CONTENT

**Description**

Activities and processes often require data in order to execute. In addition, they may produce data during or as the result of the execution.Data requirements are captured as Data Input. The produced data are captured using a Data Output notation.

**Notation**

- Data Input [ATTACHMENT filename='data_imput.png']
- Data Output [ATTACHMENT filename='data_output.png']

**Related elements**

- Class
- Resource
- Data Association

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using Data Items

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Activities and processes often require data in order to execute. In addition, they may produce data during or as the result of the execution.Data requirements are captured as Data Input. The produced data are captured using a Data Output notation.</p><p><strong>Notation</strong></p><ul><li>Data Input<br /><ac:image><ri:attachment ri:filename="data_imput.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Input and Data Output" /></ri:attachment></ac:image></li><li>Data Output<br /><ac:image><ri:attachment ri:filename="data_output.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Input and Data Output" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Data+Association">Data Association</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031879 space=CBMP2024x version=1 -->
## PAGE 00082: Data Object

- page_id: `290031879`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031879/Data+Object
- version_number: 1
- version_date: `2026-02-09T14:29:04.658+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Items and Data
- labels: []

### NORMALIZED CONTENT

**Description**

A Data Object is an element that stores or conveys items during process execution. The Data Object elements must be contained within the process or SubProcess elements.A Data Object element can optionally reference a DataState element, which is the state of data contained in a Data Object.

A Data Object element, which references an element marked as a collection, is visualized differently.

**Notation**

- Data Object [ATTACHMENT filename='data_object.png']
- Data Object that is collection [ATTACHMENT filename='data_object_is_collection.png']

**Related elements**

- Class
- Resource
- Data Association

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using Data Items

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Data Object is an element that stores or conveys items during process execution. The Data Object elements must be contained within the process or SubProcess elements.A Data Object element can optionally reference a DataState element, which is the state of data contained in a Data Object.</p><p>A Data Object element, which references an element marked as a collection, is visualized differently.</p><p><strong>Notation</strong></p><ul><li>Data Object<br /><ac:image><ri:attachment ri:filename="data_object.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Object" /></ri:attachment></ac:image></li><li>Data Object that is collection<br /><ac:image><ri:attachment ri:filename="data_object_is_collection.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Object" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Data+Association">Data Association</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031882 space=CBMP2024x version=1 -->
## PAGE 00083: Data Store

- page_id: `290031882`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031882/Data+Store
- version_number: 1
- version_date: `2026-02-09T14:29:27.313+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Items and Data
- labels: []

### NORMALIZED CONTENT

**Description**

A Data Store provides a mechanism for activities to retrieve or update stored information that will persist beyond the scope of a process.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Class
- Resource
- Data Association

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using Data Items

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Data Store provides a mechanism for activities to retrieve or update stored information that will persist beyond the scope of a process.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="data_store.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Data Store" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Data+Association">Data Association</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031691 space=CBMP2024x version=1 -->
## PAGE 00084: Definitions

- page_id: `290031691`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031691/Definitions
- version_number: 1
- version_date: `2026-02-09T13:48:15.127+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Common BPMN Elements
- labels: []

### NORMALIZED CONTENT

**Description**

The Definitions element is a root model in a business modeling project. This element is the outermost containing object for all BPMN elements. It defines the visibility scope and the namespace for all of the BPMN elements in a model.

**Example**

**[IMAGE alt='' src='']**

###### Definitions element in Containment tree

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Description</strong></p><p>The Definitions element is a root model in a business modeling project. This element is the outermost containing object for all BPMN elements. It defines the visibility scope and the namespace for all of the BPMN elements in a model.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="definition.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Definitions" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">Definitions element in Containment tree</h6><p><strong> </strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290032037 space=CBMP2024x version=1 -->
## PAGE 00085: Dependency

- page_id: `290032037`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032037/Dependency
- version_number: 1
- version_date: `2026-02-09T15:40:45.482+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Process Definition Diagram > BPMNRelationships
- labels: []

### NORMALIZED CONTENT

**Description**

A Dependency indicates a semantic relationship between two model elements (or two sets of model elements). Dependency indicates a situation in which a change to a supplier (target) element may require a change to a client (source) element in the dependency.

A Dependency is shown as a dashed arrow between model elements. The model element at the start point of the arrow (the client element) depends on the model element at the arrowhead (the supplier element). The arrow can be labeled with an optional individual name.

**Example**

[IMAGE alt='' src='']

**Related element**

- BPMN Process

**Related diagram**

- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Dependency indicates a semantic relationship between two model elements (or two sets of model elements). Dependency indicates a situation in which a change to a supplier (target) element may require a change to a client (source) element in the dependency.</p><p>A Dependency is shown as a dashed arrow between model elements. The model element at the start point of the arrow (the client element) depends on the model element at the arrowhead (the supplier element). The arrow can be labeled with an optional individual name.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="dependency.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Dependency" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031949 space=CBMP2024x version=1 -->
## PAGE 00086: Element Types Numbering Sequence

- page_id: `290031949`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031949/Element+Types+Numbering+Sequence
- version_number: 1
- version_date: `2026-02-09T14:51:47.466+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Numbering Elements
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler plugin uses a predefined sequence of numbers for specific element types as described in table.

| Element Type | Description |
| --- | --- |
| BPMN Process | A BPMN Process is numbered in the scope of a project. A BPMN Process number has “P” as a prefix. |
| BPMN Collaboration | A BPMN Collaboration is numbered in the scope of a project. A BPMN Collaboration number has “C” as a prefix. |
| Choreography | A Choreography is numbered in the scope of a project. A Choreography number has “CH” as a prefix. |
| Flow Node | A Flow Node element is numbered in the scope of an owner element (BPMN Process, BPMN Collaboration, or Choreography). The elements that belong to the Flow Node element type category are as follows:All types of tasksAll types of SubprocessesCall activitiesChoreography tasksSub-choreographiesCall choreographiesAll types of gatewaysAll types of events |
|  | An Item Aware Element is numbered in the scope of an owner element. An Item Aware Element number has “D” as a prefix. The elements that belong to the Item Aware element type category are as follows:Data ObjectData StoreData InputData OutputProperty |
|  | A Conversation Node element is numbered in the scope of an owner element. A Conversation Node number has “Conv” as a prefix. The elements that belong to the Conversation Node element type category are as follows:ConversationSub-conversationCall Conversation |
| Resource Role | A Resource Role element is numbered in the scope of an owner element. A Resource Role number has “RR” as a prefix. The elements that belong to the Resource Role element type category are as follows:Human PerformerPerformerPotential OwnerResource Role |

###### Numbered BPMN Process, BPMN Collaboration, and Choreography in Containment tree.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler plugin uses a predefined sequence of numbers for specific element types as described in table.</p><table class="relative-table wrapped" style="width: 1914.53px;"><colgroup><col style="width: 313.219px;" /><col style="width: 1600.31px;" /></colgroup><tbody><tr><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Element Type </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);"><p style="color:var(--ds-text,#172b4d);">Description</p></th></tr><tr><td style="">BPMN Process </td><td style=""><p>A BPMN Process is numbered in the scope of a project. A BPMN Process number has “P” as a prefix.</p></td></tr><tr><td style="">BPMN Collaboration </td><td style=""><p>A BPMN Collaboration is numbered in the scope of a project. A BPMN Collaboration number has “C” as a prefix.</p></td></tr><tr><td style="">Choreography </td><td style=""><p>A Choreography is numbered in the scope of a project. A Choreography number has “CH” as a prefix.</p></td></tr><tr><td style="" colspan="1">Flow Node </td><td style="" colspan="1"><p>A Flow Node element is numbered in the scope of an owner element (BPMN Process, BPMN Collaboration, or Choreography). The elements that belong to the Flow Node element type category are as follows:</p><ul><li>All types of tasks</li><li>All types of Subprocesses</li><li>Call activities</li><li>Choreography tasks</li><li>Sub-choreographies</li><li>Call choreographies</li><li>All types of gateways</li><li>All types of events</li></ul></td></tr><tr><td style="" colspan="1"><br /></td><td style="" colspan="1"><p>An Item Aware Element is numbered in the scope of an owner element. An Item Aware Element number has “D” as a prefix. The elements that belong to the Item Aware element type category are as follows:</p><ul><li>Data Object</li><li>Data Store</li><li>Data Input</li><li>Data Output</li><li>Property</li></ul></td></tr><tr><td style="" colspan="1"><br /></td><td style="" colspan="1"><p>A Conversation Node element is numbered in the scope of an owner element. A Conversation Node number has “Conv” as a prefix. The elements that belong to the Conversation Node element type category are as follows:</p><ul class="_mce_tagged_br"><li>Conversation</li><li>Sub-conversation</li><li>Call Conversation</li></ul></td></tr><tr><td style="" colspan="1">Resource Role </td><td style="" colspan="1"><p>A Resource Role element is numbered in the scope of an owner element. A Resource Role number has “RR” as a prefix. The elements that belong to the Resource Role element type category are as follows:</p><ul><li>Human Performer</li><li>Performer</li><li>Potential Owner</li><li>Resource Role</li></ul></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Numbered BPMN Process, BPMN Collaboration, and Choreography in Containment tree.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031962 space=CBMP2024x version=1 -->
## PAGE 00087: End Concept Relationships

- page_id: `290031962`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031962/End+Concept+Relationships
- version_number: 1
- version_date: `2026-02-09T14:55:21.227+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Ends Concepts
- labels: []

### NORMALIZED CONTENT

The relationships that are allowed between elements are as follows.

| Relationships | Description | Example |
| --- | --- | --- |
| Amplifies | This link connects to a . Meaning that the Goal gives an emphasis on what must be done over a prolonged period to achieve the desired Vision. |  |
| Quantifies | This link connects to a . Meaning that the Objective provides a specific time frame (for example, in June 2013) to work towards the Goal and it also gives a basis for evaluating whether the Goal is being accomplished. |  |

**Related element**

- Ends Concepts

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The relationships that are allowed between elements are as follows.</p><table class="relative-table wrapped" style="width: 83.0709%;"><colgroup><col style="width: 11.3852%;" /><col style="width: 53.9848%;" /><col style="width: 34.63%;" /></colgroup><tbody><tr><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Relationships </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Description </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);"><p style="color:var(--ds-text,#172b4d);">Example</p></th></tr><tr><td style=""><strong>Amplifies </strong></td><td style=""><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024xR1R1" ri:content-title="Goal" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024xR1R1" ri:content-title="Vision" /></ac:link>. Meaning that the Goal gives an emphasis on what must be done over a prolonged period to achieve the desired Vision.</p></td><td style=""><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="amplifies.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="End Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td style=""><strong>Quantifies </strong></td><td style=""><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024xR1R1" ri:content-title="Objective" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024xR1R1" ri:content-title="Goal" /></ac:link>. Meaning that the Objective provides a specific time frame (for example, in June 2013) to work towards the Goal and it also gives a basis for evaluating whether the Goal is being accomplished.</p></td><td style=""><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="quantifies.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="End Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr></tbody></table><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Ends+Concepts" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Ends Concepts</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031842 space=CBMP2024x version=1 -->
## PAGE 00088: End Events

- page_id: `290031842`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031842/End+Events
- version_number: 1
- version_date: `2026-02-09T14:20:21.935+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

An End Event indicates where the path of a process ends. In terms of sequence flows, an End Event ends the flow of a process, and thus, does not have any outgoing sequence flow.

Types of End Events used in business process modeling are the following:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An End Event indicates where the path of a process ends. In terms of sequence flows, an End Event ends the flow of a process, and thus, does not have any outgoing sequence flow.</p><p>Types of End Events used in business process modeling are the following:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c6e56d7f-dde1-4d62-ab4f-9e2a4885bd9c" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031955 space=CBMP2024x version=1 -->
## PAGE 00089: Ends Concepts

- page_id: `290031955`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031955/Ends+Concepts
- version_number: 1
- version_date: `2026-02-09T14:53:38.801+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram
- labels: []

### NORMALIZED CONTENT

The Ends elements show what an organization wants to achieve.

There are three types of End elements:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Ends elements show what an organization wants to achieve.</p><p>There are three types of End elements:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a4e52aa2-cd98-4d7a-8fc9-51d5d7ac64e8" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031703 space=CBMP2024x version=1 -->
## PAGE 00090: Error

- page_id: `290031703`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031703/Error
- version_number: 1
- version_date: `2026-02-09T13:49:00.184+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Common BPMN Elements
- labels: []

### NORMALIZED CONTENT

**Description**

An Error represents the content of an error event or the fault of a failed operation. An Error is generated when there is a critical problem in the processing of an Activity or when the execution of an operation fails.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Error represents the content of an error event or the fault of a failed operation. An Error is generated when there is a critical problem in the processing of an Activity or when the execution of an operation fails.</p>
````

<!--NOMAGIC_PAGE id=290031824 space=CBMP2024x version=1 -->
## PAGE 00091: Error Boundary Event

- page_id: `290031824`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031824/Error+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:17:31.036+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

An Error Boundary Event reacts to (catches) a named error or any error if no name is specified.

This Event always interrupts the Activity to which it is attached. The boundary of the event is always solid.

An Error Boundary Event displays either of the following on a diagram:

- An Error Boundary Event name if the name is specified.
- An Error Ref property value if the name is unspecified.

**Notation** 
[IMAGE alt='' src='']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Error Boundary Event reacts to (catches) a named error or any error if no name is specified.</p><p>This Event always interrupts the Activity to which it is attached. The boundary of the event is always solid.</p><p>An Error Boundary Event displays either of the following on a diagram:</p><ul><li>An Error Boundary Event name if the name is specified.</li><li>An Error Ref property value if the name is unspecified.</li></ul><p><strong>Notation</strong><br /><ac:image><ri:attachment ri:filename="boundary_event_error.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Error Boundary Event" /></ri:attachment></ac:image></p><p><br /></p><p><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link" data-uuid="b4e14ea5-72b1-4b20-a99c-a7321664e15b"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li data-uuid="67a1a5de-54b2-40af-916a-1bf2d68f2622"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link" data-uuid="103548ab-90ae-4ca6-bd7d-9b648ae6fced"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li data-uuid="5c00c2aa-f237-4823-9a06-1754aafc3240"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li data-uuid="eff53c36-97b6-4c51-8d37-05676e0c502b"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031847 space=CBMP2024x version=1 -->
## PAGE 00092: Error End Event

- page_id: `290031847`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031847/Error+End+Event
- version_number: 1
- version_date: `2026-02-09T14:21:52.287+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

An Error End Event indicates that a defined error will be generated, resulting in the termination of all of the currently active threads in a particular SubProcess.

This event displays either of the following on a diagram:

- An Error End Event name if the name is specified.
- An Error Ref property value if the name is unspecified.

**Notation** 
[IMAGE alt='' src='']

**Related elements**

- End Events
- Error

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Error End Event indicates that a defined error will be generated, resulting in the termination of all of the currently active threads in a particular SubProcess.</p><p>This event displays either of the following on a diagram:</p><ul><li>An Error End Event name if the name is specified.</li><li>An Error Ref property value if the name is unspecified.</li></ul><p><strong>Notation</strong><br /><ac:image><ri:attachment ri:filename="end_event_error.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Error End Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Error" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Error</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031771 space=CBMP2024x version=1 -->
## PAGE 00093: Error Start Event

- page_id: `290031771`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031771/Error+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:57:56.716+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

An Error Start Event triggers an in-line Event SubProcess only.

This event displays either of the following on the diagram:

- An Error Start Event name if the name is specified.
- An Error Ref property value if the name is unspecified.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Error Start Event triggers an in-line Event SubProcess only.</p><p>This event displays either of the following on the diagram:</p><ul><li>An Error Start Event name if the name is specified.</li><li>An Error Ref property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="start_event_error.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Error Start Event" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031821 space=CBMP2024x version=1 -->
## PAGE 00094: Escalation Boundary Event

- page_id: `290031821`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031821/Escalation+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:17:03.165+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

An Escalation Boundary Event is used to catch an escalation.

This event displays either of the following on a diagram:

- An Escalation Boundary Event name if the name is specified.
- An Escalation Code property value if the name is unspecified.

**Notation**

- Escalation Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_escalation_true.png']
- Escalation Boundary Event (Cancel Activity - False) [ATTACHMENT filename='boundary_event_escalation_false.png']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Escalation Boundary Event is used to catch an escalation.</p><p>This event displays either of the following on a diagram:</p><ul><li>An Escalation Boundary Event name if the name is specified.</li><li>An Escalation Code property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><ul><li>Escalation Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_escalation_true.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Escalation Boundary Event" /></ri:attachment></ac:image></li><li>Escalation Boundary Event (Cancel Activity - False)<br /><ac:image><ri:attachment ri:filename="boundary_event_escalation_false.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Escalation Boundary Event" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031849 space=CBMP2024x version=1 -->
## PAGE 00095: Escalation End Event

- page_id: `290031849`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031849/Escalation+End+Event
- version_number: 1
- version_date: `2026-02-09T14:22:24.993+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

An Escalation End Event indicates that an Escalation should be triggered. Other active threads are not affected by this event and continue to be executed.

This event displays either of the following on a diagram:

- An Escalation End Event name if the name is specified.
- An Escalation Code property value if the name is unspecified.

**Notation**

[IMAGE alt='' src='']

**Related element**

- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Escalation End Event indicates that an Escalation should be triggered. Other active threads are not affected by this event and continue to be executed.</p><p>This event displays either of the following on a diagram:</p><ul><li>An Escalation End Event name if the name is specified.</li><li>An Escalation Code property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_escalation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Escalation End Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031768 space=CBMP2024x version=1 -->
## PAGE 00096: Escalation Start Event

- page_id: `290031768`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031768/Escalation+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:57:47.836+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

An Escalation Start Event implements measures to expedite the completion of a business Activity.

This event displays either of the following on a diagram:

- An Escalation Start Event name if the name is specified.
- An Escalation Code property value if the name is unspecified.

An Escalation Start Event triggers an in-line Event SubProcess only.

**Notation**

- Interrupting Escalation Start Event [ATTACHMENT filename='start_event_escalation_interr.png']
- Non-interrupting Escalation Start Event [ATTACHMENT filename='start_event_escalation_noninterr.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Escalation Start Event implements measures to expedite the completion of a business Activity.</p><p>This event displays either of the following on a diagram:</p><ul><li>An Escalation Start Event name if the name is specified.</li><li>An Escalation Code property value if the name is unspecified.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0de6db0e-23fb-4416-bbe9-26083e7c44ae"><ac:rich-text-body><p>An Escalation Start Event triggers an in-line Event SubProcess only.</p></ac:rich-text-body></ac:structured-macro><p><strong>Notation</strong></p><ul><li>Interrupting Escalation Start Event<br /><ac:image><ri:attachment ri:filename="start_event_escalation_interr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Escalation Start Event" /></ri:attachment></ac:image></li><li>Non-interrupting Escalation Start Event<br /><ac:image><ri:attachment ri:filename="start_event_escalation_noninterr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Escalation Start Event" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031809 space=CBMP2024x version=1 -->
## PAGE 00097: Escalation Throwing Intermediate Event

- page_id: `290031809`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031809/Escalation+Throwing+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:15:08.142+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Throwing Event
- labels: []

### NORMALIZED CONTENT

**Description**

An Escalation Throwing Intermediate Event raises an Escalation.

This event displays one of the following on the diagram:

- An Escalation Throwing Intermediate Event name if the name is specified.
- An Escalation Code property value if then name is unspecified.

**Notation** 
[IMAGE alt='' src='']

**Related element**

- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Escalation Throwing Intermediate Event raises an Escalation.</p><p>This event displays one of the following on the diagram:</p><ul><li>An Escalation Throwing Intermediate Event name if the name is specified.</li><li>An Escalation Code property value if then name is unspecified.</li></ul><p><strong>Notation</strong><br /><ac:image><ri:attachment ri:filename="intermediate_throwing_event_escalation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Escalation Throwing Intermediate Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031872 space=CBMP2024x version=1 -->
## PAGE 00098: Event Based Gateway

- page_id: `290031872`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031872/Event+Based+Gateway
- version_number: 1
- version_date: `2026-02-09T14:36:33.387+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Gateways
- labels: []

### NORMALIZED CONTENT

**Description**

An Event Based Gateway represents a branching point in a process where alternative paths that follow the gateway are based on the events that occur rather than on the evaluation of expressions using process data (as with an Exclusive or Inclusive Gateway). A specific event, usually the receipt of a message, determines which path will be taken. Basically, an Event Based Gateway is used when a decision made by another participant is based on data that are not visible to the process.

**Notation**

[IMAGE alt='' src='']

**Example**

[IMAGE alt='' src='']

###### Event-Based Gateway.

**Related elements**

- Gateways
- Sequence Flow
- Intermediate Catch Event
- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using a Sequence Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Event Based Gateway represents a branching point in a process where alternative paths that follow the gateway are based on the events that occur rather than on the evaluation of expressions using process data (as with an Exclusive or Inclusive Gateway). A specific event, usually the receipt of a message, determines which path will be taken. Basically, an Event Based Gateway is used when a decision made by another participant is based on data that are not visible to the process.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="gateway_event_based.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Event Based Gateway" /></ri:attachment></ac:image></p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Event_based_gateway.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Event Based Gateway" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Event-Based Gateway.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Gateways">Gateways</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Sequence+Flow">Sequence Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031741 space=CBMP2024x version=1 -->
## PAGE 00099: Event SubProcess

- page_id: `290031741`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031741/Event+SubProcess
- version_number: 1
- version_date: `2026-02-09T13:53:11.743+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > SubProcesses
- labels: []

### NORMALIZED CONTENT

**Description**

An Event SubProcess is an ordinary SubProcess whose Triggered By Event property is set to true. It is not a part of a normal flow of its parent process - there is no incoming or outgoing sequence flow.

An Event SubProcess may occur many times. Unlike the standard SubProcess that uses the flow of the parent process as a trigger, it has a Start Event as a trigger. Whenever the Start Event is triggered while the parent process is active, the Event SubProcess will start.

The Start Event icon of a collapsed Event SubProcess will be displayed on the top left corner of the SubProcess.

**Notation**

- Expanded [ATTACHMENT filename='event_subprocess.png']
- Collapsed [ATTACHMENT filename='event_subprocess_suppressed.png']
- Collapsed (with its own Start Event) [ATTACHMENT filename='event_subprocess_send.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Event SubProcess is an ordinary SubProcess whose Triggered By Event property is set to true. It is not a part of a normal flow of its parent process - there is no incoming or outgoing sequence flow.</p><p>An Event SubProcess may occur many times. Unlike the standard SubProcess that uses the flow of the parent process as a trigger, it has a Start Event as a trigger. Whenever the Start Event is triggered while the parent process is active, the Event SubProcess will start.</p><p>The Start Event icon of a collapsed Event SubProcess will be displayed on the top left corner of the SubProcess.</p><p><strong>Notation</strong></p><ul><li>Expanded<br /><ac:image><ri:attachment ri:filename="event_subprocess.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Event SubProcess" /></ri:attachment></ac:image></li><li>Collapsed<br /><ac:image><ri:attachment ri:filename="event_subprocess_suppressed.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Event SubProcess" /></ri:attachment></ac:image></li><li>Collapsed (with its own Start Event)<br /><ac:image><ri:attachment ri:filename="event_subprocess_send.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Event SubProcess" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031862 space=CBMP2024x version=1 -->
## PAGE 00100: Exclusive Gateway

- page_id: `290031862`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031862/Exclusive+Gateway
- version_number: 1
- version_date: `2026-02-09T14:35:49.041+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Gateways
- labels: []

### NORMALIZED CONTENT

**Description**

A diverging Exclusive Gateway (Decision) is used to create alternative paths within a process flow. This is basically the diversion point in the road for a process. Only one alternative path can be taken for a given instance of the process.

A Exclusive Gateway can be thought of as a question that is asked at a particular point in the process. The question has a defined set of alternative answers. Each question is associated with two or more condition expressions associated with outgoing sequence flows of the Gateway.

A converging Exclusive Gateway is used to merge alternative paths. All incoming sequence Flows tokens will be routed to the outgoing sequence flow without synchronizing them.

There are two icons defined for an Exclusive Gateway in the BPMN2 Specification.It can be displayed with or without an internal marker.

**Notation**

- Without an Internal Marker Exclusive Gateway [ATTACHMENT filename='gateway_exclusive.png']
- An Internal Marker Exclusive Gateway [ATTACHMENT filename='gateway_exclusive_with_marker.png']

**Example**

[IMAGE alt='' src='']

###### Diverging Exclusive Gateway.

**Related elements**

- Gateways
- Sequence Flow

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using a Sequence Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A diverging Exclusive Gateway (Decision) is used to create alternative paths within a process flow. This is basically the diversion point in the road for a process. Only one alternative path can be taken for a given instance of the process.</p><p>A Exclusive Gateway can be thought of as a question that is asked at a particular point in the process. The question has a defined set of alternative answers. Each question is associated with two or more condition expressions associated with outgoing sequence flows of the Gateway.</p><p>A converging Exclusive Gateway is used to merge alternative paths. All incoming sequence Flows tokens will be routed to the outgoing sequence flow without synchronizing them.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c2b57597-5170-424b-8708-cf0c589efa75"><ac:rich-text-body>There are two icons defined for an Exclusive Gateway in the BPMN2 Specification.It can be displayed with or without an internal marker.</ac:rich-text-body></ac:structured-macro><p><strong>Notation</strong><br /><br /></p><ul><li>Without an Internal Marker Exclusive Gateway<br /><ac:image><ri:attachment ri:filename="gateway_exclusive.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Exclusive Gateway" /></ri:attachment></ac:image></li><li>An Internal Marker Exclusive Gateway<br /><ac:image><ri:attachment ri:filename="gateway_exclusive_with_marker.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Exclusive Gateway" /></ri:attachment></ac:image></li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="diverging_exclusive_gateway.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Exclusive Gateway" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Diverging Exclusive Gateway.</h6><p><br /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Gateways">Gateways</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Sequence+Flow">Sequence Flow</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032095 space=CBMP2024x version=1 -->
## PAGE 00101: Exporting Models to BPMN2

- page_id: `290032095`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032095/Exporting+Models+to+BPMN2
- version_number: 1
- version_date: `2026-02-09T16:04:03.237+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler plugin for MagicDraw supports BPMN model export to BPMN2.

The support allows you to export your BPMN Processes, Collaborations or Choreographies to BPMN2 file.

To export BPMN Processes, Collaborations or Choreographies to BPMN2

1. On the main menu, click File > Export To > BPMN2 File . The Export to BPMN2 File dialog opens.
2. Select the **Selected BPMN Processes/Collaborations/Choreographies** option button and choose the diagrams you want to export from the BPMN Processes/Collaborations list. Press and hold down the Ctrl key to select multiple BPMN Processes or Collaborations.
3. Click the ... button next to the Working Directory box to specify the place for saving the exported file.
4. Click Save .

To export an active BPMN Process, Collaboration or Choreographies to BPMN2

1. Do one of the following:
  - On the main menu, click File > Export To > BPMN2 File .
  - Right-click the BPMN Process or Collaboration diagram in the Containment tree and from the shortcut menu, select Tools > Export To BPMN2 File . The Export to BPMN2 dialog opens.
2. Select the Active BPMN Process/Collaboration/Choreographies option button.
3. Click the ... button next to the BPMN2 File box to specify the place for saving the exporting project.
4. Click Save .

BPMN Message export to BPMN2 format is not supported.

**Related element**

- BPMN2 XML support

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler plugin for MagicDraw supports BPMN model export to BPMN2.</p><p>The support allows you to export your BPMN Processes, Collaborations or Choreographies to BPMN2 file.</p><p><br /></p><p>To export BPMN Processes, Collaborations or Choreographies to BPMN2</p><hr style="" /><ol><li>On the main menu, click <strong>File</strong>&gt; <strong>Export To</strong> &gt; <strong>BPMN2 File</strong>. The <strong>Export to BPMN2 File</strong> dialog opens.</li><li><p class="auto-cursor-target">Select the <strong>Selected BPMN Processes/Collaborations/Choreographies</strong> option button and choose the diagrams you want to export from the BPMN Processes/Collaborations list.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="40c587b4-dc03-4c33-ad38-7552e7de6b80"><ac:rich-text-body>Press and hold down the Ctrl key to select multiple BPMN Processes or Collaborations.</ac:rich-text-body></ac:structured-macro></li><li>Click the <strong>...</strong> button next to the <strong>Working Directory</strong> box to specify the place for saving the exported file.</li><li>Click <strong>Save</strong>.</li></ol><p><br /></p><p>To export an active BPMN Process, Collaboration or Choreographies to BPMN2</p><hr style="" /><ol><li>Do one of the following:<ul><li>On the main menu, click <strong>File</strong> &gt;<strong> Export To</strong> &gt; <strong>BPMN2 File</strong>.</li><li>Right-click the BPMN Process or Collaboration diagram in the Containment tree and from the shortcut menu, select <strong>Tools</strong> &gt; <strong>Export To BPMN2 File</strong>. The <strong>Export to BPMN2</strong> dialog opens.</li></ul></li><li>Select the <strong>Active BPMN Process/Collaboration/Choreographies</strong> option button.</li><li>Click the <strong>...</strong> button next to the <strong>BPMN2 File</strong> box to specify the place for saving the exporting project.</li><li>Click <strong>Save</strong>.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5fc048b4-6bf4-488d-91ec-664d84ceb365"><ac:rich-text-body><p>BPMN Message export to BPMN2 format is not supported.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN2+XML+support" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN2 XML support</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032094 space=CBMP2024x version=1 -->
## PAGE 00102: Exporting Models to XPDL

- page_id: `290032094`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032094/Exporting+Models+to+XPDL
- version_number: 1
- version_date: `2026-02-09T16:03:35.136+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler plugin for MagicDraw supports BPMN 2.0 model export to XPDL 2.2.

The support for XPDL 2.2 allows you to export your BPMN Processes and Collaborations to XPDL 2.2 format. A separate XPDL file is then created for each exported BPMN Process or Collaboration diagram.

XPDL 2.2 does not support BPMN Choreography and Conversation elements from BPMN Collaborations.

To export multiple BPMN Processes or Collaborations to XPDL

1. On the main menu, click **File**> **Export To** > **XPDL File**. The **Export to XPDL** dialog opens.
2. Select the **Selected BPMN Processes/Collaborations** option button and choose the diagrams you want to export from the BPMN Processes/Collaborations list. Press and hold down the Ctrl key to select multiple BPMN Processes or Collaborations.
3. Click the ... button next to the Working Directory box to specify the place for saving the exporting project.
4. Click Save .

To export an active BPMN Process or Collaboration to XPDL

1. Do one of the following:
  - On the main menu, click File > Export To > XPDL File .
  - Right-click the BPMN Process or Collaboration diagram in the Containment tree and from the shortcut menu, select **Tools** > **Export To XPDL File**. The**Export to XPDL** dialog opens.
2. Select the Active BPMN Process/Collaboration option button.
3. Do one of the following:
  - Type the name for a destination directory in the Xpdl File box.
  - Click the ... button next to the Working Directory box to specify the place for saving the exporting project.
4. Click Save .

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler plugin for MagicDraw supports BPMN 2.0 model export to XPDL 2.2.</p><p>The support for XPDL 2.2 allows you to export your BPMN Processes and Collaborations to XPDL 2.2 format. A separate XPDL file is then created for each exported BPMN Process or Collaboration diagram.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="542e3525-5b5d-4b35-92c9-de700dbd2c49"><ac:rich-text-body>XPDL 2.2 does not support BPMN Choreography and Conversation elements from BPMN Collaborations.</ac:rich-text-body></ac:structured-macro><p><br /><br />To export multiple BPMN Processes or Collaborations to XPDL</p><hr style="" /><ol><li><p>On the main menu, click <strong>File</strong>&gt; <strong>Export To</strong> &gt; <strong>XPDL File</strong>. The <strong>Export to XPDL</strong> dialog opens.</p></li><li><p class="auto-cursor-target">Select the <strong>Selected BPMN Processes/Collaborations</strong> option button and choose the diagrams you want to export from the BPMN Processes/Collaborations list.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6c7c0d85-d577-45d2-a7fb-854da24361f9"><ac:rich-text-body>Press and hold down the Ctrl key to select multiple BPMN Processes or Collaborations.</ac:rich-text-body></ac:structured-macro></li><li>Click the<strong> ...</strong> button next to the <strong>Working Directory</strong> box to specify the place for saving the exporting project.</li><li>Click <strong>Save</strong>.</li></ol><p><br /></p><p>To export an active BPMN Process or Collaboration to XPDL</p><hr style="" /><ol><li>Do one of the following:<ul><li>On the main menu, click <strong>File</strong> &gt; <strong>Export To</strong> &gt; <strong>XPDL File</strong>.</li><li><p>Right-click the BPMN Process or Collaboration diagram in the Containment tree and from the shortcut menu, select <strong>Tools</strong> &gt; <strong>Export To XPDL File</strong>. The<strong> Export to XPDL</strong> dialog opens.</p></li></ul></li><li>Select the <strong>Active BPMN Process/Collaboration</strong> option button.</li><li>Do one of the following:<ul><li>Type the name for a destination directory in the <strong>Xpdl File</strong> box.</li><li>Click the<strong> ...</strong> button next to the <strong>Working Directory</strong> box to specify the place for saving the exporting project.</li></ul></li><li>Click <strong>Save</strong>.</li></ol><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031989 space=CBMP2024x version=1 -->
## PAGE 00103: External Influencer

- page_id: `290031989`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031989/External+Influencer
- version_number: 1
- version_date: `2026-02-09T15:00:33.191+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Influencer Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

External Influencer is this outside an enterprise's organizational boundary that can impact its employment of Means or achievement of Ends. External Influencer is usually categorized as follows:

- Competitor: A rival enterprise in a struggle for advantage over the subject enterprise.
- Customer: A role played by an individual or enterprise that has investigated, ordered, received, or paid for products or services from the subject enterprise.
- Environment: The aggregate of surrounding conditions or Influencers affecting the existence or development of an enterprise.
- Partner: An enterprise that shares risks and profit with the subject enterprise (or is associated with the subject enterprise to share risks and profit) because this is mutually beneficial.
- Regulation: An order prescribed by an authority such as a government body or the management of an enterprise.
- Supplier: A role played by an individual or enterprise that can furnish or provide products or services to the subject enterprise.
- Technology: The role of technology, including its developments and limitations — there may be prerequisites for use of technology; there may be enterprise Activity that technology enables or restricts.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Influencer Concepts
- Influence Concepts Relationship

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>External Influencer is this outside an enterprise's organizational boundary that can impact its employment of Means or achievement of Ends. External Influencer is usually categorized as follows:</p><ul><li>Competitor: A rival enterprise in a struggle for advantage over the subject enterprise.</li><li>Customer: A role played by an individual or enterprise that has investigated, ordered, received, or paid for products or services from the subject enterprise.</li><li>Environment: The aggregate of surrounding conditions or Influencers affecting the existence or development of an enterprise.</li><li>Partner: An enterprise that shares risks and profit with the subject enterprise (or is associated with the subject enterprise to share risks and profit) because this is mutually beneficial.</li><li>Regulation: An order prescribed by an authority such as a government body or the management of an enterprise.</li><li>Supplier: A role played by an individual or enterprise that can furnish or provide products or services to the subject enterprise.</li><li>Technology: The role of technology, including its developments and limitations — there may be prerequisites for use of technology; there may be enterprise Activity that technology enables or restricts.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="external_influencer.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="External Influencer" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Influencer+Concepts" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Influencer Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Influence+Concepts+Relationship">Influence Concepts Relationship</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031861 space=CBMP2024x version=1 -->
## PAGE 00104: Gateways

- page_id: `290031861`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031861/Gateways
- version_number: 1
- version_date: `2026-02-09T14:24:32.557+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

A Gateway allows you to control the flow of a process through a sequence flow. The term Gateway implies that there is a gating mechanism that either allows or disallows passage through the Gateway. Tokens that arrive at the gateway can be merged as inputs and/or split as outputs.

If the flow of a process does not need to be controlled, process does not need a gateway.

Types of Gateways are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Gateway allows you to control the flow of a process through a sequence flow. The term Gateway implies that there is a gating mechanism that either allows or disallows passage through the Gateway. Tokens that arrive at the gateway can be merged as inputs and/or split as outputs.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="35c3d694-56d8-480d-b108-857840b84e81"><ac:rich-text-body><p>If the flow of a process does not need to be controlled, process does not need a gateway.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target">Types of Gateways are as follows: </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="ec3547c1-14ec-4061-bf1f-4aeac661b320" /></p>
````

<!--NOMAGIC_PAGE id=290032017 space=CBMP2024x version=1 -->
## PAGE 00105: Generalization

- page_id: `290032017`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032017/Generalization
- version_number: 1
- version_date: `2026-02-09T15:31:25.671+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Data Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Generalization link shows that one class provides grouping criteria for sets of other classes. Generic class may define sets of properties, that are applicable to all the specific classes. The Generalization link can be among classes.

**Example**

[IMAGE alt='' src='']

**Related element**

- Class

**Related diagram**

- Business Data Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Generalization link shows that one class provides grouping criteria for sets of other classes. Generic class may define sets of properties, that are applicable to all the specific classes. The Generalization link can be among classes.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="generalization.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Generalization" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Class" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Class</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Data+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Business Data Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031680 space=CBMP2024x version=1 -->
## PAGE 00106: Getting Started

- page_id: `290031680`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031680/Getting+Started
- version_number: 1
- version_date: `2026-02-09T13:47:15.047+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler Plugin is a tool that provides a solution for modeling and analyzing business processes. This tool allows you to represent and analyze business process models based on the Business Process Modeling and Notation (BPMN) standard, define organization structure and business data as well as business motivation based on the Business Motivation Model (BMM) standard.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler Plugin is a tool that provides a solution for modeling and analyzing business processes. This tool allows you to represent and analyze business process models based on the Business Process Modeling and Notation (BPMN) standard, define organization structure and business data as well as business motivation based on the Business Motivation Model (BMM) standard.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f12c5a4c-2c6e-4de9-a8c1-4920761bf81e" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031958 space=CBMP2024x version=1 -->
## PAGE 00107: Goal

- page_id: `290031958`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031958/Goal
- version_number: 1
- version_date: `2026-02-09T14:54:22.204+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Ends Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

Unlike vision, a goal should generally be attainable and should be more specifically oriented to a single aspect of the business problem. A Goal is a statement about a state or condition of the enterprise to be brought about or sustained through appropriate Means. A Goal amplifies a Vision.It indicates what must be satisfied on a continuing basis to effectively attain the Vision.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Ends Concepts
- End Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Unlike vision, a goal should generally be attainable and should be more specifically oriented to a single aspect of the business problem. A Goal is a statement about a state or condition of the enterprise to be brought about or sustained through appropriate Means. A Goal amplifies a Vision.It indicates what must be satisfied on a continuing basis to effectively attain the Vision.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="goal.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Goal" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Ends+Concepts" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Ends Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Concept+Relationships" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032041 space=CBMP2024x version=1 -->
## PAGE 00108: Governs

- page_id: `290032041`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032041/Governs
- version_number: 1
- version_date: `2026-02-09T15:41:32.710+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Process Definition Diagram > BPMNRelationships
- labels: []

### NORMALIZED CONTENT

**Description**

Governs shows that a Business Policy governs BPMN Process.

**Example**

[IMAGE alt='' src='']

**Related element**

- BPMN Process

**Related diagram**

- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Governs shows that a Business Policy governs BPMN Process.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="governs_process.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Governs" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031701 space=CBMP2024x version=1 -->
## PAGE 00109: Group

- page_id: `290031701`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031701/Group
- version_number: 1
- version_date: `2026-02-09T13:48:52.932+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Common BPMN Elements > Artifacts
- labels: []

### NORMALIZED CONTENT

**Description**

A Group element represents an informal visual grouping of the diagram graphical elements.

A group shows all elements that belong to the same category. This type of grouping does not affect a sequence flow within the Group. A category name appears on the diagram as a Group label.

**Example**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Group element represents an informal visual grouping of the diagram graphical elements.</p><p>A group shows all elements that belong to the same category. This type of grouping does not affect a sequence flow within the Group. A category name appears on the diagram as a Group label.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="group.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Group" /></ri:attachment></ac:image></p>
````

<!--NOMAGIC_PAGE id=290032043 space=CBMP2024x version=1 -->
## PAGE 00110: Guides

- page_id: `290032043`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032043/Guides
- version_number: 1
- version_date: `2026-02-09T15:42:41.117+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Process Definition Diagram > BPMNRelationships
- labels: []

### NORMALIZED CONTENT

**Description**

Guides shows that a Business Rule guides a BPMN Process.

**Example**

[IMAGE alt='' src='']

**Related elements**

- BPMN Process
- Strategy
- Tactic
- Business Policy
- Business Rule

**Related diagram**

- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Guides shows that a Business Rule guides a BPMN Process.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="guides.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Guides" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Strategy">Strategy</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Tactic" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Tactic</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Policy" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Business Policy</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Rule">Business Rule</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031866 space=CBMP2024x version=1 -->
## PAGE 00111: Inclusive Gateway

- page_id: `290031866`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031866/Inclusive+Gateway
- version_number: 1
- version_date: `2026-02-09T14:36:04.962+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Gateways
- labels: []

### NORMALIZED CONTENT

**Description**

A diverging Inclusive Gateway (Inclusive Decision) is used to create not only alternative but also parallel paths within a process flow. Unlike an Exclusive Gateway, it evaluates all condition expressions. The true evaluation of one condition expression does not exclude the evaluation of the other condition expressions. All of the sequence flows with true evaluation will be traversed by a token.

Since each path is considered to be independent, all combinations of the paths may be taken, from zero to all. However, it should be designed in such a way that at least one path is taken.

A converging Inclusive Gateway is used to merge a combination of alternative and parallel paths. A control flow token arriving at an Inclusive Gateway may be synchronized with some other tokens that arrive later at this Gateway.

**Notation**

[IMAGE alt='' src='']

**Example**

[IMAGE alt='' src='']

###### Diverging Inclusive Gateway.

**Related elements**

- Gateways
- Sequence Flow

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using a Sequence Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A diverging Inclusive Gateway (Inclusive Decision) is used to create not only alternative but also parallel paths within a process flow. Unlike an Exclusive Gateway, it evaluates all condition expressions. The true evaluation of one condition expression does not exclude the evaluation of the other condition expressions. All of the sequence flows with true evaluation will be traversed by a token.</p><p>Since each path is considered to be independent, all combinations of the paths may be taken, from zero to all. However, it should be designed in such a way that at least one path is taken.</p><p>A converging Inclusive Gateway is used to merge a combination of alternative and parallel paths. A control flow token arriving at an Inclusive Gateway may be synchronized with some other tokens that arrive later at this Gateway.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="gateway_inclusive.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Inclusive Gateway" /></ri:attachment></ac:image></p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Diverging_inclusive_gateway.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Inclusive Gateway" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Diverging Inclusive Gateway.</h6><p><br /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Gateways">Gateways</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Sequence+Flow">Sequence Flow</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031995 space=CBMP2024x version=1 -->
## PAGE 00112: Influence Concepts Relationship

- page_id: `290031995`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031995/Influence+Concepts+Relationship
- version_number: 1
- version_date: `2026-02-09T15:14:38.450+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Influencer Concepts
- labels: []

### NORMALIZED CONTENT

The following table provides the relationship that exists between element types and the meaning.

| Relationship | Description | Example |
| --- | --- | --- |
| Is Source Of | This link connects to an Influencer ( or ).Meaning that the Influencing Organization is the source of Influencer. An Influencer may have multiple sources, ornone. |  |

**Related elements**

- Influencer Concepts

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following table provides the relationship that exists between element types and the meaning.</p><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Relationship </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Description </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);"><p style="color:var(--ds-text,#172b4d);">Example</p></th></tr><tr><td>Is Source Of </td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Influencing Organization" /></ac:link> to an Influencer (<ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="External Influencer" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Internal Influencer" /></ac:link>).<br />Meaning that the Influencing Organization is the source of Influencer. An Influencer may have multiple sources, or<br />none.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="is_source_of.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Influence Concepts Relationship" /></ri:attachment></ac:image></p></div></td></tr></tbody></table><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Influencer+Concepts">Influencer Concepts</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031988 space=CBMP2024x version=1 -->
## PAGE 00113: Influencer Concepts

- page_id: `290031988`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031988/Influencer+Concepts
- version_number: 1
- version_date: `2026-02-09T15:00:08.672+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram
- labels: []

### NORMALIZED CONTENT

The Influencer elements come up with the factors that are influencing the ends achievement of the organization.

Types of Influencer elements are as following:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Influencer elements come up with the factors that are influencing the ends achievement of the organization.</p><p>Types of Influencer elements are as following:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="59e20b22-406b-403e-ae0d-056129522fb4" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031993 space=CBMP2024x version=1 -->
## PAGE 00114: Influencing Organization

- page_id: `290031993`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031993/Influencing+Organization
- version_number: 1
- version_date: `2026-02-09T15:10:25.322+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Influencer Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

An Influencing Organization is an organization that is external to the enterprise modeled in a given enterprise BMM, and that influences that enterprise.

An Influencing Organization is the source of Influencer. The Influencer may have multiple sources, or none.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Influencer Concepts
- Influence Concepts Relationship

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Influencing Organization is an organization that is external to the enterprise modeled in a given enterprise BMM, and that influences that enterprise.</p><p>An Influencing Organization is the source of Influencer. The Influencer may have multiple sources, or none.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="influencing_organization.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Influencing Organization" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Influencer+Concepts" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Influencer Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Influence+Concepts+Relationship">Influence Concepts Relationship</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032028 space=CBMP2024x version=1 -->
## PAGE 00115: Information system

- page_id: `290032028`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032028/Information+system
- version_number: 1
- version_date: `2026-02-09T15:34:09.580+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Organization Structure Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

An Information System is a type of hardware or a software, e. g., international sales system, ticket reservation system, etc. Information system can be used by Process or Process Activity.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Resource
- Organization Unit
- Role
- Person
- Pool and Lane
- Activities
- Choreography Activities

**Related diagrams**

- Organization Structure Diagram
- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram
- BPMN Resources Usage Matrices

**Related Procedure**

- Using Organization Structure Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Information System is a type of hardware or a software, e. g., international sales system, ticket reservation system, etc. Information system can be used by Process or Process Activity.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="information_system.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Information system" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Structure+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Organization Structure Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Resources+Usage+Matrices">BPMN Resources Usage Matrices</a></li></ul><p><strong>Related Procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Organization+Structure+Diagram">Using Organization Structure Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031678 space=CBMP2024x version=1 -->
## PAGE 00116: Installation, licensing, and system requirements

- page_id: `290031678`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031678/Installation+licensing+and+system+requirements
- version_number: 1
- version_date: `2026-02-09T13:47:00.078+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation
- labels: []

### NORMALIZED CONTENT

For information regarding installation, licensing, and system requirements, visit the [CONFLUENCE_PAGE title='Installation, Licensing, and System Requirements Documentation' space='IL2024xR1'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>For information regarding installation, licensing, and system requirements, visit the <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installation, Licensing, and System Requirements Documentation" /><ac:plain-text-link-body><![CDATA[Installation, licensing, and system requirements]]></ac:plain-text-link-body></ac:link> page.</p>
````

<!--NOMAGIC_PAGE id=290031782 space=CBMP2024x version=1 -->
## PAGE 00117: Intermediate Catch Event

- page_id: `290031782`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031782/Intermediate+Catch+Event
- version_number: 1
- version_date: `2026-02-09T13:58:33.567+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

An Intermediate Catch Event indicates that something is happening between the start and end of a process. Intermediate Events affect the flow of a process, but do not start or directly terminate the process.

You can use Intermediate Catch Event to:

- Show where messages are expected or sent within a process.
- Show delays that are expected within a process.
- Interrupt normal flow through exception handling.

Types of Intermediate Catch Events are the following:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An Intermediate Catch Event indicates that something is happening between the start and end of a process. Intermediate Events affect the flow of a process, but do not start or directly terminate the process.</p><p>You can use Intermediate Catch Event to:</p><ul><li>Show where messages are expected or sent within a process.</li><li>Show delays that are expected within a process.</li><li>Interrupt normal flow through exception handling.</li></ul><p>Types of Intermediate Catch Events are the following:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3979d68d-a16d-4b70-82c8-54bf334f0d8b" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031800 space=CBMP2024x version=1 -->
## PAGE 00118: Intermediate Throwing Event

- page_id: `290031800`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031800/Intermediate+Throwing+Event
- version_number: 1
- version_date: `2026-02-09T14:10:40.276+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

An Intermediate Throwing Event indicates that something is happening between the start and end of a process. Intermediate Events affect the flow of a process, but do not start or directly terminate the process.

You can use Intermediate Throwing Events to show extra work required.

Types of Intermediate Throwing Events are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An Intermediate Throwing Event indicates that something is happening between the start and end of a process. Intermediate Events affect the flow of a process, but do not start or directly terminate the process.</p><p>You can use Intermediate Throwing Events to show extra work required.</p><p>Types of Intermediate Throwing Events are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="97042203-93bf-495a-81b9-0e6dfc83b6b8" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031991 space=CBMP2024x version=1 -->
## PAGE 00119: Internal Influencer

- page_id: `290031991`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031991/Internal+Influencer
- version_number: 1
- version_date: `2026-02-09T15:10:00.307+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Influencer Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

Internal Influencer is an enterprise that can impact its employment of Means or achievement of Ends.

Internal Influencer is usually categorized the following:

- Assumption: Something that is taken for granted or without proof.
- Explicit Corporate Value: An ideal, custom, or institution that an enterprise promotes or agrees with that is explicitly set forth and declared.
- Implicit Corporate Value: A corporate value that is not explicitly declared but nonetheless understood by some or all of the people in an enterprise.
- Habit: A customary practice or use.
- Infrastructure: The basic underlying framework or features of a system.
- Issue: A point in question or a matter that is in dispute as between contending partners.
- Management Prerogative: A right or privilege exercised by virtue of ownership or position in an enterprise.
- Resource: The resources available for carrying out the business of an enterprise, especially their quality.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Influencer Concepts
- Influence Concepts Relationship

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Internal Influencer is an enterprise that can impact its employment of Means or achievement of Ends.</p><p>Internal Influencer is usually categorized the following:</p><ul><li>Assumption: Something that is taken for granted or without proof.</li><li>Explicit Corporate Value: An ideal, custom, or institution that an enterprise promotes or agrees with that is explicitly set forth and declared.</li><li>Implicit Corporate Value: A corporate value that is not explicitly declared but nonetheless understood by some or all of the people in an enterprise.</li><li>Habit: A customary practice or use.</li><li>Infrastructure: The basic underlying framework or features of a system.</li><li>Issue: A point in question or a matter that is in dispute as between contending partners.</li><li>Management Prerogative: A right or privilege exercised by virtue of ownership or position in an enterprise.</li><li>Resource: The resources available for carrying out the business of an enterprise, especially their quality.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="internal_influencer.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Internal Influencer" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Influencer+Concepts" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Influencer Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Influence+Concepts+Relationship">Influence Concepts Relationship</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031681 space=CBMP2024x version=1 -->
## PAGE 00120: Introducing Main Concepts

- page_id: `290031681`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031681/Introducing+Main+Concepts
- version_number: 1
- version_date: `2026-02-09T13:47:21.753+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Getting Started
- labels: []

### NORMALIZED CONTENT

First of all, the chapter explains the essence of the Business Process Model and Notation (BPMN) standard. Second, the Business Motivation Model (BMM) standard is presented. Finally, the types of diagrams supported by Cameo Business Modeler Plugin are listed.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>First of all, the chapter explains the essence of the Business Process Model and Notation (BPMN) standard. Second, the Business Motivation Model (BMM) standard is presented. Finally, the types of diagrams supported by Cameo Business Modeler Plugin are listed. </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="273c2ff0-50db-49f3-ac9c-da3609997506" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031878 space=CBMP2024x version=1 -->
## PAGE 00121: Items and Data

- page_id: `290031878`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031878/Items+and+Data
- version_number: 1
- version_date: `2026-02-09T14:28:39.411+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

The traditional requirement of process modeling is to be able to model the items (physical or information items) that are created, manipulated, and used during the execution of a process. This requirement is fulfilled in BPMN through various constructs: Data Objects, Item Definition, Properties, Data Inputs, Data Outputs, Messages, Input Sets, Output Sets, and Data Associations.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The traditional requirement of process modeling is to be able to model the items (physical or information items) that are created, manipulated, and used during the execution of a process. This requirement is fulfilled in BPMN through various constructs: Data Objects, Item Definition, Properties, Data Inputs, Data Outputs, Messages, Input Sets, Output Sets, and Data Associations.</p>
````

<!--NOMAGIC_PAGE id=290031791 space=CBMP2024x version=1 -->
## PAGE 00122: Link Catching Intermediate Event

- page_id: `290031791`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031791/Link+Catching+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:01:38.640+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Link Catching Intermediate Event provides the capability to connect two sections of a process. You can use this event to either:

- Create looping situations or to avoid long sequence flow lines, as “Off-Page Connectors” to print a Process across multiple pages, or as generic Go To objects within a Process level.
- Catch a link from a Link Throwing Intermediate Event.

You can only use one Link Event for each single Process level, meaning that it cannot link a parent Process with a SubProcess.

A Link Catching Intermediate Event displays either of the following:

- A Link Catching Intermediate Event name if the name is specified.
- A Source property value if the name is unspecified.

**Notation**

[IMAGE alt='' src='']

**Example**

****[IMAGE alt='' src='']

###### Link Catching Intermediate Event

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Link Catching Intermediate Event provides the capability to connect two sections of a process. You can use this event to either:</p><ul><li>Create looping situations or to avoid long sequence flow lines, as “Off-Page Connectors” to print a Process across multiple pages, or as generic Go To objects within a Process level.</li><li>Catch a link from a Link Throwing Intermediate Event.</li></ul><p>You can only use one Link Event for each single Process level, meaning that it cannot link a parent Process with a SubProcess.</p><p>A Link Catching Intermediate Event displays either of the following:</p><ul><li>A Link Catching Intermediate Event name if the name is specified.</li><li>A Source property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event_link.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Link Catching Intermediate Event" /></ri:attachment></ac:image></p><p><strong>Example</strong></p><p><strong><br /></strong><ac:image><ri:attachment ri:filename="intermediate_catch_event_link_example.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Link Catching Intermediate Event" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;color:var(--ds-text,#172b4d);">Link Catching Intermediate Event</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031803 space=CBMP2024x version=1 -->
## PAGE 00123: Link Throwing Intermediate Event

- page_id: `290031803`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031803/Link+Throwing+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:11:45.649+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Throwing Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Link Throwing Intermediate Event is used to throw a link to a Link Catching Intermediate Event.

This event displays either of the following:

- A Link Throwing Intermediate Event name if the name is specified.
- A Target Link Event property value if the name is unspecified.

**Notation** 
[IMAGE alt='' src='']

**Related element**

- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Link Throwing Intermediate Event is used to throw a link to a Link Catching Intermediate Event.</p><p>This event displays either of the following:</p><ul><li>A Link Throwing Intermediate Event name if the name is specified.</li><li>A Target Link Event property value if the name is unspecified.</li></ul><p><strong>Notation</strong><br /><ac:image><ri:attachment ri:filename="intermediate_throwing_event_link.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Link Throwing Intermediate Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031728 space=CBMP2024x version=1 -->
## PAGE 00124: Manual Task

- page_id: `290031728`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031728/Manual+Task
- version_number: 1
- version_date: `2026-02-09T13:52:12.584+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A Manual Task is a task that is expected to be performed without the aid of any business process execution engine or application, for example, installing a telephone at a customer location.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Manual Task is a task that is expected to be performed without the aid of any business process execution engine or application, for example, installing a telephone at a customer location.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="manual_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Manual Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031976 space=CBMP2024x version=1 -->
## PAGE 00125: Mean Concept Relationships

- page_id: `290031976`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031976/Mean+Concept+Relationships
- version_number: 1
- version_date: `2026-02-09T15:22:29.213+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Means Concepts
- labels: []

### NORMALIZED CONTENT

The following table provides the relationships that exist between element types and their meaning.

| Relationship | Description | Example |
| --- | --- | --- |
| Makes Operative | This link connects to a . Meaning that the Mission lists every continuingActivity to ensure the Vision. |  |
| Component Of | This link connects to a . Meaning that the Strategy is the method orcourse of action that will be employed to achieve the Mission. |  |
| Implements | This link connects to a . Meaning that the Tactic realizes Strategies. |  |
| Enables | This link connects to a or to a . Meaning that a Strategy/Tactic makes another Strategy/Tactic doable. That is to say the latter Strategy/Tacticprovides an opportunity for the former Strategy/Tactic to be carried out. Use this linkto associate Strategy to another Strategy or Tactic to another Tactic. |  |
| Effects Enforcement Level | This link connects to a . Meaning that the Tactics influences the |  |
| Formulated Based On | This link connects or to a or . Meaningthat the Strategy or Tactic is planned according to what result the Business Policy orBusiness Rule desires. |  |
| Channel Efforts Towards | This link connects to a , or to an . Meaning that the Strategy iscoordinated as activities aimed towards Goals as Tactic towards Objective. For example, theTactic “Free delivery” channels efforts towards the Objective “5% increase in sales within 3months.” |  |
| Governs | This link connects or to a or . Meaning that the Business Policy or BusinessRule determines the Strategy or Tactic. |  |
| Basis For | This link connects to a . Meaning that the Business Policy is the key to achieve Business Rule. |  |
| Supports Achievement Of | This link connects or to a or . Meaning that the Business Policy provides anidea or reason to develop the Strategy or Tactic. |  |
| Acts As Regulation | This link connects a or a to External Influencer. |  |

**Related element**

- Means Concepts

**Related diagrams**

- Business Motivation Diagram
- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="margin-top: 10.0px;">The following table provides the relationships that exist between element types and their meaning.</p><table class="wrapped relative-table" style="width: 1931.61px;"><colgroup><col style="width: 334.094px;" /><col style="width: 1057.38px;" /><col style="width: 539.141px;" /></colgroup><tbody><tr><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Relationship </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);">Description </th><th style="background-color: rgb(241,242,244);color:var(--ds-text,#172b4d);"><p style="color:var(--ds-text,#172b4d);">Example</p></th></tr><tr><td><strong>Makes Operative </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Mission" /><ac:plain-text-link-body><![CDATA[ Mission ]]></ac:plain-text-link-body></ac:link>to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Vision" /></ac:link>. Meaning that the Mission lists every continuing<br />Activity to ensure the Vision.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="makes_operative.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Component Of </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /><ac:plain-text-link-body><![CDATA[ Strategy ]]></ac:plain-text-link-body></ac:link>to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Mission" /></ac:link>. Meaning that the Strategy is the method or<br />course of action that will be employed to achieve the Mission.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="component_of.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Implements </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /></ac:link>. Meaning that the Tactic realizes Strategies.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="implements.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Enables </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /><ac:plain-text-link-body><![CDATA[Strategy ]]></ac:plain-text-link-body></ac:link>to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /><ac:plain-text-link-body><![CDATA[Strategy ]]></ac:plain-text-link-body></ac:link>or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link>. Meaning that a Strategy/<br />Tactic makes another Strategy/Tactic doable. That is to say the latter Strategy/Tactic<br />provides an opportunity for the former Strategy/Tactic to be carried out. Use this link<br />to associate Strategy to another Strategy or Tactic to another Tactic.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="enables.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Effects Enforcement Level </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link>. Meaning that the Tactics influences the</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="effects_enforcement_level.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Formulated Based On </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /><ac:plain-text-link-body><![CDATA[Strategy ]]></ac:plain-text-link-body></ac:link>or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link>. Meaning<br />that the Strategy or Tactic is planned according to what result the Business Policy or<br />Business Rule desires.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="formulated based on.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Channel Efforts Towards </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /><ac:plain-text-link-body><![CDATA[Strategy ]]></ac:plain-text-link-body></ac:link>to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Goal" /></ac:link>, or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link> to an <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Objective" /></ac:link>. Meaning that the Strategy is<br />coordinated as activities aimed towards Goals as Tactic towards Objective. For example, the<br />Tactic “Free delivery” channels efforts towards the Objective “5% increase in sales within 3<br />months.”</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="channel_effort_towards.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Governs </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /><ac:plain-text-link-body><![CDATA[Strategy ]]></ac:plain-text-link-body></ac:link>or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ac:link>. Meaning that the Business Policy or BusinessRule determines the Strategy or Tactic.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="governs.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Basis For </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link>. Meaning that the Business Policy is the key to achieve Business Rule.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="basis_for.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td><strong>Supports Achievement Of </strong></td><td><p>This link connects <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link> to a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Goal" /></ac:link> or <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Objective" /></ac:link>. Meaning that the Business Policy provides an<br />idea or reason to develop the Strategy or Tactic.</p></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="supports_achievement_of.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr><tr><td colspan="1"><strong>Acts As Regulation </strong></td><td colspan="1"><p>This link connects a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Policy" /></ac:link> or a <ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Rule" /></ac:link> to External Influencer.</p></td><td colspan="1"><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="acts_as_regulation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mean Concept Relationships" /></ri:attachment></ac:image></p></div></td></tr></tbody></table><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Means+Concepts">Means Concepts</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031965 space=CBMP2024x version=1 -->
## PAGE 00126: Means Concepts

- page_id: `290031965`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031965/Means+Concepts
- version_number: 1
- version_date: `2026-02-09T14:55:27.711+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram
- labels: []

### NORMALIZED CONTENT

The Means elements provide a method to achieve the ends.

There are five types of Means elements:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The Means elements provide a method to achieve the ends.</p><p>There are five types of Means elements:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="91b0442e-a113-4ec6-86c6-f9f3a20bb4ae" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031815 space=CBMP2024x version=1 -->
## PAGE 00127: Message Boundary Event

- page_id: `290031815`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031815/Message+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:16:04.653+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Message Boundary Event is triggered by an arrived message. Once triggered, it changes a normal flow into an exception flow or parallel.

A Message Boundary Event displays any of the following on the diagram:

- A Message Boundary Event name if the name is specified.
- A Message Ref property value if the name is unspecified.
- An Operation Ref property if the name and Message Ref are not specified.

**Notation**

- Message Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_message.png']
- Message Boundary Event (Cancel Activity - False) [ATTACHMENT filename='boundary_event_message_cancelactivity.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Message Boundary Event is triggered by an arrived message. Once triggered, it changes a normal flow into an exception flow or parallel.</p><p>A Message Boundary Event displays any of the following on the diagram:</p><ul><li>A Message Boundary Event name if the name is specified.</li><li>A Message Ref property value if the name is unspecified.</li><li>An Operation Ref property if the name and Message Ref are not specified.</li></ul><p><strong>Notation</strong></p><ul><li>Message Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_message.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Boundary Event" /></ri:attachment></ac:image> </li><li>Message Boundary Event (Cancel Activity - False)<br /><ac:image><ri:attachment ri:filename="boundary_event_message_cancelactivity.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Boundary Event" /></ri:attachment></ac:image></li></ul><p><br /></p><p><br /></p><p />
````

<!--NOMAGIC_PAGE id=290031785 space=CBMP2024x version=1 -->
## PAGE 00128: Message Catching Intermediate Event

- page_id: `290031785`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031785/Message+Catching+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T13:59:57.971+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Message Catching Intermediate Event is used to receive a message.

This event causes a process to continue if it is waiting for the message.

A Message Catching Intermediate Event displays any of the following on a diagram:

- A Message Catching Intermediate Event name if the name is specified.
- A Message Ref property value if the name is unspecified.
- An Operation Ref property if the name and Message Ref are not specified.

**Notation** 
[IMAGE alt='' src='']

**Related elements**

- Message
- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p style="margin-top: 0.0px;"><strong>Description</strong></p><p>A Message Catching Intermediate Event is used to receive a message.</p><p>This event causes a process to continue if it is waiting for the message.</p><p>A Message Catching Intermediate Event displays any of the following on a diagram:</p><ul><li>A Message Catching Intermediate Event name if the name is specified.</li><li>A Message Ref property value if the name is unspecified.</li><li>An Operation Ref property if the name and Message Ref are not specified.</li></ul><p><strong>Notation</strong><br /><ac:image><ri:attachment ri:filename="intermediate_catch_event_message.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Catching Intermediate Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Message">Message</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031845 space=CBMP2024x version=1 -->
## PAGE 00129: Message End Event

- page_id: `290031845`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031845/Message+End+Event
- version_number: 1
- version_date: `2026-02-09T14:21:28.320+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Message End Event indicates that a message will be sent when a process is completed.

This event displays any of the following on a diagram:

- A Message End Event name if the name is specified.
- A Message Ref property value if the name is unspecified.
- An Operation Ref property if the name and Message Ref are not specified.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- End Events
- Message

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Message End Event indicates that a message will be sent when a process is completed.</p><p>This event displays any of the following on a diagram:</p><ul><li>A Message End Event name if the name is specified.</li><li>A Message Ref property value if the name is unspecified.</li><li>An Operation Ref property if the name and Message Ref are not specified.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_message.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message End Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events">End Events</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Message">Message</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p><p />
````

<!--NOMAGIC_PAGE id=290031902 space=CBMP2024x version=1 -->
## PAGE 00130: Message Flow

- page_id: `290031902`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031902/Message+Flow
- version_number: 1
- version_date: `2026-02-09T14:39:07.184+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Message Flow is used to show the flow of messages between two participants who are prepared to send and receive them.

- A Message Flow must connect separate Pools. It can be connected to the pool boundary or an element inside the pool.
- A Message Flow cannot connect two elements in the same Pool.

Messages that are sent by a Message Flow can be displayed on a diagram in two ways:

- overlapping the Message Flow
- associated with the Message Flow

However, they can also be hidden.

[IMAGE alt='' src='']

###### Message Flows between two pools.

[IMAGE alt='' src='']

###### Messages overlapping Message Flows.

[IMAGE alt='' src='']

###### Message Flows between Pools Inner elements.

**Related element**

- Pool and Lane

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Process Diagram

**Related procedure**

- Creating and Using a Sequence Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Message Flow is used to show the flow of messages between two participants who are prepared to send and receive them.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a22639dc-1888-49e6-b405-3b6ece737c90"><ac:rich-text-body><ul><li>A Message Flow must connect separate Pools. It can be connected to the pool boundary or an element inside the pool.</li><li>A Message Flow cannot connect two elements in the same Pool.</li></ul></ac:rich-text-body></ac:structured-macro><p>Messages that are sent by a Message Flow can be displayed on a diagram in two ways:</p><ul><li>overlapping the Message Flow</li><li>associated with the Message Flow</li></ul><p>However, they can also be hidden.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="collaboration_I.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Flow" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Message Flows between two pools.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="message_flow_overlapping.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Flow" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Messages overlapping Message Flows.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="collaboration_II.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Flow" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Message Flows between Pools Inner elements.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane">Pool and Lane</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031757 space=CBMP2024x version=1 -->
## PAGE 00131: Message Start Event

- page_id: `290031757`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031757/Message+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:54:12.098+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Message Start Event means that a message from a participant has arrived and triggered the start of a process.

A Message Start Event displays any of the following on a diagram:

- A Message Start Event name if the name is specified.
- A Message Ref property value if the name is unspecified.
- An Operation Ref property if the name and Message Ref are not specified.

**Notation**

- Interrupting Message Start Event [ATTACHMENT filename='start_event_interrupting.png']
- Non-interrupting Message Start Event [ATTACHMENT filename='start_event_nonint.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Message Start Event means that a message from a participant has arrived and triggered the start of a process.</p><p>A Message Start Event displays any of the following on a diagram:</p><ul><li>A Message Start Event name if the name is specified.</li><li>A Message Ref property value if the name is unspecified.</li><li>An Operation Ref property if the name and Message Ref are not specified.</li></ul><p><strong>Notation</strong></p><ul><li>Interrupting Message Start Event<br /><ac:image><ri:attachment ri:filename="start_event_interrupting.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Start Event" /></ri:attachment></ac:image></li><li>Non-interrupting Message Start Event<br /><ac:image><ri:attachment ri:filename="start_event_nonint.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Start Event" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031801 space=CBMP2024x version=1 -->
## PAGE 00132: Message Throwing Intermediate Event

- page_id: `290031801`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031801/Message+Throwing+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:11:14.492+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Throwing Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Message Throwing Intermediate Event is used to send a message.

This Event displays any of the following on a diagram:

- A Message Throwing Intermediate Event name if the name is specified.
- A Message Ref property value if the name is unspecified.
- An Operation Ref property if the name and Message Ref are not specified.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Message Throwing Intermediate Event is used to send a message.</p><p>This Event displays any of the following on a diagram:</p><ul><li>A Message Throwing Intermediate Event name if the name is specified.</li><li>A Message Ref property value if the name is unspecified.</li><li>An Operation Ref property if the name and Message Ref are not specified.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_throwing_event_message.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Message Throwing Intermediate Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032097 space=CBMP2024x version=1 -->
## PAGE 00133: Migrating from BPMN 1.1

- page_id: `290032097`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032097/Migrating+from+BPMN+1.1
- version_number: 1
- version_date: `2026-02-09T16:04:23.822+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Migration
- labels: []

### NORMALIZED CONTENT

The MagicDraw 16.8 and earlier versions support BPMN 1.1 and Business Process diagrams, this let you to model business processes using the BPMN 1.1 notation.

The support for BPMN 1.1 and Business Process diagrams is no longer available from MagicDraw version 17.0.1. It is replaced by the Cameo Business Modeler support for the BPMN 2.0 specification.

You can convert your MagicDraw projects containing old BPMN profile and Business Process diagrams to the new BPMN 2.0 standard. A backup file will be created for the project conversion. This backup file lets you find your BPMN 1.1 models when you need them.

To convert a BPMN 1.1 project to BPMN 2.0 by opening it

1. Open a MagicDraw project that contains a BPMN Profile or Business Process diagram. A Question dialog opens.
2. Click Yes to convert the project.
3. Click OK .

To convert a BPMN 1.1 project to BPMN 2.0 by importing it

1. On the main menu, click File > Import From > BPMN 1.1 Project . The Open BPMN 1.1 Project dialog opens.
2. Select a project that contains a Business Process diagram and click Open .
3. Click OK .

A backup file project_name_bpmn1.1.bak is created when the project has been migrated.The file includes the BPMN 1.1 project before the migration.

To convert a Teamwork BPMN 1.1 project to BPMN 2.0

Before migrating a Teamwork BPMN 1.1 project to BPMN 2.0, make sure that other users have not locked the BPMN elements.

1. On the main menu, click File > Import From > BPMN 1.1 Project . A Question dialog opens.
2. Click Yes to convert the project. Another Question dialog opens to inform you that all elements will be locked.
3. Click Yes .

A backup file for a Teamwork project will not be created when migrating the project to BPMN 2.0. Use a Teamwork version as a backup copy that has included the BPMN 1.1 Business Process diagrams before migrating the project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The MagicDraw 16.8 and earlier versions support BPMN 1.1 and Business Process diagrams, this let you to model business processes using the BPMN 1.1 notation.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="4b6daf14-641a-4e9c-8df7-a53a5715a61e"><ac:rich-text-body>The support for BPMN 1.1 and Business Process diagrams is no longer available from MagicDraw version 17.0.1. It is replaced by the Cameo Business Modeler support for the BPMN 2.0 specification.</ac:rich-text-body></ac:structured-macro><p>You can convert your MagicDraw projects containing old BPMN profile and Business Process diagrams to the new BPMN 2.0 standard. A backup file will be created for the project conversion. This backup file lets you find your BPMN 1.1 models when you need them.</p><p><br /></p><p>To convert a BPMN 1.1 project to BPMN 2.0 by opening it</p><hr /><ol><li>Open a MagicDraw project that contains a BPMN Profile or Business Process diagram. A Question dialog opens.</li><li>Click <strong>Yes</strong> to convert the project.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To convert a BPMN 1.1 project to BPMN 2.0 by importing it</p><hr /><ol><li>On the main menu, click <strong>File</strong> &gt; <strong>Import From</strong> &gt; <strong>BPMN 1.1 Project</strong>. The <strong>Open BPMN 1.1 Project</strong> dialog opens.</li><li>Select a project that contains a Business Process diagram and click <strong>Open</strong>.</li><li>Click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="d199a91a-85a8-45af-bef3-64c4e7aedeca"><ac:rich-text-body>A backup file project_name_bpmn1.1.bak is created when the project has been migrated.The file includes the BPMN 1.1 project before the migration.</ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p><p>To convert a Teamwork BPMN 1.1 project to BPMN 2.0</p><hr /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="82d243a8-680b-468b-b2e1-03a123601b91"><ac:rich-text-body>Before migrating a Teamwork BPMN 1.1 project to BPMN 2.0, make sure that other users have not locked the BPMN elements.</ac:rich-text-body></ac:structured-macro><ol><li>On the main menu, click <strong>File</strong> &gt;<strong> Import From</strong> &gt; <strong>BPMN 1.1 Project</strong>. A Question dialog opens.</li><li>Click <strong>Yes</strong> to convert the project. Another Question dialog opens to inform you that all elements will be locked.</li><li>Click <strong>Yes</strong>.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="de4d1ae3-6489-4e7f-b09a-c8c0c330ba39"><ac:rich-text-body>A backup file for a Teamwork project will not be created when migrating the project to BPMN 2.0. Use a Teamwork version as a backup copy that has included the BPMN 1.1 Business Process diagrams before migrating the project.</ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290032098 space=CBMP2024x version=1 -->
## PAGE 00134: Migrating to UML Profile for BPMN2 v1.0

- page_id: `290032098`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032098/Migrating+to+UML+Profile+for+BPMN2+v1.0
- version_number: 1
- version_date: `2026-02-09T16:04:32.237+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Migration
- labels: []

### NORMALIZED CONTENT

The BPMN2 is supported by Cameo Business Modeler Plugin 17.0 and later versions of the tool; however, some further changes have been made in Cameo Business Modeler Plugin 19.0 to improve the UML Profile for BPMN2 v1.0 support. The migration comes with the changes listed below:

- Some BPMN elements have been renamed

| Old Name | New Name |
| --- | --- |
| Message | BPMNMessage |
| Relationship | BPMNRelationship |
| BPMNImport | Import |
| Operation | BPMNOperation |
| Association | BPMNAssociation |
| EventGatewayType | EventBasedGatewayType |
| Event | BPMNEvent |

- Some Stereotypes' metaclasses have been changed

| Stereotype | Old Metaclass Name | New Metaclass Name |
| --- | --- | --- |
| Resource | Actor, Class | Class |
| PartnerRole | Actor, Class | Class |
| ReceiveTask | OpaqueAction | AcceptEventAction |
| SendTask | OpaqueAction | CallOperationAction |
| ServiceTask | OpaqueAction | CallOperationAction |
| Task | OpaqueAction | Action |
| BPMNMessage | CentralBufferNode | Class |
| Message Flow | Dependency | Information Flow |

Please check your model if you use Stereotypes for BPMN elements. They could have been affected by the migration.

- Some elements have been removed from the BPMN Profile

| Removed Element |
| --- |
| MessageFlowNode |
| Correlation |
| AttributeProperty |
| PinProperty |
| VariableProperty |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target">The BPMN2 is supported by Cameo Business Modeler Plugin 17.0 and later versions of the tool; however, some further changes have been made in Cameo Business Modeler Plugin 19.0 to improve the UML Profile for BPMN2 v1.0 support. The migration comes with the changes listed below: </p><ul><li>Some BPMN elements have been renamed</li></ul><table class="relative-table wrapped" style="width: 23.1487%;"><colgroup><col style="width: 48.9311%;" /><col style="width: 51.0689%;" /></colgroup><tbody><tr><th>Old Name</th><th>New Name</th></tr><tr><td>Message</td><td>BPMNMessage</td></tr><tr><td colspan="1">Relationship</td><td colspan="1">BPMNRelationship</td></tr><tr><td colspan="1">BPMNImport</td><td colspan="1">Import</td></tr><tr><td colspan="1">Operation</td><td colspan="1">BPMNOperation</td></tr><tr><td colspan="1">Association</td><td colspan="1">BPMNAssociation</td></tr><tr><td colspan="1">EventGatewayType</td><td colspan="1">EventBasedGatewayType</td></tr><tr><td colspan="1">Event</td><td colspan="1">BPMNEvent</td></tr></tbody></table><p><br /></p><ul><li>Some Stereotypes' metaclasses have been changed</li></ul><table class="relative-table wrapped" style="width: 27.6467%;"><colgroup><col style="width: 30.4175%;" /><col style="width: 33.996%;" /><col style="width: 35.5865%;" /></colgroup><tbody><tr><th>Stereotype</th><th>Old Metaclass Name</th><th colspan="1">New Metaclass Name</th></tr><tr><td>Resource</td><td>Actor, Class</td><td colspan="1">Class</td></tr><tr><td>PartnerRole</td><td>Actor, Class</td><td colspan="1">Class</td></tr><tr><td colspan="1">ReceiveTask</td><td colspan="1">OpaqueAction</td><td colspan="1">AcceptEventAction</td></tr><tr><td colspan="1">SendTask</td><td colspan="1">OpaqueAction</td><td colspan="1">CallOperationAction</td></tr><tr><td colspan="1">ServiceTask</td><td colspan="1">OpaqueAction</td><td colspan="1">CallOperationAction</td></tr><tr><td colspan="1">Task</td><td colspan="1">OpaqueAction</td><td colspan="1">Action</td></tr><tr><td colspan="1">BPMNMessage</td><td colspan="1">CentralBufferNode</td><td colspan="1">Class</td></tr><tr><td colspan="1">Message Flow</td><td colspan="1">Dependency</td><td colspan="1">Information Flow</td></tr></tbody></table><p><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="43179ce2-b127-453c-aae1-d8b16115074d"><ac:rich-text-body><p>Please check your model if you use Stereotypes for BPMN elements. They could have been affected by the migration.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><ul><li>Some elements have been removed from the BPMN Profile</li></ul><table class="relative-table wrapped" style="width: 262.0px;"><colgroup><col style="width: 0.0px;" /></colgroup><tbody><tr><th>Removed Element</th></tr><tr><td>MessageFlowNode</td></tr><tr><td>Correlation</td></tr><tr><td colspan="1">AttributeProperty</td></tr><tr><td colspan="1">PinProperty</td></tr><tr><td>VariableProperty</td></tr></tbody></table><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=290032096 space=CBMP2024x version=1 -->
## PAGE 00135: Migration

- page_id: `290032096`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032096/Migration
- version_number: 1
- version_date: `2026-02-09T16:04:14.728+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

The sections listed below cover the BPMN Migration topic:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The sections listed below cover the BPMN Migration topic:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3b3bcb22-e33b-4117-bd58-7c47f9ef7d8b" /></p>
````

<!--NOMAGIC_PAGE id=290031966 space=CBMP2024x version=1 -->
## PAGE 00136: Mission

- page_id: `290031966`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031966/Mission
- version_number: 1
- version_date: `2026-02-09T14:55:51.071+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Means Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Mission indicates the ongoing operational Activity of the enterprise. The Mission describes what the business is or will be doing on a day-to-day basis.

A Mission makes a Vision operative. It indicates the ongoing Activity that makes the Vision a reality. A Mission is planned by means of Strategies.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Means Concepts
- Mean Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Mission indicates the ongoing operational Activity of the enterprise. The Mission describes what the business is or will be doing on a day-to-day basis.</p><p>A Mission makes a Vision operative. It indicates the ongoing Activity that makes the Vision a reality. A Mission is planned by means of Strategies.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="mission.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Mission" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Means+Concepts">Means Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Mean+Concept+Relationships">Mean Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032091 space=CBMP2024x version=1 -->
## PAGE 00137: Modifying BPMN Matrices

- page_id: `290032091`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032091/Modifying+BPMN+Matrices
- version_number: 1
- version_date: `2026-02-09T16:02:21.076+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Tables and Matrices
- labels: []

### NORMALIZED CONTENT

To change a row or column scope, do one of the following

- In the Model Browser, select one or more elements you wish to see on your matrix and drag them to the Row Scope/Column Scope box in the Criteria area.
- Click the ... button next to the Row Scope/Column Scope box and in the opened dialog select what elements you wish to see on your matrix. Click OK .

To change resource assignment to an Activity for BPMN Resources Usage Matrix, do one of the following

- Double-click the cell to create/remove a relationship between Activity and resource.
- Right-click the cell and from the shortcut menu select Resource .

To save a BPMN Matrices as *.csv

- On the BPMN Matrix toolbar, click the Export button to save your matrix as a Comma Separated Values ( .csv) file. The file can be opened with MS Excel.

**Related diagrams**

- BPMN Resources Usage Matrices
- BPMN Data Usage Matrices

**Related procedures**

- Creating a Diagram

**Related external resource**

- Dependency Matrix

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To change a row or column scope, do one of the following</p><hr style="" /><ul><li>In the Model Browser, select one or more elements you wish to see on your matrix and drag them to the <strong>Row Scope/Column Scope</strong> box in the <strong>Criteria</strong> area.</li><li>Click the ... button next to the <strong>Row Scope/Column Scope</strong> box and in the opened dialog select what elements you wish to see on your matrix. Click <strong>OK</strong>.</li></ul><p><br /></p><p>To change resource assignment to an Activity for BPMN Resources Usage Matrix, do one of the following</p><hr style="" /><ul><li>Double-click the cell to create/remove a relationship between Activity and resource.</li><li>Right-click the cell and from the shortcut menu select <strong>Resource</strong>.</li></ul><p><br /></p><p>To save a BPMN Matrices as *.csv</p><hr style="" /><ul><li>On the BPMN Matrix toolbar, click the <strong>Export</strong> button to save your matrix as a Comma Separated Values ( .csv) file. The file can be opened with MS Excel.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Resources+Usage+Matrices">BPMN Resources Usage Matrices</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Data+Usage+Matrices">BPMN Data Usage Matrices</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul><p><strong>Related external resource</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Dependency+Matrix">Dependency Matrix</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032090 space=CBMP2024x version=1 -->
## PAGE 00138: Modifying BPMN Table

- page_id: `290032090`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032090/Modifying+BPMN+Table
- version_number: 1
- version_date: `2026-02-09T16:01:31.999+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Tables and Matrices
- labels: []

### NORMALIZED CONTENT

To create a new element in a BPMN table

- Click the Add New button on the Table Edit toolbar.

To add an existing element to a BPMN table, do one of the following

- In the Containment tree, select one or more Resources and drag them to the table. Hold down Shift to select multiple elements that are grouped together.Hold down Ctrl to select multiple elements that are not grouped together.
- Click the Add Existing button on the Table Edit toolbar. The select element dialog opens, select element you need to add to the table and click OK .

Multiple Selection

To remove an element from a BPMN table

- Select the element in the table and click the Delete From Table button on the Table Edit toolbar.

To delete an element from both a BPMN table and the model

- Select the element in the table and click the Delete button on the Table Edit toolbar.

To display columns of the table

1. On the Table Edit toolbar, click Show Columns .
2. From the menu, select properties to be shown in the table.

To edit element property value in a cell

The property can be edited if it is not locked.

1. Click a cell.
2. Do one of the following:
  - Edit the value directly in the selected cell.
  - Click the ... button. The property value editor dialog opens.

To export a BPMN table to the *.html, *.csv, or *.xlsx format

1. On the BPMN table toolbar, click Export . The Choose file dialog opens.
2. Do one of the following:
  - Browse for a location to save a table in.
  - Type the exported table name.
  - Select the exported table format.
3. Click Save .

**Related procedures**

- Creating a Diagram

**Related external resource**

- Generic table

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To create a new element in a BPMN table</p><hr style="" /><ul><li>Click the <strong>Add New</strong> button on the Table Edit toolbar.</li></ul><p><br /></p><p>To add an existing element to a BPMN table, do one of the following</p><hr style="" /><ul><li><p class="auto-cursor-target">In the Containment tree, select one or more Resources and drag them to the table.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9aaab316-cff6-4b41-8d7f-4d2cdf7bbdc1"><ac:rich-text-body><ul><li>Hold down Shift to select multiple elements that are grouped together.</li><li>Hold down Ctrl to select multiple elements that are not grouped together.</li></ul></ac:rich-text-body></ac:structured-macro></li><li>Click the <strong>Add Existing</strong> button on the Table Edit toolbar. The select element dialog opens, select element you need to add to the table and click <strong>OK</strong>.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5220443a-7e52-48be-8c07-f9f92b61300d"><ac:rich-text-body>To select more than one element, click the <strong>Multiple Selection</strong> button.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To remove an element from a BPMN table</p><hr style="" /><ul><li>Select the element in the table and click the <strong>Delete From Table</strong> button on the Table Edit toolbar.</li></ul><p><br /></p><p>To delete an element from both a BPMN table and the model</p><hr style="" /><ul><li>Select the element in the table and click the <strong>Delete</strong> button on the Table Edit toolbar.</li></ul><p><br /></p><p>To display columns of the table</p><hr style="" /><ol><li>On the Table Edit toolbar, click <strong>Show Columns</strong>.</li><li>From the menu, select properties to be shown in the table.</li></ol><p><br /></p><p>To edit element property value in a cell</p><hr style="" /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="12fb2e56-77b8-40e7-b5f4-2b012e9fe6c0"><ac:rich-text-body>The property can be edited if it is not locked.</ac:rich-text-body></ac:structured-macro><ol><li>Click a cell.</li><li>Do one of the following:<ul><li>Edit the value directly in the selected cell.</li><li>Click the <strong>...</strong> button. The property value editor dialog opens.</li></ul></li></ol><p><br /></p><p>To export a BPMN table to the *.html, *.csv, or *.xlsx format</p><hr style="" /><ol><li>On the BPMN table toolbar, click <strong>Export</strong>. The <strong>Choose file</strong> dialog opens.</li><li>Do one of the following:<ul><li>Browse for a location to save a table in.</li><li>Type the exported table name.</li><li>Select the exported table format.</li></ul></li><li>Click <strong>Save</strong>.</li></ol><p><br /></p><p style="margin-top: 0.0px;"><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul><p><strong>Related external resource</strong></p><ul><li><a href="https://docs.nomagic.com/display/MD2024xR1/Generic+table" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Generic table</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031941 space=CBMP2024x version=1 -->
## PAGE 00139: Multilevel with Owner Number

- page_id: `290031941`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031941/Multilevel+with+Owner+Number
- version_number: 1
- version_date: `2026-02-09T14:49:22.556+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Numbering Elements > Numbering Schemas
- labels: []

### NORMALIZED CONTENT

**Description**

A Multilevel with Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is displayed before the element number.

**Example**

[IMAGE alt='' src='']

###### Multilevel Numbering style with element owner number.

A Multilevel with Owner Number numbering schema is the default schema for all BPMN diagram elements.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Using BPMN Element Numbers

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Multilevel with Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is displayed before the element number.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="element_numbering_multilevel.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multilevel with Owner Number" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Multilevel Numbering style with element owner number.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c26a9a48-25c2-49b1-b7f4-2eb2f75b5282"><ac:rich-text-body><p>A Multilevel with Owner Number numbering schema is the default schema for all BPMN diagram elements.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Element+Numbers" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using BPMN Element Numbers</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031943 space=CBMP2024x version=1 -->
## PAGE 00140: Multilevel without Owner Number

- page_id: `290031943`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031943/Multilevel+without+Owner+Number
- version_number: 1
- version_date: `2026-02-09T14:50:06.435+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Numbering Elements > Numbering Schemas
- labels: []

### NORMALIZED CONTENT

**Description**

A Multilevel without Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is not included in the element number.

**Example**

[IMAGE alt='' src='']

###### Multilevel Numbering style without element owner number.

When a Multilevel without element number numbering schema is used, the numbers in a project are not unique. Elements with the same number can exist in multiple diagrams.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Using BPMN Element Numbers

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Multilevel without Owner Number numbering schema provides multilevel element numbering. An Element owner (BPMN Process, BPMN Collaboration, or Choreography) number is not included in the element number.</p><p><strong>Example</strong></p><p><ac:image ac:align="center" ac:height="250"><ri:attachment ri:filename="element_numbering_multilevel_II.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multilevel without Owner Number" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Multilevel Numbering style without element owner number.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="47f86cd7-cfac-410d-a52b-3266d8d1fbfe"><ac:rich-text-body><p>When a Multilevel without element number numbering schema is used, the numbers in a project are not unique. Elements with the same number can exist in multiple diagrams.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Element+Numbers" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using BPMN Element Numbers</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031836 space=CBMP2024x version=1 -->
## PAGE 00141: Multiple Boundary Event

- page_id: `290031836`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031836/Multiple+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:19:47.627+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Multiple Boundary Event indicates that there are multiple triggers assigned to the Event. Only one of the specified triggers is required. The Event that occurred changes a normal flow into an exception flow.

**Notation**

- Multiple Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_multiple.png']
- Multiple Boundary Event (Cancel Activity - False) [ATTACHMENT filename='boundary_event_multiple_false.png']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Multiple Boundary Event indicates that there are multiple triggers assigned to the Event. Only one of the specified triggers is required. The Event that occurred changes a normal flow into an exception flow.</p><p><strong>Notation</strong></p><ul><li>Multiple Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_multiple.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multiple Boundary Event" /></ri:attachment></ac:image></li><li>Multiple Boundary Event (Cancel Activity - False)<br /><ac:image><ri:attachment ri:filename="boundary_event_multiple_false.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multiple Boundary Event" /></ri:attachment></ac:image></li></ul><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031796 space=CBMP2024x version=1 -->
## PAGE 00142: Multiple Catching Intermediate Event

- page_id: `290031796`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031796/Multiple+Catching+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:02:28.967+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Multiple Catching Intermediate Event signifies that multiple types of events can be caught. Only one of the defined event triggers is required.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Multiple Catching Intermediate Event signifies that multiple types of events can be caught. Only one of the defined event triggers is required.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event_multiple.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multiple Catching Intermediate Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031859 space=CBMP2024x version=1 -->
## PAGE 00143: Multiple End Event

- page_id: `290031859`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031859/Multiple+End+Event
- version_number: 1
- version_date: `2026-02-09T14:24:25.562+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Multiple End Event shows that there are multiple consequences of ending a process and all of them occur, for example, multiple messages might be sent.

**Notation**

[IMAGE alt='' src='']

**Related element**

- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Multiple End Event shows that there are multiple consequences of ending a process and all of them occur, for example, multiple messages might be sent.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_multiple.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multiple End Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031776 space=CBMP2024x version=1 -->
## PAGE 00144: Multiple Start Event

- page_id: `290031776`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031776/Multiple+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:58:17.154+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Multiple Start Event indicates that there are multiple ways to trigger a process. However, only one is required.

**Notation**

- Interrupting Multiple Start Event [ATTACHMENT filename='start_event_multiple_interr.png']
- Non-interrupting Multiple Start Event [ATTACHMENT filename='start_event_multiple_noninterr.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Multiple Start Event indicates that there are multiple ways to trigger a process. However, only one is required.</p><p><strong>Notation</strong></p><ul><li>Interrupting Multiple Start Event<br /><ac:image><ri:attachment ri:filename="start_event_multiple_interr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multiple Start Event" /></ri:attachment></ac:image></li><li>Non-interrupting Multiple Start Event<br /><ac:image><ri:attachment ri:filename="start_event_multiple_noninterr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multiple Start Event" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031811 space=CBMP2024x version=1 -->
## PAGE 00145: Multiple Throwing Intermediate Event

- page_id: `290031811`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031811/Multiple+Throwing+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:15:31.385+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Throwing Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Multiple Throwing Intermediate Event signifies that multiple types of events are thrown. All of the defined triggers will be thrown by this event.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Multiple Throwing Intermediate Event signifies that multiple types of events are thrown. All of the defined triggers will be thrown by this event.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_throwing_event_multiple.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Multiple Throwing Intermediate Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032076 space=CBMP2024x version=1 -->
## PAGE 00146: Navigation Between BPMN Diagrams

- page_id: `290032076`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032076/Navigation+Between+BPMN+Diagrams
- version_number: 1
- version_date: `2026-02-09T15:54:45.944+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

You can navigate to

- higher level BPMN diagrams
- related Process diagrams

To navigate to a higher level BPMN diagrams

- At the bottom left corner of the diagram pane, on the toolbar, click the [ATTACHMENT filename='up_button.png'] button and select higher level BPMN diagram.

To navigate to a related Process diagrams

- At the bottom left corner of the diagram pane, on the toolbar, click the [ATTACHMENT filename='related.png'] button and select related process diagram.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Tasks
- Creating and Using SubProcesses
- Using Activities
- Creating and Using an Event
- Creating and Using a Sequence Flow
- Creating and Using Data Items

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can navigate to</p><ul><li>higher level BPMN diagrams</li><li>related Process diagrams</li></ul><p>To navigate to a higher level BPMN diagrams</p><hr style="" /><ul><li>At the bottom left corner of the diagram pane, on the toolbar, click the <ac:image><ri:attachment ri:filename="up_button.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Navigation Between BPMN Diagrams" /></ri:attachment></ac:image> button and select higher level BPMN diagram.</li></ul><p><br /></p><p>To navigate to a related Process diagrams</p><hr style="" /><ul><li>At the bottom left corner of the diagram pane, on the toolbar, click the <ac:image ac:thumbnail="true" ac:height="44"><ri:attachment ri:filename="related.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Navigation Between BPMN Diagrams" /></ri:attachment></ac:image>button and select related process diagram.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Tasks" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Tasks</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+SubProcesses" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using SubProcesses</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Activities">Using Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031843 space=CBMP2024x version=1 -->
## PAGE 00147: None End Event

- page_id: `290031843`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031843/None+End+Event
- version_number: 1
- version_date: `2026-02-09T14:20:45.426+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

A None Start Event does not have a defined result.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Boundary Events
- Activities
- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A None Start Event does not have a defined result.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="None End Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031783 space=CBMP2024x version=1 -->
## PAGE 00148: None Intermediate Event

- page_id: `290031783`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031783/None+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T13:59:12.656+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A None Intermediate Event does not have a defined trigger.

This event is used to model methodologies that use events to indicate some changes in a state of process.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A None Intermediate Event does not have a defined trigger.</p><p>This event is used to model methodologies that use events to indicate some changes in a state of process.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="None Intermediate Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031755 space=CBMP2024x version=1 -->
## PAGE 00149: None Start Event

- page_id: `290031755`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031755/None+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:54:01.559+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

A None Start Event does not have a defined trigger that invokes the start of a process.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A None Start Event does not have a defined trigger that invokes the start of a process.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="start_event.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="None Start Event" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031938 space=CBMP2024x version=1 -->
## PAGE 00150: Numbering Elements

- page_id: `290031938`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031938/Numbering+Elements
- version_number: 1
- version_date: `2026-02-09T14:48:40.485+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler offers an automatic numbering feature to number specific types of BPMN elements.

Each element number is saved in an ID property of element specification.

[IMAGE alt='' src='']

###### BPMN Process Diagram showing element numbers.

Numbering elements are described in the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler offers an automatic numbering feature to number specific types of BPMN elements.</p><p>Each element number is saved in an ID property of element specification.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="element_numbering.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Numbering Elements" /></ri:attachment></ac:image></p><h6 style="text-align: center;">BPMN Process Diagram showing element numbers.</h6><p>Numbering elements are described in the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="870a1867-d60b-4393-be38-eafdef2c714a" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031940 space=CBMP2024x version=1 -->
## PAGE 00151: Numbering Schemas

- page_id: `290031940`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031940/Numbering+Schemas
- version_number: 1
- version_date: `2026-02-09T14:48:48.952+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Numbering Elements
- labels: []

### NORMALIZED CONTENT

Types of numbering schemas predefined for BPMN elements are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Types of numbering schemas predefined for BPMN elements are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c6e3a3b5-177e-4043-b45d-24848a97f6f0" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031960 space=CBMP2024x version=1 -->
## PAGE 00152: Objective

- page_id: `290031960`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031960/Objective
- version_number: 1
- version_date: `2026-02-09T14:54:52.341+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Ends Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

An Objective is a statement of an attainable, time-targeted, and measurable target that the enterprise seeks to meet in order to achieve its Goals.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Ends Concepts
- End Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Objective is a statement of an attainable, time-targeted, and measurable target that the enterprise seeks to meet in order to achieve its Goals.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="objective.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Objective" /></ri:attachment></ac:image></p><p><br /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Ends+Concepts" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Ends Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Concept+Relationships" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032019 space=CBMP2024x version=1 -->
## PAGE 00153: Organization Structure Diagram

- page_id: `290032019`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032019/Organization+Structure+Diagram
- version_number: 1
- version_date: `2026-02-09T15:31:56.808+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

An Organization Structure Diagram represents the hierarchical structure of an organization. This diagram allows showing organization departments, roles inside departments, and actual persons inside an organization. The diagram can also represent the reporting structure of an organization.

**Example**

[IMAGE alt='' src='']

###### Organization Structure diagram.

**Related elements**

- Resource
- Organization Unit
- Role
- Person
- Information system
- Composition

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An Organization Structure Diagram represents the hierarchical structure of an organization. This diagram allows showing organization departments, roles inside departments, and actual persons inside an organization. The diagram can also represent the reporting structure of an organization.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="organization_structure_diagram.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Organization Structure Diagram" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Organization Structure diagram.</h6><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul class="childpages-macro"><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Composition">Composition</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032022 space=CBMP2024x version=1 -->
## PAGE 00154: Organization Unit

- page_id: `290032022`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032022/Organization+Unit
- version_number: 1
- version_date: `2026-02-09T15:32:56.772+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Organization Structure Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

An organization represents a group of persons, associated for a particular purpose. An Element may denote an organization, a department, or a working group inside an organization. e. g., the company, sale department, etc. This element is combined with the Participant definition.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Resource
- Role
- Person
- Information system
- Pool and Lane
- Activities
- Choreography Activities

**Related diagrams**

- Organization Structure Diagram
- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram
- BPMN Resources Usage Matrices

**Related Procedure**

- Using Organization Structure Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>An organization represents a group of persons, associated for a particular purpose. An Element may denote an organization, a department, or a working group inside an organization. e. g., the company, sale department, etc. This element is combined with the Participant definition.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="organization_unit.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Organization Unit" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Structure+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Organization Structure Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Resources+Usage+Matrices">BPMN Resources Usage Matrices</a></li></ul><p><strong>Related Procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Organization+Structure+Diagram">Using Organization Structure Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032045 space=CBMP2024x version=1 -->
## PAGE 00155: Package

- page_id: `290032045`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032045/Package
- version_number: 1
- version_date: `2026-02-09T15:43:01.605+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Process Definition Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

Package groups together processes and other model elements. You can organize all types of model elements into packages. The Packages themselves can be nested within other Packages.

**Notation**

[IMAGE alt='' src='']

**Related diagram**

- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Package groups together processes and other model elements. You can organize all types of model elements into packages. The Packages themselves can be nested within other Packages.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="package.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Package" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagram</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031869 space=CBMP2024x version=1 -->
## PAGE 00156: Parallel Gateway

- page_id: `290031869`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031869/Parallel+Gateway
- version_number: 1
- version_date: `2026-02-09T14:36:19.191+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Gateways
- labels: []

### NORMALIZED CONTENT

**Description**

A Parallel Gateway is used to synchronize (combine) and create parallel flows.

**Notation**

[IMAGE alt='' src='']

**Example**

[IMAGE alt='' src='']

###### Parallel Gateway.

**Related elements**

- Gateways
- Sequence Flow

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using a Sequence Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Parallel Gateway is used to synchronize (combine) and create parallel flows.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="gateway_parallel.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Parallel Gateway" /></ri:attachment></ac:image></p><p><strong>Example</strong></p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="Parallel_gateway.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Parallel Gateway" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Parallel Gateway.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Gateways">Gateways</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Sequence+Flow">Sequence Flow</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031839 space=CBMP2024x version=1 -->
## PAGE 00157: Parallel Multiple Boundary Event

- page_id: `290031839`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031839/Parallel+Multiple+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:20:15.364+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Parallel Multiple Boundary Event indicates that there are multiple triggers assigned to the event and all of them are required to trigger it.

**Notation**

- Parallel Multiple Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_parallel_multiple.png']
- Parallel Multiple Boundary Event (Cancel Activity - False) [ATTACHMENT filename='boundary_event_parallel_multiple_false.png']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Parallel Multiple Boundary Event indicates that there are multiple triggers assigned to the event and all of them are required to trigger it.</p><p><strong>Notation</strong></p><ul><li>Parallel Multiple Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_parallel_multiple.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Parallel Multiple Boundary Event" /></ri:attachment></ac:image></li><li>Parallel Multiple Boundary Event (Cancel Activity - False)<br /><ac:image><ri:attachment ri:filename="boundary_event_parallel_multiple_false.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Parallel Multiple Boundary Event" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031798 space=CBMP2024x version=1 -->
## PAGE 00158: Parallel Multiple Catching Intermediate Event

- page_id: `290031798`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031798/Parallel+Multiple+Catching+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:02:53.969+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Parallel Multiple Catching Intermediate Event signifies that multiple types of events are caught. All of the defined event triggers are required to trigger this event.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p style="margin-top: 0.0px;"><strong>Description</strong></p><p>A Parallel Multiple Catching Intermediate Event signifies that multiple types of events are caught. All of the defined event triggers are required to trigger this event.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event_parallel_multiple.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Parallel Multiple Catching Intermediate Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031779 space=CBMP2024x version=1 -->
## PAGE 00159: Parallel Multiple Start Event

- page_id: `290031779`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031779/Parallel+Multiple+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:58:27.184+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Parallel Multiple Start Event indicates that there are multiple triggers required before a process can be initiated.

**Notation**

- Interrupting Parallel Multiple Start Event [ATTACHMENT filename='start_event_multiple_parallel_interr.png']
- Non-Interrupting Parallel Multiple Start Event [ATTACHMENT filename='start_event_multiple_parallel_noninterr.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Parallel Multiple Start Event indicates that there are multiple triggers required before a process can be initiated.</p><p><strong>Notation</strong></p><ul><li>Interrupting Parallel Multiple Start Event<br /><ac:image><ri:attachment ri:filename="start_event_multiple_parallel_interr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Parallel Multiple Start Event" /></ri:attachment></ac:image></li><li>Non-Interrupting Parallel Multiple Start Event<br /><ac:image><ri:attachment ri:filename="start_event_multiple_parallel_noninterr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Parallel Multiple Start Event" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031917 space=CBMP2024x version=1 -->
## PAGE 00160: Participant

- page_id: `290031917`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031917/Participant
- version_number: 1
- version_date: `2026-02-09T14:43:48.511+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Participant represents a specific partner entity, such as a company and a more general partner role, for example, a buyer, seller, or manufacturer who is a participant in a collaboration. A Participant is often responsible for the execution of a process enclosed in a pool.

Participant element can be contained only in Collaboration or Choreography and represent Resource.

**Related elements**

- Pool and Lane
- Conversation
- Choreography Activities

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Using BPMN Collaboration Diagram
- Creating and Using Pool and Lanes

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Participant represents a specific partner entity, such as a company and a more general partner role, for example, a buyer, seller, or manufacturer who is a participant in a collaboration. A Participant is often responsible for the execution of a process enclosed in a pool.</p><p>Participant element can be contained only in Collaboration or Choreography and represent Resource.</p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Conversation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Conversation</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Collaboration+Diagram">Using BPMN Collaboration Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Pool+and+Lanes">Creating and Using Pool and Lanes</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032026 space=CBMP2024x version=1 -->
## PAGE 00161: Person

- page_id: `290032026`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032026/Person
- version_number: 1
- version_date: `2026-02-09T15:33:43.620+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Organization Structure Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Person is a type of human that is recognized by law as the subject of rights and duties. This element is combined with the Resource Role definition.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Resource
- Organization Unit
- Role
- Information system
- Pool and Lane
- Activities
- Choreography Activities

**Related diagrams**

- Organization Structure Diagram
- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram
- BPMN Resources Usage Matrices

**Related Procedure**

- Using Organization Structure Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Person is a type of human that is recognized by law as the subject of rights and duties. This element is combined with the Resource Role definition.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="person.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Person" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Structure+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Organization Structure Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Resources+Usage+Matrices">BPMN Resources Usage Matrices</a></li></ul><p><strong>Related Procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Organization+Structure+Diagram">Using Organization Structure Diagram</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031897 space=CBMP2024x version=1 -->
## PAGE 00162: Pool and Lane

- page_id: `290031897`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031897/Pool+and+Lane
- version_number: 1
- version_date: `2026-02-09T14:38:31.886+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Pool represents a participant in a collaboration. The participant can be a specific partner entity, for example, a company, or it can be a more general partner role, such as a buyer, seller, or manufacturer. Graphically, a Pool is a container to partition a process from the other pools.

A Pool can contain a process, or it can be a black box.

A Pool with suppressed content will display a multi-instance marker if the participant referenced by the pool has a minimum multiplicity value of two or more.

A Lane is a sub-partition within a pool. Lanes are used to organize and categorize activities within a pool according to function or role. They are as follows:

- internal roles, for example, Manager and Associate
- systems, for example, an enterprise application
- internal departments, for example, shipping or finance

In addition, Lanes can be nested in a pool. For example, there could be an outer set of Lanes for company departments and an inner set of Lanes for the roles within each department.

**Notation**

- Pool that contains a process or black box [ATTACHMENT filename='pool.png']
- Pool with suppressed content [ATTACHMENT filename='pool_suppressed.png']
- A Pool with Suppressed Contents Referencing a Multi-instance Participant [ATTACHMENT filename='pool_suppressed_multi.png']

**Example**

###### [IMAGE alt='' src=''] 
Pool with nested Lanes.

**Related elements**

- Resource
- Organization Unit
- Role
- Person
- Message Flow

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Process Diagram

**Related procedure**

- Creating and Using Pool and Lanes

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Pool represents a participant in a collaboration. The participant can be a specific partner entity, for example, a company, or it can be a more general partner role, such as a buyer, seller, or manufacturer. Graphically, a Pool is a container to partition a process from the other pools.</p><p>A Pool can contain a process, or it can be a black box.</p><p>A Pool with suppressed content will display a multi-instance marker if the participant referenced by the pool has a minimum multiplicity value of two or more.</p><p>A Lane is a sub-partition within a pool. Lanes are used to organize and categorize activities within a pool according to function or role. They are as follows:</p><ul><li>internal roles, for example, Manager and Associate</li><li>systems, for example, an enterprise application</li><li>internal departments, for example, shipping or finance</li></ul><p>In addition, Lanes can be nested in a pool. For example, there could be an outer set of Lanes for company departments and an inner set of Lanes for the roles within each department.</p><p><strong>Notation</strong></p><ul><li>Pool that contains a process or black box<br /><ac:image><ri:attachment ri:filename="pool.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Pool and Lane" /></ri:attachment></ac:image></li><li>Pool with suppressed content<br /><ac:image><ri:attachment ri:filename="pool_suppressed.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Pool and Lane" /></ri:attachment></ac:image></li><li>A Pool with Suppressed Contents Referencing a Multi-instance Participant<br /><ac:image><ri:attachment ri:filename="pool_suppressed_multi.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Pool and Lane" /></ri:attachment></ac:image></li></ul><p><strong>Example</strong></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);"><ac:image ac:align="center"><ri:attachment ri:filename="pool_with_nested_lanes.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Pool and Lane" /></ri:attachment></ac:image><br />Pool with nested Lanes.</h6><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role">Role</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Message+Flow">Message Flow</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Pool+and+Lanes">Creating and Using Pool and Lanes</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032002 space=CBMP2024x version=1 -->
## PAGE 00163: Potential Reward

- page_id: `290032002`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032002/Potential+Reward
- version_number: 1
- version_date: `2026-02-09T15:23:13.819+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Assessment Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Potential Reward is a category of Potential Impact that indicates the probability of gain. Some Potential Rewards are expressible as formulas, for example:

- Probability of gain (for example, 30% probability)
- Potential gain (for example, $40,000 gain)

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Assessment Concepts
- Assessment Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Potential Reward is a category of Potential Impact that indicates the probability of gain. Some Potential Rewards are expressible as formulas, for example:</p><ul><li>Probability of gain (for example, 30% probability)</li><li>Potential gain (for example, $40,000 gain)</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="potential_reward.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Potential Reward" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concepts">Assessment Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concept+Relationships" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Assessment Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032032 space=CBMP2024x version=1 -->
## PAGE 00164: Process Definition Diagram

- page_id: `290032032`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032032/Process+Definition+Diagram
- version_number: 1
- version_date: `2026-02-09T15:35:55.768+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Process Definition diagram is a tool for initial process analysis. The diagram allows you to draw business processes, group them into packages, and define the relations between those processes. 
When the initial process definition has been completed, a process flow can be provided in a BPMN Process diagram, which can be created for each process.

**Related elements**

- Package
- Relationships

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p style="margin-top: 0.0px;"><strong>Description</strong></p><p>A Process Definition diagram is a tool for initial process analysis. The diagram allows you to draw business processes, group them into packages, and define the relations between those processes.<br />When the initial process definition has been completed, a process flow can be provided in a BPMN Process diagram, which can be created for each process.</p><p><br /></p><p><strong>Related elements</strong></p><ul class="childpages-macro"><li data-uuid="596110c4-2d06-4c84-a6ed-9eebf249dc13"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Package">Package</a></li><li data-uuid="16ac3490-5966-4258-ab29-6ba345811144"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Relationships">Relationships</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032039 space=CBMP2024x version=1 -->
## PAGE 00165: Realizes

- page_id: `290032039`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032039/Realizes
- version_number: 1
- version_date: `2026-02-09T15:41:09.685+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Process Definition Diagram > BPMNRelationships
- labels: []

### NORMALIZED CONTENT

**Description**

Realizes shows that a BPMN Process can realizes a Strategy or Tactic.

**Example**

[IMAGE alt='' src='']

**Related element**

- BPMN Process

**Related diagram**

- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>Realizes shows that a BPMN Process can realizes a Strategy or Tactic.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="realizes.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Realizes" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031724 space=CBMP2024x version=1 -->
## PAGE 00166: Receive Task

- page_id: `290031724`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031724/Receive+Task
- version_number: 1
- version_date: `2026-02-09T13:51:55.761+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A Receive Task is a simple task that is designed to wait for a message to arrive from an external participant (relative to the Process). Once the message has been received, the task is completed.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Receive Task is a simple task that is designed to wait for a message to arrive from an external participant (relative to the Process). Once the message has been received, the task is completed.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="receive_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Receive Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290032021 space=CBMP2024x version=1 -->
## PAGE 00167: Resource

- page_id: `290032021`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032021/Resource
- version_number: 1
- version_date: `2026-02-09T15:32:34.169+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Organization Structure Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

The Resource is used to specify resources that can be referenced by Process. These Resources can be human resources as well as any other resource assigned to Activities during Process execution time.

Multiple processes can utilize the same Resource.

Resource can be element of the Organization structure such as Organization Unit, Role or Person.

**Related elements**

- Organization Unit
- Role
- Person
- Information system
- Pool and Lane
- Activities
- Choreography Activities

**Related diagrams**

- Organization Structure Diagram
- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram
- BPMN Resources Usage Matrices

**Related Procedure**

- Using Organization Structure Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>The Resource is used to specify resources that can be referenced by Process. These Resources can be human resources as well as any other resource assigned to Activities during Process execution time.</p><p>Multiple processes can utilize the same Resource.</p><p>Resource can be element of the Organization structure such as Organization Unit, Role or Person.</p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Structure+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Organization Structure Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Resources+Usage+Matrices">BPMN Resources Usage Matrices</a></li></ul><p><strong>Related Procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Organization+Structure+Diagram">Using Organization Structure Diagram</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032000 space=CBMP2024x version=1 -->
## PAGE 00168: Risk

- page_id: `290032000`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032000/Risk
- version_number: 1
- version_date: `2026-02-09T15:12:44.924+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Assessment Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Risk is a category of Impact Value that indicates the impact and probability of loss. Some Risks are expressible as formulas, for example:

- Probability of loss (for example, 5% probability)
- Potential loss (for example, $500,000 loss)
- Unit-of-measure (for example, loss in USD)

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Assessment Concepts
- Assessment Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Risk is a category of Impact Value that indicates the impact and probability of loss. Some Risks are expressible as formulas, for example:</p><ul><li>Probability of loss (for example, 5% probability)</li><li>Potential loss (for example, $500,000 loss)</li><li>Unit-of-measure (for example, loss in USD)</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="risk.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Risk" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concepts">Assessment Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Assessment+Concept+Relationships" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Assessment Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032024 space=CBMP2024x version=1 -->
## PAGE 00169: Role

- page_id: `290032024`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032024/Role
- version_number: 1
- version_date: `2026-02-09T15:33:19.482+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Organization Structure Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Role is a type of contact point or a responsible person, e. g., cashier, ticket seller counter, etc. Roles may belong to an organization. This element is combined with the Resource Role definition.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Resource
- Organization Unit
- Person
- Information system
- Pool and Lane
- Activities
- Choreography Activities

**Related diagrams**

- Organization Structure Diagram
- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram
- BPMN Resources Usage Matrices

**Related Procedure**

- Using Organization Structure Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Role is a type of contact point or a responsible person, e. g., cashier, ticket seller counter, etc. Roles may belong to an organization. This element is combined with the Resource Role definition.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="role.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Role" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Structure+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Organization Structure Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Resources+Usage+Matrices">BPMN Resources Usage Matrices</a></li></ul><p><strong>Related Procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Organization+Structure+Diagram">Using Organization Structure Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031732 space=CBMP2024x version=1 -->
## PAGE 00170: Script Task

- page_id: `290031732`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031732/Script+Task
- version_number: 1
- version_date: `2026-02-09T13:52:29.031+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A Script Task is executed by a business process engine. A modeler or an implementer defines a script in a language that the engine can interpret. When the task is ready to start, the engine will execute the script. When the script is completed, the task will also be completed.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Script Task is executed by a business process engine. A modeler or an implementer defines a script in a language that the engine can interpret. When the task is ready to start, the engine will execute the script. When the script is completed, the task will also be completed.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="script_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Script Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031722 space=CBMP2024x version=1 -->
## PAGE 00171: Send Task

- page_id: `290031722`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031722/Send+Task
- version_number: 1
- version_date: `2026-02-09T13:51:45.850+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A Send Task is a simple task that is designed to send a message to an external participant. Once the message has been sent, the task is completed.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Send Task is a simple task that is designed to send a message to an external participant. Once the message has been sent, the task is completed.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="send_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Send Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031750 space=CBMP2024x version=1 -->
## PAGE 00172: Sequence Flow

- page_id: `290031750`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031750/Sequence+Flow
- version_number: 1
- version_date: `2026-02-09T13:53:45.512+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A Sequence Flow is used to show the order of flow elements in a process or a choreography.

The source and target of a Sequence Flow must be from a set of the following elements:

- Events (Start, Intermediate, and End events)
- Activities (Task and SubProcess for Processes)
- Choreography Activities (Choreography Task and Sub-Choreography)
- Gateways

A Sequence Flow can optionally define a condition expression indicating that a token will be passed down the Sequence Flow only if the expression is evaluated to be true.

A Condition expression is typically used when the source of a Sequence Flow is a Gateway or an Activity. A conditional outgoing Sequence Flow from an Activity is with a mini-diamond (indicator) at the beginning of the Sequence Flow.

A Conditional Sequence Flow outgoing from a Gateway does not have a mini-diamond at the beginning of the Sequence Flow.

A Sequence Flow, which has an exclusive, inclusive, or complex gateway, or an Activity as its source, can also be defined as a default Sequence Flow. The default Sequence Flow is represented with a backslash.

A default Sequence Flow will be taken (a token is passed) only if all of the other outgoing Sequence Flows from an Activity or Gateway are not valid, meaning that their condition expressions are false.

**Example**

[IMAGE alt='' src='']

###### Sequence Flow between two Tasks

[IMAGE alt='' src='']

###### Conditional Sequence flow

[IMAGE alt='' src='']

###### Default Sequence Flow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Sequence Flow is used to show the order of flow elements in a process or a choreography.</p><p>The source and target of a Sequence Flow must be from a set of the following elements:</p><ul><li>Events (Start, Intermediate, and End events)</li><li>Activities (Task and SubProcess for Processes)</li><li>Choreography Activities (Choreography Task and Sub-Choreography)</li><li>Gateways</li></ul><p>A Sequence Flow can optionally define a condition expression indicating that a token will be passed down the Sequence Flow only if the expression is evaluated to be true.</p><p>A Condition expression is typically used when the source of a Sequence Flow is a Gateway or an Activity. A conditional outgoing Sequence Flow from an Activity is with a mini-diamond (indicator) at the beginning of the Sequence Flow.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7872b605-f067-4888-830e-683ee81b50ef"><ac:rich-text-body><p>A Conditional Sequence Flow outgoing from a Gateway does not have a mini-diamond at the beginning of the Sequence Flow.</p></ac:rich-text-body></ac:structured-macro><p>A Sequence Flow, which has an exclusive, inclusive, or complex gateway, or an Activity as its source, can also be defined as a default Sequence Flow. The default Sequence Flow is represented with a backslash.</p><p>A default Sequence Flow will be taken (a token is passed) only if all of the other outgoing Sequence Flows from an Activity or Gateway are not valid, meaning that their condition expressions are false.</p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="sequence_flow_tasks.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Sequence Flow" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Sequence Flow between two Tasks</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="sequence_flow_condition.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Sequence Flow" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Conditional Sequence flow</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="sequence_flow_default.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Sequence Flow" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172b4d);">Default Sequence Flow</h6><p />
````

<!--NOMAGIC_PAGE id=290031720 space=CBMP2024x version=1 -->
## PAGE 00173: Service Task

- page_id: `290031720`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031720/Service+Task
- version_number: 1
- version_date: `2026-02-09T13:51:37.533+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A Service Task is a task that uses some sort of service, which could be a Web service or an automated application.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Service Task is a task that uses some sort of service, which could be a Web service or an automated application.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="service_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Service Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031833 space=CBMP2024x version=1 -->
## PAGE 00174: Signal Boundary Event

- page_id: `290031833`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031833/Signal+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:19:21.888+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Signal Boundary Event can receive a Signal. In this context, it will change a normal flow into an exception flow upon being triggered.

A Signal Event differs from an Error Event because it defines a more general, non-error condition for interrupting Activities, such as the successful completion of another Activity, and it has a larger scope than the Error Event does.

Signal Boundary Event displays either of the following on a diagram:

- A Signal Boundary Event name if the name is specified.
- A Signal Ref property value if the name is unspecified.

**Notation**

- Signal Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_signal.png']
- Signal Boundary Event (Cancel Activity - False) [ATTACHMENT filename='boundary_event_signal_false.png']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Signal Boundary Event can receive a Signal. In this context, it will change a normal flow into an exception flow upon being triggered.</p><p>A Signal Event differs from an Error Event because it defines a more general, non-error condition for interrupting Activities, such as the successful completion of another Activity, and it has a larger scope than the Error Event does.</p><p>Signal Boundary Event displays either of the following on a diagram:</p><ul><li>A Signal Boundary Event name if the name is specified.</li><li>A Signal Ref property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><ul><li>Signal Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_signal.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Signal Boundary Event" /></ri:attachment></ac:image></li><li>Signal Boundary Event (Cancel Activity - False)<br /><ac:image><ri:attachment ri:filename="boundary_event_signal_false.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Signal Boundary Event" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031794 space=CBMP2024x version=1 -->
## PAGE 00175: Signal Catching Intermediate Event

- page_id: `290031794`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031794/Signal+Catching+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:02:04.984+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Signal Catching Intermediate Event is used to receive a signal.

This event displays either of the following on the diagram:

- A Signal Catching Intermediate Event name if the name is specified.
- A Signal Ref property value if the name is unspecified.

Signals in business process modeling are used for general communications within and across process levels.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Signal Catching Intermediate Event is used to receive a signal.</p><p>This event displays either of the following on the diagram:</p><ul><li>A Signal Catching Intermediate Event name if the name is specified.</li><li>A Signal Ref property value if the name is unspecified.</li></ul><p>Signals in business process modeling are used for general communications within and across process levels.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event_signal.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Signal Catching Intermediate Event" /></ri:attachment></ac:image></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031855 space=CBMP2024x version=1 -->
## PAGE 00176: Signal End Event

- page_id: `290031855`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031855/Signal+End+Event
- version_number: 1
- version_date: `2026-02-09T14:23:38.288+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Signal End Event indicates that a signal will be broadcast when the end has been reached.

This event displays either of the following on a diagram:

- A Signal End Event name if the name is specified.
- A Signal Ref property value if the name is unspecified.

A signal, which is broadcast to any process that can receive it, can be sent across process levels or pools.

**Notation**

[IMAGE alt='' src='']

**Related element**

- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Signal End Event indicates that a signal will be broadcast when the end has been reached.</p><p>This event displays either of the following on a diagram:</p><ul><li>A Signal End Event name if the name is specified.</li><li>A Signal Ref property value if the name is unspecified.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="44fb9c54-7a42-4c3f-99fb-c501a210eecf"><ac:rich-text-body><p>A signal, which is broadcast to any process that can receive it, can be sent across process levels or pools.</p></ac:rich-text-body></ac:structured-macro><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_signal.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Signal End Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031773 space=CBMP2024x version=1 -->
## PAGE 00177: Signal Start Event

- page_id: `290031773`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031773/Signal+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:58:06.465+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Signal Start Event means that a signal, which has been broadcast from another process, has arrived and triggered the start of a process.

A Signal Start Event displays either of the following on a diagram:

- A Signal Start Event name if the name is specified.
- A Signal Ref property value if the name is unspecified.

**Notation**

- Interrupting Signal Start Event [ATTACHMENT filename='start_event_signal_interr.png']
- Non-Interrupting Signal Start Event [ATTACHMENT filename='start_event_signal_noninterr.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Signal Start Event means that a signal, which has been broadcast from another process, has arrived and triggered the start of a process.</p><p>A Signal Start Event displays either of the following on a diagram:</p><ul><li>A Signal Start Event name if the name is specified.</li><li>A Signal Ref property value if the name is unspecified.</li></ul><p><strong>Notation</strong></p><ul><li>Interrupting Signal Start Event<br /><ac:image><ri:attachment ri:filename="start_event_signal_interr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Signal Start Event" /></ri:attachment></ac:image></li><li>Non-Interrupting Signal Start Event<br /><ac:image><ri:attachment ri:filename="start_event_signal_noninterr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Signal Start Event" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031805 space=CBMP2024x version=1 -->
## PAGE 00178: Signal Throwing Intermediate Event

- page_id: `290031805`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031805/Signal+Throwing+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:12:10.381+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Throwing Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Signal Throwing Intermediate Event is used to send a signal.

This event displays either of the following on a diagram:

- A Signal Throwing Intermediate Event name if the name is specified.
- A Signal Ref property value if the name is unspecified.

**Notation** 
[IMAGE alt='' src='']

**Related element**

- Intermediate Throwing Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Signal Throwing Intermediate Event is used to send a signal.</p><p>This event displays either of the following on a diagram:</p><ul><li>A Signal Throwing Intermediate Event name if the name is specified.</li><li>A Signal Ref property value if the name is unspecified.</li></ul><p><strong>Notation</strong><br /><ac:image><ri:attachment ri:filename="intermediate_throwing_event_signal.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Signal Throwing Intermediate Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Throwing+Event">Intermediate Throwing Event</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031754 space=CBMP2024x version=1 -->
## PAGE 00179: Start Events

- page_id: `290031754`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031754/Start+Events
- version_number: 1
- version_date: `2026-02-09T13:53:52.429+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

A Start Event indicates where a particular process starts. In terms of sequence flows, a Start Event starts the flow of a process, and thus cannot have any incoming sequence flows.

When a Start Event is owned by an Event SubProcess, it can be:

- Interrupting. The Start Event interrupts the process contained in the Event SubProcess. The Interrupting Message Start Event is drawn with a solid border.
- Non-Interrupting. The Start Event does not interrupt the process contained in the Event SubProcess and starts parallel flow. The Interrupting Message Start Event is drawn with a dashed border.

Types of Start Events are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Start Event indicates where a particular process starts. In terms of sequence flows, a Start Event starts the flow of a process, and thus cannot have any incoming sequence flows.</p><p>When a Start Event is owned by an Event SubProcess, it can be:</p><ul><li>Interrupting. The Start Event interrupts the process contained in the Event SubProcess. The Interrupting Message Start Event is drawn with a solid border.</li><li>Non-Interrupting. The Start Event does not interrupt the process contained in the Event SubProcess and starts parallel flow. The Interrupting Message Start Event is drawn with a dashed border.</li></ul><p>Types of Start Events are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e0eded90-dc2f-47bd-a07b-f136f915e6d7" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031968 space=CBMP2024x version=1 -->
## PAGE 00180: Strategy

- page_id: `290031968`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031968/Strategy
- version_number: 1
- version_date: `2026-02-09T14:56:14.040+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Means Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Strategy is one component of the plan for the Mission. A Strategy represents the essential Course of Action to achieve Ends (Goals in particular). A Strategy usually channels efforts towards those Goals.

A Strategy is more than simply a resource, skill, or competency that the enterprise can call upon. It is accepted by the enterprise as the right approach to achieve its Goals, given the environmental constraints and risks.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Means Concepts
- Mean Concept Relationships

**Related diagrams**

- Business Motivation Diagram
- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Strategy is one component of the plan for the Mission. A Strategy represents the essential Course of Action to achieve Ends (Goals in particular). A Strategy usually channels efforts towards those Goals.</p><p>A Strategy is more than simply a resource, skill, or competency that the enterprise can call upon. It is accepted by the enterprise as the right approach to achieve its Goals, given the environmental constraints and risks.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="strategy.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Strategy" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Means+Concepts">Means Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Mean+Concept+Relationships">Mean Concept Relationships</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031932 space=CBMP2024x version=1 -->
## PAGE 00181: SubChoreography

- page_id: `290031932`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031932/SubChoreography
- version_number: 1
- version_date: `2026-02-09T14:47:51.546+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Choreography Diagram > Choreography Activities
- labels: []

### NORMALIZED CONTENT

**Description**

A SubChoreography is a compound Activity that can include choreography activities and define their flows. It can be expanded to show its details within the choreography in which it is contained.

It can also be displayed in a collapsed view to hide its details. A collapsed SubChoreography is indicated with a plus sign (+) to distinguish itself from a Choreography Task.

**Notation**

**[IMAGE alt='' src='']**

**Example**

[IMAGE alt='' src='']

###### Expanded SubChoreography.

****

**Related elements**

- Organization Unit
- Role
- Person
- Choreography Activities

**Related diagram**

- BPMN Choreography Diagram

**Related procedures**

- Creating SubChoreography
- Using Choreography Activity

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A SubChoreography is a compound Activity that can include choreography activities and define their flows. It can be expanded to show its details within the choreography in which it is contained.</p><p>It can also be displayed in a collapsed view to hide its details. A collapsed SubChoreography is indicated with a plus sign (+) to distinguish itself from a Choreography Task.</p><p><strong>Notation</strong></p><p><strong><ac:image><ri:attachment ri:filename="choreography_subprocess.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="SubChoreography" /></ri:attachment></ac:image><br /></strong></p><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="choreography_subprocess_expanded.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="SubChoreography" /></ri:attachment></ac:image></p><h6 style="letter-spacing: normal;line-height: 1.66667;text-align: center;color:var(--ds-text,#172B4D);">Expanded SubChoreography.</h6><p><strong> </strong></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+SubChoreography">Creating SubChoreography</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Choreography+Activity" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using Choreography Activity</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031910 space=CBMP2024x version=1 -->
## PAGE 00182: SubConversation

- page_id: `290031910`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031910/SubConversation
- version_number: 1
- version_date: `2026-02-09T14:42:21.447+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Collaboration Diagram
- labels: []

### NORMALIZED CONTENT

**Description**

A SubConversation is a conversation node considered as a hierarchical division within a parent’s conversation.

A SubConversation is represented as a graphical object within a BPMN Conversation diagram, but it can also be opened up to show a lower-level conversation, which consists of message flows, communications, and/or other SubConversations. A SubConversation shares the participants of its parent conversation.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Pool and Lane
- Conversation Link
- Conversation

**Related diagrams**

- BPMN Collaboration Diagram
- BPMN Process Diagram

**Related procedure**

- Creating and Using Conversation Nodes

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A SubConversation is a conversation node considered as a hierarchical division within a parent’s conversation.</p><p>A SubConversation is represented as a graphical object within a BPMN Conversation diagram, but it can also be opened up to show a lower-level conversation, which consists of message flows, communications, and/or other SubConversations. A SubConversation shares the participants of its parent conversation.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="subconversation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="SubConversation" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Pool+and+Lane" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Pool and Lane</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Conversation+Link">Conversation Link</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Conversation" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Conversation</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Conversation+Nodes">Creating and Using Conversation Nodes</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031735 space=CBMP2024x version=1 -->
## PAGE 00183: SubProcess

- page_id: `290031735`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031735/SubProcess
- version_number: 1
- version_date: `2026-02-09T13:52:49.259+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > SubProcesses
- labels: []

### NORMALIZED CONTENT

**Description**

A SubProcess is used to create a context for an exception handling that applies to a group of activities.

A collapsed SubProcess can be used as a mechanism to show a compact and less clutter group of parallel activities.

**Notation**

- Expanded SubProcess [ATTACHMENT filename='expanded_subprocess.png']
- Collapsed SubProcess [ATTACHMENT filename='suppressed_subproces.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A SubProcess is used to create a context for an exception handling that applies to a group of activities.</p><p>A collapsed SubProcess can be used as a mechanism to show a compact and less clutter group of parallel activities.</p><p><strong>Notation</strong></p><ul><li>Expanded SubProcess<br /><ac:image><ri:attachment ri:filename="expanded_subprocess.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="SubProcess" /></ri:attachment></ac:image></li><li>Collapsed SubProcess<br /><ac:image><ri:attachment ri:filename="suppressed_subproces.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="SubProcess" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031734 space=CBMP2024x version=1 -->
## PAGE 00184: SubProcesses

- page_id: `290031734`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031734/SubProcesses
- version_number: 1
- version_date: `2026-02-09T13:52:35.474+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities
- labels: []

### NORMALIZED CONTENT

A SubProcess is an Activity whose internal details have been modeled using activities, gateways, events, and sequence flows. A SubProcess is a graphical object within a process. It can be “opened up” to show a lower-level process. SubProcesses define a contextual scope that can be used for attribute visibility and a transactional scope for the handling exceptions of Events or for compensation.

A collapsed view of a SubProcess hides its details while an expanded view shows its content. A collapsed SubProcess uses a plus sign (+) to distinguish itself from a Task.

Different types of SubProcesses used in business process modeling are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A SubProcess is an Activity whose internal details have been modeled using activities, gateways, events, and sequence flows. A SubProcess is a graphical object within a process. It can be “opened up” to show a lower-level process. SubProcesses define a contextual scope that can be used for attribute visibility and a transactional scope for the handling exceptions of Events or for compensation.</p><p>A collapsed view of a SubProcess hides its details while an expanded view shows its content. A collapsed SubProcess uses a plus sign (+) to distinguish itself from a Task.</p><p>Different types of SubProcesses used in business process modeling are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3f003f43-fa1f-4983-b358-1d382c2b0c77" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031684 space=CBMP2024x version=1 -->
## PAGE 00185: Supportive diagrams

- page_id: `290031684`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031684/Supportive+diagrams
- version_number: 1
- version_date: `2026-02-09T13:47:41.445+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Getting Started > Introducing Main Concepts
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler also supports diagrams that allow for specifying additional information about business model.

The following diagrams are supported:

- [CONFLUENCE_PAGE title='Process Definition Diagram' space='CBMP2024x']
- [CONFLUENCE_PAGE title='Business Data Diagram' space='CBMP2024x']
- [CONFLUENCE_PAGE title='Organization Structure Diagram' space='CBMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler also supports diagrams that allow for specifying additional information about business model.</p><p>The following diagrams are supported:</p><ul><li><ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Process Definition Diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Business Data Diagram" /></ac:link></li><li><ac:link><ri:page ri:space-key="CBMP2024x" ri:content-title="Organization Structure Diagram" /></ac:link></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031952 space=CBMP2024x version=1 -->
## PAGE 00186: Supportive Diagrams Concepts

- page_id: `290031952`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031952/Supportive+Diagrams+Concepts
- version_number: 1
- version_date: `2026-02-09T14:53:15.878+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

This chapter describes how to create and modify supportive diagrams, BPMN Matrices, Tables, and Process Structure Map.

The chapter contains the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter describes how to create and modify supportive diagrams, BPMN Matrices, Tables, and Process Structure Map.</p><p>The chapter contains the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e8edfcf5-ef77-40f3-b3a5-73ac73aedb6a" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031685 space=CBMP2024x version=1 -->
## PAGE 00187: Switching to Business Modeling Perspectives

- page_id: `290031685`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031685/Switching+to+Business+Modeling+Perspectives
- version_number: 1
- version_date: `2026-02-09T13:47:47.482+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Getting Started
- labels: []

### NORMALIZED CONTENT

The business modeling perspectives are dedicated to business process modelers. The perspectives offer a simplified user interface by showing the features that are relevant to business process modeling and hiding the others that are not.

Business Modeler offers two business modeling perspectives. They are as follow:

- Business Analyst perspective that provides set of most often used elements of BPMN standard.
- Business Architect perspective that provides all BPMN elements

To switch to the Business Architect or Business Analyst perspective

1. From the main menu, click Options > Perspectives > Perspectives . The Select Perspectives dialog will open.
2. Select Business Analyst or Business Architect appropriately and click Apply .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The business modeling perspectives are dedicated to business process modelers. The perspectives offer a simplified user interface by showing the features that are relevant to business process modeling and hiding the others that are not.</p><p>Business Modeler offers two business modeling perspectives. They are as follow:</p><ul><li data-uuid="8c4a94a7-e0b6-4cce-8371-0e4fe6182cc7">Business Analyst perspective that provides set of most often used elements of BPMN standard.</li><li data-uuid="065f5b30-e48a-4800-a37f-b6d58650aaac">Business Architect perspective that provides all BPMN elements</li></ul><p>To switch to the Business Architect or Business Analyst perspective</p><hr /><ol><li data-uuid="175b464a-3ec1-47a0-a0ae-aa315a6cb34f">From the main menu, click <strong>Options</strong> &gt; <strong>Perspectives</strong> &gt; <strong>Perspectives</strong>. The <strong>Select Perspectives</strong> dialog will open.</li><li data-uuid="121128a6-21ee-4194-9863-647b484ab28d">Select <strong>Business Analyst</strong> or <strong>Business Architect</strong> appropriately and click <strong>Apply</strong>.</li></ol>
````

<!--NOMAGIC_PAGE id=290031970 space=CBMP2024x version=1 -->
## PAGE 00188: Tactic

- page_id: `290031970`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031970/Tactic
- version_number: 1
- version_date: `2026-02-09T14:56:35.941+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Means Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A Tactic is a Course of Action that represents part of the detailing of Strategies. A Tactic implements Strategies. For example, the Tactic “Call first-time customers personally” implements the Strategy “Increase repeat business.”

Tactics generally channel efforts towards Objectives. For example, the Tactic “Ship products for free” channels efforts towards the Objective “Within six months, 10% increase in product sales”.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Means Concepts
- Mean Concept Relationships

**Related diagrams**

- Business Motivation Diagram
- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Tactic is a Course of Action that represents part of the detailing of Strategies. A Tactic implements Strategies. For example, the Tactic “Call first-time customers personally” implements the Strategy “Increase repeat business.”</p><p>Tactics generally channel efforts towards Objectives. For example, the Tactic “Ship products for free” channels efforts towards the Objective “Within six months, 10% increase in product sales”.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="tactic.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Tactic" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Means+Concepts">Means Concepts</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Mean+Concept+Relationships">Mean Concept Relationships</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031718 space=CBMP2024x version=1 -->
## PAGE 00189: Task

- page_id: `290031718`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031718/Task
- version_number: 1
- version_date: `2026-02-09T13:51:29.132+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A Task that has no specified behavior defined.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Task that has no specified behavior defined.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290031717 space=CBMP2024x version=1 -->
## PAGE 00190: Tasks

- page_id: `290031717`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031717/Tasks
- version_number: 1
- version_date: `2026-02-09T13:51:19.238+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities
- labels: []

### NORMALIZED CONTENT

A Task is an atomic Activity within a process flow. A Task is used when the work in a process cannot be broken down into finer levels of detail. Generally, an end-user and/or application are used to perform the task when it is executed. Types of Tasks used in business process modeling are as follows:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Task is an atomic Activity within a process flow. A Task is used when the work in a process cannot be broken down into finer levels of detail. Generally, an end-user and/or application are used to perform the task when it is executed. Types of Tasks used in business process modeling are as follows:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="6201b7eb-e881-4ca0-84d8-eece51b379bd" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=290031857 space=CBMP2024x version=1 -->
## PAGE 00191: Terminate End Event

- page_id: `290031857`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031857/Terminate+End+Event
- version_number: 1
- version_date: `2026-02-09T14:24:03.221+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > End Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Terminate End Event indicates that all activities in a process have to be immediately ended, including all the instances of multi-instance activities. The process will be ended without any compensation or event handling.

**Notation**

[IMAGE alt='' src='']

**Related element**

- End Events

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Terminate End Event indicates that all activities in a process have to be immediately ended, including all the instances of multi-instance activities. The process will be ended without any compensation or event handling.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="end_event_terminate.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Terminate End Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Events" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Events</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031696 space=CBMP2024x version=1 -->
## PAGE 00192: Text Annotation

- page_id: `290031696`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031696/Text+Annotation
- version_number: 1
- version_date: `2026-02-09T13:48:36.394+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > Common BPMN Elements > Artifacts
- labels: []

### NORMALIZED CONTENT

**Description**

A Text Annotation allows a modeler to provide additional information about elements for the reader of a BPMN diagram.

**Example**

****[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Text Annotation allows a modeler to provide additional information about elements for the reader of a BPMN diagram.</p><p><strong>Example</strong></p><p><strong><br /></strong><ac:image><ri:attachment ri:filename="text_annotation.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Text Annotation" /></ri:attachment></ac:image></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290031818 space=CBMP2024x version=1 -->
## PAGE 00193: Timer Boundary Event

- page_id: `290031818`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031818/Timer+Boundary+Event
- version_number: 1
- version_date: `2026-02-09T14:16:36.875+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Boundary Events
- labels: []

### NORMALIZED CONTENT

**Description**

A Timer Boundary Event, which is attached to the boundary of an Activity, change a normal flow into an exception flow upon being triggered. A particular time-date or cycle, for example, on Mondays at 9 A.M., can be specified to trigger a Timer Boundary Event.

A Timer Boundary Event displays any of the following on a diagram:

- A Timer Boundary Event name if the name is specified.
- A Time Cycle property name if the name is unspecified.
- A Time Date property if the name and Time Cycle are unspecified.

**Notation**

- Timer Boundary Event (Cancel Activity - True) [ATTACHMENT filename='boundary_event_timer.png']
- Timer Boundary Event (Cancel Activity - False) [ATTACHMENT filename='boundary_event_timer_false.png']

**Related elements**

- Boundary Events
- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Timer Boundary Event, which is attached to the boundary of an Activity, change a normal flow into an exception flow upon being triggered. A particular time-date or cycle, for example, on Mondays at 9 A.M., can be specified to trigger a Timer Boundary Event.</p><p>A Timer Boundary Event displays any of the following on a diagram:</p><ul><li>A Timer Boundary Event name if the name is specified.</li><li>A Time Cycle property name if the name is unspecified.</li><li>A Time Date property if the name and Time Cycle are unspecified.</li></ul><p><strong>Notation</strong></p><ul><li>Timer Boundary Event (Cancel Activity - True)<br /><ac:image><ri:attachment ri:filename="boundary_event_timer.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Timer Boundary Event" /></ri:attachment></ac:image></li><li>Timer Boundary Event (Cancel Activity - False)<br /><ac:image><ri:attachment ri:filename="boundary_event_timer_false.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Timer Boundary Event" /></ri:attachment></ac:image></li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Boundary+Events">Boundary Events</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031787 space=CBMP2024x version=1 -->
## PAGE 00194: Timer Catching Intermediate Event

- page_id: `290031787`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031787/Timer+Catching+Intermediate+Event
- version_number: 1
- version_date: `2026-02-09T14:00:27.922+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Intermediate Catch Event
- labels: []

### NORMALIZED CONTENT

**Description**

A Timer Catching Intermediate Event acts as a delay mechanism based on a particular time and date, or cycle, for example, on Mondays at 9 A.M.

This Event displays any of the following on a diagram:

- A Timer Catching Intermediate Event name if the name is specified.
- A Time Cycle property name if the name is unspecified.
- A Time Date property if the name and Time Cycle are unspecified.

**Notation**

[IMAGE alt='' src='']

**Related element**

- Intermediate Catch Event

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedure**

- Creating and Using an Event

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p style="margin-top: 0.0px;"><strong>Description</strong></p><p>A Timer Catching Intermediate Event acts as a delay mechanism based on a particular time and date, or cycle, for example, on Mondays at 9 A.M.</p><p>This Event displays any of the following on a diagram:</p><ul><li>A Timer Catching Intermediate Event name if the name is specified.</li><li>A Time Cycle property name if the name is unspecified.</li><li>A Time Date property if the name and Time Cycle are unspecified.</li></ul><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="intermediate_catch_event_timer.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Timer Catching Intermediate Event" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li class="ancestor-link parent-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Intermediate+Catch+Event">Intermediate Catch Event</a></li></ul><p class="ancestor-link parent-link"><strong>Related diagrams</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li></ul><p><br /></p><p />
````

<!--NOMAGIC_PAGE id=290031760 space=CBMP2024x version=1 -->
## PAGE 00195: Timer Start Event

- page_id: `290031760`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031760/Timer+Start+Event
- version_number: 1
- version_date: `2026-02-09T13:54:23.372+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Start Events
- labels: []

### NORMALIZED CONTENT

Description

A Timer Start Event allows a particular time and date or cycle setting, for example, on Mondays at 9 A.M., to trigger the start of a process.

A Timer Start Event displays any of the following on a diagram:

- A Timer Start Event name if the name is specified.
- A Time Cycle property name if the name is unspecified.
- A Time Date property if the name and Time Cycle are unspecified.

Notation

- Interrupting Timer Start Event [ATTACHMENT filename='start_event_timer_interr.png']
- Non-interrupting Timer Start Event [ATTACHMENT filename='start_event_timer_noninterr.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Description</p><p>A Timer Start Event allows a particular time and date or cycle setting, for example, on Mondays at 9 A.M., to trigger the start of a process.</p><p>A Timer Start Event displays any of the following on a diagram:</p><ul><li>A Timer Start Event name if the name is specified.</li><li>A Time Cycle property name if the name is unspecified.</li><li>A Time Date property if the name and Time Cycle are unspecified.</li></ul><p>Notation</p><ul><li>Interrupting Timer Start Event<br /><ac:image><ri:attachment ri:filename="start_event_timer_interr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Timer Start Event" /></ri:attachment></ac:image></li><li>Non-interrupting Timer Start Event<br /><ac:image><ri:attachment ri:filename="start_event_timer_noninterr.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Timer Start Event" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290031745 space=CBMP2024x version=1 -->
## PAGE 00196: Transaction

- page_id: `290031745`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031745/Transaction
- version_number: 1
- version_date: `2026-02-09T13:53:21.319+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > SubProcesses
- labels: []

### NORMALIZED CONTENT

**Description**

A Transaction is a specialized type of SubProcess whose special behavior is controlled through a transaction protocol (such as WS-Transaction).

**Notation**

- Expanded [ATTACHMENT filename='transaction.png']
- Collapsed [ATTACHMENT filename='transaction_suppressed.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Transaction is a specialized type of SubProcess whose special behavior is controlled through a transaction protocol (such as WS-Transaction).</p><p><strong>Notation</strong></p><ul><li>Expanded<br /><ac:image><ri:attachment ri:filename="transaction.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Transaction" /></ri:attachment></ac:image></li><li>Collapsed<br /><ac:image><ri:attachment ri:filename="transaction_suppressed.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Transaction" /></ri:attachment></ac:image></li></ul><p />
````

<!--NOMAGIC_PAGE id=290032035 space=CBMP2024x version=1 -->
## PAGE 00197: Usage

- page_id: `290032035`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032035/Usage
- version_number: 1
- version_date: `2026-02-09T15:36:30.105+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Process Definition Diagram > BPMNRelationships
- labels: []

### NORMALIZED CONTENT

**Description**

A Usage is a BPMNRelationship in which one element requires another element (or set of elements) for its full implementation or operation.

**Example**

[IMAGE alt='' src='']

**Related element**

- BPMN Process

**Related diagram**

- Process Definition Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A Usage is a BPMNRelationship in which one element requires another element (or set of elements) for its full implementation or operation.</p><p><strong>Example</strong></p><p><ac:image><ri:attachment ri:filename="use.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Usage" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process">BPMN Process</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Process+Definition+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Process Definition Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031679 space=CBMP2024x version=1 -->
## PAGE 00198: User Guide

- page_id: `290031679`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031679/User+Guide
- version_number: 1
- version_date: `2026-02-09T13:47:08.343+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation
- labels: []

### NORMALIZED CONTENT

The User Guide section introduces Cameo Business Modeler Plugin and then defines the main Business Process Model and Notation (BPMN) concepts, including the common BPMN elements and diagram types, and the most relevant Supportive Diagrams concepts. In addition, it presents information about the main Cameo Business Modeler Plugin features and their performance. Finally, the section describes Validation Rules the tool applies automatically.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The User Guide section introduces Cameo Business Modeler Plugin and then defines the main Business Process Model and Notation (BPMN) concepts, including the common BPMN elements and diagram types, and the most relevant Supportive Diagrams concepts. In addition, it presents information about the main Cameo Business Modeler Plugin features and their performance. Finally, the section describes Validation Rules the tool applies automatically. </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="1b7b88cf-59c6-4b9e-af3e-5ac207c460d8" /></p>
````

<!--NOMAGIC_PAGE id=290031726 space=CBMP2024x version=1 -->
## PAGE 00199: User Task

- page_id: `290031726`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031726/User+Task
- version_number: 1
- version_date: `2026-02-09T13:52:04.312+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts > BPMN Process Diagram > Activities > Tasks
- labels: []

### NORMALIZED CONTENT

**Description**

A User Task is a typical workflow task where a human performer performs the task with the assistance of software and is scheduled through a task list manager of some sort.

**Notation**

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A User Task is a typical workflow task where a human performer performs the task with the assistance of software and is scheduled through a task list manager of some sort.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="user_task.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="User Task" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=290032069 space=CBMP2024x version=1 -->
## PAGE 00200: Using Activities

- page_id: `290032069`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032069/Using+Activities
- version_number: 1
- version_date: `2026-02-09T15:50:11.645+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Process Diagram
- labels: []

### NORMALIZED CONTENT

This section will describe how to use Activities in a BPMN process diagram. Activities (Tasks, Subprocesses, and Call Activities) can have the following specific markers displayed on their shapes:

- Compensation
- Standard loop
- MultiInstance loop (parallel)
- MultiInstance loop (sequential)

To add a Compensation marker to an Activity, do one of the following

- Right-click an Activity and select Is For Compensation .
- Open the Activity Specification window. Click to clear the Is For Compensation check box and click Close .

To add a Loop marker to an Activity

- Right-click an Activity and click to select Standard Loop or MultiInstance Loop .

To display a MultiInstance Loop (sequential) marker on a MultiInstance Loop activity, do one of the following

- Right-click an Activity with a MultiInstance Loop (parallel) marker and on the shortcut menu select Is Sequential .
- Open the Activity with a MultiInstance marker Specification window. Select Is Sequential and click Close .

To convert an Activity to another type of Activity

- Right-click a Task, SubProcess, or Call Activity and from the shortcut menu select Refactor > Convert To and then select an Activity type to which you need to convert the selected Activity.

To display Resources assigned for Activities

- Right-click the diagram pane and then do one of the following:
- On the shortcut menu, click to select the Show Assigned Resources check box (see the following figure).
- From the shortcut menu, select Diagram Properties and in the open dialog, set the Show Assigned Resources property value to true.

**Related element**

- Activities

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Tasks
- Creating and Using SubProcesses
- Creating and Using an Event
- Creating and Using a Sequence Flow
- Creating and Using Data Items
- Using Common BPMN Elements
- Navigation Between BPMN Diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section will describe how to use Activities in a BPMN process diagram. Activities (Tasks, Subprocesses, and Call Activities) can have the following specific markers displayed on their shapes:</p><ul><li>Compensation</li><li>Standard loop</li><li>MultiInstance loop (parallel)</li><li>MultiInstance loop (sequential)</li></ul><p><br /></p><p>To add a Compensation marker to an Activity, do one of the following</p><hr style="" /><ul><li>Right-click an Activity and select <strong>Is For Compensation</strong>.</li><li>Open the Activity Specification window. Click to clear the <strong>Is For Compensation</strong> check box and click <strong>Close</strong>.</li></ul><p><br /></p><p>To add a Loop marker to an Activity</p><hr style="" /><ul><li>Right-click an Activity and click to select <strong>Standard Loop</strong> or <strong>MultiInstance Loop</strong>.</li></ul><p><br /></p><p>To display a MultiInstance Loop (sequential) marker on a MultiInstance Loop activity, do one of the following</p><hr style="" /><ul><li>Right-click an Activity with a MultiInstance Loop (parallel) marker and on the shortcut menu select <strong>Is Sequential</strong>.</li><li>Open the Activity with a MultiInstance marker Specification window. Select <strong>Is Sequential</strong> and click <strong>Close</strong>.</li></ul><p><br /></p><p>To convert an Activity to another type of Activity</p><hr style="" /><ul><li>Right-click a Task, SubProcess, or Call Activity and from the shortcut menu select <strong>Refactor</strong> &gt; <strong>Convert To</strong> and then select an Activity type to which you need to convert the selected Activity.</li></ul><p><br /></p><p>To display Resources assigned for Activities</p><hr style="" /><ul><li>Right-click the diagram pane and then do one of the following:</li><li>On the shortcut menu, click to select the <strong>Show Assigned Resources</strong> check box (see the following figure).</li><li>From the shortcut menu, select <strong>Diagram Properties</strong> and in the open dialog, set the <strong>Show Assigned Resources</strong> property value to true.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Activities">Activities</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Tasks" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Tasks</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+SubProcesses" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using SubProcesses</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+an+Event">Creating and Using an Event</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+a+Sequence+Flow">Creating and Using a Sequence Flow</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Data+Items" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Data Items</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Common+BPMN+Elements">Using Common BPMN Elements</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Navigation+Between+BPMN+Diagrams">Navigation Between BPMN Diagrams</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032084 space=CBMP2024x version=1 -->
## PAGE 00201: Using BPMN Choreography Diagram

- page_id: `290032084`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032084/Using+BPMN+Choreography+Diagram
- version_number: 1
- version_date: `2026-02-09T15:58:42.046+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

The following sections describe how to create and specify a a BPMN Choreography diagram:

**Related procedures**

- Creating a Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The following sections describe how to create and specify a a BPMN Choreography diagram:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="08e5b0e9-adaf-4562-a883-7f0eaca80979" /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032079 space=CBMP2024x version=1 -->
## PAGE 00202: Using BPMN Collaboration Diagram

- page_id: `290032079`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032079/Using+BPMN+Collaboration+Diagram
- version_number: 1
- version_date: `2026-02-09T15:55:18.143+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

A BPMN Collaboration diagram can contain the elementsfrom a Process diagram.

How to create and specify a BPMN Collaboration diagram describes the following sections:

**Related procedure**

- Creating a Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="859dc7b8-a45f-4be6-aea0-e603a5de7ab1"><ac:rich-text-body>A BPMN Collaboration diagram can contain the elementsfrom a Process diagram.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>How to create and specify a BPMN Collaboration diagram describes the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3c51b5c3-c8bb-4d00-ad85-ed6fc80cb498" /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032093 space=CBMP2024x version=1 -->
## PAGE 00203: Using BPMN Element Numbers

- page_id: `290032093`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032093/Using+BPMN+Element+Numbers
- version_number: 1
- version_date: `2026-02-09T16:03:12.091+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

Most BPMN elements can have specified their IDs. Element ID is automatically created for BPMN Process, Collaboration, and Choreography diagram flow elements and conversations. The element IDs are displayed (in gray) in the following places:

- On a diagram. The ID is displayed above or before the name of element.
- In the Model Browser. The ID is displayed in front of the name of element.
- In the Specification window. The ID is below the Name property.

Automatic elements numbering is turned off in all the projects that are created usingBPMN2 Project and BPMN-SoaML Project templates.

To specify or change a BPMN element’s ID manually

1. Open the Specification window of the element.
2. Type a number in the Id property value box.

To turn on/off automatic elements numbering in a project

1. On the main menu, click Options > Project .
2. In the Project Options dialog, click General project options in the options list on the left.
3. Click to clear the Use Element Auto-numbering check box.
4. Click OK .

To hide an element Id on a diagram

- Right-click the diagram pane and then do one of the following:
  - On the shortcut menu clear the Show Elements Id .
  - From the shortcut menu, select Diagram Properties . Clear the Show Elements Id check box.

To hide element numbers in the Containment tree

1. On the main menu, click Options > Project .
2. In the Project Options dialog, click General project options in the options list on the left.
3. Click to clear the Display Element Number check box.
4. Click OK .

To edit elements numbering

1. Right-click an element on the BPMN2 diagram and select Element Numbering from the shortcut menu. The Element Numberin g dialog opens.
2. Change elements numbers into desired ones at the right side in this dialog.
3. Click OK .

To change displayed numbering style for element symbols on a diagram

1. Right-click an element on the BPMN2 diagram and select Symbol(s) Properties .
2. In the Symbol Properties dialog, select the Element Number Display Mode property value from the drop-down list.
3. Select the Show Number Tag Name check box to show prefix id = before an element number.

**Related element**

- Numbering Elements

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related external resource**

- Generic numbering mechanism
- Creating Numbering Customizations

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="margin-top: 10.0px;">Most BPMN elements can have specified their IDs. Element ID is automatically created for BPMN Process, Collaboration, and Choreography diagram flow elements and conversations. The element IDs are displayed (in gray) in the following places:</p><ul><li>On a diagram. The ID is displayed above or before the name of element.</li><li>In the Model Browser. The ID is displayed in front of the name of element.</li><li>In the Specification window. The ID is below the Name property.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a635569-e049-46c1-bb41-a282ef3dc507"><ac:rich-text-body>Automatic elements numbering is turned off in all the projects that are created usingBPMN2 Project and BPMN-SoaML Project templates.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To specify or change a BPMN element’s ID manually</p><hr style="" /><ol><li>Open the Specification window of the element.</li><li>Type a number in the <strong>Id</strong> property value box.</li></ol><p><br /></p><p>To turn on/off automatic elements numbering in a project</p><hr style="" /><ol><li>On the main menu, click <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong> dialog, click <strong>General</strong> project options in the options list on the left.</li><li>Click to clear the <strong>Use Element Auto-numbering</strong> check box.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To hide an element Id on a diagram</p><hr style="" /><ul><li>Right-click the diagram pane and then do one of the following:<ul><li>On the shortcut menu clear the <strong>Show Elements Id</strong>.</li><li>From the shortcut menu, select <strong>Diagram Properties</strong>. Clear the <strong>Show Elements Id</strong> check box.</li></ul></li></ul><p><br /></p><p>To hide element numbers in the Containment tree</p><hr style="" /><ol><li>On the main menu, click <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong> dialog, click <strong>General</strong> project options in the options list on the left.</li><li>Click to clear the <strong>Display Element Number</strong> check box.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To edit elements numbering</p><hr style="" /><ol><li>Right-click an element on the BPMN2 diagram and select <strong>Element Numbering</strong> from the shortcut menu. The<strong> Element Numberin</strong>g dialog opens.</li><li>Change elements numbers into desired ones at the right side in this dialog.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To change displayed numbering style for element symbols on a diagram</p><hr style="" /><ol><li>Right-click an element on the BPMN2 diagram and select <strong>Symbol(s) Properties</strong>.</li><li>In the <strong>Symbol Properties</strong> dialog, select the <strong>Element Number Display Mode</strong> property value from the drop-down list.</li><li>Select the <strong>Show Number Tag Name</strong> check box to show prefix id = before an element number.</li></ol><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Numbering+Elements">Numbering Elements</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related external resource</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Generic+numbering+mechanism">Generic numbering mechanism</a></li><li><a href="https://docs.nomagic.com/display/MD2024xR1/Creating+Numbering+Customizations" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating Numbering Customizations</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032066 space=CBMP2024x version=1 -->
## PAGE 00204: Using BPMN Process Diagram

- page_id: `290032066`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032066/Using+BPMN+Process+Diagram
- version_number: 1
- version_date: `2026-02-09T15:48:40.353+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

A BPMN Process diagram can also contain the elements of a BPMN Collaboration diagram.

The following sections describe how to create and specify a BPMN Process diagram:

**Related procedure**

- Creating a Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2408862a-2072-4150-9ee3-8982d8c4c7aa"><ac:rich-text-body><p>A BPMN Process diagram can also contain the elements of a BPMN Collaboration diagram.</p></ac:rich-text-body></ac:structured-macro><p style="margin-top: 0.0px;">The following sections describe how to create and specify a BPMN Process diagram:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="3f51e40b-5905-4142-9a32-29263130f32c" /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032089 space=CBMP2024x version=1 -->
## PAGE 00205: Using BPMN Tables and Matrices

- page_id: `290032089`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032089/Using+BPMN+Tables+and+Matrices
- version_number: 1
- version_date: `2026-02-09T16:01:05.081+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

The following sections describe how to create and use a BPMN tables and matrices:

**Related procedure**

- Creating a Diagram
- Metric table
- Generic table
- Dependency Matrix

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p><p style="margin-top: 0.0px;">The following sections describe how to create and use a BPMN tables and matrices:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="ab0c9ff5-02c2-4103-8329-f40c621f58b4" /></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Metric+table">Metric table</a></li><li><a href="https://docs.nomagic.com/display/MD2024xR1/Generic+table" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Generic table</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Dependency+Matrix">Dependency Matrix</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032063 space=CBMP2024x version=1 -->
## PAGE 00206: Using Cameo Business Modeler Plugin

- page_id: `290032063`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032063/Using+Cameo+Business+Modeler+Plugin
- version_number: 1
- version_date: `2026-02-09T15:47:46.250+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

This chapter presents and explains the main procedures of Cameo Business Modeler Plugin and contains the following sections:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This chapter presents and explains the main procedures of Cameo Business Modeler Plugin and contains the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e0ce7a24-1f00-4934-a79a-9677a267d423" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=290032085 space=CBMP2024x version=1 -->
## PAGE 00207: Using Choreography Activity

- page_id: `290032085`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032085/Using+Choreography+Activity
- version_number: 1
- version_date: `2026-02-09T15:59:07.625+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin > Using BPMN Choreography Diagram
- labels: []

### NORMALIZED CONTENT

This section describes how to create and model choreography activities in a BPMN Choreography diagram. You can specify a list of Participants in a Choreography Activity from

- Specification window
- Smart Manipulator toolbar
- Drag-and-drop operation

To specify a list of Participants from the Specification window

1. Do one of the following:
  - Select the Choreography Activity on the diagram pane and on the Smart Manipulator toolbar, click the Participants button.
  - Open the Specification window, click the Participants property value cell and then click ... button.
2. In the open Select Recourse dialog, select Resources.
3. Click OK .

You need to specify at least two Participants for a Choreography Activity.

The MultiInstance Participants on a Choreography shape will be displayed with a MultiInstance marker in the Participants’ compartment.

To specify a list of participants from the drag-and-drop action

- Drag a Resource from the Containment tree to a Choreography Activity on diagram pane.

- Hold down Shift to select multiple elements that are grouped together.
- Hold down Ctrl to select multiple elements that are not grouped together.

To specify an Initiating Participant in a Choreography Activity

Initiating Participant

1. Open the Choreography Activity Specification window.
2. Click the Initiating Participant property value cell and select a Resource.

To add a Loop marker to a Choreography Activity

- Right-click a Choreography Activity and select Standard Loop or MultiInstance Loop .

To display a MultiInsatance Loop (sequential) marker on a MultiInstane Loop Choreography Activity, do one of the following

- Right-click a Choreography Activity with the MultiInstance Loop (parallel) marker and select Is Sequential .
- Open the Choreography Activity with the MultiInstance Loop marker Specification window. Select the Is Sequential check box.

**Related elements**

- Choreography Activities
- Participant
- Resource

**Related diagram**

- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Creating and Using Choreography Task
- Creating SubChoreography
- Creating Call Choreography Activity
- Creating and Using Participant
- Using Common BPMN Elements

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section describes how to create and model choreography activities in a BPMN Choreography diagram. You can specify a list of Participants in a Choreography Activity from</p><ul><li>Specification window</li><li>Smart Manipulator toolbar</li><li>Drag-and-drop operation</li></ul><p><br /></p><p>To specify a list of Participants from the Specification window</p><hr style="" /><ol><li>Do one of the following:<ul><li>Select the Choreography Activity on the diagram pane and on the Smart Manipulator toolbar, click the Participants button.</li><li>Open the Specification window, click the <strong>Participants</strong> property value cell and then click <strong>...</strong> button.</li></ul></li><li>In the open <strong>Select Recourse</strong> dialog, select Resources.</li><li>Click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="c2f97c90-d5b3-46b9-a205-026962be80d9"><ac:rich-text-body>You need to specify at least two Participants for a Choreography Activity.</ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f69761d2-3682-4d1d-a885-685b1752201a"><ac:rich-text-body>The MultiInstance Participants on a Choreography shape will be displayed with a MultiInstance marker in the Participants’ compartment.</ac:rich-text-body></ac:structured-macro><p><br /></p><p><br /></p><p>To specify a list of participants from the drag-and-drop action</p><hr style="" /><ul><li>Drag a Resource from the Containment tree to a Choreography Activity on diagram pane.</li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a800fff8-baec-46a8-a208-25e83834f851"><ac:rich-text-body><ul><li>Hold down Shift to select multiple elements that are grouped together.</li><li>Hold down Ctrl to select multiple elements that are not grouped together.</li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To specify an Initiating Participant in a Choreography Activity</p><hr style="" /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="372b9c3a-076b-4ce1-a64d-603fb8b74570"><ac:rich-text-body>A Choreography Activity needs the<strong> Initiating Participant</strong> property value to be specified.</ac:rich-text-body></ac:structured-macro><ol><li>Open the Choreography Activity Specification window.</li><li>Click the <strong>Initiating Participant</strong> property value cell and select a Resource.</li></ol><p><br /></p><p>To add a Loop marker to a Choreography Activity</p><hr style="" /><ul><li>Right-click a Choreography Activity and select <strong>Standard Loop</strong> or <strong>MultiInstance Loop</strong>.</li></ul><p><br /></p><p>To display a MultiInsatance Loop (sequential) marker on a MultiInstane Loop Choreography Activity, do one of the following</p><hr style="" /><ul><li>Right-click a Choreography Activity with the MultiInstance Loop (parallel) marker and select <strong>Is Sequential</strong>.</li><li>Open the Choreography Activity with the MultiInstance Loop marker Specification window. Select the <strong>Is Sequential</strong> check box.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Choreography+Activities">Choreography Activities</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Participant">Participant</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li></ul><p><strong>Related diagram</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Choreography+Task" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Creating and Using Choreography Task</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+SubChoreography">Creating SubChoreography</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+Call+Choreography+Activity">Creating Call Choreography Activity</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+and+Using+Participant">Creating and Using Participant</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Using+Common+BPMN+Elements">Using Common BPMN Elements</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032065 space=CBMP2024x version=1 -->
## PAGE 00208: Using Common BPMN Elements

- page_id: `290032065`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032065/Using+Common+BPMN+Elements
- version_number: 1
- version_date: `2026-02-09T15:48:16.131+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

Some BPMN elements can not be represented on any BPMN diagram. You can use these elements as data types for specifying values of other element properties. This kind of elements can be created in the Containment tree.

To create a BPMN element in the Containment tree

1. Right-click a package in the Containment tree.
2. From the shortcut menu, select New Element > BPMN Element , and choose a BPMN element that you want to create.

To open an element Specification window, do one of the following

- Right-click a selected symbol and from shortcut menu, select Specification .
- Double-click a symbol on the Diagram pane or in the Model Browser.
- Select a symbol on the Diagram pane and press Enter.
- Add a model element to an owning model element in its Specification window. The second Specification window opens on top of the first. Use the Back to or Forward to arrow buttons for switching between windows.

**Related element**

- Common BPMN Elements

**Related external resource**

- Specification window

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Some BPMN elements can not be represented on any BPMN diagram. You can use these elements as data types for specifying values of other element properties. This kind of elements can be created in the Containment tree.</p><p><br /></p><p>To create a BPMN element in the Containment tree</p><hr style="" /><ol><li>Right-click a package in the Containment tree. </li><li>From the shortcut menu, select <strong>New Element</strong> &gt; <strong>BPMN Element</strong>, and choose a BPMN element that you want to create.</li></ol><p><br /></p><p>To open an element Specification window, do one of the following</p><hr style="" /><ul><li>Right-click a selected symbol and from shortcut menu, select <strong>Specification</strong>.</li><li>Double-click a symbol on the Diagram pane or in the Model Browser.</li><li>Select a symbol on the Diagram pane and press Enter.</li><li>Add a model element to an owning model element in its Specification window. The second Specification window opens on top of the first. Use the <strong>Back to</strong> or <strong>Forward</strong> <strong>to</strong> arrow buttons for switching between windows.</li></ul><p><br /></p><p style="margin-top: 0.0px;"><strong>Related element</strong></p><ul><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Common+BPMN+Elements" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Common BPMN Elements</a></li></ul><p><strong>Related external resource</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/MD2024xR1/Specification+window">Specification window</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032092 space=CBMP2024x version=1 -->
## PAGE 00209: Using Organization Structure Diagram

- page_id: `290032092`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032092/Using+Organization+Structure+Diagram
- version_number: 1
- version_date: `2026-02-09T16:02:44.980+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Using Cameo Business Modeler Plugin
- labels: []

### NORMALIZED CONTENT

##### Creating and Using Resources

You can create a Resource inside a package. The Resource is not displayed on a BPMN2 diagram as it is represented by a Pool, Data Object, and Choreography Task.

To create a Resource on a Organization Structure diagram

- On the Organization Structure Diagram pallet, click the Resource button.

To create a Resource in the Containment tree

- Right-click a package in the Containment tree. On the shortcut menu, click Create Element > Resource .

To change a type of Resource

- Right-click the Resource and on the shortcut menu select needed Resource type.

To review traceability information related to a Resource

1. Right-click a created Resource in the Containment tree and click Specification to open the Resource Specification window.
2. In the Resource Specification window, select Traceability .

**Related elements**

- Resource
- Organization Unit
- Role
- Person
- Information system

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram
- BPMN Choreography Diagram

**Related procedures**

- Creating a Diagram
- Using BPMN Element Numbers

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3 style="color:var(--ds-text,#172b4d);">Creating and Using Resources</h3><p>You can create a Resource inside a package. The Resource is not displayed on a BPMN2 diagram as it is represented by a Pool, Data Object, and Choreography Task.</p><p><br /></p><p>To create a Resource on a Organization Structure diagram</p><hr style="" /><ul><li>On the Organization Structure Diagram pallet, click the Resource button.</li></ul><p><br /></p><p>To create a Resource in the Containment tree</p><hr style="" /><ul><li>Right-click a package in the Containment tree. On the shortcut menu, click <strong>Create Element</strong> &gt; <strong>Resource</strong>.</li></ul><p><br /></p><p>To change a type of Resource</p><hr style="" /><ul><li>Right-click the Resource and on the shortcut menu select needed Resource type.</li></ul><p><br /></p><p>To review traceability information related to a Resource</p><hr style="" /><ol><li>Right-click a created Resource in the Containment tree and click <strong>Specification</strong> to open the Resource Specification window.</li><li>In the Resource Specification window, select <strong>Traceability</strong>.</li></ol><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Resource">Resource</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Organization+Unit">Organization Unit</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Role" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Role</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Person">Person</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Information+system">Information system</a></li></ul><p><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Choreography+Diagram" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN Choreography Diagram</a></li></ul><p><strong>Related procedures</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Creating+a+Diagram">Creating a Diagram</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/Using+BPMN+Element+Numbers" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Using BPMN Element Numbers</a></li></ul>
````

<!--NOMAGIC_PAGE id=290032099 space=CBMP2024x version=1 -->
## PAGE 00210: Validation Rules

- page_id: `290032099`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290032099/Validation+Rules
- version_number: 1
- version_date: `2026-02-09T16:05:00.032+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

Cameo Business Modeler has the functionality to check if a created BPMN model corresponds to the most important modeling rules defined in the Business Process Modeling and Notation (BPMN) standard. 
Cameo Business Modeler provides the following three validation suites to validate BPMN models:

- BPMN2 Correctness (Active) Validation Rules suite. The active BPMN2 validation in MagicDraw instantly checks the most important correctness rules of a BPMN2 model, displays errors in the model, and suggests solutions.
- BPMN2 Correctness Validation Rules suite is included in all BPMN2 projects. You may run this suite to verify if a BPMN2 model has been created correctly. This suite verifies a bigger set of correctness rules than an active validation rules set does.
- BPMN2 Completeness Validation Rules suite is included in all BPMN2 projects. You may run this suite to verify if a BPMN2 model is fully specified.
- BPMN2 Export Completeness Validation Rules suite is included in all BPMN2 projects. You may run this suite to verify if BPMN2 models have been completely defined with the required and mandatory information in models for exporting.

BPMN2 Correctness Completeness and BPMN2 Export Completenessvalidation rules are available only in the Architect edition.

**Related rules**

- BPMN2 Correctness (Active) Validation Rules
- BPMN2 Correctness Validation Rules
- BPMN2 Completeness Validation Rules
- BPMN2 Export Completeness Validation Rules

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cameo Business Modeler has the functionality to check if a created BPMN model corresponds to the most important modeling rules defined in the Business Process Modeling and Notation (BPMN) standard.<br />Cameo Business Modeler provides the following three validation suites to validate BPMN models:</p><ul><li>BPMN2 Correctness (Active) Validation Rules suite. The active BPMN2 validation in MagicDraw instantly checks the most important correctness rules of a BPMN2 model, displays errors in the model, and suggests solutions.</li><li>BPMN2 Correctness Validation Rules suite is included in all BPMN2 projects. You may run this suite to verify if a BPMN2 model has been created correctly. This suite verifies a bigger set of correctness rules than an active validation rules set does.</li><li>BPMN2 Completeness Validation Rules suite is included in all BPMN2 projects. You may run this suite to verify if a BPMN2 model is fully specified.</li><li>BPMN2 Export Completeness Validation Rules suite is included in all BPMN2 projects. You may run this suite to verify if BPMN2 models have been completely defined with the required and mandatory information in models for exporting.</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cb66d723-1363-4c9d-bf03-b169c63763c4"><ac:rich-text-body>BPMN2 Correctness Completeness and BPMN2 Export Completenessvalidation rules are available only in the Architect edition.</ac:rich-text-body></ac:structured-macro><p><br /></p><p style="margin-top: 0.0px;"><strong>Related rules</strong></p><ul class="childpages-macro"><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN2+Correctness+%28Active%29+Validation+Rules" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN2 Correctness (Active) Validation Rules</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN2+Correctness+Validation+Rules">BPMN2 Correctness Validation Rules</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN2+Completeness+Validation+Rules" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN2 Completeness Validation Rules</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN2+Export+Completeness+Validation+Rules" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">BPMN2 Export Completeness Validation Rules</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031956 space=CBMP2024x version=1 -->
## PAGE 00211: Vision

- page_id: `290031956`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031956/Vision
- version_number: 1
- version_date: `2026-02-09T14:54:00.379+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Supportive Diagrams Concepts > Business Motivation Diagram > Ends Concepts
- labels: []

### NORMALIZED CONTENT

**Description**

A vision is a state where an organization wants to achieve in the future. It is common that a vision is made up of many aspects rather than concentrated on a specific factor of the business problem. It is the final, possibly unattainable, state the organization would like to accomplish. It does not describe how the organization will achieve the state. A Vision is often compound, rather than focused toward one particular aspect of the business problem. It is supported or made operative by Missions and amplified by Goals.

**Notation**

[IMAGE alt='' src='']

**Related elements**

- Ends Concepts
- End Concept Relationships

**Related diagram**

- Business Motivation Diagram

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Description</strong></p><p>A vision is a state where an organization wants to achieve in the future. It is common that a vision is made up of many aspects rather than concentrated on a specific factor of the business problem. It is the final, possibly unattainable, state the organization would like to accomplish. It does not describe how the organization will achieve the state. A Vision is often compound, rather than focused toward one particular aspect of the business problem. It is supported or made operative by Missions and amplified by Goals.</p><p><strong>Notation</strong></p><p><ac:image><ri:attachment ri:filename="vision.png"><ri:page ri:space-key="CBMP2024x" ri:content-title="Vision" /></ri:attachment></ac:image></p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related elements</strong></p><ul><li class="ancestor-link parent-link"><a href="https://docs.nomagic.com/display/CBMP2024xR1/Ends+Concepts" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">Ends Concepts</a></li><li><a href="https://docs.nomagic.com/display/CBMP2024xR1/End+Concept+Relationships" style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);">End Concept Relationships</a></li></ul><p><strong>Related diagram</strong></p><ul><li class="ancestor-link"><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Business+Motivation+Diagram">Business Motivation Diagram</a></li></ul>
````

<!--NOMAGIC_PAGE id=290031950 space=CBMP2024x version=1 -->
## PAGE 00212: XPDL Support

- page_id: `290031950`
- space_key: `CBMP2024x`
- source_url: https://docs.nomagic.com/spaces/CBMP2024x/pages/290031950/XPDL+Support
- version_number: 1
- version_date: `2026-02-09T14:52:14.578+01:00`
- ancestors: Cameo Business Modeler Plugin Documentation > User Guide > Business Process Model and Notation Concepts
- labels: []

### NORMALIZED CONTENT

XML Process Definition Language (XPDL) is a serialization format for BPMN. XPDL provides a file format that supports all BPMN process definition description properties. It defines a description of both model element properties and graphical descriptions of the diagram. With XPDL, Cameo Business Modeler can export or import process definitions for or from other products to read. It also allows you to exchange your models with other tools to perform further model simulation, execution, or deployment.

Cameo Business Modeler plugin supports export of BPMN models to XPDL Version 2.2. This version is backward compatible with previous versions of XPDL and can be used to export BPMN2 and BPMN 1.x models.

Cameo Business Modeler supports importing from XPDL Versions 2.0, 2.1, and 2.2 to BPMN2. Business process models created with other tools (e.g. Visio, BizAgi, Process Architect, etc) can be imported to Cameo Business Modeler.

**Related diagrams**

- BPMN Process Diagram
- BPMN Collaboration Diagram

**Related procedure**

- Exporting Models to XPDL

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>XML Process Definition Language (XPDL) is a serialization format for BPMN. XPDL provides a file format that supports all BPMN process definition description properties. It defines a description of both model element properties and graphical descriptions of the diagram. With XPDL, Cameo Business Modeler can export or import process definitions for or from other products to read. It also allows you to exchange your models with other tools to perform further model simulation, execution, or deployment.</p><p>Cameo Business Modeler plugin supports export of BPMN models to XPDL Version 2.2. This version is backward compatible with previous versions of XPDL and can be used to export BPMN2 and BPMN 1.x models.</p><p>Cameo Business Modeler supports importing from XPDL Versions 2.0, 2.1, and 2.2 to BPMN2. Business process models created with other tools (e.g. Visio, BizAgi, Process Architect, etc) can be imported to Cameo Business Modeler.</p><p><br /></p><p style="margin-top: 0.0px;"><strong>Related diagrams</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Process+Diagram">BPMN Process Diagram</a></li><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/BPMN+Collaboration+Diagram">BPMN Collaboration Diagram</a></li></ul><p><strong>Related procedure</strong></p><ul><li><a style=";color:var(--ds-background-accent-blue-bolder,#0c66e4);" href="https://docs.nomagic.com/display/CBMP2024xR1/Exporting+Models+to+XPDL">Exporting Models to XPDL</a></li></ul>
````
