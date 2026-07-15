# NOMAGIC DOCUMENTATION SPACE: SysML Plugin 2024x Refresh3

<!--NOMAGIC_SPACE key=SYSMLP2024xR3 chunk=2 -->

<!--NOMAGIC_PAGE id=227159499 space=SYSMLP2024xR3 version=1 -->
## PAGE 00234: Missing Probability stereotype

- page_id: `227159499`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159499/Missing+Probability+stereotype
- version_number: 1
- version_date: `2021-02-11T09:54:46.167+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Activities
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
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Probability[2]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks to see if the «probability» stereotype is applied to all edges coming out of the same source when the «probability» stereotype is applied to an activity edge.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity Edge<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, apply the «probability» stereotype to all edges coming out of the same source.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="probability_on_activity_edge.png"><ri:page ri:content-title="Missing Probability stereotype" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">Both Control Flows that come out of the same source must be stereotyped by the  «probability».</h6><p><strong><br /></strong></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159595 space=SYSMLP2024xR3 version=1 -->
## PAGE 00235: Missing streaming parameter

- page_id: `227159595`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159595/Missing+streaming+parameter
- version_number: 1
- version_date: `2021-01-06T12:10:14.385+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>streaming[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks if t</span><span style="color: rgb(62,63,64);">he Activity stereotyped by </span><span style="color: rgb(51,51,51);">«s</span><span style="color: rgb(62,63,64);">treaming</span><span style="color: rgb(51,51,51);">»</span><span style="color: rgb(62,63,64);"> owns at least one parameter that is streaming.</span></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity<strong><br /></strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this warning, do one of the following:</span></p><ul><li><span style="color: rgb(62,63,64);">If the parameter is created <span style="color: rgb(62,63,64);">for the streaming Activity</span>, in the </span><span style="color: rgb(62,63,64);">parameters Specification window set the </span><strong>Is Stream</strong><span style="color: rgb(62,63,64);"> property value to </span><em>true</em><span style="color: rgb(62,63,64);">.</span><strong><br class="_mce_tagged_br" /></strong></li><li><span style="color: rgb(62,63,64);">If any of parameters are not created for the streaming Activity, create it.</span></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="missing_streaming_parameter.png"><ri:page ri:content-title="Missing streaming parameter" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">The streaming <em>dry part</em> Activity owns streaming <em>in</em> Parameter.</h6></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159530 space=SYSMLP2024xR3 version=1 -->
## PAGE 00236: Missing Value Type stereotype

- page_id: `227159530`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159530/Missing+Value+Type+stereotype
- version_number: 1
- version_date: `2021-02-11T09:49:00.236+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Blocks
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
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>ValueType[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><ac:inline-comment-marker ac:ref="b3284607-8ae2-46ca-ab29-e9fd17388612">This validation rule checks if any classifier which specializes (has generalization relationship to) a Value Type</ac:inline-comment-marker> also have the <span style="color: rgb(62,63,64);">«V</span>alueType<span style="color: rgb(62,63,64);">»</span> stereotype applied.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><ac:inline-comment-marker ac:ref="2bb6e78c-ac21-4c40-b625-49466d0bb9b0">DataType</ac:inline-comment-marker><strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Apply the corresponding Value Type stereotype and/or its subtype(s) to itself</strong> - applies the <span style="color: rgb(62,63,64);">«V</span>alueType<span style="color: rgb(62,63,64);">»</span> stereotype.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="missing_value_type_stereotype.png"><ri:page ri:content-title="Missing Value Type stereotype" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">The <em>Actions</em> Data Type must be stereotyped by <span style="color: rgb(62,63,64);">«</span>valueType<span style="color: rgb(62,63,64);">».</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=227158526 space=SYSMLP2024xR3 version=2 -->
## PAGE 00237: Model Browser

- page_id: `227158526`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158526/Model+Browser
- version_number: 2
- version_date: `2025-05-02T10:28:17.873+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

233723459

233723461

233723460

[CONFLUENCE_PAGE title='Model Browser' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3036f855-1ea1-4e84-8ed4-7a3e437fe542"><ac:parameter ac:name="id">233723459</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e160fb61-199c-4f61-b912-02354807446d"><ac:parameter ac:name="id">233723461</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1206bc9d-7a99-4634-9965-ef3fbb8be29d"><ac:parameter ac:name="id">233723460</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="ca7e6f66-0320-46e7-b09f-1c9e6aed1e0b"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Model Browser" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158542 space=SYSMLP2024xR3 version=2 -->
## PAGE 00238: Model Extensions tab

- page_id: `227158542`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158542/Model+Extensions+tab
- version_number: 2
- version_date: `2025-05-02T10:28:18.309+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

235250778

235250781

235250777

**On this page**

33

235250780

[CONFLUENCE_PAGE title='Model Extensions tab' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f8887805-f05c-4dc9-b50a-b5c85a41633e"><ac:parameter ac:name="id">235250778</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f4d40783-f999-4288-b0f6-d40553c1cd63"><ac:parameter ac:name="id">235250781</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="44ecdc2f-f1b4-4d45-be1e-1c361e76bf8c"><ac:parameter ac:name="id">235250777</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="83d36313-2b23-41ad-8f43-9b367d0c77b6"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3a382692-ff17-457d-ad44-761cc9fc9f5b"><ac:parameter ac:name="id">235250780</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="923e14a4-f899-4f47-8b71-c6d59687a6ec"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Model Extensions tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227160214 space=SYSMLP2024xR3 version=3 -->
## PAGE 00239: Modelica export

- page_id: `227160214`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160214/Modelica+export
- version_number: 3
- version_date: `2025-05-02T10:28:47.131+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models
- labels: []

### NORMALIZED CONTENT

**On this page**

5

##### Introduction

Export to Modelica tool allows quick and automatic synchronization between high-level system architecture and behaviour model definitions and Modelica simulation models by translating and mapping corresponding concepts and names. The Modelica export is based on SysPhS standard that is described in details in the [OMG SysPhS specification](https://www.omg.org/spec/SysPhS/About-SysPhS/)(SysML Extension for Physical Interaction and Signal Flow Simulation).You can use the Modelica export functionality in our tool to export your model to the Modelica file. The export includes blocks, parametrics, state machines, internal structures with ports, interfaces and connectors. The generated *.mo file is ready to open with Modelica tools. As example of exported model to the Modelica file, see the figure below.

[IMAGE alt='' src='']

###### The *ConnectedTanks* Block exported to the Modelica file.

##### Preparing SysML model for Modelica export

No special prerequisites are required to be able to use SysML to Modelica transformation. Any existing pure SysML models can be exported into Modelica with a high level of success. That is especially true for black-box architecture definitions (blocks, parts, ports, parameters, interfaces and connectors). However, if user wants to export full behavior implementation and expects it to be ready and simulatable in Modelica, some special annotation may be required. Modelica can only solve the models where number of variables is no more than number of equations. That means all SysML properties can’t be exported as variables, some must be marked as constants or parameters.

**SysML properties**

You can prepare your model by:

- Applying « PhSConstant » stereotype to a SysML property if it has fixed value and not going to change during simulation. It is exported as Modelica parameter.
- Applying « PhSVariable » stereotype if you want to mark property as Modelica variable and fill appropriate tags (isContinuous, isConserved and changeCycle) if needed. [CONFLUENCE_PAGE title='Using SysPhs constant and SysPhs variable' space='SYSMLP2024xR3']>]]>

If SysML properties are not annotated with«PhSConstant»or«PhSVariable»stereotypes, they all are exported equally, as you select in the **Modelica Export Options** dialog: all as parameters, variables or skipped. >]]>[CONFLUENCE_PAGE title='Modelica export' space='SYSMLP2024xR3']

**Diagrams**

SysML IBD diagrams can be optionally converted into Modelica graphical annotations. Only one IBD diagram per Block is exported, so if you have more, make sure that the right one is the first under the Block in the model browser. Rename, remove or change the order if needed. >]]>[CONFLUENCE_PAGE title='Modelica export' space='SYSMLP2024xR3']

##### Exporting model to the Modelica file

You can export to the Modelica file:

- [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] , [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'] - exports the whole model (Read the procedure below).
- [CONFLUENCE_PAGE title='Instance Specification' space='MD2024xR3'] - exports particular configuration with initial values and subtype instances as specified in the instance model. [CONFLUENCE_PAGE title='Instance Specifications export to the Modelica file' space='SYSMLP2024xR3']>]]>
- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3'] - partial export of parts, ports and connectors from this diagram. [CONFLUENCE_PAGE title='Partial model export to the Modelica file' space='SYSMLP2024xR3']>]]>

To export the whole model to the Modelica file

1. In the [CONFLUENCE_PAGE title='Model Browser' space='SYSMLP2024xR3'] , select the Block you want to export and do one of the following:
  - In the top-left corner of the modeling tool, c lick File > Export To > Modelica .
  - Right-click the selected Block and then click Tools > Export to Modelica .
2. Specify export options in the Modelica Export Options dialog. Option descriptions >>
3. Click OK . The Modelica (.mo) file is generated and saved to your file directory.

###### Modelica Export Options

Each time you export your model to the Modelica file, the **Modelica Export Options** dialog opens. The detailed descriptions are provided in the following table.

###### [IMAGE alt='' src='']

| Option | Description |
| --- | --- |
| Export not annotated SysML properties as: | Select one of the following to define how the mechanism must export not annotated properties (read the definition below):as Variablesas ParametersDo not export Annotated SysML properties definitionAn annotated SysML properties are used in the model if the «PhsVariable» or «PhsConstant» stereotypes are applied for the Block properties. The detail information about «PhsVariable» or «PhsConstant» stereotypes, are provided in the Using SysPhs variable and SysPhs constant page and OMG SysPhS specification.Contrary to annotated SysML properties, not annotated SysML properties means that your model is without «PhsVariable» or «PhsConstant» stereotypes.You can check, if those stereotypes are used in your model by clicking in the and selecting the Show Applied Stereotypes option. The stereotypes becomes visible next to the element name in the . |
| Generate diagram layout annotations | If selected, converts SysML IBD diagram into Modelica graphical annotations. Only first IBD diagram of the Block is exported. If you have more, make sure the right one is the first under the Block in the Model Browser. Rename, remove or change the order if needed.You can modify the default value of the Generate Diagram layout annotations option in the project options dialog. To learn more about modifying the project options, refer to . |
|  | Click to specify the location of generated file or rename the file. |

**Related pages**

- Partial model export to the Modelica file
- Nested properties export to the Modelica file
- [CONFLUENCE_PAGE title='Extending models with Comments' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="35a3e451-5d2e-49f7-ade0-246c124f0149"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Introduction</h3><p>Export to Modelica tool allows quick and automatic synchronization between high-level system architecture and behaviour model definitions and Modelica simulation models by translating and mapping corresponding concepts and names. The Modelica export is based on SysPhS standard that is described in details in the <a class="external-link" href="https://www.omg.org/spec/SysPhS/About-SysPhS/" rel="nofollow">OMG SysPhS specification</a><span style="color: rgb(62,63,64);"> (SysML Extension for Physical Interaction and Signal Flow Simulation). </span>You can use the Modelica export functionality in our tool to export your model to the Modelica file. The export includes blocks, <span style="color: rgb(62,63,64);">parametrics, state machines, internal structures with ports, interfaces and connectors. The generated *.mo file is ready to open with Modelica tools. As example of exported model to the Modelica file, see the figure below. </span></p><p><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="sysml_to_modelica.png"><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The <em>ConnectedTanks</em> Block exported to the Modelica file.</span></h6><h3>Preparing SysML model for Modelica export</h3><p>No special prerequisites are required to be able to use SysML to Modelica transformation. Any existing pure SysML models can be exported into Modelica with a high level of success. That is especially true for black-box architecture definitions (blocks, parts, ports, parameters, interfaces and connectors). However, if user wants to export full behavior implementation and expects it to be ready and simulatable in Modelica, some special annotation may be required. Modelica can only solve the models where number of variables is no more than number of equations. That means all SysML properties can’t be exported as variables, some must be marked as constants or parameters.</p><p><strong>SysML properties</strong></p><p>You can prepare your model by:</p><ul><li>Applying <span style="color: rgb(51,51,51);">«</span><span style="color: rgb(62,63,64);">PhSConstant</span><span style="color: rgb(51,51,51);">»</span> stereotype to a SysML property if it has fixed value and not going to change during simulation. It is exported as Modelica parameter.</li><li>Applying <span style="color: rgb(51,51,51);">«</span><span style="color: rgb(62,63,64);">PhSVariable</span><span style="color: rgb(51,51,51);">» stereotype </span>if you want to mark property as Modelica variable and fill appropriate tags (isContinuous, isConserved and changeCycle) if needed. <ac:link><ri:page ri:content-title="Using SysPhs constant and SysPhs variable" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Read more >>]]></ac:plain-text-link-body></ac:link></li></ul><p><span>If SysML properties are not annotated with </span><span style="color: rgb(51,51,51);">«</span><span style="color: rgb(62,63,64);">PhSConstant</span><span style="color: rgb(51,51,51);">»</span><span> or </span><span style="color: rgb(51,51,51);">«</span><span style="color: rgb(62,63,64);">PhSVariable</span><span style="color: rgb(51,51,51);">»</span><span> stereotypes, they all are exported equally, as you select in the <strong>Modelica Export Options</strong> dialog: all as parameters, variables or skipped. <ac:link><ac:plain-text-link-body><![CDATA[Descriptions of export options >>]]></ac:plain-text-link-body><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /></ac:link></span></p><p><strong>Diagrams</strong></p><p>SysML IBD diagrams can be optionally converted into Modelica graphical annotations. Only one IBD diagram per Block is exported, so if you have more, make sure that the right one is the first under the Block in the model browser. Rename, remove or change the order if needed. <ac:link><ac:plain-text-link-body><![CDATA[Descriptions of export options >>]]></ac:plain-text-link-body><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /></ac:link></p><h3>Exporting model to the Modelica file</h3><p>You can export to the Modelica file:</p><ul><li><ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>, <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link>- exports the whole model (Read the procedure below).</li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance Specification" /></ac:link> - exports particular configuration with initial values and subtype instances as specified in the instance model. <ac:link><ri:page ri:content-title="Instance Specifications export to the Modelica file" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[How to >>]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Internal Block Diagram]]></ac:plain-text-link-body></ac:link> - partial export of parts, ports and connectors from this diagram. <ac:link><ri:page ri:content-title="Partial model export to the Modelica file" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[How to >>]]></ac:plain-text-link-body></ac:link></li></ul><p><br /></p><p>To export the whole model to the Modelica file</p><hr /><ol><li>In the <ac:link><ri:page ri:content-title="Model Browser" ri:space-key="SYSMLP2024xR3" /></ac:link>, select the Block you want to export and do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the top-left corner of the modeling tool, c</span><span style="color: rgb(62,63,64);">lick </span><strong>File</strong> &gt;<strong> Export To &gt; Modelica</strong>.</li><li>Right-click the selected Block and then click <strong>Tools</strong> &gt; <strong>Export to Modelica</strong>.</li></ul></li><li>Specify export options in the <strong>Modelica Export Options</strong> dialog. <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Modelica+export#Modelicaexport-ModelicaExportOptions">Option descriptions &gt;&gt;</a></li><li>Click <strong>OK</strong>.<br /><span style="color: rgb(62,63,64);">The Modelica (.mo) file is generated and saved to your file directory.</span></li></ol><h4 class="auto-cursor-target">Modelica Export Options</h4><p>Each time you export your model to the Modelica file, the <strong>Modelica Export Options</strong> dialog opens. The detailed descriptions are provided in the following table.</p><h4><ac:image ac:height="241"><ri:attachment ri:filename="modelica_export_options_dialog.png"><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></h4><table class="relative-table" style="width: 82.8305%;"><colgroup class=""><col class="" style="width: 18.9529%;" /><col class="" style="width: 81.0471%;" /></colgroup><tbody class=""><tr class=""><th>Option</th><th>Description</th></tr><tr class=""><td>Export not annotated SysML properties as:</td><td><div class="content-wrapper"><p><span style="color: rgb(51,51,51);">Select one of the following to define how the mechanism must export not annotated properties (read the definition below):</span></p><ul><li class="auto-cursor-target"><span style="color: rgb(51,51,51);">as Variables</span></li><li class="auto-cursor-target"><span style="color: rgb(51,51,51);">as Parameters</span></li><li class="auto-cursor-target"><span style="color: rgb(51,51,51);">Do not export </span></li></ul><p><strong>Annotated SysML properties </strong><strong>definition</strong></p><p>An annotated SysML properties are used in the model if the <span style="color: rgb(62,63,64);">«</span>PhsVariable<span style="color: rgb(62,63,64);">»</span> or <span style="color: rgb(62,63,64);">«</span>PhsConstant<span style="color: rgb(62,63,64);">»</span> stereotypes are applied for the Block properties. <span style="color: rgb(62,63,64);">The detail information about «PhsVariable» or «PhsConstant» stereotypes, are provided in the </span><a class="current" href="https://docs.nomagic.com/display/SYSMLP2024xR3/Using+SysPhs+variable+and+SysPhs+constant">Using SysPhs variable and SysPhs constant</a><span style="color: rgb(62,63,64);"> page and </span><a class="external-link" href="https://www.omg.org/spec/SysPhS/About-SysPhS/" rel="nofollow">OMG SysPhS specification</a><span style="color: rgb(62,63,64);">.</span></p><p><span style="color: rgb(51,51,51);">Contrary to annotated SysML properties, not annotated SysML properties means that your model is without «PhsVariable» or «PhsConstant» stereotypes.</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="28f83c90-75c7-4b3b-941f-936f334f6140"><ac:rich-text-body><p><span>You can check, if those stereotypes are used in your model by clicking </span><ac:image ac:title="Options" ac:thumbnail="true" ac:alt="Options" ac:height="22"><ri:attachment ri:filename="options_button_in_model_browser.png"><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><span> in the </span><ac:link><ri:page ri:content-title="Containment tab" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Containment tab toolbar]]></ac:plain-text-link-body></ac:link><span> and selecting the </span><strong>Show</strong><span style="color: rgb(62,63,64);"> </span><strong>Applied Stereotypes </strong><span>option. The stereotypes becomes visible </span><span style="color: rgb(62,63,64);">next to the element name in the <ac:link><ri:page ri:content-title="Containment tab" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>. </span></p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr class=""><td>Generate diagram layout annotations</td><td><div class="content-wrapper"><p>If selected, converts SysML IBD diagram into Modelica graphical annotations. Only first IBD diagram of the Block is exported. If you have more, make sure the right one is the first under the Block in the Model Browser. Rename, remove or change the order if needed.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cec4dbba-4f8a-4550-b497-6929565b82c2"><ac:rich-text-body><p>You can modify the default value of the <strong>Generate Diagram layout annotations</strong> <span style="color: rgb(23,43,77);">option<span> </span></span>in the project options dialog. To learn more about modifying the project options, refer to <ac:link><ri:page ri:content-title="Setting project options" ri:space-key="SYSMLP2024xR3" /></ac:link><span>.</span></p></ac:rich-text-body></ac:structured-macro></div></td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="19"><ri:attachment ri:filename="select_file.png"><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></div></td><td colspan="1"><span>Click to specify the location of generated file or rename the file. </span></td></tr></tbody></table></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li class="with-breadcrumbs"><a class="current" href="https://docs.nomagic.com/display/SYSMLP2024xR3/Partial+model+export+to+the+Modelica+file">Partial model export to the Modelica file</a></li><li class="with-breadcrumbs"><a class="current" href="https://docs.nomagic.com/display/SYSMLP2024xR3/Nested+properties+export+to+the+Modelica+file">Nested properties export to the Modelica file</a></li><li class="with-breadcrumbs"><ac:link><ri:page ri:content-title="Extending models with Comments" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227160063 space=SYSMLP2024xR3 version=1 -->
## PAGE 00240: Modelica import

- page_id: `227160063`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160063/Modelica+import
- version_number: 1
- version_date: `2021-08-12T07:26:38.371+02:00`
- ancestors: SysML Plugin Documentation > Importing External Simulation Models
- labels: []

### NORMALIZED CONTENT

##### **What is Modelica?**

TheModelica Languageis a non-proprietary, object-oriented, equation based language to conveniently model complex physical systems containing, for example, mechanical, electrical, electronic, hydraulic, thermal, control, electric power or process-oriented subcomponents.

##### **Modelica file import**

The modeling tools support**MO******file format, meaning that you must have your Modelica model in this format to import it. Following the Modelica file import, the **Modelica Import Options** dialog opens. It allows selecting features you want to update from the Modelica file, create, delete, or change the context-specific initial values. Blocks or Interface Blocks, introduced as property types, are created under the same owner as an imported context. The primitive type, if it was set, is also created for a Block or Interface Block. You can also create properties, connectors, and ports. Note that the imported Connectors are identified by the connector ends.

To import the Modelica file into the model

1. Select a Block.
2. In the top-left corner of the modeling tool, click File > Import From > Modelica File . [ATTACHMENT filename='modelica_import_menu.png']
3. Select the Modelica (.mo) file on your file system and click Import . [ATTACHMENT filename='modelica_import_select_file.png']
4. In the Modelica Import Options dialog, specify which features you want to update from the Modelica file.
5. Click Import .

###### An example of Modelica Import

The original Modelica data file for the example model:

[IMAGE alt='' src='']

The changes made in the Modelica data file are shown in the Modelica Import Options dialog, where you can choose whether to accept those changes or not:

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3><strong>What is Modelica?</strong></h3><p><span style="color: rgb(0,0,0);">The </span>Modelica Language<span style="color: rgb(0,0,0);"> is a non-proprietary, object-oriented, equation based language to conveniently model complex physical systems containing, for example, mechanical, electrical, electronic, hydraulic, thermal, control, electric power or process-oriented subcomponents.</span></p><h3><strong>Modelica file import</strong></h3><p>The modeling tools support<strong> MO</strong><strong> </strong>file format, meaning that you must have your Modelica model in this format to import it. Following the Modelica file import, the <strong>Modelica Import Options</strong> dialog opens. It allows s<span>electing features you want to update from the Modelica file, create, delete, or change the context-specific initial values. Blocks or Interface Blocks, introduced as property types, are created under the same owner as an imported context. The primitive type, if it was set, is also created for a Block or Interface Block.  You can also create properties, connectors, and ports. Note that the imported Connectors are identified by the connector ends.</span></p><p><br /></p><p>To import the Modelica file into the model</p><hr /><ol><li>Select a Block.</li><li>In the top-left corner of the modeling tool, click <strong>File</strong> &gt;<strong> Import From </strong>&gt; <strong>Modelica File</strong>.<br /><ac:image><ri:attachment ri:filename="modelica_import_menu.png"><ri:page ri:content-title="Modelica import" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Select the Modelica (.mo) file on your file system and click <strong>Import</strong>.<br /><ac:image><ri:attachment ri:filename="modelica_import_select_file.png"><ri:page ri:content-title="Modelica import" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>In the <strong>Modelica Import Options</strong> dialog, specify which features you want to update from the Modelica file. </li><li>Click <strong>Import</strong>.<br /><br /></li></ol><h4>An example of Modelica Import</h4><p>The original Modelica data file for the example model:</p><p><ac:image><ri:attachment ri:filename="example_modelica_import.png"><ri:page ri:content-title="Modelica import" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p>The changes made in the Modelica data file are shown in the Modelica Import Options dialog, where you can choose whether to accept those changes or not:</p><p><ac:image><ri:attachment ri:filename="modelica_import_options_dialog.png"><ri:page ri:content-title="Modelica import" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p>
````

<!--NOMAGIC_PAGE id=227159117 space=SYSMLP2024xR3 version=1 -->
## PAGE 00241: Modeling functional flows with Activities

- page_id: `227159117`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159117/Modeling+functional+flows+with+Activities
- version_number: 1
- version_date: `2018-04-27T17:37:07.001+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis
- labels: []

### NORMALIZED CONTENT

A new SysML Activity Diagram should be created for every function defined in use the cases of a system you are modeling. Though there are two or even more swimlane partitions, you should choose only those functions that are nested under the partition representing the block which captures your system.Modeling the action flow stimulates the identification of logical subsystems of the whole system.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span>A new SysML Activity Diagram should be created for every function defined in use the cases of a system you are modeling</span><span>. Though there are two or even more swimlane partitions, you should choose only those functions that are nested under the partition representing the block which captures your system</span><span>. </span><span>Modeling the action flow stimulates the identification of logical subsystems of the whole system</span><span>.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a0c6177d-fe04-4c6f-b85e-7a0d22315935" /></p>
````

<!--NOMAGIC_PAGE id=227159137 space=SYSMLP2024xR3 version=2 -->
## PAGE 00242: Modeling interactions with Sequence Diagrams

- page_id: `227159137`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159137/Modeling+interactions+with+Sequence+Diagrams
- version_number: 2
- version_date: `2025-05-02T10:28:31.541+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis
- labels: []

### NORMALIZED CONTENT

1403925404

1403925406

1403925405

[CONFLUENCE_PAGE title='Sequence diagram' space='MD2024xR3']true

1403925402

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="82a0b04b-b852-46f5-9f79-f29bf7dd2287"><ac:parameter ac:name="id">1403925404</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2ff657d8-814f-4ba4-8462-469e77cedb69"><ac:parameter ac:name="id">1403925406</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="824f771c-a977-4720-b8c0-e5f7c258ffa3"><ac:parameter ac:name="id">1403925405</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="7fb5b28f-206f-406f-a771-3c86b37ccf8e"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Sequence diagram" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ce151008-a2cb-4e73-981f-ff8565d86591"><ac:parameter ac:name="id">1403925402</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="c9dedc59-f81b-49e9-8fa4-a94c687eade1" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159013 space=SYSMLP2024xR3 version=3 -->
## PAGE 00243: Modeling parametric constraints

- page_id: `227159013`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159013/Modeling+parametric+constraints
- version_number: 3
- version_date: `2025-05-02T10:28:27.163+02:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

1318769284

1318769286

1299571190

**On this page**

4

1190221077

##### **Introduction**

SysML Parametric Diagrams provide a way to integrate engineering analysis models described in mathematical equations and constraints, with design models describing the structural and behavioral aspects of systems. Parametric diagrams include usages of constraint blocks to constrain the properties of another block. A constraint property is a property of any block that is typed by a constraint block. To empower the constraint expression to perform calculations, you have to specify what system parameters should be consumed as variables of that constraint.

See the figure below, as example of [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3'] wherein all elements are highlighted: [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'], [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'], [CONFLUENCE_PAGE title='Constraint Property' space='SYSMLP2024xR3'], Constraint expression, [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3'], [CONFLUENCE_PAGE title='Binding Connector' space='SYSMLP2024xR3'].

[IMAGE alt='' src='']

###### The main elements used in the SysML Parametric Diagram.

##### Creating parametric constraints

This section explains how to model system constraints in the[SysML Parametric Diagram](https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Parametric+Diagram). Parametric constraints are formulas, and parameters are variables that can be bound to value properties later. Variables can be inputs and outputs of the formula.In general, you must perform the following steps to model your system constraints. However, some actions may already be done in the model creation process, so you may skip these steps and use existing model data. The following procedure provides the main workflow of modeling parametric constraints manually and automatically.

There are two ways to model parametric constraints:

- [CONFLUENCE_PAGE title='Modeling parametric constraints' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Modeling parametric constraints' space='SYSMLP2024xR3']

###### Creating parametric constraints manually

To create parametric constraints manually

1. Open existing project or create new .
2. Create a Block or it's structure in [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3'] . As shown in the figure, The DC Motor Block is decomposed into Rotation part and inherited DC Power part from DC Device Block. [CONFLUENCE_PAGE title='Decomposing Blocks' space='SYSMLP2024xR3']]]> [ATTACHMENT filename='DC_Motor_Block_structure.png']
3. [CONFLUENCE_PAGE title='Creating and managing Block properties' space='SYSMLP2024xR3'] . As shown in the figure below, the highlighted Value Properties created for the DC Motor , Rotation and DC Power Blocks. Specify their types . [IMAGE alt='' src='']
4. Right-click the Block and select Create Diagram > SysML Parametric Diagram . In the opened **Display Parameters/Properties** dialog, select either:
  - Part Properties with its Value Properties, if you have enough space on the diagram pane to display part shapes. As example, see the following figure where power Value Property is displayed inside inherited dcPower Part Property shape.
  - Only Value Properties, if you need to save a space on the diagram pane. The [CONFLUENCE_PAGE title='Property path notation' space='SYSMLP2024xR3'] is used in Value Property name instead of part shape. As example, see the following figure where dot notation ( rotation.powe r) is used to express the path of power Value Property. [ATTACHMENT filename='displaying_value_properties_on_par_diagram_pane.png']
5. Click the Constraint Property button on the diagram palette and then click the empty place of that diagram pane. An unnamed[Constraint Property](https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Property) is created. Type its name.
6. Specify Constraint property type by selecting the Constraint Property shape, from the smart manipulator toolbar, click [ATTACHMENT filename='specify_type.png'] and do either:
  - Type a name of a Constraint Block and press Enter. The new Constraint Block is created automatically in the model with an empty Constraint expression. [ATTACHMENT filename='new-constraint_block_with_empty_expression.png'] Double-click {} and type an expression. To make a [CONFLUENCE_PAGE title='Creating reusable constraint libraries' space='SYSMLP2024xR3'] , we highly recommend to use different value names than exist in particular model. E.g. *efficiency=powerOutput/suppliedPower*. [CONFLUENCE_PAGE title='Creating Constraint Parameters automatically' space='SYSMLP2024xR3'] by clicking [IMAGE alt='' src=''] from Constraint Property smart manipulator toolbar. As shown in the figure below, three Constraint parameters are created: *efficiency*, *suppliedPower*, *powerOutput*. 
[IMAGE alt='' src='']
  - Select [CONFLUENCE_PAGE title='Creating reusable constraint libraries' space='SYSMLP2024xR3'] from the library. The Constraint expression appears automatically.
7. Connect Value Properties with Constraint Parameters in one of the following way: 
 - Select the Value Property shape, from smart manipulator toolbar click [IMAGE alt='' src=''] and connect it to a[Constraint Property](https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Property)shape. From the**Select Parameter**menu list, select an appropriate parameter. As example, see the figure below where *power* Value Property is binding by selecting a *supplierPower* parameter from the suggested list. 
[IMAGE alt='' src=''] 
 - [Display Constraint Parameters on Constraint Property shape](https://docs.nomagic.com/display/SYSMLP2024xR3/Displaying+parameters+and+properties#Displayingparametersandproperties-Usingthesmartmanipulatortoolbar) by clicking[IMAGE alt='' src='']smart manipulator toolbar.Select Value Property/Constraint Parameter shape, click [IMAGE alt='' src=''] and connect it to Constraint Parameter/Value Property. As shown in the figure elow, the *efficiency* Value Property is binding with an *efficiency* parameter. [IMAGE alt='' src=''] The Constraint Parameter are connected with Value Properties using Binding Connector. Now you can run the simulation of parametric data in one of the following way: 
 - Right-click the Block that owns the Parametric diagram and select**Simulation**>**Run**. 
 - From the Parametric Diagram toolbar, click [IMAGE alt='' src='']. 
In the**Variables**tab, type values and click[IMAGE alt='' src='']. [CONFLUENCE_PAGE title='Parametric evaluator' space='CST2024xR3']]]> 
[IMAGE alt='' src=''] You can create an equation system by creating bindings between parameters between separate Constraint Properties. E.g. The *BoilerEnergy* and *BoilerWaterTemperature* Constraint Properties are connected through the *dQb* parameter because the *BoilerEnergy*constraint expression provides a value for the *BoilerWaterTemperature*constraint expression.[IMAGE alt='' src='']

###### Creating parametric constraints automatically

To create parametric constraints automatically

1. Open existing project or create new .
2. Create a Block or it's structure in [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3'] . As shown in the figure, The DC Motor Block is decomposed into Rotation part and inherited DC Power part from DC Device Block. [CONFLUENCE_PAGE title='Decomposing Blocks' space='SYSMLP2024xR3']]]> [ATTACHMENT filename='DC_Motor_Block_structure.png']
3. Right-click the Block for which you want to create SysML Parametric Diagram, select Tools > Parametric Equation Wizard . L [CONFLUENCE_PAGE title='Parametric Equation Wizard' space='SYSMLP2024xR3']]]>
4. Type equation and click the Parse and Map button. The Constraint Block with parameters are created automatically. If the names of Constraint Parameter and Value property are the same, they and mapped automatically. You can change bindings by dragging Constraint Parameters in the left tree onto properties in the right tree. [Learn more about creating Parametric Diagram from an equation >](https://docs.nomagic.com/display/SYSMLP2024xR3/Parametric+Equation+Wizard#ParametricEquationWizard-HowtocreateaParametricDiagramfromanequation) [ATTACHMENT filename='par_diagram_automatically.png']
5. In the SysML Parametric Diagram toolbar, click [IMAGE alt='' src=''] to remap or include additional Value Properties.

1318769283

**Related pages**

**Sample model**

The model used in the figures of this page is the **InvertedPendulum** sample model that comes with SysML. To open this sample do one of the following:

- Download *[ATTACHMENT filename='InvertedPendulum.mdzip'].*
- Find in modeling tool <modeling tool installation directory>\samples\sysml\*Inverted Pendulum\*InvertedPendulum.mdzip.

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5006f5ac-a522-42b3-ab13-241fcc083339"><ac:parameter ac:name="id">1318769284</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d8bf6bf5-07c4-4c57-abd9-949aa0ad4bc6"><ac:parameter ac:name="id">1318769286</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e5ceeba5-4df7-4642-99a9-e998fe487811"><ac:parameter ac:name="id">1299571190</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4b3f54e3-fdf8-406f-9810-da2338ede1b8"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="933b2cc0-c98a-486e-84f9-0ff195573e54"><ac:parameter ac:name="id">1190221077</ac:parameter><ac:rich-text-body><h3><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);"><strong>Introduction</strong></span><br /></span></h3><p>SysML Parametric Diagrams provide a way to integrate engineering analysis models described in mathematical equations and constraints, with design models describing the structural and behavioral aspects of systems. Parametric diagrams include usages of constraint blocks to constrain the properties of another block. A constraint property is a property of any block that is typed by a constraint block. <span style="color: rgb(9,30,66);">To empower the constraint expression to perform calculations, you have to specify what system parameters should be consumed as variables of that constraint.</span></p><p>See the figure below, as example of <ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link> wherein all elements are highlighted: <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Value Properties]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link>, <ac:link><ri:page ri:content-title="Constraint Property" ri:space-key="SYSMLP2024xR3" /></ac:link>, Constraint expression, <ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /></ac:link>, <ac:link><ri:page ri:content-title="Binding Connector" ri:space-key="SYSMLP2024xR3" /></ac:link>.</p><p><ac:image><ri:attachment ri:filename="par_diagram_description.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The main elements used in the SysML Parametric Diagram.</h6><h3><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">Creating parametric constraints</span></span></h3><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">This section explains how to model system constraints in the </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Parametric+Diagram">SysML Parametric Diagram</a><span style="color: rgb(62,63,64);">. Parametric constraints are formulas, and parameters are variables that can be bound to value properties later. Variables can be inputs and outputs of the formula. </span>In general, you must perform the following steps to model your system constraints. However, some actions may already be done in the model creation process, so you may skip these steps and use existing model data. The following procedure provides the main workflow of modeling parametric constraints manually and automatically.</span></p><p>There are two ways to model parametric constraints:</p><ul><li><ac:link ac:anchor="Creating parametric constraints manually"><ac:plain-text-link-body><![CDATA[Manually by creating elements and binding them.]]></ac:plain-text-link-body><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link ac:anchor="Creating parametric constraints automatically"><ac:plain-text-link-body><![CDATA[Automatically by using the Parametric Equation Wizard.]]></ac:plain-text-link-body><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><h4>Creating parametric constraints manually</h4><p>To create parametric constraints manually</p><hr /><ol><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Opening+SysML+projects">Open existing project</a> or <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects">create new</a>.</li><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Defining+Blocks+in+Block+Definition+Diagram">Create a Block</a> or it's structure in <ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Block Definition Diagram]]></ac:plain-text-link-body></ac:link>. As shown in the figure, The <em>DC Motor</em> Block is decomposed into <em>Rotation</em> part and inherited <em>DC Power </em>part from <em>DC Device</em> Block. <ac:link><ri:page ri:content-title="Decomposing Blocks" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more how to decompose Blocks >]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="DC_Motor_Block_structure.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><ac:link><ri:page ri:content-title="Creating and managing Block properties" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Create Value Properties for those Blocks]]></ac:plain-text-link-body></ac:link>. As shown in the figure below, the highlighted Value Properties created for the <em>DC Motor</em>, <em>Rotation</em> and <em>DC Power</em> Blocks. <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Selecting+property+type" style="letter-spacing: 0.0px;">Specify their types</a><span style="letter-spacing: 0.0px;">.</span><br /><em><br /><ac:image><ri:attachment ri:filename="value_properties_for_blocks.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></em></li><li>Right-click the Block and select <strong>Create Diagram</strong> &gt; <strong>SysML Parametric Diagram</strong>. In the opened<a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Displaying+parameters+and+properties"> <strong>Display Parameters/Properties</strong></a> dialog, select either: <br /><ul><li>Part Properties with its Value Properties, if you have enough space on the diagram pane to display part shapes. As example, see the following figure where <em>power</em> Value Property is displayed inside inherited <em>dcPower</em> Part Property shape.</li><li>Only Value Properties, if you need to save a space on the diagram pane. The <ac:link><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[dot notation]]></ac:plain-text-link-body></ac:link> is used in Value Property name instead of part shape. As example, see the following figure where dot notation (<em>rotation.powe</em>r) is used to express the path of <em>power</em> Value Property. <br /><ac:image><ri:attachment ri:filename="displaying_value_properties_on_par_diagram_pane.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul></li><li>Click the <strong>Constraint Property</strong><span> button on the diagram palette and then click the empty place of that diagram pane. An unnamed<a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Property"> Constraint Property</a> is created. Type its name.<br /></span></li><li>Specify Constraint property type by selecting the Constraint Property shape, from the smart manipulator toolbar, click <ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="_buttons" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> and do either:<br /><ul><li>Type a name of a Constraint Block and press Enter. The new Constraint Block is created automatically in the model with an empty Constraint expression. <br /><ac:image><ri:attachment ri:filename="new-constraint_block_with_empty_expression.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br />Double-click {} and type an expression. To make a <ac:link><ri:page ri:content-title="Creating reusable constraint libraries" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[reusable Constraint Block]]></ac:plain-text-link-body></ac:link>, we highly recommend to use different value names than exist in particular model. <span style="color: rgb(62,63,64);">E.g. <em>efficiency=powerOutput/suppliedPower</em>. </span> <span style="color: rgb(62,63,64);"><ac:link><ri:page ri:content-title="Creating Constraint Parameters automatically" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Create parameters automatically from equation]]></ac:plain-text-link-body></ac:link> by clicking </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><ac:image ac:thumbnail="true" ac:alt="Parse and Create Parameters" ac:height="18"><ri:attachment ri:filename="parse_and_create_parameters.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span><span style="color: rgb(62,63,64);"> from Constraint Property smart manipulator toolbar.  As shown in the figure below, three Constraint parameters are created: <em>efficiency</em>, <em>suppliedPower</em>, <em>powerOutput</em>.<br /><ac:image><ri:attachment ri:filename="parsed_and_created_parameters_from_equation.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></li><li>Select <ac:link><ri:page ri:content-title="Creating reusable constraint libraries" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[reusable Constraint Block ]]></ac:plain-text-link-body></ac:link>from the library. The Constraint expression appears automatically.</li></ul></li><li><p class="auto-cursor-target">Connect Value Properties with Constraint Parameters in one of the following way:<br /> - Select the Value Property shape, from smart manipulator toolbar click <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="binding_connector.png"><ri:page ri:content-title="_buttons" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> and c<span style="color: rgb(62,63,64);">onnect it to a </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Property">Constraint Property</a><span style="color: rgb(62,63,64);"> shape. F<span style="color: rgb(62,63,64);">rom the </span><strong>Select Parameter</strong><span style="color: rgb(62,63,64);"> menu list, select an appropriate parameter. As example, see the figure below where <em>power</em> Value Property is binding by selecting a <em>supplierPower</em> parameter from the suggested list.<br /><ac:image><ri:attachment ri:filename="binding_value_properties_with_constraint_parameter1.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /> - <span style="color: rgb(62,63,64);"><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Displaying+parameters+and+properties#Displayingparametersandproperties-Usingthesmartmanipulatortoolbar">Display Constraint Parameters on Constraint Property shape</a> by clicking </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><ac:image ac:thumbnail="true" ac:alt="Display All Parameters" ac:height="20"><ri:attachment ri:filename="display_all_parameters.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span><span style="color: rgb(62,63,64);"> smart manipulator toolbar. </span><span style="color: rgb(62,63,64);"> Select Value Property/Constraint Parameter shape, click <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="binding_connector.png"><ri:page ri:content-title="_buttons" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> and connect it to <span style="color: rgb(62,63,64);">Constraint Parameter/<span style="color: rgb(62,63,64);">Value Property. As shown in the figure elow, the <em>efficiency</em> Value Property is binding with an <em>efficiency</em> parameter.<br /></span></span></span></span></span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="binding_value_properties_with_constraint_parameter2.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p class="auto-cursor-target">The Constraint Parameter are connected with Value Properties using Binding Connector. Now you can r<span style="color: rgb(62,63,64);">un the simulation of parametric data in one of the following way:<br />     - Right-click the Block that owns the Parametric diagram and select </span><strong>Simulation </strong><span style="color: rgb(62,63,64);">&gt; </span><strong>Run</strong><span style="color: rgb(62,63,64);">.<br />     - From the Parametric Diagram toolbar, click <ac:image ac:thumbnail="true" ac:height="24"><ri:attachment ri:filename="Run_button.png"><ri:page ri:content-title="_buttons" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>.<br />In the</span><strong> Variables </strong><span style="color: rgb(62,63,64);">tab, type values and click </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="start_button.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span><span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Parametric evaluator" /><ac:plain-text-link-body><![CDATA[Learn more about parameters simulation >]]></ac:plain-text-link-body></ac:link></span><br /><ac:image><ri:attachment ri:filename="par_diagram.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="de110311-6ab1-4be3-806c-104869de38fe"><ac:rich-text-body><p>You can create an equation system by creating bindings between parameters between separate Constraint Properties. E.g. The <em>BoilerEnergy</em> and <em>BoilerWaterTemperature</em> Constraint Properties are connected through the <em>dQb</em> parameter because the <em>BoilerEnergy </em>constraint expression provides a value for the <em>BoilerWaterTemperature</em><span> constraint expression.</span></p><p><ac:image><ri:attachment ri:filename="equation_system_in_par_diagram.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro></li></ol><div><span style="color: rgb(62,63,64);"><br /></span></div><h4>Creating parametric constraints automatically</h4><p><br /></p><p>To create parametric constraints automatically</p><hr /><ol><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Opening+SysML+projects">Open existing project</a> or <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects">create new</a>.</li><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Defining+Blocks+in+Block+Definition+Diagram">Create a Block</a> or it's structure in <ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Block Definition Diagram]]></ac:plain-text-link-body></ac:link>. As shown in the figure, The <em>DC Motor</em> Block is decomposed into <em>Rotation</em> part and inherited <em>DC Power </em>part from <em>DC Device</em> Block. <ac:link><ri:page ri:content-title="Decomposing Blocks" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more how to decompose Blocks >]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="DC_Motor_Block_structure.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Right-click the Block for which you want to create SysML Parametric Diagram, select <strong>Tools</strong> &gt; <strong>Parametric Equation Wizard</strong>. L<ac:link><ri:page ri:content-title="Parametric Equation Wizard" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[earn more about Parametric Equation Wizard >]]></ac:plain-text-link-body></ac:link></li><li>Type equation and click the <strong>Parse and Map</strong> button. The Constraint Block with parameters are created automatically. If the names of Constraint Parameter and Value property are the same, they and mapped automatically. You can change bindings <span style="color: rgb(51,51,51);">by dragging </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Parameter">Constraint Parameters</a><span style="color: rgb(51,51,51);"> in the left tree onto properties in the right tree. <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Parametric+Equation+Wizard#ParametricEquationWizard-HowtocreateaParametricDiagramfromanequation">Learn more about creating Parametric Diagram from an equation &gt;<br /></a></span><ac:image><ri:attachment ri:filename="par_diagram_automatically.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><span style="color: rgb(51,51,51);">In the SysML Parametric Diagram toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:alt="Parametric Equation Wizard"><ri:attachment ri:filename="parametric_equation_wizard_button.png"><ri:page ri:content-title="Modeling parametric constraints" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> to remap or include additional Value Properties.</span></span></li></ol><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f1051f40-b4ec-4258-90e7-130775d86461"><ac:parameter ac:name="id">1318769283</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="247a3bb0-d970-4cab-af04-cda0e253f9f1" /></p></ac:layout-cell><ac:layout-cell><p><strong>Sample model</strong></p><p>The model used in the figures of this page is the <strong>InvertedPendulum</strong> sample model that comes with SysML. To open this sample do one of the following:</p><ul><li>Download<span class="confluence-link"><em> <ac:link><ri:attachment ri:filename="InvertedPendulum.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link>.<br /></em></span></li><li>Find in modeling tool <em>&lt;modeling tool installation directory&gt;\samples\sysml\<em>Inverted Pendulum\</em>InvertedPendulum.mdzip.</em></li></ul><p><strong><br /></strong></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158671 space=SYSMLP2024xR3 version=1 -->
## PAGE 00244: Modeling structure with Blocks

- page_id: `227158671`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158671/Modeling+structure+with+Blocks
- version_number: 1
- version_date: `2024-01-29T11:18:07.732+01:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

This section describes how to work in two different types of diagrams that will model a structure of systems: the [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3'] (BDD) and [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3'] (IBD). The elements in the BDD are**elements of** **definition**,****while the elements in the IBD are **elements of usage**. Elements of definition describe unique instances and can be reused in multiple contexts to share this definition; e.g., the [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']is a definition and is used as a type in the IBD. The IBD displays usages of [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']that are the [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] and [CONFLUENCE_PAGE title='Reference Property' space='SYSMLP2024xR3'] of the Block. In other words, the Part Properties are the usages of the Block in the context of composing the Block.

Read the following topics to learn how to model your structure:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This section describes how to work in two different types of diagrams that will model a structure of systems: the <ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link> (BDD) and <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link> (IBD). The <span class="confluence-link">elements in the BDD are<strong> elements of</strong> <strong>definition</strong>,<strong> </strong>while the elements in the <span class="confluence-link">IBD are <strong>elements of usage</strong>. Elements of definition describe unique instances and can be reused in multiple contexts to share this definition; e.g., <span class="confluence-link"><span class="confluence-link">the <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Block ]]></ac:plain-text-link-body></ac:link>is a definition and is used as a type in the IBD.</span></span></span></span> The IBD displays usages of <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Blocks ]]></ac:plain-text-link-body></ac:link>that are the <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:content-title="Reference Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Reference Properties]]></ac:plain-text-link-body></ac:link> of the Block. In other words, the Part Properties are the usages of the Block in the context of composing the Block.</p><p>Read the following  topics to learn how to model your structure:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="57ac0c20-3117-4b3e-927b-952e3f931e27" /></p>
````

<!--NOMAGIC_PAGE id=227159757 space=SYSMLP2024xR3 version=1 -->
## PAGE 00245: Moe

- page_id: `227159757`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159757/Moe
- version_number: 1
- version_date: `2016-04-07T09:55:08.956+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

Moe (measure of effectiveness) represents a parameter whose value is critical for achieving the desired cost effectiveness mission.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Moe (measure of effectiveness) represents a parameter whose value is critical for achieving the desired cost effectiveness mission.</p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="29eaba80-4f85-46ba-aaf3-49a5e64ebb85"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159820 space=SYSMLP2024xR3 version=2 -->
## PAGE 00246: Most common shortcut keys

- page_id: `227159820`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159820/Most+common+shortcut+keys
- version_number: 2
- version_date: `2025-05-02T10:28:45.681+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Most common shortcut keys' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="7751aea9-eaca-4f91-b6ab-2c8e2dd370a0"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Most common shortcut keys" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227160284 space=SYSMLP2024xR3 version=2 -->
## PAGE 00247: Nested properties export to the Modelica file

- page_id: `227160284`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160284/Nested+properties+export+to+the+Modelica+file
- version_number: 2
- version_date: `2025-05-02T10:26:38.397+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Modelica export > Advanced Modelica features
- labels: []

### NORMALIZED CONTENT

When using a [CONFLUENCE_PAGE title='Partial model export to the Modelica file' space='SYSMLP2024xR3'], the nested properties can also be exported to the Modelica file.Nested properties are exported in the following rules:

- If nested properties are not displayed (Structure [CONFLUENCE_PAGE title='SysML specific compartments' space='SYSMLP2024xR3'] is disabled), all of them are exported. For example, see the figure below where the vaporGenerationPlant Part Property contains four nested parts (Heating, Evaporation, Radiation, VaporGenerationPlantCalculation) that are exported to the Modelica file. 
[IMAGE alt='' src='']
- If any of the nested elements are displayed (Structure [CONFLUENCE_PAGE title='SysML specific compartments' space='SYSMLP2024xR3'] is enabled), only they are exported, skipping any hidden elements. In the example below, only Heating and Radiation nested parts of the vaporGenerationPlant Part Property are exported to the Modelica file, while any ports and connectors are skipped. [CONFLUENCE_PAGE title='Displaying parts and ports' space='SYSMLP2024xR3']>]]> [IMAGE alt='' src='']

To export nested properties, use the procedure described in the [Partial model export to the Modelica file](https://docs.nomagic.com/display/SYSMLP2024xR3/Partial+model+export+to+the+Modelica+file#PartialmodelexporttotheModelicafile-ProcedureofpartialexporttotheModelicafile)page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">When using a <ac:link><ri:page ri:content-title="Partial model export to the Modelica file" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[partial model export]]></ac:plain-text-link-body></ac:link>, the nested properties can <span style="color: rgb(62,63,64);">also</span> be exported to the Modelica file. </span><span style="color: rgb(62,63,64);">Nested properties are exported in the following rules:</span></p><ul><li><span style="color: rgb(62,63,64);">If nested properties are not displayed (Structure <ac:link><ri:page ri:content-title="SysML specific compartments" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Compartment]]></ac:plain-text-link-body></ac:link> is disabled), all of them are exported. For example, see the figure below where the vaporGenerationPlant Part Property contains four nested parts (Heating, Evaporation, Radiation, VaporGenerationPlantCalculation) that are exported to the Modelica file.<br /><ac:image><ri:attachment ri:filename="all_nested_parts_exported_to_modelica.png"><ri:page ri:content-title="Nested properties export to the Modelica file" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></li><li><span style="color: rgb(62,63,64);">If any of the nested elements are displayed (Structure <ac:link><ri:page ri:content-title="SysML specific compartments" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Compartment]]></ac:plain-text-link-body></ac:link> is enabled), only they are exported, skipping any hidden elements. In the example below, only Heating and Radiation nested parts of the vaporGenerationPlant Part Property are exported to the Modelica file, while any ports and connectors are skipped. <ac:link><ri:page ri:content-title="Displaying parts and ports" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to display parts and ports >>]]></ac:plain-text-link-body></ac:link><br /><br /></span><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="displayed_nested_parts_exported_to_modelica.png"><ri:page ri:content-title="Nested properties export to the Modelica file" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3be444d5-e46b-47a1-86ac-86be36356272"><ac:rich-text-body><p>To export nested properties, use the procedure described in the <span style="letter-spacing: 0.0px;"><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Partial+model+export+to+the+Modelica+file#PartialmodelexporttotheModelicafile-ProcedureofpartialexporttotheModelicafile">Partial model export to the Modelica file </a>page.</span></p></ac:rich-text-body></ac:structured-macro><p /><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159568 space=SYSMLP2024xR3 version=1 -->
## PAGE 00248: No compatible Connector

- page_id: `227159568`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159568/No+compatible+Connector
- version_number: 1
- version_date: `2021-09-14T13:14:15.169+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Behavior to Structure Synchronization
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
<p><strong>Abbreviation</strong></p><p>BehaviorToStructureSync[2]</p><p><strong>Description</strong></p><p>This validation rule checks to see if the Connector exists between the two compatible Proxy Ports that can exchange flowing items found in Activities. </p><p><strong style="letter-spacing: 0.0px;">Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Create Connector</strong> - creates a missing Connector between the two compatible Proxy Ports. </p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="btos_2nd_validation_rule.png"><ri:page ri:content-title="No compatible Connector" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">Creating a Connector that is missing in the Internal Block Diagram.</h6>
````

<!--NOMAGIC_PAGE id=227159566 space=SYSMLP2024xR3 version=1 -->
## PAGE 00249: No compatible Interface

- page_id: `227159566`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159566/No+compatible+Interface
- version_number: 1
- version_date: `2021-09-10T09:56:42.390+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Behavior to Structure Synchronization
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
<p><strong>Abbreviation</strong></p><p>BehaviorToStructureSync[1]</p><p><strong><ac:inline-comment-marker ac:ref="7216feb7-efde-4071-86ed-30df4d49b0fe">Description</ac:inline-comment-marker></strong></p><p>This validation rule detects the Part Properties or containing Blocks of Part Properties having incompatible interfaces in accordance with the flowing items specified in Activities.<strong><br class="_mce_tagged_br" /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><ac:inline-comment-marker ac:ref="d88639d5-40f1-443d-8985-e8e9b51ab799">Diagram</ac:inline-comment-marker><strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Create Port </strong>- creates a new Proxy Port typed by a compatible Interface Block.</li><li><strong>Choose Compatible Interface Block </strong>- changes an already existing Proxy Port type to a compatible Interface Block.</li><li><strong>Add Missing Flow Property </strong>- adds a new Flow Property to an Interface Block that types a Proxy Port.</li><li><strong style="letter-spacing: 0.0px;">Reverse Direction of Port </strong>- changes the Proxy Port direction, thus changing the Flow Property direction of an Interface Block that types a Proxy Port.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="BehaviorToStructureSync_validtion_rule.png"><ri:page ri:content-title="No compatible Interface" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">Part Property<em> : Power</em> and the <ac:inline-comment-marker ac:ref="a06bd8af-81ef-40cf-aa5c-9863cef18b57">enclosing Block </ac:inline-comment-marker><em><ac:inline-comment-marker ac:ref="a06bd8af-81ef-40cf-aa5c-9863cef18b57">Wireless Earbuds</ac:inline-comment-marker></em> after using Behavior to Structure Synchronization solvers.</h6>
````

<!--NOMAGIC_PAGE id=227159570 space=SYSMLP2024xR3 version=1 -->
## PAGE 00250: No compatible Item Flow realization

- page_id: `227159570`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159570/No+compatible+Item+Flow+realization
- version_number: 1
- version_date: `2021-09-14T11:58:12.915+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Behavior to Structure Synchronization
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
<p><strong>Abbreviation</strong></p><p>BehaviorToStructureSync[3]</p><p><strong>Description</strong></p><p>This validation rule checks if Part Properties with correctly typed Proxy Ports and Connectors in the Internal Block Diagrams have compatible Item Flows realized on Connectors.</p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Diagram<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong>Realize Missing Item Flow</strong> - <span style="color: rgb(62,63,64);">creates a new compatible Item Flow or reuses an existing one and then realizes it on the Connector.</span></li><li><strong>Open Item Flow Manager</strong> - opens the <strong>Item Flow Manager</strong> dialog.</li><li><strong>Change Item Flow Realization Compatibility Checking</strong> - opens the <strong>Project Options</strong> dialog to turn on/turn off the Item Flow realization checking. </li></ul><p><strong>Example</strong></p><p><ac:image ac:align="center"><ri:attachment ri:filename="btos_third_validation_rule.png"><ri:page ri:content-title="No compatible Item Flow realization" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Realizing a missing Item Flow on the Connector in the Internal Block Diagram.</h6>
````

<!--NOMAGIC_PAGE id=227159485 space=SYSMLP2024xR3 version=1 -->
## PAGE 00251: No discrete with continuous Activity Edge

- page_id: `227159485`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159485/No+discrete+with+continuous+Activity+Edge
- version_number: 1
- version_date: `2021-02-11T09:53:52.669+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Activities
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
<p><strong>Abbreviation</strong></p><p>Discrete[1]<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks to make sure that the «discrete» and «continuous» stereotypes are not applied to the same Activity Edge at the same time.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Activity Edge<strong><br /></strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, leave only one </span><span style="color: rgb(62,63,64);">«discrete» or «continuous» stereotype applied for the Control Flow or Object Flow.</span><strong><br /></strong></p><p><strong>Example</strong></p><h6 style="text-align: center;"><strong><ac:image ac:align="center"><ri:attachment ri:filename="activityEdge.png"><ri:page ri:content-title="No discrete with continuous Activity Edge" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong><span style="color: rgb(128,128,128);">The</span><em style="text-align: center;"> of8</em><span style="color: rgb(128,128,128);"> Object Flow can have only one «discrete» or «continuous» stereotype applied at the same time.</span><strong><br /></strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159474 space=SYSMLP2024xR3 version=1 -->
## PAGE 00252: No discrete with continuous Object Node

- page_id: `227159474`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159474/No+discrete+with+continuous+Object+Node
- version_number: 1
- version_date: `2021-02-11T09:53:20.183+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Activities
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
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Discrete[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks to see if t</span>he «discrete» and «continuous» stereotypes are applied to the same Object Node at the same time.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Object Node<strong><br /></strong></p><p><strong>Solvers</strong></p><p>To fix this, leave only one «discrete» or «continuous» stereotype applied for the same Object Node at the same time.</p><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="continiuos_discrete.png"><ri:page ri:content-title="No discrete with continuous Object Node" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">The<em> cold dirty</em> Activity Parameter Node can have only one «discrete» or «continuous» stereotype applied at the same time.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159488 space=SYSMLP2024xR3 version=1 -->
## PAGE 00253: No discrete with continuous Parameter

- page_id: `227159488`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159488/No+discrete+with+continuous+Parameter
- version_number: 1
- version_date: `2021-02-11T09:54:04.294+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Activities
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
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>Discrete[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p>This validation rule checks to make sure the «discrete» and «continuous» stereotypes are not applied to the same <span style="color: rgb(62,63,64);">Parameter </span>at the same time.<strong> <br /> </strong></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Parameter<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, leave only one </span><span style="color: rgb(62,63,64);">«discrete» or «continuous» stereotype applied for the same Parameter at the same time.</span> <strong> <br /> </strong></p><p><strong>Example</strong></p><p><strong> <ac:image ac:align="center"><ri:attachment ri:filename="parameter_continuous.png"><ri:page ri:content-title="No discrete with continuous Parameter" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </strong></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">The</span> <em style="text-align: center;"> recovered</em> <span> Parameter can have only one «discrete» or «continuous» stereotype applied at the same time.</span> <strong> <br /> </strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159480 space=SYSMLP2024xR3 version=1 -->
## PAGE 00254: No Overwrite with noBuffer of Object Node

- page_id: `227159480`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159480/No+Overwrite+with+noBuffer+of+Object+Node
- version_number: 1
- version_date: `2021-02-11T09:53:38.111+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Activities
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
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>noBuffer[1]-Overwrite[1]<strong> <br /> </strong></p><p><strong>Description</strong></p><p>This validation rule checks to make sure the «nobuffer» and «overwrite» stereotypes are not applied to the same <span style="color: rgb(62,63,64);">Object Node </span>at the same time.<strong> <br /> </strong></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Object Node<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, leave only one</span> <span style="color: rgb(62,63,64);">«nobuffer» or «overwrite»  stereotype applied for the same Object Node<strong> </strong>at the same time.</span><strong><br /> </strong></p><p><strong>Example</strong></p><h6><strong> <ac:image ac:align="center"><ri:attachment ri:filename="nobuffer_overwrite.png"><ri:page ri:content-title="No Overwrite with noBuffer of Object Node" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </strong></h6><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">The</span> <em style="text-align: center;"> pure</em> <span> Activity Parameter Node can have only one <span>«nobuffer» or «overwrite»</span> stereotype applied at the same time.</span> <strong> <br /> </strong></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159597 space=SYSMLP2024xR3 version=1 -->
## PAGE 00255: No streaming with nonStreaming

- page_id: `227159597`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159597/No+streaming+with+nonStreaming
- version_number: 1
- version_date: `2021-01-06T12:18:50.421+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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
<p><strong>Abbreviation</strong></p><p>streaming[A]-nonStreaming[A]<strong> <br /> </strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule</span><span style="color: rgb(62,63,64);"> checks if t</span> <span style="color: rgb(62,63,64);">he Activity is not stereotyped by</span> <span style="color: rgb(51,51,51);">«s</span> <span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> and <span style="color: rgb(51,51,51);">«nons</span> <span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> at the same time.<strong> <br /> </strong></p><p><strong>Severity</strong></p><p>warning<strong> <br /> </strong></p><p><strong>Constrained Element</strong></p><p>Activity<strong> <br /> </strong></p><p><strong>Solvers</strong></p><p><span style="color: rgb(62,63,64);">To fix this, keep only one <span style="color: rgb(51,51,51);">«s</span><span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> or <span style="color: rgb(51,51,51);">«nons</span><span style="color: rgb(62,63,64);">treaming</span> <span style="color: rgb(51,51,51);">»</span> stereotype applied for the same Activity.</span></p><p><strong>Example</strong></p><p><strong> <ac:image ac:align="center"><ri:attachment ri:filename="streaming_nonStreaming_val_rule.png"><ri:page ri:content-title="No streaming with nonStreaming" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </strong></p><h6 style="text-align: center;">Only «streaming» stereotype is applied for the <em>dry part</em> Activity.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159559 space=SYSMLP2024xR3 version=1 -->
## PAGE 00256: Not Realized Item Flow

- page_id: `227159559`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159559/Not+Realized+Item+Flow
- version_number: 1
- version_date: `2022-05-25T14:50:29.827+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Ports and Flows
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
<p><strong>Abbreviation</strong></p><p>NRIF<strong><br /></strong></p><p><strong>Description</strong></p><p>This validation rule checks if there are any Item Flows in the model that are not realized. <strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Item Flow</p><p><strong>Solvers</strong></p><ul><li><strong>Remove from Model </strong>- removes the <span style="color: rgb(62,63,64);">not realized Item Flow from the model</span>.</li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="Not Realized Item Flow.png"><ri:page ri:content-title="Not Realized Item Flow" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">The Item Flow from the <em>Human-Machine Interaction</em> block to the <em>VCCU</em> block is not realized as it does not contain any realizing elements. <br />The error is resolved via the <strong>Remove from Model</strong> solver.</h6>
````

<!--NOMAGIC_PAGE id=227159758 space=SYSMLP2024xR3 version=1 -->
## PAGE 00257: Objective Function

- page_id: `227159758`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159758/Objective+Function
- version_number: 1
- version_date: `2016-04-07T09:55:51.949+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

An Objective Function (also known as 'optimization' or 'cost function') is used for determining the overall value of an alternative in terms of weighted criteria and/or Moe's.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>An Objective Function (also known as 'optimization' or 'cost function') is used for determining the overall value of an alternative in terms of weighted criteria and/or Moe's.</p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="29eaba80-4f85-46ba-aaf3-49a5e64ebb85"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159599 space=SYSMLP2024xR3 version=1 -->
## PAGE 00258: Obsolete Quantity Kind for QUDV

- page_id: `227159599`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159599/Obsolete+Quantity+Kind+for+QUDV
- version_number: 1
- version_date: `2020-12-07T07:28:39.542+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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

<!--NOMAGIC_PAGE id=227159600 space=SYSMLP2024xR3 version=1 -->
## PAGE 00259: Obsolete Quantity Kind used in Unit for QUDV

- page_id: `227159600`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159600/Obsolete+Quantity+Kind+used+in+Unit+for+QUDV
- version_number: 1
- version_date: `2020-12-07T07:28:51.136+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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

<!--NOMAGIC_PAGE id=227159601 space=SYSMLP2024xR3 version=1 -->
## PAGE 00260: Obsolete Quantity Kind used in Value Type for QUDV

- page_id: `227159601`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159601/Obsolete+Quantity+Kind+used+in+Value+Type+for+QUDV
- version_number: 1
- version_date: `2020-12-07T07:29:01.528+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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

<!--NOMAGIC_PAGE id=227159602 space=SYSMLP2024xR3 version=1 -->
## PAGE 00261: Obsolete Unit for QUDV

- page_id: `227159602`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159602/Obsolete+Unit+for+QUDV
- version_number: 1
- version_date: `2020-12-07T07:29:12.233+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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

<!--NOMAGIC_PAGE id=227159603 space=SYSMLP2024xR3 version=1 -->
## PAGE 00262: Obsolete Unit used in Value Type for QUDV

- page_id: `227159603`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159603/Obsolete+Unit+used+in+Value+Type+for+QUDV
- version_number: 1
- version_date: `2020-12-07T07:29:25.498+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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

<!--NOMAGIC_PAGE id=227158558 space=SYSMLP2024xR3 version=2 -->
## PAGE 00263: Opening SysML projects

- page_id: `227158558`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158558/Opening+SysML+projects
- version_number: 2
- version_date: `2025-05-02T10:28:18.879+02:00`
- ancestors: SysML Plugin Documentation > Getting started
- labels: []

### NORMALIZED CONTENT

565022204

565022207

231040873

**On this page**

33

565022205

[CONFLUENCE_PAGE title='Opening projects' space='MD2024xR3']true

##### Opening sample models

You can use already prepared sample models to try product features, explore diagram examples, or analyze case studies.

To open the sample model

1. Do one of the following: - Open the modeling tool directory <modeling tool installation directory>\samples. - Open your modeling tool and on the right side of the screen select Samples .
2. Select an appropriate sample model. The sample model is opened.

565022203

**Related pages**

- [CONFLUENCE_PAGE title='Working with projects' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5457fe0e-1cda-4039-ab85-f1b3f3a35263"><ac:parameter ac:name="id">565022204</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="106955e2-9d23-4bf2-9636-570ac7332d6b"><ac:parameter ac:name="id">565022207</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c5d78273-9d86-48b1-aceb-be396bc939d7"><ac:parameter ac:name="id">231040873</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e421e6e7-9b8e-4213-88ee-871cb8c8d677"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="94485179-7681-4386-8541-c4d9ed64729f"><ac:parameter ac:name="id">565022205</ac:parameter><ac:rich-text-body><p><br /></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="a82c97f2-6727-4f1c-8e44-8e26c504edd6"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Opening projects" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><h3><span style="color: rgb(62,63,64);">Opening sample models</span></h3><p>You can use already prepared sample models to try product features, explore diagram examples, or analyze case studies.</p><p>To open the sample model</p><hr /><ol><li>Do one of the following:<br />- Open the modeling tool directory <em>&lt;modeling tool installation directory&gt;\samples.<br /></em>- Open your modeling tool and on the right side of the screen select <strong>Samples</strong>.</li><li>Select an appropriate sample model.<br />The sample model is opened.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c916b3d3-ac39-47c1-a292-c719b6936447"><ac:parameter ac:name="id">565022203</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with projects" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158562 space=SYSMLP2024xR3 version=1 -->
## PAGE 00264: Organizing your model

- page_id: `227158562`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158562/Organizing+your+model
- version_number: 1
- version_date: `2024-01-29T11:24:50.651+01:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

Before modeling your system, we strongly recommend that you organize your model structure. The correct organization of packages, diagrams, model libraries, and profiles allows you to reuse them easily, ensures quick navigation, control the access, manage configurations, etc.

For more details read the following pages:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Before modeling your system, we strongly recommend that you organize your model structure. The correct organization of packages, diagrams, model libraries, and profiles allows you to reuse them easily, ensures quick navigation, control the access, manage configurations, etc.</p><p>For more details read the following pages:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7659d5dc-c5b5-41b7-ae44-80916f88c458" /></p>
````

<!--NOMAGIC_PAGE id=227159608 space=SYSMLP2024xR3 version=1 -->
## PAGE 00265: Other validation rules

- page_id: `227159608`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159608/Other+validation+rules
- version_number: 1
- version_date: `2024-04-15T18:36:43.587+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="98c37cb9-5859-4a44-8c02-78085dafb48b" /></p>
````

<!--NOMAGIC_PAGE id=227160298 space=SYSMLP2024xR3 version=1 -->
## PAGE 00266: Overview of the model

- page_id: `227160298`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160298/Overview+of+the+model
- version_number: 1
- version_date: `2020-02-10T09:08:05.846+01:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Sample models > Creating a simple model
- labels: []

### NORMALIZED CONTENT

The electrical circuit is made of three simple components: *a ground*, *an electrical source*, and *a resistor* (see the picture below). The source and the resistor both have two pins, and the ground has one pin. The positive pin of the source is connected to the negative pin of the resistor. The positive pin of the resistor is connected to the negative pin of the source. The ground is also connected to the negative pin of the source.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">The electrical circuit is made of three simple components: <em>a ground</em>, <em>an electrical source</em>, and <em>a resistor</em> (see the picture below). The source and the resistor both have two pins, and the ground has one pin. The positive pin of the source is connected to the negative pin of the resistor. The positive pin of the resistor is connected to the negative pin of the source. The ground is also connected to the negative pin of the source.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="electric_circuite_example.png"><ri:page ri:content-title="Overview of the model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p />
````

<!--NOMAGIC_PAGE id=227159048 space=SYSMLP2024xR3 version=1 -->
## PAGE 00267: Parametric Equation Wizard

- page_id: `227159048`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159048/Parametric+Equation+Wizard
- version_number: 1
- version_date: `2020-09-29T12:00:32.909+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling parametric constraints
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Information

19092521

#### CONTENT-COLUMN: Information

19092526

19212971

**On this page**

**3**

#### CONTENT-BLOCK: Information

19092525

You can automatically create the SysML Parametric Diagram with elements from a mathematicalequation by usingthe **Parametric Equation Wizard**.It parses the equation and creates a [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'] with named [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3']. The wizard analyzes underlying [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] structures and finds matching [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] in nested structures.

##### Description of the Parametric Equation Wizard areas

The **Parametric Equation Wizard** consists of the following:

- The *Constraint expression box* allows you to type or paste single or multiple mathematical equations which define the parameters you want to parse, create, and bind with properties (e.g. [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'], other [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3'],[CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3']).You can also modify the equation after clicking the **Parse and Map** button. Editing constraint expression- If you add new parameters to a preexisting equation, they are created after clicking the **Parse and Map** button.- If you remove parameters from a preexisting equation, they remain in the mapping area after clicking the **Parse and Map** button.
- The *Contextual equation area* shows the equationfrom the constraint expression box where parameter names are substituted with actual bindings. This areaincreases the readability of the parsed expression and allows you to evaluate binding correctness. Parameter substitution rules- If a parameter name already exists in the model and is connected (via Binding Connector) with another property (Value Property,Constraint Parameter, Part Property), theparameter is substituted with a property path (e.g. *altitude* is substituted with *apollo.altitude*).- If a parameter is new, its name is shown as defined in the constraint expression box.
- The *Mapping area* displays the bindings between parameters inthe *left tree* and propertiesin the *right tree*. It allows you to review and change existing mapping by re-binding, creating new bindings, or deleting them. AllBinding Connectors are shown in the *binding area*. Binding map rulesUse the following rules to create an automatic binding map according to parameter name:Exact name matches have priority over partial name matches.Upper level properties have priority over deep nested value properties.

[IMAGE alt='' src='']

###### Three main areas (highlighted in orange) in the Parametric Equation Wizard: constraint expression, contextual equation, and mapping. The mapping area contains the left and right trees and binding area.

##### How to create a Parametric Diagram from an equation

To create a SysML Parametric Diagram from a mathematicalequation

1. Open the**Parametric Equation Wizard** using one of the following:
  - From the shortcut menu of the [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] or [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'], select **Tools** > **Parametric Equation Wizard**. [ATTACHMENT filename='parametric_equation_wizard_button_from_block.png']
  - In the SysML Parametric Diagram toolbar, click [IMAGE alt='' src=''].
  - Open the SysML Parametric Diagram and press Ctrl+Alt+P.
  - In the Containment tree, select Constraint Block and drag it on the SysML Parametric Diagrampane.
2. Inthe constraint expression box, type or paste single or multiple mathematical equations(see example below).
3. Click the **Parse and Map** button (see example below). InformationIf you modify the equation in the constraint expression box, use this button to refresh the data in the Contextual Equation and mapping areas.
4. (Optional) In the Contextual Equation area, evaluate the correctness of the parsed expression (see example below).
5. (Optional) In the mapping area, review binding suggestions, and, if needed, do the following (see example below): - Modify them by dragging [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3'] in the left tree onto properties in the right tree. 
 - Delete them by selecting the [CONFLUENCE_PAGE title='Binding Connector' space='SYSMLP2024xR3'] and either: 
 - Click the **Delete** button at the bottom of the binding area; 
 - Press the **Delete** button in the keyboard.
6. Click **OK**(see example below). The SysML Parametric Diagram with [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'] (default name *ConstraintBlock*), named [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3'], and properties connected via the [CONFLUENCE_PAGE title='Binding Connector' space='SYSMLP2024xR3'], are created.

##### Example

The example below demonstrates the creation of the *MoonLanding* Parametric Diagram from the equation *gravity=g*mass/(altitude+radius)^2*. The new [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'] (default name *ConstraintBlock*) with five [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3'] (names from equation: *g*, *radius*, *mass*, *altitude*, and *gravity*) are created and connected via [CONFLUENCE_PAGE title='Binding Connector' space='SYSMLP2024xR3'] with [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] (match names with parameter names: *g*, *radius*, *mass*, *altitude*, and *gravity*).

[IMAGE alt='' src='']

###### The main steps, highlighted in orange, in the Parametric Equation Wizard when creating the SysML Parametric Diagram from mathematical equation.

19092518

**Related pages**

- [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Creating Constraint Parameters automatically' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Displaying parameters and properties' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Enforce Ports Compatibility mode' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Constraint Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Binding Connector' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']

****

**Sample model**

The sample model used in the figures on this page is the**Moon Landing**sample model.Download [ATTACHMENT filename='MoonLanding.mdzip'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c6ff401d-55d5-491c-8d53-eaf863734582"><ac:parameter ac:name="id">19092521</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="96dec900-d987-4a4a-bbdc-ac4b326241e1"><ac:parameter ac:name="id">19092526</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="81711d7e-78b6-4353-8f25-35f90ef25b12"><ac:parameter ac:name="id">19212971</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="b2fe48af-bb71-46d0-ba2a-9b04d662227a"><ac:parameter ac:name="maxLevel">3</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ca10165d-de07-407b-b563-852b0e9dcae1"><ac:parameter ac:name="id">19092525</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">You can automatically create the SysML Parametric Diagram with elements</span> <span style="color: rgb(51,51,51);">from a <span style="color: rgb(51,51,51);">mathematical </span>equation by using </span>the <strong>Parametric Equation Wizard</strong>.<span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> </span></span></span><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">It parses the equation and creates a <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link> with named <ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Constraint Parameters]]></ac:plain-text-link-body></ac:link></span>. The wizard analyzes underlying <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link> structures and finds matching <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Value Properties]]></ac:plain-text-link-body></ac:link> in <span style="color: rgb(51,51,51);">nested structures</span>.</span></span></span></span></span></span></span></span></span></p><h3><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Description of the <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Parametric Equation Wizard</span></span></span></span> areas<br /></span></span></span></h3><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">The <span style="color: rgb(51,51,51);"><strong>Parametric Equation Wizard</strong></span> consists of the following:</span></span></span></p><ul><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">The <em>Constraint expression box</em> allows you to type or paste single or multiple mathematical equations which define the parameters you want to parse, create, and bind with p<span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">roperties</span></span></span></span></span></span> (e.g. <span style="color: rgb(51,51,51);"><ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Value Properties]]></ac:plain-text-link-body></ac:link>, <span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> other <ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Constraint Parameters]]></ac:plain-text-link-body></ac:link>, </span></span></span></span></span></span></span><span class="confluence-link"><span style="color: rgb(51,51,51);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link></span></span></span></span></span></span></span></span>).</span><span style="color: rgb(51,51,51);"> <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">You can also modify the equation after clicking the <strong>Parse and Map</strong> button.</span><br /></span></span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a0aea4dc-e4e3-4968-bdab-6502007a0e6a"><ac:parameter ac:name="title">Editing constraint expression</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">- If you <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">add new parameters to a <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">preexisting equation</span></span></span>, they are created after clicking the <span style="color: rgb(51,51,51);"><strong>Parse and Map</strong> button.</span><br /></span></span></span></span></p><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">- If you remove parameters from a preexisting equation, they remain in the mapping</span> area <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">after clicking the <span style="color: rgb(51,51,51);"><strong>Parse and Map</strong> button</span></span></span></span>.</span></span></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><br class="auto-cursor-target" /></span></p></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">The <em>Contextual equation area</em> shows the equation </span><span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);">from the constraint expression box where parameter names are substituted with actual bindings. This area </span></span><span style="color: rgb(51,51,51);">increases the readability of the parsed expression and allows you to evaluate binding correctness.</span><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fce7c1ec-8fb8-4499-9c82-7ebc1b910dd2"><ac:parameter ac:name="title">Parameter substitution rules</ac:parameter><ac:rich-text-body><p><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> <span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);">- If <span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);">a parameter</span></span></span> name <span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);">already exists in the model and is connected (via Binding Connector) with</span></span></span> another property (<span style="color: rgb(51,51,51);">Value Property,<span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> Constraint Parameter, Part Property</span></span></span></span></span></span>), the </span>parameter is substituted with a property path (e.g. <em>altitude</em> is substituted with <em>apollo.altitude</em>).</span></span></span></span></span></span></span></span></p><p><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);">- If a parameter is new, its name is shown as defined in the constraint expression box.</span></span></span></span></span></span></span></span></p></ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target"><span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);">The <em>Mapping area</em> displays the bindings between parameters in<span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> the <em>left tree</em></span></span></span></span></span></span> and p<span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">roperties </span></span></span></span></span></span></span></span></span></span><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">in the <em>right tree</em></span></span></span></span></span></span>. It allows you to review and change existing mapping by re-binding, creating new bindings, or deleting them. All </span><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Binding Connectors are shown in the <em>binding area</em>. </span></span></span></span></span></span></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9fd80d07-3947-4fc2-a13e-75c6231e2991"><ac:parameter ac:name="title">Binding map rules</ac:parameter><ac:rich-text-body><p><span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Use the following rules to create an automatic binding map <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">according to parameter name:</span></span></span></span></span><br /></span></span></span></span></span></span></span></p><ul><ul><li>Exact name matches have priority over partial name matches.</li><li>Upper level properties have priority over deep nested value properties.</li></ul></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(255,0,0);"><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span class="auto-cursor-target" style="color: rgb(51,51,51);"><br /></span></span></span></span></span></span></span></p></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="parametric_equation_wizard_areas_1.png"><ri:page ri:content-title="Parametric Equation Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Three main areas (highlighted in orange) in the Parametric Equation Wizard: constraint expression, contextual equation, and mapping. The mapping area contains the left and right trees and binding area.</h6><h3><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">How to create <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">a Parametric Diagram</span></span> <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">from an equation</span></span></span><br /></span></span></h3><p><span style="color: rgb(51,51,51);">To create <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">a SysML Parametric Diagram</span></span> <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">from a <span style="color: rgb(51,51,51);">mathematical </span>equation</span></span></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Open the<span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><strong> Parametric Equation Wizard</strong> <span style="color: rgb(51,51,51);">using one of the following:</span></span></span></span><br /><ul><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">From the shortcut menu of the <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link> or <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link>, select <strong>Tools</strong> &gt; <span style="color: rgb(51,51,51);"><strong>Parametric Equation Wizard</strong></span>.<br /></span></p><ac:image><ri:attachment ri:filename="parametric_equation_wizard_button_from_block.png"><ri:page ri:content-title="Parametric Equation Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><p class="auto-cursor-target"><br /></p></li><li><span style="color: rgb(51,51,51);">In the <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">SysML Parametric Diagram</span></span> toolbar, click <ac:image ac:title="Parametric Equation Wizard" ac:alt="Parametric Equation Wizard"><ri:attachment ri:filename="parametric_equation_wizard_button.png"><ri:page ri:content-title="Parametric Equation Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>.</span></li><li><span style="color: rgb(51,51,51);">Open the <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">SysML Parametric Diagram</span></span></span> and press Ctrl+Alt+P.</span></li><li><span style="color: rgb(51,51,51);">In the Containment tree, select Constraint Block and drag it on the <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">SysML Parametric Diagram</span></span> </span>pane.<br /></span></li></ul></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">In<span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> the <span style="color: rgb(51,51,51);">constraint expression box</span></span></span></span>, type or paste single or multiple mathematical equations<span style="color: rgb(51,51,51);"> (see example below).<br /></span></span></span></span></span></p></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Click the <strong>Parse and Map</strong> button <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">(see example below)</span></span></span></span></span>.<br /></span></span></span></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="62ff99b8-63a0-4dd8-965a-18d7c14bc563"><ac:parameter ac:name="title">Information</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">If you modify the equation <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">in the constraint expression box</span></span></span></span></span></span></span></span>, use this button to refresh the data in the Contextual Equation and mapping areas. </span></span></span></span></span></span></span></span></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span class="auto-cursor-target" style="color: rgb(51,51,51);"><br /></span></span></span></p></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> (Optional) In the Contextual Equation area</span></span></span>, evaluate the correctness of the parsed expression</span></span></span></span></span></span></span></span></span></span></span></span></span> <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">(see example below)</span></span></span></span></span>.</p></li><li><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">(Optional) In the mapping area, review binding suggestions, and, if needed, do the following <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">(see example below)</span></span></span></span></span>:</span></span></span><br /><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> - Modify them by dragging <ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Constraint Parameters]]></ac:plain-text-link-body></ac:link> in the left tree onto properties in the right tree.<br /> - Delete them by selecting the <ac:link><ri:page ri:content-title="Binding Connector" ri:space-key="SYSMLP2024xR3" /></ac:link> and either:<br />          - Click <span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"> the <strong>Delete</strong> button at the bottom of the binding area; <br />          - Press the <strong>Delete</strong> button in the keyboard.</span></span></span></span></span></span><br /></span></span></span></li><li><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Click <strong>OK </strong><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">(see example below)</span></span></span></span></span>.</span></span></span><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><br />The <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">SysML Parametric Diagram</span></span></span> with <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link> (default name <em>ConstraintBlock</em>), named <ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Constraint Parameters]]></ac:plain-text-link-body></ac:link>, and properties connected via the <ac:link><ri:page ri:content-title="Binding Connector" ri:space-key="SYSMLP2024xR3" /></ac:link>, are created.</span></span></span></li></ol><h3><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Example<br /></span></span></span></h3><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">The example below demonstrates the creation of the <em>MoonLanding</em> Parametric Diagram from the equation <em>gravity=g*mass/(altitude+radius)^2</em>. The new <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link> (default name <em>ConstraintBlock</em>) with five <ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Constraint Parameters]]></ac:plain-text-link-body></ac:link> (names from equation: <em>g</em>, <em>radius</em>, <em>mass</em>, <em>altitude</em>, and <em>gravity</em>) <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">are created</span></span></span> and connected via <ac:link><ri:page ri:content-title="Binding Connector" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Binding Connectors]]></ac:plain-text-link-body></ac:link> with <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Value Properties]]></ac:plain-text-link-body></ac:link> (match names with parameter names: <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><em>g</em>, <em>radius</em>, <em>mass</em>, <em>altitude</em>, and <em>gravity</em></span></span></span>).<br /></span></span></span></p><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><ac:image ac:align="center"><ri:attachment ri:filename="creating_parametric_diagram_from_equation.png"><ri:page ri:content-title="Parametric Equation Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></span></span></p><h6 style="text-align: center;">The main steps, highlighted in orange, in the Parametric Equation Wizard when creating the SysML Parametric Diagram from mathematical equation.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0f9ceb0d-6fae-4c81-9676-7600fda879d8"><ac:parameter ac:name="id">19092518</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Creating Constraint Parameters automatically" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Displaying parameters and properties" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Enforce Ports Compatibility mode" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Constraint Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><span><span><span><span><span><span><span><span><span><span><ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></span></span></span></span></span></span></span></span></li><li><ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Binding Connector" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><span><span><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span><span><span><span><ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></span></span></span></span></span></span></li><li><span><span><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span><span><span><span><span><span><ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></span></span></span></span></span></span></span></span></li><li><span><span><span style="color: rgb(255,0,0);"><span style="color: rgb(51,51,51);"><span><span><span><span><span><span><span><ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></span></span></span></span></span></span></span></span></span></li></ul><p><strong><br /></strong></p></ac:layout-cell><ac:layout-cell><p><span><strong>Sample model</strong><br /></span></p><p><span>The sample model used in the figures on this page is the </span><strong>Moon Landing </strong><span>sample model. </span><span class="confluence-link"><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span><span class="confluence-link"><span><span><span><span><span><span><span>Download <ac:link><ri:attachment ri:filename="MoonLanding.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link>.</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159759 space=SYSMLP2024xR3 version=1 -->
## PAGE 00268: Part Property

- page_id: `227159759`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159759/Part+Property
- version_number: 1
- version_date: `2017-06-29T15:45:24.248+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

A Part Property is a property that specifies a part with strong ownership and coincidental lifetime of its containing Block. It describes a local usage or a role of the typing Block in the context of the containing Block. Every Part Property has composite AggregationKind and is typed by a Block. Part Properties are displayed in the **parts** compartment.

[IMAGE alt='' src='']

After setting a Block as a type for a Part Property the Composite Association is automatically created. You can see it in the Compartment area under the Relations node.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Part Property is a property that specifies a part with strong ownership and coincidental lifetime of its containing Block. It describes a local usage or a role of the typing Block in the context of the containing Block. Every Part Property has composite AggregationKind and is typed by a Block. Part Properties are displayed in the <strong>parts</strong> compartment.<span style="color: rgb(255,0,0);"><br /></span></p><p><ac:image ac:title="Part Property" ac:alt="Part Property"><ri:attachment ri:filename="part_property.png"><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2ab3bfb9-15b2-4025-822b-44daca5d92e9"><ac:rich-text-body><p>After setting a Block as a type for a Part Property the Composite Association is automatically created. You can see it in the Compartment area under the Relations node.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> </p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ad1d2f29-7ddc-4427-be11-2022073a6b8a"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227160229 space=SYSMLP2024xR3 version=2 -->
## PAGE 00269: Partial model export to the Modelica file

- page_id: `227160229`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160229/Partial+model+export+to+the+Modelica+file
- version_number: 2
- version_date: `2025-05-02T10:26:37.532+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Modelica export
- labels: []

### NORMALIZED CONTENT

139005951

139005963

154226034

**On this page**

**5**

139005953

##### Intoduction

You can export to Modelica file only parts, ports, and connectors displayed in the[CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3'].The mechanism generates Modelica (.mo) file with an IBD name and save it to your file directory. See the following figure as example of export result and difference between whole (exporting Block) and partial (exporting IBD) model export. After the *Circuit* IBD export, only displayed parts are exported: *Source*, *Resistor*, *Capacitor* and *Ground*. Differently, when exporting the *Circuit* Block - all parts are exported: *Source*, *Resistor*, *Capacitor*,*Inductor*,*Resistor* and *Ground.*[CONFLUENCE_PAGE title='Modelica export' space='SYSMLP2024xR3']>]]>

[IMAGE alt='' src='']

###### The difference between whole (exporting Block) and partial (exporting IBD) export.

##### Procedure of partial export to the Modelica file

You can use the [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3'] to select what to export to Modelica. Prepare the IBD by modifying an existing or creating a new one and [CONFLUENCE_PAGE title='Displaying parts and ports' space='SYSMLP2024xR3'] automatically. Follow the procedure below, to export the Inetrnal Block Diagram to the *.mo file.

To export a part of model to the Modelica file

1. Create new or modify existing Internal Block Diagram by displaying elements you want to export. Nested properties can also be exported. [CONFLUENCE_PAGE title='Nested properties export to the Modelica file' space='SYSMLP2024xR3']>]]>
2. Do one of the following:
  - In the [CONFLUENCE_PAGE title='Model Browser' space='SYSMLP2024xR3'] , select the Internal Block Diagram and i n the top-left corner of the modeling tool, click File > Export To > Modelica .
  - Right-click an empty space on the Internal Block Diagram [CONFLUENCE_PAGE title='Understanding the user interface' space='SYSMLP2024xR3'] and click Tools > Export to Modelica .
  - In the [CONFLUENCE_PAGE title='Model Browser' space='SYSMLP2024xR3'] , right-click the Internal Block Diagram and click Tools > Export to Modelica .
3. In the Modelica Export Options dialog, specify export options. Option descriptions >>
4. Click OK . The Modelica (.mo) file is generated and saved to your file directory.

139011299

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9758b5ef-dc52-4f74-aa31-00a81de58270"><ac:parameter ac:name="id">139005951</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="25262d90-02d1-469e-80c3-7a665df506f0"><ac:parameter ac:name="id">139005963</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="58a3b83e-5c3d-45d1-9c83-1fa818132987"><ac:parameter ac:name="id">154226034</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="1fc86838-c2b7-4fcd-bccc-d85acf34339e"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ce8fe7bf-9ba4-4ca5-85b5-0e47dffd9be6"><ac:parameter ac:name="id">139005953</ac:parameter><ac:rich-text-body><h3>Intoduction</h3><p>You can export to Modelica file only parts, ports, and connectors displayed in the<ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[ Internal Block Diagram]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);">. </span>The mechanism generates Modelica (.mo) file with an IBD name and save it to your file directory. See the following figure as example of export result and difference between whole (exporting Block) and partial (exporting IBD) model export. After the <em>Circuit</em> IBD export, only displayed parts are exported: <em>Source</em>, <em>Resistor</em>, <em>Capacitor</em> and <em>Ground</em>. Differently, when exporting the <em>Circuit</em> Block - all parts are exported: <em>Source</em>, <em>Resistor</em>, <em>Capacitor</em>,<em> Inductor</em>,<em> Resistor</em> and <em>Ground. </em><ac:link><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to export the whole model >>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="ibd_and_block_export_to_modelica.png"><ri:page ri:content-title="Partial model export to the Modelica file" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The difference between whole (exporting Block) and partial (exporting IBD) export.</span></h6><h3><span style="color: rgb(62,63,64);">Procedure of partial export to the Modelica file</span></h3><p><span style="color: rgb(62,63,64);">You can use the <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Internal Block Diagram]]></ac:plain-text-link-body></ac:link> to select what to export to Modelica. Prepare the IBD by modifying an existing or creating a new one and <ac:link><ri:page ri:content-title="Displaying parts and ports" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[display parts and ports]]></ac:plain-text-link-body></ac:link> automatically. Follow the procedure below, to export the Inetrnal Block Diagram to the *.mo file.</span></p><p><span style="color: rgb(62,63,64);"><span style="color: rgb(23,43,77);">To export a part of model to the Modelica file</span></span></p><hr /><ol><li class="auto-cursor-target"><p class="auto-cursor-target">Create new or modify existing Internal Block Diagram by displaying elements you want to export.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="81c9bc56-e804-4ce5-ae91-441285b272c3"><ac:rich-text-body><p>N<span style="color: rgb(62,63,64);">ested properties can also be exported. <ac:link><ri:page ri:content-title="Nested properties export to the Modelica file" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Read the rules of nested properties export to the Modelica file >>]]></ac:plain-text-link-body></ac:link></span></p></ac:rich-text-body></ac:structured-macro></li><li class="auto-cursor-target">Do one of the following:<br /><ul><li>In the <ac:link><ri:page ri:content-title="Model Browser" ri:space-key="SYSMLP2024xR3" /></ac:link>, select the Internal Block Diagram and i<span style="color: rgb(62,63,64);">n the top-left corner of the modeling tool, </span>click <strong>File</strong> &gt;<strong> Export To &gt; Modelica</strong>.</li><li>Right-click an empty space on the Internal Block Diagram <ac:link><ri:page ri:content-title="Understanding the user interface" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[pane]]></ac:plain-text-link-body></ac:link> and click <strong>Tools </strong>&gt; <strong>Export to Modelica</strong>.<strong><br /></strong></li><li>In the <ac:link><ri:page ri:content-title="Model Browser" ri:space-key="SYSMLP2024xR3" /></ac:link>, right-click the Internal Block Diagram and click <strong>Tools</strong> &gt; <strong>Export to Modelica</strong>.<strong><br /></strong></li></ul></li><li>In the <strong>Modelica Export Options</strong> dialog, specify export options. <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Modelica+export#Modelicaexport-ModelicaExportOptions">Option descriptions &gt;&gt;</a></li><li class="auto-cursor-target">Click <strong>OK</strong>.<br />The Modelica (.mo) file is generated and saved to your file directory.</li></ol><p class="auto-cursor-target" /></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a30af21a-cf13-4fb3-beb3-28e2de2622a3"><ac:parameter ac:name="id">139011299</ac:parameter><ac:rich-text-body /></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159761 space=SYSMLP2024xR3 version=2 -->
## PAGE 00270: Participant Property

- page_id: `227159761`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159761/Participant+Property
- version_number: 2
- version_date: `2025-05-02T10:26:36.044+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

1448744391

1448744393

1448744392

Participant properties can be the ends of connectors owned by an [CONFLUENCE_PAGE title='Association Block' space='SYSMLP2024xR3']. The keyword «participant» before a property name indicates the property is stereotyped by *ParticipantProperty*. The types of participant properties can be elided if desired. They are always the same as the corresponding association end type.

1448744390

**Related pages**

- Creating Association Block
- Using Association Block as Connector type

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="fc19e3cd-e9cf-44f2-93fb-a7a0197c7b59"><ac:parameter ac:name="id">1448744391</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9f8a9df4-117b-435c-93e3-ef1a9822be2f"><ac:parameter ac:name="id">1448744393</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4967739c-945d-4d95-82e9-2b92b88573c0"><ac:parameter ac:name="id">1448744392</ac:parameter><ac:rich-text-body><p>Participant properties can be the ends of connectors owned by an <span class="confluence-link"><ac:link><ri:page ri:content-title="Association Block" ri:space-key="SYSMLP2024xR3" /></ac:link></span>. The keyword «participant» before a property name indicates the property is stereotyped by <em>ParticipantProperty</em>. The types of participant properties can be elided if desired. They are always the same as the corresponding association end type.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c1ebab86-aecb-4013-b47c-09cf9ed3275f"><ac:parameter ac:name="id">1448744390</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Defining+Blocks+in+Block+Definition+Diagram#DefiningBlocksinBlockDefinitionDiagram-CreatingAssociationBlock">Creating Association Block</a></li><li><a class="current" href="https://docs.nomagic.com/display/SYSMLP2024xR3/Using+Association+Block+as+Connector+type">Using Association Block as Connector type</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159762 space=SYSMLP2024xR3 version=2 -->
## PAGE 00271: Performance Requirement

- page_id: `227159762`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159762/Performance+Requirement
- version_number: 2
- version_date: `2025-05-02T10:28:43.095+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Performance Requirement' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="e064fc05-4a65-4432-83c0-8e096b333194"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Performance Requirement" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0c1ba8be-02de-439e-a133-dcd946d3f307"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159604 space=SYSMLP2024xR3 version=1 -->
## PAGE 00272: PerformanceRequirement satisfied by an invalid element

- page_id: `227159604`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159604/PerformanceRequirement+satisfied+by+an+invalid+element
- version_number: 1
- version_date: `2021-01-06T12:24:33.014+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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
<p><strong>Abbreviation</strong></p><p>performanceRequirement[1]<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This validation rule </span><span style="color: rgb(62,63,64);">checks if the Performance <ac:inline-comment-marker ac:ref="e99f472b-03e9-46d1-bbfe-264d3f54a2e0">Requirement</ac:inline-comment-marker> is s</span>atisfied by a Value Property.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Performance Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><ul><li><strong><strong>Remove invalid Satisfy relationship(s) </strong></strong><span style="color: rgb(62,63,64);">- deletes not valid Satisfy relationship from the model.</span><strong><br class="_mce_tagged_br" /></strong></li></ul><p><strong>Example</strong></p><p><strong><ac:image ac:align="center"><ri:attachment ri:filename="perform_req_val_rule.png"><ri:page ri:content-title="PerformanceRequirement satisfied by an invalid element" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">The <em>Pad Thickness</em> Performance Requirement is satisfied by <em>thickness</em> Value Property.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159763 space=SYSMLP2024xR3 version=2 -->
## PAGE 00273: Physical Requirement

- page_id: `227159763`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159763/Physical+Requirement
- version_number: 2
- version_date: `2025-05-02T10:28:43.204+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Physical Requirement' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="d638171a-37e6-4162-8ea6-18968899871d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Physical Requirement" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227158610 space=SYSMLP2024xR3 version=1 -->
## PAGE 00274: Predefined Metric Suites

- page_id: `227158610`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158610/Predefined+Metric+Suites
- version_number: 1
- version_date: `2019-05-06T13:49:03.860+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management > Requirement coverage analysis
- labels: []

### NORMALIZED CONTENT

1924697218

1924697220

1924697219

A Metric Suite is the collection of parameters and metric definitions used to calculate metrics that evaluate specific aspects of your model. For your convenience, there are seven predefined Metric Suites. The following figure shows predefined Metric Suites and their purposes.

[IMAGE alt='' src='']

###### The diagram shows that some Metric Suites treat the owner Requirement as a grouping element, and some treat the owner as a Requirement.

**Requirement Derivation (the owner is treated as a grouping element)**

This Metric Suite checks the outgoing Derive relationships and tracks whether Requirements are derived or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:

- If the grouping Requirement has an outgoing Derive relationship, the owned Requirements are treated as derived.
- If all the owned Requirements have outgoing Derived relationships, the grouping Requirement is treated as derived.

**Requirement Refinement (the owner is treated as a grouping element)**

This Metric Suite checks the incoming Refine relationships and tracks whether Requirements are refined or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:

- If the grouping Requirement has an incoming Refine relationship, the owned Requirements are treated as refined.
- If all the owned Requirements have incoming Refined relationships, the grouping Requirement is treated as refined.

**Requirement Satisfaction (the owner is treated as a grouping element)**

This Metric Suite checks the incoming Satisfy relationships and tracks whether Requirements are satisfied or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:

- If the grouping Requirement has an incoming Satisfy relationship, the owned Requirements are treated as satisfied.
- If all the owned Requirements have incoming Satisfy relationships, the grouping Requirement is treated as satisfied.

[IMAGE alt='' src='']

###### The diagram illustrates what Requirements are satisfied if you use the **Requirement Satisfaction** Metric Suite when the owner is treated as a grouping element.

**Requirement Verification (the owner is treated as a grouping element)**

This Metric Suite checks the incoming Verify relationships and tracks whether Requirements are verified or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:

- If the grouping Requirement has an incoming Verify relationship, the owned Requirements are treated as verified.
- If all the owned Requirements have incoming Verify relationships, the grouping Requirement is treated as verified.

**Requirement Refinement (the owner is treated as a Requirement)**

This Metric Suite checks the incoming Refine relationships and tracks whether Requirements are refined or not. All Requirements are treated as independent under the following conditions:

- If the grouping Requirement has an incoming Refine relationship, the owned Requirements are not treated as refined unless they have incoming refine relationships.
- If all the owned Requirements have incoming Refined relationships, the grouping Requirement is not treated as refined unless it has an incoming Refine relationship.

**Requirement Verification (the owner is treated as a Requirement)**

This Metric Suite checks the incoming Verify relationships and tracks whether Requirements are verified or not. All Requirements are treated as independent under the following conditions:

- If the grouping Requirement has an incoming Verify relationship, the owned Requirements are not treated as verified unless they have incoming Verify relationships.
- If all the owned Requirements have incoming Verify relationships, the grouping Requirement is not treated as verified unless it has an incoming Verify relationship.

**Requirement Satisfaction (the owner is treated as a Requirement)**

This Metric Suite checks the incoming Satisfy relationships and tracks whether Requirements are satisfied or not. All Requirements are treated as independent under the following conditions:

- If the grouping Requirement has an incoming Satisfy relationship, the owned Requirements are not treated as satisfied unless they have incoming Satisfy relationships.
- If all the owned Requirements have incoming Satisfy relationships, the grouping Requirement is not treated as satisfied unless it has an incoming Satisfy relationship.

[IMAGE alt='' src='']

###### The diagram illustrates which Requirements are satisfied if you use the**Requirement Satisfaction**Metric Suite when the owner is treated as a Requirement.

1924697217

**Related pages**

- [CONFLUENCE_PAGE title='Requirement coverage analysis' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Predefined Metric Suites for MagicGrid' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bfe39114-2391-41de-9ee1-90bc9135e09a"><ac:parameter ac:name="id">1924697218</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cb40f9b2-024a-4f0e-8d93-af36ccc59b56"><ac:parameter ac:name="id">1924697220</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c6730dbe-7999-4178-9edc-0bdcd65463b1"><ac:parameter ac:name="id">1924697219</ac:parameter><ac:rich-text-body><p>A Metric S<ac:inline-comment-marker ac:ref="e4cc661e-22ce-450a-b864-f87a39977832">uite</ac:inline-comment-marker> is the collection of parameters and metric definitions used to calculate metrics that evaluate specific aspects of your model. For your convenience, there are seven predefined Metric Suites. The following figure shows predefined Metric Suites and their purposes.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="predefined_sysml_metric_suites.png"><ri:page ri:content-title="Predefined Metric Suites" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The diagram shows that some Metric Suites treat the owner Requirement as a grouping element, and some treat the owner as a Requirement.</h6><p><strong>Requirement Derivation (the owner is treated as a grouping element)</strong></p><p>This Metric Suite checks the outgoing Derive relationships and tracks whether Requirements are derived or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:</p><ul><li>If the grouping Requirement has an outgoing Derive relationship, the owned Requirements are treated as derived.</li><li>If all the owned Requirements have outgoing Derived relationships, the grouping Requirement is treated as derived.</li></ul><p><strong><br />Requirement Refinement (the owner is treated as a grouping element)</strong></p><p>This Metric Suite checks the incoming Refine relationships and tracks whether Requirements are refined or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:</p><ul><li>If the grouping Requirement has an incoming Refine relationship, the owned Requirements are treated as refined.</li><li>If all the owned Requirements have incoming Refined relationships, the grouping Requirement is treated as refined.</li></ul><p><strong><br />Requirement Satisfaction (the owner is treated as a grouping element)</strong></p><p>This Metric Suite checks the incoming Satisfy relationships and tracks whether Requirements are satisfied or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:</p><ul><li>If the grouping Requirement has an incoming Satisfy relationship, the owned Requirements are treated as satisfied.</li><li>If all the owned Requirements have incoming Satisfy relationships, the grouping Requirement is treated as satisfied.</li></ul><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="treat_owner_as_grouping_element.png"><ri:page ri:content-title="Predefined Metric Suites" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The diagram illustrates what Requirements are satisfied if you use the <strong>Requirement Satisfaction</strong> Metric Suite when the owner is treated as a grouping element.</h6><p><strong>Requirement Verification (the owner is treated as a grouping element)</strong></p><p>This Metric Suite checks the incoming Verify relationships and tracks whether Requirements are verified or not. The grouping Requirement is not treated as an independent Requirement under the following conditions:</p><ul><li>If the grouping Requirement has an incoming Verify relationship, the owned Requirements are treated as verified.</li><li>If all the owned Requirements have incoming Verify relationships, the grouping Requirement is treated as verified.</li></ul><p><strong><br />Requirement Refinement (the owner is treated as a Requirement)</strong></p><p>This Metric Suite checks the incoming Refine relationships and tracks whether Requirements are refined or not. All Requirements are treated as independent under the following conditions:</p><ul><li>If the grouping Requirement has an incoming Refine relationship, the owned Requirements are not treated as refined unless they have incoming refine relationships.</li><li>If all the owned Requirements have incoming Refined relationships, the grouping Requirement is not treated as refined unless it has an incoming Refine relationship.</li></ul><p><strong><br />Requirement Verification (the owner is treated as a Requirement)</strong></p><p>This Metric Suite checks the incoming Verify relationships and tracks whether Requirements are verified or not. All Requirements are treated as independent under the following conditions:</p><ul><li>If the grouping Requirement has an incoming Verify relationship, the owned Requirements are not treated as verified unless they have incoming Verify relationships.</li><li>If all the owned Requirements have incoming Verify relationships, the grouping Requirement is not treated as verified unless it has an incoming Verify relationship.</li></ul><p><strong><br />Requirement Satisfaction (the owner is treated as a Requirement)</strong></p><p>This Metric Suite checks the incoming Satisfy relationships and tracks whether Requirements are satisfied or not. All Requirements are treated as independent under the following conditions:</p><ul><li>If the grouping Requirement has an incoming Satisfy relationship, the owned Requirements are not treated as satisfied unless they have incoming Satisfy relationships.</li><li>If all the owned Requirements have incoming Satisfy relationships, the grouping Requirement is not treated as satisfied unless it has an incoming Satisfy relationship.</li></ul><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="treat_owner_as_requirement.png"><ri:page ri:content-title="Predefined Metric Suites" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(94,108,132);">The diagram illustrates which Requirements are satisfied if you use the </span><strong style="text-align: center;">Requirement Satisfaction</strong><span style="color: rgb(94,108,132);"> Metric Suite when the owner is treated as a Requirement.</span></h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c6fafbcd-8b2c-4508-bc8e-f935b3154f42"><ac:parameter ac:name="id">1924697217</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Requirement coverage analysis" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Predefined Metric Suites for MagicGrid" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158614 space=SYSMLP2024xR3 version=1 -->
## PAGE 00275: Predefined Metric Suites for MagicGrid

- page_id: `227158614`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158614/Predefined+Metric+Suites+for+MagicGrid
- version_number: 1
- version_date: `2024-01-29T11:32:37.998+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management > Requirement coverage analysis
- labels: []

### NORMALIZED CONTENT

MagicGrid is an MBSE method developed by No Magic, Inc.The MagicGrid approach is based on a framework consisting of viewpoints and aspects organized in a grid view. Each cell of the grid is an artifact to deliver in the systems engineering process. The method is based on existing studies in the field and real-life findings in managing models for organizations from different systems engineering domains.

MagicGrid contains a number of predefined MetricSuites that you can use to calculate Requirement coverage and Requirement covering elements. To learn more about the predefined Metric Suites for MagicGrid, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(24,24,24);">MagicGrid is an MBSE method developed by No Magic, Inc.<span style="color: rgb(24,24,24);"> The MagicGrid approach is based on a framework consisting of viewpoints and aspects organized in a grid view. Each cell of the grid is an artifact to deliver in the systems engineering process. The method is based on existing studies in the field and real-life findings in managing models for organizations from different systems engineering domains.</span></span></p><p>MagicGrid contains a number of predefined MetricSuites that you can use to calculate Requirement coverage and Requirement covering elements. To learn more about the predefined Metric Suites for MagicGrid, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="4661523d-70b6-48ed-ac5b-c53ea1713e94" /></p>
````

<!--NOMAGIC_PAGE id=227159685 space=SYSMLP2024xR3 version=3 -->
## PAGE 00276: Predefined Relation Maps

- page_id: `227159685`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159685/Predefined+Relation+Maps
- version_number: 3
- version_date: `2025-05-02T10:28:40.768+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Additional relation map

410587739

#### CONTENT-COLUMN: Additional relation map

410587741

410587738

****

#### CONTENT-BLOCK: Additional relation map

410587740

You can use all predefined relation maps to represent the traceability of system requirements and design elements. The main purpose of relation maps is to review and analyze relations among the elements and create new elements directly in the relation map. It is a special kind of diagram that automatically updates and renders an element's dependency tree according to predefined dependency criteria. You can create five kinds of predefined relation maps:

- [CONFLUENCE_PAGE title='Predefined Relation Maps' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Predefined Relation Maps' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Predefined Relation Maps' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Predefined Relation Maps' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Predefined Relation Maps' space='SYSMLP2024xR3'] .

You can create predefined relation maps only if you have the [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR3'] installed. [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='SYSMLP2024xR3']>]]>

The different purposes for each relation map are illustrated below:

- activityActivity Decomposition Map displays an Activity decomposition of the selected context. You can review, analyze, and decompose the Activities. The example below is created by using the [ATTACHMENT filename='distiller model.mdzip'] sample model that only comes with [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR3'] . [ATTACHMENT filename='activity_decomposition_map.png']
- structureStructure Decomposition Map displays the decomposition of the [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] related through the Composition relationship of the specified context. You can review, analyze, and decompose the Part Properties . The example below is created by using the [ATTACHMENT filename='VehicleStructure.mdzip'] sample model that only comes with [CONFLUENCE_PAGE title='Cameo Simulation Toolkit Documentation' space='CST2024xR3'] . [ATTACHMENT filename='structure_decomposition_map .png']

- instanceInstance Map displays a hierarchy of the [CONFLUENCE_PAGE title='Instance Specification' space='MD2024xR3'] of the selected context. You can review and analyze the hierarchy of Instance Specifications . The example below is created by using the [ATTACHMENT filename='SpacecraftMassRollup_HTMLTable.mdzip'] sample model that only comes with [CONFLUENCE_PAGE title='Cameo Simulation Toolkit Documentation' space='CST2024xR3'] . [ATTACHMENT filename='instance_map.png']

- containRequirement Containment Map displays the decomposition of the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3'] related through the [CONFLUENCE_PAGE title='Containment' space='MD2024xR3']Containmentrelationship of the specified context. You can review, analyze, and decompose the Requirements. The example below is created by using the [ATTACHMENT filename='hybrid sport utility vehicle.mdzip'] sample model that only comes with the [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR3'] . [ATTACHMENT filename='requirement_containment_map.png']

- deriveRequirement Derivation Map displays the decomposition of [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']that are related trough the [CONFLUENCE_PAGE title='Derive' space='SYSMLP2024xR3']relationship. You can review, analyze, and create Derive relationships among the Requirements. The example below is created by using the [ATTACHMENT filename='hybrid sport utility vehicle.mdzip'] sample model that only comes with the [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR3'] . [ATTACHMENT filename='requirement_derivation_map .png']

#### NOTE: Additional relation map

Additional relation map

You can also create a Relation Map Diagram if you want a rapid review, analysis, and creation of relationships among the elements of the entire model. [CONFLUENCE_PAGE title='Relation Map' space='MD2024xR3']>]]>

[CONFLUENCE_PAGE title='Relation Map' space='MD2024xR3']true

410601788

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1a103d20-4750-4ed6-bce9-c5e8793365ce"><ac:parameter ac:name="id">410587739</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2c83b2cc-3571-4232-b47d-fae1da7b234b"><ac:parameter ac:name="id">410587741</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="29cd928b-07f1-4c74-a8ee-5e23afa669dd"><ac:parameter ac:name="id">410587738</ac:parameter><ac:rich-text-body><p><strong><br /></strong></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8fa0b3ac-883d-4226-85da-178d65de722f"><ac:parameter ac:name="id">410587740</ac:parameter><ac:rich-text-body><p>You can use all predefined relation maps to represent the traceability of system requirements and design elements. The main purpose of relation maps is to review and analyze relations among the elements and create new elements directly in the relation map. <ac:inline-comment-marker ac:ref="51569211-b970-4514-86d1-0bb347c0154a">It is a special kind of diagram that automatically updates and renders an element's dependency tree according to predefined dependency criteria</ac:inline-comment-marker>. You can create five kinds of predefined relation maps:</p><ul><li><ac:link ac:anchor="activity"><ac:plain-text-link-body><![CDATA[Activity Decomposition Map]]></ac:plain-text-link-body><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link ac:anchor="structure"><ac:plain-text-link-body><![CDATA[Structure Decomposition Map]]></ac:plain-text-link-body><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link ac:anchor="instance"><ac:plain-text-link-body><![CDATA[Instance Map]]></ac:plain-text-link-body><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link ac:anchor="contain"><ac:plain-text-link-body><![CDATA[Requirement Containment Map]]></ac:plain-text-link-body><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link ac:anchor="derive"><ac:plain-text-link-body><![CDATA[Requirement Derivation Map]]></ac:plain-text-link-body><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ac:link>.<br /><br /></li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="8092e735-c113-4d66-8ef9-c3015e2e68c1"><ac:rich-text-body><p>You can create predefined relation maps only if you have the <ac:link><ri:page ri:content-title="SysML Plugin Documentation" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Plugin]]></ac:plain-text-link-body></ac:link> installed. <ac:link><ri:page ri:content-title="Installation, licensing, and system requirements" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[How to install SysML Plugin >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>The different purposes for each relation map are illustrated below:</p><ul><li><strong><ac:inline-comment-marker ac:ref="1b9168df-6e59-4a54-a7d4-e13e4ce0ebf6"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="08a37ef0-37fc-46ed-9eaa-ea70ce245b19"><ac:parameter ac:name="">activity</ac:parameter></ac:structured-macro>Activity Decomposition Map</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="1b9168df-6e59-4a54-a7d4-e13e4ce0ebf6"> displays an Activity decomposition of the selected context. You can review, analyze, and decompose the Activities.</ac:inline-comment-marker> The example below is created by using the <ac:link><ri:attachment ri:filename="distiller model.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link> sample model that only comes with <ac:link><ri:page ri:content-title="SysML Plugin Documentation" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Plugin]]></ac:plain-text-link-body></ac:link>.<br /><ac:image><ri:attachment ri:filename="activity_decomposition_map.png"><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="43e1dcf0-2167-4d76-b14a-86615b67cc04"><ac:parameter ac:name="">structure</ac:parameter></ac:structured-macro>Structure Decomposition Map</strong> displays the decomposition of the <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link> related through the <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Defining+Blocks+in+Block+Definition+Diagram#DefiningBlocksinBlockDefinitionDiagram-comp">Composition relationship</a> of the specified context. You can review, analyze, and decompose the <span class="confluence-link">Part Properties</span>. The example below is created by using the <ac:link><ri:attachment ri:filename="VehicleStructure.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link> sample model that only comes with <ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Cameo Simulation Toolkit Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Simulation Toolkit]]></ac:plain-text-link-body></ac:link>.<br /><ac:image><ri:attachment ri:filename="structure_decomposition_map .png"><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul><ul><li><strong><ac:inline-comment-marker ac:ref="9ac914de-d6cb-447d-b06c-c42bfaac5325"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7beb20ec-6fd3-49c3-8c8c-96b9bf0d9e0f"><ac:parameter ac:name="">instance</ac:parameter></ac:structured-macro>Instance Map</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="9ac914de-d6cb-447d-b06c-c42bfaac5325"> displays a hierarchy of the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance Specification" /><ac:plain-text-link-body><![CDATA[Instance Specifications]]></ac:plain-text-link-body></ac:link> of the selected context. You can review and analyze the hierarchy of Instance Specifications</ac:inline-comment-marker>. The example below is created by using the <ac:link><ri:attachment ri:filename="SpacecraftMassRollup_HTMLTable.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link>  sample model that only comes with <ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Cameo Simulation Toolkit Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Simulation Toolkit]]></ac:plain-text-link-body></ac:link>.<br /><ac:image><ri:attachment ri:filename="instance_map.png"><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul><ul><li><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="1bd99818-ab9c-4808-81a7-907bb58ed659"><ac:parameter ac:name="">contain</ac:parameter></ac:structured-macro>Requirement Containment Map</strong> displays the decomposition of the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements]]></ac:plain-text-link-body></ac:link> related through the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Containment" /><ac:link-body><span class="confluence-link">Containment </span>relationship</ac:link-body></ac:link> of the specified context. You can review, analyze, and decompose the Requirements. The example below is created by using the<em> </em><ac:link><ri:attachment ri:filename="hybrid sport utility vehicle.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link> sample model that only comes with the <ac:link><ri:page ri:content-title="SysML Plugin Documentation" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Plugin]]></ac:plain-text-link-body></ac:link>.<br /><ac:image><ri:attachment ri:filename="requirement_containment_map.png"><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul><ul><li><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="0a003e61-05d4-4094-9621-c18ace7a273d"><ac:parameter ac:name="">derive</ac:parameter></ac:structured-macro>Requirement Derivation Map</strong> <ac:inline-comment-marker ac:ref="7f285766-8348-4774-99ed-9177242f2cbc">displays the decomposition of <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements ]]></ac:plain-text-link-body></ac:link>that are related trough the <ac:link><ri:page ri:content-title="Derive" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Derive ]]></ac:plain-text-link-body></ac:link>relationship. You can review, analyze, and create Derive relationships among the Requirements.</ac:inline-comment-marker> The example below is created by using the <ac:link><ri:attachment ri:filename="hybrid sport utility vehicle.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link> sample model that only comes with the <ac:link><ri:page ri:content-title="SysML Plugin Documentation" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Plugin]]></ac:plain-text-link-body></ac:link>.<br /><ac:image><ri:attachment ri:filename="requirement_derivation_map .png"><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c4b78ee3-eaff-4989-928d-b5291f16943b"><ac:parameter ac:name="title">Additional relation map</ac:parameter><ac:rich-text-body><p>You can also create a Relation Map Diagram if you want a rapid review, analysis, and creation of relationships among the elements of the entire model. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Relation Map" /><ac:plain-text-link-body><![CDATA[Lean more about Relation Map Diagram >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="4eeb09c8-5102-4421-bfcf-db11fc914daf"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Relation Map" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7530512c-e7dd-4428-98e0-82f544e1ba22"><ac:parameter ac:name="id">410601788</ac:parameter><ac:rich-text-body /></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158668 space=SYSMLP2024xR3 version=1 -->
## PAGE 00277: Preview Affected Diagrams dialog

- page_id: `227158668`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158668/Preview+Affected+Diagrams+dialog
- version_number: 1
- version_date: `2024-03-19T18:40:14.886+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Item Flow management
- labels: []

### NORMALIZED CONTENT

The **Preview Affected Diagrams** dialog is dedicated to reviewing the diagrams that will be affected when the Item Flow is realized. The dialog can be opened from the following:

- [CONFLUENCE_PAGE title='Creating Item Flow' space='SYSMLP2024xR3']Create/Edit Item Flowdialog
- [CONFLUENCE_PAGE title='Item Flow Manager dialog' space='SYSMLP2024xR3']

[IMAGE alt='' src='']

The **Preview Affected Diagrams** dialog contains all the affected diagrams. You can preview them one by one. The affected elements where the created flows will be realized, are marked in the diagram preview pane.

While previewing the diagrams, you can select the **Update Diagram** check box for those diagrams you want to show the Conveyed Items of the selected flow.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(23,43,77);">The <strong>Preview Affected Diagrams</strong> dialog is dedicated to reviewing the diagrams that will be affected when the Item Flow is realized. The dialog can be opened from the following:</span></p><ul><li><ac:link><ri:page ri:content-title="Creating Item Flow" ri:space-key="SYSMLP2024xR3" /><ac:link-body>Create/Edit Item Flow<span style="color: rgb(23,43,77);"><span> </span>dialog</span></ac:link-body></ac:link></li><li><span style="color: rgb(23,43,77);"><ac:link><ri:page ri:content-title="Item Flow Manager dialog" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Item Flow Manager]]></ac:plain-text-link-body></ac:link></span></li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="preview_affected_diagrams_dialog.png"><ri:page ri:content-title="Preview Affected Diagrams dialog" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p><span><br /></span></p><p><span>The <strong>Preview Affected Diagrams</strong> dialog contains all the affected diagrams. You can preview them one by one. The affected elements where the created flows will be realized, are marked in the diagram preview pane.</span></p><p><span style="color: rgb(23,43,77);">While previewing the diagrams, you can select the <strong>Update Diagram</strong> check box for those diagrams you want to show the Conveyed Items of the selected flow.</span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227158547 space=SYSMLP2024xR3 version=2 -->
## PAGE 00278: Properties tab

- page_id: `227158547`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158547/Properties+tab
- version_number: 2
- version_date: `2025-05-02T10:28:18.640+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

236382134

236382136

236382135

[CONFLUENCE_PAGE title='Properties tab' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3079efb0-ec3b-4154-a953-92ced5ffe686"><ac:parameter ac:name="id">236382134</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="73597c88-c662-4528-b6fc-d944bc16007b"><ac:parameter ac:name="id">236382136</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="40f396b1-56c6-4061-af1a-2df5a50808ea"><ac:parameter ac:name="id">236382135</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="33679c82-0c6d-462f-9682-5f811d850d01"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Properties tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158725 space=SYSMLP2024xR3 version=3 -->
## PAGE 00279: Property path notation

- page_id: `227158725`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158725/Property+path+notation
- version_number: 3
- version_date: `2025-05-02T10:28:21.489+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Decomposing Blocks
- labels: ['shorthand-notation']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Additional information

1096932076

#### CONTENT-COLUMN: Additional information

1096932078

1096932074

**On this page**

43

#### CONTENT-BLOCK: Additional information

1096932077

When modeling deeply nested structures, you can display nested properties within a system hierarchy in the [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3'] and [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3']. You can represent nested properties by displaying the property shape inside another property shape. For example, on the left side of the figure below, the *wheel*, *brake*, and *caliper* are nested parts represented as nested [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] shapes. Representing deeply nested properties in this manner requires a lot of space in the diagram.

Alternatively, you can represent nested properties by using dot notation, which expresses a structural hierarchy compactly in the form of a text string. Dot notation references a nested property accessible through a sequence of intermediate properties from a referencing context. The name of the referenced property is built by a string of names separated by “.”, resulting in a path name that identifies the property in its local context. This notation is purely a notational shorthand for a property that could otherwise be shown within a structure of nested property shapes. For example, on the right side of the figure below, the nested parts are represented using dot notation with the higher-level part names (*vehicle*, *wheel*, and *brake)*.

The meaning of both of them is the same: *caliper* is a part of *brake* which is a part of *wheel*; *wheel* is a part of *vehicle*.

###### [IMAGE alt='' src='']Two alternative ways to represent nested parts in the SysML Internal Block Diagram*.*

#### INFO: Additional information

Additional information

The representation of nested properties with dot notation form is used on [CONFLUENCE_PAGE title='Lifeline' space='MD2024xR3'] and in [CONFLUENCE_PAGE title='Instance table' space='MD2024xR3'] column headers.

When working with nested properties, manage them as follows:

43

##### Displaying type names in a property path

The dot notation separates the property names. However, there are many situations when properties are unnamed (see the right side of the figure below).

[IMAGE alt='' src='']

###### The representation of a property path with dot notation of nested part*s*when they are unnamed.

If you use an earlier version than 18.5, you must set the option which shows type names in a property path with dot notation. For a new project, this option is enabled by default.

To show type names in the property path

1. Select Options > Project .
2. In the [CONFLUENCE_PAGE title='Project options' space='MD2024xR3']**Project Options** dialog , set the Show Type Names in Nested Path option to true . The type names of the nested parts are shown in the property path by separating them with a colon (:).

For example, after enabling the **Show Type Names in Nested Path** option, the part with dot notation, on the right side of the figure, provides information about nested part types.

[IMAGE alt='' src='']

###### The property type names are shown in the property path with dot notation*.*

##### Converting nested properties to dot notation

You can convert nested properties from the system structure to dot notation form.

To convert nested properties to dot notation form

- Select the nested property shape from the property shape structure, drag it to the empty space on the diagram pane, and in the Question dialog, click the Represent as Shortcut button. [ATTACHMENT filename='converting_nested_part_to_dot_notation_form.png']
- Open the **Display Parts/Ports** dialog or **Display Parameters/Properties** dialog , select an appropriate deep nested property in the element tree, and click OK . [ATTACHMENT filename='nested_part_in_display_parts_ports_dialog.png'] The nested property is displayed in dot notation form. [ATTACHMENT filename='part_with_dot_notation.png']

##### Converting properties with dot notation to a structure of nested properties

You can convert a property shape displayed with dot notation form to a nested properties structure.

To convert properties with dot notation form to a nested properties structure

1. From the property shortcut menu, select Refactor > Convert to Nested Parts . The property with dot notation is converted to a structure of nested properties.

[IMAGE alt='' src='']

###### The part *caliper* represented with dot notation is converted to a nested structure of Part Properties.

##### Moving a part from the diagram to a structure compartment

You can move a property shape with dot notation from the diagram back to the [CONFLUENCE_PAGE title='Compartments' space='MD2024xR3'] of a nested property.

To move a property with dot notation to the compartments of a nested property

1. Select the property shape with dot notation.
2. Drag it to the structure compartments. The property is moved to the structure compartments and shown in dot notation form.

[IMAGE alt='' src='']

###### The part *caliper* is moved back to the nested property compartments.

1096957352

**Related pages**

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Displaying parts and ports' space='SYSMLP2024xR3']Displaying parts and ports
- [CONFLUENCE_PAGE title='Displaying parameters and properties' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Connecting parts through interface' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Reference Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3']Value Property
- [CONFLUENCE_PAGE title='Constraint Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Flow Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Participant Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Bound Reference' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Distributed Property' space='SYSMLP2024xR3']

**Sample model**

The model used in the figures of this page is the**Car Braking Analysis**sample model.Download [ATTACHMENT filename='CarBrakingAnalysis.mdzip'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="00b54571-36fe-4e3a-865f-1c20f6d44a6a"><ac:parameter ac:name="id">1096932076</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b251e2f1-b39c-46a2-9cfa-19fefb554d72"><ac:parameter ac:name="id">1096932078</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="45840aff-4a33-4be8-b551-504adf82594c"><ac:parameter ac:name="id">1096932074</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="adfde56a-12ea-43f4-9b87-5ace60f7d547"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c551df07-6c7a-4026-9151-15f749dda8dd"><ac:parameter ac:name="id">1096932077</ac:parameter><ac:rich-text-body><p>When modeling deeply nested structures, you can display nested properties within a system hierarchy in the <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link> and <ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link>. You can represent nested properties by displaying the property shape inside another property shape. For example, on the left side of the figure below, the <em>wheel</em>, <em>brake</em>, and <em>caliper</em> are nested parts represented as nested <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /></ac:link> shapes. Representing deeply nested properties in this manner requires a lot of space in the diagram.</p><p>Alternatively, you can represent nested properties by using dot notation, which expresses a structural hierarchy compactly in the form of a text string. Dot notation references a nested property accessible through a sequence of intermediate properties from a referencing context. The name of the referenced property is built by a string of names separated by “.”, resulting in a path name that identifies the property in its local context. This notation is purely a notational shorthand for a property that could otherwise be shown within a structure of nested property shapes. For example, on the right side of the figure below, the nested parts are represented using dot notation with the higher-level part names (<em>vehicle</em>, <em>wheel</em>, and <em>brake)</em>.</p><p>The meaning of both of them is the same: <em>caliper</em> is a part of <em>brake</em> which is a part of <em>wheel</em>; <em>wheel</em> is a part of <em>vehicle</em>.</p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="representation_of_nested_parts.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>Two alternative ways to represent nested parts in the SysML Internal Block Diagram<em style="text-align: center;">.</em></h6><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b99d68d4-6e0f-4046-ab4a-4eed7eb57881"><ac:parameter ac:name="title">Additional information</ac:parameter><ac:rich-text-body><p>The representation of nested properties with dot notation form is used on <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Lifeline" /><ac:plain-text-link-body><![CDATA[Lifelines]]></ac:plain-text-link-body></ac:link> and in <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance table" /><ac:plain-text-link-body><![CDATA[Instance Table]]></ac:plain-text-link-body></ac:link> column headers.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>When working with nested properties, manage them as follows:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="5bbf7368-4a4e-4eef-9ba3-a8fd8ce990cd"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><h3>Displaying type names in a property path</h3><p>The dot notation separates the property names. However, there are many situations when properties are unnamed (see the right side of the figure below).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="unnamed_parts.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The representation of a property path with dot notation of nested part<em>s </em>when they are unnamed.</h6><p>If you use an earlier version than 18.5, you must set the option which shows type names in a property path with dot notation. For a new project, this option is enabled by default.</p><p>To show type names in the property path</p><hr /><ol><li>Select <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Project options" /><ac:link-body><strong>Project Options</strong> dialog</ac:link-body></ac:link>, set the <strong>Show Type Names in Nested Path</strong> option to <em>true</em>.<br />The type names of the nested parts are shown in the property path by separating them with a colon (:).</li></ol><p>For example, after enabling the <strong>Show Type Names in Nested Path</strong> option, the part with dot notation, on the right side of the figure, provides information about nested part types.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="show_type_names_in_property_path.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The property type names are shown in the property path with dot notation<em style="text-align: center;">.</em></h6><h3>Converting nested properties to dot notation</h3><p>You can convert nested properties from the system structure to dot notation form.</p><p>To convert nested properties to dot notation form</p><hr /><ul><li>Select the nested property shape from the property shape structure, drag it to the empty space on the diagram pane, and in the <strong>Question</strong> dialog, click the <strong>Represent as Shortcut</strong> button.<br /><ac:image><ri:attachment ri:filename="converting_nested_part_to_dot_notation_form.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Open the <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Displaying+parts+and+ports#Displayingpartsandports-UsingtheDisplayParts/Portsdialog"><strong>Display Parts/Ports</strong> dialog</a> or <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Displaying+parameters+and+properties#Displayingparametersandproperties-UsingtheDisplayParameters/Propertiesdialog"><strong>Display Parameters/Properties</strong> dialog</a>, select an appropriate deep nested property in the element tree, and click <strong>OK</strong>.<br /><ac:image><ri:attachment ri:filename="nested_part_in_display_parts_ports_dialog.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br />The nested property is displayed in dot notation form.<br /><ac:image><ri:attachment ri:filename="part_with_dot_notation.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul><h3>Converting properties with dot notation to a structure of nested properties</h3><p>You can convert a property shape displayed with dot notation form to a nested properties structure.</p><p>To convert properties with dot notation form to a nested properties structure</p><hr /><ol><li>From the property shortcut menu, select <strong>Refactor</strong> &gt; <strong>Convert to Nested Parts</strong>.<br />The property with dot notation is converted to a structure of nested properties.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="convert_to_nested_parts.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The part <em>caliper</em> represented with dot notation is converted to a nested structure of Part Properties.</h6><h3>Moving a part from the diagram to a structure compartment</h3><p>You can move a property shape with dot notation from the diagram back to the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Compartments" /><ac:plain-text-link-body><![CDATA[compartments]]></ac:plain-text-link-body></ac:link> of a nested property.</p><p>To move a property with dot notation to the compartments of a nested property</p><hr /><ol><li>Select the property shape with dot notation.</li><li>Drag it to the structure compartments.<br />The property is moved to the structure compartments and shown in dot notation form.</li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="move_part_with_dot_notation_to_compartments.png"><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The part <em>caliper</em> is moved back to the nested property compartments.</h6></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9b2e0923-8777-4291-a1f4-5a2ae2fabc78"><ac:parameter ac:name="id">1096957352</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related  pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Displaying parts and ports" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">Displaying parts and ports</span> </ac:link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Displaying parameters and properties" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Connecting parts through interface" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Reference Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">Value Property</span> </ac:link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Constraint Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Flow Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Participant Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Bound Reference" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Distributed Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><strong>Sample model</strong></p><p class="auto-cursor-target"><span>The model used in the figures of this page is the </span><strong>Car Braking Analysis</strong><span> sample model. </span><span>Download <ac:link><ri:attachment ri:filename="CarBrakingAnalysis.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link>.</span></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158772 space=SYSMLP2024xR3 version=2 -->
## PAGE 00280: Provided and Required Interfaces

- page_id: `227158772`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158772/Provided+and+Required+Interfaces
- version_number: 2
- version_date: `2025-05-02T10:28:22.640+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Defining interfaces using ports
- labels: []

### NORMALIZED CONTENT

1332950711

1332950713

1332950712

Provided/Required Interfaces help to identify compatible ports that can be connected together in the [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']. On a port, you can:

43

##### Creating provided and required interfaces

To create new Provided/Required Interface of a port

1. Do one of the following:
  - Right-click any kind of port shape and from the shortcut menu select Specification . In the [CONFLUENCE_PAGE title='Specification window' space='MD2024xR3'] , select the Provided/Required Interfaces property group.
  - Select a Port shape and from its smart manipulator, click [ATTACHMENT filename='provided_required_interfaces.png'] .
2. In the Provided/Required Interfaces pane, click the Add button and select either Provided or Required.
3. Two situations are available:

- 
  - If the port is typed, the Select Interface dialog opens (see the following figure). In this dialog you can do the following:
    - Select and existing interface (and flow specifications) to be used as the Provided / Required Interface of the port.
    - Make sure the Creation Mode is switched on, click the Create button, and select Interface . In the specification window, type its name, and click Close . The new interface is created. Select it to be used as the Provided / Required Interface of the port. [ATTACHMENT filename='select_interface_dialog.png']
  - If the port is not typed, the Select Port Type dialog opens (see the following figure). You can do the following:
    - Set provided interface as port type (for Provided Interface only). The Select Interface dialog opens. In this dialog, you can either choose an existing interface or create a new one, to be used as the Provided Interface and the type of the port.
    - Create “dummy” port type automatically . The Select Interface dialog opens. In this dialog, you can either choose an existing interface or create a new one, to be used as the Provided or Required Interface of the port. In addition, a dummy classifier, realizing (for Provided) or using (for Required) the interface, is automatically created and used as the type of the port.
    - Select or create port type manually . If you select this option, the Select Port Type dialog opens. In this dialog, choose a classifier to be used as the type of the port. Click OK , the Select Interface dialog opens. In this dialog, you either choose an existing interface or create a new one, to be used as the Provided or Required Interface of the port. In addition, a Realization (or Usage) dependency is automatically created from the port type to the Provided (or Required) Interface of the port. [ATTACHMENT filename='select_port_type.png']

##### Displaying provided/required interfaces

To display provided/required interfaces

1. Select the port shape that has the provided/required interfaces you want to display.
2. Do one of the following: - From the port shortcut menu, select Display > Display Provided/Required Interfaces . - On the diagram toolbar, click [IMAGE alt='' src=''] and select Display Provided/Required Interfaces . The Required/Provided Interfaces are displayed on the port, in the form of ball-socket (lollipop) notation.

Ports can provide or require many interfaces, therefore, you can choose which ones to display or hide. Use the [CONFLUENCE_PAGE title='SysML specific compartments' space='SYSMLP2024xR3']**Edit Compartment** dialog to manage the visibility of these interfaces.

1332950710

**Related pages**

****

**Sample model**

The model used in the figure of this page is the **Inverted****Pendulum** sample model. To open this sample do one of the following:

- Download *[InvertedPendulum.mdzip](https://docs.nomagic.com/download/attachments/9919520/InvertedPendulum.mdzip?version=1&modificationDate=1498477335401&api=v2).*
- Find in modeling tool <modeling tool installation directory>\samples\SysML\Inverted Pendulum\Inverted Pendulum.mdzip.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9091fc32-9a1a-417d-b116-fcaaec8c95a0"><ac:parameter ac:name="id">1332950711</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f4cd19b0-77ef-4dbb-8d58-24f279b193f9"><ac:parameter ac:name="id">1332950713</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="069651a1-bec6-4843-908d-cc0b0e7bfa7c"><ac:parameter ac:name="id">1332950712</ac:parameter><ac:rich-text-body><p>Provided/Required Interfaces help to identify compatible ports that can be connected together in the <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link>. On a port, you can:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="663eb1c9-1737-41bc-b4f4-5aa6091bd10c"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><h3>Creating provided and required interfaces</h3><p>To create new Provided/Required Interface of a port</p><hr /><ol><li>Do one of the following:<br /><ul><li>Right-click any kind of port shape and from the shortcut menu select <strong>Specification</strong>. In the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specification window" /></ac:link>, select the <strong>Provided/Required Interfaces</strong> property group.</li><li>Select a Port shape and from its smart manipulator, click <ac:image ac:title="Provided/Required interfaces" ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="provided_required_interfaces.png"><ri:page ri:content-title="Provided and Required Interfaces" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>.</li></ul></li><li>In the <strong>Provided/Required Interfaces</strong> pane, click the <strong>Add</strong> button and select either Provided or Required.</li><li>Two situations are available:</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li class="auto-cursor-target">If the port is typed, the <strong>Select Interface</strong> dialog opens (see the following figure). In this dialog you can do the following:<br /><ul><li>Select and existing interface (and flow specifications) to be used as the Provided / Required Interface of the port.</li><li>Make sure the <strong>Creation Mode</strong> is switched on, click the <strong>Create</strong> button, and select <strong>Interface</strong>. In the specification window, type its name, and click <strong>Close</strong>. The new interface is created. Select it to be used as the Provided / Required Interface of the port.<br /><ac:image><ri:attachment ri:filename="select_interface_dialog.png"><ri:page ri:content-title="Provided and Required Interfaces" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul></li><li>If the port is not typed, the <strong>Select Port Type</strong> dialog opens (see the following figure). You can do the following:<br /><ul><li><strong>Set provided interface as port type</strong> (for Provided Interface only). The <strong>Select Interface</strong> dialog opens. In this dialog, you can either choose an existing interface or create a new one, to be used as the Provided Interface and the type of the port.</li><li><strong>Create “dummy” port type automatically</strong>. The <strong>Select Interface</strong> dialog opens. In this dialog, you can either choose an existing interface or create a new one, to be used as the Provided or Required Interface of the port. In addition, a dummy classifier, realizing (for Provided) or using (for Required) the interface, is automatically created and used as the type of the port.</li><li><strong>Select or create port type manually</strong>. If you select this option, the <strong>Select Port Type</strong> dialog opens. In this dialog, choose a classifier to be used as the type of the port. Click <strong>OK</strong>, the <strong>Select Interface</strong> dialog opens. In this dialog, you either choose an existing interface or create a new one, to be used as the Provided or Required Interface of the port. In addition, a Realization (or Usage) dependency is automatically created from the port type to the Provided (or Required) Interface of the port.<br /><ac:image><ri:attachment ri:filename="select_port_type.png"><ri:page ri:content-title="Provided and Required Interfaces" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul></li></ul></li></ul><h3>Displaying provided/required interfaces</h3><p><br /></p><p>To display provided/required interfaces</p><hr /><ol><li>Select the port shape that has the provided/required interfaces you want to display.</li><li>Do one of the following:<br />- From the port shortcut menu, select <strong>Display</strong> &gt; <strong>Display Provided/Required Interfaces</strong>.<br />- On the diagram toolbar, click <span class="confluence-embedded-file-wrapper"><ac:image ac:alt="Display"><ri:attachment ri:filename="Display.png"><ri:page ri:content-title="Provided and Required Interfaces" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span> and select <strong>Display Provided/Required Interfaces</strong>.<br /><p>The Required/Provided Interfaces are displayed on the port, in the form of ball-socket (lollipop) notation.</p></li></ol><p>Ports can provide or require many interfaces, therefore, you can choose which ones to display or hide. Use the <ac:link><ri:page ri:content-title="SysML specific compartments" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Edit Compartment</strong> dialog</ac:link-body></ac:link> to manage the visibility of these interfaces.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="48c39722-a8da-4424-ae84-cae2e8fb8ec4"><ac:parameter ac:name="id">1332950710</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="56671277-92c7-4030-a110-f10ab90d4b0a" /><strong><br /></strong></p></ac:layout-cell><ac:layout-cell><p><strong>Sample model</strong></p><p>The model used in the figure of this page is the <strong>Inverted</strong><strong>Pendulum</strong> sample model. To open this sample do one of the following:</p><ul><li>Download<span class="confluence-link"><em><span style="color: rgb(51,51,51);"> <a href="https://docs.nomagic.com/download/attachments/9919520/InvertedPendulum.mdzip?version=1&amp;modificationDate=1498477335401&amp;api=v2">InvertedPendulum.mdzip</a>.<br /></span></em></span></li><li>Find in modeling tool <em><span style="color: rgb(51,51,51);">&lt;modeling tool installation directory&gt;\samples\SysML\Inverted Pendulum\Inverted Pendulum.mdzip.</span></em></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159764 space=SYSMLP2024xR3 version=2 -->
## PAGE 00281: Proxy Port

- page_id: `227159764`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159764/Proxy+Port
- version_number: 2
- version_date: `2025-05-02T10:28:43.319+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

314265351

314265353

314265352

A Proxy Port is a port that specifies features of owning [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] or [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] that are available to external blocks through external [CONFLUENCE_PAGE title='Connector' space='MD2024xR3'] to the ports. It can only be typed by [CONFLUENCE_PAGE title='Interface Block' space='SYSMLP2024xR3'].

[IMAGE alt='' src='']

314265349

**Related pages**

- [CONFLUENCE_PAGE title='Hiding direction arrow on port shape' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9d15fda4-bdf4-4d04-9b94-d60bc3cad884"><ac:parameter ac:name="id">314265351</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="72e21173-e0f2-4655-9d9c-60dc23286ede"><ac:parameter ac:name="id">314265353</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1dfb3373-d9dd-464f-8c45-288ea0f9e94d"><ac:parameter ac:name="id">314265352</ac:parameter><ac:rich-text-body><p><span style="color: rgb(0,0,0);">A Proxy Port is a port that specifies features of owning <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Blocks]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link> that are available to external blocks through external <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Connector" /><ac:plain-text-link-body><![CDATA[Connectors]]></ac:plain-text-link-body></ac:link> to the ports. It can only be typed by <ac:link><ri:page ri:content-title="Interface Block" ri:space-key="SYSMLP2024xR3" /></ac:link>.</span></p><p><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="proxy_ports.png"><ri:page ri:content-title="Proxy Port" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d51621f2-4dfa-45d1-8d59-f98d298968e3"><ac:parameter ac:name="id">314265349</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Hiding direction arrow on port shape" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159294 space=SYSMLP2024xR3 version=2 -->
## PAGE 00282: Publishing projects to Cameo Collaborator for TWC

- page_id: `227159294`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159294/Publishing+projects+to+Cameo+Collaborator+for+TWC
- version_number: 2
- version_date: `2025-05-02T10:28:33.902+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Generating report documents
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Publishing Cameo Collaborator documents' space='CC4TWC2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="fa9958e6-f267-4f34-959f-dbdf7b989dfa"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CC4TWC2024xR3" ri:content-title="Publishing Cameo Collaborator documents" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159771 space=SYSMLP2024xR3 version=1 -->
## PAGE 00283: Quantity Kind

- page_id: `227159771`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159771/Quantity+Kind
- version_number: 1
- version_date: `2016-03-15T10:48:26.539+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

A Quantity Kind (in SysML 1.0 and 1.1, called ‘Dimension’) is a kind of quantity that can be measured using defined and unrestricted units of measurement. For example, length, a quantity kind, may be measured by meter, kilometer, or foot units.

The only valid use of a Quantity Kind instance is to be referenced by the **quantity kind** property of a Value Type or Unit stereotype.

[IMAGE alt='' src='']

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Quantity Kind (in SysML 1.0 and 1.1, called ‘Dimension’) is a kind of quantity that can be measured using defined and unrestricted units of measurement. For example, length, a quantity kind, may be measured by meter, kilometer, or foot units.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="54b3073f-6c12-4bf8-bad7-9be5c849f19a"><ac:rich-text-body><p>The only valid use of a Quantity Kind instance is to be referenced by the <strong>quantity kind</strong> property of a Value Type or Unit stereotype.</p></ac:rich-text-body></ac:structured-macro><p><ac:image ac:alt="Quantity Kind" ac:title="Quantity Kind"><ri:attachment ri:filename="quantity_kind.png"><ri:page ri:content-title="Quantity Kind" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="3db70d55-40ce-4ef2-91cc-1d34c241634d"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Block Definition Diagram ]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159562 space=SYSMLP2024xR3 version=1 -->
## PAGE 00284: Realized Item Flow has no Conveyed Items

- page_id: `227159562`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159562/Realized+Item+Flow+has+no+Conveyed+Items
- version_number: 1
- version_date: `2024-04-18T17:02:51.748+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Ports and Flows
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
<p><strong>Abbreviation</strong></p><p><span style="color: rgb(23,43,77);">RIFHNCI</span><span class="error" style="color: rgb(23,43,77);">[2]</span></p><p><strong>Description</strong></p><p>This validation rule checks if there are any r<span style="color: rgb(23,43,77);">ealized Item Flows without Conveyed Items.</span><strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p><span style="color: rgb(23,43,77);">Connector, Association, ActivityEdge, Message</span></p><p><strong>Solvers</strong></p><ul><li><span style="color: rgb(23,43,77);"><strong>Select Conveyed Item</strong> - opens the Select Conveyed Information dialog <span style="color: rgb(23,43,77);">where you can choose the </span>Conveyed Item for the validated Item Flow.</span></li></ul><p><strong>Example</strong></p><p style="text-align: center;"><strong><ac:image><ri:attachment ri:filename="Realized_Item_Flow_has_no_Conveyed_Items.png"><ri:page ri:content-title="Realized Item Flow has no Conveyed Items" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></strong></p><h6 style="text-align: center;">An Item Flow has no Conveyed Item. The error is resolved by specifying a Conveyed Item via the <strong>Select Conveyed Item </strong>solver.</h6>
````

<!--NOMAGIC_PAGE id=227158876 space=SYSMLP2024xR3 version=1 -->
## PAGE 00285: Reconfiguration

- page_id: `227158876`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158876/Reconfiguration
- version_number: 1
- version_date: `2017-06-23T06:05:05.067+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Initial Values
- labels: []

### NORMALIZED CONTENT

In the FuelTank example (see "Progressive Reconfiguration"), the capacity of a FuelTank in a Vehicle context is reconfigured to 46 litres. In the WheelHubAssembly example, (see "Deep Reconfiguration"), the diameter of the Tire, Tire Bead and Rim, the inflationPressure of the WheelAssembly, etc., in a Truck context will be reconfigured to suit the truck.

When modeling you can use two methods of reconfiguration:

43

##### Progressive Reconfiguration

Progressive Reconfiguration enables SysML to handle a wide range of systems engineering configuration tasks. Progressive Reconfiguration continuously applies the following values:

- Static class-level default values.
- Inherited Property-specific initial values.
- Redefined Property-specific initial values.
- Property-specific initial values.

Property-specific initial values are specific to the usage of a Block as a Part Property in a higher context (i.e. another structured block or “assembly”). If there are many Part Properties of the same type, these Part Properties may have different property-specific default values and will then be initialized differently.

For more information about working with the Report Wizard, see the MagicDraw ReportWizard UserGuide.pdf Property-specific initial values are managed by the higher-context structured block, which owns the Part Properties that initialize or configure their (possibly different) values on instantiation. For example, the generic capacity of a FuelTank (not any particular one) is 40 liters (class-level default value). For a vehicle, however, the generic capacity of its FuelTank is 46 liters. An abstract Vehicle block will thus configure its tank:FuelTank part property by initializing it with a new capacity value. This can be done with Progressive Reconfiguration that will assign the instance specification tank:FuelTank to the property tank:FuelTank of the Vehicle block.

An example of Progressive Reconfiguration is when the values of y and z of a Location are reconfigured to 1 in the Thing context. Thus, the “values (Thing)” compartment in the l:Location part (in the Thing package) will display 1 as the values of y and z.

[IMAGE alt='' src='']

##### Deep Reconfiguration

Deep Reconfiguration enables you to configure deep-nested part(s) with context-specific value(s). Consider, for example, the case of a truck reusing a complex WheelHubAssembly for three pairs of wheels, each with different characteristics. Although the basic WheelHubAssembly might be suitable for a range of vehicles (a car, touring car, and minivan), it is not nearly suitable for a large truck. Some of the WheelHubAssembly parts and subparts required for a truck are larger and must be stronger to handle heavy loads. They include:

- the diameter of the Tire, TireBead, and Rim will be larger.
- the inflationPressure value of the WheelAssembly will be higher.
- the LugBoltJoint will be subject to greater torque and boltTension.
- the LugBoltThreadedHole will have larger lugBoltSize and threadSize.

In this case, Progressive Reconfiguration will fail because the new configuration requirements “cascade” throughout the entire complex WheelHubAssembly from the outermost context to the deepest part. Since no Progressive Reconfiguration approach can handle this deep reconfiguration of complex assemblies, you need to use Deep Reconfiguration.

You can start with a completely new TruckWheelHubAssembly that configures a completely new TruckWheelAssembly, right down to a TruckLugBoltJoint. However, you could use, instead, SysML PropertySpecificType strategy, which is a set of “on-the-fly” extensions (subtypes) of each Block used in a complex assembly hierarchy, to afford a point of redefinition of the Part Properties and their Value Properties as required. See the ‘PropertySpecificType‘ section in OMG SysML specifications.

An example of Deep Reconfiguration is when the value of x of a Location in the UniverseContext package is reconfigured to 3 in the UniverseContext context. Thus, the “values (UniverseContext)” compartment in the l:Location part (in the t1:Thing part in the UniverseContext package) will display 3 as the value of x. If UniverseContext is selected, the value of z, instead of x, will be reconfigured to 2.

For more information about Deep Reconfiguration, see [training.nomagic.com](http://training.nomagic.com).

#### PANEL: Sample model

Sample model

You can see an example of a Deep Reconfiguration project by opening context specific values.mdzip in the <md.install.dir>/samples/SysML directory.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><span style="color: rgb(51,51,51);">In the FuelTank example (see &quot;Progressive Reconfiguration&quot;), the capacity of a FuelTank in a Vehicle context is reconfigured to 46 litres. In the WheelHubAssembly example, (see &quot;Deep Reconfiguration&quot;), the diameter of the Tire, Tire Bead and Rim, the inflationPressure of the WheelAssembly, etc., in a Truck context will be reconfigured to suit the truck.</span></p><p>When modeling you can use two methods of reconfiguration:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="68dc0030-94c0-4a96-b664-d5fbb88ee2c6"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><h3>Progressive Reconfiguration</h3><p>Progressive Reconfiguration enables SysML to handle a wide range of systems engineering configuration tasks. Progressive Reconfiguration continuously applies the following values:</p><ul><li>Static class-level default values.</li><li>Inherited Property-specific initial values.</li><li>Redefined Property-specific initial values.</li><li>Property-specific initial values.</li></ul><p>Property-specific initial values are specific to the usage of a Block as a Part Property in a higher context (i.e. another structured block or “assembly”). If there are many Part Properties of the same type, these Part Properties may have different property-specific default values and will then be initialized differently.</p><p>For more information about working with the Report Wizard, see the MagicDraw ReportWizard UserGuide.pdf Property-specific initial values are managed by the higher-context structured block, which owns the Part Properties that initialize or configure their (possibly different) values on instantiation. For example, the generic capacity of a FuelTank (not any particular one) is 40 liters (class-level default value). For a vehicle, however, the generic capacity of its FuelTank is 46 liters. An abstract Vehicle block will thus configure its tank:FuelTank part property by initializing it with a new capacity value. This can be done with Progressive Reconfiguration that will assign the instance specification tank:FuelTank to the property tank:FuelTank of the Vehicle block.</p><p><span style="color: rgb(51,51,51);">An example of Progressive Reconfiguration is when the values of y and z of a Location are reconfigured to 1 in the Thing context. Thus, the “values (Thing)” compartment in the l:Location part (in the Thing package) will display 1 as the values of y and z.</span></p><p><ac:image><ri:attachment ri:filename="image2017-4-25_11-13-6.png"><ri:page ri:content-title="Reconfiguration" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h3>Deep Reconfiguration</h3><p>Deep Reconfiguration enables you to configure deep-nested part(s) with context-specific value(s). Consider, for example, the case of a truck reusing a complex WheelHubAssembly for three pairs of wheels, each with different characteristics. Although the basic WheelHubAssembly might be suitable for a range of vehicles (a car, touring car, and minivan), it is not nearly suitable for a large truck. Some of the WheelHubAssembly parts and subparts required for a truck are larger and must be stronger to handle heavy loads. They include:</p><ul><li>the diameter of the Tire, TireBead, and Rim will be larger.</li><li>the inflationPressure value of the WheelAssembly will be higher.</li><li>the LugBoltJoint will be subject to greater torque and boltTension.</li><li>the LugBoltThreadedHole will have larger lugBoltSize and threadSize.</li></ul><p>In this case, Progressive Reconfiguration will fail because the new configuration requirements “cascade” throughout the entire complex WheelHubAssembly from the outermost context to the deepest part. Since no Progressive Reconfiguration approach can handle this deep reconfiguration of complex assemblies, you need to use Deep Reconfiguration.</p><p>You can start with a completely new TruckWheelHubAssembly that configures a completely new TruckWheelAssembly, right down to a TruckLugBoltJoint. However, you could use, instead, SysML PropertySpecificType strategy, which is a set of “on-the-fly” extensions (subtypes) of each Block used in a complex assembly hierarchy, to afford a point of redefinition of the Part Properties and their Value Properties as required. See the ‘PropertySpecificType‘ section in OMG SysML specifications.</p><p><span style="color: rgb(51,51,51);">An example of Deep Reconfiguration is when the value of x of a Location in the UniverseContext package is reconfigured to 3 in the UniverseContext context. Thus, the “values (UniverseContext)” compartment in the l:Location part (in the t1:Thing part in the UniverseContext package) will display 3 as the value of x. If UniverseContext is selected, the value of z, instead of x, will be reconfigured to 2.</span></p><p>For more information about Deep Reconfiguration, see <a href="http://training.nomagic.com"> training.nomagic.com</a>.</p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="2d089184-f4eb-489a-b6f3-ed0f3f1ea220"><ac:parameter ac:name="title">Sample model</ac:parameter><ac:rich-text-body><p>You can see an example of a Deep Reconfiguration project by opening context specific values.mdzip in the &lt;md.install.dir&gt;/samples/SysML directory.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159773 space=SYSMLP2024xR3 version=1 -->
## PAGE 00286: Reference Property

- page_id: `227159773`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159773/Reference+Property
- version_number: 1
- version_date: `2016-04-05T13:50:03.508+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

A Reference Property is a property that specifies a reference of its containing Block to another Block. Every Reference Property has ‘none’ AggregationKind and is typed by a block. Reference Properties are displayed in the ‘references’ compartment.

[IMAGE alt='' src='']

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Reference Property is a property that specifies a reference of its containing Block to another Block. Every Reference Property has ‘none’ AggregationKind and is typed by a block. Reference Properties are displayed in the ‘references’ compartment.</p><p><ac:image><ri:attachment ri:filename="reference_property.png"><ri:page ri:content-title="Reference Property" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="ad1d2f29-7ddc-4427-be11-2022073a6b8a"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159775 space=SYSMLP2024xR3 version=2 -->
## PAGE 00287: Refine

- page_id: `227159775`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159775/Refine
- version_number: 2
- version_date: `2025-05-02T10:28:43.508+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Refine' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="d97eef8d-f6a0-4fe5-b0b3-2fec0ab40fc0"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Refine" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><span class="confluence-link"><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></li><li><span class="confluence-link"><span class="confluence-link"><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159573 space=SYSMLP2024xR3 version=1 -->
## PAGE 00288: Relationship and its ends differ in context

- page_id: `227159573`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159573/Relationship+and+its+ends+differ+in+context
- version_number: 1
- version_date: `2022-09-20T08:12:38.548+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Contextual Relationships
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
<p><strong>Abbreviation</strong></p><p><ac:inline-comment-marker ac:ref="2e406f54-d801-4fbb-b8c0-1bb02eef418e">DifferInContext</ac:inline-comment-marker></p><p><strong>Description</strong></p><p>The context of the relationship does not match the context the connected property is displayed in.</p><p><strong>Severity</strong></p><p><ac:inline-comment-marker ac:ref="18d31d91-e86f-446c-af30-4a3414317881">error</ac:inline-comment-marker></p><p><strong><ac:inline-comment-marker ac:ref="4faf89ff-d147-4f4e-a5ce-4838b8b7af97">Constrained Element</ac:inline-comment-marker></strong></p><p>Diagram</p><p><strong>Solvers</strong></p><p>You can use one of the following solvers:</p><ul><li><strong>Update Context of Relationship</strong> - updates the actual path of the connected property.</li><li><strong>Decontextualize</strong> - removes the relationship context. </li><li><strong>Remove from Diagram</strong> - removes the symbol from the diagram.</li><li><strong><ac:inline-comment-marker ac:ref="e6658119-aa99-46ba-8404-ff01f8f4e220">Delete from Model</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="e6658119-aa99-46ba-8404-ff01f8f4e220">  - deletes the element from the model.</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="e6658119-aa99-46ba-8404-ff01f8f4e220"><br /></ac:inline-comment-marker></li></ul><p><strong><ac:inline-comment-marker ac:ref="4bed668a-0532-459a-a992-a1888cb7a7e0">Example</ac:inline-comment-marker></strong></p><p><strong><ac:image ac:height="137" ac:width="517"><ri:attachment ri:filename="validatation_contextual_relationships.png"><ri:page ri:content-title="Relationship and its ends differ in context" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></strong></p>
````

<!--NOMAGIC_PAGE id=227158920 space=SYSMLP2024xR3 version=2 -->
## PAGE 00289: Removing Rollup Pattern Blocks

- page_id: `227158920`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158920/Removing+Rollup+Pattern+Blocks
- version_number: 2
- version_date: `2025-05-02T10:28:25.963+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Rollup Pattern Wizard
- labels: []

### NORMALIZED CONTENT

1348831883

1348831885

1348831884

When removing the applied rollup pattern Block from the model elements, you are removing all of the created property values, subsetted properties, redefines properties, and role names. You can remove the applied rollup pattern Block by using the **[CONFLUENCE_PAGE title='Rollup Pattern Wizard' space='SYSMLP2024xR3']**. The procedure below describes how to remove a previously applied rollup pattern Block.

To remove the rollup pattern Block

1. Right-click the [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] or [CONFLUENCE_PAGE title='Instance Specification' space='MD2024xR3'] from which you want to remove the rollup pattern Block.
2. Select**Tools** >**Remove Rollup Pattern**. [IMAGE alt='' src='']
3. In the **[CONFLUENCE_PAGE title='Rollup Pattern Wizard' space='SYSMLP2024xR3']**, select options: 
- **Recursively Remove Rollup Pattern**to remove the pattern Block recursively. 
- **Remove Role Name** to remove the role names of Part Properties. 
- **Remove Subsetted Properties** to remove the Subsetted Properties of the Part Properties. 
- **Remove Value Properties** to remove Value Properties.
4. Click **OK**. 
The pattern Block is removed from the model elements according to selected options.[IMAGE alt='' src='']

###### The CostRollupPattern is removed from the model along with all the created property values, subsetted properties, redefines properties, and role names.

1348831882

**Related pages**

[CONFLUENCE_PAGE title='Rollup Pattern Wizard' space='SYSMLP2024xR3']

**Webinar**

- Total Mass, Cost, and Power Rollups

**Sample model**

The sample model used in the figures of this page is the **Laptop Cost Analysis** that comes with [Cameo Simulation Toolkit Plugin](https://docs.nomagic.com/display/CST2024xR3/Cameo+Simulation+Toolkit+Documentation). To open this sample do one of the following:

- Download *[LaptopCostAnalysis.mdzip](https://docs.nomagic.com/download/attachments/9919520/LaptopCostAnalysis.mdzip?version=1&modificationDate=1483365649774&api=v2).*
- Find in modeling tool <modeling tool installation directory>\samples\simulation\LaptopCostAnalysis.mdzip

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8fd44040-f5e8-45c5-8d26-69ef6fb20ead"><ac:parameter ac:name="id">1348831883</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0b1d9825-bc71-4e7a-bfb9-8d5d8e2564ef"><ac:parameter ac:name="id">1348831885</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8b03c146-9b50-47f6-b73c-300a1e80d7c4"><ac:parameter ac:name="id">1348831884</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);">When removing the applied rollup pattern Block from the model elements, you are removing all of the created property values, subsetted properties, redefines properties, and role names. You can remove the applied rollup pattern Block by using the <strong><ac:link><ri:page ri:content-title="Rollup Pattern Wizard" ri:space-key="SYSMLP2024xR3" /></ac:link></strong>. The procedure below describes how to remove a previously applied rollup pattern Block.</span></p><p><span style="color: rgb(0,0,0);"><br /></span></p><p><span style="color: rgb(51,51,51);">To remove the rollup pattern Block</span></p><hr /><ol><li><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">Right-click the</span> <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link> <span style="color: rgb(51,51,51);">or</span> <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance Specification" /></ac:link> <span style="color: rgb(51,51,51);">from which you want to remove the rollup pattern Block.</span></span></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">S</span><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">elect </span><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"> <strong>Tools</strong> &gt; </span><strong><span style="color: rgb(51,51,51);">Remove Rollup Pattern</span></strong></span>. </span></p><p><ac:image><ri:attachment ri:filename="before_removing_cost_pattern.png"><ri:page ri:content-title="Removing Rollup Pattern Blocks" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></li><li><p><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">In the</span> <strong><ac:link><ri:page ri:content-title="Rollup Pattern Wizard" ri:space-key="SYSMLP2024xR3" /></ac:link></strong></span><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">, select options:</span><br /><span style="color: rgb(51,51,51);">- <strong>Recursively Remove Rollup Pattern </strong>to remove the pattern Block recursively.<br />- <strong>Remove Role Name</strong> to remove the role names of Part Properties.<br />- <strong>Remove Subsetted Properties</strong> to remove the Subsetted Properties of the Part Properties.</span><br /><span style="color: rgb(51,51,51);">- <strong>Remove Value Properties</strong> to remove Value Properties.</span></span></p></li><li><p><span style="color: rgb(51,51,51);">Click <strong>OK</strong>.<br />The pattern Block is removed from the model elements according to selected options.</span><span style="color: rgb(0,51,102);"> <ac:image ac:align="center"><ri:attachment ri:filename="after_removing_cost_pattern.png"><ri:page ri:content-title="Removing Rollup Pattern Blocks" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p></li></ol><h6 style="text-align: center;">The CostRollupPattern is removed from the model along with all the created property values, subsetted properties, redefines properties, and role names.</h6><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8dd197f0-d3cf-4274-babd-7524305efd7d"><ac:parameter ac:name="id">1348831882</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f4e3ca3d-2d77-4e62-9203-4a9a025a8b08"><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="Rollup Pattern Wizard" ri:space-key="SYSMLP2024xR3" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><strong>Webinar</strong></p><ul><li><a href="http://www.nomagic.com/mbse/events/webinars/item/webinar-7-2016-total-mass-cost-and-power-rollups.html">Total Mass, Cost, and Power Rollups</a></li></ul></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><strong>Sample model</strong></p><p>The sample model used in the figures of this page is the <strong>Laptop Cost Analysis</strong> that comes with <a href="https://docs.nomagic.com/display/CST2024xR3/Cameo+Simulation+Toolkit+Documentation">Cameo Simulation Toolkit Plugin</a>. To open this sample do one of the following:</p><ul><li>Download<span class="confluence-link"><em> <a href="https://docs.nomagic.com/download/attachments/9919520/LaptopCostAnalysis.mdzip?version=1&amp;modificationDate=1483365649774&amp;api=v2">LaptopCostAnalysis.mdzip</a>.<br /></em></span></li><li>Find in modeling tool <em>&lt;modeling tool installation directory&gt;\samples\simulation\LaptopCostAnalysis.mdzip</em></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159810 space=SYSMLP2024xR3 version=2 -->
## PAGE 00290: Reporting Issues

- page_id: `227159810`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159810/Reporting+Issues
- version_number: 2
- version_date: `2025-05-02T10:28:44.758+02:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Reporting Issues' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="303dcdbd-4cb8-4795-949f-3ce494331d4d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Reporting Issues" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159113 space=SYSMLP2024xR3 version=2 -->
## PAGE 00291: Representing Use Case scenarios in Activity diagrams

- page_id: `227159113`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159113/Representing+Use+Case+scenarios+in+Activity+diagrams
- version_number: 2
- version_date: `2025-05-02T10:28:30.458+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Use Cases > Use Case scenario
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Representing Use Case scenarios in Activity diagrams' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="483add2f-c9ba-475b-a100-5ad10660738c"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Representing Use Case scenarios in Activity diagrams" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159776 space=SYSMLP2024xR3 version=2 -->
## PAGE 00292: Requirement

- page_id: `227159776`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159776/Requirement
- version_number: 2
- version_date: `2025-05-02T10:28:43.691+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Requirement' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="2d8cc0bc-4f28-4f0f-96a4-69da30ef007d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Requirement" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158615 space=SYSMLP2024xR3 version=1 -->
## PAGE 00293: Requirement coverage

- page_id: `227158615`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158615/Requirement+coverage
- version_number: 1
- version_date: `2019-05-06T14:19:17.180+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management > Requirement coverage analysis > Predefined Metric Suites for MagicGrid
- labels: []

### NORMALIZED CONTENT

A Metric suite is a collection of parameters and metric definitions used to calculate metrics that evaluate specific aspects of your model. For your convenience, there are four predefined Metric Suites for MagicGrid that calculate Requirement coverage. The following figure shows these Metric Suites and their purposes.

#### NOTE: Important

Important

You must create a MagicGrid project or use the MagicGrid Profile in your model in order to user predefined Metric Suites for MagicGrid.

[IMAGE alt='' src='']

###### Predefined Requirement coverage Metric Suites for MagicGrid.

**Stakeholder Needs Refinement**

This Metric Suite checks incoming Refine relationships and tracks whether or not stakeholder needs are refined.Only atomic Requirements (without sub-requirements) are tracked. Stakeholder needs can only be refined by one of the following elements:

- 
  - Action
  - State
  - Part Property
  - Reference Property
  - Flow Property
  - Full Port
  - Proxy Port
  - Value Property
  - Constraint Property

**System Requirements Derivation**

This Metric Suite checks outgoing Derive relationships and tracks whether or not system Requirements are derived.Only atomic Requirements (without sub-requirements) are tracked. A Requirement is treated as derived when it or its grouping Requirement has an outgoing Derive relationship to the Requirement with no sub-requirements.

**System Requirements Verification**

This Metric Suite checks incoming Verify relationships and tracks whether or not system Requirements are verifiedby a Test Case element. Only atomic Requirements (without sub-requirements) are tracked.

**System Requirements Satisfaction**

This Metric Suite checks incoming Satisfy relationships and tracks whether or not system Requirements are satisfied.Only atomic Requirements (without sub-requirements) are tracked. System Requirements can only be satisfied by one of the following elements:

- 
  - Action
  - State
  - Part Property
  - Reference Property
  - Flow Property
  - Full Port
  - Proxy Port
  - Value Property
  - Constraint Property

[IMAGE alt='' src='']

###### This diagram illustrates which system Requirements are satisfied when using the **System Requirements Satisfaction** Metric Suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">A Metric suite is a collection of parameters and metric definitions used to calculate metrics that evaluate specific aspects of your model. For your convenience, there are four predefined Metric Suites for MagicGrid that calculate Requirement coverage. The following figure shows these Metric Suites and their purposes.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b842d5c4-e1df-46ae-9c44-ed3f6423f77f"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p>You must create a MagicGrid project or use the MagicGrid Profile in your model in order to user predefined Metric Suites for MagicGrid.</p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(62,63,64);"><br /><br /></span></p><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center" ac:height="231"><ri:attachment ri:filename="requirement_coverage_metric_suites_for_magicgrid.png"><ri:page ri:content-title="Requirement coverage" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">Predefined Requirement coverage Metric Suites for MagicGrid.</span></h6><p><strong><span style="color: rgb(62,63,64);">Stakeholder Needs Refinement</span></strong></p><p><span style="color: rgb(62,63,64);">This Metric Suite checks incoming Refine relationships and tracks whether or not stakeholder needs are refined. </span>Only atomic Requirements (without sub-requirements) are tracked. Stakeholder needs can only be refined by one of the following elements:</p><ul><li style="list-style-type: none;background-image: none;"><ul><li>Action</li><li>State</li><li>Part Property</li><li>Reference Property</li><li>Flow Property</li><li>Full Port</li><li>Proxy Port</li><li>Value Property</li><li>Constraint Property</li></ul></li></ul><p><span style="color: rgb(62,63,64);"><br /><strong>System Requirements Derivation</strong></span></p><p><span style="color: rgb(62,63,64);">This Metric Suite checks outgoing Derive relationships and tracks whether or not system Requirements are derived. </span>Only atomic Requirements (without sub-requirements) are tracked. A Requirement is treated as derived when it or its grouping Requirement has an outgoing Derive relationship to the Requirement with no sub-requirements.</p><p><span style="color: rgb(62,63,64);"><strong><br />System Requirements Verification</strong></span></p><p><span style="color: rgb(62,63,64);">This Metric Suite checks incoming Verify relationships and tracks whether or not system Requirements are verified </span>by a Test Case element. Only atomic Requirements (without sub-requirements) are tracked. </p><p><span style="color: rgb(62,63,64);"><br /><strong>System Requirements Satisfaction</strong></span></p><p><span style="color: rgb(62,63,64);">This Metric Suite checks incoming Satisfy relationships and tracks whether or not system Requirements are satisfied. </span>Only atomic Requirements (without sub-requirements) are tracked. System Requirements can only be satisfied by one of the following elements:</p><ul><li style="list-style-type: none;background-image: none;"><ul><li>Action</li><li>State</li><li>Part Property</li><li>Reference Property</li><li>Flow Property</li><li>Full Port</li><li>Proxy Port</li><li>Value Property</li><li>Constraint Property</li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="System Requirements Satisfaction MagicGrid.png"><ri:page ri:content-title="Requirement coverage" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">This diagram <ac:inline-comment-marker ac:ref="229fc5d4-7b4b-48b0-b484-bacc4777c170">illustrates</ac:inline-comment-marker> which system Requirements are satisfied when using the <strong>System Requirements Satisfaction</strong> Metric Suite.</h6>
````

<!--NOMAGIC_PAGE id=227158609 space=SYSMLP2024xR3 version=2 -->
## PAGE 00294: Requirement coverage analysis

- page_id: `227158609`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158609/Requirement+coverage+analysis
- version_number: 2
- version_date: `2025-05-02T10:28:20.272+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management
- labels: []

### NORMALIZED CONTENT

Requirement coverage analysis is based on calculating which model Requirements are satisfied and what elements satisfy them. For this purpose, metrics are introduced. You can calculate metrics for the selected elements using predefined Metric Suites. In addition, you can create your own Metrics Suites from scratch or predefined Metric Suites.

A metric is an item of information about a specific aspect of a model. You can use a collection of various metrics to evaluate the current state of your model. Calculated at regular intervals, metrics can help track the evolution of the model's development. You can calculate metrics and store the calculation results in [CONFLUENCE_PAGE title='Metric table' space='MD2024xR3'].

For more information about predefined Metric Suites, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Requirement coverage analysis is based on calculating which model Requirements are satisfied and what elements satisfy them. For this purpose, metrics are introduced. You can calculate metrics for the selected elements using predefined Metric Suites. In addition, you can create your own Metrics Suites from scratch or predefined Metric Suites.</p><p>A metric is an item of information about a specific aspect of a model. You can use a collection of various metrics to evaluate the current state of your model. Calculated at regular intervals, metrics can help track the evolution of the model's development. You can calculate metrics and store the calculation results in <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Metric table" /><ac:plain-text-link-body><![CDATA[Metric Tables]]></ac:plain-text-link-body></ac:link>.</p><p>For more information about predefined Metric Suites, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2ad6efba-59cc-447d-b047-91fe94f58b98" /></p>
````

<!--NOMAGIC_PAGE id=227158618 space=SYSMLP2024xR3 version=1 -->
## PAGE 00295: Requirement covering elements

- page_id: `227158618`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158618/Requirement+covering+elements
- version_number: 1
- version_date: `2019-05-08T12:57:13.533+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management > Requirement coverage analysis > Predefined Metric Suites for MagicGrid
- labels: []

### NORMALIZED CONTENT

A Metric suite is a collection of parameters and metric definitions used to calculate metrics that evaluate specific aspects of your model. For your convenience, there are three predefined Metric Suites for MagicGrid that calculate Requirement covering elements. The following figure outlines these Metric Suites and their purposes.

#### NOTE: Important

Important

You must create a MagicGrid project or use the MagicGrid Profile in your model in order to use predefined Metric Suites for MagicGrid.

[IMAGE alt='' src='']

###### Predefined Requirement covering elements Metric Suites for MagicGrid.

**Stakeholder Needs Refining Elements**

This Metric Suite tracks refining elements by checking the outgoing Refine relationships from behavior, structure, and parameter elements to Stakeholder Needs. Stakeholder Needs can only be refined by the following elements:

- Action
- Part Property
- Reference Property
- Value Property

**System Requirements Satisfying Elements**

This Metric Suite tracks satisfying elements by checking the outgoing Satisfy relationships from behavior, structure, and parameter elements to System Requirements. System Requirements can only by satisfied by the following elements:

- Action
- Part Property
- Reference Property
- Value Property

**System Requirements Verifying Elements**

This Metric Suite tracks verifying elements by checking the outgoing Verify relationships form Test Cases to System Requirements.

[IMAGE alt='' src='']

###### A Metric Table that tracks System Requirements satisfying elements.

##### Elements tracked by Requirement covering elements Metric Suites

The quantity of model elements tracked by Stakeholder Needs Refining Elements and System Requirements Satisfying Elements Metric Suites for MagicGrid depends on the following rules:

- In most cases, only the elements that do not own any elements (leaf elements)are tracked. ExamplesThe following examples are from the Block Definition Diagram displayed below:If relationships A and B do not exist, *Radiator*, *Heater Hose*, and *Lower Radiator Hose* Part Properties are tracked.If only relationship B exists, *Radiator*,*Heater Hose*, and*Lower Radiator Hose*Part Properties are tracked.If both relationships A and B exist, *Radiator*,*Heater Hose*, and*Lower Radiator Hose*Part Properties are tracked.
- The elements that own other elements are only tracked if they have outgoing relationships, but none of the elements they own have outgoing relationships. ExampleIf only relationship A existed in the diagram below, then *Hose* and *Radiator* Part Properties would be tracked.

[IMAGE alt='' src='']

###### A Block Definition Diagram illustrating which elements are tracked by Requirement covering elements Metric Suites. For more information, see the examples described above.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">A Metric suite is a collection of parameters and metric definitions used to calculate metrics that evaluate specific aspects of your model. For your convenience, there are three predefined Metric Suites for MagicGrid that calculate Requirement covering elements. The following figure outlines these Metric Suites and their purposes.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b842d5c4-e1df-46ae-9c44-ed3f6423f77f"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p>You must create a MagicGrid project or use the MagicGrid Profile in your model in order to use predefined Metric Suites for MagicGrid.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="requirement_covering_metric_suites_for_magicgrid.png"><ri:page ri:content-title="Requirement covering elements" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Predefined Requirement covering elements Metric Suites for MagicGrid.</h6><p><strong>Stakeholder Needs Refining Elements</strong></p><p>This Metric Suite tracks refining elements by checking the outgoing Refine relationships from behavior, structure, and parameter elements to S<ac:inline-comment-marker ac:ref="5eec8226-797a-465d-b03b-94fce4be0a7a">takeholder Needs</ac:inline-comment-marker>. Stakeholder Needs can only be refined by the following elements:</p><ul><li>Action</li><li>Part Property</li><li>Reference Property</li><li>Value Property</li></ul><p><br /><strong>System Requirements Satisfying Elements</strong></p><p>This Metric Suite tracks satisfying elements by checking the outgoing Satisfy relationships from behavior, structure, and parameter elements to S<ac:inline-comment-marker ac:ref="743ab7cc-db89-49d9-8217-30ff33086804">ystem</ac:inline-comment-marker> Requirements. System Requirements can only by satisfied by the following elements:</p><ul><li>Action</li><li>Part Property</li><li>Reference Property</li><li>Value Property</li></ul><p><br /><strong>System Requirements Verifying Elements</strong></p><p>This Metric Suite tracks verifying elements by checking the outgoing Verify relationships form Test Cases to S<ac:inline-comment-marker ac:ref="15132445-772d-4bf3-91b0-81645461e3f5">ystem</ac:inline-comment-marker> Requirements.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="metric_table_tracking_system_requirements_satisfying_elements.png"><ri:page ri:content-title="Requirement covering elements" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Metric Table that tracks System Requirements satisfying elements.</h6><h3>Elements tracked by Requirement covering elements Metric Suites</h3><p>The quantity of model elements tracked by Stakeholder Needs Refining Elements and System Requirements Satisfying Elements Metric Suites for MagicGrid depends on the following rules:</p><ul><li><p class="auto-cursor-target">In most cases, only the elements that <ac:inline-comment-marker ac:ref="57684711-8a8a-470e-815a-6804a8a19df4">do not own any elements</ac:inline-comment-marker> <span style="color: rgb(62,63,64);">(leaf  elements) </span>are tracked.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="e8a142b0-3e1f-4681-b21d-349820b2b3b1"><ac:parameter ac:name="title">Examples</ac:parameter><ac:rich-text-body><p>The following examples are from the Block Definition Diagram displayed below:</p><ul><li>If relationships A and B do not exist, <em style="letter-spacing: 0.0px;">Radiator</em>, <em style="letter-spacing: 0.0px;">Heater Hose</em>, and <em style="letter-spacing: 0.0px;">Lower Radiator Hose</em> Part Properties are tracked.</li><li>If only relationship B exists, <em>Radiator</em><span>, </span><em>Heater Hose</em><span>, and </span><em>Lower Radiator Hose</em><span> Part Properties are tracked.</span></li><li><span>If both relationships A and B exist, <em>Radiator</em><span>, </span><em>Heater Hose</em><span>, and </span><em>Lower Radiator Hose</em><span> Part Properties are tracked.</span></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">The elements that own other elements are only tracked if they have outgoing relationships, but none of the elements they own have outgoing relationships.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ae2db4d3-8f28-4c32-a83f-6d24d0557725"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p> If only relationship A existed in the diagram below, then <em>Hose</em> and <em>Radiator</em> Part Properties would be tracked.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><br /></p></li></ul><p><br /><ac:image ac:align="center"><ri:attachment ri:filename="system_structure_example.png"><ri:page ri:content-title="Requirement covering elements" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A Block Definition Diagram illustrating which elements are tracked <span style="color: rgb(94,108,132);">by Requirement covering elements Metric Suites. For more information, see the examples described above.</span></h6>
````

<!--NOMAGIC_PAGE id=227159647 space=SYSMLP2024xR3 version=2 -->
## PAGE 00296: Requirement Diagram

- page_id: `227159647`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159647/Requirement+Diagram
- version_number: 2
- version_date: `2025-05-02T10:28:39.506+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024xR3']true

#### PANEL: Related elements

Related elements

- [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Extended Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Functional Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Interface Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Performance Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Physical Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Design Constraint' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Business Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Usability Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Test Case' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Satisfy' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Verify' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Derive' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Copy' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="7772ee78-9684-4e81-ab4c-bee8564e2297"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Requirement Diagram" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="411a5fd1-40c1-4ca9-9b74-0ec999cb1c78"><ac:parameter ac:name="title">Related elements</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Extended Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Functional Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Interface Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Performance Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Physical Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Design Constraint" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Business Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Usability Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Test Case" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Satisfy" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Verify" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Derive" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Copy" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p> </ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159671 space=SYSMLP2024xR3 version=3 -->
## PAGE 00297: Requirement matrices

- page_id: `227159671`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159671/Requirement+matrices
- version_number: 3
- version_date: `2025-05-02T10:28:40.414+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions > Matrices
- labels: []

### NORMALIZED CONTENT

The matrices enables you to analyze, create, and modify relationships between Requirements and other design elements. It is especially valuable that you can display relationships that cannot be represented in diagrams, such as representations (classes by lifeline), behavior representations in other diagrams, operation representations by Call Behavior Actions, etc. All Requirement matrices allows you to perform [CONFLUENCE_PAGE title='Requirements gap and coverage analysis' space='SYSMLP2024xR3'].

You can create four kind of Requirements matrices:

- Derive Requirement Matrix.
- Refine Requirement Matrix.
- Satisfy Requirement Matrix.
- Verify Requirement Matrix.

The different purposes for each matrix are illustrated below:

- Derive Requirement Matrix allows you to analyze, create, and modify [CONFLUENCE_PAGE title='Derive' space='SYSMLP2024xR3'] relationships between Requirements and other design elements. Rows represent the elements that are the clients of Derive relationship. Columns represent the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3'] that are the suppliers of Derive relationship. The example below is created by using the [ATTACHMENT filename='extract requirement values.mdzip'] sample model that comes only with SysML Plugin . [ATTACHMENT filename='derive_matrix.png']
- Refine Requirement Matrix allows you to analyze, create, and modify [CONFLUENCE_PAGE title='Refine' space='SYSMLP2024xR3'] relationships between Requirements and other design elements. Rows represent the elements that are the clients of Refine relationship. Columns represent the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3'] that are the suppliers of the Refine relationship. The example below is created by using the [ATTACHMENT filename='extract requirement values.mdzip'] sample model that comes only with SysML Plugin . [ATTACHMENT filename='refine_matrix.png']
- **Satisfy Requirement Matrix**allows you to analyze, create, and modify [CONFLUENCE_PAGE title='Satisfy' space='SYSMLP2024xR3']relationships between Requirements and other design elements. Rows represent the elements that are the clients of Satisfy relationship. Columns represent the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3'] that are the suppliers of the Satisfy relationship. The example below is created by using the [ATTACHMENT filename='extract requirement values.mdzip'] sample model that comes only with SysML Plugin . [ATTACHMENT filename='satisfy_matrix.png']
- Verify Requirement Matrix allows you to analyze, create, and modify [CONFLUENCE_PAGE title='Verify' space='SYSMLP2024xR3']relationships between Requirements and other design elements. Rows represent the elements that are the clients of Verify relationship. Columns represent the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3'] that are the suppliers of the Verify relationship. The example below is created by using the [ATTACHMENT filename='Categorization requirements.mdzip']sample model that comes only with[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024xR3']. 
[IMAGE alt='' src='']

#### INFO: How to work with Requirement matrices

How to work with Requirement matrices

Requirement matrices are based on [CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024xR3']. That's why all it's procedures are allowable for Requirement matrices:

[CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The matrices enables you to analyze, create, and modify relationships between Requirements and other design elements. It is especially valuable that you can display relationships that cannot be represented in diagrams, such as representations (classes by lifeline), behavior representations in other diagrams, operation representations by Call Behavior Actions, etc. All Requirement matrices allows you to perform <ac:link><ri:page ri:content-title="Requirements gap and coverage analysis" ri:space-key="SYSMLP2024xR3" /></ac:link>. </p><p>You can create four kind of Requirements matrices:</p><ul><li>Derive Requirement Matrix.</li><li><div>Refine Requirement Matrix.</div></li><li><span style="color: rgb(62,63,64);">Satisfy Requirement Matrix.</span></li><li><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">Verify Requirement Matrix.</span></span><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);"><br /></span></span></li></ul><p><br /></p><p>The different purposes for each matrix are illustrated below:</p><ul><li><strong>Derive Requirement Matrix</strong> allows you to analyze, create, and modify <ac:link><ri:page ri:content-title="Derive" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Derive ]]></ac:plain-text-link-body></ac:link>relationships between Requirements and other design elements. Rows represent the elements that are the clients of Derive relationship. Columns represent the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements]]></ac:plain-text-link-body></ac:link> that are the suppliers of Derive relationship. <span style="color: rgb(62,63,64);">The example below is created by using the <ac:link><ri:attachment ri:filename="extract requirement values.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link></span><span style="color: rgb(62,63,64);"> sample model that comes only with </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Plugin+Documentation">SysML Plugin</a><span style="color: rgb(62,63,64);">.</span><br /><ac:image><ri:attachment ri:filename="derive_matrix.png"><ri:page ri:content-title="Requirement matrices" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><strong>Refine Requirement Matrix </strong>allows you to analyze, create, and modify <ac:link><ri:page ri:content-title="Refine" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Refine ]]></ac:plain-text-link-body></ac:link>relationships between Requirements and other design elements. Rows represent the elements that are the clients of Refine relationship. Columns represent the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements]]></ac:plain-text-link-body></ac:link> that are the suppliers of the Refine relationship. <span style="color: rgb(62,63,64);">The example below is created by using the <ac:link><ri:attachment ri:filename="extract requirement values.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link></span><span style="color: rgb(62,63,64);"> sample model that comes only with </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Plugin+Documentation">SysML Plugin</a><span style="color: rgb(62,63,64);">.</span><br /><ac:image><ri:attachment ri:filename="refine_matrix.png"><ri:page ri:content-title="Requirement matrices" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);"><strong>Satisfy Requirement Matrix </strong>allows you to analyze, create, and modify <ac:link><ri:page ri:content-title="Satisfy" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Satisfy ]]></ac:plain-text-link-body></ac:link>relationships between Requirements and other design elements. </span></span>Rows represent the elements that are the clients of Satisfy relationship. Columns represent the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements]]></ac:plain-text-link-body></ac:link> that are the suppliers of the Satisfy relationship. <span style="color: rgb(62,63,64);">The example below is created by using the <ac:link><ri:attachment ri:filename="extract requirement values.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link></span><span style="color: rgb(62,63,64);"> sample model that comes only with </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Plugin+Documentation">SysML Plugin</a><span style="color: rgb(62,63,64);">.</span><br /><ac:image><ri:attachment ri:filename="satisfy_matrix.png"><ri:page ri:content-title="Requirement matrices" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><strong style="color: rgb(62,63,64);">Verify Requirement Matrix </strong><span style="color: rgb(62,63,64);">allows you to analyze, create, and modify <ac:link><ri:page ri:content-title="Verify" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Verify ]]></ac:plain-text-link-body></ac:link>relationships between Requirements and other design elements. Rows represent the elements that are the clients of Verify relationship. Columns represent the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements]]></ac:plain-text-link-body></ac:link> that are the suppliers of the Verify relationship.  <span style="color: rgb(62,63,64);">The example below is created by using the <ac:link><ri:attachment ri:filename="Categorization requirements.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link></span><span style="color: rgb(62,63,64);"> sample model that comes only with </span><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Requirements Modeler Plugin]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);">.</span><br /><ac:image><ri:attachment ri:filename="verify_matrix.png"><ri:page ri:content-title="Requirement matrices" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span><br /><br /><span style="color: rgb(62,63,64);"><br /></span></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a1a761b2-266d-4e97-89bb-986cfad96aaf"><ac:parameter ac:name="title">How to work with Requirement matrices</ac:parameter><ac:rich-text-body><p class="auto-cursor-target">Requirement matrices are based on <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Dependency Matrix" /></ac:link>. That's why all it's procedures are allowable for Requirement matrices:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="48cb762c-fba2-41d8-8aea-6dce68d7130e"><ac:parameter ac:name="page"><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Dependency Matrix" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(62,63,64);"><br /></span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159691 space=SYSMLP2024xR3 version=2 -->
## PAGE 00298: Requirement Table

- page_id: `227159691`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159691/Requirement+Table
- version_number: 2
- version_date: `2025-05-02T10:28:40.953+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

96411545

96411556

96411546

[CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024xR3']true

96411544

**Related elements**

- [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Extended Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Functional Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Interface Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Performance Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Physical Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Design Constraint' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Business Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Usability Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Test Case' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Satisfy' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Verify' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Derive' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Copy' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8c5977c1-9d22-45e5-ba34-8f68e6bc49d5"><ac:parameter ac:name="id">96411545</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a6af3277-f600-4870-89da-6762ac5a798f"><ac:parameter ac:name="id">96411556</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d67fd578-6601-41bd-a5a4-d93edeaf44f4"><ac:parameter ac:name="id">96411546</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="f058413e-e54d-47d4-9811-5e2dc1993708"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Requirement Table" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="98365e06-498f-4fbf-a18b-c70c5edda9bb"><ac:parameter ac:name="id">96411544</ac:parameter><ac:rich-text-body><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Extended Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Functional Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Interface Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Performance Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Physical Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Design Constraint" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Business Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Usability Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Test Case" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Satisfy" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Verify" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Derive" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Copy" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158576 space=SYSMLP2024xR3 version=3 -->
## PAGE 00299: Requirements decomposition

- page_id: `227158576`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158576/Requirements+decomposition
- version_number: 3
- version_date: `2025-05-02T10:28:19.604+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Requirements hierarchy mode in table

819350165

#### CONTENT-COLUMN: Requirements hierarchy mode in table

819350168

819350164

**On this page**

**43true**

#### CONTENT-BLOCK: Requirements hierarchy mode in table

819350167

##### Main rules of Requirements decomposition

The following are the rules for decomposing Requirements:

- If some part of the Requirement is going to be used somewhere else (e.g. some other Requirement [CONFLUENCE_PAGE title='Derive' space='SYSMLP2024xR3'] from it, or it is subject to decomposition itself), then the requirement should be decomposed into smaller Requirements.
- If the Requirement has information from different (sub)topics, it should also be decomposed into sub-requirements.
- If parts of the Requirement are not used by any other Requirement and the Requirement holds information that naturally describes the same topic or thing, but the text of the Requirement becomes too long (e.g. 8-10 sentences), it should still be decomposed into several Requirements for better readability.

##### Decomposing Requirements

You can decompose Requirements in the following ways:

44

###### Creating requirements hierarchy in the Containment tree

You can decompose Requirements in the [CONFLUENCE_PAGE title='Containment tab' space='SYSMLP2024xR3']. The element is created in the[Model Browser](https://docs.nomagic.com/display/CRMP2024xR3/Understanding+the+user+interface). You can then represent them in the [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3'] by dragging elements or in the [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3'] by adding existing elements.

[How to create requirements in the Containment tree >>](https://docs.nomagic.com/display/CRMP2024xR3/Creating+requirements#Creatingrequirements-containment)

In the following figure, the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']are decomposed in the Containment tree. For example, the *Item purchase* Requirement is decomposed into four sub-Requirements: *Purchasing facilitation*, *Purchase request for new items*, *External global repository*, and *Item request management*.

[IMAGE alt='' src='']

###### The Requirements decomposition in the Containment tree.

###### Creating requirements hierarchy in the Requirement Diagram

While decomposing [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3'] in the [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3'] the following rules apply:

- A single Requirement Diagram should contain only one nesting level: one main Requirement shape and one level of its owned Requirements.
- If each nesting level contains only a few Requirements (e.g. 1-4 requirements), a single Requirement Diagram can contain more than one nesting level.
- If the main Requirement owns more than 5 Requirements they should be refined in a separate diagram.

[How to create Requirements in the Requirement diagram >>](https://docs.nomagic.com/display/CRMP2024xR3/Creating+requirements#Creatingrequirements-diagram)

In the following figure, the the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']are decomposed by using the Containment relationship and represented in the [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']. For example, the *Notification* Requirement is decomposed into two sub-Requirements: *Notification about available item* and *Notification methods*.

[IMAGE alt='' src='']

###### The Requirements decomposition in the Requirement Diagram.

###### Decomposing requirements in the Requirements table

You can represent and create [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']of your system in the [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']. [How to create Requirements in the Requirement table >>](https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+requirements#Creatingrequirements-tableCreatingrequirementsintheRequirementTable)

You can decompose Requirements:

- By creating Requirements in the table.
- [CONFLUENCE_PAGE title='Nesting requirements in the Requirements Table' space='CRMP2024xR3']

In the following figure, the [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']are decomposed and displayed hierarchically in the [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']. For example, the *Item purchase* Requirement is decomposed into four sub-Requirements: *Purchasing facilitation*, *Purchase request for new items*, *External global repository*, and *Item request management*.

#### INFO: Requirements hierarchy mode in table

Requirements hierarchy mode in table

You can change the Requirements hierarchy in the table by using the **Display Mode** option. This option is described in the [CONFLUENCE_PAGE title='Table toolbars' space='MD2024xR3'] page under the Options toolbar.

[IMAGE alt='' src='']

###### The Requirements decomposition in the Requirement Table.

819396999

**Sample model**

The model used in the figures of this page is the **User needs - requirements module for MagicLibrary**sample model that comes with MagicDraw. To open this sample do one of the following:

- Download *[ATTACHMENT filename='User needs - requirements module for MagicLibrary.mdzip']*.
- Find in modeling tool <modeling tool installation directory>\samples\diagrams\*User needs - requirements module for MagicLibrary*.mdzip.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8ee6a89b-9061-4f14-ac8f-95c3a47e7132"><ac:parameter ac:name="id">819350165</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f67b758a-b51d-4826-a18a-5675442838f3"><ac:parameter ac:name="id">819350168</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="579c1169-ba25-4e81-9c92-6ba2ee0b5f63"><ac:parameter ac:name="id">819350164</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="07da9471-008e-4356-b910-3a2a78b57686"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter><ac:parameter ac:name="absoluteUrl">true</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="83a73d85-7033-4921-82ed-f7815c67980c"><ac:parameter ac:name="id">819350167</ac:parameter><ac:rich-text-body><h3>Main rules of Requirements decomposition</h3><p>The following are the rules for decomposing Requirements:</p><ul><li>If some part of the Requirement is going to be used somewhere else (e.g. some other Requirement <ac:link><ri:page ri:content-title="Derive" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[derives ]]></ac:plain-text-link-body></ac:link>from it, or it is subject to decomposition itself), then the requirement should be decomposed into smaller Requirements.</li><li>If the Requirement has information from different (sub)topics, it should also be decomposed into sub-requirements.</li><li>If parts of the Requirement are not used by any other Requirement and the Requirement holds information that naturally describes the same topic or thing, but the text of the Requirement becomes too long (e.g. 8-10 sentences), it should still be decomposed into several Requirements for better readability.</li></ul><p><br /></p><h3>Decomposing Requirements</h3><p>You can decompose Requirements in the following ways:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fe6524d1-f0f2-4eb2-a8ee-b8f672821748"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></p><h4>Creating requirements hierarchy in the Containment tree</h4><p>You can decompose Requirements in the <ac:link><ri:page ri:content-title="Containment tab" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>. T<span style="color: rgb(62,63,64);">he element is created in the </span><a href="https://docs.nomagic.com/display/CRMP2024xR3/Understanding+the+user+interface">Model Browser</a><span style="color: rgb(62,63,64);">. Y</span>ou can then represent them in the <ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link> by dragging elements or in the <ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link> by adding existing elements.</p><p><a href="https://docs.nomagic.com/display/CRMP2024xR3/Creating+requirements#Creatingrequirements-containment">How to create requirements in the Containment tree &gt;&gt;</a></p><p>In the following figure, the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements ]]></ac:plain-text-link-body></ac:link>are decomposed in the Containment tree. For example, the <em>Item purchase</em> Requirement is decomposed into four sub-Requirements: <em>Purchasing facilitation</em>, <em>Purchase request for new items</em>, <em>External global repository</em>, and <em>Item request management</em>.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="req_decomposition_in_containment_tree.png"><ri:page ri:content-title="Requirements decomposition" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Requirements decomposition in the Containment tree.</h6><h4>Creating requirements hierarchy in the Requirement Diagram</h4><p>While decomposing <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements]]></ac:plain-text-link-body></ac:link> in the <ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link> the following rules apply:</p><ul><li>A single Requirement Diagram should contain only one nesting level: one main Requirement shape and one level of its owned Requirements.</li><li>If each nesting level contains only a few Requirements (e.g. 1-4 requirements), a single Requirement Diagram can contain more than one nesting level.</li><li>If the main Requirement owns more than 5 Requirements they should be refined in a separate diagram.</li></ul><p><a href="https://docs.nomagic.com/display/CRMP2024xR3/Creating+requirements#Creatingrequirements-diagram">How to create Requirements in the Requirement diagram &gt;&gt;</a></p><p>In the following figure, the the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements ]]></ac:plain-text-link-body></ac:link>are decomposed by using the Containment relationship and represented in the <ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link>. For example, the <em>Notification</em> Requirement is decomposed into two sub-Requirements: <em>Notification about available item</em> and <em>Notification methods</em>.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="req_decomposition_in_req_diagram.png"><ri:page ri:content-title="Requirements decomposition" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Requirements decomposition in the Requirement Diagram.</h6><h4>Decomposing requirements in the Requirements table</h4><p>You can represent and create <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements ]]></ac:plain-text-link-body></ac:link>of your system in the <ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements Table]]></ac:plain-text-link-body></ac:link>. <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+requirements#Creatingrequirements-tableCreatingrequirementsintheRequirementTable">How to create Requirements in the Requirement table &gt;&gt;</a></p><p>You can decompose Requirements:</p><ul><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+requirements#Creatingrequirements-AddingnestedRequirements">By creating Requirements in the table.</a></li><li><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Nesting requirements in the Requirements Table" /><ac:plain-text-link-body><![CDATA[After Requirements creation in the table.]]></ac:plain-text-link-body></ac:link></li></ul><p>In the following figure, the <ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirements ]]></ac:plain-text-link-body></ac:link>are decomposed and displayed hierarchically in the <ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link>. For example, the <em>Item purchase</em> Requirement is decomposed into four sub-Requirements: <em>Purchasing facilitation</em>, <em>Purchase request for new items</em>, <em>External global repository</em>, and <em>Item request management</em>.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="5c75c458-a90c-41bc-940b-b725f9192051"><ac:parameter ac:name="title">Requirements hierarchy mode in table</ac:parameter><ac:rich-text-body><p>You can change the Requirements hierarchy in the table by using the <strong>Display Mode</strong> option. This option is described in the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Table toolbars" /></ac:link> page under the Options toolbar.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="req_decomposition_in_req_table.png"><ri:page ri:content-title="Requirements decomposition" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Requirements decomposition in the Requirement Table.</h6><p><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="711db910-bb80-41bd-93bd-b2aa5e9a2508"><ac:parameter ac:name="id">819396999</ac:parameter><ac:rich-text-body><p><strong>Sample model</strong></p><p>The model used in the figures of this page is the <strong>User needs - requirements module for MagicLibrary </strong>sample model that comes with MagicDraw. To open this sample do one of the following:</p><ul><li>Download<span class="confluence-link"><em> <ac:link><ri:attachment ri:filename="User needs - requirements module for MagicLibrary.mdzip"><ri:page ri:space-key="SYSMLP185" ri:content-title="_sample models" /></ri:attachment></ac:link></em>.</span></li><li>Find in modeling tool <em>&lt;modeling tool installation directory&gt;\samples\diagrams\<em>User needs - requirements module for MagicLibrary</em>.mdzip.</em><em><br class="_mce_tagged_br" /></em></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158581 space=SYSMLP2024xR3 version=2 -->
## PAGE 00300: Requirements gap and coverage analysis

- page_id: `227158581`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158581/Requirements+gap+and+coverage+analysis
- version_number: 2
- version_date: `2025-05-02T10:28:19.774+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management
- labels: []

### NORMALIZED CONTENT

820726274

820726277

820726276

You can perform the Requirement gap and coverage analysis by using one of the following:

- [CONFLUENCE_PAGE title='Understanding the user interface' space='SYSMLP2024xR3'] . The diagram pane allows you to display Requirements and other design elements with a drag-and-drop from the [CONFLUENCE_PAGE title='Model Browser' space='SYSMLP2024xR3'] , and draw relationships between them. [CONFLUENCE_PAGE title='Working with paths and relationships' space='MD2024xR3']>]]>

[IMAGE alt='' src='']

###### Displaying requirements on IBD diagram

- [CONFLUENCE_PAGE title='Requirement matrices' space='SYSMLP2024xR3'] . The Requirement matrices enable you to analyze, create, and modify relationships between Requirements and other design elements. They are especially valuable in displaying relationships that cannot be represented in diagrams, such as representations (classes by lifeline), behavior representations in other diagrams, operation representations by Call Behavior Actions, etc. [CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024xR3']>]]>
- [CONFLUENCE_PAGE title='Metric table' space='MD2024xR3']. The Metrics tables allow collecting various metrics used to evaluate the current state of your model. [How to work in Metric table >>](https://docs.nomagic.com/display/MD2024xR3/Metric+table#Metrictable-SpecifictasksintheMetricTable)

820726273

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="faecad8a-47fa-45ea-95b3-e036d5ea0900"><ac:parameter ac:name="id">820726274</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="53f4ee51-6806-4c00-bcf0-14a6609b0f13"><ac:parameter ac:name="id">820726277</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ffb2f609-ced0-4ca6-8382-53e3fe5298ae"><ac:parameter ac:name="id">820726276</ac:parameter><ac:rich-text-body><p>You can perform the Requirement gap and coverage analysis by using one of the following:</p><ul><li class="auto-cursor-target"><ac:link><ri:page ri:content-title="Understanding the user interface" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Diagram pane]]></ac:plain-text-link-body></ac:link>. The diagram pane allows you to display Requirements and other design elements with a drag-and-drop from the <ac:link><ri:page ri:content-title="Model Browser" ri:space-key="SYSMLP2024xR3" /></ac:link>, and draw relationships between them. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with paths and relationships" /><ac:plain-text-link-body><![CDATA[How to work with paths and relationships in diagrams >>]]></ac:plain-text-link-body></ac:link><br /><br /></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="satisfying_requirements.png"><ri:page ri:content-title="Requirements gap and coverage analysis" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Displaying requirements on IBD diagram</h6><ul><li class="auto-cursor-target" style="text-align: left;"><ac:link><ri:page ri:content-title="Requirement matrices" ri:space-key="SYSMLP2024xR3" /></ac:link><span style="color: rgb(23,43,77);">. </span><span style="color: rgb(62,63,64);">The Requirement matrices enable you to analyze, create, and modify relationships between Requirements and other design elements. They are especially valuable in displaying relationships that cannot be represented in diagrams, such as representations (classes by lifeline), behavior representations in other diagrams, operation representations by Call Behavior Actions, etc. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Dependency Matrix" /><ac:plain-text-link-body><![CDATA[How to work in matrices >>]]></ac:plain-text-link-body></ac:link></span></li><li><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Metric table" /><ac:plain-text-link-body><![CDATA[Metric tables]]></ac:plain-text-link-body></ac:link>. The Metrics tables <span style="color: rgb(62,63,64);">allow collecting various metrics used to evaluate the current state of your model. <a href="https://docs.nomagic.com/display/MD2024xR3/Metric+table#Metrictable-SpecifictasksintheMetricTable">How to work in Metric table &gt;&gt;</a></span></span><br /><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);"><br class="_mce_tagged_br" /></span></span></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="51dfb898-d8e9-42a0-8299-9721a0da4de6"><ac:parameter ac:name="id">820726273</ac:parameter><ac:rich-text-body><p><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158570 space=SYSMLP2024xR3 version=2 -->
## PAGE 00301: Requirements management

- page_id: `227158570`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158570/Requirements+management
- version_number: 2
- version_date: `2025-05-02T10:28:19.327+02:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

822970122

822970125

822970123

You can manage your system's Requirements by identifying, describing them, and then organizing them in your project. Requirements management ensures that text-based requirements verify and meet the needs of stakeholders. The following figure illustrates the abilities of modeling Requirements in the modeling tool.

[IMAGE alt='' src='']

###### The main features of model based Requirements.

###### Gather

Capture requirements in the Requirement Diagram and Requirements Table by creating or importing them in the modeling tool. The [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']provides modeling constructs to represent text-based requirements and relates them to other modeling elements. A [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3'] is used to type requirements into a spreadsheet-like table.

###### Import, interchange and synchronize

Once requirements are gathered you can support them as follows:

- [CONFLUENCE_PAGE title='Importing text-based requirements' space='SYSMLP2024xR3'] in ReqIF format from requirement management tools, such as IBM DOORS 9.4 and 9.5, IBM DOORS Next Generation, PTC Integrity, Polarion, Siemens Teamcenter, and other tools.
- Importing and syncing requirements from the most commonly used formats, such as Comma Separated Values (CSV) and Microsoft Excel.
- Keep data synchronized in real time with IBM DOORS or Cameo Requirements+ via No Magic's Cameo DataHub.

###### Relate

The relationships among requirements and design elements (such as SysML Blocks, Test Cases, Use Cases, etc.) create a great value in your model. You can [CONFLUENCE_PAGE title='Creating a relationship' space='MD2024xR3']such as derive, refine, satisfy, or verifydirectly in the[CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']or the[CONFLUENCE_PAGE title='Matrices' space='SYSMLP2024xR3'].

###### Visualize and analyze

Requirements can be visualized in multiple predefined views:

- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Predefined Relation Maps' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Matrices' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Metric table' space='MD2024xR3'] .

The requirements analysis encompasses those tasks that determine the needs or conditions a new or altered product or project must meet. It considers the possibly conflicting requirements of the various stakeholders by analyzing, documenting, validating, and managing software or system requirements.

- Traceability: visualizing, navigating, and analyzing traces from requirements to architecture, business processes or other models related to requirements. Manage Changes with powerful traceability functionality.
- Validation: a facility for evaluating completeness and correctness of the models using built-in and custom validation suites; e.g., you will find not covered requirements, and it will be faster to communicate issues to other team members or fix them.

###### Collaborate

Work on requirements in teams by using the MagicDraw [CONFLUENCE_PAGE title='Teamwork Server Documentation' space='TWS2024xR3'] repository, which enables effective team collaboration, change and configuration management, allows for restricting access to the project, and multisite support. Use [CONFLUENCE_PAGE title='Suspect Links' space='MD2024xR3'] to track changes in requirements that are linked to design elements by satisfy, derive, refine or verify relationships, as well as allow tracking unlinked requirements and deprecated requirements.

###### Verify

With the system parameter calculated, you can verify the system requirement and give the verdict on whether it is satisfied or not. The modeling tool enables you to perform this [CONFLUENCE_PAGE title='Requirements verification' space='SYSMLP2024xR3'].

###### Tailor and Extend

- Support for custom requirement types and adding custom properties for requirements.
- Validation of custom rules.
- Ability to customize existing metric suites and introduce your own.
- Customizable report templates for generating Microsoft Word, Excel, PowerPoint, or other types of documents tailored to the requirements in your specific organization.
- Ability to customize the product so that only the frequently used functionality is visible to the end user.
- Use OpenAPI or scripts to add additional functionality or automate repeatable modeling tasks.

###### Publish

- Built-in Microsoft Word Requirements report for publishing full requirements documentation for communicating to non-model users, reviewing or signing.
- Web portal for requirements projects review by stakeholders. No product installation is required to read requirements; an automated publishing to web server makes up-to-date requirements available for a wide audience.
- Fully customizable report templates to fit your organization requirements for document appearance and contents.

In the following pages you can learn about:

822970121

**White paper**

- [ATTACHMENT filename='Requirements_Writing_in_SysML.pdf']

**Webinar**

- Model-Based Requirements Engineering

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bdc07ae1-0144-41ee-8c3b-b169cb3f5b76"><ac:parameter ac:name="id">822970122</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ba499a70-0e17-45c1-9eec-7fdee99623f0"><ac:parameter ac:name="id">822970125</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dd3a8b24-9d7c-456c-822f-c175959bdf38"><ac:parameter ac:name="id">822970123</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">You can manage your system's Requirements by identifying, describing them, and then organizing them in your project. Requirements management ensures that text-based requirements verify and meet the needs of stakeholders. The following figure illustrates the abilities of modeling Requirements in the modeling tool. </span></p><p><span style="color: rgb(34,34,34);"><ac:image ac:align="center"><ri:attachment ri:filename="cameo_requirements_management_diagram.png"><ri:page ri:content-title="Requirements management" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></p><h6 style="text-align: center;">The main features of model based Requirements.</h6><p><br /></p><h4>Gather</h4><p>Capture requirements in the Requirement Diagram and Requirements Table by creating or importing them in the modeling tool. The <ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link><span style="color: rgb(62,63,64);"> provides modeling constructs to represent text-based requirements and relates them to other modeling elements. <span style="color: rgb(62,63,64);">A <ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link> is used to type requirements into a spreadsheet-like table.</span><span style="color: rgb(62,63,64);"> </span></span></p><h4>Import, interchange and synchronize</h4><p>Once requirements are gathered you can support them as follows:</p><ul><li><ac:link><ri:page ri:content-title="Importing text-based requirements" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Importing requirements]]></ac:plain-text-link-body></ac:link> in ReqIF format from requirement management tools, such as IBM DOORS 9.4 and 9.5, IBM DOORS Next Generation, PTC Integrity, Polarion, Siemens Teamcenter, and other tools.</li><li>Importing and syncing requirements from the most commonly used formats, such as Comma Separated Values (CSV) and Microsoft Excel.</li><li>Keep data synchronized in real time with IBM DOORS or Cameo Requirements+ via No Magic's Cameo DataHub.</li></ul><h4>Relate</h4><p><span style="color: rgb(62,63,64);">The relationships <span style="color: rgb(62,63,64);">among requirements and design elements <span style="color: rgb(62,63,64);">(such as SysML Blocks, Test Cases, Use Cases, etc.)</span> create a great value in your model. <span style="color: rgb(62,63,64);">You can <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating a relationship" /><ac:plain-text-link-body><![CDATA[create relationships]]></ac:plain-text-link-body></ac:link></span><span style="color: rgb(62,63,64);"> such as derive, refine, satisfy, or verify </span><span style="color: rgb(62,63,64);">directly in the </span><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link><span style="color: rgb(62,63,64);"> or the </span><ac:link><ri:page ri:content-title="Matrices" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirement Matrices]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);">.</span></span></span></p><h4>Visualize and analyze</h4><p>Requirements can be visualized in multiple predefined views:</p><ul><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link><ri:page ri:content-title="Predefined Relation Maps" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link><ri:page ri:content-title="Matrices" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Matrices.]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Metric table" /><ac:plain-text-link-body><![CDATA[Metric Tables]]></ac:plain-text-link-body></ac:link>.</li></ul><p><span style="color: rgb(62,63,64);">The requirements analysis encompasses those tasks that determine the needs or conditions a new or altered product or project must meet. It considers the possibly conflicting requirements of the various stakeholders by analyzing, documenting, validating, and managing software or system requirements. </span></p><ul><li>Traceability: visualizing, navigating, and analyzing traces from requirements to architecture, business processes or other models related to requirements. Manage Changes with powerful traceability functionality.</li><li>Validation: a facility for evaluating completeness and correctness of the models using built-in and custom validation suites; e.g., you will find not covered requirements, and it will be faster to communicate issues to other team members or fix them.</li></ul><h4>Collaborate</h4><p>Work on requirements in teams by using the MagicDraw <ac:link><ri:page ri:space-key="TWS2024xR3" ri:content-title="Teamwork Server Documentation" /><ac:plain-text-link-body><![CDATA[Teamwork Server]]></ac:plain-text-link-body></ac:link> repository, which enables effective team collaboration, change and configuration management, allows for restricting access to the project, and multisite support. Use <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Suspect Links" /></ac:link> to t<span style="color: rgb(62,63,64);">rack changes in requirements that are linked to design elements by satisfy, derive, refine or verify relationships, as well as allow tracking unlinked requirements and deprecated requirements.</span></p><h4>Verify</h4><p><span style="color: rgb(62,63,64);">With the system parameter calculated, you can verify the system requirement and give the verdict on whether it is satisfied or not. The modeling tool enables you to perform this <ac:link><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[verification automatically]]></ac:plain-text-link-body></ac:link>.</span></p><h4>Tailor and Extend</h4><ul><li>Support for custom requirement types and adding custom properties for requirements.</li><li>Validation of custom rules.</li><li>Ability to customize existing metric suites and introduce your own.</li><li>Customizable report templates for generating Microsoft Word, Excel, PowerPoint, or other types of documents tailored to the requirements in your specific organization.</li><li>Ability to customize the product so that only the frequently used functionality is visible to the end user.</li><li>Use OpenAPI or scripts to add additional functionality or automate repeatable modeling tasks.</li></ul><h4>Publish</h4><ul><li>Built-in Microsoft Word Requirements report for publishing full requirements documentation for communicating to non-model users, reviewing or signing.</li><li>Web portal for requirements projects review by stakeholders. No product installation is required to read requirements; an automated publishing to web server makes up-to-date requirements available for a wide audience.</li><li>Fully customizable report templates to fit your organization requirements for document appearance and contents.</li></ul><p><br /></p><p>In the following pages you can learn about:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="0ba28db5-0117-4824-959f-ee82a688513f" /></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="25ac7cff-3e97-45e8-8b4e-baf26b231775"><ac:parameter ac:name="id">822970121</ac:parameter><ac:rich-text-body><p><strong>White paper</strong></p><ul><li><ac:link><ri:attachment ri:filename="Requirements_Writing_in_SysML.pdf"><ri:page ri:content-title="Requirements management" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link><strong><br class="_mce_tagged_br" /></strong></li></ul><p><strong>Webinar</strong></p><ul><li><a href="https://blog.nomagic.com/model-based-requirements-engineering/">Model-Based Requirements Engineering</a></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158580 space=SYSMLP2024xR3 version=2 -->
## PAGE 00302: Requirements numbering

- page_id: `227158580`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158580/Requirements+numbering
- version_number: 2
- version_date: `2025-05-02T10:28:19.721+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Requirements numbering' space='CRMP2024xR3']

**Sample model**

The model used in the figures of this page is the **User needs - requirements module for MagicLibrary**sample model that comes with MagicDraw. To open this sample, go tomodeling tool*<modeling tool installation directory>\samples\diagrams\User needs - requirements module for MagicLibrary.mdzip.*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="36222b8f-57d0-42eb-a0ab-dd09cbfdb60b"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Requirements numbering" /></ac:link></ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Sample model</strong></p><p>The model used in the figures of this page is the <strong>User needs - requirements module for MagicLibrary </strong>sample model that comes with MagicDraw. To open this sample, go to<span style="letter-spacing: 0.0px;"> modeling tool </span><em style="letter-spacing: 0.0px;">&lt;modeling tool installation directory&gt;\samples\diagrams\User needs - requirements module for MagicLibrary.mdzip.</em></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158585 space=SYSMLP2024xR3 version=3 -->
## PAGE 00303: Requirements verification

- page_id: `227158585`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158585/Requirements+verification
- version_number: 3
- version_date: `2025-05-02T10:28:19.917+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Additional features of Cameo Simulation Toolkit

823790431

#### CONTENT-COLUMN: Additional features of Cameo Simulation Toolkit

823790433

129321779

**On this page**

43

#### CONTENT-BLOCK: Additional features of Cameo Simulation Toolkit

823790432

Systems Modeling Language (SysML) captures systems design as descriptive and analytical system models, which relate text requirements to the design and provide a baseline for analysis and verification.With the system parameter calculated, you can verify the system requirement and decide whether it is satisfied. The modeling tool enables you to perform this verification automatically.

##### Getting ready for automated Requirements verification

Before performing the automatic Requirements verification, you need to get ready.

To get ready for automated Requirements verification

1. Define the constraint in the Requirement text.
2. Create a Satisfy relationship from the Value Property to the Requirement. The Value Property captures the system parameter whose value determines whether the system requirement is satisfied.
3. Do one of the following:

- 
  - If the **Underline Patterns in Requirement Text** option is enabled, the condition pattern in the Requirement text is underlined. Move the mouse pointer over it to see the expression in the tooltip. If correct, you are ready to perform the automatic Requirement verification. [IMAGE alt='' src=''] Learn more: 
 - [How enable/disable the **Underline Patterns in Requirement Text** option.](https://docs.nomagic.com/display/SYSMLP2024xR3/Using+Requirement+patterns+glossary#UsingRequirementpatternsglossary-Enabling/disablingtheRequirementpatternsunderlininginRequirementtext) - [How to define custom condition patterns.](https://docs.nomagic.com/display/CRMP2024xR3/Using+Requirement+patterns+glossary#UsingRequirementpatternsglossary-Definingcustomconditionpatterns) 
 - [How to check predefined condition patterns.](https://docs.nomagic.com/display/CRMP2024xR3/Using+Requirement+patterns+glossary#UsingRequirementpatternsglossary-Openingthepredefinedrequirementsglossarytable) 
 - [CONFLUENCE_PAGE title='Extracting Constraint from Requirement' space='SYSMLP2024xR3']

- 
  - If the expression in the tooltip is not correct, do the following:

1. 
  1. Perform either of the two options:
    - Right-click a value property in the compartment area of the element shape.
    - Right-click the Requirement.
  2. Select Tools > Extract Constraint Block From Requirement to create a Constraint Block automatically.
  3. You can modify the constraint expression and the parameters as needed (see Figure A below).

You are now ready to perform the automatic Requirement verification.

[IMAGE alt='' src='']

###### In the example above, a Constraint Block with the constraint *{totalMass <= 20}* and the constraint parameters is automatically created. The constraint expression is then modified to*{tm=clm+html+ctm+snm+m}{tm<=20}*.

##### Performing automated Requirements verification in Requirement Table

The automated Requirements verification analysis can be done directly in the Requirement Table. The analysis evaluates whether the property's value that satisfies the Requirement falls within a range of upper and lower bounds extracted from the Requirement text. Additionally, the automatically calculated margin value helps to determine how close the system model is to fulfilling Requirements.

700500

To perform automated Requirements verification

1. [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024xR3'] a Requirement Table. You can also use an existing Requirement Table.
2. [CONFLUENCE_PAGE title='Specifying the scope for the table' space='MD2024xR3'] for the table.
3. Set the context element (i.e., a Block as the table context) to perform the context-specific analysis. The Requirement Table with the *Property*, *Bounds*, *Value,* and *Margin* columns is created, and passing/failing Requirements are marked (see an image below).

[IMAGE alt='' src='']

###### Using the Requirement patterns mechanism, the constraint extracted from the Requirement text is shown in the **Bounds** column. The **Value** column shows the[CONFLUENCE_PAGE title='Initial Values' space='SYSMLP2024xR3']initial value (if it exists) or the default value of the Value Property. Finally, the **Margin** column displays the difference between the calculated and required values.

#### INFO: Verification context in tables

Verification context in tables

- If the table context is unspecified, properties satisfying the Requirements are collected from the entire model.
- When the table context is specified, the Requirement Verification Legend and the verification-specific columns are displayed in the table if they were not before:
  - Property - the Value Property that satisfies the Requirement.
  - Bounds - lower and upper bounds of the required value extracted from the Requirement text.
  - Value - the calculated value (default value or [CONFLUENCE_PAGE title='Initial Values' space='SYSMLP2024xR3'] ) of the property that satisfies the Requirement.
  - Margin - the difference between the calculated value and the required value.

#### WARNING: Requirements verification limitations

Requirements verification limitations

**Table context specification limits** 
The table **context** should be specified with a Block that is recursively composed of no more than 10,000 parts. Otherwise, the **Property**, **Value**, and **Margin**columns are displayed as empty, and the verification analysis is not performed. In such a case, error icons are displayed in the column headers (see image below). 
[IMAGE alt='' src='']

**Requirements refined by Constraint Blocks** The Requirements Verification analysis in the Requirement Table considers constraints extracted directly from the Requirement text only, meaning that the analysis cannot be performed for Requirements refined by Constraint Blocks.

**Simulation configuration option** If an Instance is defined as the Requirement Table context, the Requirements verification analysis does not consider the Simulation configuration option [CONFLUENCE_PAGE title='Recording Verification status of runtime values' space='CST2024xR3'].

##### Performing automated Requirements verification in Instance Table

You can also carry out Requirements verification analysis in an Instance table. While the verification in a Requirement table allows you to perform the analysis for a single instance set as the context, the verification in an Instance table allows you to perform the analysis for multiple instances simultaneously via the **Enable Patterns-Based Verification** option. In an Instance table, the columns represent the properties provided by the classifier specified for the table, and the appropriate cells display the property values specified in the instances you choose to display in the table.

700349

To perform automated Requirements verification in Instance Table

1. [CONFLUENCE_PAGE title='Creating an empty Instance Table' space='MD2024xR3'] an Instance Table.
2. [CONFLUENCE_PAGE title='Specifying the classifier' space='MD2024xR3'] for the table (i.e., the Block containing the properties satisfying the requirements).
3. Set the scope for the table or add individual instances to the table.
4. Select the properties to be displayed in table [CONFLUENCE_PAGE title='Selecting columns to display' space='MD2024xR3'] .
5. In the table toolbar, click the Options button [ATTACHMENT filename='options_button.png'] and select Enable Patterns-Based Verification to enable the verification. The Instance table displays the selected instances and performs the verification, which is visible via the highlighted cells based on their verification status (definition is specified in the Legend). [ATTACHMENT filename='Performing_automated_Requirements_verification_in_Instance_Table.png']

##### Performing automated Requirements verification using simulation

With the help of simulation, you can perform automatic Requirements verification.

To perform automatic Requirements verification, you must have the Cameo Simulation Toolkit installed. [How to install >>](https://docs.nomagic.com/display/CST2024xR3/Installation+and+licensing)

To perform automatic Requirements verification using simulation

1. Right-click the Block, which contains the Value Property.
2. From the shortcut menu, select Simulation > Run .
3. In the **Question** dialog, click **Yes**to load the validation rules and validate the model before the simulation or **No**to simulate the model without validating it.
4. In the Simulation window, click [ATTACHMENT filename='start_button.png'] or press F8 to start the simulation. The result indicating whether or not the value is satisfied is shown in the Variables pane. In the following figure, you can see when the Requirement is not satisfied (highlighted in red) and satisfied (highlighted in green). You can change the value directly in the Value cell, and the Requirement constraint is checked automatically. [ATTACHMENT filename='automatic_req_verification.png']

#### INFO: Additional features of Cameo Simulation Toolkit

Additional features of Cameo Simulation Toolkit

[CONFLUENCE_PAGE title='Elements simulation' space='CST2024xR3']>]]>

[CONFLUENCE_PAGE title='Validation and verification' space='CST2024xR3']>]]>

##### Reviewing Exported Runtime Values in Tables

When you perform Requirements verification using simulation, you can [CONFLUENCE_PAGE title='Exporting runtime objects to InstanceSpecifications' space='CST2024xR3']. The verification data (the constraint, requirement, timestamp, margin, and status) is stored within tagged values of the «VerificationStatus» stereotype, which is applied to the slot values of the exported Instance Specifications.

[IMAGE alt='' src='']

The table below lists the tagged values of the «VerificationStatus» stereotype.

| Tag | Description |
| --- | --- |
| constraint | The name of the constraint against which a value is tested. |
| margin | The result of comparing the tested value (for a property that satisfies a requirement) with the requirement boundary. |
| requirement | The name of the requirement against which a value is tested. |
| status | The verification result (pass or fail). |
| timestamp | The timestamp of the first recorded failure. |

Once the instances are enriched with verification-specific data (exported runtime values), you can use them in either **Instance** or **Requirement** tables to review the verification results. But before that, you need to ensure that the **Enable Patterns-Based Verification**option is turned off.

By default, the **Enable Patterns-Based Verification** option is enabled in Requirement tables and disabled in Instance tables. Make sure to enable/disable it based on the type of verification you want to display.

To learn more, see the [CONFLUENCE_PAGE title='Enable Patterns-Based Verification option' space='SYSMLP2024xR3'] page.

##### Webinar: Automated Requirements Verification

700500

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="72e62747-0cf3-40e2-b341-47d780865d86"><ac:parameter ac:name="id">823790431</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4895fa46-82d0-4cea-89b0-5cf905159d07"><ac:parameter ac:name="id">823790433</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="abcbde1a-1556-47bc-acba-20d99b078951"><ac:parameter ac:name="id">129321779</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="c7b2a751-c3f7-4320-a85a-649d8a7627b9"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="33941b40-1dcf-4422-9e6a-e3bf80881931"><ac:parameter ac:name="id">823790432</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Systems Modeling Language (SysML) captures systems design as descriptive and analytical system models, which relate text requirements to the design and provide a baseline for analysis and verification. </span>With the system parameter calculated, you can verify the system requirement and decide whether it is satisfied. The modeling tool enables you to perform this verification automatically.</p><h3>Getting ready for automated Requirements verification</h3><p>Before performing the automatic Requirements verification, you need to get ready.</p><p><br /></p><p>To get ready for automated Requirements verification</p><hr /><ol><li><span style="color: rgb(62,63,64);">Define the constraint in the Requirement text.</span></li><li><p class="auto-cursor-target"><span style="color: rgb(62,63,64);">Create a Satisfy relationship from the Value Property to the Requirement.<br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="df310273-5800-4057-a7b3-b16ef5a10baf"><ac:rich-text-body><p>The Value Property captures the system parameter whose value determines whether the system requirement is satisfied.</p></ac:rich-text-body></ac:structured-macro></li><li><p class="auto-cursor-target"><span style="color: rgb(62,63,64);">Do one of the following:</span></p></li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li class="auto-cursor-target"><p class="auto-cursor-target"><span style="color: rgb(62,63,64);">If the <strong>Underline Patterns in Requirement Text</strong> option is enabled, the condition pattern in the Requirement text is underlined. Move the mouse pointer over it to see the expression in the tooltip. If correct, you are ready to perform the automatic Requirement <span class="confluence-link">verification.</span> </span> <span style="color: rgb(62,63,64);"> <span class="confluence-link"> <br class="_mce_tagged_br" /><ac:image><ri:attachment ri:filename="req_term_glossary.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span> </span> <span style="color: rgb(62,63,64);"> <span class="confluence-link"> <br /></span> </span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ddde3f1a-0a95-4852-9ef9-7fedc7a57885"><ac:rich-text-body><p><span class="confluence-link">Learn more:<br />  - <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Using+Requirement+patterns+glossary#UsingRequirementpatternsglossary-Enabling/disablingtheRequirementpatternsunderlininginRequirementtext">How enable/disable the <strong>Underline Patterns in Requirement Text</strong> option.</a> <span style="color: rgb(62,63,64);"> <br />  - <a href="https://docs.nomagic.com/display/CRMP2024xR3/Using+Requirement+patterns+glossary#UsingRequirementpatternsglossary-Definingcustomconditionpatterns">How to define custom condition patterns.</a> <br />  - <a href="https://docs.nomagic.com/display/CRMP2024xR3/Using+Requirement+patterns+glossary#UsingRequirementpatternsglossary-Openingthepredefinedrequirementsglossarytable">How to check predefined condition patterns.</a> </span> <br />  - <ac:link><ri:page ri:content-title="Extracting Constraint from Requirement" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[How to extract the Constraint from Requirement text.]]></ac:plain-text-link-body></ac:link> <br /></span></p></ac:rich-text-body></ac:structured-macro></li></ul></li></ul><ul><li style="list-style-type: none;background-image: none;"><ul><li class="auto-cursor-target"><span style="color: rgb(62,63,64);">If the </span> <span style="color: rgb(62,63,64);">expression in the tooltip</span> <span style="color: rgb(62,63,64);"> is not correct, </span> <span style="color: rgb(62,63,64);">do the following:</span></li></ul></li></ul><ol><li style="list-style-type: none;background-image: none;"><ol><li class="auto-cursor-target" style="margin-left: 30.0px;">Perform either of the two options:<ul><li class="auto-cursor-target">Right-click a value property in the compartment area of the element shape.</li><li class="auto-cursor-target">Right-click the Requirement.</li></ul></li><li class="auto-cursor-target" style="margin-left: 30.0px;">Select <strong>Tools</strong> &gt; <strong>Extract Constraint Block From Requirement</strong> to create a Constraint Block automatically.</li><li class="auto-cursor-target" style="margin-left: 30.0px;">You can modify the constraint expression and the parameters as needed (see Figure A below).</li></ol></li></ol><p class="auto-cursor-target" style="margin-left: 30.0px;">You are now ready to perform the automatic Requirement <span class="confluence-link" style="letter-spacing: 0.0px;color: rgb(62,63,64);">verification.</span></p><p class="_mce_tagged_br"><span style="color: rgb(62,63,64);"> <span class="confluence-link"> <ac:image ac:align="center"><ri:attachment ri:filename="refine_req.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span> </span></p><h6 class="auto-cursor-target" style="text-align: center;">In the example above, a Constraint Block with the constraint <em>{totalMass &lt;= 20}</em> and the constraint parameters is automatically created. The constraint expression is then modified to<em> {tm=clm+html+ctm+snm+m}{tm&lt;=20}</em>.</h6><h3 class="_mce_tagged_br">Performing automated Requirements verification in Requirement Table </h3><p>The automated Requirements verification analysis can be done directly in the Requirement Table. The analysis evaluates whether the property's value that satisfies the Requirement falls within a range of upper and lower bounds extracted from the Requirement text. Additionally, the automatically calculated margin value helps to determine how close the system model is to fulfilling Requirements.  </p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="f904dec2-a9d2-4f82-bb99-a0f8d7c869d4"><ac:parameter ac:name="width">700</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=6fQ1F-YCTxY&amp;t" /></ac:parameter><ac:parameter ac:name="height">500</ac:parameter></ac:structured-macro></p><p><br /></p><p>To perform automated Requirements verification</p><hr /><ol><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[Create ]]></ac:plain-text-link-body></ac:link>a Requirement Table. You can also use an existing Requirement Table. </li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specifying the scope for the table" /><ac:plain-text-link-body><![CDATA[Specify the scope]]></ac:plain-text-link-body></ac:link> for the table.</li><li><p class="auto-cursor-target">Set the context element (i.e., a Block as the table context) to perform the context-specific analysis. </p><p class="auto-cursor-target">The Requirement Table with the <em style="letter-spacing: 0.0px;">Property</em>, <em style="letter-spacing: 0.0px;">Bounds</em>, <em style="letter-spacing: 0.0px;">Value,</em> and <em style="letter-spacing: 0.0px;">Margin</em> columns is created, and passing/failing Requirements are marked (see an image below). </p></li></ol><p><ac:image ac:align="center"><ri:attachment ri:filename="requirements_verification_example_1.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Using the Requirement patterns mechanism, the constraint extracted from the Requirement text is shown in the <strong>Bounds</strong> column. The <strong>Value</strong> column shows the<ac:link><ri:page ri:content-title="Initial Values" ri:space-key="SYSMLP2024xR3" /><ac:link-body> <span class="inline-comment-marker">initial value</span> </ac:link-body></ac:link> (if it exists) or the default value of the Value Property. Finally, the <strong>Margin</strong> column displays the difference between the calculated and required values.</h6><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b6c2babd-be53-4fd3-8f38-54f6814b4463"><ac:parameter ac:name="title">Verification context in tables</ac:parameter><ac:rich-text-body><ul><li>If the<strong> </strong>table <strong>context</strong> is unspecified, properties satisfying the Requirements are collected from the entire model.</li><li>When the table <strong>context</strong> is specified, the Requirement Verification Legend and the verification-specific columns are displayed in the table if they were not before:<br /><ul><li><strong>Property</strong> - the Value Property that satisfies the Requirement.<strong> <br /></strong></li><li><strong>Bounds</strong> - lower and upper bounds of the required value extracted from the Requirement text. </li><li><strong>Value</strong> - the calculated value (default value or<ac:link><ri:page ri:content-title="Initial Values" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[ initial value]]></ac:plain-text-link-body></ac:link>) of the property that satisfies the Requirement. </li><li><strong>Margin</strong> - the difference between the calculated value and the required value. </li></ul></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="c6496cd6-45a0-4a6a-9f9f-688de43b742f"><ac:parameter ac:name="title">Requirements verification limitations</ac:parameter><ac:rich-text-body><p style="padding-top: 9.0px;"><strong>Table context specification limits</strong> <br />The table <strong>context</strong> should be specified with a Block that is recursively composed of no more than 10,000 parts. Otherwise, the <strong>Property</strong>, <strong>Value</strong>, and <strong>Margin </strong>columns are displayed as empty, and the verification analysis is not performed. In such a case, error icons are displayed in the column headers (see image below).<br /><ac:image><ri:attachment ri:filename="error_icon_requirement_table.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p class="auto-cursor-target"><strong>Requirements refined by Constraint Blocks<br /></strong> <span>The Requirements Verification analysis in the Requirement Table considers constraints extracted directly from the Requirement text only, meaning that the analysis cannot be performed for Requirements refined by Constraint Blocks.</span></p><p><strong> <span style="color: rgb(62,63,64);">Simulation configuration option<br /></span> </strong> <span style="color: rgb(62,63,64);">If an Instance is defined as the Requirement Table context, the Requirements verification analysis does not consider the Simulation configuration option </span> <ac:link ac:anchor="Remember Failure Status option"><ri:page ri:space-key="CST2024xR3" ri:content-title="Recording Verification status of runtime values" /><ac:plain-text-link-body><![CDATA[Remember Failure Status]]></ac:plain-text-link-body></ac:link><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="8fb4b6d4-c09f-4244-b1c8-e2c39a17f992">.</ac:inline-comment-marker> </span></p></ac:rich-text-body></ac:structured-macro><h3 class="_mce_tagged_br">Performing automated Requirements verification in Instance Table</h3><p>You can also carry out Requirements verification analysis in an Instance table. While the verification in a Requirement table allows you to perform the analysis for a single instance set as the context, the verification in an Instance table allows you to perform the analysis for multiple instances simultaneously via the <strong>Enable Patterns-Based Verification</strong> option. <span>In an Instance table, the columns represent the properties provided by the classifier specified for the table, and the appropriate cells display the property values specified in the instances you choose to display in the table. </span></p><p><span style="color: rgb(23,43,77);"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="a292c6c8-e8ca-4be7-a4ec-7ede97660484"><ac:parameter ac:name="width">700</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=HqLWx9k02Dg&amp;ab_channel=NoMagic" /></ac:parameter><ac:parameter ac:name="height">349</ac:parameter></ac:structured-macro></span></p><p>To perform automated Requirements verification in Instance Table</p><hr /><ol><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating an empty Instance Table" /><ac:plain-text-link-body><![CDATA[Create ]]></ac:plain-text-link-body></ac:link>an Instance Table.</li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specifying the classifier" /><ac:plain-text-link-body><![CDATA[Specify the classifier]]></ac:plain-text-link-body></ac:link> for the table (i.e., the Block containing the properties satisfying the requirements).</li><li>Set the scope for the table or <a href="https://docs.nomagic.com/display/MD2024xR3/Filling+the+table+with+instances#Fillingthetablewithinstances-add_existing_instances">add individual instances</a> to the table. </li><li>Select the properties to be displayed in table <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Selecting columns to display" /><ac:plain-text-link-body><![CDATA[columns]]></ac:plain-text-link-body></ac:link>.</li><li>In the table toolbar, click the <strong>Options </strong>button <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="options_button.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>and select <strong>Enable Patterns-Based Verification</strong> to enable the verification.<br />The Instance table displays the selected instances and performs the verification, which is visible via the highlighted cells based on their verification status (definition is specified in the Legend).<br /><ac:image><ri:attachment ri:filename="Performing_automated_Requirements_verification_in_Instance_Table.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ol><h3>Performing automated Requirements verification using simulation</h3><p>With the help of simulation, you can perform automatic Requirements verification.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="35116cdd-a32c-4c13-b1a8-a1794274a0c6"><ac:rich-text-body><p>To perform automatic Requirements verification, you must have the Cameo Simulation Toolkit installed. <a href="https://docs.nomagic.com/display/CST2024xR3/Installation+and+licensing">How to install &gt;&gt;</a></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To perform automatic Requirements verification using simulation</p><hr /><ol><li>Right-click the Block, which contains the Value Property.</li><li>From the shortcut menu, select <strong>Simulation</strong> &gt; <strong>Run</strong>.</li><li><p class="auto-cursor-target">In the <strong>Question</strong> dialog, c<span style="color: rgb(62,63,64);">lick </span> <strong>Yes </strong><span style="color: rgb(62,63,64);">to load the validation rules and validate the model before the simulation or </span> <strong>No </strong><span style="color: rgb(62,63,64);">to simulate the model without validating it.<br /></span></p></li><li>In the Simulation window, click <ac:image ac:title="Start" ac:alt="Start"><ri:attachment ri:filename="start_button.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>or press F8 to start the simulation.<br />The result indicating whether or not the value is satisfied is shown in the Variables pane. In the following figure, you can see when the Requirement is not satisfied (highlighted in red) and satisfied (highlighted in green). You can change the value directly in the Value cell, and the Requirement constraint is checked automatically.<br /><ac:image><ri:attachment ri:filename="automatic_req_verification.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> <br /><br /></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b64b6b6c-0080-41bc-8b22-9760f56ebfc0"><ac:parameter ac:name="title">Additional features of Cameo Simulation Toolkit</ac:parameter><ac:rich-text-body><p><ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Elements simulation" /><ac:plain-text-link-body><![CDATA[Learn more about how to perform verification for a single element >>]]></ac:plain-text-link-body></ac:link></p><p><ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Validation and verification" /><ac:plain-text-link-body><![CDATA[Learn more about how to validate the model against a set of validation rules before executing it >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><h3><span>Reviewing Exported Runtime Values in Tables</span></h3><p><span>When you perform Requirements verification using simulation, you can <ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Exporting runtime objects to InstanceSpecifications" /><ac:plain-text-link-body><![CDATA[export the simulated runtime values to Instance Specifications]]></ac:plain-text-link-body></ac:link>. The verification data (the constraint, requirement, timestamp, margin, and status) is stored within tagged values of the «VerificationStatus» stereotype, which is applied to the slot values of the exported Instance Specifications.<br /></span></p><p><span> <ac:image ac:align="center"><ri:attachment ri:filename="verification_status_tagged_values.png"><ri:page ri:content-title="Requirements verification" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> <br /></span></p><p>The table below lists the tagged values of the <span>«VerificationStatus»</span> stereotype.</p><table class="relative-table wrapped"><colgroup> <col /> <col /> </colgroup><tbody><tr><th><p>Tag</p></th><th colspan="1">Description</th></tr><tr><td colspan="1"><strong>constraint</strong></td><td colspan="1">The name of the constraint against which a value is tested.</td></tr><tr><td colspan="1"><strong>margin</strong></td><td colspan="1"><p>The result of comparing the tested value (for a property that satisfies a requirement) with the requirement boundary.</p></td></tr><tr><td><p><strong>requirement <br /></strong></p></td><td colspan="1">The name of the requirement against which a value is tested.</td></tr><tr><td><p><strong>status</strong></p></td><td colspan="1">The verification result (pass or fail).</td></tr><tr><td colspan="1"><strong>timestamp</strong></td><td colspan="1">The timestamp of the first recorded failure.</td></tr></tbody></table><p><span>Once the instances are enriched with verification-specific data (exported runtime values), you can use them in either <strong>Instance</strong> or <strong>Requirement</strong> tables to review the verification results. But before that, you need to ensure that the <strong>Enable Patterns-Based Verification </strong>option is turned off. </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="af7ffaf7-c23d-4e4c-bfa8-ca55377afa06"><ac:rich-text-body><p>By default, the <strong>Enable Patterns-Based Verification</strong> option is enabled in Requirement tables and disabled in Instance tables. Make sure to enable/disable it based on the type of verification you want to display.</p></ac:rich-text-body></ac:structured-macro><p><span>To learn more, see the <ac:link><ri:page ri:content-title="Enable Patterns-Based Verification option" ri:space-key="SYSMLP2024xR3" /></ac:link> page.</span></p><h3><span style="letter-spacing: -0.006em;">Webinar: Automated Requirements Verification</span></h3><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="07ff5246-c4d5-4b41-a7c2-83b1be2c2011"><ac:parameter ac:name="width">700</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=eVzKcnafHpE" /></ac:parameter><ac:parameter ac:name="height">500</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227160238 space=SYSMLP2024xR3 version=2 -->
## PAGE 00304: Reusing and referencing existing Modelica models

- page_id: `227160238`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160238/Reusing+and+referencing+existing+Modelica+models
- version_number: 2
- version_date: `2025-05-02T10:28:47.520+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Modelica export
- labels: ['modelica-port', 'modelica-parameter', 'modelica-block']

### NORMALIZED CONTENT

284843692

284843705

284843690

**On this page**

5

284843694

##### Introduction

The «ModelicaBlock», «ModelicaParameter» and «ModelicaPort»stereotypes are created to specify which SysML properties (including ports) of its blocks correspond to Modelica library reusable component.The semantics of these elements are given by the corresponding elements in the Modelica libraries.For more details, readthe[OMG SysPhS specification](https://www.omg.org/spec/SysPhS/About-SysPhS/).

The figure below shows how the «ModelicaBlock», «ModelicaParameter» and «ModelicaPort»stereotypes are definedin the SysML profile.

[IMAGE alt='' src='']

###### Modelica stereotypes.

##### Using «ModelicaBlock» stereotype

Apply «ModelicaBlock» stereotype for a [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] to reference its [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] withan equivalent componentin the Modelica library.The value of the name tag must be a fully qualified name (e.g. Modelica.Electrical.Analog.Basic.Capacitor) of the corresponding component in the Modelica library. >]]>[CONFLUENCE_PAGE title='Reusing and referencing existing Modelica models' space='SYSMLP2024xR3']

[IMAGE alt='' src='']

###### The «ModelicaBlock» stereotype applied for a *Capacitor* Block and created referenceto corresponding component in the Modelica library.

##### Using «ModelicaParameter» stereotype

Apply «ModelicaParameter» stereotype for a [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] to reference it with an equivalent parameter of a Modelica library.The stereotyped Value Property must be owned by a Block stereotyped by «ModelicaBlock». The value of the name tag is the name of the corresponding parameter, and the value attribute gives the value of this parameter. If the value is empty, the value of the parameter must be given using initial values of the stereotyped property.

In the following image, after the «ModelicaParameter» stereotype is applied for the *r* Value Property, its name tag value is referenced with the parameter *R* in the Modelica library. >]]>[CONFLUENCE_PAGE title='Reusing and referencing existing Modelica models' space='SYSMLP2024xR3'] 
[IMAGE alt='' src='']

###### The «ModelicaBlock» *Resistor* owns *r* Value Property stereotyped by «ModelicaParameter» and created reference tothe Modelica library component.

##### Using «ModelicaPort» stereotype

Apply «ModelicaPort» stereotype for a port to reference it with an equivalent port in the Modelica library. The stereotyped port must be owned by a Block with «ModelicaBlock» stereotype applied.The value of the name tag gives the name of the corresponding port in the Modelica library. >]]>[CONFLUENCE_PAGE title='Reusing and referencing existing Modelica models' space='SYSMLP2024xR3']

[IMAGE alt='' src='']

###### The «ModelicaBlock» *Ground* owns *p* Proxy Port stereotyped by «ModelicaPort» and created reference to the Modelica library component.

##### Referencing with Modelica library components

To reference SysML elements with Modelica library components

1. Apply « ModelicaBlock », «ModelicaParameter» and «ModelicaPort» stereotypes respectively for [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'], [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] and [CONFLUENCE_PAGE title='Proxy Port' space='SYSMLP2024xR3'] . [How to apply stereotype >>](https://docs.nomagic.com/display/MD2024xR3/Stereotype#Stereotype-Applyingastereotype)
2. In the [CONFLUENCE_PAGE title='Specification window' space='MD2024xR3'], make sure the **Expert** or **All** mode is selected.
3. Select the **Tags** property group, make sure [IMAGE alt='' src=''] is switched off.
4. Select the *name* property and click **Create Value**.
5. Type the name of the corresponding component in the Modelica library as follows: 
 - for a Block type thefully qualified name,e.g. *Modelica.Electrical.Analog.Basic.Resistor*. 
 - for a Value Property type the parameter name, e.g. *R*. 
 - for a port type the port name, e.g. *p*.
6. Click **Close**. 
The SysML elements are referenced with the component in the Modelica library.

The figure below shows a comparison between exported model without and with references to the Modelica library components. [CONFLUENCE_PAGE title='Modelica export' space='SYSMLP2024xR3']>]]>

[IMAGE alt='' src='']

284848653

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c88367ed-2c3a-48af-bfa3-3db0ab20c1f5"><ac:parameter ac:name="id">284843692</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="385435a7-d302-4084-bfe5-a8c1671a1898"><ac:parameter ac:name="id">284843705</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="22d5bb49-26fc-4914-a34e-1021a7de6748"><ac:parameter ac:name="id">284843690</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="693c430c-4157-4753-b7b1-6e338df535d1"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b942815f-919b-4072-8c39-427578e3f754"><ac:parameter ac:name="id">284843694</ac:parameter><ac:rich-text-body><h3>Introduction</h3><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span>The «</span><span>ModelicaBlock</span><span>», <span>«ModelicaParameter»</span></span> and <span> «ModelicaPort» </span>stereotypes are created to specify which <span style="color: rgb(51,51,51);">SysML properties (including ports) of its blocks <span style="color: rgb(51,51,51);">correspond to Modelica</span></span> library reusable component.</span></span><span style="color: rgb(51,51,51);"> The semantics of these elements are given by the corresponding elements in the Modelica libraries.  </span><span style="color: rgb(62,63,64);">For more details, read </span><span style="color: rgb(62,63,64);">the </span><a href="https://www.omg.org/spec/SysPhS/About-SysPhS/" class="external-link" style="letter-spacing: 0.0px;" rel="nofollow">OMG SysPhS specification</a><span style="color: rgb(62,63,64);">.</span></p><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">The figure below shows how the <span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">«</span><span style="color: rgb(51,51,51);">ModelicaBlock</span><span style="color: rgb(51,51,51);">», <span style="color: rgb(51,51,51);">«ModelicaParameter»</span></span> and <span style="color: rgb(51,51,51);"> «ModelicaPort» </span>stereotypes are defined </span><span style="color: rgb(51,51,51);">in the SysML profile. </span></span></span></p><p><ac:image ac:align="center" ac:height="199"><ri:attachment ri:filename="modelica_stereotypes.png"><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Modelica stereotypes.</h6><h3><span style="color: rgb(51,51,51);">Using «ModelicaBlock» stereotype</span></h3><p><span style="color: rgb(51,51,51);">Apply «ModelicaBlock» stereotype for a <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link> to reference its <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link> with </span><span style="color: rgb(51,51,51);">an equivalent <span style="color: rgb(51,51,51);">component </span>in the Modelica library</span><span style="color: rgb(51,51,51);">. </span><span style="color: rgb(51,51,51);">The value of the name tag must be a fully qualified name (e.g. Modelica.Electrical.Analog.Basic.Capacitor) of the corresponding component in the Modelica library. <ac:link ac:anchor="Referencing with Modelica library components"><ac:plain-text-link-body><![CDATA[How to reference Block properties with Modelica library component >>]]></ac:plain-text-link-body><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ac:link></span></p><p><span style="color: rgb(51,51,51);"><span><ac:image ac:align="center"><ri:attachment ri:filename="modelica_block_reference.png"><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);"><span><span style="color: rgb(51,51,51);">The <span style="color: rgb(51,51,51);">«ModelicaBlock»</span> stereotype applied for a <em>Capacitor</em> Block and created reference</span><span style="color: rgb(51,51,51);"> to corresponding component in the Modelica library.</span></span></span></h6><h3>Using «ModelicaParameter» stereotype</h3><p>Apply «ModelicaParameter» stereotype for a <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> <span style="color: rgb(51,51,51);">to reference it with an equivalent parameter of a Modelica library</span><span style="color: rgb(51,51,51);">. </span>The stereotyped Value Property must be owned by a Block stereotyped by <span style="color: rgb(51,51,51);">«</span>ModelicaBlock<span style="color: rgb(51,51,51);">»</span>. The value of the name tag is the name of the corresponding parameter, and the value attribute gives the value of this parameter. If the value is empty, the value of the parameter must be given using initial values of the stereotyped property.</p><p><span style="color: rgb(51,51,51);">In the following image, after the «ModelicaParameter» stereotype is applied for the <em>r</em> Value Property, its name tag value is referenced with the <span>parameter <em>R</em> in the Modelica library. <ac:link ac:anchor="Referencing with Modelica library components"><ac:plain-text-link-body><![CDATA[How to reference Value Property with Modelica library parameter >>]]></ac:plain-text-link-body><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span><br /><span style="color: rgb(51,51,51);"><span><ac:image ac:align="center"><ri:attachment ri:filename="value_property _reference.png"><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);"><span><span style="color: rgb(51,51,51);">The <span style="color: rgb(51,51,51);">«ModelicaBlock» </span> <em>Resistor</em> owns <em>r</em> Value Property stereotyped by «ModelicaParameter» and created reference to </span><span style="color: rgb(51,51,51);">the Modelica library component.</span></span></span></h6><h3>Using «ModelicaPort» stereotype</h3><p>Apply «ModelicaPort» stereotype for a port <span style="color: rgb(51,51,51);">to reference it with an equivalent port in the Modelica library</span><span style="color: rgb(51,51,51);">. The stereotyped port must be owned by a Block with <span style="color: rgb(51,51,51);">«</span>ModelicaBlock<span style="color: rgb(51,51,51);">» <span style="color: rgb(51,51,51);">stereotype applied. </span></span></span><span style="letter-spacing: 0.0px;">The value of the name tag gives the name of the corresponding port in the Modelica library. <ac:link><ac:plain-text-link-body><![CDATA[How to reference port with Modelica library port >>]]></ac:plain-text-link-body><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ac:link></span></p><p><span style="letter-spacing: 0.0px;"><ac:image ac:align="center"><ri:attachment ri:filename="port_reference.png"><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);">The <span>«ModelicaBlock» </span> <em>Ground</em> owns <em>p</em> Proxy Port stereotyped by «ModelicaPort» and created reference to the Modelica library component.</span></h6><h3>Referencing with Modelica library components</h3><p><br /></p><p>To reference SysML elements with Modelica library components</p><hr /><ol><li>Apply <span style="color: rgb(51,51,51);">«</span><span style="color: rgb(51,51,51);">ModelicaBlock</span><span style="color: rgb(51,51,51);">», «ModelicaParameter» and «ModelicaPort»  </span><span style="color: rgb(51,51,51);">stereotypes respectively for <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>, <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> and <ac:link><ri:page ri:content-title="Proxy Port" ri:space-key="SYSMLP2024xR3" /></ac:link></span><span style="color: rgb(51,51,51);">. <a href="https://docs.nomagic.com/display/MD2024xR3/Stereotype#Stereotype-Applyingastereotype">How to apply stereotype &gt;&gt;</a><br /></span></li><li><span style="color: rgb(51,51,51);">In the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specification window" /></ac:link>, make sure the <strong>Expert</strong> or <strong>All</strong> mode is selected.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>Tags</strong> property group, make sure <ac:image ac:title="Show Tags with Values" ac:thumbnail="true" ac:alt="Show Tags with Values" ac:height="19"><ri:attachment ri:filename="show_tags_with_values.png"><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> is switched off.</span></li><li><span style="color: rgb(51,51,51);">Select the <em>name</em> property and click <strong>Create Value</strong>.</span></li><li><span style="color: rgb(51,51,51);">Type the name of the corresponding component in the Modelica library as follows:<br /> - for a Block t<span style="color: rgb(51,51,51);">ype the </span><span style="color: rgb(51,51,51);">fully qualified name, </span>e.g. <em>Modelica.Electrical.Analog.Basic.Resistor</em>.<br /> - for a Value Property type the parameter <span style="color: rgb(51,51,51);">name, e.g. <em>R</em>.<br /> - for a port type the port name, e.g. <em>p</em>. </span><br /></span></li><li><span style="color: rgb(51,51,51);">Click <strong>Close</strong>.<br />The SysML elements are referenced with the component in the Modelica library. </span></li></ol><p><span style="color: rgb(51,51,51);">The figure below shows a comparison between exported model without and with references to the Modelica library components. <ac:link><ri:page ri:content-title="Modelica export" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[How to export your model to Modelica file >>]]></ac:plain-text-link-body></ac:link></span></p><p><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="comparison_of_model_export_with_and_without_references_to_modelica_library_components.png"><ri:page ri:content-title="Reusing and referencing existing Modelica models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p><p><span style="color: rgb(51,51,51);"><br /></span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d4f11c7d-8d9c-4f0b-86e2-13c93dedc3de"><ac:parameter ac:name="id">284848653</ac:parameter><ac:rich-text-body><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227160088 space=SYSMLP2024xR3 version=1 -->
## PAGE 00305: Reusing and referencing Simulink models

- page_id: `227160088`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160088/Reusing+and+referencing+Simulink+models
- version_number: 1
- version_date: `2024-03-08T14:39:49.581+01:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Simulink export
- labels: ['simulink-port', 'simulink-block', 'simulink-parameter']

### NORMALIZED CONTENT

**On this page**

5

##### Introduction

The «SimulinkBlock», «SimulinkParameter» and «SimulinkPort» stereotypes are created to specify which SysML properties (including ports) of its blocks correspond to Simulinklibrary reusable component.The semantics of these elements are given by the corresponding elements in the Simulink libraries.For more details, readthe[OMG SysPhS specification](https://www.omg.org/spec/SysPhS/About-SysPhS/).

The figure below shows how the «SimulinkBlock», «SimulinkParameter» and «SimulinkPort» stereotypes are defined in the SysML profile.

[IMAGE alt='' src='']

###### Simulink stereotypes.

##### Using «SimulinkBlock» stereotype

Apply the «SimulinkBlock» stereotype for a [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] to reference its [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] with an equivalent component in Simulink. The value of the name tag must be a type of a Simulink Block (e.g. "Trigonometry").

###### [IMAGE alt='' src='']The «SimulinkBlock» stereotype is applied to the *Sin*Block and a reference is created to the corresponding component in the Simulink library.

You can also reference an already existing Simulink Model. To do that, set the "name" tag to "ModelReference", and the "url" tag to the name of the Simulink file.

When exporting a SysML element to a Simulink file, you can have the <<SimulinkBlock>> stereotype automatically applied to the Block. In such a case, the "name" and the "url" tags are automatically filled. When a part of this Block is exported, a reference to an already exported Simulink file is created instead of a full part export.

[IMAGE alt='' src='']

##### Using «SimulinkParameter» stereotype

Apply the «SimulinkParameter» stereotype for a [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] to reference it with an equivalent parameter of a Simulink library. The stereotyped Value Property must be owned by a Block stereotyped by «SimulinkBlock». The value of the name tag is the name of the corresponding parameter, and the value attribute gives the value of this parameter. If the value is empty, the value of the parameter must be given using the initial values of the stereotyped property. If the name tag is empty, the property name will be used instead.

In the following image, the «SimulinkParameter» stereotype is applied for the "operator" Value Property under the "Sin" Block described in the previous section. This property defines which Trigonometry operator is used on Simulink.

###### [IMAGE alt='' src='']The «SimulinkBlock» *Sin*owns *operator* Value Property stereotyped by «SimulinkParameter» with a reference tothe Simulink library component.

##### Using «SimulinkPort» stereotype

Apply the «SimulinkPort» stereotype for a port to reference it with an equivalent port in the Simulink library. The stereotyped port must be owned by a Block with the «SimulinkBlock» stereotype applied. The value of the name tag gives the name of the corresponding port in the Simulink library.

###### [IMAGE alt='' src='']The«SimulinkBlock»*Ground*owns*p*Proxy Port stereotyped by «SimulinkPort» with a reference to the Simulink library component.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4bd57bb4-c11c-494f-93a9-34887a10f3b7"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p><h3>Introduction</h3><p><span style="color: rgb(51,51,51);">The «SimulinkBlock», «SimulinkParameter» and  «SimulinkPort» stereotypes are created to specify which <span>SysML properties (including ports) of its blocks correspond to Simulink </span>library reusable component.</span><span style="color: rgb(51,51,51);"> The semantics of these elements are given by the corresponding elements in the Simulink libraries.  </span><span style="color: rgb(62,63,64);">For more details, read </span><span style="color: rgb(62,63,64);">the </span><a class="external-link" href="https://www.omg.org/spec/SysPhS/About-SysPhS/" rel="nofollow">OMG SysPhS specification</a><span style="color: rgb(62,63,64);">.</span></p><p><span style="color: rgb(51,51,51);"><span>The figure below shows how the «SimulinkBlock», «SimulinkParameter» and «SimulinkPort» stereotypes are defined in the SysML profile. </span></span></p><p><span style="color: rgb(51,51,51);"><span><ac:image ac:align="center"><ri:attachment ri:filename="simulink_block.png"><ri:page ri:content-title="Reusing and referencing Simulink models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></span></p><h6 style="text-align: center;"><span style="color: rgb(51,51,51);"><span>Simulink stereotypes.</span></span></h6><h3><span style="color: rgb(51,51,51);">Using «SimulinkBlock» stereotype</span></h3><p>Apply the «SimulinkBlock» stereotype for a <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link> to reference its <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link> with an equivalent component in Simulink. The value of the name tag must be a type of a Simulink Block (e.g. &quot;Trigonometry&quot;).</p><h6 style="text-align: center;"><span style="color: rgb(255,0,0);"><ac:image ac:align="center"><ri:attachment ri:filename="SimulinkBlock.PNG"><ri:page ri:content-title="Reusing and referencing Simulink models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span>The «SimulinkBlock» stereotype is applied to the <em>Sin </em>Block and a reference is created to the corresponding component in the Simulink library.</h6><p>You can also reference an already existing Simulink Model. To do that, set the &quot;name&quot; tag to &quot;ModelReference&quot;, and the &quot;url&quot; tag to the name of the Simulink file.</p><p>When exporting a SysML element to a Simulink file, you can have the &lt;&lt;SimulinkBlock&gt;&gt; stereotype automatically applied to the Block. In such a case, the &quot;name&quot; and the &quot;url&quot; tags are automatically filled. When a part of this Block is exported, a reference to an already exported Simulink file is created instead of a full part export.</p><p style="text-align: left;"><span style="color: rgb(255,0,0);"><ac:image ac:align="center"><ri:attachment ri:filename="SimulinkExport.png"><ri:page ri:content-title="Reusing and referencing Simulink models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></p><h3>Using «SimulinkParameter» stereotype</h3><p>Apply the «SimulinkParameter» stereotype for a <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> to reference it with an equivalent parameter of a Simulink library. The stereotyped Value Property must be owned by a Block stereotyped by «SimulinkBlock». The value of the name tag is the name of the corresponding parameter, and the value attribute gives the value of this parameter. If the value is empty, the value of the parameter must be given using the initial values of the stereotyped property. If the name tag is empty, the property name will be used instead.</p><p>In the following image, the «SimulinkParameter» stereotype is applied for the &quot;operator&quot; Value Property under the &quot;Sin&quot; Block described in the previous section. This property defines which Trigonometry operator is used on Simulink.</p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="SimulinkParameter.png"><ri:page ri:content-title="Reusing and referencing Simulink models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><span style="color: rgb(51,51,51);">The «SimulinkBlock» <em>Sin </em>owns <em>operator</em> Value Property stereotyped by «SimulinkParameter» with a reference to </span><span style="color: rgb(51,51,51);">the Simulink library component.</span></h6><h3>Using «SimulinkPort» stereotype</h3><p>Apply the «SimulinkPort» stereotype for a port to reference it with an equivalent port in the Simulink library. The stereotyped port must be owned by a Block with the «SimulinkBlock» stereotype applied. The value of the name tag gives the name of the corresponding port in the Simulink library. </p><h6 style="text-align: center;"><span><ac:image ac:align="center"><ri:attachment ri:filename="SimulinkPort.png"><ri:page ri:content-title="Reusing and referencing Simulink models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span><span><span style="color: rgb(51,51,51);">The </span><span style="color: rgb(51,51,51);">«SimulinkBlock» </span><span style="color: rgb(51,51,51);"> </span><em style="text-align: center;">Ground</em><span style="color: rgb(51,51,51);"> owns </span><em style="text-align: center;">p</em><span style="color: rgb(51,51,51);"> Proxy Port stereotyped by «SimulinkPort» with a reference to the Simulink library component.</span></span></h6><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227158884 space=SYSMLP2024xR3 version=2 -->
## PAGE 00306: Rollup Pattern Wizard

- page_id: `227158884`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158884/Rollup+Pattern+Wizard
- version_number: 2
- version_date: `2025-05-02T10:28:25.319+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks
- labels: ['rollups', 'rollup-pattern', 'pattern']

### NORMALIZED CONTENT

1348219185

1348219188

1348296621

**On this page**

33

1348219187

##### Introduction

Rollup calculations are among the most common use cases in systems engineering. System modelers want to calculate total mass, cost, power, or another system dimension, based on individual values of all the parts in the model. The pattern can recursively propagate the particular value up a hierarchy of components characterized by this value.

The **Rollup Pattern** **Wizard** allows you to calculate the total cost, mass, power, or another system metric of elements in the model. Different types of [CONFLUENCE_PAGE title='Creating new Rollup Pattern Block' space='SYSMLP2024xR3']pattern Blocks can be created to suit the calculation needs. This new modeling tool provides three [CONFLUENCE_PAGE title='Default Rollup Pattern Blocks' space='SYSMLP2024xR3'] that calculate the total cost, mass, or power. You can apply the default or newly created pattern Block by using the **Rollup Pattern** **Wizard**. It automatically [CONFLUENCE_PAGE title='Applying Rollup Pattern Blocks' space='SYSMLP2024xR3'] (using the [CONFLUENCE_PAGE title='Generalization' space='MD2024xR3']) to any number of [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] or [CONFLUENCE_PAGE title='Instance Specification' space='MD2024xR3'] recursively, and creates property values. This wizard also allows you to [CONFLUENCE_PAGE title='Removing Rollup Pattern Blocks' space='SYSMLP2024xR3'] from the selected Block or Instance Specification. The procedures below describe how to open and use the **Rollup Pattern Wizard**.

##### Opening the **Rollup Pattern Wizard**

To open the **Rollup Pattern Wizard**

1. From the shortcut menu of the Block or Instance Specification to which you want to apply a pattern Block, select:****
  - **Tools** > **Apply Rollup Pattern**, if you want to apply a pattern Block for the selected Block or Instance Specification.
  - **Tools** > **Remove Rollup Pattern**, if you want to remove the pattern Block from the selected Block or Instance Specification.

##### The Rollup Pattern Wizard areas

The **Rollup Pattern Wizard**consists of two areas:

- Select/Remove Pattern Block (1).
- Options (2).

[IMAGE alt='' src='']

###### The Rollup Pattern Wizard when trying to apply a rollup pattern for a Block. Two areas of the wizard are highlighted: 1- Select Pattern Block, 2 -Options.

The procedures below describe how to work with the **Rollup Pattern Wizard:**

- [CONFLUENCE_PAGE title='Rollup Pattern Wizard' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Rollup Pattern Wizard' space='SYSMLP2024xR3']

##### select_blockSelecting/ removing the pattern Block

To select/remove the pattern Block

1. Click [ATTACHMENT filename='alt_down.png'] to expand the list of available pattern Blocks.
2. Choose the rollup pattern Block that you want to apply/ remove.

##### select_optionsSelecting the options

| Apply Rollup Pattern Box | Description | Option appears when applying rollup pattern for... |
| --- | --- | --- |
| Apply Recursively | Applies the pattern Block recursively. | Block, Instance Specification |
| Set Role Name | Sets the role names of Part Properties. | Block |
| Set Subsetted Properties | Sets the Subsetted Properties of the Part Properties. | Block |
| Create Value Properties and Redefine | Creates and redefines Value Properties. | Block |

| Remove Rollup Pattern Box | Description | Option appears when applying rollup pattern for... |
| --- | --- | --- |
| Recursively Remove Rollup Pattern | Removes the pattern Block recursively. | Block, Instance Specification |
| Remove Role Name | Removes the role names of Part Properties. | Block |
| Remove Subsetted Properties | Removes the Subsetted Properties of the Part Properties. | Block |
| Remove Value Properties | Removes Value Properties. | Block |

1348219184

**Related pages**

**Webinar**

- Total Mass, Cost, and Power Rollups

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0561e98e-4b85-4c4e-83e6-bea9a75e62b9"><ac:parameter ac:name="id">1348219185</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d000c91e-fed8-4c5b-9017-23be664c5f08"><ac:parameter ac:name="id">1348219188</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="525788da-ad55-46a0-9a7e-c66fc666a728"><ac:parameter ac:name="id">1348296621</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="5b82747b-2211-4b02-817b-bb1460717284"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b5edb312-f572-4bb4-b48d-607f0475491b"><ac:parameter ac:name="id">1348219187</ac:parameter><ac:rich-text-body><h3><span style="color: rgb(51,51,51);">Introduction</span></h3><p><span style="color: rgb(51,51,51);">Rollup calculations are among the most common use cases in systems engineering. System modelers want to calculate total mass, cost, power, or another system dimension, based on individual values of all the parts in the model. The pattern can recursively propagate the particular value up a hierarchy of components characterized by this value.<br /></span></p><p><span style="color: rgb(51,51,51);">The <strong>Rollup Pattern</strong> <strong>Wizard</strong> allows you to calculate the total cost, mass, power, or another system metric of elements in the model. Different types of <ac:link><ri:page ri:content-title="Creating new Rollup Pattern Block" ri:space-key="SYSMLP2024xR3" /><ac:link-body>pattern <span class="confluence-link">Blocks</span> can be created</ac:link-body></ac:link> to suit the calculation needs. This new modeling tool provides three <ac:link><ri:page ri:content-title="Default Rollup Pattern Blocks" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[default rollup patterns]]></ac:plain-text-link-body></ac:link> that calculate the total <span style="color: rgb(51,51,51);">cost, mass, or power</span>. You can apply the default or newly created pattern Block by using the <strong>Rollup Pattern</strong> <strong>Wizard</strong>. It automatically <ac:link><ri:page ri:content-title="Applying Rollup Pattern Blocks" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[applies pattern Blocks]]></ac:plain-text-link-body></ac:link> (using the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Generalization" /></ac:link>) to any number of <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Blocks]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance Specification" /><ac:plain-text-link-body><![CDATA[Instance Specifications]]></ac:plain-text-link-body></ac:link> recursively, and creates property values. This wizard also allows  you to <ac:link><ri:page ri:content-title="Removing Rollup Pattern Blocks" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[remove pattern Blocks]]></ac:plain-text-link-body></ac:link> <span style="color: rgb(51,51,51);">from the selected Block or Instance Specification.</span> The procedures below describe how to open and use the <span style="color: rgb(51,51,51);"><strong>Rollup Pattern Wizard</strong></span>.<br /> </span></p><h3><span style="color: rgb(51,51,51);">Opening the <strong>Rollup Pattern Wizard</strong></span></h3><p><span style="color: rgb(51,51,51);">To open the <strong>Rollup Pattern Wizard</strong> </span></p><hr /><ol><li><span style="color: rgb(51,51,51);">From the shortcut menu of the Block or Instance Specification to which you want to apply a pattern Block, select:<strong> <br /> </strong> </span><ul><li><span style="color: rgb(51,51,51);"> <strong>Tools</strong> &gt; <strong>Apply Rollup Pattern</strong>, if you want to apply a pattern Block for the selected Block or Instance Specification.</span></li><li><span style="color: rgb(51,51,51);"> <strong>Tools</strong> &gt; <strong>Remove Rollup Pattern</strong>, if you want to remove the pattern Block from the selected Block or Instance Specification.</span></li></ul></li></ol><h3><span style="color: rgb(51,51,51);">The Rollup Pattern Wizard areas<br /> </span></h3><p><span style="color: rgb(51,51,51);">The <strong>Rollup Pattern Wizard </strong>consists of two areas:</span></p><ul><li><span style="color: rgb(51,51,51);">Select/Remove Pattern Block (1).</span></li><li><span style="color: rgb(51,51,51);">Options (2).<br /></span></li></ul><p><ac:image ac:align="center" ac:title="Rollup Pattern Wizard" ac:alt="Rollup Pattern Wizard"><ri:attachment ri:filename="rollup_pattern_wizard.png"><ri:page ri:content-title="Rollup Pattern Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Rollup Pattern Wizard when trying to apply a rollup pattern for a Block. Two areas of the wizard are highlighted: 1- Select Pattern Block, 2 -Options.</h6><p>The procedures below describe how to work with the <span style="color: rgb(51,51,51);"><strong>Rollup Pattern Wizard:</strong></span></p><ul><li><span style="color: rgb(51,51,51);"><ac:link ac:anchor="select_block"><ac:plain-text-link-body><![CDATA[Select/remove the pattern Block.]]></ac:plain-text-link-body><ri:page ri:content-title="Rollup Pattern Wizard" ri:space-key="SYSMLP2024xR3" /></ac:link></span></li><li><span style="color: rgb(51,51,51);"><ac:link ac:anchor="select_options"><ac:plain-text-link-body><![CDATA[Select the options.]]></ac:plain-text-link-body><ri:page ri:content-title="Rollup Pattern Wizard" ri:space-key="SYSMLP2024xR3" /></ac:link><br /></span></li></ul><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="ef1cbc24-9a57-439f-9516-5bd1fa748e32"><ac:parameter ac:name="">select_block</ac:parameter></ac:structured-macro>Selecting/ removing the pattern Block</h3><p>To select/remove the pattern Block</p><hr /><ol><li>Click <ac:image><ri:attachment ri:filename="alt_down.png"><ri:page ri:content-title="_buttons" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> to expand the list of available pattern Blocks.</li><li><p>Choose the rollup pattern Block that you want to apply/ remove.</p></li></ol><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="ea61161c-2dc4-495e-84b7-fe5a9797a258"><ac:parameter ac:name="">select_options</ac:parameter></ac:structured-macro>Selecting the options</h3><table class="relative-table wrapped" style="width: 68.2035%;"><colgroup><col style="width: 30.2917%;" /><col style="width: 41.7036%;" /><col style="width: 27.9658%;" /></colgroup><tbody><tr><th>Apply Rollup Pattern Box</th><th>Description</th><th colspan="1">Option appears when applying rollup pattern for...</th></tr><tr><td><span style="color: rgb(51,51,51);">Apply Recursively</span></td><td><span style="color: rgb(51,51,51);">Applies the pattern Block recursively.</span></td><td colspan="1">Block, Instance Specification</td></tr><tr><td><span style="color: rgb(51,51,51);">Set Role Name</span></td><td><span style="color: rgb(51,51,51);">Sets the role names of Part Properties. <br /></span></td><td colspan="1">Block</td></tr><tr><td><span style="color: rgb(51,51,51);">Set Subsetted Properties</span></td><td><span style="color: rgb(51,51,51);">Sets the Subsetted Properties of the Part Properties.<br /></span></td><td colspan="1">Block</td></tr><tr><td><span style="color: rgb(51,51,51);">Create Value Properties and Redefine</span></td><td><span style="color: rgb(51,51,51);">Creates and redefines Value Properties.</span></td><td colspan="1">Block</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><table class="relative-table wrapped"><colgroup><col style="width: 244.0px;" /><col style="width: 372.0px;" /><col style="width: 229.0px;" /></colgroup><tbody><tr><th>Remove Rollup Pattern Box</th><th>Description</th><th colspan="1">Option appears when applying rollup pattern for...</th></tr><tr><td><span style="color: rgb(51,51,51);">Recursively Remove Rollup Pattern<br /></span></td><td><span style="color: rgb(51,51,51);">Removes the pattern Block recursively.</span></td><td colspan="1">Block, Instance Specification</td></tr><tr><td><span style="color: rgb(51,51,51);">Remove Role Name<br /></span></td><td><span style="color: rgb(51,51,51);">Removes the role names of Part Properties.<br style="color: rgb(51,51,51);" /></span></td><td colspan="1">Block</td></tr><tr><td><span style="color: rgb(51,51,51);">Remove Subsetted Properties</span></td><td><span style="color: rgb(51,51,51);">Removes the Subsetted Properties of the Part Properties.<br style="color: rgb(51,51,51);" /></span></td><td colspan="1">Block</td></tr><tr><td><span style="color: rgb(51,51,51);">Remove Value Properties</span></td><td><span style="color: rgb(51,51,51);">Removes Value Properties.<span style="color: rgb(51,51,51);"><br style="color: rgb(51,51,51);" /></span></span></td><td colspan="1">Block</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="00ac4333-ef61-44d1-9955-9e7061bc3db5"><ac:parameter ac:name="id">1348219184</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e5e2cbdd-9557-402b-b043-7ffe8c3e28bc" /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><strong>Webinar</strong></p><ul><li><a href="http://www.nomagic.com/mbse/events/webinars/item/webinar-7-2016-total-mass-cost-and-power-rollups.html">Total Mass, Cost, and Power Rollups</a></li></ul><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227160291 space=SYSMLP2024xR3 version=1 -->
## PAGE 00307: Sample models

- page_id: `227160291`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160291/Sample+models
- version_number: 1
- version_date: `2024-01-29T09:11:41.801+01:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models
- labels: []

### NORMALIZED CONTENT

1552880298

1552880298

1552880298

Below, a list of example cases are provided to show the usability of the Modelica/Simulink export plugin for SysML modeling and simulation of physical interactions signal flows. Each example contains a brief description of the example as well as capabilities of the plugin that the example attempts to display.

1. Humidifier System Example: Humidifying a Room
  1. The purpose of this example is to show how a SysML model of a humidifier system, one that is trying to control the humidity in a room, can be created with state machines and signal flows. It is important to note that the signal flows between system components are unidirectional, and physical conservation laws do not apply in these applications because the same signal can be sent to multiple receiving components. In some cases, the state machines determine a timing or event trigger for when a signal flows between components. [ATTACHMENT filename='humidifier_scheme.png']
  2. Capabilities: Modeling & simulation of signal flows; exports SysML state machine diagrams into state machines in Simulink’s Stateflow environment.
2. Circuit Example: Voltage Source, Resistors, Inductor, Capacitor
  1. The purpose of this example is to show how a simple SysML model involving the flow of electric charge (current) from a voltage source to resistors, an inductor, and a capacitor can be exported into Modelica or Simulink/Simscape using the SysML extension plugin for signal flow and physical interaction. Though the documentation should lead to generating Modelica and Simulink/Simscape files from the SysML model, the already exported Modelica and Simulink/Simscape files are provided in the package as examples. [ATTACHMENT filename='electric_circuit_scheme.png']
  2. Capabilities: Modeling & simulation of physical interactions; exports the SysML plugin's properties into flow and effort variables for Simulink’s Simscape toolbox (electrical domain).
3. Signal Processor Example: From Source to Sink
  1. The purpose of this example is to show a SysML model of a signal processor, where a signal is sent from a function generator to be conditioned by an amplifier, frequency filters, and a mixer. [ATTACHMENT filename='signal_processor_scheme.png'] This example portrays the signal flows between system components. The signal flow is unidirectional, and physical conservation laws do not apply in these applications because the same signal can be sent to multiple receiving components. In this model, the function generator is being amplified and then sent to parallel filters (one high-pass filter and one low-pass filter), until the mixer combines the filtered signals for the final 
signal processor output.
  2. Capabilities: Modeling & simulation of signal flows.
4. Hydraulics Example: Two Tanks & A Pipe
  1. The purpose of this example is to show how a simple SysML model involving the flow of a fluid between two tanks can be exported into Modelica or Simulink/Simscape using the SysML extension plugin for signal flow and physical interaction. Though the documentation should lead to generating Modelica and Simulink/Simscape files from the SysML model, the already-exported Modelica and Simulink/Simscape files are provided in the package as examples. 
[IMAGE alt='' src='']
  2. Capabilities: Modeling & simulation of physical interactions; exports the SysML plugins properties into flow and effort variables for Simulink’s Simscape toolbox (mechanical domain).

1552987985

**Related pages:**

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="08857c31-8abe-4473-859e-65dc132ffc22"><ac:parameter ac:name="id">1552880298</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="35d7210c-e5de-4969-afee-2300c4cd8975"><ac:parameter ac:name="id">1552880298</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1ac5feb0-3cd0-40e9-9944-5d0620a87196"><ac:parameter ac:name="id">1552880298</ac:parameter><ac:rich-text-body><p>B<ac:inline-comment-marker ac:ref="2454b8f8-4653-4fe1-bca2-b0205e163de3">elow,</ac:inline-comment-marker> a list of example cases are provided to show the usability of the <ac:inline-comment-marker ac:ref="2ed2876d-4d96-4aaf-81cb-2f2ddf9ccc7f">Modelica/Simulink export plugin</ac:inline-comment-marker> for SysML modeling and simulation of physical interactions signal flows. Each example contains a brief description of the example as well as capabilities of the plugin that the example attempts to display.</p><ol><li><strong>Humidifier System Example: Humidifying a Room</strong><strong><br /></strong><ol><li>The purpose of this example is to show how a SysML model of a humidifier system, one that is trying to control the humidity in a room, can be created with state machines and signal flows. It is important to note that the signal flows between system components are unidirectional, and physical conservation laws do not apply in these applications because the same signal can be sent to multiple receiving components. In some cases, the state machines determine a timing or event trigger for when a signal flows between components. <br /><ac:image ac:align="center" ac:thumbnail="true" ac:height="150"><ri:attachment ri:filename="humidifier_scheme.png"><ri:page ri:content-title="Sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Capabilities: Modeling &amp; simulation of signal flows; exports SysML state machine diagrams into state machines in Simulink’s Stateflow environment. </li></ol></li><li><strong>Circuit Example: Voltage Source, Resistors, Inductor, Capacitor</strong><ol><li>The purpose of this example is to show how a simple SysML model involving the flow of electric charge (current) from a voltage source to resistors, an inductor, and a capacitor can be exported into Modelica or Simulink/Simscape using the SysML extension plugin for signal flow and physical interaction. Though the documentation should lead to generating Modelica and Simulink/Simscape files from the SysML model, the already exported Modelica and Simulink/Simscape files are provided in the package as examples.<strong><br /></strong><br /><ac:image ac:align="center" ac:thumbnail="true" ac:height="150"><ri:attachment ri:filename="electric_circuit_scheme.png"><ri:page ri:content-title="Sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Capabilities: Modeling &amp; simulation of physical interactions; exports the SysML plugin's properties into flow and effort variables for Simulink’s Simscape toolbox (electrical domain). </li></ol></li><li><strong>Signal Processor Example: From Source to Sink</strong><ol><li>The purpose of this example is to show a SysML model of a signal processor, where a signal is sent from a function generator to be conditioned by an amplifier, frequency filters, and a mixer. <strong><br /></strong><ac:image ac:align="center" ac:height="150"><ri:attachment ri:filename="signal_processor_scheme.png"><ri:page ri:content-title="Sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><p>This example portrays the signal flows between system components. The signal flow is unidirectional, and physical conservation laws do not apply in these applications because the same signal can be sent to multiple receiving components. In this model, the function generator is being amplified and then sent to parallel filters (one high-pass filter and one low-pass filter), until the mixer combines the filtered signals for the final<br />signal processor output.</p></li><li><p>Capabilities: Modeling &amp; simulation of signal flows.</p></li></ol></li><li><strong>Hydraulics Example: Two Tanks &amp; A Pipe</strong><ol><li><p>The purpose of this example is to show how a simple SysML model involving the flow of a fluid between two tanks can be exported into Modelica or Simulink/Simscape using the SysML extension plugin for signal flow and physical interaction. Though the documentation should lead to generating Modelica and Simulink/Simscape files from the SysML model, the already-exported Modelica and Simulink/Simscape files are provided in the package as examples.<br /><ac:image ac:align="center" ac:height="150"><ri:attachment ri:filename="hydraulics_scheme.png"><ri:page ri:content-title="Sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></li><li><p>Capabilities: Modeling &amp; simulation of physical interactions; exports the SysML plugins properties into flow and effort variables for Simulink’s Simscape toolbox (mechanical domain).</p></li></ol></li></ol><p /></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e0ca7214-69af-474d-bef3-bd9f8a32e610"><ac:parameter ac:name="id">1552987985</ac:parameter><ac:rich-text-body><p><strong>Related pages:</strong></p><p><strong><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="065f6bcd-70d6-4af3-964e-39653a36a029" /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159777 space=SYSMLP2024xR3 version=2 -->
## PAGE 00308: Satisfy

- page_id: `227159777`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159777/Satisfy
- version_number: 2
- version_date: `2025-05-02T10:28:43.812+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Satisfy' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="aed46a20-90b5-43e8-b627-8a25a67183ae"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Satisfy" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227158543 space=SYSMLP2024xR3 version=2 -->
## PAGE 00309: Search Results tab

- page_id: `227158543`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158543/Search+Results+tab
- version_number: 2
- version_date: `2025-05-02T10:28:18.380+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

235353405

235353407

235360251

**On this page**

33

235353406

[CONFLUENCE_PAGE title='Search Results tab' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d5ab215f-9801-44a6-aa03-5878c075a8c3"><ac:parameter ac:name="id">235353405</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b56a4a0b-daa5-4eb3-97d9-168bc387d034"><ac:parameter ac:name="id">235353407</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6778e020-b4ed-45bb-968d-e49a2e412e8d"><ac:parameter ac:name="id">235360251</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="56c8a7b9-ea70-46a7-a439-1eae9915324e"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8c56541d-baf1-4b2e-9c09-ae5e85d93ab4"><ac:parameter ac:name="id">235353406</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="db95c463-1f61-4409-a5f2-f879b8a75770"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Search Results tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158805 space=SYSMLP2024xR3 version=2 -->
## PAGE 00310: Selecting actual Connectors in the Containment tree

- page_id: `227158805`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158805/Selecting+actual+Connectors+in+the+Containment+tree
- version_number: 2
- version_date: `2025-05-02T10:28:23.668+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Connecting Blocks in SysML Internal Block Diagram > Implied Connectors
- labels: []

### NORMALIZED CONTENT

1020859818

1020859820

1020859819

If you want to see an actual Connectors underneath the implied relation without displaying them, you can select them in the Containment tree. How to select actual Connector in Containment tree read the following procedure.

To select actual Connector in the Containment tree

1. Select the implied relation.
2. From its shortcut menu, point to the Underlying Connections command group, and select an appropriate Connector. Actual Connector is selected in the Containment tree.

##### [IMAGE alt='' src='']

###### The Underlying Connectors command group provides a list of actual Connectors which are underneath the implied relation.

1020859817

**Related pages**

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Connecting parts through interface' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Hiding direction arrow on port shape' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Displaying parts and ports' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Autowire Parts' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Property path notation' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Enforce Ports Compatibility mode' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Displaying elements' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Connector' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Proxy Port' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Flow Port' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Full Port' space='SYSMLP2024xR3']

**Sample model**

The sample model used in the figures on this page is the **Implied Connectors**sample model. Download [ATTACHMENT filename='Implied Connectors.mdzip'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f3425fd2-7b4b-4a2e-9b6e-b986dd40a5fc"><ac:parameter ac:name="id">1020859818</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6fdf455f-33f8-4ea2-9110-a5446321f1eb"><ac:parameter ac:name="id">1020859820</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="45e19e77-cef1-4031-b12d-39d62d3f738d"><ac:parameter ac:name="id">1020859819</ac:parameter><ac:rich-text-body><p>If you want to see an actual Connectors underneath the implied relation without displaying them, you can select them in the Containment tree. How to select actual Connector in Containment tree read the following procedure.</p><p>To select actual Connector in the Containment tree</p><hr /><ol><li>Select the implied relation.</li><li>From its shortcut menu, point to the <strong>Underlying Connections</strong> command group, and select an appropriate Connector.<br />Actual Connector is selected in the Containment tree.</li></ol><h3 style="text-align: left;"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><ac:image ac:align="center"><ri:attachment ri:filename="underlying_connectors.png"><ri:page ri:content-title="Selecting actual Connectors in the Containment tree" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></span></h3><h6 style="text-align: center;">The Underlying Connectors command group provides a list of actual Connectors which are underneath the implied relation.</h6><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cdb0ce8a-5aae-4ffa-8129-8704776fb98e"><ac:parameter ac:name="id">1020859817</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li class="with-breadcrumbs"><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Connecting parts through interface" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Hiding direction arrow on port shape" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Displaying parts and ports" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Autowire Parts" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Enforce Ports Compatibility mode" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Displaying elements" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Connector" /></ac:link></li><li><ac:link><ri:page ri:content-title="Proxy Port" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Flow Port" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Full Port" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong>Sample model</strong></p><p class="auto-cursor-target">The sample model used in the figures on this page is the <strong>Implied Connectors </strong>sample model. <span class="confluence-link"><span style="color: rgb(51,51,51);"><span class="confluence-link"><span style="color: rgb(51,51,51);">Download <ac:link><ri:attachment ri:filename="Implied Connectors.mdzip"><ri:page ri:content-title="Implied Connectors" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link>.</span></span></span></span><span style="color: rgb(255,0,0);"><span class="confluence-link"><span style="color: rgb(51,51,51);"><span style="color: rgb(255,0,0);"><br class="confluence-link" /></span></span></span></span></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158551 space=SYSMLP2024xR3 version=1 -->
## PAGE 00311: Selecting perspective

- page_id: `227158551`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158551/Selecting+perspective
- version_number: 1
- version_date: `2024-05-06T14:19:01.133+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

Use perspectives for:

- Selecting a predefined configuration and features according to your software development process role.
- Finding features faster, because there are fewer.
- Choosing a suitable experience mode with a single click.
- Customizing a set of predefined features and configurations based on user needs.

##### Selecting perspective

To select a perspective

1. On the main menu, click Options > Perspectives > Perspectives .
2. In the Select Perspective dialog, select a perspective on the left side of the dialog. **System Engineer**perspective (recommended for SysML) provides a set of features dedicated to system engineers.**MagicGrid**perspective simplifies the modeling tool by providing only the MagicGrid-required subset of SysML elements and diagrams, making it ideal for MagicGrid beginner users.**Full Featured**perspective provides all features available in the modeling tool and installed plugins.
3. (Optional) Select the Expert check box to load all features and commands. Use the Expert mode only if you are an advanced user.
4. Click the Apply button.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(0,0,0);"><span>Use perspectives for:</span></span></p><ul><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);">Selecting a predefined configuration and features according to your software development process role.</span></span></span></span></li><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);"><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);">Finding features faster, because there are fewer.</span></span></span></span></span></span></li><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);">Choosing a suitable experience mode with a single click.</span></span></span></span></li><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);">Customizing a set of predefined features and configurations based on user needs.</span></span></span></span></li></ul><h3>Selecting perspective</h3><p>To select a perspective</p><hr /><ol><li>On the main menu, click <strong>Options </strong>&gt; <strong>Perspectives &gt; Perspectives</strong>.</li><li>In the <strong>Select Perspective</strong> dialog, select a perspective on the left side of the dialog.<br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1ba3ba60-08e4-4472-891a-2d55660c2bcf"><ac:rich-text-body><ul><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);"><strong>System Engineer </strong>perspective (recommended for SysML) provides a set of features dedicated to system engineers.</span></span></span></span></li><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);"><strong>MagicGrid </strong></span></span></span></span>perspective simplifies the modeling tool by providing only the MagicGrid-required subset of SysML elements and diagrams<span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);">, making it ideal for MagicGrid beginner users.</span></span></span></span></li><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(124,133,153);"><span style="color: rgb(0,0,0);"><strong>Full Featured </strong>perspective provides all features available in the modeling tool and installed plugins.</span></span></span></span></li></ul></ac:rich-text-body></ac:structured-macro></li><li>(Optional) Select the <strong>Expert </strong>check box to load all features and commands. Use the Expert mode only if you are an advanced user.</li><li>Click the <strong><span style="color: rgb(0,51,0);"><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">Apply </span></span></span></strong>button.</li></ol><p><ac:image><ri:attachment ri:filename="select_perspective_dialog.png"><ri:page ri:content-title="Selecting perspective" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227158750 space=SYSMLP2024xR3 version=3 -->
## PAGE 00312: Selecting port type

- page_id: `227158750`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158750/Selecting+port+type
- version_number: 3
- version_date: `2025-05-02T10:28:21.939+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Defining interfaces using ports > Creating ports
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Selecting port and part types' space='MD2024xR3']true

You can setthe [CONFLUENCE_PAGE title='Interface Block' space='SYSMLP2024xR3'] as a type of[Proxy Port](https://docs.nomagic.com/display/SYSMLP2024xR3/Proxy+Port) by dragging Interface Block onto [CONFLUENCE_PAGE title='Connector' space='MD2024xR3']. [CONFLUENCE_PAGE title='Connecting parts through interface' space='SYSMLP2024xR3']>]]>

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="032f8f46-e0d5-4c52-a136-241d95dad037"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Selecting port and part types" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f68fc3ba-f0d1-45c9-8b77-45b489afa5ae"><ac:rich-text-body><p>You can set<span style="color: rgb(62,63,64);"> the <ac:link><ri:page ri:content-title="Interface Block" ri:space-key="SYSMLP2024xR3" /></ac:link> as a type of<span> </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Proxy+Port">Proxy Port</a> by dragging Interface Block onto <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Connector" /></ac:link>. <ac:link><ri:page ri:content-title="Connecting parts through interface" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to connect parts through interface >>]]></ac:plain-text-link-body></ac:link></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227158692 space=SYSMLP2024xR3 version=2 -->
## PAGE 00313: Selecting property type

- page_id: `227158692`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158692/Selecting+property+type
- version_number: 2
- version_date: `2025-05-02T10:28:20.948+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Decomposing Blocks
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Selecting port and part types' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="62dea28d-1259-4f37-9221-0d52149eae38"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Selecting port and part types" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159778 space=SYSMLP2024xR3 version=1 -->
## PAGE 00314: Sensor

- page_id: `227159778`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159778/Sensor
- version_number: 1
- version_date: `2016-04-08T08:46:57.276+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

A Sensor is a special external system that forwards information from the environment to the system under development.

#### TIP: Example

Example

- Temperature sensor.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Sensor is a special external system that forwards information from the environment to the system under development.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0ca8ebfb-7889-4c69-b967-731d97966708"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><ul><li>Temperature sensor.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="de9adc89-d387-43d7-a667-124571a795a9"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Use Case Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227160316 space=SYSMLP2024xR3 version=1 -->
## PAGE 00315: Setting initial values

- page_id: `227160316`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160316/Setting+initial+values
- version_number: 1
- version_date: `2020-06-25T06:31:17.829+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Sample models > Creating a simple model
- labels: []

### NORMALIZED CONTENT

The last step of the modeling is to set the value for the resistance in the circuit. This can be done by creating two *InstanceSpecifications*, one for the source and one for the resistor. Values are used for the amplitude of the source, and for the resistance of the resistor respectively. These*InstanceSpecifications* are then set as default values of the circuit source and the circuit resistor (see the image below).

[IMAGE alt='' src='']

###### The *Source* and *Resistor* Instance Specifications with set default values.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The last step of the modeling is to set the value for the resistance in the circuit. This can be done by creating two <em>InstanceSpecifications</em>, one for the source and one for the resistor. Values are used for the amplitude of the source, and for the resistance of the resistor respectively. These<em> InstanceSpecifications</em> are then set as default values of the circuit source and the circuit resistor (see the image below).  </p><p><ac:image ac:align="center" ac:width="400"><ri:attachment ri:filename="initial_value_of_the_resistor.png"><ri:page ri:content-title="Setting initial values" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The <em>Source</em> and <em>Resistor</em> Instance Specifications with set default values.</h6><p />
````

<!--NOMAGIC_PAGE id=227159816 space=SYSMLP2024xR3 version=2 -->
## PAGE 00316: Setting project options

- page_id: `227159816`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159816/Setting+project+options
- version_number: 2
- version_date: `2025-05-02T10:28:45.512+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Setting project options' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="e30cfc31-3f0f-4fd6-b5d2-af9a7631ba2d"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Setting project options" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159134 space=SYSMLP2024xR3 version=2 -->
## PAGE 00317: Showing allocations using SysML Callout notation

- page_id: `227159134`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159134/Showing+allocations+using+SysML+Callout+notation
- version_number: 2
- version_date: `2025-05-02T10:28:31.293+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Functional Allocations
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Allocations

381297791

#### CONTENT-COLUMN: Allocations

381297793

#### CONTENT-BLOCK: Allocations

381297792

You can display allocations in a callout or in a compartment of an element symbol.

[IMAGE alt='' src='']

###### Examples of displaying allocations.

[CONFLUENCE_PAGE title='Note' space='MD2024xR3']true

#### NOTE: Allocations

Allocations

To display allocations, in the **Element Properties**tab, select **Allocated To**and/or **Allocated From** to display.

381297790

**Related pages**

- [CONFLUENCE_PAGE title='SysML Callout Style' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Compartments' space='MD2024xR3']
- [CONFLUENCE_PAGE title='SysML specific compartments' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bc8ad93c-c3da-4fe5-9793-c2d5b5da411f"><ac:parameter ac:name="id">381297791</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ef547430-072b-4148-9dd6-9cf860ea05d3"><ac:parameter ac:name="id">381297793</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="545b6c93-434e-4e70-9a89-8da664140371"><ac:parameter ac:name="id">381297792</ac:parameter><ac:rich-text-body><p>You can display allocations in a callout or in a compartment of an element symbol.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="displaying_allocations_in_callout.png"><ri:page ri:content-title="Showing allocations using SysML Callout notation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Examples of displaying allocations.</h6><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="762c8692-632e-4912-a4cb-3ce9e1efaa50"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Note" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b1afb0eb-49d7-4f8a-8e7a-7b7dff586f6b"><ac:parameter ac:name="title">Allocations</ac:parameter><ac:rich-text-body><p>To display allocations, in the <strong>Element Properties </strong>tab, select <strong>Allocated To </strong>and/or <strong>Allocated From </strong> to display.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4bf3711a-b455-4b2d-8823-0781236d7215"><ac:parameter ac:name="id">381297790</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SysML Callout Style" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Compartments" /></ac:link></li><li><ac:link><ri:page ri:content-title="SysML specific compartments" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159503 space=SYSMLP2024xR3 version=1 -->
## PAGE 00318: Signal incompatible with Proxy Port

- page_id: `227159503`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159503/Signal+incompatible+with+Proxy+Port
- version_number: 1
- version_date: `2022-03-30T10:36:50.141+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Activities
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
<p><strong style="letter-spacing: 0.0px;">Abbreviation</strong></p><p>SignalIncWithProxyPort</p><p><strong>Description</strong></p><p>This validation rule checks if:</p><ul><li>The Send Signal Action uses a compatible Proxy Port in the On Port property to transmit the Signal.</li><li>The Accept Event Action uses a compatible Proxy Port in the Port property to transmit the Signal.</li></ul><p>The validation rule checks each Proxy Port's flow property type, direction, and evaluates isConjugated value to determine if the specified Proxy Port is capable of transmitting the Signal. </p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>SendSignalAction, AcceptEventAction</p><p><strong>Solvers</strong></p><p>To fix this, select the Action with the failed validation, click the warning icon in the <span style="color: rgb(62,63,64);">smart manipulator toolbar</span> and select one of the following:</p><ul><li><strong>Remove '&lt;Port&gt;' Port </strong>- removes the incompatible port from the On Port/Port property.</li><li><strong>Replace '&lt;Port&gt;' Port with Compatible </strong>- removes the incompatible port from the On Port/Port property and provides a list of compatible Proxy Ports for replacing the incompatible port.</li></ul><p><strong>Example</strong></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Send Signal and Accept Event Action On Port and Port property incompatible with Proxy Port.png"><ri:page ri:content-title="Signal incompatible with Proxy Port" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The <em>Sys not Ok</em> Send Signal Action should use Proxy Port <em>out p2</em> instead of <em>in p1</em>. The <em>Stop</em> Accept Event Action should use Proxy Port <em>in p1</em> instead of <em>out p2</em>.</h6>
````

<!--NOMAGIC_PAGE id=227160278 space=SYSMLP2024xR3 version=2 -->
## PAGE 00319: Signal Processor example

- page_id: `227160278`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160278/Signal+Processor+example
- version_number: 2
- version_date: `2025-05-02T10:26:38.264+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Modelica export > Simulating exported Modelica models
- labels: []

### NORMALIZED CONTENT

This page describes how to simulate *Signal Processor* example model in Simulink. [CONFLUENCE_PAGE title='Signal processor sample' space='SYSMLP2024xR3']Learn more about *Signal Processor s*ample model >>

You can find the *Signal Processor*sample model in:

- the modeling tool: Welcome window > Samples > Simulink and Modelica Transformation > SignalProcessor.
- the Installation directory: <modeling tool installation directory>\samples\SysML\Simulink and Modelica Transformation\*Signal Processor**.*

To simulate the *TestBed* model

1. Export the TestBed Block to Modelica file. How to >>
2. Make sure the Dymola tool is installed. How to >>
3. Start the Dymola.
4. Click File > Open > Load... and select saved TestBed.mo file from your file directory. A TestBed model is displayed in the Package Browser . [ATTACHMENT filename='testBed_model_in_package_browser.png']
5. In the Graphics tab toolbar, click [ATTACHMENT filename='check_syntax_button.png'] to check model for syntax and semantic errors. The result panel displays whether the model is ready for simulation. [ATTACHMENT filename='check_syntax_testBed.png']
6. Setup the simulation run for the model: a. Select the Simulation tab and in its toolbar click [ATTACHMENT filename='setup_button.png'] . b. In the Simulation Setup dialog, specify the Start time value to 0 and the Stop time value to 20 seconds (or any other reasonable amount of time, for this model 20 seconds should be enough) . c. Click OK . [ATTACHMENT filename='simulation_setup_testBed.png']
7. In the**Simulation** tab toolbar, click [IMAGE alt='' src='']. When the simulation is completed, the output is displayed in the panel at the bottom and the *TestBed***variables are displayed in the **Variable Browser**.
8. To see the input and output of the SourceToSinkModel , variables from the Variable Browser must be chosen. Selecting SourceToSinkModel > SourceToSink > inputSignal > y will display the input on the plotting window. Selecting SourceToSinkModel > SourceToSink > scopeSignal > output will display the simulation’s output on the plotting window. [ATTACHMENT filename='plot_diagram_testBed.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This page describes how to simulate <em>Signal Processor</em> example model in Simulink. <ac:link><ri:page ri:content-title="Signal processor sample" ri:space-key="SYSMLP2024xR3" /><ac:link-body>Learn more about <em>Signal Processor s</em>ample model &gt;&gt;</ac:link-body></ac:link></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9e487fbf-eae7-49e5-902d-95e217125d96"><ac:rich-text-body><p>You can f<span style="color: rgb(51,51,51);">ind the <em>Signal Processor </em>sample model in:</span></p><ul><li><span style="color: rgb(51,51,51);">the modeling tool: Welcome window &gt; Samples &gt; Simulink and Modelica Transformation &gt; SignalProcessor.</span></li><li><span style="color: rgb(51,51,51);">the Installation directory: </span><em>&lt;modeling tool installation directory&gt;\samples\SysML\Simulink and Modelica Transformation\<em>Signal Processor</em><em>.</em></em></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To simulate the <em>TestBed</em> model</p><hr /><ol><li>Export the <em>TestBed </em>Block to Modelica file. <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Modelica+export#Modelicaexport-ExportingmodeltotheModelicafile" rel="nofollow">How to &gt;&gt;</a></li><li>Make sure the Dymola tool is installed. <a class="external-link" href="https://www.3ds.com/products-services/catia/products/dymola/?woc=%7B%22category%22%3A%5B%22category%2Fdymola%22%5D%7D&amp;wockw=card_content_cta_1_url%3A%22https%3A%2F%2Fblogs.3ds.com%2Fcatia%2F%22" rel="nofollow">How to &gt;&gt;</a></li><li>Start the Dymola.</li><li>Click <strong>File</strong> &gt;<strong> Open </strong>&gt;<strong> Load... </strong>and select saved <em>TestBed.mo</em> file from your file directory. A <em>TestBed </em>model is displayed in the <strong>Package Browser</strong>.<br /><ac:image><ri:attachment ri:filename="testBed_model_in_package_browser.png"><ri:page ri:content-title="Signal Processor example" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>In the <strong>Graphics </strong>tab toolbar, click <ac:image ac:thumbnail="true" ac:height="24"><ri:attachment ri:filename="check_syntax_button.png"><ri:page ri:content-title="_buttons_dymola" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> to check model for syntax and semantic errors. The result panel displays whether the model is ready for simulation.<br /><ac:image><ri:attachment ri:filename="check_syntax_testBed.png"><ri:page ri:content-title="Signal Processor example" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Setup the simulation run for the model:<br />    a. Select the<strong> </strong><strong>Simulation </strong>tab and in its toolbar click <ac:image ac:thumbnail="true" ac:height="21"><ri:attachment ri:filename="setup_button.png"><ri:page ri:content-title="_buttons_dymola" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>.<br />    b. In the <strong>Simulation Setup</strong> dialog, specify the <strong>Start time</strong><strong> </strong>value to <strong>0</strong> and the <strong>Stop time</strong><strong> </strong>value to<strong> 20 </strong>seconds <span style="color: rgb(62,63,64);">(or any other reasonable amount of time, for this model 20 seconds should be enough)</span> .<br />    c. Click <strong>OK</strong>.<br /><ac:image><ri:attachment ri:filename="simulation_setup_testBed.png"><ri:page ri:content-title="Signal Processor example" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">In the<strong> Simulation</strong> tab toolbar, click <ac:image ac:thumbnail="true" ac:height="21"><ri:attachment ri:filename="simulate_button.png"><ri:page ri:content-title="_buttons_dymola" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="deb0b47d-5dd8-46a1-9496-2ea9533e4ef3"><ac:rich-text-body><p>When the simulation is completed, the output is displayed in the panel at the bottom and the <em>TestBed</em><em> </em>variables are displayed in the <strong>Variable Browser</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><span style="color: rgb(62,63,64);">To see the input and output of the </span><strong>SourceToSinkModel</strong><span style="color: rgb(62,63,64);">, variables from the</span><strong> Variable Browser </strong><span style="color: rgb(62,63,64);">must be chosen. Selecting</span><strong> SourceToSinkModel</strong><span style="color: rgb(62,63,64);"> &gt; </span><strong>SourceToSink</strong><span style="color: rgb(62,63,64);"> &gt; </span><strong>inputSignal</strong><span style="color: rgb(62,63,64);"> &gt; </span><strong>y</strong><span style="color: rgb(62,63,64);"> will display the input on the plotting window. Selecting </span><strong>SourceToSinkModel</strong><span style="color: rgb(62,63,64);"> &gt; </span><strong>SourceToSink</strong><span style="color: rgb(62,63,64);"> &gt; </span><strong>scopeSignal </strong><span style="color: rgb(62,63,64);">&gt;</span><strong> output</strong><span style="color: rgb(62,63,64);"> will display the simulation’s output on the plotting window.</span><br /><ac:image><ri:attachment ri:filename="plot_diagram_testBed.png"><ri:page ri:content-title="Signal Processor example" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ol><p><span style="color: rgb(255,0,0);"> </span></p><p><span style="color: rgb(255,0,0);"> </span></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227160138 space=SYSMLP2024xR3 version=1 -->
## PAGE 00320: Signal Processor example to Simulink model

- page_id: `227160138`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160138/Signal+Processor+example+to+Simulink+model
- version_number: 1
- version_date: `2025-03-05T13:22:18.776+01:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Simulink export > Simulating exported Simulink models
- labels: []

### NORMALIZED CONTENT

To generate a Simulink model directly from the modeling tool

1. Right-click the block **TestBed**and select **Tools**> **Export to Simulink.****[IMAGE alt='' src='']**
2. In the Simulink Export Options dialog, set the options listed below and click **OK**:
  - **Format**: XML (.slx)
  - **S-Function or Simscape**: S-Function version 2 
 
[IMAGE alt='' src='']
3. Launch Matlab with Simulink extension, and open the TestBed.slx file with the help of the Current Folder browser. [IMAGE alt='' src='']
4. In the Current Folder panel, double-click on the file named TestBed.slx . The TestBed model will open up in a new Simulink window. Rearrange the blocks to reflect the signal flow arrowheads. [ATTACHMENT filename='TestBed Simulink Model.png']
5. Open the Library Browser either by clicking the Library Browser icon or by going to Tools > Library Browser . Click Simulink > Sinks and select Scope . [ATTACHMENT filename='Scope selection.png']
6. Drag and drop one Scope block from the Sinks library list into the TestBed Simulink model. Attach a signal line segment from the Scope port onto the signal line that connects the dsp block and the scopeSignalOutput block. Repeat the process of adding a Scope block and attaching it to the signal line that connects the inputSignal block to the dsp block. [ATTACHMENT filename='Scope Linked.png']
7. Go to Modeling > Model Settings:

1. 
  1. In the **Simulation time**section Select **the******Start** Time** as **0**, and the **Stop Time** as **20**.
  2. In the **Solver selection**section, select **Variable-step** as the solver type.
  3. In the **Solver details**section, set the Max step size to 0.01, click Apply , and then click OK . [IMAGE alt='' src='']
2. Go to **Simulation>****Run**. Double-click on the **Scope** blocks to see the simulation results. [IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To generate a Simulink model directly from the modeling tool</p><hr /><ol><li><p>Right-click the block <strong>TestBed </strong><span style="color: rgb(51,51,51);">and select <strong>Tools </strong>&gt; <strong>Export to Simulink.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Export to Simulink.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></strong></p></li><li><p>In the Simulink Export Options dialog, set the options listed below and click <strong>OK</strong>:</p><ul><li><p><strong>Format</strong>: XML (.slx)</p></li><li><p><strong>S-Function or Simscape</strong>: S-Function version 2<br /><br /><ac:image><ri:attachment ri:filename="Simulink Options.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br /></p></li></ul></li><li>Launch Matlab with Simulink extension, and open the <strong>TestBed.slx</strong> file with the help of the Current Folder browser.<br /><br /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image><ri:attachment ri:filename="Search file.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br /></span></li><li>In the <strong>Current Folder</strong> panel, double-click on the file <ac:inline-comment-marker ac:ref="d6c0495a-eee8-46f3-8505-736ce5194583">named </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="d6c0495a-eee8-46f3-8505-736ce5194583">TestBed.s</ac:inline-comment-marker>lx</strong>. The<strong> TestBed</strong> model will open up in a new Simulink window. Rearrange the blocks to reflect the signal flow arrowheads.<br /><br /><ac:image ac:width="1000"><ri:attachment ri:filename="TestBed Simulink Model.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>Open the <strong>Library Browser</strong> either by clicking the Library Browser icon or by going to <strong>Tools</strong> &gt; <strong>Library Browser</strong>. Click <strong>Simulink</strong>&gt; <strong>Sinks </strong>and select <strong>Scope</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Scope selection.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>Drag and drop one <strong>Scope</strong> block from the<strong> Sinks</strong> library list into the<strong> TestBed Simulink</strong> model. Attach a signal line segment from the Scope port onto the signal line that connects the <strong>dsp</strong> block and the<strong> scopeSignalOutput</strong> block. Repeat the process of adding a <strong>Scope</strong> block and attaching it to the signal line that connects the <strong>inputSignal</strong> block to the<strong> dsp</strong> block.<br /><br /><ac:image ac:width="1000"><ri:attachment ri:filename="Scope Linked.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>Go to <strong>Modeling</strong>&gt;<strong>Model Settings:</strong></li></ol><ol><li style="list-style-type: none;"><ol><li><p>In the <strong>Simulation time </strong>section Select <strong><span>the</span></strong><span> </span><strong><span><strong>Start</strong></span> Time</strong> as <strong>0</strong>, and the <strong>Stop Time</strong> as <strong>20</strong>.</p></li><li><p>In the <strong>Solver selection </strong>section, select <strong>Variable-step</strong> as the solver type.</p></li><li><span style="letter-spacing: 0.0px;">In the <strong>Solver details </strong>section, set the </span><strong style="letter-spacing: 0.0px;">Max step size</strong><span style="letter-spacing: 0.0px;"> to </span><strong style="letter-spacing: 0.0px;">0.01, </strong>click <strong style="letter-spacing: 0.0px;">Apply</strong><span style="letter-spacing: 0.0px;">, and then click </span><strong style="letter-spacing: 0.0px;">OK</strong><span style="letter-spacing: 0.0px;">.<br /><br /></span><p><ac:image ac:width="900"><ri:attachment ri:filename="Model Setting.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br /></p></li></ol></li><li><p>Go to <strong>Simulation&gt;</strong><strong>Run</strong>. Double-click on the <strong>Scope</strong> blocks to see the simulation results.</p><p><ac:image><ri:attachment ri:filename="Scope_Output.png"><ri:page ri:content-title="Signal Processor example to Simulink model" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></li></ol>
````

<!--NOMAGIC_PAGE id=227160411 space=SYSMLP2024xR3 version=1 -->
## PAGE 00321: Signal processor sample

- page_id: `227160411`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160411/Signal+processor+sample
- version_number: 1
- version_date: `2020-06-30T03:10:59.741+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Sample models
- labels: []

### NORMALIZED CONTENT

**Setup for exporting into Modelica/Simulink:**

Once the*SignalProcessor.mdzip*file is opened, the model should already be opened to the*TestBed*internal block diagram.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Setup for exporting into Modelica/Simulink:</strong></p><p style="text-align: left;"><span style="letter-spacing: 0.0px;">Once the </span><em style="letter-spacing: 0.0px;">SignalProcessor.mdzip</em><span style="letter-spacing: 0.0px;"> file is opened, the model should already be opened to the </span><em style="letter-spacing: 0.0px;">TestBed</em><span style="letter-spacing: 0.0px;"> internal block diagram.</span></p><p style="text-align: left;"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="testBed_ibd.png"><ri:page ri:content-title="Signal processor sample" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></p><p style="text-align: left;"><span style="letter-spacing: 0.0px;"><br /></span></p><p />
````

<!--NOMAGIC_PAGE id=227160258 space=SYSMLP2024xR3 version=1 -->
## PAGE 00322: Simulating exported Modelica models

- page_id: `227160258`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160258/Simulating+exported+Modelica+models
- version_number: 1
- version_date: `2024-01-29T11:26:43.745+01:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Modelica export
- labels: []

### NORMALIZED CONTENT

Four sample models are prepared to demonstrate the Modelica export usability: *Humidifier*, *Electric Circuit*, *Hydraulics* and *Signal Processor*. [CONFLUENCE_PAGE title='Sample models' space='SYSMLP2024xR3']>]]>

You can find sample models:

- In the modeling tool: Welcome window > Samples > Simulink and Modelica Transformation.
- in the Installation directory: <modeling tool installation directory>\samples\SysML\Simulink and Modelica Transformation.

This section is dedicated to describe how to simulate exported Modelica models by using the [Dymola](https://www.3ds.com/products-services/catia/products/dymola/?woc=%7B%22category%22%3A%5B%22category%2Fdymola%22%5D%7D&wockw=card_content_cta_1_url%3A%22https%3A%2F%2Fblogs.3ds.com%2Fcatia%2F%22) tool. Each Modelica model simulation is described separately:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Four sample models are prepared to demonstrate the Modelica export usability: <em>Humidifier</em>, <em>Electric Circuit</em>, <em>Hydraulics</em> and <em>Signal Processor</em>. <ac:link><ri:page ri:content-title="Sample models" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more about each of sample model >>]]></ac:plain-text-link-body></ac:link></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9ee55c68-36b9-442c-b18a-584bd4b77eba"><ac:rich-text-body><p>You can f<span style="color: rgb(51,51,51);">ind sample models:</span></p><ul><li><span style="color: rgb(51,51,51);">In the modeling tool: Welcome window &gt; Samples &gt; Simulink and Modelica Transformation. </span></li><li><span style="color: rgb(51,51,51);">in the Installation directory: </span><em>&lt;modeling tool installation directory&gt;\samples\SysML\Simulink and Modelica Transformation. </em></li></ul></ac:rich-text-body></ac:structured-macro><p><br />This section is dedicated to describe how to simulate exported Modelica models by using the <a href="https://www.3ds.com/products-services/catia/products/dymola/?woc=%7B%22category%22%3A%5B%22category%2Fdymola%22%5D%7D&amp;wockw=card_content_cta_1_url%3A%22https%3A%2F%2Fblogs.3ds.com%2Fcatia%2F%22">Dymola</a> tool. Each Modelica model simulation is described separately:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="610bbf46-f8a5-4234-93ba-c03f9ce01001" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227160102 space=SYSMLP2024xR3 version=1 -->
## PAGE 00323: Simulating exported Simulink models

- page_id: `227160102`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160102/Simulating+exported+Simulink+models
- version_number: 1
- version_date: `2024-01-29T10:36:20.356+01:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Simulink export
- labels: []

### NORMALIZED CONTENT

Four sample models are prepared to demonstrate the Simulink export usability: *Humidifier*, *Electric Circuit*, *Hydraulics* and *Signal Processor*. [CONFLUENCE_PAGE title='Sample models' space='SYSMLP2024xR3']>]]>

You can find sample models:

- In the modeling tool: Welcome window > Samples > Simulink and Modelica Transformation.
- in the Installation directory: <modeling tool installation directory>\samples\SysML\Simulink and Modelica Transformation.

This section is dedicated to describe how to simulate exported Simulink models. Each Simulink model simulation is described separately:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Four sample models are prepared to demonstrate the Simulink export usability: <em>Humidifier</em>, <em>Electric Circuit</em>, <em>Hydraulics</em> and <em>Signal Processor</em>. <ac:link><ri:page ri:content-title="Sample models" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more about each of sample model >>]]></ac:plain-text-link-body></ac:link></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="9ee55c68-36b9-442c-b18a-584bd4b77eba"><ac:rich-text-body><p>You can f<span style="color: rgb(51,51,51);">ind sample models:</span></p><ul><li><span style="color: rgb(51,51,51);">In the modeling tool: Welcome window &gt; Samples &gt; Simulink and Modelica Transformation. </span></li><li><span style="color: rgb(51,51,51);">in the Installation directory: </span><em>&lt;modeling tool installation directory&gt;\samples\SysML\Simulink and Modelica Transformation. </em></li></ul></ac:rich-text-body></ac:structured-macro><p><br />This section is dedicated to describe how to simulate exported Simulink models. Each Simulink model simulation is described separately:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="72899aac-8333-41ec-adff-c6bd698495bc" /></p>
````

<!--NOMAGIC_PAGE id=227160071 space=SYSMLP2024xR3 version=3 -->
## PAGE 00324: Simulink export

- page_id: `227160071`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160071/Simulink+export
- version_number: 3
- version_date: `2025-05-02T10:28:46.662+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models
- labels: []

### NORMALIZED CONTENT

**On this page**

43

##### Introduction

Information stored in SysML models can be reused in simulations performed by Simulink and existing Simulink models can be brought back into MBSE environment. Most often system engineers model the system down to a point of where executable models start in Simulink. The purpose is to keep these models consistent as the system design evolves.

**Export to Simulink Tool** allows to generate the Simulink model from SysML model. The SLX or MDL file format is created that contains the block diagram and block properties of the simulation. The following figure illustrates the SysML Internal Block Diagram exported to Simulink Block diagram.

[IMAGE alt='' src='']

###### The SysML Internal Block Diagram exported to Simulink Block diagram.

##### Exporting model to the Simulink file

You can export to the Simulink file:

- Block - exports the model (Read the procedure below).
- Instance Specification - exports particular configuration with initial values and subtype instances as specified in the instance model.

To export model to the Simulink file

1. In the Model Browser , select the Block you want to export and do one of the following:
  - In the top-left corner of the modeling tool, click File > Export To > Simulink .
  - Right-click the selected Block and then click Tools > Export to Simulink .
2. Specify export options in the Simulink Export Options dialog. >]]>[CONFLUENCE_PAGE title='Simulink export' space='SYSMLP2024xR3']
3. Click OK . The Simulink (.slx) file is generated and saved to your file directory.

The Simulink export generates several files depending on the model. Make sure these files are present in the MATLAB work folder for model to open correctly.

###### Simulink Export Options

Each time you export your model to the Simulink file, the**Simulink Export Options**dialog opens with already selected options. The detailed descriptions are provided in the following table.

[IMAGE alt='' src='']

| Option | Description |
| --- | --- |
| Format | Select the file format to export:Text (.mdl) - exports to legacy textual formatXML (.slx) - exports to compressed XML-based file format. |
| S-Function or Simscape | Select how to export SysML parametrics:as Simscape - file type dedicated to use in the MATLAB® environment with an extension .ssc. Use ssc_build in Matlab to generate library and blocks from generated Simscape files. If blocks have bidirectional (inout) ports, Simscape should be selected as export option, as Simulink only supports unidirectional inports and outports. as S-Function version 1 - generate all constraints into separate files that contain functions. as S-Function version 2 - generate all constraints into separate files that contain functions. |
| Simscape port libraries | Select whether to create or reuse existing port types. |
| Composite Signals | Select how to export Proxy Port/Interface Block with multiple Flow Properties (composite signals):as bus Creators/Selectors. Bus Creator blocks create buses within a subsystem or model.Bus Selector blocks extract specified elements of the bus.as bus In/Out ports.Out Bus Element blocks create a bus at a subsystem or model interface.In Bus Element blocks extract specified elements of a bus at a subsystem or model interface. |
| Apply <<SimulinkBlock>> on export | Select to automatically apply the <<SimulinkBlock>> stereotype upon the export of the selected Block. Once stereotype is applied, further Part usages of this Block get referenced to the exported Simulink model. Do not select the checkbox if you want to export this target again. For more information refer to . |
|  | Click to specify the location of generated Simulink file or rename the file. |

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4f766749-8eb2-4cc7-8347-930473bd1e2f"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Introduction</h3><p>Information stored in SysML models can be reused in simulations performed by Simulink and existing Simulink models can be brought back into MBSE environment. Most often system engineers model the system down to a point of where executable models start in Simulink. The purpose is to keep these models consistent as the system design evolves.</p><p><strong> Export to Simulink Tool</strong> allows to generate the Simulink model from SysML model. The SLX or MDL file format is created that contains the block diagram and block properties of the simulation. The following figure illustrates the SysML Internal Block Diagram exported to Simulink Block diagram.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="sysml_ibd_to_simulink_block_diagram.png"><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The SysML Internal Block Diagram exported to Simulink Block diagram.</h6><h3>Exporting model to the Simulink file</h3><p>You can export to the Simulink file:</p><ul><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Block">Block </a>- exports the model (Read the procedure below).</li><li><a href="https://docs.nomagic.com/display/MD2024xR3/Instance+Specification">Instance Specification</a> -<span style="color: rgb(62,63,64);"> exports particular configuration with initial values and subtype instances as specified in the instance model. </span></li></ul><p>To export model to the Simulink file</p><hr /><ol><li>In the <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Model+Browser">Model Browser</a>, select the Block you want to export and do one of the following:<ul><li>In the top-left corner of the modeling tool, click <strong>File</strong> &gt;<strong> Export To &gt; Simulink</strong>.</li><li>Right-click the selected Block and then click <strong>Tools</strong> &gt; <strong>Export to Simulink</strong>.</li></ul></li><li>Specify export options in the <strong>Simulink Export Options</strong> dialog. <ac:link ac:anchor="Simulink Export Options"><ac:plain-text-link-body><![CDATA[Option descriptions >>]]></ac:plain-text-link-body><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li>Click <strong>OK</strong>.<br />The Simulink (.slx) file is generated and saved to your file directory.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="59b11b92-f3b5-454b-980e-fcdfe3621b4c"><ac:rich-text-body><p>The Simulink export generates several files depending on the model. Make sure these files are present in the MATLAB work folder for model to open correctly.</p></ac:rich-text-body></ac:structured-macro><h4>Simulink Export Options</h4><p><span style="color: rgb(62,63,64);">Each time you export your model to the Simulink file, the </span><strong>Simulink Export Options</strong><span style="color: rgb(62,63,64);"> dialog opens with already selected options. The detailed descriptions are provided in the following table.</span></p><p><ac:image><ri:attachment ri:filename="simulink_export_options.png"><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p><br /></p><table class="relative-table wrapped" style="width: 76.0285%;"><colgroup><col style="width: 28.231%;" /><col style="width: 71.769%;" /></colgroup><tbody><tr><th>Option</th><th>Description</th></tr><tr><td><strong>Format</strong></td><td><p>Select the file format to export:</p><ul><li>Text (.mdl) - exports to legacy textual format</li><li>XML (.slx) - exports to compressed XML-based file format.</li></ul></td></tr><tr><td><strong>S-Function or Simscape</strong></td><td><p>Select how to export SysML parametrics:</p><ul><li>as Simscape - <span style="color: rgb(64,64,64);">file type dedicated to use in the MATLAB</span><span style="color: rgb(64,64,64);">®</span><span style="color: rgb(64,64,64);"> environment with an extension </span><code class="literal">.ssc</code><span style="color: rgb(64,64,64);">. </span>Use <span style="color: rgb(64,64,64);">ssc_build in Matlab to generate library and blocks from generated Simscape files. </span>If blocks have bidirectional (inout) ports, Simscape should be selected as export option, as Simulink only supports unidirectional inports and outports. </li><li><span>as S-Function version 1 - generate all constraints into separate files that contain functions. </span></li><li><span>as S-Function version 2 - generate all constraints into separate files that contain functions.</span><span><br /></span></li></ul></td></tr><tr><td><strong>Simscape port libraries</strong></td><td>Select whether to create or reuse existing port types.</td></tr><tr><td><strong>Composite Signals</strong></td><td><div class="content-wrapper"><p>Select how to export <span>Proxy Port/Interface Block with multiple Flow Properties (composite signals)</span>:</p><ul><li>as bus Creators/Selectors. <br /><span class="block">Bus Creator</span><span style="color: rgb(64,64,64);"> blocks create buses within a subsystem or model.</span><br /><span style="color: rgb(64,64,64);"><ac:image><ri:attachment ri:filename="bus_creator.png"><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span><span class="block">Bus Selector</span><span style="color: rgb(64,64,64);"> blocks extract specified elements of the bus.<br /><br /><ac:image ac:thumbnail="true" ac:height="47"><ri:attachment ri:filename="bus_selector.png"><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></li><li>as bus In/Out ports.<br /><span class="block">Out Bus Element</span><span style="color: rgb(64,64,64);"> blocks create a bus at a subsystem or model interface.<br /><ac:image ac:thumbnail="true" ac:height="86"><ri:attachment ri:filename="bus_out.png"><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span><span class="block">In Bus Element</span><span style="color: rgb(64,64,64);"> blocks extract specified elements of a bus at a subsystem or model interface.<br /><br /><ac:image ac:thumbnail="true" ac:height="73"><ri:attachment ri:filename="bus_in.png"><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></li></ul></div></td></tr><tr><td colspan="1"><strong>Apply &lt;&lt;SimulinkBlock&gt;&gt; on export</strong></td><td colspan="1"><div class="content-wrapper" title=""><p>Select to automatically apply the &lt;&lt;SimulinkBlock&gt;&gt; stereotype upon the export of the selected Block. <span style="letter-spacing: 0.0px;">Once stereotype is applied, further Part usages of this Block get referenced to the exported Simulink model. Do not select the checkbox if you want to export this target again. For more information refer to </span><ac:link><ri:page ri:content-title="Reusing and referencing Simulink models" ri:space-key="SYSMLP2024xR3" /></ac:link><span style="letter-spacing: 0.0px;">.</span></p></div></td></tr><tr><td colspan="1"><div class="content-wrapper"><p><ac:image ac:thumbnail="true" ac:height="19"><ri:attachment ri:filename="select_file.png"><ri:page ri:content-title="Simulink export" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></div></td><td colspan="1"><span style="color: rgb(62,63,64);">Click to specify the location of generated Simulink file or rename the file. </span></td></tr></tbody></table></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="9568182e-87a3-4783-83d5-09ee9635e5c2" /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159824 space=SYSMLP2024xR3 version=5 -->
## PAGE 00325: Simulink import

- page_id: `227159824`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159824/Simulink+import
- version_number: 5
- version_date: `2026-01-13T07:35:39.140+01:00`
- ancestors: SysML Plugin Documentation > Importing External Simulation Models
- labels: []

### NORMALIZED CONTENT

##### **What is Simulink?**

Simulink is a MATLAB-based graphical environment that allows modeling, simulating, and analyzing dynamic systems. It enables users to simulate the dynamic behavior of the modeled system; for example, it is now widely used in automatic control and digital signal processing for multi-domain simulation.

##### **Simulink file import**

The modeling tools support the **SLX** file format, meaning that you must have your Simulink model in this format to import it. Following the Simulink file import, the **Simulink Import Options** dialog opens. It allows customizing the Simulink model import options. For example, you can specify whether the parameters from the model should be imported as ports or value properties, set the name for the Simulink Block (the Simulink file name is used by default), and select the checkbox to attach the file to the model upon import automatically.

To import the Simulink file into the model

1. In the top-left corner of the modeling tool, click **File** >**Import From**> **Simulink File**. [IMAGE alt='' src='']
2. Select the Simulink (.slx) file on your file system and click **Open**. [IMAGE alt='' src='']
3. In the **Simulink Import Options** dialog, specify which properties from the Simulink file should be imported into your model as values and ports. Click **OK**. [IMAGE alt='' src='']

###### Dragging and Dropping a Simulink file on a diagram

You can import the Simulink model by dragging and dropping the Simulink file directly onto the Block Definition (BDD), Internal Block (IBD), and SysML Activity diagrams:

To import the Simulink model

1. Locate the SLX file on your file system.
2. Do one of the following:
  - Drag and drop the file from your file system onto the [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space=''] . A [CONFLUENCE_PAGE title='Block' space=''] with the applied «SimulinkBlock» stereotype is created in the model after customizing Simulink import via the Simulink Import Options dialog. [ATTACHMENT filename='importing_simulink_file_to_bdd.png']
  - Drag and drop the file from your file system onto the [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space=''] . A [CONFLUENCE_PAGE title='Part Property' space=''] is created in the model after customizing Simulink import via the Simulink Import Options dialog. [ATTACHMENT filename='importing_simulink_to_ibd.png']
  - Drag and drop the file from your file system onto the [CONFLUENCE_PAGE title='SysML Activity Diagram' space='']. The Activity (stereotyped by«SimulinkBlock»), which is assigned as behavior for a [CONFLUENCE_PAGE title='Call Behavior Action' space='MD2024xR3'], and its Input and/or Output [CONFLUENCE_PAGE title='Pin' space='MD2024xR3'] arecreated in the model. The **Simulink Import Options** dialog does not open in this case. [IMAGE alt='' src='']

The **Simulink Import Options dialog** opens immediately after dropping the file. Specify the Simulink import options and click **OK**when you are done.

The **Simulink Import Options** dialog has the following options:

| Option name | Description |
| --- | --- |
| Direction | The direction of the port: In or Out. Inputs and Outputs are selected to be imported as ports by default. |
| Name | The name of the property/parameter. |
| Type | The type of the property, for example, a value property. |
| Description | The textual description of the property. |
| As Port | Click to select whether properties should be represented as Flow or Proxy ports. Select None to import the selected properties as value properties. |
| Interface Block | Click to select a compatible interface Block or create a new one. <NEW> is selected by default.The Interface Block column is active only if Proxy Port is selected in the As Port column. |
| Redefine | Click to redefine inherited value or part properties. |
|  | Click to select all listed properties at once. |
|  | Click to deselect all listed properties at once. |
|  | If the checkbox next to Attach file to the project is selected, the imported Simulink file is automatically attached to the model. |
|  | The name of the element created in the model upon import. By default, the name of the Simulink file is used, but you can set the one you like. |

###### Dragging and dropping a Simulink file on an existing Block

You can drag and drop the external Simulink model directly onto the existing element in your model. Once the .slx file is dropped, the **Simulink Import Options** dialog opens. You can then redefine value and part properties.

In this case, a new Block is created as a subtype of the existing Block together with the[Generalization](https://docs.nomagic.com/display/MD190SP3/Generalization)relationship.

[IMAGE alt='' src='']

###### Dropping the Simulink file on the existing Block.

**In/Out properties**in the**Simulink****Import Options**dialog are, by default, imported into the model as ports of a Flow type.

###### ****

###### Updating existing Simulink Block

An existing Simulink Block can be updated by dragging and dropping the .slx file directly on it. This is useful in those cases when there is a need to update the Block, for example, to import properties that were left out at first or update the model with the latest version of the Simulink file.

To update a Simulink Block

1. Locate the SLX file on your file system.
2. Drag and drop it on the shape of your Simulink Block.
3. In the opened Simulink Import Options dialog, select the properties to update the Simulink Block with.
4. Click OK .

**[IMAGE alt='' src='']**

###### Dragging and dropping the Simulink file on the existing Simulink Block.

Alternatively, you can update the Simulink Block directly from the shortcut menu.

To update a Simulink Block

1. Right-click the Simulink Block.
2. Select Tools > Update from Simulink file from the shortcut menu. [ATTACHMENT filename='update_from_simulink_file.png']
3. In the opened Simulink Import Options dialog, select the properties to update the Simulink Block with. [ATTACHMENT filename='updating_simulink_file.png']
4. Click OK .

Already imported properties are grayed out and cannot be edited in the **Simulink Import Options**dialog.

If the **Attach file to the project** is checked in the **Simulink Import Options dialog**, a previous version of the attached file is replaced with a new one upon import.

##### **Co-simulation**

The Simulink model can be simulated using the [CONFLUENCE_PAGE title='Cameo Simulation Toolkit Documentation' space='CST2024xR3'] (CST). To learn more, please click [CONFLUENCE_PAGE title='Simulation of SysML models' space='CST2024xR3'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3><strong>What is Simulink?</strong></h3><p>Simulink is a MATLAB-based graphical environment that allows modeling, simulating, and analyzing dynamic systems. It enables users to simulate the dynamic behavior of the modeled system; for example, it is now widely used in automatic control and digital signal processing for multi-domain simulation. </p><h3><strong>Simulink file import</strong></h3><p>The modeling tools support the <strong>SLX</strong> file format, meaning that you must have your Simulink model in this format to import it. Following the Simulink file import, the <strong>Simulink Import Options</strong> dialog opens. It allows customizing the Simulink model import options. For example, you can specify whether the parameters from the model should be imported as ports or value properties, set the name for the Simulink Block (the Simulink file name is used by default), and select the checkbox to attach the file to the model upon import automatically. </p><p><br /></p><p><span style="color:var(--ds-text,#333333);">To import the Simulink file into the model</span></p><hr /><ol><li data-uuid="f33e7811-acbe-4dd3-bd46-8488e1edc8da"><span style="color:var(--ds-text,#333333);">In the top-left corner of the modeling tool, click <strong>File</strong> &gt;<strong> Import From </strong>&gt; <strong>Simulink File</strong>.<br /><br class="_mce_tagged_br" /></span><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="simulink_import_from_file_menu.png" /></ac:image><br /><br /></span></li><li data-uuid="62bcc8ef-4887-4973-ba98-2313e194a74d"><span style="color:var(--ds-text,#333333);">Select the Simulink (.slx) file on your file system and click <strong>Open</strong>.<br /><br /></span><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="simulink_import_selection_from_file_system.png" /></ac:image><br /><br /></span></li><li data-uuid="68c6c895-0cad-4f8a-b716-b180be5e3c44"><span style="color:var(--ds-text,#333333);">In the <strong>Simulink Import Options</strong> dialog, specify which properties from the Simulink file should be imported into your model as values and ports. Click <strong>OK</strong>.<br /><br /></span><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="specifying_simulink_import_properties.png" /></ac:image><br /></span></li></ol><p><br /></p><h4>Dragging and Dropping a Simulink file on a diagram</h4><p>You can import the Simulink model by dragging and dropping the Simulink file directly onto the Block Definition (BDD), Internal Block (IBD), and SysML Activity diagrams:</p><p><br /></p><p>To import the Simulink model</p><hr /><ol><li data-uuid="197091b4-8e78-4f6c-9c8f-cf0216b5f9fc">Locate the <strong>SLX</strong> file on your file system.</li><li data-uuid="321b80fc-4d2f-4ff8-b014-8ba4a64f9668">Do one of the following:<ul><li>Drag and drop the file from your file system onto the <ac:link><ri:page ri:content-title="SysML Block Definition Diagram" /><ac:plain-text-link-body><![CDATA[BDD diagram]]></ac:plain-text-link-body></ac:link>. A <ac:link><ri:page ri:content-title="Block" /><ac:plain-text-link-body><![CDATA[Block ]]></ac:plain-text-link-body></ac:link>with the applied «SimulinkBlock» stereotype is created in the model after customizing Simulink import via the <strong>Simulink Import Options</strong> dialog.<br /><ac:image><ri:attachment ri:filename="importing_simulink_file_to_bdd.png" /></ac:image></li><li>Drag and drop the file from your file system onto the <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" /><ac:plain-text-link-body><![CDATA[IBD diagram]]></ac:plain-text-link-body></ac:link>. A <ac:link><ri:page ri:content-title="Part Property" /><ac:plain-text-link-body><![CDATA[Part property]]></ac:plain-text-link-body></ac:link> is created in the model after customizing Simulink import via the <strong>Simulink Import Options</strong> dialog.<br /><ac:image><ri:attachment ri:filename="importing_simulink_to_ibd.png" /></ac:image></li><li><p class="auto-cursor-target">Drag and drop the file from your file system onto the <ac:link><ri:page ri:content-title="SysML Activity Diagram" /><ac:plain-text-link-body><![CDATA[SysML Activity diagram]]></ac:plain-text-link-body></ac:link>. The <span style="color:var(--ds-text,#333333);">Activity (stereotyped by </span><span style="color:var(--ds-text,#333333);">«</span><span style="color:var(--ds-text,#333333);">SimulinkBlock</span><span style="color:var(--ds-text,#333333);">»</span><span style="color:var(--ds-text,#333333);">), which is assigned as behavior for a</span> <span style="color:var(--ds-text,#333333);"><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Call Behavior Action" /></ac:link>,</span> <span style="color:var(--ds-text,#333333);">and its Input and/or Output <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Pin" /><ac:plain-text-link-body><![CDATA[Pins]]></ac:plain-text-link-body></ac:link> are </span>created in the model.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8e5fd31d-a590-4da2-8c1a-c87e72845124"><ac:rich-text-body><p>The <strong>Simulink Import Options</strong> dialog does not open in this case.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="simulink_import_activity_diagram.png" /></ac:image><br /><br /></p></li></ul></li></ol><p>The <strong>Simulink Import Options dialog</strong> opens immediately after dropping the file. Specify the Simulink import options and click <strong>OK </strong>when you are done.</p><p><br /></p><p>The <strong>Simulink Import Options</strong> dialog has the following options:</p><table class="relative-table wrapped" style="width: 63.4034%;"><colgroup class=""><col class="" style="width: 17.7994%;" /><col class="" style="width: 82.2006%;" /></colgroup><thead class=""><tr class=""><th><p>Option name</p></th><th><p>Description</p></th></tr></thead><tbody class=""><tr class=""><td><strong>Direction</strong></td><td>The direction of the port: <em>In</em> or <em>Out</em>. <em>Inputs</em> and <em>Outputs </em>are selected to be imported as ports by default.</td></tr><tr class=""><td><strong>Name</strong></td><td>The name of the property/parameter.</td></tr><tr class=""><td colspan="1"><strong>Type</strong></td><td colspan="1">The type of the property, for example, a value property.</td></tr><tr class=""><td colspan="1"><strong>Description</strong></td><td colspan="1">The textual description of the property.</td></tr><tr class=""><td colspan="1"><strong>As Port</strong></td><td colspan="1"><span style="color:var(--ds-text,#333333);">Click to select whether properties should be represented as Flow or Proxy ports. Select None to import the selected properties as value properties.</span></td></tr><tr class=""><td colspan="1"><strong>Interface Block</strong></td><td colspan="1"><div class="content-wrapper"><p>Click to select a compatible interface Block or create a new one. &lt;NEW&gt; is selected by default.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1c073e21-d029-4cbd-89d8-adb70a16cb5b"><ac:rich-text-body>The Interface Block column is active only if <strong>Proxy Port</strong> is selected in the <strong>As Port</strong> column.</ac:rich-text-body></ac:structured-macro></div></td></tr><tr class=""><td colspan="1"><strong>Redefine</strong></td><td colspan="1">Click to redefine inherited value or part properties.</td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="25"><ri:attachment ri:filename="select_all.png" /></ac:image></span></p></div></td><td colspan="1">Click to select all listed properties at once.</td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="24"><ri:attachment ri:filename="select_none.png" /></ac:image></span></p></div></td><td colspan="1">Click to deselect all listed properties at once.</td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="25"><ri:attachment ri:filename="attach_file_to_the_project.png" /></ac:image></span></p></div></td><td colspan="1">If the checkbox next to <strong>Attach file to the project</strong> is selected, the imported Simulink file is automatically attached to the model.</td></tr><tr class=""><td colspan="1"><div class="content-wrapper"><p><span class="confluence-embedded-file-wrapper"><ac:image><ri:attachment ri:filename="block_name.png" /></ac:image></span></p></div></td><td colspan="1">The name of the element created in the model upon import. By default, the name of the Simulink file is used, but you can set the one you like.</td></tr></tbody></table><h4><br />Dragging and dropping a Simulink file on an existing Block</h4><p>You can drag and drop the external Simulink model directly onto the existing element in your model. Once the .slx file is dropped, the <strong>Simulink Import Options</strong> dialog opens. You can then redefine value and part properties.</p><p><span style="color:var(--ds-text,#333333);">In this case, a new Block is created as a subtype of the existing Block together with the </span><a href="https://docs.nomagic.com/display/MD190SP3/Generalization">Generalization</a><span style="color:var(--ds-text,#333333);"> relationship. </span></p><p style="text-align: center;"><span style="color:var(--ds-background-accent-gray-bolder,#626f86);"><ac:image><ri:attachment ri:filename="dropping_simulink_file_on_existing_block.png" /></ac:image><br /></span></p><h6 style="text-align: center;"><span style="color:var(--ds-background-accent-gray-bolder,#626f86);">Dropping the Simulink file on the existing Block.</span></h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0acba68b-c194-488a-b53b-1549c1ce5503"><ac:rich-text-body><p><strong>In/Out properties</strong><span style="color:var(--ds-text,#333333);"> in the<strong> Simulink</strong></span><strong> Import Options</strong><span style="color:var(--ds-text,#333333);"> dialog are, by default, imported into the model as ports of a Flow type.</span></p></ac:rich-text-body></ac:structured-macro><h4><strong> </strong></h4><h4>Updating existing Simulink Block</h4><p>An existing Simulink Block can be updated by dragging and dropping the .slx file directly on it. This is useful in those cases when there is a need to update the Block, for example, to import properties that were left out at first or update the model with the latest version of the Simulink file.</p><p><br /></p><p>To update a Simulink Block</p><hr /><ol><li data-uuid="b76d46e5-42e5-4aa5-b217-9fa73d6c9e6c">Locate the <strong>SLX</strong> file on your file system.</li><li data-uuid="53d823b5-1d48-4ff6-9e02-cfa74c5a182a">Drag and drop it on the shape of your Simulink Block.</li><li data-uuid="7fd9ee9d-c15f-48b8-ba14-d9c0150d680f">In the opened <strong>Simulink Import Options</strong> dialog, select the properties to update the Simulink Block with.</li><li data-uuid="571bd4dc-8954-463c-8308-cb75c8dbe3a2">Click <strong>OK</strong>.</li></ol><p><strong><ac:image ac:align="center" ac:height="228"><ri:attachment ri:filename="updating_simulink_block_.png" /></ac:image><br /></strong></p><h6 style="text-align: center;">Dragging and dropping the Simulink file on the existing Simulink Block.</h6><p>Alternatively, you can update the Simulink Block directly from the shortcut menu.</p><p><br /></p><p>To update a Simulink Block</p><hr /><ol><li data-uuid="e6fa9ae9-e5e1-4706-8766-3f12c0d84349">Right-click the Simulink Block. </li><li data-uuid="b44d81db-cd07-4a6a-981d-1a77e4ae0b3a">Select <strong>Tools</strong> &gt;<strong> Update from Simulink</strong> <strong>file </strong>from the shortcut menu.<br /><ac:image><ri:attachment ri:filename="update_from_simulink_file.png" /></ac:image><br /><br /></li><li data-uuid="aa167c7c-3b26-4fc0-b01d-4c69df3b7ff1">In the opened <strong>Simulink Import Options</strong> dialog, select the properties to update the Simulink Block with.<br /><br /><ac:image><ri:attachment ri:filename="updating_simulink_file.png" /></ac:image><br /><br /></li><li data-uuid="3feaa988-1976-4cf8-8210-e41dbb442755">Click <strong>OK</strong>. </li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="66a34331-e28e-4465-8d15-8fe77cbec086"><ac:rich-text-body><p>Already imported properties are grayed out and cannot be edited in the <strong>Simulink Import Options </strong>dialog.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f0a75e0-1152-45ee-92b9-c6377e58678a"><ac:rich-text-body><p> If the <strong>Attach file to the project</strong> is checked in the <strong>Simulink Import Options dialog</strong>, a previous version of the attached file is replaced with a new one upon import.</p></ac:rich-text-body></ac:structured-macro><h3><strong>Co-simulation</strong></h3><p>The Simulink model can be simulated using the <ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Cameo Simulation Toolkit Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Simulation Toolkit]]></ac:plain-text-link-body></ac:link> (CST). To learn more, please click <ac:link><ri:page ri:space-key="CST2024xR3" ri:content-title="Simulation of SysML models" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>.  </p>
````

<!--NOMAGIC_PAGE id=227159106 space=SYSMLP2024xR3 version=2 -->
## PAGE 00326: Specifying a Use Case subject

- page_id: `227159106`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159106/Specifying+a+Use+Case+subject
- version_number: 2
- version_date: `2025-05-02T10:28:29.486+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Use Cases
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Specifying a Use Case subject' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="ade6b6ae-7ea5-4428-9456-2f3153e2beda"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specifying a Use Case subject" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159623 space=SYSMLP2024xR3 version=2 -->
## PAGE 00327: Specifying Constraint Element property

- page_id: `227159623`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159623/Specifying+Constraint+Element+property
- version_number: 2
- version_date: `2025-05-02T10:28:38.864+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > Custom validation > Creating new validation rules
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Specifying Constraint Element property' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="5fe18ccb-6420-4583-b475-3f54b46d5e5e"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specifying Constraint Element property" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227158777 space=SYSMLP2024xR3 version=2 -->
## PAGE 00328: Specifying feature directions

- page_id: `227158777`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158777/Specifying+feature+directions
- version_number: 2
- version_date: `2025-05-02T10:28:22.793+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Defining interfaces using ports > Provided and Required Interfaces
- labels: []

### NORMALIZED CONTENT

Before specifying the feature directions, you need to understand the following concepts:

- A [CONFLUENCE_PAGE title='Directed Feature' space='SYSMLP2024xR3'] is an enumeration type that defines literals used by directed features for specifying whether they are supported by the owning [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] , or is to be supported by other Blocks for the owning Block to use.
- A [CONFLUENCE_PAGE title='Directed Feature' space='SYSMLP2024xR3'] indicates whether the feature is supported by the owning [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] (provided), or is to be supported by other Blocks for the owning Block to use (required), or both (the owning block for features on types of [CONFLUENCE_PAGE title='Proxy Port' space='SYSMLP2024xR3'] is the type of the Block usage the Proxy Port is standing in for, which might be an internal part). Using non-flow properties means to read or write them, and using behavioral features means to invoke them. Provided non-flow properties are read and written on the owning Block, while required non-flow properties are read or written on an external Block. Provided behavioral features are invoked with the owning Block as target, while required behavioral features are invoked with an external Block as target (required).

The directed feature is a feature element that applies the «DirectedFeature» [CONFLUENCE_PAGE title='Stereotype' space='MD2024xR3']. You can specify the feature direction of the selected element.

To specify a feature direction

1. Right-click a feature’s symbols owned by a [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'] such as [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] , [CONFLUENCE_PAGE title='Attribute' space='MD2024xR3'] , [CONFLUENCE_PAGE title='Operation' space='MD2024xR3'] , and [CONFLUENCE_PAGE title='Signal Event' space='MD2024xR3'] reception.
2. From the shortcut menu, point to Feature Direction and select one of the following: The «DirectedFeature» stereotype is applied automatically.
  - Provided . Indicates that the feature shall be supported by the owning Block.
  - Required . Indicates that the feature shall be supported by other Blocks.
  - Provided and Required . Indicates that the feature shall be both provided and required.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Before specifying the feature directions, you need to understand the following concepts:</p><ul><li>A <ac:link><ri:page ri:content-title="Directed Feature" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Feature Direction]]></ac:plain-text-link-body></ac:link> is an enumeration type that defines literals used by directed features for specifying whether they are supported by the owning <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>, or is to be supported by other Blocks for the owning Block to use.</li><li>A <ac:link><ri:page ri:content-title="Directed Feature" ri:space-key="SYSMLP2024xR3" /></ac:link> indicates whether the feature is supported by the owning <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Block ]]></ac:plain-text-link-body></ac:link>(provided), or is to be supported by other Blocks for the owning Block to use (required), or both (the owning block for features on types of <ac:link><ri:page ri:content-title="Proxy Port" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Proxy Ports]]></ac:plain-text-link-body></ac:link> is the type of the Block usage the Proxy Port is standing in for, which might be an internal part). Using non-flow properties means to read or write them, and using behavioral features means to invoke them. Provided non-flow properties are read and written on the owning Block, while required non-flow properties are read or written on an external Block. Provided behavioral features are invoked with the owning Block as target, while required behavioral features are invoked with an external Block as target (required).</li></ul><p>The directed feature is a feature element that applies the «DirectedFeature» <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotype]]></ac:plain-text-link-body></ac:link>. You can specify the feature direction of the selected element.</p><p>To specify a feature direction</p><hr /><ol><li>Right-click a feature’s symbols owned by a <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link> such as <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /></ac:link>, <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Attribute" /></ac:link>, <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Operation" /></ac:link>, and <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Signal Event" /><ac:plain-text-link-body><![CDATA[Signal ]]></ac:plain-text-link-body></ac:link>reception.</li><li>From the shortcut menu, point to <strong>Feature Direction</strong> and select one of the following:<br /><ul><li><strong>Provided</strong>. Indicates that the feature shall be supported by the owning Block.</li><li><strong>Required</strong>. Indicates that the feature shall be supported by other Blocks.</li><li><strong>Provided and Required</strong>. Indicates that the feature shall be both provided and required.</li></ul>The «DirectedFeature» stereotype is applied automatically.<br /><br /></li></ol>
````

<!--NOMAGIC_PAGE id=227159822 space=SYSMLP2024xR3 version=2 -->
## PAGE 00329: Specifying project properties

- page_id: `227159822`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159822/Specifying+project+properties
- version_number: 2
- version_date: `2025-05-02T10:28:45.996+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Project Properties dialog' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="7bcb700c-aefe-4cb8-a31e-0fa4e67e3ae5"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Project Properties dialog" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159626 space=SYSMLP2024xR3 version=2 -->
## PAGE 00330: Specifying the validation rule properties

- page_id: `227159626`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159626/Specifying+the+validation+rule+properties
- version_number: 2
- version_date: `2025-05-02T10:28:39.075+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > Custom validation > Creating new validation rules
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Specifying the validation rule properties' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="b346f0ba-f36b-4e0a-ac3a-e8aea1d1e39a"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specifying the validation rule properties" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159613 space=SYSMLP2024xR3 version=2 -->
## PAGE 00331: Starting the validation

- page_id: `227159613`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159613/Starting+the+validation
- version_number: 2
- version_date: `2025-05-02T10:28:36.735+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Starting the validation' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="276f4e7c-6795-40cf-8fa0-f83989ccc0c3"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Starting the validation" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159136 space=SYSMLP2024xR3 version=2 -->
## PAGE 00332: State Machines

- page_id: `227159136`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159136/State+Machines
- version_number: 2
- version_date: `2025-05-02T10:28:31.437+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='State Machine diagram' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="932950f1-6be8-44a8-8f13-4db87558b489"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="State Machine diagram" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227158931 space=SYSMLP2024xR3 version=1 -->
## PAGE 00333: Steps of the Automatic Instantiation wizard

- page_id: `227158931`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158931/Steps+of+the+Automatic+Instantiation+wizard
- version_number: 1
- version_date: `2022-05-25T09:14:57.130+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Automatic Instantiation wizard
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Example

1349593571

#### CONTENT-COLUMN: Example

1349593573

1349593569

**On this page**

43

#### CONTENT-BLOCK: Example

1349593572

##### Introduction

This page describes each step of the **Automatic Instantiation**wizard in detail.If you are satisfied with the default values provided in the **Automatic Instantiation**wizard, you can finish the wizard in the first step without making any changes. The instances will be created with the default values and in your working package. If you want to change the default values of a single instance or create multiple sets of instances, follow all steps of the **Automatic Instantiation** wizard. You can add each set in a different package, as well as display them on the newly created diagrams.

After finishing the wizard, you can create a very large number of instance specifications, depending on the size of your system. That is why we strongly recommend selecting a new package to store all created instance specifications.

##### Opening the **Automatic Instantiation** wizard

To open the **Automatic Instantiation** wizard

1. Select the Block for which you want to create instances.
2. From the shortcut menu, select Tools > Create Instance . The Automatic Instantiation wizard opens.

##### The **Automatic Instantiation**wizard steps

The **Automatic Instantiation**wizard consists of three steps:

44

###### Step #1. Select parts to be instantiated

In this step, you can see all the available instance specification values (parts) of your selected element. At this point, you can select which parts or properties to instantiate, create or select values for parts and properties, as well as add or remove parallel parts.

You can select/deselect the parts by clicking the check marks next to the parts or the options in the Selection area.

[IMAGE alt='' src='']

Parts are displayed if the multiplicity is greater than 1. The number of parts displayed depends on the multiplicity.

- The number of parts displayed will equal the multiplicity. For example, if the multiplicity is 2, you will see 2 parts displayed in the **Automatic Instantiation**wizard. Also, in this case, you will not be able to add parallel parts or remove existing parallel parts.
- If the multiplicity is defined as an interval (for example, 0..*, 1..10, 1..* ) or *, only one part will be created by default. If you need more parts, you can create them by pressing **Insert** or selecting **Add parallel part** from the selected property’s shortcut menu.
- If the multiplicity is 1, parts will not be created.

The parts and properties are displayed with the suggested types, names, and values. In this step of the wizard, you can change them.

****

**Selecting a value for an instance**

To select a value for an instance

1. Select a part to be instantiated to which you want to add a value.
2. In **Instantiated properties**, click a **Value** specification cell and then click the ... button.
3. The **Select Instance Specification** dialog opens.
4. In the opened dialog, select the instance specification you want to add for the selected instance.
5. Click the **OK** button.

To create a value for an instance

1. Select a part to be instantiated for which you want to create a value.
2. In the **Instantiated properties**area, click the **Value** specification cell and then click the **Show Shortcut Menu** button. 
 [IMAGE alt='' src='']
3. In the opened shortcut menu, point to the **Value Specification** and then select one of the available value types.
4. In the **Value**cell, type the desired value. 
 [IMAGE alt='' src='']

****Changing the name of an instance****

Each instance has a defaultname that uses the dot notation. However, you can change the default name by clicking the value row next to the **Name** property and typing the new name for the instance. ********

****[IMAGE alt='' src='']****

**Applying a customstereotype to an instance**

You can also apply the custom stereotype to the instance. Only those stereotypes can be applied that have *Instance Specification* as their metaclass and whose customizations have a meta property named c*lassifier* with the **New Types** property value set to the instantiated element’s type.

**[IMAGE alt='' src='']**

###### The custom «ControllerFMU» and «ControllerSTM» stereotypes have *Instance Specification* as their metaclass 
and their respective customizations *ControllerFMU *Customization**and **ControllerSTM* Customization* have a meta property named c*lassifier* with the **New Types** property value set to the «Block» stereotype. 
Since the *Controller* block has the «Block» stereotype applied, the «ControllerFMU» and «ControllerSTM» stereotypes can be applied to the *Controller* block's instance.

**Changing a type for an instance**

You can change the type for the Part Property instance only if that type is a subtype of a Block (connected throughGeneralization). As shown in the following figure, the *Engine GM* Block and *Engine GMR*Block are subtypes of the *Engine*Block. When creating an instance for the *Vehicle* Block, you can change the type of the *engine*Part Property by selecting one of the following: *Engine GM* Block, *Engine GMR* Block, or *Engine*Block.

[IMAGE alt='' src='']

###### Changing the type for a Part Property instance directly in the Automatic Instantiation dialog.

###### Step #2. Select a package

In this step, you can select the package to store instance specifications. You can select an existing package from the element tree, create a new package, or clone selectedpackages. Click the **Finish** buttonafter this step if you do not want to display your created instance specifications.

[IMAGE alt='' src='']

To create a new Package in the element tree

1. In the element tree, select the Package for which you want to create the new one.
2. Click the **Creation Mode** button.
3. Click the **Create Owner** button.
4. From the open menu, select the package kind. The Specification window of that package opens.
5. Type its name.
6. Click **Close**.

To clone the Packages in the element tree

1. In the element tree, select the Package to clone. The Package is cloned recursively including all nested structures.
2. Click the **Clone** button.
3. The Specification window of cloned Package opens.
4. Type its name.
5. Click **Close**.

###### Step #3. Create a diagram (optional)

In this step, you can choose whether or not to show your created instance specifications in a new diagram. If you do not wish to create a new diagram, you can simply skip this step by clearing the **Create a new diagram** check box.

[IMAGE alt='' src='']

To display instance specifications in the new diagram

1. Make sure the **Create a new diagram** check box is selected.
2. (Optional) If you want to create and display links between your instance specification(s), select the **Create link between instances** check box.
3. Fill in the **Type diagram name** field by typing the diagram name. NoteBy default, the diagram name is the selected Package's name in Step 2.
4. From the **Select diagram type** drop-down list, select one of the diagram types.
5. Specify the owner for a new diagram:
  - Select existing Packages from the tree.
  - Click the **Create Owner** button to create a new one.
  - Click the **Clone** button to clone existing Packages.
6. Click **Finish**.

#### TIP: Example

Example

For an example of how to create instances of Blocks with complex structures, see [CONFLUENCE_PAGE title='Automatic Instantiation wizard' space='SYSMLP2024xR3'].

1349605538

**Sample model**

The model used in the figures of this page is the**VehicleStructure**sample model. To open this sample, download*[ATTACHMENT filename='VehicleStructure.mdzip'].*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="20c6b642-a930-4884-9733-65121ef8c576"><ac:parameter ac:name="id">1349593571</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3d446aeb-d8ce-477b-a985-5c300d727510"><ac:parameter ac:name="id">1349593573</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="28b3d091-7332-4414-9630-cbaec2065a94"><ac:parameter ac:name="id">1349593569</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fe562442-88e3-4d51-9701-9c53007dbf32"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d852620c-c648-488e-aa46-2b26301f3b2a"><ac:parameter ac:name="id">1349593572</ac:parameter><ac:rich-text-body><h3><span style="color: rgb(51,51,51);">Introduction</span></h3><p><span style="color: rgb(51,51,51);">This page describes each step of the <span style="color: rgb(51,51,51);"> <strong>Automatic Instantiation </strong>wizard</span> in detail.<span style="color: rgb(51,51,51);"> If you are satisfied with the default values provided in the <strong>Automatic Instantiation </strong>wizard, you can finish the wizard in the first step without making any changes. The instances will be created with the default values and in your working package. If you want to change the default values of a single instance or create multiple <span style="color: rgb(51,51,51);">sets of instances, follow</span> </span> all steps of the <strong>Automatic Instantiation</strong> wizard. You can add each set in a different package, as well as display them on the newly created diagrams. </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="598a69df-7155-4f1b-83be-1e132f79eba9"><ac:rich-text-body><p><span style="color: rgb(51,51,51);">After finishing the wizard, you can create a very large number of instance specifications, depending on the size of your system. That is why we strongly recommend selecting a new package to store all created instance specifications. <br /> </span></p></ac:rich-text-body></ac:structured-macro><h3><span>Opening the <strong>Automatic Instantiation</strong> wizard</span></h3><p><span>To open the <strong>Automatic Instantiation</strong> wizard</span></p><hr /><ol><li><span>Select the Block for which you want to create instances.</span></li><li>From the shortcut menu, select <strong>Tools</strong> &gt; <strong>Create Instance</strong>.<br />The<strong> Automatic Instantiation</strong> wizard opens.</li></ol><h3><span style="color: rgb(51,51,51);">The <strong>Automatic Instantiation </strong>wizard steps<br /> </span></h3><p><span style="color: rgb(51,51,51);">The <strong>Automatic Instantiation </strong>wizard consists of three steps:</span></p><p><span style="color: rgb(51,51,51);"> <ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ca2c73c7-9c8f-4042-b9a3-a2f4022290ce"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro> </span></p><h4><span style="color: rgb(51,51,51);">Step #1. Select parts to be instantiated<br /> </span></h4><p><span style="color: rgb(51,51,51);">In this step, you can see all the available instance specification values (parts) of your selected element. At this point, you can select which parts or properties to instantiate, create or select values for parts and properties, as well as add or remove parallel parts.</span></p><p><span style="color: rgb(51,51,51);">You can select/deselect the parts by clicking the check marks next to the parts or the options in the Selection area.</span></p><p><span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="select_properties_section.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span></p><p><span style="color: rgb(51,51,51);">Parts are displayed if the multiplicity is greater than 1. The number of parts displayed depends on the multiplicity.</span></p><ul><li><span style="color: rgb(51,51,51);">The number of parts displayed will equal the multiplicity. For example, if the multiplicity is 2, you will see 2 parts displayed in the <strong>Automatic Instantiation </strong>wizard. Also, in this case, you will not be able to add parallel parts or remove existing parallel parts.</span></li><li><span style="color: rgb(51,51,51);">If the multiplicity is defined as an interval (for example, 0..*, 1..10, 1..* ) or *, only one part will be created by default. If you need more parts, you can create them by pressing <strong>Insert</strong> or selecting <strong>Add parallel part</strong> from the selected property’s shortcut menu. </span></li><li><span style="color: rgb(51,51,51);">If the multiplicity is 1, parts will not be created.</span></li></ul><p><span style="color: rgb(51,51,51);">The parts and properties are displayed with the suggested types, names, and values. In this step of the wizard, you can change them. </span></p><p><strong> <br /> </strong></p><p><strong>Selecting <span style="color: rgb(51,51,51);">a value for an instance</span> </strong></p><p><span style="color: rgb(51,51,51);">To select a value for <span style="color: rgb(51,51,51);">an instance</span> </span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select a part to be instantiated to which you want to add a value. </span></li><li><span style="color: rgb(51,51,51);">In <strong>Instantiated properties</strong>, click a <strong>Value</strong> specification cell and then click the ... button.</span></li><li><span style="color: rgb(51,51,51);">The <strong>Select Instance Specification</strong> dialog opens.</span></li><li><span style="color: rgb(51,51,51);">In the opened dialog, select the instance specification you want to add for the selected instance.</span></li><li><span style="color: rgb(51,51,51);">Click the <strong>OK</strong> button. </span></li></ol><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">To create a value for <span style="color: rgb(51,51,51);">an instance</span> </span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select a part to be instantiated for which you want to create a value.</span></li><li><span style="color: rgb(51,51,51);">In the <strong>Instantiated properties </strong>area, click the <strong>Value</strong> specification cell and then click the <strong>Show Shortcut Menu</strong> button.<br /> <ac:image><ri:attachment ri:filename="show_shortcut_menu.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span></li><li><span style="color: rgb(51,51,51);">In the opened shortcut menu, point to the <strong>Value Specification</strong> and then select one of the available value types.</span></li><li><span style="color: rgb(51,51,51);">In the <strong>Value </strong>cell, type the desired value.<br /> <ac:image><ri:attachment ri:filename="value_property_with_defined_value.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span></li></ol><p><br /></p><p><strong> <span style="color: rgb(51,51,51);"> <strong> <span style="color: rgb(51,51,51);">Changing the name of an instance</span> </strong> </span> </strong></p><p><span style="color: rgb(51,51,51);"> <span style="color: rgb(51,51,51);">Each instance has a <span style="color: rgb(51,51,51);">default </span>name that uses the dot notation. However, you can change the default name by clicking the value row next to the <strong>Name</strong> property and typing the new name for the instance. </span> </span> <strong> <span style="color: rgb(51,51,51);"> <strong> <span style="color: rgb(51,51,51);"> </span> </strong> </span> </strong></p><p><strong> <span style="color: rgb(51,51,51);"> <strong> <span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="Changing_the_name_of_a_part.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> <br /> </span> </strong> </span> </strong></p><p><strong> <span style="color: rgb(51,51,51);"> <span style="color: rgb(51,51,51);">Applying a custom </span><span style="color: rgb(51,51,51);">stereotype</span> <span style="color: rgb(51,51,51);">to an instance</span> </span> </strong></p><p><span style="color: rgb(51,51,51);">You can also apply the custom stereotype to the instance. Only those stereotypes can be applied that have <em>Instance Specification</em> as their metaclass and whose customizations have a meta property named c<em>lassifier</em> with the <strong>New Types</strong> property value set to the instantiated element’s type.</span></p><p><strong> <span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="Apply_a_custom_stereotype_to_instance_SYSML.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span> </strong></p><h6 style="text-align: center;margin-bottom: 20.0px;"><span style="color: rgb(51,51,51);">The custom <span> <span style="color: rgb(62,63,64);">«</span></span>ControllerFMU<span><span style="color: rgb(62,63,64);">»</span> </span> and <span> <span style="color: rgb(62,63,64);">«</span></span>ControllerSTM<span><span style="color: rgb(62,63,64);">»</span> </span> stereotypes have <em>Instance Specification</em> as their metaclass <br />and their respective customizations <em>ControllerFMU <em style="text-align: center;">Customization </em></em>and <em> <em style="text-align: center;">ControllerSTM</em> Customization</em> have a meta property named c<em>lassifier</em> with the <strong>New Types</strong> property value set to the <span> <span style="color: rgb(62,63,64);">«</span></span>Block<span><span style="color: rgb(62,63,64);">»</span> </span> stereotype. <br />Since the <em>Controller</em> block has the <span> <span style="color: rgb(62,63,64);">«</span></span>Block<span><span style="color: rgb(62,63,64);">»</span> </span> stereotype applied, the <span> <span style="color: rgb(62,63,64);">«</span></span>ControllerFMU<span><span style="color: rgb(62,63,64);">»</span> </span> and <span> <span style="color: rgb(62,63,64);">«</span></span>ControllerSTM<span><span style="color: rgb(62,63,64);">»</span> </span> stereotypes can be applied to the <em>Controller</em> block's instance.</span></h6><p><strong> <span style="color: rgb(51,51,51);">Changing a type for an instance</span> </strong></p><p><span style="color: rgb(51,51,51);">You can change the type for the Part Property instance only if that type is a subtype of a Block (connected <span style="color: rgb(51,51,51);">through </span>Generalization). As shown in the following figure, the <em>Engine GM</em> Block and <em>Engine GMR </em>Block are subtypes of the <em>Engine </em>Block. When creating an instance for the <em>Vehicle</em> Block, you can change the type of the <em>engine </em>Part Property by selecting one of the following: <em>Engine GM</em> <span style="color: rgb(51,51,51);"> Block, <em>Engine GMR</em> </span> <span style="color: rgb(51,51,51);"> Block, or <em>Engine </em></span><span style="color: rgb(51,51,51);">Block.</span> </span></p><p><span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="specifying_type_for_instantiated_properties.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span></p><h6 style="text-align: center;margin-bottom: 20.0px;"><span style="color: rgb(51,51,51);">Changing the type for a Part Property instance directly in the Automatic Instantiation dialog.</span></h6><h4><span style="color: rgb(51,51,51);">Step #2. Select a package<br /> </span></h4><p><span style="color: rgb(51,51,51);">In this step, you can select the package to store instance specifications. You can select an <span style="color: rgb(51,51,51);">existing package from the element tree, create a new package, or clone selected </span>packages. <span style="color: rgb(51,51,51);">Click the <strong>Finish</strong> button </span>after this step if you do not want to display your created instance specifications.</span></p><p><span style="color: rgb(51,51,51);"> <ac:image ac:align="center"><ri:attachment ri:filename="select_package_step2.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span></p><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">To create a new Package in the element tree</span></p><hr /><ol><li><span style="color: rgb(51,51,51);">In the element tree, select the Package for which you want to create the new one.</span></li><li><span style="color: rgb(51,51,51);">Click the <strong>Creation Mode</strong> button. </span></li><li><span style="color: rgb(51,51,51);">Click the <strong>Create Owner</strong> button.</span></li><li><span style="color: rgb(51,51,51);">From the open menu, select the package kind. The Specification window of that package opens.<br /> </span></li><li><span style="color: rgb(51,51,51);">Type its name.</span></li><li><span style="color: rgb(51,51,51);">Click <strong>Close</strong>.<br /> </span></li></ol><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">To clone the Packages <span style="color: rgb(51,51,51);">in the element tree</span> </span></p><hr /><ol><li><p><span style="color: rgb(51,51,51);">In the element tree, select the Package to clone.<br /> </span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="eeb6f4cf-5cbe-45ab-9321-bf829e0ba307"><ac:rich-text-body>The Package is cloned recursively including all nested structures.</ac:rich-text-body></ac:structured-macro></li><li><span style="color: rgb(51,51,51);">Click the <strong>Clone</strong> button.</span></li><li><span style="color: rgb(51,51,51);">The Specification window of cloned Package opens.<br /> </span></li><li><span style="color: rgb(51,51,51);">Type its name.</span></li><li><span style="color: rgb(51,51,51);">Click <strong>Close</strong>.</span></li></ol><h4><span style="color: rgb(51,51,51);">Step #3. Create a diagram (optional)</span></h4><p><span style="color: rgb(51,51,51);">In this step, you can choose whether or not to show your created instance specifications in a new diagram. If you do not wish to create a new diagram, you can simply skip this step by clearing the <span style="color: rgb(51,51,51);"> <strong>Create a new diagram</strong> </span> check box.<br /> </span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="create_diagram_step3.png"><ri:page ri:content-title="Steps of the Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p><span style="color: rgb(51,51,51);"> <br /> </span></p><p><span style="color: rgb(51,51,51);">To display instance specifications in the new diagram<br /> </span></p><hr /><ol><li>Make sure the <span style="color: rgb(51,51,51);"> <strong>Create a new diagram</strong> <span style="color: rgb(51,51,51);">check box is selected.</span> </span></li><li><span style="color: rgb(51,51,51);">(Optional) If you want to create and display links between your instance specification(s), select the <strong>Create link between instances</strong> <span style="color: rgb(51,51,51);">check box</span>.</span></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">Fill in the <strong>Type diagram name</strong> field by typing the diagram name.<br /> </span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4db12659-8cdc-4979-b226-9ee2bb0450af"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);"> By default, the diagram name is the selected Package's name in Step 2.<br /> </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"> <br /> </span></p></li><li><span style="color: rgb(51,51,51);">From the <strong>Select diagram type</strong> drop-down list, select one of the diagram types.</span></li><li><span style="color: rgb(51,51,51);"> <span style="color: rgb(51,51,51);">Specify the owner for a new diagram:<br /> </span> </span><ul><li>Select existing Packages from the tree.</li><li><span style="color: rgb(51,51,51);"> <span style="color: rgb(51,51,51);">Click the <strong>Create Owner</strong> </span> </span> button to create a new one.</li><li><span style="color: rgb(51,51,51);"> <span style="color: rgb(51,51,51);">Click the <strong>Clone</strong> button to clone existing Packages.</span> </span></li></ul></li><li><span style="color: rgb(51,51,51);">Click <strong>Finish</strong>.</span></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="1b071898-67e1-41f9-b85f-744b07c8eaa6"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p>For an example of how to create instances of Blocks with complex structures, see <ac:link><ri:page ri:content-title="Automatic Instantiation wizard" ri:space-key="SYSMLP2024xR3" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="667030bd-9faf-4e6a-b1ab-735171e4e187"><ac:parameter ac:name="id">1349605538</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Sample model</strong></p><p class="auto-cursor-target"><span>The model used in the figures of this page is the </span><strong>VehicleStructure</strong><span> sample model. To open this sample, download</span><span class="confluence-link"><em> <ac:link><ri:attachment ri:filename="VehicleStructure.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link>.</em></span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158945 space=SYSMLP2024xR3 version=1 -->
## PAGE 00334: Steps of the Extract Structure Wizard

- page_id: `227158945`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158945/Steps+of+the+Extract+Structure+Wizard
- version_number: 1
- version_date: `2018-01-06T13:25:19.241+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Extract Structure Wizard
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Example

1350378385

#### CONTENT-COLUMN: Example

1350378387

1350388698

**On this page**

33

#### CONTENT-BLOCK: Example

1350378386

In this page you can read about each step of the **Extract Structure Wizard** in details, understand option boxes and buttons.

##### Opening the **Extract Structure Wizard**

To open the **Extract Structure Wizard**

1. In the SysML Internal Block Diagram or a structure compartment, right-click a Part Properties that you want to extract.
2. From the shortcut menu, select Refactor > Extract . The Extract Structure Wizard opens.

##### The Extract Structure Wizard steps

The Extract Structure Wizard consists of three steps:

44

###### Step #1. Specification of a new element

In this step, you can specify a diagram into which the extracted part will be moved and an owner wherein this new diagram will be created. You can also define the type of the newly created classifier element that will own the diagram. The Block and the SysML Internal Block Diagram type are selected by default. The name of the SysML Internal Block Diagram will be the same as the specified name of the classifier element.

[IMAGE alt='' src='']

###### Step 1 in the Extract Structure Wizard: Specify a new element.

| Dialog boxes | Description |
| --- | --- |
| Type element name | Type the name of the new element, that is, classifier, wherein the extracted part will be stored. |
| Select element type | Open the list and select the element type. The default element type is a class. By using the customized plugins, you can add custom elements to the element type list. |
| Select owner | In the model tree, select a package, profile, or model as an owner of the newly created element. You may also:Create a new owner. Click the Create Owner button, select an element type, and specify its properties.Clone an existing package, profile, or model. In the model tree, select an owner, click the Clone button, and specify properties of the cloned element. |
| Select diagram type | Open the list and select the diagram type for the extracted part. The default diagram type is a composite structure diagram. By using the customized plugins, you can add custom diagrams to the diagram type list. |

After you have specified the new element name, type, owner of the diagram, and the type of the new diagram, do one of the following:

- Click Next , if you want to specify ports and to define a referencing element. The next wizard step opens.
- Click Finish . The selected part of a composite structure diagram is extracted to a new diagram that is specified in this step. Instead of the extracted part, the selected element type is created in the SysML Internal Block Diagram referencing to the newly created diagram. The second and the third wizard steps are skipped, that is, the default options are taken.

###### Step #2. Creation of ports

In this step, there are listed the port(s) that will be created for the:

- intersected connector(s)
- incoming connector(s)
- outgoing connector(s)

The **Create ports** list is empty unless there are intersected, incoming and/or outgoing connector(s) selected in the source SysML Internal Block Diagram.

[IMAGE alt='' src='']

###### Step 2 in the Extract Structure Wizard: Create ports.

After you have selected the ports, do one of the following:

- Click Back to return to the first step.
- Click Next , if you want to define a property (that is, referencing element). The next wizard step opens.
- Click Finish . The selected part of the SysML Internal Block Diagram is extracted to a new diagram. The third wizard step is skipped, that is, the default options are taken.

###### Step #3. Creation of a property

A property is created as the result of the extraction. The property is created under the classifier that was specified in the first wizard step. The symbol of the property is created in the source SysML Internal Block Diagram and represents the elements moved to the target diagram during the extraction.

###### [IMAGE alt='' src='']Step 3 in the Extract Structure Wizard: Create a property.

After you have selected the parameters, do one of the following:

- Click Back to return to the previous step.
- Click Finish . The selected part of a SysML Internal Block Diagram is extracted to a new diagram.

#### TIP: Example

Example

As example, how to extract structure and what results to expect, read [CONFLUENCE_PAGE title='Extract Structure Wizard' space='SYSMLP2024xR3']

1350378384

**Sample model**

The model used in the figures of this page is the **climate control system** sample model. To open this sample do one of the following:

- Download *[ATTACHMENT filename='climate control system.mdzip'].*
- Find in modeling tool *<modeling tool installation directory>\samples\SysML\climate control system.mdzip.*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ea812ea0-d2e9-4195-9bd6-a684ea4f8414"><ac:parameter ac:name="id">1350378385</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="02120c18-fa53-44ab-9af7-ce9b1271e0ce"><ac:parameter ac:name="id">1350378387</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="16a73811-299c-4273-b591-bfb57b689216"><ac:parameter ac:name="id">1350388698</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="53aa8855-cc8c-425c-a2c3-b9d2eca2fd78"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b383aebb-0fd4-4aeb-a3fe-d69e572af9a4"><ac:parameter ac:name="id">1350378386</ac:parameter><ac:rich-text-body><p>In this page you can read about each step of the <strong>Extract Structure Wizard</strong> in details, understand option boxes and buttons.</p><h3>Opening the <strong>Extract Structure Wizard</strong></h3><p>To open the <strong>Extract Structure Wizard</strong></p><hr /><ol><li>In the SysML Internal Block Diagram or a structure compartment, right-click a Part Properties that you want to extract.</li><li>From the shortcut menu, select <strong>Refactor</strong> &gt; <strong>Extract</strong>. <br />The <strong>Extract Structure Wizard</strong> opens.</li></ol><h3>The Extract Structure Wizard steps</h3><p>The Extract Structure Wizard consists of three steps:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e8d829de-9816-48f5-aa11-aab1474b429a"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></p><h4>Step #1. Specification of a new element</h4><p>In this step, you can specify a diagram into which the extracted part will be moved and an owner wherein this new diagram will be created. You can also define the type of the newly created classifier element that will own the diagram. The Block and the SysML Internal Block Diagram type are selected by default. The name of the SysML Internal Block Diagram will be the same as the specified name of the classifier element.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="extract_structure_wizard_step1.png"><ri:page ri:content-title="Steps of the Extract Structure Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Step 1 in the Extract Structure Wizard: Specify a new element.</h6><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Dialog boxes</th><th>Description</th></tr><tr><td>Type element name</td><td>Type the name of the new element, that is, classifier, wherein the extracted part will be stored.</td></tr><tr><td>Select element type</td><td>Open the list and select the element type. The default element type is a class. By using the customized plugins, you can add custom elements to the element type list.</td></tr><tr><td>Select owner</td><td><p>In the model tree, select a package, profile, or model as an owner of the newly created element. You may also:</p><ul><li>Create a new owner. Click the <strong>Create Owner</strong> button, select an element type, and specify its properties.</li><li>Clone an existing package, profile, or model. In the model tree, select an owner, click the <strong>Clone</strong> button, and specify properties of the cloned element.</li></ul></td></tr><tr><td>Select diagram type</td><td>Open the list and select the diagram type for the extracted part. The default diagram type is a composite structure diagram. By using the customized plugins, you can add custom diagrams to the diagram type list.</td></tr></tbody></table><p><br /></p><p>After you have specified the new element name, type, owner of the diagram, and the type of the new diagram, do one of the following:</p><ul><li>Click <strong>Next</strong> , if you want to specify ports and to define a referencing element. The next wizard step opens.</li><li>Click <strong>Finish</strong>. The selected part of a composite structure diagram is extracted to a new diagram that is specified in this step. Instead of the extracted part, the selected element type is created in the SysML Internal Block Diagram referencing to the newly created diagram. The second and the third wizard steps are skipped, that is, the default options are taken.</li></ul><h4>Step #2. Creation of ports</h4><p>In this step, there are listed the port(s) that will be created for the:</p><ul><li>intersected connector(s)</li><li>incoming connector(s)</li><li>outgoing connector(s)</li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e0e309a7-c52c-4287-b7d5-4df133ec3729"><ac:rich-text-body><p>The <strong>Create ports</strong> list is empty unless there are intersected, incoming and/or outgoing connector(s) selected in the source SysML Internal Block Diagram.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image ac:align="center"><ri:attachment ri:filename="extract_structure_wizard_step2.png"><ri:page ri:content-title="Steps of the Extract Structure Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Step 2 in the Extract Structure Wizard: Create ports.</h6><p>After you have selected the ports, do one of the following:</p><ul><li>Click <strong>Back</strong> to return to the first step.</li><li>Click <strong>Next</strong>, if you want to define a property (that is, referencing element). The next wizard step opens.</li><li>Click <strong>Finish</strong>. The selected part of the SysML Internal Block Diagram is extracted to a new diagram. The third wizard step is skipped, that is, the default options are taken.</li></ul><h4>Step #3. Creation of a property</h4><p>A property is created as the result of the extraction. The property is created under the classifier that was specified in the first wizard step. The symbol of the property is created in the source SysML Internal Block Diagram and represents the elements moved to the target diagram during the extraction.</p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="extract_structure_wizard_step3.png"><ri:page ri:content-title="Steps of the Extract Structure Wizard" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>Step 3 in the Extract Structure Wizard: Create a property.</h6><p>After you have selected the parameters, do one of the following:</p><ul><li>Click <strong>Back</strong> to return to the previous step.</li><li>Click <strong>Finish</strong>. The selected part of a SysML Internal Block Diagram is extracted to a new diagram.</li></ul><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="1b071898-67e1-41f9-b85f-744b07c8eaa6"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p>As example, how to extract structure and what results to expect, read  <ac:link><ri:page ri:content-title="Extract Structure Wizard" ri:space-key="SYSMLP2024xR3" /></ac:link></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="98faa628-5ffe-4bbe-ab60-8a2b29322620"><ac:parameter ac:name="id">1350378384</ac:parameter><ac:rich-text-body><p><strong>Sample model</strong></p><p>The model used in the figures of this page is the <strong>climate control system</strong> sample model. To open this sample do one of the following:</p><ul><li>Download<span class="confluence-link"><em> <ac:link><ri:attachment ri:filename="climate control system.mdzip"><ri:page ri:content-title="_sample models" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link>.</em></span></li><li><span class="confluence-link">Find in modeling tool <em>&lt;modeling tool installation directory&gt;\samples\SysML\climate control system.mdzip.</em></span></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158529 space=SYSMLP2024xR3 version=1 -->
## PAGE 00335: Structure tab

- page_id: `227158529`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158529/Structure+tab
- version_number: 1
- version_date: `2024-01-29T11:05:58.663+01:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

234973073

234973075

234973072

**On this page**

33

234973074

INLINE

The Structure browser allows you to browse for deeply nested structures of the structured classifier in your model. The node: **diameter : mm** represents the property: **diameter : mm** of the classifier: **Wheel** and also the property:**w : Wheel** is the property of the classifier: **WheelAssembly**, as shown in the image below:

[IMAGE alt='' src='']

###### The Structure tab in the Model Browser.

##### Opening the Structure tab

To open the Structure tab

1. From the main menu, select Window > Structure .

The property nodes, which are shown inside the property node (the parent property node), are the properties of the classifier that type the parent property node.

In the Structure tab, you can open any selected element in a new tree.

To open a new tree

1. Select the element and in the Structure tab toolbar click [ATTACHMENT filename='open_in_new_tree_button.png'] .

##### inheritDisplaying Inherited Structure option

The Structure tab can show the properties that are inherited from the generalization classifier.

To display inherited structures from the generalization classifier in the Structure tree

1. Click [ATTACHMENT filename='options_button_in_model_browser.png'] on the right of the Structure Browser.
2. Select the Show Inherited Structure option.

[IMAGE alt='' src='']

##### Nesting Satisfied Requirements option

The Structure Tab can also show requirements nested within elements that satisfy them.

If the relationship is contextualized, its context is considered as well. [CONFLUENCE_PAGE title='Contextual relationships' space='SYSMLP2024xR3']>]]>

To nest requirements under the satisfying elements

1. Click [ATTACHMENT filename='options_button_in_model_browser.png'] on the right of the Structure Browser.
2. Select the Nest Satisfied Requirements option.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="005eefc0-9c24-4f9d-af0e-f588ff044e2d"><ac:parameter ac:name="id">234973073</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="1afec384-ac5a-4fa7-aed1-3589930b749b"><ac:parameter ac:name="id">234973075</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6b867581-172d-4fd5-a7bd-77ca76d6859c"><ac:parameter ac:name="id">234973072</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="f28409f4-7fba-4311-835f-72eb096e6fc6"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8727682f-0d0f-4290-8f63-ac0c0b38f152"><ac:parameter ac:name="id">234973074</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="71bcd187-e6fd-4a07-a515-9a453380dce0"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>The Structure browser allows you to browse for deeply nested structures of the <ac:inline-comment-marker ac:ref="2d024c67-7ebe-480c-b69d-62bbdd70f4ce">structured</ac:inline-comment-marker> classifier in your model. The node: <strong>diameter : mm</strong> represents the property: <strong>diameter : mm</strong> of the classifier: <strong>Wheel</strong> and also the property:<strong> w : Wheel</strong> is the property of the classifier: <strong>WheelAssembly</strong>, as shown in the image below:</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="structure_tree.png"><ri:page ri:content-title="Structure tab" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The Structure tab in the Model Browser.</h6><h3>Opening the Structure tab</h3><p>To open the <ac:inline-comment-marker ac:ref="854ee52b-798b-4243-b01b-3febcf9656c0">Structure tab</ac:inline-comment-marker></p><hr /><ol><li><ac:inline-comment-marker ac:ref="d54cdf9f-b03d-4a6d-bc28-7f1cce545c9d">From the</ac:inline-comment-marker> main menu, select <strong>Window</strong> &gt; <strong>Structure</strong>.</li></ol><p>The property nodes, which are shown inside the property node (the parent property node), are the properties of the classifier that type the parent property node.</p><p><br /></p><p>In the Structure tab, you can open any selected element in a new tree.</p><p>To open a new tree</p><hr /><ol><li>Select the element and in the Structure tab toolbar click <ac:image><ri:attachment ri:filename="open_in_new_tree_button.png"><ri:page ri:content-title="Structure tab" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>.</li></ol><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="a39b0a2e-5f19-4d93-9445-e7ed53ee756e"><ac:parameter ac:name="">inherit</ac:parameter></ac:structured-macro>Displaying Inherited Structure option</h3><p>The Structure tab can show the properties that are inherited from the generalization classifier.</p><p><br /></p><p>To display inherited structures from the generalization classifier in the Structure tree</p><hr /><ol><li>Click<ac:image ac:title="Options" ac:alt="Options"><ri:attachment ri:filename="options_button_in_model_browser.png"><ri:page ri:content-title="Structure tab" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> on the right of the Structure Browser.</li><li>Select the <strong>Show Inherited Structure</strong> option.</li></ol><p><ac:image><ri:attachment ri:filename="show_inherited_structure.png"><ri:page ri:content-title="Structure tab" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h3>Nesting Satisfied Requirements option</h3><p>The Structure Tab can also show requirements nested within elements that satisfy them.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="dea39c57-ba95-454d-88b6-9bfd3f0a9375"><ac:rich-text-body><p>If the relationship is contextualized, its context is considered as well. <ac:link><ri:page ri:content-title="Contextual relationships" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more about contextual relationships >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><span style="letter-spacing: 0.0px;"><br /></span></p><p><span style="letter-spacing: 0.0px;">To nest requirements under the satisfying elements<br /></span></p><hr /><ol><li>Click<ac:image ac:title="Options" ac:alt="Options"><ri:attachment ri:filename="options_button_in_model_browser.png"><ri:page ri:content-title="Structure tab" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> on the right of the Structure Browser.</li><li>Select the <strong>Nest Satisfied Requirements </strong>option.</li></ol><p><ac:image><ri:attachment ri:filename="nest_saisfied_requirements.png"><ri:page ri:content-title="Structure tab" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159779 space=SYSMLP2024xR3 version=1 -->
## PAGE 00336: Subsystem

- page_id: `227159779`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159779/Subsystem
- version_number: 1
- version_date: `2018-03-21T13:48:46.016+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Visibility representation

299594081

#### CONTENT-COLUMN: Visibility representation

299594083

#### CONTENT-BLOCK: Visibility representation

299594082

A Subsystem is typically a large, encapsulated block within a larger system.

You can convert any Block to a Subsystem if you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).

[IMAGE alt='' src='']

#### NOTE: Visibility representation

Visibility representation

In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.

##### Converting a Block to Subsystem

To convert a Block to Subsystem

1. Right-click a Block.
2. Select Refactor > Convert To > More Specific > Subsystem . The Block is converted to a Subsystem.

299594080

**Related pages**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9a1c9dba-0580-415f-b1e3-51e54fe4497f"><ac:parameter ac:name="id">299594081</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fa1d251a-6550-4ab3-b043-0c7dfb7f5399"><ac:parameter ac:name="id">299594083</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8280dc5f-99b3-4a03-b237-673214b74179"><ac:parameter ac:name="id">299594082</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>A Subsystem is typically a large, encapsulated block within a larger system.</p><p>You can convert any Block to a Subsystem <span style="color: rgb(51,51,51);">if you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).</span></p><p><br /></p><p><ac:image ac:title="Subsystem" ac:alt="Subsystem"><ri:attachment ri:filename="subsystem.png"><ri:page ri:content-title="Subsystem" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="45e244e1-7a14-47d4-88f2-ec499c585171"><ac:parameter ac:name="title">Visibility representation</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.</span><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Converting a Block to Subsystem</h3><p>To convert a Block to Subsystem</p><hr /><ol><li>Right-click a Block.</li><li>Select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>Subsystem</strong>.<br />The Block is converted to a Subsystem.</li></ol><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2d66f4a5-f6a5-4b8c-9860-d435e6b467c8"><ac:parameter ac:name="id">299594080</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Block Definition Diagram ]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227160257 space=SYSMLP2024xR3 version=2 -->
## PAGE 00337: Supported and unsupported SysML concepts

- page_id: `227160257`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160257/Supported+and+unsupported+SysML+concepts
- version_number: 2
- version_date: `2025-05-02T10:26:37.834+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Modelica export
- labels: []

### NORMALIZED CONTENT

##### SysML supported concepts

The translator can be used for both high-level black-box architecture export, when simulation engineer have to implement all block behaviors in Modelica tool, or full or partial behavior implementation too.

Export engine takes one block as a starting point and exports all containing model structure recursively including:

- [Block](https://docs.nomagic.com/display/SYSMLP2024xR3/Block)and [interface](https://docs.nomagic.com/display/SYSMLP2024xR3/Interface+Block) definitions.
- [Parts](https://docs.nomagic.com/display/SYSMLP2024xR3/Part+Property), [value properties](https://docs.nomagic.com/display/SYSMLP2024xR3/Value+Property), [flow properties](https://docs.nomagic.com/display/SYSMLP2024xR3/Flow+Property) with their default/[initial values](https://docs.nomagic.com/display/SYSMLP2024xR3/Initial+Values) and associated [units](https://docs.nomagic.com/display/SYSMLP2024xR3/Unit). We highly recommend to use part names, otherwise the artificial names are exported.
- [Proxy](https://docs.nomagic.com/display/SYSMLP2024xR3/Proxy+Port)and [flow ports](https://docs.nomagic.com/display/SYSMLP2024xR3/Flow+Port) and [connectors](https://docs.nomagic.com/display/SYSMLP2024xR3/Connectors) among them.
- Parametrics – [constraints blocks](https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Block), [constraint properties](https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Property), [constraint parameters](https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Parameter) and connections among them
- [State Machines](https://docs.nomagic.com/display/SYSMLP2024xR3/State+Machines)
- [IBD](https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Internal+Block+Diagram)diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>SysML supported concepts</h3><p>The translator can be used for both high-level black-box architecture export, when simulation engineer have to implement all block behaviors in Modelica tool, or full or partial behavior implementation too.</p><p>Export engine takes one block as a starting point and exports all containing model structure recursively including:</p><ul><li><p><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Block">Block </a>and <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Interface+Block">interface</a> definitions.</p></li><li><p><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Part+Property">Parts</a>, <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Value+Property">value properties</a>, <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Flow+Property">flow properties</a> with their default/<a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Initial+Values">initial values</a> and associated <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Unit">units</a>.</p><p>We highly recommend to use part names, otherwise the artificial names are exported.</p></li><li><p><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Proxy+Port">Proxy </a>and <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Flow+Port">flow ports</a> and <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Connectors">connectors</a> among them.</p></li><li><p>Parametrics – <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Block">constraints blocks</a>, <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Property">constraint properties</a>, <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Constraint+Parameter">constraint parameters</a> and connections among them</p></li><li><p><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/State+Machines">State Machines</a></p></li><li><p><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Internal+Block+Diagram">IBD </a>diagrams</p></li></ul><p />
````

<!--NOMAGIC_PAGE id=227159120 space=SYSMLP2024xR3 version=2 -->
## PAGE 00338: Swimlane

- page_id: `227159120`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159120/Swimlane
- version_number: 2
- version_date: `2025-05-02T10:28:31.050+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Modeling functional flows with Activities
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Swimlanes' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="7bae7095-9c78-4ccc-88e1-4b1853ac0c0d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Swimlanes" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227158559 space=SYSMLP2024xR3 version=2 -->
## PAGE 00339: Switching between multiple projects

- page_id: `227158559`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158559/Switching+between+multiple+projects
- version_number: 2
- version_date: `2025-05-02T10:28:18.952+02:00`
- ancestors: SysML Plugin Documentation > Getting started
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Working with multiple projects' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="c0ce6a53-bfa8-4d55-b889-0abc9d29a503"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with multiple projects" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158511 space=SYSMLP2024xR3 version=1 -->
## PAGE 00340: SysML 1.7 support

- page_id: `227158511`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158511/SysML+1.7+support
- version_number: 1
- version_date: `2022-10-13T11:58:53.962+02:00`
- ancestors: SysML Plugin Documentation
- labels: []

### NORMALIZED CONTENT

1552545625

INLINE

1552545636

INLINE

1552545624

INLINE

**On this page**

5

1552545626

INLINE

As of version 2022x, the SysML Plugin supports the SysML 1.7 specification.

##### QUDV model library for owned operations

The*dependsOnUnits*owned operation has been redefined with the*dependsOnUnits*operation owned by*Unit*for the following blocks:*SimpleUnit*,*DerivedUnit*, and *ConversionBasedUnit.*The *dependsOnQuantityKinds*owned operation for the *SimpleQuanitityKind* block has been redefined with the*dependsOnQuantityKinds*operation owned by *QuantityKind*.

##### *Prefix::Symbol* in the QUDV model library

In the QUDV model library, the multiplicity of*Prefix::Symbol*has been changed from [1] to [0..1].

##### Renamed allocation compartments

The **Apply SysML 1.7 Allocation Compartment Naming** symbol property allows renaming allocation compartments according to the SysML 1.7 standard. The "allocatedTo" compartment is renamed to "allocatedToElements", and the "allocatedFrom" compartment to"allocatedElements".

[IMAGE alt='' src='']

###### Renaming allocation compartments according to the SysML 1.7 standard.

To rename allocation compartments for an element shape

1. Right-click an element shape and select Symbol Properties .
2. In the open dialog, set the Apply SysML 1.7 Allocation Compartment Naming property to true .

To rename allocation compartments for all new shapes of a specific element type

1. In the main menu of a modeling tool, go to Options > Project .
2. On the left side of the Project Options dialog, expand the Symbol styles property group.
3. Find and select the desired element type.
4. On the right side of the Project Options dialog, set the Apply SysML 1.7 Allocation Compartment Naming property to true .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5aedec58-e684-4f22-84c3-bfd14d92a999"><ac:parameter ac:name="id">1552545625</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="54e89a7a-6e12-4f87-ae6e-f39d2585d403"><ac:parameter ac:name="id">1552545636</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0fb97b97-96f8-4d05-aa2c-c2b2e9c079f6"><ac:parameter ac:name="id">1552545624</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d4954e44-dca2-4dca-84d2-65fc45cfada0"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1e78176c-2a72-4264-86b1-85971a29a5fc"><ac:parameter ac:name="id">1552545626</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">As of version 2022x, the SysML Plugin supports the SysML 1.7 specification.</span></p><h3><span style="color: rgb(62,63,64);"><br />QUDV model library for owned operations</span></h3><p><span style="color: rgb(62,63,64);">The<span> </span><em>dependsOnUnits</em><span> </span>owned operation has been redefined with the<span> </span><em>dependsOnUnits </em>operation owned by<span> </span><em>Unit</em><span> </span>for the following blocks:<span> </span><em>SimpleUnit</em>,<span> </span><em>DerivedUnit</em>, and <em>ConversionBasedUnit.</em><span> </span>The <em>dependsOnQuantityKinds </em>owned operation for the <em>SimpleQuanitityKind</em> block has been redefined with the<span> </span><em>dependsOnQuantityKinds</em><span> </span>operation owned by <em>QuantityKind</em>.</span></p><h3><span style="color: rgb(62,63,64);"><br /><em>Prefix::Symbol</em> in the QUDV model library</span></h3><p>In the QUDV model library, the multiplicity of<span> </span><em>Prefix::Symbol</em><span> </span>has been changed from <span class="error">[1]</span> to <span class="error">[0..1]</span>.</p><h3><br />Renamed allocation compartments</h3><p>The <strong>Apply SysML 1.7 Allocation Compartment Naming</strong> symbol property allows renaming allocation compartments according to the SysML 1.7 standard. The &quot;allocatedTo&quot; compartment is renamed to &quot;allocatedToElements&quot;, and the &quot;allocatedFrom&quot; compartment to&quot;allocatedElements&quot;.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="renaming_allocation_compartments.png"><ri:page ri:content-title="SysML 1.7 support" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Renaming allocation compartments according to the SysML 1.7 standard.</h6><p><br /></p><p>To rename allocation compartments for an element shape</p><hr /><ol><li>Right-click an element shape and select <strong>Symbol Properties</strong>.</li><li>In the open dialog, set the <strong>Apply SysML 1.7 Allocation Compartment Naming</strong> property to <em>true</em>.</li></ol><p><br /></p><p>To rename allocation compartments for all new shapes of a specific element type</p><hr /><ol><li>In the main menu of a modeling tool, go to <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>On the left side of the <strong>Project Options</strong> dialog, expand the <strong>Symbol styles</strong> property group.</li><li>Find and select the desired element type.</li><li>On the right side of the <strong>Project Options</strong> dialog, set the <strong>Apply SysML 1.7 Allocation Compartment Naming</strong> property to <em>true</em>.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227159421 space=SYSMLP2024xR3 version=3 -->
## PAGE 00341: SysML active validation suites

- page_id: `227159421`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159421/SysML+active+validation+suites
- version_number: 3
- version_date: `2025-05-02T10:28:35.249+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation
- labels: []

### NORMALIZED CONTENT

1258309421

1258309424

1258317887

**On this page**

43

1258309423

##### Introduction

The SysML active validation suites enable you to see if a model is correct and complete immediately. It instantly displays any errors in the model and suggests appropriate solutions. The active validation suites have «activeValidationSuite» stereotype applied.

Each profile contains its own active validation suites. You can [CONFLUENCE_PAGE title='Creating validation suites' space='SYSMLP2024xR3'].

You can meet the following active validation suites in the [CONFLUENCE_PAGE title='Validation dialog' space='SYSMLP2024xR3']**Validation** dialog or [CONFLUENCE_PAGE title='Validation Suites dialog' space='SYSMLP2024xR3']**Validation Suites** dialog:

- SysML_activeValSuite - Activities contains SysML constraints on the following elements: Discrete and noBuffer.
- SysML_activeValSuite - Blocks contains SysML constraints on the following elements: Binding Connector, Block, Distributed Property and Value Type.
- SysML_activeValSuite - Constraint Blocks contains SysML constraints on the following elements: Constraint Block and Constraint Property.
- SysML_activeValSuite - Non-normative Extensions contains SysML constraints on the following elements: nonStreaming, Streaming, Design Constraint, Functional Requirement, Interface Requirement and Performance Requirement.
- SysML_activeValSuite - Port and Flows contains SysML constraints on the following elements: Flow Port, Flow Property, Flow Specification and Item Flow.
- SysML_activeValSuite - Requirements contains SysML constraints on the following elements: Copy, Requirement and Test Case.

You can find active validation suites in the [CONFLUENCE_PAGE title='Containment tab' space='SYSMLP2024xR3'] when the **Show Auxiliary Resources** option is enabled, expand the *MD Customization for SysML* Package> *SysML constraints* Package > *SysML activeValSuite* package. The **SysML activeValSuite** Package is divided into separate Packages and contain an appropriate [CONFLUENCE_PAGE title='SysML validation rules' space='SYSMLP2024xR3'].

[CONFLUENCE_PAGE title='Metaclass' space='MD2024xR3']true

##### Validating a project with active validation suites

To manually validate project with active validation suites, you can select the specific**Active ValSuite** (mentioned above) as the **Validation Suite** in the [CONFLUENCE_PAGE title='Validation dialog' space='SYSMLP2024xR3']**Validation** dialog. [How to start the validation >>](https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+validation+suites#SysMLvalidationsuites-startStartingthevalidation)

[CONFLUENCE_PAGE title='Active validation suites' space='MD2024xR3']true

1258309419

**Related pages**

- MagicDraw predefined validation suites
- MagicDraw active validation suites
- [SysML validation suites](https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+validation+suites)
- [Requirements validation suites](https://docs.nomagic.com/display/CRMP2024xR3/Requirements+validation+suites)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a44b8549-3317-441e-9946-3c452d6e4249"><ac:parameter ac:name="id">1258309421</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="520f4ccc-566c-4692-8cf2-cae17845f2c3"><ac:parameter ac:name="id">1258309424</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2bc6c556-5c0c-4b4b-8b66-24e5cb5cb0b3"><ac:parameter ac:name="id">1258317887</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e6ad03ee-b59e-4f85-b50d-0d58126a0611"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b1de6deb-bd1e-4358-9338-eb4be6f5e70a"><ac:parameter ac:name="id">1258309423</ac:parameter><ac:rich-text-body><h3>Introduction</h3><p>The SysML active validation suites enable you to see if a model is correct and complete immediately. It instantly displays any errors in the model and suggests appropriate solutions. The active validation suites have «activeValidationSuite» stereotype applied.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="66f99b95-6f83-4d42-a19c-262b473a3e29"><ac:rich-text-body><p>Each profile contains its own active validation suites. You can <ac:link><ri:page ri:content-title="Creating validation suites" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[create your own validation suites]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p>You can meet the following active validation suites in the <ac:link><ri:page ri:content-title="Validation dialog" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Validation</strong> dialog</ac:link-body></ac:link> or <ac:link><ri:page ri:content-title="Validation Suites dialog" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Validation Suites</strong> dialog</ac:link-body></ac:link>:</p><ul><li><strong>SysML_activeValSuite - Activities</strong> contains SysML constraints on the following elements: Discrete and noBuffer.</li><li><strong>SysML_activeValSuite - Blocks</strong> contains SysML constraints on the following elements: Binding Connector, Block, Distributed Property and Value Type.</li><li><strong>SysML_activeValSuite - Constraint Blocks</strong> contains SysML constraints on the following elements: Constraint Block and Constraint Property.</li><li><strong>SysML_activeValSuite - Non-normative Extensions</strong> contains SysML constraints on the following elements: nonStreaming, Streaming, Design Constraint, Functional Requirement, Interface Requirement and Performance Requirement.</li><li><strong>SysML_activeValSuite - Port and Flows</strong> contains SysML constraints on the following elements: Flow Port, Flow Property, Flow Specification and Item Flow.</li><li><strong>SysML_activeValSuite - Requirements</strong> contains SysML constraints on the following elements: Copy, Requirement and Test Case.</li></ul><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="08726141-dc44-4a52-8237-ef0a134c00c2"><ac:rich-text-body><p>You can find active validation suites in the <ac:link><ri:page ri:content-title="Containment tab" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link> when the <strong>Show Auxiliary Resources</strong> option is enabled, expand the <em>MD Customization for SysML</em> Package&gt; <em>SysML constraints</em> Package &gt; <em>SysML activeValSuite</em> package.  The <em><em>SysML activeValSuite</em></em> Package is divided into separate Packages and contain an appropriate <ac:link><ri:page ri:content-title="SysML validation rules" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[validation rules]]></ac:plain-text-link-body></ac:link>.</p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="77071334-84fe-41be-878b-c98b2236396f"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Metaclass" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><h3>Validating a project with active validation suites</h3><p>To manually validate project with active validation suites, you can select the specific<strong> Active ValSuite</strong> (mentioned above) as the <strong>Validation Suite</strong> in the <ac:link><ri:page ri:content-title="Validation dialog" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Validation</strong> dialog</ac:link-body></ac:link>. <span class="confluence-link"><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+validation+suites#SysMLvalidationsuites-startStartingthevalidation">How to start the validation &gt;&gt;</a></span></p><p><span class="confluence-link"><br /></span></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="7251f3a1-1884-46bb-8ef1-71aff53694c4"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Active validation suites" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cffb5ed7-af16-4102-bf28-58e0ea36a64d"><ac:parameter ac:name="id">1258309419</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="with-breadcrumbs"><a href="https://docs.nomagic.com/display/MD2024xR3/Predefined+validation+suites">MagicDraw predefined validation suites</a></li><li class="with-breadcrumbs"><a href="https://docs.nomagic.com/display/MD2024xR3/Active+validation+suites">MagicDraw active validation suites</a></li><li class="with-breadcrumbs"><p><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+validation+suites">SysML validation suites</a></p></li><li class="with-breadcrumbs"><p><a href="https://docs.nomagic.com/display/CRMP2024xR3/Requirements+validation+suites" rel="nofollow">Requirements validation suites</a></p></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159659 space=SYSMLP2024xR3 version=1 -->
## PAGE 00342: SysML Activity Diagram

- page_id: `227159659`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159659/SysML+Activity+Diagram
- version_number: 1
- version_date: `2019-06-18T13:53:57.570+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

949321384

949321396

949321386

Activity diagram describes control, input, and output flows among actions. It represents the system business and operational work flows. It captures actions and display their results. It is typically used for business process modeling and used in situations where all or most of the events represent the completion of internally generated actions.

Though Activity diagrams are often classified alongside interaction diagrams, they actually focus on the flows driven by internal processes (as opposed to external events).

SysML extends control in Activity diagrams and provides extensions that might be very loosely grouped under the term “continuous”, but are generally applicable to any distributed flow of information and physical items through a system. It also introduces probability concepts to activities.

[IMAGE alt='' src='']

949321383

**Related pages**

- [CONFLUENCE_PAGE title='Accept Change Structural Feature Event Action' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Change Structural Feature Event' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Invocation on Nested Port Action' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Trigger on Nested Port' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Allocation Mode' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d2878175-78ce-412d-8a46-91903ee6591a"><ac:parameter ac:name="id">949321384</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4570d330-5169-4078-906a-011801293de7"><ac:parameter ac:name="id">949321396</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f04cbd9d-46e0-46f4-803c-7d027a0dca9b"><ac:parameter ac:name="id">949321386</ac:parameter><ac:rich-text-body><p>Activity diagram describes control, input, and output flows among actions. It represents the system business and operational work flows. It captures actions and display their results. It is typically used for business process modeling and used in situations where all or most of the events represent the completion of internally generated actions.</p><p>Though Activity diagrams are often classified alongside interaction diagrams, they actually focus on the flows driven by internal processes (as opposed to external events).</p><p>SysML extends control in Activity diagrams and provides extensions that might be very loosely grouped under the term “continuous”, but are generally applicable to any distributed flow of information and physical items through a system. It also introduces probability concepts to activities.</p><p><ac:image ac:title="Activity Diagram" ac:alt="Activity Diagram"><ri:attachment ri:filename="activity_diagram.png"><ri:page ri:content-title="SysML Activity Diagram" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p> </p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bb822155-9699-4a06-89a1-0d39552d813f"><ac:parameter ac:name="id">949321383</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Accept Change Structural Feature Event Action" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Change Structural Feature Event" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Invocation on Nested Port Action" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Trigger on Nested Port" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Allocation Mode" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159677 space=SYSMLP2024xR3 version=3 -->
## PAGE 00343: SysML Allocation Matrix

- page_id: `227159677`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159677/SysML+Allocation+Matrix
- version_number: 3
- version_date: `2025-05-02T10:28:40.642+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions > Matrices
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: How to work with SysML Allocation matrices

1108000467

#### CONTENT-COLUMN: How to work with SysML Allocation matrices

1108000470

#### CONTENT-BLOCK: How to work with SysML Allocation matrices

1108000469

INLINE

The SysML Allocation matrix enables you to analyze, create, and modify Allocate relationships. Rows in the matrix represent an element that can be the client element of the Allocate relationship. Columns in the matrix represent elements that can be the supplier elements of the Allocate relationship. You can set your own element types that you want to allocate in the criteria area or you can create a matrix with predefined element types in the criteria area by selecting one of the [CONFLUENCE_PAGE title='Allocation Mode' space='SYSMLP2024xR3']

The example below is created by using the[distiller model.mdzip](https://docs.nomagic.com/download/attachments/9919520/distiller%20model.mdzip?version=1&modificationDate=1505483436734&api=v2)sample model that comes only with[SysML Plugin](https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Plugin+Documentation).

[IMAGE alt='' src='']

###### SysML Allocation Matrix.

#### INFO: How to work with SysML Allocation matrices

How to work with SysML Allocation matrices

The SysML Allocation matrices are based on [CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024xR3']. Thus, all its procedures are allowable for SysML Allocation matrices:

[CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024xR3']

904975009

**Related pages**

- [CONFLUENCE_PAGE title='Allocation Mode' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="467c910b-f0ec-4b51-b192-528e051a706b"><ac:parameter ac:name="id">1108000467</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="60ba25b8-9a35-478f-9451-84c59ee26cf7"><ac:parameter ac:name="id">1108000470</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b55a2623-034d-457a-9367-d8e8a0ab36b9"><ac:parameter ac:name="id">1108000469</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="7eb5bc1e-0409-4ad9-881e-1d25a0aedafe"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>The SysML Allocation matrix enables you to analyze, create, and modify Allocate relationships. Rows in the matrix represent an element that can be the client element of the Allocate relationship. Columns in the matrix represent elements that can be the supplier elements of the Allocate relationship. You can set your own element types that you want to allocate in the criteria area or  you can create a matrix with predefined element types in the criteria area by selecting one of the <ac:link><ri:page ri:content-title="Allocation Mode" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Allocation Matrix mode.]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(62,63,64);">The example below is created by using the </span><a href="https://docs.nomagic.com/download/attachments/9919520/distiller%20model.mdzip?version=1&amp;modificationDate=1505483436734&amp;api=v2">distiller model.mdzip</a><span style="color: rgb(62,63,64);"> sample model that comes only with </span><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+Plugin+Documentation">SysML Plugin</a><span style="color: rgb(62,63,64);">.</span></p><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center"><ri:attachment ri:filename="allocation_matrix.png"><ri:page ri:content-title="SysML Allocation Matrix" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">SysML Allocation Matrix.<br /></span></h6><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="0ef6d205-79ee-4dba-a735-2651c6ab3f41"><ac:parameter ac:name="title">How to work with SysML Allocation matrices</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><span style="color: rgb(62,63,64);">The SysML Allocation matrices</span> are based on <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Dependency Matrix" /></ac:link>. Thus, all its procedures are allowable for <span style="color: rgb(62,63,64);">SysML Allocation matrices</span>:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a63dcf01-1278-4a55-8c5d-b15c372a4f53"><ac:parameter ac:name="page"><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Dependency Matrix" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="07ddd4f9-4fae-401d-b1ed-8c97635617d6"><ac:parameter ac:name="id">904975009</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Allocation Mode" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159649 space=SYSMLP2024xR3 version=1 -->
## PAGE 00344: SysML Block Definition Diagram

- page_id: `227159649`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159649/SysML+Block+Definition+Diagram
- version_number: 1
- version_date: `2017-05-29T11:32:09.814+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

Block Definition Diagram defines the features of a block and any relationships between blocks such as associations, generalizations, and dependencies, in terms of properties, operations, and relationships (for example, a system hierarchy or a system classification tree).

Block Definition Diagrams are based on UML class diagrams and include restrictions and extensions as defined by SysML. They are generally used to display systems of blocks or show a system dictionary and/or extensions.

[IMAGE alt='' src='']

#### PANEL: Related pages

Related pages

#### PANEL: Related elements

Related elements

- [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Domain' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='External' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='System' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Subsystem' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='System Context' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Interface Block' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Flow Specification' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Value Type' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Quantity Kind' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Block Definition Diagram defines the features of a block and any relationships between blocks such as associations, generalizations, and dependencies, in terms of properties, operations, and relationships (for example, a system hierarchy or a system classification tree).</p><p>Block Definition Diagrams are based on UML class diagrams and include restrictions and extensions as defined by SysML. They are generally used to display systems of blocks or show a system dictionary and/or extensions.</p><p><ac:image ac:title="SysML Block Definition Diagram" ac:alt="SysML Block Definition Diagram"><ri:attachment ri:filename="block_definition_diagram.png"><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p> </p></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f111b3b2-73a4-4d21-87f7-c7896e912432"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="efa305dd-a8d9-4524-8b1f-0d9667bc2aed" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="b2895cbd-b00c-4420-9d2e-37f8cecce054"><ac:parameter ac:name="title">Related elements</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Domain" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="External" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="System" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Subsystem" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="System Context" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Interface Block" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Flow Specification" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Value Type" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Quantity Kind" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159330 space=SYSMLP2024xR3 version=2 -->
## PAGE 00345: SysML Callout Style

- page_id: `227159330`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159330/SysML+Callout+Style
- version_number: 2
- version_date: `2025-05-02T10:28:34.547+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Working with model elements
- labels: []

### NORMALIZED CONTENT

SysML Callout Style is applied for tagged values by default in Compartment area of the:

- [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3']Part Property
- [CONFLUENCE_PAGE title='Action' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Note' space='MD2024xR3']Note

[IMAGE alt='' src='']

To return the non-standard style

1. Open Symbol Properties dialog.
2. Set the Apply SysML Callout Style property value to false.

To hide the element type before its name

1. Open Symbol Properties dialog.
2. Set the Show SysML Element Type property value to false .

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>SysML Callout Style is applied for tagged values by default in Compartment area of the:</p><ul><li><ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement" ri:space-key="SYSMLP2024xR3" /></ac:link><span class="confluence-link"> </span></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">Part</span> Property</ac:link-body></ac:link></span></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Action" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Note" /><ac:link-body>Note<span> </span></ac:link-body></ac:link></li></ul><p><ac:image ac:title="SysML Callout style" ac:alt="SysML Callout style"><ri:attachment ri:filename="sysml_callout_style.png"><ri:page ri:content-title="SysML Callout Style" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p>To return the non-standard style</p><hr /><ol><li>Open <strong>Symbol Properties</strong> dialog.</li><li>Set the<strong> Apply SysML Callout Style</strong> property value to <em>false.</em></li></ol><p> </p><p>To hide the element type before its name</p><hr /><ol><li>Open <strong>Symbol Properties</strong> dialog.</li><li>Set the <strong>Show SysML Element Type </strong>property value to <em>false</em>.</li></ol><p><ac:image ac:title="SysML Callout Style property" ac:alt="SysML Callout Style property"><ri:attachment ri:filename="callout_style_property.png"><ri:page ri:content-title="SysML Callout Style" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227160366 space=SYSMLP2024xR3 version=1 -->
## PAGE 00346: SysML Default values and instance specifications

- page_id: `227160366`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160366/SysML+Default+values+and+instance+specifications
- version_number: 1
- version_date: `2020-07-01T03:25:20.072+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Sample models > Electric Circuit sample
- labels: []

### NORMALIZED CONTENT

Default values in the form of instance specifications*cap*,*r1*, *r2*, src and*ind* are assigned to the part properties *c:Capacitor*, *ri:Resistor*, *rc:Resistor*, *s:Source* and *i:Inductor*in the *Circuit*internal block diagram, respectively. These instance specifications *cap*,*r1*, *r2*, *src* and *ind* are assigned the values *0.01 Farads*, *20 Ohms*, *10 Ohms*,*10.0 Henries*, *220.0 Ampere* and *0.1 l* respectively. These values stay the same across each simulation run, but changes can be made by tweaking the stored values in the model’s instance specifications.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Default values in the form of instance specifications<em> cap</em>,<em> r1</em>, <em>r2</em>, src and<em> ind</em> are assigned to the part properties <em>c:Capacitor</em>, <em>ri:Resistor</em>, <em>rc:Resistor</em>, <em>s:Source</em> and  <em>i:Inductor  </em>in the <em>Circuit </em>internal block diagram, respectively. These instance specifications <em>cap</em>,<em> r1</em>, <em>r2</em>, <em>src</em> and <em>ind</em> are assigned the values <em>0.01 Farads</em>, <em>20 Ohms</em>, <em>10 Ohms</em>,<em>10.0 Henries</em>, <em>220.0 Ampere</em> and <em>0.1 l</em> respectively. These values stay the same across each simulation run, but changes can be made by tweaking the stored values in the model’s instance specifications.</p><p><ac:image><ri:attachment ri:filename="containtment_tree_circuit_model.png"><ri:page ri:content-title="SysML Default values and instance specifications" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p>
````

<!--NOMAGIC_PAGE id=227159651 space=SYSMLP2024xR3 version=1 -->
## PAGE 00347: SysML Internal Block Diagram

- page_id: `227159651`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159651/SysML+Internal+Block+Diagram
- version_number: 1
- version_date: `2017-05-29T11:17:30.805+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

Internal Block Diagram is based on UML composite structure diagram and includes restrictions and extensions as defined by SysML. An Internal Block Diagram captures the internal structure of a Block in terms of properties and connections among properties. A Block includes properties so that its values, parts, and references to other blocks can be specified. However, whereas an Internal Block Diagram created for a Block (as an inner element) will only display the inner elements of a classifier (parts, ports, and connectors), an Internal Block Diagram created for a package will display additional elements (shapes, notes, and comments).

All properties and connectors that appear inside an Internal Block Diagram belong to (are owned by) a Block whose name is written in the diagram heading. That particular Block is the context of the diagram. SysML allows any property (part) to be shown in an Internal Block Diagram to display compartments within the property (or part) symbol.

[IMAGE alt='' src='']

#### SCROLL-IGNORE: Related pages

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Enforce Ports Compatibility mode' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Property path notation' space='SYSMLP2024xR3']

#### PANEL: Related elements

Related elements

- [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Reference Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3']Value Property
- [CONFLUENCE_PAGE title='Constraint Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Flow Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Participant Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Full Port' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Proxy Port' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Participant Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Bound Reference' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Distributed Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Directed Feature' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Internal Block Diagram is based on UML composite structure diagram and includes restrictions and extensions as defined by SysML. An Internal Block Diagram captures the internal structure of a Block in terms of properties and connections among properties. A Block includes properties so that its values, parts, and references to other blocks can be specified. However, whereas an Internal Block Diagram created for a Block (as an inner element) will only display the inner elements of a classifier (parts, ports, and connectors), an Internal Block Diagram created for a package will display additional elements (shapes, notes, and comments).</p><p>All properties and connectors that appear inside an Internal Block Diagram belong to (are owned by) a Block whose name is written in the diagram heading. That particular Block is the context of the diagram. SysML allows any property (part) to be shown in an Internal Block Diagram to display compartments within the property (or part) symbol.</p><p><ac:image ac:title="Internal Block Diagram" ac:alt="Internal Block Diagram"><ri:attachment ri:filename="internal_block_diagram.png"><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="scroll-ignore" ac:schema-version="1" ac:macro-id="b2079c86-cb6f-495c-87af-2c978ffe242e"><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="8c808880-1861-4041-92da-bc6a543bcbb2"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="648fb2dd-d219-4971-8aac-e6bca46a5f64" /></p><ul><li><ac:link><ri:page ri:content-title="Enforce Ports Compatibility mode" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="4a7a5654-b241-4d28-8679-5cfd5ed50515"><ac:parameter ac:name="title">Related elements</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Reference Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">Value Property</span> </ac:link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Constraint Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Flow Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Participant Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Flow Port]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Full Port" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Proxy Port" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Participant Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Bound Reference" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Distributed Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Directed Feature" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158738 space=SYSMLP2024xR3 version=2 -->
## PAGE 00348: SysML Internal Block Diagram context

- page_id: `227158738`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158738/SysML+Internal+Block+Diagram+context
- version_number: 2
- version_date: `2025-05-02T10:28:21.635+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Decomposing Blocks
- labels: []

### NORMALIZED CONTENT

When creating a new [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']SysML Internal Block Diagram for an element which cannot be the context of this diagram (e.g. [CONFLUENCE_PAGE title='Package' space='MD2024xR3']), the new context element (which is a [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']) is created automatically.

[CONFLUENCE_PAGE title='Composite Structure Diagram context' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When creating a new <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="ancestor-link parent-link">SysML Internal Block Diagram</span></ac:link-body></ac:link> for an element which cannot be the context of this diagram (e.g. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Package" /></ac:link>), the new context element (which is a <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>) is created automatically.</p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="3b4be08f-61f2-4e64-8276-66f137cc9f6c"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Composite Structure Diagram context" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159653 space=SYSMLP2024xR3 version=2 -->
## PAGE 00349: SysML Package Diagram

- page_id: `227159653`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159653/SysML+Package+Diagram
- version_number: 2
- version_date: `2025-05-02T10:28:39.674+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

Package diagram typically enables you to organize models by partitioning model elements into packageable elements and establishing dependencies between packages and/or model elements within these packages. Since Package diagram is used to organize models in packages and views, it can include a wide array of packageable elements.

A package is a construct that enables you to organize model elements, such as [CONFLUENCE_PAGE title='Use Case' space='MD2024xR3'] or [CONFLUENCE_PAGE title='Class' space='CM180'], into groups. Packages define namespaces for packageable elements. Model elements from one package can be imported and/or accessed by another package. This organizational principle is intended to help establish unique naming of the model elements and avoid overloading a particular model element's name. Packages can also be shown on [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3'] or [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3'].

[IMAGE alt='' src='']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Working with packages' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Working with dependencies' space='MD2024xR3']

#### PANEL: Related elements

Related elements

- [CONFLUENCE_PAGE title='Package' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Model' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Package import' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Dependency' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Package diagram typically enables you to organize models by partitioning model elements into packageable elements and establishing dependencies between packages and/or model elements within these packages. Since Package diagram is used to organize models in packages and views, it can include a wide array of packageable elements.</p><p>A package is a construct that enables you to organize model elements, such as <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Use Case" /><ac:plain-text-link-body><![CDATA[use cases]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:space-key="CM180" ri:content-title="Class" /><ac:plain-text-link-body><![CDATA[classes]]></ac:plain-text-link-body></ac:link>, into groups. Packages define namespaces for packageable elements. Model elements from one package can be imported and/or accessed by another package. This organizational principle is intended to help establish unique naming of the model elements and avoid overloading a particular model element's name. Packages can also be shown on <ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Block Definition diagrams]]></ac:plain-text-link-body></ac:link> or <ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Requirement diagrams]]></ac:plain-text-link-body></ac:link>.</p><p><span style="color: rgb(255,0,0);"><ac:image><ri:attachment ri:filename="package_diagram.png"><ri:page ri:content-title="SysML Package Diagram" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f678222b-0d74-4d89-9fca-f8b21ad7b906"><ac:parameter ac:name="title">Related pages</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with packages" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with dependencies" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="72f0792b-b7a7-44c0-a19c-276f7efaeff3"><ac:parameter ac:name="title">Related elements</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Package" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Model" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Package import" /><ac:plain-text-link-body><![CDATA[Package Import]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Dependency" /><ac:plain-text-link-body><![CDATA[Element Import]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159655 space=SYSMLP2024xR3 version=1 -->
## PAGE 00350: SysML Parametric Diagram

- page_id: `227159655`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159655/SysML+Parametric+Diagram
- version_number: 1
- version_date: `2018-04-03T14:14:46.186+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

36056666

36056669

36056667

SysML Parametric diagramParametric diagram

Parametric diagram is designed to describe mathematical equations by modeling elements, e.g. to count breaking distance of a vehicle.

Parametric diagram can be defined as restricted forms of [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']. They are similar to [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']Internal Block diagrams except that the only connectors allowed are [CONFLUENCE_PAGE title='Binding Connector' space='SYSMLP2024xR3'], each having at least one end connected to a [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3']Constraint Parameter.

A Parametric diagram includes the usage of a [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'] to constrain the properties of another Block. It contains [CONFLUENCE_PAGE title='Constraint Property' space='SYSMLP2024xR3'] and constraint parameters as well as other properties from within that internal block context. All properties displayed, other than the constraints themselves, must either be bound directly to a Constraint Parameter or contain a property that is bound to a Constraint Parameter (through any number of containment levels). A Constraint Block generally contain many constraints, each of them containing many Constraint Parameters.

Constrained Properties typically have simple value types that can also carry units, quantity kinds, and probability distributions. This allows for a [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] that may be deeply nested within a containing hierarchy to be referenced at the outer containing level. The context for the usages of [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'] must also be specified in a parametric diagram to maintain the proper namespaces for the nested properties.

The state of the system can be specified in terms of the values of some of its properties. A change in state will result in a different set of constraint equations to be recalculated. This can be accommodated by specifying constraints that are conditioned on the value of the property with state. Parametric diagrams can be used to support trade-off analysis. A Constraint Block can define an objective function to compare alternative solutions.

[IMAGE alt='' src='']

36056664

**Related pages**

- [CONFLUENCE_PAGE title='Enforce Ports Compatibility mode' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Property path notation' space='SYSMLP2024xR3']

**Related elements**

- [CONFLUENCE_PAGE title='Constraint Property' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Moe' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Objective Function' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Constraint Parameter' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Binding Connector' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b5aca075-9f96-4749-b8f3-046eda2996a1"><ac:parameter ac:name="id">36056666</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="54a96455-23eb-484c-b81d-9eb7498435f7"><ac:parameter ac:name="id">36056669</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="aba861e2-2134-4d96-ab11-7c1963110805"><ac:parameter ac:name="id">36056667</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="scroll-indexterm" ac:schema-version="1" ac:macro-id="a71f9c14-2a8c-4544-ac87-c7970332df5c"><ac:parameter ac:name="secondary">SysML Parametric diagram</ac:parameter><ac:parameter ac:name="primary">Parametric diagram</ac:parameter></ac:structured-macro></p><p>Parametric diagram is designed to describe mathematical equations by modeling elements, e.g. to count breaking distance of a vehicle.</p><p>Parametric diagram can be defined as restricted forms of <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Internal Block diagrams]]></ac:plain-text-link-body></ac:link>. They are similar to <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">Internal Block diagrams</span></ac:link-body></ac:link><span class="confluence-link"> </span> except that the only connectors allowed are <ac:link><ri:page ri:content-title="Binding Connector" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Binding Connectors]]></ac:plain-text-link-body></ac:link>, each having at least one end connected to a <ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /><ac:link-body>C<span class="confluence-link">onstraint Parameter</span></ac:link-body></ac:link>.</p><p>A Parametric diagram includes the usage of a <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link> to constrain the properties of another Block. It contains <ac:link><ri:page ri:content-title="Constraint Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Constraint Properties]]></ac:plain-text-link-body></ac:link> and constraint parameters as well as other properties from within that internal block context. All properties displayed, other than the constraints themselves, must either be bound directly to a Constraint Parameter or contain a property that is bound to a Constraint Parameter (through any number of containment levels). A Constraint Block generally contain many constraints, each of them containing many Constraint Parameters.</p><p>Constrained Properties typically have simple value types that can also carry units, quantity kinds, and probability distributions. This allows for a <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> that may be deeply nested within a containing hierarchy to be referenced at the outer containing level. The context for the usages of <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Constraint Blocks]]></ac:plain-text-link-body></ac:link> must also be specified in a parametric diagram to maintain the proper namespaces for the nested properties.</p><p>The state of the system can be specified in terms of the values of some of its properties. A change in state will result in a different set of constraint equations to be recalculated. This can be accommodated by specifying constraints that are conditioned on the value of the property with state. Parametric diagrams can be used to support trade-off analysis. A Constraint Block can define an objective function to compare alternative solutions.</p><p><ac:image ac:title="Parametric Diagram" ac:alt="Parametric Diagram"><ri:attachment ri:filename="parametric_diagram.png"><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cd6daee6-34dd-4eaa-879f-378530484ecc"><ac:parameter ac:name="id">36056664</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Enforce Ports Compatibility mode" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong>Related elements</strong></p><ul><li><ac:link><ri:page ri:content-title="Constraint Property" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Moe" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Objective Function" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Constraint Parameter" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Binding Connector" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159034 space=SYSMLP2024xR3 version=2 -->
## PAGE 00351: SysML Parametric Diagram context

- page_id: `227159034`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159034/SysML+Parametric+Diagram+context
- version_number: 2
- version_date: `2025-05-02T10:28:27.445+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling parametric constraints
- labels: []

### NORMALIZED CONTENT

When creating a new [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3']SysML Parametric Diagram for an element which cannot be the context of this diagram (e.g. [CONFLUENCE_PAGE title='Package' space='MD2024xR3']), the new context element (which is a [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']) is created automatically.

[CONFLUENCE_PAGE title='Composite Structure Diagram context' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>When creating a new <ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="ancestor-link parent-link">SysML Parametric Diagram</span></ac:link-body></ac:link> for an element which cannot be the context of this diagram (e.g. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Package" /></ac:link>), the new context element (which is a <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>) is created automatically.</p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="f48c24b7-ff75-44b8-bcba-b6d5430efdbf"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Composite Structure Diagram context" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227158477 space=SYSMLP2024xR3 version=4 -->
## PAGE 00352: SysML Plugin Documentation

- page_id: `227158477`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158477/SysML+Plugin+Documentation
- version_number: 4
- version_date: `2026-05-06T10:05:07.090+02:00`
- ancestors: 
- labels: ['sysml-modeling-language']

### NORMALIZED CONTENT

The Systems Modeling Language (SysML) is designed to unify the diverse modeling languages currently used by system engineers, the same way Unified Modeling Language (UML) is used in the software industry to unify the modeling languages used by software engineers. SysML supports the specifications, analysis, designs, verifications, and validations of a broad range of complex systems.

In addition to supporting all SysML diagrams (Block Definition, Internal Block, Package, Parametric, Requirements, Activity, and Use Case diagrams), SysML Plugin also makes it possible for MagicDraw to support additional specifications, analysis, designs, and validations on a broader range of systems and system integrations.

The SysML Plugin documentation consists of the following sections:

**Documentation of earlier versions**

- 
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR2']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR1']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024x']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2022xR1']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2022x']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2021xR2']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2021xR1']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2021x']
- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP190SP4']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The Systems Modeling Language (SysML) is designed to unify the diverse modeling languages currently used by system engineers, the same way Unified Modeling Language (UML) is used in the software industry to unify the modeling languages used by software engineers. SysML supports the specifications, analysis, designs, verifications, and validations of a broad range of complex systems.</p><p>In addition to supporting all SysML diagrams (Block Definition, Internal Block, Package, Parametric, Requirements, Activity, and Use Case diagrams), SysML Plugin also makes it possible for MagicDraw to support additional specifications, analysis, designs, and validations on a broader range of systems and system integrations.</p><p>The SysML Plugin documentation consists of the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b84e43e6-dc2c-4979-a5f4-84c3b3818ca9" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Documentation of earlier versions</strong></p><ul><li data-uuid="f85d7536-f9c2-49b0-935c-7d28afab1cc3"><ac:link><ac:plain-text-link-body><![CDATA[SysML Plugin 2024x Refresh3]]></ac:plain-text-link-body></ac:link></li><li data-uuid="ca1b133b-6c43-4fb6-8b1f-8d350011e4b5"><ac:link><ri:page ri:space-key="SYSMLP2024xR2" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2024x Refresh2]]></ac:plain-text-link-body></ac:link></li><li data-uuid="9ac8f308-9294-4b15-b541-320a70c3434b"><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2024x Refresh1]]></ac:plain-text-link-body></ac:link></li><li data-uuid="6fd02fd9-9f5f-4b9d-949a-d258e22e198c"><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2024x]]></ac:plain-text-link-body></ac:link></li><li data-uuid="654e6ddf-8547-49df-a319-120181f5ef79"><ac:link><ri:page ri:space-key="SYSMLP2022xR1" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2022x Refresh1]]></ac:plain-text-link-body></ac:link></li><li data-uuid="3c26bf93-975d-445a-aa5d-87b34e60c0e0"><ac:link><ri:page ri:space-key="SYSMLP2022x" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2022x]]></ac:plain-text-link-body></ac:link></li><li data-uuid="b9cf9c60-608a-4bb5-9675-d6ec6e26df48"><ac:link><ri:page ri:space-key="SYSMLP2021xR2" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2021x Refresh2]]></ac:plain-text-link-body></ac:link></li><li data-uuid="ac921a90-5961-49ee-baca-3044904af48e"><ac:link><ri:page ri:space-key="SYSMLP2021xR1" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2021x Refresh1]]></ac:plain-text-link-body></ac:link></li><li data-uuid="6384121a-532d-4ab7-b876-64cd19e78ee1"><ac:link><ri:page ri:space-key="SYSMLP2021x" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 2021x]]></ac:plain-text-link-body></ac:link></li><li data-uuid="3e02e904-267b-4015-a1d5-b4a3138b0b06"><ac:link><ri:page ri:space-key="SYSMLP190SP4" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin 19.0 SP4]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159657 space=SYSMLP2024xR3 version=2 -->
## PAGE 00353: SysML Sequence Diagram

- page_id: `227159657`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159657/SysML+Sequence+Diagram
- version_number: 2
- version_date: `2025-05-02T10:28:39.995+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

This diagram is similar to UML [CONFLUENCE_PAGE title='Sequence diagram' space='MD2024xR3'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This diagram is similar to UML <ac:link><ri:page ri:content-title="Sequence diagram" ri:space-key="MD2024xR3" /><ac:plain-text-link-body><![CDATA[Sequence Diagram]]></ac:plain-text-link-body></ac:link>.</p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158832 space=SYSMLP2024xR3 version=2 -->
## PAGE 00354: SysML specific compartments

- page_id: `227158832`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158832/SysML+specific+compartments
- version_number: 2
- version_date: `2025-05-02T10:28:24.145+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks
- labels: []

### NORMALIZED CONTENT

The compartment is an area on or next to the shape used to display component properties. As an example, please see the figure below.

[IMAGE alt='' src='']

###### The *parts*, *values, and proxy ports* compartments are shown on the *Water Heating Element* Block shape.

The Compartment Editor allows you to display compartments and their properties on the [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']:

- constraints
- flow properties
- parts
- properties (formerly :UML properties)
- references
- values
- full ports
- proxy ports
- parameters

The following table explains which elements are displayed on a selected shape to show the additional information.

| SysML specific compartments | Displayed Elements |
| --- | --- |
| constraints | Constraints and Constraint Properties.Constraint Properties: properties typed by Constraint Blocks, or subtypes of Constraint Blocks, always having the ‘composite’ aggregation kind. |
| flow properties | Flow Properties: properties that apply the «FlowProperty» stereotype. |
| parts | Part Properties: properties typed by Blocks or subtypes of Blocks. |
| properties | All other properties that cannot be classified into the previous compartments. |
| references | Shared Properties and Reference Properties: properties typed by Blocks or subtypes of Blocks (except Constraint Block) having ‘shared’ and ‘none’ aggregation kind, respectively. There is no distinction between Shared Property and Reference Property. |
| values | Value Properties: properties typed by Value Types or subtypes of Value Types, always having the ‘composite’ aggregation kind. |
| full ports | The port is stereotyped by FullPort. |
| proxy ports | The port stereotyped by ProxyPort. |
| parameters | Constraint Parameters. |

The following sections outline the main procedures for working with the compartment area:

43

##### Creating elements in compartments

[CONFLUENCE_PAGE title='Creating elements in compartments on shapes' space='MD2024xR3']

##### Displaying and suppressing compartments

[CONFLUENCE_PAGE title='Displaying and suppressing compartments on shapes' space='MD2024xR3']

##### Customizing compartments

[CONFLUENCE_PAGE title='Displaying or hiding elements in compartments on shapes' space='MD2024xR3']

For example, the following procedure shows how to customize the compartments of a part.

To customize a compartment of a Part Property

1. Right-click a Part Property shape and from the shortcut menu, select the Edit Compartment button.
2. In the Compartment Edit dialog, select a compartment tab which you want to customize.
3. Double-click an element or use the arrow buttons to move an element from the Hidden to the Selected area to display the element.
4. Click OK when done.

###### [IMAGE alt='' src='']

###### The air and is properties are displayed on the r part shape by using the Compartment Edit dialog. The image is from the TemperatureRegulationLoop.mdzip sample model. Find it in modeling tool <modeling tool installation directory>\samples\SysML.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The compartment is an area on or next to the shape used to display component properties. As an example, please see the figure below.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="sysml_compartments.png"><ri:page ri:content-title="SysML specific compartments" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The <em>parts</em>, <em>values, and proxy ports</em> compartments are shown on the <em>Water Heating Element</em> Block shape.</h6><p><br /></p><p>The Compartment Editor allows you to display compartments and their properties on the <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>:</p><ul><li>constraints</li><li>flow properties</li><li>parts</li><li>properties (formerly :UML properties)</li><li>references</li><li>values</li><li>full ports</li><li>proxy ports</li><li>parameters</li></ul><p style="text-align: left;">The following table explains which elements are displayed on a selected shape to show the additional information.</p><table class="relative-table wrapped" style="width: 81.7965%;"><colgroup><col style="width: 22.4514%;" /><col style="width: 77.5097%;" /></colgroup><tbody><tr><th><p>SysML specific compartments</p></th><th>Displayed Elements</th></tr><tr><td>constraints</td><td><p>Constraints and Constraint Properties.</p><p>Constraint Properties: properties typed by Constraint Blocks, or subtypes of Constraint Blocks, always having the ‘composite’ aggregation kind.</p></td></tr><tr><td>flow properties</td><td>Flow Properties: properties that apply the «FlowProperty» stereotype.</td></tr><tr><td>parts</td><td>Part Properties: properties typed by Blocks or subtypes of Blocks.</td></tr><tr><td>properties</td><td><p>All other properties that cannot be classified into the previous compartments.</p></td></tr><tr><td>references</td><td><p>Shared Properties and Reference Properties: properties typed by Blocks or subtypes of Blocks (except Constraint Block) having ‘shared’ and ‘none’ aggregation kind, respectively. There is no distinction between Shared Property and Reference Property.</p></td></tr><tr><td>values</td><td><p>Value Properties: properties typed by Value Types or subtypes of Value Types, always having the ‘composite’ aggregation kind.</p></td></tr><tr><td colspan="1">full ports</td><td colspan="1"><p>The port is stereotyped by FullPort.</p></td></tr><tr><td colspan="1">proxy ports</td><td colspan="1"><p>The port stereotyped by ProxyPort.</p></td></tr><tr><td colspan="1">parameters</td><td colspan="1">Constraint Parameters.</td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target">The following sections outline the main procedures for working with the compartment area:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="41edf426-5be9-4cbf-8fd7-b714409754e0"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><h3 class="with-breadcrumbs">Creating elements in compartments</h3><p class="with-breadcrumbs"><br /></p><p class="with-breadcrumbs"><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="d7309cf2-66f9-4e91-b2da-f7071115f078"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating elements in compartments on shapes" /></ac:link></ac:parameter></ac:structured-macro></p><h3 class="with-breadcrumbs">Displaying and suppressing compartments</h3><p><br /></p><p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="b76e3398-d5d8-4109-a488-5c12f654469d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Displaying and suppressing compartments on shapes" /></ac:link></ac:parameter></ac:structured-macro></p><h3 class="with-breadcrumbs">Customizing compartments</h3><p><br /></p><p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="e3ace979-c592-478a-8a86-041cb96140a3"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Displaying or hiding elements in compartments on shapes" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p><p>For example, the following procedure shows how to customize the compartments of a part.</p><p><br /></p><p>To customize a compartment of a Part Property</p><hr /><ol><li>Right-click a Part Property shape and from the shortcut menu, select the <strong>Edit Compartment</strong> button.</li><li>In the <strong>Compartment Edit</strong> dialog, select a compartment tab which you want to customize.</li><li>Double-click an element or use the arrow buttons to move an element from the <strong>Hidden</strong> to the <strong>Selected</strong> area to display the element.</li><li>Click <strong>OK</strong> when done.</li></ol><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="edit_compartments_part.png"><ri:page ri:content-title="SysML specific compartments" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></h6><h6 style="text-align: center;">The air and is properties are displayed on the r part shape by using the Compartment Edit dialog. The image is from the TemperatureRegulationLoop.mdzip sample model. Find it in modeling tool &lt;modeling tool installation directory&gt;\samples\SysML.</h6>
````

<!--NOMAGIC_PAGE id=227159658 space=SYSMLP2024xR3 version=2 -->
## PAGE 00355: SysML State Machine Diagram

- page_id: `227159658`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159658/SysML+State+Machine+Diagram
- version_number: 2
- version_date: `2025-05-02T10:28:40.163+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

This diagram is similar to UML [CONFLUENCE_PAGE title='State Machine diagram' space='MD2024xR3'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This diagram is similar to UML <ac:link><ri:page ri:content-title="State Machine diagram" ri:space-key="MD2024xR3" /><ac:plain-text-link-body><![CDATA[State Machine Diagram]]></ac:plain-text-link-body></ac:link>.<span> </span></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227160101 space=SYSMLP2024xR3 version=1 -->
## PAGE 00356: SysML supported and unsupported concepts

- page_id: `227160101`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160101/SysML+supported+and+unsupported+concepts
- version_number: 1
- version_date: `2021-02-11T09:20:19.105+01:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Simulink export
- labels: []

### NORMALIZED CONTENT

1401802970

1401802981

1401802959

**On this page**

1401802980

##### **Supported SysML concepts**

The main (selected root owning Block) is exported into a separate *.slx file with a Block name.

All other used or referenced Blocks are exported as one library *.slx file.

- Blocks which have classifier behavior as statemachine are exported as Stateflow blocks.
- Blocks which behavior is described by Parametric equations are exported as SFunctions or Simscape models.
- If blocks have bidirectional (inout) ports, Simscape should be selected as export option, as Simulink only supports unidirectional inports and outports.
- Both flow ports and proxy ports are supported if they represent one primitive flow type (typed by Real, Integer, Boolean, or one of their specializations).
- Connector must link ports, can’t be attached directly to the part.
- Ports must be typed.
- Proxy port/Interface block with more than 1 flow property (composite signals or buses)
- InstanceSpecifications can be used to define or overwrite initial parameter values.

##### **Not supported SysML concepts**

- Behaviors defined as Activity diagrams or Interactions (Sequence diagrams)
- Mixing of Parametrics and StateMachine in one Block
- Enumerations
- Multiplicities

More constraints and examples can be found in SysPhS specification document. Click [here](https://www.omg.org/spec/SysPhS/1.0/PDF) to access it.

**Diagram layout**

Shape and path positions in IBD and Statemachine diagrams are exported, however result is not exactly the same sometimes and can be changed or distorted on the Simulink side.

Note that Simulink only allows input ports on the left, outputs on the right, so adjust your SysML IBD diagrams accordingly to get best visual result and avoid automatic ports and connectors replacements.

- First owned IBD is exported as Simulink block diagram in case of multiple owned IBDs in a Block.
- Nested symbols such as nested parts or ports are not supported
- If there is more than one connector going in or out of same port, Simulink will merge them into one and adds the branching point.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4567fea4-7173-4119-bc28-ecc6f85b969b"><ac:parameter ac:name="id">1401802970</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b0ad88d5-d15b-465a-9518-33d5a5f33781"><ac:parameter ac:name="id">1401802981</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="328dd099-5d3d-4c60-838c-288da51f61bf"><ac:parameter ac:name="id">1401802959</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6f9dbbb2-569f-4834-a227-36e18e6f4317" /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="31cb6976-173d-42ee-a7fe-e1221933dcb2"><ac:parameter ac:name="id">1401802980</ac:parameter><ac:rich-text-body><h3><strong>Supported SysML concepts</strong></h3><p>The main (selected root owning Block) is exported into a separate *.slx file with a Block name.</p><p>All other used or referenced Blocks are exported as one library *.slx file.</p><ul><li>Blocks which have classifier behavior as statemachine are exported as Stateflow blocks.</li><li>Blocks which behavior is described by Parametric equations are exported as SFunctions or Simscape models.</li><li>If blocks have bidirectional (inout) ports, Simscape should be selected as export option, as Simulink only supports unidirectional inports and outports. </li><li>Both flow ports and proxy ports are supported if they represent one primitive flow type (typed by Real, Integer, Boolean, or one of their specializations).</li><li>Connector must link ports, can’t be attached directly to the part.</li><li>Ports must be typed.</li><li>Proxy port/Interface block with more than 1 flow property (composite signals or buses) </li><li>InstanceSpecifications can be used to define or overwrite initial parameter values.</li></ul><h3><strong>Not supported SysML concepts</strong></h3><ul><li>Behaviors defined as Activity diagrams or Interactions (Sequence diagrams)</li><li>Mixing of Parametrics and StateMachine in one Block</li><li>Enumerations</li><li>Multiplicities</li></ul><p>More constraints and examples can be found in SysPhS specification document. Click <a class="external-link" href="https://www.omg.org/spec/SysPhS/1.0/PDF" rel="nofollow">here</a> to access it. </p><p><strong>Diagram layout</strong></p><p>Shape and path positions in IBD and Statemachine diagrams are exported, however result is not exactly the same sometimes and can be changed or distorted on the Simulink side. </p><p>Note that Simulink only allows input ports on the left, outputs on the right, so adjust your SysML IBD diagrams accordingly to get best visual result and avoid automatic ports and connectors replacements.</p><ul><li>First owned IBD is exported as Simulink block diagram in case of multiple owned IBDs in a Block.</li><li>Nested symbols such as nested parts or ports are not supported</li><li>If there is more than one connector going in or out of same port, Simulink will merge them into one and adds the branching point.</li></ul><p /></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159661 space=SYSMLP2024xR3 version=1 -->
## PAGE 00357: SysML Use Case Diagram

- page_id: `227159661`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159661/SysML+Use+Case+Diagram
- version_number: 1
- version_date: `2015-04-17T09:34:41.889+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

The purpose of a Use Case Diagram is to give a graphical overview of the functionalities provided by a system in terms of actors, their goals (represented as use cases), and any dependencies among those use cases.

A Use Case Diagram describes the usage of a system. The associations between actors and use cases represent the communications that occur between the actors and the subjects to accomplish the functionalities associated with the use cases. The subject of a use case can be represented through a system boundary. The use cases enclosed in the system boundary represent the functionalities performed by behaviors (activity diagrams, sequence diagrams, and state machine diagrams).

Actors may interact either directly or indirectly with the system. They are often specialized so as to represent a taxonomy of user types or external systems. The only relationship allowed between actors in a use case diagram is generalization. This is useful in defining overlapping roles between actors. Actors are connected to use cases through communication paths, each represented by a relationship. There are four use case relationships:

- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='SYSMLP2024xR3']

**CommunicationCommunication**

A communication path represents an association between two Deployment Targets. It connects actors to use cases.

**IncludeInclude**

An include relationship provides a mechanism for factoring out a common functionality that is shared among multiple use cases and is always performed as part of the base use case.

**ExtendExtend**

An extend relationship provides an optional functionality, which extends the base use case at defined extension points under specified conditions.

**GeneralizationGeneralization**

A generalization relationship provides a mechanism to specify variants of the base use case.

Use cases are often organized into packages with the corresponding dependencies among the use cases included in the packages.

[IMAGE alt='' src='']

#### PANEL: Related elements

Related elements

- [CONFLUENCE_PAGE title='External System' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Sensor' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Boundary System' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='User System' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Actuator' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Environmental Effect' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The purpose of a Use Case Diagram is to give a graphical overview of the functionalities provided by a system in terms of actors, their goals (represented as use cases), and any dependencies among those use cases.</p><p>A Use Case Diagram describes the usage of a system. The associations between actors and use cases represent the communications that occur between the actors and the subjects to accomplish the functionalities associated with the use cases. The subject of a use case can be represented through a system boundary. The use cases enclosed in the system boundary represent the functionalities performed by behaviors (activity diagrams, sequence diagrams, and state machine diagrams).</p><p>Actors may interact either directly or indirectly with the system. They are often specialized so as to represent a taxonomy of user types or external systems. The only relationship allowed between actors in a use case diagram is generalization. This is useful in defining overlapping roles between actors. Actors are connected to use cases through communication paths, each represented by a relationship. There are four use case relationships:</p><ul><li><ac:link ac:anchor="Communication"><ac:plain-text-link-body><![CDATA[communication]]></ac:plain-text-link-body><ri:page ri:content-title="SysML Use Case Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link ac:anchor="Include"><ac:plain-text-link-body><![CDATA[include ]]></ac:plain-text-link-body><ri:page ri:content-title="SysML Use Case Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link ac:anchor="Extend"><ac:plain-text-link-body><![CDATA[extend]]></ac:plain-text-link-body><ri:page ri:content-title="SysML Use Case Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link ac:anchor="Generalization"><ac:plain-text-link-body><![CDATA[generalization]]></ac:plain-text-link-body><ri:page ri:content-title="SysML Use Case Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><p><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="d86e5889-22dd-4cb4-bb37-0100597a9cce"><ac:parameter ac:name="">Communication</ac:parameter></ac:structured-macro>Communication</strong></p><p>A communication path represents an association between two Deployment Targets. It connects actors to use cases.</p><p><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="66a5368d-af5e-41a6-9a0d-a34eba3e3818"><ac:parameter ac:name="">Include</ac:parameter></ac:structured-macro>Include</strong></p><p>An include relationship provides a mechanism for factoring out a common functionality that is shared among multiple use cases and is always performed as part of the base use case.</p><p><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="592adbde-daec-4a99-a22d-c84cfab98f7d"><ac:parameter ac:name="">Extend</ac:parameter></ac:structured-macro>Extend</strong></p><p>An extend relationship provides an optional functionality, which extends the base use case at defined extension points under specified conditions.</p><p><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="3dbb0bf3-2956-4416-8ad9-7e4771cd8705"><ac:parameter ac:name="">Generalization</ac:parameter></ac:structured-macro>Generalization</strong></p><p>A generalization relationship provides a mechanism to specify variants of the base use case.</p><p> </p><p>Use cases are often organized into packages with the corresponding dependencies among the use cases included in the packages.</p><p><ac:image ac:alt="Use Case Diagram" ac:title="Use Case Diagram"><ri:attachment ri:filename="use_case_diagram.png"><ri:page ri:content-title="SysML Use Case Diagram" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="736847fa-137e-4799-a576-ed654351a06b"><ac:parameter ac:name="title">Related elements</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="External System" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Sensor" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Boundary System" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="User System" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Actuator" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Environmental Effect" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159423 space=SYSMLP2024xR3 version=1 -->
## PAGE 00358: SysML validation rules

- page_id: `227159423`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159423/SysML+validation+rules
- version_number: 1
- version_date: `2022-01-20T12:49:13.578+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation
- labels: []

### NORMALIZED CONTENT

This page contains all SysML constraints implemented in the tool as validation rules. You can find the rules in the validation suite ([CONFLUENCE_PAGE title='SysML validation suites' space='SYSMLP2024xR3']) and active validation suite ([CONFLUENCE_PAGE title='SysML active validation suites' space='SYSMLP2024xR3']) Packages stored under the **Auxiliary Resources** > **MD Customization for SysML** > **SysML constraints**.

The SysML validation suites and active validation suites include the following validation rules:

The list below displays only a few SysML validation rules. The rest are under construction.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This page contains all SysML constraints implemented in the tool as validation rules. You can find the rules in the validation suite (<ac:link><ri:page ri:content-title="SysML validation suites" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML ValSuite]]></ac:plain-text-link-body></ac:link>) and active validation suite (<ac:link><ri:page ri:content-title="SysML active validation suites" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML activeValSuite]]></ac:plain-text-link-body></ac:link>) Packages stored under the <strong>Auxiliary Resources</strong> &gt; <strong>MD Customization for SysML</strong> &gt; <strong>SysML constraints</strong>.</p><p>The SysML validation suites and active validation suites include the following validation rules:</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="733f4481-2f2a-40f1-a1f4-cb11f89284db"><ac:rich-text-body><p>The list below displays only a few SysML validation rules. The rest are under construction.</p></ac:rich-text-body></ac:structured-macro><p><br /><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f0b2b1e4-0a26-4fd4-b6b6-18c0e7620364" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159403 space=SYSMLP2024xR3 version=3 -->
## PAGE 00359: SysML validation suites

- page_id: `227159403`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159403/SysML+validation+suites
- version_number: 3
- version_date: `2025-05-02T10:28:35.102+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation
- labels: []

### NORMALIZED CONTENT

1258397415

1258397417

1258405722

**On this page**

43

1258397416

##### Introduction

You can validate your models against a set of SysML constraints called validation suites. You can use the SysML validation suite that comes with the SysML Plugin to validate SysML projects. You need to perform the validation manually to check your model against the predefined validation suites. The predefined validation suites have «validationSuite» stereotype applied.

Each Profile contains its own validation suites. You can [CONFLUENCE_PAGE title='Creating validation suites' space='SYSMLP2024xR3']create your own validation suites.

You can meet the following SysML validation suites in the [CONFLUENCE_PAGE title='Validation dialog' space='SYSMLP2024xR3']**Validation** dialog or [CONFLUENCE_PAGE title='Validation Suites dialog' space='SYSMLP2024xR3']**Validation Suites** dialog:

- SysML ValSuite - Activities contains SysML constraints on the following elements: Control Operator, Control Value, Discrete, noBuffer, Optional, Probability and Rate.
- SysML ValSuite - Blocks contains SysML constraints on the following elements: Binding Connector, Block, Distributed Property, Part Property, Reference Property, Shared Property, Value Property and Value Type.
- SysML ValSuite - Constraint Blocks contains SysML constraints on the following elements: Constraint Block and Constraint Property.
- SysML ValSuite - Model Elements contains SysML constraints on the following elements: View and Viewpoint.
- SysML ValSuite - Non-normative Extensions contains SysML constraints on the following elements: nonStreaming, Streaming, Design Constraint, Functional Requirement, Interface Requirement and Performance Requirement.
- SysML ValSuite - Port and Flows contains SysML constraints on the following elements: Flow Port, Flow Property, Flow Specification and Item Flow.
- SysML ValSuite - Requirements contains SysML constraints on the following elements: Copy, DeriveReqt, Requirement and Test Case

You can find predefined validation suites in the [CONFLUENCE_PAGE title='Containment tab' space='SYSMLP2024xR3'] when the **Show Auxiliary Resources** option is enabled, expand the *MD Customization for SysML* Package > *SysML constraints* Package > *SysML ValSuite* Package. The *SysML ValSuite* Package is divided into separate Packages and contain an appropriate [CONFLUENCE_PAGE title='SysML validation rules' space='SYSMLP2024xR3'].

[CONFLUENCE_PAGE title='Metaclass' space='MD2024xR3']true

[CONFLUENCE_PAGE title='Starting the validation' space='SYSMLP2024xR3']Learn how to start the validation >>

##### Limiting the scope of the constraints to be validated against

If you select the **SysML ValSuite** as the **Validation Suite** in the [CONFLUENCE_PAGE title='Validation dialog' space='SYSMLP2024xR3']**Validation** dialog, your model is validated against all SysML validation suites at the same time. To limit the scope of the constraints to be validated against, select a more specific validation suite, such as **SysML ValSuite - Blocks**. The model or its part is validated against the selected validation suite. The [CONFLUENCE_PAGE title='Validation Results panel' space='SYSMLP2024xR3']**Validation Results** panel shows the results, listing all elements that do not conform to some constraints in the selected validation suite. These elements are called “invalid” elements and are highlighted.

[CONFLUENCE_PAGE title='Predefined validation suites' space='MD2024xR3']true

1258397413

**Related pages**

- MagicDraw predefined validation suites
- MagicDraw active validation suites
- [SysML active validation suites](https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+active+validation+suites)
- Requirements validation suites

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7a392313-6ed3-4167-ab31-b39084ed8b84"><ac:parameter ac:name="id">1258397415</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d57c0e89-396c-444d-b934-94c4802e4a52"><ac:parameter ac:name="id">1258397417</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a4f6acd6-b054-4621-a15f-7c0e9e80a329"><ac:parameter ac:name="id">1258405722</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="afa959dc-958b-480f-96ee-5c3c0d8be3e4"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6ae25d8d-5ae3-4ed5-8141-55aace4bcf8e"><ac:parameter ac:name="id">1258397416</ac:parameter><ac:rich-text-body><h3>Introduction</h3><p>You can validate your models against a set of SysML constraints called validation suites. You can use the SysML validation suite that comes with the SysML Plugin to validate SysML projects. <span class="confluence-link">You need to perform the validation manually to check your model against the predefined validation suites. The predefined validation suites have «validationSuite» stereotype applied.</span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="861f2d9f-cb9a-431c-ab64-893247d5056d"><ac:rich-text-body><p>Each Profile contains its own validation suites. You can <ac:link><ri:page ri:content-title="Creating validation suites" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">create your own validation suites</span></ac:link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>You can meet the following SysML validation suites in the <ac:link><ri:page ri:content-title="Validation dialog" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Validation</strong> dialog</ac:link-body></ac:link> or <ac:link><ri:page ri:content-title="Validation Suites dialog" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Validation Suites</strong> dialog</ac:link-body></ac:link>:</p><ul><li><strong>SysML ValSuite - Activities</strong> contains SysML constraints on the following elements: Control Operator, Control Value, Discrete, noBuffer, Optional, Probability and Rate.</li><li><strong>SysML ValSuite - Blocks</strong> contains SysML constraints on the following elements: Binding Connector, Block, Distributed Property, Part Property, Reference Property, Shared Property, Value Property and Value Type.</li><li><strong>SysML ValSuite - Constraint Blocks</strong> contains SysML constraints on the following elements: Constraint Block and Constraint Property.</li><li><strong>SysML ValSuite - Model Elements</strong> contains SysML constraints on the following elements: View and Viewpoint.</li><li><strong>SysML ValSuite - Non-normative Extensions</strong> contains SysML constraints on the following elements: nonStreaming, Streaming, Design Constraint, Functional Requirement, Interface Requirement and Performance Requirement.</li><li><strong>SysML ValSuite - Port and Flows</strong> contains SysML constraints on the following elements: Flow Port, Flow Property, Flow Specification and Item Flow.</li><li><strong>SysML ValSuite - Requirements</strong> contains SysML constraints on the following elements: Copy, DeriveReqt, Requirement and Test Case<br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2dd220e4-7112-4724-90ad-c80a600dfdcf"><ac:rich-text-body><p>You can find predefined validation suites in the <ac:link><ri:page ri:content-title="Containment tab" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link> when the <strong>Show Auxiliary Resources</strong> option is enabled, expand the <em>MD Customization for SysML</em> Package &gt; <em>SysML constraints</em> Package &gt; <em>SysML ValSuite</em> Package. The <em>SysML ValSuite</em> Package is divided into separate Packages and contain an appropriate <ac:link><ri:page ri:content-title="SysML validation rules" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[validation rules]]></ac:plain-text-link-body></ac:link>.</p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="103c2af4-c9e8-405d-a3be-ec09a73376fe"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Metaclass" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:link><ri:page ri:content-title="Starting the validation" ri:space-key="SYSMLP2024xR3" /><ac:link-body>Learn how to <span class="confluence-link"><span class="confluence-link">start the validation &gt;&gt;</span></span></ac:link-body></ac:link></p><h3>Limiting the scope of the constraints to be validated against</h3><p>If you select the <strong>SysML ValSuite</strong> as the <strong>Validation Suite</strong> in the <span class="confluence-link"><ac:link><ri:page ri:content-title="Validation dialog" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Validation</strong> dialog</ac:link-body></ac:link></span>, your model is validated against all SysML validation suites at the same time. To limit the scope of the constraints to be validated against, select a more specific validation suite, such as <strong>SysML ValSuite - Blocks</strong>. The model or its part is validated against the selected validation suite. The <ac:link><ri:page ri:content-title="Validation Results panel" ri:space-key="SYSMLP2024xR3" /><ac:link-body><strong>Validation Results</strong> panel</ac:link-body></ac:link> shows the results, listing all elements that do not conform to some constraints in the selected validation suite. These elements are called “invalid” elements and are highlighted.</p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="36e2765b-e191-439a-bf1b-ed27f9f11c34"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Predefined validation suites" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="096a92f2-68dd-4c58-9a3d-1a9ed0e30deb"><ac:parameter ac:name="id">1258397413</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="with-breadcrumbs"><a href="https://docs.nomagic.com/display/MD2024xR3/Predefined+validation+suites">MagicDraw predefined validation suites</a></li><li class="with-breadcrumbs"><a href="https://docs.nomagic.com/display/MD2024xR3/Active+validation+suites">MagicDraw active validation suites</a></li><li class="with-breadcrumbs"><p class="with-breadcrumbs"><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/SysML+active+validation+suites">SysML active validation suites</a></p></li><li class="with-breadcrumbs"><a href="https://docs.nomagic.com/display/CRMP2024xR3/Requirements+validation+suites" rel="nofollow">Requirements validation suites</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159781 space=SYSMLP2024xR3 version=1 -->
## PAGE 00360: System

- page_id: `227159781`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159781/System
- version_number: 1
- version_date: `2018-03-21T13:43:40.128+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Visibility representation

299125027

#### CONTENT-COLUMN: Visibility representation

299125030

#### CONTENT-BLOCK: Visibility representation

299125029

A System is an artificial artifact consisting of blocks that pursue a common goal which cannot be achieved by the system's individual elements. A block can be software, hardware, a person, or an arbitrary unit.

[IMAGE alt='' src='']

#### NOTE: Visibility representation

Visibility representation

In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.

299125026

**Related pages**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d58715bb-5b47-4fd0-9ebd-785e28044f02"><ac:parameter ac:name="id">299125027</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="443e7043-7c26-4edc-8b16-63f86b5a4c25"><ac:parameter ac:name="id">299125030</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2e3f04e8-4f9d-4f80-8b0d-30595dd8ef5c"><ac:parameter ac:name="id">299125029</ac:parameter><ac:rich-text-body><p>A System is an artificial artifact consisting of blocks that pursue a common goal which cannot be achieved by the system's individual elements. A block can be software, hardware, a person, or an arbitrary unit.</p><p><ac:image ac:title="System" ac:alt="System"><ri:attachment ri:filename="system.png"><ri:page ri:content-title="System" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="45e244e1-7a14-47d4-88f2-ec499c585171"><ac:parameter ac:name="title">Visibility representation</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.</span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="533769e2-0e4b-4142-bbf0-898a7e7599e6"><ac:parameter ac:name="id">299125026</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Block Definition Diagram ]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159783 space=SYSMLP2024xR3 version=1 -->
## PAGE 00361: System Context

- page_id: `227159783`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159783/System+Context
- version_number: 1
- version_date: `2018-03-21T13:47:08.177+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Visibility representation

299472293

#### CONTENT-COLUMN: Visibility representation

299472356

#### CONTENT-BLOCK: Visibility representation

299472355

A System context element is a virtual container that includes the entire system and its actors.

You can convert any Block to System Contextif you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).

[IMAGE alt='' src='']

#### NOTE: Visibility representation

Visibility representation

In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.

##### Converting a Block to System Context

To convert a Block to System Context

1. Right-click a Block.
2. Select Refactor > Convert To > More Specific > System Context . The Block is converted to System Context.

299472292

**Related pages**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bad3b73e-8c4b-4f7d-bb73-283845098725"><ac:parameter ac:name="id">299472293</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="22094d10-8ce7-459c-ab93-94b3b03fe116"><ac:parameter ac:name="id">299472356</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6a01ba1e-6af1-45da-be6a-72173d1b142f"><ac:parameter ac:name="id">299472355</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>A System context element is a virtual container that includes the entire system and its actors.</p><p>You can convert any Block to System Context<span style="color: rgb(51,51,51);"> if you decide that the appropriate Block is decomposed. It may be called a system (i.e., Power Subsystem, Brake Subsystem, Lightening Subsystem).</span></p><p><ac:image ac:title="System Context" ac:alt="System Context" ac:height="250"><ri:attachment ri:filename="system_context.png"><ri:page ri:content-title="System Context" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="45e244e1-7a14-47d4-88f2-ec499c585171"><ac:parameter ac:name="title">Visibility representation</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">In SysML, properties and operations of the Block are public. Visibility representation literals, like +, #, ~, -, are not displayed in the Containment tree or in the element symbol on a diagram.</span><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Converting a Block to System Context</h3><p>To convert a Block to System Context</p><hr /><ol><li>Right-click a Block.</li><li>Select <strong>Refactor</strong> &gt; <strong>Convert To</strong> &gt; <strong>More Specific</strong> &gt; <strong>System Context</strong>.<br />The Block is converted to System Context.</li></ol></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="51f72765-eb9e-484d-a148-644608de25d4"><ac:parameter ac:name="id">299472292</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159785 space=SYSMLP2024xR3 version=2 -->
## PAGE 00362: Test Case

- page_id: `227159785`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159785/Test+Case
- version_number: 2
- version_date: `2025-05-02T10:28:44.007+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Test Case' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="a45da1a8-db6d-4ef1-9dda-52894061fb0e"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Test Case" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159606 space=SYSMLP2024xR3 version=1 -->
## PAGE 00363: Testcase Verdict

- page_id: `227159606`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159606/Testcase+Verdict
- version_number: 1
- version_date: `2020-12-07T07:29:48.526+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules > Validation rules of Non-normative Extensions
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
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>NoVerdict<strong><br /></strong></p><p><strong>Description</strong></p><p><span style="color: rgb(62,63,64);">This rule </span><span style="color: rgb(62,63,64);">checks if t</span><span style="color: rgb(62,63,64);">he </span>Testcase returns a parameter typed by the VerdictKind.</p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Constrained Element</strong></p><p>Behavior, Operation<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Create Verdict</strong> - creates return parameter typed by the VerdictKind.</p><p><strong>Example</strong></p><p><strong><ac:image><ri:attachment ri:filename="testCase_verdict.png"><ri:page ri:content-title="Testcase Verdict" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159116 space=SYSMLP2024xR3 version=2 -->
## PAGE 00364: The Use Case scenario created with the version 17.0.1 or earlier

- page_id: `227159116`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159116/The+Use+Case+scenario+created+with+the+version+17.0.1+or+earlier
- version_number: 2
- version_date: `2025-05-02T10:28:30.741+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Use Cases > Use Case scenario
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='The Use Case scenario created with version 17.0.1 or earlier' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="fcbfd74a-9569-461c-8ae5-60dba0959ee0"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="The Use Case scenario created with version 17.0.1 or earlier" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227158525 space=SYSMLP2024xR3 version=2 -->
## PAGE 00365: Toolbars

- page_id: `227158525`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158525/Toolbars
- version_number: 2
- version_date: `2025-05-02T10:28:17.790+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Toolbars' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="79f20eee-67f1-425d-92bc-74e8dcb14b86"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Toolbars" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227159809 space=SYSMLP2024xR3 version=2 -->
## PAGE 00366: Trace

- page_id: `227159809`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159809/Trace
- version_number: 2
- version_date: `2025-05-02T10:28:44.603+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Trace' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="094f725d-fcc8-45d7-88e5-b03c9fef3256"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Trace" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><span class="confluence-link"><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></li><li><span class="confluence-link"><span class="confluence-link"><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></span></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158584 space=SYSMLP2024xR3 version=2 -->
## PAGE 00367: Tracing requirement changes in Teamwork Cloud

- page_id: `227158584`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158584/Tracing+requirement+changes+in+Teamwork+Cloud
- version_number: 2
- version_date: `2025-05-02T10:28:19.864+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management
- labels: []

### NORMALIZED CONTENT

820860917

INLINE

820860919

INLINE

820860918

INLINE

true[CONFLUENCE_PAGE title='Suspect Links' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cc351cfb-b358-455a-b64b-8ee275936eff"><ac:parameter ac:name="id">820860917</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6fa805de-0e10-402c-9962-4db29b213fa3"><ac:parameter ac:name="id">820860919</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="997f3cb7-8c7e-4e94-a28e-d85c6c19d9e4"><ac:parameter ac:name="id">820860918</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="97c54a22-34a2-4534-812e-333824316854"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Suspect Links" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159786 space=SYSMLP2024xR3 version=1 -->
## PAGE 00368: Trigger on Nested Port

- page_id: `227159786`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159786/Trigger+on+Nested+Port
- version_number: 1
- version_date: `2016-04-08T08:37:21.886+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

A Trigger on Nested Port is a trigger that applies the «TriggerOnNestedPort» stereotype extending the UML’s Port property of the trigger to support nested ports.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Activity Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A Trigger on Nested Port is a trigger that applies the «TriggerOnNestedPort» stereotype extending the UML’s Port property of the trigger to support nested ports.</p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="cce34faa-2f55-4678-b24f-7f27f024c038"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Activity Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158523 space=SYSMLP2024xR3 version=2 -->
## PAGE 00369: Understanding the user interface

- page_id: `227158523`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158523/Understanding+the+user+interface
- version_number: 2
- version_date: `2025-05-02T10:28:17.592+02:00`
- ancestors: SysML Plugin Documentation > Getting started
- labels: []

### NORMALIZED CONTENT

232149238

232149241

232149240

[CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024xR3']true

232149237

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="91f27b33-8f74-43ba-8d62-9a98618d20b3"><ac:parameter ac:name="id">232149238</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="dea49992-cca4-45f5-9da5-dc08f0c9ee76"><ac:parameter ac:name="id">232149241</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="94e4e7bd-9746-40e0-b8ac-44a834be905c"><ac:parameter ac:name="id">232149240</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="d55c78e0-a79b-49f2-89c5-5f4008a34387"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Understanding the user interface" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4535f16c-54fc-4620-bf51-a52905418842"><ac:parameter ac:name="id">232149237</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e388fea6-449e-4874-bd40-3fbdaa6a51ce" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159787 space=SYSMLP2024xR3 version=1 -->
## PAGE 00370: Unit

- page_id: `227159787`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159787/Unit
- version_number: 1
- version_date: `2017-09-29T14:37:54.331+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

157370466

157370468

157370467

INLINE

A Unit represents a standard unit of measure. For example,metre, kilometre, or foot are units of length.Units are used to specify [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'].

157370465

**Related pages**

- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Customizing Units' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9c98f2a1-b1e4-48fd-bbdb-c92464d2372b"><ac:parameter ac:name="id">157370466</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="81403bac-9c0c-45dc-b2a9-0f1c79584dae"><ac:parameter ac:name="id">157370468</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d3dfc876-fbcd-43f3-868b-db982ea4642c"><ac:parameter ac:name="id">157370467</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="4c13a79e-137d-4cbb-ac28-046b2596cc3e"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Unit represents a standard <span>unit of measure. For example,<span> metre, kilometre, or foot are units of <span>length.<span> Units are used to specify <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Value Properties]]></ac:plain-text-link-body></ac:link>.</span></span></span></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9fbb91ea-8e6d-4bd4-a3e9-b15f808754d7"><ac:parameter ac:name="id">157370465</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Customizing Units" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159788 space=SYSMLP2024xR3 version=2 -->
## PAGE 00371: Usability Requirement

- page_id: `227159788`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159788/Usability+Requirement
- version_number: 2
- version_date: `2025-05-02T10:28:44.161+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Usability Requirement' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="5097803f-67ce-4f81-ad9f-b8a5660aa179"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Usability Requirement" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159107 space=SYSMLP2024xR3 version=2 -->
## PAGE 00372: Use Case description profile

- page_id: `227159107`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159107/Use+Case+description+profile
- version_number: 2
- version_date: `2025-05-02T10:28:29.606+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Use Cases
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Use Case description profile' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="72ae8bcd-3a71-4605-a82f-0c40633e9ee1"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Use Case description profile" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159108 space=SYSMLP2024xR3 version=2 -->
## PAGE 00373: Use Case scenario

- page_id: `227159108`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159108/Use+Case+scenario
- version_number: 2
- version_date: `2025-05-02T10:28:29.782+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Use Cases
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Use Case Scenario sketch' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="760a254f-56a4-4fa1-bada-173c607e993e"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Use Case Scenario sketch" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159104 space=SYSMLP2024xR3 version=2 -->
## PAGE 00374: Use Cases

- page_id: `227159104`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159104/Use+Cases
- version_number: 2
- version_date: `2025-05-02T10:28:29.150+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis
- labels: []

### NORMALIZED CONTENT

294344418

294344420

294344419

[CONFLUENCE_PAGE title='Use Case' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="94d990f0-e5ee-4bee-b973-9df5c3cacf9d"><ac:parameter ac:name="id">294344418</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c6539bce-6700-4641-8dbd-50b0309ee824"><ac:parameter ac:name="id">294344420</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="20e80af6-3f2e-402c-bc7c-a820c1594f93"><ac:parameter ac:name="id">294344419</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="9936e539-7d9c-40ba-9dcc-b9172be3ec2d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Use Case" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158561 space=SYSMLP2024xR3 version=1 -->
## PAGE 00375: User Guide

- page_id: `227158561`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158561/User+Guide
- version_number: 1
- version_date: `2024-01-29T11:29:24.409+01:00`
- ancestors: SysML Plugin Documentation
- labels: []

### NORMALIZED CONTENT

**Welcome to the SysML Plugin user guide!** It is intended to give an assistance to you while using MagicDraw with SysML Plugin or [CONFLUENCE_PAGE title='Cameo Systems Modeler Documentation' space='CSM185']. Go ahead – read the sections below or use the **Search** box to find a specific topic.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Welcome to the SysML Plugin user guide!</strong> It is intended to give an assistance to you while using MagicDraw with SysML Plugin or <ac:link><ri:page ri:space-key="CSM185" ri:content-title="Cameo Systems Modeler Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Systems Modeler]]></ac:plain-text-link-body></ac:link>. Go ahead – read the sections below or use the <strong>Search</strong> box to find a specific topic.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="87618ff1-e2c8-4983-a0d8-5f306322ccb2" /></p><p style="text-align: left;"><br /></p>
````

<!--NOMAGIC_PAGE id=227159789 space=SYSMLP2024xR3 version=1 -->
## PAGE 00376: User System

- page_id: `227159789`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159789/User+System
- version_number: 1
- version_date: `2016-04-08T08:48:54.530+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

An User System is a special external system that serves as medium between a user and the system without having its own interests in the communication.

#### TIP: Example

Example

- Input Device or Display.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='SysML Use Case Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>An User System is a special external system that serves as medium between a user and the system without having its own interests in the communication.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="2c988ad5-b38e-44fa-abdb-c86af35e9056"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><ul><li>Input Device or Display.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="de9adc89-d387-43d7-a667-124571a795a9"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="SysML Use Case Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158828 space=SYSMLP2024xR3 version=3 -->
## PAGE 00377: Using Association Block as Connector type

- page_id: `227158828`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158828/Using+Association+Block+as+Connector+type
- version_number: 3
- version_date: `2025-05-02T10:28:24.042+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Connecting Blocks in SysML Internal Block Diagram
- labels: []

### NORMALIZED CONTENT

1453790384

1453790386

1453790385

An [CONFLUENCE_PAGE title='Association Block' space='SYSMLP2024xR3'] can relate two [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']together, as well as having an internal structure and other features of its own. The purpose of the Connector Property is to show that internal structure and features using [CONFLUENCE_PAGE title='SysML specific compartments' space='SYSMLP2024xR3'], [CONFLUENCE_PAGE title='Property path notation' space='SYSMLP2024xR3'], [CONFLUENCE_PAGE title='Displaying internal structures on structured classifiers' space='SYSMLP2024xR3'], or [CONFLUENCE_PAGE title='Displaying elements' space='MD2024xR3']. You can specify more detail for [CONFLUENCE_PAGE title='Connector' space='MD2024xR3'] by typing them with Association Blocks. The Connector Property is created in the model after the Connector is typed by an Association Block. The Connector Property allows representation of Association Block usages in the [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3'].

To use the Association Block as a Connector type

1. Set the Association Block as a Connector type in one of the following ways: - In the Containment tree, select Association Block and drag it onto a Connector on the diagram pane. - In the Containment tree, select Association Block and drag it onto a Connector on the diagram pane. H old it down until the Tooltip appears (long drag) and drop it. From the opened menu, select the **Set as Type** command.
2. Select the Connector Property, [CONFLUENCE_PAGE title='Displaying parts and ports' space='SYSMLP2024xR3']open the **Display Parts/Ports** dialog , and select internal structure fragments of Association Block to show them on the Connector Property shape. The internal structure is shown inside the Connector Property shape. See the figure below for an example.

###### [IMAGE alt='' src=''] 
The Connector Property shows the internal structure of the *Water Delivery* Association Block and is connected with the *Diameter* Constraint Property.

1453790383

**Related pages**

- Creating Association Block

**Sample model**

The model used in the figure of this page is the **WaterSupply_19.0** sample model. Download[ATTACHMENT filename='WaterSupply_19.0.mdzip']*.*

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4d17e3af-7875-4af1-98e0-4b9c8b02da67"><ac:parameter ac:name="id">1453790384</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="db1137d2-97cd-4214-82d0-0ca87f71d659"><ac:parameter ac:name="id">1453790386</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="11c3d787-b422-4505-a773-deee5d87efc8"><ac:parameter ac:name="id">1453790385</ac:parameter><ac:rich-text-body><p>An <ac:link><ri:page ri:content-title="Association Block" ri:space-key="SYSMLP2024xR3" /></ac:link> can relate two <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Blocks ]]></ac:plain-text-link-body></ac:link>together, as well as having an internal structure and other features of its own. The purpose of the Connector Property is to show that internal structure and features using <ac:link><ri:page ri:content-title="SysML specific compartments" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Compartments]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:content-title="Property path notation" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[property paths]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:content-title="Displaying internal structures on structured classifiers" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[displaying internal structure]]></ac:plain-text-link-body></ac:link>, or <span class="confluence-link"><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Displaying elements" /><ac:plain-text-link-body><![CDATA[other Display commands]]></ac:plain-text-link-body></ac:link></span>. You can specify more detail for <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Connector" /><ac:plain-text-link-body><![CDATA[Connectors]]></ac:plain-text-link-body></ac:link> by typing them with Association Blocks. The Connector Property is created in the model after the Connector is typed by an Association Block. The Connector Property allows representation of Association Block usages in the <ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Internal Block Diagrams]]></ac:plain-text-link-body></ac:link>.</p><p><br /></p><p>To use the Association Block as a Connector type</p><hr /><ol><li>Set the Association Block as a Connector type in one of the following ways:<br /> - In the Containment tree, select Association Block and drag it onto a Connector on the diagram pane.<br /> - In the Containment tree, select Association Block and drag it onto a Connector on the diagram pane. H<span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">old it down <span style="color: rgb(51,51,51);">until the Tooltip appears (long drag)</span> and drop it. F</span></span><span style="color: rgb(51,51,51);">rom the opened menu, select the <strong>Set as Type</strong> command.</span></span></li><li>Select the Connector Property, <ac:link ac:anchor="Using the Display Parts/Ports dialog"><ri:page ri:content-title="Displaying parts and ports" ri:space-key="SYSMLP2024xR3" /><ac:link-body>open the <strong>Display Parts/Ports</strong> dialog</ac:link-body></ac:link>, and select internal structure fragments of <span style="color: rgb(51,51,51);">Association Block to show them on the Connector Property shape.</span><br />The internal structure is shown inside the Connector Property shape. See the figure below for an example.</li></ol><h6 style="text-align: center;"><br /><ac:image ac:align="center"><ri:attachment ri:filename="connectorProperty_in_ibd.png"><ri:page ri:content-title="Using Association Block as Connector type" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br />The Connector Property shows the internal structure of the <em>Water Delivery</em> Association Block and is connected with the <em>Diameter</em> Constraint Property.</h6><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a604381c-ba13-4b5c-bde5-cb64aa99557e"><ac:parameter ac:name="id">1453790383</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Defining+Blocks+in+Block+Definition+Diagram#DefiningBlocksinBlockDefinitionDiagram-CreatingAssociationBlock">Creating Association Block</a><strong><br /></strong></li></ul></ac:layout-cell><ac:layout-cell><p><strong>Sample model</strong></p><p>The model used in the figure of this page is the <strong>WaterSupply_19.0</strong> sample model. Download<span class="confluence-link"> <ac:link><ri:attachment ri:filename="WaterSupply_19.0.mdzip"><ri:page ri:content-title="Using Association Block as Connector type" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:link><em><span>.</span></em></span></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159244 space=SYSMLP2024xR3 version=2 -->
## PAGE 00378: Using Lifelines

- page_id: `227159244`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159244/Using+Lifelines
- version_number: 2
- version_date: `2025-05-02T10:28:33.201+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Modeling interactions with Sequence Diagrams
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Lifeline' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="54351584-fe79-415d-aad1-e04e72443fd2"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Lifeline" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227158563 space=SYSMLP2024xR3 version=3 -->
## PAGE 00379: Using packages

- page_id: `227158563`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158563/Using+packages
- version_number: 3
- version_date: `2025-05-02T10:28:19.058+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Organizing your model
- labels: []

### NORMALIZED CONTENT

499718654

499718657

499718655

There are multiple ways to organize your model into [CONFLUENCE_PAGE title='Package' space='MD2024xR3'].The S. Friedenthal in the "Practical Guide to SysML" recommends organizing your model structure in the following ways:

- By system hierarchy (e.g., system level, subsystem level, component level).
- By process life cycle where each model subpackage represents a stage in the process (e.g., requirements analysis, system design).
- By teams that are working on the model (e.g., Requirements Team, Integrated Product Team (IPT) 1, 2).
- By the type of model elements contained in it (e.g., requirements, behavior, structure).
- By model elements that are likely to change together.
- By model elements organized to support reuse (e.g., model libraries).
- By other logical or cohesive groupings of model elements based on defined model-partitioning criteria.
- A combination of the preceding.

###### The Package structure of MagicGrid project.

##### Automated Package Structure Creation in MagicGrid Projects

The package structure is automatically created upon the creation of the MagicGrid project. However, you can also create package structures for any additional components or subsystems within the solution domain of your model. You can do that by using predefined package structure configurations. To learn more, see the [CONFLUENCE_PAGE title='Automated Package Structure Creation' space='MD2024xR3'] page.

To create a predefined package structure in a MagicGrid project

1. Right-click a block you want to create a package structure for, and in its shortcut menu, select Tools > Create Package Structure . The Select Package Structure dialog opens.
2. In the dialog, select the class you require:
  1. To create a package structure for a component, select **PackagesForComponent** class.
  2. To create a package structure for a subsystem, select **PackagesForSubsystem**class.
3. Click OK . A package structure is created for the selected element. [ATTACHMENT filename='additional_subsystems.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0705924d-3812-4e53-bd43-d22d35d2ff38"><ac:parameter ac:name="id">499718654</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8d5fd347-6dc3-444a-8ac2-7af2d2fe99be"><ac:parameter ac:name="id">499718657</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b5eceb50-6853-41ab-b95d-3e152141051d"><ac:parameter ac:name="id">499718655</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">There are multiple ways to organize your model into <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Package" /><ac:plain-text-link-body><![CDATA[Packages]]></ac:plain-text-link-body></ac:link>. </span>The S. Friedenthal in the &quot;Practical Guide to SysML&quot; recommends organizing your model structure in the following ways:</p><ul><li><p>By system hierarchy (e.g., system level, subsystem level, component level).</p></li><li><p>By process life cycle where each model subpackage represents a stage in the process (e.g., requirements analysis, system design).</p></li><li><p>By teams that are working on the model (e.g., Requirements Team, Integrated Product Team (IPT) 1, 2).</p></li><li><p>By the type of model elements contained in it (e.g., requirements, behavior, structure).</p></li><li><p>By model elements that are likely to change together.</p></li><li><p>By model elements organized to support reuse (e.g., model libraries).</p></li><li><p>By other logical or cohesive groupings of model elements based on defined model-partitioning criteria.</p></li><li><p>A combination of the preceding.</p></li></ul><div>You can also organize your model structure according to your internal methodologies. The procedures of managing Packages in the modeling tool are provided in the<ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with packages" /><ac:plain-text-link-body><![CDATA[ Working with packages]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Package import" /></ac:link> pages.</div><div>In the following figure, the Packages are organized according to the MagicGrid approach. You can use this predefined package structure by creating a MagicGridBlank project. You can find the example and guidelines of how to use the MagicGrid approach by creating the MagicGridQuickStart project. <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects">How to create MagicGrid projects &gt;&gt;<br /><br /></a></div><div><ac:image ac:align="center"><ri:attachment ri:filename="MagicGrid_package_structure.png"><ri:page ri:content-title="Using packages" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></div><h6 style="text-align: center;">The Package structure of MagicGrid project.</h6><h3>Automated Package Structure Creation in MagicGrid Projects</h3><p>The package structure is automatically created upon the creation of the MagicGrid project. However, you can also create package structures for any additional components or subsystems within the solution domain of your model. You can do that by using predefined package structure configurations. To learn more, see the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Automated Package Structure Creation" /></ac:link> page.</p><p><br /></p><p>To create a predefined package structure in a MagicGrid project</p><hr /><ol><li class="_mce_tagged_br">Right-click a block you want to create a package structure for, and in its shortcut menu, select <strong>Tools</strong> &gt; <strong>Create Package Structure</strong>. The <strong>Select Package Structure </strong>dialog opens.</li><li class="_mce_tagged_br"><p>In the dialog, select the class you require:</p><ol><li class="_mce_tagged_br"><p>To create a package structure for a component, select <strong>PackagesForComponent</strong> class.</p></li><li class="_mce_tagged_br"><p>To create a package structure for a subsystem, select <strong>PackagesForSubsystem </strong>class.</p></li></ol></li><li>Click <strong>OK</strong>.<br />A package structure is created for the selected element.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="additional_subsystems.png"><ri:page ri:content-title="Using packages" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br /></li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158853 space=SYSMLP2024xR3 version=3 -->
## PAGE 00380: Using QUDV model library

- page_id: `227158853`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158853/Using+QUDV+model+library
- version_number: 3
- version_date: `2025-05-02T10:28:24.708+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Using Units
- labels: []

### NORMALIZED CONTENT

**On this page**

##### Description of the QUDV model library

This model library is designed so that extensions to ISQ and SI can be represented, as well as any alternative systems of quantities and units.

The SysML QUDV library:

- Complies with International Vocabulary of Metrology (VIM 3rd edition) .
- Includes ISO/IEC 80000 definitions of base quantities and units to provide semantics for computer-based dimensional analysis.

The QUDV (Quantity Unit Dimension Value) library is introduced in[OMG SysML Specification](http://www.omg.org/spec/SysML/About-SysML/): **Annex E: Non-normative Extensions** > **E.5 Model Library for Quantities, Units, Dimensions, and Values (QUDV)**.

[IMAGE alt='' src='']

##### Description of sub-libraries

Sub-libraries are located in the*modelLibraries* folder in the installation directory of your modeling tool. The SysML plugin consists of those sub-libraries:

- **ISO-80000.mdzip**. The ISO-80000 model library consists of specific quantities and units that are defined by ISO 80000. Full details of ISO-80000 Library Model definitions are available in[OMG SysML Specification](http://www.omg.org/spec/SysML/About-SysML/): **Annex E: Non-normative Extensions** > **E.6****Model Library of SysML Quantity Kinds and Units for ISO 80000**. The ISO-80000 library is loaded by default in the [MagicGrid Blank](https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects) and [MagicGrid QuickStart](https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects) projects.If you work with projects older than version 18.0, which use the QUDV library and SysML 1.3 library, the ISO-80000 library will not be compatible.
- **ISO-80000-Extension.mdzip**. The ISO-80000-Extension library extends the ISO-80000 library with the collection of imperial, nautical, and common units. The ISO-80000-Extension library is loaded by default in the [MagicGrid Blank](https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects) and [MagicGrid QuickStart](https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects) projects.
- **QUDV.mdzip**. The QUDV model library consists of the main definitions of the new units and quantity kinds system as specified in OMG SysML Specifications, such as SimpleUnit, SimpleQuantityKind, DerivedUnit, DerivedQuantityKind, AffineConversionUnit, UnitFactor, QuantityKindFactor, and many more. Full details of ISO-80000 Library Model definitions are available in [OMG SysML Specification](http://www.omg.org/spec/SysML/About-SysML/): **Annex E: Non-normative Extensions** > **E.5 Model Library for Quantities, Units, Dimensions, and Values (QUDV)**.
- **SI Value Type Library.mdzip**. The SysML Plugin provides a model library that contains predefined value types. You can use them for typing the Value Properties in your SysML model. These value types use the units and quantity kinds defined in the QUDV model library. Units and Quantity Kinds tableNameUnitQuantity Kind**A**ampere : SimpleUnitelectricCurrent : SimpleQuantityKind**A/m**amperePerMeter : DerivedUnitmagneticFieldStrength : DerivedQuantityKind**A/m²**amperePerSquareMeter :DerivedUnitcurrentDensity : DerivedQuantityKind**Bq**becquerel : DerivedUnitradionuclideActivity : DerivedQuantityKind**C**coulomb : DerivedUnitelectricCharge : DerivedQuantityKind**cd**candela : SimpleUnitluminousIntensity : SimpleQuantityKind**cd/m²**candelaPerSquareMeter :DerivedUnitluminance : DerivedQuantityKind**F**farad : DerivedUnitcapacitance : DerivedQuantityKind**Gy**gray : DerivedUnitabsorbedDose : DerivedQuantityKind**H**henry : DerivedUnitinductance : DerivedQuantityKind**Hz**hertz : DerivedUnitfrequency : DerivedQuantityKind**J**joule : DerivedUnitenergy : DerivedQuantityKind**K**kelvin : SimpleUnitthermodynamicTemperature : SimpleQuantityKind**kat**katal : DerivedUnitcatalyticActivity : DerivedQuantityKind**kg**kilogram : SimpleUnitmass : SimpleQuantityKind**kg/m³**kilogramPerCubicMeter :DerivedUnitmassDensity : DerivedQuantityKind**lm**lumen : DerivedUnitluminousFlux : DerivedQuantityKind**lx**lux : DerivedUnitilluminance : DerivedQuantityKind**m**meter : SimpleUnitlength : SimpleQuantityKind**m/s**meterPerSecond : DerivedUnitvelocity : DerivedQuantityKind**m/s²**meterPerSecondSquared :DerivedUnitacceleration : DerivedQuantityKind**mol**mole : SimpleUnitamountOfSubstance : SimpleQuantityKind**mol/m³**molePerCubicMeter : DerivedUnitamountOfSubstanceConcentration :DerivedQuantityKind**m²**squareMeter : DerivedUnitarea : DerivedQuantityKind**m³**cubicMeter : DerivedUnitvolume : DerivedQuantityKind**m³/kg**cubicMeterPerKilogram :DerivedUnitspecificVolume : DerivedQuantityKind**m־¹**reciprocalMeter : DerivedUnitwaveNumber : DerivedQuantityKind**N**newton : DerivedUnitforce : DerivedQuantityKind**Pa**pascal : DerivedUnitpressure : DerivedQuantityKind**rad**radian : DerivedUnitplaneAngle : DerivedQuantityKind**s**second : SimpleUnittime : SimpleUnit**S**siemens : DerivedUnitelectricConductance : DerivedQuantityKind**sr**steradian : DerivedUnitsolidAngle : DerivedQuantityKind**Sv**sievert : DerivedUnitdoseEquivalent : DerivedQuantityKind**T**tesla : DerivedUnitmagneticFluxDensity : DerivedQuantityKind**V**volt : DerivedUnitelectricPotentialDifference : DerivedQuantityKind**W**watt : DerivedUnitpower : DerivedQuantityKind**Wb**weber : DerivedUnitmagneticFlux : DerivedQuantityKind**°C**celciusTemperature :AffineConversionUnitcelciusTemperature : DerivedQuantityKind**Ω**ohm : DerivedUnitelectricResistance : DerivedQuantityKind
- **SIDefinitions.mdzip**. The SI Definitions library consists of predefined units and quantity kinds in QUDV system that you can use in your model. You can customize the units and value types.
- **SISpecializations.mdzip**. The SI Specializations library consists of a diagram (and Blocks). It demonstrates how to extend the current QUDV system.
- **SysML_SI_Definitions_Library.mdzip**.
- **QUDV_SysML1.4.mdzip**.

##### Loading the ISO 80000 library

If you want to use the full ISO 80000 library in your project, you can:

- [CONFLUENCE_PAGE title='Using QUDV model library' space='SYSMLP2024xR3']
- Set the ISO 80000 library usage options each time when opening the main project.[CONFLUENCE_PAGE title='Using QUDV model library' space='SYSMLP2024xR3']

manualTo load the full ISO 80000 library for a separate project, do either of the following:

- Select the value in Compartment area and click the ISO button on smart manipulator toolbar. [ATTACHMENT filename='iso_button.png']
- Click [ATTACHMENT filename='options_button_in_model_browser.png'] in the Containment tree and select the Show Auxiliary Resources option. The ISO-80000 package appears in the Containment tree. Right-click it and select Project Usages > Load . [ATTACHMENT filename='load_qudv_library.png'] All standard units and value types are loaded.

automaticTo specify the ISO80000 library usage each time when opening the main project

1. On the main menu, select **Options** > **Project Usages**.
2. On the right side of the **Used Projects** dialog, select the**ISO-80000.mdzip** package.
3. On the left side of this dialog, in the **Load Mode** area, select the desired mode:****- **Always load** - the library is always loaded when the main project is opened. - **Autoload** - the library is not loaded when the main project is loaded. The modeling tool monitors user activities in the project and loads the particular used project on the demand by the project. - **Autoload with prompt** - this mode is similar to the Autoload mode. The difference is that the modeling tool asks the user for confirmation before loading it. - **Manual load** - the library is not loaded when the main project is loaded. The model integrity is not broken, as all required elements of the used project exist as simplified versions (that is, loaded as proxies) of the elements are used in the project. This load mode is recommended for all used projects that are stable or rarely modified.
4. Click **OK**.
5. Reload the main project. 
The **ISO-80000.mdzip** package is used in the main project according to the selected mode.

##### Loading the basic units from ISO 80000 library

You can load only the basic SI, US customary, naval, and imperial units from the ISO-80000 and ISO-80000-Extension libraries instead of the whole library.

To load the basic units from the ISO 80000 library

- When [CONFLUENCE_PAGE title='Creating SysML projects' space='SYSMLP2024xR3'] , set the Use Basic Units Library option value to true. [ATTACHMENT filename='use_basic_units_library.png']
- Directly on the [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] symbol: select the Value Property symbol and click the ISO button on the smart manipulator toolbar. [ATTACHMENT filename='iso_button_value_property_symbol.png'] The basic units library is loaded, including two Basic Unit Categories and Basic Units Dependency Matrices. [ATTACHMENT filename='basic_units_library_in_containment_tree.png']

The*Basic Unit Categories* and *Basic Units* matrices, shown in the following figure, allow you to manage imports for a project. You can create or delete the relationships in the matrices in order to include or remove the units you have to use. [CONFLUENCE_PAGE title='Using Dependency Matrix' space='MD2024xR3']>]]>

[IMAGE alt='' src='']

[IMAGE alt='' src='']

**Related pages**

- [CONFLUENCE_PAGE title='Managing project usages' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="bd1d593f-abae-48a6-8c43-8edda1ad7c1e" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Description of the QUDV model library</h3><p>This model library is designed so that extensions to ISQ and SI can be represented, as well as any alternative systems of quantities and units.</p><p>The SysML QUDV library:</p><ul><li>Complies with <a href="http://www.nist.gov/pml/div688/grp40/upload/International-Vocabulary-of-Metrology.pdf" class="external-link" rel="nofollow">International Vocabulary of Metrology (VIM 3rd edition)</a>.</li><li>Includes <a href="http://www.iso.org/iso/catalogue_detail?csnumber=30669" class="external-link" rel="nofollow">ISO/IEC 80000</a> definitions of base quantities and units to provide semantics for computer-based dimensional analysis.</li></ul><p>The QUDV (Quantity Unit Dimension Value) library is introduced in<span class="confluence-link"> <a href="http://www.omg.org/spec/SysML/About-SysML/"><span class="external-link">OMG SysML Specification</span></a></span>: <strong>Annex E: Non-normative Extensions</strong> &gt; <strong>E.5 Model Library for Quantities, Units, Dimensions, and Values (QUDV)</strong>.</p><p><ac:image ac:title="SysML's QUDV in OMG SysML 1.4 ISO 80000 collection." ac:alt="SysML's QUDV in OMG SysML 1.4 ISO 80000 collection."><ri:attachment ri:filename="sysml_QUDV.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h3>Description of sub-libraries</h3><p>Sub-libraries are located in the<em> modelLibraries</em> folder in the installation directory of your modeling tool. The SysML plugin consists of those sub-libraries:</p><ul><li><p><strong>ISO-80000.mdzip</strong>. The ISO-80000 model library consists of specific quantities and units that are defined by ISO 80000. Full details of ISO-80000 Library Model definitions are available <ac:inline-comment-marker ac:ref="a14358f1-8422-473e-8d47-b26170cf6337">in</ac:inline-comment-marker><a href="http://www.omg.org/spec/SysML/About-SysML/"><ac:inline-comment-marker ac:ref="a14358f1-8422-473e-8d47-b26170cf6337"> </ac:inline-comment-marker><span class="confluence-link"><span class="external-link"><ac:inline-comment-marker ac:ref="a14358f1-8422-473e-8d47-b26170cf6337">OMG SysML Specification</ac:inline-comment-marker></span></span></a>: <strong>Annex E: Non-normative Extensions</strong> &gt; <strong>E.6</strong><strong> Model Library of SysML Quantity Kinds and Units for ISO 80000</strong>.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="61cfeac4-71b8-4d29-9fd7-641f7cfff287"><ac:rich-text-body><ul><li><span><span style="color: rgb(51,51,51);">The ISO-80000 library is loaded by default in the <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects">MagicGrid Blank</a> and <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects">MagicGrid QuickStart</a> projects.</span></span></li><li><span>If you work with projects older than version 18.0, which use the QUDV library and SysML 1.3 library, the ISO-80000 library will not be compatible.</span><span><br /></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target"><strong>ISO-80000-Extension.mdzip</strong>. The ISO-80000-Extension library extends the ISO-80000 library with the collection of imperial, nautical, and common units.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="60708858-11b0-4812-8617-901ac2bfcf3d"><ac:rich-text-body><p><span><span style="color: rgb(51,51,51);">The ISO-80000-Extension library is loaded by default in the <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects">MagicGrid Blank</a> and <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Creating+SysML+projects#CreatingSysMLprojects-CreatingMagicGridprojects">MagicGrid QuickStart</a> projects.</span></span><span><br /></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><strong>QUDV.mdzip</strong>.  The QUDV model library consists of the main definitions of the new units and quantity kinds system as specified in OMG SysML Specifications, such as SimpleUnit, SimpleQuantityKind, DerivedUnit, DerivedQuantityKind, AffineConversionUnit, UnitFactor, QuantityKindFactor, and many more. Full details of ISO-80000 Library Model definitions are available in <span class="confluence-link"><a href="http://www.omg.org/spec/SysML/About-SysML/"><span class="external-link"><ac:inline-comment-marker ac:ref="0d6bd09e-c340-4ede-b2a2-743dde001cb1">OMG SysML Specification</ac:inline-comment-marker></span></a></span><ac:inline-comment-marker ac:ref="0d6bd09e-c340-4ede-b2a2-743dde001cb1">:</ac:inline-comment-marker> <strong>Annex E: Non-normative Extensions</strong> &gt; <strong>E.5 Model Library for Quantities, Units, Dimensions, and Values (QUDV)</strong>.</p></li><li><p><strong>SI Value Type Library.mdzip</strong>. The SysML Plugin provides a model library that contains predefined value types. You can use them for typing the Value Properties in your SysML model. These value types use the units and quantity kinds defined in the QUDV model library.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="753517e9-08e9-46b9-ab2f-9d950978a59a"><ac:parameter ac:name="title">Units and Quantity Kinds table</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><table class="wrapped"><colgroup><col /><col /><col /></colgroup><tbody><tr><th>Name</th><th>Unit</th><th>Quantity Kind</th></tr><tr><td><strong>A</strong></td><td>ampere : SimpleUnit</td><td>electricCurrent : SimpleQuantityKind</td></tr><tr><td><strong>A/m </strong></td><td>amperePerMeter : DerivedUnit</td><td>magneticFieldStrength : DerivedQuantityKind</td></tr><tr><td><strong>A/m² </strong></td><td>amperePerSquareMeter :<p>DerivedUnit</p></td><td>currentDensity : DerivedQuantityKind</td></tr><tr><td><strong>Bq</strong></td><td>becquerel : DerivedUnit</td><td>radionuclideActivity : DerivedQuantityKind</td></tr><tr><td><strong>C</strong></td><td>coulomb : DerivedUnit</td><td>electricCharge : DerivedQuantityKind</td></tr><tr><td><strong>cd </strong></td><td>candela : SimpleUnit</td><td>luminousIntensity : SimpleQuantityKind</td></tr><tr><td><strong>cd/m² </strong></td><td>candelaPerSquareMeter :<p>DerivedUnit</p></td><td>luminance : DerivedQuantityKind</td></tr><tr><td><strong>F</strong></td><td>farad : DerivedUnit</td><td>capacitance : DerivedQuantityKind</td></tr><tr><td><strong>Gy </strong></td><td>gray : DerivedUnit</td><td>absorbedDose : DerivedQuantityKind</td></tr><tr><td><strong>H </strong></td><td>henry : DerivedUnit</td><td>inductance : DerivedQuantityKind</td></tr><tr><td><strong>Hz </strong></td><td>hertz : DerivedUnit</td><td>frequency : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>J</strong></td><td colspan="1">joule : DerivedUnit</td><td colspan="1">energy : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>K </strong></td><td colspan="1">kelvin : SimpleUnit</td><td colspan="1">thermodynamicTemperature : SimpleQuantityKind</td></tr><tr><td colspan="1"><strong>kat</strong></td><td colspan="1">katal : DerivedUnit</td><td colspan="1">catalyticActivity : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>kg</strong></td><td colspan="1">kilogram : SimpleUnit</td><td colspan="1">mass : SimpleQuantityKind</td></tr><tr><td colspan="1"><strong>kg/m³</strong></td><td colspan="1">kilogramPerCubicMeter :<p>DerivedUnit</p></td><td colspan="1">massDensity : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>lm </strong></td><td colspan="1">lumen : DerivedUnit</td><td colspan="1">luminousFlux : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>lx </strong></td><td colspan="1">lux : DerivedUnit</td><td colspan="1">illuminance : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>m </strong></td><td colspan="1">meter : SimpleUnit</td><td colspan="1">length : SimpleQuantityKind</td></tr><tr><td colspan="1"><strong>m/s </strong></td><td colspan="1">meterPerSecond : DerivedUnit</td><td colspan="1">velocity : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>m/s² </strong></td><td colspan="1">meterPerSecondSquared :<p>DerivedUnit</p></td><td colspan="1">acceleration : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>mol </strong></td><td colspan="1">mole : SimpleUnit</td><td colspan="1">amountOfSubstance : SimpleQuantityKind</td></tr><tr><td colspan="1"><strong>mol/m³</strong></td><td colspan="1">molePerCubicMeter : DerivedUnit</td><td colspan="1">amountOfSubstanceConcentration :<p>DerivedQuantityKind</p></td></tr><tr><td colspan="1"><strong>m² </strong></td><td colspan="1">squareMeter : DerivedUnit</td><td colspan="1">area : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>m³</strong></td><td colspan="1">cubicMeter : DerivedUnit</td><td colspan="1">volume : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>m³/kg</strong></td><td colspan="1">cubicMeterPerKilogram :<p>DerivedUnit</p></td><td colspan="1">specificVolume : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>m־¹ </strong></td><td colspan="1">reciprocalMeter : DerivedUnit</td><td colspan="1">waveNumber : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>N</strong></td><td colspan="1">newton : DerivedUnit</td><td colspan="1">force : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>Pa</strong></td><td colspan="1">pascal : DerivedUnit</td><td colspan="1">pressure : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>rad </strong></td><td colspan="1">radian : DerivedUnit</td><td colspan="1">planeAngle : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>s </strong></td><td colspan="1">second : SimpleUnit</td><td colspan="1">time : SimpleUnit</td></tr><tr><td colspan="1"><strong>S </strong></td><td colspan="1">siemens : DerivedUnit</td><td colspan="1">electricConductance : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>sr</strong></td><td colspan="1">steradian : DerivedUnit</td><td colspan="1">solidAngle : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>Sv </strong></td><td colspan="1">sievert : DerivedUnit</td><td colspan="1">doseEquivalent : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>T </strong></td><td colspan="1">tesla : DerivedUnit</td><td colspan="1">magneticFluxDensity : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>V </strong></td><td colspan="1">volt : DerivedUnit</td><td colspan="1">electricPotentialDifference : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>W </strong></td><td colspan="1">watt : DerivedUnit</td><td colspan="1">power : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>Wb </strong></td><td colspan="1">weber : DerivedUnit</td><td colspan="1">magneticFlux : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>°C </strong></td><td colspan="1">celciusTemperature :<p>AffineConversionUnit</p></td><td colspan="1">celciusTemperature : DerivedQuantityKind</td></tr><tr><td colspan="1"><strong>Ω </strong></td><td colspan="1">ohm : DerivedUnit</td><td colspan="1">electricResistance : DerivedQuantityKind</td></tr></tbody></table><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><strong>SIDefinitions.mdzip</strong>. The SI Definitions library consists of predefined units and quantity kinds in QUDV system that you can use in your model. You can customize the units and value types.</p></li><li><p><strong>SISpecializations.mdzip</strong>. The SI Specializations library consists of a diagram (and Blocks). It demonstrates how to extend the current QUDV system.</p></li><li><p><strong>SysML_SI_Definitions_Library.mdzip</strong>.</p></li><li><p><strong>QUDV_SysML1.4.mdzip</strong>.</p></li></ul><h3>Loading the ISO 80000 library</h3><p>If you want to use the full ISO 80000 library in your project, you can:</p><ul><li><ac:link ac:anchor="manual"><ac:plain-text-link-body><![CDATA[Load it manually for a separate main projects.]]></ac:plain-text-link-body><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link ac:anchor="automatic"><ac:link-body><span class="confluence-link">Set the ISO 80000 library usage options </span> each time when opening the main project.</ac:link-body><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="b1a1a729-f3fa-4fc1-9a87-f2a0624d43a2"><ac:parameter ac:name="">manual</ac:parameter></ac:structured-macro>To load the full ISO 80000 library for a separate project, do either of the following:</p><hr /><ul><li>Select the value in Compartment area and click the<strong> ISO</strong> button on smart manipulator toolbar.<br /><ac:image><ri:attachment ri:filename="iso_button.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Click <ac:image ac:title="Options" ac:alt="Options"><ri:attachment ri:filename="options_button_in_model_browser.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> in the Containment tree and select the <strong>Show Auxiliary Resources</strong> option. The <strong>ISO-80000</strong> package appears in the Containment tree. Right-click it and select <strong>Project Usages</strong> &gt;<strong> Load</strong>.<br /><ac:image ac:title="The full ISO-80000 library package stored as auxiliary resource in the Containment tree." ac:alt="The full ISO-80000 library package stored as auxiliary resource in the Containment tree."><ri:attachment ri:filename="load_qudv_library.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br />All standard units and value types are loaded.<br /><br /></li></ul><p><span style="color: rgb(51,51,51);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="a2ff14f5-8760-43ae-adfa-8f241e1950fc"><ac:parameter ac:name="">automatic</ac:parameter></ac:structured-macro>To specify the ISO80000 library usage each time when opening the main project<br /></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">On the main menu, select <strong>Options</strong> &gt; <strong>Project Usages</strong>.</span><span style="color: rgb(51,51,51);"> </span></li><li><span style="color: rgb(51,51,51);">On the right side of the <strong>Used Projects</strong> dialog, select the<strong> ISO-80000.mdzip</strong> package.</span><span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"> </span></li><li><span style="color: rgb(51,51,51);">On the left side of this dialog, in the <strong>Load Mode</strong> area, select the desired mode:<strong><br />  </strong>- <strong>Always load</strong> - the library</span> is always loaded when<span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"> </span>the main project is opened.<span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"><br />  - <strong>Autoload</strong> -</span> the library is not loaded when the main project<span style="color: rgb(51,51,51);"> </span>is loaded. The modeling tool monitors user activities in the project and loads<span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"> </span>the particular used project on the demand by the project.<span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"><br />  - <strong>Autoload with prompt</strong> -</span> this mode is similar to the <strong>Autoload</strong> mode. The<span style="color: rgb(51,51,51);"> </span>difference is that the modeling tool asks the user for confirmation before loading it.<span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"> </span><br /><span style="color: rgb(51,51,51);">  - <strong>Manual load</strong> -</span> the library is not loaded when the main<span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"> </span>project is loaded. The model integrity is not broken, as all required<span style="color: rgb(51,51,51);"> </span>elements of the used project exist as simplified versions (that is,<span style="color: rgb(51,51,51);"> </span>loaded as proxies) of the elements are used in the project. This load<span style="color: rgb(51,51,51);"> </span>mode is recommended for all used projects that are stable or rarely<span style="color: rgb(51,51,51);"> </span>modified.<span style="color: rgb(51,51,51);"> </span><span style="color: rgb(51,51,51);"><br /></span></li><li><span style="color: rgb(51,51,51);">Click <strong>OK</strong>.</span></li><li><span style="color: rgb(51,51,51);">Reload the main project.<br />The <strong>ISO-80000.mdzip</strong> package is used in the main project according to the selected mode.<br /></span></li></ol><p><br /></p><h3>Loading the basic units from ISO 80000 library</h3><p>You can load only the basic SI, US customary, naval, and imperial units from the ISO-80000 and ISO-80000-Extension libraries instead of the whole library.</p><p>To load the basic units from the ISO 80000 library</p><hr /><ul><li>When <ac:link><ri:page ri:content-title="Creating SysML projects" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[creating a new SysML project]]></ac:plain-text-link-body></ac:link>, set the <strong>Use Basic Units Library</strong> option value to true.<br /><ac:image><ri:attachment ri:filename="use_basic_units_library.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>Directly on the <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> symbol: select the Value Property symbol and <span style="color: rgb(51,51,51);">click the</span><strong> ISO</strong><span style="color: rgb(51,51,51);"> button on the smart manipulator toolbar.</span><br /><ac:image ac:height="193"><ri:attachment ri:filename="iso_button_value_property_symbol.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /><br />The basic units library is loaded, including two <em>Basic Unit Categories</em> and <em>Basic Units</em> Dependency Matrices.<br /><ac:image><ri:attachment ri:filename="basic_units_library_in_containment_tree.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li></ul><p>The<em> Basic Unit Categories</em> and <em>Basic Units</em> matrices, shown in the following figure, allow you to manage imports for a project. You can create or delete the relationships in the matrices in order to include or remove the units you have to use. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Using Dependency Matrix" /><ac:plain-text-link-body><![CDATA[Learn how to modify a Dependency Matrix >>]]></ac:plain-text-link-body></ac:link></p><p><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="basic_units_category_matrix.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> </span></p><p><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="basic_units_matrix.png"><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><span class="current"><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Managing project usages" /></ac:link></span></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158602 space=SYSMLP2024xR3 version=2 -->
## PAGE 00381: Using Requirement patterns glossary

- page_id: `227158602`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158602/Using+Requirement+patterns+glossary
- version_number: 2
- version_date: `2025-05-02T10:28:20.107+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Requirements management > Requirements verification
- labels: []

### NORMALIZED CONTENT

819722420

819722422

819722419

**On this page**

43

819722421

[CONFLUENCE_PAGE title='Using Requirement patterns glossary' space='CRMP2024xR3']true

819730027

**Related pages**

[CONFLUENCE_PAGE title='Requirements management' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b15460da-dbb9-4e0b-aad4-eb0746158504"><ac:parameter ac:name="id">819722420</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4df0ebc0-bc13-4da6-9487-da69b016c200"><ac:parameter ac:name="id">819722422</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7bf84acc-f500-477c-86ff-9e57904e7407"><ac:parameter ac:name="id">819722419</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6b167be5-b421-4751-b7fa-f82b3971de39"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cc36574a-e2ce-47e7-a524-6420364d0d74"><ac:parameter ac:name="id">819722421</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="f38b68af-c152-472d-8cc2-c7f059d1cac4"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Using Requirement patterns glossary" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2c6713c9-4bd1-414d-8561-2b6d17cf55cc"><ac:parameter ac:name="id">819730027</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5cffd566-1dbd-48ab-adb5-b51ecb5a614b"><ac:parameter ac:name="page"><ac:link><ri:page ri:content-title="Requirements management" ri:space-key="SYSMLP2024xR3" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159131 space=SYSMLP2024xR3 version=3 -->
## PAGE 00382: Using Swimlanes to allocate functions to structure

- page_id: `227159131`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159131/Using+Swimlanes+to+allocate+functions+to+structure
- version_number: 3
- version_date: `2025-05-02T10:28:31.178+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Functional analysis > Functional Allocations
- labels: []

### NORMALIZED CONTENT

With a [CONFLUENCE_PAGE title='Swimlane' space='SYSMLP2024xR3'], you can relate a Behavior (a function) with a structure. In other words, you can allocate a behavior to a structure using Swimlanes in the [CONFLUENCE_PAGE title='SysML Activity Diagram' space='SYSMLP2024xR3'] and analyze whether or not all behaviors are performed by a particular system object.

Before establishing allocations, you must define the allocation mode - **Definition**or **Usage.**The definition elements areActivity and [Block](https://docs.nomagic.com/display/SYSMLP2024xR3/Block), and usage elements are Action and [Part Property](https://docs.nomagic.com/display/SYSMLP2024xR3/Part+Property). Depending on the mode, you can convey which allocations are established considering the system context.

To allocate behavior to structure

1. Click the **Vertical Swimlanes** button on the activity diagram palette and then click an empty space on that diagram pane. The **Represent Properties** dialog opens. The **Represent Properties** dialog opens if:The Activity diagram is owned by a Block or Use Case.The owning Block or the Block set as the Use Case [CONFLUENCE_PAGE title='Specifying a Use Case subject' space='MD2024xR3'] has part properties.Partitions are created for each property you select to represent as a Swimlane in the Activity diagram. [IMAGE alt='' src=''] Otherwise, you can manually define properties represented by a Swimlane.
2. In the dialog, select the properties you want to represent as Swimlanes and click OK .
3. Right-click any of the Swimlane partitions and select**Allocation Mode**>**Usage**(if not selected yet). The allocation to usage mode is enabled in the diagram. Usage modeThis mode allows you to convey that allocations are established considering the system context. Otherwise, allocations are generic and not related to any system context.
4. Drag existing actions from the diagram pane or create new actions for particular swimlanes.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>With a <ac:link><ri:page ri:content-title="Swimlane" ri:space-key="SYSMLP2024xR3" /></ac:link>, you can relate a Behavior (a function) with a structure. In other words, you can <span>allocate a behavior to a structure using Swimlanes in the <ac:link><ri:page ri:content-title="SysML Activity Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Activity Diagram]]></ac:plain-text-link-body></ac:link> and analyze whether or not all behaviors are performed by a particular system object.</span></p><p><span>Before establishing allocations, you must define the allocation mode - <strong>Definition </strong>or <strong>Usage.</strong><span style="color: rgb(62,63,64);"> </span><span style="color: rgb(62,63,64);">The definition elements are </span><span style="color: rgb(62,63,64);"> Activity and <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Block">Block</a>, and usage elements are Action and <a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Part+Property">Part Property</a>. Depending on the mode,</span></span> you can convey which allocations are established considering the system context.</p><p><br /></p><p><span>To allocate behavior to structure</span></p><hr /><ol><li><p class="auto-cursor-target">Click the <strong>Vertical Swimlanes</strong> button on the activity diagram palette and then click an empty space on that diagram pane. The <strong>Represent Properties</strong> dialog opens.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fbf84973-0f69-44a0-a8c8-3cb95b4cc65b"><ac:rich-text-body><p>The <strong>Represent Properties</strong> dialog opens if:</p><ol><li>The Activity diagram is owned by a Block or Use Case.</li><li class="confluence-link">The owning Block or the Block set as the Use Case <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Specifying a Use Case subject" /><ac:plain-text-link-body><![CDATA[subject]]></ac:plain-text-link-body></ac:link> has part properties.</li></ol><p class="confluence-link">Partitions are created for each property you select to represent as a Swimlane in the Activity diagram.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="represent_properties_dialog.png"><ri:page ri:content-title="Using Swimlanes to allocate functions to structure" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p class="auto-cursor-target">Otherwise, you can manually define properties represented by a Swimlane.</p><p class="auto-cursor-target"><br /></p></li><li>In the dialog, select the properties you want to represent as Swimlanes and click <strong>OK</strong>.</li><li><p class="auto-cursor-target"><span>Right-click any of the Swimlane partitions and select </span><strong>Allocation Mode</strong><span> &gt; </span><strong>Usage</strong><span> (if not selected yet). The allocation to usage mode is enabled in the diagram.</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1121b6a5-4104-47ad-929e-78eb25b56cba"><ac:parameter ac:name="title">Usage mode</ac:parameter><ac:rich-text-body><p><span>This mode allows you to convey that allocations are established considering the system context. Otherwise, allocations are generic and not related to any system context.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span><br /></span></p></li><li><span>Drag existing actions from the diagram pane or create new actions for particular swimlanes.</span></li></ol><p><span><br /></span></p>
````

<!--NOMAGIC_PAGE id=227160100 space=SYSMLP2024xR3 version=1 -->
## PAGE 00383: Using SysPhs constant and SysPhs variable

- page_id: `227160100`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160100/Using+SysPhs+constant+and+SysPhs+variable
- version_number: 1
- version_date: `2020-10-22T13:41:01.836+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Simulink export
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Using SysPhs variable and SysPhs constant' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="b7e41af8-633b-4809-b30a-f5dab260722b"><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Using SysPhs variable and SysPhs constant" ri:space-key="SYSMLP2024xR3" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227160254 space=SYSMLP2024xR3 version=2 -->
## PAGE 00384: Using SysPhs variable and SysPhs constant

- page_id: `227160254`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227160254/Using+SysPhs+variable+and+SysPhs+constant
- version_number: 2
- version_date: `2025-05-02T10:28:47.901+02:00`
- ancestors: SysML Plugin Documentation > Exporting to External Simulation Models > Modelica export
- labels: ['phsconstant', 'phsvariable']

### NORMALIZED CONTENT

165087022

165087027

165087020

**On this page**

**5**

165087026

##### Introduction

The «PhSConstant» and «PhSVariable» stereotypes extend the Property metaclass (see the figure below) for physical interaction and signal flow simulation. Simulation modeling specifies how numeric and boolean variable values can change in more detail than in system models. Simulation modeling distinguishes numeric variables with values that can change continuously (possibly infinitesimally) over time from those that always change discretely (finitely), possibly only at regular intervals. It also identifies variables with values that can only change between simulations (constants), rather than during simulations. For mode details, read the[OMG SysPhS specification](https://www.omg.org/spec/SysPhS/About-SysPhS/).

[IMAGE alt='' src='']

###### Simulation stereotypes.

##### Using the «PhSConstant» stereotype

Apply a «PhSConstant» stereotype to a SysML property if it has a fixed value and will not change during simulation. It is exported as a Modelica/Simulink parameter.

Block properties stereotyped by «PhSConstant» must:

- Be typed by Real, Integer, or Boolean, or one of their specializations.
- Have a multiplicity of 1, unless they are also stereotyped by a MultidimensionalElement.
- Not redefine more than one other property, which must have the same name and type and must be stereotyped by a « PhSVariable » or « PhSConstant ».

In the example below, the «PhSConstant» stereotype is applied for the *C1* [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] of the *HeatingCalculation* [CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3']and *specificHeat*, *waterVolume* [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] of the*TemperatureIncrease*[CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'].

[IMAGE alt='' src='']

###### Usage of the «PhSConstant» and «PhSVariable» stereotypes.

##### Using the «PhSVariable» stereotype

Apply the «PhSVariable» stereotype if you want to mark property as a Modelica/Simulink variable and fill in the appropriate tags (isContinuous, isConserved and changeCycle) if needed**.**

The descriptions of the «PhSVariable» stereotype [CONFLUENCE_PAGE title='Tag' space='MD2024xR3']:

- isContinuous - determines whether the property value varies continuously or discretely.
- isConserved - determines whether values of the property value are conserved or not.
- changeCycle - specifies the time interval at which a discrete property value may change.

Follow the rules below when applying «PhSVariable» stereotype:

- The property must be typed by Real, Integer, or Boolean, or one of their specializations.
- isContinuous may be true only when the stereotyped property is typed by Real or one of its specializations.
- isConserved may be true only when isContinuous is true and the stereotyped property is on a block specialized from ConservedQuantityKind.
- changeCycle may be other than zero only when isContinuous is false.
- changeCycle must be positive or zero.
- A property stereotyped by « PhSVariable » must not be stereotyped by « PhSConstant » .
- Properties stereotyped by « PhSVariable » must have a multiplicity of 1, unless they are also stereotyped by MultidimensionalElement.
- Flow properties stereotyped by « PhSVariable » that are connected and matching must have opposite directions (in/out or out/in), the same type and multiplicity, and the same value for isContinuous on the applied stereotype.
- Flow properties stereotyped by « PhSVariable » that have an "in" direction may connect to and match no more than one other flow property stereotyped by « PhSVariable » .
- A property stereotyped « PhSVariable » can redefine at most one other property. It must have the same name and type and must be stereotyped by « PhSVariable » .
- When a property stereotyped by « PhSVariable » with isContinuous=true redefines another property, the « PhSVariable » applied to the redefined property must have isContinuous=true.
- When a property stereotyped by « PhSVariable » with isContinuous=false redefines another property stereotyped by « PhSVariable » with isContinuous=false, the redefining property’s changeCycle must be an integer multiple of the redefined property’s changeCycle.

As an example, see the figure above, where the «PhSVariable» stereotype is applied for the *xlntg* [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'] of the *HeatingCalculation*[CONFLUENCE_PAGE title='Block' space='SYSMLP2024xR3'].

165092033

**Related pages**

- [CONFLUENCE_PAGE title='Stereotype' space='MD2024xR3']
- [Tag](https://docs.nomagic.com/display/MD2024xR3/Tag)

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d87d582b-b505-42da-a416-a7dd3112654f"><ac:parameter ac:name="id">165087022</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b3afd9c5-6192-43f4-923d-8d4493ece3c3"><ac:parameter ac:name="id">165087027</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f1afa240-72d5-489a-840a-c20bcc9f3076"><ac:parameter ac:name="id">165087020</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6399dc76-967f-4301-a535-968f27a09c54"><ac:parameter ac:name="maxLevel">5</ac:parameter></ac:structured-macro><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ffacb3e8-b82b-4f34-a1c9-9c448f28f251"><ac:parameter ac:name="id">165087026</ac:parameter><ac:rich-text-body><h3>Introduction</h3><p>The <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">»</span> and <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> stereotypes extend the Property metaclass (see the figure below) for physical interaction and signal flow simulation. Simulation modeling specifies how numeric and boolean variable values can change in more detail than in system models. Simulation modeling distinguishes numeric variables with values that can change continuously (possibly infinitesimally) over time from those that always change discretely (finitely), possibly only at regular intervals. It also identifies variables with values that can only change between simulations (constants), rather than during simulations. For mode details, read <span style="color: rgb(62,63,64);">the </span><a class="external-link" href="https://www.omg.org/spec/SysPhS/About-SysPhS/" rel="nofollow">OMG SysPhS specification</a><span style="color: rgb(62,63,64);">.</span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="phsvariable_phsconstant_stereotypes.png"><ri:page ri:content-title="Using SysPhs variable and SysPhs constant" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Simulation stereotypes.</h6><h3>Using the <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">»</span>  stereotype</h3><p>Apply a <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">»</span> stereotype to a SysML property if it has a fixed value and will not change during simulation. It is exported as a Modelica/Simulink parameter. </p><p>Block properties stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">»</span> must:</p><ul><li>Be typed by Real, Integer, or Boolean, or one of their specializations. </li><li>Have a multiplicity of 1, unless they are also stereotyped by a MultidimensionalElement.</li><li>Not redefine more than one other property, which must have the same name and type and must be stereotyped by a <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> or <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">».</span></li></ul><p><span style="color: rgb(51,51,51);">In the example below, the <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">» stereotype is applied for the <em>C1</em> <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> of the <em>HeatingCalculation</em> <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Block ]]></ac:plain-text-link-body></ac:link>and <em>specificHeat</em>, <em>waterVolume</em> <span style="color: rgb(51,51,51);"><ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> of the </span><em>TemperatureIncrease</em><span style="color: rgb(51,51,51);"> <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>.</span></span></span></p><p><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="phsvariable_phsConstant_stereotypes_usage.png"><ri:page ri:content-title="Using SysPhs variable and SysPhs constant" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p><h6><span style="color: rgb(51,51,51);">Usage of the <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">»</span> and <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">» stereotypes.</span></span></h6><h3>Using the <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span>  stereotype</h3><p><ac:inline-comment-marker ac:ref="8bdc8023-e933-4677-ae29-041840cc906f">Apply the <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> stereotype if you want to mark property as a Modelica/Simulink variable and fill in the appropriate tags (isContinuous, isConserved and changeCycle) if needed<strong>. </strong></ac:inline-comment-marker></p><p>The descriptions of the <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">» stereotype</span> <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Tag" /><ac:plain-text-link-body><![CDATA[tags]]></ac:plain-text-link-body></ac:link>:</p><ul><li>isContinuous - determines whether the property value varies continuously or discretely.</li><li>isConserved - determines whether values of the property value are conserved or not. </li><li>changeCycle - specifies the time interval at which a discrete property value may change.<br /><br /></li></ul><p>Follow the rules below when applying <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">» stereotype</span>:</p><ul><li>The property must be typed by Real, Integer, or Boolean, or one of their specializations. </li><li>isContinuous may be true only when the stereotyped property is typed by Real or one of its specializations. </li><li>isConserved may be true only when isContinuous is true and the stereotyped property is on a block specialized from ConservedQuantityKind. </li><li>changeCycle may be other than zero only when isContinuous is false. </li><li>changeCycle must be positive or zero.</li><li>A property stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> must not be stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSConstant<span style="color: rgb(51,51,51);">»</span>. </li><li>Properties stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> must have a multiplicity of 1, unless they are also stereotyped by MultidimensionalElement.</li><li>Flow properties stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span>  that are connected and matching must have opposite directions (in/out or out/in), the same type and multiplicity, and the same value for isContinuous on the applied stereotype.</li><li>Flow properties stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> that have an &quot;in&quot; direction may connect to and match no more than one other flow property stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span>.</li><li>A property stereotyped <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> can redefine at most one other property. It must have the same name and type and must be stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span>. </li><li>When a property stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> with isContinuous=true redefines another property, the <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">» </span>applied to the redefined property must have isContinuous=true. </li><li>When a property stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">»</span> with isContinuous=false redefines another property stereotyped by <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">» </span>with isContinuous=false, the redefining property’s changeCycle must be an integer multiple of the redefined property’s changeCycle.</li></ul><p>As an example, see the figure above, where the <span style="color: rgb(51,51,51);">«</span>PhSVariable<span style="color: rgb(51,51,51);">» stereotype is applied for the <em>xlntg</em> <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link> of the <em>HeatingCalculation</em><span style="color: rgb(51,51,51);"> <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>.</span></span></p><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><br /></span></span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="70ca1322-bebc-4af0-a655-05fd853a9e3e"><ac:parameter ac:name="id">165092033</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Stereotype" ri:space-key="MD2024xR3" /></ac:link></li><li><p class="with-breadcrumbs"><a class="current" href="https://docs.nomagic.com/display/MD2024xR3/Tag">Tag</a></p></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158527 space=SYSMLP2024xR3 version=2 -->
## PAGE 00385: Using the Model Browser

- page_id: `227158527`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158527/Using+the+Model+Browser
- version_number: 2
- version_date: `2025-05-02T10:28:17.958+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

234757312

234757315

234757314

[CONFLUENCE_PAGE title='Using the Model Browser' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f9bcfaba-be1c-4d12-ae8e-0a8790282122"><ac:parameter ac:name="id">234757312</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c6c134c5-7505-464f-a480-0548ca2e6f6c"><ac:parameter ac:name="id">234757315</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="42affe45-3341-4ea8-9d47-c935ac7446fb"><ac:parameter ac:name="id">234757314</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="6be56d74-e500-4abb-9cf3-7cbdf7a49906"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Using the Model Browser" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158836 space=SYSMLP2024xR3 version=3 -->
## PAGE 00386: Using Units

- page_id: `227158836`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158836/Using+Units
- version_number: 3
- version_date: `2025-05-02T10:28:24.305+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks
- labels: []

### NORMALIZED CONTENT

**On this page**

43

true[CONFLUENCE_PAGE title='Unit' space='SYSMLP2024xR3'] This section explains how to specify units for a Value Property, how to display or hide units, and unit symbols in various places.

##### Specifying Unit for a Value Property

When a Block has a Value Property defined, it requires a numeric value and must be typed by the [CONFLUENCE_PAGE title='Value Type' space='SYSMLP2024xR3'], either with or without ([unitless](https://docs.nomagic.com/display/SYSMLP2024xR3/Value+Type#ValueType-UnitlessValueTypes)) a specified Unit.

To specify the Unit for a Value Property

1. Select the Value Property in the Block compartments.
2. If the ISO-80000 library is not uploaded in your project, click the**ISO** button on the smart manipulator toolbar. If you work with projects older than version 18.0, which use the QUDV library and SysML 1.3 library, the ISO-80000 library will not be compatible.If you work with Teamwork projects, the ISO-80000 library is uploaded by default. [IMAGE alt='' src='']
3. Open the **Select Type** menu inone of the following way:
  - Click [IMAGE alt='' src=''].
  - Press Ctrl+T.
  - From the shortcut menu, select **Type**.
4. Select the Value Type by typing the quantity name and unit name in the following syntax: quantity name[unit name]. Unit libraries- If you cannot find a suitable Unit in the standard libraries, you can create custom Units. To learn more about creating units, refer to the [CONFLUENCE_PAGE title='Customizing Units' space='SYSMLP2024xR3'] page. 
 - You can manage the scope of provided units with the [CONFLUENCE_PAGE title='Package import' space='MD2024xR3'] feature. The unit is specified for a Value Property. As an example, see the figure below. 
[IMAGE alt='' src='']

###### The *stoppingDistance* Value Property typed by *distance[metre]* Value Type.

##### Displaying/hiding Units

After the unit is specified you can:

- Display/hide units for Value Property.[CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']
- Display/hide unit symbolsfor values.[CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']

###### value_propertyDisplaying/hiding units for Value Property

The full name of the unit (e.g. metre, kilogram) is shown by default next to the Value Property on the Block [CONFLUENCE_PAGE title='Compartments' space='MD2024xR3'].

To hide/display the full name of a unit for a Value Property

1. Select the Block shape.
2. From its shortcut menu, select **Symbol Properties**.
3. Select the **All** options display mode.
4. Find the**Show Attributes Tagged Values** option.
5. Set its value to *true* to show the unit (default), or *false*to hide it. The full name of the unit is shown/hidden next to the values in brackets in the compartments.

[IMAGE alt='' src='']

###### symbolDisplaying/hiding unit symbols for Value Property

You can show the unit symbol in brackets (e.g. (m), (kg)) next to the Value Property on the Block [CONFLUENCE_PAGE title='Compartments' space='MD2024xR3']. If the Value Property has a value defined, the unit symbol in brackets is hidden (see the figure below). >]]>[CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']

To display/hide a unit symbol next to a Value Property

1. Select the Block shape.
2. From its shortcut menu, select **Symbol Properties**.
3. Find the**Show Unit on Value Property** option.
4. Set its value to *true* to show the unit symbol, or *false*(default) to hide it. The unit symbol is shown/hidden next to the Value Property. [IMAGE alt='' src='']

###### valuesDisplaying/hiding units symbols for values

You can hide or display a unit's symbol (e.g. m, kg):

- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']

**on blockDisplaying/hiding unit symbols next to values**

You can display or hide the unit symbols (e.g. m, kg) of values in the entire project when the Unit is already defined for the Value Property and it has a value specified. For projects older than version 18.5, you must enable the **Show Units** option in the **Project Options** dialog if you want to see unit symbols. As of version 18.5, this option is enabled by default for any new projects.

show_unitsTo display/hide unit symbols next to values

1. Select **Options** > **Project**.
2. In the **Project Options** dialog, expand the **General** option group and select **SysML**.
3. Set the **Show Units** option value to *true* to show unit symbols, or *false*to hide. 
The unit symbols are shown next to the values in the compartments. [IMAGE alt='' src='']

**slotDisplaying/hiding unit symbols next to slots**

You can display a unit symbol for a slot on the Instance Specification shape by specifying it in the following ways:

- Using the **Specify Type** button from the smart manipulator toolbar[CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3'].
- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3'] .
- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3'] .

#### WARNING: Warning

Warning

The following procedures work only if the **Show Units** option is enabled. How to enable the **Show Units** option >[CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']

typeTo specify or change the unit symbol of a slot using the **Specify Type** button

1. Do one of the following:
  - Select the value in the compartment, and click the **Specify****Type** button. [IMAGE alt='' src='']
  - Right-click the value in the compartment, and select **Type**.
  - Select the value in the compartment, and press Ctrl+T.
2. Specify the new unit, or select an existing unit from the **Select Type** menu list. InformationThe list of units in the **Select Type** menu consists of those units that are defined in the Block property type, or in its subtypes. [IMAGE alt='' src='']

manuallyTo specify or change unit by typing it manually

1. Select the slot on the Instance Specification shape.
2. Click it to edit.
3. Type the required unit symbol next to the slot value.
4. Press Enter.

right-clickTo specify or change the unit using the right-click menu

1. Select the slot in the Instance Specification compartment, the row in the [CONFLUENCE_PAGE title='Instance table' space='MD2024xR3'], or the Slot in the Containment tree.
2. Right-click it, select the **Unit** button, and choose the required unit from the list. InformationThe list of units under the **Unit** button consists of those units that are defined either in the Block property type or in its subtypes.

**cells_columnsDisplaying unit symbols in the Instance table**

You can display units in the [CONFLUENCE_PAGE title='Instance table' space='MD2024xR3'] in the following ways:

- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3']

unit_in_cellTo show unit symbols in the cells of an Instance Table

1. Click the **Options** button.
2. Select the **Show Units on Values** option. 
The unit symbols are displayed next to the values in the cells.

[IMAGE alt='' src='']

#### WARNING: Warning

Warning

Show Units on Values

Show Unit

Project Options

Show Units

unit_in_columnTo show the unit symbol in the column header of the Instance Table

1. Click the **Options** button.
2. Select the **Show Units on Columns**option. 
The unit symbols are displayed on the column header.

[IMAGE alt='' src='']

**Related pages**

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="661ef7d2-5937-4034-b39a-4c87799f34b0"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="192b386e-41db-4071-aeba-5c17191b4fe2"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Unit" ri:space-key="SYSMLP2024xR3" /></ac:link></ac:parameter></ac:structured-macro> This section explains how to specify units for a Value Property, how to display or hide units, and unit symbols in various places.<br /></span></p><h3><span>Specifying Unit for a Value Property<br /></span></h3><p><span> When a Block has a Value Property defined, it requires a numeric value and must be typed by the <ac:link><ri:page ri:content-title="Value Type" ri:space-key="SYSMLP2024xR3" /></ac:link>, either with or without (<a href="https://docs.nomagic.com/display/SYSMLP2024xR3/Value+Type#ValueType-UnitlessValueTypes">unitless</a>) a specified Unit. <br /></span></p><p><span><span style="color: rgb(51,51,51);">To specify the Unit for a Value Property</span><br /></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select the Value Property in the Block compartments.</span></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">If the ISO-80000 library is not uploaded in your project, click the<strong> ISO</strong> button on the smart manipulator toolbar.</span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="b3c05294-e3a9-46ac-9f04-52320826559c"><ac:rich-text-body><ul><li><span>If you work with projects older than version 18.0, which use the QUDV library and SysML 1.3 library, the ISO-80000 library will not be compatible.</span></li><li><span><span style="color: rgb(51,51,51);">If you work with Teamwork projects, the ISO-80000 library is uploaded by default.</span></span><span><span style="color: rgb(51,51,51);"><br /></span></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><ac:image ac:height="143"><ri:attachment ri:filename="iso_button.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></p></li><li><span style="color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">Open the <strong>Select Type</strong> menu in </span></span>one of the following way:<br /></span><ul><li><span style="color: rgb(51,51,51);">Click <ac:image ac:title="Specify Type" ac:thumbnail="true" ac:alt="Specify Type" ac:height="17"><ri:attachment ri:filename="specify_type.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>.</span></li><li><span style="color: rgb(51,51,51);">Press Ctrl+T.</span></li><li><span style="color: rgb(51,51,51);">From the shortcut menu, select <strong>Type</strong>.<br /></span></li></ul></li><li><p><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">Select the Value Type by t</span></span>yping the quantity name and unit name in the following syntax: quantity name[unit name].</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="70fa28d6-f24e-4612-acd8-2581559432b8"><ac:parameter ac:name="title">Unit libraries</ac:parameter><ac:rich-text-body><span style="color: rgb(51,51,51);"><span> - If you cannot find a suitable Unit in the standard libraries, you can create custom Units. To learn more about creating units, refer to the <ac:link><ri:page ri:content-title="Customizing Units" ri:space-key="SYSMLP2024xR3" /></ac:link> page.<br /> - You can manage the scope of provided units with the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Package import" /><ac:plain-text-link-body><![CDATA[Package Import]]></ac:plain-text-link-body></ac:link> feature.<br /></span></span></ac:rich-text-body></ac:structured-macro><p>The unit is specified for a Value Property. As an example, see the figure below.<br /><ac:image ac:align="center"><ri:attachment ri:filename="selecting_unit_for_value.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></li></ol><h6 style="text-align: center;"><span>The <em>stoppingDistance</em> Value Property typed by <em>distance[metre]</em> Value Type.</span></h6><h3>Displaying/hiding Units</h3><p>After the unit is specified you can:</p><ul><li><span class="toc-item-body"><ac:link ac:anchor="value_property"><ac:link-body><span class="toc-link">Display/hide units for</span> Value Property.</ac:link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link></span></li><li><span class="toc-item-body"><ac:link ac:anchor="symbol"><ac:plain-text-link-body><![CDATA[Display/hide unit symbols for Value Property.]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link><br /></span></li><li><ac:link ac:anchor="values"><ac:link-body><span class="toc-item-body"><span class="toc-link">Display/hide unit symbols </span>for values</span>.</ac:link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6f20e55b-f20c-4708-abc7-242f81495829"><ac:parameter ac:name="">value_property</ac:parameter></ac:structured-macro>Displaying/hiding units for Value Property</h4><p>The full name of the unit (e.g. metre, kilogram) is shown by default next to the Value Property on the Block <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Compartments" /><ac:plain-text-link-body><![CDATA[compartments]]></ac:plain-text-link-body></ac:link>.</p><p><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">To hide/display the full name of a unit</span> <span style="color: rgb(51,51,51);">for a Value Property</span><br /></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select the Block shape.</span></li><li><span style="color: rgb(51,51,51);">From its shortcut menu, select <strong>Symbol Properties</strong>.</span></li><li><span style="color: rgb(51,51,51);">Select the <strong>All</strong> options display mode.</span></li><li><span style="color: rgb(51,51,51);">Find the<strong> Show Attributes Tagged Values</strong> option.</span></li><li><span style="color: rgb(51,51,51);">Set its value to <em>true</em> to show the unit (default), or <em>false </em>to hide it.</span><br /><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">The full name of the unit is shown/hidden next to the values in brackets in the compartments.</span></span></li></ol><p><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="show_attributes_tagged_values_option.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></span></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="44d8a4ce-feea-4b07-a4b5-950b0ee8d0f1"><ac:parameter ac:name="">symbol</ac:parameter></ac:structured-macro>Displaying/hiding unit symbols for Value Property</h4><p><span style="color: rgb(51,51,51);">You can show the unit symbol in brackets (e.g. (m), (kg)) next to the Value Property on the Block <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Compartments" /><ac:plain-text-link-body><![CDATA[compartments]]></ac:plain-text-link-body></ac:link>. If the Value Property has a value defined, the unit symbol in brackets is hidden (see the figure below). <ac:link ac:anchor="on block"><ac:plain-text-link-body><![CDATA[How to show unit symbols next to values >>]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link><br /></span></p><p><span style="color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">To display/hide a unit</span> <span style="color: rgb(51,51,51);">symbol next to a Value Property</span></span></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select the Block shape.</span></li><li><span style="color: rgb(51,51,51);">From its shortcut menu, select <strong>Symbol Properties</strong>.</span></li><li><span style="color: rgb(51,51,51);">Find the<strong> Show Unit on Value Property</strong> option.</span></li><li><span style="color: rgb(51,51,51);">Set its value to <em>true</em> to show the unit symbol, or <em>false </em>(default) to hide it.</span><br /><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">The unit symbol is shown/hidden next to the Value Property.</span></span><br /><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="unit_symbol_in_brackets.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></span></li></ol><p><span style="color: rgb(51,51,51);"><br /></span></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="0b9ec9ed-a16d-4567-8880-c314ea9fcdde"><ac:parameter ac:name="">values</ac:parameter></ac:structured-macro>Displaying/hiding units symbols for values</h4><p>You can hide or display a unit's symbol (e.g. m, kg):</p><ul><li><ac:link ac:anchor="on block"><ac:plain-text-link-body><![CDATA[Next to values in the whole project.]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link ac:anchor="slot"><ac:plain-text-link-body><![CDATA[Next to slots on the Instance Specification shape.]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link ac:anchor="cells_columns"><ac:plain-text-link-body><![CDATA[In cells and column headers of the Instance Table.]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link><span style="color: rgb(51,51,51);"><br /><br /></span></li></ul><p><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6ffa5635-8dcd-4464-bd41-934624c5e374"><ac:parameter ac:name="">on block</ac:parameter></ac:structured-macro>Displaying/hiding unit symbols next to values<br /></strong></p><p>You can display or hide the unit symbols (e.g. m, kg) of values in <span style="color: rgb(51,51,51);">the entire project</span> when the Unit is already defined for the Value Property and it has a value specified. For projects older than version 18.5, you must enable the <span style="color: rgb(51,51,51);"><strong>Show Units</strong> option in the <strong>Project Options</strong> dialog if you want to see unit symbols. As of version 18.5, this option is enabled by default for any new projects.</span><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"><br /></span></span></p><p><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="e53d24f9-aeb7-4e01-a653-b1dd0a4572ef"><ac:parameter ac:name="">show_units</ac:parameter></ac:structured-macro>To display/hide unit</span> <span style="color: rgb(51,51,51);">symbols next to values</span><br /></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select <strong>Options</strong> &gt; <strong>Project</strong>.</span></li><li><span style="color: rgb(51,51,51);">In the <strong>Project Options</strong> dialog, expand the <strong>General</strong> option group and select <strong>SysML</strong>.</span></li><li><p><span style="color: rgb(51,51,51);">Set the <strong>Show Units</strong> option value to <em>true</em> to show unit symbols, or <em>false </em>to hide.</span><br /><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">The unit symbols are shown next to the values in the compartments.</span><br /></span></p><p><ac:image><ri:attachment ri:filename="show_units_option.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p class="auto-cursor-target"><br /></p></li></ol><p><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="45461112-3769-496f-8c1d-f667cb9d53c1"><ac:parameter ac:name="">slot</ac:parameter></ac:structured-macro>Displaying/hiding unit symbols next to slots<br /></strong></p><p>You can display a unit symbol for a slot on the Instance Specification shape by specifying it in the following ways:</p><ul><li><span class="confluence-link" style="color: rgb(51,51,51);"><ac:link ac:anchor="type"><ac:link-body><span class="confluence-link">Using the <strong>Specify Type</strong> button from the smart manipulator toolbar</span></ac:link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link>.</span></li><li><ac:link ac:anchor="manually"><ac:plain-text-link-body><![CDATA[Typing the appropriate unit symbol directly next to slot value]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link>.</li><li><ac:link ac:anchor="right-click"><ac:plain-text-link-body><![CDATA[From the right-click menu]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link>.<br /><br /></li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1f06fca2-e4aa-4fa6-a65e-80664466287c"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>The following procedures work only if the <strong>Show Units</strong> option is enabled. <span style="color: rgb(51,51,51);"><ac:link ac:anchor="show_units"><ac:link-body>How to enable the <strong>Show Units</strong> option &gt;</ac:link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link><br /></span></p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(0,0,0);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="45782e97-40db-400c-b3fa-48bb220c1232"><ac:parameter ac:name="">type</ac:parameter></ac:structured-macro><span style="color: rgb(51,51,51);">To specify or change the unit symbol of a slot using the <strong>Specify Type</strong> button</span><br /></span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Do one of the following:<br /></span><ul><li><span style="color: rgb(51,51,51);">Select the value in the compartment, and click the <strong>Specify</strong><strong> Type</strong> button.</span><br /><span style="color: rgb(51,51,51);">  <ac:image ac:title="The Specify Type button from smart manipulator toolbar." ac:alt="The Specify Type button from smart manipulator toolbar."><ri:attachment ri:filename="specify_value_type.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></li><li><span style="color: rgb(51,51,51);">Right-click the value in the compartment, and select <strong>Type</strong>. </span></li><li><span style="color: rgb(51,51,51);">Select the value in the compartment, and press Ctrl+T.</span></li></ul></li><li><p><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">Specify the new unit, or select an existing unit from the <strong>Select Type</strong> menu list.</span><br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="af7b6b38-79ce-4ab2-a6b5-eca3eda9db0f"><ac:parameter ac:name="title">Information</ac:parameter><ac:rich-text-body><p>The list of units in the <strong>Select Type</strong> menu consists of those units that are defined in the Block property type, or in its subtypes.</p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(0,0,0);"><ac:image ac:title="The Select Type dialog opens automatically when specifying unit." ac:alt="The Select Type dialog opens automatically when specifying unit."><ri:attachment ri:filename="specify_unit.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span><span style="color: rgb(51,51,51);"> <br /></span></p><p><span style="color: rgb(51,51,51);"><br /></span></p></li></ol><p><span style="color: rgb(51,51,51);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9aecab09-acdd-471e-9f17-20276ef29709"><ac:parameter ac:name="">manually</ac:parameter></ac:structured-macro>To specify or change unit by typing it manually</span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select the slot on the Instance Specification shape.</span></li><li><span style="color: rgb(51,51,51);">Click it to edit.</span></li><li><span style="color: rgb(51,51,51);">Type the required unit symbol next to the slot value.</span></li><li><span style="color: rgb(51,51,51);">Press Enter.<br /></span></li></ol><p><span style="color: rgb(51,51,51);"><br /></span></p><p><span style="color: rgb(51,51,51);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="4c8af13e-24fe-4c80-9cfe-1b62acc63d01"><ac:parameter ac:name="">right-click</ac:parameter></ac:structured-macro>To specify or change the unit using the right-click menu</span></p><hr /><ol><li><span style="color: rgb(51,51,51);">Select the slot in the Instance Specification compartment, the row in the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance table" /></ac:link>, or the Slot in the Containment tree.</span></li><li><p><span style="color: rgb(51,51,51);">Right-click it, select the <strong>Unit</strong> button, and choose the required unit from the list.</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fe649446-f729-4ffb-8837-64caaf21b8c9"><ac:parameter ac:name="title">Information</ac:parameter><ac:rich-text-body><p>The list of units under the <strong>Unit</strong> button consists of those units that are defined either in the Block property type or in its subtypes.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p><strong><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7e6fd710-1cd2-4e29-9a42-aff72f795328"><ac:parameter ac:name="">cells_columns</ac:parameter></ac:structured-macro>Displaying unit symbols in the Instance table</strong><span style="color: rgb(0,0,0);"><br /></span></p><p><span style="color: rgb(51,51,51);">You can display units in the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance table" /></ac:link> in the following ways:</span></p><ul><li><span style="color: rgb(51,51,51);"><ac:link ac:anchor="unit_in_cell"><ac:plain-text-link-body><![CDATA[Next to the values in cells.]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link></span></li><li><span style="color: rgb(51,51,51);"><ac:link ac:anchor="unit_in_column"><ac:plain-text-link-body><![CDATA[On column header of the table.]]></ac:plain-text-link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link><br /></span></li></ul><p><span style="color: rgb(51,51,51);"><br /></span></p><p><span style="color: rgb(51,51,51);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="90e96b33-f49e-4b25-a9ea-528bed5ff7d5"><ac:parameter ac:name="">unit_in_cell</ac:parameter></ac:structured-macro>To show unit symbols in the cells of an Instance Table</span></p><hr /><ol><li><p><span style="color: rgb(51,51,51);">Click the <strong>Options</strong> button.</span></p></li><li><p><span style="color: rgb(51,51,51);">Select the <strong>Show Units on Values</strong> option.<br />The unit symbols are displayed next to the values in the cells.<br /></span></p></li></ol><p><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="show_units_on_values.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image><br /></span></p><p><span style="color: rgb(51,51,51);"> </span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="5355ab6d-2428-4f15-97b1-2e904096dadf"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><span style="color: rgb(51,51,51);">The<strong> Show Units on Values</strong> option does not allow you to specify units directly in the row of the Instance Table. </span><span style="color: rgb(51,51,51);">If you want to edit them, enable the <strong>Show Unit</strong> option in the <strong>Project Options</strong> dialog. <ac:link ac:anchor="show_units"><ac:link-body>How to enable <strong>Show Units</strong> option &gt;</ac:link-body><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link> <br /></span></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(51,51,51);"><br /></span></p><p><span style="color: rgb(51,51,51);"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="a0eca118-d180-4d72-95db-f6338b07ad98"><ac:parameter ac:name="">unit_in_column</ac:parameter></ac:structured-macro>To show the unit symbol in the column header of the Instance Table</span></p><hr /><ol><li><p><span style="color: rgb(51,51,51);">Click the <strong>Options</strong> button.</span></p></li><li><p><span style="color: rgb(51,51,51);">Select the <strong>Show Units on Columns </strong>option.<br />The unit symbols are displayed on the column header.</span></p></li></ol><p><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="show_units_on_columns.png"><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong class="confluence-link" style="letter-spacing: 0.0px;">Related pages</strong></p><p><strong class="confluence-link"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5958aa0b-73df-495c-a542-7c09eef3ebd1" /></strong></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159386 space=SYSMLP2024xR3 version=2 -->
## PAGE 00387: Validation

- page_id: `227159386`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159386/Validation
- version_number: 2
- version_date: `2025-05-02T10:28:34.922+02:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Solvers of invalid elements

1357269946

#### CONTENT-COLUMN: Solvers of invalid elements

1357269948

219567689

**On this page**

43

#### CONTENT-BLOCK: Solvers of invalid elements

1357269947

##### Purpose

Validation checks the accuracy, completeness, and correctness of a model, marks invalid elements in the model, and suggests solutions.

##### Validation suites

Models are validated against a set of validation rules. Each validation rule captures an imperative condition that must be checked against the model. Validation rules are grouped into meaningful groups called validation suites. There are predefined validation suites that you can customize. You can also create your own rules and group them into suites. Some validation rules are active; that is, they run all the time. Validation rules and suites can be exported into a separate project in order to reuse them. They are stored in the Teamwork Server or Teamwork Cloud server for exchange.

- [CONFLUENCE_PAGE title='Predefined validation suites' space='MD2024xR3']>]]>
- [CONFLUENCE_PAGE title='SysML validation suites' space='SYSMLP2024xR3']>]]>
- [CONFLUENCE_PAGE title='Active validation suites' space='MD2024xR3']>]]>
- [CONFLUENCE_PAGE title='SysML active validation suites' space='SYSMLP2024xR3']>]]>
- [CONFLUENCE_PAGE title='Requirements validation suites' space='CRMP2024xR3']>]]>
- [CONFLUENCE_PAGE title='Creating validation suites' space='SYSMLP2024xR3']>]]>
- [CONFLUENCE_PAGE title='Creating new validation rules' space='SYSMLP2024xR3']>]]>
- [CONFLUENCE_PAGE title='Global validation rules' space='SYSMLP2024xR3']>]]>

##### Validating your model

The validation can run on the entire model or on a selected part of it. All the elements in that scope are checked against relevant validation rules, and elements that violate these rules are reported in the [CONFLUENCE_PAGE title='Validation Results panel' space='SYSMLP2024xR3']**Validation Results** panel. They are also marked in the [CONFLUENCE_PAGE title='Model Browser' space='SYSMLP2024xR3']Model Browser, and their symbols are highlighted. Diagrams, tables, matrices, and relation maps displaying these highlighted symbols have the validation results marker bar.

- [CONFLUENCE_PAGE title='Starting the validation' space='SYSMLP2024xR3']>]]>
- [CONFLUENCE_PAGE title='Validation results marker bar' space='SYSMLP2024xR3']Learn more about validation results marker bar >>
- [CONFLUENCE_PAGE title='Validation Results panel' space='SYSMLP2024xR3']Learn more about Validation Results panel >>
- [CONFLUENCE_PAGE title='Validation dialog' space='SYSMLP2024xR3']>]]>

##### Invalid elements representation

The invalid elements are marked as follows:

- [ATTACHMENT filename='error_icon.png'] - error or fatal error.
- [ATTACHMENT filename='warning_icon.png'] - warning.
- [ATTACHMENT filename='info_icon.png'] - debug or info.

[CONFLUENCE_PAGE title='Customizing severity levels' space='SYSMLP2024xR3']>]]>

You can see invalid elements in the following areas:

- In the [CONFLUENCE_PAGE title='Model Browser' space='SYSMLP2024xR3']Model Browser an invalid element is marked with a small symbol that depends on the failure severity. [ATTACHMENT filename='invalid_element_in_model_brower.png']
- On the [CONFLUENCE_PAGE title='Understanding the user interface' space='SYSMLP2024xR3'] an invalid symbol is highlighted. [ATTACHMENT filename='invalid_symbol_on_diagram_pane.png']
- In the [CONFLUENCE_PAGE title='Validation results marker bar' space='SYSMLP2024xR3'] every marker of an invalid symbol is colored according to the violation severity. [ATTACHMENT filename='invalid_symbol_in_validation_results_marker_bar.png']
- On the [CONFLUENCE_PAGE title='Understanding the user interface' space='SYSMLP2024xR3'] the failure indicator displays the severity icon, number of errors, and the first letter of the error severity (F - fatal error; E - error; W - warning; D - debug; I - info). 
[IMAGE alt='' src='']

#### NOTE: Solvers of invalid elements

Solvers of invalid elements

You can analyze invalid elements and solve problems by selecting appropriate commands from the invalid element or symbol shortcut menu or in the [CONFLUENCE_PAGE title='Validation Results panel' space='SYSMLP2024xR3']**Validation Results** panel.

1357269945

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4481d76a-f8ba-4fe4-a38e-b3a054ff0fb5"><ac:parameter ac:name="id">1357269946</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="7c32b627-d8f0-4305-a15b-9d7e8433c01a"><ac:parameter ac:name="id">1357269948</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1919a7b6-48d2-4539-8641-7f2bbca731c6"><ac:parameter ac:name="id">219567689</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="2d308b7b-962b-451c-b529-71f9bc667d22"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7ae9a492-7cbf-4e2e-80da-098ef9fedc7e"><ac:parameter ac:name="id">1357269947</ac:parameter><ac:rich-text-body><h3>Purpose</h3><p>Validation checks the accuracy, completeness, and correctness of a model, marks invalid elements in the model, and suggests solutions.</p><h3>Validation suites</h3><p>Models are validated against a set of validation rules. Each validation rule captures an imperative condition that must be checked against the model. Validation rules are grouped into meaningful groups called validation suites. There are predefined validation suites that you can customize. You can also create your own rules and group them into suites. Some validation rules are active; that is, they run all the time. Validation rules and suites can be exported into a separate project in order to reuse them. They are stored in the Teamwork Server or Teamwork Cloud server for exchange.</p><ul><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Predefined validation suites" /><ac:plain-text-link-body><![CDATA[Learn more about MagicDraw predefined validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="SysML validation suites" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more about SysML validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Active validation suites" /><ac:plain-text-link-body><![CDATA[Learn more about MagicDraw active validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="SysML active validation suites" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more about SysML active validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Requirements validation suites" /><ac:plain-text-link-body><![CDATA[Learn more about Requirements validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Creating validation suites" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to create new validation suites >>]]></ac:plain-text-link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Creating new validation rules" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to create new validation rule >>]]></ac:plain-text-link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Global validation rules" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more about global validation rules >>]]></ac:plain-text-link-body></ac:link></span></li></ul><h3>Validating your model</h3><p>The validation can run on the entire model or on a selected part of it. All the elements in that scope are checked against relevant validation rules, and elements that violate these rules are reported in the <ac:link><ri:page ri:content-title="Validation Results panel" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link"><strong>Validation Results</strong> panel</span></ac:link-body></ac:link>. They are also marked in the <ac:link><ri:page ri:content-title="Model Browser" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">Model Browser</span></ac:link-body></ac:link>, and their symbols are highlighted. Diagrams, tables, matrices, and relation maps displaying these highlighted symbols have the <span class="confluence-link">validation results marker bar</span>.</p><ul><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Starting the validation" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to start the validation >>]]></ac:plain-text-link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Validation results marker bar" ri:space-key="SYSMLP2024xR3" /><ac:link-body>Learn more about <span class="current">validation results marker bar &gt;&gt;</span></ac:link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Validation Results panel" ri:space-key="SYSMLP2024xR3" /><ac:link-body>Learn more about <span class="current">Validation Results panel &gt;&gt;</span></ac:link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Validation dialog" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn more about Validation dialog >>]]></ac:plain-text-link-body></ac:link></span></li></ul><h3>Invalid elements representation</h3><p>The invalid elements are marked as follows:</p><ul><li><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="error_icon.png"><ri:page ri:content-title="Validation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> - error or fatal error.</li><li><ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="warning_icon.png"><ri:page ri:content-title="Validation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> - warning.</li><li><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="info_icon.png"><ri:page ri:content-title="Validation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image> - debug or info.<br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d02a399a-e347-4ed9-a562-d89caa67449f"><ac:rich-text-body><p><span class="confluence-link"><ac:link><ri:page ri:content-title="Customizing severity levels" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to customize severity levels >>]]></ac:plain-text-link-body></ac:link></span></p></ac:rich-text-body></ac:structured-macro><p>You can see invalid elements in the following areas:</p><ul><li>In the <ac:link><ri:page ri:content-title="Model Browser" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">Model Browser</span></ac:link-body></ac:link> an invalid element is marked with a small symbol that depends on the failure severity.<br /><ac:image><ri:attachment ri:filename="invalid_element_in_model_brower.png"><ri:page ri:content-title="Validation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>On the <ac:link><ri:page ri:content-title="Understanding the user interface" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link> an invalid symbol is highlighted.<br /><ac:image><ri:attachment ri:filename="invalid_symbol_on_diagram_pane.png"><ri:page ri:content-title="Validation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li>In the <ac:link><ri:page ri:content-title="Validation results marker bar" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[validation results marker bar]]></ac:plain-text-link-body></ac:link> every marker of an invalid symbol is colored according to the violation severity.<br /><ac:image><ri:attachment ri:filename="invalid_symbol_in_validation_results_marker_bar.png"><ri:page ri:content-title="Validation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">On the <ac:link><ri:page ri:content-title="Understanding the user interface" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[status bar]]></ac:plain-text-link-body></ac:link> the failure indicator displays the severity icon, number of errors, and the first letter of the error severity (F - fatal error; E - error; W - warning; D - debug; I - info).<br /><ac:image ac:thumbnail="true" ac:height="81"><ri:attachment ri:filename="example_of_error.png"><ri:page ri:content-title="Validation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b6e9bd0-8afb-4361-9b9f-432a6b38dbdb"><ac:parameter ac:name="title">Solvers of invalid elements</ac:parameter><ac:rich-text-body><p>You can analyze invalid elements and solve problems by selecting appropriate commands from the invalid element or symbol shortcut menu or in the <ac:link><ri:page ri:content-title="Validation Results panel" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link"><strong>Validation Results</strong> panel</span></ac:link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6b5c7957-4e28-49c4-b8aa-d671d858ab9d"><ac:parameter ac:name="id">1357269945</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="351b05b9-7df2-4a0d-b1d3-8a04a32838c6" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159616 space=SYSMLP2024xR3 version=2 -->
## PAGE 00388: Validation dialog

- page_id: `227159616`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159616/Validation+dialog
- version_number: 2
- version_date: `2025-05-02T10:28:37.803+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation
- labels: []

### NORMALIZED CONTENT

223327072

223327074

223327071

**On this page**

43

223327073

[CONFLUENCE_PAGE title='Validation dialog' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="38cb685e-d44f-4e93-9111-4e905e893d76"><ac:parameter ac:name="id">223327072</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="efb37f05-a1e5-4ba4-b2a8-9de5cb621728"><ac:parameter ac:name="id">223327074</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="28368d16-f915-446d-abec-f1ad696150c0"><ac:parameter ac:name="id">223327071</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="52157cda-fd8e-48c3-82f5-fd2bc153f3c5"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="42fc8d3b-f468-4f72-9ac1-a00c7f16e235"><ac:parameter ac:name="id">223327073</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="d4fc9d7a-ac23-400b-984a-a45c7836ee48"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Validation dialog" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159614 space=SYSMLP2024xR3 version=2 -->
## PAGE 00389: Validation results marker bar

- page_id: `227159614`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159614/Validation+results+marker+bar
- version_number: 2
- version_date: `2025-05-02T10:28:37.022+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Validation results marker bar' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="4872f13c-46bd-4a70-94cf-064b40c1d226"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Validation results marker bar" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227159615 space=SYSMLP2024xR3 version=2 -->
## PAGE 00390: Validation Results panel

- page_id: `227159615`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159615/Validation+Results+panel
- version_number: 2
- version_date: `2025-05-02T10:28:37.295+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation
- labels: []

### NORMALIZED CONTENT

223258400

223258402

223258399

**On this page**

43

223258401

[CONFLUENCE_PAGE title='Validation Results panel' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a8478939-f8a3-454e-bdcf-57c1a762a41c"><ac:parameter ac:name="id">223258400</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="80e66886-0f1f-4de5-85ea-3ad41124aa08"><ac:parameter ac:name="id">223258402</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="39f4edb8-3f12-4f16-8aea-1dffe613bd8a"><ac:parameter ac:name="id">223258399</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ac3ae89a-5223-44af-bcc6-8ef411bafeee"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4ca3209a-8c8e-4d2e-9cbd-d5b3809d07ff"><ac:parameter ac:name="id">223258401</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="d9db98ba-2ecd-4c01-86c1-a95418183f80"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Validation Results panel" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159435 space=SYSMLP2024xR3 version=1 -->
## PAGE 00391: Validation rules of Activities

- page_id: `227159435`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159435/Validation+rules+of+Activities
- version_number: 1
- version_date: `2024-01-29T12:10:53.332+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belong to active and passive*Activites*validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belong to active and passive </span><em>Activites</em><span style="color: rgb(62,63,64);"> validation suite.</span></p><p><span style="color: rgb(62,63,64);"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8b218e6c-0974-402c-8d53-a799fccf94f9" /></span></p>
````

<!--NOMAGIC_PAGE id=227159506 space=SYSMLP2024xR3 version=1 -->
## PAGE 00392: Validation rules of Allocations

- page_id: `227159506`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159506/Validation+rules+of+Allocations
- version_number: 1
- version_date: `2024-01-29T11:22:37.737+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Allocations***validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Allocations</em></span><span style="color: rgb(62,63,64);"><em> </em>validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="231e3b0d-f393-4be4-baaf-36c4da9a2ad1" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159565 space=SYSMLP2024xR3 version=1 -->
## PAGE 00393: Validation rules of Behavior to Structure Synchronization

- page_id: `227159565`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159565/Validation+rules+of+Behavior+to+Structure+Synchronization
- version_number: 1
- version_date: `2024-01-29T09:35:53.667+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belong to the passive Behavior to Structure Synchronization**validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belong to <ac:inline-comment-marker ac:ref="b3a26d4c-e766-4621-9600-30ab00191223">the passive</ac:inline-comment-marker> Behavior to Structure Synchronization</span><span style="color: rgb(62,63,64);"><em> </em></span><span style="color: rgb(62,63,64);">validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d95b5232-42b2-4a7b-b9e2-6f35266387dc" /></p>
````

<!--NOMAGIC_PAGE id=227159514 space=SYSMLP2024xR3 version=1 -->
## PAGE 00394: Validation rules of Blocks

- page_id: `227159514`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159514/Validation+rules+of+Blocks
- version_number: 1
- version_date: `2024-01-29T11:41:16.563+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Blocks***validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Blocks</em></span><span style="color: rgb(62,63,64);"><em> </em>validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="6672bfd9-d612-40b7-a913-8d33bdf79a0c" /></p>
````

<!--NOMAGIC_PAGE id=227159572 space=SYSMLP2024xR3 version=1 -->
## PAGE 00395: Validation rules of Contextual Relationships

- page_id: `227159572`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159572/Validation+rules+of+Contextual+Relationships
- version_number: 1
- version_date: `2021-01-01T08:29:28.840+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Contextual Relationships***validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Contextual Relationships</em></span><span style="color: rgb(62,63,64);"><em> </em>validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="911a68ce-172a-45e2-b479-369ea5733e9d" /></p>
````

<!--NOMAGIC_PAGE id=227159577 space=SYSMLP2024xR3 version=1 -->
## PAGE 00396: Validation rules of Non-normative Extensions

- page_id: `227159577`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159577/Validation+rules+of+Non-normative+Extensions
- version_number: 1
- version_date: `2024-01-29T11:46:49.322+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides the detailed descriptions of all validation rules that belongs to active and passive *Non-normative Extensions* validation suite.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides the detailed descriptions of all validation rules that belongs to active and passive <em>Non-normative Extensions</em> validation suite.</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e46f07c5-69de-43d0-9777-938fcd3fad23" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=227159555 space=SYSMLP2024xR3 version=1 -->
## PAGE 00397: Validation rules of Ports and Flows

- page_id: `227159555`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159555/Validation+rules+of+Ports+and+Flows
- version_number: 1
- version_date: `2024-01-29T11:27:52.689+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > SysML validation rules
- labels: []

### NORMALIZED CONTENT

This section provides detailed descriptions of all validation rules that belong to the active and passive*Ports and Flows*validation suites.

The list below displays only a few SysML validation rules. The rest are under construction.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(62,63,64);">This section provides detailed descriptions of all validation rules that belong to the active and passive </span><em>Ports and Flows</em><span style="color: rgb(62,63,64);"> validation suites.</span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="733f4481-2f2a-40f1-a1f4-cb11f89284db"><ac:rich-text-body><p>The list below displays only a few SysML validation rules. The rest are under construction.</p></ac:rich-text-body></ac:structured-macro><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="fdcdea8c-a1b3-400e-bacb-d833a3065ebe" /></p>
````

<!--NOMAGIC_PAGE id=227159619 space=SYSMLP2024xR3 version=2 -->
## PAGE 00398: Validation Suites dialog

- page_id: `227159619`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159619/Validation+Suites+dialog
- version_number: 2
- version_date: `2025-05-02T10:28:38.434+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Validation > Custom validation > Creating validation suites
- labels: []

### NORMALIZED CONTENT

223440474

223440476

223440473

**On this page**

43

223440475

[CONFLUENCE_PAGE title='Validation Suites dialog' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ba0a8bbf-c1fb-433d-9034-8ca20a32b991"><ac:parameter ac:name="id">223440474</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="2bd821ba-56a6-4878-a7c2-9d16649a1d86"><ac:parameter ac:name="id">223440476</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e4dbfe45-9fb3-4aa9-ab0d-ff80ffccafc4"><ac:parameter ac:name="id">223440473</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="0bfa8b93-86d0-4c58-857a-96caab59297e"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e7e054aa-365e-4719-86fd-5cb0a541f90f"><ac:parameter ac:name="id">223440475</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="c6f40a77-8a44-4c5c-b87c-6934baf0712d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Validation Suites dialog" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158878 space=SYSMLP2024xR3 version=1 -->
## PAGE 00399: Value Propagation

- page_id: `227158878`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158878/Value+Propagation
- version_number: 1
- version_date: `2017-04-27T14:20:50.479+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling structure with Blocks > Initial Values
- labels: []

### NORMALIZED CONTENT

The value propagation mechanism enables values that are not overridden by the values from the selected context in the *initialValue* compartment to be displayed. Assuming the property and the Value Propagation options are enabled, the value available in the next context will be used to reconfigure the property if there is no value in the selected context to reconfigure the property. However, if there is no value available in any context, the class-level default value will be displayed in the *initialValue* compartment, indicating that the property is not reconfigured at all.

The value propagation mechanism is enabled by default. To disable this mechanism, follow the procedure below.

To disable the value propagation mechanism

1. On the main toolbar, click Options > Project . .
2. In the Project Options dialog, select General > SysML .
3. Select the Propagate SysML Values property value to false .
4. Click OK .

#### TIP: Example when the value propagation mechanism is enabled

Example when the value propagation mechanism is enabled

In the UniverseContext package, only the value of x of a Location is reconfigured to 3 in the UniverseContext context. The values of y and z are not set by the selected context. Since the value propagation is enabled, the next context, Universe, is considered. In the Universe context, the value of z is set to 2. However, the value of y is still missing; therefore, the next context, Thing, is considered. In the Thing context, the value of y is set to 1. Now, all attributes of the Location are set as follows:

- x = 3
- y = 1
- z = 2

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>The value propagation mechanism enables values that are not overridden by the values from the selected context in the <em>initialValue</em> compartment to be displayed. Assuming the property and the Value Propagation options are enabled, the value available in the next context will be used to reconfigure the property if there is no value in the selected context to reconfigure the property. However, if there is no value available in any context, the class-level default value will be displayed in the <em>initialValue</em> compartment, indicating that the property is not reconfigured at all.</p><p>The value propagation mechanism is enabled by default. To disable this mechanism, follow the procedure below.</p><p>To disable the value propagation mechanism</p><hr /><ol><li>On the main toolbar, click <strong>Options</strong> &gt; <strong>Project</strong>. .</li><li>In the <strong>Project Options</strong> dialog, select <strong>General</strong> &gt; <strong>SysML</strong>.</li><li>Select the <strong>Propagate SysML Values</strong> property value to<em>false</em>.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9bc5f836-d58e-41be-8162-97be77a1bb60"><ac:parameter ac:name="title">Example when the value propagation mechanism is enabled</ac:parameter><ac:rich-text-body><p>In the UniverseContext package, only the value of x of a Location is reconfigured to 3 in the UniverseContext context. The values of y and z are not set by the selected context. Since the value propagation is enabled, the next context, Universe, is considered. In the Universe context, the value of z is set to 2. However, the value of y is still missing; therefore, the next context, Thing, is considered. In the Thing context, the value of y is set to 1. Now, all attributes of the Location are set as follows:</p><ul><li>x = 3</li><li>y = 1</li><li>z = 2</li></ul><p><ac:image><ri:attachment ri:filename="image2017-4-25_11-26-56.png"><ri:page ri:content-title="Value Propagation" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159790 space=SYSMLP2024xR3 version=1 -->
## PAGE 00400: Value Property

- page_id: `227159790`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159790/Value+Property
- version_number: 1
- version_date: `2020-03-24T06:43:28.145+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

230681161

230681163

230681162

A Value Property is a property that specifies the quantitative property of its containing Block. Every Value Property has composite AggregationKind and is typed by a SysML Value Type. Value Properties are displayed in the **values** compartment.

[IMAGE alt='' src='']

The name of the Value Property must be without space. Otherwise, the [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3'] will not calculate results correctly.

230681160

**Related diagrams**

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8b3d4113-3f5b-434c-93d6-8b4de01e665d"><ac:parameter ac:name="id">230681161</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="4572af5d-42c0-4f16-afa6-6d486ce349d7"><ac:parameter ac:name="id">230681163</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cd91460d-415c-40bb-9343-ddb1680bf187"><ac:parameter ac:name="id">230681162</ac:parameter><ac:rich-text-body><p>A Value Property is a property that specifies the quantitative property of its containing Block. Every Value Property has composite AggregationKind and is typed by a SysML Value Type. Value Properties are displayed in the <strong>values</strong> compartment.</p><p><ac:image ac:title="Value Property" ac:alt="Value Property"><ri:attachment ri:filename="value_property.png"><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="f26a2d68-717d-4d57-9e80-6696c24ebff9"><ac:rich-text-body><p>The name of the Value Property must be without space. Otherwise, the <ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link> will not calculate results correctly.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d4b78eda-b93a-4f10-ab43-64242e53cde1"><ac:parameter ac:name="id">230681160</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related diagrams</strong></p><ul><li class="auto-cursor-target"><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159792 space=SYSMLP2024xR3 version=2 -->
## PAGE 00401: Value Type

- page_id: `227159792`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159792/Value+Type
- version_number: 2
- version_date: `2025-05-02T10:28:44.313+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

133530759

133530762

133530760

A Value Type is defined as a stereotype of UML Data Type to establish a more neutral term for system values that may never be given a concrete data representation. A Value Type adds an ability to carry a [CONFLUENCE_PAGE title='Unit' space='SYSMLP2024xR3']unitsof measure of a [CONFLUENCE_PAGE title='Quantity Kind' space='SYSMLP2024xR3'] associated with the value.

Use the [CONFLUENCE_PAGE title='Using QUDV model library' space='SYSMLP2024xR3'] to find all standard value types.

[IMAGE alt='' src='']

When specifying the Value Type for a [CONFLUENCE_PAGE title='Value Property' space='SYSMLP2024xR3'], you can select one of the following:

- Unitless Value Type.
- Value Type with specified [CONFLUENCE_PAGE title='Unit' space='SYSMLP2024xR3']unit.

Look at the table below to see the differences.

- If you cannot find the Value Type you need, you can create a custom Value Type. [CONFLUENCE_PAGE title='Customizing Units' space='SYSMLP2024xR3']>]]>
- If you cannot find the [CONFLUENCE_PAGE title='Unit' space='SYSMLP2024xR3']you need, you can create a custom Unit. [CONFLUENCE_PAGE title='Customizing Units' space='SYSMLP2024xR3']>]]>

If you want to specify the Value Type for a Value Property, follow the procedures in the [CONFLUENCE_PAGE title='Using Units' space='SYSMLP2024xR3'] page.

| Value Type | Name construction | Purpose | Example |
| --- | --- | --- | --- |
| Unitless | Quantity name, e.g. distance. | Use this to create a general-purpose model. and its Slots can contain different units of the same . |  |
| With specified | Quantity and unit names, e.g. distance[metre]. | Use this to create a specific-purpose model. Instance Specifications and its Slots can contain the same units of the same . |  |

133530758

**Related diagrams**

- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1431c954-eda6-40c5-855a-a9d134e7fbd3"><ac:parameter ac:name="id">133530759</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fb6184c2-4af3-4814-8aef-b0710e62d312"><ac:parameter ac:name="id">133530762</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1a981aee-d3a0-4969-a755-fe720ed2fe50"><ac:parameter ac:name="id">133530760</ac:parameter><ac:rich-text-body><p>A Value Type is defined as a stereotype of UML Data Type to establish a more neutral term for system values that may never be given a concrete data representation. A Value Type adds an ability to carry a <ac:link><ri:page ri:content-title="Unit" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">units</span> </ac:link-body></ac:link>of measure of a <ac:link><ri:page ri:content-title="Quantity Kind" ri:space-key="SYSMLP2024xR3" /></ac:link> associated with the value.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="19c0e762-25f2-442f-969a-966776a30389"><ac:rich-text-body><p>Use the <span class="confluence-link"><ac:link><ri:page ri:content-title="Using QUDV model library" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[QUDV model library]]></ac:plain-text-link-body></ac:link></span> to find all standard value types.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="unitless_value_type.png"><ri:page ri:content-title="Value Type" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p><br /></p><p><span> When specifying the Value Type for a <ac:link><ri:page ri:content-title="Value Property" ri:space-key="SYSMLP2024xR3" /></ac:link>, you can select one of the following:</span></p><ul><li><span>Unitless Value Type.</span></li><li><span>Value Type with specified <ac:link><ri:page ri:content-title="Unit" ri:space-key="SYSMLP2024xR3" /><ac:link-body><span class="confluence-link">unit</span></ac:link-body></ac:link>.</span></li></ul><p><span>Look at the table below to see the differences.</span></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="645b475e-5a16-4534-a281-1695f2eb7e92"><ac:rich-text-body><ul><li><span>If you cannot find the Value Type you need, you can create a custom Value Type. <ac:link ac:anchor="Creating custom Value Type"><ri:page ri:content-title="Customizing Units" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to create a custom Value Type >>]]></ac:plain-text-link-body></ac:link></span></li><li><span>If you cannot find the <ac:link><ri:page ri:content-title="Unit" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[unit ]]></ac:plain-text-link-body></ac:link>you need, you can create a custom Unit. <ac:link ac:anchor="Creating custom Unit"><ri:page ri:content-title="Customizing Units" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to create a custom units >>]]></ac:plain-text-link-body></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span>If you want to specify the Value Type for a Value Property, follow the procedures in the <ac:link><ri:page ri:content-title="Using Units" ri:space-key="SYSMLP2024xR3" /></ac:link> page.</span></p><table class="relative-table wrapped"><colgroup><col style="width: 116.0px;" /><col style="width: 226.0px;" /><col style="width: 410.0px;" /><col style="width: 349.0px;" /></colgroup><tbody><tr><th>Value Type</th><th>Name construction</th><th>Purpose</th><th>Example</th></tr><tr><td>Unitless</td><td><span><span>Quantity name, e.g. distance.</span></span></td><td><span><span>Use this <span><span>to create a general-purpose model</span></span>. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance Specification" /><ac:plain-text-link-body><![CDATA[Instance Specifications]]></ac:plain-text-link-body></ac:link> and its <span class="confluence-link">Slots</span> can contain different units of the same <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>.</span></span></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="unitless_value_type_1.png"><ri:page ri:content-title="Value Type" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></div></td></tr><tr><td>With <span>specified <span class="confluence-link"><ac:link><ri:page ri:content-title="Unit" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[units]]></ac:plain-text-link-body></ac:link></span></span></td><td><span>Quantity and unit names, e.g. distance[metre].</span></td><td><span>Use this to create a specific-purpose model. <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Instance Specification" /><ac:link-body>I<span><span>nstance Specifications</span></span></ac:link-body></ac:link><span><span> and its Slots can contain the same units of the same <ac:link><ri:page ri:content-title="Block" ri:space-key="SYSMLP2024xR3" /></ac:link>.</span></span></span></td><td><div class="content-wrapper"><p><ac:image><ri:attachment ri:filename="value_type_with_unit.png"><ri:page ri:content-title="Value Type" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></div></td></tr></tbody></table></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ed7ecf3a-999b-4742-b0cb-c84182483660"><ac:parameter ac:name="id">133530758</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related diagrams</strong></p><ul><li class="auto-cursor-target"><ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Block Definition Diagram ]]></ac:plain-text-link-body></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159797 space=SYSMLP2024xR3 version=2 -->
## PAGE 00402: Verify

- page_id: `227159797`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159797/Verify
- version_number: 2
- version_date: `2025-05-02T10:28:44.458+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Verify' space='CRMP2024xR3']true

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Requirement Table' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="eb71704a-033f-4979-b05e-e2bb2d485e0c"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024xR3" ri:content-title="Verify" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Requirement Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Requirement Table" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p> </ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159798 space=SYSMLP2024xR3 version=1 -->
## PAGE 00403: View

- page_id: `227159798`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159798/View
- version_number: 1
- version_date: `2016-04-08T09:46:24.961+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

A View is a representation of a whole system from the perspective of a single [CONFLUENCE_PAGE title='Viewpoint' space='SYSMLP2024xR3']. A view can only own element import, package import, comment, and constraint elements.

[IMAGE alt='' src='']

#### PANEL: Related diagram

Related diagram

- [CONFLUENCE_PAGE title='Views and Viewpoints Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A View is a representation of a whole system from the perspective of a single <ac:link><ri:page ri:content-title="Viewpoint" ri:space-key="SYSMLP2024xR3" /></ac:link>. A view can only own element import, package import, comment, and constraint elements.</p><p><ac:image ac:alt="View" ac:title="View"><ri:attachment ri:filename="view.png"><ri:page ri:content-title="View" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p> </p></ac:layout-cell><ac:layout-cell><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="945c9ebe-05c7-4a1c-b7c9-5fdadbc65f5c"><ac:parameter ac:name="title">Related diagram</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Views and Viewpoints Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159800 space=SYSMLP2024xR3 version=1 -->
## PAGE 00404: Viewpoint

- page_id: `227159800`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159800/Viewpoint
- version_number: 1
- version_date: `2024-08-19T16:02:33.696+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

A Viewpoint is a specification of the conventions and rules for constructing and using a view for the purpose of addressing a set of stakeholder concerns. The languages and methods for specifying a View can reference methods and languages in another Viewpoint. They specify the elements expected to be represented in the view that may be formally or informally defined.

[IMAGE alt='' src='']

A Viewpoint has a Method property which describes the expectation of what stakeholder(s) wish to see exposed from the model, how the stakeholder wishes the information to be structured and presented, and in what kind of artifact the stakeholder wants to consume the information. It is the set of rules that describe how the view should express the information from the model to address the stakeholder concerns. The methods are used to construct the [CONFLUENCE_PAGE title='View' space='SYSMLP2024xR3'] for the Viewpoint.

#### PANEL: Related diagram

Related diagram

- [CONFLUENCE_PAGE title='Views and Viewpoints Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Viewpoint is a specification of the conventions and rules for constructing and using a view for the purpose of addressing a set of stakeholder concerns. The languages and methods for specifying a View can reference methods and languages in another Viewpoint. They specify the elements expected to be represented in the view that may be formally or informally defined.</p><p><ac:image ac:title="Viewpoint" ac:alt="Viewpoint"><ri:attachment ri:filename="viewpoint.png"><ri:page ri:content-title="Viewpoint" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p>A Viewpoint has a Method property which describes the expectation of what stakeholder(s) wish to see exposed from the model, how the stakeholder wishes the information to be structured and presented, and in what kind of artifact the stakeholder wants to consume the information. It is the set of rules that describe how the view should express the information from the model to address the stakeholder concerns. The methods are used to construct the <ac:link><ri:page ri:content-title="View" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Views]]></ac:plain-text-link-body></ac:link> for the Viewpoint.</p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="945c9ebe-05c7-4a1c-b7c9-5fdadbc65f5c"><ac:parameter ac:name="title">Related diagram</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Views and Viewpoints Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159259 space=SYSMLP2024xR3 version=1 -->
## PAGE 00405: Views and Viewpoints

- page_id: `227159259`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159259/Views+and+Viewpoints
- version_number: 1
- version_date: `2024-07-31T14:40:10.670+02:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

1249494231

INLINE

1249494233

INLINE

1249494232

INLINE

Using SysML [CONFLUENCE_PAGE title='View' space='SYSMLP2024xR3']and [CONFLUENCE_PAGE title='Viewpoint' space='SYSMLP2024xR3']elements you may create your custom templates and publish the document in Cameo Collaborator.

1249494230

INLINE

**Related pages**

- [CONFLUENCE_PAGE title='View' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Viewpoint' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Views and Viewpoints Diagram' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5ca8a760-1d29-4e6a-8095-8ad8c803beb6"><ac:parameter ac:name="id">1249494231</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b13a0a4f-5527-4962-aad1-7bd534991940"><ac:parameter ac:name="id">1249494233</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6454a22b-dc33-4f1b-8441-9aca12a2d340"><ac:parameter ac:name="id">1249494232</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>Using SysML <ac:link><ri:page ri:content-title="View" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[View ]]></ac:plain-text-link-body></ac:link>and <ac:link><ri:page ri:content-title="Viewpoint" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Viewpoint ]]></ac:plain-text-link-body></ac:link>elements you may create your custom templates and publish the document in Cameo Collaborator.</p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e6b5d240-d77a-48ba-bca5-ea0aa5f4c369"><ac:parameter ac:name="id">1249494230</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="View" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Viewpoint" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Views and Viewpoints Diagram" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159663 space=SYSMLP2024xR3 version=1 -->
## PAGE 00406: Views and Viewpoints Diagram

- page_id: `227159663`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159663/Views+and+Viewpoints+Diagram
- version_number: 1
- version_date: `2020-12-03T13:27:39.103+01:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

The concept of View and Viewpoint reflects perspectives of different stakeholders. The views are constructed from a subset of the model that addresses their concerns.

[IMAGE alt='' src='']

#### PANEL: Related elements

Related elements

- [CONFLUENCE_PAGE title='View' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Viewpoint' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Conform' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Expose' space='SYSMLP2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The concept of View and Viewpoint reflects perspectives of different stakeholders. The views are constructed from a subset of the model that addresses their concerns.</p><p><ac:image ac:title="Views and Viewpoints Diagram" ac:alt="Views and Viewpoints Diagram"><ri:attachment ri:filename="views_viewpoints_diagram.png"><ri:page ri:content-title="Views and Viewpoints Diagram" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="c9f9dad6-40f7-401e-8058-c9141b751f38"><ac:parameter ac:name="title">Related elements</ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="View" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Viewpoint" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Conform" ri:space-key="SYSMLP2024xR3" /></ac:link></li><li><ac:link><ri:page ri:content-title="Expose" ri:space-key="SYSMLP2024xR3" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227159696 space=SYSMLP2024xR3 version=2 -->
## PAGE 00407: Whitebox ICD Table

- page_id: `227159696`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159696/Whitebox+ICD+Table
- version_number: 2
- version_date: `2025-05-02T10:28:41.098+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Glossary of SysML concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

The purpose of Whitebox ICD Table is to show how [CONFLUENCE_PAGE title='Part Property' space='SYSMLP2024xR3'] are connected via ports/interfaces. This table collects all parts of the context element. Those parts are connected through the ports/interfaces using [CONFLUENCE_PAGE title='Connector' space='MD2024xR3']. You can visually identify what kind of ports/interfaces (Port A and Port B) and flows (Item Flow) are used to connects two Part Properties (Part A and Part B).

In the row 1 of the following figure, the*Controller* Part Property sends the *control* Signal to the *Boiler* Part Property through the ports *b* and *c*. The *Controller* receives the *Status* signal from the *Boiler* through the Ports *c* and *b*.In the row 2, the Part *Controller* sends the flow *Elec Power* to the Part *Boiler* through the Ports *bp* and *p in*. [CONFLUENCE_PAGE title='Creating Interface Control Document tables' space='SYSMLP2024xR3']>]]>

###### [IMAGE alt='' src='']An example of Whitebox ICD Table.

In the created table, a row represents the Connector and the columns represent features of that Connector. You can [CONFLUENCE_PAGE title='Working with columns' space='MD2024xR3'] them ifno longer need.

Using **Show Parts**, you can easily filter connectors and choose which ones should be displayed in the table or hidden from it. In the **Show Parts** filter, you can:

- See all the connectors used in a defined context.
- Easier identify and multi-select the needed connectors (they are grouped by parts).
- Scroll through the list with the possibility to expand or collapse groups.
- Use the search field which allows to quickly find needed connectors.

To choose which connectors should be displayed or hidden

1. In the Whitebox ICD Table toolbar, click **Show Parts**. 
[IMAGE alt='' src='']
2. In the **Show Parts** dialog, select the connectors you want to hide or display.
3. Click **OK**.

- If the part is in a partially selected or empty state, clicking it selects all the connectors under that part. If the part is in fully selected state, clicking it cancels all the connector selections.
- The connectors are represented under both end parts, so if you choose the connector under one end, the second end will be selected as well. It works the same way when clearing the selection.

A Whitebox ICD Table consists of the following columns.

| Column name | Description |
| --- | --- |
| # | A row number. |
| Part A | Displays a Part that is connected with Part B. |
| Port A | Displays a Port that is connected with Port B. |
| Port A Features | Displays all the properties of the Port A. |
| Item Flow | Displays the flow kind and its direction which flows through the Connector between two Parts (Part A and Part B). |
| Port B | Displays a Port that is connected with Port A. |
| Port B Features | Displays all the properties of the Port B. |
| Part B | Displays a Part that is connected with Part A. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(51,51,51);">The purpose of Whitebox ICD Table is to show how <ac:link><ri:page ri:content-title="Part Property" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Part Properties]]></ac:plain-text-link-body></ac:link> are connected via ports/interfaces. This table collects all parts of the context element. Those parts are connected through the ports/interfaces using <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Connector" /><ac:plain-text-link-body><![CDATA[Connectors]]></ac:plain-text-link-body></ac:link>. You can visually identify what kind of ports/interfaces (Port A and Port B) and flows (Item Flow) are used to connects two Part Properties (Part A and Part B). </span></p><p><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">In the row 1 of the following figure, the<span style="color: rgb(51,51,51);"> </span><em>Controller</em> <span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);">Part <span style="color: rgb(51,51,51);">Property</span></span></span> sends the <em>control</em> Signal to the <span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"><em>Boiler</em></span></span> Part <span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Property</span></span></span> </span></span> through the ports <em>b</em> and <em>c</em>. The <em>Controller</em> receives the <em>Status</em> signal from the <em>Boiler</em> through the Ports <em>c</em> and <em>b</em>.</span><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);"> In the row 2,  the Part <em>Controller</em> sends the flow <em>Elec Power</em> to the Part <em>Boiler</em> through the Ports <em>bp</em> and <em>p in</em>.</span> <ac:link><ri:page ri:content-title="Creating Interface Control Document tables" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[Learn how to create and work in the Interface Control Documents >>]]></ac:plain-text-link-body></ac:link></span></span></p><p><span style="color: rgb(0,0,0);"><br /></span></p><h6 style="text-align: center;"><span style="color: rgb(0,0,0);"><ac:image ac:align="center" ac:title="Whitebox ICD Table" ac:alt="Whitebox ICD Table"><ri:attachment ri:filename="whitebox_icd_table.png"><ri:page ri:content-title="Whitebox ICD Table" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image>An example of Whitebox ICD Table.</span></h6><p><span style="color: rgb(0,0,0);">In the created table, a row represents the Connector and the columns represent <span style="color: rgb(51,51,51);">features of that Connector. You can <ac:link ac:anchor="Adding and removing columns"><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with columns" /><ac:plain-text-link-body><![CDATA[add more features (columns) or remove]]></ac:plain-text-link-body></ac:link> them if</span></span><span style="color: rgb(51,51,51);"> no longer need.</span></p><p><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">Using <strong>Show Parts</strong>, you can easily filter connectors and choose which ones should be displayed in the table or hidden from it.</span> In the <strong>Show Parts</strong> filter, you can:</span></p><ul><li><span style="color: rgb(62,63,64);">See all the connectors used in a defined context.</span></li><li><p>Easier identify and multi-select the needed connectors (they are grouped by parts).</p></li><li><span style="color: rgb(62,63,64);">Scroll through the list with the possibility to expand or collapse groups.</span><span style="color: rgb(62,63,64);"><br /></span></li><li><span style="color: rgb(62,63,64);">Use the search field which allows to quickly find needed connectors. </span></li></ul><p><span style="color: rgb(62,63,64);"><br /></span></p><p><span style="color: rgb(0,0,0);">To choose which connectors should be displayed or hidden<br /></span></p><hr /><ol><li><span style="color: rgb(0,0,0);">In the Whitebox ICD Table toolbar, click <strong>Show Parts</strong>.<br /><ac:image><ri:attachment ri:filename="show_parts.png"><ri:page ri:content-title="Whitebox ICD Table" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></span></li><li><p class="auto-cursor-target"><span style="color: rgb(0,0,0);">In the <strong>Show Parts</strong> dialog, select the connectors you want to hide or display.</span></p></li><li><p class="auto-cursor-target"><span style="color: rgb(0,0,0);">Click <strong>OK</strong>.</span></p></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="60bb71b0-1c3a-4db0-938f-f288e92fbc2e"><ac:rich-text-body><ul><li>If the part is in a partially selected or empty state, clicking it selects all the connectors under that part. If the part is in fully selected state, clicking it cancels all the connector selections.</li><li>The connectors are represented under both end parts, so if you choose the connector under one end, the second end will be selected as well. It works the same way when clearing the selection.</li></ul></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(0,0,0);"><br /></span></p><p><span style="color: rgb(51,51,51);">A Whitebox ICD Table consists of the following columns.</span></p><table><colgroup><col /><col /></colgroup><tbody><tr><th><span style="color: rgb(0,0,0);">Column name</span></th><th><span style="color: rgb(0,0,0);">Description</span></th></tr><tr><td><span style="color: rgb(0,0,0);"><strong>#</strong></span></td><td><span style="color: rgb(51,51,51);">A row number.</span></td></tr><tr><td><span style="color: rgb(0,0,0);"><strong>Part A</strong></span></td><td><span style="color: rgb(51,51,51);">Displays a Part that is connected with Part B.</span></td></tr><tr><td><span style="color: rgb(0,0,0);"><strong>Port A</strong></span></td><td><span style="color: rgb(51,51,51);">Displays a Port  that is connected with Port B.</span></td></tr><tr><td><span style="color: rgb(0,0,0);"><strong>Port A Features</strong></span></td><td><span style="color: rgb(51,51,51);">Displays all the properties of the Port A.</span></td></tr><tr><td><span style="color: rgb(0,0,0);"><strong>Item Flow</strong></span></td><td><span style="color: rgb(51,51,51);">Displays the flow kind and its direction which flows through the Connector between two Parts (Part A and Part B).</span></td></tr><tr><td colspan="1"><span style="color: rgb(0,0,0);"><strong>Port B</strong></span></td><td colspan="1"><span style="color: rgb(51,51,51);">Displays a Port  that is connected with Port A.</span></td></tr><tr><td><span style="color: rgb(0,0,0);"><strong>Port B Features</strong></span></td><td><span style="color: rgb(51,51,51);">Displays all the properties of the Port B.</span></td></tr><tr><td><span style="color: rgb(0,0,0);"><strong>Part B</strong></span></td><td><span style="color: rgb(51,51,51);">Displays a Part  that is connected with Part A.</span></td></tr></tbody></table><p><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><br style="color: rgb(0,0,0);" /></span></span></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227159307 space=SYSMLP2024xR3 version=2 -->
## PAGE 00408: Working with model elements

- page_id: `227159307`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159307/Working+with+model+elements
- version_number: 2
- version_date: `2025-05-02T10:28:34.171+02:00`
- ancestors: SysML Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

1080417108

1080417110

1080417109

[CONFLUENCE_PAGE title='Working with model elements' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="dff075ab-16a4-444d-9fbc-bad5ef93d8ff"><ac:parameter ac:name="id">1080417108</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="416a26a4-9a61-444a-9f9c-88e1a240be7d"><ac:parameter ac:name="id">1080417110</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5317733b-82a7-443c-8231-e311b75dd90f"><ac:parameter ac:name="id">1080417109</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="8c060254-9b02-4d87-80c7-831e7990748b"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with model elements" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227158548 space=SYSMLP2024xR3 version=2 -->
## PAGE 00409: Working with model elements in the Model Browser

- page_id: `227158548`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158548/Working+with+model+elements+in+the+Model+Browser
- version_number: 2
- version_date: `2025-05-02T10:28:18.698+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

236521125

236521127

236521126

[CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="514fd426-22e5-4791-b4e4-39774a7aa649"><ac:parameter ac:name="id">236521125</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="33722809-23fd-4202-9998-5634097cfae8"><ac:parameter ac:name="id">236521127</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c633879c-2414-4123-8937-8d3d623320b3"><ac:parameter ac:name="id">236521126</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="46e05561-6f28-4f8c-b7f5-b816e47b8aee"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Working with model elements in the Model Browser" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=227159099 space=SYSMLP2024xR3 version=2 -->
## PAGE 00410: Wrapping MATLAB functions

- page_id: `227159099`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227159099/Wrapping+MATLAB+functions
- version_number: 2
- version_date: `2025-05-02T10:28:28.789+02:00`
- ancestors: SysML Plugin Documentation > User Guide > Modeling parametric constraints
- labels: []

### NORMALIZED CONTENT

MATLAB source code contains a functions declaration. The m-file is a text file containing a list of commands written in MATLAB or Octave syntax. You can define functions and scripts in the m-file.

You can move the mathematical expressions from MATLAB source code into the model. Use the m-file to transfer functions to a [CONFLUENCE_PAGE title='Constraint Block' space='SYSMLP2024xR3'], [CONFLUENCE_PAGE title='Constraint Property' space='SYSMLP2024xR3'], or [CONFLUENCE_PAGE title='Call Behavior Action' space='MD2024xR3'].

Creation of elements from MATLAB source code is supported in the following diagrams:

- [CONFLUENCE_PAGE title='SysML Internal Block Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Block Definition Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Parametric Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='SysML Activity Diagram' space='SYSMLP2024xR3']
- [CONFLUENCE_PAGE title='Class diagram' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Composite Structure diagram' space='MD2024xR3']
- [CONFLUENCE_PAGE title='Activity diagram' space='MD2024xR3']

##### Wrapping the mathematical expressions from MATLAB source code

To wrap the mathematical expressions from MATLAB source code into the model, use one of the following methods:

- Drag the m-file directly to the diagram pane to create one of the following:
  - Constraint Block with its properties and parameters in the SysML Block Definition or UML Class diagrams.
  - Constraint Property and Constraint Block in the SysML Internal Block, SysML Parametric, or UML Composite Structure diagrams. Constraint Block is automatically set as the type for the newly created Constraint Property. The properties and parameters of the Constraint Block are displayed on the Constraint Property shape.
  - Call Behavior Action with its pins and opaque in the SysML or UML Activity diagrams.
- Drag the m-file onto the already existing element shape (empty or full) to set one of the following:
  - Constraints and parameters for Constraint Block in the SysML Block Definition or UML Class diagrams.
  - Type for Constraint Property by creating a new Constraint Block in SysML Internal Block, SysML Parametric, or UML Composite Structure diagrams. The properties and parameters of the newly created Constraint Block are displayed on the Constraint Property shape.
- Use the shortcut menu on the already existing element shape (empty or full). Choose Tools > Create Expression from M-File .

- The name of the created element is the same as the name of the function in the m-file. If the name of that element already exists, it will appear with an incremental number at the end of the name.

[IMAGE alt='' src='']

- If the m-file contains multiple functions declarations, only the first function is wrapped into the model.

[IMAGE alt='' src='']

##### Setting the constraints and parameters for Constraint Block using m-file

To set constraints and parameters for a Constraint Block using m-file

1. In the Containment tree or on the diagram pane, select a Constraint Block or Constraint Property (with set type).
2. From the shortcut menu, choose Tools > Create Expression from M-File . The Open file dialog opens.
3. Select the m-file and click Open . The constraints and parameters are set for Constraint Block.

#### TIP: Example

Example

The following figure illustrates the function declaration in m-file. It is for least-square fitting to find the slope (m) and the y-intercept (b) of a straight-line equation from two given input parameters x and y. The constraint expression is: [m, b] = linefit(x, y). The constraint parameters are x, y, m, and b. After the function transfer into the element, its type, property, and parameter are set automatically and are displayed on the element shape.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>MATLAB source code contains a functions declaration. The m-file is a text file containing a list of commands written in MATLAB or Octave syntax. You can define functions and scripts in the m-file.</p><p>You can move the mathematical expressions from MATLAB source code into the model. Use the m-file to transfer functions to a <ac:link><ri:page ri:content-title="Constraint Block" ri:space-key="SYSMLP2024xR3" /></ac:link>, <ac:link><ri:page ri:content-title="Constraint Property" ri:space-key="SYSMLP2024xR3" /></ac:link>, or <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Call Behavior Action" /></ac:link>.</p><p>Creation of elements from MATLAB source code is supported in the following diagrams:</p><ul><li><ac:link><ri:page ri:content-title="SysML Internal Block Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Internal Block Definition diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Block Definition Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Block Definition diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Parametric Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Parametric diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="SysML Activity Diagram" ri:space-key="SYSMLP2024xR3" /><ac:plain-text-link-body><![CDATA[SysML Activity diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Class diagram" /><ac:plain-text-link-body><![CDATA[UML Class diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Composite Structure diagram" /><ac:plain-text-link-body><![CDATA[UML Composite Structure diagram]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Activity diagram" /><ac:plain-text-link-body><![CDATA[UML Activity diagram]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><h3>Wrapping the mathematical expressions from MATLAB source code</h3><p><br /></p><hr /><p>To wrap the mathematical expressions from MATLAB source code into the model, use one of the following methods:</p><p><br /></p><ul><li>Drag the m-file directly to the diagram pane to create one of the following:<ul><li>Constraint Block with its properties and parameters in the SysML Block Definition or UML Class diagrams.</li><li>Constraint Property and Constraint Block in the SysML Internal Block, SysML Parametric, or UML Composite Structure diagrams. Constraint Block is automatically set as the type for the newly created Constraint Property. The properties and parameters of the Constraint Block are displayed on the Constraint Property shape.</li><li>Call Behavior Action with its pins and opaque in the SysML or UML Activity diagrams.</li></ul></li><li>Drag the m-file onto the already existing element shape (empty or full) to set one of the following:<ul><li>Constraints and parameters for Constraint Block in the SysML Block Definition or UML Class diagrams.</li><li>Type for Constraint Property by creating a new Constraint Block in SysML Internal Block, SysML Parametric, or UML Composite Structure diagrams. The properties and parameters of the newly created Constraint Block are displayed on the Constraint Property shape.</li></ul></li><li>Use the shortcut menu on the already existing element shape (empty or full). Choose <strong>Tools</strong> &gt; <strong>Create Expression from M-File</strong>.</li></ul><p> </p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="c56b40cd-8a7b-48c4-b422-7e9503289719"><ac:rich-text-body><ul><li>The name of the created element is the same as the name of the function in the m-file. If the name of that element already exists, it will appear with an incremental number at the end of the name.</li></ul><p><ac:image><ri:attachment ri:filename="name_duplication.png"><ri:page ri:content-title="Wrapping MATLAB functions" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p><p> </p><ul><li>If the m-file contains multiple functions declarations, only the first function is wrapped into the model.</li></ul><p><ac:image><ri:attachment ri:filename="wrap_multiple_math_functions.png"><ri:page ri:content-title="Wrapping MATLAB functions" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p> </p><h3>Setting the constraints and parameters for Constraint Block using m-file</h3><p>To set constraints and parameters for a Constraint Block using m-file</p><hr /><ol><li>In the Containment tree or on the diagram pane, select a Constraint Block or Constraint Property (with set type).</li><li>From the shortcut menu, choose <strong>Tools</strong> &gt; <strong>Create Expression from M-File</strong>. The <strong>Open file</strong> dialog opens.</li><li>Select the m-file and click <strong>Open</strong>.<br />The constraints and parameters are set for Constraint Block.</li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="0efdc0d3-9f82-4a57-a50e-9b240a255441"><ac:parameter ac:name="title">Example</ac:parameter><ac:rich-text-body><p> The following figure illustrates the function declaration in m-file. It is for least-square fitting to find the slope (m) and the y-intercept (b) of a straight-line equation from two given input parameters x and y. The constraint expression is: [m, b] = linefit(x, y). The constraint parameters are x, y, m, and b. After the function transfer into the element, its type, property, and parameter are set automatically and are displayed on the element shape.</p><p><ac:image ac:title="Creating Constraint Block, Constraint Property, or Call Behavior Action from MATLAB source code" ac:alt="Creating Constraint Block, Constraint Property, or Call Behavior Action from MATLAB source code"><ri:attachment ri:filename="wrap_math_function.png"><ri:page ri:content-title="Wrapping MATLAB functions" ri:space-key="SYSMLP2024xR3" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p> </p><p> </p><p> </p><p> </p><p> </p><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227158545 space=SYSMLP2024xR3 version=2 -->
## PAGE 00411: Zoom tab

- page_id: `227158545`
- space_key: `SYSMLP2024xR3`
- source_url: https://docs.nomagic.com/spaces/SYSMLP2024xR3/pages/227158545/Zoom+tab
- version_number: 2
- version_date: `2025-05-02T10:28:18.516+02:00`
- ancestors: SysML Plugin Documentation > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

236219610

236219612

236219611

[CONFLUENCE_PAGE title='Zoom tab' space='MD2024xR3']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="7ab7d56a-40e9-4b46-9a1f-6bc2002bd495"><ac:parameter ac:name="id">236219610</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0511e713-5ea4-4c7c-aa54-65db2b6020b9"><ac:parameter ac:name="id">236219612</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e7868022-ba38-4dbb-af6f-9e3a0078cfe2"><ac:parameter ac:name="id">236219611</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="4ae32cb2-16c9-4ff5-90a8-ecdf243e3592"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Zoom tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
