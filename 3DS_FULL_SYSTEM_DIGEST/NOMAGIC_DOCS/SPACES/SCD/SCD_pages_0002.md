# NOMAGIC DOCUMENTATION SPACE: Systems Cybersecurity Designer

<!--NOMAGIC_SPACE key=SCD chunk=2 -->

<!--NOMAGIC_PAGE id=249574492 space=SCD version=5 -->
## PAGE 00150: Threat  scenario

- page_id: `249574492`
- space_key: `SCD`
- source_url: https://docs.nomagic.com/spaces/SCD/pages/249574492/Threat+scenario
- version_number: 5
- version_date: `2025-11-18T11:08:03.551+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

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

1. Create a general threat scenario as defined in the section.
2. Open the Specification dialog of the newly created threat scenario in the **Expert** mode.
3. Set the **Is Abstract** property to *True*. 
 
[IMAGE alt='' src=''] 
 
The newly created threat scenario will now be displayed in italics in the Containment tree and will be available under the **custom**package in the Select Threat Type dialog. [ATTACHMENT filename='Custom Threat Type.png']

Threat Types are displayed by default in the TARA analysis as Threat Scenarios. To prevent that, you must create the Threat Types in a dedicated package or library.

##### Creating custom packages for custom-created threat types

You can group the custom-created threat types by creating custom packages and placing them under the custom packages. To create a new package, you must create a generalization set of the required custom threat types.To learn more about creating a generalization set, refer to[CONFLUENCE_PAGE title='Generalization set' space='MED']t.

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p><strong>Threat Scenario</strong></p><p><span style="color:var(--ds-text,#333333);">Potential cause of compromise of cybersecurity properties of one or more assets  in order to realize a damage scenario.</span></p><p><strong>Attack Path</strong></p><p>Set of deliberate actions to realize a threat scenario.</p><p><strong>Failure</strong></p><p>Termination of an intended behavior of an element or an item due to a fault manifestation.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Threat Scenario</h3><p>To create a Threat Scenario</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<span> </span><strong>Threat Scenario</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Threat Scenario</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="3 DirectlySelectThreatScenario.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword <strong>threat</strong> and then select<span> </span><strong>Threat Scenario.<br /><br /><ac:image><ri:attachment ri:filename="2 WriteThreat.png" /></ac:image><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Threat Scenario in the Containment tree and press Enter. The Threat Scenario has the prefix <span><strong>D</strong></span><strong>S</strong>,<span> </span>which denotes that the created element is a Threat Scenario; the number<span> </span><strong style="text-align: left;">1</strong> indicates that it is the first Threat Scenario created.<br /><br /><ac:image><ri:attachment ri:filename="4 ThreatScenarioCreated.png" /></ac:image><br /></span></li></ol><h3><span style="color:var(--ds-text,#333333);">Creating a Threat Scenario Table<br /></span></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8bfaf83d-4424-4723-83be-76cbbc167205"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color:var(--ds-text,#172b4d);">, then a<span> </span><strong>Threat Scenario Table<span> </span></strong>already exists in the<span> <strong>1.2 Threat Scenarios</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create a<span> </span><span style="color:var(--ds-text,#333333);">Threat Scenario<span> </span></span>Table</p><hr /><ol><li><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">In the Containment tree, right-click</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><strong><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">Threat Scenario</ac:inline-comment-marker></strong><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">and select</ac:inline-comment-marker><strong><span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">Create Diagram.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png" /></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO</strong> <strong>21434 </strong>and select <strong>Threat Scenario Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Threat Scenario Table_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword threat and then select<span> </span><strong>Threat Scenario Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="196"><ri:attachment ri:filename="Threat Scenario Table_Search.png" /></ac:image><br /><br /></strong>The Threat Scenario Table is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Threat Scenario Table.png" /></ac:image></li></ul></li></ol><h3>Adding a Threat Scenario to the Threat Scenario Table</h3><p>To add a new Threat Scenario to the Threat Scenario Table</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Threat Scenario Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New. </strong><span style="color:var(--ds-text,#333333);">A row is added in the Threat Scenario Table, which shows the new Threat Scenario.</span><strong style="text-align: left;"><br /><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">In the newly created Threat Scenario's row and the <strong>Name </strong>column, double-click the designated cell to name the Threat Scenario.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="2 AfterAddingThreatScenario.png" /></ac:image></strong><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color:var(--ds-text,#333333);">To add an existing Threat Scenario to the Threat Scenario Table</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Threat Scenario Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="3 ClickAddExisting.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Threat Scenario</strong> dialog, select the required Threat Scenario. A row is added to the Threat Scenario Table, showing the existing Threat Scenario.<br /><br /><ac:image><ri:attachment ri:filename="Threat Scenario Dialog.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);"> In the existing Threat Scenario's row and the <strong>Name </strong>column, double-click the designated cell to rename the Threat Scenario.<br /><br /><strong style="text-align: left;"><ac:image ac:height="249"><ri:attachment ri:filename="2 AfterAddingThreatScenario.png" /></ac:image></strong><br /></span></li></ol><h3><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="668ed2cf-1efb-41ff-8f28-6c23538b037a">Creating a custom threat type</ac:inline-comment-marker></span></h3><p><span style="color:var(--ds-text,#333333);">To create a custom threat type</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Create a general threat scenario as defined in the <ac:link ac:anchor="Creating a Threat Scenario" /> section.</span></li><li><span style="color:var(--ds-text,#333333);">Open the Specification dialog of the newly created threat scenario in the <strong>Expert</strong> mode.</span></li><li><span style="color:var(--ds-text,#333333);">Set the <strong>Is Abstract</strong> property to <em>True</em>.<br /><br /><ac:image><ri:attachment ri:filename="Specification Dialog.png" /></ac:image><br /><br />The newly created threat scenario will now be displayed in italics in the Containment tree and will be available under the <strong>custom </strong>package in the Select Threat Type dialog. <br /><br /></span><ac:image><ri:attachment ri:filename="Custom Threat Type.png" /></ac:image><br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6844d142-575d-4c9d-be5f-b2833b703c80"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">Threat Types are displayed by default in the TARA analysis as Threat Scenarios. To prevent that, you must create the Threat Types in a dedicated package or library.</span></span></p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="86496062-e728-4cc2-a157-ff38237b101e">Creating custom packages for custom-created threat types</ac:inline-comment-marker></h3><p>You can group the custom-created threat types by creating custom packages and placing them under the custom packages. <span>To create a new package, you must create a generalization set of the required custom threat types. </span><span>To learn more about creating a generalization set, refer to </span><ac:link><ri:page ri:space-key="MED" ri:content-title="Generalization set" /><ac:plain-text-link-body><![CDATA[Generalization se]]></ac:plain-text-link-body></ac:link>t<span>.<br /><br /></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Generalization set_Threat Type.png" /></ac:image></p><h6 style="text-align: center;">Select Threat Type dialog showing the custom threat types places under the custom created packages.<br /><br /></h6><p>The following example displays a typical scenario in which a generalization set can be created.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Generalizarion Example.png" /></ac:image></p><h6 style="text-align: center;">Generalization set example.</h6><h3><ac:inline-comment-marker ac:ref="b2a3beea-cf3f-4e8e-877a-7e54200c78ee">Creating subcategory for the custom-created threat type</ac:inline-comment-marker></h3><p><span style="letter-spacing: 0.0px;">You can also create subcategories of the custom-created threat types. Doing so will create a nesting effect in the Select Threat Type dialog.<br /><br /></span></p><p style="text-align: center;"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="Nesting Effect.png" /></ac:image></span></p><h6 style="text-align: center;">Select Threat Type dialog showing the nesting effect due to subcategorization of the threat types.</h6><p><br /></p><p>To create subcategories of the custom-created threat type</p><hr /><ol><li>In the <span style="color:var(--ds-text,#333333);">Specification dialog of the newly created threat Type, click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image> in the<strong style="text-align: left;"> <span style="color:var(--ds-text,#172b4d);">Base Classifier</span></strong> property.<br /><br /><ac:image><ri:attachment ri:filename="Custom Subcategory for threat type.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">Select any parent threat type under which you want to place the newly created custom threat type.<br /><br /><ac:image><ri:attachment ri:filename="Select Class dialog.png" /></ac:image><br /></span></li></ol><h3>Adding a Threat Type</h3><p><span style="color:var(--ds-text,#333333);">To add a Threat Type</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Double-click the designated cell in the <strong>Threat Type </strong></span><span style="color:var(--ds-text,#333333);">column <ac:inline-comment-marker ac:ref="c03df453-8eef-4927-9271-99fd6a3835b7">and</ac:inline-comment-marker> the required Threat Scenario's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Edit_Button_Three_Dots.png" /></ac:image><br /><br /></span></span></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Threat Type </strong>dialog, <ac:inline-comment-marker ac:ref="2d78d067-b411-4118-8db0-7620df8624af">select a threat type(s)</ac:inline-comment-marker> from either the <strong><a href="https://en.wikipedia.org/wiki/STRIDE_%28security%29"> STRIDE </a></strong>or <strong><a href="https://unece.org/sites/default/files/2023-02/R155e%20%282%29.pdf"> UNECE </a></strong>package. You can also select a custom-created threat type.<br /><br /><ac:image><ri:attachment ri:filename="Nesting Effect.png" /></ac:image><br /></span><br /><span style="color:var(--ds-text,#333333);">The Threat Type will be added to the Threat Scenarios Table.</span><br /><br /><ac:image><ri:attachment ri:filename="Threat Type Applied.png" /></ac:image></li></ol><h3>Adding an Attack Path</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c581d357-c34b-43b7-a2cb-efc6411e9256"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">You can add multiple attack paths for a given Threat Scenario.</span></p></ac:rich-text-body></ac:structured-macro><p>To add an Attack Path</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Double-click the designated cell in the <strong>Attack Path </strong></span><span style="color:var(--ds-text,#333333);">column and the required Threat Scenario's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Three dot-Attack Path Steps.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From <ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">Select Elements</ac:inline-comment-marker></strong><strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85"> </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">dialog, select Attack</ac:inline-comment-marker> Path.<br /><br /><ac:image><ri:attachment ri:filename="Select Element_Attack Path.png" /></ac:image><br /></span><span style="color:var(--ds-text,#333333);"><br /><ac:inline-comment-marker ac:ref="ed16e46c-9c6e-4aea-8b13-97eab5097f69">The Attack Path is added to the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Attack Path added.png" /></ac:image><br style="text-align: left;" /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a5f66ac-ca84-4422-a7e4-11e5ddccf5bb"><ac:rich-text-body><ul><li>You can also drag and drop the Attack Paths from the Containment tree to the Threat Scenario Table.</li><li>The Aggregated Attack Feasibility Rating is added automatically after you add the Attack Path.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Adding a Failure</h3><p>To add a Failure</p><hr /><ol><li><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">Double-click the designated cell in the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">Failure </ac:inline-comment-marker></strong></span><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">column and the required Threat Scenario's row and cl</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">ick</ac:inline-comment-marker> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Adding Failure_Three dot.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Class</strong><strong> </strong>dialog, select Failure.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectFailureWindow_v2.png" /></ac:image><br /></span><span style="color:var(--ds-text,#333333);"><br /><ac:inline-comment-marker ac:ref="40a0d885-7391-4f2a-9357-e7d0abf552bf">The Failure is now shown in the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Failure added.png" /></ac:image><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="88ded4ef-a5bc-47f5-96bf-2d2829c714ab"><ac:rich-text-body><p>You can also drag and drop the Failure modes from the Containment tree to the Threat Scenario Table.</p></ac:rich-text-body></ac:structured-macro><h3>Adding an Impacted Asset</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="415c82df-db8d-4115-a637-19735c45920e"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">You can add multiple Impacted Assets for a given Threat Scenario.</span></p></ac:rich-text-body></ac:structured-macro><p>To add an Impacted Asset</p><hr /><ol><li><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">Double-click the designated cell in the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">Impacted Asset </ac:inline-comment-marker></strong></span><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">column and the required Threat Scenario's row and cl</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">ick</ac:inline-comment-marker> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Adding Impacted Assets.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Element</strong><strong> </strong>dialog, select Impacted Asset.<br /><br /><ac:image><ri:attachment ri:filename="1 SelectAssetWindow_v2.png" /></ac:image><br /></span><span style="color:var(--ds-text,#333333);"><br /><ac:inline-comment-marker ac:ref="e96f5570-448a-43bc-8157-2a3e4b973c59">The Impacted Asset is added to the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Impacted Asset added.png" /></ac:image><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b020098c-6c00-47ee-b5df-0adb690f9033"><ac:rich-text-body><p>You can also drag and drop the Impacted Assets from the Containment tree to the Threat Scenario Table.</p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="4c718e6a-c1af-4784-8d55-2e7af05d5dfa">Threat Scenario Table Example</ac:inline-comment-marker></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a22e06b7-0a8c-4b90-a2da-d78dd453ed8d"><ac:rich-text-body><p>The maximum value among all the attacks paths for the given threat scenario is considered as the Aggregated Attack Feasibility Rating.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="Threat Scenario Example.png" /></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="913c17ef-41fc-4abc-9236-e55fcf09aa7a"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO/SAE 21434:2021 Road vehicles-Cybersecurity engineering</a></li><li><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO 26262-1:2018 Road vehicles-Functional safety</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=249574986 space=SCD version=5 -->
## PAGE 00151: Threat Sources

- page_id: `249574986`
- space_key: `SCD`
- source_url: https://docs.nomagic.com/spaces/SCD/pages/249574986/Threat+Sources
- version_number: 5
- version_date: `2025-11-18T11:11:45.474+01:00`
- ancestors: Systems Cybersecurity Designer > DO-326A Preliminary Security Risk Assessment > Pre Risk Assessment
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

**Threat Source**

A situation and method that can mistakenly trigger vulnerability. The threat source of a threat is intent and method: the attacker and the attack vector.

##### Adding a Threat Source

To add a Threat Source

1. In the Containment tree, right-click the 06 -Threat Sources package and select Create Element. 
 
[IMAGE alt='' src='']
2. I n the dialog, expand **DO-326A** and select **Threat Source**. 
 
**[IMAGE alt='' src='']**
3. Name the created threat sources in the Containment tree. 
 
**[IMAGE alt='' src='']**

You can add the newly created Threat Source to the Pre-Threat Scenario Table.

##### Assigning Source Type to a Threat Source

To assign a source type to a threat source

1. Open the Specification dialog of the required Threat Source.
2. In the Specification of ThreatSource Test Threat Source dialog, select Tags>sourceType and click Create Value . [ATTACHMENT filename='Specification dialog_source type.png']
3. In the Value section, select Human Threat Accidental. [ATTACHMENT filename='Specification dialog_Value selection.png']
4. Click Close .

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p class="TableParagraph"><strong>Threat Source</strong></p><p class="TableParagraph"><span style="color:var(--ds-text,#333333);">A situation and method that can mistakenly trigger vulnerability. The threat source of a threat is intent and method: the attacker and the attack vector.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Adding a Threat Source</h3><p>To add a Threat Source</p><hr /><ol><li>In the Containment tree, right-click the <strong>06 -Threat Sources </strong><span>package and select</span><strong> Create Element.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.png" /></ac:image><br /><br /></strong></li><li>I<span style="color:var(--ds-text,#333333);">n the dialog, expand <strong>DO-326A</strong> and select <strong>Threat Source</strong>.<br /><br /><strong><ac:image><ri:attachment ri:filename="Threat source selection.png" /></ac:image></strong><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">Name the created threat sources in the Containment tree.<br /><br /><strong><ac:image><ri:attachment ri:filename="Threat source created.png" /></ac:image></strong></span></li></ol><p>You can add the newly created Threat Source to the Pre-Threat Scenario Table.</p><h3>Assigning Source Type to a Threat Source</h3><p>To assign a source type to a threat source</p><hr /><ol><li>Open the Specification dialog of the required Threat Source.</li><li>In the Specification of ThreatSource Test Threat Source dialog, select <strong>Tags&gt;sourceType </strong>and click <strong>Create Value</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Specification dialog_source type.png" /></ac:image><br /><br /></li><li>In the Value section, select Human Threat Accidental.<br /><br /><ac:image><ri:attachment ri:filename="Specification dialog_Value selection.png" /></ac:image><br /><br /></li><li>Click <strong>Close</strong>.</li></ol></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=253046449 space=SCD version=21 -->
## PAGE 00152: Troubleshooting

- page_id: `253046449`
- space_key: `SCD`
- source_url: https://docs.nomagic.com/spaces/SCD/pages/253046449/Troubleshooting
- version_number: 21
- version_date: `2026-06-11T09:48:45.242+02:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

