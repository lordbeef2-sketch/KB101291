# NOMAGIC DOCUMENTATION SPACE: Cameo Safety and Reliability Analyzer 2024x Refresh1

<!--NOMAGIC_SPACE key=CSRA2024xR1 chunk=1 -->

<!--NOMAGIC_PAGE id=170466444 space=CSRA2024xR1 version=19 -->
## PAGE 00001: 2024x Refresh1 Version News

- page_id: `170466444`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466444/2024x+Refresh1+Version+News
- version_number: 19
- version_date: `2024-10-07T09:28:06.391+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

### Cameo Safety and Reliability Analyzer

Released on: July 5, 2024

This version was released for compatibility purposes only. It does not contain new capabilities.

Check the product compatibility [here](https://www.nomagic.com/support/compatibility).

**News of related plugin**

- [CONFLUENCE_PAGE title='2024x Refresh1 Version News' space='SCD2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;">Cameo Safety and Reliability Analyzer</h1><p style="text-align: center;"><span style="color: rgb(62,63,64);"><span style="color: rgb(128,128,128);">Released on: July 5, 2024</span></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This version was released for compatibility purposes only. It does not contain new capabilities.</p><p>Check the product compatibility <a class="external-link" href="https://www.nomagic.com/support/compatibility" style="text-decoration: none;">here</a>.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>News of related plugin</strong></p><ul><li><ac:link><ri:page ri:space-key="SCD2024xR1" ri:content-title="2024x Refresh1 Version News" /><ac:plain-text-link-body><![CDATA[Systems Cybersecurity Designer ]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466454 space=CSRA2024xR1 version=4 -->
## PAGE 00002: 2024x Version News

- page_id: `170466454`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466454/2024x+Version+News
- version_number: 4
- version_date: `2024-10-07T09:28:14.890+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

### Cameo Safety and Reliability Analyzer

Released on: November 10, 2023

This version was released for compatibility purposes only. It does not contain new capabilities.

Check the product compatibility [here](https://www.nomagic.com/support/compatibility).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;">Cameo Safety and Reliability Analyzer</h1><p style="text-align: center;"><span style="color: rgb(62,63,64);"><span style="color: rgb(128,128,128);">Released on: November 10, 2023</span></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This version was released for compatibility purposes only. It does not contain new capabilities.</p><p>Check the product compatibility <a class="external-link" href="https://www.nomagic.com/support/compatibility" style="text-decoration: none;">here</a>.</p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466541 space=CSRA2024xR1 version=1 -->
## PAGE 00003: Accident Scenarios Table

- page_id: `170466541`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466541/Accident+Scenarios+Table
- version_number: 1
- version_date: `2023-06-26T06:37:32.470+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Use filters to find elements quicker

2057153239

#### CONTENT-COLUMN: Use filters to find elements quicker

2057153250

2057153238

**On this page**

4

#### CONTENT-BLOCK: Use filters to find elements quicker

2057153240

An Accident Scenarios Table allows you to define Accident Scenarios as a combination of Malfunctioning Behaviors and Operational Situations. The sections below explain how to create Accident Scenarios and assign the Controllabilitylevel, Malfunctioning Behavior, and Operational Situations.

[IMAGE alt='' src='']

###### An example of an Accident Scenarios Table.

##### Creating Accident Scenarios Table

You can create an Accident Scenarios Table as described below.

To create an Accident Scenario Table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select Accident Scenarios Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select Create Diagram, and select Accident Scenarios Table in the open dialog . [ATTACHMENT filename='creating_accident_scenarios_table.png']
3. When the table is created, type the name of the table and press Enter.

After following the above steps, an Accident Scenarios Table is created. The scope and element type of the table are already specified for you.

##### Creating Accident Scenarios

There are two ways to create an Accident Scenario: you can do it right in an Accident Scenarios Table or in the Containment tree.

To create an Accident Scenario in the Containment tree

1. In the Containment tree, right-click the owner of a new element and select Create Element .
2. In the open window, select Accident Scenario . [ATTACHMENT filename='creating_accident_scenario.png']
3. When an Accident Scenario is created, type the name of the element and press Enter.

When you create an Accident Scenario in the model browser, it is automatically added to an Accident Scenarios Table if it exists.

To create an Accident Scenario in an Accident Scenario Table

1. In an Accident Scenarios Table, select a table row.
2. Do one of the following:
  - In the table toolbar, click Add Sibling to create an element of the same level as the one you have selected. [ATTACHMENT filename='Add Sibling.png']
  - In the table toolbar, click **Add Nested**to create an element nested under the selected element. 
 
[IMAGE alt='' src='']
3. Type the name of the new element and press Enter.

****When you create an Accident Scenario and add it to an Accident Scenarios Table, you need to define the element as described in the section below.

##### Defining Accident Scenarios

After creating an Accident Scenario, you need to define its Controllability level which allows you to estimate the probability of avoiding the specified harm or damage. Also, you have to assign a Malfunctioning Behavior and Operational Situations to the Accident Scenario.

To define a Controllability level

1. In an Accident Scenarios Table, double-click the cell of the **Controllability** column and select the desired Controllability level from the list. 
 
[IMAGE alt='' src='']
2. Double-click the cell of the **Justification of Controllability** column and write the justification to explain the selected Controllability level.

##### Assigning a Malfunctioning Behavior

1. In an Accident Scenarios Table, double-click the cell of the **Malfunctioning Behavior** column and click [IMAGE alt='' src=''].
2. On the left side of the **Select Elements**dialog, open the **List** tab.
3. Select the Malfunctioning Behavior you want to assign and click **OK**.

You can also drag and drop the Malfunctioning Behaviorfrom the Containment tree to the Accident Scenarios Table.

[IMAGE alt='' src='']

##### Assigning Operational Situations

1. In an Accident Scenarios Table, double-click the cell of the Operational Situation column and click [IMAGE alt='' src=''].
2. On the left side of the **Select Elements** dialog, open the **List** tab.
3. Double-click the Operational Situations you want to assign. The elements should be added to the selected elements area on the right side of the dialog. 
 
[IMAGE alt='' src='']
4. Click **OK**.

You can also drag and drop the Operational Situationsfrom the Containment tree to the Accident Scenarios Table.

[IMAGE alt='' src='']

#### TIP: Use filters to find elements quicker

Use filters to find elements quicker

When you assign a Malfunctioning Behavior or Operational Situations, use a filter after step 2 to find elements quicker:

1. In the Select Elements dialog, click [ATTACHMENT filename='Three Dot_Select Element.png'] next to the Filter by ISO properties box.
2. In the Select Properties dialog, click the Value box of the property and select the desired property value from the list. [ATTACHMENT filename='Select Properties.png']
3. Click OK .

Now the **List** tab displays the elements with the selected property value.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6711896b-cfa4-4638-b57e-1f7865a9d4ca"><ac:parameter ac:name="id">2057153239</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="28206ed5-bd54-48bd-affe-7936bc1c24b3"><ac:parameter ac:name="id">2057153250</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5cefc4a2-0f1d-40d5-a7fe-de752c81cfcf"><ac:parameter ac:name="id">2057153238</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ea9c7ae1-4c30-463f-bc43-e06ef5e4a2bd"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="53830c55-0662-4844-820d-90af3a9a4653"><ac:parameter ac:name="id">2057153240</ac:parameter><ac:rich-text-body><p>An Accident Scenarios Table allows you to define Accident Scenarios as a combination of Malfunctioning Behaviors and Operational Situations. The sections below explain how to create Accident Scenarios and assign the <span style="color: rgb(62,63,64);">Controllability </span>level, Malfunctioning Behavior, and Operational Situations.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="accident_scenarios_table1.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of an Accident Scenarios Table.</h6><h3>Creating Accident Scenarios Table</h3><p>You can create an Accident Scenarios Table as described below.</p><p><br /></p><p>To create an Accident Scenario Table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>Accident Scenarios Table</strong> in the open dialog.</li><li>In the Containment tree, right-click the owner of the table, select <strong>Create Diagram,</strong> and select <strong>Accident Scenarios Table</strong> in the open <ac:inline-comment-marker ac:ref="232d101f-64f1-4a3e-b6da-85cfcd24b8db">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="creating_accident_scenarios_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image><br /><br /></li></ul></li><li>When the table is created, type the name of the table and press Enter.</li></ol><p><span style="color: rgb(62,63,64);"><br />After following the above steps, an Accident Scenarios Table is created. The scope and element type of the table are already specified for you.</span></p><h3>Creating Accident Scenarios</h3><p>There are two ways to create an Accident Scenario: you can do it right in an Accident Scenarios Table or in the Containment tree.</p><p><br /></p><p>To create an Accident Scenario in the Containment tree</p><hr /><ol><li>In the Containment tree, right-click the owner of a new element and select <strong>Create Element</strong>.</li><li>In the open window, select <strong>Accident Scenario</strong>.<br /><br /><ac:image><ri:attachment ri:filename="creating_accident_scenario.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image><br /><br /></li><li>When an Accident Scenario is created, type the name of the element and press Enter.</li></ol><p><br />When you create an Accident Scenario in the model browser, it is automatically added to an Accident Scenarios Table if it exists.</p><p><br /></p><p>To create an Accident Scenario in an Accident Scenario Table</p><hr /><ol><li>In an Accident Scenarios Table, select a table row.</li><li>Do one of the following:<br /><ul><li>In the table toolbar, click <strong>Add Sibling </strong>to create an element of the same level as the one you have selected.<br /><br /><ac:image><ri:attachment ri:filename="Add Sibling.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">In the table toolbar, click <strong>Add Nested </strong>to create an element nested under the selected element.<br /><br /><ac:image><ri:attachment ri:filename="Add Nested.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image></p></li></ul></li><li>Type the name of the new element and press Enter.</li></ol><p><strong><br /></strong><span style="color: rgb(62,63,64);">When you create an Accident Scenario and add it to an Accident Scenarios Table, you need to define the element as described in the section below.</span></p><h3><span style="color: rgb(62,63,64);">Defining Accident Scenarios</span></h3><p>After creating an Accident Scenario, you need to define its Controllability level which allows you to estimate the probability of avoiding the specified harm or damage. Also, you have to assign a Malfunctioning Behavior and Operational Situations to the Accident Scenario. </p><p><br /></p><p><span style="color: rgb(62,63,64);">To define a Controllability level</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In an Accident Scenarios Table, double-click the cell of the <strong>Controllability</strong> column and select the desired Controllability level from the <ac:inline-comment-marker ac:ref="e61b8865-4d24-4fed-aba5-e2ab96cfbfe2">list</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="defining_controllability_level.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">Double-click the cell of the <strong>Justification of Controllability</strong> column and write the justification to explain the selected Controllability level.</span></li></ol><h3><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="4a8d6a07-9903-4863-9316-184fe619aba3">Assigning a Malfunctioning Behavior</ac:inline-comment-marker></span></h3><hr /><ol><li><span style="color: rgb(62,63,64);">In an Accident Scenarios Table, double-click the cell of the <strong>Malfunctioning Behavior</strong> column and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image>.</span></li><li><span style="color: rgb(62,63,64);">On the left side of the <strong>Select Elements</strong><span style="color: rgb(62,63,64);"> dialog, open the <strong>List</strong> tab.</span></span></li><li><span style="color: rgb(62,63,64);">Select the Malfunctioning Behavior you want to assign and click <strong><ac:inline-comment-marker ac:ref="bda74b48-a06a-47b1-b777-e6d5b9f516c9">OK</ac:inline-comment-marker></strong>.<br /><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3b2617c3-0e1e-44b5-bf5a-10414df0b6e7"><ac:rich-text-body><p>You can also drag and drop the <span style="color: rgb(62,63,64);">Malfunctioning Behavior </span>from the Containment tree to the Accident Scenarios Table.</p><p><ac:image><ri:attachment ri:filename="Malfunctioning Behavior_Drag-Drop.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(62,63,64);"><br /></span></p><h3><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="859e98bf-beae-49fe-8ed5-b217197cd38f">Assigning Operational Situations</ac:inline-comment-marker></span></h3><hr /><ol><li><span style="color: rgb(62,63,64);">In an Accident Scenarios Table, double-click the cell of the Operational Situation column and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image>.</span></li><li><span style="color: rgb(62,63,64);">On the left side of the <strong>Select Elements</strong> dialog, open the <strong>List</strong> tab.</span></li><li><span style="color: rgb(62,63,64);">Double-click the Operational Situations you want to assign. The elements should be added to the selected elements area on the right side of the <ac:inline-comment-marker ac:ref="1d9605a0-0529-41e5-ab35-8af309e1d684">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="assigning_operational_situations.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">Click <strong>OK</strong>.<br /><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f3a52720-7378-419f-9a32-2bbc36cfae00"><ac:rich-text-body><p>You can also drag and drop the <span style="color: rgb(62,63,64);">Operational Situations </span>from the Containment tree to the Accident Scenarios Table.</p><p><ac:image><ri:attachment ri:filename="Operational Situation_Drag-Drop.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(62,63,64);"><span style="color: rgb(23,43,77);"><br /></span></span></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f0e87259-8b7b-49ec-9d16-ffb1dc053285"><ac:parameter ac:name="title">Use filters to find elements quicker</ac:parameter><ac:rich-text-body><p>When you assign a Malfunctioning Behavior or Operational Situations, use a filter after step 2 to find elements quicker:</p><ol><li>In the <strong>Select Elements</strong> dialog, click <ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="Three Dot_Select Element.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image>next to the <strong>Filter by ISO properties</strong> box.</li><li>In the <strong>Select Properties</strong> dialog, click the <strong>Value</strong> box of the property and select the desired property value from the list.<br /><br /><ac:image><ri:attachment ri:filename="Select Properties.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Accident Scenarios Table" /></ri:attachment></ac:image><br /><br /></li><li>Click <strong>OK</strong>.</li></ol><p>Now the <strong>List</strong> tab displays the elements with the selected property value.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466632 space=CSRA2024xR1 version=1 -->
## PAGE 00004: Adding new guide words to a HazOp Table

- page_id: `170466632`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466632/Adding+new+guide+words+to+a+HazOp+Table
- version_number: 1
- version_date: `2023-06-20T06:11:32.192+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Customizations
- labels: []

### NORMALIZED CONTENT

You can add new guide words to a HazOp Table as described below.

To add a guide word to a HazOp Table

1. In your model, create a Profile Diagram.
2. In the Profile Diagram, create and name a Class, e.g., NewGuideWord .
3. Apply the «MalfunctioningBehavior» stereotype to the Class.
4. In the ISO 26262 Library, find the AnyMalfunction element and drag it to the Profile diagram.
5. Create a Generalization relationship from the Class created in Step 2 to AnyMalfunction .
6. Save and reload the project. [ATTACHMENT filename='adding_guide_words_to_hazop_table.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can add new guide words to a HazOp Table as described below.</p><p><br /></p><p>To add a guide word to a HazOp Table</p><hr /><ol><li>In your model, create a Profile Diagram.</li><li>In the Profile Diagram, create and name a Class, e.g., <em>NewGuideWord</em>.</li><li>Apply the «MalfunctioningBehavior» stereotype to the Class.</li><li>In the ISO 26262 Library, find the <em>AnyMalfunction</em> element and drag it to the Profile diagram.</li><li>Create a Generalization relationship from the Class created in Step 2 to <em><ac:inline-comment-marker ac:ref="3428b7f0-9c3e-4ad2-a659-74be943bffbf">AnyMalfunction</ac:inline-comment-marker></em>.</li><li><p><span style="color: rgb(62,63,64);">Save and reload the project.</span></p><br /><ac:image><ri:attachment ri:filename="adding_guide_words_to_hazop_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Adding new guide words to a HazOp Table" /></ri:attachment></ac:image></li></ol>
````

<!--NOMAGIC_PAGE id=170466629 space=CSRA2024xR1 version=1 -->
## PAGE 00005: Adding new types to a HazOp Table

- page_id: `170466629`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466629/Adding+new+types+to+a+HazOp+Table
- version_number: 1
- version_date: `2019-12-12T11:05:36.036+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Customizations
- labels: []

### NORMALIZED CONTENT

A HazOp table supports three element types: Activity, Use Case, and Class. If you want to use a different system function type, you can extend the default type list by using customization.

To add a new element type to a HazOp Table

1. Create a Profile Diagram.
2. In the Profile Diagram, create a Customization for adding a new element type to a HazOp Table and name it.
3. In the model browser, find the stereotype or metaclass of the element type you want to add and drag it to the Customization shape. Now this element type is the target of the Customization.
4. In the model browser, find the *HazOp Table Element Customization* and drag it to the Profile Diagram. Locating HazOp Table Element Customization*HazOp Table Element Customization* is an auxiliary resource. To see it in the model browser, click [IMAGE alt='' src=''] and select **Show Auxiliary Resources**.
5. Create a Generalization relationship from the Customization created in step 2 to HazOp Table Element Customization .
6. Save and reload the project. [IMAGE alt='' src='']

**Now a HazOp table supports your custom element type.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(51,51,51);">A HazOp table supports three element types: Activity, Use Case, and Class. If you want to use a different system function type, you can extend the default type list by using customization.</span></p><p><br /></p><p>To add a new element type to a HazOp Table</p><hr /><ol><li>Create a Profile Diagram.</li><li>In the Profile Diagram, create a Customization for adding a new element type to a HazOp Table and name it.</li><li>In the model browser, find the stereotype or metaclass of the element type you want to add and drag it to the Customization shape. Now this element type is the target of the Customization.</li><li><p class="auto-cursor-target">In the model browser, find the <em>HazOp Table Element Customization</em> and drag it to the Profile Diagram.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="458346a8-ddcd-4d8d-8974-977a8c84b048"><ac:parameter ac:name="title">Locating HazOp Table Element Customization</ac:parameter><ac:rich-text-body><p><em>HazOp Table Element Customization</em> is an auxiliary resource. To see it in the model browser, click <ac:image ac:thumbnail="true" ac:height="22"><ri:attachment ri:filename="options.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Adding new types to a HazOp Table" /></ri:attachment></ac:image> and select <strong>Show Auxiliary Resources</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Create a Generalization relationship from the Customization created in step 2 to <em>HazOp Table Element Customization</em>.</li><li>Save and reload the project.<em><br /><br /><ac:image><ri:attachment ri:filename="customization_for_adding_new_type_to_hazop_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Adding new types to a HazOp Table" /></ri:attachment></ac:image></em></li></ol><p><em><br /></em>Now a HazOp table supports your custom element type.</p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170466481 space=CSRA2024xR1 version=1 -->
## PAGE 00006: Additional features

- page_id: `170466481`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466481/Additional+features
- version_number: 1
- version_date: `2018-06-04T04:06:18.643+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

949532672

949532675

949532673

After completing the safety and reliability analysis, you can use a number of additional post-analysis features to further analyze, manage, and trace your model by:

- Creating [CONFLUENCE_PAGE title='Traceability maps' space='CSRA2024xR1'] to review the relations between Safety Analysis Items or FMEA Items and other elements of your model.
- Performing [CONFLUENCE_PAGE title='Safety and Reliability Coverage Analysis' space='CSRA2024xR1'] to identify which design elements are covered by safety analysis and FMEA.
- [CONFLUENCE_PAGE title='Generating reports' space='CSRA2024xR1'] from FMEA, Risk, or Risk Reduction Tables.

949532670

**Related pages**

- [CONFLUENCE_PAGE title='Getting started' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Reliability analysis using FMEA' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Safety analysis' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Customizing Safety Analysis and FMEA configurations' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="50cb7f77-007e-4d91-95da-c3b3370c8b9d"><ac:parameter ac:name="id">949532672</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3b5ac0d6-66ad-483b-a426-6cc95049acc6"><ac:parameter ac:name="id">949532675</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cd3315d0-7810-440e-bd0c-1c2b60e16aa8"><ac:parameter ac:name="id">949532673</ac:parameter><ac:rich-text-body><p>After completing the safety and reliability analysis, you can use a number of additional post-analysis features to further analyze, manage, and trace your model by:</p><ul><li>Creating <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /><ac:plain-text-link-body><![CDATA[traceability maps]]></ac:plain-text-link-body></ac:link> to review the relations between Safety Analysis Items or FMEA Items and other elements of your model.</li><li>Performing <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety and Reliability Coverage Analysis" /></ac:link> to identify which design elements are covered by safety analysis and FMEA.</li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generating reports" /></ac:link> from FMEA, Risk, or Risk Reduction Tables.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6b771a55-1610-4a90-a913-98a785468a19"><ac:parameter ac:name="id">949532670</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Getting started" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Reliability analysis using FMEA" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety analysis" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Customizing Safety Analysis and FMEA configurations" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466598 space=CSRA2024xR1 version=1 -->
## PAGE 00007: ASIL Decompose and DeriveReqt Relationships

- page_id: `170466598`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466598/ASIL+Decompose+and+DeriveReqt+Relationships
- version_number: 1
- version_date: `2020-03-09T13:31:39.511+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Validation Rules
- labels: []

### NORMALIZED CONTENT

**Constrained Element:** Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement

**Constrained Element Filter:** Safety Requirements that have outgoing DeriveReqt and ASIL Decompose relationships

**Severity:** error

**Error Message:** The ASIL value is incorrect due to ASIL Decompose and DeriveReqt relationships.

**Abbreviation:** ASILDcmpDrv

**Description:** Safety Requirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement) fail when the highest ASIL value defined by outgoing DeriveReqt relationships is not equal to the ASIL value of the constrained element.

[IMAGE alt='' src='']

###### Illustration of the ASIL Decompose and DeriveReqt Relationships validation rule.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Constrained Element:</strong> Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement</p><p><strong>Constrained Element Filter:</strong> <ac:inline-comment-marker ac:ref="1fd85623-4547-4176-b85f-d09d8e36101f">Safety Requirements</ac:inline-comment-marker> that have outgoing DeriveReqt and ASIL Decompose relationships</p><p><strong>Severity:</strong> error</p><p><strong>Error Message:</strong> The ASIL value is incorrect due to ASIL Decompose and DeriveReqt relationships.</p><p><strong>Abbreviation:</strong> ASILDcmpDrv</p><p><strong>Description:</strong> Safety Requirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement) fail when the highest ASIL value defined by outgoing DeriveReqt relationships is not equal to the ASIL value of the constrained element.</p><p style="text-align: center;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="ASIL_Decompose_and_DeriveReqt_Relationships_validation_rule.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ASIL Decompose and DeriveReqt Relationships" /></ri:attachment></ac:image></p><h6 class="with-breadcrumbs" style="text-align: center;">Illustration of the ASIL Decompose and DeriveReqt Relationships validation rule.</h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=170466600 space=CSRA2024xR1 version=1 -->
## PAGE 00008: ASIL Decompose and Independence Requirement Relationships

- page_id: `170466600`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466600/ASIL+Decompose+and+Independence+Requirement+Relationships
- version_number: 1
- version_date: `2020-03-09T13:40:59.012+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Validation Rules
- labels: []

### NORMALIZED CONTENT

**Constrained Element:** Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement

**Constrained Element Filter:** Safety Requirements that have outgoing Independence Requirement and ASIL Decompose relationships

**Severity:** Error

**Error Message:** The ASIL value is incorrect due to ASIL Decompose and Independence Requirement relationships.

**Abbreviation:** ASILDcmpIndp

**Description:** SafetyRequirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement) fail when an ASIL value is not equal to the ASIL value from the target element.

[IMAGE alt='' src='']

###### Illustration of the ASIL Decompose and Independence Requirement Relationships validation rule.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Constrained Element:</strong> Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement</p><p><strong>Constrained Element Filter:</strong> Safety Requirements that have outgoing Independence Requirement and ASIL Decompose relationships</p><p><strong>Severity:</strong> Error</p><p><strong>Error Message:</strong> The ASIL value is incorrect due to ASIL Decompose and Independence Requirement relationships.</p><p><strong>Abbreviation:</strong> ASILDcmpIndp</p><p><strong><ac:inline-comment-marker ac:ref="4ec2338e-450d-4c5c-ba3f-73b7e83b05be">Description</ac:inline-comment-marker>:</strong> <ac:inline-comment-marker ac:ref="0d822689-75ff-4156-8c69-243abb7140f1">Safety</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="f3928e45-f228-4dde-a6cd-05924794cbb2"> Requirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement)</ac:inline-comment-marker> fail when an ASIL value is not equal to the ASIL value from the target element.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="ASIL_Decompose_and_Independence_Requirement_Relationships_validation_rule.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ASIL Decompose and Independence Requirement Relationships" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Illustration of the ASIL Decompose and Independence Requirement Relationships validation rule.</h6><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170466602 space=CSRA2024xR1 version=1 -->
## PAGE 00009: ASIL Decomposition

- page_id: `170466602`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466602/ASIL+Decomposition
- version_number: 1
- version_date: `2020-03-09T13:44:52.000+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Validation Rules
- labels: []

### NORMALIZED CONTENT

**Constrained Element:** Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement

**Constrained Element Filter:** Two Safety Requirements that have outgoing ASIL Decompose relationships to the same target element.

**Severity:** error

**Error Message:** The ASIL value is decomposed incorrectly.

**Abbreviation:** ASILDecompose

**Solvers**: Change ASIL to[correct ASIL value]

**Description:** Safety Requirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement) fail when they decompose the target element[CONFLUENCE_PAGE title='ASIL Decomposition' space='CSRA2024xR1']incorrectly.

[IMAGE alt='' src='']

###### Illustration of the ASIL Decomposition validation rule.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Constrained Element:</strong> Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement</p><p><strong style="letter-spacing: 0.0px;">Constrained Element Filter:</strong> Two <ac:inline-comment-marker ac:ref="e5c4b42a-bb82-48d8-9af8-19b21eda7ded">Safety</ac:inline-comment-marker> Requirements that have outgoing  ASIL Decompose relationships to the same target element.</p><p><strong style="letter-spacing: 0.0px;">Severity:</strong> error</p><p><strong style="letter-spacing: 0.0px;">Error Message:</strong> The ASIL value is decomposed incorrectly.</p><p><strong style="letter-spacing: 0.0px;">Abbreviation:</strong> ASILDecompose</p><p><strong style="letter-spacing: 0.0px;">Solvers</strong>: <span style="letter-spacing: 0.0px;">Change ASIL to </span><span class="error" style="letter-spacing: 0.0px;">[correct ASIL value]</span></p><p><strong style="letter-spacing: 0.0px;">Description:</strong> <ac:inline-comment-marker ac:ref="0c636991-231b-474e-bad6-ebe98c3048b5">Safety</ac:inline-comment-marker> Requirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement) fail when they <ac:link><ac:link-body>decompose the target <span class="inline-comment-marker">element</span></ac:link-body><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ASIL Decomposition" /></ac:link><ac:inline-comment-marker ac:ref="b1ca6d06-75ac-4a66-9b46-f2841eb3a344"> incorrectly</ac:inline-comment-marker>.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="ASIl_Decomposition_validation_rule.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ASIL Decomposition" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(94,108,132);">Illustration of the ASIL Decomposition validation rule.</span></h6><p><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170466705 space=CSRA2024xR1 version=1 -->
## PAGE 00010: Asset

- page_id: `170466705`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466705/Asset
- version_number: 1
- version_date: `2024-04-18T09:23:23.443+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

3

**Asset**

Asset is an object that has value or contributes to value. It has has one or more cybersecurity properties whose compromise can lead to one or 
more damage scenarios.

**Confidentiality**

A property that contains sensitive information that should not be disclosed to unauthorized entities.

**Integrity**

Guarding against improper information modification or destruction. It includes ensuring information non-repudiation and authenticity. Quality of being complete and unaltered.

**Availability**

Property of being accessible and usable on demand by an authorized entity.

##### Creating an Asset

An Asset must be created in the context of an Item.

To create an asset do one of the following:

- To create an Asset using an Item

1. In the Containment tree, right-click an Item and select Create Element . [ATTACHMENT filename='1 ClickCreateElement.png']
2. In the dialog, expand **ISO 21434**and select **Asset**. [ATTACHMENT filename='Create Asset_Menu.png']
3. Name the created Asset in the Containment tree and press Enter. The Asset has the prefix **AS**, which denotes that the created element is an Asset; the number 1 indicates that it is the first Asset created. [ATTACHMENT filename='2 BreakingRequestAssetCreated.png']

- To create an Asset using the Item Table

1. In the Item Table, double-click to select a Member(s) or Boundary Member(s).
2. Right-click and select Security>Add an Asset to the Item. [ATTACHMENT filename='Adding asset to the item.png']
3. Name the created Asset in the Containment tree and press Enter. The Asset has the prefix**AS**,which denotes that the created element is an Asset; the number**5**indicates that it is the fifth Asset created. 
 
[IMAGE alt='' src=''] If you select an already added Member(s) or Boundary Member(s) to add as an underlying element, the **Add as an Asset to the Item** command will be unavailable. 
 
[IMAGE alt='' src='']The following notification message appears at the bottom right corner of the modeling tool once the asset is created. The message also provides a hyperlink to the item under which the asset is created. 
 
[IMAGE alt='' src=''] After creating an asset, it is beneficial to find its location in the model tree by performing one of the following:Right-click the asset, and, from the shortcut menu, choose the**Select in Containment Tree**command.Select the asset and press Alt+B.

##### Creatingan Asset from a System Diagram

To create an asset from a system diagram

1. In the system diagram, right-click an element(s) and select **Security>Add as an Asset. 
 
[IMAGE alt='' src='']** Once you add a system diagram element as an asset, a legend appears at the top right corner of the element. 
 
[IMAGE alt='' src='']
2. From the Select Elements dialog, select the item you want to add an asset under and click OK . [IMAGE alt='' src='']
3. Name the created Asset in the Containment tree and press Enter. The Asset has the suffix **AS**, which denotes that the created element is an Asset; the number **6**indicates that it is the sixth Asset created. 
 
[IMAGE alt='' src=''] If you select an already added system diagram element(s) to add as an asset, the Select Elements dialog will exclude the item to which the selected element was linked earlier.The following notification message appears at the bottom right corner of the modeling tool once the asset is created. The message also provides a hyperlink to the item under which the asset is created. 
 
[IMAGE alt='' src=''] ****

##### Creating an Asset Table

An Asset Table is automatically created while creating an Item. An Asset Table should always be linked to an Item to be compliant with the standard. You can also manually create an Asset Table.

[IMAGE alt='' src='']

If you create a new project using the**ISO 21434 Project**template, then an**Asset Table**already exists in the**2.1 Items & Assets Definition**package.

To create an Asset Table

1. In the Containment tree, right-click **Items & Assets Definition** and select**Create Diagram.** An Asset Table can be created under both Package and Item. **[IMAGE alt='' src='']******
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Asset Table**. [IMAGE alt='' src='']
  - In the search tab, type the keyword asset and then select Asset Table. 
 
[IMAGE alt='' src=''] The Asset Table is displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='2 ContainmentTreeAssetsTable.png']

##### Adding an Asset to the Asset Table

To add a new Asset to the Asset Table

1. In the Asset Table, click Add New. A row is added in the Asset table, which shows the new Asset. [IMAGE alt='' src='']
2. In the newly created Asset's row and in the Name column, double-click the designated cell to name the Asset. [ATTACHMENT filename='2 AddingBreakingRequestAsset.png']

##### Adding an Underlying Element

To add an underlying element for the asset do one of the following:

- To add an Underlying Element from the Asset Table

- From the Containment tree, drag the Underlying Element and drop it in the designated cell of the **Underlying Element**column and the required Asset's row. 
 
[IMAGE alt='' src=''] You can also drag and drop SysML Elements (such as Connector, port, etc.) from the Containment tree to the Asset Table.To add multiple Underlying Elements in the Asset Table, hold the Ctrl key on the keyboard to select multiple Underlying Elements from the Containment tree. Drag and drop the selected Underlying Elements into the required cell.
- To add an Underlying Element from the Item Table
  1. In the Item Table, double-click to select a Member(s) or Boundary Member(s).
  2. Right-click and select Security>Add to an existing asset. 
 
[IMAGE alt='' src='']
  3. From the Select Elements dialog, select the Asset you want to add the underlying element to and click OK . [ATTACHMENT filename='Select Elements dialog.png']

##### Adding an Underlying Element from a System Diagram

To add an Underlying Element for the asset in a system diagram

1. In the system diagram, right-click an element(s) and select Security>Add to an existing Asset. 
 
[IMAGE alt='' src='']
2. From the Select Elements dialog, select the Asset you want to add the element to and click OK . [IMAGE alt='' src='']

##### Assigning CIA properties

To assign CIA properties in the Asset Table

- Double-click each cell , namely Confidentiality , Integrity, and Availability in the Asset row. From the drop-down list, select the CIA properties. [ATTACHMENT filename='CIA property selection.png'] [ATTACHMENT filename='CIA property selected.png']

##### Asset Table Example 
 
[IMAGE alt='' src='']

#### INFO: References

References

- NIST-Confidentiality .
- Security and Privacy Controls for Information Systems and Organizations
- Engineering Trustworthy Secure Systems
- Engineering Trustworthy Secure Systems

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="ef31c9bf-152a-4aec-94ef-ec768faf3b0b"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Asset</strong></p><p>Asset is an object that has value or contributes to value. <span style="color: rgb(23,43,77);">It has has one or more cybersecurity properties whose compromise can lead to one or</span><br /><span style="color: rgb(23,43,77);">more damage scenarios.</span></p><p><strong>Confidentiality</strong></p><p>A property that contains sensitive information <span style="color: rgb(23,43,77);">that should not be disclosed</span> to unauthorized entities.</p><p><strong>Integrity</strong></p><p>Guarding against improper information modification or destruction. It includes ensuring information non-repudiation and authenticity. Quality of being complete and unaltered.</p><p><strong>Availability</strong></p><p>Property of being accessible and usable on demand by an authorized entity.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="4ee9e7c3-f470-4cb4-8e64-0673e1b9ca71">Creating an Asset</ac:inline-comment-marker></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4e545fa2-bd88-48e6-b89a-d462301947ac"><ac:rich-text-body><p><span style="color: rgb(62,63,64);"> An Asset must be created in the context of an Item.</span></p></ac:rich-text-body></ac:structured-macro><p>To create an asset do one of the following:</p><ul><li>To create an Asset using an Item</li></ul><hr /><ol><li>In the Containment tree, right-click an Item and select <strong>Create Element</strong>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><strong><br /><br /></strong></li><li class="auto-cursor-target"><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Asset</strong>.<br /></span><br /><ac:image><ri:attachment ri:filename="Create Asset_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></li><li class="auto-cursor-target">Name the created Asset in the Containment tree and press Enter. The Asset has the prefix <span><strong>AS</strong>,</span><span> </span>which denotes that the created element is an Asset; the number<span> </span><strong>1</strong><span> </span>indicates that it is the first Asset created.<br /><br /><ac:image><ri:attachment ri:filename="2 BreakingRequestAssetCreated.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></li></ol><ul><li>To create an Asset using the Item Table</li></ul><hr /><ol><li>In the Item Table, double-click to select a Member(s) or Boundary Member(s).</li><li>Right-click and select <strong>Security&gt;Add an Asset to the Item.</strong><br /><br /><ac:image><ri:attachment ri:filename="Adding asset to the item.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></li><li><p>Name the created Asset in the Containment tree and press Enter. The Asset has the prefix<span> <strong>AS</strong>,</span><span> </span><span>which denotes that the created element is an Asset; the number</span><span> <strong>5</strong></span><span> </span><span>indicates that it is the fifth Asset created.<br /><br /><ac:image><ri:attachment ri:filename="Containment Tree-New Asset.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="05e3955a-d037-438f-bf78-d0bd0b609e7e"><ac:rich-text-body><ul><li>If you select an already added Member(s) or Boundary Member(s) <ac:inline-comment-marker ac:ref="5473c06e-3b6f-46ca-bf52-2fae0b99108b">to add as an underlying element</ac:inline-comment-marker>, the <strong>Add as an Asset to the Item</strong> command will be unavailable.<br /><br /><ac:image><ri:attachment ri:filename="Add asset command- unavailable.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></li><li>The following notification message appears at the bottom right corner of the modeling tool once the asset is created. The message also provides a hyperlink to the item under which the asset is created.<br /><br /><ac:image><ri:attachment ri:filename="New Asset Added-Message.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="500928e5-b5aa-4deb-9f12-f5f3dccc4ed1"><ac:rich-text-body><p><span style="color: rgb(51,51,51);">After creating an asset, it is beneficial to find its location in the model tree by performing one of the following:</span></p><ul><li><span style="color: rgb(51,51,51);">Right-click the asset, and, from the shortcut menu, choose the<span> </span></span><strong>Select in Containment Tree</strong><span style="color: rgb(51,51,51);"><span> </span>command.</span></li><li><span style="color: rgb(51,51,51);">Select the asset and press Alt+B.</span></li></ul></ac:rich-text-body></ac:structured-macro></li></ol><h3><span>Creating </span><span>an Asset from a System Diagram</span></h3><p>To create an asset from a system diagram</p><hr /><ol><li><p class="auto-cursor-target">In the system diagram, right-click an element(s) and select <strong>Security&gt;Add as an Asset.<br /><br /><ac:image><ri:attachment ri:filename="Add an Asset-Sys Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /></strong></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6f92a462-f533-4238-b4cd-c4eee2c90a93"><ac:rich-text-body><p>Once you add <ac:inline-comment-marker ac:ref="8aa738cc-f1ab-4d55-84c7-9af64ed6f66a">a</ac:inline-comment-marker> system diagram element as an asset, a legend appears at the top right corner of the element.<br /><br /><ac:image><ri:attachment ri:filename="Asset_Legend.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>From the <strong>Select Elements</strong> dialog, select the item you want to add an asset under and click <strong>OK</strong>.<br /><br /><strong><ac:image><ri:attachment ri:filename="Select Elements-Sys Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /></strong></li><li><p>Name the created Asset in the Containment tree and press Enter. The Asset has the suffix <strong>AS</strong>, which denotes that the created element is an Asset; the number <strong>6 </strong>indicates that it is the sixth Asset created.<br /><br /><ac:image><ri:attachment ri:filename="Containment Tree-New Asset-Sys Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="50906262-b8ec-443d-a002-779e4dfa12ad"><ac:rich-text-body><ul><li>If you select an already added system diagram element(s) to <ac:inline-comment-marker ac:ref="00f367b6-68e9-4af0-a40a-f882046a7c7d">add as an asset,</ac:inline-comment-marker> the Select Elements dialog will exclude the item to which the selected element was linked earlier.</li><li>The following notification message appears at the bottom right corner of the modeling tool once the asset is created. The message also provides a hyperlink to the item under which the asset is created.<br /><br /><ac:image ac:thumbnail="true" ac:height="105"><ri:attachment ri:filename="New Asset Added-Message-Sys Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><p><strong><span> </span></strong></p></li></ol><h3>Creating an Asset Table</h3><p>An Asset Table is automatically created while creating an Item. An Asset Table should always be linked to an Item to be compliant with the standard. You can also manually create an Asset Table.</p><p><ac:image><ri:attachment ri:filename="Automatically created Asset Table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="17d8aa92-df27-4391-9f75-ae822300267f"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color: rgb(23,43,77);">, then an<span> </span><strong>Asset Table<span> </span></strong>already exists in the<span> </span><strong>2.1 Items &amp; Assets Definition</strong><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><span style="letter-spacing: 0.0px;">To create an Asset Table</span></p><hr /><ol><li><p>In the Containment tree, right-click <strong style="text-align: left;">Items &amp; Assets Definition</strong> and select<strong><span> </span>Create Diagram.<br /></strong></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ef7e122f-9fc2-4ffa-9dbd-87e176e3ef6a"><ac:rich-text-body><p>An Asset Table can be created under both Package and Item.</p></ac:rich-text-body></ac:structured-macro><p><strong><ac:image><ri:attachment ri:filename="Create Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /></strong><strong><br /></strong></p></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Asset Table</strong>.</span><br /><strong><br /><ac:image><ri:attachment ri:filename="Asset Table_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword asset and then select<span> </span><strong>Asset Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="174"><ri:attachment ri:filename="Asset Table_Menu_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></strong> The Asset Table is displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="2 ContainmentTreeAssetsTable.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></li></ul></li></ol><h3>Adding an Asset to the Asset Table</h3><p>To add a new Asset to the Asset Table</p><hr /><ol><li>In the Asset Table, click<span> </span><strong>Add New. </strong>A row is added in the Asset table, which shows the new Asset.<strong><br /><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></strong></li><li>In the newly created Asset's row and in the <strong>Name </strong>column, double-click the designated cell to name the Asset.<br /><br /><ac:image><ri:attachment ri:filename="2 AddingBreakingRequestAsset.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></li></ol><h3>Adding an Underlying Element</h3><p>To add an underlying element for the asset do one of the following:</p><ul><li>To add an Underlying Element from the Asset Table</li></ul><hr /><ul><li><p>From the Containment tree, drag the Underlying Element and drop it in the designated cell of the <strong>Underlying Element </strong>column and the required Asset's row.<br /><br /><ac:image><ri:attachment ri:filename="1 DragAndDropUnderlyingElement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1eb723ed-fb21-4e78-9c8f-fa7037b55b2f"><ac:rich-text-body><ul><li>You can also drag and drop SysML Elements (such as Connector, port, etc.) from the Containment tree to the Asset Table.</li><li>To add multiple Underlying Elements in the Asset Table, hold the Ctrl key on the keyboard to select multiple Underlying Elements from the Containment tree. Drag and drop the selected Underlying Elements into the required cell.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>To add an Underlying Element from the Item Table<hr /><ol><li>In the Item Table, double-click to select a Member(s) or Boundary Member(s).</li><li>Right-click and select <strong>Security&gt;Add to an existing asset.<br /><br /><ac:image><ri:attachment ri:filename="Add to an existing asset.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></strong></li><li>From the <strong>Select Elements</strong> dialog, select the Asset you want to add the underlying element to and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></li></ol></li></ul><h3>Adding an Underlying Element from a System Diagram</h3><p>To add an Underlying Element for the asset in a system diagram</p><hr /><ol><li>In the system diagram, right-click an element(s) and select <strong>Security&gt;Add to an existing Asset.<br /><br /><ac:image><ri:attachment ri:filename="Add to an existing asset-Sys Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></strong></li><li>From the <strong>Select Elements</strong> dialog, select the Asset you want to add the element to and click <strong>OK</strong>.<strong><br /><br /><ac:image><ri:attachment ri:filename="Select Elements-add existing-Sys Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></strong></li></ol><h3><ac:inline-comment-marker ac:ref="dc55f102-972a-4620-8a54-36f519bb7a76">Assigning CIA properties</ac:inline-comment-marker></h3><p>To assign CIA properties in the Asset Table</p><hr /><ul><li>  Double-click each cell<span style="color: rgb(22,22,22);">, namely </span><strong>Confidentiality</strong>, <strong>Integrity, </strong>and <strong>Availability </strong>in the Asset row. From the drop-down list, select the CIA properties.<br /><br /><ac:image><ri:attachment ri:filename="CIA property selection.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /><ac:image><ri:attachment ri:filename="CIA property selected.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image></li></ul><h3>Asset Table Example<br /><br /><ac:image><ri:attachment ri:filename="Asset Table Example.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Asset" /></ri:attachment></ac:image><br /><br /></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="82562ffd-ad3e-4312-b7bb-e489b1d03ed8"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a href="https://csrc.nist.gov/glossary/term/confidentiality#:~:text=Confidentiality%20covers%20data%20in%20storage%2C%20during%20processing%2C%20and,to%20the%20authors%20of%20the%20linked%20Source%20publication">NIST-Confidentiality</a>.</li><li><a class="external-link" href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf">Security and Privacy Controls for Information Systems and Organizations</a></li><li><a class="external-link" href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf">Engineering Trustworthy Secure Systems</a></li><li><a class="external-link" href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf">Engineering Trustworthy Secure Systems</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170467026 space=CSRA2024xR1 version=1 -->
## PAGE 00011: Attack Path Step

- page_id: `170467026`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170467026/Attack+Path+Step
- version_number: 1
- version_date: `2024-04-29T08:07:11.152+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
- labels: []

### NORMALIZED CONTENT

An Attack Path Step is elementary action performed on the system component and could be reused in several threat scenarios.

##### Creating an Attack Path Step

To create an Attack Path Step

1. In the Containment tree, right-click**Attack Paths and Feasibility Ratings** and select Create Element . [ATTACHMENT filename='Create Element.jpg']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Attack Path****Step**. [ATTACHMENT filename='Attack Path Step Menu.png']
  - In the search tab, type the keyword attackand then select Attack Path Step. [IMAGE alt='' src='']
3. Name the created Attack Path Step in the Containment tree and press Enter. [ATTACHMENT filename='4 AttackPathStepCreated.png']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>An Attack Path Step is elementary action performed on the system component and could be reused in several threat scenarios.</p><h3>Creating an Attack Path Step</h3><p>To create an Attack Path Step</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click<strong> Attack Paths and Feasibility Ratings</strong> and select</span> <strong>Create Element</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Path Step" /></ri:attachment></ac:image><br /><strong style="text-align: left;"><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong><ac:inline-comment-marker ac:ref="20ef5502-d9cb-436b-a1f8-c4bc7c4853b1">Attack Path</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="20ef5502-d9cb-436b-a1f8-c4bc7c4853b1"> </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="20ef5502-d9cb-436b-a1f8-c4bc7c4853b1">Step</ac:inline-comment-marker></strong>.</span><br /><strong><br /></strong><ac:image><ri:attachment ri:filename="Attack Path Step Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Path Step" /></ri:attachment></ac:image><br /><strong><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword <span style="color: rgb(62,63,64);">attack<span> and </span></span>then select<span> </span><strong><ac:inline-comment-marker ac:ref="5b8c43fd-07fe-4f56-943d-16f221f1b7c8">Attack Path Step</ac:inline-comment-marker>.<br /><br /></strong><strong><ac:image><ri:attachment ri:filename="Attack Path Step Search Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Path Step" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Attack Path Step in the Containment tree and press Enter.<br /><br /></span><ac:image><ri:attachment ri:filename="4 AttackPathStepCreated.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Path Step" /></ri:attachment></ac:image></li></ol><h3><span style="color: rgb(62,63,64);"> </span></h3>
````

<!--NOMAGIC_PAGE id=170466989 space=CSRA2024xR1 version=1 -->
## PAGE 00012: Attack Potential Based Attack Path

- page_id: `170466989`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466989/Attack+Potential+Based+Attack+Path
- version_number: 1
- version_date: `2024-04-29T08:04:29.970+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
- labels: []

### NORMALIZED CONTENT

33

Attack Potential based method is supported by the ISO/IEC 18045 standard.

##### Creating an Attack Potential Based Attack Path

To create an Attack Potential Based Attack Path

1. In the Containment tree, right-click**Attack Paths and Feasibility Ratings**and select Create Element. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Attack Potential Based Attack Path**. [IMAGE alt='' src='']
  - In the search tab, type the keyword attack and then select **Attack Potential Based Attack Path** . 
 
[IMAGE alt='' src='']
3. Name the created Attack Potential Based Attack Path in the Containment tree and press Enter. The Attack Potential Based Attack Path has the prefix **AP**,which denotes that the created element is an an Attack Path (Manual or Potential-Based); the number**1** indicates that it is the first Attack Path (Manual or Potential-Based) created. 
 
**[IMAGE alt='' src='']**

##### Creating an Attack Potential Based Attack Path Table

If you create a new project using the**ISO 21434 Project**template, then a**Attack Potential Based Attack Path**tablealready exists in the**1.3 Attack Paths and Feasibility Ratings**package.

To create anAttack Potential Based Attack PathTable

1. In the Containment tree , right-click **Attack Paths and Feasibility Ratings** and select Create Diagram. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Attack Potential Based Attack Path Table**. [IMAGE alt='' src='']
  - In the search tab, type the keyword attack and then select **Attack Potential Based Attack Path** Table. 
 
[IMAGE alt='' src=''] The Attack Potential Based Attack Path Table is displayed in the diagram pane of the modeling tool. [IMAGE alt='' src='']

##### Adding an Attack Potential Based Attack Path to the Attack Potential Based Attack Path Table

Adding a new or existing Attack Potential Based Attack Path to the Attack Potential Based Attack Path Table is the same as adding a new or existing Manual Attack Path to the Manual Attack Path Table. To learn more about adding a Manual Attack Path to the Manual Attack Path Table, refer to [CONFLUENCE_PAGE title='Manual Attack Path' space='CSRA2024xR1'].

##### Adding Attack Path Steps

Attack path steps in an Attack Based Potential Attack Path table are added in the same as they are added in a Simple Attack Path table. To learn more about adding attack path steps in a Simple Attack Path table, refer to [CONFLUENCE_PAGE title='Manual Attack Path' space='CSRA2024xR1'].

##### Rating the Potential Attack core parameters

To rate the Potential Attack core parameters

- Double-click each cell's column namely **Elapsed Time, Specialist Expertise, Knowledge of Item/Component, Window of Opportunity,**and **Equipment** in the Attack Based Potential Attack Path's row and select the required option from the drop-down list. 
 
[IMAGE alt='' src='']

The Attack Feasibility Rating is calculated with help of core parameters viz. Elapsed Time, Specialist Expertise, Knowledge of Item/Component, Window of Opportunity, and Equipment. Each parameter has different grading system which has a numerical value assigned to it. These numerical values are based on the ISO/IEC 18045 standard.

The following table shows the assigned numerical values to each parameter. 
 
[IMAGE alt='' src='']

The numerical values are added together to calculate the Attack Feasibility Rating. Following is the formula used to calculate the Attack Feasibility Rating.

- Attack Feasibility Rating = Elapsed Time + Specialist Expertise+ Knowledge of Item/Component+ Window of Opportunity+ Equipment

The following table shows the numerical values assigned to the Attack Feasibility Rating.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="60ee50d5-fba1-43b2-aa1f-a4ffa04768d3"><ac:parameter ac:name="maxLevel">3</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>Attack Potential based method is supported by the ISO/IEC 18045 standard.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating an Attack Potential Based Attack Path</h3><p>To create an <span style="color: rgb(62,63,64);">Attack Potential Based Attack Path </span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click<span> </span><strong>Attack Paths and Feasibility Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Attack Potential Based Attack Path</strong>.<br /><br /></span><strong><ac:image><ri:attachment ri:filename="AP_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong>Attack Potential Based Attack Path</strong></span><strong>.<br /><br /><ac:image><ri:attachment ri:filename="AP_Menu_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Attack Potential Based Attack Path in the Containment tree and press Enter. The Attack Potential Based Attack Path has the prefix <span><strong>AP</strong>, </span>which denotes that the created element <ac:inline-comment-marker ac:ref="e2ccbbe1-1d06-4ff2-b453-088e481a1261">is an <span style="color: rgb(23,43,77);">an Attack Path (Manual or Potential-Based)</span></ac:inline-comment-marker>; the number<span> </span><strong style="text-align: left;">1</strong> indicates that it is the <ac:inline-comment-marker ac:ref="04adb341-47be-4092-8e66-59b49a92c088">first <span style="color: rgb(62,63,64);"><span style="color: rgb(23,43,77);">Attack Path (Manual or Potential-Based)</span></span></ac:inline-comment-marker> created.<br /><br /><strong><ac:image><ri:attachment ri:filename="AP_Created_Containment Tree.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image></strong><br /></span></li></ol><h3>Creating an Attack Potential Based Attack Path Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fa731bd7-f3e3-4691-8670-2f2ab9a94c52"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color: rgb(23,43,77);">, then a<span> <span style="color: rgb(62,63,64);"><strong>Attack Potential Based Attack Path </strong></span></span>table<span> </span>already exists in the<span> <strong>1.3 Attack Paths and Feasibility Ratings</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create an<span> Attack Potential Based Attack Path </span>Table</p><hr /><ol><li><ac:inline-comment-marker ac:ref="d3d2d78f-ade4-4c8d-862a-f017c198a2ea">In the Containment tree</ac:inline-comment-marker>, right-click<span> <span style="color: rgb(62,63,64);"><strong>Attack Paths and Feasibility Ratings</strong></span></span><span style="color: rgb(62,63,64);"> </span>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Attack Potential Based Attack Path Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="AP_Table_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong>Attack Potential Based Attack Path </strong></span><strong>Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="196"><ri:attachment ri:filename="AP_Table_Menu_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /><br /></strong>The Attack Potential Based Attack Path Table is displayed in the diagram pane of the modeling tool.<br /><br /><strong><ac:image><ri:attachment ri:filename="AP_Table_Created.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image></strong></li></ul></li></ol><h3>Adding an Attack Potential Based Attack Path to the Attack Potential Based Attack Path Table</h3><p>Adding a new or existing Attack Potential Based Attack Path to the Attack Potential Based Attack Path Table is the same as adding a new or existing Manual Attack Path to the Manual Attack Path Table. To learn more about adding a Manual <ac:inline-comment-marker ac:ref="093c246e-d7ef-483e-a8a4-364cff6ae8f1">Attack Path</ac:inline-comment-marker> to the Manual Attack Path Table, refer to <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ac:link>.</p><h3>Adding Attack Path Steps</h3><p>Attack path steps in an Attack Based Potential Attack Path table are added in the same as they are added in a Simple Attack Path table. To learn more about adding attack path steps in a Simple Attack Path table, refer to <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ac:link>.</p><h3>Rating the Potential Attack core parameters</h3><p>To rate the Potential Attack core parameters</p><hr /><ul><li><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="54784e0f-7c81-4b6b-a155-6e73ca26b34d">Double-click each cell's</ac:inline-comment-marker> column</span><span style="color: rgb(22,22,22);"><span> namely <strong>Elapsed Time, Specialist Expertise, Knowledge of Item/Component, Window of Opportunity, </strong>and <strong>Equipment</strong> in the Attack Based Potential Attack Path's </span></span><span style="color: rgb(62,63,64);">row and select the required option from the drop-down list.<br /><br /><ac:image><ri:attachment ri:filename="Rating the Potential Attack core parameters.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /></span></li></ul><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8bde7915-02a8-4097-a418-ea8eff9333d1"><ac:rich-text-body><p>The Attack Feasibility Rating is calculated with help of core parameters viz. <span style="color: rgb(22,22,22);">Elapsed Time, Specialist Expertise, Knowledge of Item/Component, Window of Opportunity, and Equipment. Each parameter has different grading system which has a numerical value assigned to it. These numerical values are based on the ISO/IEC 18045 standard. </span></p><p><span style="color: rgb(22,22,22);">The following table shows the assigned numerical values to each parameter.<br /><br /><ac:image><ri:attachment ri:filename="Attack Feasibility Rating _Parameters_Table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image><br /><br /></span></p><p><span style="color: rgb(22,22,22);">The numerical values are added together to calculate the  Attack Feasibility Rating. Following is the formula used to calculate the Attack Feasibility Rating.</span></p><ul><li><span>Attack Feasibility Rating = Elapsed Time + <span style="color: rgb(22,22,22);">Specialist Expertise</span>+ <span style="color: rgb(22,22,22);">Knowledge of Item/Component</span>+ <span style="color: rgb(22,22,22);">Window of Opportunity</span>+ <span style="color: rgb(22,22,22);">Equipment</span></span></li></ul><p>The <ac:inline-comment-marker ac:ref="17f1a584-e363-405b-aea7-2dbc939069ac">following table</ac:inline-comment-marker> shows the numerical values assigned to the Attack Feasibility Rating.</p><p><ac:image ac:thumbnail="true" ac:height="101"><ri:attachment ri:filename="Attack Feasibility Rating values.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Attack Potential Based Attack Path" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466443 space=CSRA2024xR1 version=1 -->
## PAGE 00013: Cameo Safety and Reliability Analyzer

- page_id: `170466443`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466443/Cameo+Safety+and+Reliability+Analyzer
- version_number: 1
- version_date: `2024-01-31T07:47:05.734+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

238007870

100.00002%

238007872

238007871

INLINE

The Cameo Safety and Reliability Analyzer Plugin provides risk analysis during the entire product modeling process. For now, the plugin is designed to analyze risks in the modeling of medical devices and is build on the **Medical devices – Application of risk management to medical devices (ISO 14971:2007, Corrected version 2007-10-01)** standard.

Risk analysis adds the following value:

- Ability to demonstrate that risks are addressed by safety requirements/risk control measures.
- Increased agility between Risk/Hazard Analysis, Design, and FMEA: a frequent exchange of information between risks/hazards and FMEA cross-functional teams, along with shorter development cycles followed by shorter risk analysis and FMEA.
- Ensured traceability of risks to requirements, design elements, critical quality attributes (CQA) and other artifacts, traceability from design elements to FMEA, two-way traceability between FMEA and risks/hazard analysis.
- Performing safety analysis: automatic Risk Score Number calculations, and risk reduction analysis.
- Impact Analysis : validation rules highlight risks with high or medium risk score, risks without risk control measures, failure modes that need attention from hazard analysis cross-functional team and have not been addressed yet, etc.

The Cameo Safety and Reliability Analyzer Plugin can be used together with the [CONFLUENCE_PAGE title='ISO 26262 Functional Safety' space='CSRA2024xR1']. The plugin supports the ISO 26262 standard which is derived from IEC 61508. ISO 26262 is intended for electric and/or electronic systems in production vehicles. This includes driver assistance, propulsion, and vehicle dynamics control systems. The goal of ISO 26262 is to ensure safety throughout the lifecycle of automotive systems and equipment.

[Risk Analysis and Assessment Modeling Language (RAAML)](https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML) is an extension of SysML that supports safety and reliability analysis. RAAML is a set of 7 profiles and 6 libraries. These profiles and libraries are divided mainly into 4 separate domains: FMEA, FTA, ISO 26262, and STPA. There are also sets of Core and General profiles and libraries. These sets can be used as they are or you can derive your own set of safety and reliability methodologies and stereotypes based on the domain and usage. For example, the Systems Cybersecurity Designer plugin is based on RAAML, but stereotypes and methodologies are created with the help of available profiles and libraries. The three plugins present in this guide, ISO 26262, Systems Cybersecurity Designer, and Fault Tree Analysis, are based on the RAAML 1.0 standard.

To learn more about the product, see:

948190294

INLINE

**Docs of other versions**

- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA2022x']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA2021xR2']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA2021xR1']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA2021x']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA190SP4']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA190SP3']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA190SP2']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA190SP1']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA190']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="64dbd221-651e-4b60-b6cb-50871801061e"><ac:parameter ac:name="id">238007870</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="132ce5f7-fc66-49d3-b10c-9981e6e8c0a6"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">238007872</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="de6fccef-c233-4e55-83ac-6701a9eebaec"><ac:parameter ac:name="id">238007871</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="8afe5a5d-5361-441f-ad6e-27e8cda271d0"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>The Cameo Safety and Reliability Analyzer Plugin provides risk analysis during the entire product modeling process. For now, the plugin is designed to analyze risks in the modeling of medical devices and is build on the <strong>Medical devices – Application of risk management to medical devices (ISO 14971:2007, Corrected version 2007-10-01)</strong> standard.</p><p>Risk analysis adds the following value:</p><ul><li><strong>Ability to demonstrate</strong> that risks are addressed by safety requirements/risk control measures.</li><li><strong>Increased agility</strong> between Risk/Hazard Analysis, Design, and FMEA: a frequent exchange of information between risks/hazards and FMEA cross-functional teams, along with shorter development cycles followed by shorter risk analysis and FMEA.</li><li><strong>Ensured traceability </strong>of risks to requirements, design elements, critical quality attributes (CQA) and other artifacts, traceability from design elements to FMEA, two-way traceability between FMEA and risks/hazard analysis.</li><li><strong>Performing </strong>safety analysis: automatic Risk Score Number calculations, and risk reduction analysis.</li><li><strong>Impact Analysis</strong>: validation rules highlight risks with high or medium risk score, risks without risk control measures, failure modes that need attention from hazard analysis cross-functional team and have not been addressed yet, etc.</li></ul><p><ac:inline-comment-marker ac:ref="cab79aa7-abe2-4bc4-ad24-8f5b685fd555">The Cameo Safety and Reliability Analyzer Plugin can be used tog</ac:inline-comment-marker>ether with the <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 26262 Functional Safety" /><ac:plain-text-link-body><![CDATA[ISO 26262 Functional Safety Plugin]]></ac:plain-text-link-body></ac:link>. The plugin supports the ISO 26262 standard which is derived from IEC 61508. ISO 26262 is intended for electric and/or electronic systems in production vehicles. <span style="color: rgb(62,63,64);">This includes driver assistance, propulsion, and vehicle dynamics control systems. The goal of ISO 26262 is to ensure safety throughout the lifecycle of automotive systems and equipment.</span></p><p><a href="https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML">Risk Analysis and Assessment Modeling Language (RAAML)</a> is an extension of SysML that supports safety and reliability analysis. RAAML is a set of 7 profiles and 6 libraries. These profiles and libraries are divided mainly into 4 separate domains: FMEA, FTA, ISO 26262, and STPA. There are also sets of Core and General profiles and libraries. These sets can be used as they are or you can derive your own set of safety and reliability methodologies and stereotypes based on the domain and usage. For example, the Systems Cybersecurity Designer plugin is based on RAAML, but stereotypes and methodologies are created with the help of available profiles and libraries. The three plugins present in this guide, ISO 26262, Systems Cybersecurity Designer, and Fault Tree Analysis, are based on the RAAML 1.0 standard.</p><p><span style="color: rgb(62,63,64);">To learn more about the product, see:</span></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="69a217e0-df60-423a-a6fd-e45dd8643645" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="05a3efe0-b071-4d0f-9fb9-00b7a4cb0136"><ac:parameter ac:name="id">948190294</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="6371a64a-3e79-4057-9184-c0c10b4163b8"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><strong>Docs of other versions</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2022x" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 2022x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2021xR2" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 2021x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2021xR1" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 2021x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2021x" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 2021x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA190SP4" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 19.0 SP4]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA190SP3" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 19.0 SP3]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA190SP2" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 19.0 SP2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA190SP1" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 19.0 SP1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA190" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer 19.0]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466469 space=CSRA2024xR1 version=1 -->
## PAGE 00014: Cloning FMEA Table rows

- page_id: `170466469`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466469/Cloning+FMEA+Table+rows
- version_number: 1
- version_date: `2024-03-13T08:10:18.091+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > Reliability analysis using FMEA
- labels: []

### NORMALIZED CONTENT

Usually, FMEA Tables contain a number of rows that only slightly differ from each other. To create new rows more quickly, you can clone existing FMEA Table rows with their column values. The cloning feature allows you to clone one or multiple rows at a time, and select which column values should be cloned.

To clone existing FMEA table rows

1. Select The FMEA Table row(s) you want to clone. To select multiple rows, hold down the Ctrl key. If you want to select several consecutive rows, select the first row in a sequence, then hold down the Shift key, and select the last row in a sequence.
2. Do one of the following:
  - In the table toolbar, click [ATTACHMENT filename='clone_row.png'] .
  - Right-click the selected rows, and, from the menu, select Clone Row .
3. In the **Select Properties** dialog, select the columns you would like to clone. By default, all the columns are selected, as shown in the figure below. To clear the check boxes of all table columns, click **Clear All**, and, to select all table columns, click **Select All**. [ATTACHMENT filename='select_properties_dialog.png']
4. Click OK .

After following the procedure described above, the selected rows of an FMEA Table are cloned reusing the values of the columns selected in the **Select Properties** dialog. As a result, new FMEA Items are created in the package specified as the scope of an FMEA Table, and new table rows (clones) are added for each new FMEA Item. By default, the names of new FMEA Items are the same as the names of the FMEA Items described in the source rows with the word *clone* added as a suffix. See the *Name* column of the sample FMEA Table displayed below.

[IMAGE alt='' src='']

###### The sample FMEA Table demonstrates the behavior of the row cloning feature. The selected rows (highlighted in blue) have been cloned, and each row clone appears right below the row from which it was cloned.

#### TIP: Recommendation

Recommendation

It is recommended that you change the names of the new FMEA Items that are created by cloning table rows to meaningful ones.

**Sample model**

The model used for the figures of this page is the *Medical FMEA and Hazard Analysis* sample model that comes with Cameo Safety and Reliability Analyzer plugin. To open this model do one of the following

- Download [ATTACHMENT filename='Medical FMEA and Hazard Analysis.mdzip'] .
- Open the model from the < install_root >\ samples \ Safety and Reliability Analysis directory.

**Related pages**

- [CONFLUENCE_PAGE title='Reliability analysis using FMEA' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Describing FMEA Items' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>Usually, FMEA Tables contain a number of rows that only slightly differ from each other. To create new rows more quickly, you can clone existing FMEA Table rows with their column values. The cloning feature allows you to clone one or multiple rows at a time, and select which column values should be cloned.</p><p><br />To clone existing FMEA table rows</p><hr /><ol><li>Select The FMEA Table row(s) you want to clone. To select multiple rows, hold down the Ctrl key. If you want to select several consecutive rows, select the first row in a sequence, then hold down the Shift key, and select the last row in a sequence.</li><li><p>Do one of the following:</p><ul><li class="auto-cursor-target">In the table toolbar, click <ac:image><ri:attachment ri:filename="clone_row.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cloning FMEA Table rows" /></ri:attachment></ac:image>.</li><li class="auto-cursor-target">Right-click the selected rows, and, from the menu, select <strong>Clone Row</strong>.</li></ul></li><li><p>In the <strong>Select Properties</strong> dialog, select the columns you would like to clone. By default, all the columns are selected, as shown in the figure below. To clear the check boxes of all table columns, click <strong>Clear All</strong>, and, to select all table columns, click <strong>Select All</strong>.<br /><br /></p><ac:image><ri:attachment ri:filename="select_properties_dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cloning FMEA Table rows" /></ri:attachment></ac:image><br /><br /></li><li>Click <strong>OK</strong>.</li></ol><p><br />After following the procedure described above, the selected rows of an FMEA Table are cloned reusing the values of the columns selected in the <strong>Select Properties</strong> dialog. As a result, new FMEA Items are created in the package specified as the scope of an FMEA Table, and new table rows (clones) are added for each new FMEA Item. By default, the names of new FMEA Items are the same as the names of the FMEA Items described in the source rows with the word <em>clone</em> added as a suffix. See the <em>Name</em> column of the sample FMEA Table displayed below.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="cloning_FMEA_table_rows.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cloning FMEA Table rows" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The sample FMEA Table demonstrates the behavior of the row cloning feature. The selected rows (highlighted in blue) have been cloned, and each row clone appears right below the row from which it was cloned.</h6><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="d86133cc-03c0-4ad9-acc6-90c515ae0304"><ac:parameter ac:name="title">Recommendation</ac:parameter><ac:rich-text-body><p>It is recommended that you change the names of the new FMEA Items that are created by cloning table rows to meaningful ones.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Sample model</strong></p><p>The model used for the figures of this page is the <em>Medical FMEA and Hazard Analysis</em> sample model that comes with Cameo Safety and Reliability Analyzer plugin. To open this model do one of the following</p><ul><li>Download <ac:link><ri:attachment ri:filename="Medical FMEA and Hazard Analysis.mdzip"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Sample models" /></ri:attachment></ac:link>.</li><li>Open the model from the &lt;<em style="text-align: left;">install_root</em>&gt;\<em>samples</em>\<em>Safety and Reliability Analysis</em> directory.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Reliability analysis using FMEA" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing FMEA Items" /></ac:link></li></ul></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170467111 space=CSRA2024xR1 version=2 -->
## PAGE 00015: Collaborative modeling

- page_id: `170467111`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170467111/Collaborative+modeling
- version_number: 2
- version_date: `2024-05-08T14:01:17.530+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity
- labels: []

### NORMALIZED CONTENT

Team members can individually develop separate parts of a single model and then merge them together to form a complete model. In comparison to individual modeling, collaborative modeling is more effective and produces better results because each member employs his/her best skills and experience.

We offer you a server for your team's collaboration – [CONFLUENCE_PAGE title='Using Teamwork Cloud' space='MD2024xR1'], and [CONFLUENCE_PAGE title='Collaboration powered by 3DEXPERIENCE platform' space='MD2024xR1']collaboration capabilities powered by **3D**EXPERIENCE platform.

Both servers provide a repository for storing projects and users. They also support the management of users' permissions as well as sharing and versioning projects.

Projects stored in the server repository can be accessed through the network from multiple clients who have MagicDraw or any Cameo Suite product installed. Different users, depending on their role in a team or enterprise, can have different permissions to the projects.

The same model or even the same diagram can be accessed and modified in parallel. Every user may instantly obtain the newest version of the model as well as commit his/her own changes.

##### Basic concepts

For better understanding further material, get acquainted with basic concepts of collaborative modeling.

| Concept | Description |
| --- | --- |
| Repository | A place for storing projects and users managed by Teamwork Cloud. |
| User | A collaboration team member, who has credentials to log into Teamwork Cloud and holds permissions to access one or more server projects. |
| Teamwork Cloud project | A project stored in Teamwork Cloud repository. |
| Server project | A common name for Teamwork Cloud projects. |
| Version | A snapshot of a project at a particular point in time. A new version of a project is created after successful commit of changes made in this project. All versions of the same project have unique numbers. |
| Comment | An optional description about changes in a project version. |
| Tag | Information about the status of a project version (for example, approved or initially tested) or other. |
| Commit | A process of sending the changes made in the project to the server. Each commit creates a new project version. |
| Author | A user who has committed a particular project version. |
| Update | A process of getting from the server the latest version of a project you are working with. |
| Category | A concept for grouping projects in a Teamwork Cloud repository. |
| Locked item | A part of the model that can be edited by the user, who has locked it. Other users cannot edit locked items. The locks can be released during the commit of a new version. |
| Server project usage | Another server project used in the project you are working with. It can be a library, profile or regular project. |
| Branch | A duplicate of a server project version. Branching allows the users to work in parallel on the same project version. |
| Trunk | A permanent branch of a server project that is a base for all other branches. It cannot be deleted. |

##### Scenario to get started

Independent of what server your team or enterprise uses, we offer you to follow these steps to get started with collaborative modelling:

1. Obtain user's credentials. Creating users and deciding the access rights of the users against projects is an administrative task. For more information, see [CONFLUENCE_PAGE title='User Guide' space='TWCloud2024xR1'].
2. Log into a server.
3. Add a project to the server and/or open it.
4. Lock the elements you want to edit (to prevent other users could not change the elements you are working with) and edit them. You can skip this step if you are working in the [CONFLUENCE_PAGE title='Using Lock-Free Editing mode' space='MD2024xR1'].
5. Edit these elements and/or create new ones.
6. Commit the changes to the server so that other users could see these modifications.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Team members can individually develop separate parts of a single model and then merge them together to form a complete model. In comparison to individual modeling, collaborative modeling is more effective and produces better results because each member employs his/her best skills and experience.</p><p>We offer you a server for your team's collaboration – <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud]]></ac:plain-text-link-body></ac:link>, and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Collaboration powered by 3DEXPERIENCE platform" /><ac:link-body>collaboration capabilities powered by <strong>3D</strong>EXPERIENCE platform</ac:link-body></ac:link>.</p><p>Both servers provide a repository for storing projects and users. They also support the management of users' permissions as well as sharing and versioning projects.</p><p>Projects stored in the server repository can be accessed through the network from multiple clients who have MagicDraw or any Cameo Suite product installed. Different users, depending on their role in a team or enterprise, can have different permissions to the projects.</p><p>The same model or even the same diagram can be accessed and modified in parallel. Every user may instantly obtain the newest version of the model as well as commit his/her own changes.</p><h3>Basic concepts</h3><p>For better understanding further material, get acquainted with basic concepts of collaborative modeling.</p><table><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>Concept</th><th>Description</th></tr><tr class=""><td><h4>Repository</h4></td><td>A place for storing projects and users managed by Teamwork Cloud.</td></tr><tr class=""><td colspan="1"><h4>User</h4></td><td colspan="1">A collaboration team member, who has credentials to log into <span>Teamwork Cloud </span>and holds permissions to access one or more server projects.</td></tr><tr class=""><td><h4><span>Teamwork Cloud</span> project</h4></td><td>A project stored in <span>Teamwork Cloud</span> repository.</td></tr><tr class=""><td colspan="1"><h4>Server project</h4></td><td colspan="1">A common name for <span>Teamwork Cloud </span>projects.</td></tr><tr class=""><td colspan="1"><h4>Version</h4></td><td colspan="1"><p>A snapshot of a project at a particular point in time. A new version of a project is created after successful commit of changes made in this project. All versions of the same project have unique numbers.</p></td></tr><tr class=""><td colspan="1"><h4>Comment</h4></td><td colspan="1">An optional description about changes in a project version.</td></tr><tr class=""><td colspan="1"><h4>Tag</h4></td><td colspan="1"><p>Information about the status of a project version (for example, <em>approved</em> or <em>initially tested</em>) or other.</p></td></tr><tr class=""><td colspan="1"><h4>Commit</h4></td><td colspan="1">A process of sending the changes made in the project to the server. Each commit creates a new project version.</td></tr><tr class=""><td colspan="1"><h4>Author</h4></td><td colspan="1">A user who has committed a particular project version.</td></tr><tr class=""><td colspan="1"><h4>Update</h4></td><td colspan="1">A process of getting from the server the latest version of a project you are working with.</td></tr><tr class=""><td colspan="1"><h4>Category</h4></td><td colspan="1">A concept for grouping projects in a <span>Teamwork Cloud </span>repository.</td></tr><tr class=""><td colspan="1"><h4>Locked item</h4></td><td colspan="1"><p>A part of the model that can be edited by the user, who has locked it. Other users cannot edit locked items. The locks can be released during the commit of a new version.</p></td></tr><tr class=""><td colspan="1"><h4>Server project usage</h4></td><td colspan="1">Another server project used in the project you are working with. It can be a library, profile or regular project.</td></tr><tr class=""><td colspan="1"><h4>Branch</h4></td><td colspan="1">A duplicate of a server project version. Branching allows the users to work in parallel on the same project version.</td></tr><tr class=""><td colspan="1"><h4>Trunk</h4></td><td colspan="1">A permanent branch of a server project that is a base for all other branches. It cannot be deleted.</td></tr></tbody></table><h3>Scenario to get started</h3><p><span style="color: rgb(64,64,64);">Independent of what server your team or enterprise uses, we offer you to follow these steps to get started with collaborative modelling:<br /></span></p><ol><li><p>Obtain user's credentials.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fdf54cab-334a-4c97-bf90-2e090c9170ce"><ac:rich-text-body><p>Creating users and deciding <span style="color: rgb(64,64,64);">the access rights of the users against projects is an administrative task. For more information, see <ac:link><ri:page ri:space-key="TWCloud2024xR1" ri:content-title="User Guide" /><ac:plain-text-link-body><![CDATA[Teamwork Cloud User Guide]]></ac:plain-text-link-body></ac:link>. <br /></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Log into a server.</li><li>Add a project to the server and/or open it.</li><li><p class="auto-cursor-target">Lock the elements you want to edit (to prevent other users could not change the elements you are working with) and edit them.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d67b2692-c71a-45d6-bc55-e968302f380f"><ac:rich-text-body><p>You can skip this step if you are working in the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Lock-Free Editing mode" /><ac:plain-text-link-body><![CDATA[Lock-Free Editing mode]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Edit these elements and/or create new ones.</li><li>Commit the changes to the server so that other users could see these modifications.</li></ol>
````

<!--NOMAGIC_PAGE id=170466645 space=CSRA2024xR1 version=1 -->
## PAGE 00016: Concept

- page_id: `170466645`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466645/Concept
- version_number: 1
- version_date: `2024-04-18T08:03:35.174+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity
- labels: []

### NORMALIZED CONTENT

##### TARA process

[IMAGE alt='' src='']

###### TARA process

The TARA (Threat Analysisand Risk Assessment) process is described in Chapter 15 of ISO/SAE 21434:2021. It is a methodology used to identify and assess cyber security threats and vulnerabilities beginning with the design phase of a product.

The following is the standard procedure followed in TARA:

1. Define the items you want to study. These items are components or sets of components of the considered system.
2. For each item identify t he assets to be protected and allocate CIA (Confidentiality, Integrity, and Availability) properties for each asset.
3. Define any damage scenarios that can affect a vehicle system/function or a road user. After identifying those damage scenarios, you need to rate their impact in terms of Safety, Financial, Operational, and Privacy.
4. Create threat scenarios that can lead to the identified damage scenarios and rate them in terms of feasibility. Threat scenarios that lead to an asset compromise can be described by one or several attack paths. Each attack path is rated with an attack feasibility value.
5. Assess the risks. The risk is the probability that the threat will occur and entails the damage scenario impact. The risk valu e is automaticallycomputed based on this formula from ISO/SAE 21434:2021, Annex H: Risk = 1 + Impact x Feasibility.
6. According to the computed risk value, decide the risk treatment for each threat scenario: Retain, Reduce, Share, or Avoid. Depending on the risk treatment decision, determine cybersecurity claims or goals that will eventually be detailed in the cybersecurity requirements (functional, technical, hardware, or software type).

An Item is a part of the system architecture to be protected. An Item with a Functional Cybersecurity Concept (output of the study) is the system architecture with additional requirements and claims that ensures a secure system.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>T<ac:inline-comment-marker ac:ref="bf287acc-bf9b-439c-9577-f57d30a2a79c">ARA process</ac:inline-comment-marker></h3><p style="text-align: center;"><ac:image><ri:attachment ri:filename="TARA_Process_Image.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Concept" /></ri:attachment></ac:image></p><h6 style="text-align: center;">TARA process</h6><p>The TARA (Threat <span style="color: rgb(23,43,77);">Analysis </span>and Risk Assessment) process is described in Chapter 15 of ISO/SAE 21434:2021. It is a methodology used to identify and assess cyber security threats and vulnerabilities beginning with the design phase of a product.</p><p>The following is the standard procedure followed in TARA:</p><ol style="text-align: left;"><li>Define the items you want to study. These items are components or sets of components of the considered system.</li><li>For each item identify t<ac:inline-comment-marker ac:ref="af0ba61b-9718-49e9-a668-3aa8aeead8c3"><ac:inline-comment-marker ac:ref="c05e0205-3381-4c26-8d3b-1c549d91a8fd">he assets</ac:inline-comment-marker></ac:inline-comment-marker> to be protected and allocate CIA (Confidentiality, Integrity, and Availability) properties for each asset.</li><li><ac:inline-comment-marker ac:ref="3052ec32-3de2-449c-bfd4-0a2305aae43e"><ac:inline-comment-marker ac:ref="2c6a74a6-ec8c-4b17-9c7f-c36e00ca043c">Define any dama</ac:inline-comment-marker>ge scenarios</ac:inline-comment-marker> that can affect a vehicle system/function or a road user. After identifying those damage scenarios, you need to rate their impact in terms of Safety, Financial, Operational, and Privacy.</li><li>Create threat scenarios that can lead to the identified damage scenarios and rate them in terms of feasibility. Threat scenarios that lead to an asset compromise can be described by one or several attack paths. Each attack path is rated with an attack feasibility value.</li><li>Assess the risks. The risk is the probability that the threat will occur and entails the damage scenario impact. The risk valu<ac:inline-comment-marker ac:ref="17f8e5a8-8899-4fa5-a8e1-c7971384ff30">e is <span style="color: rgb(62,63,64);">automatically </span>computed</ac:inline-comment-marker> based on this formula from ISO/SAE 21434:2021,<span> </span><em>Annex H: Risk = 1 + Impact x Feasibility.</em></li><li> According to the computed risk value,<ac:inline-comment-marker ac:ref="f77ed7e0-6738-4276-95e2-b33854c5d6e2"> decide</ac:inline-comment-marker> the risk treatment for each threat scenario: Retain, Reduce, Share, or Avoid. Depending on the risk treatment decision, <ac:inline-comment-marker ac:ref="b18dd0f5-50da-48e5-a536-d3e96f0b1e8c">determine</ac:inline-comment-marker> cybersecurity claims or goals that will eventually be detailed in the cybersecurity requirements (functional, technical, hardware, or software type).</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="faa93582-b57b-4b49-bd25-28be3230adea"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">An Item is a part of the system architecture to be protected. An Item with a Functional Cybersecurity Concept (output of the study) is the system architecture with additional requirements and claims that <ac:inline-comment-marker ac:ref="eb7839d2-148c-42c6-9a64-784c8e8da763">ensures</ac:inline-comment-marker> a secure system.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170466459 space=CSRA2024xR1 version=1 -->
## PAGE 00017: Concepts

- page_id: `170466459`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466459/Concepts
- version_number: 1
- version_date: `2019-07-30T11:05:35.734+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Getting started
- labels: []

### NORMALIZED CONTENT

948517801

948517804

948517803

For better understanding further material, get acquainted with basic concepts of analyzing safety and reliability.

##### Risk concepts

| Concept | Description |
| --- | --- |
| Risk | Combination of the probability of occurrence of harm and the severity of that harm. |
| Hazard | A potential source of harm.A hazard is any source of potential damage, harm or adverse health effects on something or someone under certain conditions at work. |
| Hazardous situation | Circumstance in which people, property, or the environment are exposed to one or more hazard(s). |
| Harm | Physical injury or damage to the health of people, or damage to property or the environment. |
| Severity | Measure of the possible consequences of a hazard. |
| Probability | Quantitative evaluation of a event happening.There are two types of probabilities emphasized in ISO 14971:2012:P1 – probability of foreseeable sequence of events leading to hazardous situation.P2 – probability that harm will occur when exposed to hazard. |
| Detectability | Hazard detection index accounts for the likelihood of discovering and correcting a hazard or failure mode prior to harm occurrence. |
| Hazard Correctability | Factor rates the relative ease of mitigating a certain risk. It accounts for the associated feasibility and effort required in reducing a particular risk to the lowest practicable level. |
| Product Utility | Factor is meant to integrate clinical benefit into the risk score. |

##### FMEA concepts

| Concept | Description |
| --- | --- |
| Item | Enter the items, interfaces, or parts which have been identified through block diagrams, P-diagrams, schematics and other drawings, and other analysis conducted by the team. |
| Failure Mode | Potential failure mode is defined as the manner in which a component, subsystem, or system could potentially fail to meet or deliver the intended function described in the item column. |
| Effect of Failure | Effects of failure are defined as the effects of the failure mode on the function, as perceived by the customer(s). |
| Severity | Severity is the value associated with the most serious effect for a given failure mode. |
| Cause of Failure | Potential cause of failure is defined as an indication of how the design process could allow the failure to occur, described in terms of something that can be corrected or can be controlled. |
| Occurrence | Occurrence is the likelihood that a specific cause/mechanism will occur resulting in the failure mode within the design life. |
| Current Design Controls | Current Design Controls are those activities conducted as part of the design process that have been completed or committed to and that will assure the design adequacy for the design functional and reliability requirements under consideration. |
| Detectability | Detection is the rank associated with the best detection control listed in the Current Design Control Detection column. |
| Recommended Action | The intent of recommended actions is to improve the design. Identifying these actions should consider reducing rankings in the following order: severity, occurrence, and detection. |
| Responsibility Target Completion Date | The name of the individual and organization which is responsible for completing each recommended action including the target completion date. |
| Action taken | A brief description of the action taken and actual completion date. |
| Hazard Analysis Reference | Reference to Risk. |

##### ISO 26262 Functional Safety concepts

| Concept | Description |
| --- | --- |
| Malfunctioning Behavior | A Malfunctioning Behavior describes a failure or unintended behavior of an item with respect to its design intent. It is a subtype of a Failure Mode. |
| Operational Situation | An Operational Situation describes the operational scenario or driving scenario which is considered in a Hazardous Event, as part of the Hazard Analysis and Risk Assessment process. |
| ASIL | Automotive Safety Integrity Level is one of four levels to specify the necessary requirements for ISO-26262 and safety measures for avoiding unreasonable risks.There are four ASILs identified by ISO 26262 - A, B, C, and D. ASIL A represents the lowest degree, and ASIL D represents the highest degree of automotive hazard. |
| Exposure | Exposure is the likelihood of being in a particular operational situation.Exposure Classifications (E): E0 Incredibly unlikely E1 Very low probability (injury could happen only in rare operating conditions) E2 Low probability E3 Medium probability E4 High probability (injury could happen under most operating conditions) |
| Severity | "Estimate of the extent of harm." Severity Classifications (S): S0 No Injuries S1 Light to moderate injuries S2 Severe to life-threatening (survival probable) injuries S3 Life-threatening (survival uncertain) to fatal injuries |
| Controllability | "Ability to avoid a specified harm or damage through timely reactions of individuals involved in the scenario." Controllability Classifications (C): C0 Controllable in general C1 Simply controllable C2 Normally controllable (most drivers could act to prevent injury) C3 Difficult to control or uncontrollable |
| Safety Goal | It represents a top-level safety requirement, defined as a result of the Hazard Analysis and Risk Assessment process.A safety goal is a top-level safety requirement that is assigned to a system, with the purpose of reducing the risk of one or more hazardous events to a tolerable level. |
| Functional Safety Requirement | A functional safety requirement specifies an implementation independent safety behavior, or an implementation independent safety measure, required for achievement of a safety goal from which it is derived. |
| Technical Safety Requirement | A technical safety requirement specifies the implementation of the functional safety requirement(s) from which it is derived. Technical safety requirements express the behaviors and details necessary to realize the safety aspects of the item at the system level. Additional details that do not act at the system level can be specified in the hardware safety requirements or software safety requirements. |
| Software Safety Requirement | A software safety requirement provides implementation details for software. They can express behaviors or specific software mechanisms which realize the technical safety requirements from which they are derived |
| Hardware Safety Requirement | A hardware safety requirement specifies hardware behaviors or hardware specific details necessary for implementing the safety concept. Hardware safety requirements are implementation specific and assigned to components or subcomponents. |
| ASIL Decompose relationship | An ASIL decompose relation is used to connect two safety requirements for the purposes of performing ASIL decomposition. The target requirement (supplier) should be of a higher abstraction than the source (client). ASIL decompose relations shall be applied in pairs (e.g. a requirement cannot be the supplier of a single ASIL decompose relation). |
| Independece Requirement relationship | A relationship between requirement elements indicating that the child requirement specifies an independence criteria that needs to be satisfied in order for an ASIL decomposition to be valid. The decomposition between the parent requirement and 2 other children requirements. |
| Safe State | A state of function realized by one or more architectural components. May be composed of serval subfunctions or called by other functions. Associated with safety specific behaviors, typically (but not necessarily) triggered by a failure mode. |
| Operating Mode | A state of function realized by one or more architectural components. May be composed of serval subfunctions or called by other functions. Associated with specific behaviors. |
| Recovery Requirement | A RecoveryRequirement relationship is a dependency between a safe state and requirement where the requirement indicates the criteria to recover from the safe state to another operational mode. |
| User Info Requirement | "A UserInfoRequirement relationship is a dependency which links a State to a requirement. The arrow direction points from a state (client) to a FSR or TSR (supplier). Linked requirements specify information that must be presented to vehicle occupants when the vehicle enters a safe state." |
| FTTIfault tolerant time interval | time-span in which a fault or faults can be present in a system before a hazardous event occurs. |
| System Level Effect | System- or vehicle-level effect which is or could result in harm. |
| Vehicle Level Effect | System- or vehicle-level effect which is or could result in harm. |
| Traffic And People | It is used to describe the presence and behavior of any motorists or non-motorists considered in a hazardous event. |
| Vehicle Usage | It is used to describe the usage of a vehicle during a hazardous event. |
| Road Condition | It is used to describe the conditions or state of the surface a vehicle is driving on (Low-traction, Grade(Slope), etc.) during a hazardous event. |
| Location | It is used to describe the physical location (high speed road, intersection, parking lot, etc.) of a vehicle during a hazardous event. |
| Environmental Condition | It and is used to describe the environmental conditions at the time of vehicle operation in a hazardous event. |
| Hazardous Event | Combination of hazard and operational situation to identify automotive safety integrity level.A hazardous event is a relevant combination of a vehicle-level hazard and an operational situation of the vehicle with potential to lead to an accident if not controlled by timely driver action. |
| Hazard | Potential source of harm. |
| Accident Scenario | A combination of operational situation and malfunctioning behavior |
| More | This kind of malfunctioning behavior represents a failure resulting from providing more output/behavior than required. |
| Less | This kind of malfunctioning behavior represents a failure resulting from providing less output/behavior than required. |
| No | This kind of malfunctioning behavior represents a failure resulting from the behavior not being performed when required. |
| Intermittent | This kind of malfunctioning behavior represents a failure from the behavior being performed intermittently. |
| Unintended | This kind of malfunctioning behavior represents a failure resulting from the behavior being provided when not required. |
| Early | This kind of malfunctioning behavior represents a failure resulting from the behavior being performed earlier than required. |
| Late | This kind of malfunctioning behavior represents a failure resulting from the behavior being performed later than required. |
| Inverted | This kind of malfunctioning behavior represents a failure resulting from the behavior providing an inverted output. |

948517799

**Related pages**

- [CONFLUENCE_PAGE title='Getting started' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Process description' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Project templates' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="2e6de61e-1633-4820-aee3-625724333e94"><ac:parameter ac:name="id">948517801</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0c39acdc-459e-485d-aac9-00f321fa2c5b"><ac:parameter ac:name="id">948517804</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="10e582a6-ea5f-4c1b-b527-205535ca1487"><ac:parameter ac:name="id">948517803</ac:parameter><ac:rich-text-body><p>For better understanding further material, get acquainted with basic concepts of analyzing safety and reliability.</p><h3>Risk concepts</h3><table class="wrapped relative-table" style="width: 74.8217%;"><colgroup><col style="width: 19.7359%;" /><col style="width: 80.2641%;" /></colgroup><tbody><tr><th><p><strong>Concept</strong></p></th><th>Description</th></tr><tr><td><p><strong>Risk</strong></p></td><td>Combination of the probability of occurrence of harm and the severity of that harm.</td></tr><tr><td><p><strong>Hazard</strong></p></td><td><p>A potential source of harm.</p>A hazard is any source of potential damage, harm or adverse health effects on something or someone under certain conditions at work.</td></tr><tr><td><p><strong>Hazardous situation</strong></p></td><td><p>Circumstance in which people, property, or the environment are exposed to one or more hazard(s).</p></td></tr><tr><td><p><strong>Harm</strong></p></td><td>Physical injury or damage to the health of people, or damage to property or the environment.</td></tr><tr><td><p><strong>Severity</strong></p></td><td>Measure of the possible consequences of a hazard.</td></tr><tr><td><p><strong>Probability</strong></p></td><td><p>Quantitative evaluation of a event happening.</p><p>There are two types of probabilities emphasized in ISO 14971:2012:</p><ul><li>P1 – probability of foreseeable sequence of events leading to hazardous situation.</li><li>P2 – probability that harm will occur when exposed to hazard.</li></ul></td></tr><tr><td colspan="1"><p class="MsoNormal"><strong>Detectability</strong></p></td><td colspan="1"><p>Hazard detection index accounts for the likelihood of discovering and correcting a hazard or failure mode prior to harm occurrence.</p></td></tr><tr><td colspan="1"><p><strong>Hazard Correctability </strong></p></td><td colspan="1"><p>Factor rates the relative ease of mitigating a certain risk. It accounts for the associated feasibility and effort required in reducing a particular risk to the lowest practicable level.</p></td></tr><tr><td colspan="1"><p><strong>Product Utility </strong></p></td><td colspan="1"><p>Factor is meant to integrate clinical benefit into the risk score.</p></td></tr></tbody></table><p><br /></p><h3>FMEA concepts</h3><table class="wrapped"><colgroup><col /><col /></colgroup><tbody><tr><th><span style="color: rgb(0,0,0);">Concept</span></th><th><span style="color: rgb(0,0,0);">Description</span></th></tr><tr><td><p><strong>Item</strong></p></td><td>Enter the items, interfaces, or parts which have been identified through block diagrams, P-diagrams, schematics and other drawings, and other analysis conducted by the team.</td></tr><tr><td><p><strong>Failure Mode</strong></p></td><td>Potential failure mode is defined as the manner in which a component, subsystem, or system could potentially fail to meet or deliver the intended function described in the item column.</td></tr><tr><td><p><strong>Effect of Failure</strong></p></td><td>Effects of failure are defined as the effects of the failure mode on the function, as perceived by the customer(s).</td></tr><tr><td><p><strong>Severity</strong></p></td><td>Severity is the value associated with the most serious effect for a given failure mode.</td></tr><tr><td><p><strong>Cause of Failure</strong></p></td><td>Potential cause of failure is defined as an indication of how the design process could allow the failure to occur, described in terms of something that can be corrected or can be controlled.</td></tr><tr><td colspan="1"><p><strong>Occurrence</strong></p></td><td colspan="1">Occurrence is the likelihood that a specific cause/mechanism will occur resulting in the failure mode within the design life.</td></tr><tr><td colspan="1"><p><strong>Current Design Controls</strong></p></td><td colspan="1">Current Design Controls are those activities conducted as part of the design process that have been completed or committed to and that will assure the design adequacy for the design functional and reliability requirements under consideration.</td></tr><tr><td colspan="1"><p><strong>Detectability</strong></p></td><td colspan="1">Detection is the rank associated with the best detection control listed in the Current Design Control Detection column.</td></tr><tr><td colspan="1"><p><strong>Recommended Action</strong></p></td><td colspan="1">The intent of recommended actions is to improve the design. Identifying these actions should consider reducing rankings in the following order: severity, occurrence, and detection.</td></tr><tr><td colspan="1"><p><strong>Responsibility Target Completion Date</strong></p></td><td colspan="1">The name of the individual and organization which is responsible for completing each recommended action including the target completion date. </td></tr><tr><td colspan="1"><p><strong>Action taken</strong></p></td><td colspan="1">A brief description of the action taken and actual completion date.</td></tr><tr><td colspan="1"><p><strong>Hazard Analysis Reference</strong></p></td><td colspan="1">Reference to Risk.</td></tr></tbody></table><h3 class="auto-cursor-target"><br />ISO 26262 Functional Safety concepts</h3><table class="relative-table wrapped" style="margin-left: 2.0px;width: 99.8903%;"><colgroup><col style="width: 14.2857%;" /><col style="width: 85.7143%;" /></colgroup><tbody><tr><th style="text-align: left;">Concept</th><th style="text-align: left;">Description</th></tr><tr><td><strong>Malfunctioning Behavior</strong></td><td>A Malfunctioning Behavior describes a failure or unintended behavior of an item with respect to its design intent. It is a subtype of a Failure Mode.</td></tr><tr><td><strong>Operational Situation</strong></td><td>An Operational Situation describes the operational scenario or driving scenario which is considered in a Hazardous Event, as part of the Hazard Analysis and Risk Assessment process.</td></tr><tr><td><strong>ASIL</strong></td><td>Automotive Safety Integrity Level is one of four levels to specify the necessary requirements for ISO-26262 and safety measures for avoiding unreasonable risks.<br />There are four ASILs identified by ISO 26262 - A, B, C, and D. ASIL A represents the lowest degree, and ASIL D represents the highest degree of automotive hazard.</td></tr><tr><td><strong>Exposure</strong></td><td>Exposure is the likelihood of being in a particular operational situation.<br /><ins>Exposure Classifications (E):</ins> <br /><strong>E0</strong> Incredibly unlikely <br /><strong>E1</strong> Very low probability (injury could happen only in rare operating conditions) <br /><strong>E2</strong> Low probability <br /><strong>E3</strong> Medium probability <br /><strong>E4</strong> High probability (injury could happen under most operating conditions)</td></tr><tr><td><strong>Severity</strong></td><td>&quot;Estimate of the extent of harm.&quot;<br /> <br /><ins>Severity Classifications (S):</ins> <br /><strong>S0</strong> No Injuries <br /><strong>S1</strong> Light to moderate injuries <br /><strong>S2</strong> Severe to life-threatening (survival probable) injuries <br /><strong>S3</strong> Life-threatening (survival uncertain) to fatal injuries</td></tr><tr><td><strong>Controllability</strong></td><td>&quot;Ability to avoid a specified harm or damage through timely reactions of individuals involved in the scenario.&quot;<br /> <br /><ins>Controllability Classifications (C):</ins> <br /><strong>C0</strong> Controllable in general <br /><strong>C1</strong> Simply controllable <br /><strong>C2</strong> Normally controllable (most drivers could act to prevent injury) <br /><strong>C3</strong> Difficult to control or uncontrollable</td></tr><tr><td><strong>Safety Goal</strong></td><td>It represents a top-level safety requirement, defined as a result of the Hazard Analysis and Risk Assessment process.<br />A <em>safety goal</em> is a top-level safety requirement that is assigned to a system, with the purpose of reducing the risk of one or more <em>hazardous events</em> to a tolerable level.</td></tr><tr><td><strong>Functional Safety Requirement</strong></td><td>A functional safety requirement specifies an implementation independent safety behavior, or an implementation independent safety measure, required for achievement of a safety goal from which it is derived.</td></tr><tr><td><strong>Technical Safety Requirement</strong></td><td>A technical safety requirement specifies the implementation of the functional safety requirement(s) from which it is derived. Technical safety requirements express the behaviors and details necessary to realize the safety aspects of the item at the system level. Additional details that do not act at the system level can be specified in the hardware safety requirements or software safety requirements.</td></tr><tr><td><strong>Software Safety Requirement</strong></td><td>A software safety requirement provides implementation details for software. They can express behaviors or specific software mechanisms which realize the technical safety requirements from which they are derived</td></tr><tr><td><strong>Hardware Safety Requirement</strong></td><td>A hardware safety requirement specifies hardware behaviors or hardware specific details necessary for implementing the safety concept. Hardware safety requirements are implementation specific and assigned to components or subcomponents.</td></tr><tr><td><strong>ASIL Decompose relationship</strong></td><td>An ASIL decompose relation is used to connect two safety requirements for the purposes of performing ASIL decomposition. The target requirement (supplier) should be of a higher abstraction than the source (client). ASIL decompose relations shall be applied in pairs (e.g. a requirement cannot be the supplier of a single ASIL decompose relation).</td></tr><tr><td><strong>Independece Requirement relationship</strong></td><td>A relationship between requirement elements indicating that the child requirement specifies an independence criteria that needs to be satisfied in order for an ASIL decomposition to be valid. The decomposition between the parent requirement and 2 other children requirements.</td></tr><tr><td><strong>Safe State</strong></td><td>A state of function realized by one or more architectural components. May be composed of serval subfunctions or called by other functions. Associated with safety specific behaviors, typically (but not necessarily) triggered by a failure mode.</td></tr><tr><td><strong>Operating Mode</strong></td><td>A state of function realized by one or more architectural components. May be composed of serval subfunctions or called by other functions. Associated with specific behaviors.</td></tr><tr><td><strong>Recovery Requirement</strong></td><td>A RecoveryRequirement relationship is a dependency between a safe state and requirement where the requirement indicates the criteria to recover from the safe state to another operational mode.</td></tr><tr><td><strong>User Info Requirement</strong></td><td>&quot;A UserInfoRequirement relationship is a dependency which links a State to a requirement. The arrow direction points from a state (client) to a FSR or TSR (supplier). Linked requirements specify information that must be presented to vehicle occupants when the vehicle enters a safe state.<br />&quot;</td></tr><tr><td><strong>FTTI</strong><br /><strong>fault tolerant time interval</strong></td><td> time-span in which a fault or faults can be present in a system before a hazardous event occurs.</td></tr><tr><td><strong>System Level Effect</strong></td><td>System- or vehicle-level effect which is or could result in harm.</td></tr><tr><td><strong>Vehicle Level Effect</strong></td><td>System- or vehicle-level effect which is or could result in harm.</td></tr><tr><td><strong>Traffic And People</strong></td><td>It is used to describe the presence and behavior of any motorists or non-motorists considered in a hazardous event.</td></tr><tr><td><strong>Vehicle Usage</strong></td><td>It is used to describe the usage of a vehicle during a hazardous event.</td></tr><tr><td><strong>Road Condition</strong></td><td>It is used to describe the conditions or state of the surface a vehicle is driving on (Low-traction, Grade(Slope), etc.) during a hazardous event.</td></tr><tr><td><strong>Location</strong></td><td>It is used to describe the physical location (high speed road, intersection, parking lot, etc.) of a vehicle during a hazardous event.</td></tr><tr><td><strong>Environmental Condition</strong></td><td>It and is used to describe the environmental conditions at the time of vehicle operation in a hazardous event.</td></tr><tr><td><strong>Hazardous Event</strong></td><td>Combination of hazard and operational situation to identify automotive safety integrity level.<br />A <em>hazardous event</em> is a relevant combination of a vehicle-level <em>hazard</em> and an operational situation of the vehicle with potential to lead to an accident if not controlled by timely driver action.</td></tr><tr><td><strong>Hazard</strong></td><td> Potential source of harm.</td></tr><tr><td><strong>Accident Scenario</strong></td><td>A combination of operational situation and malfunctioning behavior</td></tr><tr><td><strong>More</strong></td><td>This kind of malfunctioning behavior represents a failure resulting from providing more output/behavior than required.</td></tr><tr><td><strong>Less</strong></td><td>This kind of malfunctioning behavior represents a failure resulting from providing less output/behavior than required.</td></tr><tr><td><strong>No</strong></td><td>This kind of malfunctioning behavior represents a failure resulting from the behavior not being performed when required.</td></tr><tr><td><strong>Intermittent</strong></td><td>This kind of malfunctioning behavior represents a failure from the behavior being performed intermittently.</td></tr><tr><td><strong>Unintended</strong></td><td>This kind of malfunctioning behavior represents a failure resulting from the behavior being provided when not required.</td></tr><tr><td><strong>Early</strong></td><td>This kind of malfunctioning behavior represents a failure resulting from the behavior being performed earlier than required.</td></tr><tr><td><strong>Late</strong></td><td>This kind of malfunctioning behavior represents a failure resulting from the behavior being performed later than required.</td></tr><tr><td><strong>Inverted</strong></td><td>This kind of malfunctioning behavior represents a failure resulting from the behavior providing an inverted output.</td></tr></tbody></table></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="41bc0ad7-2aeb-44d5-a731-97a9dfb15e6c"><ac:parameter ac:name="id">948517799</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Getting started" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Process description" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Project templates" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466627 space=CSRA2024xR1 version=1 -->
## PAGE 00018: Customizations

- page_id: `170466627`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466627/Customizations
- version_number: 1
- version_date: `2024-01-31T07:30:05.323+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety
- labels: []

### NORMALIZED CONTENT

You can extend the ISO 26262 library by adding new types of elements to default tables or creating new properties for ISO 26262 elements. To learn more about different customization options, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can extend the ISO 26262 library by adding new types of elements to default tables or creating new properties for ISO 26262 elements. To learn more about different customization options, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="d7aa1aeb-73b8-4f21-8c53-af9f40623b66" /></p>
````

<!--NOMAGIC_PAGE id=170466497 space=CSRA2024xR1 version=2 -->
## PAGE 00019: Customizing Safety Analysis and FMEA configurations

- page_id: `170466497`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466497/Customizing+Safety+Analysis+and+FMEA+configurations
- version_number: 2
- version_date: `2024-05-08T14:01:16.118+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Note

950070133

#### CONTENT-COLUMN: Note

950070136

#### CONTENT-BLOCK: Note

950070135

In your safety and reliability analysis model, you can define the values and expressions for all calculable properties, such as **Correctablity**, **Probability**, **Severity**, **Risk Score** and other. To do this, use the Safety Analysis Configuration and FMEA Configuration elements.

Every model has predefined Safety Analysis and FMEA Configuration elements coming with the FMEA Profile and Medical Risk Profile. However, you can create one more custom Safety Analysis Configuration element and one more custom FMEA Configuration element. If you decide to define custom Configuration elements, you can modify all the values and expressions used for analysis and calculation(in this case, Configuration elements coming with predefined profiles are not used).

configure

To create custom Configuration element

1. Create your safety and reliability analysis model or open an existing one.
2. In the [CONFLUENCE_PAGE title='Model Browser' space='MD2024xR1'] , do one of the following:
  - right-click on the package wherein you want to save a configuration and select the Create Element command.
  - select a package wherein you want to save a configuration and press Ctrl+Shift+E.
3. In the open **Create Element**dialog, select the **Safety Analysis Configuration** or **FMEA Configuration** element. The selected element is created in your model. TipStart typing "conf" to filter Risk Analysis and FMEA related elements.[IMAGE alt='' src='']
4. Type the element name.
5. Open the element [CONFLUENCE_PAGE title='Specification window' space='MD2024xR1'] and specify the values of desired properties.
6. Close the window when you are done.

To create safety analysis calculation expressions

1. [CONFLUENCE_PAGE title='Customizing Safety Analysis and FMEA configurations' space='CSRA2024xR1'] the Safety Analysis or FMEA Configuration element and open its Specification window.
2. Under the Safety Analysis Calculations Group , select the value box of the expression you want to edit.
3. Click the Edit button. [ATTACHMENT filename='safety_analysis_expression_editing.png']
4. In the open****dialog, select an operation and [CONFLUENCE_PAGE title='Getting started with specifying criteria' space='MD2024xR1'] by modifying a predefined expression. NoteBy default, custom Configuration elements already have predefined expressions. So if a certain predefined expression meets your needs, you don't need to modify it.
5. When you are done, click OK and close the Specification window.

950070132

**Related pages**

- [CONFLUENCE_PAGE title='Getting started' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Reliability analysis using FMEA' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Safety analysis' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Additional features' space='CSRA2024xR1']Additional features
- [CONFLUENCE_PAGE title='Getting started with specifying criteria' space='MD2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8b94d295-6bf4-455c-8100-3d70f28adbb8"><ac:parameter ac:name="id">950070133</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d288735a-19e1-4e47-82d1-55e2c0c42cf5"><ac:parameter ac:name="id">950070136</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d594518d-0557-4597-adb6-50561097e7c2"><ac:parameter ac:name="id">950070135</ac:parameter><ac:rich-text-body><p><ac:inline-comment-marker ac:ref="331298a8-e5d7-4170-91e6-f7513ad58b58">In your safety</ac:inline-comment-marker> and reliability analysis model, you can define the values and expressions for all calculable properties, such as <strong>Correctablity</strong>, <strong>Probability</strong>, <strong>Severity</strong>, <strong>Risk Score</strong> and <ac:inline-comment-marker ac:ref="0866c20f-b10d-47b5-bdc9-840250cdc91a">other</ac:inline-comment-marker>. To do this, use the Safety Analysis Configuration and FMEA Configuration elements.</p><p>Every model has predefined Safety Analysis and FMEA Configuration elements <ac:inline-comment-marker ac:ref="a5448a40-d80c-46e6-adcb-d2735b96b9e3">coming with</ac:inline-comment-marker> the FMEA Profile and Medical Risk Profile. <ac:inline-comment-marker ac:ref="e87a365c-ba73-4688-bc1b-8a22fbcf35e1">However, you can create one more custom Safety Analysis Configuration element and one more custom FMEA Configuration element.</ac:inline-comment-marker> If you decide to <ac:inline-comment-marker ac:ref="2503ca32-5e15-4c94-88fe-6652cad7bc35">define custom</ac:inline-comment-marker> Configuration elements, you can modify all the values and expressions used for analysis and calculation<ac:inline-comment-marker ac:ref="ee76a245-c8c9-4881-b155-41f97d5be4ba"> (in this case, Configuration elements <ac:inline-comment-marker ac:ref="1d71389b-8549-4e6d-82d2-f985f0a0bccd">coming</ac:inline-comment-marker> with predefined profiles are not used)</ac:inline-comment-marker>.</p><p> </p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="10a91455-ae22-420d-ab07-2a7df4a37988"><ac:parameter ac:name="">configure</ac:parameter></ac:structured-macro></p><p>To create custom Configuration element</p><hr /><ol><li><ac:inline-comment-marker ac:ref="5d51deb5-ec51-4322-b981-856275035cd7">Create your safety and reliability analysis model or open an existing one.</ac:inline-comment-marker></li><li>In the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Model Browser" /></ac:link>, do one of the following:<br /><ul><li>right-click on the package wherein you want to save a configuration and select the <strong>Create Element</strong> command.</li><li>select a package wherein you want to save a configuration and press Ctrl+Shift+E.</li></ul></li><li><p>In the open <strong>Create Element </strong>dialog, select the <strong>Safety Analysis Configuration</strong> or <strong>FMEA Configuration</strong> element. The selected element is created in your model.<br /> </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c6c5bc09-ac37-4dde-8327-d54e56cec8bb"><ac:parameter ac:name="title">Tip</ac:parameter><ac:rich-text-body><p>Start typing &quot;conf&quot; to filter Risk Analysis and FMEA related elements. </p><p><ac:image><ri:attachment ri:filename="risk_FMEA_configuration_element.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Customizing Safety Analysis and FMEA configurations" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Type the element name.</li><li>Open the element <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> and specify the values of desired properties.</li><li><ac:inline-comment-marker ac:ref="3c1d8800-c7bd-4c10-8e82-d4bc507f6e0c">Close the window when you are done.</ac:inline-comment-marker></li></ol><p> </p><p>To create <ac:inline-comment-marker ac:ref="64bf8791-1396-46bf-87fb-d3517e9bf026">safety analysis</ac:inline-comment-marker> calculation expressions</p><hr /><ol><li><ac:link ac:anchor="configure"><ac:plain-text-link-body><![CDATA[Create]]></ac:plain-text-link-body><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Customizing Safety Analysis and FMEA configurations" /></ac:link> the Safety Analysis or FMEA Configuration element and open its Specification window.</li><li>Under the <strong>Safety Analysis Calculations Group</strong>, select the value box of the expression you want to edit.</li><li>Click the <strong>Edit</strong> button.<br /><br /><ac:image><ri:attachment ri:filename="safety_analysis_expression_editing.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Customizing Safety Analysis and FMEA configurations" /></ri:attachment></ac:image><br /><br /></li><li><p>In the open<strong> </strong>dialog, select an operation and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Getting started with specifying criteria" /><ac:plain-text-link-body><![CDATA[specify criteria]]></ac:plain-text-link-body></ac:link> by modifying a predefined expression.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ed30333f-a348-4c67-8da4-4a352ed5b251"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>By default, <ac:inline-comment-marker ac:ref="e36ffef1-f405-4964-a875-d881ee3ca51f">custom Configuration</ac:inline-comment-marker> elements already have predefined expressions. So if a certain predefined expression meets your needs, you don't need to modify it.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>When you are done, click <strong>OK</strong> and close the Specification window.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5ecbcb7f-6eee-4c9c-92d2-b31ee581817b"><ac:parameter ac:name="id">950070132</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Getting started" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Reliability analysis using FMEA" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety analysis" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Additional features" /><ac:link-body>Additional features<br /></ac:link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Getting started with specifying criteria" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170467038 space=CSRA2024xR1 version=2 -->
## PAGE 00020: Cyber Security Attack Graph

- page_id: `170467038`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170467038/Cyber+Security+Attack+Graph
- version_number: 2
- version_date: `2024-05-08T14:01:17.344+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
- labels: []

### NORMALIZED CONTENT

##### Creating a Cyber Security Attack Graph Diagram

To create aCyber Security Attack Graph Diagram

1. In the Containment tree, right-click any required package and select Create Diagram. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand**ISO 21434**and select **Cyber****Security Attack Graph Diagram**. [IMAGE alt='' src='']
  - In the search tab, type the keyword graph and then select **Cyber Security Attack Graph Diagram** . 
 
[IMAGE alt='' src=''] The Cyber Security Attack Graph Diagram**** is displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='Cyber Security Attack Graph Diagram.png']

##### Adding an Attack Path Step in the Attack Graph

To add a new Attack Path Step in the Attack Graph

- From the diagram palette, select Attack Path Step and c lick on the diagram pane. Name the created Attack Path Step. 
 
[IMAGE alt='' src='']

To add an existing Attack Path Step, CWE Element, or any Situation in the Attack Graph

- Drag the required Attack Path Step, CWE Element, or any Situation from the Containment tree and drop it in the diagram pane. [ATTACHMENT filename='Attack Steps_Drag and Drop.png']

##### Creating a Causality Relation between Attack Path Steps

To create a Causality Relation between Attack Path Steps

- Do one of the following:
  - Click the attack path step to open the [CONFLUENCE_PAGE title='Smart manipulator toolbar' space='MD2024xR1'] , select the Causality relationship, and create a relationship. To learn more about creating relationships, refer to [CONFLUENCE_PAGE title='Creating a relationship' space='MD2024xR1'] [ATTACHMENT filename='Causality Relation_Smart Manipulator.png']
  - From the diagram palette, select the Causality command and then select the required attack path steps . [ATTACHMENT filename='Causality_Diagram Palette.png']

An arrow icon is displayed in the graph which denotes that causality relation is created.[IMAGE alt='' src='']

##### Generating an Attack Path from the Attack Graph

To generate an Attack Path from the Attack Graph

1. In the attack graph, select the two required attack steps by holding down the Shift key. The selected attack paths are considered as two ends of an attack path.
2. Right-click and select the Generate Attack Paths command. [ATTACHMENT filename='Generate Attack Paths.png']
3. In the Select Attack Paths dialog, select the required attack path from the list of available attack paths and click OK. Loops present in the attack graph are eliminated while calculating the attack path(s). [IMAGE alt='' src='']
4. In the Select Destination Package dialog, select the package to save the generated attack path(s). 
 
[IMAGE alt='' src=''] After generation of an Attack Path, if Attack Graph changes in such a way that the path is not valid anymore, a validation rule is triggered and an error occurs. You can fix the error from the Attack Path, but in such case, the path will not be linked to the graph anymore. Also, no further errors will be reported on that Attack Path if the graph is further modified.The generated attack path(s) are manual attack paths.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="a1514b4b-ace4-45ca-b6c7-ed1e918be3cb" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="da1d3de1-7fe0-4f45-b5ba-f59f1e700918">Creating a Cyber Security Attack Graph</ac:inline-comment-marker> Diagram</h3><p>To create a<span> Cyber Security Attack Graph Diagram</span></p><hr /><ol><li>In the Containment tree, right-click<span> </span>any required package<span style="color: rgb(62,63,64);"> </span>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand<span> </span><strong>ISO 21434<span> </span></strong>and select <strong>Cyber</strong><span><strong> Security Attack Graph Diagram</strong></span>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Cyber Security Attack Graph Diagram_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword graph and then select<span> <strong>Cyber Security Attack Graph Diagram</strong></span><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Cyber Security Attack Graph Diagram_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /><br /></strong>The <span>Cyber Security Attack Graph Diagram<strong> </strong></span>is displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Cyber Security Attack Graph Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image></li></ul></li></ol><h3>Adding an Attack Path Step in the Attack Graph</h3><p>To add a new Attack Path Step in the Attack Graph</p><hr /><ul><li>From the diagram palette, select <strong>Attack Path Step</strong> and c<span style="color: rgb(23,43,77);">lick on the diagram pane. Name the created Attack Path Step.<br /><br /><ac:image><ri:attachment ri:filename="Attack Path step_Diagram Pallete.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /></span></li></ul><p><br /></p><p><span style="color: rgb(23,43,77);">To add an existing Attack Path Step, CWE Element, or any Situation in the Attack Graph</span></p><hr /><ul><li><ac:inline-comment-marker ac:ref="975d17d3-ec2c-4d2d-8111-7bee0c82aa15">Drag the required <span style="color: rgb(23,43,77);">Attack Path Step, CWE Element, or any Situation</span></ac:inline-comment-marker> from the Containment tree and drop it in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Attack Steps_Drag and Drop.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image></li></ul><h3>Creating a Causality Relation between Attack Path Steps</h3><p>To create a Causality Relation between Attack Path Steps</p><hr /><ul><li>Do one of the following:<br /><br /><ul><li>Click the attack path step to open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Smart manipulator toolbar" /><ac:plain-text-link-body><![CDATA[Smart Manipulator toolbar]]></ac:plain-text-link-body></ac:link>, select the Causality relationship, and create a relationship. To learn more about creating relationships, refer to <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Creating a relationship" /></ac:link><br /><br /><ac:image><ri:attachment ri:filename="Causality Relation_Smart Manipulator.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /><br /></li><li>From the diagram palette, select the Causality command and then select the <ac:inline-comment-marker ac:ref="10887742-853d-4e1c-96f3-3f31fdf9f597">required attack path steps</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Diagram Palette.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image></li></ul></li></ul><p>An arrow icon is displayed in the graph which denotes that causality relation is created.<span style="color: rgb(23,43,77);"><br /><br /><ac:image><ri:attachment ri:filename="Causality Relation created.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /></span></p><h3>Generating an Attack Path from the Attack Graph</h3><p>To generate an Attack Path from the Attack Graph</p><hr /><ol><li><p class="auto-cursor-target">In the attack graph, select the two required attack steps by holding down the Shift key. The selected attack paths are considered as two ends of an attack path.</p></li><li>Right-click and select the Generate Attack Paths command.<br /><br /><ac:image><ri:attachment ri:filename="Generate Attack Paths.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /><br /></li><li><p class="auto-cursor-target">In the Select Attack Paths dialog, select the required attack path from the list of available attack paths and click OK.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d0907153-873c-43f4-9f47-b725a1f54485"><ac:rich-text-body><p>Loops present in the attack graph are eliminated while calculating the attack path(s).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Select Attack Path_Dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /><br /></p></li><li><p class="auto-cursor-target">In the Select Destination Package dialog, select the package to save the generated attack path(s).<br /><br /><ac:image><ri:attachment ri:filename="Select Destination Package_Dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cyber Security Attack Graph" /></ri:attachment></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4f1e46a7-c6bb-4d05-a42d-1b4a4967644a"><ac:rich-text-body><ul><li>After generation of an Attack Path, if Attack Graph changes in such a way that the path is not valid anymore, a validation rule is triggered and an error occurs. You can fix the error from the Attack Path, but in such case, the path will not be linked to the graph anymore. Also, no further errors will be reported on that Attack Path if the graph is further modified.</li><li>The generated attack path(s) are manual attack paths.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466752 space=CSRA2024xR1 version=2 -->
## PAGE 00021: Damage scenario

- page_id: `170466752`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466752/Damage+scenario
- version_number: 2
- version_date: `2024-05-08T14:01:16.894+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

3

**Damage Scenario**

Adverse consequence involving a vehicle or vehicle function and affecting a road user.

**Effect**

Allows you to define and manage system and vehicle level effects that can result in harm.

**Failure**

Termination of an intended behavior of an element or an item due to a fault manifestation.

**Operational Situation**

A scenario that can occur during a vehicle's life.

**Impact category**

Impact rating is done for four categories: Safety, Financial, Operational, and Privacy. The assessment should be done according to the definition given in ISO/SAE 21434:2021(annex F).

**Impact scale**

By default, the plugin adopts the scale provided in the ISO/SAE 21434:2021 standard: Negligible / Moderate / Major or Severe.

##### Creating a Damage Scenario

To create a Damage Scenario

1. In the Containment tree, right-click **Damage Scenario and Impact Ratings** and select Create Element. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Damage** **Scenario**. [IMAGE alt='' src='']
  - In the search tab, type the keyword damage and then select Damage Scenario. 
 
[IMAGE alt='' src='']
3. Name the created Damage Scenario in the Containment tree and press Enter. The Damage Scenario has the prefix **D****S** which denotes the created element is a Damage Scenario; the number **1** indicates that it is the first Damage Scenario created. 
 
[IMAGE alt='' src='']

##### Creating a Damage Scenarios Table

If you create a new project using the**ISO 21434 Project**template, then an**Damage Scenarios Table**already exists in the**1.1 Damage Scenarios and Impact Ratings**package.

To create a Damage ScenarioTable

1. In the Containment tree, right-click Damage Scenario and Impact Ratings and select Create Diagram. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Damage Scenario Table**. [IMAGE alt='' src='']
  - In the search tab, type the keyword damage and then select Damage Scenarios Table. 
 
[IMAGE alt='' src=''] The Damage Scenarios Table is displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='1 ContainmentTreeDamageScenariosTable.png']

##### Adding a Damage Scenario to the Damage Scenarios Table

To add a new Damage Scenario to the Damage Scenarios Table

1. In the Damage Scenario Table, click Add New. A row is added in the Damage Scenarios Table, which shows the new Damage Scenario. [IMAGE alt='' src='']
2. In the newly created Damage Scenario's row and the **Name**column, double-click the designated cell to name the Damage Scenario. 
 
[IMAGE alt='' src='']

To add an existing Damage Scenario to the Damage Scenarios Table

1. In the Damage Scenarios Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the **Select Damage Scenario**dialog, select the required Damage Scenario. A row is added to the Damage Scenarios Table, which shows the existing Damage Scenario. 
 
[IMAGE alt='' src='']
3. In the existing Damage Scenario's row and the **Name**column, double-click the designated cell to rename the Damage Scenario. 
 
[IMAGE alt='' src='']

##### Adding a Failure

To add a Failure to the Damage Scenarios Table

1. Double-click the designated cell in the Failure column and the required Damage Scenario's row and click [ATTACHMENT filename='Three Dot _Icon.png'] . [ATTACHMENT filename='1 ClickThreeDots_Failure.png']
2. From the Select Class dialog, select Failure. [ATTACHMENT filename='2 SelectFailureWindow_v2.png'] The Failure is shown in the Damage Scenarios Table. [ATTACHMENT filename='3 AfterAddingFailure.png']

You can also drag and drop the Failure modes from the Containment tree to the Damage Scenarios Table.

##### Adding an Effect

To add an Effect in the Damage Scenarios Table

1. Double-click the designated cell in the Effect column and the required Damage Scenario's row and click [ATTACHMENT filename='Three Dot _Icon.png'] . [ATTACHMENT filename='1 ClickThreeDots_Effect.png']
2. From the Select Class dialog, select Effect. [ATTACHMENT filename='2 SelectEffectWindow_v2.png'] The Effect is shown in the Damage Scenarios Table. [ATTACHMENT filename='3 AfterAddingEffect.png']

You can also drag and drop the Effects such as Vehicle Level Effects and System Level Effects from the Containment tree to the Damage Scenarios Table.

##### Adding an Operational Situation

To add an Operational Situation in the Damage Scenarios Table

1. Double-click the designated cell in the Operational Situation column and the required Damage Scenario's row and click [ATTACHMENT filename='Three Dot _Icon.png'] . [ATTACHMENT filename='1 ClickThreeDots_Operation Situation.png']
2. From the Select Class dialog, select Operational Situation. [ATTACHMENT filename='2 SelectOpSituation_v2.png'] The Operational Situation is added in the Damage Scenarios Table. [ATTACHMENT filename='3 AfterAddingOpSituation.png']

You can also drag and drop the Operation Situations from the Containment tree to the Damage Scenarios Table.

##### Rating SFOP Impact

- The Damage Scenario cannot be rated if there is no Effect associated to it.
- All the Damage Scenarios sharing the same Effect get the same impact ratings. In such case, if you update any impact rating(s) for one Damage Scenario, the impact rating(s) for other Damage Scenarios are updated.

To rate the SFOP Impact

- Double-click each cell, namely**Safety Impact**, **Financial Impact**, **Operational Impact**, and **Privacy Impact**in the Damage Scenario row. From the drop-down list, select the impact rating. 
 
[IMAGE alt='' src=''] 
The Impact rating is done in the Damage Scenarios Table. 
 
[IMAGE alt='' src='']

The plugin behavior when you use the Effect element from the used project in your local project:

- When you update the SFOP Impact ratings of the damage scenario, a cloned Effect element is created in your local project and is visible in the Containment tree. The following notification message is displayed with the cloned Effect element link at the bottom right corner of the modeling tool. [ATTACHMENT filename='Cloned_Notification.png']

The plugin behavior when you use the Effect element from the used project in the TWC server project:

- When you update the SFOP Impact ratings of the damage scenario, a cloned Effect element is created in your server project and is visible in the Containment tree. The following notification message is displayed with the cloned Effect element link at the bottom right corner of the modeling tool. [ATTACHMENT filename='Cloned_Notification.png']

The plugin behavior when you use the Effect element from your own TWC server project:

- When you update the SFOP ratings of the damage scenario and the Effect element is in a read-only state, the Effect element gets locked automatically by you.
- When you update the SFOP ratings of the damage scenario and the Effect element is locked by another user, the following notification is displayed with the locked Effect element link at the bottom right corner of the modeling tool. [ATTACHMENT filename='Locked_Notification.PNG']

##### Damage Scenarios Table Example 
 
[IMAGE alt='' src='']

#### INFO: References

References

- ISO 26262-1:2018 Road vehicles-Functional safety
- Tables and diagrams

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="229a5782-5207-42a0-ae6b-698c1e1367dd"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Damage Scenario</strong></p><p>Adverse consequence involving a vehicle or vehicle function and affecting a road user.</p><p><strong>Effect</strong></p><p>Allows you to define and manage system and vehicle level effects that can result in harm.</p><p><strong>Failure</strong></p><p>Termination of an intended behavior of an element or an item due to a fault manifestation.</p><p><strong>Operational Situation </strong></p><p>A scenario that can occur during a vehicle's life.</p><p><strong>Impact category</strong></p><p>Impact rating is done for four categories: Safety, Financial, Operational, and Privacy.  The assessment should be done according to the definition given in ISO/SAE 21434:2021(annex F).</p><p><strong><ac:inline-comment-marker ac:ref="f9331154-8121-4939-80cf-3a54ebb5a194">Impact scale</ac:inline-comment-marker></strong></p><p>By default, the plugin adopts the scale provided in the ISO/SAE 21434:2021 <ac:inline-comment-marker ac:ref="f55a94f1-8539-4dda-8a8d-eee0cacf6d5e">standard: <span style="color: rgb(23,43,77);">Negligible / Moderate / Major or Severe.</span></ac:inline-comment-marker></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Damage Scenario</h3><p>To create a Damage Scenario</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click <strong>Damage Scenario and Impact Ratings</strong> and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Damage</strong> <strong>Scenario</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="3 DirectlySelectDamageScenario.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword damage and then select<span> </span><strong>Damage Scenario.<br /><br /><ac:image><ri:attachment ri:filename="2 WriteDamage.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Damage Scenario in the Containment tree and press Enter. The Damage Scenario has the prefix <span><strong>D</strong></span><strong>S</strong> which denotes the created element is a Damage Scenario; the number <strong style="text-align: left;">1</strong> indicates that it is the first Damage Scenario created.<br /><br /><ac:image><ri:attachment ri:filename="4 DamageScenarioCreated.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /></span></li></ol><h3><span style="color: rgb(62,63,64);">Creating a Damage Scenarios Table<br /></span></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d04b1ff4-bbca-47f1-9e94-886674d33795"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color: rgb(23,43,77);">, then an<span> </span><strong>Damage Scenarios Table<span> </span></strong>already exists in the<span> <strong>1.1 Damage Scenarios and Impact Ratings</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create a <span style="color: rgb(62,63,64);">Damage Scenario </span>Table</p><hr /><ol><li><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">In the Containment tree, right-click </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">Damage Scenario and Impact Ratings</ac:inline-comment-marker></strong><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">and select</ac:inline-comment-marker><strong><span><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">Create Diagram.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Create Diagram_Command.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Damage Scenario Table</strong>.</span><strong><br /><br /><ac:image><ri:attachment ri:filename="Damage Scenario Table Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword damage and then select<span> </span><strong>Damage Scenarios Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="198"><ri:attachment ri:filename="Damage Scenario Table_Seach.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong>The Damage Scenarios Table is displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="1 ContainmentTreeDamageScenariosTable.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image></li></ul></li></ol><h3>Adding a Damage Scenario to the Damage Scenarios Table</h3><p>To add a new Damage Scenario to the Damage Scenarios Table</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Damage Scenario Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add New. </strong><span style="color: rgb(62,63,64);">A row is added in the Damage Scenarios Table, which shows the new Damage Scenario.</span><br /><strong style="text-align: left;"><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">In the newly created Damage Scenario's row and the <strong>Name </strong>column, double-click the designated cell to name the Damage Scenario.<br /><br /><ac:image ac:height="210"><ri:attachment ri:filename="2 AfterAddingDamageScenario.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color: rgb(62,63,64);">To add an existing Damage Scenario to the Damage Scenarios Table</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Damage Scenarios Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="3 ClickAddExisting.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Damage Scenario </strong>dialog, select the required Damage Scenario. A row is added to the Damage Scenarios Table, which shows the existing Damage Scenario. <br /><br /><ac:image><ri:attachment ri:filename="4 SelectExistingDamageScenario_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">In the existing Damage Scenario's row and the <strong>Name </strong>column, double-click the designated cell to rename the Damage Scenario.<br /><br /><ac:image><ri:attachment ri:filename="5 AfterAddingExistingDamageScenario.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br style="text-align: left;" /></span></li></ol><h3>Adding a Failure</h3><p>To add a Failure to the Damage Scenarios Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Failure </strong>column and the required Damage Scenario's row and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickThreeDots_Failure.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></li><li>From the <strong>Select Class</strong><strong> </strong>dialog, select Failure.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectFailureWindow_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br />The Failure is shown in the Damage Scenarios Table.<br /><br /><ac:image ac:height="223"><ri:attachment ri:filename="3 AfterAddingFailure.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2a741443-4456-43c3-9b41-ecd0582595e3"><ac:rich-text-body><p>You can also drag and drop the Failure modes from the Containment tree to the Damage Scenarios Table.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Adding an Effect</h3><p>To add an Effect in the Damage Scenarios Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Effect </strong>column and the required Damage Scenario's row and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickThreeDots_Effect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></li><li>From the <strong>Select Class</strong><strong> </strong>dialog, select Effect.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectEffectWindow_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br />The Effect is shown in the Damage Scenarios Table.<br /><br /><ac:image><ri:attachment ri:filename="3 AfterAddingEffect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="71709c22-7e35-46d3-b43f-89e912b6a30b"><ac:rich-text-body><p>You can also drag and drop the Effects such as Vehicle Level Effects and System Level Effects from the Containment tree to the Damage Scenarios Table.</p></ac:rich-text-body></ac:structured-macro><h3>Adding an Operational Situation</h3><p>To add an Operational Situation in the Damage Scenarios Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Operational Situation </strong>column and the required Damage Scenario's row and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickThreeDots_Operation Situation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br /></li><li>From the <strong>Select Class </strong>dialog, select Operational Situation.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectOpSituation_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /><br />The Operational Situation is added in the Damage Scenarios Table.<br /><br /><ac:image><ri:attachment ri:filename="3 AfterAddingOpSituation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b5b6c59c-57af-4ec2-8384-d1a99f663c5d"><ac:rich-text-body><p>You can also drag and drop the Operation Situations from the Containment tree to the Damage Scenarios Table.</p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="516ed4d0-1fc9-40ad-948c-245338bcaeb1">Rating SFOP Impact</ac:inline-comment-marker></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c30dc5fb-c3ec-4666-a078-efae78e20973"><ac:rich-text-body><ul><li>The Damage Scenario cannot be rated if there is no Effect associated to it.</li><li>All the Damage Scenarios sharing the same Effect get the same impact ratings. In such case, if you update any impact rating(s) for one Damage Scenario, the impact rating(s) for other Damage Scenarios are updated.</li></ul></ac:rich-text-body></ac:structured-macro><br /><p><span style="letter-spacing: 0.0px;">To rate the SFOP Impact</span></p><hr /><ul><li><span style="color: rgb(62,63,64);">  Double-click each cell,<span> </span></span><span style="color: rgb(22,22,22);">namely<span> <strong>Safety Impact</strong>, <strong>Financial Impact</strong>, <strong>Operational Impact</strong>, and <strong>Privacy Impact </strong>in the Damage Scenario </span></span><span style="color: rgb(62,63,64);">row. From the drop-down list, select the impact rating.<br /><br /><ac:image><ri:attachment ri:filename="Impact Rating selection.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br />The Impact rating is done in the Damage Scenarios Table.<br /><br /><ac:image><ri:attachment ri:filename="Impact Rating selected.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image><br /></span></li></ul><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2c0ad3e4-67f2-44fa-ba80-78757c382bd7"><ac:rich-text-body><p>The plugin behavior when you use the Effect element from the used project in your local project:</p><ul><li>When you update the SFOP Impact ratings of the damage scenario, a cloned Effect element is created in your local project and is visible in the Containment tree. The following notification message is displayed with the cloned Effect element link at the bottom right corner of the modeling tool.<br /><br /><ac:image ac:height="121"><ri:attachment ri:filename="Cloned_Notification.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image></li></ul><p>The plugin behavior when you use the Effect element from the used project in the TWC server project:</p><ul><li>When you update the SFOP Impact ratings of the damage scenario, a cloned Effect element is created in your server project and is visible in the Containment tree. The following notification message is displayed with the cloned Effect element link at the bottom right corner of the modeling tool.<br /><br /><ac:image ac:height="121"><ri:attachment ri:filename="Cloned_Notification.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image></li></ul><p>The plugin behavior when you use the Effect element from your own TWC server project:</p><ul><li>When you update the SFOP ratings of the damage scenario and the Effect element is in a read-only state, the Effect element gets locked automatically by you.</li><li>When you update the SFOP ratings of the damage scenario and the Effect element is locked by another user, the following notification is displayed with the locked Effect element link at the bottom right corner of the modeling tool.<br /><br /><ac:image ac:height="154"><ri:attachment ri:filename="Locked_Notification.PNG"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target"><ac:inline-comment-marker ac:ref="7eba9344-79dc-4ea0-a9f1-d01cabdc6bf2">Damage Scenarios Table Example</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Damage Scenarios Example.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Damage scenario" /></ri:attachment></ac:image></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b327f344-eb80-4f95-8e82-df85cdda6744"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a class="external-link" href="https://www.iso.org/obp/ui">ISO 26262-1:2018 Road vehicles-Functional safety</a></li><li><a href="https://docs.nomagic.com/display/CSRA2024xR1/Tables+and+diagrams">Tables and diagrams</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466587 space=CSRA2024xR1 version=1 -->
## PAGE 00022: Decomposing ASIL

- page_id: `170466587`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466587/Decomposing+ASIL
- version_number: 1
- version_date: `2019-10-30T09:53:32.058+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams > Safety Requirement Diagram
- labels: []

### NORMALIZED CONTENT

The Automotive Safety Integrity Level (ASIL) expresses the criticality associated with a function of the system. It defines the safety requirements that must be fulfilled by the design and development of the system in such a way that, even in conditions of failure, the system provides a sufficient margin of safety for the users (driver, passengers, road traffic participants, etc.). Under certain circumstances, the ASIL can be lowered through the technique of ASIL decomposition.

The following table displays valid ASIL decomposition combinations:

| ASIL value | ASIL decomposition combinations |  |  |
| --- | --- | --- | --- |
| D | C(D) + A(D) | B(D) + B(D) | D(D) + QM(D) |
| D(D) | C(D) + A(D) | B(D) + B(D) | D(D) + QM(D) |
| C | B(C) + A(C) | C(C) + QM(C) |  |
| C(D) | B(D) + A(D) | C(D) + QM(D) |  |
| C(C) | B(C) + A(C) | C(C) + QM(C) |  |
| B | A(B) + A(B) | B(B) + QM(B) |  |
| B(D) | A(D) + A(D) | B(D) + QM(D) |  |
| B(C) | A(C) + A(C) | B(C) + QM(C) |  |
| B(B) | A(B) + A(B) | B(B) + QM(B) |  |
| A | A(A) + QM(A) |  |  |
| A(D) | A(D) + QM(D) |  |  |
| A(C) | A(C) + QM(C) |  |  |
| A(B) | A(B) + QM(B) |  |  |
| A(A) | A(A) + QM(A) |  |  |

To decompose an ASIL value

1. In a [CONFLUENCE_PAGE title='Safety Requirement Diagram' space='CSRA2024xR1'] , create two Safety Requirements and name them. These will be the Requirements with decomposed (lower) ASIL values.
2. Create ASIl Decomposition relationships from the Safety Requirements created in the previous step to the Safety Requirement whose ASIL value you want to decompose.
3. Right-click the shape of one of the Safety Requirements created in step 1, select ASIL , and select the desired ASIL value for that Requirement . The ASIL value of the other Safety Requirement is specified automatically according to the ASIL decomposition rules described in the above table. [ATTACHMENT filename='specifying_asil_values.png']
4. In the same diagram, create one more Safety Requirement.
5. Create the Independence Req relationship from the Requirement created in the previous step to the Safety Requirement whose ASIL value you decomposed.

After completing the above steps, your diagram should look similar to the sample diagram shown below.

[IMAGE alt='' src='']

###### A sample Safety Requirement Diagram displaying how to decompose the ASIL value of the *Detect Deviation* Safety Requirement.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Automotive Safety Integrity Level (ASIL) expresses the criticality associated with a function of the system. It defines the safety requirements that must be fulfilled by the design and development of the system in such a way that, even in conditions of failure, the system provides a sufficient margin of safety for the users (driver, passengers, road traffic participants, etc.). Under certain circumstances, the ASIL can be lowered through the technique of ASIL decomposition.</p><p>The following table displays valid ASIL decomposition combinations:</p><table class="relative-table" style="width: 45.9682%;"><colgroup><col style="width: 14.8148%;" /><col style="width: 27.1207%;" /><col style="width: 29.5102%;" /><col style="width: 28.5544%;" /></colgroup><tbody><tr><th style="text-align: center;">ASIL value</th><th style="text-align: center;" colspan="3"><p>ASIL decomposition combinations</p></th></tr><tr><th style="text-align: center;">D</th><td style="text-align: center;">C(D) + A(D)</td><td style="text-align: center;">B(D) + B(D)</td><td style="text-align: center;">D(D) + QM(D)</td></tr><tr><th style="text-align: center;">D(D)</th><td style="text-align: center;"><span>C(D) + A(D)</span></td><td style="text-align: center;"><span>B(D) + B(D)</span></td><td style="text-align: center;"><span>D(D) + QM(D)</span></td></tr><tr><th style="text-align: center;">C</th><td style="text-align: center;">B(C) + A(C)</td><td style="text-align: center;">C(C) + QM(C)</td><td style="text-align: center;"><br /></td></tr><tr><th style="text-align: center;">C(D)</th><td style="text-align: center;">B(D) + A(D)</td><td style="text-align: center;">C(D) + QM(D)</td><td style="text-align: center;"><br /></td></tr><tr><th style="text-align: center;">C(C)</th><td style="text-align: center;">B(C) + A(C)</td><td style="text-align: center;">C(C) + QM(C)</td><td style="text-align: center;"><br /></td></tr><tr><th style="text-align: center;">B</th><td style="text-align: center;">A(B) + A(B)</td><td style="text-align: center;">B(B) + QM(B)</td><td style="text-align: center;"><br /></td></tr><tr><th style="text-align: center;">B(D)</th><td style="text-align: center;">A(D) + A(D)</td><td style="text-align: center;">B(D) + QM(D)</td><td style="text-align: center;"><br /></td></tr><tr><th style="text-align: center;" colspan="1">B(C)</th><td style="text-align: center;" colspan="1">A(C) + A(C)</td><td style="text-align: center;" colspan="1">B(C) + QM(C)</td><td style="text-align: center;" colspan="1"><br /></td></tr><tr><th style="text-align: center;" colspan="1">B(B)</th><td style="text-align: center;" colspan="1">A(B) + A(B)</td><td style="text-align: center;" colspan="1">B(B) + QM(B)</td><td style="text-align: center;" colspan="1"><br /></td></tr><tr><th style="text-align: center;" colspan="1">A</th><td style="text-align: center;" colspan="1">A(A) + QM(A)</td><td style="text-align: center;" colspan="1"><br /></td><td style="text-align: center;" colspan="1"><br /></td></tr><tr><th style="text-align: center;" colspan="1">A(D)</th><td style="text-align: center;" colspan="1">A(D) + QM(D)</td><td style="text-align: center;" colspan="1"><br /></td><td style="text-align: center;" colspan="1"><br /></td></tr><tr><th style="text-align: center;" colspan="1">A(C)</th><td style="text-align: center;" colspan="1">A(C) + QM(C)</td><td style="text-align: center;" colspan="1"><br /></td><td style="text-align: center;" colspan="1"><br /></td></tr><tr><th style="text-align: center;" colspan="1">A(B)</th><td style="text-align: center;" colspan="1">A(B) + QM(B)</td><td style="text-align: center;" colspan="1"><br /></td><td style="text-align: center;" colspan="1"><br /></td></tr><tr><th style="text-align: center;" colspan="1">A(A)</th><td style="text-align: center;" colspan="1">A(A) + QM(A)</td><td style="text-align: center;" colspan="1"><br /></td><td style="text-align: center;" colspan="1"><br /></td></tr></tbody></table><p><br /></p><p>To decompose an ASIL value</p><hr /><ol><li>In a <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety Requirement Diagram" /></ac:link>, create two Safety Requirements and name them. These will be the Requirements with decomposed (lower) ASIL values.</li><li>Create ASIl Decomposition relationships from the Safety Requirements created in the previous step to the Safety Requirement whose ASIL value you want to decompose.</li><li>Right-click the shape of one of the Safety Requirements created in step 1, select <strong>ASIL</strong>, and select the desired ASIL value for that <ac:inline-comment-marker ac:ref="0422d063-70e6-4c98-b780-073fc33f94cb">Requirement</ac:inline-comment-marker>. The ASIL value of the other Safety Requirement is specified automatically according to the ASIL decomposition rules described in the above table.<br /><br /><ac:image><ri:attachment ri:filename="specifying_asil_values.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Decomposing ASIL" /></ri:attachment></ac:image><br /><br /></li><li>In the same diagram, create one more Safety Requirement.</li><li>Create the Independence Req relationship from the Requirement created in the previous step to the Safety Requirement whose ASIL value you decomposed.</li></ol><p><br />After completing the above steps, your diagram should look similar to the sample diagram shown below. </p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="asil_decomposition.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Decomposing ASIL" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A sample Safety Requirement Diagram displaying how to decompose the ASIL value of the <em>Detect Deviation</em> Safety Requirement.</h6>
````

<!--NOMAGIC_PAGE id=170466466 space=CSRA2024xR1 version=2 -->
## PAGE 00023: Describing FMEA Items

- page_id: `170466466`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466466/Describing+FMEA+Items
- version_number: 2
- version_date: `2024-05-08T14:01:15.334+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Reliability analysis using FMEA
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Productivity tip

948849469

#### CONTENT-COLUMN: Productivity tip

948849471

948861679

**On this page**

4

#### CONTENT-BLOCK: Productivity tip

948849470

FMEA Items should be described in an FMEA Table. Since FMEA Tables are based on [CONFLUENCE_PAGE title='Generic table' space='MD2024xR1'], the [CONFLUENCE_PAGE title='Table toolbars' space='MD2024xR1'] and the [CONFLUENCE_PAGE title='Table Criteria area' space='MD2024xR1'] work in the same manner.

An FMEA Table allows you to analyze the reliability aspect of your model, and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. In an FMEA Table, you can:

- Create a new FMEA Item directly in a table or add an existing one.
- Directly edit the properties of FMEA Items in a table.
- Generate an FMEA analysis report, and export a table into a CSV or HTML file format.

An FMEA Table has the following columns:

| Table column name | Description |
| --- | --- |
| Id | An FMEA Item ID. |
| Name | The name of an FMEA Item. |
| Classification | The classification of failures (FMEA Items) by certain aspects of a system. |
| Item | The design model element (Block, Part, Operation or Activity) undergoing analysis related to a particular FMEA Item.Parts or Blocks?It is recommended that you select Parts instead of Blocks, because Blocks may be too generic. |
| Subsystem | An element identifying the subsystem of a model to which an Item belongs. The valid values are Parts and Blocks. |
| Failure Mode | An element describing the specific manner in which a component, subsystem, system, process, etc., could potentially fail to meet the design intent. |
| Local Effect of Failure | An element describing the effect that a Failure Mode has on the system element under consideration. An FMEA Item, e.g, a single row of an FMEA Table, can have multiple Local Effects of Failure. |
| Final Effect of Failure | An element describing the effect that Failure Mode has on an end user or environment. You can specify multiple Final Effect of Failure values for a single FMEA Item.Every Final Effect of Failure can have a default severity value assigned as its property. To assign a value, open the of a Final Effect of Failure, and set the desired Severity value.Adding severity valuesIf you add a Final Effect of Failure with a specified severity value to a certain row of an FMEA Table for the first time, the value is automatically entered into the appropriate cell of the SEV column. The value is entered even if the cell already has a value specified. You can manually change the severity value that was automatically added to an FMEA Table. This action does not change the default severity value assigned to this specific Final Effect of Failure element. |
| SEV | A property describing the assessment of the severity of the effect(s) of a potential Failure Mode on a component, subsystem, end-user, or environment. The valid values of this property are 1 to 4 (lowest to highest severity).Click an appropriate cell to select its value from a drop-down list. |
| Cause of Failure | An element indicating the design weakness causing a Failure Mode. An FMEA Item, e.g., a single row of an FMEA Table, can have multiple Causes of Failure.Every Cause of Failure can have a default occurrence and/or detectability value(s) assigned as its property(ies). To assign an occurrence or value, open the of a Cause of Failure, and set the desired Occurrence and/or Detectability value(s).Adding occurrence and detectability valuesIf you add a Cause of Failure with a specified occurrence or detectability value (or both) to a certain row of an FMEA Table for the first time, this value is automatically entered into an appropriate cell of the OCC or DET column. The value is entered even if the cell already has a value specified. You can manually change the occurrence or detectability value that was automatically added to an FMEA Table. This action does not change the default occurrence or detectability value assigned to the specific Cause of Failure element. |
| OCC | Occurrence (OCC) is a property showing the likelihood that a specific Cause of Failure will occur. The valid values of this property are 1 to 5 (lowest to highest probability of occurrence).Click an appropriate cell to select its value from a drop-down list. |
| Prevention ControlandDetection Control | A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode. A Detection Control element describes the measures for detecting a Failure Mode, if it occurs. You can specify multiple Prevention and Detection Control values for a single FMEA Item.Reusing Prevention and Detection Control valuesIn an FMEA Table, each Prevention Control and Detection Control value is usually related to a specific Cause of Failure. After adding a Cause of Failure to a specific row of a table, you can quickly reuse the Prevention Control and/or Detection Control value(s) associated with it in another row of the same table. To reuse the values:Right-click the row where you want to reuse a previously associated Prevention Control and/or Detection Control value(s). This row should already have a Cause of Failure element specified.From the open menu, select Reuse Design Controls. If the Cause of Failure has a reusable Detection Control and/or Prevention Control element(s), the Reuse Design Controls dialog opens.In the open dialog, select the element(s) you want to reuse as Prevention Control and/or Detection Control value(s), and click OK. |
| DET | Detectability (DET) measures the likelihood of discovering a possible failure prior to its occurrence. The valid values of this property are 1 to 5 (highest to lowest detectability).Click an appropriate column cell to select its value from a drop-down list. |
| OxD | The product of OCC and DET ratings. |
| RPN | A risk priority number is a derived property calculated by using a customizable function. By default, the function includes SEV, OCC, and DET values. |
| Hazard Analysis Reference | The Hazard Analysis Reference to a Safety Analysis Item shows that the safety aspect has been analyzed for this particular FMEA Item. |
| Required Hazard Analysis | A property indicating whether or not an FMEA Item requires hazard analysis. The valid values of this property are true or false. If you create your project using the Safety and Reliability Analysis Project template, the FMEA Items marked as requiring hazard analysis are added to the FMEAs to Be Analyzed package. If not, you must configure a Smart Package to manually filter these elements. When a specific FMEA Item is addressed in a Safety Analysis Item, it is removed from the FMEAs to Be Analyzed package after refreshing your model. |
| Recommended Action | The description of a recommended action that will reduce RPN. All critical or significant failures (FMEA Items) should have recommended actions associated with them. Recommended actions should be focused on design, and directed towards mitigating the Cause of Failure or eliminating the Failure Mode. |
| Mitigation | The reference to any element that mitigates a failure. |
| Responsibility | A property indicating the person responsible for completing a Recommended Action. |
| Target Completion Date | A property defining the completion date of a Recommended Action. The value of the Target Completion Date property can be specified in the Date and Time Settings dialog. |
| Action Taken | A property describing what actions have been taken and the results of these actions. |
| Reduced SEV | A property assessing the seriousness of the effect(s) that a potential Failure Mode has on a component, subsystem, end-user, or environment after the mitigation. The valid values of this property are 1 to 4 (lowest to highest severity).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced OCC | Reduced occurrence is a property showing the likelihood that a specific Cause of Failure will occur after the mitigation. The valid values of this property are 1 to 5 (lowest to highest probability of occurrence).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced DET | Reduced detectability measures the likelihood of discovering a possible failure after the mitigation. The valid values of this property are 1 to 5 (highest to lowest detectability).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced OxD | The product of the Reduced OCC and Reduced DET ratings. |
| Reduced RPN | A reduced risk priority number is a derived property calculated by using a customizable function. By default, the function includes Reduced SEV, Reduced OCC, and Reduced DET values. |

##### Creating an FMEA Table

To keep your model clean and simple, you should create an FMEA Table in the package that contains FMEA Items that are to be included in the table.

To create an FMEA Table

1. Do one of the following:
  - Right-click the Package in which you want to create an FMEA Table, and select Create Diagram from the menu.
  - Select the Package in which you want to create an FMEA Table, and click the Create Diagram button on the main toolbar.
2. Click FMEA Table under the Safety and Reliability Analysis group.
3. If needed, change the name of the newly created FMEA Table.

A new FMEA Table has been created in the selected Package. Now you should add FMEA Items to the table, as described in the next section.

##### Adding FMEA Items to an FMEA Table

There are two ways to add FMEA Items to an FMEA Table:

- Create new FMEA Items directly in the table.
- Add existing FMEA Items to the table.

To create a new FMEA Item in an FMEA Table

- Do one of the following:
- Click the Add New button on the table toolbar.
- Press Insert (Cmd+I on Mac OS).

A row containing a newly created FMEA Item is added at the end of the table. In the model browser, the FMEA Item is placed in the Package containing the related FMEA Table. Now you can define the FMEA Item directly in the table by double-clicking an appropriate cell.

#### INFO: Model structure information

Model structure information

To have a clear model structure, you should create FMEA Items in dedicated Packages.

To add an existing FMEA Item to an FMEA Table

1. Do one of the following:
  - Click the Add Existing button on the table toolbar.
  - Press Ctrl+Insert (Cmd+E on Mac OS).
2. In the open dialog, select the FMEA Item you want to add to the table. To [CONFLUENCE_PAGE title='Elements multiple selection' space='MD2024xR1'] , click [ATTACHMENT filename='multiple_selection.png'] , and add the desired FMEA Items to the Selected elements area on the right side of the dialog.
3. Click OK .

#### TIP: Productivity tip

Productivity tip

To make your work quicker, you can add existing FMEA Items to an FMEA Table by dragging them directly to the table. Simply select one or more FMEA Items in the model browser and drag them to an FMEA Table. New rows for the added elements are created automatically.

Selected FMEA Items are added to the FMEA Table as new rows. You can change the properties of the added elements directly in the table by double-clicking an appropriate cell.

948849467

**Related pages**

- [CONFLUENCE_PAGE title='Reliability analysis using FMEA' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Cloning FMEA Table rows' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f67dbf25-1273-45a6-bcb9-e5e25e426e43"><ac:parameter ac:name="id">948849469</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="e529283d-8ee3-4aee-825c-1d5b2c475925"><ac:parameter ac:name="id">948849471</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="58a7146f-dd00-45fe-8d7d-bb644d8afcd2"><ac:parameter ac:name="id">948861679</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="855c8378-2dc2-48d3-a7fb-0e512ace84a5"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2ec8fac7-f658-473e-939b-49f9ab467dc7"><ac:parameter ac:name="id">948849470</ac:parameter><ac:rich-text-body><p>FMEA Items should be described in an FMEA Table. Since FMEA Tables are based on <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Generic table" /><ac:plain-text-link-body><![CDATA[Generic Tables]]></ac:plain-text-link-body></ac:link>, the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Table toolbars" /><ac:plain-text-link-body><![CDATA[toolbar]]></ac:plain-text-link-body></ac:link> and the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Table Criteria area" /><ac:plain-text-link-body><![CDATA[Criteria area]]></ac:plain-text-link-body></ac:link> work in the same manner.</p><p>An FMEA Table allows you to analyze the reliability aspect of your model, and provides you with a convenient way to fill in FMEA Item information using a spreadsheet-like tabular format. Each row in a table represents an FMEA Item. Table columns represent the properties of FMEA Items. In an FMEA Table, you can:</p><ul><li>Create a new FMEA Item directly in a table or add an existing one.</li><li>Directly edit the properties of FMEA Items in a table.</li><li>Generate an FMEA analysis report, and export a table into a CSV or HTML file format. </li></ul><p><br />An FMEA Table has the following columns:</p><table class="relative-table" style="width: 100.0%;"><colgroup><col style="width: 16.3882%;" /><col style="width: 83.6118%;" /></colgroup><tbody><tr><th>Table column name</th><th>Description</th></tr><tr><td colspan="1"><strong>Id</strong></td><td colspan="1">An FMEA Item ID.</td></tr><tr><td colspan="1"><strong>Name</strong></td><td colspan="1">The name of an FMEA Item.</td></tr><tr><td colspan="1"><strong>Classification</strong></td><td colspan="1">The classification of failures (FMEA Items) by certain aspects of a system.</td></tr><tr><td colspan="1"><strong>Item</strong></td><td colspan="1"><div class="content-wrapper"><p>The design model element (Block, Part, Operation or Activity) undergoing analysis related to a particular FMEA Item.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="31347255-6565-4b20-a4b4-6e40da57c99e"><ac:parameter ac:name="title">Parts or Blocks?</ac:parameter><ac:rich-text-body><p>It is recommended that you select Parts instead of Blocks, because Blocks may be too generic.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td colspan="1"><strong>Subsystem</strong></td><td colspan="1">An element identifying the subsystem of a model to which an Item belongs. The valid values are Parts and Blocks.</td></tr><tr><td colspan="1"><strong>Failure Mode</strong></td><td colspan="1">An element describing the specific manner in which a component, subsystem, system, process, etc., could potentially fail to meet the design intent.</td></tr><tr><td colspan="1"><strong>Local Effect of Failure</strong></td><td colspan="1">An element describing the effect that a Failure Mode has on the system element under consideration. An FMEA Item, e.g, a single row of an FMEA Table, can have multiple Local Effects of Failure.</td></tr><tr><td colspan="1"><strong>Final Effect of Failure</strong></td><td colspan="1"><div class="content-wrapper"><p>An element describing the effect that Failure Mode has on an end user or environment. You can specify multiple Final Effect of Failure values for a single FMEA Item.</p><p>Every Final Effect of Failure can have a default severity value assigned as its property. To assign a value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Final Effect of Failure, and set the desired <strong>Severity</strong> value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="202dad50-ca70-4b9b-9b39-f1376a444aff"><ac:parameter ac:name="title">Adding severity values</ac:parameter><ac:rich-text-body><p>If you add a Final Effect of Failure with a specified severity value to a certain row of an FMEA Table for the first time, the value is automatically entered into the appropriate cell of the SEV column. The value is entered even if the cell already has a value specified. You can manually change the severity value that was automatically added to an FMEA Table. This action does not change the default severity value assigned to this specific Final Effect of Failure element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>SEV</strong></td><td><p>A property describing the assessment of the severity of the effect(s) of a potential Failure Mode on a component, subsystem, end-user, or environment. The valid values of this property are 1 to 4 (lowest to highest severity).</p><p>Click an appropriate cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Cause of Failure </strong></td><td colspan="1"><div class="content-wrapper"><p>An element indicating the design weakness causing a Failure Mode. An FMEA Item, e.g., a single row of an FMEA Table, can have multiple Causes of Failure.</p><p>Every Cause of Failure can have a default occurrence and/or detectability value(s) assigned as its property(ies). To assign an occurrence or value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Cause of Failure, and set the desired <strong>Occurrence</strong> and/or<strong> Detectability</strong> value(s).</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4f5767f0-016d-4226-b667-3294310b41b0"><ac:parameter ac:name="title">Adding occurrence and detectability values</ac:parameter><ac:rich-text-body><p>If you add a Cause of Failure with a specified occurrence or detectability value (or both) to a certain row of an FMEA Table for the first time, this value is automatically entered into an appropriate cell of the OCC or DET column. The value is entered even if the cell already has a value specified. You can manually change the occurrence or detectability value that was automatically added to an FMEA Table. This action does not change the default occurrence or detectability value assigned to the specific Cause of Failure element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td colspan="1"><strong>OCC</strong></td><td colspan="1"><p>Occurrence (OCC) is a property showing the likelihood that a specific Cause of Failure will occur. The valid values of this property are 1 to 5 (lowest to highest probability of occurrence).</p><p>Click an appropriate cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><p><strong>Prevention Control</strong></p><p>and</p><p><strong>Detection Control</strong></p></td><td colspan="1"><div class="content-wrapper"><p><span style="color: rgb(0,0,0);">A Prevention Control element describes the measures for preventing the occurrence of a possible Failure Mode.</span> <span style="color: rgb(0,0,0);">A Detection Control element describes the measures for detecting a Failure Mode, if it occurs.</span> You can specify multiple Prevention and Detection Control values for a single FMEA Item.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a55a2653-1a5c-4602-80cd-2b15196840e5"><ac:parameter ac:name="title">Reusing Prevention and Detection Control values</ac:parameter><ac:rich-text-body><p>In an FMEA Table, each Prevention Control and Detection Control value is usually related to a specific Cause of Failure. After adding a Cause of Failure to a specific row of a table, you can quickly reuse the Prevention Control and/or Detection Control value(s) associated with it in another row of the same table. To reuse the values:</p><ol><li>Right-click the row where you want to reuse a previously associated Prevention Control and/or Detection Control value(s). This row should already have a Cause of Failure element specified.</li><li>From the open menu, select <strong>Reuse Design Controls</strong>. If the Cause of Failure has a reusable Detection Control and/or Prevention Control element(s), the <strong>Reuse Design Controls</strong> dialog opens.</li><li>In the open dialog, select the element(s) you want to reuse as Prevention Control and/or Detection Control value(s), and click <strong>OK</strong>.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td colspan="1"><strong>DET</strong></td><td colspan="1"><p>Detectability (DET) measures the likelihood of discovering a possible failure prior to its occurrence. The valid values of this property are 1 to 5 (highest to lowest detectability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>OxD</strong></td><td colspan="1">The product of OCC and DET ratings.</td></tr><tr><td colspan="1"><strong>RPN</strong></td><td colspan="1">A risk priority number is a derived property calculated by using a customizable function. By default, the function includes SEV, OCC, and DET values.</td></tr><tr><td colspan="1"><strong>Hazard Analysis Reference</strong></td><td colspan="1"><p>The Hazard Analysis Reference to a Safety Analysis Item shows that the safety aspect has been analyzed for this particular FMEA Item.</p></td></tr><tr><td><strong>Required Hazard Analysis</strong></td><td><p>A property indicating whether or not an FMEA Item requires hazard analysis. The valid values of this property are <em>true</em> or <em>false</em>. If you create your project using the <em>Safety and Reliability Analysis Project</em> template, the FMEA Items marked as requiring hazard analysis are added to the <em>FMEAs to Be Analyzed</em> package. If not, you must configure a Smart Package to manually filter these elements. When a specific FMEA Item is addressed in a Safety Analysis Item, it is removed from the <em>FMEAs to Be Analyzed</em> package after refreshing your model.</p></td></tr><tr><td colspan="1"><strong>Recommended Action</strong></td><td colspan="1">The description of a recommended action that will reduce RPN. All critical or significant failures (FMEA Items) should have recommended actions associated with them. Recommended actions should be focused on design, and directed towards mitigating the Cause of Failure or eliminating the Failure Mode.</td></tr><tr><td colspan="1"><strong>Mitigation</strong></td><td colspan="1">The reference to any element that mitigates a failure.</td></tr><tr><td colspan="1"><strong>Responsibility</strong></td><td colspan="1">A property indicating the person responsible for completing a Recommended Action.</td></tr><tr><td colspan="1"><strong>Target Completion Date</strong></td><td colspan="1">A property defining the completion date of a Recommended Action. The value of the Target Completion Date property can be specified in the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Setting date and time" /><ac:link-body><strong>Date and Time Settings</strong> dialog</ac:link-body></ac:link>.</td></tr><tr><td colspan="1"><strong>Action Taken</strong></td><td colspan="1">A property describing what actions have been taken and the results of these actions.</td></tr><tr><td colspan="1"><p><strong>Reduced SEV</strong></p></td><td colspan="1"><p>A property assessing the seriousness of the effect(s) that a potential Failure Mode has on a component, subsystem, end-user, or environment after the mitigation. The valid values of this property are 1 to 4 (lowest to highest severity).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced OCC</strong></td><td colspan="1"><p>Reduced occurrence is a property showing the likelihood that a specific Cause of Failure will occur after the mitigation. The valid values of this property are 1 to 5 (lowest to highest probability of occurrence).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced DET</strong></td><td colspan="1"><p>Reduced detectability measures the likelihood of discovering a possible failure after the mitigation. The valid values of this property are 1 to 5 (highest to lowest detectability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced OxD</strong></td><td colspan="1">The product of the Reduced OCC and Reduced DET ratings.</td></tr><tr><td colspan="1"><strong>Reduced RPN</strong></td><td colspan="1">A reduced risk priority number is a derived property calculated by using a customizable function. By default, the function includes Reduced SEV, Reduced OCC, and Reduced DET values.</td></tr></tbody></table><h3><br />Creating an FMEA Table</h3><p>To keep your model clean and simple, you should create an FMEA Table in the package that contains FMEA Items that are to be included in the table.<br /> </p><p>To create an FMEA Table</p><hr /><ol><li>Do one of the following:<br /><ul><li>Right-click the Package in which you want to create an FMEA Table, and select <strong>Create Diagram</strong> from the menu.</li><li>Select the Package in which you want to create an FMEA Table, and click the <strong>Create Diagram</strong> button on the main toolbar.</li></ul></li><li>Click <strong>FMEA Table</strong> under the <strong>Safety and Reliability Analysis</strong> group.</li><li>If needed, change the name of the newly created FMEA Table.</li></ol><p>A new FMEA Table has been created in the selected Package. Now you should add FMEA Items to the table, as described in the next section.<br /> </p><h3>Adding FMEA Items to an FMEA Table</h3><p>There are two ways to add FMEA Items to an FMEA Table:</p><ul><li>Create new FMEA Items directly in the table.</li><li>Add existing FMEA Items to the table.</li></ul><p><br /></p><p>To create a new FMEA Item in an FMEA Table</p><hr /><ul><li>Do one of the following:</li><li style="margin-left: 30.0px;">Click the <strong>Add New</strong> button on the table toolbar.</li><li style="margin-left: 30.0px;">Press Insert (Cmd+I on Mac OS).</li></ul><p><br />A row containing a newly created FMEA Item is added at the end of the table. In the model browser, the FMEA Item is placed in the Package containing the related FMEA Table. Now you can define the FMEA Item directly in the table by double-clicking an appropriate cell.<br /> </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="eace8ed8-522e-4377-8c18-708ffbcd7a23"><ac:parameter ac:name="title">Model structure information</ac:parameter><ac:rich-text-body><p>To have a clear model structure, you should create FMEA Items in dedicated Packages.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To add an existing FMEA Item to an FMEA Table</p><hr /><ol><li>Do one of the following:<br /><ul><li>Click the <strong>Add Existing</strong> button on the table toolbar.</li><li>Press Ctrl+Insert (Cmd+E on Mac OS).</li></ul></li><li>In the open dialog, select the FMEA Item you want to add to the table. To <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Elements multiple selection" /><ac:plain-text-link-body><![CDATA[select multiple elements]]></ac:plain-text-link-body></ac:link>, click <ac:image><ri:attachment ri:filename="multiple_selection.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing FMEA Items" /></ri:attachment></ac:image>, and add the desired FMEA Items to the <strong>Selected elements</strong> area on the right side of the dialog.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="964d4d12-a384-408d-8aca-559c8eb248ff"><ac:parameter ac:name="title">Productivity tip</ac:parameter><ac:rich-text-body><p>To make your work quicker, you can add existing FMEA Items to an FMEA Table by dragging them directly to the table. Simply select one or more FMEA Items in the model browser and drag them to an FMEA Table. New rows for the added elements are created automatically.</p></ac:rich-text-body></ac:structured-macro><p>Selected FMEA Items are added to the FMEA Table as new rows. You can change the properties of the added elements directly in the table by double-clicking an appropriate cell.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="50281a79-47c5-4422-89ac-27c472967350"><ac:parameter ac:name="id">948849467</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Reliability analysis using FMEA" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cloning FMEA Table rows" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466477 space=CSRA2024xR1 version=2 -->
## PAGE 00024: Describing reduced risks

- page_id: `170466477`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466477/Describing+reduced+risks
- version_number: 2
- version_date: `2024-05-08T14:01:15.595+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Safety analysis
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Productivity tip

949334895

#### CONTENT-COLUMN: Productivity tip

949334898

949334893

**On this page**

4

#### CONTENT-BLOCK: Productivity tip

949334897

After the mitigation phase, risks (Safety Analysis Items) can be further described in a Risk Reduction Table. Since Risk Reduction Tables are based on [CONFLUENCE_PAGE title='Generic table' space='MD2024xR1'], the [CONFLUENCE_PAGE title='Table toolbars' space='MD2024xR1'] and the [CONFLUENCE_PAGE title='Table Criteria area' space='MD2024xR1'] work in the same manner.

A Risk Reduction Table allows you to analyze the safety aspect of your model both before and after the mitigation. This gives you an opportunity to evaluate the effectiveness of recommended risk reduction actions. Each row in a table represents a Safety Analysis Item, and table columns represent the properties of Safety Analysis Items. In a Risk Table, you can:

- Create a new Safety Analysis Item directly in a table, or add an existing one.
- Edit the properties of Safety Analysis Items directly in a table.
- Generate a risk analysis report, or export a table into a CSV or HTML file format.

A Risk Table has the following columns:

| Table column name | Description |
| --- | --- |
| Id | Safety Analysis Item ID. |
| FMEA Reference | The reference to an FMEA Item. |
| Initiating Cause | A short description of a Safety Analysis Item. |
| Hazard | A potential source of Harm. |
| Sequence of Events | Sequence of Events leading to a Hazardous Situation.Every Sequence of Events can have a default P1 value assigned as its property. To assign a value, open the of a Sequence of Events, and set the desired P1 value.Adding P1 valuesIf you add a Sequence of Events with a specified P1 value to a certain row of a Risk Reduction Table for the first time, this value is automatically entered into an appropriate cell of the P1 column. The value is entered even if the cell already has a value specified. You can manually change the P1 value that was automatically added to a Risk Reduction Table. This action does not change the default P1 value assigned to this specific Sequence of Events element. |
| Hazardous Situation | A situation in which a subject or an object of the environment is exposed to one or more Hazards.Every Hazardous Situation can have a default P2 value assigned as its property. To assign a value, open the of a Hazardous Situation, and set the desired P2 value.Adding P2 valuesIf you add a Hazardous Situation with a specified P2 value to a certain row of a Risk Reduction Table for the first time, this value is automatically entered into an appropriate cell of the P2 column. The value is entered even if the cell already has a value specified. You can manually change the P2 value that was automatically added to a Risk Reduction Table. This action does not change the default P2 value assigned to this specific Hazardous Situation element. |
| Harm | Damage to the health of people, damage to the property or environment, or both.Every Harm can have a default severity (S) value assigned as its property. To assign a value, open the of a Harm, and set the desired Severity value.Adding severity valuesIf you add a Harm with a specified severity value to a certain row of a Risk Reduction Table for the first time, this value is automatically entered into an appropriate cell of the S column. The value is entered even if the cell already has a value specified. You can manually change the severity value that was automatically added to a Risk Reduction Table. This action does not change the default severity value assigned to this specific Harm element. |
| S | Severity is the quantitative evaluation of the Harm that is caused if exposed to a Hazard. The valid values of this property are 1 to 4 (lowest to highest severity).Click an appropriate column cell to select its value from a drop-down list. |
| P1 | Probability of a foreseeable Sequence of Events leading to a Hazardous Situation. The valid values of this property are 1 to 5 (lowest to highest probability).Click an appropriate column cell to select its value from a drop-down list. |
| P2 | Probability of a Harm occurring when exposed to a Hazard. The valid values of this property are 1 to 5 (lowest to highest probability).Click an appropriate column cell to select its value from a drop-down list. |
| P | The function of P1 and P2. |
| D | Detectability measures the likelihood of discovering and correcting a Hazard prior to Harm occurrence. The valid values of this property are 1 to 5 (highest to lowest detectability).Click an appropriate column cell to select its value from a drop-down list. |
| C | Correctability is the rate of relative ease of mitigating a certain risk. The valid values of this property are 1 to 5 (lowest to highest correctability).Click an appropriate column cell to select its value from a drop-down list. |
| PU | Product Utility shows the clinical benefits of a product, taking into account the risks it holds. The valid values of this property are 1 to 5 (highest to lowest clinical benefits that outweigh the risks).Click an appropriate column cell to select its value from a drop-down list. |
| Risk | A customizable function of P and S. |
| Risk Control Measures Description | A brief, qualitative description of the proposed method of risk control. |
| Risk Control Measures | A reference to the safety requirement that mitigates the risk. |
| Mitigators | A reference to any element that satisfies the related safety requirement. |
| Reduced S | Reduced severity is the quantitative evaluation of the Harm that is caused if exposed to a Hazard after the mitigation (or simply severity value after the mitigation). The valid values of this property are 1 to 4 (lowest to highest severity).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced P1 | Probability of a foreseeable Sequence of Events leading to a Hazardous Situation after the mitigation. The valid values of this property are 1 to 5 (lowest to highest probability).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced P2 | Probability of a Harm occurring when exposed to a Hazard after the mitigation. The valid values of this property are 1 to 5 (lowest to highest probability).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced P | The function of Reduced P1 and Reduced P2. |
| Reduced D | Reduced detectability measures the likelihood of discovering and correcting a Hazard prior to Harm occurrence, but after the mitigation (or simply - detectability value after the mitigation). The valid values of this property are 1 to 5 (highest to lowest detectability).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced C | Correctability is the rate of relative ease of mitigating a certain risk if it is faced after the mitigation. The valid values of this property are 1 to 5 (lowest to highest correctability).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced PU | Reduced Product Utility shows the clinical benefits of a product taking into account the risks it holds after the mitigation (or simply - product utility value after the mitigation). The valid values of this property are 1 to 5 (highest to lowest clinical benefits that outweigh the risks).Click an appropriate column cell to select its value from a drop-down list. |
| Reduced Risk | A customizable function of Reduced P and Reduced S. |
| Use Related | The property indicating a Hazard's relation to device usage. The values of this property can be one or multiple Use Cases. |

##### Creating a Risk Reduction Table

To keep your model clean and simple, create a Risk Table in the package that contains the Safety Analysis Items to be included in the table.

To create a Risk Reduction Table

1. Do one of the following:
  - Right-click the Package in which you want to create a Risk Reduction Table, and select Create Diagram from the menu.
  - Select the Package in which you want to create a Risk Reduction Table, and click the Create Diagram button on the main toolbar.
2. Click Risk Reduction Table under the Safety and Reliability Analysis group.
3. If needed, change the name of the newly created Risk Reduction Table

A new Risk Reduction Table has been created in the selected Package. Now, you should add Safety Analysis Items to the table, as described in the next section.

##### Adding Safety Analysis Items to a Risk Reduction Table

There are two ways to add Safety Analysis Items to a Risk Reduction Table:

- Create new Safety Analysis Items directly in the table.
- Add existing Safety Analysis Items to the table.

To create a new Safety Analysis Item in a Risk Reduction Table

- Do one of the following:
- Click the Add New button on the table toolbar.
- Press Insert (Cmd+I on Mac OS).

A new row containing the newly created Safety Analysis Item is added at the end of the table. In the model browser, the safety Analysis Item is placed in the package containing the related Risk Reduction Table. Now you can define the Safety Analysis Item directly in the table by double-clicking an appropriate cell.

#### INFO: Model structure information

Model structure information

To have a clear model structure, create Safety Analysis Items in dedicated Packages.

To add an existing Safety Analysis Item to a Risk Reduction Table

1. Do one of the following:
  - Click the Add Existing button on the table toolbar.
  - Press Ctrl+Insert (Cmd+E on Mac OS).
2. In the open dialog, select the Safety Analysis Item you want to add to the table. To [CONFLUENCE_PAGE title='Elements multiple selection' space='MD2024xR1'] , click [ATTACHMENT filename='multiple_selection.png'] , and add the desired Safety Analysis Items to the Selected elements area on the right side of the dialog.
3. Click OK .

#### TIP: Productivity tip

Productivity tip

To make your work quicker, you can add existing Safety Analysis Items to a Risk Table by dragging them directly to the table. Simply select one or more Safety Analysis Items in the model browser and drag them to a Risk Table. New rows for the added elements are created automatically.

Selected Safety Analysis Item(s) are now added to the Risk Reduction Table as new row(s). You can change the properties of the added elements directly in the table by double-clicking an appropriate cell.

949381712

**Related pages**

- [CONFLUENCE_PAGE title='Safety analysis' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Describing Safety Analysis Items' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='FMEAs to be analyzed' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="10d70086-5f10-4ca6-bfda-068a3fb2b71a"><ac:parameter ac:name="id">949334895</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a613457e-936e-4bde-8618-0a6e08e41ef9"><ac:parameter ac:name="id">949334898</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d924c7d8-538b-4c10-995c-2dd050b0fe2e"><ac:parameter ac:name="id">949334893</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="55bd068a-df80-4fab-b620-284c4bcecb3c"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="97228d92-7461-4924-b63a-959d8ce9e528"><ac:parameter ac:name="id">949334897</ac:parameter><ac:rich-text-body><p>After the mitigation phase, risks (Safety Analysis Items) can be further described in a Risk Reduction Table. Since Risk Reduction Tables are based on <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Generic table" /><ac:plain-text-link-body><![CDATA[Generic Tables]]></ac:plain-text-link-body></ac:link>, the <span class="external-link"><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Table toolbars" /><ac:plain-text-link-body><![CDATA[toolbar]]></ac:plain-text-link-body></ac:link></span> and the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Table Criteria area" /><ac:plain-text-link-body><![CDATA[Criteria area]]></ac:plain-text-link-body></ac:link> work in the same manner.</p><p>A Risk Reduction Table allows you to analyze the safety aspect of your model both before and after the mitigation. This gives you an opportunity to evaluate the effectiveness of recommended risk reduction actions. Each row in a table represents a Safety Analysis Item, and table columns represent the properties of Safety Analysis Items. In a Risk Table, you can:</p><ul><li>Create a new Safety Analysis Item directly in a table, or add an existing one.</li><li>Edit the properties of Safety Analysis Items directly in a table.</li><li>Generate a risk analysis report, or export a table into a CSV or HTML file format.</li></ul><p><br />A Risk Table has the following columns:</p><table class="relative-table" style="width: 100.0%;"><colgroup><col style="width: 16.4678%;" /><col style="width: 83.5322%;" /></colgroup><tbody><tr><th>Table column name</th><th>Description</th></tr><tr><td><strong>Id</strong></td><td>Safety Analysis Item ID.</td></tr><tr><td><strong>FMEA Reference</strong></td><td>The reference to an FMEA Item.</td></tr><tr><td><strong>Initiating Cause</strong></td><td>A short description of a Safety Analysis Item.</td></tr><tr><td><strong>Hazard</strong></td><td>A potential source of Harm.</td></tr><tr><td><strong>Sequence of Events</strong></td><td><div class="content-wrapper"><p>Sequence of Events leading to a Hazardous Situation.</p><p>Every Sequence of Events can have a default <strong>P1</strong> value assigned as its property. To assign a value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Sequence of Events, and set the desired <strong>P1</strong> value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e72d5932-5f4d-4d6e-b957-14449ffaa36a"><ac:parameter ac:name="title">Adding P1 values</ac:parameter><ac:rich-text-body><p>If you add a Sequence of Events with a specified <strong>P1</strong> value to a certain row of a Risk Reduction Table for the first time, this value is automatically entered into an appropriate cell of the P1 column. The value is entered even if the cell already has a value specified. You can manually change the P1 value that was automatically added to a Risk Reduction Table. This action does not change the default <strong>P1</strong> value assigned to this specific Sequence of Events element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>Hazardous Situation</strong></td><td><div class="content-wrapper"><p>A situation in which a subject or an object of the environment is exposed to one or more Hazards.</p><p>Every Hazardous Situation can have a default <strong>P2</strong> value assigned as its property. To assign a value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Hazardous Situation, and set the desired <strong>P2</strong> value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f1e3a6b2-07e9-45ee-bb0a-8427888f89b8"><ac:parameter ac:name="title">Adding P2 values</ac:parameter><ac:rich-text-body><p>If you add a Hazardous Situation with a specified <strong>P2</strong> value to a certain row of a Risk Reduction Table for the first time, this value is automatically entered into an appropriate cell of the P2 column. The value is entered even if the cell already has a value specified. You can manually change the P2 value that was automatically added to a Risk Reduction Table. This action does not change the default <strong>P2</strong> value assigned to this specific Hazardous Situation element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>Harm</strong></td><td><div class="content-wrapper"><p>Damage to the health of people, damage to the property or environment, or both.</p><p>Every Harm can have a default severity (S) value assigned as its property. To assign a value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Harm, and set the desired <strong>Severity</strong> value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a3dbdc2f-8302-4ae7-b90b-df943d9d2a65"><ac:parameter ac:name="title">Adding severity values</ac:parameter><ac:rich-text-body><p>If you add a Harm with a specified severity value to a certain row of a Risk Reduction Table for the first time, this value is automatically entered into an appropriate cell of the S column. The value is entered even if the cell already has a value specified. You can manually change the severity value that was automatically added to a Risk Reduction Table. This action does not change the default severity value assigned to this specific Harm element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>S</strong></td><td><p>Severity is the quantitative evaluation of the Harm that is caused if exposed to a Hazard. The valid values of this property are 1 to 4 (lowest to highest severity).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td><strong>P1</strong></td><td><p>Probability of a foreseeable Sequence of Events leading to a Hazardous Situation. The valid values of this property are 1 to 5 (lowest to highest probability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td><strong>P2</strong></td><td><p>Probability of a Harm occurring when exposed to a Hazard. The valid values of this property are 1 to 5 (lowest to highest probability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td><strong>P</strong></td><td>The function of P1 and P2.</td></tr><tr><td><strong>D</strong></td><td><p>Detectability measures the likelihood of discovering and correcting a Hazard prior to Harm occurrence. The valid values of this property are 1 to 5 (highest to lowest detectability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td><strong>C</strong></td><td><p>Correctability is the rate of relative ease of mitigating a certain risk. The valid values of this property are 1 to 5 (lowest to highest correctability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td><strong>PU</strong></td><td><p>Product Utility shows the clinical benefits of a product, taking into account the risks it holds. The valid values of this property are 1 to 5 (highest to lowest clinical benefits that outweigh the risks).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td><strong>Risk</strong></td><td>A customizable function of P and S.</td></tr><tr><td><strong>Risk Control Measures Description</strong></td><td>A brief, qualitative description of the proposed method of risk control.</td></tr><tr><td><strong>Risk Control Measures</strong></td><td>A reference to the safety requirement that mitigates the risk.</td></tr><tr><td><strong>Mitigators</strong></td><td>A reference to any element that satisfies the related safety requirement.</td></tr><tr><td><strong>Reduced S</strong></td><td><p>Reduced severity is the quantitative evaluation of the Harm that is caused if exposed to a Hazard after the mitigation (or simply severity value after the mitigation). The valid values of this property are 1 to 4 (lowest to highest severity).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced P1</strong></td><td colspan="1"><p>Probability of a foreseeable Sequence of Events leading to a Hazardous Situation after the mitigation. The valid values of this property are 1 to 5 (lowest to highest probability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced P2</strong></td><td colspan="1"><p>Probability of a Harm occurring when exposed to a Hazard after the mitigation. The valid values of this property are 1 to 5 (lowest to highest probability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced P</strong></td><td colspan="1">The function of Reduced P1 and Reduced P2.</td></tr><tr><td colspan="1"><strong>Reduced D</strong></td><td colspan="1"><p>Reduced detectability measures the likelihood of discovering and correcting a Hazard prior to Harm occurrence, but after the mitigation (or simply - detectability value after the mitigation). The valid values of this property are 1 to 5 (highest to lowest detectability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced C</strong></td><td colspan="1"><p>Correctability is the rate of relative ease of mitigating a certain risk if it is faced after the mitigation. The valid values of this property are 1 to 5 (lowest to highest correctability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced PU</strong></td><td colspan="1"><p>Reduced Product Utility shows the clinical benefits of a product taking into account the risks it holds after the mitigation (or simply - product utility value after the mitigation). The valid values of this property are 1 to 5 (highest to lowest clinical benefits that outweigh the risks).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Reduced Risk</strong></td><td colspan="1">A customizable function of Reduced P and Reduced S.</td></tr><tr><td colspan="1"><strong>Use Related</strong></td><td colspan="1">The property indicating a Hazard's relation to device usage. <span style="color: rgb(62,63,64);">The values of this property can be one or multiple Use Cases.</span></td></tr></tbody></table><h3><br />Creating a Risk Reduction Table</h3><p>To keep your model clean and simple, create a Risk Table in the package that contains the Safety Analysis Items to be included in the table.</p><p> </p><p>To create a Risk Reduction Table</p><hr /><ol><li>Do one of the following:<br /><ul><li>Right-click the Package in which you want to create a Risk Reduction Table, and select <strong>Create Diagram</strong> from the menu.</li><li>Select the Package in which you want to create a Risk Reduction Table, and click the <strong>Create Diagram</strong> button on the main toolbar.</li></ul></li><li>Click <strong>Risk Reduction Table</strong> under the <strong>Safety and Reliability Analysis</strong> group.</li><li>If needed, change the name of the newly created Risk Reduction Table</li></ol><p>A new Risk Reduction Table has been created in the selected Package. Now, you should add Safety Analysis Items to the table, as described in the next section.</p><h3><br />Adding Safety Analysis Items to a Risk Reduction Table</h3><p>There are two ways to add Safety Analysis Items to a Risk Reduction Table:</p><ul><li>Create new Safety Analysis Items directly in the table.</li><li>Add existing Safety Analysis Items to the table.</li></ul><p> </p><p>To create a new Safety Analysis Item in a Risk Reduction Table</p><hr /><ul><li>Do one of the following:</li><li style="margin-left: 30.0px;">Click the <strong>Add New</strong> button on the table toolbar.</li><li style="margin-left: 30.0px;">Press Insert (Cmd+I on Mac OS).</li></ul><p><br />A new row containing the newly created Safety Analysis Item is added at the end of the table. In the model browser, the safety Analysis Item is placed in the package containing the related Risk Reduction Table. Now you can define the Safety Analysis Item directly in the table by double-clicking an appropriate cell.<br /> </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="523ede30-9d84-4d23-94c9-40cf05450f9e"><ac:parameter ac:name="title">Model structure information</ac:parameter><ac:rich-text-body><p>To have a clear model structure, create Safety Analysis Items in dedicated Packages.</p></ac:rich-text-body></ac:structured-macro><p> </p><p>To add an existing Safety Analysis Item to a Risk Reduction Table</p><hr /><ol><li>Do one of the following:<br /><ul><li>Click the <strong>Add Existing</strong> button on the table toolbar.</li><li>Press Ctrl+Insert (Cmd+E on Mac OS).</li></ul></li><li>In the open dialog, select the Safety Analysis Item you want to add to the table. To <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Elements multiple selection" /><ac:plain-text-link-body><![CDATA[select multiple elements]]></ac:plain-text-link-body></ac:link>, click <ac:image><ri:attachment ri:filename="multiple_selection.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing reduced risks" /></ri:attachment></ac:image>, and add the desired Safety Analysis Items to the <strong>Selected elements</strong> area on the right side of the dialog.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="ff4ca58c-4645-4c29-9302-1e95d5120f91"><ac:parameter ac:name="title">Productivity tip</ac:parameter><ac:rich-text-body><p>To make your work quicker, you can add existing Safety Analysis Items to a Risk Table by dragging them directly to the table. Simply select one or more Safety Analysis Items in the model browser and drag them to a Risk Table. New rows for the added elements are created automatically.</p></ac:rich-text-body></ac:structured-macro><p>Selected Safety Analysis Item(s) are now added to the Risk Reduction Table as new row(s). You can change the properties of the added elements directly in the table by double-clicking an appropriate cell.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="efc00c8c-fb67-4543-a7a1-0c2d9299d1f7"><ac:parameter ac:name="id">949381712</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety analysis" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing Safety Analysis Items" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="FMEAs to be analyzed" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466474 space=CSRA2024xR1 version=2 -->
## PAGE 00025: Describing Safety Analysis Items

- page_id: `170466474`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466474/Describing+Safety+Analysis+Items
- version_number: 2
- version_date: `2024-05-08T14:01:15.481+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Safety analysis
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Productivity tip

949218266

#### CONTENT-COLUMN: Productivity tip

949218268

949218264

**On this page**

4

#### CONTENT-BLOCK: Productivity tip

949218267

Safety Analysis Items should be described in a predefined Risk Table. Since Risk Tables are based on [CONFLUENCE_PAGE title='Generic table' space='MD2024xR1'], the [CONFLUENCE_PAGE title='Table toolbars' space='MD2024xR1'] and the [CONFLUENCE_PAGE title='Table Criteria area' space='MD2024xR1'] work in the same manner.

A Risk Table allows you to analyze the safety aspect of your model, and provides a convenient way to fill-in Safety Analysis Item information using a spreadsheet-like tabular format. Each row in a table represents a Safety Analysis Item. Table columns represent the properties Safety Analysis Items. In a Risk Table, you can:

- Create a new Safety Analysis Item directly in a table, or add an existing one.
- Edit the properties of Safety Analysis Items directly in a table.
- Generate a risk analysis report, and export a table into a CSV or HTML file format.

A Risk Table has the following columns:

| Table column name | Description |
| --- | --- |
| Id | Safety Analysis Item ID. |
| MHT Reference | The reference to a Master Hazard Table. |
| FMEA Reference | The reference to an FMEA Item. |
| Initiating Cause | A short description of a Safety Analysis Item reflecting the cause of a risk. |
| Hazard | A potential source of Harm. |
| Sequence of Events | Sequence of Events leading to a Hazardous Situation.Every Sequence of Events can have a default P1 value assigned as its property. To assign a value, open the of a Sequence of Events, and set the desired P1 value.Adding P1 valuesIf you add a Sequence of Events with a specified P1 value to a certain row of a Risk Table for the first time, this value is automatically entered into an appropriate cell of the P1 column. The value is entered even if the cell already has a value specified. You can manually change the P1 value that was automatically added to a Risk Table. This action does not change the default P1 value assigned to this specific Sequence of Events element. |
| Hazardous Situation | A situation in which a subject or object of the environment is exposed to one or more Hazards.Every Hazardous Situation can have a default P2 value assigned as its property. To assign a value, open the of a Hazardous Situation, and set the desired P2 value.Adding P2 valuesIf you add a Hazardous Situation with a specified P2 value to a certain row of a Risk Table for the first time, this value is automatically entered into an appropriate cell of the P2 column. The value is entered even if the cell already has a value specified. You can manually change the P2 value that was automatically added to a Risk Table. This action does not change the default P2 value assigned to this specific Hazardous Situation element. |
| Harm | Damage to the health of people, damage to property or environment, or both.Every Harm can have a default severity (S) value assigned as its property. To assign a value, open the of a Harm, and set the desired Severity value.Adding severity valuesIf you add a Harm with a specified severity value to a certain row of a Risk Table for the first time, this value is automatically entered into an appropriate cell of the S column. The value is entered even if the cell already has a value specified. You can manually change the severity value that was automatically added to a Risk Table. This action does not change the default severity value assigned to this specific Harm element. |
| S | Severity is the quantitative evaluation of the Harm that is caused if exposed to a Hazard. The valid values of this property are 1 to 4 (lowest to highest severity).Click an appropriate column cell to select its value from a drop-down list. |
| P1 | Probability of a foreseeable Sequence of Events leading to a Hazardous Situation. The valid values of this property are 1 to 5 (lowest to highest probability).Click an appropriate column cell to select its value from a drop-down list. |
| P2 | Probability of a Harm occurring when exposed to a Hazard. The valid values of this property are 1 to 5 (lowest to highest probability).Click an appropriate column cell to select its value from a drop-down list. |
| P | The function of P1 and P2. |
| D | Detectability measures the likelihood of discovering and correcting a Hazard prior to Harm occurrence. The valid values of this property are 1 to 5 (highest to lowest detectability).Click an appropriate column cell to select its value from a drop-down list. |
| C | Correctability is the rate of relative ease of mitigating a certain risk. The valid values of this property are 1 to 5 (lowest to highest correctability).Click an appropriate column cell to select its value from a drop-down list. |
| PU | Product Utility shows the clinical benefits of a product taking into account the risks it holds. The valid values of this property are 1 to 5 (highest to lowest clinical benefits that outweigh the risks).Click an appropriate column cell to select its value from a drop-down list. |
| Risk | The function of P and S. |
| Use Related | The property indicating a Hazard's relation to device usage. The values of this property can be one or multiple Use Cases. |

##### Creating a Risk Table

To keep your model clean and simple, create a Risk Table in the package that contains the Safety Analysis Items to be included in the table.

To create a Risk Table

1. Do one of the following:
  - Right-click the Package in which you want to create a Risk Table, and select Create Diagram from the menu.
  - Select the Package in which you want to create a Risk Table, and click the Create Diagram button on the main toolbar.
2. Click Risk Table under the Safety and Reliability Analysis group.
3. If needed, change the name of the newly created Risk Table.

A new Risk Table is created in the selected Package. Now, you should add Safety Analysis Items to the table, as described in the next section.

##### Adding Safety Analysis Items to a Risk Table

There are two ways to add Safety Analysis Items to a Risk Table:

- Create new Safety Analysis Items directly in the table.
- Add existing Safety Analysis Items to the table.

To create a new Safety Analysis Item in a Risk Table

- Do one of the following:
- Click the Add New button on the table toolbar.
- Press Insert (Cmd+I on Mac OS).

A new row containing the newly created Safety Analysis Item is added at the end of the table. In the model browser, the Safety Analysis Item is placed in the Package containing the related Risk Table. Now you can define the Safety Analysis Item directly in the table by double-clicking an appropriate cell.

#### INFO: Model structure information

Model structure information

To have a clear model structure, create Safety Analysis Items in dedicated Packages.

To add an existing Safety Analysis Item to a Risk Table

1. Do one of the following:
  - Click the Add Existing button on the table toolbar.
  - Press Ctrl+Insert (Cmd+E on Mac OS).
2. In the open dialog, select the Safety Analysis Item you want to add to the table. To [CONFLUENCE_PAGE title='Elements multiple selection' space='MD2024xR1'] , click [ATTACHMENT filename='multiple_selection.png'] , and add the desired Safety Analysis Items to the Selected elements area on the right side of the dialog.
3. Click OK .

#### TIP: Productivity tip

Productivity tip

To make your work quicker, you can add existing Safety Analysis Items to a Risk Table by dragging them directly to the table. Simply select one or more Safety Analysis Items in the model browser, and drag them to a Risk Table. New rows for the added elements are created automatically.

Selected Safety Analysis Item(s) are now added to the Risk Table as new row(s). You can change the properties of the added elements directly in the table by double-clicking an appropriate cell.

949254094

**Related pages**

- [CONFLUENCE_PAGE title='Safety analysis' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Describing reduced risks' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='FMEAs to be analyzed' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="92c50e5f-6373-4d1b-888b-1c554962591f"><ac:parameter ac:name="id">949218266</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cca6106b-8055-42f9-9e7b-16f2b4b30fe3"><ac:parameter ac:name="id">949218268</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9ecb145a-c9de-4aa2-b5fc-662b84ecba96"><ac:parameter ac:name="id">949218264</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4b5f4111-eb39-4d48-934d-2bbd1a52cbbf"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ac90e076-7623-42f9-a2ac-088c90a8437b"><ac:parameter ac:name="id">949218267</ac:parameter><ac:rich-text-body><p>Safety Analysis Items should be described in a predefined Risk Table. Since Risk Tables are based on <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Generic table" /><ac:plain-text-link-body><![CDATA[Generic Tables]]></ac:plain-text-link-body></ac:link>, the <span class="external-link"><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Table toolbars" /><ac:plain-text-link-body><![CDATA[toolbar]]></ac:plain-text-link-body></ac:link></span> and the <span class="external-link"><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Table Criteria area" /><ac:plain-text-link-body><![CDATA[Criteria area]]></ac:plain-text-link-body></ac:link></span> work in the same manner.</p><p>A Risk Table allows you to analyze the safety aspect of your model, and provides a convenient way to fill-in Safety Analysis Item information using a spreadsheet-like tabular format. Each row in a table represents a Safety Analysis Item. Table columns represent the properties Safety Analysis Items. In a Risk Table, you can:</p><ul><li>Create a new Safety Analysis Item directly in a table, or add an existing one.</li><li>Edit the properties of Safety Analysis Items directly in a table.</li><li>Generate a risk analysis report, and export a table into a CSV or HTML file format.</li></ul><p><br />A Risk Table has the following columns:</p><table class="relative-table" style="width: 100.0%;"><colgroup><col style="width: 20.0477%;" /><col style="width: 79.9523%;" /></colgroup><tbody><tr><th>Table column name</th><th>Description</th></tr><tr><td><strong>Id</strong></td><td>Safety Analysis Item ID.</td></tr><tr><td><strong>MHT Reference</strong></td><td>The reference to a Master Hazard Table.</td></tr><tr><td><strong>FMEA Reference</strong></td><td>The reference to an FMEA Item.</td></tr><tr><td><strong>Initiating Cause</strong></td><td>A short description of a Safety Analysis Item reflecting the cause of a risk.</td></tr><tr><td><strong>Hazard</strong></td><td>A potential source of Harm.</td></tr><tr><td><strong>Sequence of Events</strong></td><td><div class="content-wrapper"><p>Sequence of Events leading to a Hazardous Situation.</p><p>Every Sequence of Events can have a default <strong>P1</strong> value assigned as its property. To assign a value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Sequence of Events, and set the desired <strong>P1</strong> value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c3bf2544-55c1-4bfb-9184-0c373a643f5d"><ac:parameter ac:name="title">Adding P1 values</ac:parameter><ac:rich-text-body><p>If you add a Sequence of Events with a specified <strong>P1</strong> value to a certain row of a Risk Table for the first time, this value is automatically entered into an appropriate cell of the P1 column. The value is entered even if the cell already has a value specified. You can manually change the P1 value that was automatically added to a Risk Table. This action does not change the default <strong>P1</strong> value assigned to this specific Sequence of Events element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>Hazardous Situation</strong></td><td><div class="content-wrapper"><p>A situation in which a subject or object of the environment is exposed to one or more Hazards.</p><p>Every Hazardous Situation can have a default <strong>P2</strong> value assigned as its property. To assign a value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Hazardous Situation, and set the desired <strong>P2</strong> value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cd01d40c-c303-4b45-824c-13dbd131d295"><ac:parameter ac:name="title">Adding P2 values</ac:parameter><ac:rich-text-body><p>If you add a Hazardous Situation with a specified <strong>P2</strong> value to a certain row of a Risk Table for the first time, this value is automatically entered into an appropriate cell of the P2 column. The value is entered even if the cell already has a value specified. You can manually change the P2 value that was automatically added to a Risk Table. This action does not change the default <strong>P2</strong> value assigned to this specific Hazardous Situation element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>Harm</strong></td><td><div class="content-wrapper"><p>Damage to the health of people, damage to property or environment, or both.</p><p>Every Harm can have a default severity (S) value assigned as its property. To assign a value, open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of a Harm, and set the desired <strong>Severity</strong> value.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="126b92a2-23a2-4a21-8aed-70fade0c325d"><ac:parameter ac:name="title">Adding severity values</ac:parameter><ac:rich-text-body><p>If you add a Harm with a specified severity value to a certain row of a Risk Table for the first time, this value is automatically entered into an appropriate cell of the S column. The value is entered even if the cell already has a value specified. You can manually change the severity value that was automatically added to a Risk Table. This action does not change the default severity value assigned to this specific Harm element.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></div></td></tr><tr><td><strong>S</strong></td><td><p>Severity is the quantitative evaluation of the Harm that is caused if exposed to a Hazard. The valid values of this property are 1 to 4 (lowest to highest severity).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td><strong>P1</strong></td><td><p>Probability of a foreseeable Sequence of Events leading to a Hazardous Situation. The valid values of this property are 1 to 5 (lowest to highest probability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>P2</strong></td><td colspan="1"><p>Probability of a Harm occurring when exposed to a Hazard. The valid values of this property are 1 to 5 (lowest to highest probability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>P</strong></td><td colspan="1">The function of P1 and P2.</td></tr><tr><td colspan="1"><strong>D</strong></td><td colspan="1"><p>Detectability measures the likelihood of discovering and correcting a Hazard prior to Harm occurrence. The valid values of this property are 1 to 5 (highest to lowest detectability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>C</strong></td><td colspan="1"><p>Correctability is the rate of relative ease of mitigating a certain risk. The valid values of this property are 1 to 5 (lowest to highest correctability).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>PU</strong></td><td colspan="1"><p>Product Utility shows the clinical benefits of a product taking into account the risks it holds. The valid values of this property are 1 to 5 (highest to lowest clinical benefits that outweigh the risks).</p><p>Click an appropriate column cell to select its value from a drop-down list.</p></td></tr><tr><td colspan="1"><strong>Risk</strong></td><td colspan="1">The function of P and S.</td></tr><tr><td colspan="1"><strong>Use Related</strong></td><td colspan="1">The property indicating a Hazard's relation to device usage. The values of this property can be one or multiple Use Cases.</td></tr></tbody></table><p> </p><h3>Creating a Risk Table</h3><p>To keep your model clean and simple, create a Risk Table in the package that contains the Safety Analysis Items to be included in the table.</p><p> </p><p>To create a Risk Table</p><hr /><ol><li>Do one of the following:<br /><ul><li>Right-click the Package in which you want to create a Risk Table, and select <strong>Create Diagram</strong> from the menu.</li><li>Select the Package in which you want to create a Risk Table, and click the <strong>Create Diagram</strong> button on the main toolbar.</li></ul></li><li>Click <strong>Risk Table</strong> under the <strong>Safety and Reliability Analysis</strong> group.</li><li>If needed, change the name of the newly created Risk Table.</li></ol><p><br />A new Risk Table is created in the selected Package. Now, you should add Safety Analysis Items to the table, as described in the next section.</p><h3><br />Adding Safety Analysis Items to a Risk Table</h3><p>There are two ways to add Safety Analysis Items to a Risk Table:</p><ul><li>Create new Safety Analysis Items directly in the table.</li><li>Add existing Safety Analysis Items to the table.</li></ul><p><br /></p><p>To create a new Safety Analysis Item in a Risk Table</p><hr /><ul><li>Do one of the following:</li><li style="margin-left: 30.0px;">Click the <strong>Add New</strong> button on the table toolbar.</li><li style="margin-left: 30.0px;">Press Insert (Cmd+I on Mac OS).</li></ul><p><br />A new row containing the newly created Safety Analysis Item is added at the end of the table. In the model browser, the Safety Analysis Item is placed in the Package containing the related Risk Table. Now you can define the Safety Analysis Item directly in the table by double-clicking an appropriate cell.<br /> </p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2aa7adbf-f866-470e-b7bb-9976fb2de295"><ac:parameter ac:name="title">Model structure information</ac:parameter><ac:rich-text-body><p>To have a clear model structure, create Safety Analysis Items in dedicated Packages.</p></ac:rich-text-body></ac:structured-macro><p> </p><p>To add an existing Safety Analysis Item to a Risk Table</p><hr /><ol><li>Do one of the following:<br /><ul><li>Click the <strong>Add Existing</strong> button on the table toolbar.</li><li>Press Ctrl+Insert (Cmd+E on Mac OS).</li></ul></li><li>In the open dialog, select the Safety Analysis Item you want to add to the table. To <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Elements multiple selection" /><ac:plain-text-link-body><![CDATA[select multiple elements]]></ac:plain-text-link-body></ac:link>, click <ac:image><ri:attachment ri:filename="multiple_selection.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing Safety Analysis Items" /></ri:attachment></ac:image>, and add the desired Safety Analysis Items to the <strong>Selected elements</strong> area on the right side of the dialog.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="eb51c9cc-5701-46ae-aaae-490f48fea306"><ac:parameter ac:name="title">Productivity tip</ac:parameter><ac:rich-text-body><p>To make your work quicker, you can add existing Safety Analysis Items to a Risk Table by dragging them directly to the table. Simply select one or more Safety Analysis Items in the model browser, and drag them to a Risk Table. New rows for the added elements are created automatically.</p></ac:rich-text-body></ac:structured-macro><p>Selected Safety Analysis Item(s) are now added to the Risk Table as new row(s). You can change the properties of the added elements directly in the table by double-clicking an appropriate cell.</p><p class="auto-cursor-target"> </p><p> </p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="af19eba0-a347-48f3-8213-803f0292ef5e"><ac:parameter ac:name="id">949254094</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety analysis" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing reduced risks" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="FMEAs to be analyzed" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466830 space=CSRA2024xR1 version=1 -->
## PAGE 00026: Effect

- page_id: `170466830`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466830/Effect
- version_number: 1
- version_date: `2024-04-25T09:38:16.303+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Damage scenario
- labels: []

### NORMALIZED CONTENT

##### Creating an Effect

To create an Effect

1. In the Containment tree, right-click**Damage Scenario****and Impact Ratings**and select Create Element. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Vehicle Level Effect**or **System Level Effect**. **[IMAGE alt='' src='']**
  - In the search tab, type the keyword effect and then select Vehicle Level Effect or System Level Effect. **[IMAGE alt='' src='']**
3. Name the created Effect in the Containment tree and press Enter. 
 
**[IMAGE alt='' src='']**

##### Adding Effects to the Effects Table

Using the Effects Table you can only add nested Effects.

To add an Effects

1. In the Effects Table, select an Effect and then click Add Nested. A row is added in the Effects Table, which shows the nested Effect. 
 
[IMAGE alt='' src='']
2. In the newly created Effect's row and the **Name**column, double-click the designated cell to name the Effect. 
 
[IMAGE alt='' src='']

##### Adding Relevant Element in the Effects Table

To add Relevant To

1. Double-click the designated cell in the**Relevant Element** column and the required Effect's row and click [IMAGE alt='' src='']. 
 
[IMAGE alt='' src='']
2. From the **Select Elements******dialog, select Relevant Element. 
 
[IMAGE alt='' src=''] The Relevant Element is added to the Effects Table. 
 
[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e94677a0-cdac-4b08-8d36-4987f490a951" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="c0001038-dc02-4862-8b55-0ea3f529a632">Creating an Effect</ac:inline-comment-marker></h3><p>To create an Effect</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click<span> <strong>Damage Scenario </strong></span><strong>and Impact Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Vehicle Level Effect </strong>or <strong>System Level Effect</strong>.<br /></span><strong><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Effect.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image></strong><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword effect and then select<span> </span><strong>Vehicle Level Effect<span> </span></strong>or <strong><span>System Level Effect.</span></strong><strong><br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Effect_Search.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image></strong><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Effect in the Containment tree and press Enter.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="4 EffectCreated.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image></strong></span></li></ol><h3>Adding Effects to the Effects Table</h3><p>Using the Effects Table you can only add nested Effects.</p><p>To add an Effects</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Effects Table, select an Effect and then click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add Nested.<span> </span></strong><span style="color: rgb(62,63,64);">A row is added in the Effects Table, which shows the nested Effect.<br /><br /><ac:image><ri:attachment ri:filename="Add Nested_Effect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">In the newly created Effect's row and the <strong style="text-align: left;">Name<span> </span></strong>column, double-click the designated cell to name the Effect.<br style="text-align: left;" /><br /><ac:image><ri:attachment ri:filename="Nested Effect added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image><br /></span></li></ol><h3>Adding Relevant Element in the Effects Table</h3><p><span style="color: rgb(23,43,77);">To add Relevant To</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">Double-click the designated cell in the<span> </span><strong>Relevant Element </strong></span><span style="color: rgb(62,63,64);">column and the required Effect's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image></span></span>.<br /><br /><ac:image><ri:attachment ri:filename="Relevant To_Three Dot_Effect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image><br /><br /></span></span></li><li><span style="color: rgb(62,63,64);"><span>From the <strong style="text-align: left;">Select Elements</strong><strong style="text-align: left;"> </strong>dialog, select Relevant Element.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog_Effect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image><br /><br style="text-align: left;" /></span></span><span style="color: rgb(62,63,64);"><span>The Relevant Element is added to the Effects Table.<br /><br /><ac:image><ri:attachment ri:filename="Relevant To added_Effect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effect" /></ri:attachment></ac:image><br /></span></span></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466556 space=CSRA2024xR1 version=1 -->
## PAGE 00027: Effects Table

- page_id: `170466556`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466556/Effects+Table
- version_number: 1
- version_date: `2023-06-26T06:42:04.485+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

116136483

116136496

116136482

**On this page**

4

116136484

An Effects Table allows you to define and manage system and vehicle level effects that can result in harm. To identify Effects, you can use two predefined Effect groups: System level effects and Vehicle level effects. If you want to define an additional group, extend the group list by [CONFLUENCE_PAGE title='Extending ISO 26262 elements with new properties' space='CSRA2024xR1'].

[IMAGE alt='' src='']

###### The example of an Effects Table.

##### Creating Effects Table

You can create an Effects Table as described below.

To create an Effects Table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select Effects Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select Create Diagram, and select Effects Table in an open dialog . [ATTACHMENT filename='creating_effects_table.png']
3. When the table is created, type the name of the table and press Enter.

After completing the above steps, an Effects Table with two predefined Effect groups is created. The scope and element type of the table are already specified for you.

##### Creating Effects

There are two ways to create an Effect: you can do it right in an Effects Table or in the Containment tree.

To create an Effect in the Containment tree

1. In the Containment tree, right-click the owner of a new element and select Create Element .
2. In the open window, select the Effect group ( Vehicle Level Effect or System Level Effect ) for which you want to create an Effect. [ATTACHMENT filename='creating_effects.png']
3. When an Effect is created, type the name of the element and press Enter.

When you create an Effect in the model browser, it is automatically added to an Effects Table if it exists.

To create an Effect in an Effects Table

1. In an Effects Table, select the Effects group ( Vehicle Level Effect or System Level Effect ) for which you want to create an Operational Condition or select an existing element in that group.
2. Do one of the following:
  - In the table toolbar, click Add Sibling to create an element of the same level as the one you have selected. [ATTACHMENT filename='Add Sibling.png']
  - In the table toolbar, click **Add Nested**to create an element nested under the selected element. 
 
[IMAGE alt='' src='']
3. Type the name of the new element and press Enter.

##### Defining Effects

After creating an Effect, you need to specify its Severitylevel and the relevant elements associated with the Effect.

To define a Severity level

1. In an Effects Table, double-click the cell of the Severity column and select the desired Severity level from the list. 
 
[IMAGE alt='' src='']
2. Double-click the**Justification Of Severity**cell and write the justification explaining the selected Severity level.

To specify relevant elements

1. In an Effects Table, double-click the cell of the Relevant Element column and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. In the element tree on the left side of the **Select Elements** dialog, double-click the elements you want to specify. The elements should be added to the selected elements area on the right side of the dialog.
3. Click **OK**.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="11aeddbe-42c0-49e6-9d65-e523edf91371"><ac:parameter ac:name="id">116136483</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d22d881a-c383-4d50-b952-dd90a2de4f3d"><ac:parameter ac:name="id">116136496</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4036aa66-ccce-464d-ae6e-feb8baa1afe9"><ac:parameter ac:name="id">116136482</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="5c3919c5-ab40-4fa5-b568-f2175a320094"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dbff5485-f2f9-4928-aaf9-ace8464cfa6a"><ac:parameter ac:name="id">116136484</ac:parameter><ac:rich-text-body><p>An Effects Table allows you to define and manage system and vehicle level effects that can result in harm. To identify Effects, you can use two predefined Effect groups: System level effects and Vehicle level effects. If you want to define an additional group, extend the group <ac:inline-comment-marker ac:ref="3b3226cd-0b96-487a-9a65-96ce2c28d3f4">list</ac:inline-comment-marker> by <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Extending ISO 26262 elements with new properties" /><ac:plain-text-link-body><![CDATA[extending the ISO 26262 library]]></ac:plain-text-link-body></ac:link>.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="effects_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effects Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of an Effects Table.</h6><h3>Creating Effects Table</h3><p>You can create an Effects Table as described below.</p><p><br /></p><p>To create an Effects Table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>Effects Table</strong> in the open dialog.</li><li>In the Containment tree, right-click the owner of the table, select <strong>Create Diagram,</strong> and select <strong>Effects Table</strong> in an open <ac:inline-comment-marker ac:ref="ad5b8a4a-80f6-44f9-a6a2-a8263fda3949">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="creating_effects_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effects Table" /></ri:attachment></ac:image><br /><br /></li></ul></li><li>When the table is created, type the name of the table and press Enter.</li></ol><p><br /><span style="color: rgb(62,63,64);">After completing the above steps, an Effects Table with two predefined Effect groups is created. The scope and element type of the table are already specified for you.</span></p><h3><span style="color: rgb(62,63,64);">Creating Effects</span></h3><p>There are two ways to create an Effect: you can do it right in an Effects Table or in the Containment tree.</p><p><br /></p><p>To create an Effect in the Containment tree</p><hr /><ol><li>In the Containment tree, right-click the owner of a new element and select <strong>Create Element</strong>.</li><li>In the open window, select the Effect group (<strong>Vehicle Level Effect</strong> or <strong>System Level Effect</strong>) for which you want to create an Effect.<br /><br /><ac:image><ri:attachment ri:filename="creating_effects.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effects Table" /></ri:attachment></ac:image><br /><br /></li><li>When an Effect is created, type the name of the element and press Enter.</li></ol><p><br /><span style="color: rgb(62,63,64);">When you create an Effect in the model browser, it is automatically added to an Effects Table if it exists.</span></p><p><span style="color: rgb(62,63,64);"><br /></span></p><p><span style="color: rgb(62,63,64);">To create an Effect in an Effects Table</span></p><hr /><ol><li>In an Effects Table, select the Effects group (<strong>Vehicle Level Effect</strong> or <strong>System Level Effect</strong><span>) for which you want to create an Operational Condition or select an existing element in that group.</span></li><li>Do one of the following:<br /><ul><li>In the table toolbar, click <strong>Add Sibling </strong>to create an element of the same level as the one you have selected.<br /><br /><ac:image><ri:attachment ri:filename="Add Sibling.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effects Table" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">In the table toolbar, click <strong>Add Nested </strong>to create an element nested under the selected element.<br /><br /><ac:image><ri:attachment ri:filename="Add Nested.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effects Table" /></ri:attachment></ac:image></p></li></ul></li><li>Type the name of the new element and press Enter.</li></ol><h3>Defining Effects</h3><p>After creating an Effect, you need to specify its <span style="color: rgb(62,63,64);">Severity </span>level and the relevant elements associated with the Effect.</p><p><br /></p><p>To define a Severity level</p><hr /><ol><li><span style="color: rgb(62,63,64);">In an Effects Table, double-click the cell of the </span><strong>Severity</strong><span style="color: rgb(62,63,64);"> column and select the desired Severity level from the list.<br /><br /><ac:image><ri:attachment ri:filename="defining_severity_level.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effects Table" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);"><span style="color: rgb(62,63,64);">Double-click the </span><strong>Justification Of Severity</strong><span style="color: rgb(62,63,64);"> cell and write the justification explaining the selected Severity level.</span><br /></span></li></ol><p><br /></p><p>To specify relevant elements</p><hr /><ol><li>In an Effects Table, double-click the cell of the <strong>Relevant Element</strong> column and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Effects Table" /></ri:attachment></ac:image>.</li><li><span style="color: rgb(62,63,64);">In the element tree on the left side of the <strong>Select Elements</strong> dialog, double-click the elements you want to specify. The elements should be added to the selected elements area on the right side of the dialog.</span></li><li><span style="color: rgb(62,63,64);">Click <strong>OK</strong>.</span></li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466634 space=CSRA2024xR1 version=2 -->
## PAGE 00028: Extending ISO 26262 elements with new properties

- page_id: `170466634`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466634/Extending+ISO+26262+elements+with+new+properties
- version_number: 2
- version_date: `2024-05-08T14:01:16.719+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Customizations
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Specifying values for a new Part Property

850603437

#### CONTENT-COLUMN: Specifying values for a new Part Property

850603439

850603435

**On this page**

4

#### CONTENT-BLOCK: Specifying values for a new Part Property

850603438

You can extend the default ISO 26262 library by adding new properties to ISO 26262 elements. In this chapter, you will learn how to add Value Properties and Part Properties by analyzing specific use cases.

##### Case study: Adding new Value Properties

You can add new Value Properties to an element by creating a custom element type with these properties. Let's analyze the workflow of adding a custom Exposure property to an Operational Situation. Since you cannot edit the default Operational Situation from the ISO 26262 library, you will have to create a custom Operational Situation with a new Value property, as described below.

To add a custom Exposure property to an Operational Situation

1. In your model, create a Profile Diagram.
2. In the Profile Diagram, create a Class and name it, e.g., Crash Automotive Situation .
3. Apply the «OperationalSituation» stereotype to the Class.
4. In the ISO 26262 Library, find the TypicalAutomotiveSituation element and drag it to the Profile diagram.
5. Create a Generalization relationship from the Class created in step 2 to TypicalAutomotiveSituation .
6. Create a Value Property for the Class and name it, e.g., crashExposure .
7. Set the Type property of the newly created Value Property to Exposure.
8. Set the Multiplicity property of the Value Property to 1.
9. Apply the «InputField» stereotype to the Value Property.
10. In the Specification window of the Value Property, select the Tags property group and set the multiple property to false . Now your Profile Diagram should look as displayed below. [ATTACHMENT filename='adding_new_value_property.png']
11. Save and reload the project.

You have created a new type of Operational Situation (e.g., *Crash Automotive Situation*) with a custom Exposure property (e.g., *crashExposure*). Now you can [CONFLUENCE_PAGE title='Working with columns' space='MD2024xR1'] for this property in an Operational Situations Table as displayed in the following figure.

#### INFO: Justification for Value Properties

Justification for Value Properties

When you create a new Value Property, the column for justification of that property is automatically created as well and you can add to a table.

[IMAGE alt='' src='']

###### The example of an Operational Situations Table with two additional columns for a new Value Property.

##### Case study: Adding new Part Properties

You can add new Part Properties to an element by creating a custom element type with these properties. Let's analyze the workflow of adding a new Part Property with multiple values to an Operational Situation. Since you cannot edit the default Operational Situation from the ISO 26262 library, you will have to create a custom Operational Situation with a new Part Property. In this workflow, the Part Property is based on Operational Condition.

To add a Part property to an Operational Situation

1. In your model, create a Profile Diagram.
2. In the Profile Diagram, create a Class and name it, e.g., Crash Automotive Situation .
3. Apply the «OperationalSituation» stereotype to the Class.
4. In the ISO 26262 Library, find the TypicalAutomotiveSituation element and drag it to the Profile diagram.
5. Create a Generalization relationship from the Class created in step 2 to TypicalAutomotiveSituation .
6. Create a Part Property for the Class, type its name followed by a colon and the name of the Part property type, e.g., CrumpleZone:CrumpleZone . [ATTACHMENT filename='creating_part_property.png']
7. Set the Multiplicity property of the Part Property to 0..*.
8. Apply the «InputField» stereotype to the Part Property.
9. Drag the Part Property from the Class created in step 2 to the diagram pane. The type of the Part property should be automatically displayed in the diagram.
10. In the ISO 26262 Library, find the OperationalCondition element and drag it to the Profile diagram.
11. Create a Generalization relationship from the type of the Part Property to OperationalCondition . Now your Profile Diagram should look as displayed below. [ATTACHMENT filename='adding_new_part_property.png']
12. Save and reload the project.

You have created a new type of Operational Situation (e.g., *Crash Automotive Situation*) with a custom Part Property (e.g., *CrumpleZone*). Now you can add a new column for this property in an Operational Situations Table as displayed in the following figure.

[IMAGE alt='' src='']

###### The example of an Operational Situations Table with an additional column for a new Part Property.

#### NOTE: Specifying values for a new Part Property

Specifying values for a new Part Property

To specify the values of the newly created Part Property, you need to create a custom stereotype and a Customization for that stereotype. You can find an example of such Customization in the [ATTACHMENT filename='Functional Safety Analysis Sample.mdzip'] sample model. To learn more about creating Customizations, see [CONFLUENCE_PAGE title='Creating Customization Data' space='MD2024xR1'].

##### Creating tables for custom element types

If you need a table to display custom elements and their properties, use a [CONFLUENCE_PAGE title='Generic Safety Table' space='CSRA2024xR1'] which allows displaying all relevant elements depending on the selected scope.

856245337

**Sample model**

To download the model used in the examples described on this page, click [ATTACHMENT filename='Functional Safety Analysis Sample.mdzip'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="e210b154-e033-4ca7-8c53-a0770b406475"><ac:parameter ac:name="id">850603437</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="54395a0a-b51c-43e6-9b19-ae735c1e800e"><ac:parameter ac:name="id">850603439</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="28d5f17c-2941-444c-b03e-aa1299a972c2"><ac:parameter ac:name="id">850603435</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="cd7d7612-10fa-460c-b01b-e61fa4f7c3a7"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="90c8d8d5-c3f5-4357-a4e5-20d2c2f47d3f"><ac:parameter ac:name="id">850603438</ac:parameter><ac:rich-text-body><p><ac:inline-comment-marker ac:ref="0410e93b-709e-483f-971b-b6a6fc89e851">You</ac:inline-comment-marker> can extend the default ISO 26262 library by adding new properties to ISO 26262 elements. In this chapter, you will learn how to add Value Properties and Part Properties by analyzing specific use cases.</p><h3><br />Case study: Adding new Value Properties</h3><p>You can add new Value Properties to an element by creating a custom element type with these properties. Let's analyze the workflow of adding a custom Exposure property to an Operational Situation. Since you cannot edit the default Operational Situation from the ISO 26262 library, you will have to create a custom Operational Situation with a new Value property, as described below.</p><p><br /></p><p>To add a custom Exposure property to an Operational Situation</p><hr /><ol><li>In your model, create a Profile Diagram.</li><li>In the Profile Diagram, create a Class and name it, e.g., <em>Crash Automotive Situation</em>.</li><li>Apply the «OperationalSituation» stereotype to the Class.</li><li>In the ISO 26262 Library, find the <em>TypicalAutomotiveSituation</em> element and drag it to the Profile diagram.</li><li>Create a Generalization relationship from the Class created in step 2 to <em>TypicalAutomotiveSituation</em>.</li><li>Create a Value Property for the Class and name it, e.g., <em>crashExposure</em>.</li><li>Set the <strong>Type</strong> property of the newly created Value Property to Exposure.</li><li>Set the <strong>Multiplicity</strong> property of the Value Property to 1.</li><li>Apply the «InputField» stereotype to the Value Property.</li><li>In the Specification window of the Value Property, select the <strong>Tags</strong> property group and set the <strong>multiple</strong> property to <em>false</em>. Now your Profile Diagram should look as displayed below.<br /><br /><ac:image><ri:attachment ri:filename="adding_new_value_property.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Extending ISO 26262 elements with new properties" /></ri:attachment></ac:image><br /><br /></li><li><ac:inline-comment-marker ac:ref="118d87a1-757e-42f2-8c0f-2e4c10f56079">Save and reload the project.</ac:inline-comment-marker></li></ol><p><br />You have created a new type of Operational Situation (e.g., <em>Crash Automotive Situation</em>) with a custom Exposure property (e.g., <em>crashExposure</em>). Now you can <ac:link ac:anchor="Adding and removing columns"><ri:page ri:space-key="MD2024xR1" ri:content-title="Working with columns" /><ac:plain-text-link-body><![CDATA[add new columns]]></ac:plain-text-link-body></ac:link> for this property in an Operational Situations Table as displayed in the <ac:inline-comment-marker ac:ref="34693711-5cc9-4dd0-b9fb-3a57d2be1135">following</ac:inline-comment-marker> <ac:inline-comment-marker ac:ref="00492abb-04a2-4da3-bdb6-78f78a415d95">figure</ac:inline-comment-marker>.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c22ece5e-c3ae-441e-8b56-8f88e4cbd86b"><ac:parameter ac:name="title">Justification for Value Properties</ac:parameter><ac:rich-text-body><p>When you create a new Value Property, the column for justification of that property is automatically created as well and you can add to a table.</p></ac:rich-text-body></ac:structured-macro><p style="text-align: center;"><br /><ac:image><ri:attachment ri:filename="new_columns_for_value_property.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Extending ISO 26262 elements with new properties" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of an Operational Situations Table with two additional columns for a new Value Property.</h6><h3><br />Case study: Adding new Part Properties</h3><p>You can add new Part Properties to an element by creating a custom element type with these properties. Let's analyze the workflow of adding a new Part Property with multiple values to an Operational Situation. Since you cannot edit the default Operational Situation from the ISO 26262 library, you will have to create a custom Operational Situation with a new Part Property. In this workflow, the Part Property is based on Operational Condition.</p><p><br /></p><p>To add a Part property to an Operational Situation</p><hr /><ol><li>In your model, create a Profile Diagram.</li><li>In the Profile Diagram, create a Class and name it, e.g., <em>Crash Automotive Situation</em>.</li><li>Apply the «OperationalSituation» stereotype to the Class.</li><li>In the ISO 26262 Library, find the <em>TypicalAutomotiveSituation</em> element and drag it to the Profile diagram.</li><li>Create a Generalization relationship from the Class created in step 2 to <em>TypicalAutomotiveSituation</em>.</li><li>Create a Part Property for the Class, type its name followed by a colon and the name of the Part property type, e.g., <em>CrumpleZone:CrumpleZone</em>.<br /><br /><ac:image><ri:attachment ri:filename="creating_part_property.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Extending ISO 26262 elements with new properties" /></ri:attachment></ac:image><br /><br /></li><li>Set the <strong>Multiplicity</strong> property of the Part Property to 0..*.</li><li>Apply the «InputField» stereotype to the Part Property.</li><li>Drag the Part Property from the Class created in step 2 to the diagram pane. The type of the Part property should be automatically displayed in the diagram.</li><li>In the ISO 26262 Library, find the <em>OperationalCondition</em> element and drag it to the Profile diagram.</li><li>Create a Generalization relationship from the type of the Part Property to <em>OperationalCondition</em>. Now your Profile Diagram should look as displayed below.<br /><br /><ac:image><ri:attachment ri:filename="adding_new_part_property.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Extending ISO 26262 elements with new properties" /></ri:attachment></ac:image><br /><br /></li><li><ac:inline-comment-marker ac:ref="f3921c49-d189-4934-ab07-74a95cd04a49">Save and reload the project.</ac:inline-comment-marker></li></ol><p><br />You have created a new type of Operational Situation (e.g., <em>Crash Automotive Situation</em>) with a custom Part Property (e.g., <em>CrumpleZone</em>). Now you can add a new column for this property in an Operational Situations Table as displayed in the <ac:inline-comment-marker ac:ref="c5d43fac-23cb-49c5-a287-2fb3de34bd66">following</ac:inline-comment-marker> <ac:inline-comment-marker ac:ref="efd94a7f-d7e5-4900-a5be-772fe772b5c1">figure</ac:inline-comment-marker>.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="new_column_for_part_property.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Extending ISO 26262 elements with new properties" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The example of an Operational Situations Table with an additional column for a new Part Property.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f116ca36-03e9-4d17-b26e-bb93ea6e1bbc"><ac:parameter ac:name="title">Specifying values for a new Part Property</ac:parameter><ac:rich-text-body><p>To specify the values of the newly created Part Property, you need to create a custom stereotype and a Customization for that stereotype. You can find an example of such Customization in the <ac:link><ri:attachment ri:filename="Functional Safety Analysis Sample.mdzip"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Sample models" /></ri:attachment></ac:link> sample model. To learn more about creating Customizations, see <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Creating Customization Data" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><h3><br />Creating tables for custom element types</h3><p>If you need a table to display custom elements and their properties, use <span style="color: rgb(62,63,64);">a <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ac:link> which allows displaying all relevant elements depending on the selected scope.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cd8be4fb-d158-47f5-96f2-86ca47f6929a"><ac:parameter ac:name="id">856245337</ac:parameter><ac:rich-text-body><p><strong>Sample model</strong></p><p>To download the model used in the examples described on this page, click <ac:link><ri:attachment ri:filename="Functional Safety Analysis Sample.mdzip"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Sample models" /></ri:attachment></ac:link>.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466806 space=CSRA2024xR1 version=1 -->
## PAGE 00029: Failure Mode

- page_id: `170466806`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466806/Failure+Mode
- version_number: 1
- version_date: `2024-04-25T09:34:00.975+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Damage scenario
- labels: []

### NORMALIZED CONTENT

##### Creating a Failure Mode

To create a Failure Mode

1. In the Containment tree, right-click**Damage Scenario****and Impact Ratings**and select Create Element. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Failure Mode**. [IMAGE alt='' src='']
  - In the search tab, type the keyword failure and then select Failure Mode. 
 
[IMAGE alt='' src='']
3. Name the created Failure Mode in the Containment tree and press Enter. 
 
[IMAGE alt='' src='']

##### Adding Failure Mode to the Failure Modes Table

To add a new Failure Mode to the Failure Modes Table

1. In the Failure Modes Table, click Add New. A row is added in the Failure Modes Table, which shows the new Failure Mode. [IMAGE alt='' src='']
2. Select between the FailureMode and MalfucntioningBehavior . [ATTACHMENT filename='Select the failure mode or Malfunction Behavior.png']
3. In the newly created Failure Mode's row and the**Name**column, double-click the designated cell to name the Failure Mode. 
 
[IMAGE alt='' src='']

To add an existing Failure Mode to the Failure Modes Table

1. In the Failure Modes Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the**Select Failure Mode**dialog, select the required Failure Mode. A row is added to the Failure Modes Table, which shows the existing Failure Mode. 
 
[IMAGE alt='' src='']
3. In the existing Failure Mode's row and the**Name**column, double-click the designated cell to rename the Failure Mode. 
 
[IMAGE alt='' src='']

##### Adding Relevant To in the Failure Modes Table

To add Relevant To

1. Double-click the designated cell in the **Relevant To** column and the required Failure Mode's row and click [IMAGE alt='' src='']. [ATTACHMENT filename='Relevant To_Three Dot.png']
2. Fromthe**Select Elements******dialog, select Relevant To. 
 
[IMAGE alt='' src=''] The Relevant To is added to the Failure Modes Table. 
 
[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d58c152e-6a7a-4abe-8996-75c9e3ef9dd0" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Failure Mode</h3><p>To create a Failure Mode</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click<span> <strong>Damage Scenario </strong></span><strong>and Impact Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Failure Mode</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Failure Mode.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword failure and then select<span> </span><strong>Failure Mode.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_Search.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Failure Mode in the Containment tree and press Enter.<br /><br /><ac:image><ri:attachment ri:filename="4 FailureModeCreated.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /></span></li></ol><h3>Adding Failure Mode to the Failure Modes Table</h3><p>To add a new Failure Mode to the Failure Modes Table</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Failure Modes Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add New.<span> </span></strong><span style="color: rgb(62,63,64);">A row is added in the Failure Modes Table, which shows the new Failure Mode.</span><br /><strong style="text-align: left;"><br /><ac:image><ri:attachment ri:filename="Add New_Failure Mode.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></strong></li><li>Select between the <strong>FailureMode</strong> and <strong>MalfucntioningBehavior</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select the failure mode or Malfunction Behavior.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">In the newly created Failure Mode's row and the<span> </span><strong>Name<span> </span></strong>column, double-click the designated cell to name the Failure Mode.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color: rgb(62,63,64);">To add an existing Failure Mode to the Failure Modes Table</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Failure Modes Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="Add Existing_Failure Mode.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">From the<span> </span><strong>Select Failure Mode </strong>dialog, select the required Failure Mode. A row is added to the Failure Modes Table, which shows the existing Failure Mode.<br /><br /><ac:image><ri:attachment ri:filename="Select Failure Mode dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">In the existing Failure Mode's row and the<span> </span><strong>Name<span> </span></strong>column, double-click the designated cell to rename the Failure Mode.<br /><br /><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="Failure Mode added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image></span><br /></span></li></ol><h3>Adding Relevant To in the Failure Modes Table</h3><p>To add Relevant To</p><hr /><ol><li><span style="color: rgb(62,63,64);">Double-click the designated cell in the <strong>Relevant To</strong> </span><span style="color: rgb(62,63,64);">column and the required Failure Mode's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image></span></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Relevant To_Three Dot.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">From<span> </span>the<span> </span><strong>Select Elements</strong><strong><span> </span></strong>dialog, select Relevant To.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /></span><span style="color: rgb(62,63,64);"><br />The Relevant To is added to the Failure Modes Table.<br /><br /><ac:image><ri:attachment ri:filename="Relevant To added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Failure Mode" /></ri:attachment></ac:image><br /></span></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466501 space=CSRA2024xR1 version=1 -->
## PAGE 00030: Fault Tree Analysis

- page_id: `170466501`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466501/Fault+Tree+Analysis
- version_number: 1
- version_date: `2023-07-31T13:50:51.903+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

The Fault Tree Analysis method is mainly used in safety and reliability engineering to understand how systems can fail or to determine the cause of system failure. This method also determines risk rates and identifies the best ways to reduce risk.

The Fault Tree Analysis plugin lets you create a Fault Tree Analysis diagram with the aid of different types of events and gates. An event is a basic item representing an event or a situation which could possibly lead to failure.A gate performs logical operations to figure out the failure reason. Generally, a gate has multiple inputs and a single output. The Fault Tree Analysis diagram is based on the UML Composite Structure Diagram and follows the Risk Analysis and Assessment Modeling Language (RAAML) methods.

The Fault Tree Analysis plugin lets you import a complete Fault Tree Analysis diagram as an event in your diagram, with the help of the Transfer In event. Fault Tree Analysis is a quantitative method; however, the plugin also lets you specify the probabilities of basic events. The probabilities of intermediate and top events are automatically calculated once you run the simulation with the help of the Cameo Simulation Toolkit. The fault tree can be simulated directly as-is. Also, the tree can be instantiated and multiple simulations can be run. You can interconnect the Fault Tree Analysis diagram and the main system model in the same project, with the help of Dependency matrices and Relevant To relationships. Additionally, you can create Libraries of typical failure types and reuse them across multiple projects.

###### [IMAGE alt='' src='']Fault Tree Analysis diagram.

#### NOTE: Prerequisites

Prerequisites

To install and use the Fault Tree Analysis plugin, ensure that the following plugins are installed in your modeling tool:

- Cameo Safety and Reliability Analyzer
- ISO 26262 plugin
- Cameo Simulation Toolkit

You only need the Cameo Simulation Toolkit plugin to calculate the probabilities of the Intermediate and Top Events.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Fault Tree Analysis method is mainly used in safety and reliability engineering to understand how systems can fail or to determine the cause of system failure. This method also determines risk rates and identifies the best ways to reduce risk.</p><p>The Fault Tree Analysis plugin lets you create a Fault Tree Analysis diagram with the aid of different types of events and gates.  <span style="color: rgb(34,34,34);">An event is a basic item representing an event or a situation which could possibly lead to failure. </span>A gate performs logical operations to figure out the failure reason. Generally, a gate has multiple inputs and a single output. The Fault Tree Analysis diagram is based on the UML Composite Structure Diagram and follows the Risk Analysis and Assessment Modeling Language (RAAML) methods.</p><p>The Fault Tree Analysis plugin lets you import a complete Fault Tree Analysis diagram as an event in your diagram, with the help of the Transfer In event. Fault Tree Analysis is a quantitative method; however, the plugin also lets you specify the probabilities of basic events. The probabilities of intermediate and top events are automatically calculated once you run the simulation with the help of the Cameo Simulation Toolkit. The fault tree can be simulated directly as-is. Also, the tree can be instantiated and multiple simulations can be run. You can interconnect the Fault Tree Analysis diagram and the main system model in the same project, with the help of Dependency matrices and Relevant To relationships. Additionally, you can create Libraries of typical failure types and reuse them across multiple projects.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="FTA_Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis" /></ri:attachment></ac:image>Fault Tree Analysis diagram.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5960d6a0-bf4a-46d1-bfa7-59dd6a3c8121"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">To install and use the Fault Tree Analysis plugin, ensure that the following plugins are installed in your modeling tool:</span></p><ul><li>Cameo Safety and Reliability Analyzer</li><li>ISO 26262 plugin</li><li>Cameo Simulation Toolkit</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ad317022-dd77-4a81-b13a-dce1b5950533"><ac:rich-text-body><p>You only need the Cameo Simulation Toolkit plugin to calculate the probabilities of the Intermediate and Top Events.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170466503 space=CSRA2024xR1 version=2 -->
## PAGE 00031: Fault Tree Analysis Diagram

- page_id: `170466503`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466503/Fault+Tree+Analysis+Diagram
- version_number: 2
- version_date: `2024-05-08T14:01:16.210+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Fault Tree Analysis
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Reference

421619005

#### CONTENT-COLUMN: Reference

421619016

421619004

3

#### CONTENT-BLOCK: Reference

421619015

##### Creating a Fault Tree Analysis Diagram

To create aFault Tree Analysis Diagram

1. In the Containment Tree, find the required package and select Create Diagram . [ATTACHMENT filename='Containment Tree.png']
2. Do one of the following:
  - In the dialog, expand**Safety and Reliability Analysis**and select**Fault Tree Analysis Diagram**. 
 
[IMAGE alt='' src=''] 
****
  - In the search tab, type the keyword "fault" and then select **Fault Tree Analysis Diagram****. 
 
[IMAGE alt='' src='']**

##### Adding a Fault Tree Event in the Fault Tree Analysis Diagram

To add a Fault Tree Event in the Fault Tree Analysis Diagram

- From the Fault Tree Event pane, drag and drop any event in the diagram pane of the modeling tool. [ATTACHMENT filename='Basic_Event.png']

You can import a complete Fault Tree Analysis Diagram with the help of the **Transfer In**event.

##### Adding a Fault Tree Gate in the Fault Tree Analysis Diagram

To add a Fault Tree Gate in the Fault Tree Analysis Diagram

- From the Fault Tree Gate pane, drag and drop any gate in the diagram pane of the modeling tool. [IMAGE alt='' src='']

##### Adding probability to theFault Tree Event

To add probability to the Fault Tree Event

1. From the Fault Tree Properties pane, drag and drop Define Basic Event Probability in any Fault Tree Event. [ATTACHMENT filename='Probability.png']
2. Double-click the probability to open the Specification of Value Property probability window and enter the probability value in the Default Value tab. 
 
[IMAGE alt='' src=''] The probability value will be displayed in the Fault Tree Analysis Diagram. 
 
[IMAGE alt='' src=''] The probability value of the Basic events will be used to calculate the probabilities of the Intermediate and Top events.

##### Calculating the probability of the Intermediate and Top Event

To calculate the probability of the Intermediate and Top Event

- Click the **Run** button in the diagram toolbar to run the simulation. The probabilities for the Intermediate and Top Events will be calculated automatically. 
 
[IMAGE alt='' src=''] 
[IMAGE alt='' src='']

##### Interconnecting the Fault Tree Analysis diagram with the System Model

To Interconnect the Fault Tree Analysis diagram with the System Model

- Use the dependency matrices to establish a connection between the Fault Tree Analysis diagram and the System Model. All created events should be connected with the system model using the Relevant To relationship. [ATTACHMENT filename='Dependancy Matrices.png']

#### INFO: Reference

Reference

- To learn more about simulation, refer to [CONFLUENCE_PAGE title='Cameo Simulation Toolkit Documentation' space='CST2024xR1'] .
- To learn more about dependency matrices, refer to [CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024xR1'] .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b8004f95-8716-4f32-978a-774ac8b689d0"><ac:parameter ac:name="id">421619005</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="7cbf0991-bd5e-4730-9171-6995c9f9943d"><ac:parameter ac:name="id">421619016</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="96bca38f-bf05-4c9f-b681-ea37f3bf9a89"><ac:parameter ac:name="id">421619004</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6b4aa9a9-7df2-4a78-ad36-c569a2d42d3d"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="aa7af449-0ff1-495b-a1bf-3e758ef517d2"><ac:parameter ac:name="id">421619015</ac:parameter><ac:rich-text-body><h3>Creating a Fault Tree Analysis Diagram</h3><p><span style="color: rgb(62,63,64);">To create a </span>Fault Tree Analysis Diagram</p><hr /><ol><li>In the Containment Tree, find the required package and select <strong>Create Diagram</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Containment Tree.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul><li><span style="color: rgb(62,63,64);">In the dialog, expand<span> </span><strong>Safety and Reliability Analysis </strong>and select<span> </span><strong>Fault Tree Analysis Diagram</strong>.<br /><br /><ac:image><ri:attachment ri:filename="FTA_Diagram_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image><br /><strong style="text-align: left;"><br /></strong></span></li><li><span style="color: rgb(62,63,64);">In the search tab, type the keyword &quot;fault&quot; and then select <strong>Fault Tree Analysis Diagram</strong><strong style="text-align: left;">.<br /><br /><ac:image><ri:attachment ri:filename="Search Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image></strong></span></li></ul></li></ol><h3><span style="color: rgb(62,63,64);">Adding a Fault Tree Event in the Fault Tree Analysis Diagram</span></h3><p><span style="color: rgb(62,63,64);">To a</span>dd a Fault Tree Event in the Fault Tree Analysis Diagram</p><hr /><ul><li>From the Fault Tree Event pane, drag and drop any event in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Basic_Event.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="522f32e3-9b86-4d89-9a79-9dbe22eeaf74"><ac:rich-text-body><p>You can import a complete Fault Tree Analysis Diagram with the help of the <strong>Transfer In </strong>event.</p></ac:rich-text-body></ac:structured-macro><h3><span style="color: rgb(62,63,64);">Adding a Fault Tree Gate in the Fault Tree Analysis Diagram</span></h3><p><span style="color: rgb(62,63,64);">To add a Fault Tree Gate in the Fault Tree Analysis Diagram</span></p><hr /><ul><li>From the Fault Tree Gate pane, drag and drop any gate in the diagram pane of the modeling tool.<br /><br /><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="OR Gate.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image></span></li></ul><h3><span style="color: rgb(62,63,64);">Adding probability to the </span>Fault Tree Event</h3><p>To add probability to the Fault Tree Event</p><hr /><ol><li>From the Fault Tree Properties pane, drag and drop <strong>Define Basic Event Probability</strong> in any Fault Tree Event.<br /><br /><ac:image><ri:attachment ri:filename="Probability.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image><br /><br /></li><li><p>Double-click the probability to open the Specification of Value Property probability window and enter the probability value in the Default Value tab. <br /><br /><ac:image><ri:attachment ri:filename="Specification Window.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image></p><p>The probability value will be displayed in the Fault Tree Analysis Diagram.<br /><br /><ac:image><ri:attachment ri:filename="All probailities displayed.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0b4b52e6-7223-4459-8fc5-31088772683c"><ac:rich-text-body><p>The probability value of the Basic events will be used to calculate the probabilities of the Intermediate and Top events.</p></ac:rich-text-body></ac:structured-macro></li></ol><h3>Calculating the probability of the Intermediate and Top Event</h3><p>To calculate the probability of the Intermediate and Top Event</p><hr /><ul><li><p>Click the <strong>Run</strong> button in the diagram toolbar to run the simulation. The probabilities for the Intermediate and Top Events will be calculated automatically.<br /><br /><ac:image><ri:attachment ri:filename="Run Simulation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image><br /><ac:image><ri:attachment ri:filename="Top Event Probability.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image></p></li></ul><h3>Interconnecting the Fault Tree Analysis diagram with the System Model</h3><p>To Interconnect the Fault Tree Analysis diagram with the System Model</p><hr /><ul><li>Use the dependency matrices to establish a connection between the Fault Tree Analysis diagram and the System Model. All created events should be connected with the system model using the Relevant To relationship.<br /><br /><ac:image><ri:attachment ri:filename="Dependancy Matrices.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Fault Tree Analysis Diagram" /></ri:attachment></ac:image></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="438adb70-9cd6-4194-bcb4-0c3df4c3c0cf"><ac:parameter ac:name="title">Reference</ac:parameter><ac:rich-text-body><ul><li>To learn more about simulation, refer to <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Cameo Simulation Toolkit Documentation" /></ac:link>.</li><li>To learn more about dependency matrices, refer to <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Dependency Matrix" /></ac:link>.</li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466480 space=CSRA2024xR1 version=2 -->
## PAGE 00032: FMEAs to be analyzed

- page_id: `170466480`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466480/FMEAs+to+be+analyzed
- version_number: 2
- version_date: `2024-05-08T14:01:15.719+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Safety analysis
- labels: []

### NORMALIZED CONTENT

949458882

949458884

949458883

When you select an FMEA Item to be analyzed (the **Requires Hazard Analysis** property is set to *true*), it is automatically included in the*****FMEA to be analyzed* [CONFLUENCE_PAGE title='Smart Package' space='MD2024xR1'] predefined in the [CONFLUENCE_PAGE title='Project templates' space='CSRA2024xR1']. After the safety aspect is analyzed for that FMEA Item and a particular Safety Analysis Item is referenced to it, the FMEA Item is removed from the*****FMEA to be analyzed* Smart Package.

949458881

**Related pages**

- [CONFLUENCE_PAGE title='Safety analysis' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Describing Safety Analysis Items' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Describing reduced risks' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4cc35bd9-cb57-40db-a1e2-a7053f7c476c"><ac:parameter ac:name="id">949458882</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9a36458d-58dc-455b-9f18-79ddbf382e5d"><ac:parameter ac:name="id">949458884</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0f904e0b-c9e7-497c-a44d-c36710ebf8f0"><ac:parameter ac:name="id">949458883</ac:parameter><ac:rich-text-body><p>When you select an FMEA Item to be analyzed (the <strong>Requires Hazard Analysis</strong> property is set to <em>true</em>), it is automatically included in the<strong> </strong><em>FMEA to be analyzed</em> <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Smart Package" /></ac:link> predefined in the <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Project templates" /><ac:plain-text-link-body><![CDATA[project template]]></ac:plain-text-link-body></ac:link>. After the safety aspect is analyzed for that FMEA Item and a particular Safety Analysis Item is referenced to it, the FMEA Item is removed from the<strong> </strong><em>FMEA to be analyzed</em> Smart Package.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d9f22415-b8f0-491b-a1e8-b5d8147ce99c"><ac:parameter ac:name="id">949458881</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety analysis" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing Safety Analysis Items" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing reduced risks" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170467096 space=CSRA2024xR1 version=1 -->
## PAGE 00033: Functional Cybersecurity Concept

- page_id: `170467096`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170467096/Functional+Cybersecurity+Concept
- version_number: 1
- version_date: `2024-04-29T09:34:25.775+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

3

A Cybersecurity Requirement Diagram displays cybersecurity goals, cybersecurity requirements, and their relations. The main purpose of this diagram is to create requirements that cover the goals defined in TARA.

##### Deriving Cybersecurity Requirements

Cybersecurity Requirements are derived from Cybersecurity Goals defined in a TARA table. You can use the Cybersecurity Requirement Diagram to derive four types of Cybersecurity Requirements: Functional, Technical, Software, and Hardware.

To derive a Cybersecurity Requirement

1. From the Index page, open the Functional Cybersecurity Concept.
2. Find the Cybersecurity Goal you want to derive the C ybersecurity Requirement from and drag it to the diagram.
3. Create the Cybersecurity Requirement you want to derive by clicking it in the diagram palette and clicking an empty space on the diagram pane.
4. Name the created C ybersecurity Requirement and write the required text.
5. Create a derived relationship from the C ybersecurity Requirement to the Safety Goal as displayed below. [ATTACHMENT filename='Cybersecurity GoalsAndRequirements.png']

##### Creating a Cybersecurity Goal

To create a Cybersecurity Goal

1. In the Containment tree, right-click Functional Cybersecurity Concept and select Create Element. [IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO** **21434** and select **Cybersecurity Goal**. [ATTACHMENT filename='Cybersecurity Goal Menu.png']
  - In the search tab, type the keyword goals and then select **Cybersecurity Goal** . [IMAGE alt='' src='']
3. Name the created Cybersecurity Goal in the Containment tree. The cybersecurity goal has the prefix CG, which denotes that the created element is c ybersecurity goals; the number 1 indicates that it is the first c ybersecurity goal**** created. [IMAGE alt='' src='']

You can also create a Cybersecurity Goal in the Cybersecurity Goal Table or by using the diagram panel.

##### Creating a Cybersecurity Requirement

To create a Cybersecurity Requirement

1. In the Containment tree, right-click Functional Cybersecurity Concept and select Create Element. [IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**. From the drop-down list, choose one of the following:
    - Functional Cybersecurity Requirement
    - Hardware Cybersecurity Requirement
    - Software Cybersecurity Requirement
    - Technical Cybersecurity Requirement [ATTACHMENT filename='Cybersecurity Requirement_Menu.jpg']
  - In the search tab, type the keyword goals and then select the required Cybersecurity Requirement . [ATTACHMENT filename='Cybersecurity Requirement_Search.jpg']
3. Name the created Cybersecurity Requirement in the Containment tree. 
 
[IMAGE alt='' src='']

You can also create a cybersecurity requirement in the cybersecurity requirement tables.

##### Functional Cybersecurity Concept Table

The Functional Cybersecurity Concept Table provides an overview of goals & requirements to be implemented to secure assets.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fa760972-d553-481d-9841-f7390fbfff7f"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>A Cybersecurity Requirement Diagram displays cybersecurity goals, cybersecurity requirements, and their relations. The main purpose of this diagram is to create requirements that cover the goals defined in TARA. </p><h3>Deriving Cybersecurity Requirements</h3><p>Cybersecurity Requirements are derived from Cybersecurity Goals defined in a TARA table. You can use the Cybersecurity  Requirement Diagram to derive four types of Cybersecurity Requirements: Functional, Technical, Software, and Hardware.</p><p>To derive a Cybersecurity Requirement</p><hr /><ol><li><span style="color: rgb(62,63,64);">From the Index page, open the Functional Cybersecurity Concept.</span></li><li>Find the Cybersecurity Goal you want to derive the C<span style="color: rgb(62,63,64);">ybersecurity </span>Requirement from and drag it to the diagram.</li><li>Create the Cybersecurity Requirement you want to derive by clicking it in the diagram palette and clicking an empty space on the diagram pane.</li><li>Name the created C<span style="color: rgb(62,63,64);">ybersecurity </span>Requirement and write the required text.</li><li>Create a derived relationship from the C<span style="color: rgb(62,63,64);">ybersecurity </span>Requirement to the Safety Goal as displayed below.<br /><br /><ac:image><ri:attachment ri:filename="Cybersecurity GoalsAndRequirements.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image></li></ol><h3>Creating a Cybersecurity Goal</h3><p>To create a Cybersecurity Goal</p><hr /><ol><li>In the Containment tree, right-click <strong>Functional Cybersecurity Concept </strong>and select<strong><span> </span>Create Element.</strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Create Element.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">Do one of the following:<ul><li class="auto-cursor-target"><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="8e2d61f6-324f-4d14-a611-205ffa444e5b">In the dialog</ac:inline-comment-marker>, expand <strong>ISO</strong> <strong>21434</strong> and select <strong>Cybersecurity Goal</strong>.</span><br /><strong><br /></strong><ac:image><ri:attachment ri:filename="Cybersecurity Goal Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image><br /><br /></li><li class="auto-cursor-target">In the search tab, type the keyword goals and then select<span> <strong>Cybersecurity Goal</strong></span><strong>.<br /></strong><br /><strong><ac:image><ri:attachment ri:filename="Cybersecurity Goal_Search.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image></strong><br /><br /></li></ul></li><li class="auto-cursor-target">Name the created Cybersecurity Goal in the Containment tree. The cybersecurity goal has the prefix <strong>CG, </strong>which denotes that the created element is c<span>ybersecurity goals; </span>the number <strong>1</strong> indicates that it is the first c<span>ybersecurity goal<strong> </strong></span>created.<br /><br /><strong><ac:image><ri:attachment ri:filename="Cybersecurity Goal_Created.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image></strong></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="095dae29-e483-4570-8157-e73c2f75ecf9"><ac:rich-text-body><p>You can also create a Cybersecurity Goal in the Cybersecurity Goal Table or by using the diagram panel.</p></ac:rich-text-body></ac:structured-macro><h3>Creating a Cybersecurity Requirement</h3><p>To create a Cybersecurity Requirement</p><hr /><ol><li>In the Containment tree, right-click <strong>Functional Cybersecurity Concept </strong>and select<strong><span> </span>Create Element.</strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Create Element.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">Do one of the following:<ul><li><p>In the dialog, expand <strong>ISO 21434</strong>. From the drop-down list, choose one of the following:</p><ul><li>Functional Cybersecurity Requirement</li><li>Hardware Cybersecurity Requirement </li><li>Software Cybersecurity Requirement</li><li>Technical Cybersecurity Requirement<strong><br /><br /></strong><ac:image><ri:attachment ri:filename="Cybersecurity Requirement_Menu.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image><br /><br /></li></ul></li><li class="auto-cursor-target">In the search tab, type the keyword goals and then select<span> the required Cybersecurity Requirement</span><strong>.<br /><br /></strong><ac:image><ri:attachment ri:filename="Cybersecurity Requirement_Search.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image><br /><br /></li></ul></li><li class="auto-cursor-target"><p class="auto-cursor-target">Name the created Cybersecurity Requirement in the Containment tree.<br /><br /><ac:image><ri:attachment ri:filename="Cybersecurity Requirement_Created.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image></p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="27d4e3c8-4ffa-4234-b9c7-5e53ac4dbe8c"><ac:rich-text-body><p>You can also create a cybersecurity requirement in the cybersecurity requirement tables.</p></ac:rich-text-body></ac:structured-macro><h3>Functional Cybersecurity Concept Table</h3><p>The Functional Cybersecurity Concept Table provides an overview of goals &amp; requirements to be implemented to secure assets.</p><p><ac:image><ri:attachment ri:filename="Functional cybersecurity concept table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Functional Cybersecurity Concept" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170467112 space=CSRA2024xR1 version=2 -->
## PAGE 00034: Generating  Cybersecurity Reports

- page_id: `170467112`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170467112/Generating+Cybersecurity+Reports
- version_number: 2
- version_date: `2024-05-08T14:01:17.626+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

The cybersecurity reports are generated using the [Report Wizard](https://docs.nomagic.com/display/MD2024xR1/Report+Wizard). The report template used for generating the cybersecurity reports is the**TARA Report Template**.****To learn more about how to generate the cybersecurity reports, refer to the [CONFLUENCE_PAGE title='Reports' space='CSRA2024xR1'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:inline-comment-marker ac:ref="0c271641-a816-4a1e-b63e-5f0ee7e2d8d3">The cybersecurity reports are generated using the <span style="color: rgb(23,43,77);"><a href="https://docs.nomagic.com/display/MD2024xR1/Report+Wizard" rel="nofollow">Report Wizard</a>. The report template used for generating the cybersecurity reports is the </span><span style="color: rgb(23,43,77);"><strong>TARA Report Template</strong>.<strong> </strong></span>To learn more about how to generate the cybersecurity reports</ac:inline-comment-marker>, refer to the <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Reports" /></ac:link> page.</p>
````

<!--NOMAGIC_PAGE id=170466465 space=CSRA2024xR1 version=1 -->
## PAGE 00035: Generating FMEA Items

- page_id: `170466465`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466465/Generating+FMEA+Items
- version_number: 1
- version_date: `2017-11-13T14:52:00.199+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > Reliability analysis using FMEA
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Important

563844983

#### CONTENT-COLUMN: Important

563844985

#### CONTENT-BLOCK: Important

563844984

After [CONFLUENCE_PAGE title='Linking Failure Modes to model elements' space='CSRA2024xR1'] of your model, you can use these design elements as the source to generate FMEA Items. Each Failure mode linked to a specific model element should result in a new FMEA Item. Generating FMEA Items from design elements of your model saves time and helps avoid mistakes, because some properties (such as **Item**,**Failure Mode** and **Subsystem**) are specified for you.

FMEA Items can be generated for:

- Actions
- Blocks
- Part Properties
- Requirements
- Operations
- Activities

To generate an FMEA Item(s)

1. In the model browser, right-click the element from which you want to generate an FMEA Item, or right-click the shape of that element in a diagram.
2. In the menu, select **Tools** > **Generate FMEA Item(s)**. ImportantThe **Generate FMEA Item(s)** command is only active if the element you try to generate an FMEA Item from has at least one Failure Mode linked to it.
3. In the Select Destination Package dialog, select the package that you want to contain the newly created FMEA Item(s).
4. Click OK .

After completing the above steps, a new FMEA Item is created for each Failure Mode linked to the source model element. The name of the new FMEA Item is s*ource element name + Failure*. For example, if you generate an FMEA Item from the *Battery* Block, the FMEA Item is named *Battery Failure*.

If you generate an FMEA Item from a design element of your model, the following FMEA item properties are specified automatically:

- Item - the property value is set to the source element from which the FMEA Item is generated.
- Failure Mode - the property value is set to the Failure Mode linked to the source element.
- Subsystem - the property value is set to one of the following:
  - Activity owning the Action from which the FMEA Item is generated.
  - Block owning the Part from which the FMEA Item is generated.
  - The owner (the Owner property value) of the Operation from which the FMEA Item is generated.
  - If the source element is other than Action, Part or Operation, the Subsystem property is not specified.

563844982

**Related pages**

- [CONFLUENCE_PAGE title='Reliability analysis using FMEA' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Describing FMEA Items' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Cloning FMEA Table rows' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b02c575f-706d-4b32-9036-52ebe9777e73"><ac:parameter ac:name="id">563844983</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a2d23897-9994-443b-9530-1c92a560f612"><ac:parameter ac:name="id">563844985</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cb9b83c4-8ee3-4446-9026-85ad99cca14d"><ac:parameter ac:name="id">563844984</ac:parameter><ac:rich-text-body><p>After <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /><ac:plain-text-link-body><![CDATA[linking Failure Modes to the design elements]]></ac:plain-text-link-body></ac:link> of your model, you can use these design elements as the source to generate FMEA Items. Each Failure mode linked to a specific model element should result in a new FMEA Item. Generating FMEA Items from design elements of your model saves time and helps avoid mistakes, because some properties (such as <strong>Item</strong>,<strong><ac:inline-comment-marker ac:ref="ff4a4833-5521-4283-a2c6-d305821f0594"> Failure Mode</ac:inline-comment-marker></strong> and <strong>Subsystem</strong>) are specified for you.</p><p>FMEA Items can be generated <ac:inline-comment-marker ac:ref="e5954bb5-d01d-4463-9a20-64bce76699f9">for</ac:inline-comment-marker>:</p><ul><li>Actions</li><li>Blocks</li><li>Part Properties</li><li>Requirements</li><li>Operations</li><li>Activities</li></ul><p><br /></p><p>To generate an FMEA Item(s)</p><hr /><ol><li>In the model browser, right-click the element from which you want to generate an FMEA Item, or right-click the shape of that element in a diagram.</li><li><p class="auto-cursor-target">In the menu, select <strong>Tools</strong> &gt; <strong>Generate FMEA Item(s)</strong>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2c4c3a5c-e1d4-4e8a-8398-12c4b5e4dd8c"><ac:parameter ac:name="title">Important</ac:parameter><ac:rich-text-body><p>The <strong>Generate FMEA Item(s)</strong> command is only active if the element you try to generate an FMEA Item from has at least one Failure Mode linked to it.</p></ac:rich-text-body></ac:structured-macro></li><li>In the <strong>Select Destination Package</strong> dialog, select the package that you want to contain the newly created FMEA Item(s).</li><li>Click <strong>OK</strong>.</li></ol><p><br />After completing the above steps, a new FMEA Item is created for each Failure Mode linked to the source model element. The name of the new FMEA Item is s<em>ource element name + Failure</em>. For example, if you generate an FMEA Item from the <em>Battery</em> Block, the FMEA Item is named <em>Battery Failure</em>.</p><p>If you generate an FMEA Item from a design element of your model, the following FMEA item properties are specified automatically:</p><ul><li><strong>Item</strong> - the property value is set to the source element from which the FMEA Item is generated.</li><li><strong>Failure Mode</strong> - the property value is set to the Failure Mode linked to the source element.</li><li><strong>Subsystem</strong> - the property value is set to one of the following:<ul><li>Activity owning the Action from which the FMEA Item is generated.</li><li>Block owning the Part from which the FMEA Item is generated.</li><li>The owner (the <strong>Owner</strong> property value) of the Operation from which the FMEA Item is generated.</li><li>If the source element is other than Action, Part or Operation, the <strong>Subsystem</strong> property is not specified.</li></ul></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="646ba7e7-e9e3-4902-bd64-8ec29a993422"><ac:parameter ac:name="id">563844982</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Reliability analysis using FMEA" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing FMEA Items" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cloning FMEA Table rows" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466489 space=CSRA2024xR1 version=2 -->
## PAGE 00036: Generating reports

- page_id: `170466489`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466489/Generating+reports
- version_number: 2
- version_date: `2024-05-08T14:01:15.951+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Additional features
- labels: []

### NORMALIZED CONTENT

949872724

949872726

949872725

You can generate reports in the .xlsx format directly from the [CONFLUENCE_PAGE title='Describing FMEA Items' space='CSRA2024xR1'], [CONFLUENCE_PAGE title='Describing Safety Analysis Items' space='CSRA2024xR1'], or [CONFLUENCE_PAGE title='Describing reduced risks' space='CSRA2024xR1'] tables.

To generate a report with all data in a table

1. Open a desired table.
2. In the table toolbar, click the Report button. The Generate Report dialog opens.
3. In the open dialog, define Output Options and click Generate . The report is generated.

If you want to customize your report, you may use the **[CONFLUENCE_PAGE title='Report Wizard' space='MD2024xR1']** to generate the report. In the report templates list, the **FMEA template** and **Risk and Risk reduction template** are prepared for **Safety and Reliability Analysis**. Using the **Report Wizard**, you can modify a selected template, define variables, select objects to add to the report, and perform various other actions.

949872723

**Related pages**

- [CONFLUENCE_PAGE title='Additional features' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Traceability maps' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Safety and Reliability Coverage Analysis' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Linking Failure Modes to model elements' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="eb1d3911-406f-42c8-8813-98f248b7c97e"><ac:parameter ac:name="id">949872724</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="1f1b02ab-6b91-4aca-b978-bc26ce0eeb69"><ac:parameter ac:name="id">949872726</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c3ee252f-fa58-4184-8319-ffa76ace5dbb"><ac:parameter ac:name="id">949872725</ac:parameter><ac:rich-text-body><p>You can generate reports in the .xlsx format directly from the <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing FMEA Items" /><ac:plain-text-link-body><![CDATA[FMEA]]></ac:plain-text-link-body></ac:link>, <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing Safety Analysis Items" /><ac:plain-text-link-body><![CDATA[Risk]]></ac:plain-text-link-body></ac:link>, or <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing reduced risks" /><ac:plain-text-link-body><![CDATA[Risk Reductions]]></ac:plain-text-link-body></ac:link> tables.</p><p> </p><p>To generate a report with all data in a table</p><hr /><ol><li>Open a desired table.</li><li>In the table toolbar, click the <strong>Report </strong>button. The <strong>Generate Report </strong>dialog opens.</li><li>In the open dialog, define <strong>Output Options</strong> and click <strong>Generate</strong>. The report is generated.</li></ol><p> </p><p>If you want to customize your report, you may use the <strong><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Report Wizard" /></ac:link></strong> to generate the report. In the report templates list, the <strong>FMEA template</strong> and <strong>Risk and Risk reduction template</strong> are prepared for <strong>Safety and Reliability Analysis</strong>. Using the <strong>Report Wizard</strong>, you can modify a selected template, define variables, select objects to add to the report, and perform various other actions.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4df43455-6167-4410-b6bf-621e901a4014"><ac:parameter ac:name="id">949872723</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Additional features" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety and Reliability Coverage Analysis" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466590 space=CSRA2024xR1 version=2 -->
## PAGE 00037: Generic Safety Table

- page_id: `170466590`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466590/Generic+Safety+Table
- version_number: 2
- version_date: `2024-05-08T14:01:16.410+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: []

### NORMALIZED CONTENT

1102391337

1102391340

1102426125

**On this page**

4

1102391339

You can use a Generic Safety Table to display all relevant elements depending on the selected scope as shown in the following figure. An element added as a scope element should extend the ISO 26262 library (e.g., Typical Automotive Situation, Accident Scenario, Hazardous Event, Automotive Effect).

[IMAGE alt='' src='']

###### An example of a Generic Safety Table

##### Creating a Generic Safety Table

You can create a Generic Safety Table as described below.

To create a Generic Safety Table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select Generic Safety Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select Create Diagram and select Generic Safety Table in the open dialog. [ATTACHMENT filename='creating_generic_safety_table.png']
3. When the table is created, type the name of the table and press Enter.
4. Click [ATTACHMENT filename='3dot_long.png'] next to the Element Type box.
5. In the Select Element Type dialog, select the types of elements you want to display in the table, and click OK .
6. Click [ATTACHMENT filename='3dot_long.png'] next to the Scope box.
7. On the left side of the Select Scope dialog, select the scope element of the table, click [ATTACHMENT filename='add_button.png'] to add the element to the selected elements area, and click OK .
8. [CONFLUENCE_PAGE title='Working with columns' space='MD2024xR1'] (by default, a Generic Safety Table has only the Name column).

##### Creating elements in a Generic Safety Table

There are two ways to create elements for a Generic Safety Table: you can do it right in the table or in the Containment tree. If you create an element in the Containment tree and it falls under the scope of a Generic Safety Table, the element is automatically added to the table. If you want to create an element right in a Generic Safety Table, follow the steps below.

To create an element in a Generic Safety Table

1. In a Generic Safety Table, select a table row.
2. Do one of the following:
  - In the table toolbar, click [ATTACHMENT filename='add_sibling.png'] to create an element of the same level as the one you have selected.
  - In the table toolbar, click [IMAGE alt='' src='']to create an element nested under the selected element.
3. Type the name of the new element and press Enter.

##### Case study: Creating Generic Safety Table for a custom element type

You can use a Generic Safety Table to display custom element types with their properties. Let's analyze the workflow of creating a custom Operational Situation and displaying it in a Generic Safety Table.

To create a custom Operational Situation and display it in a Generic Safety Table

1. In your model, create a Profile Diagram.
2. In the Profile Diagram, create a Class and name it, e.g., Crash Automotive Situation .
3. Apply the «OperationalSituation» stereotype to the Class.
4. In the ISO 26262 Library, find the TypicalAutomotiveSituation element and drag it to the Profile diagram.
5. Create a Generalization relationship from the Class created in step 2 to TypicalAutomotiveSituation . Your Profile Diagram should look as displayed below. [ATTACHMENT filename='creating_custom_operational_situation.png']
6. Save an reload the project.
7. In the Containment tree, right-click the element you want to be the owner of a Generic Safety Table, select Create Diagram , and select Generic Safety Table in the open dialog.
8. When the table is created, type the name of the table, e.g., *Crash Operational Situations*, and press Enter.
9. Click [ATTACHMENT filename='3dot_long.png'] next to the Element Type box.
10. In the Select Element Type dialog, select OperationalSituation , and click OK .
11. Click [ATTACHMENT filename='3dot_long.png'] next to the Scope box.
12. On the left side of the Select Scope dialog, select the scope element of the table, e.g., Crash Automotive Situation , click [ATTACHMENT filename='add_button.png'] to add the element to the selected elements area, and click OK .
13. In the Generic Safety Table, create new elements of the custom element type defined as the table scope, e.g., Crash Automotive Situation .
14. [CONFLUENCE_PAGE title='Working with columns' space='MD2024xR1'] (by default, a Generic Safety Table has only the Name column).

After following the above steps and defining the properties displayed in your Generic Safety Table, it should look similar to the example below.

[IMAGE alt='' src='']

###### An example of a Generic Safety Table created for a custom Operational Situation.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8dd74909-7f3c-4534-a2fa-437004b760d9"><ac:parameter ac:name="id">1102391337</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="98a91ffa-d743-47b7-8cd4-4da80a6728a0"><ac:parameter ac:name="id">1102391340</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="102fd9b3-db52-4bc1-8350-496ad07957dc"><ac:parameter ac:name="id">1102426125</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="91f7ff6e-35ea-43c9-a95a-74779658c222"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4e87f573-44a3-449d-8b7f-0ffb1aa6b7b6"><ac:parameter ac:name="id">1102391339</ac:parameter><ac:rich-text-body><p>You can use a Generic Safety Table to display all relevant elements depending on the selected scope as shown in the following figure. An element added as a scope element should extend the ISO 26262 library (e.g., Typical Automotive Situation, Accident Scenario, Hazardous Event, Automotive Effect).<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="generic_safety_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of a Generic Safety Table</h6><h3>Creating a Generic Safety Table</h3><p>You can create a Generic Safety Table as described below.</p><p><br /></p><p>To create a Generic Safety Table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>Generic Safety Table</strong> in the open dialog.</li><li>In the Containment tree, right-click the owner of the table, select <strong>Create Diagram</strong> and select <strong>Generic Safety Table</strong> in the open dialog.<br /><br /><ac:image><ri:attachment ri:filename="creating_generic_safety_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ri:attachment></ac:image><br /><br /></li></ul></li><li><span style="color: rgb(62,63,64);">When the table is created, type the name of the table and press Enter.</span></li><li>Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="3dot_long.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image> next to the <strong>Element Type</strong> box.</li><li>In the <strong>Select Element Type</strong> dialog, select the types of elements you want to display in the table, and click <strong>OK</strong>.</li><li>Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="3dot_long.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image> next to the <strong>Scope</strong> box.</li><li>On the left side of the <strong>Select Scope</strong> dialog, select the scope element of the table, click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="add_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image> to add the element to the selected elements area, and click <strong>OK</strong>.</li><li><ac:link ac:anchor="Adding and removing columns"><ri:page ri:space-key="MD2024xR1" ri:content-title="Working with columns" /><ac:plain-text-link-body><![CDATA[Add the desired columns to the table]]></ac:plain-text-link-body></ac:link> (by default, a Generic Safety Table has only the <em>Name</em> column).</li></ol><p><br /></p><h3>Creating elements in a Generic Safety Table</h3><p>There are two ways to create elements for a Generic Safety Table: you can do it right in the table or in the Containment tree. If you create an element in the Containment tree and it falls under the scope of a Generic Safety Table, the element is automatically added to the table. If you want to create an element right in a Generic Safety Table, follow the steps below.</p><p><br /></p><p>To create an element in a Generic Safety Table</p><hr /><ol><li>In a Generic Safety Table, select a table row.</li><li>Do one of the following:<br /><ul><li>In the table toolbar, click <ac:image><ri:attachment ri:filename="add_sibling.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image> to create an element of the same level as the one you have selected.</li><li><p class="auto-cursor-target">In the table toolbar, click <ac:image><ri:attachment ri:filename="add_nested.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image>to create an element nested under the selected element.</p></li></ul></li><li>Type the name of the new element and press Enter.</li></ol><h3><br />Case study: Creating Generic Safety Table for a custom element type</h3><p>You can use a Generic Safety Table to display custom element types with their properties. <span style="color: rgb(62,63,64);">Let's analyze the workflow of creating a custom Operational Situation and displaying it in a Generic Safety Table.</span></p><p><span style="color: rgb(62,63,64);"><br /></span></p><p><span style="color: rgb(62,63,64);">To create a custom Operational Situation and display it in a Generic Safety Table</span></p><hr /><ol><li>In your model, create a Profile Diagram.</li><li>In the Profile Diagram, create a Class and name it, e.g., <em>Crash Automotive Situation</em>.</li><li>Apply the «OperationalSituation» stereotype to the Class.</li><li>In the ISO 26262 Library, find the <em>TypicalAutomotiveSituation</em> element and drag it to the Profile diagram.</li><li>Create a Generalization relationship from the Class created in step 2 to <em>TypicalAutomotiveSituation</em>. Your Profile Diagram should look as displayed below.<br /><br /><ac:image><ri:attachment ri:filename="creating_custom_operational_situation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ri:attachment></ac:image><br /><br /></li><li>Save an reload the project.</li><li>In the Containment tree, right-click the element you want to be the owner of a Generic Safety Table, select <strong>Create Diagram</strong>, and select <strong>Generic Safety Table</strong> in the open dialog.</li><li><span style="color: rgb(62,63,64);">When the table is created, type the name of the table, e.g., <em>Crash Operational Situations</em>, and press Enter.</span></li><li>Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="3dot_long.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ri:attachment></ac:image> next to the <strong>Element Type</strong> box.</li><li>In the <strong>Select Element Type</strong> dialog, select <strong>OperationalSituation</strong>, and click <strong>OK</strong>.</li><li>Click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="3dot_long.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ri:attachment></ac:image> next to the <strong>Scope</strong> box.</li><li>On the left side of the <strong>Select Scope</strong> dialog, select the scope element of the table, e.g., <em>Crash Automotive Situation</em>, click <ac:image ac:thumbnail="true" ac:height="23"><ri:attachment ri:filename="add_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ri:attachment></ac:image> to add the element to the selected elements area, and click <strong>OK</strong>.</li><li>In the Generic Safety Table, create new elements of the custom element type defined as the table scope, e.g., <em>Crash Automotive Situation</em>.</li><li><ac:link ac:anchor="Adding and removing columns"><ri:page ri:space-key="MD2024xR1" ri:content-title="Working with columns" /><ac:plain-text-link-body><![CDATA[Add the desired columns to the table]]></ac:plain-text-link-body></ac:link> (by default, a Generic Safety Table has only the <em>Name</em> column).</li></ol><p><br />After following the above steps and defining the properties displayed in your Generic Safety Table, it should look similar to the example below.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="generic_safety_table_for_crash_automotive_situation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generic Safety Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of a Generic Safety Table created for a custom Operational Situation.</h6></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466458 space=CSRA2024xR1 version=1 -->
## PAGE 00038: Getting started

- page_id: `170466458`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466458/Getting+started
- version_number: 1
- version_date: `2018-06-04T03:48:07.624+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

948442199

948442201

948442200

The Cameo Safety and Reliability Analyzer plugin requires the [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP184'] to be installed in your modeling tool.

Use the following procedures to install the Cameo Safety and Reliability Analyzer plugin.

To download and install a plugin via the **Resource/Plugin Manager** dialog

1. Start your modeling tool.
2. From the modeling tool main menu, select Help > Resource/Plugin Manager . The Resource/Plugin Manager dialog opens and prompt you to check for the latest product updates and resources. Click Check for Updates > Check .
3. Select the check box near the desired plugin and click Download/Install .
4. Restart your modeling tool.

To install a plugin from the downloaded archive file (zip) via the **Resource/Plugin Manager** dialog

1. Start your modeling tool.
2. From the main menu of a modeling tool, select Help > Resource/Plugin Manager .
3. Click the Import button to specify the downloaded plugin file location. The plugin is extracted and installed automatically.
4. Restart your modeling tool.

948442198

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="66b0b9ea-9474-4381-b6d7-626e24c3b942"><ac:parameter ac:name="id">948442199</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="61adcf5b-6ffa-4ba0-84f5-874503d57412"><ac:parameter ac:name="id">948442201</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="58c3cb98-9094-4c58-bd22-e1cc6fdbc203"><ac:parameter ac:name="id">948442200</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1402f173-2577-4964-bcd6-ca4c67adefa6"><ac:rich-text-body><p>The Cameo Safety and Reliability Analyzer plugin requires the <ac:link><ri:page ri:space-key="SYSMLP184" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML plugin]]></ac:plain-text-link-body></ac:link> to be installed in your modeling tool.</p></ac:rich-text-body></ac:structured-macro><p> </p><p>Use the following procedures to install the <span>Cameo Safety and Reliability Analyzer plugin.</span></p><p><span><br /></span></p><p>To download and install a plugin via the <strong>Resource/Plugin Manager</strong> dialog</p><hr /><ol><li>Start your modeling tool.</li><li>From the modeling tool main menu, select <strong>Help</strong> &gt; <strong>Resource/Plugin Manager</strong>. The <strong>Resource/Plugin Manager</strong> dialog opens and prompt you to check for the latest product updates and resources. Click <strong>Check for Updates</strong> &gt; <strong>Check</strong>.</li><li>Select the check box near the desired plugin and click <strong>Download/Install</strong>.</li><li>Restart your modeling tool.<br /><br /></li></ol><p>To install a plugin from the downloaded archive file (zip) via the <strong>Resource/Plugin Manager</strong> dialog</p><hr /><ol><li>Start your modeling tool.</li><li>From the main menu of a modeling tool, select <strong>Help</strong> &gt; <strong>Resource/Plugin Manager</strong>.</li><li>Click the <strong>Import</strong> button to specify the downloaded plugin file location. The plugin is extracted and installed automatically.</li><li>Restart your modeling tool.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7be319d8-9520-4c69-b98b-4b4cf75c0dab"><ac:parameter ac:name="id">948442198</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="29531500-548e-4caa-8a43-e73fe422fea4" /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466571 space=CSRA2024xR1 version=1 -->
## PAGE 00039: HARA Table

- page_id: `170466571`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466571/HARA+Table
- version_number: 1
- version_date: `2023-10-18T09:40:34.897+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

#### CONTENT-LAYER: Use filters to find elements quicker

126940009

#### CONTENT-COLUMN: Use filters to find elements quicker

126940023

126940007

**On this page:**

4

#### CONTENT-BLOCK: Use filters to find elements quicker

126940013

A HARA Table allows you to define Hazardous Events as a combination of Hazards, Effects and an Accident Scenario. By default, the table shows seven columns. The rest of the columns are hidden, but you can show them if needed.

[IMAGE alt='' src='']

###### An example of a HARA Table.

ASIL returns a calculated value according to the specified values of **Exposure**, **Controllability**and **Severity**. If there are more than one values of **Severity**or **Exposure**then take the higher value (single value).

[IMAGE alt='' src='']

###### ASIL Table

##### Creating HARA Table

You can create a HARA Table as described below.

To create a HARA Table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select HARA Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select Create Diagram and select HARA Table in an open dialog . [ATTACHMENT filename='creating_hara_table.png']
3. When the table is created, type the name of the table and press Enter.

After completing the above steps, a HARA Table is created. The scope and element type of the table are already specified for you.

##### Creating Hazardous Events

There are two ways to create a Hazardous Event: you can do it right in a HARA Table or in the Containment tree.

To create a Hazardous Event in the Containment tree

1. In the Containment tree, right-click the owner of a new element and select Create Element .
2. In the open window, select Hazardous Event . [ATTACHMENT filename='creating_hazardous_events.png']
3. When a Hazardous Event is created, type the name of the element and press Enter.

When you create a Hazardous Event in the model browser, it is automatically added to a HARA Table if it exists.

To create a Hazardous Event in a HARA Table

1. In a HARA Table, select a table row.
2. Do one of the following:
  - In the table toolbar, click Add Sibling to create an element of the same level as the one you have selected.
  - In the table toolbar, click **Add Nested** to create an element nested under the selected element.
3. Type the name of the new element and press Enter.

****When you create a Hazardous Event and add it to a HARA Table, you need to define the element as described in the section below.

##### Defining Hazardous Events

After creating a Hazardous Event, you need to define it by assigning an Accident Scenario, Hazards, and Effects to the element. You also need to create and assign a Safety Goal. The Accident Scenario, Hazards, Effectsand Safety Goal also can be dragged from the Containment tree.

[IMAGE alt='' src='']

###### Dragging and dropping the **Hazard** in the HARA Table

To assign an Accident Scenario

1. In a HARA Table, double-click the cell the Accident Scenario column and click [ATTACHMENT filename='edit_button.png'] .
2. On the left side of the Select Element dialog, open the List tab.
3. Select the Accident Scenario you want to assign.
4. Click **OK**. Use filters to find elements quickerWhen you assign a Accident Scenario, use a filter after step 2 to find elements quicker:In the **Select Elements** dialog, click [IMAGE alt='' src=''] next to the **Filter by ISO properties** box.In the **Select Properties** dialog, click the **Value** box of a property and select the desired property value from the list. 
 
[IMAGE alt='' src='']Click **OK**.Now the **List** tab displays the elements with the selected property value.

After assigning an Accident Scenario to a Hazardous Event, the Automotive Safety Integrity Level (ASIL) is calculated automatically.

Assigning Hazards

1. In a HARA Table, double-click the cell of the Hazard column and click [ATTACHMENT filename='edit_button.png'] .
2. On the left side of the Select Element dialog, open the List tab.
3. Double-click the Hazards you want to assign. The elements should be added to the selected elements area.
4. Click OK .

To assign an Effect

1. In a HARA Table, double-click the cell of the column representing the group of Effects ( Vehicle Level Effects or System Level Effects ) you want to assign an click [ATTACHMENT filename='edit_button.png'] .
2. On the left side of the Select Element dialog, open the List tab.
3. Double-click the Effects you want to assign. The elements should be added to the selected elements area.
4. Click OK .

To create and assign Safety Goal

1. In a HARA Table, double-click the cell of the Safety Goal column and click [ATTACHMENT filename='edit_button.png'] .
2. In the Select Elements dialog, enable the Creation Mode if it is not enabled yet.
3. In the element tree on the left side of the dialog, select the owner of a Safety Goal and click the Create button.
4. When the Specification window of the created element opens, enter the element name and close the Specification window. The element is created and automatically added to the selected elements area on the right side of the **Select Elements** dialog. 
 
[IMAGE alt='' src='']
5. Click**OK**to close the**Select Elements**dialog.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f9697ac8-4139-4727-b5c1-622b43c3b02e"><ac:parameter ac:name="id">126940009</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="900dfe6e-29e9-49ec-97df-ff9f966b30b7"><ac:parameter ac:name="id">126940023</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5f031b39-c633-4a97-b79a-db3c52903240"><ac:parameter ac:name="id">126940007</ac:parameter><ac:rich-text-body><p><strong>On this page:</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="074a4cca-d351-4c1c-9d4a-8956dbe7afd3"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b4c0608f-31c3-453c-b31c-c0afc0bf2bae"><ac:parameter ac:name="id">126940013</ac:parameter><ac:rich-text-body><p>A HARA Table allows you to define Hazardous Events as a combination of Hazards, Effects and an Accident Scenario. By default, the table shows seven columns. The rest of the columns are hidden, but you can show them if needed.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="HARA_Table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of a HARA Table.</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="3bc90445-6610-4d5d-9285-45c849f157cf"><ac:rich-text-body><p>ASIL returns a calculated value according to the specified values of <strong>Exposure</strong>, <strong>Controllability </strong>and <strong>Severity</strong>. If there are more than one values of <strong>Severity </strong>or <strong>Exposure </strong>then take the higher value (single value).</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="ASIL_Table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">ASIL Table</h6></ac:rich-text-body></ac:structured-macro><h3>Creating HARA Table</h3><p>You can create a HARA Table as described below.</p><p><br /></p><p>To create a HARA Table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>HARA Table</strong> in the open dialog.</li><li>In the Containment tree, right-click the owner of the table, select <strong>Create Diagram</strong> and select <strong>HARA Table</strong> in an open <ac:inline-comment-marker ac:ref="644484b6-488b-462a-8d1b-ff85fe07af7f">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="creating_hara_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image><br /><br /></li></ul></li><li>When the table is created, type the name of the table and press Enter.</li></ol><p><br /></p><p>After completing the above steps, a HARA Table is created. The scope and element type of the table are already specified for you.</p><h3><br />Creating Hazardous Events</h3><p>There are two ways to create a Hazardous Event: you can do it right in a HARA Table or in the Containment tree.</p><p><br /></p><p>To create a Hazardous Event in the Containment tree</p><hr /><ol><li>In the Containment tree, right-click the owner of a new element and select <strong>Create Element</strong>.</li><li>In the open window, select <strong>Hazardous Event</strong>.<br /><br /><ac:image><ri:attachment ri:filename="creating_hazardous_events.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">When a Hazardous Event is created, type the name of the element and press Enter.</span></li></ol><p><span style="color: rgb(62,63,64);"><br /><span style="color: rgb(62,63,64);">When you create a Hazardous Event in the model browser, it is automatically added to a HARA Table if it exists.</span></span></p><p><span style="color: rgb(62,63,64);"><br /></span></p><p><br /></p><p>To create a Hazardous Event in a HARA Table</p><hr /><ol><li>In a HARA Table, select a table row.</li><li>Do one of the following:<br /><ul><li>In the table toolbar, click <strong style="text-align: left;">Add Sibling</strong> to create an element of the same level as the one you have selected.</li><li><p class="auto-cursor-target">In the table toolbar, click <strong style="text-align: left;">Add Nested</strong> to create an element nested under the selected element.</p></li></ul></li><li>Type the name of the new element and press Enter.</li></ol><p><strong><br /></strong>When you create a Hazardous Event and add it to a HARA Table, you need to define the element as described in the section below.</p><h3><br />Defining Hazardous Events</h3><p>After creating a Hazardous Event, you need to define it by assigning an <ac:inline-comment-marker ac:ref="a9b0c581-cf45-46f4-910e-7c17c4e3f959">Accident Scenario, Hazards, and Effects to the element. You also need to create and assign a Safety Goa</ac:inline-comment-marker>l. T<span style="color: rgb(62,63,64);">he Accident Scenario, Hazards, Effects</span><span style="color: rgb(62,63,64);"> and Safety Goal also can be dragged from the Containment tree.<br /></span></p><p><span style="color: rgb(62,63,64);"><ac:image ac:align="center"><ri:attachment ri:filename="HARA_Table_Hazard_Drag.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image><br /></span></p><h6 style="text-align: center;">Dragging and dropping the <strong>Hazard</strong> in the HARA Table</h6><p>To assign an Accident Scenario</p><hr /><ol><li>In a HARA Table, double-click the cell the <strong>Accident Scenario</strong> column and click <ac:image ac:thumbnail="true" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image>.</li><li>On the left side of the <strong>Select Element</strong> dialog, open the <strong>List</strong> tab.</li><li>Select the Accident Scenario you want to assign.</li><li><p class="auto-cursor-target">Click <strong>OK</strong>.</p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="f0e87259-8b7b-49ec-9d16-ffb1dc053285"><ac:parameter ac:name="title">Use filters to find elements quicker</ac:parameter><ac:rich-text-body><p>When you assign a <span style="color: rgb(62,63,64);">Accident Scenario</span>, use a filter after step 2 to find elements quicker:</p><ol><li>In the <strong>Select Elements</strong> dialog, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="3dot_long.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image> next to the <strong>Filter by ISO properties</strong> box.</li><li>In the <strong>Select Properties</strong> dialog, click the <strong>Value</strong> box of a property and select the desired property value from the list.<br /><br /><ac:image><ri:attachment ri:filename="filtering_by_iso _properties1.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image><br /><br /></li><li>Click <strong>OK</strong>.</li></ol><p>Now the <strong>List</strong> tab displays the elements with the selected property value.</p><p><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro></li></ol><p>After assigning an Accident Scenario to a Hazardous Event, the Automotive Safety Integrity Level (ASIL) is calculated automatically.</p><p><br /></p><p>Assigning Hazards</p><hr /><ol><li>In a HARA Table, double-click the cell of the <strong>Hazard</strong> column and click <ac:image ac:thumbnail="true" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image>.</li><li>On the left side of the <strong>Select Element</strong> dialog, open the <strong>List</strong> tab.</li><li>Double-click the Hazards you want to assign. The elements should be added to the selected elements area.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To assign an Effect</p><hr /><ol><li>In a HARA Table, double-click the cell of the column representing the group of Effects (<strong>Vehicle Level Effects</strong> or <strong>System Level Effects</strong>) you want to assign an click <ac:image ac:thumbnail="true" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image>.</li><li>On the left side of the <strong>Select Element</strong> dialog, open the <strong>List</strong> tab.</li><li>Double-click the Effects you want to assign. The elements should be added to the selected elements area.</li><li>Click <strong>OK</strong>.</li></ol><p><br /></p><p>To create and assign Safety Goal</p><hr /><ol><li>In a HARA Table, double-click the cell of the <strong>Safety Goal</strong> column and click <ac:image ac:thumbnail="true" ac:height="11"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image>.</li><li>In the <strong>Select Elements</strong> dialog, enable the <strong>Creation Mode</strong> if it is not enabled yet.</li><li>In the element tree on the left side of the dialog, select the owner of a Safety Goal and click the <strong>Create</strong> button.</li><li><p class="auto-cursor-target">When the Specification window of the created element opens, enter the element name and close the Specification window. The element is created and automatically added to the selected elements area on the right side of the <strong>Select Elements</strong> dialog.<br /><br /><ac:image><ri:attachment ri:filename="creating_safety_goal.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ri:attachment></ac:image><br /><br /></p></li><li><p class="auto-cursor-target"><span style="color: rgb(62,63,64);">Click </span><strong>OK</strong><span style="color: rgb(62,63,64);"> to close the </span><strong>Select Elements</strong><span style="color: rgb(62,63,64);"> dialog.</span></p></li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466565 space=CSRA2024xR1 version=1 -->
## PAGE 00040: Hazards Table

- page_id: `170466565`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466565/Hazards+Table
- version_number: 1
- version_date: `2023-10-18T09:32:24.363+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Enable the Expert mode

116205869

#### CONTENT-COLUMN: Enable the Expert mode

116205881

116205868

**On this page**

4

#### CONTENT-BLOCK: Enable the Expert mode

116205870

A Hazards Table allows you to define and manage potential sources of harm that have an effect on something or someone under certain conditions at work. Essentially, the Hazards table acts as a library for the functional safety analysis.

[IMAGE alt='' src='']

###### An example of a Hazards Table.

##### Creating Hazards Table

You can create a Hazards Table as described below.

To create a Hazards Table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select Hazards Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select **Create Diagram** and select **Hazards Table** in the open dialog. 
 
[IMAGE alt='' src=''] Enable the Expert modeTo be able to create a Hazards Table, you need to enable the Expert mode.
3. When the table is created, type the name of the table and press Enter.

After following the above steps, a Hazards Table is created. The scope and element type of the table are already specified for you.

##### Creating Hazards

There are two ways to create a Hazard: you can do it right in a Hazards Table or in the Containment tree.

To create a Hazard in the Containment tree

1. In the Containment tree, right-click the owner of a new element and select Create Element .
2. In the open window, select Hazard . [ATTACHMENT filename='creating_hazards.png']
3. When a Hazard is created, type the name of the element and press Enter.

To create a Hazard in a Hazards Table

1. In a Hazards Table, select a table row.
2. Do one of the following:
  - In the table toolbar, click Add Sibling to create an element of the same level as the one you have selected.
  - In the table toolbar, click **Add Nested** to create an element nested under the selected element.
3. Type the name of the new element and press Enter.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="cfed2d43-ee3b-41e6-9118-3940e075ab34"><ac:parameter ac:name="id">116205869</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="cdf1a779-ee0d-44fc-a207-3074d5543cdf"><ac:parameter ac:name="id">116205881</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c9775d16-3d89-4b6d-91d1-6e4440af736b"><ac:parameter ac:name="id">116205868</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="12512df7-f8f8-4aef-bc05-0e2976a378eb"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="158069d1-92c1-4d07-9611-749793f57679"><ac:parameter ac:name="id">116205870</ac:parameter><ac:rich-text-body><p>A Hazards Table allows you to define and manage potential sources of harm that have an effect on something or someone under certain conditions at work. Essentially, the Hazards table acts as a library for the functional safety analysis.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="hazards_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Hazards Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of a Hazards Table.</h6><h3>Creating Hazards Table</h3><p>You can create a Hazards Table as described below.</p><p><br /></p><p>To create a Hazards Table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>Hazards Table</strong> in the open dialog.</li><li><p class="auto-cursor-target">In the Containment tree, right-click the owner of the table, select <strong>Create Diagram</strong> and select <strong>Hazards Table</strong> in the open <ac:inline-comment-marker ac:ref="7944cf89-5e5a-4384-8cef-1948ec8cc642">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="creating_hazards_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Hazards Table" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="849d9500-a22b-4872-853b-45687e139068"><ac:parameter ac:name="title">Enable the Expert mode</ac:parameter><ac:rich-text-body><p>To be able to create a Hazards Table, you need to enable the Expert mode.</p></ac:rich-text-body></ac:structured-macro></li></ul></li><li>When the table is created, type the name of the table and press Enter.</li></ol><p><br /><span style="color: rgb(62,63,64);">After following the above steps, a Hazards Table is created. The scope and element type of the table are already specified for you.</span></p><h3><span style="color: rgb(62,63,64);"><br />Creating Hazards</span></h3><p>There are two ways to create a Hazard: you can do it right in a Hazards Table or in the Containment tree.</p><p><br /></p><p>To create a Hazard in the Containment tree</p><hr /><ol><li>In the Containment tree, right-click the owner of a new element and select <strong>Create Element</strong>.</li><li>In the open window, select <strong>Hazard</strong>.<br /><br /><ac:image><ri:attachment ri:filename="creating_hazards.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Hazards Table" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">When a Hazard is created, type the name of the element and press Enter.</span></li></ol><p><span style="color: rgb(62,63,64);"><br /></span></p><p><span style="color: rgb(62,63,64);">To create a Hazard in a Hazards Table</span></p><hr /><ol><li>In a Hazards Table, select a table <ac:inline-comment-marker ac:ref="0bb2e8a1-40a5-49e6-bec2-ad512bcd9e99">row.</ac:inline-comment-marker></li><li>Do one of the following:<br /><ul><li>In the table toolbar, click <strong>Add Sibling</strong> to create an element of the same level as the one you have selected.</li><li><p class="auto-cursor-target">In the table toolbar, click <strong>Add Nested</strong> to create an element nested under the selected element.</p></li></ul></li><li>Type the name of the new element and press Enter.</li></ol><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466520 space=CSRA2024xR1 version=1 -->
## PAGE 00041: HazOp Table

- page_id: `170466520`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466520/HazOp+Table
- version_number: 1
- version_date: `2019-10-30T06:03:09.472+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Adding additional Malfunctioning Behavior

415732011

#### CONTENT-COLUMN: Adding additional Malfunctioning Behavior

100.00002%

415732025

415732009

**On this page**

4

#### CONTENT-BLOCK: Adding additional Malfunctioning Behavior

415732015

A HazOp Table allows you to perform hazards and operability analysis which is a common hazard analysis method for complex systems. In the HazOp Table, you can identify the Malfunctioning Behaviors for each function of your system.

[IMAGE alt='' src='']

###### An example of a HazOp Table.

##### Creating a HazOp Table

You can create a HazOp table as described below.

#### NOTE: Supported element types

Supported element types

To create a HazOp Table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select HazOp Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select Create Diagram and select HazOp Table in the open dialog. 
 
[IMAGE alt='' src='']
3. Type the name of the table and press Enter.
4. To specify the scope of the table, drag the Package containing system functions from the Containment tree to the Scope box.
5. To specify the type of your system functions, drag any system function from the Containment tree to the Element Type box.

After you create a HazOp Table with the system functions displayed in it, you can start creating Malfunctioning Behaviors, as described in the section below.

##### Creating Malfunctioning Behaviors

There are two ways to create Malfunctioning Behaviors:

- Create Malfunctioning Behaviors in the Containment tree and add them to a HazOp Table.
- Create Malfunctioning Behaviors right in a HazOp Table.

#### NOTE: Identifying Malfunctioning Behaviors

Identifying Malfunctioning Behaviors

To help identify Malfunctioning Behaviors in a HazOp Table, you can use eight predefined table columns (guide words): More, Less, Unintended, Late, Early, Inverted, Late, and No.

To create a Malfunctioning Behavior in the Containment tree

1. In the Containment tree , right-click the owner of a new element and select Create Element .
2. In the open window, select Malfunctioning Behavior . [ATTACHMENT filename='creating_malfunctioning_behavior.png']
3. Type the name of the element and press Enter .
4. To assign the Malfunctioning Behavior to a system function, drag it from the Containment tree to the desired cell of the HazOp Table. 
 
[IMAGE alt='' src='']

To create a Malfunctioning Behavior in a HazOp Table

1. In a HazOp Table, double-click the cell for which you want to create a Malfunctioning Behavior and click [ATTACHMENT filename='edit_button.png'] .
2. In the Select Elements dialog, enable the Creation Mode if it is not enabled yet.
3. In the element tree on the left side of the dialog, select the owner of a new element and click the Create button.
4. When the Specification window of the created element opens, enter the element name and close the Specification window. The element is created and automatically added to the selected elements area on the right side of the **Select Elements** dialog. 
 
[IMAGE alt='' src=''] Adding additional Malfunctioning BehaviorTo add an additional Malfunctioning Behavior to the related table cell, double-click that element in the element tree on the left side of the **Select Elements** dialog. To find the element quicker, go to the **List** tab displaying the list of all the Malfunctioning Behaviors of your model.
5. Click OK to close the Select Elements dialog.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a4cf6a7f-3712-4d39-a131-f44a5d82044d"><ac:parameter ac:name="id">415732011</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fe91e5ba-6655-4af0-80c0-c338af174828"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">415732025</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="edcb4711-a19d-41db-963e-d2bf873e80f9"><ac:parameter ac:name="id">415732009</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3d7234a4-622a-4432-8b91-7296a2cab3c1"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="bf5e0760-0e97-42cb-8e21-1dc8a16b0369"><ac:parameter ac:name="id">415732015</ac:parameter><ac:rich-text-body><p>A HazOp Table allows you to perform hazards and operability analysis which is a common hazard analysis method for complex systems. In the HazOp Table, you can identify the Malfunctioning Behaviors <span style="color: rgb(62,63,64);">for each function of your <ac:inline-comment-marker ac:ref="16cdbe47-d409-4fcd-a59e-3c33e4af2786">system</ac:inline-comment-marker></span>.</p><p style="text-align: center;"><br /><ac:image><ri:attachment ri:filename="hazop_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HazOp Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of a HazOp Table.</h6><h3>Creating a HazOp Table</h3><p><ac:inline-comment-marker ac:ref="e232d58a-cde3-455d-bfcf-b2e38e6c0445">You can create a HazOp table as described <ac:inline-comment-marker ac:ref="01446728-2ace-4286-ac20-49e7c3e358fe">below</ac:inline-comment-marker>.</ac:inline-comment-marker></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="394dd61d-170b-4113-ab8c-c03a74dece75"><ac:parameter ac:name="title">Supported element types</ac:parameter><ac:rich-text-body>A HazOp table supports three element types: Activity, Use Case, and Class. If you want to use a different system function type, you can extend the default type list by using <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Customizations" /><ac:plain-text-link-body><![CDATA[customization]]></ac:plain-text-link-body></ac:link>.</ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create a HazOp Table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>HazOp Table</strong> in the open dialog.</li><li><ac:inline-comment-marker ac:ref="92cbf40b-ef49-46ca-b498-7ccdb24202ff">In the Containment tree, right-click the owner of the table, select </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="92cbf40b-ef49-46ca-b498-7ccdb24202ff">Create Diagram</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="92cbf40b-ef49-46ca-b498-7ccdb24202ff"> and select </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="92cbf40b-ef49-46ca-b498-7ccdb24202ff">HazOp Table</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="92cbf40b-ef49-46ca-b498-7ccdb24202ff"> in the open <ac:inline-comment-marker ac:ref="3bc4190f-9588-4c7d-a16c-8cf42a4eb734">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="creating_hazop_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HazOp Table" /></ri:attachment></ac:image><br /><br /></ac:inline-comment-marker></li></ul></li><li><ac:inline-comment-marker ac:ref="e8f56fae-865c-4c2b-959d-fb77cdd72079">Type the name of the table and press Enter.</ac:inline-comment-marker></li><li>To specify the scope of the table, drag the Package containing system functions from the Containment tree to the <strong>Scope</strong> box.</li><li>To specify the type of your system functions, drag any system function from the Containment tree to the <strong>Element Type</strong> box.</li></ol><p><br />After you create a HazOp Table with the system functions displayed in it, you can start creating Malfunctioning Behaviors, as described in the section below.</p><h3><br />Creating Malfunctioning Behaviors</h3><p>There are two ways to create Malfunctioning Behaviors:</p><ul><li>Create Malfunctioning Behaviors in the Containment tree and add them to a <ac:inline-comment-marker ac:ref="0ea5cfcd-cc84-47fe-bcb5-ac9988dd4c03">HazOp</ac:inline-comment-marker> Table.</li><li>Create Malfunctioning Behaviors right in a HazOp Table.<br /><br /></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="478413ef-22b8-4d6d-8d13-f00febfec9de"><ac:parameter ac:name="title">Identifying Malfunctioning Behaviors</ac:parameter><ac:rich-text-body>To help identify Malfunctioning Behaviors in a HazOp Table, you can use eight predefined table columns (guide words): More, Less, Unintended, Late, Early, Inverted, Late, and No.</ac:rich-text-body></ac:structured-macro><p><ac:inline-comment-marker ac:ref="d8ca1e86-dad3-4390-9bc6-4014646620d0"><br /></ac:inline-comment-marker></p><p><ac:inline-comment-marker ac:ref="d8ca1e86-dad3-4390-9bc6-4014646620d0">To create a Malfunctioning Behavior in the Containment tree</ac:inline-comment-marker></p><hr /><ol><li>In the <ac:inline-comment-marker ac:ref="abaebc35-9ab4-4246-9028-42b4a85c3717">Containment tree</ac:inline-comment-marker>, right-click the owner of a new element and select <strong style="letter-spacing: 0.0px;">Create Element</strong>.</li><li>In the open window, select <strong>Malfunctioning Behavior</strong>.<br /><br /><ac:image><ri:attachment ri:filename="creating_malfunctioning_behavior.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HazOp Table" /></ri:attachment></ac:image><br /><br /></li><li><ac:inline-comment-marker ac:ref="15b529b0-5db7-43c3-9e76-6a988ab2aad9">Type the name of the element and press Enter</ac:inline-comment-marker>.</li><li><ac:inline-comment-marker ac:ref="16791fbe-8fc6-4aa7-9170-df2f96d5ff74">To assign the Malfunctioning Behavior to a system function, drag it from the Containment tree to the desired cell of the HazOp Table.<br /><br /><ac:image><ri:attachment ri:filename="adding_elements_to_hazop_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HazOp Table" /></ri:attachment></ac:image></ac:inline-comment-marker></li></ol><p><br /><br /></p><p>To create a Malfunctioning Behavior in a HazOp Table</p><hr /><ol><li>In a HazOp Table, double-click the cell for which you want to create a Malfunctioning Behavior and click <ac:image ac:height="11" ac:thumbnail="true"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image>.</li><li>In the <strong>Select Elements</strong> dialog, enable the <strong>Creation Mode</strong> if it is not enabled yet.</li><li>In the element tree on the left side of the dialog, select the owner of a new element and click the <strong>Create</strong> button.</li><li><p class="auto-cursor-target">When the Specification window of the created element opens, enter the element name and close the Specification window. The element is created and automatically added to the selected elements area on the right side of the <strong>Select Elements</strong> dialog.<br /><br /><ac:image><ri:attachment ri:filename="creating_malfunctioning_behavior_in_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HazOp Table" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="34780f0c-067a-4fe6-9530-6e6f5b3e8ed5"><ac:parameter ac:name="title">Adding additional Malfunctioning Behavior</ac:parameter><ac:rich-text-body><p>To add an additional Malfunctioning Behavior to the related table cell, double-click that element in the element tree on the left side of the <strong>Select Elements</strong> <ac:inline-comment-marker ac:ref="1ce13bb2-e545-4d32-bf3e-9aed6334db01">dialog</ac:inline-comment-marker>. To find the element quicker, go to the <strong>List</strong> tab displaying the list of all the Malfunctioning Behaviors of your model.</p></ac:rich-text-body></ac:structured-macro></li><li>Click <strong>OK</strong> to close the <strong>Select Elements</strong> dialog.</li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466604 space=CSRA2024xR1 version=1 -->
## PAGE 00042: Incompatible Types

- page_id: `170466604`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466604/Incompatible+Types
- version_number: 1
- version_date: `2020-02-04T11:40:52.130+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Validation Rules
- labels: []

### NORMALIZED CONTENT

**Constrained Element:** Operational Situation, Situation

**Constrained Element Filter**: Base Classifier is Typical Automotive Situation or Hazardous Event for Operational Situation; Base Classifier is Accident Scenario or Hazardous Event for Situation

**Severity:** error

**Error Message:** The types of [column name] for [failing element name] are not compatible with the types of [column name] for [incompatible element name].

**Abbreviation:** IncmptblType

**Solver:**Change the types of[column name]to be compatible with[incompatible element name].

**Description:** ISO 26262 elements (Operational Situation, Accident Scenario, and Hazardous Event) fail if they have properties with incompatible types in a hierarchy.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Constrained Element:</strong> Operational Situation, Situation</p><p><strong>Constrained Element Filter</strong>: Base Classifier is Typical Automotive Situation or Hazardous Event for Operational Situation; Base Classifier is Accident Scenario or Hazardous Event for Situation</p><p><strong>Severity:</strong> error</p><p><strong>Error Message:</strong> The types of <span class="error">[column name]</span> for <span class="error">[failing element name]</span> are not compatible with the types of <span class="error">[column name]</span> for <span class="error">[incompatible element name]</span>.</p><p><strong>Abbreviation:</strong> IncmptblType</p><p><strong>Solver: </strong><span style="letter-spacing: 0.0px;">Change the types of </span><span class="error" style="letter-spacing: 0.0px;">[column name]</span><span style="letter-spacing: 0.0px;"> to be compatible with </span><span class="error" style="letter-spacing: 0.0px;">[incompatible element name].</span></p><p><strong>Description:</strong> <ac:inline-comment-marker ac:ref="982e557d-678c-4dcc-9e83-580d93d904b4">ISO 26262</ac:inline-comment-marker> elements (Operational Situation, Accident Scenario, and Hazardous Event) fail if they have properties with incompatible types in a hierarchy.</p>
````

<!--NOMAGIC_PAGE id=170466605 space=CSRA2024xR1 version=1 -->
## PAGE 00043: Independence Requirement and DeriveReqt Relationships

- page_id: `170466605`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466605/Independence+Requirement+and+DeriveReqt+Relationships
- version_number: 1
- version_date: `2020-03-09T13:49:30.919+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Validation Rules
- labels: []

### NORMALIZED CONTENT

**Constrained Element:** Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement

**Constrained Element Filter:** Safety Requirements that have outgoing DeriveReqt and Independence Requirement relationships

**Severity:** error

**Error Message:** The ASIL value is incorrect due to Independence Requirement and DeriveReqt relationships.

**Abbreviation:** IndpDrv

**Description:** Safety Requirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement) fail when the highest ASIL value defined by outgoing DeriveReqt relationships is not equal to the ASIL value defined by an outgoing Independence Requirement relationship.

[IMAGE alt='' src='']

###### Illustration of the Independence Requirement and DeriveReqt Relationships validation rule.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><strong style="letter-spacing: 0.0px;">Constrained Element:</strong> Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement</p><p><strong>Constrained Element Filter:</strong> Safety Requirements that have outgoing DeriveReqt and Independence Requirement relationships</p><p><strong>Severity:</strong> error</p><p><strong>Error Message:</strong> The ASIL value is incorrect due to Independence Requirement and DeriveReqt relationships.</p><p><strong>Abbreviation:</strong> IndpDrv</p><p><strong>Description:</strong> Safety Requirements (Functional Safety Requirement, Technical Safety Requirement, Hardware Safety Requirement, Software Safety Requirement) fail when the highest ASIL value defined by outgoing DeriveReqt relationships is not equal to the ASIL value defined by an outgoing Independence Requirement relationship.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Independence_Requirement_and_DeriveReqt_Relationships_validation_ rule.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Independence Requirement and DeriveReqt Relationships" /></ri:attachment></ac:image></p><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">Illustration of the Independence Requirement and DeriveReqt Relationships validation rule.</span></h6><p><br /></p>
````

<!--NOMAGIC_PAGE id=170466457 space=CSRA2024xR1 version=2 -->
## PAGE 00044: Installation, licensing, and system requirements

- page_id: `170466457`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466457/Installation+licensing+and+system+requirements
- version_number: 2
- version_date: `2024-05-08T14:01:15.268+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Software requirements

571578853

#### CONTENT-COLUMN: Software requirements

571578855

#### CONTENT-BLOCK: Software requirements

571578854

#### NOTE: Software requirements

Software requirements

To install and use the Cameo Safety and Reliability Analyzer Plugin, the following plugins must be installed in your modeling tool:

- [CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR1']
- [CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024xR1']
- [CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA2024xR1']

For information regarding installation, licensing, and system requirements, visit the [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024xR1'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="53b9e87c-4fe2-4454-ad35-478bc401b97e"><ac:parameter ac:name="id">571578853</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="51500371-0a94-434f-bece-e000e6fabdfd"><ac:parameter ac:name="id">571578855</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="66c9b269-d843-423f-80af-fd812bf0a2d0"><ac:parameter ac:name="id">571578854</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="cf5f9e56-8cc7-4000-9e40-6cba2f223d04"><ac:parameter ac:name="title">Software requirements</ac:parameter><ac:rich-text-body><p>To install and use the Cameo Safety and Reliability Analyzer Plugin, the following plugins must be installed in your modeling tool:</p><ul><li><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML Plugin]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024xR1" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Requirements Modeler Plugin]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cameo Safety and Reliability Analyzer" /><ac:plain-text-link-body><![CDATA[Cameo Safety and Reliability Analyzer Plugin]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><p class="with-breadcrumbs">For information regarding installation, licensing, and system requirements, visit the <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installation, licensing, and system requirements" /></ac:link> page.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466456 space=CSRA2024xR1 version=1 -->
## PAGE 00045: Introduction to Cameo Safety and Reliability Analyzer

- page_id: `170466456`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466456/Introduction+to+Cameo+Safety+and+Reliability+Analyzer
- version_number: 1
- version_date: `2024-01-31T08:18:31.307+01:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

Cameo Safety and Reliability Analyzer[CONFLUENCE_PAGE title='Cameo Safety and Reliability Analyzer' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="b7fc252d-d10d-4009-aa98-ec678d796b3b"><ac:parameter ac:name="page">Cameo Safety and Reliability Analyzer</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Cameo Safety and Reliability Analyzer" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170466641 space=CSRA2024xR1 version=1 -->
## PAGE 00046: ISO 21434 Functional Cybersecurity

- page_id: `170466641`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466641/ISO+21434+Functional+Cybersecurity
- version_number: 1
- version_date: `2023-08-25T07:53:48.152+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

Cybersecurity engineering is a critical discipline to ensure safe and secure human experiences using cyber physical systems. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events.

Systems Cybersecurity Designer allows you to identify assets to be protected, threats and attacks to be tackled, and cybersecurity requirements to mitigate identified risks. The Systems Cybersecurity Designer supports the[ISO/SAE 21434 standard](https://www.iso.org/standard/70918.html). Itenables a proactive and continuous security assessment in the initial design phase to reduce product development cost and time. Systems cybersecurity designers are able to create a Threat Analysis and Risk Assessment (TARA) project template to comply with the ISO/SAE 21434:2021.

The****ISO/SAE 21434:2021 standard specifies engineering requirements for cybersecurity risk management regarding the Concept, Product development, Production, Operations, and maintenance and decommissioning of electrical and electronic (E/E) systems in road vehicles. This standard includes the integral components and interfaces of the road vehicles. A framework includes requirements for cybersecurity processes and a common language for communicating and managing cybersecurity risk. It is applicable to electrical and electronic (E/E) systems of production road vehicles whose development or modification began after the publication of ISO/SAE 21434:2021. ISO/SAE 21434:2021 does not prescribe specific technology or solutions related to cybersecurity.

The Systems Cybersecurity Designerallows a cybersecurity designer to:

- Design a safe and secure system through a built-in scalable cyber system model, which includes assets, weaknesses, threats, attack paths, and security requirements.
- Perform continuous threat assessment and hazard analyses to enhance design through real world scenarios.
- Support certification needs with consistent safety and cybersecurity compliance views.

The Systems Cybersecurity Designerdirectly covers the following parts of the standard:

**9. Concept**

This chapter specifies the item with its cybersecurity goals and claims. It is composed of cybersecurity requirements and the operational environment requirements of an item.

**15. Threat analysis and risk assessment methods**

This chapter specifies the methods to determine the extent to which a threat scenario can impact a road user. These methods and their work products are known as Threat Analysis and Risk Assessment (TARA) and are performed from the viewpoint of affected road users. The TARA steps are generic modules that can be invoked systematically from any point in the lifecycle of an item or component.

[IMAGE alt='' src='']

###### Overview of ISO/SAE 21434:2021 standard

#### NOTE: Prerequisites

Prerequisites

To install and use the Systems Cybersecurity Designer, ensure that one of the following modeling tools is installed:

- Magic Cyber Systems Engineer
- Magic Cyber Systems of Systems Architect
- Cameo Systems Modeler - Architect Edition
- Cameo Systems Modeler - Enterprise Edition
- Cameo Enterprise Architecture
- Magic Draw (any version) with SysML plugin installed

To learn more about how to download the installation files, refer [CONFLUENCE_PAGE title='Downloading installation files' space='NMDOC'].

To install and use the Systems Cybersecurity Designer, ensure that the following plugins are installed in your modeling tool:

- Cameo Safety and Reliability Analyzer
- ISO 26262 plugin

The cybersecurity plugin is compliant to [RAAML standard](https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML).

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cybersecurity engineering is a critical discipline to <span style="color: rgb(62,63,64);">ensure safe and secure human experiences using cyber physical systems</span>. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events.</p><p>Systems Cybersecurity Designer <span style="color: rgb(62,63,64);">allows you to identify assets to be protected, threats and attacks to be tackled, and cybersecurity requirements to mitigate identified risks</span>. <span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="5aa9f7b7-f09d-4e88-9c6c-564d4e1ae5e3">The <ac:inline-comment-marker ac:ref="aa078253-f98a-42c8-851b-60551bb5183d">Systems Cybersecurity</ac:inline-comment-marker> Designer supports t</ac:inline-comment-marker>he<a href="https://www.iso.org/standard/70918.html"> ISO/SAE 21434 standard</a>. It </span>enables a proactive and continuous security assessment in the initial design phase to reduce product development cost and time. Systems cybersecurity designers are able to create a Threat Analysis and Risk Assessment (TARA) project template to comply with the ISO/SAE 21434:2021.</p><p>The<strong> </strong>ISO/SAE 21434:2021 standard specifies engineering requirements for cybersecurity risk management regarding the Concept, Product development, Production, Operations, and maintenance and decommissioning of electrical and electronic (E/E) systems in road vehicles. This standard includes the integral components and interfaces of the road vehicles. A framework includes requirements for cybersecurity processes and a common language for communicating and managing cybersecurity risk. It is applicable to electrical and electronic (E/E) systems of production road vehicles whose development or modification began after the publication of ISO/SAE 21434:2021. ISO/SAE 21434:2021 does not prescribe specific technology or solutions related to cybersecurity.</p><p>The <ac:inline-comment-marker ac:ref="895e8af4-0a2f-4aea-b5ef-49e70b4ac1ec">Systems</ac:inline-comment-marker> <span style="color: rgb(62,63,64);">Cybersecurity Designer </span>allows a cybersecurity designer to:</p><ul><li>Design a safe and secure system through a built-in scalable cyber system model, which includes assets, weaknesses, threats, attack paths, and security requirements.</li><li>Perform continuous threat assessment and hazard analyses to enhance design through real world scenarios.</li><li>Support certification needs with consistent safety and cybersecurity compliance views.</li></ul><p>The Systems <span style="color: rgb(62,63,64);">Cybersecurity Designer </span>directly covers the following parts of the standard:</p><p><strong>9. Concept</strong> </p><p>This chapter specifies the item with its cybersecurity goals and claims. It is composed of cybersecurity requirements and the operational environment requirements of an item.</p><p><strong>15. Threat analysis and risk assessment methods</strong></p><p>This chapter specifies the methods to determine the extent to which a threat scenario can impact a road user. These methods and their work products are known as Threat Analysis and Risk Assessment (TARA) and are performed from the viewpoint of affected road users. The TARA steps are generic modules that can be invoked systematically from any point in the lifecycle of an item or component.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="ISOFramework.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 21434 Functional Cybersecurity" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Overview of ISO/SAE 21434:2021 standard</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6f459f96-4d19-47a8-8187-d08bea2c157e"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">To install and use the Sy<ac:inline-comment-marker ac:ref="5a62dbbe-3f21-4ffe-a890-35f81a113da1">stem</ac:inline-comment-marker>s Cybersecurity Designer, ensure that one of the following modeling tools is installed:</span></p><ul><li><p>Magic Cyber Systems Engineer</p></li><li><p>Magic Cyber Systems of Systems Architect</p></li><li><p>Cameo Systems Modeler - Architect Edition</p></li><li><p>Cameo Systems Modeler - Enterprise Edition</p></li><li><p><ac:inline-comment-marker ac:ref="61d83bad-579d-4a05-86ed-b4075f1788b9">Cameo Enterprise Architecture</ac:inline-comment-marker></p></li><li><ac:inline-comment-marker ac:ref="61d83bad-579d-4a05-86ed-b4075f1788b9"><span style="color: rgb(62,63,64);">Magic Draw (any version) with SysML plugin installed</span></ac:inline-comment-marker></li></ul><p>To learn more about how to download the installation files, refer <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Downloading installation files" /></ac:link>.</p><p><span style="color: rgb(62,63,64);">To install and use the Sy<ac:inline-comment-marker ac:ref="5b0a6940-6649-4125-b4e0-a03cb02cd91f">stems</ac:inline-comment-marker> Cybersecurity Designer, ensure that the following plugins are installed in your modeling tool:</span></p><ul><li>Cameo Safety and Reliability Analyzer</li><li>ISO 26262 plugin</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e9fbfa8c-d2e1-4821-998e-868b1d97f93e"><ac:rich-text-body><p>The cybersecurity plugin is compliant to <a href="https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML">RAAML standard</a>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170466651 space=CSRA2024xR1 version=1 -->
## PAGE 00047: ISO 21434 project

- page_id: `170466651`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466651/ISO+21434+project
- version_number: 1
- version_date: `2024-02-23T16:56:36.826+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity
- labels: []

### NORMALIZED CONTENT

3

##### Creating ISO 21434 project

To create a new ISO 21434 project

1. Do one of the following:
  - From the File menu, select New Project from the drop-down list. [IMAGE alt='' src='']
  - Click Create New Project on the welcome screen. [ATTACHMENT filename='Create New Project_Command.png']
  - Press Ctrl + Shift + N.
2. In the New Project dialog, select **ISO 21434 Project.** 
[IMAGE alt='' src='']
3. Specify the file name in the Name box.
4. Click the[IMAGE alt='' src='']button to select the location to store the project in a folder.
5. Select the checkbox to automatically create a folder for the project in the specified location.
6. Click **OK**.

A new ISO 21434 project is displayed with the default packages in the Containment tree and the Index.

Required libraries and profiles are loaded while opening the project. If required plugins are not installed, the following Message dialog will appear: 
 
[IMAGE alt='' src='']

##### ISO 21434 Project Template

A default ISO 21434 project template is displayed once you open the project. This template is provided to help you initiate the process.

**Containment Tree**

The Containment tree displays the default packages. One package, one table, and one element of each type are provided in the Containment tree. You can add, modify or delete any element or package from the Containment tree.

**Index**

The Index displays the default tables and information related to it. It also displays other elements, such as Operational Conditions, Operation Situations, etc., at the bottom. You can navigate to the tables and elements by clicking the icons. Only the default tables and elements are displayed in the Index. The Index will not display any table or element created later.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:macro-id="46c4561c-0f22-492b-8293-80bfb1550691" ac:name="toc" ac:schema-version="1"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating ISO 21434 project</h3><p>To create a new ISO 21434 project</p><hr /><ol><li>Do one of the following:<ul><li class="atl-forced-newline">From the<span> </span><strong>File</strong><span> </span>menu, select <strong>New Project </strong>from the drop-down list.<br /><em><br /><ac:image><ri:attachment ri:filename="New Project_command.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 21434 project" /></ri:attachment></ac:image><br /><br /></em></li><li>Click <strong>Create New Project </strong>on the welcome screen.<br /><br /><ac:image><ri:attachment ri:filename="Create New Project_Command.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 21434 project" /></ri:attachment></ac:image><br /><br /></li><li>Press Ctrl + Shift + N.</li></ul></li><li><p class="auto-cursor-target">In the New Project dialog, select <strong>ISO 21434 Project.<br /></strong><br /><ac:image><ri:attachment ri:filename="New Project_Window.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 21434 project" /></ri:attachment></ac:image><br /><br /></p></li><li><p class="auto-cursor-target">Specify the file name in the Name box.</p></li><li><p class="auto-cursor-target"><span style="color: rgb(62,63,64);">Click the</span><span style="color: rgb(62,63,64);"><span> <ac:image><ri:attachment ri:filename="Three Dot Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 21434 project" /></ri:attachment></ac:image> </span>button to select the location to store the project in a folder.</span></p></li><li><p class="auto-cursor-target">Select the checkbox to automatically create a folder for the project in the specified location.</p></li><li><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li></ol><p>A new ISO 21434 project is displayed with the default packages in the Containment tree and the Index.</p><ac:structured-macro ac:macro-id="df13aefb-d300-4916-8e58-5927a3285c35" ac:name="note" ac:schema-version="1"><ac:rich-text-body><p>Required libraries and profiles are loaded while opening the project. If required plugins are not installed, <ac:inline-comment-marker ac:ref="3104bf7f-9aeb-412a-8d92-79623c88ba4c">the following Message dialog will appear</ac:inline-comment-marker>:<br /><br /><ac:image><ri:attachment ri:filename="Notification_Missing Plugin.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 21434 project" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">ISO 21434 Project Template</h3><p>A default ISO 21434 project template is displayed once you open the project. This template is provided to help you initiate the process.</p><p><strong>Containment Tree</strong></p><p>The Containment tree displays the default packages. One package, one table, and one element of each type are provided in the Containment tree. You can add, modify or delete any element or package from the Containment tree.</p><p><strong>Index</strong></p><p>The Index displays the default tables and information related to it. It also displays other elements, such as Operational Conditions, Operation Situations, etc., <ac:inline-comment-marker ac:ref="2524d519-a457-4cd3-aa8d-3b00de1cee79">at the bottom</ac:inline-comment-marker>. You can navigate to the tables and elements by <ac:inline-comment-marker ac:ref="e3889777-fca1-4399-926c-39b8be2b8e53">clicking the icons</ac:inline-comment-marker>. Only the default tables and elements are displayed in the Index. The Index will not display any table or element created later.</p><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="Index.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 21434 project" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466516 space=CSRA2024xR1 version=1 -->
## PAGE 00048: ISO 26262 Functional Safety

- page_id: `170466516`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466516/ISO+26262+Functional+Safety
- version_number: 1
- version_date: `2021-10-28T05:27:34.969+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

The ISO 26262 Functional Safety Plugin supports the ISO 26262 standard which is intended for electric and/or electronic systems in production vehicles. This includes driver assistance, propulsion, and vehicle dynamics control systems. The goal of ISO 26262 is to ensure safety throughout the lifecycle of automotive systems and equipment.

The International Organization for Standardization (ISO) put forth ISO 26262 for road vehicle functional safety. The standard was created to help avoid the risk of systematic failures and random hardware failures through feasible requirements and processes. ISO 26262 is a risk-based safety standard that’s derived from IEC 61508. The standard is comprised of 10 parts that span the breadth of the automotive safety lifecycle including management, development, production, operation service and decommissioning.

The ISO 26262 Functional Safety plugin directlycoversthe following parts of the standard:

**3-7 Hazard analysis and Risk assessment** 
Exposes all hazards and determines the risk involved. A safety goal with an assigned Automotive Safety Integrity Level (ASIL) is the result of performing Hazard Analysis and Risk Assessment (HARA).

**3-8 Functional Safety Concept** 
The Functional Safety Concept encompasses functional implementation of independent requirements on the safety of an item. It refines safety goals by defining safety goals attributes and establishes the link between functional safety requirements and the preliminary architecture.

[IMAGE alt='' src='']

###### The ISO 26262 standard structure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The ISO 26262 Functional Safety Plugin supports the ISO 26262 standard which is intended for electric and/or electronic systems in production vehicles. This includes driver assistance, propulsion, and vehicle dynamics control systems. The goal of ISO 26262 is to ensure safety throughout the lifecycle of automotive systems and equipment.</p><p>The International Organization for Standardization (ISO) put forth ISO 26262 for road vehicle functional safety. The standard was created to help avoid the risk of systematic failures and random hardware failures through feasible requirements and processes. ISO 26262 is a risk-based safety standard that’s derived from IEC 61508. The standard is comprised of 10 parts that span the breadth of the automotive safety lifecycle including management, development, production, operation service and decommissioning.</p><p><ac:inline-comment-marker ac:ref="06c9aa75-afbd-411e-996b-85bf6ad6bb2b">The ISO 26262 Functional Safety plugin directly </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="a89cefa3-781b-4c1c-90de-74097b32a43e"><ac:inline-comment-marker ac:ref="06c9aa75-afbd-411e-996b-85bf6ad6bb2b">covers</ac:inline-comment-marker></ac:inline-comment-marker><ac:inline-comment-marker ac:ref="06c9aa75-afbd-411e-996b-85bf6ad6bb2b"> the following parts of the standard:</ac:inline-comment-marker></p><p><strong>3-7 Hazard analysis and Risk assessment</strong><br />Exposes all hazards and determines the risk involved. A safety goal with an assigned Automotive Safety Integrity Level (ASIL) is the result of performing Hazard Analysis and Risk Assessment (HARA).</p><p><strong>3-8 Functional Safety Concept</strong><br />The Functional Safety Concept encompasses functional implementation of independent requirements on the safety of an item. It refines safety goals by defining safety goals attributes and establishes the link between functional safety requirements and the preliminary architecture.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="ISO26262_structure.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="ISO 26262 Functional Safety" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The ISO 26262 standard structure.</h6>
````

<!--NOMAGIC_PAGE id=170466662 space=CSRA2024xR1 version=1 -->
## PAGE 00049: Item

- page_id: `170466662`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466662/Item
- version_number: 1
- version_date: `2024-04-18T09:17:41.285+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

3

**Item**

Component or set of components that implements a function at the vehicle level.

**Item Block**

An Item Block is a part of the system that needs to be assessed with a TARA process. An Item Block is a SysML Block.

**Members**

Elements that are within the item block.

**Boundary Members**

Elements and/or ports that connect the item with other elements.

##### Creating an Item

To create an Item

1. In the Containment tree, right-click Items & Assets Definition and select Create Element. [IMAGE alt='' src='']
2. Do one of the following:
  - I n the dialog, expand **ISO 21434**and select **Single Block Item.** [ATTACHMENT filename='Single Block Item.png']
  - In the search tab, type the keyword item and then select Single Block Item. [ATTACHMENT filename='Create Item_Search.png']
3. Name the created Item in the Containment tree. The Item has the prefix IT , which denotes that the created element is an Item; the number 1 indicates that it is the first Item created. [ATTACHMENT filename='1 ContainmentTreeAEBS.png']

After creating an asset, it is beneficial to find its location in the model tree by performing one of the following:

- Right-click the asset, and, from the shortcut menu, choose the Select in Containment Tree command.
- Select the asset and press Alt+B.

##### Creating an Item Table

If you create a new project using the**ISO 21434 Project**template, then an **Item Table**already exists in the **2.1 Items & Assets Definition** package.

To create an Item Table

1. In the Containment tree, right-click Items & Assets Definition and select Create Diagram. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Item Table.** [IMAGE alt='' src='']
  - In the search tab, type the keyword item and then select Item Table. 
 
[IMAGE alt='' src=''] The Item Table is now displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='1 ContainmentTreeItemsTable.png']

##### Adding an Item to the Item Table

To add a new Item to the Item Table

1. In the Item Table, click Add New. A row is added to the Item table, which shows the new Item. [IMAGE alt='' src='']
2. In the newly created Item's row and in the Name column, double-click the designated cell to name the Item. [ATTACHMENT filename='2 AfterAddingAEBSasItem.png']

To add an existing Item in the Item Table

1. In the Item Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the Select Single Block Item dialog, select the required Item. A row is added to the Item table, which shows the existing Item. [ATTACHMENT filename='4 SelectSingleItemBlockWindow_v2.png']
3. In the existing Item's row and in the Name column, double-click the designated cell to rename the Item. [ATTACHMENT filename='5 AfterAddingExistingHeadlampAsItem.png']

##### Assigning SysML Block as an Item Block

To assign SysML Block as an Item Block

- Double-click the designated cell in the Item's row and the Item Block column . I n the drop-down list, select the Item Block. [ATTACHMENT filename='2 DoubleClickItemBlockCell_v2.png'] The added Item Block is now displayed in the Item Table. [ATTACHMENT filename='5 AfterAssigningAnItemBlock.png']

- You can also drag and drop the SysML Block from the Containment tree to the Item Table.
- Once you declare a SysML Block as an Item Block, a legend appears at the top left corner of the element. [ATTACHMENT filename='Item_Legend.png']

##### Item Table Example

In an Item Table, **Members**and **Boundary** **Members**columns are automatically filled based on the Item Block definition.

[IMAGE alt='' src='']

#### INFO: References

References

- ISO/SAE 21434:2021 Road vehicles-Cybersecurity engineering

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="aa162ffa-f4d7-4293-b409-6496bc4c160e"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Item</strong></p><p>Component or set of components that implements a function at the vehicle level.</p><p><strong>Item Block</strong></p><p>An Item Block is a part of the system that needs to be assessed with a TARA process. <span style="letter-spacing: 0.0px;">An Item Block is a SysML Block.</span></p><p><strong>Members</strong></p><p>Elements that are within the item block.</p><p><strong>Boundary Members</strong></p><p>Elements and/or ports that connect the item with other elements.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="4d7400a9-4746-4fc9-b733-09d729e7585d">Creating an Item</ac:inline-comment-marker></h3><p>To create an Item</p><hr /><ol><li>In the Containment tree, right-click <strong>Items &amp; Assets Definition </strong>and select<strong> Create Element.</strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Create Element.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">Do one of the following:<ul><li class="auto-cursor-target"><span style="color: rgb(62,63,64);">I</span><span style="color: rgb(62,63,64);">n the dialog, expand <strong>ISO 21434 </strong>and select <strong>Single Block Item.</strong></span><strong><br /><br /></strong><ac:image><ri:attachment ri:filename="Single Block Item.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></li><li class="auto-cursor-target">In the search tab, type the keyword item and then select <strong>Single Block Item.<br /></strong><br /><ac:image ac:thumbnail="true" ac:height="187"><ri:attachment ri:filename="Create Item_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></li></ul></li><li class="auto-cursor-target">Name the created Item in the Containment tree. The Item has the prefix <strong>IT</strong>, which denotes that the created element is an Item; the number <strong>1</strong> indicates that it is the first Item created.<br /><br /><ac:image><ri:attachment ri:filename="1 ContainmentTreeAEBS.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="500928e5-b5aa-4deb-9f12-f5f3dccc4ed1"><ac:rich-text-body><p><span style="color: rgb(51,51,51);">After creating an asset, it is beneficial to find its location in the model tree by performing one of the following:</span></p><ul><li><span style="color: rgb(51,51,51);">Right-click the asset, and, from the shortcut menu, choose the<span> </span></span><strong>Select in Containment Tree</strong><span style="color: rgb(51,51,51);"><span> </span>command.</span></li><li><span style="color: rgb(51,51,51);">Select the asset and press Alt+B.</span></li></ul></ac:rich-text-body></ac:structured-macro><h3>Creating an Item Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b731e3bf-11d8-4757-a15e-afa992b85247"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project </strong>template<span style="color: rgb(23,43,77);">, then an <strong>Item Table </strong>already exists in the <strong>2.1 Items &amp; Assets Definition</strong> package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:inline-comment-marker ac:ref="799bf929-1740-4ea7-a937-3f76c0165a6e">To create an Item Table</ac:inline-comment-marker></p><hr /><ol><li>In the Containment tree, right-click <strong>Items &amp; Assets Definition </strong>and select<strong> Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram_Containment tree.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /></strong><strong><br /></strong></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Item Table.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Item Table_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword item and then select <strong>Item Table.<br /><br /><ac:image><ri:attachment ri:filename="Item Table_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></strong>The Item Table is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="1 ContainmentTreeItemsTable.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image></li></ul></li></ol><h3>Adding an Item to the Item Table</h3><p>To add a new Item to the Item Table</p><hr /><ol><li>In the Item Table, click <strong>Add New. </strong>A row is added to the Item table, which shows the new Item.<strong><br /><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></strong></li><li> In the newly created Item's row and in the <strong>Name </strong>column, double-click the designated cell to name the Item.<br /><br /><ac:image><ri:attachment ri:filename="2 AfterAddingAEBSasItem.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></li></ol><p>To add an existing Item in the Item Table</p><hr /><ol><li>In the Item Table, click <strong>Add Existing.<br /><br /><ac:image ac:height="194"><ri:attachment ri:filename="3 ClickAddExisting.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></strong></li><li>From the <strong>Select Single Block Item</strong><strong> </strong>dialog, select the required Item. A row is added to the Item table, which shows the existing Item.<br /><br /><ac:image><ri:attachment ri:filename="4 SelectSingleItemBlockWindow_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br /></li><li>In the existing Item's row and in the <strong>Name </strong>column, double-click the designated cell to rename the Item.<br /><br /><ac:image><ri:attachment ri:filename="5 AfterAddingExistingHeadlampAsItem.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image></li></ol><h3>Assigning SysML Block as an Item Block</h3><p>To assign SysML Block as an Item Block</p><hr /><ul><li>Double-click the designated cell in the Item's row and the <strong>Item Block column</strong>. I<span style="color: rgb(62,63,64);">n the drop-down list, select the Item Block.</span><br /><br /><ac:image><ri:attachment ri:filename="2 DoubleClickItemBlockCell_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image><br /><br />The added Item Block is now displayed in the Item Table.<br /><br /><ac:image><ri:attachment ri:filename="5 AfterAssigningAnItemBlock.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8954b67c-823f-4ac9-9998-8f53065b77ae"><ac:rich-text-body><ul><li>You can also drag and drop the SysML Block from the Containment tree to the Item Table.</li><li>Once you declare a SysML Block as an Item Block, a legend appears at the top left corner of the element.<br /><br /><ac:image><ri:attachment ri:filename="Item_Legend.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><h3>Item Table Example</h3><p><span style="color: rgb(62,63,64);">In an Item Table, <strong>Members </strong>and <strong>Boundary</strong> <strong>Members </strong>columns are automatically filled based on the Item Block definition.</span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="5 AfterAssigningAnItemBlock.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Item" /></ri:attachment></ac:image></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ecb29b23-9bba-4d3c-b9c0-8d100bee465f"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a href="https://www.iso.org/obp/ui/fr/#iso:std:iso-sae:21434:ed-1:v1:en">ISO/SAE 21434:2021 Road vehicles-Cybersecurity engineering</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170467113 space=CSRA2024xR1 version=1 -->
## PAGE 00050: Libraries

- page_id: `170467113`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170467113/Libraries
- version_number: 1
- version_date: `2024-03-25T11:22:41.095+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

You can import multiple libraries in the Systems Cybersecurity Designer plugin instead of creating elements. All imported libraries are treated as used projects in your current project.

##### Adding a library to the project

To add a library to the project

- In the Containment tree, right-click Model> Security and then select the required library. [ATTACHMENT filename='Add Library.png']

If you click on any element in the library, you will be redirected to the web page of the respective element.

##### MITRE CWE Library

The addition of the MITRE CWE Library adds a package to the Containment tree. The MITRE CWE Librarycontains two sub-packages: Common Weakness Enumeration and Functional Cybersecurity Requirements. The Common Weakness Enumeration package contains a list of weaknesses. Each weakness contains a hyperlink that redirects you to the CWE definition web page. The Functional Cybersecurity Requirements package contains the requirements to mitigate the weakness. These requirements are segregated with the help of sub-packages based on the type of requirement.

###### [IMAGE alt='' src='']MITRE Library present in the Containment tree.

##### MITRE ATT&CK EnterpriseTechnique Library

The addition of MITRE ATT&CK Enterprise Technique Library adds two packages to the Containment tree: MITRE ATT&CK Enterprise Technique Library and MITRE ATT&CK Platforms Library. The MITRE ATT&CK Enterprise Technique Library package contains sub-packages which contain enterprise mitigation, tactics and techniques. The MITRE ATT&CK Platforms Library contains the platforms through which the attacks can take place.

[IMAGE alt='' src='']

###### MITRE ATT&CK Enterprise Technique Library present in the Containment tree.

##### MITRE ATT&CK ICSTechnique Library

The addition of MITRE ATT&CK ICS Technique Library adds a package to the Containment tree. The MITRE ATT&CK ICS Technique Library package contains sub-packages which contain ICS mitigation, tactics and techniques.

[IMAGE alt='' src='']

###### MITRE ATT&CK ICSTechnique Library present in the Containment tree.

##### NIST Control Library

The addition of the NIST Control Library adds a package to the Containment tree. The NIST Control Library package contains a sub-package that lists the cyber security requirements.[IMAGE alt='' src='']

###### NIST Control Library present in the Containment tree.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can import multiple libraries in the Systems Cybersecurity Designer plugin instead of creating elements. All imported libraries are treated as used projects in your current project. </p><h3>Adding a library to the project</h3><p>To add a library to the project </p><hr /><ul><li>In the Containment tree, right-click <strong>Model&gt; Security </strong>and then select the required library.<br /><br /><ac:image><ri:attachment ri:filename="Add Library.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Libraries" /></ri:attachment></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="28d0d24c-3743-4be7-85c9-4bf6856b9cdd"><ac:rich-text-body><p>If you click on any element in the library, you will be redirected to the web page of the respective element.</p></ac:rich-text-body></ac:structured-macro><h3>MITRE CWE Library</h3><p><span style="color: rgb(62,63,64);">The addition of the MITRE CWE Library <span style="color: rgb(23,43,77);">adds a package to the Containment tree. The <span style="color: rgb(62,63,64);">MITRE CWE Library </span></span>contains two sub-packages: Common Weakness Enumeration and Functional Cybersecurity Requirements.  The Common Weakness Enumeration package contains a list of weaknesses. Each weakness contains a hyperlink that redirects you to the CWE definition web page. The Functional Cybersecurity Requirements package contains the requirements to mitigate the weakness. These requirements are segregated with the help of sub-packages based on the type of requirement.</span></p><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="MITRE CWE Library.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Libraries" /></ri:attachment></ac:image>MITRE Library present in the Containment tree.</h6><h3><span style="color: rgb(23,43,77);">MITRE ATT&amp;CK Enterprise </span><span style="color: rgb(23,43,77);">Technique Library</span></h3><p><span style="color: rgb(23,43,77);">The addition of MITRE ATT&amp;CK Enterprise Technique Library adds two packages to the Containment tree: MITRE ATT&amp;CK Enterprise Technique Library and MITRE ATT&amp;CK Platforms Library. The MITRE ATT&amp;CK Enterprise Technique Library package contains sub-packages which contain enterprise mitigation, tactics and techniques. The MITRE ATT&amp;CK Platforms Library contains the platforms through which the attacks can take place.<br /><br /></span></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="Enterprise_Library.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Libraries" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">MITRE ATT&amp;CK Enterprise Technique Library present in the Containment tree.</h6><h3><span style="color: rgb(23,43,77);">MITRE ATT&amp;CK ICS </span><span style="color: rgb(23,43,77);">Technique Library</span></h3><p><span style="color: rgb(23,43,77);">The addition of MITRE ATT&amp;CK ICS Technique Library adds a package to the Containment tree. The MITRE ATT&amp;CK ICS Technique Library package contains sub-packages which contain ICS mitigation, tactics and techniques.<br /><br /></span></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="ICS_Library.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Libraries" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">MITRE ATT&amp;CK ICSTechnique Library present in the Containment tree.</h6><h3><span style="color: rgb(23,43,77);">NIST Control Library</span></h3><p style="text-align: left;"><span style="color: rgb(23,43,77);">The addition of the NIST Control Library adds a package to the Containment tree. The NIST Control Library package contains a sub-package that lists the c</span><span style="color: rgb(23,43,77);">yber security requirements.<br /></span><span style="color: rgb(23,43,77);"><br /><ac:image ac:align="center"><ri:attachment ri:filename="NIST Library.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Libraries" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">NIST Control Library present in the Containment tree.</h6>
````

<!--NOMAGIC_PAGE id=170466490 space=CSRA2024xR1 version=2 -->
## PAGE 00051: Linking Failure Modes to model elements

- page_id: `170466490`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466490/Linking+Failure+Modes+to+model+elements
- version_number: 2
- version_date: `2024-05-08T14:01:16.023+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Additional features
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Removing links

949945905

#### CONTENT-COLUMN: Removing links

949945907

949945903

**On this page**

4

#### CONTENT-BLOCK: Removing links

949945906

The Cameo Safety and Reliability Analyzer plugin allows you to link Failure Modes to model elements in any stage of the modeling process. This enables you to foresee any possible element-related Failure Modes and add them to your model before starting actual safety and reliability analysis. Failure Modes can be linked to the following model elements:

- Actions
- Blocks
- Part Properties
- Requirements
- Operations
- Activities

You can link Failure Modes in the following ways:

- [CONFLUENCE_PAGE title='Linking Failure Modes to model elements' space='CSRA2024xR1'] (recommended).
- Specify the **Failure Modes** property in the Specification window of an element[CONFLUENCE_PAGE title='Linking Failure Modes to model elements' space='CSRA2024xR1'] .

##### linking_in_diagramLinking Failure Modes to elements in a diagram

The easiest way to link a Failure Mode to a model element is to drag it from the containment tree in the model browser to the desired element shape in a diagram.

To link a Failure Mode to an element in a diagram

1. Open the diagram displaying the element you want to link.
2. In the model browser, locate the desired Failure Mode, and drag it directly to the element shape.

Dragging a Failure Mode to an element shape specifies the Failure Mode as the value of the **Failure Modes** property of that element. In addition, the **Failure Modes** property is automatically displayed in the compartment of the element shape to which the Failure Mode was dragged, as shown in the figure below.

[IMAGE alt='' src='']

###### In this Activity Diagram, the *Read sensor value* and *Control insulin delivery* Actions are linked to the *Drop in sensitivity* and *Voltage error* Failure Modes.

#### TIP: Usability tip

Usability tip

An element can be linked to multiple Failure Modes. You can either select multiple Failure Modes and drag them to the element shape all at once, or drag the Failure Modes one by one. The element shape is then updated and displays all linked Failure Modes.

##### linking_in_specificationLinking Failure Modes to elements in the Specification window

Linking a Failure Mode to a model element specifies it as the property value of that element. This link can be defined in the Specification window of the element, as described below.

To link a Failure Mode to an element in the Specification window

1. Open the [CONFLUENCE_PAGE title='Specification window' space='MD2024xR1'] of the element you want to link.
2. In the Properties drop-down box, select the All property display mode, if it is not already selected.
3. In the property specification area, select the **Failure Modes** property specification cell, and click [IMAGE alt='' src=''].
4. In the **Select Elements** dialog, select the Failure Mode(s) you want to link to the element.
5. Click [IMAGE alt='' src=''] to add the selected Failure Mode(s) to the **Selected elements** area. If you want to add all Failure Modes contained in a specific Package, select a Package and click [IMAGE alt='' src='']. Removing linksIf an an element already has a Failure Mode linked to it, you can use the **Select Elements** dialog to remove the link:In the **Selected elements** area, select the Failure Mode(s) the link(s) to which you want to remove.Click [IMAGE alt='' src='']. If you want to remove the links to all the Failure Modes shown in the **Selected elements** area, click [IMAGE alt='' src=''].Click **OK**, and close the Specification window.
6. Click OK .
7. Close the Specification window.

After following the steps described above, the selected Failure Modes are specified as the values of the **Failure Modes** property of the desired element. In addition, the **Failure Modes** property is automatically displayed on the element shape if that element is displayed in a diagram.

949982653

**Related pages**

- [CONFLUENCE_PAGE title='Additional features' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Traceability maps' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Safety and Reliability Coverage Analysis' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Generating reports' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5d981c14-7f89-4ff6-b83f-42acecfed563"><ac:parameter ac:name="id">949945905</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="217c59f8-49ef-4332-adc7-49a144f99c42"><ac:parameter ac:name="id">949945907</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5770051c-4d86-48e2-b22e-d3a51abb75bb"><ac:parameter ac:name="id">949945903</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="45d0a1a4-26fc-4af6-bcd9-e725f7613a46"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="78c446bc-7535-4a9a-885b-d8a1fecb94a0"><ac:parameter ac:name="id">949945906</ac:parameter><ac:rich-text-body><p>The Cameo Safety and Reliability Analyzer plugin allows you to link Failure Modes to model elements in any stage of the modeling process. This enables you to foresee any possible element-related Failure Modes and add them to your model before starting actual safety and reliability analysis. Failure Modes can be linked to the following model elements:</p><ul><li>Actions</li><li>Blocks</li><li>Part Properties</li><li>Requirements</li><li>Operations</li><li>Activities</li></ul><p>You can link Failure Modes in the following ways:</p><ul><li><ac:link ac:anchor="linking_in_diagram"><ac:plain-text-link-body><![CDATA[Drag Failure Modes to an element shape in a diagram]]></ac:plain-text-link-body><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ac:link> (recommended).</li><li><ac:link ac:anchor="linking_in_specification"><ac:link-body>Specify the <strong>Failure Modes</strong> property in the Specification window of an element</ac:link-body><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ac:link>.</li></ul><h3><br /><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="e01b5787-93c4-4de2-bf73-80db9ca83227"><ac:parameter ac:name="">linking_in_diagram</ac:parameter></ac:structured-macro>Linking Failure Modes to elements in a diagram</h3><p>The easiest way to link a Failure Mode to a model element is to drag it from the containment tree in the model browser to the desired element shape in a diagram.</p><p><br />To link a Failure Mode to an element in a diagram</p><hr /><ol><li><ac:inline-comment-marker ac:ref="ecdc48d1-fed5-4f8d-9331-c448efb8bf28">Open the diagram displaying the element you want to link.</ac:inline-comment-marker></li><li>In the model browser, locate the desired Failure Mode, and drag it directly to the element shape.</li></ol><p><br />Dragging a Failure Mode to an element shape specifies the Failure Mode as the value of the <strong>Failure Modes</strong> property of that element. In addition, the <strong>Failure Modes</strong> property is automatically displayed <ac:inline-comment-marker ac:ref="a03ffbfe-d831-4e63-8716-ba61b0b488f5">in the compartment of the element shape</ac:inline-comment-marker> to which the Failure Mode was dragged, as shown in the figure below.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="activity_diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ri:attachment></ac:image></p><h6 style="text-align: center;">In this Activity Diagram, the <em>Read sensor value</em> and <em>Control insulin delivery</em> Actions are linked to the <em>Drop in sensitivity</em> and <em>Voltage error</em> Failure Modes.</h6><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="cca08189-c9f3-42bd-9322-ae97304d381a"><ac:parameter ac:name="title">Usability tip</ac:parameter><ac:rich-text-body><p>An element can be linked to multiple Failure Modes. You can either select multiple Failure Modes and drag them to the element shape all at once, or drag the Failure Modes one by one. The element shape is then updated and displays all linked Failure Modes.</p></ac:rich-text-body></ac:structured-macro><h3><br /><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="e8420653-ab15-4014-a152-b1a1b51839c1"><ac:parameter ac:name="">linking_in_specification</ac:parameter></ac:structured-macro>Linking Failure Modes to elements in the Specification window</h3><p>Linking a Failure Mode to a model element specifies it as the property value of that element. This link can be defined in the Specification window of the element, as described below.</p><p><br />To link a Failure Mode to an element in the Specification window</p><hr /><ol><li>Open the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specification window" /></ac:link> of the element you want to link.</li><li>In the <strong>Properties</strong> drop-down box, select the <strong>All</strong> property display mode, if it is not already selected.</li><li><p class="auto-cursor-target">In the property specification area, select the <strong>Failure Modes</strong> property specification cell, and click <ac:image ac:title="Edit" ac:alt="Edit"><ri:attachment ri:filename="edit_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ri:attachment></ac:image>.</p></li><li><p class="auto-cursor-target">In the <strong>Select Elements</strong> dialog, select the Failure Mode(s) you want to link to the element.</p></li><li><p class="auto-cursor-target">Click <ac:image ac:title="Add" ac:alt="Add"><ri:attachment ri:filename="add_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ri:attachment></ac:image> to add the selected Failure Mode(s) to the <strong>Selected elements</strong> area. If you want to add all Failure Modes contained in a specific Package, select a Package and click <ac:image ac:title="Add Recursively" ac:alt="Add Recursively"><ri:attachment ri:filename="add_recursively_button.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ri:attachment></ac:image>.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="25b2938f-b2d0-4c69-a488-a7b34120126d"><ac:parameter ac:name="title">Removing links</ac:parameter><ac:rich-text-body><p>If an an element already has a Failure Mode linked to it, you can use the <strong>Select Elements</strong> dialog to remove the link:</p><ol><li>In the <strong>Selected elements</strong> area, select the Failure Mode(s) the link(s) to which you want to remove.</li><li>Click <ac:image ac:title="Remove" ac:alt="Remove"><ri:attachment ri:filename="remove.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ri:attachment></ac:image>. If you want to remove the links to all the Failure Modes shown in the <strong>Selected elements</strong> area, click <ac:image ac:title="Remove All" ac:alt="Remove All"><ri:attachment ri:filename="remove_all.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ri:attachment></ac:image>.</li><li>Click <strong>OK</strong>, and close the Specification window.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Click <strong>OK</strong>.</li><li>Close the Specification window.</li></ol><p><br />After following the steps described above, the selected Failure Modes are specified as the values of the <strong>Failure Modes</strong> property of the desired element. In addition, the <strong>Failure Modes</strong> property is automatically displayed on the element shape if that element is displayed in a diagram.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a4d89db4-c3df-4960-a419-c05530d4d0d6"><ac:parameter ac:name="id">949982653</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Additional features" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety and Reliability Coverage Analysis" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generating reports" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466934 space=CSRA2024xR1 version=1 -->
## PAGE 00052: Manual Attack Path

- page_id: `170466934`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466934/Manual+Attack+Path
- version_number: 1
- version_date: `2024-04-29T07:47:11.518+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
- labels: []

### NORMALIZED CONTENT

3

**Attack Path**

Set of deliberate actions to realize a threat scenario.

**Attack Path Steps**

Enumerate each step needed to perform the threat scenario.

**Attack Feasibility Rating**

An attribute of an attack path describes the ease of successfully carrying out the corresponding set of actions. By default, the ISO/SAE 21434:2021 rating scale is used.

##### Creating a Manual Attack Path

A ManualAttack Path refers to the manual way of describing and rating the feasibility of attack paths. It does not refer to potential based attacks or CVSS methodologies.

To create a ManualAttack Path

1. In the Containment tree, right-click**Attack Paths and Feasibility Ratings**and select Create Element. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **ManualAttack Path**. [IMAGE alt='' src='']
  - In the search tab, type the keyword attack and then select **Manual** Attack Path. 
 
[IMAGE alt='' src='']
3. Name the created Manual Attack Path in the Containment tree and press Enter. The ManualAttack Path has the prefix **AP**,which denotes that the created element is a Manual Attack Path; the number**1** indicates that it is the first Manual Attack Path created. 
 
**[IMAGE alt='' src='']**

##### Creating a Manual Attack Path Table

If you create a new project using the**ISO 21434 Project**template, then a**Manual Attack Paths**tablealready exists in the**1.3 Attack Paths and Feasibility Ratings**package.

To create aManual Attack PathTable

1. In the Containment tree, right-click **Attack Paths and Feasibility Ratings** and select Create Diagram. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Manual Attack** **Path Table**. [IMAGE alt='' src='']
  - In the search tab, type the keyword attack and then select **Manual Attack Path** Table. 
 
[IMAGE alt='' src=''] The Manual Attack Table is displayed in the diagram pane of the modeling tool. [IMAGE alt='' src='']

##### Adding a Manual Attack Path to Manual Attack Path Table

To add a new Manual Attack Path to the Manual Attack Path Table

1. In the Manual Attack Path Table, click Add New. A row is added in the Manual Attack Path Table, which shows the new Manual Attack Path. [IMAGE alt='' src='']
2. In the newly created Manual Attack Path's row and the**Name**column, double-click the designated cell to name the Manual Attack Path. 
 
**[IMAGE alt='' src='']**

To add an existing Manual Attack Path to the Manual Attack Path Table

1. In the Manual Attack Path Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the **Select Attack Path** dialog, select the required Manual Attack Path. A row is added to the Manual Attack Path Table, which shows the existing Manual Attack Path. 
 
[IMAGE alt='' src='']
3. In the existing Manual Attack Path's row and the**Name**column, double-click the designated cell to rename the Manual Attack Path. 
 
**[IMAGE alt='' src='']**

##### Adding Attack Path Steps

To add Attack Path Steps to the Manual Attack Path Table

1. Double-click the designated cell in the **Attack Path Steps** column and the required Manual Attack Path's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Adding attack path_Three dot.png']
2. From the **Select Situation******dialog, select Attack Path Steps. 
 
[IMAGE alt='' src=''] 
 
The Attack Path Steps now shown in the Manual Attack Path Table. 
 
[IMAGE alt='' src='']

- You can also drag and drop the Attack Path Step from the Containment tree to the Threat Scenario Table.
- You can move the Attack Path Steps in the Select Situation dialog by clicking Up or Down . [ATTACHMENT filename='Movement of attack paths.png']

##### Adding an Attack Feasibility Rating

To rate the Attack Feasibility

- Double-click the cell in the Manual Attack Path's row and from the drop-down list, select Attack Feasibility Rating. 
 
[IMAGE alt='' src=''] 
 
The Attack Feasibility Rating is now shown in the Manual Attack Path Table. 
 
[IMAGE alt='' src='']

##### Manual Attack Path Table Example

[IMAGE alt='' src='']

#### INFO: References

References

[ISO/SAE 21434:2021 Road vehicles-Cybersecurity enginee](https://www.iso.org/obp/ui/fr/)r

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="39f05532-31d7-4667-8819-b22c5f860cf0"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Attack Path</strong></p><p>Set of deliberate actions to realize a threat scenario.</p><p><strong>Attack Path Steps</strong></p><p>Enumerate each step needed to perform the threat scenario.</p><p><strong>Attack Feasibility Rating</strong></p><p>An attribute of an attack path describes the ease of successfully carrying out the corresponding set of actions. By default, the ISO/SAE 21434:2021 rating scale is used.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Manual <span>Attack Path</span></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="33960afa-9338-4985-843d-537893e4b919"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">A <span style="color: rgb(23,43,77);">Manual </span>Attack Path refers to the manual way of describing and rating the feasibility of attack paths. It does not refer to potential based attacks or CVSS methodologies.</span></p></ac:rich-text-body></ac:structured-macro><p>To create a <span style="color: rgb(23,43,77);">Manual </span><span style="color: rgb(62,63,64);">Attack Path</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click<span> </span><strong>Attack Paths and Feasibility Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong><span style="color: rgb(23,43,77);">Manual </span>Attack Path</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Manual Attack Path_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong><span style="color: rgb(23,43,77);">Manual </span></strong></span><strong>Attack Path.<br /><br /><ac:image><ri:attachment ri:filename="Manual Attack Path_Menu_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Manual Attack Path in the Containment tree and press Enter. The <span style="color: rgb(23,43,77);">Manual </span>Attack Path has the prefix <span><strong><ac:inline-comment-marker ac:ref="36c001cf-dca2-40db-87f2-dd5774b62d1d">AP</ac:inline-comment-marker></strong>, </span>which denotes that the created element is a Manual Attack Path; the number<span> </span><strong style="text-align: left;">1</strong> indicates that it is the first Manual Attack Path created.<br /><br /><strong><ac:image><ri:attachment ri:filename="Containment Tree.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></strong><br /></span></li></ol><h3>Creating a Manual Attack Path Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ac3fdcfd-bb62-48d6-a13a-b462ed970031"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color: rgb(23,43,77);">, then a<span> </span><strong>Manual Attack Paths </strong>table<span> </span>already exists in the<span> <strong>1.3 Attack Paths and Feasibility Ratings</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:inline-comment-marker ac:ref="bc6650c9-7c62-42c5-8f4d-246e2a504771">To create a</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="bc6650c9-7c62-42c5-8f4d-246e2a504771"> Manual Attack Path </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="bc6650c9-7c62-42c5-8f4d-246e2a504771">Table</ac:inline-comment-marker></p><hr /><ol><li>In the Containment tree, right-click<span> <span style="color: rgb(62,63,64);"><strong>Attack Paths and Feasibility Ratings</strong></span></span><span style="color: rgb(62,63,64);"> </span>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Manual Attack</strong> <strong>Path Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Manual Attack Path Table_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong>Manual Attack Path </strong></span><strong>Table.<br /><br /><ac:image><ri:attachment ri:filename="Manual Attack Path Table_Menu_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong>The Manual Attack Table is displayed in the diagram pane of the modeling tool.<br /><br /><strong><ac:image><ri:attachment ri:filename="Manual Attack Path Table_Created.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></strong></li></ul></li></ol><h3>Adding a Manual Attack Path to Manual Attack Path Table</h3><p>To add a new Manual Attack Path to the Manual Attack Path Table</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Manual Attack Path Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add New. </strong><span style="color: rgb(62,63,64);">A row is added in the Manual Attack Path Table, which shows the new Manual Attack Path.</span><strong style="text-align: left;"><span style="color: rgb(62,63,64);"> </span><br /><br /><ac:image><ri:attachment ri:filename="Add New.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">In the newly created Manual Attack Path's row and the<span> </span><strong>Name<span> </span></strong>column, double-click the designated cell to name the Manual Attack Path.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="New added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></strong><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color: rgb(62,63,64);">To add an existing Manual Attack Path to the Manual Attack Path Table</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Manual Attack Path Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="Add Existing.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Attack Path</strong> dialog, select the required Manual Attack Path. A row is added to the Manual Attack Path Table, which shows the existing Manual Attack Path. <br /><br /><ac:image><ri:attachment ri:filename="Select Attack Path dialog box.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">In the existing Manual Attack Path's row and the<span> </span><strong style="text-align: left;">Name<span> </span></strong>column, double-click the designated cell to rename the Manual Attack Path.<br style="text-align: left;" /><br /><span style="color: rgb(62,63,64);"><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="New added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></strong></span><br style="text-align: left;" /></span></li></ol><h3>Adding Attack Path Steps</h3><p>To add Attack Path Steps to the Manual Attack Path Table</p><hr /><ol><li>Double-click the designated cell in the<span> <strong>Attack Path Steps </strong></span>column and the required Manual Attack Path's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Adding attack path_Three dot.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br /></li><li><p><span style="color: rgb(62,63,64);">From the <strong>Select Situation</strong><strong> </strong>dialog, <ac:inline-comment-marker ac:ref="0095b215-7b06-4c59-b208-bd489cf1c532">select Attack Path Steps.</ac:inline-comment-marker></span><br style="text-align: left;" /><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="Select Element Dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br style="text-align: left;" /><br style="text-align: left;" /><span style="color: rgb(62,63,64);">The Attack Path Steps now shown in the Manual Attack Path Table.<br /><br /><ac:image><ri:attachment ri:filename="Attack Path Steps added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /></span></p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a20036fc-d84f-496a-8521-30c4fd021e0b"><ac:rich-text-body><ul><li>You can also drag and drop the Attack Path Step from the Containment tree to the Threat Scenario Table.</li><li>You can move the Attack Path Steps in the <strong>Select Situation</strong><strong> </strong>dialog by clicking <strong>Up </strong>or <strong>Down</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Movement of attack paths.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(62,63,64);"> </span></p><h3>Adding an Attack Feasibility Rating</h3><p>To rate the Attack Feasibility</p><hr /><ul><li><span style="color: rgb(62,63,64);">Double-click the cell </span><span style="color: rgb(22,22,22);"><span>in the <ac:inline-comment-marker ac:ref="3cdd3203-a6de-44a0-ac78-27acd9233c8b">Manual Attack Path's </ac:inline-comment-marker></span></span><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="3cdd3203-a6de-44a0-ac78-27acd9233c8b">row</ac:inline-comment-marker> and from the drop-down list, select Attack Feasibility Rating.<br /><br /><ac:image><ri:attachment ri:filename="Attack Feasibility Rating_Selection.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image><br /><br style="text-align: left;" /><ac:inline-comment-marker ac:ref="1ad0fcee-334d-488f-af31-80b41680fef6">The Attack Feasibility</ac:inline-comment-marker> Rating is now shown in the Manual Attack Path Table.<br /><br /><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="Attack Feasibility Rating_Selected.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></span><br /></span></li></ul><h3><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="5e0c1889-ac92-4cf1-88fe-58a76a8a21b0">Manual Attack Path Table Example</ac:inline-comment-marker><br /><br /></span></h3><p><span style="color: rgb(62,63,64);"><ac:image><ri:attachment ri:filename="Example_Manual Attack Path.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Manual Attack Path" /></ri:attachment></ac:image></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="45a1ec35-b666-48f8-a3c3-7f8c169ccbc8"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><p><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO/SAE 21434:2021 Road vehicles-Cybersecurity enginee</a>r</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466527 space=CSRA2024xR1 version=1 -->
## PAGE 00053: Operational Conditions Table

- page_id: `170466527`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466527/Operational+Conditions+Table
- version_number: 1
- version_date: `2020-01-28T11:39:28.789+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Enable the Expert mode

2059861906

#### CONTENT-COLUMN: Enable the Expert mode

100.00002%

2059861917

2059861904

**On this page**

4

#### CONTENT-BLOCK: Enable the Expert mode

2059861907

An Operational Conditions Table allows you to define and manage various Operational Conditions that will be used as a part of an Operational Situation. Essentially, the Operational Conditions table acts as a library for functional safety analysis. To identify Operational Conditions, you can use five predefined Operational Condition groups: Location, Road Condition, Traffic and People, Vehicle Usage, and Environmental Condition. If you want to define an additional group, extend the group list by [CONFLUENCE_PAGE title='Extending ISO 26262 elements with new properties' space='CSRA2024xR1'].

[IMAGE alt='' src='']

###### An example of Operational Conditions Table.

##### **Creating an****Operational Conditions Table**

Create an Operational Conditions Table as described below.

To create an Operational Conditions Table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select Operational Conditions Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select **Create Diagram** and select **Operational Conditions Table** in the open dialog. 
 
[IMAGE alt='' src=''] Enable the Expert modeTo be able to create an Operational Conditions Table, you need to enable the Expert mode.
3. When the table is created, type the name of the table and press Enter.

After completing the above steps, an Operational Conditions Table with five predefined Operational Condition groups is created. The scope and element type of the table are already specified for you.

##### Creating Operational Conditions

There are two ways to create an Operational Condition: you can do it right in an Operational Conditions Table or in the Containment tree.

To create an Operational Condition in the Containment tree

1. In the Containment tree, right-click the owner of a new element and select Create Element .
2. In the open window, select the Operational Condition group ( Vehicle Usage , Traffic and People , Location , Road Condition , or Environmental Condition ) for which you want to create an Operational Condition. [ATTACHMENT filename='creating_operational_condition.png']
3. When an Operational Condition is created, type the name of the element and press Enter.

When you create an Operational Condition in the model browser, it is automatically added to an Operational Conditions Table if it exists.

To create an Operational Condition in an Operational Conditions Table

1. In an Operational Conditions Table, select the Operational Condition group ( Vehicle Usage , Traffic and People , Location , Road Condition , or Environmental Condition ) for which you want to create an Operational Condition or select an existing element in that group.
2. Do one of the following:
  - In the table toolbar, click [ATTACHMENT filename='add_sibling.png'] to create an element of the same level as the one you have selected.
  - In the table toolbar, click [IMAGE alt='' src=''] to create an element nested under the selected element.
3. Type the name of the new element and press Enter.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d8acfd83-ff7c-47f8-999b-e19814ee0f85"><ac:parameter ac:name="id">2059861906</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d3d60f40-2759-44df-aee0-9b4cf709e189"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">2059861917</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="635d0a64-b2cd-4c16-a9f3-a08c39fad675"><ac:parameter ac:name="id">2059861904</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="da509a8f-cbb4-4634-a5d7-9ecbfd763259"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="86a9689b-fcee-4364-af08-2ad593b1560d"><ac:parameter ac:name="id">2059861907</ac:parameter><ac:rich-text-body><p>An Operational Conditions Table allows you to define and manage various Operational Conditions that will be used as a part of an Operational Situation. Essentially, the Operational Conditions table acts as a library for functional safety analysis. To identify Operational Conditions, you can use five predefined Operational Condition groups: Location, Road Condition, Traffic and People, Vehicle Usage, and Environmental Condition. If you want to define an additional group, extend the <ac:inline-comment-marker ac:ref="dd4a6db1-3746-4e0f-97c0-59f6ad297563">group <ac:inline-comment-marker ac:ref="dea85688-63ab-4fc1-9424-5943e4b071e7">list</ac:inline-comment-marker></ac:inline-comment-marker> by <ac:inline-comment-marker ac:ref="3e0dfef6-7945-4805-9df8-d21efa138fa7"><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Extending ISO 26262 elements with new properties" /><ac:plain-text-link-body><![CDATA[extending the ISO 26262 library]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker>.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="operational_conditions_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Conditions Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of Operational Conditions Table.</h6><h3><strong>Creating an </strong><strong style="letter-spacing: 0.0px;">Operational Conditions Table</strong></h3><p>Create an Operational Conditions Table as described below.</p><p><br /></p><p>To create an Operational Conditions Table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>Operational Conditions Table</strong> in the open dialog.</li><li><p class="auto-cursor-target">In the Containment tree, right-click the owner of the table, select <strong>Create Diagram</strong> and select <strong>Operational Conditions Table</strong> in the open <ac:inline-comment-marker ac:ref="f7cf2a25-103c-4cf7-9e59-320ddb480bf8">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="creating_operational_conditions_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Conditions Table" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="849d9500-a22b-4872-853b-45687e139068"><ac:parameter ac:name="title">Enable the Expert mode</ac:parameter><ac:rich-text-body><p>To be able to create an Operational Conditions Table, you need to enable the Expert mode.</p></ac:rich-text-body></ac:structured-macro></li></ul></li><li>When the table is created, type the name of the table and press Enter.</li></ol><p><br />After completing the above steps, an Operational Conditions Table with five predefined Operational Condition groups is created. The scope and element type of the table are already specified for you.</p><h3><br />Creating Operational Conditions</h3><p><span style="color: rgb(62,63,64);">There are two ways to create an Operational Condition: you can do it right in an Operational Conditions Table or in the Containment tree.</span></p><p><br /></p><p>To create an Operational Condition in the Containment tree</p><hr /><ol><li>In the Containment tree, right-click the owner of a new element and select <strong>Create Element</strong>.</li><li>In the open window, select the Operational Condition group (<strong>Vehicle Usage</strong>, <strong>Traffic and People</strong>, <strong>Location</strong>, <strong>Road Condition</strong>, or <strong>Environmental Condition</strong>) for which you want to create an Operational Condition.<br /><br /><ac:image><ri:attachment ri:filename="creating_operational_condition.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Conditions Table" /></ri:attachment></ac:image><br /><br /></li><li>When an Operational Condition is created, type the name of the element and press Enter.</li></ol><p><br />When you create an Operational Condition in the model browser, it is automatically added to an Operational Conditions Table if it exists.</p><p><br /></p><p>To create an Operational Condition in an Operational Conditions Table</p><hr /><ol><li>In an Operational Conditions Table, select the Operational Condition group (<strong style="letter-spacing: 0.0px;">Vehicle Usage</strong><span style="letter-spacing: 0.0px;">, </span><strong style="letter-spacing: 0.0px;">Traffic and People</strong><span style="letter-spacing: 0.0px;">, </span><strong style="letter-spacing: 0.0px;">Location</strong><span style="letter-spacing: 0.0px;">, </span><strong style="letter-spacing: 0.0px;">Road Condition</strong><span style="letter-spacing: 0.0px;">, or </span><strong style="letter-spacing: 0.0px;">Environmental Condition</strong><span style="letter-spacing: 0.0px;">) for which you want to create an Operational Condition or select an existing element in that group.</span></li><li><ac:inline-comment-marker ac:ref="eca80890-c4a5-4aa4-a76d-f43f22652508">Do one of the following:</ac:inline-comment-marker><br /><ul><li>In the table toolbar, click <ac:image><ri:attachment ri:filename="add_sibling.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image> to create an element of the same level as the one you have selected.</li><li><p class="auto-cursor-target">In the table toolbar, click <ac:image><ri:attachment ri:filename="add_nested.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image> to create an element nested under the selected element.</p></li></ul></li><li>Type the name of the new element and press Enter.</li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466850 space=CSRA2024xR1 version=1 -->
## PAGE 00054: Operational Situation

- page_id: `170466850`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466850/Operational+Situation
- version_number: 1
- version_date: `2024-04-25T09:32:32.044+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Damage scenario
- labels: []

### NORMALIZED CONTENT

##### Creating an Operational Situation

To create an Operational Situation

1. In the Containment tree, right-click**Damage Scenario****and Impact Ratings**and select Create Element. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Operational Situation**. **[IMAGE alt='' src='']**
  - In the search tab, type the keyword operational and then select Operational Situation. 
 
**[IMAGE alt='' src='']**
3. Name the created Operational Situation in the Containment tree and press Enter. 
 
**[IMAGE alt='' src='']**

##### Adding Operational Situation to the Operational Situations Table

Using the Operational SituationsTable you can only add nested Operational Situations.

To add an Operational Situation

1. In the Operational SituationsTable, select an Operational Situationand then click Add Nested. A row is added in the Operational SituationsTable, which shows the nested Operational Situation. 
 
[IMAGE alt='' src='']
2. In the newly created Operational Situation'srow and the **Name**column, double-click the designated cell to name the Effect. 
 
[IMAGE alt='' src='']

##### Adding Operational Situation's parameters to the Operational Situations Table

To add Operational Situation's parameters to the Operational Situations Table

1. Double-click the designated cell in the**Vehicle Usage** column and the required Operational Situation's row and click [IMAGE alt='' src='']. 
 
[IMAGE alt='' src='']
2. From the **Select Elements******dialog, select the Vehicle Usage. 
 
[IMAGE alt='' src=''] 
 
The Vehicle Usage is added to the Operational Situations Table. 
 
[IMAGE alt='' src=''] 
 
All other Operational Situation parameters are added to the Operational Situations Table using the same procedure. 
 
[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="70fcfd66-8d5f-4095-8e17-03f0e7dfbb9c" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="84cf21db-815d-4ff0-9ede-465c908157bf">Creating an Operational Situation</ac:inline-comment-marker></h3><p>To create an Operational Situation</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click<span> <strong>Damage Scenario </strong></span><strong>and Impact Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Operational Situation</strong>.</span><br /><strong><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Operational Situation.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image></strong><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword operational and then select<span> </span><strong>Operational Situation.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Operational Situation_Search.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image></strong><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Operational Situation in the Containment tree and press Enter.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="4 OpSituationCreated.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image></strong></span></li></ol><h3 style="">Adding Operational Situation to the Operational Situations Table</h3><p style="">Using the <span style="letter-spacing: 0.0px;">Operational Situations </span><span style="letter-spacing: 0.0px;">Table you can only add nested <span style="">Operational Situations.</span></span></p><p style="">To add an <span style="letter-spacing: 0.0px;">Operational Situation</span></p><hr style="" /><ol style=""><li><span style="color: rgb(62,63,64);">In the <span style="">Operational Situations </span>Table, select an <span style="">Operational Situation </span>and then click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add Nested.<span> </span></strong><span style="color: rgb(62,63,64);">A row is added in the <span style="">Operational Situations </span>Table, which shows the nested <span style="">Operational Situation</span>.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Add Nested.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">In the newly created <span style="">Operational Situation's </span>row and the <strong style="text-align: left;">Name<span> </span></strong>column, double-click the designated cell to name the Effect.<br style="text-align: left;" /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image><br /></span></li></ol><h3><span style="color: rgb(62,63,64);">Adding Operational Situation's parameters to the Operational Situations Table</span></h3><p><span style="color: rgb(62,63,64);">To add Operational Situation's parameters to the Operational Situations Table</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">Double-click the designated cell in the<span> </span><strong>Vehicle Usage </strong></span><span style="color: rgb(62,63,64);">column and the required Operational Situation's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image></span></span>.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Parameters_Three Dot.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image><br /><br /></span></span></li><li><span style="color: rgb(62,63,64);"><span>From the <strong style="text-align: left;">Select Elements</strong><strong style="text-align: left;"> </strong>dialog, select the Vehicle Usage.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Select Elements dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image><br /><br />The Vehicle Usage is added to the Operational Situations Table.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Parameters_added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image><br /><br style="text-align: left;" />All other Operational Situation parameters are added to the Operational Situations Table using the same procedure.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Parameters_added_all.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situation" /></ri:attachment></ac:image><br /></span></span></li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466531 space=CSRA2024xR1 version=1 -->
## PAGE 00055: Operational Situations Table

- page_id: `170466531`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466531/Operational+Situations+Table
- version_number: 1
- version_date: `2023-06-26T06:33:39.847+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

2060987200

2060987204

2060987199

**On this page**

4

2060987203

An Operational Situations Table allows you to define and manage various Operational Situations as a combination of Operational Conditions. The sections below explain how to create Operational Situations and how to assign the Exposure level, along with various Operational Conditions.

[IMAGE alt='' src='']

###### An example of an Operational Situations Table.

##### Creating Operational Situations Table

You can create an Operational Situations Table as described below.

To create an Operational Situations table

1. In the Containment tree, select the element that you want to be the owner of the table.
2. Do one of the following:
  - In the main menu, go to Diagrams > Create Diagram , then select Operational Situations Table in the open dialog.
  - In the Containment tree, right-click the owner of the table, select Create Diagram, and select Operational Situations Table in the open dialog . [ATTACHMENT filename='creating_operational_situations_table.png']
3. When the table is created, type the name of the table and press Enter.

After following the above steps, an Operational Situations Table is created. The scope and element type of the table are already specified for you.

##### Creating Operational Situations

There are two ways to create an Operational Situation: you can do it right in an Operational Situations Table or in the Containment tree.

To create an Operational Situation in the Containment tree

1. In the Containment tree, right-click the owner of a new element and select Create Element .
2. In the open window, select Operational Situation . [ATTACHMENT filename='creating_operational_situation.png']
3. When an Operational Situation is created, type the name of the element and press Enter.

When you create an Operational Situation in the Containment tree, it is automatically added to an Operational Situations Table if it exists.

To create an Operational Situation in an Operational Situations Table

1. In an Operational Situations Table, select a table row .
2. Do one of the following:
  - In the table toolbar, click Add Sibling to create an element of the same level as the one you have selected. [ATTACHMENT filename='Add Sibling.png']
  - In the table toolbar, click **Add Nested**to create an element nested under the selected element. 
 
[IMAGE alt='' src='']
3. Type the name of the new element and press Enter.

When you create an Operational Situation and add it to an Operational Situations Table, you need to define the element as described below.

##### Defining Operational Situations

After creating an Operational Situation, you need to define its Exposure level which allows you to estimate the probability of the vehicle being in a hazardous or risky situation. Also, you need to specify the Operational Conditions associated with the Operational Situation.

To define an Exposure level

1. In an Operational Situations Table, double-click the cell of the Exposure column and select the desired exposure level from the list . [ATTACHMENT filename='defining_exposure_level.png']
2. Double-click the Justification of Exposure cell and write the justification explaining the selected E xposure level.

To assign Operational Conditions

1. Double-click the cell of the column representing the desired Operational Condition group and click [ATTACHMENT filename='Three Dot _Icon.png'] .
2. On the left side of the Select Elements dialog, open the List tab.
3. Double-click the Operational Conditions you want to assign. The elements should be added to the selected elements area on the right side of the dialog. [ATTACHMENT filename='specifying_operational_conditions.png']
4. Click OK .
5. Repeat the steps from 1 to 4 to assign the Operational Conditions of other groups.

You can also drag and drop the Operational Conditions from the Containment tree to the Operational Situations Table.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d241ec98-36da-468f-a1a1-5669198db404"><ac:parameter ac:name="id">2060987200</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="416e75ff-136a-4393-8abc-d3ee1605c940"><ac:parameter ac:name="id">2060987204</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cb3de681-b424-4eec-a68c-c0d61a42f402"><ac:parameter ac:name="id">2060987199</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="a732a85e-72a9-4958-96fa-a420ba81253b"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="55de395d-b71a-4989-87c3-97831171246d"><ac:parameter ac:name="id">2060987203</ac:parameter><ac:rich-text-body><p>An Operational Situations Table allows you to define and manage various Operational Situations as a combination of Operational Conditions. The sections below explain how to create Operational Situations and how to assign the Exposure level, along with various Operational Conditions.<br /><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="operational_situations_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image></p><h6 style="text-align: center;">An example of an Operational Situations Table.</h6><h3>Creating Operational Situations Table</h3><p>You can create an Operational Situations Table as described below.</p><p><br /></p><p>To create an Operational Situations table</p><hr /><ol><li>In the Containment tree, select the element that you want to be the owner of the table.</li><li>Do one of the following:<ul><li>In the main menu, go to <strong>Diagrams</strong> &gt; <strong>Create Diagram</strong>, then select <strong>Operational Situations Table</strong> in the open dialog.</li><li>In the Containment tree, right-click the owner of the table, select <strong>Create Diagram,</strong> and select <strong>Operational Situations Table</strong> in the open <ac:inline-comment-marker ac:ref="660a88e6-c3ec-419d-a5b0-3a5a06cd1067">dialog</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="creating_operational_situations_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image><br /><br /></li></ul></li><li>When the table is created, type the name of the table and press Enter.</li></ol><p><br /><span style="color: rgb(62,63,64);">After following the above steps, an Operational Situations Table is created. The scope and element type of the table are already specified for you.</span></p><h3>Creating Operational Situations</h3><p>There are two ways to create an Operational Situation: you can do it right in an Operational Situations Table or in the Containment tree.</p><p><br /></p><p>To create an Operational Situation in the Containment tree</p><hr /><ol><li>In the Containment tree, right-click the owner of a new element and select <strong>Create Element</strong>.</li><li>In the open window, select <strong>Operational </strong><strong>Situation</strong>.<br /><br /><ac:image><ri:attachment ri:filename="creating_operational_situation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image><br /><br /></li><li>When an Operational Situation is created, type the name of the element and press Enter.</li></ol><p><br />When you create an Operational Situation in the Containment tree, it is automatically added to an Operational Situations Table if it exists.</p><p><br /></p><p>To create an Operational Situation in an Operational Situations Table</p><hr /><ol><li>In an Operational Situations Table, select a table row<span>.</span></li><li>Do one of the following:<br /><ul><li>In the table toolbar, click <strong>Add Sibling </strong>to create an element of the same level as the one you have selected.<br /><br /><ac:image><ri:attachment ri:filename="Add Sibling.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">In the table toolbar, click <strong>Add Nested </strong>to create an element nested under the selected element.<br /><br /><ac:image><ri:attachment ri:filename="Add Nested.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image></p></li></ul></li><li>Type the name of the new element and press Enter.</li></ol><p><br />When you create an Operational Situation and add it to an Operational Situations Table, you need to define the element as described below.</p><h3>Defining Operational Situations</h3><p>After creating an Operational Situation, you need to define its Exposure level which allows you to estimate the probability of the vehicle being in a hazardous or risky situation. Also, you need to specify the Operational Conditions associated with the Operational Situation.</p><p><br /></p><p>To define an Exposure level</p><hr /><ol><li>In an Operational Situations Table, double-click the cell of the <strong>Exposure</strong> column and select the desired exposure level from the <ac:inline-comment-marker ac:ref="1ad418f6-9790-488c-8970-ee76eca114ed">list</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="defining_exposure_level.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image><br /><br /></li><li>Double-click the <strong>Justification of Exposure</strong> cell and write the justification explaining the selected E<ac:inline-comment-marker ac:ref="a81e244d-58af-47da-b72d-9985cb1f2683">xposure</ac:inline-comment-marker> level.</li></ol><p><br /></p><p><ac:inline-comment-marker ac:ref="38c93acb-7c8f-4a4f-86b6-af44052eaa28">To assign Operational Conditions</ac:inline-comment-marker></p><hr /><ol><li>Double-click the cell of the column representing the desired Operational Condition group and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image>.</li><li>On the left side of the <strong>Select Elements</strong> dialog, open the <strong>List</strong> tab.</li><li>Double-click the Operational Conditions you want to assign. The elements should be added to the selected elements area on the right side of the dialog.<br /><br /><ac:image><ri:attachment ri:filename="specifying_operational_conditions.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image><br /><br /></li><li>Click <strong>OK</strong>.</li><li>Repeat the steps from 1 to 4 to assign the Operational Conditions of other groups.</li></ol><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="633b1f87-efc8-4b67-8123-53812a5be5ce"><ac:rich-text-body><p>You can also drag and drop the Operational Conditions from the Containment tree to the Operational Situations Table.</p><p><ac:image><ri:attachment ri:filename="Operational Condition_Drag-Drop.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Operational Situations Table" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466460 space=CSRA2024xR1 version=1 -->
## PAGE 00056: Process description

- page_id: `170466460`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466460/Process+description
- version_number: 1
- version_date: `2018-06-04T03:50:52.073+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Getting started
- labels: []

### NORMALIZED CONTENT

948592443

948592445

948592444

For analyzing the safety and reliability of your model, we recommend the following workflow:

1. Create or use an existing model of your system design. A model of your design depends on your particular case.
2. Define failure modes of your particular case for each design element and perform the [CONFLUENCE_PAGE title='Describing FMEA Items' space='CSRA2024xR1'].
3. Identify possible risks and use them for further [CONFLUENCE_PAGE title='Describing Safety Analysis Items' space='CSRA2024xR1'].
4. Address the risks in your system design (by introducing new design elements) for controlling and [CONFLUENCE_PAGE title='Describing reduced risks' space='CSRA2024xR1'].

The product safety analysis process is cyclic and requires constant review as depicted in the following figure:

[IMAGE alt='' src='']

948592442

**Related pages**

- [CONFLUENCE_PAGE title='Getting started' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Concepts' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Project templates' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="4fb60f8f-91b2-4b6d-9003-5c4a33a6eeff"><ac:parameter ac:name="id">948592443</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="52cc8e67-14f2-40c3-a4c2-50eae91dcf49"><ac:parameter ac:name="id">948592445</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f8242654-d027-4346-8c2d-c6fe3f46976d"><ac:parameter ac:name="id">948592444</ac:parameter><ac:rich-text-body><p>For analyzing the safety and reliability of your model, we recommend the following workflow:</p><ol><li><p>Create or use an existing model of your system design. A model of your design depends on your particular case.</p></li><li><p>Define failure modes of your particular case for each design element and perform the <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing FMEA Items" /><ac:plain-text-link-body><![CDATA[FMEA analysis]]></ac:plain-text-link-body></ac:link>.</p></li><li><p>Identify possible risks and use them for further <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing Safety Analysis Items" /><ac:plain-text-link-body><![CDATA[risk analysis]]></ac:plain-text-link-body></ac:link>.</p></li><li><p>Address the risks in your system design (by introducing new design elements) for controlling and <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing reduced risks" /><ac:plain-text-link-body><![CDATA[reducing potential hazards]]></ac:plain-text-link-body></ac:link>.</p></li></ol><p> </p><p>The product safety analysis process is cyclic and requires constant review as depicted in the following figure:</p><p><ac:image ac:align="center"><ri:attachment ri:filename="safety_analysis_process.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Process description" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="18dfc1b8-751a-49f4-9394-266caac4a7c8"><ac:parameter ac:name="id">948592442</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Getting started" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Concepts" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Project templates" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466462 space=CSRA2024xR1 version=1 -->
## PAGE 00057: Project templates

- page_id: `170466462`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466462/Project+templates
- version_number: 1
- version_date: `2019-10-30T10:35:02.557+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > Getting started
- labels: []

### NORMALIZED CONTENT

948680083

948680086

948680084

You can use three predefined templates to create a project:

- FMEA Project (Failure Mode Effects Analysis Project). Select this template if you need the reliability analysis only.
- Safety and Reliability Analysis Project (FMEA Project included). Select this template if you need both - the FMEA and risk analysis.
- ISO 26262 Project (Functional Safety Project). Select this template if you need to perform hazard analysis and risk assessment.

Templates contain predefined packages and diagrams to start creating your risk analysis model. Usually, design, FMEA, Risk/Hazard Analysis, Safety Requirements packages are created.

To create a project from a template

1. Do one of the following:
  - 
    - From the File menu, select New Project .
    - On the main toolbar, click the New Project button.
    - Press Ctrl+N.
2. When the New Project dialog opens, double-click the icon of the desired template under the Safety and Reliability Analysis group. The project template with predefined tables, samples, and resources opens.
3. Type a project name, specify a project location, and click **OK** when you are done.

[IMAGE alt='' src='']

948680081

**Related pages**

- [CONFLUENCE_PAGE title='Getting started' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Concepts' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Process description' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="813c1b7a-e860-4b76-bfe1-1aabe12c7a93"><ac:parameter ac:name="id">948680083</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="71e95aa4-dbdc-418d-b964-dfc7d7285621"><ac:parameter ac:name="id">948680086</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="74cbecab-3830-43ec-94a2-232d127366f3"><ac:parameter ac:name="id">948680084</ac:parameter><ac:rich-text-body><p><span style="color: rgb(51,51,51);"><ac:inline-comment-marker ac:ref="807a74e6-88f4-4ebd-bc1b-5fbe67170b92">You can use three predefined templates to create a project:</ac:inline-comment-marker></span></p><ul><li><strong>FMEA Project </strong>(Failure Mode Effects Analysis Project). Select this template if you need the reliability analysis only.</li><li><strong>Safety and Reliability Analysis Project </strong>(FMEA Project included). Select this template if you need both - the FMEA and risk analysis.</li><li><strong>ISO 26262 Project</strong> (Functional Safety Project). Select this template if you need to perform hazard analysis and risk assessment.</li></ul><p>Templates contain predefined packages and diagrams to start creating your risk analysis model. Usually, design, FMEA, Risk/Hazard Analysis, Safety Requirements packages are created.</p><p><br /></p><p>To create a project from a template</p><hr /><ol><li>Do one of the following:<br /><ul><li style="list-style-type: none;background-image: none;"><ul><li>From the <strong>File</strong> menu, select <strong>New Project</strong>.</li><li>On the main toolbar, click the <strong>New Project</strong> button.</li><li>Press Ctrl+N.</li></ul></li></ul></li><li>When the <strong>New Project</strong> dialog opens, double-click the icon of the desired template under the <strong>Safety and Reliability Analysis</strong> group. The project template with predefined tables, samples, and resources opens.</li><li><p>Type a project name, specify a project location, and click <strong>OK</strong> when you are done.</p></li></ol><p style="margin-left: 30.0px;"><ac:image ac:title="Structure of Safety and Reliability Analysis project template" ac:alt="Structure of Safety and Reliability Analysis project template"><ri:attachment ri:filename="safety_and_reliability_analysis_project_template.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Project templates" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c887db79-d14c-4e38-9c53-ed71186a74fb"><ac:parameter ac:name="id">948680081</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Getting started" /></ac:link><ul><li class="_mce_tagged_br"><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Concepts" /></ac:link></li><li class="_mce_tagged_br"><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Process description" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466464 space=CSRA2024xR1 version=1 -->
## PAGE 00058: Reliability analysis using FMEA

- page_id: `170466464`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466464/Reliability+analysis+using+FMEA
- version_number: 1
- version_date: `2018-06-04T03:53:22.854+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

948756908

948756910

948756909

FMEA (Failure Mode and Effect Analysis) is methodology designed:

- To identify potential failure modes for a product or process
- To assess the risks associated with these failure modes
- To rank the issues in term of importance
- To identify and carry out corrective actions to address the most serious concerns.

948756907

**Related pages**

- [CONFLUENCE_PAGE title='Getting started' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Safety analysis' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Additional features' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Customizing Safety Analysis and FMEA configurations' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6772dc02-2fb4-420d-b6a7-4d9f211bedb7"><ac:parameter ac:name="id">948756908</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9532c8ea-0301-4498-a978-88c9ed352c4d"><ac:parameter ac:name="id">948756910</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="758eaab2-3094-4d67-a814-02ed44289160"><ac:parameter ac:name="id">948756909</ac:parameter><ac:rich-text-body><p>FMEA (Failure Mode and Effect Analysis) is methodology designed:</p><div class="O1"><ul><li>To identify potential failure modes for a product or process</li><li>To assess the risks associated with these failure modes</li><li>To rank the issues in term of importance </li><li>To identify and carry out corrective actions to address the most  serious concerns.</li></ul></div></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="66b833a2-7ebe-437e-83d7-78d0c2b90dc9"><ac:parameter ac:name="id">948756907</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Getting started" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety analysis" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Additional features" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Customizing Safety Analysis and FMEA configurations" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466610 space=CSRA2024xR1 version=5 -->
## PAGE 00059: Reports

- page_id: `170466610`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466610/Reports
- version_number: 5
- version_date: `2024-06-18T11:25:55.072+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety
- labels: []

### NORMALIZED CONTENT

The [CONFLUENCE_PAGE title='Report Wizard' space='MD2024xR1'] is capable of generating reports that include data on HARA (Hazard Analysis and Risk Assessment) and functional Safety Concept. Once the report is generated, it automatically opens for viewing. The HARA report presents a comprehensive overview of identified potential hazards and their associated risks. It categorizes these hazards and provides an analysis of the risks involved. The****Functional Safety Concept****report focuses on the derived functional safety requirements. It shows how these requirements are derived from the safety goals and demonstrates their relationships.

To generate a report

1. In the main menu of your modeling tool, select **Tools**> **Report Wizard**.
2. Do one of the following:
  - Select **HARA Report Template**to create a report containing HARA data and click **Next.** 
 
[IMAGE alt='' src='']
  - Select **Functional Safety Concept Report**to generate a report containing functional safety concept data and click **Next.** 
 
**[IMAGE alt='' src='']**
3. To include built-in data in the report, select Built-in and click Next.
4. Do one of the following:
  - To generate a **HARA**report, select the packages containing HARA elements and system functions and then click **Next**.
  - To generate the **Functional Safety Concept**report, select the packages containing Functional Safety Concept elements and then click **Next. 
 
[IMAGE alt='' src='']** To learn more about selecting report data, refer to the [CONFLUENCE_PAGE title='Select Element Scope pane' space='MD2024xR1'].
5. Configure the report file by specifying the report file location and image format. Then Click **Generate**. To learn more about configuring output options, refer to the [CONFLUENCE_PAGE title='Generate Output pane' space='MD2024xR1'].

Following are examples of the **HARA**and **Functional Safety Concept**reports.

[IMAGE alt='' src='']

###### Example of the **HARA**report.

[IMAGE alt='' src='']

###### Example of the **Functional Safety Concept**report.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Report Wizard" /></ac:link> is capable of generating reports that include data on HARA (Hazard Analysis and Risk Assessment) and functional Safety Concept. Once the report is generated, it automatically opens for viewing. The HARA report presents a comprehensive overview of identified potential hazards and their associated risks. It categorizes these hazards and provides an analysis of the risks involved. The<strong> </strong>Functional Safety Concept<strong> </strong>report focuses on the derived functional safety requirements. It shows how these requirements are derived from the safety goals and demonstrates their relationships.</p><p><br /></p><p>To generate a r<span style="color: rgb(23,43,77);">eport</span></p><hr /><ol><li><p>In the main menu of your modeling tool, select <strong>Tools </strong>&gt; <strong>Report Wizard</strong>.</p></li><li><span style="color: rgb(23,43,77);">Do one of the following:</span><ul><li><span style="color: rgb(23,43,77);">Select <strong>HARA Report Template </strong>to create a report containing HARA data and click <strong>Next.</strong><br /><br /><ac:image><ri:attachment ri:filename="HARA_report.png" /></ac:image><br /><br /></span></li><li><span style="color: rgb(23,43,77);">Select <strong>Functional Safety Concept Report </strong>to generate a report containing functional safety concept data and click <strong>Next.</strong><br /><br /><strong><ac:image><ri:attachment ri:filename="Functional Safety Report.png" /></ac:image><br /><br /></strong></span></li></ul></li><li>To include built-in data in the report, select <strong>Built-in </strong>and click <strong>Next.</strong></li><li><p><span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);"><span> Do one of the following:</span></span></span></p><ul><li><p>To generate a <strong>HARA </strong>report, select the packages containing  HARA elements and system functions and then click <strong>Next</strong>.</p></li><li><p>To generate the <strong>Functional Safety Concept </strong>report, select the packages containing Functional Safety Concept elements and then click <strong>Next.<br /><br /><ac:image><ri:attachment ri:filename="Select Element Scope.png" /></ac:image><br /></strong></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a7e0c1cf-1761-4df4-b506-f0833aac2be4"><ac:rich-text-body><p>To learn more about selecting report data, refer to the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Select Element Scope pane" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li></ul></li><li><p><span style="color: rgb(62,63,64);"><span> C</span>onfigure the report file by specifying the report file location and image format. Then C</span>lick <strong>Generate</strong>. <span style="color: rgb(62,63,64);"><br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1e09bc38-d021-45a9-bb8b-8a8ee1b252fb"><ac:rich-text-body><p>To learn more about configuring output options, refer to the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Generate Output pane" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li></ol><p>Following are examples of the <strong>HARA </strong>and <strong>Functional Safety Concept </strong>reports.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="HARA_report_example.png" /></ac:image></p><h6 style="text-align: center;">Example of the <strong>HARA </strong>report.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="FSC_report.png" /></ac:image></p><h6 style="text-align: center;">Example of the <strong>Functional Safety Concept </strong>report.</h6>
````

<!--NOMAGIC_PAGE id=170466473 space=CSRA2024xR1 version=1 -->
## PAGE 00060: Safety analysis

- page_id: `170466473`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466473/Safety+analysis
- version_number: 1
- version_date: `2018-06-04T03:59:36.612+02:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

949133889

949133892

949133891

Safety analysis should be performed by:

- Creating and [CONFLUENCE_PAGE title='Describing Safety Analysis Items' space='CSRA2024xR1'] in a Risk Table.
- Creating a [CONFLUENCE_PAGE title='Describing reduced risks' space='CSRA2024xR1'] to analyze the safety aspect of your model, both before and after the mitigation.
- Using the [CONFLUENCE_PAGE title='FMEAs to be analyzed' space='CSRA2024xR1'] folder to track the FMEA Items that still require safety analysis.

949133888

**Related pages**

- [CONFLUENCE_PAGE title='Getting started' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Reliability analysis using FMEA' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Additional features' space='CSRA2024xR1']
- [CONFLUENCE_PAGE title='Customizing Safety Analysis and FMEA configurations' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d88cf3d7-f214-43d5-a98e-33dadb53cfad"><ac:parameter ac:name="id">949133889</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0283e6c9-6b6d-43d5-bcbb-6c0cd98aecf5"><ac:parameter ac:name="id">949133892</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="58076a76-0f9d-4cc2-bd52-89fd76146d13"><ac:parameter ac:name="id">949133891</ac:parameter><ac:rich-text-body><p>Safety analysis should be performed by:</p><ul><li>Creating and <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing Safety Analysis Items" /><ac:plain-text-link-body><![CDATA[describing Safety Analysis Items]]></ac:plain-text-link-body></ac:link> in a Risk Table.</li><li>Creating a <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Describing reduced risks" /><ac:plain-text-link-body><![CDATA[Risk Reduction Table]]></ac:plain-text-link-body></ac:link> to analyze the safety aspect of your model, both before and after the mitigation.</li><li>Using the <em><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="FMEAs to be analyzed" /><ac:plain-text-link-body><![CDATA[FMEAs to Be Analyzed]]></ac:plain-text-link-body></ac:link></em> folder to track the FMEA Items that still require safety analysis.</li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="93e554a3-dc25-48ac-a064-e9ed7e2b4288"><ac:parameter ac:name="id">949133888</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Getting started" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Reliability analysis using FMEA" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Additional features" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Customizing Safety Analysis and FMEA configurations" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466487 space=CSRA2024xR1 version=2 -->
## PAGE 00061: Safety and Reliability Coverage Analysis

- page_id: `170466487`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466487/Safety+and+Reliability+Coverage+Analysis
- version_number: 2
- version_date: `2024-05-08T14:01:15.884+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Additional features
- labels: []

### NORMALIZED CONTENT

949791490

949791492

949791491

Safety and reliability coverage analysis is designed as a table. Thustable describes how many design elements are covered with risks and FMEA in the model.

[IMAGE alt='' src='']

To perform a coverage analysis

1. In your model, select a package and [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024xR1'] in it. Diagram is located in the **Safety and Reliability Analysis** group and is named **Safety and Reliability Coverage Analysis**.
2. Specify a scope for the analysis. In the **Scope** box, define a package wherein you want to perform the analysis:

- 
  - You may drag a package directly from the Model Browser. In this way, only one package can be specified for analysis.
  - Click the **Select Scope** button [IMAGE alt='' src=''] located after the **Scope** box. In the open **Select Scope** dialog, select one or more packages and click **OK**.

The coverage analysis table is created.

949791489

**Related pages**

- [CONFLUENCE_PAGE title='Additional features' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Traceability maps' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Generating reports' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Linking Failure Modes to model elements' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bc9de22c-37c9-426b-a0f2-1e8d2e6660fe"><ac:parameter ac:name="id">949791490</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c4f4cf64-e3a6-4412-aa5c-f697c473a8e1"><ac:parameter ac:name="id">949791492</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="84bb9ee2-3505-4e0f-a5de-75be31d0ce11"><ac:parameter ac:name="id">949791491</ac:parameter><ac:rich-text-body><p>Safety and reliability coverage analysis is designed as a table. Thus<span style="color: rgb(0,0,0);"> table describes how many design elements are covered with risks and FMEA in the model.</span></p><p><span style="color: rgb(0,0,0);"><ac:image ac:title="Coverage analysis table" ac:alt="Coverage analysis table"><ri:attachment ri:filename="covarage_analysis_table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety and Reliability Coverage Analysis" /></ri:attachment></ac:image></span></p><p><span style="color: rgb(0,0,0);"><br /></span></p><p><span style="color: rgb(0,0,0);">To perform a coverage analysis</span></p><hr /><ol><li><span style="color: rgb(0,0,0);">In your model, select a package and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[create a diagram]]></ac:plain-text-link-body></ac:link> in it. Diagram is located in the <strong>Safety and Reliability Analysis</strong> group and is named <strong>Safety and Reliability Coverage Analysis</strong>.</span></li><li><span style="color: rgb(0,0,0);">Specify a scope for the analysis. In the <strong>Scope</strong> box, define a package wherein you want to perform the analysis:</span></li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li><span style="color: rgb(0,0,0);">You may drag a package directly from the Model Browser. In this way, only one package can be specified for analysis.</span></li><li><span style="color: rgb(0,0,0);">Click the <strong>Select Scope</strong> button <ac:image><ri:attachment ri:filename="3dot_button_long.png"><ri:page ri:space-key="MD184" ri:content-title="_buttons" /></ri:attachment></ac:image> located after the <strong>Scope</strong> box. In the open <strong>Select Scope</strong> dialog, select one or more packages and click <strong>OK</strong>.</span></li></ul></li></ul><p><span style="color: rgb(0,0,0);">The coverage analysis table is created.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9ac1f05d-9109-48c7-bbdd-782d41c51e3c"><ac:parameter ac:name="id">949791489</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Additional features" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generating reports" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170466584 space=CSRA2024xR1 version=2 -->
## PAGE 00062: Safety Requirement Diagram

- page_id: `170466584`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466584/Safety+Requirement+Diagram
- version_number: 2
- version_date: `2024-05-08T14:01:16.331+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety > Tables and diagrams
- labels: []

### NORMALIZED CONTENT

A Safety Requirement Diagram displays safety goals, safety requirements and their relations. The main purpose of this diagram is to create requirements that cover the safety goals defined in HARA. In this chapter, you will learn how to derive safety requirements using the Safety Requirement Diagram and how to assign ASIL values.

[IMAGE alt='' src='']

###### A sample Safety Requirement Diagram displaying different types of Safety Requirements derived from a Safety Goal.

##### Deriving Safety Requirements

Safety Requirements are derived from Safety Goals defined in a [CONFLUENCE_PAGE title='HARA Table' space='CSRA2024xR1']. You can use the Safety Requirement Diagram to derive four types of Safety Requirements: Functional Safety Requirements, Technical Safety Requirements, Software Safety Requirements, and Hardware Safety Requirements.

To derive a Safety Requirement

1. [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024xR1'] .
2. In the model browser, find the Safety Goal you want to derive a Safety Requirement from and drag it to the diagram.
3. Create the Safety Requirement you want to derive by clicking it in the diagram palette and clicking an empty space on the diagram pane. Safety Requirement typesYou can create four types of Safety Requirements: Functional Safety Requirements, Technical Safety Requirements, Software Safety Requirements, and Hardware Safety Requirements.
4. Name the created Safety Requirement and write the requirement text.
5. Create a Derive relationship from the Safety Requirement to the Safety Goal as displayed below [ATTACHMENT filename='deriving_safety_requirement.png']

After you derive a Safety Requirement, the ASIL value is automatically determined by the Safety Goal you have derived the Requirement from. If a Safety Requirement is derived from more than one safety goal or Safety Requirement, a higher ASIL value is set. However, you can specify a different ASIL value than the one defined by a Derive relationship.

To change the ASIL value

1. Open the Specification window of the Safety Requirement for which you want to change the ASIL value.
2. Select the property specification cell of the ASIL Override Justification property and write an explanation why the value is changed.
3. Click the property specification cell of the ASIL property and select the desired ASIL value from the menu.
4. Close the Specification window.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>A Safety Requirement Diagram displays safety goals, safety requirements and their relations. The main purpose of this diagram is to create requirements that cover the safety goals defined in HARA. In this chapter, you will learn how to derive safety requirements using the Safety Requirement Diagram and how to assign ASIL values.<br /><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="safety_requirement_diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety Requirement Diagram" /></ri:attachment></ac:image></p><h6 style="text-align: center;">A sample Safety Requirement Diagram displaying different types of Safety Requirements derived from a Safety Goal.</h6><h3>Deriving Safety Requirements</h3><p>Safety Requirements are derived from Safety Goals defined in a <ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="HARA Table" /></ac:link>. You can use the Safety Requirement Diagram to derive four types of Safety Requirements: Functional Safety Requirements, Technical Safety Requirements, Software Safety Requirements, and Hardware Safety Requirements.</p><p><br /></p><p>To derive a Safety Requirement</p><hr /><ol><li><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[Create a Safety Requirement Diagram]]></ac:plain-text-link-body></ac:link>.</li><li>In the model browser, find the Safety Goal you want to derive a Safety Requirement from and drag it to the diagram.</li><li><p class="auto-cursor-target">Create the Safety Requirement you want to derive by clicking it in the diagram palette and clicking an empty space on the diagram pane.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ef6e3d6d-9632-4dd6-badf-472c4e1ef6c1"><ac:parameter ac:name="title">Safety Requirement types</ac:parameter><ac:rich-text-body><p>You can create four types of Safety Requirements: Functional Safety Requirements, Technical Safety Requirements, Software Safety Requirements, and Hardware Safety Requirements.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Name the created Safety Requirement and write the requirement text.</li><li>Create a Derive relationship from the Safety Requirement to the Safety Goal as displayed below<br /><br /><ac:image><ri:attachment ri:filename="deriving_safety_requirement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety Requirement Diagram" /></ri:attachment></ac:image></li></ol><p><br />After you derive a Safety Requirement, the ASIL value is automatically determined by the Safety Goal you have derived the Requirement from. If a Safety Requirement is derived from more than one safety goal or Safety Requirement, a higher ASIL value is set. However, you can specify a different ASIL value than the one defined by a Derive relationship.</p><p><br /></p><p>To change the ASIL value</p><hr /><ol><li>Open the Specification window of the Safety Requirement for which you want to change the ASIL value.</li><li>Select the property specification cell of the <strong style="letter-spacing: 0.0px;">ASIL Override Justification</strong> property and write an explanation why the value is changed.</li><li>Click the property specification cell of the <strong>ASIL</strong> property and select the desired ASIL value from the menu.</li><li>Close the Specification window.</li></ol>
````

<!--NOMAGIC_PAGE id=170466640 space=CSRA2024xR1 version=1 -->
## PAGE 00063: Systems Cybersecurity Designer

- page_id: `170466640`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466640/Systems+Cybersecurity+Designer
- version_number: 1
- version_date: `2024-03-26T07:59:23.498+01:00`
- ancestors: Cameo Safety and Reliability Analyzer
- labels: []

### NORMALIZED CONTENT

Cybersecurity engineering is a critical discipline to ensure safe and secure human experiences using cyber-physical systems. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events.

Based on a system architecture, the Systems Cybersecurity Designer enables:

- Selection of Assets for protection
- Threat and Cyberattack Modeling
- Risk Evaluation
- Cybersecurity requirements creation to mitigate identified risks

The Systems Cybersecurity Designer supports the following risk assessment methodologies :

- Threat Analysis and Risk Assessment as per ISO/SAE 21434:2021

To learn more about Systems Cybersecurity Designer, refer to:

2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cybersecurity engineering is a critical discipline to ensure safe and secure human experiences using cyber-physical systems. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events.</p><p>Based on a system architecture, the Systems Cybersecurity Designer enables:</p><ul><li>Selection of Assets for protection</li><li>Threat and Cyberattack Modeling</li><li>Risk Evaluation</li><li>Cybersecurity requirements creation to mitigate identified risks</li></ul><p>The Systems Cybersecurity Designer supports the following risk assessment methodologies :</p><ul><li>Threat Analysis and Risk Assessment as per <a href="https://www.iso.org/standard/70918.html">ISO/SAE 21434:2021</a></li></ul><p>To learn more about Systems Cybersecurity Designer, refer to:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="7832867d-5240-44d1-b79b-877fd5dbba46"><ac:parameter ac:name="depth">2</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=170466661 space=CSRA2024xR1 version=1 -->
## PAGE 00064: Table

- page_id: `170466661`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466661/Table
- version_number: 1
- version_date: `2024-01-31T07:30:01.476+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity
- labels: []

### NORMALIZED CONTENT

Learn more about tables and diagrams of the ISO 21434 project template from the following chapters:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:inline-comment-marker ac:ref="2b195a29-57e4-432b-98b8-4c02aeb8a869">Learn more a</ac:inline-comment-marker>bout tables and diagrams of the ISO 21434 project template from the following chapters: </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e53f8925-cb18-4682-9fb1-5a9ac41082e0" /></p>
````

<!--NOMAGIC_PAGE id=170466519 space=CSRA2024xR1 version=1 -->
## PAGE 00065: Tables and diagrams

- page_id: `170466519`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466519/Tables+and+diagrams
- version_number: 1
- version_date: `2024-01-31T07:29:57.767+01:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety
- labels: []

### NORMALIZED CONTENT

To learn more about tables and diagrams of the ISO 26262 Plugin, see:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To learn more about tables and diagrams of the ISO 26262 Plugin, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b0ff9cd7-4449-422b-9df4-7f7f5dff63c3" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=170467057 space=CSRA2024xR1 version=1 -->
## PAGE 00066: TARA

- page_id: `170467057`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170467057/TARA
- version_number: 1
- version_date: `2024-04-29T09:52:12.886+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

3

The TARA table gathers all elements that have been modeled in the previous steps and gives a global overview of the threat scenario that has to be mitigated, retained, shared, or avoided. The risk value is automatically calculated according to the ISO/SAE 21434:2021 standard.

**Cybersecurity Risk**

An effect of uncertainty on road vehicle cybersecurity expressed in terms of attack feasibility and impact.

**Cybersecurity Control**

A measure that is modifying risk.

**Cybersecurity Claim**

A statement about a risk.

**Cybersecurity Goal**

A concept-level cybersecurity requirement associated with one or more threat scenarios.

##### Creating a TARA Table

If you create a new project using the**ISO 21434 Project**template, then a**TARA**tablealready exists in the**1.4 Risk Treatment and Cybersecurity Control**package.

To create aTARATable

1. In the Containment tree, right-click Risk Treatment and Cybersecurity Control and select Create Diagram. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **TARA** **Table**. [IMAGE alt='' src='']
  - In the search tab, type the keyword TARA and then select TARA Table. 
 
**[IMAGE alt='' src='']** The TARA Table is displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='TARA Table created.png']

##### Adding Threat Scenarios

To add Threat Scenarios to the TARA Table

1. In the TARA Table, click Add Existing. [ATTACHMENT filename='Add Existing.png']
2. From the **Select Threat Scenario******dialog, select the required Threat Scenario. [ATTACHMENT filename='Select TS-Dialog.jpg'] A row is added to the TARA Table, which shows the existing Threat Scenario. 
 
[IMAGE alt='' src=''] Threat Type, Impacted Asset, and Damage Scenarios are automatically added to the TARA Table based on the Damage Scenario Table and Threat Scenarios Table. The association between Threat Scenarios and Damage Scenarios tables is done through failure. The Damage Scenarios which have the same Failure Modes as a given Threat Scenario are taken into account for Risk Values computation.The risk values are automatically computed according to ISO/SAE 21434:2021 standard. Risk values are read-only values.

##### Assigning Risk Treatment Decision

To assign Risk Treatment Decision

- Double-click the cellin the**Risk Treatment Decision** column and the requiredThreat Scenario'srow. From the drop-down list, assign Risk Treatment Decision. 
 
[IMAGE alt='' src=''] 
The Risk Treatment Decision is assigned in the TARA Table. 
 
[IMAGE alt='' src=''] If the risk treatment decision is Retain, adding a claim is mandatory. In those cases, the cybersecurity goals and controls are notrequired.

##### Adding Cybersecurity Goal

To add a Cybersecurity Goal to the TARA Table

1. Double-click the designated cell in the Cybersecurity Goals column and the required Threat Scenario's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Goal creation_Three dots.png']
2. From the **Select Element******dialog, select Cybersecurity Goal. [ATTACHMENT filename='Select Element dialog_Goal creation.png'] The Cybersecurity Goal is added to the TARA Table.
3. [ATTACHMENT filename='Goal creation_Done.png']

- You can also add a safety goal from another project (HARA analysis) as a cybersecurity goal. Doing this will create a clone of the safety goal in your project. To add a safety goal as a cybersecurity goal, follow the same procedure as defined above.
- If the ASIL value of the safety goal is inconsistent with the Safety Risk Value of the threat scenario, a validation rule is triggered and the particular row is displayed in red. You can view the error message in the Active Validation Results pane.
- You can mitigate the error by making the ASIL value and the Safety Risk Value consistent with each other. [ATTACHMENT filename='Error.jpg']

To Generate/Synchronize the Cybersecurity Goals to the TARA Table

- Right-click the threat scenario in the TARA table and select Generate/Synchronize Cybersecurity Goals. 
 
[IMAGE alt='' src='']

- The cybersecurity goal is autogenerated based on the following formula:
  - [Asset Name]of the[Item]shall be protected against[Threat type]
- If you add an item, asset or a threat type for a threat scenario, the command autogenerates a cybersecurity goal.
- If you update an item, asset or a threat type for a threat scenario, the command synchronizes the autogenerated cybersecurity goal. Following are the two scenarios in which synchronization happens:
  - If you rename an item, asset or a threat type, then the existing autogenerated cybersecurity goal is renamed.
  - If you add/remove an item, asset or a threat type, then an autogenerated cybersecurity goal is added/removed.

##### Adding Controls

To add Controls to the TARA Table

1. Double-click the designated cell in the Controls column and the required Threat Scenario's row and click [IMAGE alt='' src=''] . [ATTACHMENT filename='Adding control_three dots.png']
2. From the **Select Elements******dialog, select Controls. 
[IMAGE alt='' src=''] The Controls are added to the TARA Table. 
 
[IMAGE alt='' src=''] Controls are a list of Cybersecurity Requirements. There are 4 types of Cybersecurity Requirements: Functional, Technical, Hardware, and Software.

To ease the process of adding controls, the plugin provides a feature to add the controls with the aid of the Recommend Control command. The controls are recommended on the basis of assigned cybersecurity goals and CWE elements used as attack path steps.

To add controls using the Recommend Control command to the TARA Table

1. Right-click the threat scenario in the TARA table and select Recommended Control, as follows: [ATTACHMENT filename='Recommended Controls.png']
2. From the **Select Elements**dialog, select or remove the recommended controls. 
 
[IMAGE alt='' src=''] For requirements to be reflected as recommended controls in the Select Elements dialog, either of these conditions should be satisfied:A Threat scenario should have assigned cybersecurity goals with all the derived requirements. 
 
[IMAGE alt='' src='']A Threat Scenario should have an Attack Path, which itself has a step, which is either a CWE or a Technique. In such case, if the CWE or Technique has a Recommendation from a Cybersecurity Requirement, then that requirement will be automatically proposed by **Recommend control**command. The recommended controls are added to the TARA Table. 
 
[IMAGE alt='' src='']

##### Adding Claim

To add a Claim to the TARA Table

- Double-click the cell in the **Claims**column and the required Threat Scenario's row and type in the necessary Claim. 
 
[IMAGE alt='' src=''] If the risk treatment decision is Retain, adding a claim is mandatory. In those cases, the cybersecurity goals and controls are not required and cannot be specified. Due to some performance reason, the claim does not appear in the containment tree directly after specifying it in the claim's cell. You must save the project to see the claims in the containment tree under the smart package **2.3 Cybersecurity Claims**.

TARA Table Example

- The Safety, Financial, Operational, Privacy risk values are calculated automatically by using following formula:
  - Risk Value = 1 + Maximum(Impact) * Aggregated Attack Feasibility Rating [ATTACHMENT filename='Impact Rating.png']
- The maximum value among all the risk values viz. Safety, Financial, Operational, Privacy is considered as the Global Risk Value.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="8fa4a3e4-b081-4fe8-b6ad-a0ee28a4ad60"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>The TARA table gathers all elements that have been modeled in the previous steps and gives a global overview of the threat scenario that has to be mitigated, retained, shared, or avoided. The risk value is automatically calculated according to the ISO/SAE 21434:2021 standard.</p><p><strong>Cybersecurity Risk</strong></p><p>An effect of uncertainty on road vehicle cybersecurity expressed in terms of attack feasibility and impact.</p><p><strong>Cybersecurity Control</strong></p><p>A measure that is modifying risk.</p><p><strong>Cybersecurity Claim</strong></p><p>A statement about a risk.</p><p><strong>Cybersecurity Goal</strong></p><p>A concept-level cybersecurity requirement associated with one or more threat scenarios.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a TARA Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7e648328-edd6-4bc0-9aed-66cdf7a757f4"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color: rgb(23,43,77);">, then a<span> <span style="color: rgb(62,63,64);"><strong>TARA</strong> </span></span>table<span> </span>already exists in the<span> <strong>1.4 Risk Treatment and Cybersecurity Control</strong> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec">To create a</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec"> </ac:inline-comment-marker></span><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec">TARA</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec"> </ac:inline-comment-marker></span></span><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec">Table</ac:inline-comment-marker></p><hr /><ol><li>In the Containment tree, right-click<span> </span><strong>Risk Treatment and Cybersecurity Control </strong>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="1 SelectCreateDiagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>TARA</strong> <strong>Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="2 DirectlySelectTARAtable.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target"><span style="color: rgb(62,63,64);">In the search tab, type the keyword TARA and then select</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">TARA Table.<br /><br /><strong><ac:image><ri:attachment ri:filename="3 WriteTARAtable.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></strong><br /><br /></strong><span style="color: rgb(62,63,64);">The TARA Table is displayed in the diagram pane of the modeling tool.<br /></span><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="TARA Table created.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></li></ul></li></ol><h3>Adding Threat Scenarios</h3><p>To add Threat Scenarios to the TARA Table</p><hr /><ol><li>In the TARA Table, click Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="Add Existing.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Threat Scenario</strong><strong> </strong>dialog, select the required Threat Scenario.<br /><br /></span><ac:image><ri:attachment ri:filename="Select TS-Dialog.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /><p><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="7b589376-fb3c-43cb-b74d-d3ec594130f7">A row is added to the TARA</ac:inline-comment-marker> Table, which shows the existing Threat Scenario.</span><br /><br /><ac:image><ri:attachment ri:filename="Existing TS added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="77e20d62-232c-4810-8df2-d4c1d4888c49"><ac:rich-text-body><ul><li>Threat Type, Impacted Asset, and <ac:inline-comment-marker ac:ref="a7612104-f5f2-450b-973f-517cbe6aaab5">Damage Scenarios</ac:inline-comment-marker> are automatically added to the TARA Table based on the Damage Scenario Table and Threat Scenarios Table. <span style="color: rgb(23,43,77);">The association between Threat Scenarios and Damage Scenarios tables is done through failure. The Damage Scenarios which have the same Failure Modes as a given Threat Scenario are taken into account for Risk Values computation.</span></li><li>The risk values are automatically computed according to ISO/SAE 21434:2021 standard. Risk values are read-only values.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><h3><span>Assigning Risk Treatment Decision</span></h3><p>To assign Risk Treatment Decision</p><hr /><ul><li><p><span style="color: rgb(62,63,64);">  Double-click the cell </span><span style="color: rgb(22,22,22);"><span>in the<strong> Risk Treatment Decision</strong> column and the <span style="color: rgb(62,63,64);">required </span><ac:inline-comment-marker ac:ref="6f5a9180-4325-47b6-bd76-846e832408b2">Threat Scenario's</ac:inline-comment-marker> </span></span><span style="color: rgb(62,63,64);">row. From the drop-down list, assign Risk Treatment Decision.<br /><br /><ac:image><ri:attachment ri:filename="Assigning Risk Treatment Decision.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br />The Risk Treatment Decision is assigned in the <ac:inline-comment-marker ac:ref="7acc8642-88b3-462f-8d34-ca4f06afe485">TARA Table</ac:inline-comment-marker>.<br style="text-align: left;" /><br /><ac:image><ri:attachment ri:filename="Risk Treatment Decision assigned.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8f7913eb-62eb-4cac-ada5-8e0f0922b472"><ac:rich-text-body><p>If the risk treatment decision is Retain, adding a claim is mandatory. In those cases, the cybersecurity goals and controls are not<span> </span>required.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><h3><ac:inline-comment-marker ac:ref="96f9d859-049c-465c-aa24-64e270a761ed">Adding Cybersecurity Goal</ac:inline-comment-marker></h3><p>To add a Cybersecurity Goal to the TARA Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Cybersecurity Goals </strong>column and the required Threat Scenario's row and click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Goal creation_Three dots.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Element</strong><strong> </strong>dialog, select Cybersecurity Goal.</span><br style="text-align: left;" /><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="Select Element dialog_Goal creation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br style="text-align: left;" /><br style="text-align: left;" /><span style="color: rgb(62,63,64);">The Cybersecurity Goal is added to the TARA Table.</span><br style="text-align: left;" /><br /></li><li><ac:image><ri:attachment ri:filename="Goal creation_Done.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1f707f02-74e9-452f-be65-7ab470f0cb77"><ac:rich-text-body><ul><li>You can also add a safety goal from another project (HARA analysis) as a cybersecurity goal. Doing this will create a clone of the safety goal in your project. To add a safety goal as a cybersecurity goal, follow the same procedure as defined above.</li><li>If the ASIL value of the safety goal is inconsistent with the Safety Risk Value of the threat scenario, a validation rule is triggered and the particular row is displayed in red. You can view the error message in the Active Validation Results pane.</li><li>You can mitigate the error by making the ASIL value and the Safety Risk Value consistent with each other.<br /><br /><ac:image><ri:attachment ri:filename="Error.jpg"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><p>To Generate/Synchronize the Cybersecurity Goals to the TARA Table</p><hr /><ul><li>Right-click  the threat scenario in the TARA table and select <strong>Generate/Synchronize Cybersecurity Goals.<br /><br /><ac:image><ri:attachment ri:filename="Generate or Synchronize Cybersecurity Goals.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></strong></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="482534e4-e6ea-48be-8952-8297ceae1473"><ac:rich-text-body><ul><li>The cybersecurity goal is autogenerated based on the following formula:<ul><li><p style="text-align: left;"><span> </span><span style="letter-spacing: 0.0px;"><span class="error" style="color: rgb(23,43,77);">[Asset Name]</span><span style="color: rgb(23,43,77);"> of the </span><span class="error" style="color: rgb(23,43,77);">[Item]</span><span style="color: rgb(23,43,77);"> shall be protected against </span><span class="error" style="color: rgb(23,43,77);">[Threat type]</span></span></p></li></ul></li><li>If you add an item, asset or a threat type for a threat scenario, the command <ac:inline-comment-marker ac:ref="8bd65be0-1e49-4d25-9844-40347193bece">autogenerates</ac:inline-comment-marker> a cybersecurity goal.</li><li>If you update an item, asset or a threat type for a threat scenario, the command synchronizes the autogenerated cybersecurity goal. Following are the two scenarios in which synchronization happens:<ul><li>If you rename an item, asset or a threat type, then the existing autogenerated cybersecurity goal is renamed.</li><li>If you add/remove an item, asset or a threat type, then <ac:inline-comment-marker ac:ref="2ac9f00b-da95-40e2-ac69-0550d05bedbe">an </ac:inline-comment-marker>autogenerated cybersecurity goal is added/removed.</li></ul></li></ul></ac:rich-text-body></ac:structured-macro><h3>Adding Controls</h3><p>To add Controls to the TARA Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Controls </strong>column and the required Threat Scenario's row and click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Adding control_three dots.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></li><li><p><span style="color: rgb(62,63,64);">From the <strong>Select Elements</strong><strong> </strong>dialog, select Controls.<br /></span><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="Select Element dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></p><p><br style="text-align: left;" /><span style="color: rgb(62,63,64);">The Controls are added to the TARA Table.<br /><br /><ac:image><ri:attachment ri:filename="Controls added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /></span></p><p><span style="color: rgb(62,63,64);"> </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="134e66d9-b566-4d6b-a8f1-a28a54abcc70"><ac:rich-text-body><p>Controls are a list of Cybersecurity Requirements. There are 4 types of Cybersecurity Requirements: Functional, Technical, Hardware, and Software.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p>To ease the process of adding controls, the plugin provides a feature to add the controls with the aid of the Recommend Control command. The controls are recommended on the basis of assigned cybersecurity goals and CWE elements used as attack path steps.</p><p>To add controls using the Recommend Control command to the TARA Table</p><hr /><ol><li>Right-click the threat scenario in the TARA table and select <strong>Recommended Control,</strong> as follows:<br /><br /><ac:image><ri:attachment ri:filename="Recommended Controls.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></li><li><p><span style="color: rgb(62,63,64);">From the <strong>Select Elements </strong>dialog, select or remove the recommended controls.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements Dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="14a75f63-82fb-4424-b1e2-de4fba1e9d60"><ac:rich-text-body><p>For requirements to be reflected as recommended controls in the Select Elements dialog, either of these conditions should be satisfied:</p><ul><li>A Threat scenario should have assigned cybersecurity goals with all the derived requirements.<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Dreived Requirements.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(23,43,77);">A Threat Scenario should have an Attack Path, which itself has a step, which is either a CWE or a Technique. In such case, if the CWE or Technique has a Recommendation from a Cybersecurity Requirement, then that requirement will be automatically proposed by <strong>Recommend control </strong>command.</span></li></ul></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(62,63,64);"> </span></p><span style="color: rgb(62,63,64);">The recommended controls are added to the TARA Table.<br /><br /><ac:image><ri:attachment ri:filename="Recommended Controls_Added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /></span></li></ol><h3><span>Adding Claim</span></h3><p>To add a Claim to the TARA Table</p><hr /><ul><li><p>Double-click the cell in the <strong>Claims </strong>column and the required Threat Scenario's row and type in the necessary Claim. <br /><br /><ac:image><ri:attachment ri:filename="Adding claim.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fbac0599-a233-4659-a473-5460133a0011"><ac:rich-text-body><p>If the risk treatment decision is Retain, adding a claim is mandatory. In those cases, the cybersecurity goals and controls are not required <span style="color: rgb(62,63,64);">and cannot be specified.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7a794356-545a-4198-8751-3c2a1fb2df47"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">Due to some performance reason, the claim does not appear in the containment tree directly after specifying it in the claim's cell. You must save the project to see the claims in the containment tree under the smart package <strong>2.3 Cybersecurity Claims</strong>.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><p><span style="font-size: 16.0px;font-weight: bold;letter-spacing: -0.006em;">TARA Table Example</span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7c53fe9f-4eba-4f52-9c80-3bdd2b2a14c4"><ac:rich-text-body><ul><li>The Safety, Financial, Operational, Privacy risk values are calculated automatically by using following formula:<ul><li>Risk Value =  1 + Maximum(Impact) * Aggregated Attack Feasibility Rating<br /><br /><ac:image><ri:attachment ri:filename="Impact Rating.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image><br /><br /></li></ul></li><li><span style="color: rgb(51,51,51);">The maximum value among all the risk values viz. Safety, Financial, Operational, Privacy is considered as the Global Risk Value.</span></li></ul></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="1 TARA_illustration.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="TARA" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466865 space=CSRA2024xR1 version=2 -->
## PAGE 00067: Threat  scenario

- page_id: `170466865`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466865/Threat+scenario
- version_number: 2
- version_date: `2024-05-08T14:01:17.074+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

53

**Threat Scenario**

Potential cause of compromise of cybersecurity properties of one or more assets in order to realize a damage scenario.

**Attack Path**

Set of deliberate actions to realize a threat scenario.

**Failure**

Termination of an intended behavior of an element or an item due to a fault manifestation.

##### Creating a Threat Scenario

To create a Threat Scenario

1. In the Containment tree, right-click**Threat Scenario**and select Create Element. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO 21434**and select **Threat Scenario**. [IMAGE alt='' src='']
  - In the search tab, type the keyword threat and then select Threat Scenario. 
 
[IMAGE alt='' src='']
3. Name the created Threat Scenario in the Containment tree and press Enter. The Threat Scenario has the prefix **D****S**,which denotes that the created element is a Threat Scenario; the number**1** indicates that it is the first Threat Scenario created. 
 
[IMAGE alt='' src='']

##### Creating a Threat Scenario Table

If you create a new project using the**ISO 21434 Project**template, then a**Threat Scenario Table**already exists in the**1.2 Threat Scenarios**package.

To create aThreat ScenarioTable

1. In the Containment tree, right-click Threat Scenario and select Create Diagram. 
 
[IMAGE alt='' src='']
2. Do one of the following:
  - In the dialog, expand **ISO** **21434**and select **Threat Scenario Table**. [IMAGE alt='' src='']
  - In the search tab, type the keyword threat and then select Threat Scenario Table. 
 
[IMAGE alt='' src=''] The Threat Scenario Table is now displayed in the diagram pane of the modeling tool. [ATTACHMENT filename='Threat Scenario Table.png']

##### Adding a Threat Scenario to the Threat Scenario Table

To add a new Threat Scenario to the Threat Scenario Table

1. In the Threat Scenario Table, click Add New. A row is added in the Threat Scenario Table, which shows the new Threat Scenario. [IMAGE alt='' src='']
2. In the newly created Threat Scenario's row and the **Name**column, double-click the designated cell to name the Threat Scenario. 
 
**[IMAGE alt='' src='']**

To add an existing Threat Scenario to the Threat Scenario Table

1. In the Threat Scenario Table, click Add Existing. 
 
[IMAGE alt='' src='']
2. From the **Select Threat Scenario** dialog, select the required Threat Scenario. A row is added to the Threat Scenario Table, showing the existing Threat Scenario. 
 
[IMAGE alt='' src='']
3. In the existing Threat Scenario's row and the **Name**column, double-click the designated cell to rename the Threat Scenario. 
 
**[IMAGE alt='' src='']**

##### Creating a custom threat type

To create a custom threat type

1. Create a general threat scenario as defined in the [CONFLUENCE_PAGE title='Threat scenario' space='CSRA2024xR1'] section.
2. Open the Specification dialog of the newly created threat scenario in the **Expert** mode.
3. Set the **Is Abstract** property to *True*. 
 
[IMAGE alt='' src=''] 
 
The newly created threat scenario will now be displayed in italics in the Containment tree and will be available under the **custom**package in the Select Threat Type dialog. [ATTACHMENT filename='Custom Threat Type.png']

Threat Types are displayed by default in the TARA analysis as Threat Scenarios. To prevent that, you must create the Threat Types in a dedicated package or library.

##### Creating custom packages for custom-created threat types

You can group the custom-created threat types by creating custom packages and placing them under the custom packages. To create a new package, you must create a generalization set of the required custom threat types.To learn more about creating a generalization set, refer to[CONFLUENCE_PAGE title='Generalization set' space='MD2024xR1'].

[IMAGE alt='' src='']

###### Select Threat Type dialog showing the custom threat types places under the custom created packages.

The following example displays a typical scenario in which a generalization set can be created.

[IMAGE alt='' src='']

###### Generalization set example.

##### Creating subcategory for the custom-created threat type

You can also create subcategories of the custom-created threat types. Doing so will create a nesting effect in the Select Threat Type dialog.

[IMAGE alt='' src='']

###### Select Threat Type dialog showing the nesting effect due to subcategorization of the threat types.

To create subcategories of the custom-created threat type

1. In the Specification dialog of the newly created threat Type, click [IMAGE alt='' src=''] in the**Base Classifier** property. 
 
[IMAGE alt='' src='']
2. Select any parent threat type under which you want to place the newly created custom threat type. 
 
[IMAGE alt='' src='']

##### Adding a Threat Type

To add a Threat Type

1. Double-click the designated cell in the **Threat Type** column and the required Threat Scenario's row and click [IMAGE alt='' src='']. 
 
[IMAGE alt='' src='']
2. From the **Select Threat Type**dialog, select a threat type(s) from either the **[STRIDE](https://en.wikipedia.org/wiki/STRIDE_%28security%29)**or **[UNECE](https://unece.org/sites/default/files/2023-02/R155e%20%282%29.pdf)**package. You can also select a custom-created threat type. 
 
[IMAGE alt='' src=''] The Threat Type will be added to the Threat Scenarios Table. [ATTACHMENT filename='Threat Type Applied.png']

##### Adding an Attack Path

You can add multiple attack paths for a given Threat Scenario.

To add an Attack Path

1. Double-click the designated cell in the **Attack Path** column and the required Threat Scenario's row and click [IMAGE alt='' src='']. [ATTACHMENT filename='Three dot-Attack Path Steps.png']
2. From the**Select Elements******dialog, select Attack Path. 
 
[IMAGE alt='' src=''] The Attack Path is added to the Threat Scenario Table. 
 
[IMAGE alt='' src='']

- You can also drag and drop the Attack Paths from the Containment tree to the Threat Scenario Table.
- The Aggregated Attack Feasibility Rating is added automatically after you add the Attack Path.

##### Adding a Failure

To add a Failure

1. Double-click the designated cell in the**Failure** column and the required Threat Scenario's row and click [IMAGE alt='' src='']. [ATTACHMENT filename='Adding Failure_Three dot.png']
2. From the **Select Class******dialog, select Failure. 
 
[IMAGE alt='' src=''] The Failure is now shown in the Threat Scenario Table. 
 
[IMAGE alt='' src='']

You can also drag and drop the Failure modes from the Containment tree to the Threat Scenario Table.

##### Adding an Impacted Asset

You can add multiple Impacted Assets for a given Threat Scenario.

To add an Impacted Asset

1. Double-click the designated cell in the**Impacted Asset** column and the required Threat Scenario's row and click [IMAGE alt='' src='']. [ATTACHMENT filename='Adding Impacted Assets.png']
2. From the **Select Element******dialog, select Impacted Asset. 
 
[IMAGE alt='' src=''] The Impacted Asset is added to the Threat Scenario Table. 
 
[IMAGE alt='' src='']

You can also drag and drop the Impacted Assets from the Containment tree to the Threat Scenario Table.

##### Threat Scenario Table Example

The maximum value among all the attacks paths for the given threat scenario is considered as the Aggregated Attack Feasibility Rating.

[IMAGE alt='' src='']

#### INFO: References

References

- ISO/SAE 21434:2021 Road vehicles-Cybersecurity engineering
- ISO 26262-1:2018 Road vehicles-Functional safety

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="bb292072-80c4-4b3d-8518-52eb6bb7f816"><ac:parameter ac:name="maxLevel">5</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Threat Scenario</strong></p><p><span style="color: rgb(62,63,64);">Potential cause of compromise of cybersecurity properties of one or more assets  in order to realize a damage scenario.</span></p><p><strong>Attack Path</strong></p><p>Set of deliberate actions to realize a threat scenario.</p><p><strong>Failure</strong></p><p>Termination of an intended behavior of an element or an item due to a fault manifestation.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Threat Scenario</h3><p>To create a Threat Scenario</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Containment tree, right-click<span> </span><strong>Threat Scenario</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Threat Scenario</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="3 DirectlySelectThreatScenario.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword <strong>threat</strong> and then select<span> </span><strong>Threat Scenario.<br /><br /><ac:image><ri:attachment ri:filename="2 WriteThreat.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong></li></ul></li><li><span style="color: rgb(62,63,64);">Name the created Threat Scenario in the Containment tree and press Enter. The Threat Scenario has the prefix <span><strong>D</strong></span><strong>S</strong>,<span> </span>which denotes that the created element is a Threat Scenario; the number<span> </span><strong style="text-align: left;">1</strong> indicates that it is the first Threat Scenario created.<br /><br /><ac:image><ri:attachment ri:filename="4 ThreatScenarioCreated.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span></li></ol><h3><span style="color: rgb(62,63,64);">Creating a Threat Scenario Table<br /></span></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8bfaf83d-4424-4723-83be-76cbbc167205"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color: rgb(23,43,77);">, then a<span> </span><strong>Threat Scenario Table<span> </span></strong>already exists in the<span> <strong>1.2 Threat Scenarios</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create a<span> </span><span style="color: rgb(62,63,64);">Threat Scenario<span> </span></span>Table</p><hr /><ol><li><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">In the Containment tree, right-click</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><strong><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">Threat Scenario</ac:inline-comment-marker></strong><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">and select</ac:inline-comment-marker><strong><span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">Create Diagram.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color: rgb(62,63,64);">In the dialog, expand <strong>ISO</strong> <strong>21434 </strong>and select <strong>Threat Scenario Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Threat Scenario Table_Menu.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword threat and then select<span> </span><strong>Threat Scenario Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="196"><ri:attachment ri:filename="Threat Scenario Table_Search.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong>The Threat Scenario Table is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Threat Scenario Table.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></li></ul></li></ol><h3>Adding a Threat Scenario to the Threat Scenario Table</h3><p>To add a new Threat Scenario to the Threat Scenario Table</p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Threat Scenario Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add New. </strong><span style="color: rgb(62,63,64);">A row is added in the Threat Scenario Table, which shows the new Threat Scenario.</span><strong style="text-align: left;"><br /><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">In the newly created Threat Scenario's row and the <strong>Name </strong>column, double-click the designated cell to name the Threat Scenario.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="2 AfterAddingThreatScenario.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></strong><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color: rgb(62,63,64);">To add an existing Threat Scenario to the Threat Scenario Table</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">In the Threat Scenario Table, click</span><span style="color: rgb(62,63,64);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="3 ClickAddExisting.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></strong></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Threat Scenario</strong> dialog, select the required Threat Scenario. A row is added to the Threat Scenario Table, showing the existing Threat Scenario.<br /><br /><ac:image><ri:attachment ri:filename="Threat Scenario Dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);"> In the existing Threat Scenario's row and the <strong>Name </strong>column, double-click the designated cell to rename the Threat Scenario.<br /><br /><strong style="text-align: left;"><ac:image ac:height="249"><ri:attachment ri:filename="2 AfterAddingThreatScenario.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></strong><br /></span></li></ol><h3><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="668ed2cf-1efb-41ff-8f28-6c23538b037a">Creating a custom threat type</ac:inline-comment-marker></span></h3><p><span style="color: rgb(62,63,64);">To create a custom threat type</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">Create a general threat scenario as defined in the <ac:link ac:anchor="Creating a Threat Scenario"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ac:link> section.</span></li><li><span style="color: rgb(62,63,64);">Open the Specification dialog of the newly created threat scenario in the <strong>Expert</strong> mode.</span></li><li><span style="color: rgb(62,63,64);">Set the <strong>Is Abstract</strong> property to <em>True</em>.<br /><br /><ac:image><ri:attachment ri:filename="Specification Dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br />The newly created threat scenario will now be displayed in italics in the Containment tree and will be available under the <strong>custom </strong>package in the Select Threat Type dialog. <br /><br /></span><ac:image><ri:attachment ri:filename="Custom Threat Type.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6844d142-575d-4c9d-be5f-b2833b703c80"><ac:rich-text-body><p><span style="color: rgb(62,63,64);"><span style="color: rgb(23,43,77);">Threat Types are displayed by default in the TARA analysis as Threat Scenarios. To prevent that, you must create the Threat Types in a dedicated package or library.</span></span></p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="86496062-e728-4cc2-a157-ff38237b101e">Creating custom packages for custom-created threat types</ac:inline-comment-marker></h3><p>You can group the custom-created threat types by creating custom packages and placing them under the custom packages. <span>To create a new package, you must create a generalization set of the required custom threat types. </span><span>To learn more about creating a generalization set, refer to </span><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Generalization set" /></ac:link><span>.<br /><br /></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Generalization set_Threat Type.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Select Threat Type dialog showing the custom threat types places under the custom created packages.<br /><br /></h6><p>The following example displays a typical scenario in which a generalization set can be created.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Generalizarion Example.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Generalization set example.</h6><h3><ac:inline-comment-marker ac:ref="b2a3beea-cf3f-4e8e-877a-7e54200c78ee">Creating subcategory for the custom-created threat type</ac:inline-comment-marker></h3><p><span style="letter-spacing: 0.0px;">You can also create subcategories of the custom-created threat types. Doing so will create a nesting effect in the Select Threat Type dialog.<br /><br /></span></p><p style="text-align: center;"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="Nesting Effect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">Select Threat Type dialog showing the nesting effect due to subcategorization of the threat types.</h6><p><br /></p><p>To create subcategories of the custom-created threat type</p><hr /><ol><li>In the <span style="color: rgb(62,63,64);">Specification dialog of the newly created threat Type, click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image> in the<strong style="text-align: left;"> <span style="color: rgb(23,43,77);">Base Classifier</span></strong> property.<br /><br /><ac:image><ri:attachment ri:filename="Custom Subcategory for threat type.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></span></li><li><span style="color: rgb(62,63,64);">Select any parent threat type under which you want to place the newly created custom threat type.<br /><br /><ac:image><ri:attachment ri:filename="Select Class dialog.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span></li></ol><h3>Adding a Threat Type</h3><p><span style="color: rgb(62,63,64);">To add a Threat Type</span></p><hr /><ol><li><span style="color: rgb(62,63,64);">Double-click the designated cell in the <strong>Threat Type </strong></span><span style="color: rgb(62,63,64);">column <ac:inline-comment-marker ac:ref="c03df453-8eef-4927-9271-99fd6a3835b7">and</ac:inline-comment-marker> the required Threat Scenario's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Edit_Button_Three_Dots.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></span></span></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Threat Type </strong>dialog, <ac:inline-comment-marker ac:ref="2d78d067-b411-4118-8db0-7620df8624af">select a threat type(s)</ac:inline-comment-marker> from either the <strong><a href="https://en.wikipedia.org/wiki/STRIDE_%28security%29"> STRIDE </a></strong>or <strong><a href="https://unece.org/sites/default/files/2023-02/R155e%20%282%29.pdf"> UNECE </a></strong>package. You can also select a custom-created threat type.<br /><br /><ac:image><ri:attachment ri:filename="Nesting Effect.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span><br /><span style="color: rgb(62,63,64);">The Threat Type will be added to the Threat Scenarios Table.</span><br /><br /><ac:image><ri:attachment ri:filename="Threat Type Applied.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></li></ol><h3>Adding an Attack Path</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c581d357-c34b-43b7-a2cb-efc6411e9256"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">You can add multiple attack paths for a given Threat Scenario.</span></p></ac:rich-text-body></ac:structured-macro><p>To add an Attack Path</p><hr /><ol><li><span style="color: rgb(62,63,64);">Double-click the designated cell in the <strong>Attack Path </strong></span><span style="color: rgb(62,63,64);">column and the required Threat Scenario's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Three dot-Attack Path Steps.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">From <ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">Select Elements</ac:inline-comment-marker></strong><strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85"> </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">dialog, select Attack</ac:inline-comment-marker> Path.<br /><br /><ac:image><ri:attachment ri:filename="Select Element_Attack Path.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span><span style="color: rgb(62,63,64);"><br /><ac:inline-comment-marker ac:ref="ed16e46c-9c6e-4aea-8b13-97eab5097f69">The Attack Path is added to the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Attack Path added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br style="text-align: left;" /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a5f66ac-ca84-4422-a7e4-11e5ddccf5bb"><ac:rich-text-body><ul><li>You can also drag and drop the Attack Paths from the Containment tree to the Threat Scenario Table.</li><li>The Aggregated Attack Feasibility Rating is added automatically after you add the Attack Path.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Adding a Failure</h3><p>To add a Failure</p><hr /><ol><li><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">Double-click the designated cell in the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">Failure </ac:inline-comment-marker></strong></span><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">column and the required Threat Scenario's row and cl</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">ick</ac:inline-comment-marker> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Adding Failure_Three dot.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Class</strong><strong> </strong>dialog, select Failure.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectFailureWindow_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span><span style="color: rgb(62,63,64);"><br /><ac:inline-comment-marker ac:ref="40a0d885-7391-4f2a-9357-e7d0abf552bf">The Failure is now shown in the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Failure added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="88ded4ef-a5bc-47f5-96bf-2d2829c714ab"><ac:rich-text-body><p>You can also drag and drop the Failure modes from the Containment tree to the Threat Scenario Table.</p></ac:rich-text-body></ac:structured-macro><h3>Adding an Impacted Asset</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="415c82df-db8d-4115-a637-19735c45920e"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">You can add multiple Impacted Assets for a given Threat Scenario.</span></p></ac:rich-text-body></ac:structured-macro><p>To add an Impacted Asset</p><hr /><ol><li><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">Double-click the designated cell in the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">Impacted Asset </ac:inline-comment-marker></strong></span><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">column and the required Threat Scenario's row and cl</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">ick</ac:inline-comment-marker> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(62,63,64);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Adding Impacted Assets.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /><br /></li><li><span style="color: rgb(62,63,64);">From the <strong>Select Element</strong><strong> </strong>dialog, select Impacted Asset.<br /><br /><ac:image><ri:attachment ri:filename="1 SelectAssetWindow_v2.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span><span style="color: rgb(62,63,64);"><br /><ac:inline-comment-marker ac:ref="e96f5570-448a-43bc-8157-2a3e4b973c59">The Impacted Asset is added to the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Impacted Asset added.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b020098c-6c00-47ee-b5df-0adb690f9033"><ac:rich-text-body><p>You can also drag and drop the Impacted Assets from the Containment tree to the Threat Scenario Table.</p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="4c718e6a-c1af-4784-8d55-2e7af05d5dfa">Threat Scenario Table Example</ac:inline-comment-marker></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a22e06b7-0a8c-4b90-a2da-d78dd453ed8d"><ac:rich-text-body><p>The maximum value among all the attacks paths for the given threat scenario is considered as the Aggregated Attack Feasibility Rating.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="Threat Scenario Example.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Threat  scenario" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="913c17ef-41fc-4abc-9236-e55fcf09aa7a"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO/SAE 21434:2021 Road vehicles-Cybersecurity engineering</a></li><li><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO 26262-1:2018 Road vehicles-Functional safety</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466482 space=CSRA2024xR1 version=2 -->
## PAGE 00068: Traceability maps

- page_id: `170466482`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466482/Traceability+maps
- version_number: 2
- version_date: `2024-05-08T14:01:15.782+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > Additional features
- labels: []

### NORMALIZED CONTENT

**On this page**

4

Traceability maps allow you to increase the traceability between model elements. You can use this type of map to review and analyze the relations between a Safety Analysis Item or an FMEA Item and the entire model. A visual analysis is shown by updating and rendering the dependency tree of the selected element according to predefined dependency criteria.

The Safety and Reliability Analyzer plugin allows you to create two types of predefined traceability maps:

- Safety Analysis Traceability Map
- Reliability Analysis Traceability Map

A Safety Analysis Traceability Map and a Reliability Analysis Traceability Map work the same way; however, they have different context and predefined relation criteria. Essentially, these maps trace relations of different types of model elements. A Safety Analysis Traceability Map allows you to trace the relations between a Safety Analysis Item and other safety analysis specific model elements. A Reliability Analysis Traceability Map allows you to trace the relations between an FMEA Item and other reliability analysis specific model elements.

On this page, you will learn how to [CONFLUENCE_PAGE title='Traceability maps' space='CSRA2024xR1'], and define the relations between model elements in the [CONFLUENCE_PAGE title='Traceability maps' space='CSRA2024xR1'].

##### creating_mapsCreating traceability maps

To keep your model clean and simple, you should create a traceability map under the element (Safety Analysis Item or FMEA Item depending on a traceability map), which automatically becomes the **Context** of the map. Otherwise, you need to manually select the **Context** value.

#### NOTE: Note

Note

A traceability map must have a context. A map with no context does not contain any data. The****valid value of the **Context** property is any Safety Analysis Item or FMEA Item (depending on a traceability map) in your model.

The default values of all the properties of a map are specified automatically, but you can change them, if needed.

To create a Safety Analysis Traceability Map

1. Do one of the following:
  - Select the desired Safety Analysis Item, and click the Create Diagram button on the main toolbar.
  - Right-click the desired Safety Analysis Item, and select Create Diagram .
2. Select Safety Analysis Traceability Map under the Safety and Reliability Analysis group.
3. If needed, change the predefined values of the map properties. You can do this in the same way you would [CONFLUENCE_PAGE title='Specifying criteria, layout, and depth' space='MD2024xR1'] .

To create a Reliability Analysis Traceability Map

1. Do one of the following:
  - Select the desired FMEA Item, and click the Create Diagram button on the main toolbar.
  - Right-click the desired FMEA Item, and select Create Diagram .
2. Select Reliability Analysis Traceability Map under the Safety and Reliability Analysis group.
3. If needed, change the predefined values of the map properties. You can do this in the same way you would [CONFLUENCE_PAGE title='Specifying criteria, layout, and depth' space='MD2024xR1'] .

After completing the steps above, a Safety Analysis Traceability Map or Reliability Analysis Traceability Map is created. The following figure illustrates the predefined Safety Analysis Traceability Map of the sample insulin pump model that comes with Cameo Safety and Reliability Analyzer plugin. The map shows the relations between a specific Safety Analysis Item of the model and Harm, Hazard, Hazardous Situation, and other safety analysis and design elements.

[IMAGE alt='' src='']

###### This Predefined Safety Analysis Traceability Map displays the relations between the *Discharged battery leads to coma or death* Safety Analysis Item and other model elements.

By default, traceability maps show the following relations between the context element and other elements of your model:

| Safety Analysis Traceability Map | Reliability Analysis Traceability Map |
| --- | --- |
| Safety Analysis Item -> Effected Design Elements | FMEA Item -> Current Design Control |
| Safety Analysis Item -> New Design Elements | FMEA Item -> Cause of Failure |
| Safety Analysis Item -> Requirements | FMEA Item -> Effect of Failure |
| Safety Analysis Item -> FMEA Item | FMEA Item -> Failure Mode |
| Safety Analysis Item -> Hazard | FMEA Item -> Design Item |
| Safety Analysis Item -> Hazardous Situation | FMEA Item -> Detection Control |
| Safety Analysis Item -> Harm | FMEA Item -> Prevention Control |
| Safety Analysis Item -> Sequence of Events | FMEA Item -> Safety Analysis Item |

However, you can change the relations displayed in the map by customizing **Relation Criteria** in the Expert mode.

##### expert_modeManipulations in the Expert mode

If the default relations displayed in a traceability map are not sufficient, the Expert mode allows you to create new operations to represent relations between desired model elements, or to customize the existing operations.

To create a new operation to represent a relation between model elements

1. Click [ATTACHMENT filename='3dot_button_long.png'] next to the Relation Criteria box in the Criteria area of a map.
2. In the Relation Criteria dialog, click [ATTACHMENT filename='expert.png'] to enable the Expert mode.
3. On the left side of the dialog, click Create operation .
4. In the Operations area of the dialog, select the Filter operation.

###### [IMAGE alt='' src=''] 
In the Expert mode, the **Relation Criteria** dialog allows you to create a new Filter operation, and define it to represent a desired relation.

After following the above procedure, a new Filter operation is created. Now, you can specify its properties to represent the desired relation between model elements. For more information about the properties of a Filter operation, see [CONFLUENCE_PAGE title='Built-in operations' space='MD2024xR1'].

**Sample model**

The model used for the figures of this page is the *Medical FMEA and Hazard Analysis* sample model that comes with Cameo Safety and Reliability Analyzer plugin. To open this model do one of the following

- Download [ATTACHMENT filename='Medical FMEA and Hazard Analysis.mdzip'] .
- Open the model from the < install_root >\ samples \ Safety and Reliability Analysis directory.

**Related pages**

- [CONFLUENCE_PAGE title='Additional features' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Safety and Reliability Coverage Analysis' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Generating reports' space='CSRA2024xR1']
  - [CONFLUENCE_PAGE title='Linking Failure Modes to model elements' space='CSRA2024xR1']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="efc9fe5a-df08-4bc6-ad52-e2574ba5e6b7"><ac:parameter ac:name="maxLevel">4</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(0,0,0);">Traceability maps allow you to increase the traceability between model elements</span>. You can use this type of map to review and analyze the relations between a Safety Analysis Item or an FMEA Item and the entire model. A visual analysis is shown by updating and rendering the dependency tree of the selected element according to predefined dependency criteria.</p><p>The Safety and Reliability Analyzer plugin allows you to create two types of predefined traceability maps:</p><ul><li>Safety Analysis Traceability Map</li><li>Reliability Analysis Traceability Map</li></ul><p>A Safety Analysis Traceability Map and a Reliability Analysis Traceability Map work the same way; however, they have different context and predefined relation criteria. Essentially, these maps trace relations of different types of model elements. A Safety Analysis Traceability Map allows you to trace the relations between a Safety Analysis Item and other safety analysis specific model elements. A Reliability Analysis Traceability Map allows you to trace the relations between an FMEA Item and other reliability analysis specific model elements.</p><p>On this page, you will learn how to <ac:link ac:anchor="creating_maps"><ac:plain-text-link-body><![CDATA[create traceability maps]]></ac:plain-text-link-body><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ac:link>, and define the relations between model elements in the <ac:link ac:anchor="expert_mode"><ac:plain-text-link-body><![CDATA[Expert mode]]></ac:plain-text-link-body><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ac:link>.<br /> </p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="829b397b-ed2a-496a-bbcc-936157c1ff74"><ac:parameter ac:name="">creating_maps</ac:parameter></ac:structured-macro>Creating traceability maps</h3><p>To keep your model clean and simple, you should create a traceability map under the element (Safety Analysis Item or FMEA Item depending on a traceability map), which automatically becomes the <strong>Context</strong> of the map. Otherwise, you need to manually select the <strong>Context</strong> value. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="75b64f28-d26e-4957-b016-fb6418b0201a"><ac:parameter ac:name="title">Note</ac:parameter><ac:rich-text-body><p>A traceability map must have a context. A map with no context does not contain any data. The<strong> </strong>valid value of the <strong>Context</strong> property is any Safety Analysis Item or FMEA Item (depending on a traceability map) in your model.</p></ac:rich-text-body></ac:structured-macro><p>The default values of all the properties of a map are specified automatically, but you can change them, if needed.</p><p><br /></p><p>To create a Safety Analysis Traceability Map</p><hr /><ol><li>Do one of the following:<br /><ul><li>Select the desired Safety Analysis Item, and click the <strong>Create Diagram</strong> button on the main toolbar.</li><li>Right-click the desired Safety Analysis Item, and select <strong>Create Diagram</strong>. </li></ul></li><li>Select <strong>Safety Analysis Traceability Map</strong> under the <strong>Safety and Reliability Analysis</strong> group.</li><li>If needed, change the predefined values of the map properties. You can do this in the same way you would <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specifying criteria, layout, and depth" /><ac:plain-text-link-body><![CDATA[change the properties of a Relation Map]]></ac:plain-text-link-body></ac:link>.</li></ol><p><br /></p><p>To create a Reliability Analysis Traceability Map</p><hr /><ol><li>Do one of the following:<br /><ul><li>Select the desired FMEA Item, and click the <strong>Create Diagram</strong> button on the main toolbar.</li><li>Right-click the desired FMEA Item, and select <strong>Create Diagram</strong>. </li></ul></li><li>Select <strong>Reliability Analysis Traceability Map</strong> under the <strong>Safety and Reliability Analysis</strong> group.</li><li>If needed, change the predefined values of the map properties. You can do this in the same way you would <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Specifying criteria, layout, and depth" /><ac:plain-text-link-body><![CDATA[change the properties of a Relation Map]]></ac:plain-text-link-body></ac:link>.</li></ol><p><br />After completing the steps above, a Safety Analysis Traceability Map or Reliability Analysis Traceability Map is created. The following figure illustrates the predefined Safety Analysis Traceability Map of the sample insulin pump model that comes with Cameo Safety and Reliability Analyzer plugin. The map shows the relations between a specific Safety Analysis Item of the model and Harm, Hazard, Hazardous Situation, and other safety analysis and design elements.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="safety_analysis_traceability_map.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ri:attachment></ac:image></p><h6 style="text-align: center;">This Predefined Safety Analysis Traceability Map displays the relations between the <em>Discharged battery leads to coma or death</em> Safety Analysis Item and other model elements.</h6><p>By default, traceability maps show the following relations between the context element and other elements of your model:</p><table><colgroup class=""><col class="" /><col class="" /></colgroup><tbody class=""><tr class=""><th>Safety Analysis Traceability Map</th><th>Reliability Analysis Traceability Map</th></tr><tr class=""><td><p>Safety Analysis Item -&gt; Effected Design Elements</p></td><td>FMEA Item -&gt; Current Design Control</td></tr><tr class=""><td><p>Safety Analysis Item -&gt; New Design Elements</p></td><td>FMEA Item -&gt; Cause of Failure</td></tr><tr class=""><td><p>Safety Analysis Item -&gt; Requirements</p></td><td>FMEA Item -&gt; Effect of Failure</td></tr><tr class=""><td><p>Safety Analysis Item -&gt; FMEA Item</p></td><td>FMEA Item -&gt; Failure Mode</td></tr><tr class=""><td><p>Safety Analysis Item -&gt; Hazard</p></td><td>FMEA Item -&gt; Design Item</td></tr><tr class=""><td colspan="1">Safety Analysis Item -&gt; Hazardous Situation</td><td colspan="1">FMEA Item -&gt; Detection Control</td></tr><tr class=""><td><p>Safety Analysis Item -&gt; Harm</p></td><td>FMEA Item -&gt; Prevention Control</td></tr><tr class=""><td><p>Safety Analysis Item -&gt; Sequence of Events</p></td><td>FMEA Item -&gt; Safety Analysis Item</td></tr></tbody></table><p>However, you can change the relations displayed in the map by customizing <strong>Relation Criteria</strong> in the Expert mode.</p><h3><br /><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9169be20-f361-4c63-ab17-167c57ecbc5b"><ac:parameter ac:name="">expert_mode</ac:parameter></ac:structured-macro>Manipulations in the Expert mode</h3><p>If the default relations displayed in a traceability map are not sufficient, the Expert mode allows you to create new operations to represent relations between desired model elements, or to customize the existing operations.</p><p><br /></p><p>To create a new operation to represent a relation between model elements</p><hr /><ol><li>Click <ac:image><ri:attachment ri:filename="3dot_button_long.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ri:attachment></ac:image> next to the <strong>Relation Criteria</strong> box in the <strong>Criteria</strong> area of a map.</li><li>In the <strong>Relation Criteria</strong> dialog, click <ac:image><ri:attachment ri:filename="expert.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ri:attachment></ac:image> to enable the Expert mode.</li><li>On the left side of the dialog, click <strong>Create operation</strong>.</li><li>In the <strong>Operations</strong> area of the dialog, select the <strong>Filter</strong> operation.</li></ol><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="creating_filter_operation.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Traceability maps" /></ri:attachment></ac:image><br />In the Expert mode, the <strong>Relation Criteria</strong> dialog allows you to create a new Filter operation, and define it to represent a desired relation.  </h6><p>After following the above procedure, a new Filter operation is created. Now, you can specify its properties to represent the desired relation between model elements. For more information about the properties of a Filter operation, see <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Built-in operations" /></ac:link>.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Sample model</strong></p><p>The model used for the figures of this page is the <em>Medical FMEA and Hazard Analysis</em> sample model that comes with Cameo Safety and Reliability Analyzer plugin. To open this model do one of the following</p><ul><li>Download <ac:link><ri:attachment ri:filename="Medical FMEA and Hazard Analysis.mdzip"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Sample models" /></ri:attachment></ac:link>.</li><li>Open the model from the &lt;<em style="text-align: left;">install_root</em>&gt;\<em>samples</em>\<em>Safety and Reliability Analysis</em> directory.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Additional features" /></ac:link><ul><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Safety and Reliability Coverage Analysis" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Generating reports" /></ac:link></li><li><ac:link><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Linking Failure Modes to model elements" /></ac:link></li></ul></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170466607 space=CSRA2024xR1 version=2 -->
## PAGE 00069: Tracking ISO 26262 properties

- page_id: `170466607`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466607/Tracking+ISO+26262+properties
- version_number: 2
- version_date: `2024-05-08T14:01:16.537+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety
- labels: []

### NORMALIZED CONTENT

You can track ISO 26262 properties in [CONFLUENCE_PAGE title='Relation Map' space='MD2024xR1']. To do that, specify the relation criteria by using the [CONFLUENCE_PAGE title='Using Simple Navigation' space='MD2024xR1'] which allows you to select ISO 26262 properties.

To track ISO 26262 properties

1. [CONFLUENCE_PAGE title='Creating relation map' space='MD2024xR1'].
2. In the **Criteria** area, [CONFLUENCE_PAGE title='Changing the context' space='MD2024xR1'] of the relation Map.
3. In the same area, click [IMAGE alt='' src=''] next to the **Relation Criteria** box.
4. On the left side of the the **Relation Criteria** dialog, select the Simple Navigation operation.
5. In the Simple Navigation operation specification area, select the ISO 26262 properties you want to track as displayed in the figure below.

[IMAGE alt='' src='']

###### Specifying relation criteria for a Relation map to track ISO 26262 properties.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can track ISO 26262 properties in <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Relation Map" /><ac:plain-text-link-body><![CDATA[Relation Maps]]></ac:plain-text-link-body></ac:link>. To do that, specify the relation criteria by using the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Simple Navigation" /><ac:plain-text-link-body><![CDATA[Simple Navigation operation]]></ac:plain-text-link-body></ac:link> which allows you to select ISO 26262 properties.</p><p><span style="color: rgb(62,63,64);"><br /></span></p><p><span style="color: rgb(62,63,64);">To track ISO 26262 properties</span></p><hr /><ol><li><span style="color: rgb(62,63,64);"><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Creating relation map" /><ac:plain-text-link-body><![CDATA[Create a Relation map]]></ac:plain-text-link-body></ac:link>.</span></li><li><span style="color: rgb(62,63,64);">In the <strong>Criteria</strong> area, <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Changing the context" /><ac:plain-text-link-body><![CDATA[specify the context element]]></ac:plain-text-link-body></ac:link> of the relation Map.</span></li><li><span style="color: rgb(62,63,64);">In the same area, click <ac:image ac:thumbnail="true" ac:height="16"><ri:attachment ri:filename="3dot_long.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Buttons" /></ri:attachment></ac:image> next to the <strong>Relation Criteria</strong> box.</span></li><li><span style="color: rgb(62,63,64);">On the left side of the the <strong>Relation Criteria</strong> dialog, select the Simple Navigation operation.</span></li><li><span style="color: rgb(62,63,64);">In the Simple Navigation operation specification area, select the ISO 26262 properties you want to <ac:inline-comment-marker ac:ref="c9cadf94-1ced-4841-a7f7-da557a63b116">track</ac:inline-comment-marker> as displayed in the figure below.<br class="_mce_tagged_br" /><br /></span></li></ol><p style="text-align: center;"><ac:image><ri:attachment ri:filename="tracking_ISO_26262_properties.png"><ri:page ri:space-key="CSRA2024xR1" ri:content-title="Tracking ISO 26262 properties" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Specifying relation criteria for a Relation map to track ISO 26262 properties.</h6>
````

<!--NOMAGIC_PAGE id=170466597 space=CSRA2024xR1 version=2 -->
## PAGE 00070: Validation Rules

- page_id: `170466597`
- space_key: `CSRA2024xR1`
- source_url: https://docs.nomagic.com/spaces/CSRA2024xR1/pages/170466597/Validation+Rules
- version_number: 2
- version_date: `2025-05-05T11:24:31.182+02:00`
- ancestors: Cameo Safety and Reliability Analyzer > ISO 26262 Functional Safety
- labels: []

### NORMALIZED CONTENT

To learn more about ISO 26262 Plugin validation rules, see:

The validation rules do not replace a qualified use of the tool according to the activities described in the ISO 26262.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To learn more about ISO 26262 Plugin validation rules, see:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="0ffe147d-38fd-4850-934a-aa585d0d853e" /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f2832d9e-5f87-4403-b4a2-b1e7244ae321"><ac:rich-text-body><p><span style="color: rgb(61,61,61);">The validation rules do not replace a qualified use of the tool according to the activities described in the ISO 26262.</span></p></ac:rich-text-body></ac:structured-macro>
````
