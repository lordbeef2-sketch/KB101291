# NOMAGIC DOCUMENTATION SPACE: Systems Safety Engineer

<!--NOMAGIC_SPACE key=SSE chunk=1 -->

<!--NOMAGIC_PAGE id=304009480 space=SSE version=2 -->
## PAGE 00001: (2026x Refresh1) Boundary Diagram

- page_id: `304009480`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009480/2026x+Refresh1+Boundary+Diagram
- version_number: 2
- version_date: `2026-04-29T15:32:25.249+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer > (2026x Refresh1) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

Boundary diagram and Boundary diagram item aid in identifying and capturing in exhaustive detail about :

- The Internal sub-systems and components and external “actors”/entities
- The different scopes of analysis by visually outlining the system boundary.
- The interactions with legends
- Missing interactions.

##### Creating a Boundary Diagram

To create a Boundary Diagram

1. In the Containment tree, right-click the Boundary Diagram package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Boundary Diagram****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword boundary and then select Boundary Diagram . 
 
[IMAGE alt='' src='']

The Boundary Diagram is now displayed in the diagram pane and in the Containment tree of the modeling tool. 
 
[IMAGE alt='' src='']

##### Adding an Internal Block Diagram of a Use Project

To add an Internal Block Diagram of a Use Project

1. Add the required local project to your project. To learn more, refer to the Using local projects page.
2. Drag and drop the required block from the Containment tree to the Boundary Diagram. [ATTACHMENT filename='Block drag and drop.png']
3. Right-click the block and select Display>Display Internal Structure>Lamp in context>Lamp in context. 
 
[IMAGE alt='' src='']

The internal structure of the Lamp block is displayed in the diagram pane.

##### Creating a Boundary Diagram Item

To create a Boundary Diagram Item

1. Drag and drop the Boundary Diagram Item element in the diagram pane. [ATTACHMENT filename='Boundary diagram_Item.png']
2. In the Contain ment tre e, select the newly created Boundary Diagram Item and rename it with the help of the Specification dialog. 
 
[IMAGE alt='' src='']

##### Drawing an Anchor

To draw an Anchor

- Draw an anchor from the newly created Item Scope to the elements of interest. To learn more about drawing and configuring an Anchor, refer to the Anchor page. [ATTACHMENT filename='Scope Done.png']

##### Creating a Signal Category

To create a Signal Category

1. Create a SysML Block Definition Diagram in the Boundary Diagram package. To learn more about creating a diagram, click here .
2. Drag and drop the signals from the Lamp>Signals package in the diagram pane. [ATTACHMENT filename='Signal drag and drop.png']
3. Drag and drop the EnergyTransfer , InformationTransfer , InteractionClass , MaterialExchange, and PhysicalConnection elements from the FMA Library package in the diagram pane. [ATTACHMENT filename='FMA drag and drop.png']
4. Rearrange the elements and create Dependencies as per your requirements. To learn more about creating a Dependency, refer to the Dependency page. [ATTACHMENT filename='Dependency created.png']
5. Select and apply the TransferType[Dependency] stereotype to all the dependencies. To learn more about applying a stereotype, refer to the [CONFLUENCE_PAGE title='Stereotype' space='MED'] page.
6. On the diagram toolbar, click the [IMAGE alt='' src=''] button to change the diagram layout. To learn more about changing diagram layout, refer to the[https://docs.nomagic.com/spaces/MT/pages/9917874/Layout](https://docs.nomagic.com/spaces/MT/pages/9917874/Layout)[Layout](https://docs.nomagic.com/MT/?contextKey=layout&version=2026x Refresh1&variant=default)page. 
 
[IMAGE alt='' src='']

##### Working with Legends

A Legend is a model element that allows you to define the styles of diagram symbols and table rows. It helps you to visually group model elements according to specified criteria. A Legend increases the readability of the diagram and table contents by highlighting important information. To learn more, refer to the [Legends](https://docs.nomagic.com/MT/?contextKey=legends&version=2026x Refresh1&variant=default)page.

###### Applying a Legend

To apply a Legend

1. In the diagram toolbar. Click [IMAGE alt='' src=''] and from the drop-down menu, select Apply Legends .
2. Select the Legend(s) you want to display and click OK. [IMAGE alt='' src='']

To learn more, refer to the [Applying Legends](https://docs.nomagic.com/MT/?contextKey=applying-legends&version=2026x Refresh1&variant=default)page.

###### Extracting a Legend

To extract a Legend

1. In the diagram toolbar. Click [IMAGE alt='' src=''] and from the drop-down menu, select Extract Legends .
2. Select the Legend(s) you want to display and click Extract. [IMAGE alt='' src='']

To learn more, refer to the [Extracting Legends](https://docs.nomagic.com/MT/?contextKey=creating-legends-automatically&version=2026x Refresh1&variant=default)page.

###### Specifying Legend Item adornment

To open the adornment properties of a Legend Item

1. Open the Specification window of the Legend Item **Lamp Scope** in the **Boundary Diagram Item**. 
 
[IMAGE alt='' src='']
2. Click the specification cell of the Adornment property, and then click [IMAGE alt='' src=''] .
3. In the Adornment Properties dialog, specify the Fill Color property and click OK . [IMAGE alt='' src='']

To learn more, refer to the[Specifying Legend Item adornment](https://docs.nomagic.com/MT/?contextKey=specifying-legend-item-adornment&version=2026x Refresh1&variant=default).

After completing the above procedures, the Boundary Diagram is updated in the following manner.

[IMAGE alt='' src='']

###### Boundary Diagram after applying, extracting, and specifying the Legends.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p>Boundary diagram and Boundary diagram item aid in identifying and capturing in exhaustive detail about :</p><ul><li data-uuid="3085777f-da5f-4dc1-973d-903ca3366cad">The Internal sub-systems and components and external “actors”/entities</li><li data-uuid="ba0845e6-48b0-4474-bee3-7702eda1491c">The different scopes of analysis by visually outlining the system boundary.</li><li data-uuid="95efaa3d-3768-43ce-a8fd-1ea37fcddecb">The interactions with legends</li><li data-uuid="3d6286df-2e79-4ed8-8dae-bfa3b5204e5a">Missing interactions.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Boundary Diagram</h3><p>To create a Boundary Diagram </p><hr /><ol><li data-uuid="3547a66c-39c0-46e9-bdad-2077594db1f6">In the Containment tree, right-click the <strong>Boundary Diagram </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="513d755e-9e19-44b9-b639-94da05d12a34">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Boundary Diagram</strong><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram Select.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword boundary and then select <strong>Boundary Diagram</strong><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram Search.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li></ol><p>The Boundary Diagram is now displayed in the diagram pane and in the Containment tree of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram created.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></p><h3>Adding an Internal Block Diagram of a Use Project</h3><p>To add an Internal Block Diagram of a Use Project</p><hr /><ol><li data-uuid="5c7ee77a-dc84-492b-8540-ff3132c1c2f3">Add the required local project to your project. To learn more, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=using-local-projects&amp;version=2026x Refresh1">Using local projects</a> page.</li><li data-uuid="3ddaa88e-0e0c-4a03-b3ae-616fa2d2ab63">Drag and drop the required block from the Containment tree to the Boundary Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Block drag and drop.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="9e0fa85a-16ad-48d6-9ea6-f49e499b79a7">Right-click the block and select <strong>Display&gt;Display Internal Structure&gt;Lamp in context&gt;Lamp in context.<br /><br /><ac:image><ri:attachment ri:filename="Lamp in contect command.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /></strong></li></ol><p>The internal structure of the Lamp block is displayed in the diagram pane.</p><h3>Creating a Boundary Diagram Item </h3><p>To create a Boundary Diagram Item</p><hr /><ol><li data-uuid="03543445-37ff-4e90-a59b-624a09c6e688">Drag and drop the <strong>Boundary Diagram Item </strong>element in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram_Item.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="a3d74fef-0943-412f-ada3-170db6845425">In the Contain<ac:inline-comment-marker ac:ref="950adda0-c6ed-423c-bc12-e16093ed44a4">ment tre</ac:inline-comment-marker>e, select the newly created<ac:inline-comment-marker ac:ref="84c7744b-378c-4b37-8276-9c0a2333c911"> Boundary Diagram Item and rename it with the help of the Specification dialog.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram_Item_Containment tree.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /></ac:inline-comment-marker></li></ol><h3>Drawing an Anchor</h3><p>To draw an Anchor</p><hr /><ul><li data-uuid="6b602302-2aba-4775-aa51-2b8e5ed387b3">Draw an anchor from the newly created Item Scope to the elements of interest. To learn more about drawing and configuring an Anchor, refer to the<a href="https://docs.nomagic.com/MT/?contextKey=anchor&amp;version=2026x Refresh1&amp;variant=default"> Anchor </a>page.<br /><br /><ac:image><ri:attachment ri:filename="Scope Done.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></li></ul><h3>Creating a Signal Category</h3><p>To create a Signal Category</p><hr /><ol><li data-uuid="d01f0ebe-5479-4e13-a0ea-21f8475aada5">Create a <strong>SysML Block Definition Diagram</strong> in the Boundary Diagram package. To learn more about creating a diagram, click <a href="https://docs.nomagic.com/MT/?contextKey=creating-diagrams&amp;version=2026x Refresh1&amp;variant=default">here</a>.</li><li data-uuid="85620cc4-4cb3-4143-956c-3fa912f3d77f">Drag and drop the signals from the <strong>Lamp&gt;Signals</strong> package in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Signal drag and drop.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="386c649c-dfaf-4106-9531-c656666cc711">Drag and drop the <strong>EnergyTransfer</strong>, <strong>InformationTransfer</strong>, <strong>InteractionClass</strong>, <strong>MaterialExchange, </strong>and <strong>PhysicalConnection </strong>elements from the <strong>FMA Library </strong>package in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="FMA drag and drop.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="d4559a7b-cd10-4e75-9040-5febdc01e6d1">Rearrange the elements and create Dependencies as per your requirements. To learn more about creating a Dependency, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=dependency&amp;version=2026x Refresh1&amp;variant=default">Dependency</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Dependency created.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="95a5f2e2-dad5-431f-8e43-3f43240476fd">Select and apply the <strong>TransferType[Dependency]</strong> stereotype to all the dependencies. To learn more about applying a stereotype, refer to the <ac:link><ri:page ri:space-key="MED" ri:content-title="Stereotype" /></ac:link> page.</li><li data-uuid="64c05ca9-2220-47d6-ac21-419c89fb73df"><span style="color:var(--ds-text,#172b4d);">On the diagram toolbar, click the<span> </span></span><span class="confluence-embedded-file-wrapper" style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="quick_diagram_layout.gif"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image> button to change the</span><span style="color:var(--ds-text,#172b4d);"> diagram layout. To learn more about changing diagram layout, refer to the<a href="https://docs.nomagic.com/spaces/MT/pages/9917874/Layout"> </a><a href="https://docs.nomagic.com/MT/?contextKey=layout&amp;version=2026x Refresh1&amp;variant=default"> Layout </a>page.<br /><br /><ac:image><ri:attachment ri:filename="diagram layout.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /></span></li></ol><h3>Working with Legends</h3><p><span style="color:var(--ds-text,#172b4d);">A Legend is a model element that allows you to define the styles of diagram symbols and table rows. It helps you to visually group model elements according to specified criteria. A Legend increases the readability of the diagram and table contents by highlighting important information. To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=legends&amp;version=2026x Refresh1&amp;variant=default"> Legends </a>page.</span></p><h4>Applying a Legend</h4><p>To a<ac:inline-comment-marker ac:ref="3354d760-dae3-4493-98ee-1ff93685756d">pply a Legend</ac:inline-comment-marker></p><hr /><ol><li data-uuid="cc70408d-3f1b-4049-b60f-12cffbc05a60">In the diagram toolbar. Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="legend_button.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></span> and from the drop-down menu, select<span style="letter-spacing: 0.0px;"> </span><strong style="letter-spacing: 0.0px;">Apply Legends</strong><span style="letter-spacing: 0.0px;">.</span></li><li data-uuid="a76fcb8a-13df-4027-8f47-5add73b860ed">Select the Legend(s) you want to display and click<span style="letter-spacing: 0.0px;"> </span><strong style="letter-spacing: 0.0px;">OK.</strong><span style="letter-spacing: 0.0px;"><br /><br /><ac:image><ri:attachment ri:filename="Applying Legends.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="954827ba-719b-478c-ad4a-664b0d88fed7"><ac:rich-text-body><p>To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=applying-legends&amp;version=2026x Refresh1&amp;variant=default">Applying Legends </a><span>page.</span></p></ac:rich-text-body></ac:structured-macro><h4>Extracting a Legend</h4><p>To extract a Legend</p><hr /><ol><li data-uuid="bd201c0f-6f9d-465f-8f12-ad86bce41f96">In the diagram toolbar. Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="legend_button.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></span> and from the drop-down menu, select<span> </span><strong>Extract Legends</strong><span>.</span></li><li data-uuid="1072c44f-cb71-4638-bdb4-373ab53adc91">Select the Legend(s) you want to display and click<span> </span><strong>Extract.</strong><span><br /><br /><ac:image><ri:attachment ri:filename="Extracting Legends.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="529793d6-0c70-4c46-bd52-c484471006d9"><ac:rich-text-body><p>To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=creating-legends-automatically&amp;version=2026x Refresh1&amp;variant=default">Extracting Legends </a><span>page.</span></p></ac:rich-text-body></ac:structured-macro><h4>Specifying Legend Item adornment</h4><p style="text-align: left;">To open the adornment properties of a Legend Item</p><hr style="text-align: left;" /><ol style="text-align: left;"><li data-uuid="6fc9f089-631d-45c2-b223-bba4949aecc6"><p>Open the Specification window of the Legend Item <strong>Lamp Scope</strong> in the <strong>Boundary Diagram Item</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Adornment_Specification.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image><br /><br /></p></li><li data-uuid="b0c0b73c-66ca-44d5-ad9a-834c7d91c601">Click the specification cell of the <strong>Adornment</strong> property, and then click <span class="confluence-embedded-file-wrapper"><ac:image><ri:attachment ri:filename="edit.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></span>.</li><li data-uuid="4fa49fa7-3b6a-4898-aec3-d0f9039142f8">In the Adornment Properties dialog, specify the <strong style="letter-spacing: 0.0px;">Fill Color </strong><span style="letter-spacing: 0.0px;">property and click </span><strong style="letter-spacing: 0.0px;">OK</strong><span style="letter-spacing: 0.0px;">.<br /></span><span style="letter-spacing: 0.0px;"><br /><ac:image><ri:attachment ri:filename="Adornment Properties.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4e013f77-4514-4d5b-b058-986b643945b3"><ac:rich-text-body><p><span> To learn more, refer to the </span><a href="https://docs.nomagic.com/MT/?contextKey=specifying-legend-item-adornment&amp;version=2026x Refresh1&amp;variant=default">Specifying Legend Item adornment</a>.<span><br /></span></p></ac:rich-text-body></ac:structured-macro><p><span style="letter-spacing: 0.0px;">After completing the above procedures, the Boundary Diagram is updated in the following manner.<br /><br /></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Scope and Legend created.png"><ri:page ri:content-title="(2026x Refresh1) Boundary Diagram" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Boundary Diagram after applying, extracting, and specifying the Legends.</h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=304009594 space=SSE version=2 -->
## PAGE 00002: (2026x Refresh1) Failure Mode & Effect Analysis

- page_id: `304009594`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009594/2026x+Refresh1+Failure+Mode+Effect+Analysis
- version_number: 2
- version_date: `2026-04-29T15:32:26.033+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer > (2026x Refresh1) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

An FMEA Table allows you to analyze the reliability aspect of your model and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. The RAAML-based FMEA Table diagram is derived from an activity object and represents each FMEA Item—defined as the unique pairing of a failure mode with its corresponding cause—through a dedicated row associated with the activity.

In an FMEA Table, you can:

- Create a new FMEA Item directly in a table or add an existing one.
- Directly edit the properties of FMEA Items in a table.

The following table describes each column name, its purpose, and relevant details:

| Column Name | Description |
| --- | --- |
| Name | Displays an auto-generated counter for the FMEA item (this prefix counter is a preset customization) and a name. If the name is generated automatically (e.g., from the creation of an FMEA Item in the Robustness Checklist), it is composed of the Failure Cause and its associated Failure Mode. |
| Inputs | List of input pins of the activity element selected as the Scope of the FMEA study. This is a non-editable field. |
| Function | Activity selected as the scope of the FMEA study. This is a non-editable field. |
| Output | Lists one or more of the output pins that are declared on the activity element selected as the Scope of the FMEA study and that are being affected by a dedicated failure mode. Your selection is limited to the declared output pins on the activity referenced on the Function cell. |
| Failure Mode | Specifies the Failure Mode specific to the FMEA Item Line. Failure Mode definition is as introduced in the Parameter Diagram section, referring to the description of the specific manner in which a component, subsystem, or system could potentially fail to meet the design intent. |
| Classification | Corresponds to the categorization of FMEA items, derived from the evaluation of Severity and Occurrence values using a customizable function (preset out-of-the-box as: CC in case severity >= 9, SC in case 9 > severity >= 7, and AC in case 7 > severity >= 5). |
| Final Effect | Describes the effect of a Failure Mode on the end user or the environment (i.e., at the system-of-interest level). Multiple Final Effects can be specified for a single FMEA item. Each Final Effect can have a default Severity value assigned as its property. To assign a Severity value, open the Specification window of the Final Effect and set the desired value. |
| Computed Effect | An element describing the effect that a Failure Mode has on the system element under consideration. An FMEA Item (e.g., a single row of an FMEA Table) can have multiple Local Effects of Failure. If the element under consideration is a subsystem directly underneath the system of interest level itself, the effect of the Failure Mode is the same as the Final Effect mentioned above in this table. |
| Severity | The Severity of effects is a rating number associated with the most serious effect for a given failure mode for the operation being evaluated. It is a relative rating within the scope of the individual FMEA item and is determined without regard for occurrence or detection. Valid values range from 1 to 10 (lowest to highest severity). |
| Cause | An element (either a lower-level Failure Mode or a dedicated Cause element) indicating the design weakness that leads to a Failure Mode. An FMEA item (e.g., a single row of an FMEA table) can have one Cause of Failure. A Cause can have default Occurrence and Detectability values assigned as properties. To assign these values, either open the Specification window of the Cause and set the desired Occurrence or Detectability, or edit them directly in the corresponding columns of the FMEA table. |
| Prevention Controls | A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode. You can specify multiple Prevention controls for a single FMEA Item. The type of object that can be elected as a Prevention Control is by default preset as a Requirement. The type can be customized. |
| Occurrence | A rating number is associated with each cause for a given failure mode being evaluated. The occurrence rating considers the likelihood of occurrence during production. Valid values range from 1 to 10 (lowest to highest probability). A Cause must be identified in the dedicated cell before setting this value. Enter the value directly in the corresponding FMEA table cell or set it on the Failure Mode or Cause object via the containment tree. |
| Criticality | The product of Severity and Occurrence ratings. |
| Detection Controls | An element describing the measures implemented to detect a Failure Mode. Multiple Detection Control entries can be specified for a single FMEA item. The type of object that can be elected as a Detection Control is by default preset as a Block. The type can be customized. |
| Detection | Detection is the rating associated with the likelihood of detecting the failure mode and/or associated cause, according to defined criteria. Ability to detect is the rating number associated with the combined capabilities of all the current process controls for a given cause and/or failure mode. You should not automatically presume the detection rating is low because the occurrence rating is low. Instead, the User assumes the failure has occurred, then assesses the capabilities of all the detection-type design controls to detect low-frequency failure modes and/or causes. The detection rating is identified without regard for severity or occurrence. Valid Values range from 1 to 10 (highest to lowest detectability). |
| Risk Priority Number | The risk priority number (RPN) is the product of the severity (S), occurrence (O), and detection (D) ratings. Within the scope of the individual FMEA, this value is between “1” and “1000”. A benefit of RPN is that it provides an indicator of improvement (before and after actions taken) that reduces any one factor of severity, occurrence, or detection. It shows the distribution of RPN values for a project (Pareto), giving a high-level overview of the risk assessment. You should be aware that the final RPN ratings are subjective and relative to a particular analysis. |
| Action Priority | Assessment of the internal priority affecting the recommended actions, as per the SAEJ 1739 rating scale. |
| Recommended Action | The description of an action intended to reduce the Risk Priority Number. All critical or significant FMEA items should have associated recommended actions. These actions should focus on design improvements and be directed at mitigating the Cause of Failure or eliminating the Failure Mode. The type of object that can be elected as a Recommended Action element creation is by default preset as a Block. The type can be customized. |
| Action Taken | A property describing what actions have been taken and the results of these actions (free text capture). |
| Responsible Person | Indicates the person responsible for completing a Recommended Action. No specific object type is being preset to represent a Person. |
| Target Date | A property defining the targeted completion date of a Recommended Action. |
| Completion Date | A property assessing the completion date of a Recommended Action. |
| Revised Severity | A property assessing the seriousness of the effect(s) of a potential Failure Mode on a component, subsystem, end user, or environment after mitigation. Valid values range from 1 to 10 (lowest to highest severity). A prerequisite is that an action has been taken |
| Revised Occurrence | A property indicating the likelihood that a specific Cause of Failure will occur after mitigation. Valid values range from 1 to 10 (lowest to highest probability of occurrence). |
| Revised Criticality | The product of Revised Severity and Revised Occurrence ratings. |
| Revised Detection | A property measuring the likelihood of detecting a potential failure after mitigation. Valid values range from 1 to 10 (highest to lowest detectability). |
| Revised Risk Priority Number | The product of Revised Criticality by Revised Detection. |
| Revised Action Priority | Assessment of the internal priority affected by the recommended actions after mitigation. |

#### TIP: Tips

Tips

- While selecting an FMEA Item element (line in the table):
  - You can remove the line from the table using the dedicated Remove From Table command.
  - You can delete it from the containment tree (and the table) using the dedicated Delete command.
- If a Robustness Check List (RCL) and/or Parameter Diagram exists for the activity, the user can navigate from the FMEA Table to one of those diagrams through a dedicated panel above the diagram. To learn more, refer to the [CONFLUENCE_PAGE title='(2026x Refresh1) Robustness Checklist' space=''] page.

##### Creating a Failure Mode and Effect Analysis (FMEA) Table

To create a Failure Mode and Effect Analysis (FMEA) Table

1. In the Containment tree, right-click the FMEA package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Safety and Reliability Analysis**and select **RAAML-based FMEA Table.** [IMAGE alt='' src='']
  - In the search tab, type the keyword FMEA and then select RAAML-based FMEA Table. 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity dialog_FMEA.png'] The FMEA Table is now displayed in the diagram pane of the modeling tool.

##### Adding an FMEA Item to the FMEA Table

Each Failure mode linked to a Failure Effect (end user effect of a Failure Mode) or to a Failure Cause (element indicating a Design Weakness resulting in a Failure Mode) should result in a new FMEA Item. Generating FMEA Items from the design elements of your model identified earlier in the Robustness Check list diagram saves time and helps avoid mistakes.

You can add existing FMEA Items to an FMEA Table by dragging them from the Containment tree to the FMEA table. New rows are created automatically. You can modify the added items and update the property in the table.

To add a new FMEA Item to the FMEA Table

1. In the FMEA Table, click Add New. A row is added in the FMEA Table, which shows the new FMEA Item. [IMAGE alt='' src='']
2. In the newly created FMEA Item's row and the **Name**column, double-click the designated cell to name the FMEA Item.

To add an existing FMEA Item to the FMEA Table

1. In the FMEA Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the **Select FMEA Item**dialog, select the required FMEA Item and click **OK**. A row is added to the FMEA Table, which shows the existing FMEA Item. 
 
**[IMAGE alt='' src='']**
3. In the newly created FMEA Item's row and the **Name**column, double-click the designated cell to name the FMEA Item.

##### Updating a Failure Mode

To update a Failure Mode to the FMEA Table

1. Double-click the designated cell in the **Failure Mode** column and the required FMEA Item's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Failure Mode_Edit button.png']
2. From the Select Class dialog, select the required Failure Mode and click OK. [ATTACHMENT filename='Select Class dialog.png']

Similarly, you can update the Cause in the FMEA Table.

##### Adding a Final Effect

To add a Final Effect to theFMEA Table

1. Double-click the designated cell in the **Final Effect** column and the required FMEA Item's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Final Effect_Edit.png']
2. From the Select Elements dialog, select the required Failure Mode and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Elements_dialog.png']

Similarly, you can add **Computed Effects, Prevention Controls, Detection Controls,** and **Recommended Actions**in the FMEA Table.

##### Adding an Action Priority

To add an Action Priority to theFMEA Table

1. Double-click the designated cell in the **Action Priority** column and the required FMEA Item's row and click [IMAGE alt='' src=''] .
2. In the Action Priority dialog, type in the required content.

Similarly, you can add **Revised Action Priority**in the FMEA Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p>An FMEA Table allows you to analyze the reliability aspect of your model and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. <span style="color:var(--ds-text,#172b4d);">The RAAML-based FMEA Table diagram is derived from an activity object and represents each FMEA Item—defined as the unique pairing of a failure mode with its corresponding cause—through a dedicated row associated with the activity.</span></p><p>In an FMEA Table, you can:</p><ul><li data-uuid="bcada771-7e23-4bea-88dd-0d0fc2d32fa2">Create a new FMEA Item directly in a table or add an existing one.</li><li data-uuid="aa59e8a2-b620-41f7-908a-8ff10b3d3936">Directly edit the properties of FMEA Items in a table.</li></ul><p>The following table describes each column name, its purpose, and relevant details:</p><table class="wrapped"><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><td><p><strong>Column Name</strong></p></td><td><p><strong>Description</strong></p></td></tr><tr class=""><td><p>Name</p></td><td><p>Displays an auto-generated counter for the FMEA item (this prefix counter is a preset customization) and a name. If the name is generated automatically (e.g., <span style="color:var(--ds-text,#172b4d);">from the creation of an FMEA Item in the Robustness Checklist)</span>, it is composed of the Failure Cause and its associated Failure Mode.</p></td></tr><tr class=""><td><p>Inputs</p></td><td><p>List of input pins of the activity element selected as the Scope of the FMEA study. <span style="color:var(--ds-text,#172b4d);">This is a non-editable field.</span></p></td></tr><tr class=""><td><p>Function</p></td><td><p>Activity selected as the scope of the FMEA study. <span style="color:var(--ds-text,#172b4d);">This is a non-editable field.</span></p></td></tr><tr class=""><td><p>Output</p></td><td><p><span>Lists one or more of the output pins that are declared on the activity element selected as the Scope of the FMEA study and that are being affected by a dedicated failure mode. Your selection is limited to the declared output pins on the activity referenced on the Function cell.</span></p></td></tr><tr class=""><td><p>Failure Mode</p></td><td><p>Specifies the Failure Mode specific to the FMEA Item Line. Failure Mode definition is as introduced in the <strong>Parameter Diagram </strong>section, referring to the description of the specific manner in which a component, subsystem, or system could potentially fail to meet the design intent.</p></td></tr><tr class=""><td><p>Classification</p></td><td><p>Corresponds to the categorization of FMEA items, derived from the evaluation of Severity and Occurrence values using a customizable function (preset out-of-the-box as: <span style="color:var(--ds-text,#172b4d);">CC in case severity &gt;= 9, SC in case 9 &gt; severity &gt;= 7, and AC in case 7 &gt; severity &gt;= 5</span>).</p></td></tr><tr class=""><td><p>Final Effect</p></td><td><p>Describes the effect of a Failure Mode on the end user or the environment (i.e., at the system-of-interest level). Multiple Final Effects can be specified for a single FMEA item. Each Final Effect can have a default Severity value assigned as its property. <span style="color:var(--ds-text,#172b4d);">To assign a Severity value, open the Specification window of the Final Effect and set the desired value.</span></p></td></tr><tr class=""><td><p>Computed Effect</p></td><td><p>An element describing <strong>the effect</strong> that a <strong>Failure Mode</strong> has <strong>on the system element under consideration</strong>. An FMEA Item (e.g., a single row of an FMEA Table) can have multiple Local Effects of Failure. <br />If the element under consideration is a subsystem directly underneath the system of interest level itself, <strong>the effect of the Failure Mode</strong> is the same as the <strong>Final Effect</strong> mentioned above in this table.</p></td></tr><tr class=""><td><p>Severity</p></td><td><p><span>The Severity of effects is a rating number associated with the most serious effect for a given failure mode for the operation being evaluated. It is a relative rating within the scope of the individual FMEA item and is determined without regard for occurrence or detection. Valid values range from 1 to 10 (lowest to highest severity).</span></p></td></tr><tr class=""><td><p>Cause</p></td><td><p><span>An element (either a lower-level Failure Mode or a dedicated Cause element) indicating the design weakness that leads to a Failure Mode. An FMEA item (e.g., a single row of an FMEA table) can have one Cause of Failure. A Cause can have default Occurrence and Detectability values assigned as properties. To assign these values, either open the Specification window of the Cause and set the desired Occurrence or Detectability, or edit them directly in the corresponding columns of the FMEA table.</span></p></td></tr><tr class=""><td><p>Prevention Controls</p></td><td><p>A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode. You can specify multiple Prevention controls for a single FMEA Item. <span style="color:var(--ds-text,#172b4d);">The type of object that can be elected as a Prevention Control is by default preset as a Requirement. The type can be customized.</span></p></td></tr><tr class=""><td><p>Occurrence</p></td><td><p><span>A rating number is associated with each cause for a given failure mode being evaluated. The occurrence rating considers the likelihood of occurrence during production. Valid values range from 1 to 10 (lowest to highest probability). A Cause must be identified in the dedicated cell before setting this value. Enter the value directly in the corresponding FMEA table cell or set it on the Failure Mode or Cause object via the containment tree.</span></p></td></tr><tr class=""><td><p>Criticality</p></td><td><p>The product of Severity and Occurrence ratings.</p></td></tr><tr class=""><td><p>Detection Controls</p></td><td><p>An element describing the measures implemented to detect a Failure Mode. Multiple Detection Control entries can be specified for a single FMEA <span style="color:var(--ds-text,#172b4d);">item. The type of object that can be elected as a Detection Control is by default preset as a Block. The type can be customized.</span></p></td></tr><tr class=""><td><p>Detection</p></td><td><p><span>Detection is the rating associated with the likelihood of detecting the failure mode and/or associated cause, according to defined criteria. </span><span>Ability to detect is the rating number associated with the combined capabilities of all the current process controls for a given cause and/or failure mode. You should not automatically presume the detection rating is low because the occurrence rating is low. Instead, the User assumes the failure has occurred, then assesses the capabilities of all the detection-type design controls to detect low-frequency failure modes and/or causes. The detection rating is identified without regard for severity or occurrence. </span><span>Valid Values range from 1 to 10 (highest to lowest detectability).</span></p></td></tr><tr class=""><td><p>Risk Priority Number</p></td><td><p><span>The risk priority number (RPN) is the product of the severity (S), occurrence (O), and detection (D) ratings. Within the scope of the individual FMEA, this value is between “1” and “1000”. </span><span>A benefit of RPN is that it provides an indicator of improvement (before and after actions taken) that reduces any one factor of severity, occurrence, or detection. It shows the distribution of RPN values for a project (Pareto), giving a high-level overview of the risk assessment. </span><span>You should be aware that the final RPN ratings are subjective and relative to a particular analysis.</span></p></td></tr><tr class=""><td><p>Action Priority</p></td><td><p><span>Assessment of the internal priority affecting the recommended <span style="color:var(--ds-text,#172b4d);">actions, as per the SAEJ 1739 rating scale.</span></span></p></td></tr><tr class=""><td><p>Recommended Action</p></td><td><p><span style="color:var(--ds-text,#172b4d);">The description of an action intended to reduce the Risk Priority Number. All critical or significant FMEA items should have associated recommended actions. These actions should focus on design improvements and be directed at mitigating the Cause of Failure or eliminating the Failure Mode. The type of object that can be elected as a Recommended Action element creation is by default preset as a Block. The type can be customized.</span></p></td></tr><tr class=""><td><p>Action Taken</p></td><td><p>A property describing what actions have been taken and the results of these actions <span style="color:var(--ds-text,#172b4d);">(free text capture)</span>.</p></td></tr><tr class=""><td><p>Responsible Person</p></td><td><p>Indicates the person responsible for completing a Recommended Action. <span style="color:var(--ds-text,#172b4d);">No specific object type is being preset to represent a Person.</span></p></td></tr><tr class=""><td><p>Target Date</p></td><td><p>A property defining the targeted completion date of a Recommended Action.</p></td></tr><tr class=""><td><p>Completion Date</p></td><td><p>A property assessing the completion date of a Recommended Action.</p></td></tr><tr class=""><td><p>Revised Severity</p></td><td><p><span>A property assessing the seriousness of the effect(s) of a potential Failure Mode on a component, subsystem, end user, or environment after mitigation. Valid values range from 1 to 10 (lowest to highest severity). A prerequisite is that an action has been taken</span></p></td></tr><tr class=""><td><p>Revised Occurrence</p></td><td><p><span style="color:var(--ds-text,#172b4d);">A property indicating the likelihood that a specific Cause of Failure will occur after mitigation. Valid values range from 1 to 10 (lowest to highest probability of occurrence).</span></p></td></tr><tr class=""><td><p>Revised Criticality</p></td><td><p>The product of Revised Severity and Revised Occurrence ratings.</p></td></tr><tr class=""><td><p>Revised Detection</p></td><td><p><span>A property measuring the likelihood of detecting a potential failure after mitigation. Valid values range from 1 to 10 (highest to lowest detectability).</span></p></td></tr><tr class=""><td><p>Revised Risk Priority Number</p></td><td><p>The product of Revised Criticality by Revised Detection.</p></td></tr><tr class=""><td><p>Revised Action Priority</p></td><td><p><span style="color:var(--ds-text,#172b4d);">Assessment of the internal priority affected by the recommended actions after mitigation.</span></p></td></tr></tbody></table><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="355c44ea-98b8-47eb-964b-a88c170180af"><ac:parameter ac:name="title">Tips</ac:parameter><ac:rich-text-body><ul><li data-uuid="6dc08ad0-c86e-4706-a2e5-1c692046f243">While selecting an FMEA Item element (line in the table):<ul><li>You can remove the line from the table using the dedicated <strong>Remove From Table </strong><span>command.</span></li><li>You can delete it from the containment tree (and the table) using the dedicated <strong>Delete </strong><span>command.</span></li></ul></li><li data-uuid="a323ffce-cc0f-4034-9733-2c195440a163">If a Robustness Check List (RCL) and/or Parameter Diagram exists for the activity, the user can navigate from the FMEA Table to one of those diagrams through a dedicated panel above the diagram. To learn more, refer to the <span style="color:var(--ds-text,#172b4d);"><ac:link><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ac:link> </span>page.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Failure Mode and Effect Analysis (FMEA) Table</h3><p>To create a Failure Mode and Effect Analysis (<span>FMEA) Table</span></p><hr /><ol><li data-uuid="35c8888d-77bc-4053-ba6a-fe840702910d">In the Containment tree, right-click the <strong>FMEA </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="946293a1-1c93-4661-a3fc-b76e9cf33ae4">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Safety and Reliability Analysis </strong>and select <strong>RAAML-based FMEA Table.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="FMEA_Select.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword FMEA and then select <strong><span style="color:var(--ds-text,#333333);">RAAML-based FMEA Table</span>.<br /><br /><ac:image><ri:attachment ri:filename="FMEA_Search.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="49d63220-7598-4a57-90fe-7d8160e7de7a">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog_FMEA.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image><br /><br />The FMEA Table is now displayed in the diagram pane of the modeling tool.</li></ol><h3 style="text-align: left;">Adding an FMEA Item to the <span>FMEA Table</span></h3><p>Each Failure mode linked to a Failure Effect (end user effect of a Failure Mode) or to a Failure Cause (element indicating a Design Weakness resulting in a Failure Mode) should result in a new FMEA Item. Generating FMEA Items from the design elements of your model identified earlier in the Robustness Check list diagram saves time and helps avoid mistakes.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="626fe21c-f3f6-4855-a861-577a41e59f18"><ac:rich-text-body><p>You can add existing FMEA Items to an FMEA Table by dragging them from the Containment tree to the FMEA table. New rows are created automatically. You can <span>modify the added items and update the property in the table.</span></p></ac:rich-text-body></ac:structured-macro><p>To add a new FMEA Item to the FMEA Table</p><hr /><ol><li data-uuid="e7ad82d4-332d-4d7a-836a-2c93674634d2"><span style="color:var(--ds-text,#333333);">In the FMEA Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New. </strong><span style="color:var(--ds-text,#333333);">A row is added in the FMEA Table, which shows the new FMEA Item.</span><br /><strong style="text-align: left;"><br /><ac:image><ri:attachment ri:filename="Add New.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image><br /><br /></strong></li><li data-uuid="01cf3e59-a5ce-48bb-b1a9-c6de4f3d757e"><span style="color:var(--ds-text,#333333);">In the newly created FMEA Item's row and the <strong>Name </strong>column, double-click the designated cell to name the FMEA Item.</span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><br /></p><p><span style="color:var(--ds-text,#333333);">To add an existing FMEA Item to the FMEA Table</span></p><hr /><ol><li data-uuid="a1de3be7-0d64-4926-ab31-2496fcd6c5a5"><span style="color:var(--ds-text,#333333);">In the FMEA Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="Add Existing.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image></span><br /><br /></strong></li><li data-uuid="57fd063a-272d-46b4-86e2-827d5ac8da90"><span style="color:var(--ds-text,#333333);">From the <strong>Select FMEA Item </strong>dialog, select the required FMEA Item and click <strong>OK</strong>. A row is added to the FMEA Table, which shows the existing FMEA  Item. <br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Select Activity dialog_FMEA.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image></strong><br /><br /></span></li><li data-uuid="c5aa1e5f-5fb5-45c1-a94e-80300938fb59"><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#333333);">In the newly created FMEA Item's row and the <strong>Name </strong>column, double-click the designated cell to name the FMEA Item.</span><br /></span></li></ol><h3 style="text-align: left;">Updating a Failure Mode</h3><p style="text-align: left;">To update a Failure Mode to the <span style="color:var(--ds-text,#333333);">FMEA Table</span></p><hr style="text-align: left;" /><ol style="text-align: left;"><li data-uuid="0a2cf8c1-9293-44ce-901b-c66a2397ea2c">Double-click the designated cell in the<span> <strong>Failure Mode </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_Edit button.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="4104f30c-a4b9-4d37-b7d5-0debc2c67b3d">From the<span> </span><strong>Select Class </strong>dialog, select the required Failure Mode and click <strong>OK.</strong><br /><br /><ac:image><ri:attachment ri:filename="Select Class dialog.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image><br /><br /></li></ol><p><span>Similarly, you can update the Cause in the FMEA Table.</span></p><h3>Adding a Final Effect</h3><p>To add a Final Effect <span style="color:var(--ds-text,#172b4d);">to the </span><span style="color:var(--ds-text,#172b4d);">FMEA Table</span></p><hr /><ol><li data-uuid="2542b7fd-c317-435f-b632-3124a0d9fa10">Double-click the designated cell in the<span> <strong>Final Effect </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Final Effect_Edit.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="f482c46e-680d-4477-a748-19131ef50d28">From the<span> </span><strong>Select Elements </strong>dialog, select the required Failure Mode and click <strong>OK</strong>. <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">To learn more about selecting elements, refer to the<span> </span></span><a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x Refresh1&amp;variant=default">Selecting Elements</a><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span> </span>page.<br /></span><br /><ac:image><ri:attachment ri:filename="Select Elements_dialog.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image></li></ol><p>Similarly, you can add <strong>Computed Effects,  Prevention Controls, Detection Controls,</strong> and <strong>Recommended Actions </strong>in the FMEA Table.</p><h3>Adding an Action Priority</h3><p>To add an Action Priority <span style="color:var(--ds-text,#172b4d);">to the </span><span style="color:var(--ds-text,#172b4d);">FMEA Table</span></p><hr /><ol><li data-uuid="5c661554-f0ec-4115-87e3-982e2404b31b">Double-click the designated cell in the<span> <strong>Action Priority </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode &amp; Effect Analysis" /></ri:attachment></ac:image></span>.</li><li data-uuid="2b68566d-4a44-4e53-9bda-bddd73203ceb">In the Action Priority dialog, type in the required content.</li></ol><p>Similarly, you can add <strong>Revised Action Priority </strong>in the FMEA Table.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=304009476 space=SSE version=1 -->
## PAGE 00003: (2026x Refresh1) Failure Mode Avoidance

- page_id: `304009476`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009476/2026x+Refresh1+Failure+Mode+Avoidance
- version_number: 1
- version_date: `2026-04-29T15:31:50.553+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

Quality and Safety disciplines are critical to ensure**reliable**and**safe**systems. The System Safety Engineer can perform a Design FMEA per SAE J1739:2021. Design FMEA is a type of FMEA that analyzes product design, focusing on potential design-related deficiencies to improve the design and ensure the product's safe and reliable operation during its useful life.

Based on the system architecture, the Systems Safety Engineer plugin enables:

- The creation of the Boundary Diagram and **Item** to finalize the scope (the relevant parts of the system to be analyzed).
- The creation of an item-based Interface Analysis table to study connections between functions.
- The creation of a Parameter Diagram to identify the measurable parameters that could affect the intended output of a given function.
- The creation of a Robustness Checklist to identify causality links between elements of a given function.
- The creation of a Failure Mode and Effects Analysis table

The Systems Safety Engineer is**RAAML-based**and partiallysupports **SAE J1739.**

**[IMAGE alt='' src='']**

###### Systems Safety Engineer workflow

To learn more about FMA, refer to the following pages:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">Quality and Safety disciplines are critical to ensure<span> </span><strong>reliable</strong><span> </span>and<span> </span><strong>safe</strong><span> </span>systems. The System Safety Engineer can perform a Design FMEA per SAE J1739:2021. Design FMEA is a type of FMEA that analyzes product design, focusing on potential design-related deficiencies to improve the design and ensure the product's safe and reliable operation during its useful life.</p><p style="text-align: left;">Based on the system architecture, the Systems Safety Engineer plugin enables: </p><ul style="text-align: left;"><li data-uuid="063b53a3-485f-4940-b472-b5ece00b238e">The creation of the <strong>Boundary Diagram</strong><span> </span>and<span> <strong>Item </strong></span>to finalize the scope (the relevant parts of the system to be analyzed).</li><li data-uuid="df94e614-94f0-4a97-943e-7ec0c8723c36">The creation of an item-based<span> </span><strong>Interface Analysis</strong><span> </span>table to study connections between functions.</li><li data-uuid="46d2d7be-34c0-4c8e-83f7-cf0e594d5821">The creation of a<span> </span><strong>Parameter Diagram</strong><span> </span>to identify the measurable parameters that could affect the intended output of a given function.</li><li data-uuid="b660748e-8aeb-455c-810d-b5b7bc0f528e">The creation of a<span> </span><strong>Robustness Checklist</strong><span> </span>to identify causality links between elements of a given function.</li><li data-uuid="a5ecc256-f5bf-4d09-a6a0-c443cfbcdd8b">The creation of a<span> </span><strong>Failure Mode and Effects Analysis</strong><span> </span>table </li></ul><p style="text-align: left;">The Systems Safety Engineer is<span> </span><strong>RAAML-based</strong><span> </span>and partially<span> </span>supports <strong>SAE J1739.</strong></p><p style="text-align: center;"><strong><ac:image ac:border="true" ac:height="646" ac:width="983"><ri:attachment ri:filename="SSE_Workflow.png"><ri:page ri:content-title="(2026x Refresh1) Failure Mode Avoidance" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">Systems Safety Engineer workflow</h6><p style="text-align: left;"><br /></p><p style="text-align: left;">To learn more about FMA, refer to the following pages:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2604d644-6c66-4c5d-9fcd-f56de98f5a3e" /></p>
````

<!--NOMAGIC_PAGE id=304009465 space=SSE version=2 -->
## PAGE 00004: (2026x Refresh1) Installation, licensing, and system requirements

- page_id: `304009465`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009465/2026x+Refresh1+Installation+licensing+and+system+requirements
- version_number: 2
- version_date: `2026-04-29T15:32:25.129+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

For information regarding installation, licensing, and system requirements, visit the[Installation, licensing, and system requirements](https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&version=2026x Refresh1)page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="with-breadcrumbs conf-macro output-block">For information regarding installation, licensing, and system requirements, visit the<span> </span><a href="https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&amp;version=2026x Refresh1">Installation, licensing, and system requirements</a><span> </span>page.</p>
````

<!--NOMAGIC_PAGE id=304009509 space=SSE version=1 -->
## PAGE 00005: (2026x Refresh1) Interface Analysis

- page_id: `304009509`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009509/2026x+Refresh1+Interface+Analysis
- version_number: 1
- version_date: `2026-04-29T15:31:50.855+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer > (2026x Refresh1) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

An Interface Analysis table consists of system interfaces, their types (e.g., physical, data, energy, etc.), source/target, and related functions. An Interface Analysis table:

- Starts from any item identified in the Boundary Diagram.
- Captures the interaction between source and target elements.
- Informs the “class” of the interaction.
- Tells whether the interface involves external actors/components.
- Identifies if the interaction is beneficial or detrimental.
- Assigns explicit responsibility to each end of the interaction.
- Defines the functions involved and their “measurable” target and range of variation.

##### Creating an Interface Analysis Table

To create an Interface Analysis Table

1. In the Containment tree, right-click the **Interface** **Analysis** package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Interface Analysis****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword interface and then select **Interface Analysis** . 
 
[IMAGE alt='' src=''] The Interface Analysis Table is now displayed in the diagram pane of the modeling tool.

##### Defining the scope

To define the scope for the Interface Analysis Table

- From the Containment tree, drag and drop the Lamp Scope element on the Scope of the Interface Analysis table. [ATTACHMENT filename='Lamp Scope_drag and drop.png']

##### Adding an Interaction Connector to the Interface Analysis Table

To add an existing Interaction Connector

1. In the Interface Analysis Table, click **Add Existing. 
 
[IMAGE alt='' src='']**
2. In the Select Interaction Connector dialog, select the required Interaction Connector. 
 
[IMAGE alt='' src=''] 
 
A row is added to the Interface Analysis Table, displaying the existing Interaction Connector.

##### Adding a Functional Range

To add a Functional Range

1. Double-click the designated cell in the**Functional Range** column and the required scope element's row and click [IMAGE alt='' src=''].
2. In the Enter Range dialog, enter the Min and Max values and click **OK**. 
 
[IMAGE alt='' src='']

##### Adding a Functional Target

To add a Functional Target

1. Double-click the designated cell in the**Functional Target** column and the required scope element's row and click [IMAGE alt='' src=''].
2. In the Enter Functional Target dialog, enter the****Value and click **OK**. 
 
[IMAGE alt='' src='']

##### Assigning Strength

To assign Strength

1. Double-click the designated cell in the **Strength**column and the required scope element's row, and select the strength from the drop-down list. 
 
[IMAGE alt='' src='']

##### Adding Affected Function

To add Affected Function

1. Double-click the designated cell in the scope element's row and the Affected Function column and click [ATTACHMENT filename='Three Dot _Icon.png'] . The Select Affected Function dialog opens. [ATTACHMENT filename='Affected Function dialog.png']
2. In the Select Affected Function dialog, click the [ATTACHMENT filename='Three Dot _Icon.png'] icon, found near the Call Behavior Action Element.
3. In the Select Call Behavior Action dialog, select the Call Behavior Action and click OK. [ATTACHMENT filename='Call Behavior Action dialog.png']
4. In the Select Affected Function dialog, click the [ATTACHMENT filename='Three Dot _Icon.png'] icon, found near the Activity Element.
5. In the Select Activity dialog, select the Activity and click OK. [IMAGE alt='' src='']

##### Adding a Source/Target Interface Owner, Interface Owner Concurrence Date, and Interface Owner Activity

To add a Source/Target Interface Owner

1. Double-click the designated cell in the scope element's row and the Source Interface Owner column and type in the required details.
2. Double-click the designated cell in the scope element's row and the Target Interface Owner column and type in the required details.

Similarly, add the required details for the Source/Target Interface Owner Concurrence Date and Interface Owner Activity.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p style="text-align: left;">An Interface Analysis table consists of system interfaces, their types (e.g., physical, data, energy, etc.), source/target, and related functions. An Interface Analysis table:</p><ul style="text-align: left;"><li data-uuid="52217361-d5da-4dda-87b4-a46da0933df3">Starts from any item identified in the Boundary Diagram.</li><li data-uuid="56991033-a84f-469c-9f20-62431475e121">Captures the interaction between source and target elements.</li><li data-uuid="f57dd2a2-c065-4fc4-a642-3d6cc0c8c146">Informs the “class” of the interaction.</li><li data-uuid="f958a193-e77f-44ad-ba9a-62970de7ad2b">Tells whether the interface involves external actors/components.</li><li data-uuid="7977e60e-17da-4f2d-b3be-c28d3abf5849">Identifies if the interaction is beneficial or detrimental.</li><li data-uuid="dc995ceb-7e10-4fbc-b612-042fd75e143e">Assigns explicit responsibility to each end of the interaction.</li><li data-uuid="1211dab6-f46d-4485-a93d-db7f59127fe5">Defines the functions involved and their “measurable” target and range of variation.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating an Interface Analysis Table</h3><p>To create an <span>Interface Analysis Table</span></p><hr /><ol><li data-uuid="39362494-d719-4f02-8a50-ee4590d531d4">In the Containment tree, right-click the <span><strong>Interface</strong> <strong>Analysis </strong></span>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="7de72549-c91d-4c5d-9dec-ebca2efb1500">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <span><strong>Interface Analysis</strong></span><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Interface Analysis_Select.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword interface and then select <span style="color:var(--ds-text,#333333);"><span><strong>Interface Analysis</strong></span></span><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Interface Analysis_Search.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /><br /></strong>The <span style="color:var(--ds-text,#333333);">Interface </span><span style="color:var(--ds-text,#333333);">Analysis Table </span><span>is now displayed in the diagram pane of the modeling tool.</span></li></ul></li></ol><h3>Defining the scope</h3><p>To define the scope for the Interface Analysis Table </p><hr /><ul><li data-uuid="b83b8c21-31f0-4fd6-8961-f41db919a507">From the Containment tree, drag and drop the <strong>Lamp Scope </strong>element on the<strong> Scope </strong>of the Interface Analysis table.<br /><br /><ac:image><ri:attachment ri:filename="Lamp Scope_drag and drop.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image></li></ul><h3 style="text-align: left;">Adding an Interaction Connector to the <span>Interface Analysis Table</span></h3><p><span>To add an existing Interaction Connector</span></p><hr /><ol><li data-uuid="89cd3896-12cc-4745-bd61-fd66b25168e4"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Interface <ac:inline-comment-marker ac:ref="97cddb50-b898-41ac-a21e-39bc461109a2">Analysis Table</ac:inline-comment-marker>, click <strong style="text-align: left;"><ac:inline-comment-marker ac:ref="d8c254f3-4fe4-4660-ac9a-de2286ac4a54">Add Existing.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Add Existing.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /><br /></strong></span></li><li data-uuid="ac17b159-822a-46bd-953f-1038fa52db8f"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Select Interaction Connector <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">dialog, select the required Interaction Connector.<br /><br /><ac:image><ri:attachment ri:filename="Select Interaction Connector dialog.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /><br />A row is added to the Interface Analysis Table, displaying the existing <span>Interaction Connector</span>.<br /></span></span></li></ol><h3>Adding a Functional Range</h3><p>To add a Functional Range</p><hr /><ol><li data-uuid="94d1f86d-6a6d-4c3c-8235-eac52692072f"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the<span> </span><strong>Functional Range</strong> </span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">column and the required scope element's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image></span></span>.</span></span></li><li data-uuid="39a510c8-3932-469e-8982-e6462c13a708"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span>In the Enter Range dialog, enter the Min and Max values and click <strong>OK</strong>.<br /><br /><ac:image ac:border="true" ac:height="105" ac:width="249"><ri:attachment ri:filename="Functional Range dialog.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /></span></span></li></ol><h3>Adding a Functional Target</h3><p>To add a Functional Target</p><hr /><ol><li data-uuid="7f19c8ea-bef1-426f-a449-cc6e15699001"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the<span> </span><strong>Functional Target </strong></span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">column and the required scope element's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image></span></span>.</span></span></li><li data-uuid="5db8be0f-102f-45fc-bc17-d278e3aded1b"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span>In the Enter Functional Target dialog, enter the<strong> </strong>Value and click <strong>OK</strong>.<br /><br /><ac:image ac:border="true" ac:height="103" ac:width="226"><ri:attachment ri:filename="Functional Target dialog.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /></span></span></li></ol><h3>Assigning Strength</h3><p><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">To assign Strength</span></p><hr /><ol><li data-uuid="93e08759-3115-4e8d-9aa5-5660a14c50ba"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the <strong>Strength </strong>column and the required scope element's row, and select the strength from the drop-down list.<br /><br /><ac:image><ri:attachment ri:filename="Strenth drop-down.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /></span></li></ol><h3><span>Adding Affected Function</span></h3><p><span>To add Affected Function</span></p><hr /><ol><li data-uuid="46f4eca3-2eeb-4caa-b0a1-8b62c16d130f">Double-click the designated cell in the scope element's row and the Affected Function column and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image>. The Select Affected Function dialog opens.<br /><br /><ac:image ac:border="true" ac:height="163" ac:width="354"><ri:attachment ri:filename="Affected Function dialog.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="dfa1db28-1ec2-4fc4-b661-6329c53c33be">In the Select Affected Function dialog, click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image> icon, found near the Call Behavior Action Element.</li><li data-uuid="ca4a35c1-0032-412f-9f32-32b48e54ae66">In the Select Call Behavior Action dialog, select the Call Behavior Action and click OK.<br /><br /><ac:image ac:border="true" ac:height="410" ac:width="533"><ri:attachment ri:filename="Call Behavior Action dialog.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="7286495b-99a4-49b1-ab8a-244eababa7fd">In the Select Affected Function dialog, click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image> icon, found near the Activity Element.</li><li data-uuid="e4645f88-b602-4fe3-ba86-f7a36510b49e">In the Select Activity dialog, select the Activity and click OK.<br /><span><br /><ac:image ac:border="true" ac:height="382" ac:width="531"><ri:attachment ri:filename="Select Activity dialog.png"><ri:page ri:content-title="(2026x Refresh1) Interface Analysis" /></ri:attachment></ac:image><br /></span></li></ol><h3>Adding a Source/Target Interface Owner, Interface Owner Concurrence Date, and Interface Owner Activity</h3><p>To add a Source/Target Interface Owner</p><hr /><ol><li data-uuid="bec27aff-a909-4417-b4ac-e901c8406ab8">Double-click the designated cell in the scope element's row and the<strong> Source Interface Owner </strong>column and type in the required details.</li><li data-uuid="49f4f2a7-b598-45ae-a1e6-e1e60c81be49">Double-click the designated cell in the scope element's row and the <strong>Target Interface Owner </strong>column and type in the required details.</li></ol><p>Similarly, add the required details for the <span>Source/Target Interface Owner Concurrence Date and Interface Owner Activity.</span></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=304009463 space=SSE version=2 -->
## PAGE 00006: (2026x Refresh1) Introduction to Systems Safety Engineer

- page_id: `304009463`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009463/2026x+Refresh1+Introduction+to+Systems+Safety+Engineer
- version_number: 2
- version_date: `2026-04-29T15:32:25.038+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

**Model-based safety** refers to a systematic approach to ensure the safety of complex systems by using formal models that represent the system’s structure, behavior, and environment. These models are used to analyze, predict, and verify safety properties before and during the system’s operation. Model-based safety engineering also aims to :

- Identify safety risks early , perform safety verification and validation , and guide the design of safety mechanisms.
- Help detect unsafe states or behaviors before physical implementation or deployment , reducing costly errors.
- Unify domains into one analysis framework, as safety issues may arise from software bugs, hardware faults, cyber-attacks, or their combination.
- Provide traceable, repeatable proofs of safety requirements to ease regulatory compliance and certification
- Enables the use of automated model checking and simulation tools that can exhaustively explore possible scenarios .

The Systems Safety Engineering plugin contains the ISO 26262 plugin. To learn more, refer to the [ISO 26262 plugin](https://docs.nomagic.com/CSRA/?contextKey=iso-26262-functional-safety&version=2026x Refresh1) user guide.

#### NOTE: Prerequisites

Prerequisites

To install and use the Systems Safety Designer, ensure that one of the following modeling tools is installed:

- Magic Cyber Systems Engineer
- Magic Cyber Systems of Systems Architect
- Cameo Systems Modeler - Architect Edition
- Cameo Systems Modeler - Enterprise Edition
- Cameo Enterprise Architecture
- Magic Draw (any version) with SysML plugin installed

To learn more about how to download the installation files, refer to [Downloading installation files](https://docs.nomagic.com/IL/?contextKey=downloading-installation-files&version=2026x Refresh1).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Model-based safety</strong> refers to a systematic approach to ensure the safety of complex systems by using formal models that represent the system’s structure, behavior, and environment. These models are used to analyze, predict, and verify safety properties before and during the system’s operation. Model-based safety engineering also aims to :</p><ul><li data-uuid="151084d2-589a-49ae-90fc-0a1300fd4e74"><strong>Identify safety risks early</strong>, perform <strong>safety verification and validation</strong>, and guide the design of safety mechanisms.</li><li data-uuid="c9c4db51-4534-4d29-876e-2a6b3f45ccc9">Help detect unsafe states or behaviors <strong>before physical implementation or deployment</strong>, reducing costly errors.</li><li data-uuid="69d2ebba-63b2-428e-8d52-dcdf7af979c2">Unify domains into one analysis framework, as safety issues may arise from software bugs, hardware faults, cyber-attacks, or their combination.</li><li data-uuid="045a44ee-ba3e-4791-a440-b36774af581c">Provide traceable, repeatable proofs of safety requirements to ease regulatory compliance and certification</li><li data-uuid="83cd63c7-58f4-4412-9ec3-cd8ffb06e4a4">Enables the use of automated model checking and simulation tools that can exhaustively explore possible scenarios<ac:inline-comment-marker ac:ref="b862b50b-d6d3-475f-a880-b127214b6211">.</ac:inline-comment-marker></li></ul><p>The Systems Safety Engineering plugin contains the ISO 26262 plugin. To learn more, refer to the <a href="https://docs.nomagic.com/CSRA/?contextKey=iso-26262-functional-safety&amp;version=2026x Refresh1">ISO 26262 plugin</a> user guide.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6f459f96-4d19-47a8-8187-d08bea2c157e"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">To install and use the Systems Safety Designer, ensure that one of the following modeling tools is installed:</span></p><ul><li data-uuid="5ebb08d5-10cc-46ca-9e49-452622525e38"><p>Magic Cyber Systems Engineer</p></li><li data-uuid="5cfec0e3-e6d2-43c6-9613-2b89f1358904"><p>Magic Cyber Systems of Systems Architect</p></li><li data-uuid="76e1c66e-ba4d-4d18-a2ee-1a7881aa1fec"><p>Cameo Systems Modeler - Architect Edition</p></li><li data-uuid="f1569cc9-99d7-4240-8052-3e011dee6936"><p>Cameo Systems Modeler - Enterprise Edition</p></li><li data-uuid="af8a0cd7-8238-4b27-b35f-207bdcd91045"><p>Cameo Enterprise Architecture</p></li><li data-uuid="fdae7457-7c07-4075-b5c5-7b5fe32f3acc"><span style="color:var(--ds-text,#333333);">Magic Draw (any version) with SysML plugin installed</span></li></ul><p>To learn more about how to download the installation files, refer to <a href="https://docs.nomagic.com/IL/?contextKey=downloading-installation-files&amp;version=2026x Refresh1">Downloading installation files</a>.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=304009527 space=SSE version=2 -->
## PAGE 00007: (2026x Refresh1) Parameter Diagram

- page_id: `304009527`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009527/2026x+Refresh1+Parameter+Diagram
- version_number: 2
- version_date: `2026-04-29T15:32:25.617+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer > (2026x Refresh1) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

| Concepts | Description |
| --- | --- |
| Failure Mode | A Failure Mode represents a Specific way in which a component, subsystem, or system can fail to perform its intended function. It describes how the failure happens, i.e., the manner or mechanism of failure, not the cause or the consequence directly, but the mode or form the failure takes. |
| Failure Effect | An element describing the effect that a Failure Mode has on the system element under consideration (user, system, subsystem) |
| Noise Factors | Noise factors are sources of uncontrollable variability in a system. These are typically outside the direct control of the designer and introduce disturbances that may affect performance or reliability. The following are the types of Noise Factors that can be created. |
| Piece-to-Piece Variation Noise Factor | Piece-to-Piece Variation is a noise factor referring to variability between different units or parts of the same product. It can include:Manufacturing tolerances (dimension, weight, resistance, etc.)Material variability or changes in suppliersTool wear or production environment conditionsBatch-to-batch differences (also referenced as lot-to-lot variation) in production |
| Change Over Time Noise Factor | Change Over Time refers to system or component variations that occur gradually or incrementally during the lifetime of a product, often due to aging, fatigue, wear, drift, or environmental exposure. |
| Customer Usage Noise Factor | A Customer Usage Noise Factor is a type of uncontrollable variation stemming from how different users interact with the product in real-life scenarios, including misuse within plausible limits, erratic behavior, or varying usage environments. |
| System Interaction Noise Factor | A System Interaction Noise Factor is a disturbance or variability introduced by another system, component, or module, which is outside the local design scope, but interacts through a shared interface, environment, or resource.They are often not visible in unit testing but appear in integration testing.They may stem from electrical, mechanical, software, or communication interfaces.They are uncontrolled from the perspective of the system under analysis. |
| External Environment Noise Factor | An External Environment Noise Factor is a type of variability introduced by the physical, chemical, or climatic conditions in the system’s operating environment that may affect its behavior, functionality, or lifetime. |
| Control Factor | A Control factor is a design parameter or setting that you can actively choose, design, or adjust to achieve the desired system behavior, despite the presence of noise or variation. |
| Unintended output | An unintended output is any system response, signal, or command that is not expected, not commanded, or not aligned with the intended function, whether due to a failure, error, or disturbance. It should be selected among the type "activity pins" (i.e., object "parameters" and its derivative). |

##### Creating a Parameter Diagram

To create a Parameter Diagram

1. In the Containment tree, right-click Parameter Diagram package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Parameter Diagram****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword parameter and then select Parameter Diagram . 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity dialog.png'] The Parameter Diagram is now displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='Parameter diagram.png']

##### Creating a Failure Mode or Effect

To create a Failure Mode or Effect

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  - In the dialog, expand RAAML and select Failure Mode or Effect. 
 
[IMAGE alt='' src='']
  - In the search tab, type the keyword failure or effect, and then select Failure Mode or Effect. 
 
[IMAGE alt='' src='']
3. Name the newly created Failure Mode or Failure Effect in the Containment tree. An automated number is added with a **Counter** that is automatically added once validated.

##### Adding a Failure Mode or Effect in the Parameter Diagram

To add a Failure Mode or Effect in the Parameter Diagram

1. In the Parameter Diagram, select the Failure Mode or Failure Effect cell and cl ick[IMAGE alt='' src=''].
2. In the Select Elements dialog, select the required failure modes or failure effects and click **OK**. To learn more about selecting elements, refer to the [Selecting Elements](https://docs.nomagic.com/MT/?contextKey=selecting-elements&version=2026x Refresh1&variant=default) page. 
 
[IMAGE alt='' src='']

##### Creating a Noise Factor

To create a Noise Factor from the containment tree

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  - In the dialog, expand Failure Mode Avoidance and select the required type of Noise Factor. [IMAGE alt='' src='']
  - In the search tab, type the required keyword and then select the required type of Noise Factor . [ATTACHMENT filename='Piece to Piece Variation_search.png'] Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.
3. Name the newly created Piece-to-Piece Variation Noise Factor in the Containment tree.

##### Adding a Noise Factor

To add a Noise Factor in the Parameter Diagram

1. In the Parameter Diagram, select the corresponding Noise Factor cell (i.e., Piece to Piece Variation, Change Over Time, Customer Usage, System Interaction, or External Environment ), and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. In the Select Elements dialog, select the required Noise Factor and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Activity dialog_Noise Factor addition.png'] You can create any type of Noise Factor in the Select Elements dialog. To learn more, refer to the [Creating new elements](https://docs.nomagic.com/MT/?contextKey=creating-new-elements&version=2026x Refresh1&variant=default)page.Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.

##### Creating Control Factor or Unintended Output

To create a Control Factor or Unintended Output from the containment tree

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  1. In the dialog, expand General and select Requirement. 
 
[IMAGE alt='' src='']
  2. In the search tab, type the keyword "requirement" and then select Requirement. 
 
[IMAGE alt='' src='']
3. Name the newly created Requirement in the Containment tree. An automated number is added with a **Counter** that is automatically added once validated.

##### Adding a Control Factor, Unintended Output, or Failure Mode of Unintended Output

To add a Control Factor or Unintended Output in the Parameter Diagram

1. In the Parameter Diagram, select the corresponding cell for Control Factor, Unintended Output, or Failure Mode of Unintended Output and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. In the Select Elements dialog, select the required Control Factor or Unintended Output, or Failure Mode of Unintended Output, and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Elements_Control Factor or Unintended Output.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Concepts</th><th>Description</th></tr><tr><td><strong>Failure Mode</strong></td><td>A Failure Mode represents a Specific way in which a component, subsystem, or system can fail to perform its intended function. It describes <strong>how</strong> the failure happens, i.e., the manner or mechanism of failure, not the cause or the consequence directly, but the mode or form the failure takes.</td></tr><tr><td><strong><span>Failure Effect</span></strong></td><td><span><span style="color:var(--ds-text,#172b4d);">An element describing </span><strong style="text-align: left;">the effect</strong><span style="color:var(--ds-text,#172b4d);"> that a </span><strong style="text-align: left;">Failure Mode</strong><span style="color:var(--ds-text,#172b4d);"> has </span><strong style="text-align: left;">on the system element under consideration (</strong><span style="color:var(--ds-text,#172b4d);">user, system, subsystem)</span></span></td></tr><tr><td><strong>Noise Factors</strong></td><td>Noise factors are sources of uncontrollable variability in a system. These are typically outside the direct control of the designer and introduce disturbances that may affect performance or reliability. The following are the types of Noise Factors that can be created.</td></tr><tr><td><strong>Piece-to-Piece Variation </strong><strong>Noise Factor</strong></td><td><p>Piece-to-Piece Variation is a noise factor referring to variability between different units or parts of the same product. It can include:</p><ul><li data-uuid="45d53b73-45e9-4759-9eee-60375f1ab59a">Manufacturing tolerances (dimension, weight, resistance, etc.)</li><li data-uuid="8e07dfc9-0b1a-40e2-b34f-8a8826a5052a">Material variability or changes in suppliers</li><li data-uuid="d56c1e58-8fd2-4b12-b3e2-9a8baff69c8b">Tool wear or production environment conditions</li><li data-uuid="79ac5502-dcc3-4344-9ec0-9b57bbc7802f">Batch-to-batch differences (also referenced as lot-to-lot variation) in production</li></ul></td></tr><tr><td><strong>Change Over Time Noise Factor</strong></td><td>Change Over Time refers to system or component variations that occur gradually or incrementally during the lifetime of a product, often due to aging, fatigue, wear, drift, or environmental exposure.</td></tr><tr><td><strong>Customer Usage Noise Factor</strong></td><td><span>A </span><span>Customer Usage Noise Factor</span><span> is a type of </span><span>uncontrollable variation</span><span> stemming from how </span><span>different users</span><span> interact with the product in </span><span>real-life scenarios</span><span>, including </span><span>misuse within plausible limits</span><span>, </span><span>erratic behavior</span><span>, or </span><span>varying usage environments</span><span>.</span></td></tr><tr><td><strong>System Interaction Noise Factor</strong></td><td><p>A System Interaction Noise Factor is a disturbance or variability introduced by another system, component, or module, which is outside the local design scope, but interacts through a shared interface, environment, or resource.</p><ul><li data-uuid="efc14096-f0e3-49ad-ad99-fa28e1858de7">They are often not visible in unit testing but appear in integration testing.</li><li data-uuid="4a5ed891-db93-44a6-980e-d41d1afffe60">They may stem from electrical, mechanical, software, or communication interfaces.</li><li data-uuid="74c12ac5-1882-44a6-b2bb-4289b4f259e7">They are uncontrolled from the perspective of the system under analysis.</li></ul></td></tr><tr><td><strong>External Environment Noise Factor</strong></td><td>An External Environment Noise Factor is a type of variability introduced by the physical, chemical, or climatic conditions in the system’s operating environment that may affect its behavior, functionality, or lifetime.</td></tr><tr><td><strong>Control Factor</strong></td><td>A Control factor is a design parameter or setting that you can actively choose, design, or adjust to achieve the desired system behavior, despite the presence of noise or variation.</td></tr><tr><td><strong><span>Unintended output</span></strong></td><td><span style="color:var(--ds-text,#172b4d);">An </span><span style="color:var(--ds-text,#172b4d);">unintended output</span><span style="color:var(--ds-text,#172b4d);"> is any system response, signal, or command that is </span><span style="color:var(--ds-text,#172b4d);">not expected</span><span style="color:var(--ds-text,#172b4d);">, </span><span style="color:var(--ds-text,#172b4d);">not commanded</span><span style="color:var(--ds-text,#172b4d);">, or </span><span style="color:var(--ds-text,#172b4d);">not aligned with the intended function,</span><span style="color:var(--ds-text,#172b4d);"> whether due to a failure, error, or disturbance. It should be selected among the type &quot;activity pins&quot; (i.e., object &quot;parameters&quot; and its derivative). </span></td></tr></tbody></table></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Parameter Diagram</h3><p>To create a Parameter Diagram </p><hr /><ol><li data-uuid="dbe06a17-67f5-4968-9595-84f52eb78e67">In the Containment tree, right-click <strong>Parameter Diagram </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="3685c10d-64e6-47a9-8466-8087547d61cd">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Parameter Diagram</strong><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Parameter diagram_Select.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword parameter and then select <strong>Parameter Diagram</strong><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Parameter diagram_Search.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="d961e2e9-472f-427a-bb0f-f3007bd0373a">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br />The Parameter Diagram is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image ac:border="true" ac:height="510" ac:width="1065"><ri:attachment ri:filename="Parameter diagram.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image></li></ol><h3><span style="color:var(--ds-text,#172b4d);">Creating a Failure Mode or Effect</span></h3><p>To create a Failure Mode or Effect</p><hr /><ol><li data-uuid="1721bc3d-9dc8-43ba-add0-b1ab2ddcdc85">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="c8eeb92d-dd2f-46e6-915c-5ddc0713548e">Do one of the following:<br /><ul><li>In the dialog, expand <strong>RAAML </strong>and select <strong>Failure Mode </strong>or <strong>Effect.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_select.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br /></strong></li><li>In the search tab, type the keyword failure or effect, and then select <strong>Failure Mode </strong>or <strong>Effect.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_search.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li data-uuid="7c21892f-9237-419c-b496-c167e592c6be"><span style="color:var(--ds-text,#172b4d);">Name the newly created Failure Mode or Failure Effect in the Containment tree.</span><br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3d915e30-1796-4499-b98b-66fb6e771a7d"><ac:rich-text-body><p>An automated number is added with a <strong>Counter</strong> that is automatically added once validated.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3><span style="color:var(--ds-text,#172b4d);">Adding a Failure Mode or Effect in the Parameter Diagram</span></h3><p>To add a Failure Mode or Effect in the Parameter Diagram</p><hr /><ol><li data-uuid="d0ea622d-64ec-4806-a05a-f7fc4ce85074">In the Parameter Diagram, select the Failure Mode or Failure Effect cell and <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">cl</span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">ick<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image></span></span>.</span></li><li data-uuid="90424724-5225-48e2-b816-cdf0250b7dba"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Select Elements dialog, select the required failure modes or failure effects and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x Refresh1&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /></span></li></ol><h3>Creating a <span>Noise Factor</span></h3><p>To create a Noise Factor from the containment tree</p><hr /><ol><li data-uuid="7e644063-f402-4f2f-9f29-c5d7f28045fc">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="6e9aaef9-ffa3-4262-adc2-c4d9e90e74bd">Do one of the following:<br /><ul><li>In the dialog, expand <strong>Failure Mode Avoidance </strong>and select the required type of Noise Factor.<strong><br /><br /><ac:image><ri:attachment ri:filename="Piece to Piece Variation_select.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br /></strong></li><li>In the search tab, type the required keyword and then select the required type of Noise Factor<strong>.<br /></strong><br /><ac:image><ri:attachment ri:filename="Piece to Piece Variation_search.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="04bf90ca-1ca8-4a7e-9ade-30b78249ba4b"><ac:rich-text-body><p>Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.</p></ac:rich-text-body></ac:structured-macro></li></ul></li><li data-uuid="fcd957b2-48b9-4c0e-a061-23ae3d26406b"><span style="color:var(--ds-text,#172b4d);">Name the newly created Piece-to-Piece Variation Noise Factor in the Containment tree.</span></li></ol><h3>Adding a Noise Factor</h3><p>To add a Noise Factor in the Parameter Diagram</p><hr /><ol><li data-uuid="af64a9b1-5c71-4e34-b4e6-768dc948ce85">In the Parameter Diagram, select the corresponding Noise Factor cell (i.e., <strong>Piece to Piece Variation, Change Over Time, Customer Usage, System Interaction, </strong>or<strong> External Environment</strong>),<strong> </strong>and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image>.</li><li data-uuid="d09e8bf0-f64c-47f4-8b50-4fdfcdcd184d">In the Select Elements dialog, select the required Noise Factor and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x Refresh1&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog_Noise Factor addition.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4a74c2e1-4677-437e-804a-06824d20908d"><ac:rich-text-body><ul><li>You can create any type of Noise Factor in the Select Elements dialog. To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=creating-new-elements&amp;version=2026x Refresh1&amp;variant=default">Creating new elements</a><span> page.</span></li><li>Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.</li></ul></ac:rich-text-body></ac:structured-macro></li></ol><h3>Creating Control Factor or Unintended Output</h3><p>To create a Control Factor or Unintended Output from the containment tree</p><hr /><ol><li data-uuid="e6db19f3-b399-4125-9e1b-282a6109b8a8">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="09acf9ab-2852-4a0f-8355-172958cec6db">Do one of the following:<ol><li>In the dialog, expand <strong>General </strong><span>and select </span><strong>Requirement.<br /><br /><ac:image><ri:attachment ri:filename="Requirement_select.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br /></strong></li><li>In the search tab, type the keyword &quot;requirement&quot; and then select <strong>Requirement.<br /><br /><ac:image ac:thumbnail="true" ac:height="170"><ri:attachment ri:filename="Requirement_search.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image><br /><br /></strong></li></ol></li><li data-uuid="5c74b968-ba79-46f5-be09-d6562fc66dfa"><span style="color:var(--ds-text,#172b4d);">Name the newly created Requirement in the Containment tree.<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cf339c00-03ea-4f63-ae24-80251e57fa31"><ac:rich-text-body><p>An automated number is added with a <strong>Counter</strong> that is automatically added once validated.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3>Adding a Control Factor, Unintended Output, or Failure Mode of Unintended Output</h3><p>To add a Control Factor or Unintended Output in the Parameter Diagram</p><hr /><ol><li data-uuid="781ecf57-8603-4d35-ab8a-2c04dbf5bba9">In the Parameter Diagram, select the corresponding cell for Control Factor, Unintended Output, or Failure Mode of Unintended Output and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image>.</li><li data-uuid="70fdbe5d-8106-4e32-bfde-e8aa4223361c">In the Select Elements dialog, select the required Control Factor or Unintended Output, or Failure Mode of Unintended Output, and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x Refresh1&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements_Control Factor or Unintended Output.png"><ri:page ri:content-title="(2026x Refresh1) Parameter Diagram" /></ri:attachment></ac:image></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=304009563 space=SSE version=2 -->
## PAGE 00008: (2026x Refresh1) Robustness Checklist

- page_id: `304009563`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009563/2026x+Refresh1+Robustness+Checklist
- version_number: 2
- version_date: `2026-04-29T15:32:25.825+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer > (2026x Refresh1) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

For a specific function/activity, a Robustness Check List allows verifying that prevention controls (design methods) and detection controls (test methods) are adequate given the impact of failure modes/failure effects to be covered and the range of variation of noise factors that cause these failure modes/failure effects to arise.

The rows and columns of the Robustness Check List display the noise factors with their associated ranges of variation, the failure causes, the failure modes, the failure effects, the prevention controls, the detection controls, and the recommended actions associated with the function/activity for which the RCL is established. All these elements could come from the function/activity Parameter Diagram, except the failure causes, which are introduced manually in the Robustness Check List.

**EssentialInformation:**

- The robustness checklist diagram is created based on an activity object.
- All relationships in the Robustness Checklist can be deleted by right-clicking the cell and selecting the corresponding delete command. It can also be deleted from the model itself by pressing the Delete key on the Keyboard.
- The Parameter diagram and the FMEA table also show all existing relationships.
- If a Parameter Diagram and/or an FMEA table exist for the activity, you can navigate from the Robustness Checklist with the help of the commands present in the toolbar. The following table displays the icons and functions of the commands: IconDescription[IMAGE alt='' src='']Opens the Function in the Parameter Diagram[IMAGE alt='' src='']Opens the Function in the RAAML-based FMEA Table

The Robustness Checklist is a Dependency Matrix. To learn more, refer to the [Dependency Matrix](https://docs.nomagic.com/MT/?contextKey=dependency-matrix&version=2026x Refresh1&variant=default)page.

##### Creating a Robustness Checklist

To create a Robustness Checklist

1. In the Containment tree, right-click the Robustness Checklist package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Robustness Checklist.** [IMAGE alt='' src='']
  - In the search tab, type the keyword robust and then select Robustness Checklist. 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity.png'] The Robustness Checklist is now displayed in the diagram pane of the modeling tool. You must focus on identifying relationships with the aid of the white cells, as the grey cells are not editable. [ATTACHMENT filename='Robustness_Checklist.png']

##### Adding an element to the Robustness Checklist

To add an element to the Robustness Checklist

1. In the containment Tree, select the element to be added.
2. Drag and drop the element on the Column corresponding to the element folder and refresh the diagram. [ATTACHMENT filename='Adding element.png']

##### Deleting elements from the Robustness Checklist

To delete elements from the Robustness Checklist

1. In the Robustness Checklist, select the element to be deleted.
2. Right-click and select Remove from the Matrix from the Contextual menu. [ATTACHMENT filename='Delete Element.png']

You can completely delete the element by pressing the Delete button on the Keyboard.

##### Creating a range for the Noise Factor

With the Robustness checklist, you can enter a range describing the boundaries in an existing Unit of measure for the variation of the Noise Factor.

To create a range for the Noise Factor

1. Select the cell corresponding to the targeted Noise Factor and the first column Range.
2. Right-click and select Define Range from the Contextual menu. [ATTACHMENT filename='Define Range Command.png']
3. In the Define Range dialog, insert the required Min value, Max value, and define the Unit. [IMAGE alt='' src='']
4. C lick OK.

##### Creating Design Limits for the Activity

To create a Design Limit for the Activity

1. Select the cell corresponding to the targeted Noise Factor and the second column, Design Limits .
2. Right-click and select Design Limits from the Contextual menu. [ATTACHMENT filename='Desgin Limit command.png']
3. In the Define Range dialog, insert the required Min value, Max value, and define the Unit. [ATTACHMENT filename='Define Range dialog_Desgin Limit.png']
4. C lick OK.

##### Defining coverage for Prevention or Detection Controls

Design methods and test methods may cover a fraction of the range of a noise factor or more than the range of the noise factor. The end user can capture the range of the coverage when a prevention control or detection control is associated to a noise factor using a contextual menu item **Define coverage**. A dialog allows capturing a minimal value and a maximal value covered by the control, with the same unit as the covered noise factor. The covered range is persisted in the prevention or detection dependency, allowing controls to be enriched without modifying them directly.

The formula to compute the percentage of coverage follows the following rule: if the full range of the noise factor is not covered, the fraction that is covered is computed and the ratio to the full range of the noise factor is displayed; otherwise, the percentage of coverage is the ratio between the control range and the noise factor range.

To Define Coverage

1. Select the cell corresponding to the targeted controls to be defined.
2. Right-click and select Define Coverage from the Contextual menu. [ATTACHMENT filename='Define Coverage.png']
3. In the Define Range dialog, insert the required Min value and Max value. [ATTACHMENT filename='Define Range dialog_Define coverage.png']
4. Click OK .

- The percentage of coverage is displayed in the Robustness Checklist.
- The relationship between the control and the other element must be established beforehand.

##### Prioritizing the High Impact Failure Mode

To highlight the High Impact Failure mode in the Robustness Checklist.

- Right-click the required Failure Mode and select Toggle High Impact Status from the Contextual menu. [ATTACHMENT filename='Toggle High Impact Status.png']

##### Creating a Relevant To Relationship

A **Relevant** **To**relationship can be created between:

- Noise Factor and Activity Input
- Failure Mode and Activity Output

To create a Relevant To relationship

1. Select the white cell between a Noise Factor and an Input.
2. Right-click and select Create Relevant To from the Contextual menu. [ATTACHMENT filename='Input_Relevant To.png']
3. Select the white cell between a Failure mode and an Output
4. Right-click and select Create Relevant To from the Contextual menu. [ATTACHMENT filename='Output_Relevant To.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the **Red Arrow**.

##### Creating Causality Relationship

A**Causality**relationship can be created between:

- Noise Factor and Failure Cause
- Noise Factor and Failure Mode

To create a Causality relationship

1. Select the white cell between a Noise Factor and a Failure Cause.
2. Right-click and select Create Causality from the Contextual menu. [ATTACHMENT filename='Causality_Failure Cause.png']
3. Select the white cell between a Noise factor and a Failure Mode.
4. Right-click and select Create Causality from the Contextual menu. [ATTACHMENT filename='Causality_Failure Mode.png']

An association is created between the two elements and is visible in the Robustness Checklist with the help of the **Blue Line**.

##### Creating a PreventionRelationship

A **Prevention**relationship can be created between Prevention Control and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Preventionrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Prevention from the Contextual menu. [ATTACHMENT filename='Create Prevention.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the **Green Arrow**.

##### Creating aDetectionRelationship

A**Detection**relationship can be created between Detection Control and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Detectionrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Detection from the Contextual menu. [ATTACHMENT filename='Create Detection.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the **Orange Arrow**.

##### Creating aRecommendation Relationship

A**Recommendation**relationship can be created between the Recommended Action and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Recommendationrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Recommendation from the Contextual menu. [ATTACHMENT filename='Create Recommendation.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the **Purple Arrow**.

##### Creating an FMEA Item

An FMEA Item relationship can be created between a Failure Mode and:

- A Failure Cause
- A Failure Effect

To create an FMEA Item

1. Select the white cell between the targeted elements.
2. Right-click and select Create FMEA Item from the Contextual menu. [ATTACHMENT filename='Create FMEA Item.png']

- A Failure Mode to Failure Effect relationship is created between the two elements and is visible in the Robustness Checklist with the help of the Pink Arrow .
- A Failure Cause to Failure Mode relationship is created between the two elements and is visible in the Robustness Checklist with the help of the Dark Blue Arrow .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);">For a specific function/activity, a Robustness Check List allows verifying that prevention controls (design methods) and detection controls (test methods) are adequate given the impact of failure modes/failure effects to be covered and the range of variation of noise factors that cause these failure modes/failure effects to arise.</span></p><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);">The rows and columns of the Robustness Check List display the noise factors with their associated ranges of variation, the failure causes, the failure modes, the failure effects, the prevention controls, the detection controls, and the recommended actions associated with the function/activity for which the RCL is established. All these elements could come from the function/activity Parameter Diagram, except the failure causes, which are introduced manually in the Robustness Check List.</span></p><p><strong><span style="color:var(--ds-text,#172b4d);">Essential </span>Information:</strong></p><ul><li data-uuid="85458ff3-010b-4be7-9903-1f24cada3f7d">The robustness checklist diagram is created based on an activity object.</li><li data-uuid="42487df7-6c2b-4033-9cfa-1c1ac4e18806">All relationships in the Robustness Checklist can be deleted by right-clicking the cell and selecting the corresponding delete command. It can also be deleted from the model itself by pressing the Delete key on the Keyboard.</li><li data-uuid="8fc13858-2b5f-469c-8f6b-56862bc6da93">The Parameter diagram and the FMEA table also show all existing relationships.</li><li data-uuid="cfc9b423-d988-48d2-b5c8-9359861e0d93">If a Parameter Diagram and/or an FMEA table exist for the activity, you can navigate from the Robustness Checklist with the help of the commands present in the toolbar. The following table displays the icons and functions of the commands:<br /><br /><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th style="text-align: center;">Icon</th><th style="text-align: center;">Description</th></tr><tr><td style="text-align: center;"><div class="content-wrapper" title=""><p><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Open Function in Parameter Diagram.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></p></div></td><td style="text-align: left;">Opens the Function in the Parameter Diagram</td></tr><tr><td style="text-align: center;"><div class="content-wrapper" title=""><p><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Open Function in RAAML based FMEA Table.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></p></div></td><td style="text-align: left;">Opens the Function in the RAAML-based FMEA Table</td></tr></tbody></table></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fda1a168-75a0-45d4-957b-71e2562c2713"><ac:rich-text-body><p>The Robustness Checklist is a <span style="color:var(--ds-text,#172b4d);">Dependency Matrix</span>. To learn more, refer to the <span style="color:var(--ds-text,#172b4d);"><a href="https://docs.nomagic.com/MT/?contextKey=dependency-matrix&amp;version=2026x Refresh1&amp;variant=default">Dependency Matrix</a> </span>page.</p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Robustness Checklist</h3><p>To create a Robustness Checklist </p><hr /><ol><li data-uuid="892fc8f0-795d-47aa-8761-c9ed64f015aa">In the Containment tree, right-click the <strong>Robustness Checklist </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="2d14e84a-b761-4561-9363-6e13079341d3">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Robustness Checklist.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Robustness_Select.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword robust and then select <strong>Robustness Checklist.<br /><br /><ac:image ac:thumbnail="true" ac:height="162"><ri:attachment ri:filename="Robustness_Search.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="a5d0d5d4-6d6e-4687-be18-590ec7fc7a2e">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br />The Robustness Checklist is now displayed in the diagram pane of the modeling tool.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9e61e657-7953-4837-be46-58d6639b3e94"><ac:rich-text-body><p>You must focus on identifying relationships with the aid of the white cells, as the grey cells are not editable.</p></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="Robustness_Checklist.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><h3>Adding an element to the Robustness Checklist</h3><p>To add an element to the Robustness Checklist</p><hr /><ol><li data-uuid="b24ed1a7-9041-4ed0-abad-f84064d823d8">In the containment Tree, select the element to be added.</li><li data-uuid="4d5d38bc-064b-4e55-9a71-7d88a5d4d483">Drag and drop the element on the Column corresponding to the element folder and refresh the diagram.<br /><br /><ac:image><ri:attachment ri:filename="Adding element.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><h3>Deleting elements from the Robustness Checklist</h3><p>To delete elements from the Robustness Checklist</p><hr /><ol><li data-uuid="78dcbe1c-7f26-4777-b6d9-4448133127a7">In the Robustness Checklist, select the element to be deleted.</li><li data-uuid="a271a947-821d-4540-b69c-8775b2863344">Right-click and select <strong>Remove from the Matrix </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Delete Element.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e0866958-7124-453c-a2b8-22dd157bfdf8"><ac:rich-text-body><p>You can completely delete the element by pressing the Delete button on the Keyboard.</p></ac:rich-text-body></ac:structured-macro><h3>Creating a range for the Noise Factor</h3><p>With the Robustness checklist, you can enter a range describing the boundaries in an existing Unit of measure for the variation of the Noise Factor.</p><p>To create a range for the Noise Factor</p><hr /><ol><li data-uuid="a7345d17-5745-42ac-a5b4-c698e107e42b">Select the cell corresponding to the targeted Noise Factor and the first column <strong>Range.</strong></li><li data-uuid="af2a4d11-17a7-488b-8468-003e478eeac2">Right-click and select <strong>Define Range </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Define Range Command.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="d76e50f7-3625-4ad2-b2d8-4dfff84089f6">In the Define Range dialog, insert the required <strong>Min </strong>value, <strong>Max </strong>value, and define the <strong>Unit. </strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></strong></li><li data-uuid="88382b09-135b-470c-bd76-c6b125ed7184">C<span>lick </span><strong>OK.</strong></li></ol><h3>Creating Design Limits for the Activity</h3><p>To c<span>reate a Design Limit for the Activity</span></p><hr /><ol><li data-uuid="8e6c3f42-d08a-486b-8ccc-ce398f82e9dc">Select the cell corresponding to the targeted Noise Factor and the second column, <strong>Design Limits</strong>.</li><li data-uuid="6aa04f5c-a0bf-48c9-a3f7-6ff85c1f5e11">Right-click and select <strong>Design Limits </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Desgin Limit command.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="2018a8e2-9aa8-46f4-b163-76c1047ae1a9">In the Define Range dialog, insert the required <strong>Min </strong>value, <strong>Max </strong>value, and define the <strong>Unit.</strong><br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog_Desgin Limit.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="69d9fe17-d48e-4bae-b8f7-d4ae4b3b2fe3">C<span>lick </span><strong>OK.</strong></li></ol><h3>Defining coverage for Prevention or Detection Controls</h3><p>Design methods and test methods may cover a fraction of the range of a noise factor or more than the range of the noise factor. The end user can capture the range of the coverage when a prevention control or detection control is associated to a noise factor using a contextual menu item <strong>Define coverage</strong>. A dialog allows capturing a minimal value and a maximal value covered by the control, with the same unit as the covered noise factor. The covered range is persisted in the prevention or detection dependency, allowing controls to be enriched without modifying them directly.</p><p>The formula to compute the percentage of coverage follows the following rule: if the full range of the noise factor is not covered, the fraction that is covered is computed and the ratio to the full range of the noise factor is displayed; otherwise, the percentage of coverage is the ratio between the control range and the noise factor range.</p><p><br /></p><p><span>To Define Coverage </span></p><hr /><ol><li data-uuid="94b2061e-2845-4be1-9d0b-bc6b3628f8ea">Select the cell corresponding to the targeted controls to be defined.</li><li data-uuid="c5078f61-d639-4e50-a382-a9f51c3902f8">Right-click and select <strong>Define Coverage </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Define Coverage.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="4e6bca39-338a-4871-baa4-1eff63417e1a">In the Define Range dialog, insert the required <strong>Min </strong>value and  <strong>Max </strong>value. <br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog_Define coverage.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="df3e917e-eba2-4692-9efc-a047d13f6221">Click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0b85f398-5ea0-4100-9f0f-9c9f1e0d91d5"><ac:rich-text-body><ul><li data-uuid="44160890-1b00-403e-b129-ec217ccf9126">The percentage of coverage is displayed in the Robustness Checklist.</li><li data-uuid="2f023968-545f-4cfb-a9c5-15c572ab3eaa"><p>The relationship between the control and the other element must be established beforehand.</p></li></ul></ac:rich-text-body></ac:structured-macro><h3>Prioritizing the High Impact Failure Mode</h3><p><span>To highlight the High Impact Failure mode in the Robustness Checklist.</span></p><hr /><ul><li data-uuid="51947f67-450f-46f0-9bdd-bf64675d28b8">Right-click the required Failure Mode and select <strong>Toggle High Impact Status </strong><span>from the Contextual menu.<br /><br /></span><ac:image><ri:attachment ri:filename="Toggle High Impact Status.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ul><h3>Creating a Relevant To Relationship</h3><p>A <strong>Relevant</strong> <strong>To </strong>relationship can be created between:</p><ul><li data-uuid="7088c7a2-6d65-42fb-95fb-87865ddf45ed">Noise Factor and Activity Input</li><li data-uuid="88479b76-7825-4ee2-b179-abb45ae3dede">Failure Mode and Activity Output</li></ul><p>To create a Relevant To relationship</p><hr /><ol><li data-uuid="acaf710c-bc6a-4493-ace4-ed9e3065b175">Select the white cell between a Noise Factor and an Input.</li><li data-uuid="6fffbf05-1bc0-4987-bad5-0b97f0c45ffe">Right-click and select <strong>Create Relevant To </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Input_Relevant To.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="26ee81af-800f-4a33-a37c-82f58b95b9d1">Select the white cell between a Failure mode and an Output</li><li data-uuid="36545424-4fd4-414b-a652-4ccedfe8cb5e">Right-click and select <strong>Create Relevant To </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Output_Relevant To.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c12d578d-3a4e-4b48-873b-487cd765b396"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Red Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3>Creating Causality Relationship</h3><p>A<strong> Causality </strong>relationship can be created between:</p><ul><li data-uuid="e96040a3-1f79-4d09-95b3-aaa93ff95885">Noise Factor and Failure Cause</li><li data-uuid="ba3aa7a4-de82-43be-ad6d-a0ef7e745f56">Noise Factor and Failure Mode</li></ul><p><br /></p><p>To create a Causality relationship</p><hr /><ol><li data-uuid="9d70cda2-5608-4f6c-9ff8-86a3086d1d62">Select the white cell between a Noise Factor and a Failure Cause.</li><li data-uuid="570bb26f-96e0-4925-8f6e-b95f8328eacd">Right-click and select <strong>Create Causality </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Failure Cause.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image><br /><br /></li><li data-uuid="837f85a6-a7a8-47bd-ab07-38e0e20e526a">Select the white cell between a Noise factor and a Failure Mode.</li><li data-uuid="ec28be0e-5ec8-4edf-9d7a-ccb1326ee5fb">Right-click and select <strong>Create Causality </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Failure Mode.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="04342581-82fe-45e1-93f5-f2ee6ca5bdd2"><ac:rich-text-body><p><span>An association is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Blue Line</strong>.</span></p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a Prevention </span><span>Relationship</span></h3><p>A <strong>Prevention </strong>relationship can be created between Prevention Control and :</p><ul><li data-uuid="fc3464a9-b0f4-4528-a26d-8b363d3c5b3b">Noise factor</li><li data-uuid="1f4742e4-3352-41ba-9bf7-759b706a82b8">Failure Cause</li><li data-uuid="4019f463-3fc2-4b5e-b988-985284e662f8">Failure Mode</li><li data-uuid="938cd914-1ff3-4d86-b66f-0f82bec5e105">Failure Effect</li></ul><p>To create a <span>Prevention </span><span>relationship</span></p><hr /><ol><li data-uuid="aa197250-4208-4548-885d-32e5b59c900e">Select the white cell between the targeted elements.</li><li data-uuid="d1460d36-5cf6-4e48-a3d0-40bab0655431">Right-click and select <strong>Create Prevention </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Prevention.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5b9acbc9-09cf-4d30-a5db-1a4eed2e812c"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the <strong>Green Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a </span><span>Detection </span><span>Relationship</span></h3><p>A<strong> Detection </strong>relationship can be created between Detection Control and :</p><ul><li data-uuid="a01fb4b2-5267-4860-844e-095b9594d99b">Noise factor</li><li data-uuid="fc85d6d1-a86b-43aa-a233-7bed8ee0950a">Failure Cause</li><li data-uuid="19dc5177-6ca4-42b8-b59f-c05bdc653315">Failure Mode</li><li data-uuid="170e1b9b-e092-476e-ae39-dbfa2425aed5">Failure Effect</li></ul><p>To create a <span>Detection </span><span>relationship</span></p><hr /><ol><li data-uuid="4bab0dfe-a834-4b8a-a0a0-70ea004663e4">Select the white cell between the targeted elements.</li><li data-uuid="455d3108-8fe8-441c-8072-4460825af268">Right-click and select <strong>Create Detection </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Detection.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="aec35c91-e3e9-4d79-8a1f-32e8c5f2fcdb"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the <strong>Orange Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a </span><span>Recommendation Relationship</span></h3><p>A<strong> Recommendation </strong>relationship can be created between the Recommended Action and  :</p><ul><li data-uuid="d2b237bb-99f1-400e-9190-078b5a7bd929">Noise factor</li><li data-uuid="c29234a1-738d-4e5d-8520-ff02b0f3b9ba">Failure Cause</li><li data-uuid="0beb4d1a-1aea-4500-974a-10f8cdb702b5">Failure Mode</li><li data-uuid="6fdc28ff-b107-4a67-92f1-071579334eda">Failure Effect</li></ul><p>To create a <span>Recommendation </span><span>relationship</span></p><hr /><ol><li data-uuid="d285265c-5cfb-45fb-955d-b70eab5d1b08">Select the white cell between the targeted elements.</li><li data-uuid="bcafb79a-26c9-4a86-ac6c-60eb14dd71e4">Right-click and select <strong>Create <span>Recommendation </span></strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Recommendation.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b2e31893-834d-46da-a2e0-32284880626a"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the <strong>Purple Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3>Creating an FMEA Item</h3><p>An FMEA Item relationship can be created between a Failure Mode and:</p><ul><li data-uuid="116085d4-cf32-42f8-bedd-873c262d2c71">A Failure Cause</li><li data-uuid="86b6acd3-136d-44bb-a2cb-6152ecd1d999">A Failure Effect</li></ul><p>To create an FMEA Item</p><hr /><ol><li data-uuid="5b34a555-7d9d-453f-9a94-a0a5d2e3d704">Select the white cell between the targeted elements.</li><li data-uuid="44cc3523-496c-4cc5-b3ce-cc28639f9b8f">Right-click and select <strong>Create <span>FMEA Item </span></strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create FMEA Item.png"><ri:page ri:content-title="(2026x Refresh1) Robustness Checklist" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4e59ec84-97a2-4020-b0c1-92413d6d808c"><ac:rich-text-body><ul><li data-uuid="2907a060-fdd1-48ca-8417-ac98f2ee1ca4">A Failure Mode to Failure Effect relationship is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Pink Arrow</strong>.</li><li data-uuid="5232dc13-6830-4e21-8367-333242da8858">A Failure Cause to Failure Mode relationship is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Dark Blue Arrow</strong>.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=304009460 space=SSE version=1 -->
## PAGE 00009: (2026x Refresh1) Systems Safety Engineer

- page_id: `304009460`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009460/2026x+Refresh1+Systems+Safety+Engineer
- version_number: 1
- version_date: `2026-04-29T15:31:50.386+02:00`
- ancestors: Versions of Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

#### WARNING: Technology Preview

Technology Preview

This is the **technology preview** version. We **do not** recommend using it to create any long-term projects because it may change without notice. The migration to the latest version will not be possible.

Quality and Safety disciplines are critical to ensure**reliable**and**safe**systems.

Based on the system architecture, the Systems Safety Engineer plugin enables:

- The creation of the Boundary Diagram and **Item** to finalize the scope (the relevant parts of the system to be analyzed).
- The creation of an item-based Interface Analysis table to study connections between functions.
- The creation of a Parameter Diagram to identify the measurable parameters that could affect the intended output of a given function.
- The creation of a Robustness Checklist to identify causality links between elements of a given function.
- The creation of a Failure Mode and Effects Analysis table

Systems Safety Engineer is**RAAML-based**and partiallysupports **SAE J1739.**

**[IMAGE alt='' src='']**

###### Systems Safety Engineer workflow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1ce8104b-f556-4ea4-b382-01746572a2e6"><ac:parameter ac:name="title">Technology Preview</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">This is the <strong>technology preview</strong> version. We <u><strong>do not</strong></u> recommend using it to create any long-term projects because it may change without notice. The migration to the latest version will not be possible. </span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p style="text-align: left;">Quality and Safety discipline<ac:inline-comment-marker ac:ref="37466a70-af18-4867-94b1-fb68120a27ce">s are critical</ac:inline-comment-marker> to ensure<span> </span><strong>reliable</strong><span> </span>and<span> </span><strong>safe</strong><span> </span>systems.</p><p style="text-align: left;">Based on the system architecture, the Systems Safety Engineer plugin enables: </p><ul style="text-align: left;"><li data-uuid="3f540db5-e389-4a4b-8523-cdc36585110f">The creation of the <strong>Boundary Diagram</strong><span> </span>and<span> <strong>Item </strong></span>to finalize the scope (the relevant parts of the system to be analyzed).</li><li data-uuid="80725f4b-abb9-4e63-946d-6db68b3bee78">The creation of an item-based<span> </span><strong>Interface Analysis</strong><span> </span>table to study connections between functions.</li><li data-uuid="e5730bf5-a485-4dbd-bb43-07aaca877242">The creation of a<span> </span><strong>Parameter Diagram</strong><span> </span>to identify the measurable parameters that could affect the intended output of a given function.</li><li data-uuid="d91ec259-dcf9-47cd-b160-9373cac38c8c">The creation of a<span> </span><strong>Robustness Checklist</strong><span> </span>to identify causality links between elements of a given function.</li><li data-uuid="d39015c0-af0f-4b64-8254-537060761b99">The creation of a<span> </span><strong>Failure Mode and Effects Analysis</strong><span> </span>table </li></ul><p style="text-align: left;">Systems Safety Engineer is<span> </span><strong>RAAML-based</strong><span> </span>and partially<span> </span>supports <strong>SAE J1739.</strong></p><p style="text-align: center;"><strong><ac:image ac:border="true" ac:height="646" ac:width="983"><ri:attachment ri:filename="SSE_Workflow.png"><ri:page ri:content-title="(2026x Refresh1) Systems Safety Engineer" /></ri:attachment></ac:image></strong></p><h6 style="text-align: center;">Systems Safety Engineer workflow</h6>
````

<!--NOMAGIC_PAGE id=304009467 space=SSE version=1 -->
## PAGE 00010: (2026x Refresh1) Systems Safety Engineer Project

- page_id: `304009467`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/304009467/2026x+Refresh1+Systems+Safety+Engineer+Project
- version_number: 1
- version_date: `2026-04-29T15:31:50.470+02:00`
- ancestors: Versions of Systems Safety Engineer > (2026x Refresh1) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

**On this page**

**3**

##### Creating a Failure Mode Avoidance project

To create a new Failure Mode Avoidance project

1. Do one of the following:
  - From the File menu, select New Project from the drop-down list. [IMAGE alt='' src='']
  - Click Create New Project on the welcome screen. [ATTACHMENT filename='Create New Project_Command.png']
  - Press Ctrl + Shift + N.
2. In the New Project dialog, select the **Failure Mode Avoidance Project.** 
[IMAGE alt='' src='']
3. Specify the file name in the Name box.
4. Click the[IMAGE alt='' src='']button to select the location to store the project in a folder.
5. Select the checkbox to automatically create a folder for the project in the specified location.
6. Click **OK**.

A new FMA project is displayed with the default packages in the Containment tree and the Index.

If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling tool.

##### FMA Project Template

A default FMA project template is displayed once you open the project. This template is provided to help you initiate the process.

**Containment Tree**

The Containment tree displays the default packages in the Containment tree. You can add, modify or delete any element or package from the Containment tree.

**Index**

The Index displays the default information related to FMA.

If you press the CTRL key and double-click any table's icon, the table opens in a new tab.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong> On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="46c4561c-0f22-492b-8293-80bfb1550691"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Failure Mode Avoidance project</h3><p>To create a new Failure Mode Avoidance project</p><hr /><ol><li data-uuid="c9663650-be20-4101-a6f2-9e1cc79268c0">Do one of the following:<ul><li class="atl-forced-newline">From the<span> </span><strong>File</strong><span> </span>menu, select <strong>New Project </strong>from the drop-down list.<br /><em><br /><ac:image><ri:attachment ri:filename="New Project_command.jpg"><ri:page ri:content-title="(2026x Refresh1) Systems Safety Engineer Project" /></ri:attachment></ac:image><br /><br /></em></li><li>Click <strong>Create New Project </strong>on the welcome screen.<br /><br /><ac:image><ri:attachment ri:filename="Create New Project_Command.png"><ri:page ri:content-title="(2026x Refresh1) Systems Safety Engineer Project" /></ri:attachment></ac:image><br /><br /></li><li>Press Ctrl + Shift + N.</li></ul></li><li data-uuid="4310d984-d576-48e0-8043-17f8f317b18e"><p class="auto-cursor-target">In the New Project dialog, select the <strong>Failure Mode Avoidance Project.<br /></strong><br /><ac:image><ri:attachment ri:filename="Create new project.png"><ri:page ri:content-title="(2026x Refresh1) Systems Safety Engineer Project" /></ri:attachment></ac:image><br /><br /></p></li><li data-uuid="d890174a-ac09-481f-87f7-9b950bd6b214"><p class="auto-cursor-target">Specify the file name in the Name box.</p></li><li data-uuid="e39405d4-db37-4b91-be61-253584a3ad9e"><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Click the</span><span style="color:var(--ds-text,#333333);"><span> <ac:image><ri:attachment ri:filename="Three Dot Icon.png"><ri:page ri:content-title="(2026x Refresh1) Systems Safety Engineer Project" /></ri:attachment></ac:image> </span>button to select the location to store the project in a folder.</span></p></li><li data-uuid="a19816a0-a524-478e-b6c8-2f26f808363e"><p class="auto-cursor-target">Select the checkbox to automatically create a folder for the project in the specified location.</p></li><li data-uuid="d62ba4ba-6a2c-433f-b1ae-205655313535"><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li></ol><p>A new FMA project is displayed with the default packages in the Containment tree and the Index.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="df13aefb-d300-4916-8e58-5927a3285c35"><ac:rich-text-body><p>If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling tool.</p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">FMA Project Template</h3><p>A default FMA project template is displayed once you open the project. This template is provided to help you initiate the process.</p><p><strong>Containment Tree</strong></p><p>The Containment tree displays the default packages in the Containment tree. You can add, modify or delete any element or package from the Containment tree.</p><p><strong>Index</strong></p><p>The Index displays the default information related to FMA. </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="99614ef4-6697-44ce-a28f-8369f17b828d"><ac:rich-text-body><p>If you press the CTRL key and double-click any table's icon, the table opens in a new tab.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="FMEA Template.png"><ri:page ri:content-title="(2026x Refresh1) Systems Safety Engineer Project" /></ri:attachment></ac:image></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254421577 space=SSE version=10 -->
## PAGE 00011: (2026x) Boundary Diagram

- page_id: `254421577`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421577/2026x+Boundary+Diagram
- version_number: 10
- version_date: `2025-11-18T10:44:20.835+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer > (2026x) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

Boundary diagram and Boundary diagram item aid in identifying and capturing in exhaustive detail about :

- The Internal sub-systems and components, and external “actors”/entities
- The different scopes of analysis by visually outlining the system boundary.
- The interactions with legends
- Missing interactions.

##### Creating a Boundary Diagram

To create a Boundary Diagram

1. In the Containment tree, right-click the Boundary Diagram package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Boundary Diagram****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword boundary and then select Boundary Diagram . 
 
[IMAGE alt='' src='']

The Boundary Diagram is now displayed in the diagram pane and in the Containment tree of the modeling tool. 
 
[IMAGE alt='' src='']

##### Adding an Internal Block Diagram of a Use Project

To add an Internal Block Diagram of a Use Project

1. Add the required local project to your project. To learn more, refer to the Using local projects page.
2. Drag and drop the required block from the Containment tree to the Boundary Diagram. [ATTACHMENT filename='Block drag and drop.png']
3. Right-click the block and select Display>Display Internal Structure>Lamp in context>Lamp in context. 
 
[IMAGE alt='' src='']

The internal structure of the Lamp block is displayed in the diagram pane.

##### Creating a Boundary Diagram Item

To create a Boundary Diagram Item

1. Drag and drop the Boundary Diagram Item element in the diagram pane. [ATTACHMENT filename='Boundary diagram_Item.png']
2. In the Contain ment tre e, select the newly created Boundary Diagram Item and rename it with the help of the Specification dialog. 
 
[IMAGE alt='' src='']

##### Drawing an Anchor

To draw an Anchor

- Draw an anchor from the newly created Item Scope to the elements of interest. To learn more about drawing and configuring an Anchor, refer to the Anchor page. [ATTACHMENT filename='Scope Done.png']

##### Creating a Signal Category

To create a Signal Category

1. Create a SysML Block Definition Diagram in the Boundary Diagram package. To learn more about creating a diagram, click here .
2. Drag and drop the signals from the Lamp>Signals package in the diagram pane. [ATTACHMENT filename='Signal drag and drop.png']
3. Drag and drop the EnergyTransfer , InformationTransfer , InteractionClass , MaterialExchange, and PhysicalConnection elements from the FMA Library package in the diagram pane. [ATTACHMENT filename='FMA drag and drop.png']
4. Rearrange the elements and create Dependencies as per your requirements. To learn more about creating Dependency, refer to the Dependency page. [ATTACHMENT filename='Dependency created.png']
5. Select and apply the TransferType[Dependency] stereotype to all the dependencies. To learn more about applying stereotype, refer to the [CONFLUENCE_PAGE title='Stereotype' space='MED'] page.
6. On the diagram toolbar, click the [IMAGE alt='' src=''] button to change the diagram layout. To learn more about changing diagram layout, refer to the[https://docs.nomagic.com/spaces/MT/pages/9917874/Layout](https://docs.nomagic.com/spaces/MT/pages/9917874/Layout)[Layout](https://docs.nomagic.com/MT/?contextKey=layout&version=2026x&variant=default)page. 
 
[IMAGE alt='' src='']

##### Working with Legends

A Legend is a model element that allows you to define the styles of diagram symbols and table rows. It helps you to visually group model elements according to specified criteria. A Legend increases the readability of the diagram and table contents by highlighting important information. To learn more, refer to the [Legends](https://docs.nomagic.com/MT/?contextKey=legends&version=2026x&variant=default)page.

###### Applying a Legend

To apply a Legend

1. In the diagram toolbar. Click [IMAGE alt='' src=''] and from the drop-down menu, select Apply Legends .
2. Select the Legend(s) you want to display and click OK. [IMAGE alt='' src='']

To learn more, refer to the [Applying Legends](https://docs.nomagic.com/MT/?contextKey=applying-legends&version=2026x&variant=default)page.

###### Extracting a Legend

To extract a Legend

1. In the diagram toolbar. Click [IMAGE alt='' src=''] and from the drop-down menu, select Extract Legends .
2. Select the Legend(s) you want to display and click Extract. [IMAGE alt='' src='']

To learn more, refer to the [Extracting Legends](https://docs.nomagic.com/MT/?contextKey=creating-legends-automatically&version=2026x&variant=default)page.

###### Specifying Legend Item adornment

To open the adornment properties of a Legend Item

1. Open the Specification window of the Legend Item **Lamp Scope** in the **Boundary Diagram Item**. 
 
[IMAGE alt='' src='']
2. Click the specification cell of the Adornment property, and then click [IMAGE alt='' src=''] .
3. In the Adornment Properties dialog, specify the Fill Color property and click OK . [IMAGE alt='' src='']

To learn more, refer to the[Specifying Legend Item adornment](https://docs.nomagic.com/MT/?contextKey=specifying-legend-item-adornment&version=2026x&variant=default).

After completing the above procedures, the Boundary Diagram is updated in the following manner.

[IMAGE alt='' src='']

###### Boundary Diagram after applying, extracting, and specifying the Legends.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p style="text-align: left;">Boundary diagram and Boundary diagram item aid in identifying and capturing in exhaustive detail about :</p><ul><li data-uuid="3085777f-da5f-4dc1-973d-903ca3366cad">The Internal sub-systems and components, and external “actors”/entities</li><li data-uuid="ba0845e6-48b0-4474-bee3-7702eda1491c">The different scopes of analysis by visually outlining the system boundary.</li><li data-uuid="95efaa3d-3768-43ce-a8fd-1ea37fcddecb">The interactions with legends</li><li data-uuid="3d6286df-2e79-4ed8-8dae-bfa3b5204e5a">Missing interactions.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Boundary Diagram</h3><p>To create a Boundary Diagram </p><hr /><ol><li data-uuid="3547a66c-39c0-46e9-bdad-2077594db1f6">In the Containment tree, right-click the <strong>Boundary Diagram </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="513d755e-9e19-44b9-b639-94da05d12a34">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Boundary Diagram</strong><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword boundary and then select <strong>Boundary Diagram</strong><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram Search.png" /></ac:image><br /><br /></strong></li></ul></li></ol><p>The Boundary Diagram is now displayed in the diagram pane and in the Containment tree of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram created.png" /></ac:image></p><h3>Adding an Internal Block Diagram of a Use Project</h3><p>To add an Internal Block Diagram of a Use Project</p><hr /><ol><li data-uuid="5c7ee77a-dc84-492b-8540-ff3132c1c2f3">Add the required local project to your project. To learn more, refer to the <a href="https://docs.nomagic.com/SYSML2P/http://?contextKey=using-local-projects&amp;version=2026x">Using local projects</a> page.</li><li data-uuid="3ddaa88e-0e0c-4a03-b3ae-616fa2d2ab63">Drag and drop the required block from the Containment tree to the Boundary Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Block drag and drop.png" /></ac:image><br /><br /></li><li data-uuid="9e0fa85a-16ad-48d6-9ea6-f49e499b79a7">Right-click the block and select <strong>Display&gt;Display Internal Structure&gt;Lamp in context&gt;Lamp in context.<br /><br /><ac:image><ri:attachment ri:filename="Lamp in contect command.png" /></ac:image><br /></strong></li></ol><p>The internal structure of the Lamp block is displayed in the diagram pane.</p><h3>Creating a Boundary Diagram Item </h3><p>To create a Boundary Diagram Item</p><hr /><ol><li data-uuid="03543445-37ff-4e90-a59b-624a09c6e688">Drag and drop the <strong>Boundary Diagram Item </strong>element in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram_Item.png" /></ac:image><br /><br /></li><li data-uuid="a3d74fef-0943-412f-ada3-170db6845425">In the Contain<ac:inline-comment-marker ac:ref="950adda0-c6ed-423c-bc12-e16093ed44a4">ment tre</ac:inline-comment-marker>e, select the newly created<ac:inline-comment-marker ac:ref="84c7744b-378c-4b37-8276-9c0a2333c911"> Boundary Diagram Item and rename it with the help of the Specification dialog.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram_Item_Containment tree.png" /></ac:image><br /></ac:inline-comment-marker></li></ol><h3>Drawing an Anchor</h3><p>To draw an Anchor</p><hr /><ul><li data-uuid="6b602302-2aba-4775-aa51-2b8e5ed387b3">Draw an anchor from the newly created Item Scope to the elements of interest. To learn more about drawing and configuring an Anchor, refer to the<a href="https://docs.nomagic.com/MT/?contextKey=anchor&amp;version=2026x&amp;variant=default"> Anchor </a>page.<br /><br /><ac:image><ri:attachment ri:filename="Scope Done.png" /></ac:image></li></ul><h3>Creating a Signal Category</h3><p>To create a Signal Category</p><hr /><ol><li data-uuid="d01f0ebe-5479-4e13-a0ea-21f8475aada5">Create a <strong>SysML Block Definition Diagram</strong> in the Boundary Diagram package. To learn more about creating a diagram, click <a href="https://docs.nomagic.com/MT/?contextKey=creating-diagrams&amp;version=2026x&amp;variant=default">here</a>.</li><li data-uuid="85620cc4-4cb3-4143-956c-3fa912f3d77f">Drag and drop the signals from the <strong>Lamp&gt;Signals</strong> package in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Signal drag and drop.png" /></ac:image><br /><br /></li><li data-uuid="386c649c-dfaf-4106-9531-c656666cc711">Drag and drop the <strong>EnergyTransfer</strong>, <strong>InformationTransfer</strong>, <strong>InteractionClass</strong>, <strong>MaterialExchange, </strong>and <strong>PhysicalConnection </strong>elements from the <strong>FMA Library </strong>package in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="FMA drag and drop.png" /></ac:image><br /><br /></li><li data-uuid="d4559a7b-cd10-4e75-9040-5febdc01e6d1">Rearrange the elements and create Dependencies as per your requirements. To learn more about creating Dependency, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=dependency&amp;version=2026x&amp;variant=default">Dependency</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Dependency created.png" /></ac:image><br /><br /></li><li data-uuid="95a5f2e2-dad5-431f-8e43-3f43240476fd">Select and apply the <strong>TransferType[Dependency]</strong> stereotype to all the dependencies. To learn more about applying stereotype, refer to the <ac:link><ri:page ri:space-key="MED" ri:content-title="Stereotype" /></ac:link> page.</li><li data-uuid="64c05ca9-2220-47d6-ac21-419c89fb73df"><span style="color:var(--ds-text,#172b4d);">On the diagram toolbar, click the<span> </span></span><span class="confluence-embedded-file-wrapper" style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="quick_diagram_layout.gif" /></ac:image> button to change the</span><span style="color:var(--ds-text,#172b4d);"> diagram layout. To learn more about changing diagram layout, refer to the<a href="https://docs.nomagic.com/spaces/MT/pages/9917874/Layout"> </a><a href="https://docs.nomagic.com/MT/?contextKey=layout&amp;version=2026x&amp;variant=default"> Layout </a>page.<br /><br /><ac:image><ri:attachment ri:filename="diagram layout.png" /></ac:image><br /></span></li></ol><h3>Working with Legends</h3><p><span style="color:var(--ds-text,#172b4d);">A Legend is a model element that allows you to define the styles of diagram symbols and table rows. It helps you to visually group model elements according to specified criteria. A Legend increases the readability of the diagram and table contents by highlighting important information. To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=legends&amp;version=2026x&amp;variant=default"> Legends </a>page.</span></p><h4>Applying a Legend</h4><p>To a<ac:inline-comment-marker ac:ref="3354d760-dae3-4493-98ee-1ff93685756d">pply a Legend</ac:inline-comment-marker></p><hr /><ol><li data-uuid="cc70408d-3f1b-4049-b60f-12cffbc05a60">In the diagram toolbar. Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="legend_button.png" /></ac:image></span> and from the drop-down menu, select<span style="letter-spacing: 0.0px;"> </span><strong style="letter-spacing: 0.0px;">Apply Legends</strong><span style="letter-spacing: 0.0px;">.</span></li><li data-uuid="a76fcb8a-13df-4027-8f47-5add73b860ed">Select the Legend(s) you want to display and click <strong style="letter-spacing: 0.0px;">OK.</strong><span style="letter-spacing: 0.0px;"><br /><br /><ac:image><ri:attachment ri:filename="Applying Legends.png" /></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="954827ba-719b-478c-ad4a-664b0d88fed7"><ac:rich-text-body><p>To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=applying-legends&amp;version=2026x&amp;variant=default">Applying Legends </a><span>page.</span></p></ac:rich-text-body></ac:structured-macro><h4>Extracting a Legend</h4><p>To extract a Legend</p><hr /><ol><li data-uuid="bd201c0f-6f9d-465f-8f12-ad86bce41f96">In the diagram toolbar. Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="legend_button.png" /></ac:image></span> and from the drop-down menu, select<span> </span><strong>Extract Legends</strong><span>.</span></li><li data-uuid="1072c44f-cb71-4638-bdb4-373ab53adc91">Select the Legend(s) you want to display and click <strong>Extract.</strong><span><br /><br /><ac:image><ri:attachment ri:filename="Extracting Legends.png" /></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="529793d6-0c70-4c46-bd52-c484471006d9"><ac:rich-text-body><p>To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=creating-legends-automatically&amp;version=2026x&amp;variant=default">Extracting Legends </a><span>page.</span></p></ac:rich-text-body></ac:structured-macro><h4>Specifying Legend Item adornment</h4><p style="text-align: left;">To open the adornment properties of a Legend Item</p><hr style="text-align: left;" /><ol style="text-align: left;"><li data-uuid="6fc9f089-631d-45c2-b223-bba4949aecc6"><p>Open the Specification window of the Legend Item <strong>Lamp Scope</strong> in the <strong>Boundary Diagram Item</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Adornment_Specification.png" /></ac:image><br /><br /></p></li><li data-uuid="b0c0b73c-66ca-44d5-ad9a-834c7d91c601">Click the specification cell of the <strong>Adornment</strong> property, and then click <span class="confluence-embedded-file-wrapper"><ac:image><ri:attachment ri:filename="edit.png" /></ac:image></span>.</li><li data-uuid="4fa49fa7-3b6a-4898-aec3-d0f9039142f8">In the Adornment Properties dialog, specify the <strong style="letter-spacing: 0.0px;">Fill Color </strong><span style="letter-spacing: 0.0px;">property and click </span><strong style="letter-spacing: 0.0px;">OK</strong><span style="letter-spacing: 0.0px;">.<br /></span><span style="letter-spacing: 0.0px;"><br /><ac:image><ri:attachment ri:filename="Adornment Properties.png" /></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4e013f77-4514-4d5b-b058-986b643945b3"><ac:rich-text-body><p><span> To learn more, refer to the </span><a href="https://docs.nomagic.com/MT/?contextKey=specifying-legend-item-adornment&amp;version=2026x&amp;variant=default">Specifying Legend Item adornment</a>.<span><br /></span></p></ac:rich-text-body></ac:structured-macro><p><span style="letter-spacing: 0.0px;">After completing the above procedures, the Boundary Diagram is updated in the following manner.<br /><br /></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Scope and Legend created.png" /></ac:image></p><h6 style="text-align: center;">Boundary Diagram after applying, extracting, and specifying the Legends.</h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254421691 space=SSE version=7 -->
## PAGE 00012: (2026x) Failure Mode & Effect Analysis

- page_id: `254421691`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421691/2026x+Failure+Mode+Effect+Analysis
- version_number: 7
- version_date: `2025-11-18T10:44:24.002+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer > (2026x) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

An FMEA Table allows you to analyze the reliability aspect of your model and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. The RAAML-based FMEA Table diagram is derived from an activity object and represents each FMEA Item—defined as the unique pairing of a failure mode with its corresponding cause—through a dedicated row associated with the activity.

In an FMEA Table, you can:

- Create a new FMEA Item directly in a table or add an existing one.
- Directly edit the properties of FMEA Items in a table.

The following table describes each column name, its purpose, and relevant details:

| Column Name | Description |
| --- | --- |
| Name | Displays an auto-generated counter for the FMEA item (this prefix counter is a preset customization) and a name. If the name is generated automatically (e.g., from the creation of an FMEA Item in the Robustness Checklist), it is composed of the Failure Cause and its associated Failure Mode. |
| Inputs | List of input pins of the activity element selected as the Scope of the FMEA study. This is a non-editable field. |
| Function | Activity selected as the scope of the FMEA study. This is a non-editable field. |
| Output | Lists one or more of the output pins that are declared on the activity element selected as the Scope of the FMEA study and that are being affected by a dedicated failure mode. Your selection is limited to the declared output pins on the activity referenced on the Function cell. |
| Failure Mode | Specifies the Failure Mode specific to the FMEA Item Line. Failure Mode definition is as introduced in the Parameter Diagram section, referring to the description of the specific manner in which a component, subsystem, or system could potentially fail to meet the design intent. |
| Classification | Corresponds to the categorization of FMEA items, derived from the evaluation of Severity and Occurrence values using a customizable function (preset out-of-the-box as: CC in case severity >= 9, SC in case 9 > severity >= 7, and AC in case 7 > severity >= 5). |
| Final Effect | Describes the effect of a Failure Mode on the end user or the environment (i.e., at the system-of-interest level). Multiple Final Effects can be specified for a single FMEA item. Each Final Effect can have a default Severity value assigned as its property. To assign a Severity value, open the Specification window of the Final Effect and set the desired value. |
| Computed Effect | An element describing the effect that a Failure Mode has on the system element under consideration. An FMEA Item (e.g., a single row of an FMEA Table) can have multiple Local Effects of Failure. If the element under consideration is a subsystem directly underneath the system of interest level itself, the effect of the Failure Mode is the same as the Final Effect mentioned above in this table. |
| Severity | The Severity of effects is a rating number associated with the most serious effect for a given failure mode for the operation being evaluated. It is a relative rating within the scope of the individual FMEA item and is determined without regard for occurrence or detection. Valid values range from 1 to 10 (lowest to highest severity). |
| Cause | An element (either a lower-level Failure Mode or a dedicated Cause element) indicating the design weakness that leads to a Failure Mode. An FMEA item (e.g., a single row of an FMEA table) can have one Cause of Failure. A Cause can have default Occurrence and Detectability values assigned as properties. To assign these values, either open the Specification window of the Cause and set the desired Occurrence or Detectability, or edit them directly in the corresponding columns of the FMEA table. |
| Prevention Controls | A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode. You can specify multiple Prevention controls for a single FMEA Item. The type of object that can be elected as a Prevention Control is by default preset as a Requirement. The type can be customized. |
| Occurrence | A rating number is associated with each cause for a given failure mode being evaluated. The occurrence rating considers the likelihood of occurrence during production. Valid values range from 1 to 10 (lowest to highest probability). A Cause must be identified in the dedicated cell before setting this value. Enter the value directly in the corresponding FMEA table cell or set it on the Failure Mode or Cause object via the containment tree. |
| Criticality | The product of Severity and Occurrence ratings. |
| Detection Controls | An element describing the measures implemented to detect a Failure Mode. Multiple Detection Control entries can be specified for a single FMEA item. The type of object that can be elected as a Detection Control is by default preset as a Block. The type can be customized. |
| Detection | Detection is the rating associated with the likelihood of detecting the failure mode and/or associated cause, according to defined criteria. Ability to detect is the rating number associated with the combined capabilities of all the current process controls for a given cause and/or failure mode. You should not automatically presume the detection rating is low because the occurrence rating is low. Instead, the User assumes the failure has occurred, then assesses the capabilities of all the detection-type design controls to detect low-frequency failure modes and/or causes. The detection rating is identified without regard for severity or occurrence. Valid Values range from 1 to 10 (highest to lowest detectability). |
| Risk Priority Number | The risk priority number (RPN) is the product of the severity (S), occurrence (O), and detection (D) ratings. Within the scope of the individual FMEA, this value is between “1” and “1000”. A benefit of RPN is that it provides an indicator of improvement (before and after actions taken) that reduces any one factor of severity, occurrence, or detection. It shows the distribution of RPN values for a project (Pareto), giving a high-level overview of the risk assessment. You should be aware that the final RPN ratings are subjective and relative to a particular analysis. |
| Action Priority | Assessment of the internal priority affecting the recommended actions, as per the SAEJ 1739 rating scale. |
| Recommended Action | The description of an action intended to reduce the Risk Priority Number. All critical or significant FMEA items should have associated recommended actions. These actions should focus on design improvements and be directed at mitigating the Cause of Failure or eliminating the Failure Mode. The type of object that can be elected as a Recommended Action element creation is by default preset as a Block. The type can be customized. |
| Action Taken | A property describing what actions have been taken and the results of these actions (free text capture). |
| Responsible Person | Indicates the person responsible for completing a Recommended Action. No specific object type is being preset to represent a Person. |
| Target Date | A property defining the targeted completion date of a Recommended Action. |
| Completion Date | A property assessing the completion date of a Recommended Action. |
| Revised Severity | A property assessing the seriousness of the effect(s) of a potential Failure Mode on a component, subsystem, end user, or environment after mitigation. Valid values range from 1 to 10 (lowest to highest severity). A prerequisite is that an action has been taken |
| Revised Occurrence | A property indicating the likelihood that a specific Cause of Failure will occur after mitigation. Valid values range from 1 to 10 (lowest to highest probability of occurrence). |
| Revised Criticality | The product of Revised Severity and Revised Occurrence ratings. |
| Revised Detection | A property measuring the likelihood of detecting a potential failure after mitigation. Valid values range from 1 to 10 (highest to lowest detectability). |
| Revised Risk Priority Number | The product of Revised Criticality by Revised Detection. |
| Revised Action Priority | Assessment of the internal priority affected by the recommended actions after mitigation. |

#### TIP: Tips

Tips

- While selecting an FMEA Item element (line in the table):
  - You can remove the line from the table using the dedicated Remove From Table command.
  - You can delete it from the containment tree (and the table) using the dedicated Delete command.
- If a Robustness Check List (RCL) and/or Parameter Diagram exists for the activity, the user can navigate from the FMEA Table to one of those diagrams through a dedicated panel above the diagram. To learn more, refer to the [CONFLUENCE_PAGE title='(2026x) Robustness Checklist' space=''] page.

##### Creating a Failure Mode and Effect Analysis (FMEA) Table

To create a Failure Mode and Effect Analysis (FMEA) Table

1. In the Containment tree, right-click the FMEA package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Safety and Reliability Analysis**and select **RAAML-based FMEA Table.** [IMAGE alt='' src='']
  - In the search tab, type the keyword FMEA and then select RAAML-based FMEA Table. 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity dialog_FMEA.png'] The FMEA Table is now displayed in the diagram pane of the modeling tool.

##### Adding an FMEA Item to the FMEA Table

Each Failure mode linked to a Failure Effect (end user effect of a Failure Mode) or to a Failure Cause (element indicating a Design Weakness resulting in a Failure Mode) should result in a new FMEA Item. Generating FMEA Items from the design elements of your model identified earlier in the Robustness Check list diagram saves time and helps avoid mistakes.

You can add existing FMEA Items to an FMEA Table by dragging them from the Containment tree to the FMEA table. New rows are created automatically. You can modify the added items and update the property in the table.

To add a new FMEA Item to the FMEA Table

1. In the FMEA Table, click Add New. A row is added in the FMEA Table, which shows the new FMEA Item. [IMAGE alt='' src='']
2. In the newly created FMEA Item's row and the **Name**column, double-click the designated cell to name the FMEA Item.

To add an existing FMEA Item to the FMEA Table

1. In the FMEA Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the **Select FMEA Item**dialog, select the required FMEA Item and click **OK**. A row is added to the FMEA Table, which shows the existing FMEA Item. 
 
**[IMAGE alt='' src='']**
3. In the newly created FMEA Item's row and the **Name**column, double-click the designated cell to name the FMEA Item.

##### Updating a Failure Mode

To update a Failure Mode to the FMEA Table

1. Double-click the designated cell in the **Failure Mode** column and the required FMEA Item's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Failure Mode_Edit button.png']
2. From the Select Class dialog, select the required Failure Mode and click OK. [ATTACHMENT filename='Select Class dialog.png']

Similarly, you can update the Cause in the FMEA Table.

##### Adding a Final Effect

To add a Final Effect to theFMEA Table

1. Double-click the designated cell in the **Final Effect** column and the required FMEA Item's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Final Effect_Edit.png']
2. From the Select Elements dialog, select the required Failure Mode and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Elements_dialog.png']

Similarly, you can add **Computed Effects, Prevention Controls, Detection Controls,** and **Recommended Actions**in the FMEA Table.

##### Adding an Action Priority

To add an Action Priority to theFMEA Table

1. Double-click the designated cell in the **Action Priority** column and the required FMEA Item's row and click [IMAGE alt='' src=''] .
2. In the Action Priority dialog, type in the required content.

Similarly, you can add **Revised Action Priority**in the FMEA Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p>An FMEA Table allows you to analyze the reliability aspect of your model and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. <span style="color:var(--ds-text,#172b4d);">The RAAML-based FMEA Table diagram is derived from an activity object and represents each FMEA Item—defined as the unique pairing of a failure mode with its corresponding cause—through a dedicated row associated with the activity.</span></p><p>In an FMEA Table, you can:</p><ul><li data-uuid="22e4ee15-0282-4923-8d7e-ff66935f2be7">Create a new FMEA Item directly in a table or add an existing one.</li><li data-uuid="4e9df312-245c-4e98-b5c1-62f66166e7b1">Directly edit the properties of FMEA Items in a table.</li></ul><p>The following table describes each column name, its purpose, and relevant details:</p><table><colgroup><col /><col /></colgroup><tbody><tr><td><p><strong>Column Name</strong></p></td><td><p><strong>Description</strong></p></td></tr><tr><td><p>Name</p></td><td><p>Displays an auto-generated counter for the FMEA item (this prefix counter is a preset customization) and a name. If the name is generated automatically (e.g., <span style="color:var(--ds-text,#172b4d);">from the creation of an FMEA Item in the Robustness Checklist)</span>, it is composed of the Failure Cause and its associated Failure Mode.</p></td></tr><tr><td><p>Inputs</p></td><td><p>List of input pins of the activity element selected as the Scope of the FMEA study. <span style="color:var(--ds-text,#172b4d);">This is a non-editable field.</span></p></td></tr><tr><td><p>Function</p></td><td><p>Activity selected as the scope of the FMEA study. <span style="color:var(--ds-text,#172b4d);">This is a non-editable field.</span></p></td></tr><tr><td><p>Output</p></td><td><p><span>Lists one or more of the output pins that are declared on the activity element selected as the Scope of the FMEA study and that are being affected by a dedicated failure mode. Your selection is limited to the declared output pins on the activity referenced on the Function cell.</span></p></td></tr><tr><td><p>Failure Mode</p></td><td><p>Specifies the Failure Mode specific to the FMEA Item Line. Failure Mode definition is as introduced in the <strong>Parameter Diagram </strong>section, referring to the description of the specific manner in which a component, subsystem, or system could potentially fail to meet the design intent.</p></td></tr><tr><td><p>Classification</p></td><td><p>Corresponds to the categorization of FMEA items, derived from the evaluation of Severity and Occurrence values using a customizable function (preset out-of-the-box as: <span style="color:var(--ds-text,#172b4d);">CC in case severity &gt;= 9, SC in case 9 &gt; severity &gt;= 7, and AC in case 7 &gt; severity &gt;= 5</span>).</p></td></tr><tr><td><p>Final Effect</p></td><td><p>Describes the effect of a Failure Mode on the end user or the environment (i.e., at the system-of-interest level). Multiple Final Effects can be specified for a single FMEA item. Each Final Effect can have a default Severity value assigned as its property. <span style="color:var(--ds-text,#172b4d);">To assign a Severity value, open the Specification window of the Final Effect and set the desired value.</span></p></td></tr><tr><td><p>Computed Effect</p></td><td><p>An element describing <strong>the effect</strong> that a <strong>Failure Mode</strong> has <strong>on the system element under consideration</strong>. An FMEA Item (e.g., a single row of an FMEA Table) can have multiple Local Effects of Failure. <br />If the element under consideration is a subsystem directly underneath the system of interest level itself, <strong>the effect of the Failure Mode</strong> is the same as the <strong>Final Effect</strong> mentioned above in this table.</p></td></tr><tr><td><p>Severity</p></td><td><p><span>The Severity of effects is a rating number associated with the most serious effect for a given failure mode for the operation being evaluated. It is a relative rating within the scope of the individual FMEA item and is determined without regard for occurrence or detection. Valid values range from 1 to 10 (lowest to highest severity).</span></p></td></tr><tr><td><p>Cause</p></td><td><p><span>An element (either a lower-level Failure Mode or a dedicated Cause element) indicating the design weakness that leads to a Failure Mode. An FMEA item (e.g., a single row of an FMEA table) can have one Cause of Failure. A Cause can have default Occurrence and Detectability values assigned as properties. To assign these values, either open the Specification window of the Cause and set the desired Occurrence or Detectability, or edit them directly in the corresponding columns of the FMEA table.</span></p></td></tr><tr><td><p>Prevention Controls</p></td><td><p>A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode. You can specify multiple Prevention controls for a single FMEA Item. <span style="color:var(--ds-text,#172b4d);">The type of object that can be elected as a Prevention Control is by default preset as a Requirement. The type can be customized.</span></p></td></tr><tr><td><p>Occurrence</p></td><td><p><span>A rating number is associated with each cause for a given failure mode being evaluated. The occurrence rating considers the likelihood of occurrence during production. Valid values range from 1 to 10 (lowest to highest probability). A Cause must be identified in the dedicated cell before setting this value. Enter the value directly in the corresponding FMEA table cell or set it on the Failure Mode or Cause object via the containment tree.</span></p></td></tr><tr><td><p>Criticality</p></td><td><p>The product of Severity and Occurrence ratings.</p></td></tr><tr><td><p>Detection Controls</p></td><td><p>An element describing the measures implemented to detect a Failure Mode. Multiple Detection Control entries can be specified for a single FMEA <span style="color:var(--ds-text,#172b4d);">item. The type of object that can be elected as a Detection Control is by default preset as a Block. The type can be customized.</span></p></td></tr><tr><td><p>Detection</p></td><td><p><span>Detection is the rating associated with the likelihood of detecting the failure mode and/or associated cause, according to defined criteria. </span><span>Ability to detect is the rating number associated with the combined capabilities of all the current process controls for a given cause and/or failure mode. You should not automatically presume the detection rating is low because the occurrence rating is low. Instead, the User assumes the failure has occurred, then assesses the capabilities of all the detection-type design controls to detect low-frequency failure modes and/or causes. The detection rating is identified without regard for severity or occurrence. </span><span>Valid Values range from 1 to 10 (highest to lowest detectability).</span></p></td></tr><tr><td><p>Risk Priority Number</p></td><td><p><span>The risk priority number (RPN) is the product of the severity (S), occurrence (O), and detection (D) ratings. Within the scope of the individual FMEA, this value is between “1” and “1000”. </span><span>A benefit of RPN is that it provides an indicator of improvement (before and after actions taken) that reduces any one factor of severity, occurrence, or detection. It shows the distribution of RPN values for a project (Pareto), giving a high-level overview of the risk assessment. </span><span>You should be aware that the final RPN ratings are subjective and relative to a particular analysis.</span></p></td></tr><tr><td><p>Action Priority</p></td><td><p><span>Assessment of the internal priority affecting the recommended <span style="color:var(--ds-text,#172b4d);">actions, as per the SAEJ 1739 rating scale.</span></span></p></td></tr><tr><td><p>Recommended Action</p></td><td><p><span style="color:var(--ds-text,#172b4d);">The description of an action intended to reduce the Risk Priority Number. All critical or significant FMEA items should have associated recommended actions. These actions should focus on design improvements and be directed at mitigating the Cause of Failure or eliminating the Failure Mode. The type of object that can be elected as a Recommended Action element creation is by default preset as a Block. The type can be customized.</span></p></td></tr><tr><td><p>Action Taken</p></td><td><p>A property describing what actions have been taken and the results of these actions <span style="color:var(--ds-text,#172b4d);">(free text capture)</span>.</p></td></tr><tr><td><p>Responsible Person</p></td><td><p>Indicates the person responsible for completing a Recommended Action. <span style="color:var(--ds-text,#172b4d);">No specific object type is being preset to represent a Person.</span></p></td></tr><tr><td><p>Target Date</p></td><td><p>A property defining the targeted completion date of a Recommended Action.</p></td></tr><tr><td><p>Completion Date</p></td><td><p>A property assessing the completion date of a Recommended Action.</p></td></tr><tr><td><p>Revised Severity</p></td><td><p><span>A property assessing the seriousness of the effect(s) of a potential Failure Mode on a component, subsystem, end user, or environment after mitigation. Valid values range from 1 to 10 (lowest to highest severity). A prerequisite is that an action has been taken</span></p></td></tr><tr><td><p>Revised Occurrence</p></td><td><p><span style="color:var(--ds-text,#172b4d);">A property indicating the likelihood that a specific Cause of Failure will occur after mitigation. Valid values range from 1 to 10 (lowest to highest probability of occurrence).</span></p></td></tr><tr><td><p>Revised Criticality</p></td><td><p>The product of Revised Severity and Revised Occurrence ratings.</p></td></tr><tr><td><p>Revised Detection</p></td><td><p><span>A property measuring the likelihood of detecting a potential failure after mitigation. Valid values range from 1 to 10 (highest to lowest detectability).</span></p></td></tr><tr><td><p>Revised Risk Priority Number</p></td><td><p>The product of Revised Criticality by Revised Detection.</p></td></tr><tr><td><p>Revised Action Priority</p></td><td><p><span style="color:var(--ds-text,#172b4d);">Assessment of the internal priority affected by the recommended actions after mitigation.</span></p></td></tr></tbody></table><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="355c44ea-98b8-47eb-964b-a88c170180af"><ac:parameter ac:name="title">Tips</ac:parameter><ac:rich-text-body><ul><li data-uuid="6dc08ad0-c86e-4706-a2e5-1c692046f243">While selecting an FMEA Item element (line in the table):<ul><li>You can remove the line from the table using the dedicated <strong>Remove From Table </strong><span>command.</span></li><li>You can delete it from the containment tree (and the table) using the dedicated <strong>Delete </strong><span>command.</span></li></ul></li><li data-uuid="a323ffce-cc0f-4034-9733-2c195440a163">If a Robustness Check List (RCL) and/or Parameter Diagram exists for the activity, the user can navigate from the FMEA Table to one of those diagrams through a dedicated panel above the diagram. To learn more, refer to the <span style="color:var(--ds-text,#172b4d);"><ac:link><ri:page ri:content-title="(2026x) Robustness Checklist" /></ac:link> </span>page.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Failure Mode and Effect Analysis (FMEA) Table</h3><p>To create a Failure Mode and Effect Analysis (<span>FMEA) Table</span></p><hr /><ol><li data-uuid="35c8888d-77bc-4053-ba6a-fe840702910d">In the Containment tree, right-click the <strong>FMEA </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="946293a1-1c93-4661-a3fc-b76e9cf33ae4">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Safety and Reliability Analysis </strong>and select <strong>RAAML-based FMEA Table.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="FMEA_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword FMEA and then select <strong><span style="color:var(--ds-text,#333333);">RAAML-based FMEA Table</span>.<br /><br /><ac:image><ri:attachment ri:filename="FMEA_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="49d63220-7598-4a57-90fe-7d8160e7de7a">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog_FMEA.png" /></ac:image><br /><br />The FMEA Table is now displayed in the diagram pane of the modeling tool.</li></ol><h3 style="text-align: left;">Adding an FMEA Item to the <span>FMEA Table</span></h3><p>Each Failure mode linked to a Failure Effect (end user effect of a Failure Mode) or to a Failure Cause (element indicating a Design Weakness resulting in a Failure Mode) should result in a new FMEA Item. Generating FMEA Items from the design elements of your model identified earlier in the Robustness Check list diagram saves time and helps avoid mistakes.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="626fe21c-f3f6-4855-a861-577a41e59f18"><ac:rich-text-body><p>You can add existing FMEA Items to an FMEA Table by dragging them from the Containment tree to the FMEA table. New rows are created automatically. You can <span>modify the added items and update the property in the table.</span></p></ac:rich-text-body></ac:structured-macro><p>To add a new FMEA Item to the FMEA Table</p><hr /><ol><li data-uuid="e7ad82d4-332d-4d7a-836a-2c93674634d2"><span style="color:var(--ds-text,#333333);">In the FMEA Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New. </strong><span style="color:var(--ds-text,#333333);">A row is added in the FMEA Table, which shows the new FMEA Item.</span><br /><strong style="text-align: left;"><br /><ac:image><ri:attachment ri:filename="Add New.png" /></ac:image><br /><br /></strong></li><li data-uuid="01cf3e59-a5ce-48bb-b1a9-c6de4f3d757e"><span style="color:var(--ds-text,#333333);">In the newly created FMEA Item's row and the <strong>Name </strong>column, double-click the designated cell to name the FMEA Item.</span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><br /></p><p><span style="color:var(--ds-text,#333333);">To add an existing FMEA Item to the FMEA Table</span></p><hr /><ol><li data-uuid="a1de3be7-0d64-4926-ab31-2496fcd6c5a5"><span style="color:var(--ds-text,#333333);">In the FMEA Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="Add Existing.png" /></ac:image></span><br /><br /></strong></li><li data-uuid="57fd063a-272d-46b4-86e2-827d5ac8da90"><span style="color:var(--ds-text,#333333);">From the <strong>Select FMEA Item </strong>dialog, select the required FMEA Item and click <strong>OK</strong>. A row is added to the FMEA Table, which shows the existing FMEA  Item. <br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Select Activity dialog_FMEA.png" /></ac:image></strong><br /><br /></span></li><li data-uuid="c5aa1e5f-5fb5-45c1-a94e-80300938fb59"><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#333333);">In the newly created FMEA Item's row and the <strong>Name </strong>column, double-click the designated cell to name the FMEA Item.</span><br /></span></li></ol><h3 style="text-align: left;">Updating a Failure Mode</h3><p style="text-align: left;">To update a Failure Mode to the <span style="color:var(--ds-text,#333333);">FMEA Table</span></p><hr style="text-align: left;" /><ol style="text-align: left;"><li data-uuid="0a2cf8c1-9293-44ce-901b-c66a2397ea2c">Double-click the designated cell in the<span> <strong>Failure Mode </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_Edit button.png" /></ac:image><br /><br /></li><li data-uuid="4104f30c-a4b9-4d37-b7d5-0debc2c67b3d">From the<span> </span><strong>Select Class </strong>dialog, select the required Failure Mode and click <strong>OK.</strong><br /><br /><ac:image><ri:attachment ri:filename="Select Class dialog.png" /></ac:image><br /><br /></li></ol><p><span>Similarly, you can update the Cause in the FMEA Table.</span></p><h3>Adding a Final Effect</h3><p>To add a Final Effect <span style="color:var(--ds-text,#172b4d);">to the </span><span style="color:var(--ds-text,#172b4d);">FMEA Table</span></p><hr /><ol><li data-uuid="2542b7fd-c317-435f-b632-3124a0d9fa10">Double-click the designated cell in the<span> <strong>Final Effect </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Final Effect_Edit.png" /></ac:image><br /><br /></li><li data-uuid="f482c46e-680d-4477-a748-19131ef50d28">From the<span> </span><strong>Select Elements </strong>dialog, select the required Failure Mode and click <strong>OK</strong>. <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">To learn more about selecting elements, refer to the<span> </span></span><a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x&amp;variant=default">Selecting Elements</a><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span> </span>page.<br /></span><br /><ac:image><ri:attachment ri:filename="Select Elements_dialog.png" /></ac:image></li></ol><p>Similarly, you can add <strong>Computed Effects,  Prevention Controls, Detection Controls,</strong> and <strong>Recommended Actions </strong>in the FMEA Table.</p><h3>Adding an Action Priority</h3><p>To add an Action Priority <span style="color:var(--ds-text,#172b4d);">to the </span><span style="color:var(--ds-text,#172b4d);">FMEA Table</span></p><hr /><ol><li data-uuid="5c661554-f0ec-4115-87e3-982e2404b31b">Double-click the designated cell in the<span> <strong>Action Priority </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</li><li data-uuid="2b68566d-4a44-4e53-9bda-bddd73203ceb">In the Action Priority dialog, type in the required content.</li></ol><p>Similarly, you can add <strong>Revised Action Priority </strong>in the FMEA Table.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254421573 space=SSE version=3 -->
## PAGE 00013: (2026x) Failure Mode Avoidance

- page_id: `254421573`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421573/2026x+Failure+Mode+Avoidance
- version_number: 3
- version_date: `2025-11-18T10:44:19.943+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

Quality and Safety disciplines are critical to ensure**reliable**and**safe**systems. The System Safety Engineer can perform a Design FMEA per SAE J1739:2021. Design FMEA is a type of FMEA that analyzes product design, focusing on potential design-related deficiencies to improve the design and ensure the product's safe and reliable operation during its useful life.

Based on the system architecture, the Systems Safety Engineer plugin enables:

- The creation of the Boundary Diagram and **Item** to finalize the scope (the relevant parts of the system to be analyzed).
- The creation of an item-based Interface Analysis table to study connections between functions.
- The creation of a Parameter Diagram to identify the measurable parameters that could affect the intended output of a given function.
- The creation of a Robustness Checklist to identify causality links between elements of a given function.
- The creation of a Failure Mode and Effects Analysis table

The Systems Safety Engineer is**RAAML-based**and partiallysupports **SAE J1739.**

**[IMAGE alt='' src='']**

###### Systems Safety Engineer workflow

To learn more about FMA, refer to the following pages:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">Quality and Safety disciplines are critical to ensure<span> </span><strong>reliable</strong><span> </span>and<span> </span><strong>safe</strong><span> </span>systems. The System Safety Engineer can perform a Design FMEA per SAE J1739:2021. Design FMEA is a type of FMEA that analyzes product design, focusing on potential design-related deficiencies to improve the design and ensure the product's safe and reliable operation during its useful life.</p><p style="text-align: left;">Based on the system architecture, the Systems Safety Engineer plugin enables: </p><ul style="text-align: left;"><li data-uuid="a3a4b363-2439-4dda-bad0-3108e5199b3f">The creation of the <strong>Boundary Diagram</strong><span> </span>and<span> <strong>Item </strong></span>to finalize the scope (the relevant parts of the system to be analyzed).</li><li data-uuid="1ff366ce-defd-4594-b301-87ed10c0bd75">The creation of an item-based<span> </span><strong>Interface Analysis</strong><span> </span>table to study connections between functions.</li><li data-uuid="ad5fc33c-c2a1-4d12-bf27-872154c31da3">The creation of a<span> </span><strong>Parameter Diagram</strong><span> </span>to identify the measurable parameters that could affect the intended output of a given function.</li><li data-uuid="ee703be2-74a1-459a-8788-33e6baf49f94">The creation of a<span> </span><strong>Robustness Checklist</strong><span> </span>to identify causality links between elements of a given function.</li><li data-uuid="c2b45559-9a91-45a3-a1b3-85ba067b239f">The creation of a<span> </span><strong>Failure Mode and Effects Analysis</strong><span> </span>table </li></ul><p style="text-align: left;">The Systems Safety Engineer is<span> </span><strong>RAAML-based</strong><span> </span>and partially<span> </span>supports <strong>SAE J1739.</strong></p><p style="text-align: center;"><strong><ac:image ac:border="true" ac:height="646" ac:width="983"><ri:attachment ri:filename="SSE_Workflow.png" /></ac:image></strong></p><h6 style="text-align: center;">Systems Safety Engineer workflow</h6><p style="text-align: left;"><br /></p><p style="text-align: left;">To learn more about FMA, refer to the following pages:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2604d644-6c66-4c5d-9fcd-f56de98f5a3e" /></p>
````

<!--NOMAGIC_PAGE id=254421562 space=SSE version=3 -->
## PAGE 00014: (2026x) Installation, licensing, and system requirements

- page_id: `254421562`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421562/2026x+Installation+licensing+and+system+requirements
- version_number: 3
- version_date: `2025-11-18T10:44:18.742+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

For information regarding installation, licensing, and system requirements, visit the[Installation, licensing, and system requirements](https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&version=2026x)page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="with-breadcrumbs conf-macro output-block">For information regarding installation, licensing, and system requirements, visit the<span> </span><a href="https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&amp;version=2026x">Installation, licensing, and system requirements</a><span> </span>page.</p>
````

<!--NOMAGIC_PAGE id=254421606 space=SSE version=4 -->
## PAGE 00015: (2026x) Interface Analysis

- page_id: `254421606`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421606/2026x+Interface+Analysis
- version_number: 4
- version_date: `2025-11-18T10:44:22.003+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer > (2026x) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

An Interface Analysis table consists of system interfaces, their types (e.g., physical, data, energy, etc.), source/target, and related functions. An Interface Analysis table:

- Starts from any item identified in the Boundary Diagram.
- Captures the interaction between source and target elements.
- Informs the “class” of the interaction.
- Tells whether the interface involves external actors/components.
- Identifies if the interaction is beneficial or detrimental.
- Assigns explicit responsibility to each end of the interaction.
- Defines the functions involved and their “measurable” target and range of variation.

##### Creating an Interface Analysis Table

To create an Interface Analysis Table

1. In the Containment tree, right-click the **Interface** **Analysis** package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Interface Analysis****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword interface and then select **Interface Analysis** . 
 
[IMAGE alt='' src=''] The Interface Analysis Table is now displayed in the diagram pane of the modeling tool.

##### Defining the scope

To define the scope for the Interface Analysis Table

- From the Containment tree, drag and drop the Lamp Scope element on the Scope of the Interface Analysis table. [ATTACHMENT filename='Lamp Scope_drag and drop.png']

##### Adding an Interaction Connector to the Interface Analysis Table

To add an existing Interaction Connector

1. In the Interface Analysis Table, click **Add Existing. 
 
[IMAGE alt='' src='']**
2. In the Select Interaction Connector dialog, select the required Interaction Connector. 
 
[IMAGE alt='' src=''] 
 
A row is added to the Interface Analysis Table, displaying the existing Interaction Connector.

##### Adding a Functional Range

To add a Functional Range

1. Double-click the designated cell in the**Functional Range** column and the required scope element's row and click [IMAGE alt='' src=''].
2. In the Enter Range dialog, enter the Min and Max values and click **OK**. 
 
[IMAGE alt='' src='']

##### Adding a Functional Target

To add a Functional Target

1. Double-click the designated cell in the**Functional Target** column and the required scope element's row and click [IMAGE alt='' src=''].
2. In the Enter Functional Target dialog, enter the****Value and click **OK**. 
 
[IMAGE alt='' src='']

##### Assigning Strength

To assign Strength

1. Double-click the designated cell in the **Strength**column and the required scope element's row, and select the strength from the drop-down list. 
 
[IMAGE alt='' src='']

##### Adding Affected Function

To add Affected Function

1. Double-click the designated cell in the scope element's row and the Affected Function column and click [ATTACHMENT filename='Three Dot _Icon.png'] . The Select Affected Function dialog opens. [ATTACHMENT filename='Affected Function dialog.png']
2. In the Select Affected Function dialog, click [ATTACHMENT filename='Three Dot _Icon.png'] the icon, found near the Call Behavior Action Element.
3. In the Select Call Behavior Action dialog, select the Call Behavior Action and click OK. [ATTACHMENT filename='Call Behavior Action dialog.png']
4. In the Select Affected Function dialog, click [ATTACHMENT filename='Three Dot _Icon.png'] the icon found near the Activity Element.
5. In the Select Activity dialog, select the Activity and click OK. [IMAGE alt='' src='']

##### Adding a Source/Target Interface Owner, Interface Owner Concurrence Date, and Interface Owner Activity

To add a Source/Target Interface Owner

1. Double-click the designated cell in the scope element's row and the Source Interface Owner column and type in the required details.
2. Double-click the designated cell in the scope element's row and the Target Interface Owner column and type in the required details.

Similarly, add the required details for the Source/Target Interface Owner Concurrence Date and Interface Owner Activity.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p style="text-align: left;">An Interface Analysis table consists of system interfaces, their types (e.g., physical, data, energy, etc.), source/target, and related functions. An Interface Analysis table:</p><ul style="text-align: left;"><li data-uuid="06662a0f-d0d5-4dc4-ae59-51da45c1de01">Starts from any item identified in the Boundary Diagram.</li><li data-uuid="ffbc81a6-78a2-4a5d-b9e7-dcb63b3bd385">Captures the interaction between source and target elements.</li><li data-uuid="83016606-a300-4899-a9be-408fef3c1355">Informs the “class” of the interaction.</li><li data-uuid="8f27ab29-7032-494c-82da-cbcd0758e596">Tells whether the interface involves external actors/components.</li><li data-uuid="fcb94ded-4565-4206-b845-61ff55cdd07f">Identifies if the interaction is beneficial or detrimental.</li><li data-uuid="2cd47a93-4755-44aa-8b9a-5f7e9e24758a">Assigns explicit responsibility to each end of the interaction.</li><li data-uuid="d9a6ea07-3df1-4b89-8d83-7a1f40ef4bca">Defines the functions involved and their “measurable” target and range of variation.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating an Interface Analysis Table</h3><p>To create an <span>Interface Analysis Table</span></p><hr /><ol><li data-uuid="39362494-d719-4f02-8a50-ee4590d531d4">In the Containment tree, right-click the <span><strong>Interface</strong> <strong>Analysis </strong></span>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="7de72549-c91d-4c5d-9dec-ebca2efb1500">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <span><strong>Interface Analysis</strong></span><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Interface Analysis_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword interface and then select <span style="color:var(--ds-text,#333333);"><span><strong>Interface Analysis</strong></span></span><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Interface Analysis_Search.png" /></ac:image><br /><br /></strong>The <span style="color:var(--ds-text,#333333);">Interface </span><span style="color:var(--ds-text,#333333);">Analysis Table </span><span>is now displayed in the diagram pane of the modeling tool.</span></li></ul></li></ol><h3>Defining the scope</h3><p>To define the scope for the Interface Analysis Table </p><hr /><ul><li data-uuid="b83b8c21-31f0-4fd6-8961-f41db919a507">From the Containment tree, drag and drop the <strong>Lamp Scope </strong>element on the<strong> Scope </strong>of the Interface Analysis table.<br /><br /><ac:image><ri:attachment ri:filename="Lamp Scope_drag and drop.png" /></ac:image></li></ul><h3 style="text-align: left;">Adding an Interaction Connector to the <span>Interface Analysis Table</span></h3><p><span>To add an existing Interaction Connector</span></p><hr /><ol><li data-uuid="89cd3896-12cc-4745-bd61-fd66b25168e4"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Interface Analysis Table, click <strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="Add Existing.png" /></ac:image><br /><br /></strong></span></li><li data-uuid="ac17b159-822a-46bd-953f-1038fa52db8f"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Select Interaction Connector <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">dialog, select the required Interaction Connector.<br /><br /><ac:image><ri:attachment ri:filename="Select Interaction Connector dialog.png" /></ac:image><br /><br />A row is added to the Interface Analysis Table, displaying the existing <span>Interaction Connector</span>.<br /></span></span></li></ol><h3>Adding a Functional Range</h3><p>To add a Functional Range</p><hr /><ol><li data-uuid="94d1f86d-6a6d-4c3c-8235-eac52692072f"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the<span> </span><strong>Functional Range</strong> </span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">column and the required scope element's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.</span></span></li><li data-uuid="39a510c8-3932-469e-8982-e6462c13a708"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span>In the Enter Range dialog, enter the Min and Max values and click <strong>OK</strong>.<br /><br /><ac:image ac:border="true" ac:height="105" ac:width="249"><ri:attachment ri:filename="Functional Range dialog.png" /></ac:image><br /></span></span></li></ol><h3>Adding a Functional Target</h3><p>To add a Functional Target</p><hr /><ol><li data-uuid="7f19c8ea-bef1-426f-a449-cc6e15699001"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the<span> </span><strong>Functional Target </strong></span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">column and the required scope element's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.</span></span></li><li data-uuid="5db8be0f-102f-45fc-bc17-d278e3aded1b"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span>In the Enter Functional Target dialog, enter the<strong> </strong>Value and click <strong>OK</strong>.<br /><br /><ac:image ac:border="true" ac:height="103" ac:width="226"><ri:attachment ri:filename="Functional Target dialog.png" /></ac:image><br /></span></span></li></ol><h3>Assigning Strength</h3><p><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">To assign Strength</span></p><hr /><ol><li data-uuid="93e08759-3115-4e8d-9aa5-5660a14c50ba"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the <strong>Strength </strong>column and the required scope element's row, and select the strength from the drop-down list.<br /><br /><ac:image><ri:attachment ri:filename="Strenth drop-down.png" /></ac:image><br /></span></li></ol><h3><span>Adding Affected Function</span></h3><p><span>To add Affected Function</span></p><hr /><ol><li data-uuid="46f4eca3-2eeb-4caa-b0a1-8b62c16d130f">Double-click the designated cell in the scope element's row and the Affected Function column and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>. The Select Affected Function dialog opens.<br /><br /><ac:image ac:border="true" ac:height="163" ac:width="354"><ri:attachment ri:filename="Affected Function dialog.png" /></ac:image><br /><br /></li><li data-uuid="dfa1db28-1ec2-4fc4-b661-6329c53c33be">In the Select Affected Function dialog, click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image> the icon, found near the Call Behavior Action Element.</li><li data-uuid="ca4a35c1-0032-412f-9f32-32b48e54ae66">In the Select Call Behavior Action dialog, select the Call Behavior Action and click OK.<br /><br /><ac:image ac:border="true" ac:height="410" ac:width="533"><ri:attachment ri:filename="Call Behavior Action dialog.png" /></ac:image><br /><br /></li><li data-uuid="7286495b-99a4-49b1-ab8a-244eababa7fd">In the Select Affected Function dialog, click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image> the icon found near the Activity Element.</li><li data-uuid="e4645f88-b602-4fe3-ba86-f7a36510b49e">In the Select Activity dialog, select the Activity and click OK.<br /><span><br /><ac:image ac:border="true" ac:height="382" ac:width="531"><ri:attachment ri:filename="Select Activity dialog.png" /></ac:image><br /></span></li></ol><h3>Adding a Source/Target Interface Owner, Interface Owner Concurrence Date, and Interface Owner Activity</h3><p>To add a Source/Target Interface Owner</p><hr /><ol><li data-uuid="bec27aff-a909-4417-b4ac-e901c8406ab8">Double-click the designated cell in the scope element's row and the<strong> Source Interface Owner </strong>column and type in the required details.</li><li data-uuid="49f4f2a7-b598-45ae-a1e6-e1e60c81be49">Double-click the designated cell in the scope element's row and the <strong>Target Interface Owner </strong>column and type in the required details.</li></ol><p>Similarly, add the required details for the <span>Source/Target Interface Owner Concurrence Date and Interface Owner Activity.</span></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254421560 space=SSE version=4 -->
## PAGE 00016: (2026x) Introduction to Systems Safety Engineer

- page_id: `254421560`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421560/2026x+Introduction+to+Systems+Safety+Engineer
- version_number: 4
- version_date: `2025-11-18T10:44:18.293+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

**Model-based safety** refers to a systematic approach to ensure the safety of complex systems by using formal models that represent the system’s structure, behavior, and environment. These models are used to analyze, predict, and verify safety properties before and during the system’s operation. Model-based safety engineering also aims to :

- Identify safety risks early , perform safety verification and validation , and guide the design of safety mechanisms.
- Help detect unsafe states or behaviors before physical implementation or deployment , reducing costly errors.
- Unify domains into one analysis framework, as safety issues may arise from software bugs, hardware faults, cyber-attacks, or their combination.
- Provide traceable, repeatable proofs of safety requirements to ease regulatory compliance and certification
- Enables the use of automated model checking and simulation tools that can exhaustively explore possible scenarios .

The Systems Safety Engineering plugin contains the ISO 26262 plugin. To learn more, refer to the [ISO 26262 plugin](https://docs.nomagic.com/CSRA/?contextKey=iso-26262-functional-safety&version=2026x) user guide.

#### NOTE: Prerequisites

Prerequisites

To install and use the Systems Safety Designer, ensure that one of the following modeling tools is installed:

- Magic Cyber Systems Engineer
- Magic Cyber Systems of Systems Architect
- Cameo Systems Modeler - Architect Edition
- Cameo Systems Modeler - Enterprise Edition
- Cameo Enterprise Architecture
- Magic Draw (any version) with SysML plugin installed

To learn more about how to download the installation files, refer to [Downloading installation files](https://docs.nomagic.com/IL/?contextKey=downloading-installation-files&version=2026x).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Model-based safety</strong> refers to a systematic approach to ensure the safety of complex systems by using formal models that represent the system’s structure, behavior, and environment. These models are used to analyze, predict, and verify safety properties before and during the system’s operation. Model-based safety engineering also aims to :</p><ul><li data-uuid="151084d2-589a-49ae-90fc-0a1300fd4e74"><strong>Identify safety risks early</strong>, perform <strong>safety verification and validation</strong>, and guide the design of safety mechanisms.</li><li data-uuid="c9c4db51-4534-4d29-876e-2a6b3f45ccc9">Help detect unsafe states or behaviors <strong>before physical implementation or deployment</strong>, reducing costly errors.</li><li data-uuid="69d2ebba-63b2-428e-8d52-dcdf7af979c2">Unify domains into one analysis framework, as safety issues may arise from software bugs, hardware faults, cyber-attacks, or their combination.</li><li data-uuid="045a44ee-ba3e-4791-a440-b36774af581c">Provide traceable, repeatable proofs of safety requirements to ease regulatory compliance and certification</li><li data-uuid="83cd63c7-58f4-4412-9ec3-cd8ffb06e4a4">Enables the use of automated model checking and simulation tools that can exhaustively explore possible scenarios<ac:inline-comment-marker ac:ref="b862b50b-d6d3-475f-a880-b127214b6211">.</ac:inline-comment-marker></li></ul><p>The Systems Safety Engineering plugin contains the ISO 26262 plugin. To learn more, refer to the <a href="https://docs.nomagic.com/CSRA/?contextKey=iso-26262-functional-safety&amp;version=2026x">ISO 26262 plugin</a> user guide.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6f459f96-4d19-47a8-8187-d08bea2c157e"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">To install and use the Systems Safety Designer, ensure that one of the following modeling tools is installed:</span></p><ul><li data-uuid="5ebb08d5-10cc-46ca-9e49-452622525e38"><p>Magic Cyber Systems Engineer</p></li><li data-uuid="5cfec0e3-e6d2-43c6-9613-2b89f1358904"><p>Magic Cyber Systems of Systems Architect</p></li><li data-uuid="76e1c66e-ba4d-4d18-a2ee-1a7881aa1fec"><p>Cameo Systems Modeler - Architect Edition</p></li><li data-uuid="f1569cc9-99d7-4240-8052-3e011dee6936"><p>Cameo Systems Modeler - Enterprise Edition</p></li><li data-uuid="af8a0cd7-8238-4b27-b35f-207bdcd91045"><p>Cameo Enterprise Architecture</p></li><li data-uuid="fdae7457-7c07-4075-b5c5-7b5fe32f3acc"><span style="color:var(--ds-text,#333333);">Magic Draw (any version) with SysML plugin installed</span></li></ul><p>To learn more about how to download the installation files, refer to <a href="https://docs.nomagic.com/IL/?contextKey=downloading-installation-files&amp;version=2026x">Downloading installation files</a>.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=254421624 space=SSE version=5 -->
## PAGE 00017: (2026x) Parameter Diagram

- page_id: `254421624`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421624/2026x+Parameter+Diagram
- version_number: 5
- version_date: `2025-11-18T10:44:22.159+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer > (2026x) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

| Concepts | Description |
| --- | --- |
| Failure Mode | A Failure Mode represents a Specific way in which a component, subsystem, or system can fail to perform its intended function. It describes how the failure happens, i.e., the manner or mechanism of failure, not the cause or the consequence directly, but the mode or form the failure takes. |
| Failure Effect | An element describing the effect that a Failure Mode has on the system element under consideration (user, system, subsystem) |
| Noise Factors | Noise factors are sources of uncontrollable variability in a system. These are typically outside the direct control of the designer and introduce disturbances that may affect performance or reliability. The following are the types of Noise Factors that can be created. |
| Piece-to-Piece Variation Noise Factor | Piece-to-Piece Variation is a noise factor referring to variability between different units or parts of the same product. It can include:Manufacturing tolerances (dimension, weight, resistance, etc.)Material variability or changes in suppliersTool wear or production environment conditionsBatch-to-batch differences (also referenced as lot-to-lot variation) in production |
| Change Over Time Noise Factor | Change Over Time refers to system or component variations that occur gradually or incrementally during the lifetime of a product, often due to aging, fatigue, wear, drift, or environmental exposure. |
| Customer Usage Noise Factor | A Customer Usage Noise Factor is a type of uncontrollable variation stemming from how different users interact with the product in real-life scenarios, including misuse within plausible limits, erratic behavior, or varying usage environments. |
| System Interaction Noise Factor | A System Interaction Noise Factor is a disturbance or variability introduced by another system, component, or module, which is outside the local design scope, but interacts through a shared interface, environment, or resource.They are often not visible in unit testing but appear in integration testing.They may stem from electrical, mechanical, software, or communication interfaces.They are uncontrolled from the perspective of the system under analysis. |
| External Environment Noise Factor | An External Environment Noise Factor is a type of variability introduced by the physical, chemical, or climatic conditions in the system’s operating environment that may affect its behavior, functionality, or lifetime. |
| Control Factor | A Control factor is a design parameter or setting that you can actively choose, design, or adjust to achieve the desired system behavior, despite the presence of noise or variation. |
| Unintended output | An unintended output is any system response, signal, or command that is not expected, not commanded, or not aligned with the intended function, whether due to a failure, error, or disturbance. It should be selected among the type "activity pins" (i.e., object "parameters" and its derivative). |

##### Creating a Parameter Diagram

To create a Parameter Diagram

1. In the Containment tree, right-click Parameter Diagram package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Parameter Diagram****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword parameter and then select Parameter Diagram . 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity dialog.png'] The Parameter Diagram is now displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='Parameter diagram.png']

##### Creating a Failure Mode or Effect

To create a Failure Mode or Effect

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  - In the dialog, expand RAAML and select Failure Mode or Effect. 
 
[IMAGE alt='' src='']
  - In the search tab, type the keyword failure or effect, and then select Failure Mode or Effect. 
 
[IMAGE alt='' src='']
3. Name the newly created Failure Mode or Failure Effect in the Containment tree. An automated number is added with a **Counter** that is automatically added once validated.

##### Adding a Failure Mode or Effect in the Parameter Diagram

To add a Failure Mode or Effect in the Parameter Diagram

1. In the Parameter Diagram, select the Failure Mode or Failure Effect cell and cl ick[IMAGE alt='' src=''].
2. In the Select Elements dialog, select the required failure modes or failure effects and click **OK**. To learn more about selecting elements, refer to the [Selecting Elements](https://docs.nomagic.com/MT/?contextKey=selecting-elements&version=2026x&variant=default) page. 
 
[IMAGE alt='' src='']

##### Creating a Noise Factor

To create a Noise Factor from the containment tree

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  - In the dialog, expand Failure Mode Avoidance and select the required type of Noise Factor. [IMAGE alt='' src='']
  - In the search tab, type the required keyword and then select the required type of Noise Factor . [ATTACHMENT filename='Piece to Piece Variation_search.png'] Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.
3. Name the newly created Piece-to-Piece Variation Noise Factor in the Containment tree.

##### Adding a Noise Factor

To add a Noise Factor in the Parameter Diagram

1. In the Parameter Diagram, select the corresponding Noise Factor cell (i.e., Piece to Piece Variation, Change Over Time, Customer Usage, System Interaction, or External Environment ), and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. In the Select Elements dialog, select the required Noise Factor and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Activity dialog_Noise Factor addition.png'] You can create any type of Noise Factor in the Select Elements dialog. To learn more, refer to the [Creating new elements](https://docs.nomagic.com/MT/?contextKey=creating-new-elements&version=2026x&variant=default)page.Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.

##### Creating Control Factor or Unintended Output

To create a Control Factor or Unintended Output from the containment tree

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  1. In the dialog, expand General and select Requirement. 
 
[IMAGE alt='' src='']
  2. In the search tab, type the keyword "requirement" and then select Requirement. 
 
[IMAGE alt='' src='']
3. Name the newly created Requirement in the Containment tree. An automated number is added with a **Counter** that is automatically added once validated.

##### Adding a Control Factor, Unintended Output, or Failure Mode of Unintended Output

To add a Control Factor or Unintended Output in the Parameter Diagram

1. In the Parameter Diagram, select the corresponding cell for Control Factor, Unintended Output, or Failure Mode of Unintended Output and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. In the Select Elements dialog, select the required Control Factor or Unintended Output, or Failure Mode of Unintended Output, and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Elements_Control Factor or Unintended Output.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><table class="wrapped"><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>Concepts</th><th>Description</th></tr><tr class=""><td><strong>Failure Mode</strong></td><td>A Failure Mode represents a Specific way in which a component, subsystem, or system can fail to perform its intended function. It describes <strong>how</strong> the failure happens, i.e., the manner or mechanism of failure, not the cause or the consequence directly, but the mode or form the failure takes.</td></tr><tr class=""><td><strong><span>Failure Effect</span></strong></td><td><span><span style="color:var(--ds-text,#172b4d);">An element describing </span><strong style="text-align: left;">the effect</strong><span style="color:var(--ds-text,#172b4d);"> that a </span><strong style="text-align: left;">Failure Mode</strong><span style="color:var(--ds-text,#172b4d);"> has </span><strong style="text-align: left;">on the system element under consideration (</strong><span style="color:var(--ds-text,#172b4d);">user, system, subsystem)</span></span></td></tr><tr class=""><td><strong>Noise Factors</strong></td><td>Noise factors are sources of uncontrollable variability in a system. These are typically outside the direct control of the designer and introduce disturbances that may affect performance or reliability. The following are the types of Noise Factors that can be created.</td></tr><tr class=""><td><strong>Piece-to-Piece Variation </strong><strong>Noise Factor</strong></td><td><p>Piece-to-Piece Variation is a noise factor referring to variability between different units or parts of the same product. It can include:</p><ul><li data-uuid="bb9bc359-1f18-4ffc-8a1c-531351e9caf4">Manufacturing tolerances (dimension, weight, resistance, etc.)</li><li data-uuid="346e3285-2a12-4ba1-a5c4-d55e810df35d">Material variability or changes in suppliers</li><li data-uuid="54379206-f226-4e52-8cc3-6c1225168557">Tool wear or production environment conditions</li><li data-uuid="96908e82-b1f5-46db-b90b-d6a6a59b7007">Batch-to-batch differences (also referenced as lot-to-lot variation) in production</li></ul></td></tr><tr class=""><td><strong>Change Over Time Noise Factor</strong></td><td>Change Over Time refers to system or component variations that occur gradually or incrementally during the lifetime of a product, often due to aging, fatigue, wear, drift, or environmental exposure.</td></tr><tr class=""><td><strong>Customer Usage Noise Factor</strong></td><td><span>A </span><span>Customer Usage Noise Factor</span><span> is a type of </span><span>uncontrollable variation</span><span> stemming from how </span><span>different users</span><span> interact with the product in </span><span>real-life scenarios</span><span>, including </span><span>misuse within plausible limits</span><span>, </span><span>erratic behavior</span><span>, or </span><span>varying usage environments</span><span>.</span></td></tr><tr class=""><td><strong>System Interaction Noise Factor</strong></td><td><p>A System Interaction Noise Factor is a disturbance or variability introduced by another system, component, or module, which is outside the local design scope, but interacts through a shared interface, environment, or resource.</p><ul><li data-uuid="499ba7cf-be8a-4ddc-977c-a30d4c51407c">They are often not visible in unit testing but appear in integration testing.</li><li data-uuid="c43a7efe-31d1-49e8-94c9-1694fe61a352">They may stem from electrical, mechanical, software, or communication interfaces.</li><li data-uuid="ed941eed-246e-4907-a06b-23d370a61a4d">They are uncontrolled from the perspective of the system under analysis.</li></ul></td></tr><tr class=""><td><strong>External Environment Noise Factor</strong></td><td>An External Environment Noise Factor is a type of variability introduced by the physical, chemical, or climatic conditions in the system’s operating environment that may affect its behavior, functionality, or lifetime.</td></tr><tr class=""><td><strong>Control Factor</strong></td><td>A Control factor is a design parameter or setting that you can actively choose, design, or adjust to achieve the desired system behavior, despite the presence of noise or variation.</td></tr><tr class=""><td><strong><span>Unintended output</span></strong></td><td><span style="color:var(--ds-text,#172b4d);">An </span><span style="color:var(--ds-text,#172b4d);">unintended output</span><span style="color:var(--ds-text,#172b4d);"> is any system response, signal, or command that is </span><span style="color:var(--ds-text,#172b4d);">not expected</span><span style="color:var(--ds-text,#172b4d);">, </span><span style="color:var(--ds-text,#172b4d);">not commanded</span><span style="color:var(--ds-text,#172b4d);">, or </span><span style="color:var(--ds-text,#172b4d);">not aligned with the intended function,</span><span style="color:var(--ds-text,#172b4d);"> whether due to a failure, error, or disturbance. It should be selected among the type &quot;activity pins&quot; (i.e., object &quot;parameters&quot; and its derivative). </span></td></tr></tbody></table><h3><br /><br /></h3></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Parameter Diagram</h3><p>To create a Parameter Diagram </p><hr /><ol><li data-uuid="dbe06a17-67f5-4968-9595-84f52eb78e67">In the Containment tree, right-click <strong>Parameter Diagram </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="3685c10d-64e6-47a9-8466-8087547d61cd">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Parameter Diagram</strong><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Parameter diagram_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword parameter and then select <strong>Parameter Diagram</strong><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Parameter diagram_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="d961e2e9-472f-427a-bb0f-f3007bd0373a">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog.png" /></ac:image><br /><br />The Parameter Diagram is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image ac:border="true" ac:height="510" ac:width="1065"><ri:attachment ri:filename="Parameter diagram.png" /></ac:image></li></ol><h3><span style="color:var(--ds-text,#172b4d);">Creating a Failure Mode or Effect</span></h3><p>To create a Failure Mode or Effect</p><hr /><ol><li data-uuid="1721bc3d-9dc8-43ba-add0-b1ab2ddcdc85">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="c8eeb92d-dd2f-46e6-915c-5ddc0713548e">Do one of the following:<br /><ul><li>In the dialog, expand <strong>RAAML </strong>and select <strong>Failure Mode </strong>or <strong>Effect.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_select.png" /></ac:image><br /><br /></strong></li><li>In the search tab, type the keyword failure or effect, and then select <strong>Failure Mode </strong>or <strong>Effect.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_search.png" /></ac:image><br /><br /></strong></li></ul></li><li data-uuid="7c21892f-9237-419c-b496-c167e592c6be"><span style="color:var(--ds-text,#172b4d);">Name the newly created Failure Mode or Failure Effect in the Containment tree.</span><br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3d915e30-1796-4499-b98b-66fb6e771a7d"><ac:rich-text-body><p>An automated number is added with a <strong>Counter</strong> that is automatically added once validated.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3><span style="color:var(--ds-text,#172b4d);">Adding a Failure Mode or Effect in the Parameter Diagram</span></h3><p>To add a Failure Mode or Effect in the Parameter Diagram</p><hr /><ol><li data-uuid="d0ea622d-64ec-4806-a05a-f7fc4ce85074">In the Parameter Diagram, select the Failure Mode or Failure Effect cell and <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">cl</span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">ick<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.</span></li><li data-uuid="90424724-5225-48e2-b816-cdf0250b7dba"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Select Elements dialog, select the required failure modes or failure effects and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog.png" /></ac:image><br /></span></li></ol><h3>Creating a <span>Noise Factor</span></h3><p>To create a Noise Factor from the containment tree</p><hr /><ol><li data-uuid="7e644063-f402-4f2f-9f29-c5d7f28045fc">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="6e9aaef9-ffa3-4262-adc2-c4d9e90e74bd">Do one of the following:<br /><ul><li>In the dialog, expand <strong>Failure Mode Avoidance </strong>and select the required type of Noise Factor.<strong><br /><br /><ac:image><ri:attachment ri:filename="Piece to Piece Variation_select.png" /></ac:image><br /><br /></strong></li><li>In the search tab, type the required keyword and then select the required type of Noise Factor<strong>.<br /></strong><br /><ac:image><ri:attachment ri:filename="Piece to Piece Variation_search.png" /></ac:image><br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="04bf90ca-1ca8-4a7e-9ade-30b78249ba4b"><ac:rich-text-body><p>Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.</p></ac:rich-text-body></ac:structured-macro></li></ul></li><li data-uuid="fcd957b2-48b9-4c0e-a061-23ae3d26406b"><span style="color:var(--ds-text,#172b4d);">Name the newly created Piece-to-Piece Variation Noise Factor in the Containment tree.</span></li></ol><h3>Adding a Noise Factor</h3><p>To add a Noise Factor in the Parameter Diagram</p><hr /><ol><li data-uuid="6b0fff90-8fe4-4491-be2a-71cf025d3dfd">In the Parameter Diagram, select the corresponding Noise Factor cell (i.e., <strong>Piece to Piece Variation, Change Over Time, Customer Usage, System Interaction, </strong>or<strong> External Environment</strong>),<strong> </strong>and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>.</li><li data-uuid="d09e8bf0-f64c-47f4-8b50-4fdfcdcd184d">In the Select Elements dialog, select the required Noise Factor and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog_Noise Factor addition.png" /></ac:image><br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4a74c2e1-4677-437e-804a-06824d20908d"><ac:rich-text-body><ul><li>You can create any type of Noise Factor in the Select Elements dialog. To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=creating-new-elements&amp;version=2026x&amp;variant=default">Creating new elements</a><span> page.</span></li><li>Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.</li></ul></ac:rich-text-body></ac:structured-macro></li></ol><h3>Creating Control Factor or Unintended Output</h3><p>To create a Control Factor or Unintended Output from the containment tree</p><hr /><ol><li data-uuid="e6db19f3-b399-4125-9e1b-282a6109b8a8">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="09acf9ab-2852-4a0f-8355-172958cec6db">Do one of the following:<ol><li>In the dialog, expand <strong>General </strong><span>and select </span><strong>Requirement.<br /><br /><ac:image><ri:attachment ri:filename="Requirement_select.png" /></ac:image><br /><br /></strong></li><li>In the search tab, type the keyword &quot;requirement&quot; and then select <strong>Requirement.<br /><br /><ac:image ac:thumbnail="true" ac:height="170"><ri:attachment ri:filename="Requirement_search.png" /></ac:image><br /><br /></strong></li></ol></li><li data-uuid="5c74b968-ba79-46f5-be09-d6562fc66dfa"><span style="color:var(--ds-text,#172b4d);">Name the newly created Requirement in the Containment tree.<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cf339c00-03ea-4f63-ae24-80251e57fa31"><ac:rich-text-body><p>An automated number is added with a <strong>Counter</strong> that is automatically added once validated.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3>Adding a Control Factor, Unintended Output, or Failure Mode of Unintended Output</h3><p>To add a Control Factor or Unintended Output in the Parameter Diagram</p><hr /><ol><li data-uuid="781ecf57-8603-4d35-ab8a-2c04dbf5bba9">In the Parameter Diagram, select the corresponding cell for Control Factor, Unintended Output, or Failure Mode of Unintended Output and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>.</li><li data-uuid="70fdbe5d-8106-4e32-bfde-e8aa4223361c">In the Select Elements dialog, select the required Control Factor or Unintended Output, or Failure Mode of Unintended Output, and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=2026x&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements_Control Factor or Unintended Output.png" /></ac:image></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254421660 space=SSE version=7 -->
## PAGE 00018: (2026x) Robustness Checklist

- page_id: `254421660`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421660/2026x+Robustness+Checklist
- version_number: 7
- version_date: `2025-11-18T10:44:23.032+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer > (2026x) Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

For a specific function/activity, a Robustness Check List allows verifying that prevention controls (design methods) and detection controls (test methods) are adequate given the impact of failure modes/failure effects to be covered and the range of variation of noise factors that cause these failure modes/failure effects to arise.

The rows and columns of the Robustness Check List display the noise factors with their associated ranges of variation, the failure causes, the failure modes, the failure effects, the prevention controls, the detection controls, and the recommended actions associated with the function/activity for which the RCL is established. All these elements could come from the function/activity Parameter Diagram, except the failure causes, which are introduced manually in the Robustness Check List.

**EssentialInformation:**

- The robustness checklist diagram is created based on an activity object.
- All relationships in the Robustness Checklist can be deleted by right-clicking the cell and selecting the corresponding delete command. It can also be deleted from the model itself by pressing the Delete key on the Keyboard.
- The Parameter diagram and the FMEA table also show all existing relationships.
- In case a Parameter Diagram and/or an FMEA table exist for the activity, you can navigate from the Robustness Checklist with the help of the commands present in the toolbar. The following table displays the icons and functions of the commands: IconDescription[IMAGE alt='' src='']Opens the Function in the Parameter Diagram[IMAGE alt='' src='']Opens the Function in the RAAML-based FMEA Table

The Robustness Checklist is a Dependency Matrix. To learn more, refer to the [Dependency Matrix](https://docs.nomagic.com/MT/?contextKey=dependency-matrix&version=2026x&variant=default)page.

##### Creating a Robustness Checklist

To create a Robustness Checklist

1. In the Containment tree, right-click the Robustness Checklist package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Robustness Checklist.** [IMAGE alt='' src='']
  - In the search tab, type the keyword robust and then select Robustness Checklist. 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity.png'] The Robustness Checklist is now displayed in the diagram pane of the modeling tool. You must focus on identifying relationships with the aid of the white cells, as the grey cells are not editable. [ATTACHMENT filename='Robustness_Checklist.png']

##### Adding an element to the Robustness Checklist

To add an element to the Robustness Checklist

1. In the containment Tree, select the element to be added.
2. Drag and drop the element on the Column corresponding to the element folder and refresh the diagram. [ATTACHMENT filename='Adding element.png']

##### Deleting elements from the Robustness Checklist

To delete elements from the Robustness Checklist

1. In the Robustness Checklist, select the element to be deleted.
2. Right-click and select Remove from the Matrix from the Contextual menu. [ATTACHMENT filename='Delete Element.png']

You can completely delete the element by pressing the Delete button on the Keyboard.

##### Creating a range for the Noise Factor

With the Robustness checklist, you can enter a range describing the boundaries in an existing Unit of measure for the variation of the Noise Factor.

To create a range for the Noise Factor

1. Select the cell corresponding to the targeted Noise Factor and the first column Range.
2. Right-click and select Define Range from the Contextual menu. [ATTACHMENT filename='Define Range Command.png']
3. In the Define Range dialog, insert the required Min value, Max value, and define the Unit. [IMAGE alt='' src='']
4. C lick OK.

##### Creating Design Limits for the Activity

To create a Design Limit for the Activity

1. Select the cell corresponding to the targeted Noise Factor and the second column, Design Limits .
2. Right-click and select Design Limits from the Contextual menu. [ATTACHMENT filename='Desgin Limit command.png']
3. In the Define Range dialog, insert the required Min value, Max value, and define the Unit. [ATTACHMENT filename='Define Range dialog_Desgin Limit.png']
4. C lick OK.

##### Defining coverage for Prevention or Detection Controls

Design methods and test methods may cover a fraction of the range of a noise factor or more than the range of the noise factor. The end user can capture the range of the coverage when a prevention control or detection control is associated to a noise factor using a contextual menu item **Define coverage**. A dialog allows capturing a minimal value and a maximal value covered by the control, with the same unit as the covered noise factor. The covered range is persisted in the prevention or detection dependency, allowing controls to be enriched without modifying them directly.

The formula to compute the percentage of coverage follows the following rule: if the full range of the noise factor is not covered, the fraction that is covered is computed, and the ratio to the full range of the noise factor is displayed; otherwise, the percentage of coverage is the ratio between the control range and the noise factor range.

To Define Coverage

1. Select the cell corresponding to the targeted controls to be defined.
2. Right-click and select Define Coverage from the Contextual menu. [ATTACHMENT filename='Define Coverage.png']
3. In the Define Range dialog, insert the required Min value and Max value. [ATTACHMENT filename='Define Range dialog_Define coverage.png']
4. Click OK .

- The percentage of coverage is displayed in the Robustness Checklist.
- The relationship between the control and the other element must be established beforehand.

##### Prioritizing the High Impact Failure Mode

To highlight the High Impact Failure mode in the Robustness Checklist.

- Right-click the required Failure Mode and select Toggle High Impact Status from the Contextual menu. [ATTACHMENT filename='Toggle High Impact Status.png']

##### Creating a Relevant To Relationship

A **Relevant To**relationship can be created between:

- Noise Factor and Activity Input
- Failure Mode and Activity Output

To create a Relevant To relationship

1. Select the white cell between a Noise Factor and an Input.
2. Right-click and select Create Relevant To from the Contextual menu. [ATTACHMENT filename='Input_Relevant To.png']
3. Select the white cell between a Failure mode and an Output
4. Right-click and select Create Relevant To from the Contextual menu. [ATTACHMENT filename='Output_Relevant To.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the **Red Arrow**.

##### Creating Causality Relationship

A**Causality**relationship can be created between:

- Noise Factor and Failure Cause
- Noise Factor and Failure Mode

To create a Causality relationship

1. Select the white cell between a Noise Factor and a Failure Cause.
2. Right-click and select Create Causality from the Contextual menu. [ATTACHMENT filename='Causality_Failure Cause.png']
3. Select the white cell between a Noise factor and a Failure Mode.
4. Right-click and select Create Causality from the Contextual menu. [ATTACHMENT filename='Causality_Failure Mode.png']

An association is created between the two elements and is visible in the Robustness Checklist with the help of the **Blue Line**.

##### Creating a PreventionRelationship

A **Prevention**relationship can be created between Prevention Control and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Preventionrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Prevention from the Contextual menu. [ATTACHMENT filename='Create Prevention.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the **Green Arrow**.

##### Creating aDetectionRelationship

A**Detection**relationship can be created between Detection Control and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Detectionrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Detection from the Contextual menu. [ATTACHMENT filename='Create Detection.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the **Orange Arrow**.

##### Creating aRecommendation Relationship

A**Recommendation**relationship can be created between the Recommended Action and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Recommendationrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Recommendation from the Contextual menu. [ATTACHMENT filename='Create Recommendation.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the **Purple Arrow**.

##### Creating an FMEA Item

An FMEA Item relationship can be created between a Failure Mode and:

- A Failure Cause
- A Failure Effect

To create an FMEA Item

1. Select the white cell between the targeted elements.
2. Right-click and select Create FMEA Item from the Contextual menu. [ATTACHMENT filename='Create FMEA Item.png']

- A Failure Mode to Failure Effect relationship is created between the two elements and is visible in the Robustness Checklist with the help of the Pink Arrow .
- A Failure Cause to Failure Mode relationship is created between the two elements and is visible in the Robustness Checklist with the help of the Dark Blue Arrow .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);">For a specific function/activity, a Robustness Check List allows verifying that prevention controls (design methods) and detection controls (test methods) are adequate given the impact of failure modes/failure effects to be covered and the range of variation of noise factors that cause these failure modes/failure effects to arise.</span></p><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);">The rows and columns of the Robustness Check List display the noise factors with their associated ranges of variation, the failure causes, the failure modes, the failure effects, the prevention controls, the detection controls, and the recommended actions associated with the function/activity for which the RCL is established. All these elements could come from the function/activity Parameter Diagram, except the failure causes, which are introduced manually in the Robustness Check List.</span></p><p><strong><span style="color:var(--ds-text,#172b4d);">Essential </span>Information:</strong></p><ul><li data-uuid="d09df54a-2d28-4174-9ba5-db21df3cbb45">The robustness checklist diagram is created based on an activity object.</li><li data-uuid="ec4b945c-3771-406a-91df-20ee31128d17">All relationships in the Robustness Checklist can be deleted by right-clicking the cell and selecting the corresponding delete command. It can also be deleted from the model itself by pressing the Delete key on the Keyboard.</li><li data-uuid="cfac1aac-b5d5-4f6f-86dc-e3ba6f7c01d7">The Parameter diagram and the FMEA table also show all existing relationships.</li><li data-uuid="9f76ab11-4678-439e-9487-bcec57f7462a">In case a Parameter Diagram and/or an FMEA table exist for the activity, you can navigate from the Robustness Checklist with the help of the commands present in the toolbar. The following table displays the icons and functions of the commands:<br /><br /><table class="wrapped"><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th style="text-align: center;">Icon</th><th style="text-align: center;">Description</th></tr><tr class=""><td style="text-align: center;"><div class="content-wrapper" title=""><p><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Open Function in Parameter Diagram.png" /></ac:image></p></div></td><td style="text-align: left;">Opens the Function in the Parameter Diagram</td></tr><tr class=""><td style="text-align: center;"><div class="content-wrapper" title=""><p><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Open Function in RAAML based FMEA Table.png" /></ac:image></p></div></td><td style="text-align: left;">Opens the Function in the RAAML-based FMEA Table</td></tr></tbody></table></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fda1a168-75a0-45d4-957b-71e2562c2713"><ac:rich-text-body><p>The Robustness Checklist is a <span style="color:var(--ds-text,#172b4d);">Dependency Matrix</span>. To learn more, refer to the <span style="color:var(--ds-text,#172b4d);"><a href="https://docs.nomagic.com/MT/?contextKey=dependency-matrix&amp;version=2026x&amp;variant=default">Dependency Matrix</a> </span>page.</p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Robustness Checklist</h3><p>To create a Robustness Checklist </p><hr /><ol><li data-uuid="892fc8f0-795d-47aa-8761-c9ed64f015aa">In the Containment tree, right-click the <strong>Robustness Checklist </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="2d14e84a-b761-4561-9363-6e13079341d3">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Robustness Checklist.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Robustness_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword robust and then select <strong>Robustness Checklist.<br /><br /><ac:image ac:thumbnail="true" ac:height="162"><ri:attachment ri:filename="Robustness_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="a5d0d5d4-6d6e-4687-be18-590ec7fc7a2e">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity.png" /></ac:image><br /><br />The Robustness Checklist is now displayed in the diagram pane of the modeling tool.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9e61e657-7953-4837-be46-58d6639b3e94"><ac:rich-text-body><p>You must focus on identifying relationships with the aid of the white cells, as the grey cells are not editable.</p></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="Robustness_Checklist.png" /></ac:image></li></ol><h3>Adding an element to the Robustness Checklist</h3><p>To add an element to the Robustness Checklist</p><hr /><ol><li data-uuid="b24ed1a7-9041-4ed0-abad-f84064d823d8">In the containment Tree, select the element to be added.</li><li data-uuid="4d5d38bc-064b-4e55-9a71-7d88a5d4d483">Drag and drop the element on the Column corresponding to the element folder and refresh the diagram.<br /><br /><ac:image><ri:attachment ri:filename="Adding element.png" /></ac:image></li></ol><h3>Deleting elements from the Robustness Checklist</h3><p>To delete elements from the Robustness Checklist</p><hr /><ol><li data-uuid="78dcbe1c-7f26-4777-b6d9-4448133127a7">In the Robustness Checklist, select the element to be deleted.</li><li data-uuid="a271a947-821d-4540-b69c-8775b2863344">Right-click and select <strong>Remove from the Matrix </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Delete Element.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e0866958-7124-453c-a2b8-22dd157bfdf8"><ac:rich-text-body><p>You can completely delete the element by pressing the Delete button on the Keyboard.</p></ac:rich-text-body></ac:structured-macro><h3>Creating a range for the Noise Factor</h3><p>With the Robustness checklist, you can enter a range describing the boundaries in an existing Unit of measure for the variation of the Noise Factor.</p><p>To create a range for the Noise Factor</p><hr /><ol><li data-uuid="a7345d17-5745-42ac-a5b4-c698e107e42b">Select the cell corresponding to the targeted Noise Factor and the first column <strong>Range.</strong></li><li data-uuid="af2a4d11-17a7-488b-8468-003e478eeac2">Right-click and select <strong>Define Range </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Define Range Command.png" /></ac:image><br /><br /></li><li data-uuid="d76e50f7-3625-4ad2-b2d8-4dfff84089f6">In the Define Range dialog, insert the required <strong>Min </strong>value, <strong>Max </strong>value, and define the <strong>Unit. </strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog.png" /></ac:image><br /><br /></strong></li><li data-uuid="88382b09-135b-470c-bd76-c6b125ed7184">C<span>lick </span><strong>OK.</strong></li></ol><h3>Creating Design Limits for the Activity</h3><p>To c<span>reate a Design Limit for the Activity</span></p><hr /><ol><li data-uuid="8e6c3f42-d08a-486b-8ccc-ce398f82e9dc">Select the cell corresponding to the targeted Noise Factor and the second column, <strong>Design Limits</strong>.</li><li data-uuid="6aa04f5c-a0bf-48c9-a3f7-6ff85c1f5e11">Right-click and select <strong>Design Limits </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Desgin Limit command.png" /></ac:image><br /><br /></li><li data-uuid="2018a8e2-9aa8-46f4-b163-76c1047ae1a9">In the Define Range dialog, insert the required <strong>Min </strong>value, <strong>Max </strong>value, and define the <strong>Unit.</strong><br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog_Desgin Limit.png" /></ac:image><br /><br /></li><li data-uuid="69d9fe17-d48e-4bae-b8f7-d4ae4b3b2fe3">C<span>lick </span><strong>OK.</strong></li></ol><h3>Defining coverage for Prevention or Detection Controls</h3><p>Design methods and test methods may cover a fraction of the range of a noise factor or more than the range of the noise factor. The end user can capture the range of the coverage when a prevention control or detection control is associated to a noise factor using a contextual menu item <strong>Define coverage</strong>. A dialog allows capturing a minimal value and a maximal value covered by the control, with the same unit as the covered noise factor. The covered range is persisted in the prevention or detection dependency, allowing controls to be enriched without modifying them directly.</p><p>The formula to compute the percentage of coverage follows the following rule: if the full range of the noise factor is not covered, the fraction that is covered is computed, and the ratio to the full range of the noise factor is displayed; otherwise, the percentage of coverage is the ratio between the control range and the noise factor range.</p><p><br /></p><p><span>To Define Coverage </span></p><hr /><ol><li data-uuid="94b2061e-2845-4be1-9d0b-bc6b3628f8ea">Select the cell corresponding to the targeted controls to be defined.</li><li data-uuid="c5078f61-d639-4e50-a382-a9f51c3902f8">Right-click and select <strong>Define Coverage </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Define Coverage.png" /></ac:image><br /><br /></li><li data-uuid="4e6bca39-338a-4871-baa4-1eff63417e1a">In the Define Range dialog, insert the required <strong>Min </strong>value and  <strong>Max </strong>value. <br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog_Define coverage.png" /></ac:image><br /><br /></li><li data-uuid="df3e917e-eba2-4692-9efc-a047d13f6221">Click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0b85f398-5ea0-4100-9f0f-9c9f1e0d91d5"><ac:rich-text-body><ul><li data-uuid="44160890-1b00-403e-b129-ec217ccf9126">The percentage of coverage is displayed in the Robustness Checklist.</li><li data-uuid="2f023968-545f-4cfb-a9c5-15c572ab3eaa"><p>The relationship between the control and the other element must be established beforehand.</p></li></ul></ac:rich-text-body></ac:structured-macro><h3>Prioritizing the High Impact Failure Mode</h3><p><span>To highlight the High Impact Failure mode in the Robustness Checklist.</span></p><hr /><ul><li data-uuid="51947f67-450f-46f0-9bdd-bf64675d28b8">Right-click the required Failure Mode and select <strong>Toggle High Impact Status </strong><span>from the Contextual menu.<br /><br /></span><ac:image><ri:attachment ri:filename="Toggle High Impact Status.png" /></ac:image></li></ul><h3>Creating a Relevant To Relationship</h3><p>A <strong>Relevant To </strong>relationship can be created between:</p><ul><li data-uuid="7088c7a2-6d65-42fb-95fb-87865ddf45ed">Noise Factor and Activity Input</li><li data-uuid="88479b76-7825-4ee2-b179-abb45ae3dede">Failure Mode and Activity Output</li></ul><p>To create a Relevant To relationship</p><hr /><ol><li data-uuid="acaf710c-bc6a-4493-ace4-ed9e3065b175">Select the white cell between a Noise Factor and an Input.</li><li data-uuid="6fffbf05-1bc0-4987-bad5-0b97f0c45ffe">Right-click and select <strong>Create Relevant To </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Input_Relevant To.png" /></ac:image><br /><br /></li><li data-uuid="26ee81af-800f-4a33-a37c-82f58b95b9d1">Select the white cell between a Failure mode and an Output</li><li data-uuid="36545424-4fd4-414b-a652-4ccedfe8cb5e">Right-click and select <strong>Create Relevant To </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Output_Relevant To.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c12d578d-3a4e-4b48-873b-487cd765b396"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Red Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3>Creating Causality Relationship</h3><p>A<strong> Causality </strong>relationship can be created between:</p><ul><li data-uuid="e96040a3-1f79-4d09-95b3-aaa93ff95885">Noise Factor and Failure Cause</li><li data-uuid="ba3aa7a4-de82-43be-ad6d-a0ef7e745f56">Noise Factor and Failure Mode</li></ul><p><br /></p><p>To create a Causality relationship</p><hr /><ol><li data-uuid="9d70cda2-5608-4f6c-9ff8-86a3086d1d62">Select the white cell between a Noise Factor and a Failure Cause.</li><li data-uuid="570bb26f-96e0-4925-8f6e-b95f8328eacd">Right-click and select <strong>Create Causality </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Failure Cause.png" /></ac:image><br /><br /></li><li data-uuid="837f85a6-a7a8-47bd-ab07-38e0e20e526a">Select the white cell between a Noise factor and a Failure Mode.</li><li data-uuid="ec28be0e-5ec8-4edf-9d7a-ccb1326ee5fb">Right-click and select <strong>Create Causality </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Failure Mode.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="04342581-82fe-45e1-93f5-f2ee6ca5bdd2"><ac:rich-text-body><p><span>An association is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Blue Line</strong>.</span></p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a Prevention </span><span>Relationship</span></h3><p>A <strong>Prevention </strong>relationship can be created between Prevention Control and :</p><ul><li data-uuid="fc3464a9-b0f4-4528-a26d-8b363d3c5b3b">Noise factor</li><li data-uuid="1f4742e4-3352-41ba-9bf7-759b706a82b8">Failure Cause</li><li data-uuid="4019f463-3fc2-4b5e-b988-985284e662f8">Failure Mode</li><li data-uuid="938cd914-1ff3-4d86-b66f-0f82bec5e105">Failure Effect</li></ul><p>To create a <span>Prevention </span><span>relationship</span></p><hr /><ol><li data-uuid="aa197250-4208-4548-885d-32e5b59c900e">Select the white cell between the targeted elements.</li><li data-uuid="d1460d36-5cf6-4e48-a3d0-40bab0655431">Right-click and select <strong>Create Prevention </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Prevention.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5b9acbc9-09cf-4d30-a5db-1a4eed2e812c"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Green Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a </span><span>Detection </span><span>Relationship</span></h3><p>A<strong> Detection </strong>relationship can be created between Detection Control and :</p><ul><li data-uuid="a01fb4b2-5267-4860-844e-095b9594d99b">Noise factor</li><li data-uuid="fc85d6d1-a86b-43aa-a233-7bed8ee0950a">Failure Cause</li><li data-uuid="19dc5177-6ca4-42b8-b59f-c05bdc653315">Failure Mode</li><li data-uuid="170e1b9b-e092-476e-ae39-dbfa2425aed5">Failure Effect</li></ul><p>To create a <span>Detection </span><span>relationship</span></p><hr /><ol><li data-uuid="4bab0dfe-a834-4b8a-a0a0-70ea004663e4">Select the white cell between the targeted elements.</li><li data-uuid="455d3108-8fe8-441c-8072-4460825af268">Right-click and select <strong>Create Detection </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Detection.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="aec35c91-e3e9-4d79-8a1f-32e8c5f2fcdb"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Orange Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a </span><span>Recommendation Relationship</span></h3><p>A<strong> Recommendation </strong>relationship can be created between the Recommended Action and  :</p><ul><li data-uuid="d2b237bb-99f1-400e-9190-078b5a7bd929">Noise factor</li><li data-uuid="c29234a1-738d-4e5d-8520-ff02b0f3b9ba">Failure Cause</li><li data-uuid="0beb4d1a-1aea-4500-974a-10f8cdb702b5">Failure Mode</li><li data-uuid="6fdc28ff-b107-4a67-92f1-071579334eda">Failure Effect</li></ul><p>To create a <span>Recommendation </span><span>relationship</span></p><hr /><ol><li data-uuid="d285265c-5cfb-45fb-955d-b70eab5d1b08">Select the white cell between the targeted elements.</li><li data-uuid="bcafb79a-26c9-4a86-ac6c-60eb14dd71e4">Right-click and select <strong>Create <span>Recommendation </span></strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Recommendation.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b2e31893-834d-46da-a2e0-32284880626a"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Purple Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3>Creating an FMEA Item</h3><p>An FMEA Item relationship can be created between a Failure Mode and:</p><ul><li data-uuid="116085d4-cf32-42f8-bedd-873c262d2c71">A Failure Cause</li><li data-uuid="86b6acd3-136d-44bb-a2cb-6152ecd1d999">A Failure Effect</li></ul><p>To create an FMEA Item</p><hr /><ol><li data-uuid="5b34a555-7d9d-453f-9a94-a0a5d2e3d704">Select the white cell between the targeted elements.</li><li data-uuid="44cc3523-496c-4cc5-b3ce-cc28639f9b8f">Right-click and select <strong>Create <span>FMEA Item </span></strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create FMEA Item.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4e59ec84-97a2-4020-b0c1-92413d6d808c"><ac:rich-text-body><ul><li data-uuid="825a86aa-6266-457f-b2b4-036c21397c1c">A Failure Mode to Failure Effect relationship is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Pink Arrow</strong>.</li><li data-uuid="279470ab-ec4f-4e22-8f9d-5bbed7684c6e">A Failure Cause to Failure Mode relationship is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Dark Blue Arrow</strong>.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254421557 space=SSE version=3 -->
## PAGE 00019: (2026x) Systems Safety Engineer

- page_id: `254421557`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421557/2026x+Systems+Safety+Engineer
- version_number: 3
- version_date: `2026-04-24T11:19:28.592+02:00`
- ancestors: Versions of Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

#### WARNING: Technology Preview

Technology Preview

This is the **technology preview** version. We **do not** recommend using it to create any long-term projects because it may change without notice. The migration to the latest version will not be possible.

Quality and Safety disciplines are critical to ensure**reliable**and**safe**systems.

Based on the system architecture, the Systems Safety Engineer plugin enables:

- The creation of the Boundary Diagram and **Item** to finalize the scope, the relevant parts of the system to be analyzed.
- The creation of an item-based Interface Analysis table to study connections between functions.
- The creation of a Parameter Diagram to identify the measurable parameters that could affect the intended output of a given function.
- The creation of a Robustness Checklist to identify causality links between elements of a given function.
- The creation of a Failure Mode and Effects Analysis table

Systems Safety Engineer is**RAAML-based**and partiallysupports **SAE J1739.**

**[IMAGE alt='' src='']**

###### Systems Safety Engineer workflow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1ce8104b-f556-4ea4-b382-01746572a2e6"><ac:parameter ac:name="title">Technology Preview</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">This is the <strong>technology preview</strong> version. We <u><strong>do not</strong></u> recommend using it to create any long-term projects because it may change without notice. The migration to the latest version will not be possible. </span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p style="text-align: left;">Quality and Safety discipline<ac:inline-comment-marker ac:ref="37466a70-af18-4867-94b1-fb68120a27ce">s are critical</ac:inline-comment-marker> to ensure<span> </span><strong>reliable</strong><span> </span>and<span> </span><strong>safe</strong><span> </span>systems.</p><p style="text-align: left;">Based on the system architecture, the Systems Safety Engineer plugin enables: </p><ul style="text-align: left;"><li data-uuid="3f540db5-e389-4a4b-8523-cdc36585110f">The creation of the <strong>Boundary Diagram</strong><span> </span>and<span> <strong>Item </strong></span>to finalize the scope, the relevant parts of the system to be analyzed.</li><li data-uuid="80725f4b-abb9-4e63-946d-6db68b3bee78">The creation of an item-based<span> </span><strong>Interface Analysis</strong><span> </span>table to study connections between functions.</li><li data-uuid="e5730bf5-a485-4dbd-bb43-07aaca877242">The creation of a<span> </span><strong>Parameter Diagram</strong><span> </span>to identify the measurable parameters that could affect the intended output of a given function.</li><li data-uuid="d91ec259-dcf9-47cd-b160-9373cac38c8c">The creation of a<span> </span><strong>Robustness Checklist</strong><span> </span>to identify causality links between elements of a given function.</li><li data-uuid="d39015c0-af0f-4b64-8254-537060761b99">The creation of a<span> </span><strong>Failure Mode and Effects Analysis</strong><span> </span>table </li></ul><p style="text-align: left;">Systems Safety Engineer is<span> </span><strong>RAAML-based</strong><span> </span>and partially<span> </span>supports <strong>SAE J1739.</strong></p><p style="text-align: center;"><strong><ac:image ac:border="true" ac:height="646" ac:width="983"><ri:attachment ri:filename="SSE_Workflow.png" /></ac:image></strong></p><h6 style="text-align: center;">Systems Safety Engineer workflow</h6>
````

<!--NOMAGIC_PAGE id=254421564 space=SSE version=3 -->
## PAGE 00020: (2026x) Systems Safety Engineer Project

- page_id: `254421564`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421564/2026x+Systems+Safety+Engineer+Project
- version_number: 3
- version_date: `2025-11-18T10:44:19.435+01:00`
- ancestors: Versions of Systems Safety Engineer > (2026x) Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

**On this page**

**3**

##### Creating a Failure Mode Avoidance project

To create a new Failure Mode Avoidance project

1. Do one of the following:
  - From the File menu, select New Project from the drop-down list. [IMAGE alt='' src='']
  - Click Create New Project on the welcome screen. [ATTACHMENT filename='Create New Project_Command.png']
  - Press Ctrl + Shift + N.
2. In the New Project dialog, select the **Failure Mode Avoidance Project.** 
[IMAGE alt='' src='']
3. Specify the file name in the Name box.
4. Click the[IMAGE alt='' src='']button to select the location to store the project in a folder.
5. Select the checkbox to automatically create a folder for the project in the specified location.
6. Click **OK**.

A new FMA project is displayed with the default packages in the Containment tree and the Index.

If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling tool.

##### FMA Project Template

A default FMA project template is displayed once you open the project. This template is provided to help you initiate the process.

**Containment Tree**

The Containment tree displays the default packages in the Containment tree. You can add, modify or delete any element or package from the Containment tree.

**Index**

The Index displays the default information related to FMA.

If you press the CTRL key and double-click any table's icon, the table opens in a new tab.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong> On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="46c4561c-0f22-492b-8293-80bfb1550691"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Failure Mode Avoidance project</h3><p>To create a new Failure Mode Avoidance project</p><hr /><ol><li data-uuid="c9663650-be20-4101-a6f2-9e1cc79268c0">Do one of the following:<ul><li class="atl-forced-newline">From the<span> </span><strong>File</strong><span> </span>menu, select <strong>New Project </strong>from the drop-down list.<br /><em><br /><ac:image><ri:attachment ri:filename="New Project_command.jpg" /></ac:image><br /><br /></em></li><li>Click <strong>Create New Project </strong>on the welcome screen.<br /><br /><ac:image><ri:attachment ri:filename="Create New Project_Command.png" /></ac:image><br /><br /></li><li>Press Ctrl + Shift + N.</li></ul></li><li data-uuid="4310d984-d576-48e0-8043-17f8f317b18e"><p class="auto-cursor-target">In the New Project dialog, select the <strong>Failure Mode Avoidance Project.<br /></strong><br /><ac:image><ri:attachment ri:filename="Create new project.png" /></ac:image><br /><br /></p></li><li data-uuid="d890174a-ac09-481f-87f7-9b950bd6b214"><p class="auto-cursor-target">Specify the file name in the Name box.</p></li><li data-uuid="e39405d4-db37-4b91-be61-253584a3ad9e"><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Click the</span><span style="color:var(--ds-text,#333333);"><span> <ac:image><ri:attachment ri:filename="Three Dot Icon.png" /></ac:image> </span>button to select the location to store the project in a folder.</span></p></li><li data-uuid="a19816a0-a524-478e-b6c8-2f26f808363e"><p class="auto-cursor-target">Select the checkbox to automatically create a folder for the project in the specified location.</p></li><li data-uuid="d62ba4ba-6a2c-433f-b1ae-205655313535"><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li></ol><p>A new FMA project is displayed with the default packages in the Containment tree and the Index.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="df13aefb-d300-4916-8e58-5927a3285c35"><ac:rich-text-body><p>If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling tool.</p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">FMA Project Template</h3><p>A default FMA project template is displayed once you open the project. This template is provided to help you initiate the process.</p><p><strong>Containment Tree</strong></p><p>The Containment tree displays the default packages in the Containment tree. You can add, modify or delete any element or package from the Containment tree.</p><p><strong>Index</strong></p><p>The Index displays the default information related to FMA. </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="99614ef4-6697-44ce-a28f-8369f17b828d"><ac:rich-text-body><p>If you press the CTRL key and double-click any table's icon, the table opens in a new tab.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="FMEA Template.png" /></ac:image><br /><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249578367 space=SSE version=13 -->
## PAGE 00021: Boundary Diagram

- page_id: `249578367`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578367/Boundary+Diagram
- version_number: 13
- version_date: `2025-11-18T10:42:49.843+01:00`
- ancestors: Systems Safety Engineer > Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

Boundary diagram and Boundary diagram item aid in identifying and capturing in exhaustive detail about :

- The Internal sub-systems and components and external “actors”/entities
- The different scopes of analysis by visually outlining the system boundary.
- The interactions with legends
- Missing interactions.

##### Creating a Boundary Diagram

To create a Boundary Diagram

1. In the Containment tree, right-click the Boundary Diagram package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Boundary Diagram****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword boundary and then select Boundary Diagram . 
 
[IMAGE alt='' src='']

The Boundary Diagram is now displayed in the diagram pane and in the Containment tree of the modeling tool. 
 
[IMAGE alt='' src='']

##### Adding an Internal Block Diagram of a Use Project

To add an Internal Block Diagram of a Use Project

1. Add the required local project to your project. To learn more, refer to the Using local projects page.
2. Drag and drop the required block from the Containment tree to the Boundary Diagram. [ATTACHMENT filename='Block drag and drop.png']
3. Right-click the block and select Display>Display Internal Structure>Lamp in context>Lamp in context. 
 
[IMAGE alt='' src='']

The internal structure of the Lamp block is displayed in the diagram pane.

##### Creating a Boundary Diagram Item

To create a Boundary Diagram Item

1. Drag and drop the Boundary Diagram Item element in the diagram pane. [ATTACHMENT filename='Boundary diagram_Item.png']
2. In the Contain ment tre e, select the newly created Boundary Diagram Item and rename it with the help of the Specification dialog. 
 
[IMAGE alt='' src='']

##### Drawing an Anchor

To draw an Anchor

- Draw an anchor from the newly created Item Scope to the elements of interest. To learn more about drawing and configuring an Anchor, refer to the Anchor page. [ATTACHMENT filename='Scope Done.png']

##### Creating a Signal Category

To create a Signal Category

1. Create a SysML Block Definition Diagram in the Boundary Diagram package. To learn more about creating a diagram, click here .
2. Drag and drop the signals from the Lamp>Signals package in the diagram pane. [ATTACHMENT filename='Signal drag and drop.png']
3. Drag and drop the EnergyTransfer , InformationTransfer , InteractionClass , MaterialExchange, and PhysicalConnection elements from the FMA Library package in the diagram pane. [ATTACHMENT filename='FMA drag and drop.png']
4. Rearrange the elements and create Dependencies as per your requirements. To learn more about creating a Dependency, refer to the Dependency page. [ATTACHMENT filename='Dependency created.png']
5. Select and apply the TransferType[Dependency] stereotype to all the dependencies. To learn more about applying a stereotype, refer to the [CONFLUENCE_PAGE title='Stereotype' space='MED'] page.
6. On the diagram toolbar, click the [IMAGE alt='' src=''] button to change the diagram layout. To learn more about changing diagram layout, refer to the[https://docs.nomagic.com/spaces/MT/pages/9917874/Layout](https://docs.nomagic.com/spaces/MT/pages/9917874/Layout)[Layout](https://docs.nomagic.com/MT/?contextKey=layout&version=latest&variant=default)page. 
 
[IMAGE alt='' src='']

##### Working with Legends

A Legend is a model element that allows you to define the styles of diagram symbols and table rows. It helps you to visually group model elements according to specified criteria. A Legend increases the readability of the diagram and table contents by highlighting important information. To learn more, refer to the [Legends](https://docs.nomagic.com/MT/?contextKey=legends&version=latest&variant=default)page.

###### Applying a Legend

To apply a Legend

1. In the diagram toolbar. Click [IMAGE alt='' src=''] and from the drop-down menu, select Apply Legends .
2. Select the Legend(s) you want to display and click OK. [IMAGE alt='' src='']

To learn more, refer to the [Applying Legends](https://docs.nomagic.com/MT/?contextKey=applying-legends&version=latest&variant=default)page.

###### Extracting a Legend

To extract a Legend

1. In the diagram toolbar. Click [IMAGE alt='' src=''] and from the drop-down menu, select Extract Legends .
2. Select the Legend(s) you want to display and click Extract. [IMAGE alt='' src='']

To learn more, refer to the [Extracting Legends](https://docs.nomagic.com/MT/?contextKey=creating-legends-automatically&version=latest&variant=default)page.

###### Specifying Legend Item adornment

To open the adornment properties of a Legend Item

1. Open the Specification window of the Legend Item **Lamp Scope** in the **Boundary Diagram Item**. 
 
[IMAGE alt='' src='']
2. Click the specification cell of the Adornment property, and then click [IMAGE alt='' src=''] .
3. In the Adornment Properties dialog, specify the Fill Color property and click OK . [IMAGE alt='' src='']

To learn more, refer to the[Specifying Legend Item adornment](https://docs.nomagic.com/MT/?contextKey=specifying-legend-item-adornment&version=latest&variant=default).

After completing the above procedures, the Boundary Diagram is updated in the following manner.

[IMAGE alt='' src='']

###### Boundary Diagram after applying, extracting, and specifying the Legends.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p>Boundary diagram and Boundary diagram item aid in identifying and capturing in exhaustive detail about :</p><ul><li data-uuid="3085777f-da5f-4dc1-973d-903ca3366cad">The Internal sub-systems and components and external “actors”/entities</li><li data-uuid="ba0845e6-48b0-4474-bee3-7702eda1491c">The different scopes of analysis by visually outlining the system boundary.</li><li data-uuid="95efaa3d-3768-43ce-a8fd-1ea37fcddecb">The interactions with legends</li><li data-uuid="3d6286df-2e79-4ed8-8dae-bfa3b5204e5a">Missing interactions.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Boundary Diagram</h3><p>To create a Boundary Diagram </p><hr /><ol><li data-uuid="3547a66c-39c0-46e9-bdad-2077594db1f6">In the Containment tree, right-click the <strong>Boundary Diagram </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="513d755e-9e19-44b9-b639-94da05d12a34">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Boundary Diagram</strong><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword boundary and then select <strong>Boundary Diagram</strong><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram Search.png" /></ac:image><br /><br /></strong></li></ul></li></ol><p>The Boundary Diagram is now displayed in the diagram pane and in the Containment tree of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram created.png" /></ac:image></p><h3>Adding an Internal Block Diagram of a Use Project</h3><p>To add an Internal Block Diagram of a Use Project</p><hr /><ol><li data-uuid="5c7ee77a-dc84-492b-8540-ff3132c1c2f3">Add the required local project to your project. To learn more, refer to the <a href="https://docs.nomagic.com/SYSML2P/?contextKey=using-local-projects&amp;version=latest">Using local projects</a> page.</li><li data-uuid="3ddaa88e-0e0c-4a03-b3ae-616fa2d2ab63">Drag and drop the required block from the Containment tree to the Boundary Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Block drag and drop.png" /></ac:image><br /><br /></li><li data-uuid="9e0fa85a-16ad-48d6-9ea6-f49e499b79a7">Right-click the block and select <strong>Display&gt;Display Internal Structure&gt;Lamp in context&gt;Lamp in context.<br /><br /><ac:image><ri:attachment ri:filename="Lamp in contect command.png" /></ac:image><br /></strong></li></ol><p>The internal structure of the Lamp block is displayed in the diagram pane.</p><h3>Creating a Boundary Diagram Item </h3><p>To create a Boundary Diagram Item</p><hr /><ol><li data-uuid="03543445-37ff-4e90-a59b-624a09c6e688">Drag and drop the <strong>Boundary Diagram Item </strong>element in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram_Item.png" /></ac:image><br /><br /></li><li data-uuid="a3d74fef-0943-412f-ada3-170db6845425">In the Contain<ac:inline-comment-marker ac:ref="950adda0-c6ed-423c-bc12-e16093ed44a4">ment tre</ac:inline-comment-marker>e, select the newly created<ac:inline-comment-marker ac:ref="84c7744b-378c-4b37-8276-9c0a2333c911"> Boundary Diagram Item and rename it with the help of the Specification dialog.<br /><br /><ac:image><ri:attachment ri:filename="Boundary diagram_Item_Containment tree.png" /></ac:image><br /></ac:inline-comment-marker></li></ol><h3>Drawing an Anchor</h3><p>To draw an Anchor</p><hr /><ul><li data-uuid="6b602302-2aba-4775-aa51-2b8e5ed387b3">Draw an anchor from the newly created Item Scope to the elements of interest. To learn more about drawing and configuring an Anchor, refer to the<a href="https://docs.nomagic.com/MT/?contextKey=anchor&amp;version=latest&amp;variant=default"> Anchor </a>page.<br /><br /><ac:image><ri:attachment ri:filename="Scope Done.png" /></ac:image></li></ul><h3>Creating a Signal Category</h3><p>To create a Signal Category</p><hr /><ol><li data-uuid="d01f0ebe-5479-4e13-a0ea-21f8475aada5">Create a <strong>SysML Block Definition Diagram</strong> in the Boundary Diagram package. To learn more about creating a diagram, click <a href="https://docs.nomagic.com/MT/?contextKey=creating-diagrams&amp;version=latest&amp;variant=default">here</a>.</li><li data-uuid="85620cc4-4cb3-4143-956c-3fa912f3d77f">Drag and drop the signals from the <strong>Lamp&gt;Signals</strong> package in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Signal drag and drop.png" /></ac:image><br /><br /></li><li data-uuid="386c649c-dfaf-4106-9531-c656666cc711">Drag and drop the <strong>EnergyTransfer</strong>, <strong>InformationTransfer</strong>, <strong>InteractionClass</strong>, <strong>MaterialExchange, </strong>and <strong>PhysicalConnection </strong>elements from the <strong>FMA Library </strong>package in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="FMA drag and drop.png" /></ac:image><br /><br /></li><li data-uuid="d4559a7b-cd10-4e75-9040-5febdc01e6d1">Rearrange the elements and create Dependencies as per your requirements. To learn more about creating a Dependency, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=dependency&amp;version=latest&amp;variant=default">Dependency</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Dependency created.png" /></ac:image><br /><br /></li><li data-uuid="95a5f2e2-dad5-431f-8e43-3f43240476fd">Select and apply the <strong>TransferType[Dependency]</strong> stereotype to all the dependencies. To learn more about applying a stereotype, refer to the <ac:link><ri:page ri:space-key="MED" ri:content-title="Stereotype" /></ac:link> page.</li><li data-uuid="64c05ca9-2220-47d6-ac21-419c89fb73df"><span style="color:var(--ds-text,#172b4d);">On the diagram toolbar, click the<span> </span></span><span class="confluence-embedded-file-wrapper" style="color:var(--ds-text,#172b4d);"><ac:image><ri:attachment ri:filename="quick_diagram_layout.gif" /></ac:image> button to change the</span><span style="color:var(--ds-text,#172b4d);"> diagram layout. To learn more about changing diagram layout, refer to the<a href="https://docs.nomagic.com/spaces/MT/pages/9917874/Layout"> </a><a href="https://docs.nomagic.com/MT/?contextKey=layout&amp;version=latest&amp;variant=default"> Layout </a>page.<br /><br /><ac:image><ri:attachment ri:filename="diagram layout.png" /></ac:image><br /></span></li></ol><h3>Working with Legends</h3><p><span style="color:var(--ds-text,#172b4d);">A Legend is a model element that allows you to define the styles of diagram symbols and table rows. It helps you to visually group model elements according to specified criteria. A Legend increases the readability of the diagram and table contents by highlighting important information. To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=legends&amp;version=latest&amp;variant=default"> Legends </a>page.</span></p><h4>Applying a Legend</h4><p>To a<ac:inline-comment-marker ac:ref="3354d760-dae3-4493-98ee-1ff93685756d">pply a Legend</ac:inline-comment-marker></p><hr /><ol><li data-uuid="cc70408d-3f1b-4049-b60f-12cffbc05a60">In the diagram toolbar. Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="legend_button.png" /></ac:image></span> and from the drop-down menu, select<span style="letter-spacing: 0.0px;"> </span><strong style="letter-spacing: 0.0px;">Apply Legends</strong><span style="letter-spacing: 0.0px;">.</span></li><li data-uuid="a76fcb8a-13df-4027-8f47-5add73b860ed">Select the Legend(s) you want to display and click<span style="letter-spacing: 0.0px;"> </span><strong style="letter-spacing: 0.0px;">OK.</strong><span style="letter-spacing: 0.0px;"><br /><br /><ac:image><ri:attachment ri:filename="Applying Legends.png" /></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="954827ba-719b-478c-ad4a-664b0d88fed7"><ac:rich-text-body><p>To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=applying-legends&amp;version=latest&amp;variant=default">Applying Legends </a><span>page.</span></p></ac:rich-text-body></ac:structured-macro><h4>Extracting a Legend</h4><p>To extract a Legend</p><hr /><ol><li data-uuid="bd201c0f-6f9d-465f-8f12-ad86bce41f96">In the diagram toolbar. Click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="12"><ri:attachment ri:filename="legend_button.png" /></ac:image></span> and from the drop-down menu, select<span> </span><strong>Extract Legends</strong><span>.</span></li><li data-uuid="1072c44f-cb71-4638-bdb4-373ab53adc91">Select the Legend(s) you want to display and click<span> </span><strong>Extract.</strong><span><br /><br /><ac:image><ri:attachment ri:filename="Extracting Legends.png" /></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="529793d6-0c70-4c46-bd52-c484471006d9"><ac:rich-text-body><p>To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=creating-legends-automatically&amp;version=latest&amp;variant=default">Extracting Legends </a><span>page.</span></p></ac:rich-text-body></ac:structured-macro><h4>Specifying Legend Item adornment</h4><p style="text-align: left;">To open the adornment properties of a Legend Item</p><hr style="text-align: left;" /><ol style="text-align: left;"><li data-uuid="6fc9f089-631d-45c2-b223-bba4949aecc6"><p>Open the Specification window of the Legend Item <strong>Lamp Scope</strong> in the <strong>Boundary Diagram Item</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Adornment_Specification.png" /></ac:image><br /><br /></p></li><li data-uuid="b0c0b73c-66ca-44d5-ad9a-834c7d91c601">Click the specification cell of the <strong>Adornment</strong> property, and then click <span class="confluence-embedded-file-wrapper"><ac:image><ri:attachment ri:filename="edit.png" /></ac:image></span>.</li><li data-uuid="4fa49fa7-3b6a-4898-aec3-d0f9039142f8">In the Adornment Properties dialog, specify the <strong style="letter-spacing: 0.0px;">Fill Color </strong><span style="letter-spacing: 0.0px;">property and click </span><strong style="letter-spacing: 0.0px;">OK</strong><span style="letter-spacing: 0.0px;">.<br /></span><span style="letter-spacing: 0.0px;"><br /><ac:image><ri:attachment ri:filename="Adornment Properties.png" /></ac:image></span></li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="4e013f77-4514-4d5b-b058-986b643945b3"><ac:rich-text-body><p><span> To learn more, refer to the </span><a href="https://docs.nomagic.com/MT/?contextKey=specifying-legend-item-adornment&amp;version=latest&amp;variant=default">Specifying Legend Item adornment</a>.<span><br /></span></p></ac:rich-text-body></ac:structured-macro><p><span style="letter-spacing: 0.0px;">After completing the above procedures, the Boundary Diagram is updated in the following manner.<br /><br /></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Scope and Legend created.png" /></ac:image></p><h6 style="text-align: center;">Boundary Diagram after applying, extracting, and specifying the Legends.</h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249578479 space=SSE version=17 -->
## PAGE 00022: Failure Mode & Effect Analysis

- page_id: `249578479`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578479/Failure+Mode+Effect+Analysis
- version_number: 17
- version_date: `2025-11-18T10:43:07.866+01:00`
- ancestors: Systems Safety Engineer > Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

An FMEA Table allows you to analyze the reliability aspect of your model and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. The RAAML-based FMEA Table diagram is derived from an activity object and represents each FMEA Item—defined as the unique pairing of a failure mode with its corresponding cause—through a dedicated row associated with the activity.

In an FMEA Table, you can:

- Create a new FMEA Item directly in a table or add an existing one.
- Directly edit the properties of FMEA Items in a table.

The following table describes each column name, its purpose, and relevant details:

| Column Name | Description |
| --- | --- |
| Name | Displays an auto-generated counter for the FMEA item (this prefix counter is a preset customization) and a name. If the name is generated automatically (e.g., from the creation of an FMEA Item in the Robustness Checklist), it is composed of the Failure Cause and its associated Failure Mode. |
| Inputs | List of input pins of the activity element selected as the Scope of the FMEA study. This is a non-editable field. |
| Function | Activity selected as the scope of the FMEA study. This is a non-editable field. |
| Output | Lists one or more of the output pins that are declared on the activity element selected as the Scope of the FMEA study and that are being affected by a dedicated failure mode. Your selection is limited to the declared output pins on the activity referenced on the Function cell. |
| Failure Mode | Specifies the Failure Mode specific to the FMEA Item Line. Failure Mode definition is as introduced in the Parameter Diagram section, referring to the description of the specific manner in which a component, subsystem, or system could potentially fail to meet the design intent. |
| Classification | Corresponds to the categorization of FMEA items, derived from the evaluation of Severity and Occurrence values using a customizable function (preset out-of-the-box as: CC in case severity >= 9, SC in case 9 > severity >= 7, and AC in case 7 > severity >= 5). |
| Final Effect | Describes the effect of a Failure Mode on the end user or the environment (i.e., at the system-of-interest level). Multiple Final Effects can be specified for a single FMEA item. Each Final Effect can have a default Severity value assigned as its property. To assign a Severity value, open the Specification window of the Final Effect and set the desired value. |
| Computed Effect | An element describing the effect that a Failure Mode has on the system element under consideration. An FMEA Item (e.g., a single row of an FMEA Table) can have multiple Local Effects of Failure. If the element under consideration is a subsystem directly underneath the system of interest level itself, the effect of the Failure Mode is the same as the Final Effect mentioned above in this table. |
| Severity | The Severity of effects is a rating number associated with the most serious effect for a given failure mode for the operation being evaluated. It is a relative rating within the scope of the individual FMEA item and is determined without regard for occurrence or detection. Valid values range from 1 to 10 (lowest to highest severity). |
| Cause | An element (either a lower-level Failure Mode or a dedicated Cause element) indicating the design weakness that leads to a Failure Mode. An FMEA item (e.g., a single row of an FMEA table) can have one Cause of Failure. A Cause can have default Occurrence and Detectability values assigned as properties. To assign these values, either open the Specification window of the Cause and set the desired Occurrence or Detectability, or edit them directly in the corresponding columns of the FMEA table. |
| Prevention Controls | A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode. You can specify multiple Prevention controls for a single FMEA Item. The type of object that can be elected as a Prevention Control is by default preset as a Requirement. The type can be customized. |
| Occurrence | A rating number is associated with each cause for a given failure mode being evaluated. The occurrence rating considers the likelihood of occurrence during production. Valid values range from 1 to 10 (lowest to highest probability). A Cause must be identified in the dedicated cell before setting this value. Enter the value directly in the corresponding FMEA table cell or set it on the Failure Mode or Cause object via the containment tree. |
| Criticality | The product of Severity and Occurrence ratings. |
| Detection Controls | An element describing the measures implemented to detect a Failure Mode. Multiple Detection Control entries can be specified for a single FMEA item. The type of object that can be elected as a Detection Control is by default preset as a Block. The type can be customized. |
| Detection | Detection is the rating associated with the likelihood of detecting the failure mode and/or associated cause, according to defined criteria. Ability to detect is the rating number associated with the combined capabilities of all the current process controls for a given cause and/or failure mode. You should not automatically presume the detection rating is low because the occurrence rating is low. Instead, the User assumes the failure has occurred, then assesses the capabilities of all the detection-type design controls to detect low-frequency failure modes and/or causes. The detection rating is identified without regard for severity or occurrence. Valid Values range from 1 to 10 (highest to lowest detectability). |
| Risk Priority Number | The risk priority number (RPN) is the product of the severity (S), occurrence (O), and detection (D) ratings. Within the scope of the individual FMEA, this value is between “1” and “1000”. A benefit of RPN is that it provides an indicator of improvement (before and after actions taken) that reduces any one factor of severity, occurrence, or detection. It shows the distribution of RPN values for a project (Pareto), giving a high-level overview of the risk assessment. You should be aware that the final RPN ratings are subjective and relative to a particular analysis. |
| Action Priority | Assessment of the internal priority affecting the recommended actions, as per the SAEJ 1739 rating scale. |
| Recommended Action | The description of an action intended to reduce the Risk Priority Number. All critical or significant FMEA items should have associated recommended actions. These actions should focus on design improvements and be directed at mitigating the Cause of Failure or eliminating the Failure Mode. The type of object that can be elected as a Recommended Action element creation is by default preset as a Block. The type can be customized. |
| Action Taken | A property describing what actions have been taken and the results of these actions (free text capture). |
| Responsible Person | Indicates the person responsible for completing a Recommended Action. No specific object type is being preset to represent a Person. |
| Target Date | A property defining the targeted completion date of a Recommended Action. |
| Completion Date | A property assessing the completion date of a Recommended Action. |
| Revised Severity | A property assessing the seriousness of the effect(s) of a potential Failure Mode on a component, subsystem, end user, or environment after mitigation. Valid values range from 1 to 10 (lowest to highest severity). A prerequisite is that an action has been taken |
| Revised Occurrence | A property indicating the likelihood that a specific Cause of Failure will occur after mitigation. Valid values range from 1 to 10 (lowest to highest probability of occurrence). |
| Revised Criticality | The product of Revised Severity and Revised Occurrence ratings. |
| Revised Detection | A property measuring the likelihood of detecting a potential failure after mitigation. Valid values range from 1 to 10 (highest to lowest detectability). |
| Revised Risk Priority Number | The product of Revised Criticality by Revised Detection. |
| Revised Action Priority | Assessment of the internal priority affected by the recommended actions after mitigation. |

#### TIP: Tips

Tips

- While selecting an FMEA Item element (line in the table):
  - You can remove the line from the table using the dedicated Remove From Table command.
  - You can delete it from the containment tree (and the table) using the dedicated Delete command.
- If a Robustness Check List (RCL) and/or Parameter Diagram exists for the activity, the user can navigate from the FMEA Table to one of those diagrams through a dedicated panel above the diagram. To learn more, refer to the [CONFLUENCE_PAGE title='Robustness Checklist' space=''] page.

##### Creating a Failure Mode and Effect Analysis (FMEA) Table

To create a Failure Mode and Effect Analysis (FMEA) Table

1. In the Containment tree, right-click the FMEA package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Safety and Reliability Analysis**and select **RAAML-based FMEA Table.** [IMAGE alt='' src='']
  - In the search tab, type the keyword FMEA and then select RAAML-based FMEA Table. 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity dialog_FMEA.png'] The FMEA Table is now displayed in the diagram pane of the modeling tool.

##### Adding an FMEA Item to the FMEA Table

Each Failure mode linked to a Failure Effect (end user effect of a Failure Mode) or to a Failure Cause (element indicating a Design Weakness resulting in a Failure Mode) should result in a new FMEA Item. Generating FMEA Items from the design elements of your model identified earlier in the Robustness Check list diagram saves time and helps avoid mistakes.

You can add existing FMEA Items to an FMEA Table by dragging them from the Containment tree to the FMEA table. New rows are created automatically. You can modify the added items and update the property in the table.

To add a new FMEA Item to the FMEA Table

1. In the FMEA Table, click Add New. A row is added in the FMEA Table, which shows the new FMEA Item. [IMAGE alt='' src='']
2. In the newly created FMEA Item's row and the **Name**column, double-click the designated cell to name the FMEA Item.

To add an existing FMEA Item to the FMEA Table

1. In the FMEA Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the **Select FMEA Item**dialog, select the required FMEA Item and click **OK**. A row is added to the FMEA Table, which shows the existing FMEA Item. 
 
**[IMAGE alt='' src='']**
3. In the newly created FMEA Item's row and the **Name**column, double-click the designated cell to name the FMEA Item.

##### Updating a Failure Mode

To update a Failure Mode to the FMEA Table

1. Double-click the designated cell in the **Failure Mode** column and the required FMEA Item's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Failure Mode_Edit button.png']
2. From the Select Class dialog, select the required Failure Mode and click OK. [ATTACHMENT filename='Select Class dialog.png']

Similarly, you can update the Cause in the FMEA Table.

##### Adding a Final Effect

To add a Final Effect to theFMEA Table

1. Double-click the designated cell in the **Final Effect** column and the required FMEA Item's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Final Effect_Edit.png']
2. From the Select Elements dialog, select the required Failure Mode and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Elements_dialog.png']

Similarly, you can add **Computed Effects, Prevention Controls, Detection Controls,** and **Recommended Actions**in the FMEA Table.

##### Adding an Action Priority

To add an Action Priority to theFMEA Table

1. Double-click the designated cell in the **Action Priority** column and the required FMEA Item's row and click [IMAGE alt='' src=''] .
2. In the Action Priority dialog, type in the required content.

Similarly, you can add **Revised Action Priority**in the FMEA Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p>An FMEA Table allows you to analyze the reliability aspect of your model and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. <span style="color:var(--ds-text,#172b4d);">The RAAML-based FMEA Table diagram is derived from an activity object and represents each FMEA Item—defined as the unique pairing of a failure mode with its corresponding cause—through a dedicated row associated with the activity.</span></p><p>In an FMEA Table, you can:</p><ul><li data-uuid="bcada771-7e23-4bea-88dd-0d0fc2d32fa2">Create a new FMEA Item directly in a table or add an existing one.</li><li data-uuid="aa59e8a2-b620-41f7-908a-8ff10b3d3936">Directly edit the properties of FMEA Items in a table.</li></ul><p>The following table describes each column name, its purpose, and relevant details:</p><table class="wrapped"><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><td><p><strong>Column Name</strong></p></td><td><p><strong>Description</strong></p></td></tr><tr class=""><td><p>Name</p></td><td><p>Displays an auto-generated counter for the FMEA item (this prefix counter is a preset customization) and a name. If the name is generated automatically (e.g., <span style="color:var(--ds-text,#172b4d);">from the creation of an FMEA Item in the Robustness Checklist)</span>, it is composed of the Failure Cause and its associated Failure Mode.</p></td></tr><tr class=""><td><p>Inputs</p></td><td><p>List of input pins of the activity element selected as the Scope of the FMEA study. <span style="color:var(--ds-text,#172b4d);">This is a non-editable field.</span></p></td></tr><tr class=""><td><p>Function</p></td><td><p>Activity selected as the scope of the FMEA study. <span style="color:var(--ds-text,#172b4d);">This is a non-editable field.</span></p></td></tr><tr class=""><td><p>Output</p></td><td><p><span>Lists one or more of the output pins that are declared on the activity element selected as the Scope of the FMEA study and that are being affected by a dedicated failure mode. Your selection is limited to the declared output pins on the activity referenced on the Function cell.</span></p></td></tr><tr class=""><td><p>Failure Mode</p></td><td><p>Specifies the Failure Mode specific to the FMEA Item Line. Failure Mode definition is as introduced in the <strong>Parameter Diagram </strong>section, referring to the description of the specific manner in which a component, subsystem, or system could potentially fail to meet the design intent.</p></td></tr><tr class=""><td><p>Classification</p></td><td><p>Corresponds to the categorization of FMEA items, derived from the evaluation of Severity and Occurrence values using a customizable function (preset out-of-the-box as: <span style="color:var(--ds-text,#172b4d);">CC in case severity &gt;= 9, SC in case 9 &gt; severity &gt;= 7, and AC in case 7 &gt; severity &gt;= 5</span>).</p></td></tr><tr class=""><td><p>Final Effect</p></td><td><p>Describes the effect of a Failure Mode on the end user or the environment (i.e., at the system-of-interest level). Multiple Final Effects can be specified for a single FMEA item. Each Final Effect can have a default Severity value assigned as its property. <span style="color:var(--ds-text,#172b4d);">To assign a Severity value, open the Specification window of the Final Effect and set the desired value.</span></p></td></tr><tr class=""><td><p>Computed Effect</p></td><td><p>An element describing <strong>the effect</strong> that a <strong>Failure Mode</strong> has <strong>on the system element under consideration</strong>. An FMEA Item (e.g., a single row of an FMEA Table) can have multiple Local Effects of Failure. <br />If the element under consideration is a subsystem directly underneath the system of interest level itself, <strong>the effect of the Failure Mode</strong> is the same as the <strong>Final Effect</strong> mentioned above in this table.</p></td></tr><tr class=""><td><p>Severity</p></td><td><p><span>The Severity of effects is a rating number associated with the most serious effect for a given failure mode for the operation being evaluated. It is a relative rating within the scope of the individual FMEA item and is determined without regard for occurrence or detection. Valid values range from 1 to 10 (lowest to highest severity).</span></p></td></tr><tr class=""><td><p>Cause</p></td><td><p><span>An element (either a lower-level Failure Mode or a dedicated Cause element) indicating the design weakness that leads to a Failure Mode. An FMEA item (e.g., a single row of an FMEA table) can have one Cause of Failure. A Cause can have default Occurrence and Detectability values assigned as properties. To assign these values, either open the Specification window of the Cause and set the desired Occurrence or Detectability, or edit them directly in the corresponding columns of the FMEA table.</span></p></td></tr><tr class=""><td><p>Prevention Controls</p></td><td><p>A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode. You can specify multiple Prevention controls for a single FMEA Item. <span style="color:var(--ds-text,#172b4d);">The type of object that can be elected as a Prevention Control is by default preset as a Requirement. The type can be customized.</span></p></td></tr><tr class=""><td><p>Occurrence</p></td><td><p><span>A rating number is associated with each cause for a given failure mode being evaluated. The occurrence rating considers the likelihood of occurrence during production. Valid values range from 1 to 10 (lowest to highest probability). A Cause must be identified in the dedicated cell before setting this value. Enter the value directly in the corresponding FMEA table cell or set it on the Failure Mode or Cause object via the containment tree.</span></p></td></tr><tr class=""><td><p>Criticality</p></td><td><p>The product of Severity and Occurrence ratings.</p></td></tr><tr class=""><td><p>Detection Controls</p></td><td><p>An element describing the measures implemented to detect a Failure Mode. Multiple Detection Control entries can be specified for a single FMEA <span style="color:var(--ds-text,#172b4d);">item. The type of object that can be elected as a Detection Control is by default preset as a Block. The type can be customized.</span></p></td></tr><tr class=""><td><p>Detection</p></td><td><p><span>Detection is the rating associated with the likelihood of detecting the failure mode and/or associated cause, according to defined criteria. </span><span>Ability to detect is the rating number associated with the combined capabilities of all the current process controls for a given cause and/or failure mode. You should not automatically presume the detection rating is low because the occurrence rating is low. Instead, the User assumes the failure has occurred, then assesses the capabilities of all the detection-type design controls to detect low-frequency failure modes and/or causes. The detection rating is identified without regard for severity or occurrence. </span><span>Valid Values range from 1 to 10 (highest to lowest detectability).</span></p></td></tr><tr class=""><td><p>Risk Priority Number</p></td><td><p><span>The risk priority number (RPN) is the product of the severity (S), occurrence (O), and detection (D) ratings. Within the scope of the individual FMEA, this value is between “1” and “1000”. </span><span>A benefit of RPN is that it provides an indicator of improvement (before and after actions taken) that reduces any one factor of severity, occurrence, or detection. It shows the distribution of RPN values for a project (Pareto), giving a high-level overview of the risk assessment. </span><span>You should be aware that the final RPN ratings are subjective and relative to a particular analysis.</span></p></td></tr><tr class=""><td><p>Action Priority</p></td><td><p><span>Assessment of the internal priority affecting the recommended <span style="color:var(--ds-text,#172b4d);">actions, as per the SAEJ 1739 rating scale.</span></span></p></td></tr><tr class=""><td><p>Recommended Action</p></td><td><p><span style="color:var(--ds-text,#172b4d);">The description of an action intended to reduce the Risk Priority Number. All critical or significant FMEA items should have associated recommended actions. These actions should focus on design improvements and be directed at mitigating the Cause of Failure or eliminating the Failure Mode. The type of object that can be elected as a Recommended Action element creation is by default preset as a Block. The type can be customized.</span></p></td></tr><tr class=""><td><p>Action Taken</p></td><td><p>A property describing what actions have been taken and the results of these actions <span style="color:var(--ds-text,#172b4d);">(free text capture)</span>.</p></td></tr><tr class=""><td><p>Responsible Person</p></td><td><p>Indicates the person responsible for completing a Recommended Action. <span style="color:var(--ds-text,#172b4d);">No specific object type is being preset to represent a Person.</span></p></td></tr><tr class=""><td><p>Target Date</p></td><td><p>A property defining the targeted completion date of a Recommended Action.</p></td></tr><tr class=""><td><p>Completion Date</p></td><td><p>A property assessing the completion date of a Recommended Action.</p></td></tr><tr class=""><td><p>Revised Severity</p></td><td><p><span>A property assessing the seriousness of the effect(s) of a potential Failure Mode on a component, subsystem, end user, or environment after mitigation. Valid values range from 1 to 10 (lowest to highest severity). A prerequisite is that an action has been taken</span></p></td></tr><tr class=""><td><p>Revised Occurrence</p></td><td><p><span style="color:var(--ds-text,#172b4d);">A property indicating the likelihood that a specific Cause of Failure will occur after mitigation. Valid values range from 1 to 10 (lowest to highest probability of occurrence).</span></p></td></tr><tr class=""><td><p>Revised Criticality</p></td><td><p>The product of Revised Severity and Revised Occurrence ratings.</p></td></tr><tr class=""><td><p>Revised Detection</p></td><td><p><span>A property measuring the likelihood of detecting a potential failure after mitigation. Valid values range from 1 to 10 (highest to lowest detectability).</span></p></td></tr><tr class=""><td><p>Revised Risk Priority Number</p></td><td><p>The product of Revised Criticality by Revised Detection.</p></td></tr><tr class=""><td><p>Revised Action Priority</p></td><td><p><span style="color:var(--ds-text,#172b4d);">Assessment of the internal priority affected by the recommended actions after mitigation.</span></p></td></tr></tbody></table><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="355c44ea-98b8-47eb-964b-a88c170180af"><ac:parameter ac:name="title">Tips</ac:parameter><ac:rich-text-body><ul><li data-uuid="6dc08ad0-c86e-4706-a2e5-1c692046f243">While selecting an FMEA Item element (line in the table):<ul><li>You can remove the line from the table using the dedicated <strong>Remove From Table </strong><span>command.</span></li><li>You can delete it from the containment tree (and the table) using the dedicated <strong>Delete </strong><span>command.</span></li></ul></li><li data-uuid="a323ffce-cc0f-4034-9733-2c195440a163">If a Robustness Check List (RCL) and/or Parameter Diagram exists for the activity, the user can navigate from the FMEA Table to one of those diagrams through a dedicated panel above the diagram. To learn more, refer to the <span style="color:var(--ds-text,#172b4d);"><ac:link><ri:page ri:content-title="Robustness Checklist" /></ac:link> </span>page.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Failure Mode and Effect Analysis (FMEA) Table</h3><p>To create a Failure Mode and Effect Analysis (<span>FMEA) Table</span></p><hr /><ol><li data-uuid="35c8888d-77bc-4053-ba6a-fe840702910d">In the Containment tree, right-click the <strong>FMEA </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="946293a1-1c93-4661-a3fc-b76e9cf33ae4">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Safety and Reliability Analysis </strong>and select <strong>RAAML-based FMEA Table.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="FMEA_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword FMEA and then select <strong><span style="color:var(--ds-text,#333333);">RAAML-based FMEA Table</span>.<br /><br /><ac:image><ri:attachment ri:filename="FMEA_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="49d63220-7598-4a57-90fe-7d8160e7de7a">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog_FMEA.png" /></ac:image><br /><br />The FMEA Table is now displayed in the diagram pane of the modeling tool.</li></ol><h3 style="text-align: left;">Adding an FMEA Item to the <span>FMEA Table</span></h3><p>Each Failure mode linked to a Failure Effect (end user effect of a Failure Mode) or to a Failure Cause (element indicating a Design Weakness resulting in a Failure Mode) should result in a new FMEA Item. Generating FMEA Items from the design elements of your model identified earlier in the Robustness Check list diagram saves time and helps avoid mistakes.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="626fe21c-f3f6-4855-a861-577a41e59f18"><ac:rich-text-body><p>You can add existing FMEA Items to an FMEA Table by dragging them from the Containment tree to the FMEA table. New rows are created automatically. You can <span>modify the added items and update the property in the table.</span></p></ac:rich-text-body></ac:structured-macro><p>To add a new FMEA Item to the FMEA Table</p><hr /><ol><li data-uuid="e7ad82d4-332d-4d7a-836a-2c93674634d2"><span style="color:var(--ds-text,#333333);">In the FMEA Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New. </strong><span style="color:var(--ds-text,#333333);">A row is added in the FMEA Table, which shows the new FMEA Item.</span><br /><strong style="text-align: left;"><br /><ac:image><ri:attachment ri:filename="Add New.png" /></ac:image><br /><br /></strong></li><li data-uuid="01cf3e59-a5ce-48bb-b1a9-c6de4f3d757e"><span style="color:var(--ds-text,#333333);">In the newly created FMEA Item's row and the <strong>Name </strong>column, double-click the designated cell to name the FMEA Item.</span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><br /></p><p><span style="color:var(--ds-text,#333333);">To add an existing FMEA Item to the FMEA Table</span></p><hr /><ol><li data-uuid="a1de3be7-0d64-4926-ab31-2496fcd6c5a5"><span style="color:var(--ds-text,#333333);">In the FMEA Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="Add Existing.png" /></ac:image></span><br /><br /></strong></li><li data-uuid="57fd063a-272d-46b4-86e2-827d5ac8da90"><span style="color:var(--ds-text,#333333);">From the <strong>Select FMEA Item </strong>dialog, select the required FMEA Item and click <strong>OK</strong>. A row is added to the FMEA Table, which shows the existing FMEA  Item. <br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Select Activity dialog_FMEA.png" /></ac:image></strong><br /><br /></span></li><li data-uuid="c5aa1e5f-5fb5-45c1-a94e-80300938fb59"><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#333333);">In the newly created FMEA Item's row and the <strong>Name </strong>column, double-click the designated cell to name the FMEA Item.</span><br /></span></li></ol><h3 style="text-align: left;">Updating a Failure Mode</h3><p style="text-align: left;">To update a Failure Mode to the <span style="color:var(--ds-text,#333333);">FMEA Table</span></p><hr style="text-align: left;" /><ol style="text-align: left;"><li data-uuid="0a2cf8c1-9293-44ce-901b-c66a2397ea2c">Double-click the designated cell in the<span> <strong>Failure Mode </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_Edit button.png" /></ac:image><br /><br /></li><li data-uuid="4104f30c-a4b9-4d37-b7d5-0debc2c67b3d">From the<span> </span><strong>Select Class </strong>dialog, select the required Failure Mode and click <strong>OK.</strong><br /><br /><ac:image><ri:attachment ri:filename="Select Class dialog.png" /></ac:image><br /><br /></li></ol><p><span>Similarly, you can update the Cause in the FMEA Table.</span></p><h3>Adding a Final Effect</h3><p>To add a Final Effect <span style="color:var(--ds-text,#172b4d);">to the </span><span style="color:var(--ds-text,#172b4d);">FMEA Table</span></p><hr /><ol><li data-uuid="2542b7fd-c317-435f-b632-3124a0d9fa10">Double-click the designated cell in the<span> <strong>Final Effect </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Final Effect_Edit.png" /></ac:image><br /><br /></li><li data-uuid="f482c46e-680d-4477-a748-19131ef50d28">From the<span> </span><strong>Select Elements </strong>dialog, select the required Failure Mode and click <strong>OK</strong>. <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">To learn more about selecting elements, refer to the<span> </span></span><a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=latest&amp;variant=default">Selecting Elements</a><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span> </span>page.<br /></span><br /><ac:image><ri:attachment ri:filename="Select Elements_dialog.png" /></ac:image></li></ol><p>Similarly, you can add <strong>Computed Effects,  Prevention Controls, Detection Controls,</strong> and <strong>Recommended Actions </strong>in the FMEA Table.</p><h3>Adding an Action Priority</h3><p>To add an Action Priority <span style="color:var(--ds-text,#172b4d);">to the </span><span style="color:var(--ds-text,#172b4d);">FMEA Table</span></p><hr /><ol><li data-uuid="5c661554-f0ec-4115-87e3-982e2404b31b">Double-click the designated cell in the<span> <strong>Action Priority </strong></span>column and the required FMEA Item's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</li><li data-uuid="2b68566d-4a44-4e53-9bda-bddd73203ceb">In the Action Priority dialog, type in the required content.</li></ol><p>Similarly, you can add <strong>Revised Action Priority </strong>in the FMEA Table.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249578364 space=SSE version=4 -->
## PAGE 00023: Failure Mode Avoidance

- page_id: `249578364`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578364/Failure+Mode+Avoidance
- version_number: 4
- version_date: `2025-11-18T10:42:45.274+01:00`
- ancestors: Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

Quality and Safety disciplines are critical to ensure**reliable**and**safe**systems. The System Safety Engineer can perform a Design FMEA per SAE J1739:2021. Design FMEA is a type of FMEA that analyzes product design, focusing on potential design-related deficiencies to improve the design and ensure the product's safe and reliable operation during its useful life.

Based on the system architecture, the Systems Safety Engineer plugin enables:

- The creation of the Boundary Diagram and **Item** to finalize the scope (the relevant parts of the system to be analyzed).
- The creation of an item-based Interface Analysis table to study connections between functions.
- The creation of a Parameter Diagram to identify the measurable parameters that could affect the intended output of a given function.
- The creation of a Robustness Checklist to identify causality links between elements of a given function.
- The creation of a Failure Mode and Effects Analysis table

The Systems Safety Engineer is**RAAML-based**and partiallysupports **SAE J1739.**

**[IMAGE alt='' src='']**

###### Systems Safety Engineer workflow

To learn more about FMA, refer to the following pages:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p style="text-align: left;">Quality and Safety disciplines are critical to ensure<span> </span><strong>reliable</strong><span> </span>and<span> </span><strong>safe</strong><span> </span>systems. The System Safety Engineer can perform a Design FMEA per SAE J1739:2021. Design FMEA is a type of FMEA that analyzes product design, focusing on potential design-related deficiencies to improve the design and ensure the product's safe and reliable operation during its useful life.</p><p style="text-align: left;">Based on the system architecture, the Systems Safety Engineer plugin enables: </p><ul style="text-align: left;"><li data-uuid="063b53a3-485f-4940-b472-b5ece00b238e">The creation of the <strong>Boundary Diagram</strong><span> </span>and<span> <strong>Item </strong></span>to finalize the scope (the relevant parts of the system to be analyzed).</li><li data-uuid="df94e614-94f0-4a97-943e-7ec0c8723c36">The creation of an item-based<span> </span><strong>Interface Analysis</strong><span> </span>table to study connections between functions.</li><li data-uuid="46d2d7be-34c0-4c8e-83f7-cf0e594d5821">The creation of a<span> </span><strong>Parameter Diagram</strong><span> </span>to identify the measurable parameters that could affect the intended output of a given function.</li><li data-uuid="b660748e-8aeb-455c-810d-b5b7bc0f528e">The creation of a<span> </span><strong>Robustness Checklist</strong><span> </span>to identify causality links between elements of a given function.</li><li data-uuid="a5ecc256-f5bf-4d09-a6a0-c443cfbcdd8b">The creation of a<span> </span><strong>Failure Mode and Effects Analysis</strong><span> </span>table </li></ul><p style="text-align: left;">The Systems Safety Engineer is<span> </span><strong>RAAML-based</strong><span> </span>and partially<span> </span>supports <strong>SAE J1739.</strong></p><p style="text-align: center;"><strong><ac:image ac:border="true" ac:height="646" ac:width="983"><ri:attachment ri:filename="SSE_Workflow.png" /></ac:image></strong></p><h6 style="text-align: center;">Systems Safety Engineer workflow</h6><p style="text-align: left;"><br /></p><p style="text-align: left;">To learn more about FMA, refer to the following pages:</p><p style="text-align: left;"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2604d644-6c66-4c5d-9fcd-f56de98f5a3e" /></p>
````

<!--NOMAGIC_PAGE id=249578354 space=SSE version=4 -->
## PAGE 00024: Installation, licensing, and system requirements

- page_id: `249578354`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578354/Installation+licensing+and+system+requirements
- version_number: 4
- version_date: `2025-11-18T10:42:34.488+01:00`
- ancestors: Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

For information regarding installation, licensing, and system requirements, visit the[Installation, licensing, and system requirements](https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&version=latest)page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="with-breadcrumbs conf-macro output-block">For information regarding installation, licensing, and system requirements, visit the<span> </span><a href="https://docs.nomagic.com/IL/?contextKey=installation-licensing-and-system-requirements&amp;version=latest">Installation, licensing, and system requirements</a><span> </span>page.</p>
````

<!--NOMAGIC_PAGE id=249578399 space=SSE version=8 -->
## PAGE 00025: Interface Analysis

- page_id: `249578399`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578399/Interface+Analysis
- version_number: 8
- version_date: `2025-11-18T10:42:53.974+01:00`
- ancestors: Systems Safety Engineer > Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

An Interface Analysis table consists of system interfaces, their types (e.g., physical, data, energy, etc.), source/target, and related functions. An Interface Analysis table:

- Starts from any item identified in the Boundary Diagram.
- Captures the interaction between source and target elements.
- Informs the “class” of the interaction.
- Tells whether the interface involves external actors/components.
- Identifies if the interaction is beneficial or detrimental.
- Assigns explicit responsibility to each end of the interaction.
- Defines the functions involved and their “measurable” target and range of variation.

##### Creating an Interface Analysis Table

To create an Interface Analysis Table

1. In the Containment tree, right-click the **Interface** **Analysis** package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Interface Analysis****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword interface and then select **Interface Analysis** . 
 
[IMAGE alt='' src=''] The Interface Analysis Table is now displayed in the diagram pane of the modeling tool.

##### Defining the scope

To define the scope for the Interface Analysis Table

- From the Containment tree, drag and drop the Lamp Scope element on the Scope of the Interface Analysis table. [ATTACHMENT filename='Lamp Scope_drag and drop.png']

##### Adding an Interaction Connector to the Interface Analysis Table

To add an existing Interaction Connector

1. In the Interface Analysis Table, click **Add Existing. 
 
[IMAGE alt='' src='']**
2. In the Select Interaction Connector dialog, select the required Interaction Connector. 
 
[IMAGE alt='' src=''] 
 
A row is added to the Interface Analysis Table, displaying the existing Interaction Connector.

##### Adding a Functional Range

To add a Functional Range

1. Double-click the designated cell in the**Functional Range** column and the required scope element's row and click [IMAGE alt='' src=''].
2. In the Enter Range dialog, enter the Min and Max values and click **OK**. 
 
[IMAGE alt='' src='']

##### Adding a Functional Target

To add a Functional Target

1. Double-click the designated cell in the**Functional Target** column and the required scope element's row and click [IMAGE alt='' src=''].
2. In the Enter Functional Target dialog, enter the****Value and click **OK**. 
 
[IMAGE alt='' src='']

##### Assigning Strength

To assign Strength

1. Double-click the designated cell in the **Strength**column and the required scope element's row, and select the strength from the drop-down list. 
 
[IMAGE alt='' src='']

##### Adding Affected Function

To add Affected Function

1. Double-click the designated cell in the scope element's row and the Affected Function column and click [ATTACHMENT filename='Three Dot _Icon.png'] . The Select Affected Function dialog opens. [ATTACHMENT filename='Affected Function dialog.png']
2. In the Select Affected Function dialog, click the [ATTACHMENT filename='Three Dot _Icon.png'] icon, found near the Call Behavior Action Element.
3. In the Select Call Behavior Action dialog, select the Call Behavior Action and click OK. [ATTACHMENT filename='Call Behavior Action dialog.png']
4. In the Select Affected Function dialog, click the [ATTACHMENT filename='Three Dot _Icon.png'] icon, found near the Activity Element.
5. In the Select Activity dialog, select the Activity and click OK. [IMAGE alt='' src='']

##### Adding a Source/Target Interface Owner, Interface Owner Concurrence Date, and Interface Owner Activity

To add a Source/Target Interface Owner

1. Double-click the designated cell in the scope element's row and the Source Interface Owner column and type in the required details.
2. Double-click the designated cell in the scope element's row and the Target Interface Owner column and type in the required details.

Similarly, add the required details for the Source/Target Interface Owner Concurrence Date and Interface Owner Activity.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p style="text-align: left;">An Interface Analysis table consists of system interfaces, their types (e.g., physical, data, energy, etc.), source/target, and related functions. An Interface Analysis table:</p><ul style="text-align: left;"><li data-uuid="52217361-d5da-4dda-87b4-a46da0933df3">Starts from any item identified in the Boundary Diagram.</li><li data-uuid="56991033-a84f-469c-9f20-62431475e121">Captures the interaction between source and target elements.</li><li data-uuid="f57dd2a2-c065-4fc4-a642-3d6cc0c8c146">Informs the “class” of the interaction.</li><li data-uuid="f958a193-e77f-44ad-ba9a-62970de7ad2b">Tells whether the interface involves external actors/components.</li><li data-uuid="7977e60e-17da-4f2d-b3be-c28d3abf5849">Identifies if the interaction is beneficial or detrimental.</li><li data-uuid="dc995ceb-7e10-4fbc-b612-042fd75e143e">Assigns explicit responsibility to each end of the interaction.</li><li data-uuid="1211dab6-f46d-4485-a93d-db7f59127fe5">Defines the functions involved and their “measurable” target and range of variation.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating an Interface Analysis Table</h3><p>To create an <span>Interface Analysis Table</span></p><hr /><ol><li data-uuid="39362494-d719-4f02-8a50-ee4590d531d4">In the Containment tree, right-click the <span><strong>Interface</strong> <strong>Analysis </strong></span>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="7de72549-c91d-4c5d-9dec-ebca2efb1500">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <span><strong>Interface Analysis</strong></span><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Interface Analysis_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword interface and then select <span style="color:var(--ds-text,#333333);"><span><strong>Interface Analysis</strong></span></span><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Interface Analysis_Search.png" /></ac:image><br /><br /></strong>The <span style="color:var(--ds-text,#333333);">Interface </span><span style="color:var(--ds-text,#333333);">Analysis Table </span><span>is now displayed in the diagram pane of the modeling tool.</span></li></ul></li></ol><h3>Defining the scope</h3><p>To define the scope for the Interface Analysis Table </p><hr /><ul><li data-uuid="b83b8c21-31f0-4fd6-8961-f41db919a507">From the Containment tree, drag and drop the <strong>Lamp Scope </strong>element on the<strong> Scope </strong>of the Interface Analysis table.<br /><br /><ac:image><ri:attachment ri:filename="Lamp Scope_drag and drop.png" /></ac:image></li></ul><h3 style="text-align: left;">Adding an Interaction Connector to the <span>Interface Analysis Table</span></h3><p><span>To add an existing Interaction Connector</span></p><hr /><ol><li data-uuid="89cd3896-12cc-4745-bd61-fd66b25168e4"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Interface <ac:inline-comment-marker ac:ref="97cddb50-b898-41ac-a21e-39bc461109a2">Analysis Table</ac:inline-comment-marker>, click <strong style="text-align: left;"><ac:inline-comment-marker ac:ref="d8c254f3-4fe4-4660-ac9a-de2286ac4a54">Add Existing.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Add Existing.png" /></ac:image><br /><br /></strong></span></li><li data-uuid="ac17b159-822a-46bd-953f-1038fa52db8f"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Select Interaction Connector <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">dialog, select the required Interaction Connector.<br /><br /><ac:image><ri:attachment ri:filename="Select Interaction Connector dialog.png" /></ac:image><br /><br />A row is added to the Interface Analysis Table, displaying the existing <span>Interaction Connector</span>.<br /></span></span></li></ol><h3>Adding a Functional Range</h3><p>To add a Functional Range</p><hr /><ol><li data-uuid="94d1f86d-6a6d-4c3c-8235-eac52692072f"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the<span> </span><strong>Functional Range</strong> </span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">column and the required scope element's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.</span></span></li><li data-uuid="39a510c8-3932-469e-8982-e6462c13a708"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span>In the Enter Range dialog, enter the Min and Max values and click <strong>OK</strong>.<br /><br /><ac:image ac:border="true" ac:height="105" ac:width="249"><ri:attachment ri:filename="Functional Range dialog.png" /></ac:image><br /></span></span></li></ol><h3>Adding a Functional Target</h3><p>To add a Functional Target</p><hr /><ol><li data-uuid="7f19c8ea-bef1-426f-a449-cc6e15699001"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the<span> </span><strong>Functional Target </strong></span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">column and the required scope element's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.</span></span></li><li data-uuid="5db8be0f-102f-45fc-bc17-d278e3aded1b"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span>In the Enter Functional Target dialog, enter the<strong> </strong>Value and click <strong>OK</strong>.<br /><br /><ac:image ac:border="true" ac:height="103" ac:width="226"><ri:attachment ri:filename="Functional Target dialog.png" /></ac:image><br /></span></span></li></ol><h3>Assigning Strength</h3><p><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">To assign Strength</span></p><hr /><ol><li data-uuid="93e08759-3115-4e8d-9aa5-5660a14c50ba"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">Double-click the designated cell in the <strong>Strength </strong>column and the required scope element's row, and select the strength from the drop-down list.<br /><br /><ac:image><ri:attachment ri:filename="Strenth drop-down.png" /></ac:image><br /></span></li></ol><h3><span>Adding Affected Function</span></h3><p><span>To add Affected Function</span></p><hr /><ol><li data-uuid="46f4eca3-2eeb-4caa-b0a1-8b62c16d130f">Double-click the designated cell in the scope element's row and the Affected Function column and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>. The Select Affected Function dialog opens.<br /><br /><ac:image ac:border="true" ac:height="163" ac:width="354"><ri:attachment ri:filename="Affected Function dialog.png" /></ac:image><br /><br /></li><li data-uuid="dfa1db28-1ec2-4fc4-b661-6329c53c33be">In the Select Affected Function dialog, click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image> icon, found near the Call Behavior Action Element.</li><li data-uuid="ca4a35c1-0032-412f-9f32-32b48e54ae66">In the Select Call Behavior Action dialog, select the Call Behavior Action and click OK.<br /><br /><ac:image ac:border="true" ac:height="410" ac:width="533"><ri:attachment ri:filename="Call Behavior Action dialog.png" /></ac:image><br /><br /></li><li data-uuid="7286495b-99a4-49b1-ab8a-244eababa7fd">In the Select Affected Function dialog, click the <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image> icon, found near the Activity Element.</li><li data-uuid="e4645f88-b602-4fe3-ba86-f7a36510b49e">In the Select Activity dialog, select the Activity and click OK.<br /><span><br /><ac:image ac:border="true" ac:height="382" ac:width="531"><ri:attachment ri:filename="Select Activity dialog.png" /></ac:image><br /></span></li></ol><h3>Adding a Source/Target Interface Owner, Interface Owner Concurrence Date, and Interface Owner Activity</h3><p>To add a Source/Target Interface Owner</p><hr /><ol><li data-uuid="bec27aff-a909-4417-b4ac-e901c8406ab8">Double-click the designated cell in the scope element's row and the<strong> Source Interface Owner </strong>column and type in the required details.</li><li data-uuid="49f4f2a7-b598-45ae-a1e6-e1e60c81be49">Double-click the designated cell in the scope element's row and the <strong>Target Interface Owner </strong>column and type in the required details.</li></ol><p>Similarly, add the required details for the <span>Source/Target Interface Owner Concurrence Date and Interface Owner Activity.</span></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249578351 space=SSE version=3 -->
## PAGE 00026: Introduction to Systems Safety Engineer

- page_id: `249578351`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578351/Introduction+to+Systems+Safety+Engineer
- version_number: 3
- version_date: `2025-09-12T11:40:30.555+02:00`
- ancestors: Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

**Model-based safety** refers to a systematic approach to ensure the safety of complex systems by using formal models that represent the system’s structure, behavior, and environment. These models are used to analyze, predict, and verify safety properties before and during the system’s operation. Model-based safety engineering also aims to :

- Identify safety risks early , perform safety verification and validation , and guide the design of safety mechanisms.
- Help detect unsafe states or behaviors before physical implementation or deployment , reducing costly errors.
- Unify domains into one analysis framework, as safety issues may arise from software bugs, hardware faults, cyber-attacks, or their combination.
- Provide traceable, repeatable proofs of safety requirements to ease regulatory compliance and certification
- Enables the use of automated model checking and simulation tools that can exhaustively explore possible scenarios .

The Systems Safety Engineering plugin contains the ISO 26262 plugin. To learn more, refer to the [ISO 26262 plugin](https://docs.nomagic.com/CSRA/?contextKey=iso-26262-functional-safety&version=latest) user guide.

#### NOTE: Prerequisites

Prerequisites

To install and use the Systems Safety Designer, ensure that one of the following modeling tools is installed:

- Magic Cyber Systems Engineer
- Magic Cyber Systems of Systems Architect
- Cameo Systems Modeler - Architect Edition
- Cameo Systems Modeler - Enterprise Edition
- Cameo Enterprise Architecture
- Magic Draw (any version) with SysML plugin installed

To learn more about how to download the installation files, refer to [Downloading installation files](https://docs.nomagic.com/IL/?contextKey=downloading-installation-files&version=latest).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong>Model-based safety</strong> refers to a systematic approach to ensure the safety of complex systems by using formal models that represent the system’s structure, behavior, and environment. These models are used to analyze, predict, and verify safety properties before and during the system’s operation. Model-based safety engineering also aims to :</p><ul><li data-uuid="151084d2-589a-49ae-90fc-0a1300fd4e74"><strong>Identify safety risks early</strong>, perform <strong>safety verification and validation</strong>, and guide the design of safety mechanisms.</li><li data-uuid="c9c4db51-4534-4d29-876e-2a6b3f45ccc9">Help detect unsafe states or behaviors <strong>before physical implementation or deployment</strong>, reducing costly errors.</li><li data-uuid="69d2ebba-63b2-428e-8d52-dcdf7af979c2">Unify domains into one analysis framework, as safety issues may arise from software bugs, hardware faults, cyber-attacks, or their combination.</li><li data-uuid="045a44ee-ba3e-4791-a440-b36774af581c">Provide traceable, repeatable proofs of safety requirements to ease regulatory compliance and certification</li><li data-uuid="83cd63c7-58f4-4412-9ec3-cd8ffb06e4a4">Enables the use of automated model checking and simulation tools that can exhaustively explore possible scenarios<ac:inline-comment-marker ac:ref="b862b50b-d6d3-475f-a880-b127214b6211">.</ac:inline-comment-marker></li></ul><p>The Systems Safety Engineering plugin contains the ISO 26262 plugin. To learn more, refer to the <a href="https://docs.nomagic.com/CSRA/?contextKey=iso-26262-functional-safety&amp;version=latest">ISO 26262 plugin</a> user guide.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6f459f96-4d19-47a8-8187-d08bea2c157e"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">To install and use the Systems Safety Designer, ensure that one of the following modeling tools is installed:</span></p><ul><li data-uuid="5ebb08d5-10cc-46ca-9e49-452622525e38"><p>Magic Cyber Systems Engineer</p></li><li data-uuid="5cfec0e3-e6d2-43c6-9613-2b89f1358904"><p>Magic Cyber Systems of Systems Architect</p></li><li data-uuid="76e1c66e-ba4d-4d18-a2ee-1a7881aa1fec"><p>Cameo Systems Modeler - Architect Edition</p></li><li data-uuid="f1569cc9-99d7-4240-8052-3e011dee6936"><p>Cameo Systems Modeler - Enterprise Edition</p></li><li data-uuid="af8a0cd7-8238-4b27-b35f-207bdcd91045"><p>Cameo Enterprise Architecture</p></li><li data-uuid="fdae7457-7c07-4075-b5c5-7b5fe32f3acc"><span style="color:var(--ds-text,#333333);">Magic Draw (any version) with SysML plugin installed</span></li></ul><p>To learn more about how to download the installation files, refer to <a href="https://docs.nomagic.com/IL/?contextKey=downloading-installation-files&amp;version=latest">Downloading installation files</a>.</p></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249578411 space=SSE version=9 -->
## PAGE 00027: Parameter Diagram

- page_id: `249578411`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578411/Parameter+Diagram
- version_number: 9
- version_date: `2025-11-18T10:42:57.684+01:00`
- ancestors: Systems Safety Engineer > Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

| Concepts | Description |
| --- | --- |
| Failure Mode | A Failure Mode represents a Specific way in which a component, subsystem, or system can fail to perform its intended function. It describes how the failure happens, i.e., the manner or mechanism of failure, not the cause or the consequence directly, but the mode or form the failure takes. |
| Failure Effect | An element describing the effect that a Failure Mode has on the system element under consideration (user, system, subsystem) |
| Noise Factors | Noise factors are sources of uncontrollable variability in a system. These are typically outside the direct control of the designer and introduce disturbances that may affect performance or reliability. The following are the types of Noise Factors that can be created. |
| Piece-to-Piece Variation Noise Factor | Piece-to-Piece Variation is a noise factor referring to variability between different units or parts of the same product. It can include:Manufacturing tolerances (dimension, weight, resistance, etc.)Material variability or changes in suppliersTool wear or production environment conditionsBatch-to-batch differences (also referenced as lot-to-lot variation) in production |
| Change Over Time Noise Factor | Change Over Time refers to system or component variations that occur gradually or incrementally during the lifetime of a product, often due to aging, fatigue, wear, drift, or environmental exposure. |
| Customer Usage Noise Factor | A Customer Usage Noise Factor is a type of uncontrollable variation stemming from how different users interact with the product in real-life scenarios, including misuse within plausible limits, erratic behavior, or varying usage environments. |
| System Interaction Noise Factor | A System Interaction Noise Factor is a disturbance or variability introduced by another system, component, or module, which is outside the local design scope, but interacts through a shared interface, environment, or resource.They are often not visible in unit testing but appear in integration testing.They may stem from electrical, mechanical, software, or communication interfaces.They are uncontrolled from the perspective of the system under analysis. |
| External Environment Noise Factor | An External Environment Noise Factor is a type of variability introduced by the physical, chemical, or climatic conditions in the system’s operating environment that may affect its behavior, functionality, or lifetime. |
| Control Factor | A Control factor is a design parameter or setting that you can actively choose, design, or adjust to achieve the desired system behavior, despite the presence of noise or variation. |
| Unintended output | An unintended output is any system response, signal, or command that is not expected, not commanded, or not aligned with the intended function, whether due to a failure, error, or disturbance. It should be selected among the type "activity pins" (i.e., object "parameters" and its derivative). |

##### Creating a Parameter Diagram

To create a Parameter Diagram

1. In the Containment tree, right-click Parameter Diagram package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Parameter Diagram****.** [IMAGE alt='' src='']
  - In the search tab, type the keyword parameter and then select Parameter Diagram . 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity dialog.png'] The Parameter Diagram is now displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='Parameter diagram.png']

##### Creating a Failure Mode or Effect

To create a Failure Mode or Effect

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  - In the dialog, expand RAAML and select Failure Mode or Effect. 
 
[IMAGE alt='' src='']
  - In the search tab, type the keyword failure or effect, and then select Failure Mode or Effect. 
 
[IMAGE alt='' src='']
3. Name the newly created Failure Mode or Failure Effect in the Containment tree. An automated number is added with a **Counter** that is automatically added once validated.

##### Adding a Failure Mode or Effect in the Parameter Diagram

To add a Failure Mode or Effect in the Parameter Diagram

1. In the Parameter Diagram, select the Failure Mode or Failure Effect cell and cl ick[IMAGE alt='' src=''].
2. In the Select Elements dialog, select the required failure modes or failure effects and click **OK**. To learn more about selecting elements, refer to the [Selecting Elements](https://docs.nomagic.com/MT/?contextKey=selecting-elements&version=latest&variant=default) page. 
 
[IMAGE alt='' src='']

##### Creating a Noise Factor

To create a Noise Factor from the containment tree

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  - In the dialog, expand Failure Mode Avoidance and select the required type of Noise Factor. [IMAGE alt='' src='']
  - In the search tab, type the required keyword and then select the required type of Noise Factor . [ATTACHMENT filename='Piece to Piece Variation_search.png'] Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.
3. Name the newly created Piece-to-Piece Variation Noise Factor in the Containment tree.

##### Adding a Noise Factor

To add a Noise Factor in the Parameter Diagram

1. In the Parameter Diagram, select the corresponding Noise Factor cell (i.e., Piece to Piece Variation, Change Over Time, Customer Usage, System Interaction, or External Environment ), and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. In the Select Elements dialog, select the required Noise Factor and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Activity dialog_Noise Factor addition.png'] You can create any type of Noise Factor in the Select Elements dialog. To learn more, refer to the [Creating new elements](https://docs.nomagic.com/MT/?contextKey=creating-new-elements&version=latest&variant=default)page.Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.

##### Creating Control Factor or Unintended Output

To create a Control Factor or Unintended Output from the containment tree

1. In the Containment tree, right-click the Parameter Diagram package and select Create Element.
2. Do one of the following:
  1. In the dialog, expand General and select Requirement. 
 
[IMAGE alt='' src='']
  2. In the search tab, type the keyword "requirement" and then select Requirement. 
 
[IMAGE alt='' src='']
3. Name the newly created Requirement in the Containment tree. An automated number is added with a **Counter** that is automatically added once validated.

##### Adding a Control Factor, Unintended Output, or Failure Mode of Unintended Output

To add a Control Factor or Unintended Output in the Parameter Diagram

1. In the Parameter Diagram, select the corresponding cell for Control Factor, Unintended Output, or Failure Mode of Unintended Output and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. In the Select Elements dialog, select the required Control Factor or Unintended Output, or Failure Mode of Unintended Output, and click OK . To learn more about selecting elements, refer to the Selecting Elements page. [ATTACHMENT filename='Select Elements_Control Factor or Unintended Output.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th>Concepts</th><th>Description</th></tr><tr><td><strong>Failure Mode</strong></td><td>A Failure Mode represents a Specific way in which a component, subsystem, or system can fail to perform its intended function. It describes <strong>how</strong> the failure happens, i.e., the manner or mechanism of failure, not the cause or the consequence directly, but the mode or form the failure takes.</td></tr><tr><td><strong><span>Failure Effect</span></strong></td><td><span><span style="color:var(--ds-text,#172b4d);">An element describing </span><strong style="text-align: left;">the effect</strong><span style="color:var(--ds-text,#172b4d);"> that a </span><strong style="text-align: left;">Failure Mode</strong><span style="color:var(--ds-text,#172b4d);"> has </span><strong style="text-align: left;">on the system element under consideration (</strong><span style="color:var(--ds-text,#172b4d);">user, system, subsystem)</span></span></td></tr><tr><td><strong>Noise Factors</strong></td><td>Noise factors are sources of uncontrollable variability in a system. These are typically outside the direct control of the designer and introduce disturbances that may affect performance or reliability. The following are the types of Noise Factors that can be created.</td></tr><tr><td><strong>Piece-to-Piece Variation </strong><strong>Noise Factor</strong></td><td><p>Piece-to-Piece Variation is a noise factor referring to variability between different units or parts of the same product. It can include:</p><ul><li data-uuid="45d53b73-45e9-4759-9eee-60375f1ab59a">Manufacturing tolerances (dimension, weight, resistance, etc.)</li><li data-uuid="8e07dfc9-0b1a-40e2-b34f-8a8826a5052a">Material variability or changes in suppliers</li><li data-uuid="d56c1e58-8fd2-4b12-b3e2-9a8baff69c8b">Tool wear or production environment conditions</li><li data-uuid="79ac5502-dcc3-4344-9ec0-9b57bbc7802f">Batch-to-batch differences (also referenced as lot-to-lot variation) in production</li></ul></td></tr><tr><td><strong>Change Over Time Noise Factor</strong></td><td>Change Over Time refers to system or component variations that occur gradually or incrementally during the lifetime of a product, often due to aging, fatigue, wear, drift, or environmental exposure.</td></tr><tr><td><strong>Customer Usage Noise Factor</strong></td><td><span>A </span><span>Customer Usage Noise Factor</span><span> is a type of </span><span>uncontrollable variation</span><span> stemming from how </span><span>different users</span><span> interact with the product in </span><span>real-life scenarios</span><span>, including </span><span>misuse within plausible limits</span><span>, </span><span>erratic behavior</span><span>, or </span><span>varying usage environments</span><span>.</span></td></tr><tr><td><strong>System Interaction Noise Factor</strong></td><td><p>A System Interaction Noise Factor is a disturbance or variability introduced by another system, component, or module, which is outside the local design scope, but interacts through a shared interface, environment, or resource.</p><ul><li data-uuid="efc14096-f0e3-49ad-ad99-fa28e1858de7">They are often not visible in unit testing but appear in integration testing.</li><li data-uuid="4a5ed891-db93-44a6-980e-d41d1afffe60">They may stem from electrical, mechanical, software, or communication interfaces.</li><li data-uuid="74c12ac5-1882-44a6-b2bb-4289b4f259e7">They are uncontrolled from the perspective of the system under analysis.</li></ul></td></tr><tr><td><strong>External Environment Noise Factor</strong></td><td>An External Environment Noise Factor is a type of variability introduced by the physical, chemical, or climatic conditions in the system’s operating environment that may affect its behavior, functionality, or lifetime.</td></tr><tr><td><strong>Control Factor</strong></td><td>A Control factor is a design parameter or setting that you can actively choose, design, or adjust to achieve the desired system behavior, despite the presence of noise or variation.</td></tr><tr><td><strong><span>Unintended output</span></strong></td><td><span style="color:var(--ds-text,#172b4d);">An </span><span style="color:var(--ds-text,#172b4d);">unintended output</span><span style="color:var(--ds-text,#172b4d);"> is any system response, signal, or command that is </span><span style="color:var(--ds-text,#172b4d);">not expected</span><span style="color:var(--ds-text,#172b4d);">, </span><span style="color:var(--ds-text,#172b4d);">not commanded</span><span style="color:var(--ds-text,#172b4d);">, or </span><span style="color:var(--ds-text,#172b4d);">not aligned with the intended function,</span><span style="color:var(--ds-text,#172b4d);"> whether due to a failure, error, or disturbance. It should be selected among the type &quot;activity pins&quot; (i.e., object &quot;parameters&quot; and its derivative). </span></td></tr></tbody></table></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Parameter Diagram</h3><p>To create a Parameter Diagram </p><hr /><ol><li data-uuid="dbe06a17-67f5-4968-9595-84f52eb78e67">In the Containment tree, right-click <strong>Parameter Diagram </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="3685c10d-64e6-47a9-8466-8087547d61cd">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Parameter Diagram</strong><strong>.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Parameter diagram_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword parameter and then select <strong>Parameter Diagram</strong><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Parameter diagram_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="d961e2e9-472f-427a-bb0f-f3007bd0373a">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog.png" /></ac:image><br /><br />The Parameter Diagram is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image ac:border="true" ac:height="510" ac:width="1065"><ri:attachment ri:filename="Parameter diagram.png" /></ac:image></li></ol><h3><span style="color:var(--ds-text,#172b4d);">Creating a Failure Mode or Effect</span></h3><p>To create a Failure Mode or Effect</p><hr /><ol><li data-uuid="1721bc3d-9dc8-43ba-add0-b1ab2ddcdc85">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="c8eeb92d-dd2f-46e6-915c-5ddc0713548e">Do one of the following:<br /><ul><li>In the dialog, expand <strong>RAAML </strong>and select <strong>Failure Mode </strong>or <strong>Effect.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_select.png" /></ac:image><br /><br /></strong></li><li>In the search tab, type the keyword failure or effect, and then select <strong>Failure Mode </strong>or <strong>Effect.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_search.png" /></ac:image><br /><br /></strong></li></ul></li><li data-uuid="7c21892f-9237-419c-b496-c167e592c6be"><span style="color:var(--ds-text,#172b4d);">Name the newly created Failure Mode or Failure Effect in the Containment tree.</span><br /><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3d915e30-1796-4499-b98b-66fb6e771a7d"><ac:rich-text-body><p>An automated number is added with a <strong>Counter</strong> that is automatically added once validated.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3><span style="color:var(--ds-text,#172b4d);">Adding a Failure Mode or Effect in the Parameter Diagram</span></h3><p>To add a Failure Mode or Effect in the Parameter Diagram</p><hr /><ol><li data-uuid="d0ea622d-64ec-4806-a05a-f7fc4ce85074">In the Parameter Diagram, select the Failure Mode or Failure Effect cell and <span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">cl</span><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">ick<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text-accent-magenta-bolder,#50253f);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.</span></li><li data-uuid="90424724-5225-48e2-b816-cdf0250b7dba"><span style="color:var(--ds-text-accent-magenta-bolder,#50253f);">In the Select Elements dialog, select the required failure modes or failure effects and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=latest&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog.png" /></ac:image><br /></span></li></ol><h3>Creating a <span>Noise Factor</span></h3><p>To create a Noise Factor from the containment tree</p><hr /><ol><li data-uuid="7e644063-f402-4f2f-9f29-c5d7f28045fc">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="6e9aaef9-ffa3-4262-adc2-c4d9e90e74bd">Do one of the following:<br /><ul><li>In the dialog, expand <strong>Failure Mode Avoidance </strong>and select the required type of Noise Factor.<strong><br /><br /><ac:image><ri:attachment ri:filename="Piece to Piece Variation_select.png" /></ac:image><br /><br /></strong></li><li>In the search tab, type the required keyword and then select the required type of Noise Factor<strong>.<br /></strong><br /><ac:image><ri:attachment ri:filename="Piece to Piece Variation_search.png" /></ac:image><br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="04bf90ca-1ca8-4a7e-9ade-30b78249ba4b"><ac:rich-text-body><p>Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.</p></ac:rich-text-body></ac:structured-macro></li></ul></li><li data-uuid="fcd957b2-48b9-4c0e-a061-23ae3d26406b"><span style="color:var(--ds-text,#172b4d);">Name the newly created Piece-to-Piece Variation Noise Factor in the Containment tree.</span></li></ol><h3>Adding a Noise Factor</h3><p>To add a Noise Factor in the Parameter Diagram</p><hr /><ol><li data-uuid="af64a9b1-5c71-4e34-b4e6-768dc948ce85">In the Parameter Diagram, select the corresponding Noise Factor cell (i.e., <strong>Piece to Piece Variation, Change Over Time, Customer Usage, System Interaction, </strong>or<strong> External Environment</strong>),<strong> </strong>and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>.</li><li data-uuid="d09e8bf0-f64c-47f4-8b50-4fdfcdcd184d">In the Select Elements dialog, select the required Noise Factor and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=latest&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity dialog_Noise Factor addition.png" /></ac:image><br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="4a74c2e1-4677-437e-804a-06824d20908d"><ac:rich-text-body><ul><li>You can create any type of Noise Factor in the Select Elements dialog. To learn more, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=creating-new-elements&amp;version=latest&amp;variant=default">Creating new elements</a><span> page.</span></li><li>Optional: You can also enter a range describing the boundaries in an existing Unit of measure for the Variation, or else cancel the range definition.</li></ul></ac:rich-text-body></ac:structured-macro></li></ol><h3>Creating Control Factor or Unintended Output</h3><p>To create a Control Factor or Unintended Output from the containment tree</p><hr /><ol><li data-uuid="e6db19f3-b399-4125-9e1b-282a6109b8a8">In the Containment tree, right-click the <strong>Parameter Diagram </strong>package and select<strong> Create Element.</strong></li><li data-uuid="09acf9ab-2852-4a0f-8355-172958cec6db">Do one of the following:<ol><li>In the dialog, expand <strong>General </strong><span>and select </span><strong>Requirement.<br /><br /><ac:image><ri:attachment ri:filename="Requirement_select.png" /></ac:image><br /><br /></strong></li><li>In the search tab, type the keyword &quot;requirement&quot; and then select <strong>Requirement.<br /><br /><ac:image ac:thumbnail="true" ac:height="170"><ri:attachment ri:filename="Requirement_search.png" /></ac:image><br /><br /></strong></li></ol></li><li data-uuid="5c74b968-ba79-46f5-be09-d6562fc66dfa"><span style="color:var(--ds-text,#172b4d);">Name the newly created Requirement in the Containment tree.<br /></span><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cf339c00-03ea-4f63-ae24-80251e57fa31"><ac:rich-text-body><p>An automated number is added with a <strong>Counter</strong> that is automatically added once validated.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3>Adding a Control Factor, Unintended Output, or Failure Mode of Unintended Output</h3><p>To add a Control Factor or Unintended Output in the Parameter Diagram</p><hr /><ol><li data-uuid="781ecf57-8603-4d35-ab8a-2c04dbf5bba9">In the Parameter Diagram, select the corresponding cell for Control Factor, Unintended Output, or Failure Mode of Unintended Output and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>.</li><li data-uuid="70fdbe5d-8106-4e32-bfde-e8aa4223361c">In the Select Elements dialog, select the required Control Factor or Unintended Output, or Failure Mode of Unintended Output, and click <strong>OK</strong>. To learn more about selecting elements, refer to the <a href="https://docs.nomagic.com/MT/?contextKey=selecting-elements&amp;version=latest&amp;variant=default">Selecting Elements</a> page.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements_Control Factor or Unintended Output.png" /></ac:image></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249578446 space=SSE version=12 -->
## PAGE 00028: Robustness Checklist

- page_id: `249578446`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578446/Robustness+Checklist
- version_number: 12
- version_date: `2025-11-18T10:43:04.057+01:00`
- ancestors: Systems Safety Engineer > Failure Mode Avoidance
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

For a specific function/activity, a Robustness Check List allows verifying that prevention controls (design methods) and detection controls (test methods) are adequate given the impact of failure modes/failure effects to be covered and the range of variation of noise factors that cause these failure modes/failure effects to arise.

The rows and columns of the Robustness Check List display the noise factors with their associated ranges of variation, the failure causes, the failure modes, the failure effects, the prevention controls, the detection controls, and the recommended actions associated with the function/activity for which the RCL is established. All these elements could come from the function/activity Parameter Diagram, except the failure causes, which are introduced manually in the Robustness Check List.

**EssentialInformation:**

- The robustness checklist diagram is created based on an activity object.
- All relationships in the Robustness Checklist can be deleted by right-clicking the cell and selecting the corresponding delete command. It can also be deleted from the model itself by pressing the Delete key on the Keyboard.
- The Parameter diagram and the FMEA table also show all existing relationships.
- If a Parameter Diagram and/or an FMEA table exist for the activity, you can navigate from the Robustness Checklist with the help of the commands present in the toolbar. The following table displays the icons and functions of the commands: IconDescription[IMAGE alt='' src='']Opens the Function in the Parameter Diagram[IMAGE alt='' src='']Opens the Function in the RAAML-based FMEA Table

The Robustness Checklist is a Dependency Matrix. To learn more, refer to the [Dependency Matrix](https://docs.nomagic.com/MT/?contextKey=dependency-matrix&version=latest&variant=default)page.

##### Creating a Robustness Checklist

To create a Robustness Checklist

1. In the Containment tree, right-click the Robustness Checklist package and select Create Diagram.
2. Do one of the following:
  - In the dialog, expand **Failure Mode Avoidance**and select **Robustness Checklist.** [IMAGE alt='' src='']
  - In the search tab, type the keyword robust and then select Robustness Checklist. 
 
[IMAGE alt='' src='']
3. In the Select Activity dialog, select the required Activity and click OK . [ATTACHMENT filename='Select Activity.png'] The Robustness Checklist is now displayed in the diagram pane of the modeling tool. You must focus on identifying relationships with the aid of the white cells, as the grey cells are not editable. [ATTACHMENT filename='Robustness_Checklist.png']

##### Adding an element to the Robustness Checklist

To add an element to the Robustness Checklist

1. In the containment Tree, select the element to be added.
2. Drag and drop the element on the Column corresponding to the element folder and refresh the diagram. [ATTACHMENT filename='Adding element.png']

##### Deleting elements from the Robustness Checklist

To delete elements from the Robustness Checklist

1. In the Robustness Checklist, select the element to be deleted.
2. Right-click and select Remove from the Matrix from the Contextual menu. [ATTACHMENT filename='Delete Element.png']

You can completely delete the element by pressing the Delete button on the Keyboard.

##### Creating a range for the Noise Factor

With the Robustness checklist, you can enter a range describing the boundaries in an existing Unit of measure for the variation of the Noise Factor.

To create a range for the Noise Factor

1. Select the cell corresponding to the targeted Noise Factor and the first column Range.
2. Right-click and select Define Range from the Contextual menu. [ATTACHMENT filename='Define Range Command.png']
3. In the Define Range dialog, insert the required Min value, Max value, and define the Unit. [IMAGE alt='' src='']
4. C lick OK.

##### Creating Design Limits for the Activity

To create a Design Limit for the Activity

1. Select the cell corresponding to the targeted Noise Factor and the second column, Design Limits .
2. Right-click and select Design Limits from the Contextual menu. [ATTACHMENT filename='Desgin Limit command.png']
3. In the Define Range dialog, insert the required Min value, Max value, and define the Unit. [ATTACHMENT filename='Define Range dialog_Desgin Limit.png']
4. C lick OK.

##### Defining coverage for Prevention or Detection Controls

Design methods and test methods may cover a fraction of the range of a noise factor or more than the range of the noise factor. The end user can capture the range of the coverage when a prevention control or detection control is associated to a noise factor using a contextual menu item **Define coverage**. A dialog allows capturing a minimal value and a maximal value covered by the control, with the same unit as the covered noise factor. The covered range is persisted in the prevention or detection dependency, allowing controls to be enriched without modifying them directly.

The formula to compute the percentage of coverage follows the following rule: if the full range of the noise factor is not covered, the fraction that is covered is computed and the ratio to the full range of the noise factor is displayed; otherwise, the percentage of coverage is the ratio between the control range and the noise factor range.

To Define Coverage

1. Select the cell corresponding to the targeted controls to be defined.
2. Right-click and select Define Coverage from the Contextual menu. [ATTACHMENT filename='Define Coverage.png']
3. In the Define Range dialog, insert the required Min value and Max value. [ATTACHMENT filename='Define Range dialog_Define coverage.png']
4. Click OK .

- The percentage of coverage is displayed in the Robustness Checklist.
- The relationship between the control and the other element must be established beforehand.

##### Prioritizing the High Impact Failure Mode

To highlight the High Impact Failure mode in the Robustness Checklist.

- Right-click the required Failure Mode and select Toggle High Impact Status from the Contextual menu. [ATTACHMENT filename='Toggle High Impact Status.png']

##### Creating a Relevant To Relationship

A **Relevant** **To**relationship can be created between:

- Noise Factor and Activity Input
- Failure Mode and Activity Output

To create a Relevant To relationship

1. Select the white cell between a Noise Factor and an Input.
2. Right-click and select Create Relevant To from the Contextual menu. [ATTACHMENT filename='Input_Relevant To.png']
3. Select the white cell between a Failure mode and an Output
4. Right-click and select Create Relevant To from the Contextual menu. [ATTACHMENT filename='Output_Relevant To.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the **Red Arrow**.

##### Creating Causality Relationship

A**Causality**relationship can be created between:

- Noise Factor and Failure Cause
- Noise Factor and Failure Mode

To create a Causality relationship

1. Select the white cell between a Noise Factor and a Failure Cause.
2. Right-click and select Create Causality from the Contextual menu. [ATTACHMENT filename='Causality_Failure Cause.png']
3. Select the white cell between a Noise factor and a Failure Mode.
4. Right-click and select Create Causality from the Contextual menu. [ATTACHMENT filename='Causality_Failure Mode.png']

An association is created between the two elements and is visible in the Robustness Checklist with the help of the **Blue Line**.

##### Creating a PreventionRelationship

A **Prevention**relationship can be created between Prevention Control and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Preventionrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Prevention from the Contextual menu. [ATTACHMENT filename='Create Prevention.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the **Green Arrow**.

##### Creating aDetectionRelationship

A**Detection**relationship can be created between Detection Control and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Detectionrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Detection from the Contextual menu. [ATTACHMENT filename='Create Detection.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the **Orange Arrow**.

##### Creating aRecommendation Relationship

A**Recommendation**relationship can be created between the Recommended Action and :

- Noise factor
- Failure Cause
- Failure Mode
- Failure Effect

To create a Recommendationrelationship

1. Select the white cell between the targeted elements.
2. Right-click and select Create Recommendation from the Contextual menu. [ATTACHMENT filename='Create Recommendation.png']

A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the **Purple Arrow**.

##### Creating an FMEA Item

An FMEA Item relationship can be created between a Failure Mode and:

- A Failure Cause
- A Failure Effect

To create an FMEA Item

1. Select the white cell between the targeted elements.
2. Right-click and select Create FMEA Item from the Contextual menu. [ATTACHMENT filename='Create FMEA Item.png']

- A Failure Mode to Failure Effect relationship is created between the two elements and is visible in the Robustness Checklist with the help of the Pink Arrow .
- A Failure Cause to Failure Mode relationship is created between the two elements and is visible in the Robustness Checklist with the help of the Dark Blue Arrow .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);">For a specific function/activity, a Robustness Check List allows verifying that prevention controls (design methods) and detection controls (test methods) are adequate given the impact of failure modes/failure effects to be covered and the range of variation of noise factors that cause these failure modes/failure effects to arise.</span></p><p style="margin-left: 0.0in;"><span style="color:var(--ds-text,#172b4d);">The rows and columns of the Robustness Check List display the noise factors with their associated ranges of variation, the failure causes, the failure modes, the failure effects, the prevention controls, the detection controls, and the recommended actions associated with the function/activity for which the RCL is established. All these elements could come from the function/activity Parameter Diagram, except the failure causes, which are introduced manually in the Robustness Check List.</span></p><p><strong><span style="color:var(--ds-text,#172b4d);">Essential </span>Information:</strong></p><ul><li data-uuid="85458ff3-010b-4be7-9903-1f24cada3f7d">The robustness checklist diagram is created based on an activity object.</li><li data-uuid="42487df7-6c2b-4033-9cfa-1c1ac4e18806">All relationships in the Robustness Checklist can be deleted by right-clicking the cell and selecting the corresponding delete command. It can also be deleted from the model itself by pressing the Delete key on the Keyboard.</li><li data-uuid="8fc13858-2b5f-469c-8f6b-56862bc6da93">The Parameter diagram and the FMEA table also show all existing relationships.</li><li data-uuid="cfc9b423-d988-48d2-b5c8-9359861e0d93">If a Parameter Diagram and/or an FMEA table exist for the activity, you can navigate from the Robustness Checklist with the help of the commands present in the toolbar. The following table displays the icons and functions of the commands:<br /><br /><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th style="text-align: center;">Icon</th><th style="text-align: center;">Description</th></tr><tr><td style="text-align: center;"><div class="content-wrapper" title=""><p><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Open Function in Parameter Diagram.png" /></ac:image></p></div></td><td style="text-align: left;">Opens the Function in the Parameter Diagram</td></tr><tr><td style="text-align: center;"><div class="content-wrapper" title=""><p><ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="Open Function in RAAML based FMEA Table.png" /></ac:image></p></div></td><td style="text-align: left;">Opens the Function in the RAAML-based FMEA Table</td></tr></tbody></table></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fda1a168-75a0-45d4-957b-71e2562c2713"><ac:rich-text-body><p>The Robustness Checklist is a <span style="color:var(--ds-text,#172b4d);">Dependency Matrix</span>. To learn more, refer to the <span style="color:var(--ds-text,#172b4d);"><a href="https://docs.nomagic.com/MT/?contextKey=dependency-matrix&amp;version=latest&amp;variant=default">Dependency Matrix</a> </span>page.</p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Robustness Checklist</h3><p>To create a Robustness Checklist </p><hr /><ol><li data-uuid="892fc8f0-795d-47aa-8761-c9ed64f015aa">In the Containment tree, right-click the <strong>Robustness Checklist </strong>package and select<strong> Create Diagram.</strong><strong><br /></strong></li><li data-uuid="2d14e84a-b761-4561-9363-6e13079341d3">Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>Failure Mode Avoidance </strong>and select <strong>Robustness Checklist.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Robustness_Select.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword robust and then select <strong>Robustness Checklist.<br /><br /><ac:image ac:thumbnail="true" ac:height="162"><ri:attachment ri:filename="Robustness_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li class="auto-cursor-target" data-uuid="a5d0d5d4-6d6e-4687-be18-590ec7fc7a2e">In the Select Activity dialog, select the required Activity and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Activity.png" /></ac:image><br /><br />The Robustness Checklist is now displayed in the diagram pane of the modeling tool.<br /><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="9e61e657-7953-4837-be46-58d6639b3e94"><ac:rich-text-body><p>You must focus on identifying relationships with the aid of the white cells, as the grey cells are not editable.</p></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="Robustness_Checklist.png" /></ac:image></li></ol><h3>Adding an element to the Robustness Checklist</h3><p>To add an element to the Robustness Checklist</p><hr /><ol><li data-uuid="b24ed1a7-9041-4ed0-abad-f84064d823d8">In the containment Tree, select the element to be added.</li><li data-uuid="4d5d38bc-064b-4e55-9a71-7d88a5d4d483">Drag and drop the element on the Column corresponding to the element folder and refresh the diagram.<br /><br /><ac:image><ri:attachment ri:filename="Adding element.png" /></ac:image></li></ol><h3>Deleting elements from the Robustness Checklist</h3><p>To delete elements from the Robustness Checklist</p><hr /><ol><li data-uuid="78dcbe1c-7f26-4777-b6d9-4448133127a7">In the Robustness Checklist, select the element to be deleted.</li><li data-uuid="a271a947-821d-4540-b69c-8775b2863344">Right-click and select <strong>Remove from the Matrix </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Delete Element.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e0866958-7124-453c-a2b8-22dd157bfdf8"><ac:rich-text-body><p>You can completely delete the element by pressing the Delete button on the Keyboard.</p></ac:rich-text-body></ac:structured-macro><h3>Creating a range for the Noise Factor</h3><p>With the Robustness checklist, you can enter a range describing the boundaries in an existing Unit of measure for the variation of the Noise Factor.</p><p>To create a range for the Noise Factor</p><hr /><ol><li data-uuid="a7345d17-5745-42ac-a5b4-c698e107e42b">Select the cell corresponding to the targeted Noise Factor and the first column <strong>Range.</strong></li><li data-uuid="af2a4d11-17a7-488b-8468-003e478eeac2">Right-click and select <strong>Define Range </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Define Range Command.png" /></ac:image><br /><br /></li><li data-uuid="d76e50f7-3625-4ad2-b2d8-4dfff84089f6">In the Define Range dialog, insert the required <strong>Min </strong>value, <strong>Max </strong>value, and define the <strong>Unit. </strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog.png" /></ac:image><br /><br /></strong></li><li data-uuid="88382b09-135b-470c-bd76-c6b125ed7184">C<span>lick </span><strong>OK.</strong></li></ol><h3>Creating Design Limits for the Activity</h3><p>To c<span>reate a Design Limit for the Activity</span></p><hr /><ol><li data-uuid="8e6c3f42-d08a-486b-8ccc-ce398f82e9dc">Select the cell corresponding to the targeted Noise Factor and the second column, <strong>Design Limits</strong>.</li><li data-uuid="6aa04f5c-a0bf-48c9-a3f7-6ff85c1f5e11">Right-click and select <strong>Design Limits </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Desgin Limit command.png" /></ac:image><br /><br /></li><li data-uuid="2018a8e2-9aa8-46f4-b163-76c1047ae1a9">In the Define Range dialog, insert the required <strong>Min </strong>value, <strong>Max </strong>value, and define the <strong>Unit.</strong><br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog_Desgin Limit.png" /></ac:image><br /><br /></li><li data-uuid="69d9fe17-d48e-4bae-b8f7-d4ae4b3b2fe3">C<span>lick </span><strong>OK.</strong></li></ol><h3>Defining coverage for Prevention or Detection Controls</h3><p>Design methods and test methods may cover a fraction of the range of a noise factor or more than the range of the noise factor. The end user can capture the range of the coverage when a prevention control or detection control is associated to a noise factor using a contextual menu item <strong>Define coverage</strong>. A dialog allows capturing a minimal value and a maximal value covered by the control, with the same unit as the covered noise factor. The covered range is persisted in the prevention or detection dependency, allowing controls to be enriched without modifying them directly.</p><p>The formula to compute the percentage of coverage follows the following rule: if the full range of the noise factor is not covered, the fraction that is covered is computed and the ratio to the full range of the noise factor is displayed; otherwise, the percentage of coverage is the ratio between the control range and the noise factor range.</p><p><br /></p><p><span>To Define Coverage </span></p><hr /><ol><li data-uuid="94b2061e-2845-4be1-9d0b-bc6b3628f8ea">Select the cell corresponding to the targeted controls to be defined.</li><li data-uuid="c5078f61-d639-4e50-a382-a9f51c3902f8">Right-click and select <strong>Define Coverage </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Define Coverage.png" /></ac:image><br /><br /></li><li data-uuid="4e6bca39-338a-4871-baa4-1eff63417e1a">In the Define Range dialog, insert the required <strong>Min </strong>value and  <strong>Max </strong>value. <br /><br /><ac:image><ri:attachment ri:filename="Define Range dialog_Define coverage.png" /></ac:image><br /><br /></li><li data-uuid="df3e917e-eba2-4692-9efc-a047d13f6221">Click <strong>OK</strong>.</li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0b85f398-5ea0-4100-9f0f-9c9f1e0d91d5"><ac:rich-text-body><ul><li data-uuid="44160890-1b00-403e-b129-ec217ccf9126">The percentage of coverage is displayed in the Robustness Checklist.</li><li data-uuid="2f023968-545f-4cfb-a9c5-15c572ab3eaa"><p>The relationship between the control and the other element must be established beforehand.</p></li></ul></ac:rich-text-body></ac:structured-macro><h3>Prioritizing the High Impact Failure Mode</h3><p><span>To highlight the High Impact Failure mode in the Robustness Checklist.</span></p><hr /><ul><li data-uuid="51947f67-450f-46f0-9bdd-bf64675d28b8">Right-click the required Failure Mode and select <strong>Toggle High Impact Status </strong><span>from the Contextual menu.<br /><br /></span><ac:image><ri:attachment ri:filename="Toggle High Impact Status.png" /></ac:image></li></ul><h3>Creating a Relevant To Relationship</h3><p>A <strong>Relevant</strong> <strong>To </strong>relationship can be created between:</p><ul><li data-uuid="7088c7a2-6d65-42fb-95fb-87865ddf45ed">Noise Factor and Activity Input</li><li data-uuid="88479b76-7825-4ee2-b179-abb45ae3dede">Failure Mode and Activity Output</li></ul><p>To create a Relevant To relationship</p><hr /><ol><li data-uuid="acaf710c-bc6a-4493-ace4-ed9e3065b175">Select the white cell between a Noise Factor and an Input.</li><li data-uuid="6fffbf05-1bc0-4987-bad5-0b97f0c45ffe">Right-click and select <strong>Create Relevant To </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Input_Relevant To.png" /></ac:image><br /><br /></li><li data-uuid="26ee81af-800f-4a33-a37c-82f58b95b9d1">Select the white cell between a Failure mode and an Output</li><li data-uuid="36545424-4fd4-414b-a652-4ccedfe8cb5e">Right-click and select <strong>Create Relevant To </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Output_Relevant To.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c12d578d-3a4e-4b48-873b-487cd765b396"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Red Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3>Creating Causality Relationship</h3><p>A<strong> Causality </strong>relationship can be created between:</p><ul><li data-uuid="e96040a3-1f79-4d09-95b3-aaa93ff95885">Noise Factor and Failure Cause</li><li data-uuid="ba3aa7a4-de82-43be-ad6d-a0ef7e745f56">Noise Factor and Failure Mode</li></ul><p><br /></p><p>To create a Causality relationship</p><hr /><ol><li data-uuid="9d70cda2-5608-4f6c-9ff8-86a3086d1d62">Select the white cell between a Noise Factor and a Failure Cause.</li><li data-uuid="570bb26f-96e0-4925-8f6e-b95f8328eacd">Right-click and select <strong>Create Causality </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Failure Cause.png" /></ac:image><br /><br /></li><li data-uuid="837f85a6-a7a8-47bd-ab07-38e0e20e526a">Select the white cell between a Noise factor and a Failure Mode.</li><li data-uuid="ec28be0e-5ec8-4edf-9d7a-ccb1326ee5fb">Right-click and select <strong>Create Causality </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Failure Mode.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="04342581-82fe-45e1-93f5-f2ee6ca5bdd2"><ac:rich-text-body><p><span>An association is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Blue Line</strong>.</span></p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a Prevention </span><span>Relationship</span></h3><p>A <strong>Prevention </strong>relationship can be created between Prevention Control and :</p><ul><li data-uuid="fc3464a9-b0f4-4528-a26d-8b363d3c5b3b">Noise factor</li><li data-uuid="1f4742e4-3352-41ba-9bf7-759b706a82b8">Failure Cause</li><li data-uuid="4019f463-3fc2-4b5e-b988-985284e662f8">Failure Mode</li><li data-uuid="938cd914-1ff3-4d86-b66f-0f82bec5e105">Failure Effect</li></ul><p>To create a <span>Prevention </span><span>relationship</span></p><hr /><ol><li data-uuid="aa197250-4208-4548-885d-32e5b59c900e">Select the white cell between the targeted elements.</li><li data-uuid="d1460d36-5cf6-4e48-a3d0-40bab0655431">Right-click and select <strong>Create Prevention </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Prevention.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5b9acbc9-09cf-4d30-a5db-1a4eed2e812c"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the <strong>Green Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a </span><span>Detection </span><span>Relationship</span></h3><p>A<strong> Detection </strong>relationship can be created between Detection Control and :</p><ul><li data-uuid="a01fb4b2-5267-4860-844e-095b9594d99b">Noise factor</li><li data-uuid="fc85d6d1-a86b-43aa-a233-7bed8ee0950a">Failure Cause</li><li data-uuid="19dc5177-6ca4-42b8-b59f-c05bdc653315">Failure Mode</li><li data-uuid="170e1b9b-e092-476e-ae39-dbfa2425aed5">Failure Effect</li></ul><p>To create a <span>Detection </span><span>relationship</span></p><hr /><ol><li data-uuid="4bab0dfe-a834-4b8a-a0a0-70ea004663e4">Select the white cell between the targeted elements.</li><li data-uuid="455d3108-8fe8-441c-8072-4460825af268">Right-click and select <strong>Create Detection </strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Detection.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="aec35c91-e3e9-4d79-8a1f-32e8c5f2fcdb"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the <strong>Orange Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3><span>Creating a </span><span>Recommendation Relationship</span></h3><p>A<strong> Recommendation </strong>relationship can be created between the Recommended Action and  :</p><ul><li data-uuid="d2b237bb-99f1-400e-9190-078b5a7bd929">Noise factor</li><li data-uuid="c29234a1-738d-4e5d-8520-ff02b0f3b9ba">Failure Cause</li><li data-uuid="0beb4d1a-1aea-4500-974a-10f8cdb702b5">Failure Mode</li><li data-uuid="6fdc28ff-b107-4a67-92f1-071579334eda">Failure Effect</li></ul><p>To create a <span>Recommendation </span><span>relationship</span></p><hr /><ol><li data-uuid="d285265c-5cfb-45fb-955d-b70eab5d1b08">Select the white cell between the targeted elements.</li><li data-uuid="bcafb79a-26c9-4a86-ac6c-60eb14dd71e4">Right-click and select <strong>Create <span>Recommendation </span></strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create Recommendation.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b2e31893-834d-46da-a2e0-32284880626a"><ac:rich-text-body><p>A dependency is created between the two elements and is visible in the Robustness Checklist with the aid of the <strong>Purple Arrow</strong>.</p></ac:rich-text-body></ac:structured-macro><h3>Creating an FMEA Item</h3><p>An FMEA Item relationship can be created between a Failure Mode and:</p><ul><li data-uuid="116085d4-cf32-42f8-bedd-873c262d2c71">A Failure Cause</li><li data-uuid="86b6acd3-136d-44bb-a2cb-6152ecd1d999">A Failure Effect</li></ul><p>To create an FMEA Item</p><hr /><ol><li data-uuid="5b34a555-7d9d-453f-9a94-a0a5d2e3d704">Select the white cell between the targeted elements.</li><li data-uuid="44cc3523-496c-4cc5-b3ce-cc28639f9b8f">Right-click and select <strong>Create <span>FMEA Item </span></strong>from the Contextual menu.<br /><br /><ac:image><ri:attachment ri:filename="Create FMEA Item.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4e59ec84-97a2-4020-b0c1-92413d6d808c"><ac:rich-text-body><ul><li data-uuid="2907a060-fdd1-48ca-8417-ac98f2ee1ca4">A Failure Mode to Failure Effect relationship is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Pink Arrow</strong>.</li><li data-uuid="5232dc13-6830-4e21-8367-333242da8858">A Failure Cause to Failure Mode relationship is created between the two elements and is visible in the Robustness Checklist with the help of the <strong>Dark Blue Arrow</strong>.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249578347 space=SSE version=3 -->
## PAGE 00029: Systems Safety Engineer

- page_id: `249578347`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578347/Systems+Safety+Engineer
- version_number: 3
- version_date: `2026-04-24T13:24:01.455+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

#### WARNING: Technology Preview

Technology Preview

This is the **technology preview** version. We **do not** recommend using it to create any long-term projects because it may change without notice. The migration to the latest version will not be possible.

Quality and Safety disciplines are critical to ensure**reliable**and**safe**systems.

Based on the system architecture, the Systems Safety Engineer plugin enables:

- The creation of the Boundary Diagram and **Item** to finalize the scope (the relevant parts of the system to be analyzed).
- The creation of an item-based Interface Analysis table to study connections between functions.
- The creation of a Parameter Diagram to identify the measurable parameters that could affect the intended output of a given function.
- The creation of a Robustness Checklist to identify causality links between elements of a given function.
- The creation of a Failure Mode and Effects Analysis table

Systems Safety Engineer is**RAAML-based**and partiallysupports **SAE J1739.**

**[IMAGE alt='' src='']**

###### Systems Safety Engineer workflow

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="1ce8104b-f556-4ea4-b382-01746572a2e6"><ac:parameter ac:name="title">Technology Preview</ac:parameter><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">This is the <strong>technology preview</strong> version. We <u><strong>do not</strong></u> recommend using it to create any long-term projects because it may change without notice. The migration to the latest version will not be possible. </span></p></ac:rich-text-body></ac:structured-macro><p style="text-align: left;"><br /></p><p style="text-align: left;">Quality and Safety discipline<ac:inline-comment-marker ac:ref="37466a70-af18-4867-94b1-fb68120a27ce">s are critical</ac:inline-comment-marker> to ensure<span> </span><strong>reliable</strong><span> </span>and<span> </span><strong>safe</strong><span> </span>systems.</p><p style="text-align: left;">Based on the system architecture, the Systems Safety Engineer plugin enables: </p><ul style="text-align: left;"><li data-uuid="3f540db5-e389-4a4b-8523-cdc36585110f">The creation of the <strong>Boundary Diagram</strong><span> </span>and<span> <strong>Item </strong></span>to finalize the scope (the relevant parts of the system to be analyzed).</li><li data-uuid="80725f4b-abb9-4e63-946d-6db68b3bee78">The creation of an item-based<span> </span><strong>Interface Analysis</strong><span> </span>table to study connections between functions.</li><li data-uuid="e5730bf5-a485-4dbd-bb43-07aaca877242">The creation of a<span> </span><strong>Parameter Diagram</strong><span> </span>to identify the measurable parameters that could affect the intended output of a given function.</li><li data-uuid="d91ec259-dcf9-47cd-b160-9373cac38c8c">The creation of a<span> </span><strong>Robustness Checklist</strong><span> </span>to identify causality links between elements of a given function.</li><li data-uuid="d39015c0-af0f-4b64-8254-537060761b99">The creation of a<span> </span><strong>Failure Mode and Effects Analysis</strong><span> </span>table </li></ul><p style="text-align: left;">Systems Safety Engineer is<span> </span><strong>RAAML-based</strong><span> </span>and partially<span> </span>supports <strong>SAE J1739.</strong></p><p style="text-align: center;"><strong><ac:image ac:border="true" ac:height="646" ac:width="983"><ri:attachment ri:filename="SSE_Workflow.png" /></ac:image></strong></p><h6 style="text-align: center;">Systems Safety Engineer workflow</h6>
````

<!--NOMAGIC_PAGE id=249578355 space=SSE version=6 -->
## PAGE 00030: Systems Safety Engineer Project

- page_id: `249578355`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/249578355/Systems+Safety+Engineer+Project
- version_number: 6
- version_date: `2025-11-18T10:42:42.419+01:00`
- ancestors: Systems Safety Engineer
- labels: []

### NORMALIZED CONTENT

**On this page**

**3**

##### Creating a Failure Mode Avoidance project

To create a new Failure Mode Avoidance project

1. Do one of the following:
  - From the File menu, select New Project from the drop-down list. [IMAGE alt='' src='']
  - Click Create New Project on the welcome screen. [ATTACHMENT filename='Create New Project_Command.png']
  - Press Ctrl + Shift + N.
2. In the New Project dialog, select the **Failure Mode Avoidance Project.** 
[IMAGE alt='' src='']
3. Specify the file name in the Name box.
4. Click the[IMAGE alt='' src='']button to select the location to store the project in a folder.
5. Select the checkbox to automatically create a folder for the project in the specified location.
6. Click **OK**.

A new FMA project is displayed with the default packages in the Containment tree and the Index.

If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling tool.

##### FMA Project Template

A default FMA project template is displayed once you open the project. This template is provided to help you initiate the process.

**Containment Tree**

The Containment tree displays the default packages in the Containment tree. You can add, modify or delete any element or package from the Containment tree.

**Index**

The Index displays the default information related to FMA.

If you press the CTRL key and double-click any table's icon, the table opens in a new tab.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong> On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="46c4561c-0f22-492b-8293-80bfb1550691"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></strong></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Failure Mode Avoidance project</h3><p>To create a new Failure Mode Avoidance project</p><hr /><ol><li data-uuid="c9663650-be20-4101-a6f2-9e1cc79268c0">Do one of the following:<ul><li class="atl-forced-newline">From the<span> </span><strong>File</strong><span> </span>menu, select <strong>New Project </strong>from the drop-down list.<br /><em><br /><ac:image><ri:attachment ri:filename="New Project_command.jpg" /></ac:image><br /><br /></em></li><li>Click <strong>Create New Project </strong>on the welcome screen.<br /><br /><ac:image><ri:attachment ri:filename="Create New Project_Command.png" /></ac:image><br /><br /></li><li>Press Ctrl + Shift + N.</li></ul></li><li data-uuid="4310d984-d576-48e0-8043-17f8f317b18e"><p class="auto-cursor-target">In the New Project dialog, select the <strong>Failure Mode Avoidance Project.<br /></strong><br /><ac:image><ri:attachment ri:filename="Create new project.png" /></ac:image><br /><br /></p></li><li data-uuid="d890174a-ac09-481f-87f7-9b950bd6b214"><p class="auto-cursor-target">Specify the file name in the Name box.</p></li><li data-uuid="e39405d4-db37-4b91-be61-253584a3ad9e"><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Click the</span><span style="color:var(--ds-text,#333333);"><span> <ac:image><ri:attachment ri:filename="Three Dot Icon.png" /></ac:image> </span>button to select the location to store the project in a folder.</span></p></li><li data-uuid="a19816a0-a524-478e-b6c8-2f26f808363e"><p class="auto-cursor-target">Select the checkbox to automatically create a folder for the project in the specified location.</p></li><li data-uuid="d62ba4ba-6a2c-433f-b1ae-205655313535"><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li></ol><p>A new FMA project is displayed with the default packages in the Containment tree and the Index.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="df13aefb-d300-4916-8e58-5927a3285c35"><ac:rich-text-body><p>If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling tool.</p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">FMA Project Template</h3><p>A default FMA project template is displayed once you open the project. This template is provided to help you initiate the process.</p><p><strong>Containment Tree</strong></p><p>The Containment tree displays the default packages in the Containment tree. You can add, modify or delete any element or package from the Containment tree.</p><p><strong>Index</strong></p><p>The Index displays the default information related to FMA. </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="99614ef4-6697-44ce-a28f-8369f17b828d"><ac:rich-text-body><p>If you press the CTRL key and double-click any table's icon, the table opens in a new tab.</p></ac:rich-text-body></ac:structured-macro><ac:image><ri:attachment ri:filename="FMEA Template.png" /></ac:image></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=254421554 space=SSE version=1 -->
## PAGE 00031: Versions of Systems Safety Engineer

- page_id: `254421554`
- space_key: `SSE`
- source_url: https://docs.nomagic.com/spaces/SSE/pages/254421554/Versions+of+Systems+Safety+Engineer
- version_number: 1
- version_date: `2025-09-12T11:45:50.366+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

75e416cf904e3e67fc592050334d0e2d

Systems Safety Engineer

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="72db3a89-62d7-4e08-b660-f869606894a4"><ac:parameter ac:name="permaId">75e416cf904e3e67fc592050334d0e2d</ac:parameter><ac:parameter ac:name="documentTitle">Systems Safety Engineer</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````