##### Attack Potential Rating of Attack path is not updating automatically in the Attack Path window

The Attack Potential Rating is not updating automatically after you change the Upper bound and Lower bound values of EnumerationLiteral.

To see the new Attack Potential Rating, you need to reopen the properties of the Attack path in the **Attack Path** window.

##### PowerBy Migration Error: Cybersecurity Goals not displayed in Dependency Matrix

In PowerBy, after migrating an ISO 21434 project from an earlier version to 2026x, Cybersecurity Goals are not displayed in the Cybersecurity Goals table or the Cybersecurity Assurance Diagram. The error also affects any user-defined matrix that uses stereotypes moved from the ISO 21434 profile to the Cybersecurity Core profile. 
 
[IMAGE alt='' src='']

###### Cybersecurity Assurance Diagrams with and without errors; the diagram with the error is missing Cybersecurity Goals.

This error may occur if the project meets all of the following conditions.

#### WARNING: Conditions that may cause the error:

Conditions that may cause the error:

- The ISO 21434 project is created in a version before 2026x.
- The ISO 21434 project contains a Cybersecurity Assurance dependency matrix.
- The ISO 21434 project contains at least one Cybersecurity Goal element, Cybersecurity Assurance Level element, and Cybersecurity Assurance relation (dependency) between two of those elements.

If your project meets all of the above-mentioned conditions after migration, the following error message is displayed when you open the Cybersecurity Assurance Diagram.

[IMAGE alt='' src='']

###### An error message displayed at the bottom of the modeling tool.

To fix this error

1. Lock the Cybersecurity Assurance D iagram.
2. Click Cybersecurity Core Profile -> Cybersecurity Core Profile -> CybersecurityGoalAssurance to locate the «CybersecurityGoalAssurance **»** stereotype.
3. Drag and drop the «CybersecurityGoalAssurance» stereotype onto the top of the diagram in the field labeled Dependency Criteria.
4. Refresh the dependency matrix. To learn more, click here .
5. Unlock the Cybersecurity Assurance D iagram and commit the change.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3 style="text-align: left;">Attack Potential Rating of Attack path is not updating automatically in the Attack Path window</h3><p>The Attack Potential Rating is not updating automatically after you change the Upper bound and Lower bound values of EnumerationLiteral.</p><p>To see the new Attack Potential Rating, you need to reopen the properties of the Attack path in the <strong>Attack Path</strong> window.</p><h3>PowerBy Migration Error: Cybersecurity Goals not displayed in Dependency Matrix </h3><p>In PowerBy, after migrating an ISO 21434 project from an earlier version to 2026x, Cybersecurity Goals are not displayed in the Cybersecurity Goals table or the Cybersecurity Assurance Diagram. <span>The error also affects any user-defined matrix that uses stereotypes moved from the ISO 21434 profile to the Cybersecurity Core profile.<br /><br /><ac:image ac:align="center" ac:border="true" ac:height="493" ac:width="1122"><ri:attachment ri:filename="CybersecurityAssurance_Comparison.png" /></ac:image></span><span><br /></span></p><h6 style="text-align: center;">Cybersecurity Assurance Diagrams with and without errors; the diagram with the error is missing Cybersecurity Goals.</h6><p>This error may occur if the project meets all of the following conditions.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a257a58b-2d17-4501-9303-b08f94453c34"><ac:parameter ac:name="title">Conditions that may cause the error:</ac:parameter><ac:rich-text-body><ul><li data-uuid="63badcb1-c068-4d67-8063-9854bea12f8e">The ISO 21434 project is created in a version before 2026x.</li><li data-uuid="03e66055-d527-4713-83b1-23ee34473a82">The ISO 21434 project contains a Cybersecurity Assurance dependency matrix.</li><li data-uuid="f7abe6ba-ba38-442c-ad20-c9a60a2c727d">The ISO 21434 project contains at least one Cybersecurity Goal element, Cybersecurity Assurance Level element, and Cybersecurity Assurance relation (dependency) between two of those elements.</li></ul></ac:rich-text-body></ac:structured-macro><p>If your project meets all of the above-mentioned conditions after migration, the following error message is displayed when you open the <span>Cybersecurity Assurance D</span><span>iagram.</span></p><p><span><ac:image ac:align="center" ac:border="true" ac:height="81" ac:width="413"><ri:attachment ri:filename="ErrorMessage.png" /></ac:image></span></p><h6 style="text-align: center;"><span>An error message displayed at the bottom of the modeling tool.</span></h6><p>To fix this error</p><hr /><ol><li data-uuid="ffa01d2f-ed04-4acb-b4a5-e0364c048906">Lock the <span>Cybersecurity Assurance D</span>iagram.</li><li data-uuid="a3acf3c4-187b-4f0c-898c-8439c2a1ef82"> Click <strong>Cybersecurity Core Profile -&gt; Cybersecurity Core Profile -&gt; CybersecurityGoalAssurance </strong>to locate the <strong>«CybersecurityGoalAssurance</strong><span><strong>»</strong> stereotype.</span></li><li data-uuid="d1d7fb3d-e493-4c15-9ce1-6a8b42796045">Drag and drop the <strong>«CybersecurityGoalAssurance»</strong> stereotype onto the top of the diagram in the field labeled <strong>Dependency Criteria.</strong></li><li data-uuid="1226cd72-92c1-4e8c-bed0-a6ffe0469556">Refresh the dependency matrix. To learn more, click <a href="https://docs.nomagic.com/MT/?contextKey=dependency-matrix-toolbar&amp;version=latest&amp;variant=default">here</a>.<strong><br /></strong></li><li data-uuid="57bc7661-fed3-4e00-88b9-f639724275c3">Unlock the Cybersecurity Assurance D<span>iagram </span>and commit the change.</li></ol>
````

<!--NOMAGIC_PAGE id=254420764 space=SCD version=1 -->
## PAGE 00153: Versions of Systems Cybersecurity Designer

- page_id: `254420764`
- space_key: `SCD`
- source_url: https://docs.nomagic.com/spaces/SCD/pages/254420764/Versions+of+Systems+Cybersecurity+Designer
- version_number: 1
- version_date: `2025-09-12T11:15:31.054+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

3271e970c781f06a956406725278630b

Systems Cybersecurity Designer

documentVersions

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="scroll-document-location" ac:schema-version="1" ac:macro-id="da9b67c8-d05f-4d34-a92e-95c12262c6b9"><ac:parameter ac:name="permaId">3271e970c781f06a956406725278630b</ac:parameter><ac:parameter ac:name="documentTitle">Systems Cybersecurity Designer</ac:parameter><ac:parameter ac:name="key">documentVersions</ac:parameter></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=249574970 space=SCD version=5 -->
## PAGE 00154: Vulnerabilities

- page_id: `249574970`
- space_key: `SCD`
- source_url: https://docs.nomagic.com/spaces/SCD/pages/249574970/Vulnerabilities
- version_number: 5
- version_date: `2025-11-18T11:11:36.868+01:00`
- ancestors: Systems Cybersecurity Designer > DO-326A Preliminary Security Risk Assessment > Pre Risk Assessment
- labels: []

### NORMALIZED CONTENT

##### Basic Concepts

**Vulnerability**

A flaw or weakness in system security procedures, design, implementation, or internal controls that could be exploited and result in a security breach or a violation of the system's security.

##### Adding Vulnerabilities

To add vulnerabilities

1. In the Containment tree, right-click the 04 - Vulnerabilities package and select Create Element. 
 
[IMAGE alt='' src='']
2. I n the dialog, expand **DO-326A** and select **Vulnerability**. 
 
[IMAGE alt='' src='']
3. Name the newly created vulnerability in the Containment tree. 
 
[IMAGE alt='' src='']

You can add the newly created Vulnerability to the Pre-Threat Scenario Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Basic Concepts</h3><p><strong>Vulnerability</strong></p><p>A flaw or weakness in system security procedures, design, implementation, or internal controls that could be exploited and result in a security breach or a violation of the system's security.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Adding Vulnerabilities</h3><p>To add vulnerabilities</p><hr /><ol><li>In the Containment tree, right-click the <strong style="letter-spacing: 0.0px;">04 - Vulnerabilities </strong><span style="letter-spacing: 0.0px;">package and select</span><strong style="letter-spacing: 0.0px;"> Create Element.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.png" /></ac:image><br /><br /></strong></li><li>I<span style="color:var(--ds-text,#333333);">n the dialog, expand <strong>DO-326A</strong> and select <strong>Vulnerability</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Vulnerability_Menu.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">Name the newly created vulnerability in the Containment tree.<br /><br /><ac:image><ri:attachment ri:filename="Vulnerability_created.png" /></ac:image><br /></span></li></ol><p><span style="color:var(--ds-text,#333333);">You can add the newly created Vulnerability to the Pre-Threat Scenario Table.</span></p></ac:layout-cell></ac:layout-section></ac:layout>
````
