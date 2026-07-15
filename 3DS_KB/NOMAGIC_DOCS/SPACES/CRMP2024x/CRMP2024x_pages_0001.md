# NOMAGIC DOCUMENTATION SPACE: Cameo Requirements Modeler Plugin 2024x

<!--NOMAGIC_SPACE key=CRMP2024x chunk=1 -->

<!--NOMAGIC_PAGE id=136720069 space=CRMP2024x version=3 -->
## PAGE 00001: 2024x Version News

- page_id: `136720069`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720069/2024x+Version+News
- version_number: 3
- version_date: `2023-09-21T10:27:24.609+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation
- labels: []

### NORMALIZED CONTENT

1126333275

INLINE

1126333277

INLINE

1126333276

INLINE

###### Cameo Requirements Modeler Plugin

Released on: November 10, 2023

1126333274

INLINE

The version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.

Check the product compatibility [CONFLUENCE_PAGE title='Product compatibility' space='NMDOC'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f478c03d-5aea-4354-ac52-12c70c230a20"><ac:parameter ac:name="id">1126333275</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="1783dcbb-2017-41ee-adec-618d49505d98"><ac:parameter ac:name="id">1126333277</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8a32796c-989c-43b7-b1c9-575eb7f82a5b"><ac:parameter ac:name="id">1126333276</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5 style="text-align: center;">Cameo Requirements Modeler Plugin</h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: November 10, 2023</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ef2befd3-e559-42d9-9070-d9acc58a0a17"><ac:parameter ac:name="id">1126333274</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>The version was released for compatibility purposes only. It does not contain new capabilities only minor bug fixes.</p><p>Check the product compatibility <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Product compatibility" /><ac:plain-text-link-body><![CDATA[here]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=136720063 space=CRMP2024x version=1 -->
## PAGE 00002: _buttons

- page_id: `136720063`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720063/_buttons
- version_number: 1
- version_date: `2023-09-21T10:22:33.794+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><br /></p>
````

<!--NOMAGIC_PAGE id=136720065 space=CRMP2024x version=1 -->
## PAGE 00003: _sample models

- page_id: `136720065`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720065/_sample+models
- version_number: 1
- version_date: `2023-09-21T10:22:33.928+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

All details here: [CONFLUENCE_PAGE title='Sample models' space='MD185'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>All details here: <ac:link><ri:page ri:content-title="Sample models" ri:space-key="MD185" /></ac:link>.</p>
````

<!--NOMAGIC_PAGE id=136720181 space=CRMP2024x version=1 -->
## PAGE 00004: Analyzing dependencies in dependency matrix

- page_id: `136720181`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720181/Analyzing+dependencies+in+dependency+matrix
- version_number: 1
- version_date: `2023-09-21T10:22:37.161+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements
- labels: []

### NORMALIZED CONTENT

830972946

830972948

830972947

You can create, analyze, and modify requirement relations in the matrix, which provides a compact visual view for analysis. Using a dependency matrix, you can also edit relations between a selected requirement and model element (i.e., add or remove a desired relation).

The Dependency Matrix enables:

- The visualization of more than one element relations from different diagrams.
- The capability to create domain-specific matrices and their templates.
- Ready-to-use matrix templates: traceability of elements and behavior diagrams, traceability of requirements, traceability of requirements and elements refining, satisfying, verifying them, and others.
- Faster creation of traceability links between elements (for example, between requirements and the architecture or requirements and test cases). This improvement saves a huge amount of time in comparison to linking elements in diagrams.

To create a dependency matrix

1. From a requirements specification package shortcut menu in the Containment tree, select **Create****Diagram** and then select one of the following:
  - Derive Requirement Matrix to create a Dependency Matrix to analyze, create, and modify derivation relations between a derived requirement and a source requirement.
  - Refine Requirement Matrix to create a Dependency Matrix to analyze, create, and modify refined relations between a requirement and a model element or a set of elements refining the requirement.
  - Satisfy Requirement Matrix to create a Dependency Matrix to analyze, create, and modify satisfaction relations between requirements and model elements fulfilling the requirements.
  - **Verify Requirement Matrix** to create a Dependency Matrix to analyze, create, or modify verification relations between requirements and named elements that can determine whether the systems fulfill the requirements.
2. Type a diagram name.
3. Select criteria and a scope to be represented in the matrix. You can specify requirements to be represented as rows and class elements to be represented as columns.
4. Click the **Refresh** button. 
The following figure shows how particular requirements satisfy particular model class elements.

[IMAGE alt='' src='']

###### Example of a dependency matrix.

You can also remove redundant or create missing dependencies using a dependency matrix. For detailed instructions on how to use dependency matrixes, see[CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024x'].

830972945

**Related pages**

- [CONFLUENCE_PAGE title='Dependency Matrix' space='MD2024x']
- [CONFLUENCE_PAGE title='Requirement matrices' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="9ec2a86b-a6cc-4f62-9f8e-1c3dcb7fb72e"><ac:parameter ac:name="id">830972946</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="7c2593b0-411e-473e-b58b-3977710d26a0"><ac:parameter ac:name="id">830972948</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5b3960e4-7295-4eb4-a4a2-fc85b9d8f5f6"><ac:parameter ac:name="id">830972947</ac:parameter><ac:rich-text-body><p>You can create, analyze, and modify requirement relations in the matrix, which provides a compact visual view for analysis. Using a dependency matrix, you can also edit relations between a selected requirement and model element (i.e., add or remove a desired relation).</p><p>The Dependency Matrix enables:</p><ul><li>The visualization of more than one element relations from different diagrams.</li><li>The capability to create domain-specific matrices and their templates. </li><li>Ready-to-use matrix templates: traceability of elements and behavior diagrams, traceability of requirements, traceability of requirements and elements refining, satisfying, verifying them, and others.</li><li>Faster creation of traceability links between elements (for example, between requirements and the architecture or requirements and test cases). This improvement saves a huge amount of time in comparison to linking elements in diagrams.</li></ul><p>To create a dependency matrix</p><hr /><ol><li><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">From a requirements specification package shortcut menu in the Containment tree, select <strong>Create</strong><strong> Diagram</strong> and then select one of the following:<br /></span></span><ul><li><strong>Derive</strong><strong> Requirement</strong><strong> Matrix</strong> to create a Dependency Matrix to analyze, create, and modify derivation relations between a derived requirement and a source requirement.</li><li><strong>Refine </strong><strong>Requirement </strong><strong>Matrix</strong> to create a Dependency Matrix to analyze, create, and modify refined relations between a requirement and a model element or a set of elements refining the requirement.</li><li><strong>Satisfy Requirement Matrix</strong> to create a Dependency Matrix to analyze, create, and modify satisfaction relations between requirements and model elements fulfilling the requirements.</li><li><span style="color: rgb(51,51,51);"><strong>Verify Requirement Matrix</strong> to create a Dependency Matrix to analyze, create, or modify verification relations between requirements and named elements that can determine whether the systems fulfill the requirements.</span></li></ul></li><li><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">Type a diagram name.</span></span></li><li><p class="auto-cursor-target"><span style="color: rgb(51,51,51);">Select criteria and a scope to be represented in the matrix.<br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="11eae72e-474b-44bb-a0cd-f3e032497cc0"><ac:rich-text-body><p><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">You can specify requirements to be represented as rows and class elements to be represented as columns.</span></span></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);"><span class="auto-cursor-target" style="color: rgb(51,51,51);"><br /></span></span></span></p></li><li><span style="color: rgb(51,51,51);">Click the <strong>Refresh</strong> button.<br />The following figure shows how particular requirements satisfy particular model class elements.</span></li></ol><p><span style="color: rgb(51,51,51);"><ac:image ac:align="center"><ri:attachment ri:filename="dependency_matrix_example.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Analyzing dependencies in dependency matrix" /></ri:attachment></ac:image></span></p><h6 style="color: rgb(129,137,156);text-align: center;"><span style="color: rgb(51,51,51);">Example of a dependency matrix.</span></h6><p style="color: rgb(129,137,156);text-align: left;"><br class="atl-forced-newline" /><span style="color: rgb(51,51,51);">  You can also remove redundant or create missing dependencies <span style="color: rgb(51,51,51);">using a dependency matrix</span>. For detailed instructions on how to use dependency matrixes, see<ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Dependency Matrix" /><ac:plain-text-link-body><![CDATA[ Dependency Matrix]]></ac:plain-text-link-body></ac:link>.</span></p><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="43d20f1f-69f4-4521-b1d1-928269455470"><ac:parameter ac:name="id">830972945</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><span style="color: rgb(51,51,51);"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Dependency Matrix" /></ac:link></span></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement matrices" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720183 space=CRMP2024x version=1 -->
## PAGE 00005: Analyzing dependencies in relation map

- page_id: `136720183`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720183/Analyzing+dependencies+in+relation+map
- version_number: 1
- version_date: `2023-09-21T10:22:37.260+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements
- labels: []

### NORMALIZED CONTENT

831044545

831044548

831044547

A relation map allows visual analysis among multiple levels of abstraction, such as how requirements are satisfied by other model elements. The relation map enables you to show existing relationships, visualize multilevel relationships, observe traceability from requirements to implementation, or any other analysis you need.

The relation map is useful for:

- Making fast analysis and overview of a model.
- Observing traceability from requirements to implementation all the way through different levels of abstraction (such as analysis, design, etc.).
- Discovering the requirements structure.

You are not allowed to edit relations in the relation map diagram.

To create a relation map

1. From a package or requirement shortcut menu in the Containment tree, select **Create Diagram** and then select one of the following:
  - Requirement Containment Map .
  - Requirement Derivation Map .
2. Type a diagram name.
3. Specify a relation criterion, element type, and scope.
4. Click the **Refresh** button. 
The following figure shows how particular requirements satisfy particular model class elements.

[IMAGE alt='' src='']

###### Example of relation map

For detailed instructions on how to use relation maps, see [CONFLUENCE_PAGE title='Relation Map' space='MD2024x'].

831044543

**Related pages**

- [CONFLUENCE_PAGE title='Relation Map' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a62ef4e4-df13-46c9-ac90-49c703cfc710"><ac:parameter ac:name="id">831044545</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="1d44a43d-b3a8-4c57-972b-9a282cfb76b7"><ac:parameter ac:name="id">831044548</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e382ef95-b5c1-453d-a849-a3a7031a7654"><ac:parameter ac:name="id">831044547</ac:parameter><ac:rich-text-body><p>A relation map allows visual analysis among multiple levels of abstraction, such as how requirements are satisfied by other model elements. The relation map enables you to show existing relationships, visualize multilevel relationships, observe traceability from requirements to implementation, or any other analysis you need.</p><p>The relation map is useful for:</p><ul><li>Making fast analysis and overview of a model.</li><li>Observing traceability from requirements to implementation all the way through different levels of abstraction (such as analysis, design, etc.).</li><li>Discovering the requirements structure.</li></ul><p><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="cf772b43-daa8-457f-a7be-4f2eec2a0a7e"><ac:rich-text-body><p>You are not allowed to edit relations in the relation map diagram.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p style="color: rgb(129,137,156);"><span style="color: rgb(51,51,51);">To create a relation map</span></p><hr /><ol><li><span style="color: rgb(51,51,51);"><span style="color: rgb(51,51,51);">From a package or requirement shortcut menu in the Containment tree, select <strong>Create Diagram</strong> and then select one of the following:<br /></span></span><ul><li><strong>Requirement Containment Map</strong>.</li><li class="auto-cursor-target"><strong>Requirement Derivation Map</strong>.</li></ul></li><li><span style="color: rgb(51,51,51);">Type a diagram name.</span></li><li><span style="color: rgb(51,51,51);">Specify a relation criterion, element type, and scope.</span></li><li><span style="color: rgb(51,51,51);">Click the <strong>Refresh</strong> button.<br />The following figure shows how particular requirements satisfy particular model class elements.</span></li></ol><p><span style="color: rgb(51,51,51);"><ac:image ac:align="center"><ri:attachment ri:filename="relation_map_example.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Analyzing dependencies in relation map" /></ri:attachment></ac:image><br /></span></p><h6 style="color: rgb(129,137,156);text-align: center;"><span style="color: rgb(51,51,51);">Example of relation map</span></h6><p>For detailed instructions on how to use relation maps, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Relation Map" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="60372022-f41d-4f4b-bf1d-1897bfec2f26"><ac:parameter ac:name="id">831044543</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li class="auto-cursor-target"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Relation Map" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720168 space=CRMP2024x version=2 -->
## PAGE 00006: Analyzing Requirements

- page_id: `136720168`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720168/Analyzing+Requirements
- version_number: 2
- version_date: `2024-01-29T14:59:46.542+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

INLINE

The requirements analysis encompasses those tasks that determine the needs or conditions a new or altered product or project must meet. It considers the possibly conflicting requirements of the various stakeholders by analyzing, documenting, validating and managing software or system requirements. Requirements analysis is critical to the success or failure of a systems or software project.

You can analyze requirements using the following tools:

- Usages and Dependencies . Discovers the Requirements usage and dependencies on other model parts: traceability, change impact analysis.
- Dependency Matrix . Checks the Gap analysis, Change Impact analysis, Requirements completeness and correctness.
- Model validation . Checks Requirements completeness and correctness based on build in or custom validation suites.
- Traceability . Tracks, visualizes, navigates, and analyzes the elements involved in traceability relations.
- Relation Map . Visualizes the relations of multilevel requirements: traceability, coverage analysis.
- Generic and Requirements Tables . Makes the coverage analysis in a compact format.
- Report Wizard . Analysis (e.g. coverage) and estimation (e.g. functional points method) based on built in or custom documentation generation templates.

The following sections describe the procedures for analyzing requirements:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="17662e2b-ebb9-4185-ad91-d5447b12e073"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>The requirements analysis encompasses those tasks that determine the needs or conditions a new or altered product or project must meet. It considers the possibly conflicting requirements of the various stakeholders by analyzing, documenting, validating and managing software or system requirements. Requirements analysis is critical to the success or failure of a systems or software project.</p><p>You can analyze requirements using the following tools:</p><ul><li><strong>Usages and Dependencies</strong>. Discovers the Requirements usage and dependencies on other model parts: traceability, change impact analysis.</li><li><strong>Dependency Matrix</strong>. Checks the Gap analysis, Change Impact analysis, Requirements completeness and correctness.</li><li><strong>Model validation</strong>. Checks Requirements completeness and correctness based on build in or custom validation suites.</li><li><strong>Traceability</strong>. Tracks, visualizes, navigates, and analyzes the elements involved in traceability relations.</li><li><strong>Relation Map</strong>. Visualizes the relations of multilevel requirements: traceability, coverage analysis.</li><li><strong>Generic and Requirements Tables</strong>. Makes the coverage analysis in a compact format.</li><li><strong>Report Wizard</strong>. Analysis (e.g. coverage) and estimation (e.g. functional points method) based on built in or custom documentation generation templates.</li></ul><p>The following sections describe the procedures for analyzing requirements:</p><p class="atl-forced-newline"><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2b1811ee-daf8-465f-90e8-9ae46eca8e70" /><br /><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720224 space=CRMP2024x version=1 -->
## PAGE 00007: Applying  «invariant» and «validationRule» stereotype

- page_id: `136720224`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720224/Applying+%C2%ABinvariant%C2%BB+and+%C2%ABvalidationRule%C2%BB+stereotype
- version_number: 1
- version_date: `2023-09-21T10:22:40.066+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation > Creating new validation rules
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Applying validationRule stereotype' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="941a62d7-70b6-4c50-9bbe-08a99149b879"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Applying validationRule stereotype" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720137 space=CRMP2024x version=1 -->
## PAGE 00008: Applying automated post-processing scripts after ReqIF file import

- page_id: `136720137`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720137/Applying+automated+post-processing+scripts+after+ReqIF+file+import
- version_number: 1
- version_date: `2023-09-21T10:22:35.698+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Importing requirements > Importing ReqIF files
- labels: []

### NORMALIZED CONTENT

After the ReqIF file import, you can apply an automated post-processing script to your project in order to modify requirements and create custom mapping upon requirements interchange through ReqIF.

In order to see the scripts and execute them, you must be using ReqIF Profile. To set the profile, go to **File** > **Use Project**, then scroll to select *ReqIF Profile.mdzip* and click **Finish**.

[IMAGE alt='' src='']

To apply the post-processing rules

1. From the Options menu, select Project .
2. In the options group list, select General , then scroll down to the ReqIF options group.
3. Under the ReqIF Import category, find Post-processing rules and select the one you want to apply.
4. Click OK .

| Post-processing Rule | Description |
| --- | --- |
| Fill Empty Requirement Name | When applied to a requirement with an unspecified Name property, the rule picks the data from Element ID and uses it as the element name. |
| Set CustomID as ID | When applied to a requirement with an empty Element ID, the rule sets the specified CustomID as an element ID. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>After the ReqIF file import, you can apply an automated post-processing script to your project in order to modify requirements and create custom mapping upon requirements interchange through ReqIF.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d942ed88-5d32-4e2f-ac22-050f019816a6"><ac:rich-text-body><p>In order to see the scripts and execute them, you must be using ReqIF Profile. To set the profile, go to <strong>File</strong> &gt; <strong>Use Project</strong>, then scroll to select <em>ReqIF Profile.mdzip</em> and click <strong>Finish</strong>.</p><p><ac:image ac:border="true" ac:height="140" ac:width="581"><ri:attachment ri:filename="reqif_profile_used.jpg"><ri:page ri:space-key="CRMP2024x" ri:content-title="Applying automated pre-processing scripts before ReqIF file export" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p> </p><p>To apply the post-processing rules</p><hr /><ol><li>From the <strong>Options</strong> menu, select <strong>Project</strong>.</li><li>In the options group list, select <strong>General</strong>, then scroll down to the <strong>ReqIF</strong> options group.</li><li>Under the<strong> ReqIF Import</strong> category, find <strong>Post-processing rules</strong> and select the one you want to apply.</li><li>Click <strong>OK</strong>.</li></ol><table><tbody><tr><th style="text-align: left;">Post-processing Rule</th><th style="text-align: center;">Description</th></tr><tr><td>Fill Empty Requirement Name</td><td>When applied to a requirement with an unspecified <strong>Name</strong> property, the <ac:inline-comment-marker ac:ref="0e6ad2d6-0dac-458f-b39e-ef25257112c2">r</ac:inline-comment-marker>ule picks the data from <strong>Element ID</strong> and uses it as the element name.</td></tr><tr><td>Set CustomID as ID</td><td>When applied to a requirement with an empty <strong>Element ID</strong>, the rule sets the specified <strong>CustomID</strong> as an element ID.</td></tr></tbody></table></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720145 space=CRMP2024x version=1 -->
## PAGE 00009: Applying automated pre-processing scripts before ReqIF file export

- page_id: `136720145`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720145/Applying+automated+pre-processing+scripts+before+ReqIF+file+export
- version_number: 1
- version_date: `2023-09-21T10:22:35.984+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Exporting requirements
- labels: []

### NORMALIZED CONTENT

Prior to the ReqIF file export, you can apply an automated pre-processing script to your project in order to modify requirements and create custom mapping upon requirements interchange through ReqIF.

In order to see the scripts and execute them, you must be using ReqIF Profile. To set the profile, go to**File**>**Use Project**, then scroll to select *ReqIF Profile.mdzip* and click **Finish**.

[IMAGE alt='' src='']

To apply the pre-processing rule

1. From the Options menu, select Project .
2. In the options group list, select General , then scroll down to the ReqIF options group.
3. Under **ReqIF Export**, find **Pre-processing rules** and select the one you want to apply.
4. Click OK .

| Pre-processing Rule | Description |
| --- | --- |
| Restore Empty Requirement Name | When applied to a requirement with a specified Name property, the rule removes the element name upon export. |

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Prior to the ReqIF file export, you can apply an automated pre-processing script to your project in order to modify requirements and create custom mapping upon requirements interchange through ReqIF.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d942ed88-5d32-4e2f-ac22-050f019816a6"><ac:rich-text-body><p><ac:inline-comment-marker ac:ref="a0459773-8b83-4869-aa7b-f597a39c4b0a">In order to see the scripts and execute them, you must be using ReqIF Profile. To set the profile, go to </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="a0459773-8b83-4869-aa7b-f597a39c4b0a">File</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="a0459773-8b83-4869-aa7b-f597a39c4b0a"> &gt; </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="a0459773-8b83-4869-aa7b-f597a39c4b0a">Use Project</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="a0459773-8b83-4869-aa7b-f597a39c4b0a">, then scroll to select <em>ReqIF Profile.mdzip</em> and click <strong>Finish</strong>.<br /></ac:inline-comment-marker></p><p><ac:image ac:border="true" ac:height="140" ac:width="581"><ri:attachment ri:filename="reqif_profile_used.jpg"><ri:page ri:space-key="CRMP2024x" ri:content-title="Applying automated pre-processing scripts before ReqIF file export" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p> </p><p>To apply the pre-processing rule</p><hr /><ol><li>From the <strong>Options</strong> menu, select <strong>Project</strong>.</li><li>In the options group list, select <strong>General</strong>, then scroll down to the <strong>ReqIF</strong> options group.</li><li><p>Under <strong>ReqIF Export</strong>, find <strong>Pre-processing rules</strong> and select the one you want to apply.</p></li><li>Click <strong>OK</strong>.</li></ol><table><tbody><tr><th>Pre-processing Rule</th><th>Description</th></tr><tr><td>Restore Empty Requirement Name</td><td><p>When applied to a requirement with a specified <strong>Name</strong> property, the rule removes the element name upon export.</p></td></tr></tbody></table><p class="auto-cursor-target"><br /></p><p> </p>
````

<!--NOMAGIC_PAGE id=136720310 space=CRMP2024x version=2 -->
## PAGE 00010: Assigning shortcut keys

- page_id: `136720310`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720310/Assigning+shortcut+keys
- version_number: 2
- version_date: `2024-01-29T14:31:22.034+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Assigning shortcut keys' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="d0bf1dd2-9339-4526-a7cc-d5bbe257f367"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Assigning shortcut keys" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720275 space=CRMP2024x version=1 -->
## PAGE 00011: Basic requirement concepts

- page_id: `136720275`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720275/Basic+requirement+concepts
- version_number: 1
- version_date: `2023-09-21T10:22:41.821+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

This section contains all basic concepts that are used while using the Cameo Requirements Modeler Plugin.

Basic requirement concepts:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This section contains all basic concepts that are used while using the Cameo Requirements Modeler Plugin.</p><p>Basic requirement concepts:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="df699e6c-b430-4a13-9509-914512a0ec87" /></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720284 space=CRMP2024x version=1 -->
## PAGE 00012: Business Requirement

- page_id: `136720284`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720284/Business+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:42.590+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Business Requirement is a requirement that specifies characteristics of the business process that must be satisfied by the system.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="d27a0102-fe68-4aef-8fd8-0be60ee8fd3d"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Business Requirement is a requirement that specifies characteristics of the business process that must be satisfied by the system.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720067 space=CRMP2024x version=2 -->
## PAGE 00013: Cameo Requirements Modeler Plugin Documentation

- page_id: `136720067`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720067/Cameo+Requirements+Modeler+Plugin+Documentation
- version_number: 2
- version_date: `2024-01-29T14:59:08.043+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

565187525

565187527

565187526

INLINE

**Purpose**

Cameo Requirements Modeler Plugin is dedicated for business analysts and architects, software engineers, enterprise architects, systems engineers, and other users, who work in model-based requirements engineering. The plugin supports the requirements part of the OMG SysML standard and provides means to import, export and manage requirements in the model.

The plugin supports Requirements Interchange Format (ReqIF), the industry standard enabling users to interchange requirements among different requirements management tools. The standard is managed by the Object Management Group and supported by major tool vendors.

**Model-based requirements engineering benefits**

- Easy identification of the scope and potential consequence of any change.
- Single and consistent data source: requirements, processes, and design.
- Increased quality of requirements due to the automatic validation and better visibility.
- Saved time and resources as you are working in the same environment where your models are.
- Improved team communication due to the simple and standard notation, clear diagrams, and web-based reports.

**With this plugin you can**

- Import and export requirements to ReqIF files to use them with other requirements management tools, such as
  - IBM DOORS 9.4, 9.5, and 9.6
  - IBM DOORS Next Generation
  - PTC Integrity
  - Polarion REQUIREMENTS
  - Siemens Teamcenter
  - Dassault Systemes Reqtify.
- Trace from requirements to other model elements of business, software, or systems architecture and align requirements with your model.
- Analyze the impact of changes.
- Track metrics.
- Capture requirements in dedicated diagrams, matrices, and tables.
- Document requirements.
- Extend the plugin by creating new requirement types and customizing the plugin's functionality.

The Cameo Requirements Modeler Plugin documentation consists of the following sections:

800700

565187524

**Docs of other versions**

- [CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP184']
- [CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP183']
- [CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP182']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a21a2dac-dd2b-49d2-a72a-eb6734f42ccf"><ac:parameter ac:name="id">565187525</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8d5b0bcf-6832-49d0-89a5-f14ed810f6f3"><ac:parameter ac:name="id">565187527</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="debd1af2-cd47-417c-a838-ea2a82fc181f"><ac:parameter ac:name="id">565187526</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="62fee33e-4eb4-486f-a3ba-6c4583e26f07"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><strong>Purpose</strong></p><p>Cameo Requirements Modeler Plugin is dedicated for business analysts and architects, software engineers, enterprise architects, systems engineers, and other users, who work in model-based requirements engineering. The plugin supports the requirements part of the OMG SysML standard and provides means to import, export and manage requirements in the model.</p><p>The plugin supports Requirements Interchange Format (ReqIF), the industry standard enabling users to interchange requirements among different requirements management tools. The standard is managed by the Object Management Group and supported by major tool vendors.</p><p><strong>Model-based requirements engineering benefits</strong></p><ul><li>Easy identification of the scope and potential consequence of any change.</li><li>Single and consistent data source: requirements, processes, and design.</li><li>Increased quality of requirements due to the automatic validation and better visibility.</li><li>Saved time and resources as you are working in the same environment where your models are.</li><li>Improved team communication due to the simple and standard notation, clear diagrams, and web-based reports.</li></ul><p><strong>With this plugin you can</strong></p><ul><li>Import and export requirements to ReqIF files to use them with other requirements management tools, such as<ul><li>IBM DOORS 9.4, 9.5, and 9.6</li><li>IBM DOORS Next Generation</li><li>PTC Integrity</li><li>Polarion REQUIREMENTS</li><li>Siemens Teamcenter</li><li>Dassault Systemes Reqtify.</li></ul></li><li>Trace from requirements to other model elements of business, software, or systems architecture and align requirements with your model.</li><li>Analyze the impact of changes.</li><li>Track metrics.</li><li>Capture requirements in dedicated diagrams, matrices, and tables.</li><li>Document requirements.</li><li>Extend the plugin by creating new requirement types and customizing the plugin's functionality.</li></ul><p>The Cameo Requirements Modeler Plugin documentation consists of the following sections:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="5269876b-22d5-4afd-9058-1d70ea4525d0" /></p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="4016dd6c-12d6-41c0-ae51-87f4f347fec6"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=OK_Z7zjJKeg" /></ac:parameter><ac:parameter ac:name="height">700</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="40df5f58-4bbc-409b-a9d2-a520299b8ab9"><ac:parameter ac:name="id">565187524</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Docs of other versions</strong></p><ul><li><ac:link><ri:page ri:space-key="CRMP184" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Requirements Modeler Plugin 18.4]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP183" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Requirements Modeler Plugin 18.3]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP182" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Requirements Modeler Plugin 18.2]]></ac:plain-text-link-body></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720180 space=CRMP2024x version=1 -->
## PAGE 00014: Change impact analysis

- page_id: `136720180`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720180/Change+impact+analysis
- version_number: 1
- version_date: `2023-09-21T10:22:37.061+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements
- labels: []

### NORMALIZED CONTENT

Impact analysis minimizes the risk of introducing undesirable effects to the system by increasing your understanding of how the proposed change might affect the elements in the system change. Once a change is proposed its impact should be identified.

Traceability links and visualization of related elements display dependencies of requirements and help you see the full impact of a proposed change in those requirements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Impact analysis minimizes the risk of introducing undesirable effects to the system by increasing your understanding of how the proposed change might affect the elements in the system change. Once a change is proposed its impact should be identified.</p><p>Traceability links and visualization of related elements display dependencies of requirements and help you see the full impact of a proposed change in those requirements.</p><p> </p>
````

<!--NOMAGIC_PAGE id=136720095 space=CRMP2024x version=1 -->
## PAGE 00015: Changing interface style

- page_id: `136720095`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720095/Changing+interface+style
- version_number: 1
- version_date: `2023-09-21T10:22:34.908+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Changing interface style' space='MD2024x']true

#### PANEL: On this page

On this page

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Main menu' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Toolbars' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Image Library tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="a08d53b6-493f-4e45-9539-e6ac555303c1"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Changing interface style" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="da03c114-3616-4df7-ac7f-3f5bb86fc6a8"><ac:parameter ac:name="title">
       On this page
      </ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="18e07c87-6ff0-4efe-a29b-8c9137fc82f2" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="7f8b169a-3bc8-4bc5-8721-f45adc6153dc"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Main menu" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Toolbars" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Image Library tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720311 space=CRMP2024x version=2 -->
## PAGE 00016: Configuration files

- page_id: `136720311`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720311/Configuration+files
- version_number: 2
- version_date: `2024-01-29T14:51:30.807+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Configuration files' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="15c516b1-7354-4250-9a8b-78ce90c79912"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Configuration files" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720079 space=CRMP2024x version=2 -->
## PAGE 00017: Containment tab

- page_id: `136720079`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720079/Containment+tab
- version_number: 2
- version_date: `2024-01-29T14:55:43.316+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

733231863

733231874

733231864

true[CONFLUENCE_PAGE title='Containment tab' space='MD2024x']

733231862

**Related pages**

****

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="da4cb431-6ba6-4fa2-8e43-0bfbc39932a7"><ac:parameter ac:name="id">733231863</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a42c7106-b286-4ef3-bd4b-c91c8bdeb23b"><ac:parameter ac:name="id">733231874</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3eab2be9-f5c9-48c2-a4f0-9a3c71a4d831"><ac:parameter ac:name="id">733231864</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="b9986127-2c40-4ea1-915b-8352bec344a5"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Containment tab" /></ac:link></ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="62af2290-8c46-492e-9a48-c2aae80702a8"><ac:parameter ac:name="id">733231862</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><strong><br /></strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720164 space=CRMP2024x version=1 -->
## PAGE 00018: Converting requirements

- page_id: `136720164`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720164/Converting+requirements
- version_number: 1
- version_date: `2023-09-21T10:22:36.552+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Converting Elements' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="b74507d6-0974-4081-a43f-e451340dcafc"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Converting Elements" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720294 space=CRMP2024x version=1 -->
## PAGE 00019: Copy

- page_id: `136720294`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720294/Copy
- version_number: 1
- version_date: `2023-09-21T10:22:43.544+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Ignoring solver

1141561110

#### CONTENT-COLUMN: Ignoring solver

1141561112

#### CONTENT-BLOCK: Ignoring solver

1141561111

#### EXCERPT: Ignoring solver

INLINE

A Copy relationship is a dependency between a supplier requirement (master) and a client requirement (slave), specifying that the client requirement text is a read-only copy of the supplier requirement text. In other words, by creating a Copy dependency between two Requirements, you copy the text property from the supplier to the client.

[IMAGE alt='' src='']

1. On the diagram, select a client Requirement symbol (slave), a symbol you want to be a copy of the supplier Requirement (master). The smart manipulator appears. [ATTACHMENT filename='copy_smart_manipulator.png']
2. Select the Copy command as depicted in the preceding figure and connect the client Requirement to the supplier Requirement.
3. The Copy path goes yellow because of violation of the rule Invalid Slave Requirement text meaning the text of the slave Requirement must be the same as of the master Requirement. Click the Copy path and, in the smart manipulator, select the Validation command. [ATTACHMENT filename='copy_validation.png']
4. The list of suggested solvers appears. Select **Copy text of the supplier requirement to the client requirement**to create and sustain this dependency in your model correctly. Ignoring solverYou may select other solvers but note:**Remove Copy dependency** - removes the dependency from the diagram and the entire model.**Ignore** - ignores the violation and the dependency is created and sustained in the model with the violation.

1141561109

**Related pages**

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Validation' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="afe32cdd-13b8-4d3d-8551-8f5dd2c3ab58"><ac:parameter ac:name="id">1141561110</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5bdf4b59-bbb5-4017-9df5-1131bec36c49"><ac:parameter ac:name="id">1141561112</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="44e6b71c-fdca-403d-8717-a659e3ad9330"><ac:parameter ac:name="id">1141561111</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="80a128f6-04e5-4818-b078-17f597a892fa"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Copy relationship is a dependency between a supplier requirement (master) and a client requirement (slave), specifying that the client requirement text is a read-only copy of the supplier requirement text. In other words, by creating a Copy dependency between two Requirements, you copy the text property from the supplier to the client.</p><p><ac:image><ri:attachment ri:filename="copy_relationship.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Copy" /></ri:attachment></ac:image></p><p><br /></p>To create a Copy dependency between two requirements on the diagram<hr /><ol><li>On the diagram, select a client Requirement symbol (slave), a symbol you want to be a copy of the supplier Requirement (master). The smart manipulator appears.<br /><ac:image ac:thumbnail="true" ac:height="239"><ri:attachment ri:filename="copy_smart_manipulator.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Copy" /></ri:attachment></ac:image></li><li>Select the Copy command as depicted in the preceding figure and connect the client Requirement to the supplier Requirement.</li><li>The Copy path goes yellow because of violation of the rule <strong>Invalid Slave Requirement text</strong> meaning the text of the slave Requirement must be the same as of the master Requirement. Click the Copy path and, in the smart manipulator, select the Validation command.<br /><ac:image><ri:attachment ri:filename="copy_validation.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Copy" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">The list of suggested solvers appears. Select <strong>Copy text of the supplier requirement to the client requirement </strong>to create and sustain this dependency in your model correctly.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b28d5edd-ff53-418a-ab58-d7a392836b78"><ac:parameter ac:name="title">Ignoring solver</ac:parameter><ac:rich-text-body><p>You may select other solvers but note:</p><ul><li><strong>Remove Copy dependency</strong> - removes the dependency from the diagram and the entire model.</li><li><strong>Ignore</strong> - ignores the violation and the dependency is created and sustained in the model with the violation.</li></ul></ac:rich-text-body></ac:structured-macro></li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="eaf1d62c-0460-4e0c-b6c3-d2a7ff79cf50"><ac:parameter ac:name="id">1141561109</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Validation" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720179 space=CRMP2024x version=1 -->
## PAGE 00020: Coverage analysis

- page_id: `136720179`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720179/Coverage+analysis
- version_number: 1
- version_date: `2023-09-21T10:22:36.973+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements
- labels: []

### NORMALIZED CONTENT

The Coverage analysis provides coverage information at immediate higher or lower levels by analyzing traceability properties values. Coverage analysis visualizes and verifies that requirements are covered with design, implementation, test cases, or other subjects.

Test cases not only plan how to verify each requirement, but also identify a relation between the requirement and test case and show the coverage to ensure that each requirement will be appropriately tested.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Coverage analysis provides coverage information at immediate higher or lower levels by analyzing traceability properties values. Coverage analysis visualizes and verifies that requirements are covered with design, implementation, test cases, or other subjects.</p><p>Test cases not only plan how to verify each requirement, but also identify a relation between the requirement and test case and show the coverage to ensure that each requirement will be appropriately tested.</p><p> </p>
````

<!--NOMAGIC_PAGE id=136720219 space=CRMP2024x version=2 -->
## PAGE 00021: Creating new validation rules

- page_id: `136720219`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720219/Creating+new+validation+rules
- version_number: 2
- version_date: `2024-01-29T14:59:19.416+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation
- labels: []

### NORMALIZED CONTENT

228054337

228054339

228054338

[CONFLUENCE_PAGE title='Creating new validation rules' space='MD2024x']true

228054335

**Related pages**

****

**Related pages in Developer Guide**

- [CONFLUENCE_PAGE title='Creating validation rules' space='MD2024x']Creating validation rules

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="3db5c19c-5408-40f3-a72e-28e342f4e3a8"><ac:parameter ac:name="id">228054337</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9c62b730-f2c3-4d13-a1c0-9ea6735e4b2d"><ac:parameter ac:name="id">228054339</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="79f06d8f-7b6a-4ca6-a5b7-b9b2efa728ed"><ac:parameter ac:name="id">228054338</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="607fd600-ac44-4ccd-a2d0-cd0159f28e4e"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating new validation rules" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="adaba817-e503-4395-b397-c5b319116394"><ac:parameter ac:name="id">228054335</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><strong><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="881cbeeb-81f0-4c88-a48d-8189f5ded26f" /></strong></p><p><strong>Related pages <span class="confluence-link">in Developer Guide</span><br /></strong></p><ul><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating validation rules" /><ac:link-body><span class="current">Creating validation rules</span></ac:link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720313 space=CRMP2024x version=2 -->
## PAGE 00022: Creating path variables

- page_id: `136720313`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720313/Creating+path+variables
- version_number: 2
- version_date: `2024-01-29T14:51:55.666+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations > Customizing environment options
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Creating path variables' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="e39ae7de-9841-415a-acde-9ecbe71d6da8"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating path variables" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720150 space=CRMP2024x version=1 -->
## PAGE 00023: Creating Requirement Diagram for sub-requirements

- page_id: `136720150`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720150/Creating+Requirement+Diagram+for+sub-requirements
- version_number: 1
- version_date: `2023-09-21T10:22:36.232+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

You can create a Requirements Diagram for sub-requirements of the selected requirement directly on the diagram pane.

To create Requirements Diagram for sub-requirements

1. Select a Requirement shape on the diagram pane.
2. On the smart manipulator, click the Create diagram for sub-requirements button.

A new requirements diagram for the sub-requirements is created having the same name as the selected requirement. The selected requirement is an owner of sub-requirements diagram and is marked with the diagram sign.

Double click the owner symbol to open a diagram for sub-requirements and use navigation buttons on the diagram toolbar to move back or forward through diagrams.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can create a Requirements Diagram for sub-requirements of the selected requirement directly on the diagram pane.</p><p><br /></p><p>To create Requirements Diagram for sub-requirements</p><hr /><ol><li>Select a Requirement shape on the diagram pane.</li><li>On the smart manipulator, click the <strong>Create diagram for sub-requirements</strong> button.</li></ol><p>A new requirements diagram for the sub-requirements is created having the same name as the selected requirement. The selected requirement is an owner of sub-requirements diagram and is marked with the diagram sign.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d7cdcdd2-5841-4506-98d0-037b50f64bd5"><ac:rich-text-body><p>Double click the owner symbol to open a diagram for sub-requirements and use navigation buttons on the diagram toolbar to move back or forward through diagrams.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720103 space=CRMP2024x version=1 -->
## PAGE 00024: Creating requirements

- page_id: `136720103`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720103/Creating+requirements
- version_number: 1
- version_date: `2023-09-21T10:22:35.138+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

576911758

576911760

576956753

**On this page**

576911759

INLINE

You can create and represent text-based requirements and relate them to other modeling elements. The requirements can be depicted in graphical, tabular, or tree structure format. This page provides instructions for creating requirements in the model. You can create requirements in the:

- [CONFLUENCE_PAGE title='Creating requirements' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Creating requirements' space='CRMP2024x'] .
- [CONFLUENCE_PAGE title='Creating requirements' space='CRMP2024x'] .

##### containmentCreating requirements in the Containment tree

If you create Requirements in the Containment tree, the element is created in the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x']. After that you can represent them on the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'] by dragging them or in the [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x'] by adding an existing element.

To create requirements in the Containment tree

1. Open an existing or create a new Requirement Diagram. [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x']]]>
2. In the [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x'] , right-click the package, or another Requirement where you want to create or nest a new Requirement.
3. From the shortcut menu, click Create Element .
4. In the **Create Element** dialog, select any type of Requirement. If you have created your own custom Requirement types, they appear under the**Custom Requirements** group.
5. Type a Requirement name. The new requirement is created in the Model Browser.

##### diagramCreating requirements in the Requirement diagram

If you create Requirements directly on the diagram pane, the element is created in the[CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x']as well.

To create Requirements on the Requirement Diagram pane

1. Open an existing or create a new Requirement Diagram. [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x']]]>
2. On the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'], select a **Requirement** or other type of requirement button and click on the diagram pane. The element is created in the same package where the diagram is stored.
3. On the Requirement shape, type a name, ID, and description. The Requirement is created and added in the table.

You can find more information about how to work in diagrams on the page [CONFLUENCE_PAGE title='Diagramming' space='MD2024x'].

To select a different owner

1. Hold **Shift**, click**Add New** button, and select a Requirement type from the drop-down menu. 
The **Select Owner** dialog opens, enabling you to choose a different owner.

##### tableCreating requirements in the Requirement Table

You can create new, nested requirements, or add existing ones in the Requirement Table.

###### Creating a new Requirements

To create a new Requirement in a Requirement Table

1. Open an existing or create a new Requirement Table. [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x']]]>
2. On the Requirement table toolbar, click the Add New button or press Insert ( Ctrl+I for Mac users). The list of Requirement types opens.
3. Click a desired requirement type. A new line above the first numbered requirement appears.
4. In that empty line, type a requirement name and specify other requirement properties. To select a different owner1. Hold **Shift**, click**Add New** button, and select a Requirement type from the drop-down menu. 
The **Select Owner** dialog opens, enabling you to choose a different owner.

###### Adding existing Requirements

To add existing Requirements in a Requirement Table

1. Open an existing or create a new Requirement Table. [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x']]]>
2. Do one of the following:
  - On the Requirement table toolbar, click the Add Existing button or press Ctrl + Insert ( Ctrl+I for Mac users). In the Select Requirement dialog, select the requirements you want to represent in the table and click OK .
  - Drag the entire requirements Package from the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'] and drop it on the empty Requirement table to represent all its content in the table.

###### Adding nested Requirements

To add nested Requirement in the Requirement Table

1. Select Requirement you want to nest in the table.
2. Click the Add Nested button or press Alt+Insert ( Alt+I for Mac users).
3. Select the desired Requirement type from the drop-down menu. If you have created your own custom Requirement types, they appear under the Custom Requirements group in the drop-down menu.

More information about how to work in tables you can find in the following pages:

- Table toolbars
- Table Criteria area
- Basic tasks in tables

576911757

**Related pages**

- [CONFLUENCE_PAGE title='Creating diagrams' space='MD2024x']
- [CONFLUENCE_PAGE title='Opening diagrams' space='MD2024x']
- [CONFLUENCE_PAGE title='Dragging objects' space='MD2024x']
- [CONFLUENCE_PAGE title='Relating requirements' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Table toolbars' space='MD2024x']
- [CONFLUENCE_PAGE title='Table Criteria area' space='MD2024x']
- [CONFLUENCE_PAGE title='Basic tasks in tables' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5640cc9c-96bb-44be-bfb4-8267ecee35f5"><ac:parameter ac:name="id">576911758</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="49f66323-ec3c-4c9b-8351-258df8d4a5d7"><ac:parameter ac:name="id">576911760</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3f5a9240-03a9-4eb6-97f6-af09b61ab7ce"><ac:parameter ac:name="id">576956753</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="a1db3358-95ef-4c73-ad55-e0174cc48bdc" /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="865f046f-7570-4a8a-94da-ebf8c4210f3a"><ac:parameter ac:name="id">576911759</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="f0d72c05-2465-45d7-8bef-6b730584d846"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>You can create and represent text-based requirements and relate them to other modeling elements. The requirements can be depicted in graphical, tabular, or tree structure format. This page provides instructions for creating requirements in the model. You can create requirements in the:</p><ul><li><ac:link ac:anchor="containment"><ac:plain-text-link-body><![CDATA[Containment tree.]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating requirements" /></ac:link></li><li><ac:link ac:anchor="diagram"><ac:plain-text-link-body><![CDATA[Requirement Diagram]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating requirements" /></ac:link>.</li><li><ac:link ac:anchor="table"><ac:plain-text-link-body><![CDATA[Requirement Table]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating requirements" /></ac:link>.</li></ul><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="8237217a-aef1-4047-a44c-f957fe84ee2c"><ac:parameter ac:name="">containment</ac:parameter></ac:structured-macro>Creating requirements in the Containment tree</h3><p>If you create Requirements in the Containment tree, the element is created in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[Model Browser]]></ac:plain-text-link-body></ac:link>. After that you can represent them on the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link> by dragging them or in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link> by adding an existing element.</p><p>To create requirements in the Containment tree</p><hr /><ol><li>Open an existing or create a new Requirement Diagram. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[How to create a new diagram >]]></ac:plain-text-link-body></ac:link></li><li>In the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link>, right-click the package, or another Requirement where you want to create or nest a new Requirement.</li><li>From the shortcut menu, click <strong>Create Element</strong>.</li><li><p class="auto-cursor-target">In the <strong>Create Element</strong> dialog, select any type of Requirement.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c6b5653d-02d5-4395-8b2c-2c3ffe0cc3ef"><ac:rich-text-body><p>If you have created your own custom Requirement types, they appear under the<strong> Custom Requirements</strong> group.</p></ac:rich-text-body></ac:structured-macro></li><li><span>Type a Requirement name.</span><br /><span>The new requirement is created in the Model Browser.</span></li></ol><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="ca912ddd-ca72-4df0-a31c-c6197c6c637f"><ac:parameter ac:name="">diagram</ac:parameter></ac:structured-macro>Creating requirements in the Requirement diagram</h3><p><span>If you create Requirements directly on the diagram pane, the element is created in the </span><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[Model Browser]]></ac:plain-text-link-body></ac:link><span> as well.</span></p><p>To create Requirements on the Requirement Diagram pane</p><hr /><ol><li>Open an existing or create a new Requirement Diagram. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[How to create a new diagram >]]></ac:plain-text-link-body></ac:link></li><li><p class="auto-cursor-target">On the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pallet]]></ac:plain-text-link-body></ac:link>, select a <strong>Requirement</strong> or other type of requirement button and click on the diagram pane.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="01bb1960-e357-4ecc-84b4-d3c5a623f2b3"><ac:rich-text-body><p>The element is created in the same package where the diagram is stored.</p></ac:rich-text-body></ac:structured-macro></li><li>On the Requirement shape, type a name, ID, and description. <br />The Requirement is created and added in the table.<br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d7a2f973-09ca-45d8-b443-72d396a20f4e"><ac:rich-text-body><p>You can find more information about how to work in diagrams on the page <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Diagramming" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fe06ca89-4a1d-4f06-8848-9aafb5c28174"><ac:rich-text-body><p>To select a different owner</p><hr /><p>1. Hold <strong>Shift</strong>, click<strong> Add New</strong> button, and select a Requirement type from the drop-down menu.<br />The <strong>Select Owner</strong> dialog opens, enabling you to choose a different owner.</p></ac:rich-text-body></ac:structured-macro><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6ddd2de8-c294-412e-aa9e-200266fc5f90"><ac:parameter ac:name="">table</ac:parameter></ac:structured-macro>Creating requirements in the Requirement Table</h3><p>You can create new, nested requirements, or add existing ones in the Requirement Table.</p><h4>Creating a new Requirements</h4><p>To create a new Requirement in a Requirement Table</p><hr /><ol><li>Open an existing or create a new Requirement Table. <span class="confluence-link"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[How to create a table >]]></ac:plain-text-link-body></ac:link></span></li><li>On the Requirement table toolbar, click the <strong>Add New</strong> button or press Insert (<strong>Ctrl+I</strong> for Mac users). The list of Requirement types opens.</li><li>Click a desired requirement type. A new line above the first numbered requirement appears.</li><li><p class="auto-cursor-target">In that empty line, type a requirement name and specify other requirement properties.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="502f83f1-7535-48ea-a85a-6ef13aacf04f"><ac:rich-text-body><p>To select a different owner</p><hr /><p>1. Hold <strong>Shift</strong>, click<strong> Add New</strong> button, and select a Requirement type from the drop-down menu.<br />The <strong>Select Owner</strong> dialog opens, enabling you to choose a different owner.</p></ac:rich-text-body></ac:structured-macro></li></ol><h4>Adding existing Requirements</h4><p>To add existing Requirements in a Requirement Table</p><hr /><ol><li>Open an existing or create a new Requirement Table. <span class="confluence-link"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /><ac:plain-text-link-body><![CDATA[How to create a table >]]></ac:plain-text-link-body></ac:link></span></li><li>Do one of the following:<br /><ul><li>On the Requirement table toolbar, click the <strong>Add Existing</strong> button or press Ctrl + Insert (<strong>Ctrl+I</strong> for Mac users). In the <strong>Select Requirement</strong> dialog, select the requirements you want to represent in the table and click <strong>OK</strong>.</li><li>Drag the entire requirements Package from the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link> and drop it on the empty Requirement table to represent all its content in the table.<br /><br /></li></ul></li></ol><h4>Adding nested Requirements</h4><p>To add nested Requirement in the Requirement Table</p><hr /><ol><li>Select Requirement you want to nest in the table.</li><li>Click the <strong>Add Nested</strong> button or press <strong>Alt+Insert </strong>(<strong>Alt+I </strong>for Mac users).</li><li><p>Select the desired Requirement type from the drop-down menu.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ec84a738-898f-4f40-ad05-548e092fffdd"><ac:rich-text-body><p>If you have created your own custom Requirement types, they appear under the Custom Requirements group in the drop-down menu.</p></ac:rich-text-body></ac:structured-macro><p><br /><br /></p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2165c4db-3c9c-47e9-a6c7-057659d50b24"><ac:rich-text-body><p>More information about how to work in tables you can find in the following pages:</p><ul><li><a href="https://docs.nomagic.com/display/MD2024x/Table+toolbars">Table toolbars</a></li><li><a href="https://docs.nomagic.com/display/MD2024x/Table+Criteria+area">Table Criteria area</a></li><li><a href="https://docs.nomagic.com/display/MD2024x/Basic+tasks+in+tables">Basic tasks in tables</a></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="edf84565-6b66-47fb-9909-41966a174d54"><ac:parameter ac:name="id">576911757</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating diagrams" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Opening diagrams" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Dragging objects" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Relating requirements" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Table toolbars" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Table Criteria area" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Basic tasks in tables" /></ac:link></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720096 space=CRMP2024x version=1 -->
## PAGE 00025: Creating Requirements Project

- page_id: `136720096`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720096/Creating+Requirements+Project
- version_number: 1
- version_date: `2023-09-21T10:22:34.951+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started
- labels: []

### NORMALIZED CONTENT

564722837

564722839

564722838

You can create requirements using the the Requirements Project template. It contains predefined packages, elements, and diagrams to start creating your own requirements in the model.

The Requirements Project template is only available in MagicDraw with Cameo Requirement Modeler Plugin installed.

To create a Requirement Project

1. Open the New Project dialog. Do one of the following:
  - 
    - From the File menu, select New Project .
    - On the main toolbar, click the New Project button.
    - Press Ctrl + Shift + N.
2. In the New Project dialog, specify the following:
  - On the left side of the dialog, under the General-Purpose Modeling domain, select the Requirements Project .
  - On the right side of the dialog, type the file name in the Name box.
  - On the right side of the dialog, click the [ATTACHMENT filename='select_location_button.png'] button and select the location to store the created project. [ATTACHMENT filename='requirements_projects_templates.png']
3. Click OK . The new Requirement project is created with predefined structure as shown in the image below. [ATTACHMENT filename='requirements_project_structure.png']

564722836

**Related pages**

- [CONFLUENCE_PAGE title='Working with projects' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="55319c2c-48c2-4bbe-ab07-ec54b8cc9874"><ac:parameter ac:name="id">564722837</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="ae2caa32-efd0-4f0b-a402-a8c5f01faf5d"><ac:parameter ac:name="id">564722839</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0aef4ddb-a104-46be-b9bc-4da9a25d1b8b"><ac:parameter ac:name="id">564722838</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>You can create requirements using the the Requirements Project template. It contains predefined packages, elements, and diagrams to start creating your own requirements in the model.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="16ac13b5-48ab-4cc4-b773-d1c8fd43d925"><ac:rich-text-body><p>The Requirements Project template is only available in MagicDraw with Cameo Requirement Modeler Plugin installed.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p class="atl-forced-newline">To create a Requirement Project</p><hr /><ol><li class="atl-forced-newline">Open the <strong>New Project</strong> dialog. Do one of the following:<br /><ul><li style="list-style-type: none;background-image: none;"><ul><li class="atl-forced-newline">From the <strong>File</strong> menu, select <strong>New Project</strong>.</li><li class="atl-forced-newline">On the main toolbar, click the <strong>New Project</strong> button.</li><li class="atl-forced-newline">Press Ctrl + Shift + N.</li></ul></li></ul></li><li class="atl-forced-newline">In the <strong>New Project</strong> dialog, specify the following:<br /><ul><li class="auto-cursor-target">On the left side of the dialog, under the <strong>General-Purpose Modeling</strong> domain, select the <strong>Requirements Project</strong>.</li><li class="auto-cursor-target">On the right side of the dialog, type the file name in the <strong>Name</strong> box.</li><li class="auto-cursor-target">On the right side of the dialog, click the <ac:image ac:thumbnail="true" ac:height="20"><ri:attachment ri:filename="select_location_button.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating Requirements Project" /></ri:attachment></ac:image> button and select the location to store the created project.<br /><ac:image><ri:attachment ri:filename="requirements_projects_templates.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating Requirements Project" /></ri:attachment></ac:image></li></ul></li><li class="atl-forced-newline">Click <strong>OK</strong>.<br />The new Requirement project is created with predefined structure as shown in the image below.<br /><ac:image><ri:attachment ri:filename="requirements_project_structure.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating Requirements Project" /></ri:attachment></ac:image></li></ol></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6ca5c72d-4d73-41ba-9f08-187394058cf6"><ac:parameter ac:name="id">564722836</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Working with projects" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720217 space=CRMP2024x version=1 -->
## PAGE 00026: Creating validation suites

- page_id: `136720217`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720217/Creating+validation+suites
- version_number: 1
- version_date: `2023-09-21T10:22:39.390+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Creating validation suites' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="4548ab2e-69df-473e-9086-d8e7c9a8bda7"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating validation suites" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720216 space=CRMP2024x version=2 -->
## PAGE 00027: Custom validation

- page_id: `136720216`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720216/Custom+validation
- version_number: 2
- version_date: `2024-01-29T14:58:20.379+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation
- labels: []

### NORMALIZED CONTENT

You can extend existing validation suites that come with [Profile](https://docs.nomagic.com/display/MD2024x/Profile)by customizing existing or creating your own validation suites and rules.

Find an appropriate topic:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can extend existing validation suites that come with <a href="https://docs.nomagic.com/display/MD2024x/Profile">Profile </a>by customizing existing or creating your own validation suites and rules.</p><p>Find an appropriate topic:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="220527e9-4a18-4cb6-9542-33054078b7f9" /></p>
````

<!--NOMAGIC_PAGE id=136720308 space=CRMP2024x version=2 -->
## PAGE 00028: Customizations

- page_id: `136720308`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720308/Customizations
- version_number: 2
- version_date: `2024-01-29T14:59:37.514+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT



### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="48183dd8-6841-43df-856a-270bcb5f1b03" /></p>
````

<!--NOMAGIC_PAGE id=136720312 space=CRMP2024x version=2 -->
## PAGE 00029: Customizing environment options

- page_id: `136720312`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720312/Customizing+environment+options
- version_number: 2
- version_date: `2024-01-29T14:54:34.052+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Customizing environment options' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="3b10d860-a699-4a69-90e6-f520f78375cc"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Customizing environment options" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720161 space=CRMP2024x version=1 -->
## PAGE 00030: Customizing requirement properties

- page_id: `136720161`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720161/Customizing+requirement+properties
- version_number: 1
- version_date: `2023-09-21T10:22:36.456+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

You can create specific properties in requirements specifications. This will help identify the requirement’s version, complexity, priority, severity, status, and other properties. Use the [CONFLUENCE_PAGE title='UML Profiling and DSL Guide' space='MD2024x'] to extend Requirements with custom properties. Add custom properties to the general properties list by extending the [CONFLUENCE_PAGE title='Extended Requirement' space='CRMP2024x'] class.

Customizing procedure details are described in [CONFLUENCE_PAGE title='Creating Customization Data' space='MD2024x'] and [CONFLUENCE_PAGE title='Using Customization Data' space='MD2024x'] in the [CONFLUENCE_PAGE title='UML Profiling and DSL Guide' space='MD2024x'].

To create custom properties

1. In your project, create a Package for your custom properties. How to create a new packageTo create a new package 
In the Containment tree, right-click the element.The element should be a namespace, such as a package, class, or requirement.Select **Create Element**> **Package**.Type a name for the new Package (e.g. Custom Properties).Press Enter.
2. In that package, create a new stereotype. [How to create a new stereotype >>](https://docs.nomagic.com/display/MD190/Stereotype#Stereotype-Creatingastereotype)
3. Apply a metaclass Class to the created stereotype. How to apply metaclass for a stereotypeTo apply a metaclass to a stereotypea. In the Containment tree, right-click the newly created stereotype. 
 b. From the shortcut menu, select **Metaclass**. 
 c. In the **Metaclass** dialog, select a Class. 
 d. Click **Apply**.
4. For the stereotype with the applied metaclass Class, create custom properties. How to create custom properties for a stereotypeTo create custom properties for a stereotypea. In the Containment tree, right-click stereotype. 
 b. From the shortcut menu, select **Create Element**. 
 c. In the **Create Element** dialog, select **Property**. 
 d.Type a property name and specify a value type.
5. Extend the ExtendedRequirement class using properties created in the stereotype (i.e., you must relate the stereotype with the Generalization relationship to the ExtendedRequirement class). How to extend ExtendedRequirement class by custom propertiesTo extend the ExtendedRequirement class using custom propertiesa. In the Containment tree, right-click stereotype. 
 b. From the shortcut menu, select **Create Relation** > **Outgoing**. 
 c. In the **Outgoing** dialog, select **Generalization**. 
 d. In the **Create New Generalization To** dialog, select the **List** tab, clear the **Apply Filter** check box, and select the *ExtendedRequirement [Class]*. 
 e. Click **OK**.
6. On the [CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024x'], click **Save Project** button and restart your project. 
Your custom properties are added to the general requirement properties. You can assign values to them in the Requirement’s [CONFLUENCE_PAGE title='Specification window' space='MD2024x'] or in the Properties panel. The following figure depicts how the stereotype related to the *ExtendedRequirement [Class]* looks in the [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x'] and [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'].

###### [IMAGE alt='' src=''] 
The *ExtendedRequirement [Class]* extended by the *author* property is shown in the Containment tree and diagram pane.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>You can create specific properties in requirements specifications. This will help identify the requirement’s version, complexity, priority, severity, status, and other properties. Use the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="UML Profiling and DSL Guide" /></ac:link> to extend Requirements with custom properties. Add custom properties to the general properties list by extending the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Extended Requirement" /><ac:plain-text-link-body><![CDATA[ExtendedRequirement]]></ac:plain-text-link-body></ac:link> class.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b1ffbe4a-24ac-4bbd-a744-effda597f978"><ac:rich-text-body><p>Customizing procedure details are described in <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating Customization Data" /></ac:link> and <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using Customization Data" /></ac:link> in the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="UML Profiling and DSL Guide" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create custom properties</p><hr /><ol><li><p class="auto-cursor-target">In your project, create a Package for your custom properties.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="11320caf-c4fc-4da1-a49c-cd7fbe8793a0"><ac:parameter ac:name="title">How to create a new package</ac:parameter><ac:rich-text-body>To create a new package<br /><hr /><ol><li><p>In the Containment tree, right-click the element.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="6ff24927-c919-4c94-bbb4-f1bb3397f1b2"><ac:rich-text-body><p>The element should be a namespace, such as a package, class, or requirement.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Select <strong>Create Element </strong>&gt;  <strong>Package</strong>.</li><li>Type a name for the new Package (e.g. Custom Properties).</li><li>Press Enter.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p class="auto-cursor-target">In that package, create a new stereotype. <a href="https://docs.nomagic.com/display/MD190/Stereotype#Stereotype-Creatingastereotype">How to create a new stereotype &gt;&gt;</a></p></li><li><p>Apply a metaclass Class to the created stereotype.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="f8688626-252a-482d-a15b-3d6fc52b2a44"><ac:parameter ac:name="title">How to apply metaclass for a stereotype</ac:parameter><ac:rich-text-body><p>To apply a metaclass to a stereotype</p><hr /><p>      a. In the Containment tree, right-click the newly created stereotype.<br />      b. From the shortcut menu, select <strong>Metaclass</strong>.<br />      c. In the <strong>Metaclass</strong> dialog, select a Class.<br />      d. Click <strong>Apply</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p>For the stereotype with the applied metaclass Class, create custom properties.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="4fc39c60-af1d-411d-91f3-4df8c32cf567"><ac:parameter ac:name="title">How to create custom properties for a stereotype</ac:parameter><ac:rich-text-body><p>To create custom properties for a stereotype</p><hr /><p>     a. In the Containment tree, right-click stereotype.<br />     b. From the shortcut menu, select <strong>Create Element</strong>.<br />     c. In the <strong>Create Element</strong> dialog, select <strong>Property</strong>.<br />     d.Type a property name and specify a value type.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p>Extend the ExtendedRequirement class using properties created in the stereotype (i.e., you must relate the stereotype with the Generalization relationship to the ExtendedRequirement class).</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="27695cab-7708-4273-b8de-02fe74d173e9"><ac:parameter ac:name="title">How to extend ExtendedRequirement class by custom properties</ac:parameter><ac:rich-text-body><p>To extend the ExtendedRequirement class using custom properties</p><hr /><p>     a. In the Containment tree, right-click stereotype.<br />     b. From the shortcut menu, select <strong>Create Relation</strong> &gt; <strong>Outgoing</strong>.<br />     c. In the <strong>Outgoing</strong> dialog, select <strong>Generalization</strong>.<br />     d. In the <strong>Create New Generalization To</strong> dialog, select the <strong>List</strong> tab, clear the <strong>Apply Filter</strong> check box, and select the <em>ExtendedRequirement [Class]</em>.<br />     e. Click <strong>OK</strong>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p>On the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[main toolbar]]></ac:plain-text-link-body></ac:link>, click <strong>Save Project</strong> button and restart your project.<br />Your custom properties are added to the general requirement properties. You can assign values to them in the Requirement’s <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Specification window" /></ac:link> or in the Properties panel.</p><p>The following figure depicts how the stereotype related to the <em>ExtendedRequirement [Class]</em> looks in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>.</p></li></ol><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="extended_requirement_with_custom_properties.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Customizing requirement properties" /></ri:attachment></ac:image><br />The <em>ExtendedRequirement [Class]</em> extended by the <em>author</em> property is shown in the <span class="confluence-link">Containment tree</span> and <span class="confluence-link">diagram pane</span>.</h6><p> </p>
````

<!--NOMAGIC_PAGE id=136720227 space=CRMP2024x version=1 -->
## PAGE 00031: Customizing severity levels

- page_id: `136720227`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720227/Customizing+severity+levels
- version_number: 1
- version_date: `2023-09-21T10:22:40.325+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation > Creating new validation rules > Specifying the validation rule properties
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Customizing severity levels' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="c472f826-023e-4cea-9782-7de375a19cdc"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Customizing severity levels" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720234 space=CRMP2024x version=1 -->
## PAGE 00032: Defining Constraint condition

- page_id: `136720234`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720234/Defining+Constraint+condition
- version_number: 1
- version_date: `2023-09-21T10:22:40.540+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation > Creating new validation rules
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Defining Constraint condition' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="94b4d96d-f5d8-4a3e-8d6d-618dd256ba3f"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Defining Constraint condition" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720293 space=CRMP2024x version=1 -->
## PAGE 00033: Derive

- page_id: `136720293`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720293/Derive
- version_number: 1
- version_date: `2023-09-21T10:22:43.522+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A 'Derive' relationship is a dependency between two requirements (a derived requirement and a source requirement), where the derived requirement is generated or inferred from the source requirement.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Derive Requirement Matrix' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="f4f79867-c1bd-4824-9b48-3a29c0ecc2af"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A 'Derive' relationship is a dependency between two requirements (a derived requirement and a source requirement), where the derived requirement is generated or inferred from the source requirement.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Derive Requirement Matrix" /></ac:link><br /></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720285 space=CRMP2024x version=1 -->
## PAGE 00034: Design Constraint

- page_id: `136720285`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720285/Design+Constraint
- version_number: 1
- version_date: `2023-09-21T10:22:42.696+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Design Constraint is a requirement that specifies a constraint on the implementation of a system or on a part of it.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="07bbde82-ce7f-4ddb-b31d-c442984f8a27"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Design Constraint is a requirement that specifies a constraint on the implementation of a system or on a part of it.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720276 space=CRMP2024x version=1 -->
## PAGE 00035: Diagram descriptions

- page_id: `136720276`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720276/Diagram+descriptions
- version_number: 1
- version_date: `2023-09-21T10:22:41.920+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts
- labels: []

### NORMALIZED CONTENT

This sections provides all descriptions of the requirement diagrams, tables, and matrices.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This sections provides all descriptions of the requirement diagrams, tables, and matrices.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="a0884140-1993-4632-8116-e15f80ffc3fa" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720086 space=CRMP2024x version=2 -->
## PAGE 00036: Diagrams tab

- page_id: `136720086`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720086/Diagrams+tab
- version_number: 2
- version_date: `2024-01-29T14:29:30.494+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

1361237152

1361237173

1361237163

true[CONFLUENCE_PAGE title='Diagrams tab' space='MD2024x']

1361237151

**On this page**

****

1361242634

**Related pages**

****

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="84491abb-f59e-4deb-aad6-ea6a22a37bbe"><ac:parameter ac:name="id">1361237152</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8e0567a3-4358-467e-9fac-14e34fdcbbb3"><ac:parameter ac:name="id">1361237173</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="82253d66-3018-41ef-9281-afeb097949b8"><ac:parameter ac:name="id">1361237163</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="058605a1-caf2-425a-b8f6-663041ed9043"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Diagrams tab" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0111d468-09bc-4958-8c77-1ea96ef8093d"><ac:parameter ac:name="id">1361237151</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4b09e412-4fb8-41a3-96ff-b96e8193a8b7" /></p><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e2529fe1-3862-4e78-981f-589273d5ed6b"><ac:parameter ac:name="id">1361242634</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><strong><br /></strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720314 space=CRMP2024x version=2 -->
## PAGE 00037: Disabling inbound network activity

- page_id: `136720314`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720314/Disabling+inbound+network+activity
- version_number: 2
- version_date: `2024-01-29T14:29:53.508+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Disabling inbound network activity' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="9ca239ea-f797-410d-968c-02e16c4b5c85"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Disabling inbound network activity" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720091 space=CRMP2024x version=1 -->
## PAGE 00038: Documentation tab

- page_id: `136720091`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720091/Documentation+tab
- version_number: 1
- version_date: `2023-09-21T10:22:34.741+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Documentation tab' space='MD2024x']true

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="23daaef9-926a-4932-a540-b00dc849b422"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Documentation tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f66a763c-1625-4208-9fa1-67e984e84365"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720283 space=CRMP2024x version=1 -->
## PAGE 00039: Element descriptions

- page_id: `136720283`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720283/Element+descriptions
- version_number: 1
- version_date: `2023-09-21T10:22:42.467+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts
- labels: []

### NORMALIZED CONTENT

This section provides all descriptions of the requirement elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This section provides all descriptions of the requirement elements.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="54827e81-6e19-4d8b-ab2e-d2c80760c18f" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720263 space=CRMP2024x version=1 -->
## PAGE 00040: Exchanging requirements with ReqIf

- page_id: `136720263`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720263/Exchanging+requirements+with+ReqIf
- version_number: 1
- version_date: `2023-09-21T10:22:41.408+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

23716579

23716590

23716580

Requirements are gathered and managed in dedicated requirements tools. When it comes to requirements refinement and integration with business, software, and system architecture, different requirements interchange formats are used. It can be comma separated value, MS Excel, Word, or XML. These are nonstandard ways, which bring drawbacks. It is clear that need for dedicated common format exists. This is why the German automotive industry started the open, non-proprietary format for requirements exchange development.

Starting with the upcoming v18.0, all MagicDraw-based Cameo Suite products will support ReqIF import as part of the new Cameo Requirements Modeler plugin.

23716578

##### What is ReqIF?

ReqIF is the XML-based international standard for requirement data exchange, standardized by the Object Management Group (OMG). It has solid recognition in the industry and adoption by many requirements management tool vendors. It is used to exchange requirement information between different tools and toolchains.

[IMAGE alt='' src='']“For requirement analysis, ReqIF is the same as Unified Modeling Language (UML) for modeling – it is the most popular and dedicated requirements interchange format.”

##### ReqIF Support in MagicDraw

ReqIF Importer imports and updates (previously imported) requirements in models with the following capabilities:

- Import process includes the ability for custom mapping with the option to import all data and dynamically create properties.
- Update process includes changing management support with requirements status identification. After import, new, changed, updated or obsolete requirements are identified with the ability to check the impact of changes.

[IMAGE alt='' src='']

Once imported, requirements become first-class citizens in the modeling world. That means they can be:

- Integrated with other models: business, software, and systems architecture, test cases, and toolchains: PLM tools (e.g. Teamcenter), CAD tools (e.g. Catia), and others. This enables requirements-driven design and communication of changes with all stakeholders.
- Reviewed with visualization in diagrams, tables, matrices, and structure maps.
- Analyzed with built-in and custom validation suites, coverage metrics, traceability.
- Collaborated with a global modeling project’s repository, supporting collaboration inside a project, change and configuration management, multisite support.
- Simulated with OMG standard-based model execution, debugging, animation, and user interface prototyping supporting framework.
- Published with MS Office and Open Office docs, Web-based reports, with the ability to have custom reports incorporating required data.

##### ReqIF Importer Features

1. Import data that originated in a wide variety of tools* [ATTACHMENT filename='021714_2253_Requirement3.png'] * Import tested with: IBM Rational DOORS 9.4, 9.5, Next Generation, Polarion, PTC Integrity, Siemens TC, and other ReqIF 1.0 compatible data sources.
2. Update existing data. It is possible to create relations to any other model element, e.g. test cases, or architectural components, to realize total traceability as required by the processes. On update, all custom relations are left untouched.
3. Change status identification (updated, new, unchanged, or obsolete) [ATTACHMENT filename='status5.png']
4. Requirements structure and structure changes support [ATTACHMENT filename='Structure1.png']
5. Physical requirements remove action [ATTACHMENT filename='remove-action2.png']
6. Status and summary notification message [ATTACHMENT filename='021714_2244_Requirement7.png']
7. Custom mapping 
[IMAGE alt='' src='']
8. Dynamic properties discovery , no need to determine what data is in ReqIF file, all the properties can be imported
9. Omit the data you don’t need to import
10. Rich text support [ATTACHMENT filename='rich.png']

##### More About ReqIF

###### ReqIF Recognition

The group working on the initial release of ReqIF consists of the ProSTEP iViP Association, Atego Systems GmbH, Audi AG, BMW AG, Continental AG, Daimler AG, HOOD GmbH, IBM, MKS GmbH, PROSTEP AG, Robert Bosch GmbH, and Volkswagen AG.

###### ReqIF Sources

- Rational DOORS, DOORS Next generation, IBM Rational Requirements composer ( http://www-01.ibm.com/software/rational/ )
- Polarion ( http://www.polarion.com/2014/reqif-solution.php )
- PTC Integrity ( http://www.mks.com/platform/our-product )
- Siemens Teamcenter ( http://m.plm.automation.siemens.com/en_us/Images/Siemens-PLM-Teamcenter-Requirements-Integrator-for-RIF-ReqIF-fs_tcm1224-213684.pdf )
- LieberLieber for EA ( http://www.lieberlieber.com/en/model-engineering/reqif/ )
- Agosense ( http://www.agosense.com/english/products/platform-und-adapter/agosensesymphony )
- ReqIF Server ( http://enso-managers.de/ )
- MS Excel to ReqIF exporter ( http://www.pyrrho.com/en/ReqIF/ReqIF-Intro.htm )
- GitHub EnterpriseArchitect_ReqIF_AddIn ( https://github.com/redsteve/EnterpriseArchitect_ReqIF_AddIn )
- Requisis Rex ([https://requisis.com/de/produkte/rex-doors-reqif-rif-export.html](https://requisis.com/de/produkte/rex-doors-reqif-rif-export.html))
- VISURE ([http://www.visuresolutions.com/](http://www.visuresolutions.com/))
- Formalmind ([www.formalmind.com/](http://www.formalmind.com/))

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f76d3b19-8b3d-4ade-8cce-5379ec648978"><ac:parameter ac:name="id">23716579</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6bb64e0f-ad96-4947-957b-cf188feaa8fb"><ac:parameter ac:name="id">23716590</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c5dcd745-c2ed-4229-b4f0-d1a4953710bf"><ac:parameter ac:name="id">23716580</ac:parameter><ac:rich-text-body><p>Requirements are gathered and managed in dedicated requirements tools. When it comes to requirements refinement and integration with business, software, and system architecture, different requirements interchange formats are used. It can be comma separated value, MS Excel, Word, or XML. These are nonstandard ways, which bring drawbacks. It is clear that need for dedicated common format exists. This is why the German automotive industry started the open, non-proprietary format for requirements exchange development.</p><p>Starting with the upcoming v18.0, all MagicDraw-based Cameo Suite products will support ReqIF import as part of the new Cameo Requirements Modeler plugin.</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="455cfe49-c146-495c-95dc-f3db76e3fbdf" /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5370ae4c-781c-4444-a886-49891db6b4ad"><ac:parameter ac:name="id">23716578</ac:parameter><ac:rich-text-body><h3>What is ReqIF?</h3><p>ReqIF is the XML-based international standard for requirement data exchange, standardized by the Object Management Group (OMG). It has solid recognition in the industry and adoption by many requirements management tool vendors. It is used to exchange requirement information between different tools and toolchains.</p><p><ac:image ac:thumbnail="true" ac:height="65"><ri:attachment ri:filename="Requirements_Interchange_Format_ReqIF_Importer.jpg"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image>“For requirement analysis, ReqIF is the same as Unified Modeling Language (UML) for modeling – it is the most popular and dedicated requirements interchange format.”</p><h3>ReqIF Support in MagicDraw</h3><p>ReqIF Importer imports and updates (previously imported) requirements in models with the following capabilities:</p><ul><li>Import process includes the ability for custom mapping with the option to import all data and dynamically create properties.</li><li>Update process includes changing management support with requirements status identification. After import, new, changed, updated or obsolete requirements are identified with the ability to check the impact of changes.</li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="main-diagram-good.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image></p><p>Once imported, requirements become first-class citizens in the modeling world. That means they can be:</p><ul><li><strong>Integrated</strong> with other models: business, software, and systems architecture, test cases, and toolchains: PLM tools (e.g. Teamcenter), CAD tools (e.g. Catia), and others. This enables requirements-driven design and communication of changes with all stakeholders.</li><li><strong>Reviewed</strong> with visualization in diagrams, tables, matrices, and structure maps.</li><li><strong>Analyzed</strong> with built-in and custom validation suites, coverage metrics, traceability.</li><li><strong>Collaborated</strong> with a global modeling project’s repository, supporting collaboration inside a project, change and configuration management, multisite support.</li><li><strong>Simulated</strong> with OMG standard-based model execution, debugging, animation, and user interface prototyping supporting framework.</li><li><strong>Published</strong> with MS Office and Open Office docs, Web-based reports, with the ability to have custom reports incorporating required data.</li></ul><h3>ReqIF Importer Features</h3><ol><li><strong>Import</strong> data that originated in a wide variety of tools*<br /><ac:image ac:align="center"><ri:attachment ri:filename="021714_2253_Requirement3.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image><br />* Import tested with: IBM Rational DOORS 9.4, 9.5, Next Generation, Polarion, PTC Integrity, Siemens TC, and other ReqIF 1.0 compatible data sources.</li><li><strong>Update</strong> existing data. It is possible to create relations to any other model element, e.g. test cases, or architectural components, to realize total traceability as required by the processes. On update, all custom relations are left untouched.</li><li><strong>Change status</strong> identification (updated, new, unchanged, or obsolete)<br /><ac:image ac:align="center"><ri:attachment ri:filename="status5.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image></li><li><strong>Requirements structure</strong> and structure changes support<br /><ac:image ac:align="center"><ri:attachment ri:filename="Structure1.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image></li><li><strong>Physical requirements remove</strong> action<br /><ac:image ac:align="center"><ri:attachment ri:filename="remove-action2.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image></li><li><strong>Status and summary </strong>notification message<br /><ac:image ac:align="center"><ri:attachment ri:filename="021714_2244_Requirement7.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image></li><li><strong>Custom mapping<br /><ac:image ac:align="center"><ri:attachment ri:filename="mapping2.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image></strong></li><li><strong>Dynamic properties discovery</strong>, no need to determine what data is in ReqIF file, all the properties can be imported</li><li><strong>Omit the data</strong> you don’t need to import</li><li><strong>Rich text</strong> support<br /><ac:image ac:align="center"><ri:attachment ri:filename="rich.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ri:attachment></ac:image></li></ol><h3>More About ReqIF</h3><h4>ReqIF Recognition</h4><p>The group working on the initial release of ReqIF consists of the ProSTEP iViP Association, Atego Systems GmbH, Audi AG, BMW AG, Continental AG, Daimler AG, HOOD GmbH, IBM, MKS GmbH, PROSTEP AG, Robert Bosch GmbH, and Volkswagen AG.</p><h4>ReqIF Sources</h4><ul><li>Rational DOORS, DOORS Next generation, IBM Rational Requirements composer (<a href="http://www-01.ibm.com/software/rational/">http://www-01.ibm.com/software/rational/</a>)</li><li>Polarion (<a href="http://www.polarion.com/2014/reqif-solution.php">http://www.polarion.com/2014/reqif-solution.php</a>)</li><li>PTC Integrity (<a href="http://www.mks.com/platform/our-product">http://www.mks.com/platform/our-product</a>)</li><li>Siemens Teamcenter (<a href="http://m.plm.automation.siemens.com/en_us/Images/Siemens-PLM-Teamcenter-Requirements-Integrator-for-RIF-ReqIF-fs_tcm1224-213684.pdf">http://m.plm.automation.siemens.com/en_us/Images/Siemens-PLM-Teamcenter-Requirements-Integrator-for-RIF-ReqIF-fs_tcm1224-213684.pdf</a>)</li><li>LieberLieber for EA (<a href="http://www.lieberlieber.com/en/model-engineering/reqif/">http://www.lieberlieber.com/en/model-engineering/reqif/</a>)</li><li>Agosense (<a href="http://www.agosense.com/english/products/platform-und-adapter/agosensesymphony">http://www.agosense.com/english/products/platform-und-adapter/agosensesymphony</a>)</li><li>ReqIF Server (<a href="http://enso-managers.de/">http://enso-managers.de/</a>)</li><li>MS Excel to ReqIF exporter (<a href="http://www.pyrrho.com/en/ReqIF/ReqIF-Intro.htm">http://www.pyrrho.com/en/ReqIF/ReqIF-Intro.htm</a>)</li><li>GitHub EnterpriseArchitect_ReqIF_AddIn (<a href="https://github.com/redsteve/EnterpriseArchitect_ReqIF_AddIn">https://github.com/redsteve/EnterpriseArchitect_ReqIF_AddIn</a>)</li><li><p>Requisis Rex (<a href="https://requisis.com/de/produkte/rex-doors-reqif-rif-export.html">https://requisis.com/de/produkte/rex-doors-reqif-rif-export.html</a>)</p></li><li><p>VISURE (<a href="http://www.visuresolutions.com/">http://www.visuresolutions.com/</a>)</p></li><li><p>Formalmind (<a href="http://www.formalmind.com/">www.formalmind.com/</a>)</p></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720147 space=CRMP2024x version=1 -->
## PAGE 00041: Exporting ReqIF files from the command-line interface

- page_id: `136720147`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720147/Exporting+ReqIF+files+from+the+command-line+interface
- version_number: 1
- version_date: `2023-09-21T10:22:36.057+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Exporting requirements
- labels: []

### NORMALIZED CONTENT

Exporting from the command-line interface is useful when you want to export files automatically, e.g., once a day at midnight.

To export a ReqIF file from the command-line interface

1. Open the Command Prompt window
2. Go to the <model editor installationdirectory>/plugins/com.nomagic.requirements directory containing the *reqifexport.exe* file.
3. At the command prompt, type the following command and specify the values of the required arguments: reqifexport project_descriptor=<project URL> reqif_file=<path to ReqIF file> export_type=<specifications|elements> elements= <hyperlinks or qualified names of elements> source_tool_id=<ReqIF flavor> Where:
  - **project_descriptor** is the URL of a project. How to get a project descriptor?Start your modeling tool and open the required project.In the main menu, go to **File** > **Project Properties** and select the **General** tab.Find the project descriptor specified in the **Project Descriptor** box at the bottom of the **Project Properties** dialog and copy it to the clipboard.
  - **reqif_file** is the path to the ReqIF file you want to export. If there is a space in a path, surround the argument and its value with escaped quote (\").
  - **export_type** is the type of exported data. The valid value of this argument:
    - 
      - **elements** - if you want to export the plain list of requirements.
      - **specifications** - if you want to export requirements and hierarchical relationships between them.
  - **elements** are hyperlinks or qualified names (or the combination of both) of the elements to be exported. They must be separated by semicolon (;) symbols. How to get the hyperlink of an element?Start your modeling tool and open the required project.In the Containment tree, right-click an element and select **Copy Element Hyperlink**.The hyperlink of the element is now copied to the clipboard. If you want to export**Specifications**, make sure you specify packages with the «Specification» stereotype applied. To apply the stereotype, your project has to usethe*ReqIF Profile*. if you try to export packages that don't have the «Specification» stereotype, the command will fail.
  - **source_tool_id** is the flavor of the ReqIF file. Currently supported flavors are **MagicDraw**, **IBM Rational DOORS**, **Polarion**, **Teamcenter** and **Reqtify**. Note that the **source_tool_id** argument is optional.
4. Press **Enter**.

The ReqIF file with the desired data is now exported to the specified directory.

##### Using a properties file

To make exporting from the command-line interface quicker you can specify arguments in a properties file, which can be easily edited or reused.

To export a ReqIF file from the command-line interface using a properties file

1. Create a properties file and specify the values of the following arguments: See the example of a properties file below. text1trueProject Properties > General.
#
reqif_file=C:/Users/johnsmith/Documents/Project_Requirements/project_requirements.reqif
#
# Specify the path to the ReqIF file.
# NOTE: If there is a space in a path, surround the argument and its value with escaped quote (\").
#
export_type=elements
#
# Specify the type of exported data. The value of the argument can be "specifications" or "elements".
#
elements=mdel://_17_0_2_8f90291_1308667744583_445317_24132;mdel://_17_0_2_8f90291_1308667618344_111153_24071
#
# Specify the hyperlinks or qualified names (or the combination of both) of the elements to be exported.
# To get the hyperlink of an element, open a project, right-click the element in the Containment tree and select "Copy Element Hyperlink".
#
source_tool_id=MagicDraw
#
# Specify the flavor of the ReqIF file. Supported flavors are: "MagicDraw", "IBM Rational DOORS", "Polarion", "Teamcenter" and "Reqtify".
# NOTE: This argument is optional.
#]]> When creating a properties file on Windows OS, use only / or \\ as a path separator, otherwise the command will fail.
  - project_descriptor
  - reqif_file
  - **export_type**
  - **elements**
  - **source_tool_id**
2. Open the Command Prompt window.
3. Go to the <model editor installationdirectory>/plugins/com.nomagic.requirements directory containing the *reqifexport.exe* file.
4. At the command prompt, type the following command and specify the value of the **properties_file** argument. reqifexport properties_file=<path to properties file> Where **properties_file** is the path to the properties file to be used.
5. Press **Enter**.

The ReqIF file with the desired data is now exported to the specified directory.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Exporting from the command-line interface is useful when you want to export files automatically, e.g., once a day at midnight.</p><p> </p><p>To export a ReqIF file from the command-line interface</p><hr /><ol><li>Open the Command Prompt window</li><li>Go to the <em><span style="color: rgb(0,0,0);">&lt;model editor installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.requirements</span></em><span style="color: rgb(0,0,0);"> directory containing the <em>reqifexport.exe</em> file.</span></li><li><span style="color: rgb(0,0,0);">At the command prompt, type the following command and specify the values of the required arguments:</span><pre>reqifexport project_descriptor=&lt;project URL&gt; reqif_file=&lt;path to ReqIF file&gt; export_type=&lt;specifications|elements&gt; elements=</pre><pre>&lt;hyperlinks or qualified names of elements&gt; source_tool_id=&lt;ReqIF flavor&gt;</pre><p>Where:</p><ul><li><p><strong>project_descriptor</strong> is the URL of a project.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="bc06a5ad-5a37-4ffe-bbdf-b3d946ace80e"><ac:parameter ac:name="title">How to get a project descriptor?</ac:parameter><ac:rich-text-body><ol><li>Start your modeling tool and open the required project.</li><li>In the main menu, go to <strong>File</strong> &gt; <strong>Project Properties</strong> and select the <strong>General</strong> tab.</li><li>Find the project descriptor specified in the <strong>Project Descriptor</strong> box at the bottom of the <strong>Project Properties</strong> dialog and copy it to the clipboard.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><strong>reqif_file</strong> is the path to the ReqIF file you want to export.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="0e7bc59b-b174-403d-a104-a5a654c8d79a"><ac:rich-text-body><p>If there is a space in a path, surround the argument and its value with escaped quote <span>(\&quot;).</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><strong>export_type</strong> is the type of exported data. The valid value of this argument:<br /> </p><ul><li style="list-style-type: none;background-image: none;"><ul><li><p><strong>elements</strong> - i<span style="color: rgb(0,0,0);">f you want to export the plain list of requirements.</span></p></li><li><p><strong>specifications</strong> - i<span style="color: rgb(0,0,0);">f you want to export requirements and hierarchical relationships between them.</span></p><p> </p></li></ul></li></ul></li><li><p><strong>elements</strong> are hyperlinks or qualified names (or the combination  of both) of the elements to be exported. They must be separated by semicolon (;) symbols.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="fcbe8166-4962-4789-b836-dbbd969ec63d"><ac:parameter ac:name="title">How to get the hyperlink of an element?</ac:parameter><ac:rich-text-body><ol><li>Start your modeling tool and open the required project.</li><li>In the Containment tree, right-click an element and select <strong>Copy Element Hyperlink</strong>.</li></ol><p>The hyperlink of the element is now copied to the clipboard.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5f9d182a-cd4b-4d01-b08e-7cd23b33f52a"><ac:rich-text-body><p><span>If you want to export </span><strong>Specifications</strong><span>, make sure you specify packages with the «Specification» stereotype applied</span><span>. To apply the stereotype, your project has to use </span><span>the </span><em>ReqIF Profile</em><span>. if you try to export packages that don't have <span>the «Specification» stereotype, the command will fail.</span></span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li><p><strong>source_tool_id</strong> is the flavor of the ReqIF file. Currently supported flavors are <strong>MagicDraw</strong>, <strong>IBM Rational DOORS</strong>, <strong>Polarion</strong>, <strong>Teamcenter</strong> and <strong>Reqtify</strong>. Note that the <strong>source_tool_id</strong> argument is optional.</p></li></ul></li><li><p>Press <strong>Enter</strong>.</p></li></ol><p>The ReqIF file with the desired data is now exported to the specified directory.<br /> </p><h3><span>Using a properties file</span></h3><p>To make exporting from the command-line interface quicker you can specify arguments in a properties file, which can be easily edited or reused.</p><p> </p><p>To export a ReqIF file from the command-line interface using a properties file</p><hr /><ol><li>Create a properties file and specify the values of the following arguments:<br /><ul><li><strong>project_descriptor</strong></li><li><strong>reqif_file</strong></li><li><strong><strong>export_type</strong></strong></li><li><strong><strong>elements</strong></strong></li><li><strong><strong>source_tool_id</strong><br /> </strong></li></ul><p>See the example of a properties file below.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e9b0a07d-28d7-4388-94f1-32faec5da20c"><ac:parameter ac:name="language">text</ac:parameter><ac:parameter ac:name="firstline">1</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[project_descriptor=file:/C:/Users/johnsmith/Downloads/MagicDraw_185/samples/requirements/MagicLibrary%20requirements.mdzip
#
# Specify the project URL.
# To get a project descriptor, open a project and in the main menu go to File > Project Properties > General.
#
reqif_file=C:/Users/johnsmith/Documents/Project_Requirements/project_requirements.reqif
#
# Specify the path to the ReqIF file.
# NOTE: If there is a space in a path, surround the argument and its value with escaped quote (\").
#
export_type=elements
#
# Specify the type of exported data. The value of the argument can be "specifications" or "elements".
#
elements=mdel://_17_0_2_8f90291_1308667744583_445317_24132;mdel://_17_0_2_8f90291_1308667618344_111153_24071
#
# Specify the hyperlinks or qualified names (or the combination  of both) of the elements to be exported.
# To get the hyperlink of an element, open a project, right-click the element in the Containment tree and select "Copy Element Hyperlink".
#
source_tool_id=MagicDraw
#
# Specify the flavor of the ReqIF file. Supported flavors are: "MagicDraw", "IBM Rational DOORS", "Polarion", "Teamcenter" and "Reqtify".
# NOTE: This argument is optional.
#]]></ac:plain-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a747b836-052e-4bff-a358-e5edaed77878"><ac:rich-text-body><p>When creating a properties file on Windows OS, use only / or \\ as a path separator, otherwise the command will fail.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>Open the Command Prompt window.</li><li>Go to the <em><span style="color: rgb(0,0,0);">&lt;model editor installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.requirements</span></em><span style="color: rgb(0,0,0);"> directory containing the <em>reqifexport.exe</em> file.</span></li><li><p>At the command prompt, type the following command and specify the value of the <strong>properties_file</strong> argument.</p><pre>reqifexport properties_file=&lt;path to properties file&gt;</pre><p>Where <strong>properties_file</strong> is the path to the properties file to be used.<br /><br /></p></li><li><span style="color: rgb(0,0,0);"><span><span style="color: rgb(51,51,51);">Press <strong>Enter</strong>.</span></span></span></li></ol><p>The ReqIF file with the desired data is now exported to the specified directory.</p><p> </p>
````

<!--NOMAGIC_PAGE id=136720141 space=CRMP2024x version=2 -->
## PAGE 00042: Exporting requirements

- page_id: `136720141`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720141/Exporting+requirements
- version_number: 2
- version_date: `2024-01-29T14:58:50.619+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

831575275

831575277

831575276

You can export ReqIF files to be used with:

- IBM DOORS 9.4, 9.5, and 9.6
- IBM DOORS Next Generation
- PTC Integrity
- Polarion REQUIREMENTS
- Siemens Teamcenter
- Dassault Systemes Reqtify

Exporting requirements to ReqIF files ensures that all html formatting, images, and hyperlinks are represented in ReqIF format file properly. You can choose to export project elements or specifications, also, advanced users can create automated exports and scheduled exports from Teamwork Server or Teamwork Cloud projects. It should be noted that the exported files keep their original names.

It is recommended to export requirements into a separate project which can be later used in other models as a used project.

To export requirements to a ReqIF file

1. Open a project from which you want to export requirements .
2. From the File menu, select Export To > Requirement Interchange Format (ReqIF) File .
3. Choose to export one of the following:
  - Elements - i f you want to export the plain list of requirements.
  - **Specifications** - if you want to export requirements and hierarchical relationships between them. If you choose to export **Specifications**, make sure you have at least one package with the «Specification» stereotype applied. To apply the stereotype, your project has to usethe *ReqIF Profile*. When you try to export specifications from the project that doesn't have the *ReqIF Profile* used in it, you get the message asking if you want to use the profile. In this case, click **Yes**, apply the «Specification» stereotype to the required packages and repeat the export procedure.
4. In the open **Select Elements / Select Specification Package** dialog, select the elements or specification packages you want to export and click [IMAGE alt='' src=''] or [IMAGE alt='' src=''] (if you want to add elements recursively). Then they appear in the **Selected elements** list on the right side of the dialog.
5. When you're done selecting, click **OK**.
6. In the **Select ReqIF file** dialog, select the output location for the exported ReqIF file, then select the file you want to export or type the file name to create a new one.
7. In the **ReqIF Flavor** pane on the right of the **Select ReqIF file** dialog, select the flavor of your exported ReqIF file. 
[IMAGE alt='' src=''] If you cannot find the needed **ReqIF Flavor**on the list, please choose**MagicDraw**.
8. Click **Export**.

Images attached to the model are exported to the ReqIF file automatically as well.

When the ReqIF file is exported, a notification message appears, stating the quantity of exported specifications, elements and relationships. If you choose to export elements only, the message doesn't contain lines that indicate exported specifications and relationships. 
 
Click the **Note: you can change import/export and mapping options here** link in the notification message, if you want to change these options.

[IMAGE alt='' src='']

The notification message is displayed for a fixed duration, but you can find all project notification messages in the Notification Window. To open the Notification Window, click **Window** > **Notification Window**, or press Ctrl+M.

##### Changing requirements exporting options

Changing requirements exporting options is beneficial if you have a custom requirement type defined, or you are exporting not a requirement file but another type of data, for example, test cases.

A requirement type is limited to class and class extended types.

You can change the following export options:

- Specify an element type to create for the objects you are exporting
- Specify a relationship type to create for the relationships you are exporting
- Specify a path to the output location for exported resources (images, documents, etc.)
- Choose whether to export all properties or not and form a list of ignored and not exported properties

To change ReqIF file exporting options

1. Click Options > Project . The Project Options dialog opens.
2. In the options group list, select General , then scroll down to the ReqIF options group.
3. Click a desired option specification cell to change it's value.
4. Click OK after you are finished.

831575274

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="b88424ea-8ded-47af-ba86-3f670bd0f8ea"><ac:parameter ac:name="id">831575275</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b38a5fff-7672-4da8-ba16-5d0c76f7b79a"><ac:parameter ac:name="id">831575277</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="60f48de4-7291-4ac2-9dca-2545921276dd"><ac:parameter ac:name="id">831575276</ac:parameter><ac:rich-text-body><p>You can export ReqIF files to be used with:</p><ul><li>IBM DOORS 9.4, 9.5, and 9.6</li><li>IBM DOORS Next Generation</li><li>PTC Integrity<ac:inline-comment-marker ac:ref="df9cd3fc-66fd-495a-82c3-e313948825c4"> <br /></ac:inline-comment-marker></li><li>Polarion REQUIREMENTS</li><li>Siemens Teamcenter</li><li>Dassault Systemes Reqtify</li></ul><p><ac:inline-comment-marker ac:ref="362c5c55-7846-48e2-a041-900f38cb0c54">Exporting requirements to ReqIF files ensures that all html formatting, images, and hyperlinks are represented in ReqIF format file properly.</ac:inline-comment-marker> You can choose to export project elements or specifications, also, advanced users can create automated exports and scheduled exports from <ac:inline-comment-marker ac:ref="8cd4c4a0-62cc-4a68-9e38-9d392ee85014">Teamwork Server or Teamwork Cloud</ac:inline-comment-marker> projects. It should be noted that the exported files keep their original names. </p><p><span style="color: rgb(51,51,51);">It is recommended to export requirements into a separate project which can be later used in other models as a used project. </span></p><p><br /></p><p>To export requirements to a ReqIF file</p><hr /><ol><li>Open a project from which you want to export requirements<ac:inline-comment-marker ac:ref="fe6aea72-d48c-400a-b6c2-f81169ebbab8">.</ac:inline-comment-marker></li><li>From the <strong>File</strong> menu, select <strong>Export To</strong> &gt; <strong>Requirement Interchange Format (ReqIF) File</strong>.</li><li>Choose to export one of the following:<br /><br /><ul><li><strong>Elements</strong> - i<span style="color: rgb(0,0,0);">f you want to export the plain list of requirements.</span></li><li><p><strong>Specifications</strong> - i<span style="color: rgb(0,0,0);">f you want to export requirements and hierarchical relationships between them.<br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e609815c-6c8d-48cc-8086-fc0bda6658ea"><ac:rich-text-body><p>If you choose to export <strong>Specifications</strong>, make sure you have at least one package with the «Specification» stereotype applied<span>. To apply the stereotype, your project has to use </span>the <em>ReqIF Profile</em>. When you try to export specifications from the project that doesn't have the <em>ReqIF Profile</em> used in it, you get the message asking if you want to use the profile. In this case, click <strong>Yes</strong>, apply the <span>«Specification» stereotype to the required packages and repeat the export procedure.</span></p></ac:rich-text-body></ac:structured-macro></li></ul></li><li><p>In the open <strong>Select Elements / Select Specification Package</strong> dialog, <ac:inline-comment-marker ac:ref="45829242-2d6a-4005-b772-bb99a2425bde">select</ac:inline-comment-marker> the elements or specification packages you want to export and click <ac:image ac:title="Add" ac:alt="Add"><ri:attachment ri:filename="add_button.png"><ri:page ri:space-key="MD185" ri:content-title="_buttons" /></ri:attachment></ac:image> or <ac:image ac:title="Add Recursively" ac:alt="Add Recursively"><ri:attachment ri:filename="add_recursively_button.png"><ri:page ri:space-key="MD185" ri:content-title="_buttons" /></ri:attachment></ac:image> (if you want to add elements recursively). Then they appear in the <strong>Selected elements</strong> list on the right side of the dialog.</p></li><li><p>When you're done selecting, click <strong>OK</strong>.</p></li><li><p>In the <strong>Select ReqIF file</strong> dialog, select the output location for the exported ReqIF file, then select the file you want to export or type the file name to create a new one.</p></li><li class="inline-comment-marker"><p class="auto-cursor-target">In the <strong>ReqIF Flavor</strong> pane on the right of the <strong>Select ReqIF file</strong> dialog, select the flavor of your exported ReqIF file.<br /><ac:image><ri:attachment ri:filename="ReqIF.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exporting requirements" /></ri:attachment></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9a572b05-9240-4f9c-a046-cb5572017166"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">If you cannot find the needed <strong>ReqIF Flavor </strong>on the list</span><span style="color: rgb(62,63,64);">, please choose </span><strong>MagicDraw</strong><span style="color: rgb(62,63,64);">.</span></p></ac:rich-text-body></ac:structured-macro></li><li><p>Click <strong>Export</strong>.</p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="56fcc733-fb33-4319-9b88-086c88f0049b"><ac:rich-text-body><p>Images attached to the model are exported to the ReqIF file automatically as well.</p></ac:rich-text-body></ac:structured-macro><p><span style="color: rgb(51,51,51);"><br />When the ReqIF file is exported, a notification message appears, stating the quantity of exported specifications, elements and relationships. If you choose to export elements only, the message doesn't contain lines that indicate exported specifications and relationships.</span><br class="atl-forced-newline" /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(51,51,51);"> </span><br class="atl-forced-newline" />Click the <strong>Note: you can change import/export and mapping options here</strong> link in the notification message, if you want to change these options.</p><p><ac:image ac:title="Notification message informing about exported requirements " ac:alt="Notification message informing about exported requirements "><ri:attachment ri:filename="export_notification.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Exporting requirements" /></ri:attachment></ac:image></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="16e5f407-cc18-4a60-a1cc-71dbf73bf520"><ac:rich-text-body><p>The notification message is displayed for a fixed duration, but you can find all project notification messages in the Notification Window. To open the Notification Window, click <strong>Window</strong> &gt; <strong>Notification Window</strong>, or press <ac:inline-comment-marker ac:ref="3c27ab2b-a016-4d25-a51b-435310c34dc7">Ctrl</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="3c27ab2b-a016-4d25-a51b-435310c34dc7"> + </ac:inline-comment-marker><ac:inline-comment-marker ac:ref="3c27ab2b-a016-4d25-a51b-435310c34dc7">M</ac:inline-comment-marker><ac:inline-comment-marker ac:ref="3c27ab2b-a016-4d25-a51b-435310c34dc7">.</ac:inline-comment-marker></p></ac:rich-text-body></ac:structured-macro><h3>Changing requirements exporting options</h3><p>Changing requirements exporting options is beneficial if you have a custom requirement type defined, or you are exporting not a requirement file but another type of data, for example, test cases.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="ee07efc4-ebf6-4882-8665-d219e6feae09"><ac:rich-text-body><p>A requirement type is limited to class and class extended types.</p></ac:rich-text-body></ac:structured-macro><p>You can change the following export options:</p><ul><li>Specify an element type to create for the objects you are exporting</li><li>Specify a relationship type to create for the relationships you are exporting</li><li>Specify a path to the output location for exported resources (images, documents, etc.)</li><li>Choose whether to export all properties or not and form a list of ignored and not exported properties</li></ul><p><br class="atl-forced-newline" /> To change ReqIF file exporting options</p><hr /><ol><li>Click <strong>Options</strong> &gt; <strong>Project</strong>. The <strong>Project Options</strong> dialog opens.</li><li>In the options group list, select <strong>General</strong>, then scroll down to the <strong>ReqIF</strong> options group.</li><li>Click a desired option specification cell to change it's value.<span style="color: rgb(129,137,156);"> </span></li><li>Click <strong>OK</strong> after you are finished.</li></ol></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="82e73ee2-98e0-45d1-9c52-19845d20d6ba"><ac:parameter ac:name="id">831575274</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="b474465c-d7e9-4e74-b0e0-62173284ff6e" /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720286 space=CRMP2024x version=1 -->
## PAGE 00043: Extended Requirement

- page_id: `136720286`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720286/Extended+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:42.799+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

An Extended Requirement is a standard Requirement subtype, which adds some properties to a requirement element. These properties such as a source, risk, and verify method are important for the requirement management. Specific projects should add their own properties. All these properties are now available in the standard Requirement Specification window and Requirements Table. If any of these property values is specified, a requirement is automatically converted to ExtendedRequirement.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="ae6d89ac-5ed9-4155-b690-090226ad8d5e"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>An Extended Requirement is a standard Requirement subtype, which adds some properties to a requirement element. These properties such as a source, risk, and verify method are important for the requirement management. Specific projects should add their own properties. All these properties are now available in the standard Requirement Specification window and Requirements Table. If any of these property values is specified, a requirement is automatically converted to ExtendedRequirement.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720253 space=CRMP2024x version=2 -->
## PAGE 00044: Extracting Constraint from Requirement

- page_id: `136720253`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720253/Extracting+Constraint+from+Requirement
- version_number: 2
- version_date: `2025-01-22T08:02:11.535+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

INLINE

The Extracting Constraint from Requirement functionality provides the ability to verify Requirements easier when trying to prove the assertion is true (or false). A glossary mechanism extracts the constraint directly from the Requirement text. If you want to create constraints and associate them with the requirements automatically, you can use the extract Constraint from Requirement text functionality.

To extract Constraint value from Requirement text

1. [CONFLUENCE_PAGE title='Using Requirement patterns glossary' space='']Use the Requirements patterns glossary in Requirement text.
2. 
3. .

##### creating_satisfyCreating the Satisfy relationship

The specific value of the design element must satisfy the Requirement. As shown below, the *distanceOnQuickCharge* value of the *High-voltage Battery* Block satisfies the *Quick charge mode distance* Requirement.

[IMAGE alt='' src='']

##### extracting_constExtracting Constraint from Requirement

To extract a Constraint from a Requirement

1. Right-click a value property in the compartment area of the element shape.
2. Select Tools > Extract Constraint From Requirement . The constraint is created automatically with a value and condition pattern defined in the Requirement.

In the example below, the text "at least 70" of the *Quick charge mode distance* Requirement is automatically parsed to "distanceOnQuickCharge >= 70" and solved as a constraint.

[IMAGE alt='' src='']

After selecting the **Extract Constraint From Requirement** command, the constraint {distanceOnQuickCharge >=70.0} is automatically created. It satisfies the requirement text "at least 70".

[IMAGE alt='' src='']

**Related pages**

- [CONFLUENCE_PAGE title='Importing requirements' space='']
- [CONFLUENCE_PAGE title='Exporting requirements' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="ee5a8af3-70cb-429a-97e0-483970224533"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>The Extracting Constraint from Requirement functionality provides the ability to verify Requirements easier when trying to prove the assertion is true (or false). A glossary mechanism extracts the constraint directly from the Requirement text. If you want to create constraints and associate them with the requirements automatically, you can use the extract Constraint from Requirement text functionality.</p><p><br /></p><p>To extract Constraint value from Requirement text</p><hr /><ol><li><span class="confluence-link"><ac:link><ri:page ri:content-title="Using Requirement patterns glossary" /><ac:link-body><span class="confluence-link">Use the Requirements patterns glossary in Requirement text</span>.</ac:link-body></ac:link><br /></span></li><li><ac:link ac:anchor="creating_satisfy"><ac:plain-text-link-body><![CDATA[Create the Satisfy relationship between the specific value of design element and requirement.]]></ac:plain-text-link-body></ac:link><span style="color: rgb(51,51,51);"><br /></span></li><li><span style="color: rgb(51,51,51);"><span class="confluence-embedded-file-wrapper"><ac:link ac:anchor="extracting_const"><ac:plain-text-link-body><![CDATA[Extract Constraint from Requirement text]]></ac:plain-text-link-body></ac:link>.<br /></span></span></li></ol><h3><span class="confluence-link"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="30a8ab4b-ccaa-4983-b265-8f31d6d39727"><ac:parameter ac:name="">creating_satisfy</ac:parameter></ac:structured-macro>Creating the Satisfy relationship </span></h3><p><span style="color: rgb(51,51,51);"><span class="confluence-link">The specific value of the design element must satisfy the Requirement. As shown below</span>, the <em>distanceOnQuickCharge</em> value of the <em>High-voltage Battery</em> Block satisfies the <em>Quick charge mode distance</em> Requirement.</span></p><p><span style="color: rgb(51,51,51);"><ac:image><ri:attachment ri:filename="block_satisfies_requirement.png" /></ac:image><br /></span></p><h3><span class="confluence-link"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="21f658d7-5a60-4c9a-aab6-9470de1093ad"><ac:parameter ac:name="">extracting_const</ac:parameter></ac:structured-macro>Extracting Constraint from Requirement</span></h3><p>To extract a Constraint from a Requirement</p><hr /><ol><li>Right-click a value property in the compartment area of the element shape.</li><li>Select<strong> Tools</strong> &gt; <strong>Extract Constraint From Requirement</strong>.<br />The constraint is created automatically with a value and condition pattern defined in the Requirement.</li></ol><p><br /></p><p>In the example below, the text &quot;at least 70&quot; of the <span style="color: rgb(51,51,51);"><em>Quick charge mode distance</em></span> Requirement is automatically parsed to &quot;<span style="color: rgb(51,51,51);">distanceOnQuickCharge &gt;= 70</span>&quot; and solved as a constraint.</p><p><ac:image><ri:attachment ri:filename="extract_constraint_from_requirement_command.png" /></ac:image></p><p>After selecting the <strong>Extract Constraint From Requirement</strong> command, the constraint {distanceOnQuickCharge &gt;=70.0} is automatically created. It satisfies the requirement text &quot;at least 70&quot;.</p><p><ac:image><ri:attachment ri:filename="automatically_created_constraint.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:content-title="Importing requirements" /></ac:link></li><li><ac:link><ri:page ri:content-title="Exporting requirements" /></ac:link></li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720287 space=CRMP2024x version=1 -->
## PAGE 00045: Functional Requirement

- page_id: `136720287`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720287/Functional+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:42.919+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Functional Requirement is a requirement that specifies a behavior that a system or a part of a system must perform.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="24c0a823-706f-42a0-ada5-cbafe982b108"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Functional Requirement is a requirement that specifies a behavior that a system or a part of a system must perform.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720273 space=CRMP2024x version=1 -->
## PAGE 00046: Generating requirement reports

- page_id: `136720273`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720273/Generating+requirement+reports
- version_number: 1
- version_date: `2023-09-21T10:22:41.665+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Report customization

159793458

#### CONTENT-COLUMN: Report customization

159793460

#### CONTENT-BLOCK: Report customization

159793459

#### EXCERPT: Report customization

INLINE

You can generate Requirement reports in the .docx and .html/.htm formats directly from your model.

43

##### Generating the Word document report

You can generate the Requirement report in word document in the following ways:

44

#### INFO: Report customization

Report customization

If you want to customize the report or create your own template for a requirement report , you may use the **[Report Wizard](https://docs.nomagic.com/display/MD2024x/MagicDraw+Report+wizard+overview)**.

###### Generating requirement report by using the**Report Wizard**

****

To create a .docx format report by using the **Report Wizard**

1. In the Tools menu, click Report Wizard .
2. In the Select Template area, select **Requirements**, and choose one of the following report type: 
-**Requirement Dependencies Report**. This report contains tables of requirement dependencies, that is separate tables for Copy, Derive, Refine, Satisfy, Trace, and Verify relations.-**Requirement Diagram**. This report lists all requirement diagrams of a selected scope. Diagram elements and dependencies are described in tables under each diagram.-**Requirement Report**. This is a standard detailed requirement report, containing all requirements attributes. This template may be used as a requirement specification report.-**Requirements Table Diagram Report**. This report lists all requirement tables of a selected scope.
3. Click**Next**.
4. In the Select Report Data area, you can then select a predefined report data for the selected template (default = Built-in). Click Next .
5. In the Select Element Scope area use:
  - The Add button to add an element selected in the element tree to the Selected objects area.
  - The Add All button to add all elements directly owned by the element selected in the element tree to the Selected objects area.
  - The Add Recursively button in to add all elements listed under the element selected in the element tree to the Selected objects area.
  - The Remove button in to remove the selected element from the Selected objects area.
  - The Remove All button in to remove all selected elements from the Selected objects area.
6. Click Next .
7. In the Output Options area, define the appropriate options.
8. Click Generate . Your report is generated and automatically opens.

###### Generating requirement report from the Containment tree

To generate Requirement reports from the Containment tree

1. In the Containment tree, right-click the selected requirement specification (Package) or Requirement.
2. From the shortcut menu, click Generate Report > Requirements and select a desired requirement template.
3. In the Select Location dialog, specify a report location and specify a report file name.
4. Click Save . The report is generated.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="95911cf0-57c4-441c-ace3-e4f788a380f8"><ac:parameter ac:name="id">159793458</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="11a3f08a-a800-4380-87b2-79e03348685f"><ac:parameter ac:name="id">159793460</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a29ef01a-4eac-4567-8fd1-8970693a4961"><ac:parameter ac:name="id">159793459</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="d7bf210c-9021-43b0-b486-56a30822a43a"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>You can generate Requirement reports in the .docx and .html/.htm formats directly from your model.</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="7c57d64f-b037-49b0-b431-dbc38e340b0e"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><h3>Generating the Word document report</h3><p>You can generate the Requirement report in word document in the following ways:</p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="6fba890a-1608-4ea3-87ba-345029480370"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">4</ac:parameter></ac:structured-macro></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="91ef625e-776a-440b-91b3-83a82eaf0d29"><ac:parameter ac:name="title">Report customization</ac:parameter><ac:rich-text-body><p>If you want to customize the report or create your own template for a requirement report , you may use the <strong><a href="https://docs.nomagic.com/display/MD2024x/MagicDraw+Report+wizard+overview">Report Wizard</a></strong>.</p></ac:rich-text-body></ac:structured-macro><h4>Generating requirement report by using t<span>he </span><strong>Report Wizard</strong></h4><p><strong><br /></strong></p><p>To create a .docx format report by using the <strong>Report Wizard</strong></p><hr /><ol><li>In the <strong>Tools</strong> menu, click <strong>Report Wizard</strong>.</li><li><p class="auto-cursor-target">In the Select Template area, select <strong>Requirements</strong>, and choose one of the following report type:<br /><span>- </span><strong>Requirement Dependencies Report</strong><span>. This report contains tables of requirement dependencies, that is separate tables for Copy, Derive, Refine, Satisfy, Trace, and Verify relations.<br /></span><span>- </span><strong>Requirement Diagram</strong><span>. This report lists all requirement diagrams of a selected scope. Diagram elements and dependencies are described in tables under each diagram. <br /></span><span>- </span><strong>Requirement Report</strong><span>. This is a standard detailed requirement report, containing all requirements attributes. This template may be used as a requirement specification report.<br /></span><span>- </span><strong>Requirements Table Diagram Report</strong><span>. This report lists all requirement tables of a selected scope.</span></p></li><li><p class="auto-cursor-target"><span>Click </span><strong>Next</strong><span>.</span></p></li><li>In the <strong>Select Report Data</strong> area, you can then select a predefined report data for the selected template (default = Built-in). Click <strong>Next</strong>.</li><li>In the <strong>Select Element Scope</strong> area use:<br /><ul><li>The <strong>Add</strong> button to add an element selected in the element tree to the <strong>Selected objects</strong> area.</li><li>The <strong>Add All</strong> button to add all elements directly owned by the element selected in the element tree to the <strong>Selected objects</strong> area.</li><li>The <strong>Add Recursively</strong> button in to add all elements listed under the element selected in the element tree to the <strong>Selected objects</strong> area.</li><li>The <strong>Remove</strong> button in to remove the selected element from the <strong>Selected objects</strong> area.</li><li>The <strong>Remove All</strong> button in to remove all selected elements from the <strong>Selected objects</strong> area.</li></ul></li><li>Click <strong>Next</strong>.</li><li>In the <strong>Output Options</strong> area, define the appropriate options.</li><li>Click<strong> Generate</strong>.<br />Your report is generated and automatically opens.</li></ol><h4>Generating requirement report <span>from the Containment tree</span></h4><p><br /></p><p>To generate Requirement reports from the Containment tree</p><hr /><ol><li>In the Containment tree, right-click the selected requirement specification (Package) or Requirement.</li><li>From the shortcut menu, click <strong>Generate Report</strong> &gt; <strong>Requirements</strong> and select a desired requirement template.</li><li>In the <strong>Select Location</strong> dialog, specify a report location and specify a report file name.</li><li>Click <strong>Save</strong>.<br />The report is generated.</li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720073 space=CRMP2024x version=1 -->
## PAGE 00047: Getting started

- page_id: `136720073`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720073/Getting+started
- version_number: 1
- version_date: `2023-09-21T10:22:34.191+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

The Cameo Requirement Modeler Plugin implements the requirements’ part of the OMG SysML standard that is widely used in systems engineering. All concepts and modeling approaches that are used in requirements modeling with the plugin come from the requirements’ part of the SysML standard which can be found at [http://www.omgsysml.org](http://www.omgsysml.org/). The SysML requirements’ part provides clear essential means for the model-based requirements management independently from the system engineering domain, so it is easy to adopt in every other domain such as software, business, and enterprise.

The article [Requirements Writing in SysML Guide](https://blog.nomagic.com/requirements-writing-in-sysml-guide/) presents one of the possible requirements modeling processes which we adopt internally for the development of all our products.

To start working with the Cameo Requirement Modeler Plugin, [CONFLUENCE_PAGE title='Installing plugins' space='NMDOC'] in the MagicDraw tool.

If you use the [Cameo Systems Modeler](https://docs.nomagic.com/display/CSM185/Cameo+Systems+Modeler+Documentation) or [CONFLUENCE_PAGE title='Cameo Enterprise Architecture' space='NMDOC'] you can start using requirement features at once.

How to start:****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>The Cameo Requirement Modeler Plugin implements the requirements’ part of the OMG SysML standard that is widely used in systems engineering. All concepts and modeling approaches that are used in requirements modeling with the plugin come from the requirements’ part of the SysML standard which can be found at <a href="http://www.omgsysml.org/">http://www.omgsysml.org</a>. The SysML requirements’ part provides clear essential means for the model-based requirements management independently from the system engineering domain, so it is easy to adopt in every other domain such as software, business, and enterprise.</p><p>The article <a href="https://blog.nomagic.com/requirements-writing-in-sysml-guide/">Requirements Writing in SysML Guide</a> presents one of the possible requirements modeling processes which we adopt internally for the development of all our products.</p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="33948ef4-8db8-4f49-a0bf-828f27d34a17"><ac:rich-text-body><p>To start working with the Cameo Requirement Modeler Plugin, <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Installing plugins" /><ac:plain-text-link-body><![CDATA[install it]]></ac:plain-text-link-body></ac:link> in the MagicDraw tool.</p><p>If you use the <a href="https://docs.nomagic.com/display/CSM185/Cameo+Systems+Modeler+Documentation"><span class="confluence-link">Cameo Systems Modeler</span></a> or <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Cameo Enterprise Architecture" /></ac:link> you can start using requirement features at once.</p></ac:rich-text-body></ac:structured-macro><p>How to start:<strong><br /></strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="8c700262-d9f7-413c-b940-18bb719589fa" /></p>
````

<!--NOMAGIC_PAGE id=136720237 space=CRMP2024x version=1 -->
## PAGE 00048: Global validation rules

- page_id: `136720237`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720237/Global+validation+rules
- version_number: 1
- version_date: `2023-09-21T10:22:40.676+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation > Creating new validation rules
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Global validation rules' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="cf53e9e6-22e0-4c55-b880-d335827feb4e"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Global validation rules" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720094 space=CRMP2024x version=1 -->
## PAGE 00049: Image Library tab

- page_id: `136720094`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720094/Image+Library+tab
- version_number: 1
- version_date: `2023-09-21T10:22:34.865+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Image Library tab' space='MD2024x']true

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Main menu' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Toolbars' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Changing interface style' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="b024934d-924c-4a42-8ddd-d4ec8e5bb07a"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Image Library tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="7f8b169a-3bc8-4bc5-8721-f45adc6153dc"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Main menu" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Toolbars" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Changing interface style" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720135 space=CRMP2024x version=2 -->
## PAGE 00050: Importing ReqIF files

- page_id: `136720135`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720135/Importing+ReqIF+files
- version_number: 2
- version_date: `2024-01-29T15:00:08.145+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Importing requirements
- labels: []

### NORMALIZED CONTENT

818054109

818054112

818062608

**On this page**

43

818054111

##### Importing ReqIF files

You can import ReqIF files from:

- IBM DOORS 9.4, 9.5, and 9.6
- IBM DOORS Next Generation
- PTC Integrity
- Polarion REQUIREMENTS
- Siemens Teamcenter
- Dassault Systemes Reqtify

You can import any ReqIF file – with or without specifications.

To import a ReqIF requirement file

1. Open a project wherein you want to import requirements.
2. From the File menu, select Import From > Requirement Interchange Format (ReqIF) File .
3. In the opened **Load** dialog, browse for your ReqIF file and click **Open**.
4. The ReqIF file is imported.

If Requirements in the ReqIF file have ID prefixes, they are set automatically after import only for imported Requirements. Manage ID prefixes when [CONFLUENCE_PAGE title='Requirements numbering' space='CRMP2024x'].

800700

When the ReqIF file is imported, a notification message appears, stating the quantity of imported or updated elements. If you import a ReqIF file without specification, the message doesn't contain the line that indicates new or updated specifications. You also see no option **Show imported specification table(s)**. 
 
If you imported a ReqIF file with the specification, you can view the list of imported elements. To do that, click the **Show imported specification table(s)** link in the opened notification message. The list is displayed in a generic table format.

[IMAGE alt='' src='']

To change import options, click the **You can change import and mapping options here** link in the opened notification message.

The notification message is displayed for a fixed duration, but you can find all project notification messages in the Notification Window. To open the Notification Window, click **Window** > **Notification Window**, or press Ctrl + M.

Imported requirements are presented in the **Containment** tree. The requirement specification is represented as a model package and requirements are represented as model elements. 
[IMAGE alt='' src='']

If there are images or files attached to the ReqIF file, they are marked with the «AttachedFile» stereotype and placed in a separate package as model elements after the import.

All images in the *BMP* file format are automatically converted to the *PNG*format.

If there are any deleted elements in the source file, they are automatically marked with the «deprecated» stereotype once imported onto the modeling tool.

[IMAGE alt='' src='']

##### Changing requirements importing options

Changing requirements importing options is beneficial if you have a custom requirement type defined, or you are importing another type of data instead of requirements, for example, test cases.

A requirement type is limited to class and class extended types.

You can change the following import options:

- Specify an element type to create for the objects you are importing
- Specify a relationship type to create for the relationships you are importing
- Specify a path to the resource location
- Choose whether to import all properties into the model or not and form a list of ignored and not imported properties

To change ReqIF file importing options

We recommend changing importing options before requirements are imported and no changes are made in the project, because after you have changed importing options, you need to remove the requirements you have imported and re-import it.

1. Click Options > Project . The Project Options dialog opens.
2. In the options group list, select General , then scroll down to the ReqIF options group.
3. Click a desired option specification cell to change it's value.
4. Click OK after you are finished.

##### Updating requirements

It is common to modify requirements after importing them. Importing requirements in a ReqIF format allows updating the requirements present in the model without any data loss – all changes are identified. 
 
 To update ReqIF file by importing a new file

1. Open a project wherein you want to update requirements.
2. Import a ReqIF file with updated requirements.

To update requirements from the project

1. Open the project containing imported requirements.
2. In the Containment tree, select a requirement specification package and open it's shortcut menu.
3. Click Tools > ReqIF > Update From Requirements Interchange Format (ReqIF) File .
4. In the opened Load dialog, browse for your ReqIF file and click Open . The ReqIF file is updated.

After requirements have been updated, you get a notification message informing about an update status. If you update a ReqIF file without specification, the message doesn't contain the line that indicates new or updated specifications. You also see no option **Show imported specification table(s)**. 
[IMAGE alt='' src=''] 
 
 In the change log table, you can see the detailed list of updated elements. 
[IMAGE alt='' src=''] 
 
 During update, no elements are removed, only new elements are added and statuses of all elements are updated. Elements not present in an updated ReqIF file are marked as obsolete.

##### Managing obsolete requirement elements

In the model, obsolete elements are marked with an exclamation mark in a yellow triangle. A «deprecated» stereotype is applied to such requirement elements automatically. 
[IMAGE alt='' src=''] 
 
**Removing Obsolete Elements** 
 In the project, you can choose to remove only the selected obsolete element or all obsolete elements at a time. To remove one selected obsolete element, use the [CONFLUENCE_PAGE title='Importing ReqIF files' space='CRMP2024x'] that is described in the following section. 
 
 To remove all obsolete elements

1. In the Containment tree, right-click the requirements specification package.
2. From the shortcut menu, select Tools > ReqIF > Remove Obsolete Elements .

****

**Searching for obsolete elements**

#validationTo search for obsolete elements

1. In the Containment tree, right-click the requirements specification package.
2. From the shortcut menu, select Validation > Obsolete Elements and one of the following:

- 
  - Remove Obsolete Elements – removes the selected obsolete elements from a project
  - Ignore – ignores obsolescence from the element and leaves it in the model
  - Select in Validation Results – opens the Active Validation Results panel wherein you can perform appropriate validation actions.

818054108

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="0a350d2e-0616-4489-9e4f-2f25415a3a95"><ac:parameter ac:name="id">818054109</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="89694ec5-7615-45af-acff-504fc1fac54c"><ac:parameter ac:name="id">818054112</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="12de35f4-b3e0-4924-9111-7e0047a52ac2"><ac:parameter ac:name="id">818062608</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="43707498-0333-43e4-b126-7dbf4f138bbd"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4170df4f-86ae-4741-8800-76863bafd336"><ac:parameter ac:name="id">818054111</ac:parameter><ac:rich-text-body><h3>Importing ReqIF files</h3><p>You can import ReqIF files from:</p><ul><li><ac:inline-comment-marker ac:ref="df9cd3fc-66fd-495a-82c3-e313948825c4">IBM DOORS 9.4, 9.5, and 9.6</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="df9cd3fc-66fd-495a-82c3-e313948825c4">IBM DOORS Next Generation</ac:inline-comment-marker></li><li>PTC Integrity</li><li>Polarion REQUIREMENTS</li><li><ac:inline-comment-marker ac:ref="df9cd3fc-66fd-495a-82c3-e313948825c4">Siemens Teamcenter</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="df9cd3fc-66fd-495a-82c3-e313948825c4">Dassault Systemes Reqtify</ac:inline-comment-marker></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a6015838-4ae6-4eab-b2ba-e4e2736dbc4e"><ac:rich-text-body><p>You can import any ReqIF file – with or without specifications.</p></ac:rich-text-body></ac:structured-macro><p>To import a ReqIF requirement file</p><hr /><ol><li>Open a project wherein you want to import requirements.</li><li>From the <strong>File</strong> menu, select <strong>Import From</strong> &gt; <strong>Requirement Interchange Format (ReqIF) File</strong>.</li><li><p class="_mce_tagged_br">In the opened <strong>Load</strong> dialog, browse for your ReqIF file and click <strong>Open</strong>.</p></li><li><p class="_mce_tagged_br">The ReqIF file is imported.</p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2781102a-f912-4cce-b767-85b16dad75f3"><ac:rich-text-body><p>If Requirements in the ReqIF file have ID prefixes, they are set automatically after import only for imported Requirements. Manage ID prefixes when <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirements numbering" /><ac:plain-text-link-body><![CDATA[numbering Requirements]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="8edbcb55-2194-4655-9bff-39b4279198fb"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=w12dprJkT_0" /></ac:parameter><ac:parameter ac:name="height">700</ac:parameter></ac:structured-macro></p><p><br /></p><p><span style="color: rgb(51,51,51);">When the ReqIF file is imported, a notification message appears, stating the quantity of imported or updated elements. If you import a ReqIF file without specification, the message doesn't contain the line that indicates new or updated specifications. You also see no option <strong>Show imported specification table(s)</strong>.</span><br class="atl-forced-newline" /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color: rgb(51,51,51);"> </span><br class="atl-forced-newline" /><span style="color: rgb(51,51,51);"> If you imported a ReqIF file with the specification, you can view the list of imported elements. To do that, click the <strong>Show imported specification table(s)</strong> link in the opened notification message. The list is displayed in a generic table format.</span></p><p><ac:image ac:title="Notification message informing about imported requirements " ac:alt="Notification message informing about imported requirements " ac:height="150" ac:width="411"><ri:attachment ri:filename="worddav5c44ae713dfcb6f3bb017b0c84781d6d.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing requirements" /></ri:attachment></ac:image></p><p><br /></p><p>To change import options, click the <strong>You can change import and mapping options here</strong> link in the opened notification message.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="e2ec9ad7-3755-4eff-abf9-ebd02f8e370b"><ac:rich-text-body><p>The notification message is displayed for a fixed duration, but you can find all project notification messages in the Notification Window. To open the Notification Window, click <strong>Window</strong> &gt; <strong>Notification Window</strong>, or press Ctrl + M.</p></ac:rich-text-body></ac:structured-macro><p>Imported requirements are presented in the <strong>Containment</strong> tree. The requirement specification is represented as a model package and requirements are represented as model elements. <br class="atl-forced-newline" /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:border="true" ac:title="Representation of requirements in Containment tree" ac:alt="Representation of requirements in Containment tree" ac:height="318" ac:width="427"><ri:attachment ri:filename="worddav6a5cccd856023d2120dc99ff1ede7b87.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing requirements" /></ri:attachment></ac:image></span></p><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><br /></span></p><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><span>If there are <ac:inline-comment-marker ac:ref="e418f27d-0f0e-441b-a78c-67c9b7efe81d">images</ac:inline-comment-marker> or files attached to the ReqIF file, they are marked with the «AttachedFile» stereotype and placed in a separate <ac:inline-comment-marker ac:ref="26dc9f64-68cd-4073-973a-b4ba590ea44d">package</ac:inline-comment-marker> as model elements after the import. </span></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8b4c750d-22c1-4798-a463-3f8cfde63ef6"><ac:rich-text-body><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size">All images in the <em>BMP</em> file format are automatically converted to the <em><ac:inline-comment-marker ac:ref="f2940cf0-f4da-48f3-94e6-e1cdd35c1510">PNG </ac:inline-comment-marker></em><ac:inline-comment-marker ac:ref="f2940cf0-f4da-48f3-94e6-e1cdd35c1510">format</ac:inline-comment-marker>. </span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="16fd8e0d-621a-4983-98a9-d5619ebdf3c1"><ac:rich-text-body><p>If there are any deleted elements in the source file, they are automatically marked with the «deprecated» stereotype once imported onto the modeling tool.</p></ac:rich-text-body></ac:structured-macro><p><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><br /><ac:image><ri:attachment ri:filename="imported_images_reqif.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing ReqIF files" /></ri:attachment></ac:image></span></p><h3>Changing requirements importing options</h3><p>Changing requirements importing options is beneficial if you have a custom requirement type defined, or you are importing another type of data instead of requirements, for example, test cases.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="955bae83-0fd4-469c-873c-c59046348bf2"><ac:rich-text-body><p>A requirement type is limited to class and class extended types.</p></ac:rich-text-body></ac:structured-macro><p>You can change the following import options:</p><ul><li>Specify an element type to create for the objects you are importing</li><li>Specify a relationship type to create for the relationships you are importing</li><li>Specify a path to the resource location</li><li>Choose whether to import all properties into the model or not and form a list of ignored and not imported properties</li></ul><p><br class="atl-forced-newline" /> To change ReqIF file importing options</p><hr /><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="083995ad-0d2d-4366-af56-981ad15fb47c"><ac:rich-text-body><p>We recommend changing importing options before requirements are imported and no changes are made in the project, because after you have changed importing options, you need to remove the requirements you have imported and re-import it.</p></ac:rich-text-body></ac:structured-macro><ol><li>Click <strong>Options</strong> &gt; <strong>Project</strong>. The <strong>Project Options</strong> dialog opens.</li><li>In the options group list, select <strong>General</strong>, then scroll down to the <strong>ReqIF</strong> options group.</li><li>Click a desired option specification cell to change it's value.<span style="color: rgb(129,137,156);"> </span></li><li>Click <strong>OK</strong> after you are finished.</li></ol><h3>Updating requirements</h3><p><br class="atl-forced-newline" /> It is common to modify requirements after importing them. Importing requirements in a ReqIF format allows updating the requirements present in the model without any data loss – all changes are identified. <br class="atl-forced-newline" /><br class="atl-forced-newline" /> To update ReqIF file by importing a new file</p><hr /><ol><li>Open a project wherein you want to update requirements.</li><li>Import a ReqIF file with updated requirements.</li></ol><p><br class="atl-forced-newline" /> To update requirements from the project</p><hr /><ol><li>Open the project containing imported requirements.</li><li>In the <strong>Containment</strong> tree, select a requirement specification package and open it's shortcut menu.</li><li>Click <strong>Tools</strong> &gt; <strong>ReqIF</strong> &gt; <strong>Update From Requirements Interchange Format (ReqIF) File</strong>.</li><li>In the opened <strong>Load</strong> dialog, browse for your ReqIF file and click <strong>Open</strong>. The ReqIF file is updated.</li></ol><p>After requirements have been updated, you get a notification message informing about an update status. <span style="color: rgb(51,51,51);"> If you update a ReqIF file without specification, the message doesn't contain the line that indicates new or updated specifications. You also see no option <strong>Show imported specification table(s)</strong>.</span> <br class="atl-forced-newline" /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:title="Notification window about updated requirements" ac:alt="Notification window about updated requirements" ac:height="221" ac:width="398"><ri:attachment ri:filename="worddaveb8528a09ea20172fba7cd204846dbe6.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing requirements" /></ri:attachment></ac:image></span><br class="atl-forced-newline" /><br class="atl-forced-newline" /> In the change log table, you can see the detailed list of updated elements. <br class="atl-forced-newline" /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:title="Change log table" ac:alt="Change log table" ac:height="166" ac:width="443"><ri:attachment ri:filename="worddavc67674f1d31deffe5f80226c2f459353.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing requirements" /></ri:attachment></ac:image></span><br class="atl-forced-newline" /><br class="atl-forced-newline" /> During update, no elements are removed, only new elements are added and statuses of all elements are updated. Elements not present in an updated ReqIF file are marked as obsolete.</p><h3><span style="color: rgb(51,51,51);">Managing obsolete requirement elements</span></h3><p><br class="atl-forced-newline" /> In the model, obsolete elements are marked with an exclamation mark in a yellow triangle. A «deprecated» stereotype is applied to such requirement elements automatically.<br class="atl-forced-newline" /><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:title="Obsolete elements in Containment tree" ac:alt="Obsolete elements in Containment tree" ac:height="65" ac:width="393"><ri:attachment ri:filename="worddav0c7c2dd9585346d2c1f4826df65557fa.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing requirements" /></ri:attachment></ac:image></span><br class="atl-forced-newline" /><br class="atl-forced-newline" /><strong>Removing Obsolete Elements</strong><br class="atl-forced-newline" /> In the project, you can choose to remove only the selected obsolete element or all obsolete elements at a time. To remove one selected obsolete element, use the <ac:link ac:anchor="validation"><ac:plain-text-link-body><![CDATA[validating procedure]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing ReqIF files" /></ac:link> that is described in the following section. <br class="atl-forced-newline" /><br class="atl-forced-newline" /> To remove all obsolete elements</p><hr /><ol><li>In the <strong>Containment</strong> tree, right-click the requirements specification package.</li><li>From the shortcut menu, select <strong>Tools</strong> &gt; <strong>ReqIF</strong> &gt; <strong>Remove Obsolete Elements</strong>. </li></ol><p><strong><br /></strong></p><p><strong>Searching for obsolete elements</strong></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="54bb4677-4d0f-43f2-aab5-3db2a64661ca"><ac:parameter ac:name="">#validation</ac:parameter></ac:structured-macro>To search for obsolete elements</p><hr /><ol><li>In the <strong>Containment</strong> tree, right-click the requirements specification package.</li><li>From the shortcut menu, select <strong>Validation</strong> &gt; <strong>Obsolete Elements</strong> and one of the following:</li></ol><ul><li style="list-style-type: none;background-image: none;"><ul><li><strong>Remove Obsolete Elements</strong> – removes the selected obsolete elements from a project<span style="color: rgb(129,137,156);"> </span></li><li><strong>Ignore</strong> – ignores obsolescence from the element and leaves it in the model<span style="color: rgb(129,137,156);"> <br /></span></li><li><strong>Select </strong><strong>in</strong><strong> Validation </strong><strong>Results</strong> – opens the <strong>Active</strong><strong> Validation</strong><strong> Results</strong> panel wherein you can perform appropriate validation actions.</li></ul></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7236c132-0814-4fa8-a0b9-f4947fc155ba"><ac:parameter ac:name="id">818054108</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="2ee18d72-cc07-4e8e-9848-b8743cd545ac" /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720138 space=CRMP2024x version=1 -->
## PAGE 00051: Importing ReqIF files from the command-line interface

- page_id: `136720138`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720138/Importing+ReqIF+files+from+the+command-line+interface
- version_number: 1
- version_date: `2023-09-21T10:22:35.751+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Importing requirements > Importing ReqIF files
- labels: []

### NORMALIZED CONTENT

Importing from the command-line interface is useful when you want to import files automatically, e.g., once a day at midnight.

To import a ReqIF file from the command-line interface

1. Open the Command Prompt window
2. Go to the <model editor installationdirectory>/plugins/com.nomagic.requirements directory containing the *reqifimport.exe* file.
3. At the command prompt, type the following command and specify the values of the required arguments: reqifimport project_descriptor=<project URL> reqif_file=<path to ReqIF file> owner=<element hyperlink or qualified name> Where:
  - **project_descriptor** is the URL of a project. How to get a project descriptor?Start your modeling tool and open the required project.In the main menu, go to **File** > **Project Properties** and select the **General** tab.Find the project descriptor specified in the **Project Descriptor** box at the bottom of the **Project Properties** dialog and copy it to the clipboard.
  - **reqif_file** is the path to the ReqIF file you want to import. If there is a space in a path, surround the argument and its value with escaped quote(\").
  - **owner** is the hyperlink or qualified name of the owner element. If newly imported elements are not contained by the Specification element, they are placed under the specified owner. Note that the **owner** argument is optional. How to get the hyperlink of an element?Start your modeling tool and open the required project.In the Containment tree, right-click an element and select **Copy Element Hyperlink**.The hyperlink of the element is now copied to the clipboard.
4. Press **Enter**.

Now after opening the project you have imported the ReqIF file into, the imported data is already present in the Containment tree of the project.

##### Using a properties file

To make importing from the command-line interface quicker you can specify arguments in a properties file, which can be easily edited or reused.

To import a ReqIF file from the command-line interface using a properties file

1. Create a properties file and specify the values of the following arguments: See the example of a properties file below. text1trueProject Properties > General.
#
reqif_file=C:/Users/johnsmith/Documents/project_requirements.reqif
#
# Specify the path to the ReqIF file.
# NOTE: If there is a space in a path, surround the argument and its value with escaped quote (\").
#
owner=mdel://eee_1045467100313_135436_1
#
# Specify the hyperlink or qualified name of the owner element. 
# To get the hyperlink of an element, open a project, right-click the element in the Containment tree and select "Copy Element Hyperlink".
# NOTE: This argument is optional.
#]]> When creating a properties file on Windows OS, use only / or \\ as a path separator, otherwise the command will fail.
  - project_descriptor
  - reqif_file
  - owner
2. Open the Command Prompt window.
3. Go to the <model editor installationdirectory>/plugins/com.nomagic.requirements directory containing the *reqifimport.exe* file.
4. At the command prompt, type the following command and specify the value of the **properties_file** argument. reqifimport properties_file=<path to properties file> Where **properties_file** is the path to the properties file to be used.
5. Press **Enter**.

Now after opening the project you have imported the ReqIF file into, the imported data is already present in the Containment tree of the project.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>Importing from the command-line interface is useful when you want to import files automatically, e.g., once a day at midnight.</p><p> </p><p>To import a ReqIF file from the command-line interface</p><hr /><ol><li>Open the Command Prompt window</li><li>Go to the <em><span style="color: rgb(0,0,0);">&lt;model editor installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.requirements</span></em><span style="color: rgb(0,0,0);"> directory containing the <em>reqifimport.exe</em> file.</span></li><li><span style="color: rgb(0,0,0);">At the command prompt, type the following command and specify the values of the required arguments:</span><span style="color: rgb(0,0,0);"><br /></span><pre>reqifimport project_descriptor=&lt;project URL&gt; reqif_file=&lt;path to ReqIF file&gt; owner=&lt;element hyperlink or qualified name&gt;</pre><p>Where:</p><ul><li><p><strong>project_descriptor</strong> is the URL of a project.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="bc06a5ad-5a37-4ffe-bbdf-b3d946ace80e"><ac:parameter ac:name="title">How to get a project descriptor?</ac:parameter><ac:rich-text-body><ol><li>Start your modeling tool and open the required project.</li><li>In the main menu, go to <strong>File</strong> &gt; <strong>Project Properties</strong> and select the <strong>General</strong> tab.</li><li>Find the project descriptor specified in the <strong>Project Descriptor</strong> box at the bottom of the <strong>Project Properties</strong> dialog and copy it to the clipboard.</li></ol></ac:rich-text-body></ac:structured-macro></li><li><p><strong>reqif_file</strong> is the path to the ReqIF file you want to import.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="00b1ee10-546f-4653-8d08-5ad3b977342b"><ac:rich-text-body><p><span>If there is a space in a path, surround the argument and its value with escaped quote </span><span>(\&quot;).</span></p></ac:rich-text-body></ac:structured-macro></li><li><p><strong>owner</strong> is the hyperlink or qualified name of the owner element. If newly imported elements are not contained by the Specification element, they are placed under the specified owner. Note that the <strong>owner</strong> argument is optional.</p><ac:structured-macro ac:name="expand" ac:schema-version="1" ac:macro-id="fcbe8166-4962-4789-b836-dbbd969ec63d"><ac:parameter ac:name="title">How to get the hyperlink of an element?</ac:parameter><ac:rich-text-body><ol><li>Start your modeling tool and open the required project.</li><li>In the Containment tree, right-click an element and select <strong>Copy Element Hyperlink</strong>.</li></ol><p>The hyperlink of the element is now copied to the clipboard.</p></ac:rich-text-body></ac:structured-macro></li></ul></li><li><p>Press <strong>Enter</strong>.</p></li></ol><p>Now after opening the project you have imported the ReqIF file into, the imported data is already present in the Containment tree of the project.<br /> </p><h3><span style="color: rgb(0,0,0);">Using a properties file</span></h3><p>To make importing from the command-line interface quicker you can specify arguments in a properties file, which can be easily edited or reused.</p><p> </p><p>To import a ReqIF file from the command-line interface using a properties file</p><hr /><ol><li>Create a properties file and specify the values of the following arguments:<br /><ul><li><strong>project_descriptor</strong></li><li><strong>reqif_file</strong></li><li><strong>owner<br /> </strong></li></ul><p>See the example of a properties file below.</p><ac:structured-macro ac:name="code" ac:schema-version="1" ac:macro-id="e9b0a07d-28d7-4388-94f1-32faec5da20c"><ac:parameter ac:name="language">text</ac:parameter><ac:parameter ac:name="firstline">1</ac:parameter><ac:parameter ac:name="linenumbers">true</ac:parameter><ac:plain-text-body><![CDATA[project_descriptor=file:/C:/Users/johnsmith/Downloads/MagicDraw_185/samples/requirements/MagicLibrary%20requirements.mdzip
#
# Specify the project URL.
# To get a project descriptor, open a project and in the main menu go to File > Project Properties > General.
#
reqif_file=C:/Users/johnsmith/Documents/project_requirements.reqif
#
# Specify the path to the ReqIF file.
# NOTE: If there is a space in a path, surround the argument and its value with escaped quote (\").
#
owner=mdel://eee_1045467100313_135436_1
#
# Specify the hyperlink or qualified name of the owner element. 
# To get the hyperlink of an element, open a project, right-click the element in the Containment tree and select "Copy Element Hyperlink".
# NOTE: This argument is optional.
#]]></ac:plain-text-body></ac:structured-macro><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="a747b836-052e-4bff-a358-e5edaed77878"><ac:rich-text-body><p><span>When creating a properties file on Windows OS, use only / or \\ as a path separator, otherwise the command will fail.</span></p></ac:rich-text-body></ac:structured-macro></li><li>Open the Command Prompt window.</li><li>Go to the <em><span style="color: rgb(0,0,0);">&lt;model editor installa</span><span style="color: rgb(0,0,0);">tion </span><span style="color: rgb(0,0,0);">directory&gt;/plugins/com.nomagic.requirements</span></em><span style="color: rgb(0,0,0);"> directory containing the <em>reqifimport.exe</em> file.</span></li><li><p>At the command prompt, type the following command and specify the value of the <strong>properties_file</strong> argument.</p><pre>reqifimport properties_file=&lt;path to properties file&gt;</pre><p>Where <strong>properties_file</strong> is the path to the properties file to be used.<br /><br /></p></li><li><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);line-height: 1.42857;">Press <strong>Enter</strong>.</span></span></span></li></ol><p><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);"><span style="color: rgb(51,51,51);line-height: 1.42857;">Now after opening the project you have imported the ReqIF file into, the imported data is already present in the Containment tree of the project.<br /></span></span></span></p></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720127 space=CRMP2024x version=1 -->
## PAGE 00052: Importing requirements

- page_id: `136720127`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720127/Importing+requirements
- version_number: 1
- version_date: `2023-09-21T10:22:35.482+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

577280013

577280015

577280014

INLINE

It is recommended that you import requirements into a separate project which can be used in other models as a used project. [CONFLUENCE_PAGE title='Managing used projects' space='MD2024x']>]]>

You can import requirements in one of the following ways:

- [CONFLUENCE_PAGE title='Importing ReqIF files' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Sync with Excel or CSV files' space='MD2024x']
- [CONFLUENCE_PAGE title='Importing data from Excel or CSV files' space='MD2024x']
- By pasting into Requirement table.
- [CONFLUENCE_PAGE title='Creating elements from other resources' space='MD2024x']
- [CONFLUENCE_PAGE title='Interchanging of requirements using Cameo DataHub' space='CRMP2024x']

577280012

**Related pages**

2

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="47685fc7-411e-4c2e-bbfa-3e6c1d527241"><ac:parameter ac:name="id">577280013</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="a8591a1b-7610-495c-aabf-9d53e2ef5e64"><ac:parameter ac:name="id">577280015</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1774e1f3-5cbe-4a46-ad38-a6a427c3c9bb"><ac:parameter ac:name="id">577280014</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="9b33b353-b548-422c-b1e3-986d2ee597f9"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="10f724db-e174-4e5f-9954-64ed3e6e9115"><ac:rich-text-body><p>It is recommended that you import requirements into a separate project which can be used in other models as a used project. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Managing used projects" /><ac:plain-text-link-body><![CDATA[How to manage used projects >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p><br class="atl-forced-newline" /> You can import requirements in one of the following ways:</p><ul><li class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Importing ReqIF files" /><ac:plain-text-link-body><![CDATA[By importing ReqIF files.]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Sync with Excel or CSV files" /><ac:plain-text-link-body><![CDATA[By syncing Excel or CSV files with Requirement table.]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Importing data from Excel or CSV files" /><ac:plain-text-link-body><![CDATA[By importing data from Excel or CSV file.]]></ac:plain-text-link-body></ac:link></li><li><a style="letter-spacing: 0.0px;" href="https://docs.nomagic.com/display/MD2024x/Basic+tasks+in+tables#Basictasksintables-Copyingandpastingdata">By pasting into Requirement table.</a></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Creating elements from other resources" /><ac:plain-text-link-body><![CDATA[By pasting into Requirements diagram, or Containment tree.]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Interchanging of requirements using Cameo DataHub" /><ac:plain-text-link-body><![CDATA[Using Cameo DataHub.]]></ac:plain-text-link-body></ac:link></li></ul><p><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f4c71f59-88f7-44a7-a9ad-74bd436b1890"><ac:parameter ac:name="id">577280012</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="249a5500-bd71-4490-94d2-854b8c0aa189"><ac:parameter ac:name="depth">2</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720085 space=CRMP2024x version=2 -->
## PAGE 00053: Inheritance tab

- page_id: `136720085`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720085/Inheritance+tab
- version_number: 2
- version_date: `2024-01-29T14:52:21.414+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

136169830

136169851

136169840

true[CONFLUENCE_PAGE title='Inheritance tab' space='MD2024x']

136169829

**On this page**

****

136178503

**Related pages**

****

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="a9dcf143-7abb-42b0-b838-920d7d4f0e43"><ac:parameter ac:name="id">136169830</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="df1a4f8b-3856-4a5d-841e-6b2375a5d221"><ac:parameter ac:name="id">136169851</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0e3a94c7-9ee2-4b48-9a9d-5f8cb64869b5"><ac:parameter ac:name="id">136169840</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="074b0a5c-00ca-4e05-a1ae-3ed5e0b9b982"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Inheritance tab" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a8d61783-8dcb-40c0-bb3d-addc02901199"><ac:parameter ac:name="id">136169829</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="adb57e4b-4c23-4c45-bbf9-13f3409457bc" /><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5d8c73f4-82cb-4ab4-9ed0-926cb43bd17b"><ac:parameter ac:name="id">136178503</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><strong><br /></strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720071 space=CRMP2024x version=1 -->
## PAGE 00054: Installation, licensing, and system requirements

- page_id: `136720071`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720071/Installation+licensing+and+system+requirements
- version_number: 1
- version_date: `2023-09-21T10:22:34.135+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation
- labels: []

### NORMALIZED CONTENT

507519710

507519712

507519711

For information regarding installation, licensing, and system requirements, visit the [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024x'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bbda9ad5-59ee-42bf-96b3-7e8346535e6b"><ac:parameter ac:name="id">507519710</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="9332a4ca-4aea-4809-bb8e-5a9e1966fc4b"><ac:parameter ac:name="id">507519712</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="411dfd87-9733-4270-bbca-1c8aefcd0718"><ac:parameter ac:name="id">507519711</ac:parameter><ac:rich-text-body><p class="with-breadcrumbs">For information regarding installation, licensing, and system requirements, visit the <ac:link><ri:page ri:space-key="IL2024x" ri:content-title="Installation, licensing, and system requirements" /></ac:link> page.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720139 space=CRMP2024x version=3 -->
## PAGE 00055: Interchanging of requirements using Cameo DataHub

- page_id: `136720139`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720139/Interchanging+of+requirements+using+Cameo+DataHub
- version_number: 3
- version_date: `2024-07-30T08:46:31.419+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Importing requirements
- labels: []

### NORMALIZED CONTENT

The Cameo DataHub is a dedicated solution for the requirements synchronization between different sources, such as MagicDraw, Rational DOORS®, CSV files, and other. Cameo DataHub is a data bridge that allows for data importing and exporting, automatic synchronization and creation of references between requirements and other artifacts. It allows to use different import and synchronization methods while importing or exporting requirements.

Came DataHub allows to:

- Associate and synchronize data.
- Change the monitoring statuses such as active, pending update, and pending delete whenever associated data items are modified or deleted.
- Impact monitoring. Whenever the referenced data item changes, Cameo DataHub reports the suspect status to direct traceability from each requirement to the respective design artifact.
- Define mappings between data and its’ properties.

The Cameo DataHub must be installed before taking the following actions. For more information refer to,[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='CDH2024x'].

To interchange of requirements using Cameo DataHub

1. Open an existing project or create a new one.
2. On the main menu, click Tools > Requirements > DataHub and select a desired action.

For more information about working with Cameo DataHub, see [CONFLUENCE_PAGE title='User Guide' space='CDH2024x'].

800700

**Related pages**

- [CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='CDH2024x']
- [CONFLUENCE_PAGE title='User Guide' space='CDH2024x']
- Importing requirements

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The Cameo DataHub is a dedicated solution for the requirements synchronization between different sources, such as MagicDraw, Rational DOORS®, CSV files, and other. Cameo DataHub is a data bridge that allows for data importing and exporting, automatic synchronization and creation of references between requirements and other artifacts. It allows to use different import and synchronization methods while importing or exporting requirements.</p><p>Came DataHub allows to:</p><ul><li>Associate and synchronize data.</li><li>Change the monitoring statuses such as active, pending update, and pending delete whenever associated data items are modified or deleted.</li><li>Impact monitoring. Whenever the referenced data item changes, Cameo DataHub reports the suspect status to direct traceability from each requirement to the respective design artifact.</li><li>Define mappings between data and its’ properties.<br /><br /></li></ul><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="032c5bb3-f0a2-4ffd-b155-7e6e92f7f095"><ac:rich-text-body><p>The Cameo DataHub must be installed before taking the following actions. For more information refer to,<span> </span><ac:link><ri:page ri:space-key="CDH2024x" ri:content-title="Installation, licensing, and system requirements" /></ac:link><span>.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p>To interchange of requirements using Cameo DataHub</p><hr /><ol><li>Open an existing project or create a new one.</li><li>On the main menu, click <strong>Tools</strong> &gt; <strong>Requirements</strong> &gt; <strong>DataHub</strong> and select a desired action.<br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="28a8a749-ad13-40eb-9a49-b30d3085cc71"><ac:rich-text-body><p>For more information about working with Cameo DataHub, see <ac:link><ri:page ri:space-key="CDH2024x" ri:content-title="User Guide" /><ac:plain-text-link-body><![CDATA[Cameo DataHub documentation]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="d1859acf-3ac8-4578-bfd6-4a4e6d8e3e01"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=w12dprJkT_0&amp;t=1s" /></ac:parameter><ac:parameter ac:name="height">700</ac:parameter></ac:structured-macro> </p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CDH2024x" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installing Cameo DataHub]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CDH2024x" ri:content-title="User Guide" /><ac:plain-text-link-body><![CDATA[Cameo DataHub documentation]]></ac:plain-text-link-body></ac:link></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Importing+requirements">Importing requirements</a></li></ul><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720288 space=CRMP2024x version=1 -->
## PAGE 00056: Interface Requirement

- page_id: `136720288`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720288/Interface+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:43.029+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

An Interface Requirement is a requirement that specifies the ports for connecting systems and parts of a system. Optionally, it may include the items that flow across the connector and/or the Interface constraints.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="f788e870-e9d7-4e71-bb6c-8a657c8c0d9f"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>An Interface Requirement is a requirement that specifies the ports for connecting systems and parts of a system. Optionally, it may include the items that flow across the connector and/or the Interface constraints.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720070 space=CRMP2024x version=1 -->
## PAGE 00057: Introduction

- page_id: `136720070`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720070/Introduction
- version_number: 1
- version_date: `2023-09-21T10:22:34.112+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='']true

800700

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="c2934982-bee7-4645-b0d2-1e97cf80689e"><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Cameo Requirements Modeler Plugin Documentation" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="4016dd6c-12d6-41c0-ae51-87f4f347fec6"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=OK_Z7zjJKeg" /></ac:parameter><ac:parameter ac:name="height">700</ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720200 space=CRMP2024x version=1 -->
## PAGE 00058: Invalid Copy of requirement

- page_id: `136720200`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720200/Invalid+Copy+of+requirement
- version_number: 1
- version_date: `2023-09-21T10:22:37.851+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720207 space=CRMP2024x version=1 -->
## PAGE 00059: Invalid generalization of Requirement

- page_id: `136720207`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720207/Invalid+generalization+of+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:38.420+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720208 space=CRMP2024x version=1 -->
## PAGE 00060: Invalid owned attribute of Requirement

- page_id: `136720208`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720208/Invalid+owned+attribute+of+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:38.495+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720209 space=CRMP2024x version=1 -->
## PAGE 00061: Invalid owned operation of Requirement

- page_id: `136720209`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720209/Invalid+owned+operation+of+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:38.599+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720201 space=CRMP2024x version=1 -->
## PAGE 00062: Invalid return parameter type

- page_id: `136720201`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720201/Invalid+return+parameter+type
- version_number: 1
- version_date: `2023-09-21T10:22:37.937+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720202 space=CRMP2024x version=1 -->
## PAGE 00063: Invalid Slave Requirement text

- page_id: `136720202`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720202/Invalid+Slave+Requirement+text
- version_number: 1
- version_date: `2023-09-21T10:22:38.014+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720206 space=CRMP2024x version=1 -->
## PAGE 00064: Invalid source or target of DeriveReqt

- page_id: `136720206`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720206/Invalid+source+or+target+of+DeriveReqt
- version_number: 1
- version_date: `2023-09-21T10:22:38.342+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720203 space=CRMP2024x version=1 -->
## PAGE 00065: Invalid stereotype(s) of client/supplier of Copy

- page_id: `136720203`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720203/Invalid+stereotype+s+of+client+supplier+of+Copy
- version_number: 1
- version_date: `2023-09-21T10:22:38.095+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720089 space=CRMP2024x version=1 -->
## PAGE 00066: Lock View tab

- page_id: `136720089`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720089/Lock+View+tab
- version_number: 1
- version_date: `2023-09-21T10:22:34.665+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Lock View tab' space='MD2024x']true

#### PANEL: On this page

On this page

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="078f2ecd-e45a-40cc-b3fc-8282ba145879"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Lock View tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p><p><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="0c6b482e-b875-46d5-96ea-36daba589129"><ac:parameter ac:name="title">
       On this page
      </ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="2e74da9b-5554-413c-8fb8-5aa956f934f5" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f66a763c-1625-4208-9fa1-67e984e84365"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720075 space=CRMP2024x version=2 -->
## PAGE 00067: Main menu

- page_id: `136720075`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720075/Main+menu
- version_number: 2
- version_date: `2024-01-29T14:52:45.131+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Main menu' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="c53a3a03-529c-4985-8d89-4ff3d945fba2"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Main menu" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=136720243 space=CRMP2024x version=1 -->
## PAGE 00068: Metrics

- page_id: `136720243`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720243/Metrics
- version_number: 1
- version_date: `2023-09-21T10:22:40.861+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements
- labels: []

### NORMALIZED CONTENT

831322168

831322171

831322170

A metric is information about a specific aspect of the model. A collection of various metrics can be used to evaluate the current state of your model. When calculated at regular intervals, they can help track the evolution of the model's development.

There are two metric suites dedicated to coverage analysis:

- The Design metric suite checks incoming satisfy relations.
- The Test cases metric suite checks incoming verify relations.

###### [IMAGE alt='' src='']Example of metrics table.

When working with requirements, it is useful to know what and how many requirements are covered by design elements (satisfy relations), by test cases (verify relations), are user requirements covered with system requirements, and how many requirements are already implemented or tested. In these situations metrics help you evaluate the current state of requirements in your model and track the progress of their coverage.

The metric suite Requirement Coverage (Treat Owner as Grouping Element) is considered as covered if it satisfies one of the following conditions:

- A requirement has a satisfy relation with a design element.
- The owning requirement is covered.
- All owned requirements are covered.

The metric suite Requirement Coverage (Treat Owner as Regular Requirement) is considered as covered if the requirement has a satisfy relation with a design element:

- If all child requirements have incoming satisfy relations, grouping requirements are not considered as satisfied unless they also have incoming satisfy relations.
- If the grouping requirement has incoming satisfy relation, its child requirements are not considered as covered unless they have incoming satisfy relations.

###### [IMAGE alt='' src='']Examples of covered requirements.

To use coverage analysis metrics

1. Select the package that includes the requirements.
2. From the shortcut menu, select Tools > Metrics > New Metric Table .
3. In the Create Metric Table dialog, set to true one of the metric suite:
  - Requirement Coverage (Treat Owner as Grouping Element).
  - Requirement Coverage (Treat Owner as Regular Requirement).
4. Click OK . The new metric table with calculated results is created.

You can create custom metric suites using structured expressions or scripts. For detailed procedures on creating metric suites, calculating metrics, and managing metric results, please see [CONFLUENCE_PAGE title='Metric Suites' space='MD2024x']Creating Metric Suites and [CONFLUENCE_PAGE title='Metric table' space='MD2024x'].

800700

831322167

**Related pages**

- Creating Metric Suites
- Metric table

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="53f83ebd-cf04-4391-8059-f4038c69a7b8"><ac:parameter ac:name="id">831322168</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="87a2fce3-3456-4050-aa09-c7ca158d354a"><ac:parameter ac:name="id">831322171</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="44294e44-b40d-42b6-b8aa-6422d9182901"><ac:parameter ac:name="id">831322170</ac:parameter><ac:rich-text-body><p>A metric is information about a specific aspect of the model. A collection of various metrics can be used to evaluate the current state of your model. When calculated at regular intervals, they can help track the evolution of the model's development.</p><p>There are two metric suites dedicated to coverage analysis:</p><ul><li>The Design metric suite checks incoming satisfy relations.</li><li>The Test cases metric suite checks incoming verify relations.</li></ul><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="metrics_table_example.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Metrics" /></ri:attachment></ac:image>Example of metrics table.</h6><p>When working with requirements, it is useful to know what and how many requirements are covered by design elements (satisfy relations), by test cases (verify relations), are user requirements covered with system requirements, and how many requirements are already implemented or tested. In these situations metrics help you evaluate the current state of requirements in your model and track the progress of their coverage.</p><p>The metric suite Requirement Coverage (Treat Owner as Grouping Element) is considered as covered if it satisfies one of the following conditions:</p><ul><li>A requirement has a satisfy relation with a design element.</li><li>The owning requirement is covered.</li><li>All owned requirements are covered.</li></ul><p><br class="atl-forced-newline" />The metric suite Requirement Coverage (Treat Owner as Regular Requirement) is considered as covered if the requirement has a satisfy relation with a design element:</p><ul><li>If all child requirements have incoming satisfy relations, grouping requirements are not considered as satisfied unless they also have incoming satisfy relations.</li><li>If the grouping requirement has incoming satisfy relation, its child requirements are not considered as covered unless they have incoming satisfy relations.</li></ul><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="examples_of_covered_requirements.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Metrics" /></ri:attachment></ac:image>Examples of covered requirements.</h6><p><br class="atl-forced-newline" />To use coverage analysis metrics</p><hr /><ol><li>Select the package that includes the requirements.</li><li>From the shortcut menu, select <strong>Tools</strong> &gt; <strong>Metrics</strong> &gt; <strong>New </strong><strong>Metric</strong><strong> Table</strong>.</li><li>In the <strong>Create</strong><strong> Metric</strong><strong> Table </strong>dialog, set to <em>true</em> one of the metric suite:<br /><ul><li>Requirement Coverage (Treat Owner as Grouping Element).</li><li>Requirement Coverage (Treat Owner as Regular Requirement).</li></ul></li><li>Click <strong>OK</strong>.<br />The new metric table with calculated results is created.</li></ol><p>You can create custom metric suites using structured expressions or scripts. For detailed procedures on creating metric suites, calculating metrics, and managing metric results, please see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Metric Suites" /><ac:link-body><span class="confluence-link">Creating Metric</span> Suites</ac:link-body></ac:link> and <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Metric table" /></ac:link><span style="color: rgb(129,137,156);"><span>.</span></span></p><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="23f2b5b2-71c9-4979-8739-bf0409535ae6"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=YgyeNgpR7TA" /></ac:parameter><ac:parameter ac:name="height">700</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="60a274f2-d5f1-4c52-a8b5-b35bdfd6c997"><ac:parameter ac:name="id">831322167</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><a href="https://docs.nomagic.com/display/MD2024x/Creating+Metric+Suites" class="current">Creating Metric Suites</a></li><li><a href="https://docs.nomagic.com/display/MD2024x/Metric+table" class="current">Metric table</a></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720204 space=CRMP2024x version=1 -->
## PAGE 00069: Missing Recursive copy of sub-requirement

- page_id: `136720204`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720204/Missing+Recursive+copy+of+sub-requirement
- version_number: 1
- version_date: `2023-09-21T10:22:38.175+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720210 space=CRMP2024x version=1 -->
## PAGE 00070: Missing requirement stereotype

- page_id: `136720210`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720210/Missing+requirement+stereotype
- version_number: 1
- version_date: `2023-09-21T10:22:38.727+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720077 space=CRMP2024x version=2 -->
## PAGE 00071: Model Browser

- page_id: `136720077`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720077/Model+Browser
- version_number: 2
- version_date: `2024-01-29T14:33:20.414+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Model Browser' space='MD2024x']

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Understanding the user interface' space='']
  - [CONFLUENCE_PAGE title='Main menu' space='']
  - [CONFLUENCE_PAGE title='Toolbars' space='']
  - [CONFLUENCE_PAGE title='Image Library tab' space='']
  - [CONFLUENCE_PAGE title='Changing interface style' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="afc760cf-73e7-46e1-838f-4eb723e4091e"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Browser" /></ac:link></ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="63349bd7-e910-4a5b-b125-96c1f3862f0c"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul><li><ac:link><ri:page ri:content-title="Understanding the user interface" /></ac:link><ul><li><ac:link><ri:page ri:content-title="Main menu" /></ac:link></li><li><ac:link><ri:page ri:content-title="Toolbars" /></ac:link></li><li><ac:link><ri:page ri:content-title="Image Library tab" /></ac:link></li><li><ac:link><ri:page ri:content-title="Changing interface style" /></ac:link></li></ul></li></ul><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="46817e87-c665-4b12-b32e-09e9e13ed86d" /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720087 space=CRMP2024x version=2 -->
## PAGE 00072: Model Extensions tab

- page_id: `136720087`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720087/Model+Extensions+tab
- version_number: 2
- version_date: `2024-01-29T14:30:58.420+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

1361354348

1361354369

1361354359

true[CONFLUENCE_PAGE title='Model Extensions tab' space='MD2024x']

1361414267

**On this page**

****

1361354347

**Related pages**

****

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5484e1d7-fd99-4ff2-bc24-dd6cd0b960bf"><ac:parameter ac:name="id">1361354348</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="0c4b8afe-6d7a-4ee2-8c44-33cee5b09e81"><ac:parameter ac:name="id">1361354369</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3153143b-c764-434b-b551-1ae8c7c2e978"><ac:parameter ac:name="id">1361354359</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="061ee20c-c215-40a1-9413-f863c264443c"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Extensions tab" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="27a34e6e-5886-492f-b47c-b9911b7336b8"><ac:parameter ac:name="id">1361414267</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="d81836fd-6a2b-4535-823f-181fb1ffa485" /><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e78633ae-42cb-4e33-8470-ce44f4abd72b"><ac:parameter ac:name="id">1361354347</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><strong><br /></strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720151 space=CRMP2024x version=1 -->
## PAGE 00073: Modifying requirement text

- page_id: `136720151`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720151/Modifying+requirement+text
- version_number: 1
- version_date: `2023-09-21T10:22:36.288+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: HTML text editors

823840096

#### CONTENT-COLUMN: HTML text editors

823840099

823840095

**On this page**

43

#### CONTENT-BLOCK: HTML text editors

823840098

The requirement always contains two properties: id and text. This section describes how to modify the text property of the requirement.

[IMAGE alt='' src='']

###### The*Stopping Distance* Requirement shape with filled Text property.

##### Editing the requirement text

You can edit the requirement text directly on shapes and in cells, or use the **Text** dialog.

To open the edit mode of the requirement text, do one of the following

- On the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'] , select the Text box on the Requirement shape. Click the text box again. The edit mode opens on the shape.
- In the Requirements table, double-click the Text cell. The edit mode opens on the cell.
- In the Requirements table, double-click the Text cell, and select [ATTACHMENT filename='edit_button_in_specification_window.png'] . The Text dialog opens.
- [CONFLUENCE_PAGE title='Specification window' space='MD2024x'] of the Requirement, select the Text property, and click [ATTACHMENT filename='edit_button_in_specification_window.png'] . The Text dialog opens.

##### switchSwitching the requirement text to HTML or Plain text

You can change the requirement text to HTML or Plain text directly on the Requirement shape or in the **Text** dialog.

To switch the requirement text to HTML or Plain text directly on the Requirement shape

1. On the diagram pane, select the text box on the Requirement shape.
2. Click one of the following buttons appearing on the lower left corner of the shape:
  - HTML - converts the text to HTML text. [ATTACHMENT filename='switch_to_html_text.png']
  - Plain - converts the text to plain text. [ATTACHMENT filename='switch_to_plain_text.png']

To switch the requirement text to HTML or Plain text in the **Text** dialog

1. Open the Text dialog:
  - In the Requirements table, double-click the Text cell, and select [ATTACHMENT filename='edit_button_in_specification_window.png'] .
  - [CONFLUENCE_PAGE title='Specification window' space='MD2024x'] of the Requirement, select the Text property, and click [ATTACHMENT filename='edit_button_in_specification_window.png'] .
2. In the Text dialog tootbar, do one of the following:
  - Select the HTML check box to convert the text to HTML text. [ATTACHMENT filename='html_text_in_text_dialog.png']
  - Clear the HTML check box to convert the text to plain text. [ATTACHMENT filename='plain_text_in_text_dialog.png']
3. Click OK .

##### Modifying the requirement text

You can modify the Requirement text in the following ways:

- [CONFLUENCE_PAGE title='Modifying requirement text' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Modifying requirement text' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Modifying requirement text' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Modifying requirement text' space='CRMP2024x']

###### richRich text formatting

If you [CONFLUENCE_PAGE title='Modifying requirement text' space='CRMP2024x'], you can use the toolbar in the **Text** dialog to format it as rich text.

To open the rich text formatting toolbar

- On the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'] , select the Text box on the Requirement shape. Click the text box again.
- In the Requirements table, double-click the Requirement Text cell, and select [ATTACHMENT filename='edit_button_in_specification_window.png'] .
- [CONFLUENCE_PAGE title='Specification window' space='MD2024x'] of the Requirement, select the Text property, and click [ATTACHMENT filename='edit_button_in_specification_window.png'] . If the Requirement text is in HTML format, the rich text formatting toolbar appears as shown in the following image. [ATTACHMENT filename='rich_text_formatting_toolbar.png']

#### INFO: HTML text editors

HTML text editors

Learn more about how to work with HTML texts:

- [CONFLUENCE_PAGE title='Advanced HTML Editor dialog' space='MD2024x']
- HTML editor

###### glossaryUsing Glossary terms

You can use the terms from the Glossary Table to ensure the same definitions of the concepts. [CONFLUENCE_PAGE title='Glossary table' space='MD2024x']>]]>

If you want to extract a Constraint from a Requirement, you must use the special condition terms when defining the Requirement text.

The full procedure for extracting a Constraint from a Requirement is provided in the section [CONFLUENCE_PAGE title='Extracting Constraint from Requirement' space='CRMP2024x'].

[CONFLUENCE_PAGE title='Extracting Constraint from Requirement' space='CRMP2024x']true

###### hyperlinkDefining hyperlinks

You can add a hyperlink on the requirement text. How to add hyperlinks in text read in the [CONFLUENCE_PAGE title='Hyperlinks in texts' space='MD2024x'] page.

###### imageInserting images into HTML text

[CONFLUENCE_PAGE title='Inserting images into HTML text' space='MD2024x']true

824150503

**Related pages**

- [CONFLUENCE_PAGE title='Extracting Constraint from Requirement' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Advanced HTML Editor dialog' space='MD2024x']
- [CONFLUENCE_PAGE title='HTML editor' space='MD2024x']
- [CONFLUENCE_PAGE title='Text Box' space='MD2024x']
- [CONFLUENCE_PAGE title='Basic tasks in tables' space='MD2024x']
- [CONFLUENCE_PAGE title='Defining hyperlinks' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="5418a282-ea48-448c-9bd1-8a85a0500439"><ac:parameter ac:name="id">823840096</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3e2137f4-60db-441b-b893-06d9643160b4"><ac:parameter ac:name="id">823840099</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="deed9bda-3a68-42cf-8c94-abb3ff742e49"><ac:parameter ac:name="id">823840095</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="48e2a5d1-53bc-47de-a4ae-c4f6fc35874e"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="4ca5230b-e1da-4e95-b8e1-c6e68157f681"><ac:parameter ac:name="id">823840098</ac:parameter><ac:rich-text-body><p>The requirement always contains two properties: id and text. This section describes how to modify the text property of the requirement.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="text_property_requirement.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image></p><h6 style="text-align: center;">The<em> Stopping Distance</em> Requirement shape with filled Text property.</h6><h3>Editing the requirement text</h3><p>You can edit the requirement text directly on shapes and in cells, or use the <strong>Text</strong> dialog.</p><p>To open the edit mode of the requirement text, do one of the following</p><hr /><ul><li>On the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>, select the Text box on the Requirement shape. Click the text box again. The edit mode opens on the shape.</li><li>In the Requirements table, double-click the Text cell. The edit mode opens on the cell.</li><li>In the Requirements table, double-click the Text cell, and select <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="_buttons" /></ri:attachment></ac:image>. The <strong>Text</strong> dialog opens.</li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Open Specification window]]></ac:plain-text-link-body></ac:link> of the Requirement, select the Text property, and click <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="_buttons" /></ri:attachment></ac:image>. The <strong>Text</strong> dialog opens.</li></ul><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="902903b8-4326-48d0-b34c-cb984bb43785"><ac:parameter ac:name="">switch</ac:parameter></ac:structured-macro>Switching the requirement text to HTML or Plain text</h3><p>You can change the requirement text to HTML or Plain text directly on the Requirement shape or in the <strong>Text</strong> dialog.</p><p><br /></p><p>To switch the requirement text to HTML or Plain text directly on the Requirement shape</p><hr /><ol><li>On the diagram pane, select the text box on the Requirement shape.</li><li>Click one of the following buttons appearing on the lower left corner of the shape:<ul><li><strong>HTML</strong> - converts the text to HTML text.<br /><ac:image><ri:attachment ri:filename="switch_to_html_text.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image></li><li><strong>Plain</strong> - converts the text to plain text.<br /><ac:image ac:thumbnail="true" ac:height="139"><ri:attachment ri:filename="switch_to_plain_text.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image></li></ul></li></ol><p><br /></p><p>To switch the requirement text to HTML or Plain text in the <strong>Text</strong> dialog</p><hr /><ol><li>Open the <strong>Text</strong> dialog:<br /><ul><li>In the Requirements table, double-click the Text cell, and select <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image>.</li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Open Specification window]]></ac:plain-text-link-body></ac:link> of the Requirement, select the Text property, and click <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image>.</li></ul></li><li>In the <strong>Text</strong> dialog tootbar, do one of the following:<br /><ul><li>Select the <strong>HTML</strong> check box to convert the text to HTML text.<br /><ac:image><ri:attachment ri:filename="html_text_in_text_dialog.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image></li><li>Clear the <strong>HTML</strong> check box to convert the text to plain text.<br /><ac:image><ri:attachment ri:filename="plain_text_in_text_dialog.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image></li></ul></li><li>Click <strong>OK</strong>.<br /><br /></li></ol><h3>Modifying the requirement text</h3><p>You can modify the Requirement text in the following ways:</p><ul><li><ac:link ac:anchor="rich"><ac:plain-text-link-body><![CDATA[Rich text formatting]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ac:link></li><li><ac:link ac:anchor="glossary"><ac:plain-text-link-body><![CDATA[Using Glossary terms]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ac:link></li><li><ac:link ac:anchor="hyperlink"><ac:plain-text-link-body><![CDATA[Defining Hyperlinks]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ac:link></li><li><p><ac:link ac:anchor="image"><ac:plain-text-link-body><![CDATA[Inserting images into HTML text]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ac:link></p></li></ul><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="897b2415-539f-47a8-b859-1ed336917947"><ac:parameter ac:name="">rich</ac:parameter></ac:structured-macro>Rich text formatting</h4><p>If you <ac:link ac:anchor="switch"><ac:plain-text-link-body><![CDATA[switch the requirement text to HTML]]></ac:plain-text-link-body><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ac:link>, you can use the toolbar in the <strong>Text</strong> dialog to format it as rich text.</p><p><br /></p><p>To open the rich text formatting toolbar</p><hr /><ul><li>On the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link>, select the Text box on the Requirement shape. Click the text box again.</li><li>In the Requirements table, double-click the Requirement Text cell, and select <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image>.</li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Specification window" /><ac:plain-text-link-body><![CDATA[Open Specification window]]></ac:plain-text-link-body></ac:link> of the Requirement, select the Text property, and click <ac:image ac:title="Edit " ac:thumbnail="true" ac:alt="Edit " ac:height="17"><ri:attachment ri:filename="edit_button_in_specification_window.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image>.<br />If the Requirement text is in HTML format, the rich text formatting toolbar appears as shown in the following image.<br /><ac:image><ri:attachment ri:filename="rich_text_formatting_toolbar.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Modifying requirement text" /></ri:attachment></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2558b809-3a73-4ca0-9837-780ceb765587"><ac:parameter ac:name="title">HTML text editors</ac:parameter><ac:rich-text-body><p>Learn more about how to work with HTML texts:</p><ul><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Advanced HTML Editor dialog" /></ac:link></li><li><a href="https://docs.nomagic.com/display/MD2024x/HTML+editor" rel="nofollow">HTML editor</a></li></ul></ac:rich-text-body></ac:structured-macro><p><br /></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="cd74e719-40a4-4aa9-afd4-0c8f83725f11"><ac:parameter ac:name="">glossary</ac:parameter></ac:structured-macro>Using Glossary terms</h4><p>You can use the terms from the Glossary Table to ensure the same definitions of the concepts. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Glossary table" /><ac:plain-text-link-body><![CDATA[How to work with Glossary table >>]]></ac:plain-text-link-body></ac:link></p><p>If you want to extract a Constraint from a Requirement, you must use the special condition terms when defining the Requirement text.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d9d288ea-41be-4a29-ad93-a7ed28cfd26f"><ac:rich-text-body><p>The full procedure for extracting a Constraint from a Requirement is provided in the section <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Extracting Constraint from Requirement" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="2558f3f7-faed-4672-84f9-29b89e3d08a4"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Extracting Constraint from Requirement" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="76ef6479-4057-47f5-9992-fe0ca51e7185"><ac:parameter ac:name="">hyperlink</ac:parameter></ac:structured-macro>Defining hyperlinks</h4><p>You can add a hyperlink on the requirement text. How to add hyperlinks in text read in the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Hyperlinks in texts" /><ac:plain-text-link-body><![CDATA[Hyperlinks in text]]></ac:plain-text-link-body></ac:link> page.</p><p><br /></p><p><br /></p><h4><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2489dd0-e0f4-460b-9766-0d87c0544b0c"><ac:parameter ac:name="">image</ac:parameter></ac:structured-macro>Inserting images into HTML text</h4><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="679142f3-12df-4fc9-ae1e-fb1d48048a2a"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Inserting images into HTML text" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f7c235b1-33f4-42ea-97f4-766e3d5756cf"><ac:parameter ac:name="id">824150503</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Extracting Constraint from Requirement" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Advanced HTML Editor dialog" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="HTML editor" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Text Box" /></ac:link></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Basic tasks in tables" /></ac:link></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Defining hyperlinks" /></ac:link></span></li></ul><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720315 space=CRMP2024x version=2 -->
## PAGE 00074: Most common shortcut keys

- page_id: `136720315`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720315/Most+common+shortcut+keys
- version_number: 2
- version_date: `2024-01-29T14:57:04.317+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Most common shortcut keys' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="d1a6579f-e8d0-4bf9-9734-ec79e13fd069"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Most common shortcut keys" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720149 space=CRMP2024x version=1 -->
## PAGE 00075: Nesting requirements in the Requirements Table

- page_id: `136720149`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720149/Nesting+requirements+in+the+Requirements+Table
- version_number: 1
- version_date: `2023-09-21T10:22:36.177+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

INLINE

If you want to import nested structure of requirements, you must define the Owner property before the import, with the name or id of the requirement that owns it in the Excel file. When importing a nested structure of requirements from an Excel file you need to map the Owner column (defined in the excel file) with the Owner property. [CONFLUENCE_PAGE title='Importing data from Excel or CSV files' space='MD2024x']>]]>

To nest Requirement

1. Select a Requirement you want to nest in the Requirements Table.
2. Click the Nest button on the table toolbar. The selected Requirement is owned by the requirement in the previous row.

To unnest Requirement

1. Select a Requirement you want to unnest in the Requirements Table.
2. Click the Unnest button on the table toolbar. The selected requirement is owned by the owner of the current one.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="6af0fffc-b66c-47b4-ae92-6e346a62ae1f"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="bdc03c90-34b9-4212-b7c8-057e1bb1f1ca"><ac:rich-text-body><p>If you want to import nested structure of requirements, you must define the Owner property before the import, with the name or id of the requirement that owns it in the Excel file. When importing a nested structure of requirements from an Excel file you need to map the Owner column (defined in the excel file) with the Owner property. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Importing data from Excel or CSV files" /><ac:plain-text-link-body><![CDATA[Learn more how to import data from Excel/CSV file >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To nest Requirement</p><hr /><ol><li>Select a Requirement you want to nest in the Requirements Table.</li><li>Click the <strong>Nest </strong>button on the table toolbar.<br />The selected Requirement is owned by the requirement in the previous row.</li></ol><p> </p><p>To unnest Requirement</p><hr /><ol><li>Select a Requirement you want to unnest in the Requirements Table.</li><li>Click the <strong>Unnest </strong>button on the table toolbar.<br />The selected requirement is owned by the owner of the current one.</li></ol></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p> </p>
````

<!--NOMAGIC_PAGE id=136720101 space=CRMP2024x version=1 -->
## PAGE 00076: Opening projects

- page_id: `136720101`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720101/Opening+projects
- version_number: 1
- version_date: `2023-09-21T10:22:35.052+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started
- labels: []

### NORMALIZED CONTENT

564952218

564952220

564952219

[CONFLUENCE_PAGE title='Opening projects' space='MD2024x']true

564952217

**Related pages**

- [CONFLUENCE_PAGE title='Working with projects' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1e460928-0cfc-4c22-b77f-c71a63d15c82"><ac:parameter ac:name="id">564952218</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="66120c7a-7634-4d20-bdfc-94ba0be3e0d5"><ac:parameter ac:name="id">564952220</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7a7a019d-fd4c-43fa-841a-769a3941b537"><ac:parameter ac:name="id">564952219</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="dde6304d-b117-47cd-96d0-87a0f316c818"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Opening projects" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dfaa2768-ecc0-44ad-b874-7e906bc79098"><ac:parameter ac:name="id">564952217</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Working with projects" /></ac:link></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720305 space=CRMP2024x version=1 -->
## PAGE 00077: Other descriptions

- page_id: `136720305`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720305/Other+descriptions
- version_number: 1
- version_date: `2023-09-21T10:22:43.740+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts
- labels: []

### NORMALIZED CONTENT

This section contains other concepts related with the requirements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>This section contains other concepts related with the requirements.</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f8d0e103-9e85-40bf-a3cb-e087c968c39d" /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720289 space=CRMP2024x version=1 -->
## PAGE 00078: Performance Requirement

- page_id: `136720289`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720289/Performance+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:43.135+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Performance Requirement refers to a requirement that quantitatively measures the extent to which a system or a system part satisfy a required capability or condition.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="ff6c1156-434c-474d-9abb-307cc60746eb"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Performance Requirement refers to a requirement that quantitatively measures the extent to which a system or a system part satisfy a required capability or condition.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720290 space=CRMP2024x version=1 -->
## PAGE 00079: Physical Requirement

- page_id: `136720290`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720290/Physical+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:43.244+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Physical Requirement specifies the physical characteristics and/or physical constraints of a system or a system part.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="6e09f9bb-fc15-40cf-ada2-76cbf5e41dda"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Physical Requirement specifies the physical characteristics and/or physical constraints of a system or a system part.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720092 space=CRMP2024x version=1 -->
## PAGE 00080: Properties tab

- page_id: `136720092`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720092/Properties+tab
- version_number: 1
- version_date: `2023-09-21T10:22:34.781+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Properties tab' space='MD2024x']true

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="ce8aea57-5fb8-461e-8810-81f9e2713657"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Properties tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f66a763c-1625-4208-9fa1-67e984e84365"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720205 space=CRMP2024x version=1 -->
## PAGE 00081: Recursive loop of Copy dependencies

- page_id: `136720205`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720205/Recursive+loop+of+Copy+dependencies
- version_number: 1
- version_date: `2023-09-21T10:22:38.262+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
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

<!--NOMAGIC_PAGE id=136720301 space=CRMP2024x version=1 -->
## PAGE 00082: Refine

- page_id: `136720301`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720301/Refine
- version_number: 1
- version_date: `2023-09-21T10:22:43.664+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A 'Refine' relationship is a dependency that describes how a model element or a set of elements refine a requirement. For example, a use case or activity diagram may be used to refine a text-based functional requirement. Alternatively, it may be used to show how a text-based requirement refines a model element. In this case, some elaborated text could be used to refine a less fine- grained model element.

[IMAGE alt='' src='']

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="49bb7774-95dd-456c-9472-c42aaf7e3998"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A 'Refine' relationship is a dependency that describes how a model element or a set of elements refine a requirement. For example, a use case or activity diagram may be used to refine a text-based functional requirement. Alternatively, it may be used to show how a text-based requirement refines a model element. In this case, some elaborated text could be used to refine a less fine- grained model element.</p><p><ac:image ac:height="196" ac:width="167"><ri:attachment ri:filename="refine_relationship.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Refine" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720148 space=CRMP2024x version=2 -->
## PAGE 00083: Relating requirements

- page_id: `136720148`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720148/Relating+requirements
- version_number: 2
- version_date: `2024-01-29T11:13:56.372+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

820004269

820004271

820013872

**On this page**

820004270

INLINE

You can create relationships directly on the Requirement Diagram pane or in the Requirement Matrices such as Derive, Refine, Satisfy, or Verify.

##### Relating Requirements in the Requirement Diagram

To relate requirements on the Requirement Diagram pane

1. Open an existing or create a new Requirement Diagram. How to create a new diagram >
2. Represent requirements on the Requirement diagram.
3. Select a relation type either from the diagram pane or the smart manipulator of the selected requirement shape on the diagram pane.
4. Draw the selected relation from one requirement element to other.

##### Relating Requirements in the Requirement Matrices

To create a relation in the Requirement Matrices

1. Create a corresponding matrix or open an existing one.
2. In the intersection cell do one of the following: The relation is created. You can create more than one relation in the same cell.
  - Double click the intersection cell. The appropriate relation is created.
  - Right-click the intersection cell and, on the shortcut menu, and click the relation name.

820004266

**Related pages**

- [CONFLUENCE_PAGE title='Creating requirements' space='CRMP2024x']
- Derive Requirement Matrix
- Refine Requirement Matrix
- Satisfy Requirement Matrix
- Verify Requirement Matrix
- Derive
- Copy
- [CONFLUENCE_PAGE title='Trace' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Verify' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Refine' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Satisfy' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="bb298710-5b2b-4131-b9bf-61b4d344cc39"><ac:parameter ac:name="id">820004269</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="f5d95429-ad46-4c72-9735-c59e1bc7214a"><ac:parameter ac:name="id">820004271</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5bc512b8-c7ab-418e-8acc-7391e6a463d3"><ac:parameter ac:name="id">820013872</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="37f708e3-963c-467f-a001-e37f51053af9" /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d2b28037-58d4-4825-b2fe-f535fa575869"><ac:parameter ac:name="id">820004270</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="e0e96e4f-ac0b-4c01-af05-e1cc982a56fc"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>You can create relationships directly on the Requirement Diagram pane or in the Requirement Matrices such as Derive, Refine, Satisfy, or Verify.</p><h3>Relating Requirements in the Requirement Diagram</h3><p><br /></p><p>To relate requirements on the Requirement Diagram pane</p><hr /><ol><li>Open an existing or create a new Requirement Diagram. <a href="https://docs.nomagic.com/display/MD2024x/Creating+diagrams">How to create a new diagram &gt;</a></li><li>Represent requirements on the Requirement diagram.</li><li>Select a relation type either from the diagram pane or the smart manipulator of the selected requirement shape on the diagram pane.</li><li>Draw the selected relation from one requirement element to other.</li></ol><h3><br class="atl-forced-newline" />Relating Requirements in the Requirement Matrices</h3><p><br class="atl-forced-newline" />To create a relation in the Requirement Matrices</p><hr /><ol><li>Create a corresponding matrix or open an existing one. </li><li>In the intersection cell do one of the following:<br /><ul><li>Double click the intersection cell. The appropriate relation is created.</li><li>Right-click the intersection cell and, on the shortcut menu, and click the relation name.</li></ul><p class="auto-cursor-target">The relation is created.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e2e1d3d6-1d3c-4ffb-9cd9-556591a0ce7f"><ac:rich-text-body><p>You can create more than one relation in the same cell.</p></ac:rich-text-body></ac:structured-macro></li></ol></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9011fc32-a0cc-43d1-b819-3d9ae5b114a3"><ac:parameter ac:name="id">820004266</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating requirements" /></ac:link></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Derive+Requirement+Matrix">Derive Requirement Matrix</a></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Refine+Requirement+Matrix">Refine Requirement Matrix</a></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Satisfy+Requirement+Matrix">Satisfy Requirement Matrix</a></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Verify+Requirement+Matrix">Verify Requirement Matrix</a></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Derive">Derive</a></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Copy">Copy</a></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Trace" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Verify" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Refine" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Satisfy" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720165 space=CRMP2024x version=1 -->
## PAGE 00084: Replacing requirements

- page_id: `136720165`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720165/Replacing+requirements
- version_number: 1
- version_date: `2023-09-21T10:22:36.616+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Replacing elements' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="ab85b392-1d6e-4ddb-b6c1-d6bdbf4aeb70"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Replacing elements" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720306 space=CRMP2024x version=1 -->
## PAGE 00085: ReqIF

- page_id: `136720306`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720306/ReqIF
- version_number: 1
- version_date: `2023-09-21T10:22:43.764+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Other descriptions
- labels: []

### NORMALIZED CONTENT

25156739

25156750

25156749

The Requirement Interchange Format (ReqIF) standard is an XML based international standard adopted by Object Management Group (OMG) as a formal specification for exchanging requirements between software tools from different vendors.

25156728

**Related pages**

- [CONFLUENCE_PAGE title='Exchanging requirements with ReqIf' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ab15b1c1-f151-4d10-a77b-5ac66c2103ab"><ac:parameter ac:name="id">25156739</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6f6f78ac-cc03-42d6-b131-5f41f2b25ab4"><ac:parameter ac:name="id">25156750</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f405bc8d-4b8f-45ec-ac67-ba39ed049da9"><ac:parameter ac:name="id">25156749</ac:parameter><ac:rich-text-body><p>The Requirement Interchange Format (ReqIF) standard is an XML based international standard adopted by Object Management Group (OMG) as a formal specification for exchanging requirements between software tools from different vendors.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c6ed1d39-3740-45d8-86db-030e1e69a00f"><ac:parameter ac:name="id">25156728</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ac:link></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720291 space=CRMP2024x version=1 -->
## PAGE 00086: Requirement

- page_id: `136720291`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720291/Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:43.359+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Requirement specifies a capability or a condition that must (or should) be satisfied. Requirements are used to establish a contract between the customer (or other stakeholders) and those responsible for designing and implementing the system. A requirement can also appear on other diagrams to show its relationship to other modeling elements.

When a requirement nests other requirements, all the nested requirements apply as part of the container requirement (the requirement that contains all the nested requirements). Deleting the container requirement will thus delete all the nested requirements it contains; a functionality inherited from UML.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="0bf8ce73-9c31-4604-abd2-ec9eb00a7083"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Requirement specifies a capability or a condition that must (or should) be satisfied. Requirements are used to establish a contract between the customer (or other stakeholders) and those responsible for designing and implementing the system. A requirement can also appear on other diagrams to show its relationship to other modeling elements.</p><p>When a requirement nests other requirements, all the nested requirements apply as part of the container requirement (the requirement that contains all the nested requirements). Deleting the container requirement will thus delete all the nested requirements it contains; a functionality inherited from UML.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720277 space=CRMP2024x version=1 -->
## PAGE 00087: Requirement Diagram

- page_id: `136720277`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720277/Requirement+Diagram
- version_number: 1
- version_date: `2023-09-21T10:22:42.029+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

Requirement Diagram is particularly valuable when you want to demonstrate the traceability from the requirements to the elements in your system model that are dependent on them. This diagram provides modeling constructs to represent text-based requirements and relate them to other modeling elements. These requirement modeling constructs are intended to provide a bridge between traditional requirement management tools and other SysML models.

Requirements diagrams display requirements, packages, other classifiers, test cases, rationales, and relationships. Possible relationships available for Requirements diagrams are containments, deriveReqt and requirement dependencies (‘Copy’, ‘Refine’, ‘Satisfy’, ‘Trace’, and ‘Verify’). The callout notation can also be used to reflect the relationships of other models.

Requirements can also be shown on other diagrams to illustrate their relationships to other modeling elements.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="9dd51f45-3db7-4c35-bb36-8d9741b63664"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>Requirement Diagram is particularly valuable when you want to demonstrate the traceability from the requirements to the elements in your system model that are dependent on them. This diagram provides modeling constructs to represent text-based requirements and relate them to other modeling elements. These requirement modeling constructs are intended to provide a bridge between traditional requirement management tools and other SysML models.</p><p>Requirements diagrams display requirements, packages, other classifiers, test cases, rationales, and relationships. Possible relationships available for Requirements diagrams are containments, deriveReqt and requirement dependencies (‘Copy’, ‘Refine’, ‘Satisfy’, ‘Trace’, and ‘Verify’). The callout notation can also be used to reflect the relationships of other models.</p><p>Requirements can also be shown on other diagrams to illustrate their relationships to other modeling elements.</p><p><ac:image ac:title="Requirement Diagram" ac:alt="Requirement Diagram"><ri:attachment ri:filename="requirement_diagram.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p> </p>
````

<!--NOMAGIC_PAGE id=136720282 space=CRMP2024x version=1 -->
## PAGE 00088: Requirement matrices

- page_id: `136720282`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720282/Requirement+matrices
- version_number: 1
- version_date: `2023-09-21T10:22:42.346+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Matrices' space='SYSMLP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="8832965e-3cdc-4a96-a2f3-fc63b0b3913b"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Matrices" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136720307 space=CRMP2024x version=1 -->
## PAGE 00089: Requirement Specification

- page_id: `136720307`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720307/Requirement+Specification
- version_number: 1
- version_date: `2023-09-21T10:22:43.790+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Other descriptions
- labels: []

### NORMALIZED CONTENT

A represented collection of requirements that are related by a user decision or needs. A Requirement Specification may represent requirements for a system, a component, or other subjects. In a means of MagicDraw, a Requirement Specification is a package of requirements. A Usability Requirement specifies the fitness for use of a system for its users and other actors.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p>A represented collection of requirements that are related by a user decision or needs. A Requirement Specification may represent requirements for a system, a component, or other subjects. In a means of MagicDraw, a Requirement Specification is a package of requirements. A Usability Requirement specifies the fitness for use of a system for its users and other actors.</p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720280 space=CRMP2024x version=1 -->
## PAGE 00090: Requirement Table

- page_id: `136720280`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720280/Requirement+Table
- version_number: 1
- version_date: `2023-09-21T10:22:42.195+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Diagram descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Requirement Table is used to type a requirements into a spreadsheet-like table.

Requirements Table contains requirements. All requirements are text-based. Each row in the table represents a requirement. A new table consists of four columns by default (#, Id, Name, Text). You can add more columns to represent the properties of each requirement in the table. With this table, you can:

- Create new requirements directly in the table, or import existing ones from your model to the table.
- Edit the properties of requirements directly in the table.
- Generate requirements reports, renumber requirements’ IDs, or export the table into a CSV or HTML format, or into a Microsoft Excel (.xlsx) spreadsheet.
- Search and filter requirements.
- Access custom requirement’s properties.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="dffb03c3-578e-47e6-8650-19754f1c0520"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Requirement Table is used to type a requirements into a spreadsheet-like table.<span> </span></p><p>Requirements Table contains requirements. All requirements are text-based. Each row in the table represents a requirement. A new table consists of four columns by default (#, Id, Name, Text). You can add more columns to represent the properties of each requirement in the table. With this table, you can:</p><ul><li>Create new requirements directly in the table, or import existing ones from your model to the table.</li><li>Edit the properties of requirements directly in the table.</li><li>Generate requirements reports, renumber requirements’ IDs, or export the table into a CSV or HTML format, or into a Microsoft Excel (.xlsx) spreadsheet.</li><li>Search and filter requirements.</li><li>Access custom requirement’s properties.</li></ul><p><ac:image ac:title="Requirement Table" ac:alt="Requirement Table"><ri:attachment ri:filename="requirement_table.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ri:attachment></ac:image></p><p> </p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p> </p>
````

<!--NOMAGIC_PAGE id=136720166 space=CRMP2024x version=1 -->
## PAGE 00091: Requirements numbering

- page_id: `136720166`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720166/Requirements+numbering
- version_number: 1
- version_date: `2023-09-21T10:22:36.678+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

597916043

597916045

820209561

****

597916044

INLINE

When you create Requirements they are numbered by default with their unique IDs. The default Requirement IDs in the modeling tool are hierarchical numbers: 1, 1.1, 1.1.1, etc. See the following figure.

[IMAGE alt='' src='']

###### Requirements numbering.

The special validation rules ensure that each Requirement ID in your project is unique. For example, it is valuable when working with Teamwork Server orTeamwork Cloud and Requirements appear with the same IDs after commits. The validation rules check that and show errors.

If you want a different Requirement numbering than the default, you can [CONFLUENCE_PAGE title='Generic numbering mechanism' space='MD2024x']it manually by using the [CONFLUENCE_PAGE title='Element Numbering dialog' space='MD185']**Element Numbering** dialog. However, it is not recommended.

597916042

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="fdf56cfb-f406-49dd-b492-3b2e38f4d230"><ac:parameter ac:name="id">597916043</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="8ec0bb30-4a36-4d26-831f-eb0555e0f3b8"><ac:parameter ac:name="id">597916045</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8c7214dd-91ce-49a5-8759-687494033535"><ac:parameter ac:name="id">820209561</ac:parameter><ac:rich-text-body><p><br /></p><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="26c39913-97ee-4b23-9be5-b7e6b087842b"><ac:parameter ac:name="id">597916044</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="bc102ce6-0a97-43e9-b231-da40496c8dfa"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>When you create Requirements they are numbered by default with their unique IDs. The default Requirement IDs in the modeling tool are hierarchical numbers: 1, 1.1, 1.1.1, etc. See the following figure.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="req_numbering.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirements numbering" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Requirements numbering.</h6><p>The special validation rules ensure that each Requirement ID in your project is unique. For example, it is valuable when working with <span style="color: rgb(62,63,64);">Teamwork Server or </span>Teamwork Cloud and Requirements appear with the same IDs after commits. The validation rules check that and show errors.</p><p>If you want a different Requirement numbering than the default, you can <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Generic numbering mechanism" /><ac:plain-text-link-body><![CDATA[customize ]]></ac:plain-text-link-body></ac:link>it manually by using the <ac:link><ri:page ri:space-key="MD185" ri:content-title="Element Numbering dialog" /><ac:link-body><strong>Element Numbering</strong> dialog</ac:link-body></ac:link>. However, it is not recommended.</p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8e35b710-7039-46e2-8177-178c91830762"><ac:parameter ac:name="id">597916042</ac:parameter><ac:rich-text-body><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720199 space=CRMP2024x version=2 -->
## PAGE 00092: Requirements validation rules

- page_id: `136720199`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720199/Requirements+validation+rules
- version_number: 2
- version_date: `2024-01-29T14:59:28.315+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation
- labels: []

### NORMALIZED CONTENT

This page contains all constraints for the Requirements implemented in the tool as validation rules.

The Requirements validation suites and active validation suites include the following validation rules:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>This page contains all constraints for the Requirements implemented in the tool as validation rules.</p><p>The Requirements validation suites and active validation suites include the following validation rules:</p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="ef79c128-188b-421b-9404-13e69e2683db" /></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720198 space=CRMP2024x version=1 -->
## PAGE 00093: Requirements validation suites

- page_id: `136720198`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720198/Requirements+validation+suites
- version_number: 1
- version_date: `2023-09-21T10:22:37.665+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation
- labels: []

### NORMALIZED CONTENT

226644911

226644913

226644912

You can validate your model against a set of constraints called validation suites.

Each Profile contains its own validation suites. You can [CONFLUENCE_PAGE title='Creating validation suites' space='CRMP2024x'].

You can meet the following Requirements validation suites in the [CONFLUENCE_PAGE title='Validation dialog' space='CRMP2024x']**Validation** dialog or [CONFLUENCE_PAGE title='Validation Suites dialog' space='CRMP2024x']**Validation Suites** dialog:

- ActiveValSuite - Requirements contains active validation rules about [CONFLUENCE_PAGE title='Copy' space='CRMP2024x'] relationship and [CONFLUENCE_PAGE title='Test Case' space='CRMP2024x'] . The active validation suites enable you to see if a model is correct and complete immediately. It instantly displays any errors in the model and suggests appropriate solutions. The active validation suites have «activeValidationSuite» stereotype applied. [CONFLUENCE_PAGE title='Active validation suites' space='MD2024x']>]]>
- ValSuite - Requirements contains predefined Requirements validation rules about [CONFLUENCE_PAGE title='Copy' space='CRMP2024x'] relationship, Derive Requirement, [CONFLUENCE_PAGE title='Requirement' space='CRMP2024x'] , and [CONFLUENCE_PAGE title='Test Case' space='CRMP2024x'] . You need to perform the validation manually to check your model against the predefined validation suites. The predefined validation suites have «validationSuite» stereotype applied. [CONFLUENCE_PAGE title='Predefined validation suites' space='MD2024x']>]]>
- ValSuite - Suspect Links contains predefined Requirements validation rules about [CONFLUENCE_PAGE title='Suspect Links' space='MD2024x'] . You need to perform the validation manually to check your model against the predefined validation suites. The predefined validation suites have «validationSuite» stereotype applied. [CONFLUENCE_PAGE title='Predefined validation suites' space='MD2024x']>]]>

You can find predefined validation suites in the [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x'] when the **Show Auxiliary Resources** option is enabled, expand the *MD Customization for Requirements* Package> *Requirement constraints* Package. The *Requirement constraints* Package is divided into separate Packages and contain an appropriate [CONFLUENCE_PAGE title='Requirements validation rules' space='CRMP2024x'].

[CONFLUENCE_PAGE title='Metaclass' space='MD2024x']true

226644910

**Related pages**

- [CONFLUENCE_PAGE title='Predefined validation suites' space='MD2024x']
- [CONFLUENCE_PAGE title='Active validation suites' space='MD2024x']
- [CONFLUENCE_PAGE title='SysML validation suites' space='SYSMLP2024x']
- [CONFLUENCE_PAGE title='SysML active validation suites' space='SYSMLP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d4efa0dd-38bd-43df-b4d5-585c3689ce2b"><ac:parameter ac:name="id">226644911</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="03eebc9f-e182-4ab0-88da-bc0d8cc46910"><ac:parameter ac:name="id">226644913</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7b89b653-f65a-40ad-b7d8-68c0ba1716df"><ac:parameter ac:name="id">226644912</ac:parameter><ac:rich-text-body><p>You can validate your model against a set of constraints called validation suites.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="861f2d9f-cb9a-431c-ab64-893247d5056d"><ac:rich-text-body><p>Each Profile contains its own validation suites. You can <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating validation suites" /><ac:plain-text-link-body><![CDATA[create your own validation suites]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p>You can meet the following Requirements validation suites in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation dialog" /><ac:link-body><strong>Validation</strong> dialog</ac:link-body></ac:link> or <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation Suites dialog" /><ac:link-body><strong>Validation Suites</strong> dialog</ac:link-body></ac:link>:</p><ul><li><strong>ActiveValSuite - Requirements</strong>  contains active validation rules about <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Copy" /><ac:plain-text-link-body><![CDATA[Copy ]]></ac:plain-text-link-body></ac:link>relationship and <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Test Case" /></ac:link>. The active validation suites enable you to see if a model is correct and complete immediately. It instantly displays any errors in the model and suggests appropriate solutions. The active validation suites have «activeValidationSuite» stereotype applied. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Active validation suites" /><ac:plain-text-link-body><![CDATA[Learn how to work with active validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><strong>ValSuite - Requirements</strong> contains predefined Requirements validation rules about <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Copy" /><ac:plain-text-link-body><![CDATA[Copy ]]></ac:plain-text-link-body></ac:link>relationship, Derive Requirement, <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement" /></ac:link>, and <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Test Case" /></ac:link>. You need to perform the validation manually to check your model against the predefined validation suites. The predefined validation suites have «validationSuite» stereotype applied. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Predefined validation suites" /><ac:plain-text-link-body><![CDATA[Learn how to work with predefined validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><strong>ValSuite - Suspect Links </strong>contains predefined Requirements validation rules about<ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Suspect Links" /><ac:plain-text-link-body><![CDATA[ suspect links]]></ac:plain-text-link-body></ac:link>. You need to perform the validation manually to check your model against the predefined validation suites. The predefined validation suites have «validationSuite» stereotype applied. <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Predefined validation suites" /><ac:plain-text-link-body><![CDATA[Learn how to work with predefined validation suites >>]]></ac:plain-text-link-body></ac:link></li></ul><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2dd220e4-7112-4724-90ad-c80a600dfdcf"><ac:rich-text-body><p>You can find predefined validation suites in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /><ac:plain-text-link-body><![CDATA[Containment tree]]></ac:plain-text-link-body></ac:link> when the <strong>Show Auxiliary Resources</strong> option is enabled, expand the <em>MD Customization for Requirements</em> Package&gt; <em>Requirement constraints</em> Package. The <em>Requirement constraints</em> Package is divided into separate Packages and contain an appropriate <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirements validation rules" /><ac:plain-text-link-body><![CDATA[validation rules]]></ac:plain-text-link-body></ac:link>.</p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="b9d1327e-c590-49fb-8d1c-b17a15703fc7"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Metaclass" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7994f29b-e790-4457-a149-fe57d5ba4636"><ac:parameter ac:name="id">226644910</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul><li class="with-breadcrumbs"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Predefined validation suites" /><ac:plain-text-link-body><![CDATA[MagicDraw predefined validation suites]]></ac:plain-text-link-body></ac:link></li><li class="with-breadcrumbs"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Active validation suites" /><ac:plain-text-link-body><![CDATA[MagicDraw active validation suites]]></ac:plain-text-link-body></ac:link></li><li class="with-breadcrumbs"><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="SysML validation suites" /></ac:link></li><li class="with-breadcrumbs"><p class="with-breadcrumbs"><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="SysML active validation suites" /></ac:link></p></li></ul><p><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720303 space=CRMP2024x version=1 -->
## PAGE 00094: Satisfy

- page_id: `136720303`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720303/Satisfy
- version_number: 1
- version_date: `2023-09-21T10:22:43.700+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

946309211

946309223

946309213

INLINE

A 'Satisfy' relationship is a dependency between a requirement and a model element that fulfills that requirement. As with other dependencies, the arrow direction points from the satisfying (client) model element to the (supplier) requirement that is satisfied.

[IMAGE alt='' src='']

946309210

**Related pages**

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement matrices' space='SYSMLP2024x']

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d4e223cd-608e-4ee3-9763-62efe11fd252"><ac:parameter ac:name="id">946309211</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="b9b3bf01-dbaa-4a92-8609-f456ebefdd15"><ac:parameter ac:name="id">946309223</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="031dfabb-dab0-4b27-be01-391e2fb9ea47"><ac:parameter ac:name="id">946309213</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="7dd48974-36fd-41c1-b1d6-e67d70c23813"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A 'Satisfy' relationship is a dependency between a requirement and a model element that fulfills that requirement. As with other dependencies, the arrow direction points from the satisfying (client) model element to the (supplier) requirement that is satisfied.</p><p><ac:image><ri:attachment ri:filename="satisfy_relationship.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Satisfy" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="90905ab3-3eec-4177-8a9d-b6466ba2309c"><ac:parameter ac:name="id">946309210</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>Related pages</strong></p><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Requirement matrices" /><ac:plain-text-link-body><![CDATA[Satisfy Requirement Matrix]]></ac:plain-text-link-body></ac:link></span></li></ul><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720088 space=CRMP2024x version=2 -->
## PAGE 00095: Search Results tab

- page_id: `136720088`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720088/Search+Results+tab
- version_number: 2
- version_date: `2024-01-29T14:29:05.765+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

1361540657

1361540668

1361540667

true[CONFLUENCE_PAGE title='Search Results tab' space='MD2024x']

1361540646

**On this page**

****

1361569667

**Related pages**

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

****

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="1afef686-5af3-4f78-8a0c-f52e59b6e809"><ac:parameter ac:name="id">1361540657</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="1800c21b-f1dc-4085-8f74-0a59441dd2bc"><ac:parameter ac:name="id">1361540668</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7fdfdee1-cc77-4d49-ba3a-c42d31f32d90"><ac:parameter ac:name="id">1361540667</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="346f5d41-164f-48cd-8058-e58edd92b928"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Search Results tab" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cc9ef420-a342-4538-9515-4b32b59556b6"><ac:parameter ac:name="id">1361540646</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><strong><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="3a728bc3-2666-463a-b6c9-d99c1cd91c5d" /><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="405f8cff-5abe-4363-9c12-8a7822df5b14"><ac:parameter ac:name="id">1361569667</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720316 space=CRMP2024x version=1 -->
## PAGE 00096: Setting project options

- page_id: `136720316`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720316/Setting+project+options
- version_number: 1
- version_date: `2023-09-21T10:22:44.026+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Setting project options' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="dac7cdd6-2e1a-49a8-8113-6b6a5c2ec64d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Setting project options" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720222 space=CRMP2024x version=1 -->
## PAGE 00097: Specifying Constraint Element property

- page_id: `136720222`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720222/Specifying+Constraint+Element+property
- version_number: 1
- version_date: `2023-09-21T10:22:39.943+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation > Creating new validation rules
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Specifying Constraint Element property' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="71e105d6-a712-44f8-8868-83a9a7cd2d0b"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Specifying Constraint Element property" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720309 space=CRMP2024x version=1 -->
## PAGE 00098: Specifying project properties

- page_id: `136720309`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720309/Specifying+project+properties
- version_number: 1
- version_date: `2023-09-21T10:22:43.839+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Customizations
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Project Properties dialog' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="b94f1495-33f7-45bc-b74a-108ae31f98cb"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Project Properties dialog" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=136720225 space=CRMP2024x version=1 -->
## PAGE 00099: Specifying the validation rule properties

- page_id: `136720225`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720225/Specifying+the+validation+rule+properties
- version_number: 1
- version_date: `2023-09-21T10:22:40.148+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation > Creating new validation rules
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Specifying the validation rule properties' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="bee0d524-bb0a-4bd5-b9d5-d752c35928ac"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Specifying the validation rule properties" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720212 space=CRMP2024x version=1 -->
## PAGE 00100: Starting the validation

- page_id: `136720212`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720212/Starting+the+validation
- version_number: 1
- version_date: `2023-09-21T10:22:38.983+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Starting the validation' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="83bc0c49-6868-4e49-9e63-41d549187fbd"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Starting the validation" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720080 space=CRMP2024x version=3 -->
## PAGE 00101: Structure tab

- page_id: `136720080`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720080/Structure+tab
- version_number: 3
- version_date: `2024-01-29T14:56:37.995+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

733455784

733455804

733455794

true[CONFLUENCE_PAGE title='Structure tab' space='MD2024x']

733455782

**On this page**

- [The Structure tab in the Model Browser.](https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-TheStructuretabintheModelBrowser.)
- [Opening the Structure tab](https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-OpeningtheStructuretab)
- [Displaying Inherited Structure option](https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-inheritDisplayingInheritedStructureoption)
- [Nesting Satisfied Requirements option](https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-NestingSatisfiedRequirementsoption)
- [Structure tab toolbar](https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-Structuretabtoolbar)

****

733462571

**Related pages**

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="dd43690e-aff9-4f61-a817-b15c6630d97e"><ac:parameter ac:name="id">733455784</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="6e3d9bd3-e7d9-4b82-a0f3-54a453772b02"><ac:parameter ac:name="id">733455804</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a87ef663-1331-4f01-8cc5-5676ba912c03"><ac:parameter ac:name="id">733455794</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="43bedfc7-8663-446f-9931-bd0e9cfe874d"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Structure tab" /></ac:link></ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a78f2009-a6d3-4c42-8bdc-3cd7bce6881f"><ac:parameter ac:name="id">733455782</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><ul><li><span class="toc-item-body"><a href="https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-TheStructuretabintheModelBrowser." class="toc-link">The Structure tab in the Model Browser.</a></span></li><li><span class="toc-item-body"><a href="https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-OpeningtheStructuretab" class="toc-link">Opening the Structure tab</a></span></li><li><span class="toc-item-body"><a href="https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-inheritDisplayingInheritedStructureoption" class="toc-link">Displaying Inherited Structure option</a></span></li><li><span class="toc-item-body"><a href="https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-NestingSatisfiedRequirementsoption" class="toc-link">Nesting Satisfied Requirements option</a></span></li><li><span class="toc-item-body"><a class="toc-link" href="https://docs.nomagic.com/display/CRMP2024x/Structure+tab#Structuretab-Structuretabtoolbar">Structure tab toolbar</a></span></li></ul><p><strong><br /></strong></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5f10224b-9aff-463c-9883-1b701bf039d5"><ac:parameter ac:name="id">733462571</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720211 space=CRMP2024x version=1 -->
## PAGE 00102: Suspect Unlinked Requirement

- page_id: `136720211`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720211/Suspect+Unlinked+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:38.859+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Requirements validation rules
- labels: []

### NORMALIZED CONTENT

**Abbreviation**

UnlinkReq****

**Description**

An unlinked element was found.****

**Severity**

warning****

**Context element**

Abstract Requirement****

**Solvers**

**Example**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Abbreviation</strong></p><p>UnlinkReq<strong><br /></strong></p><p><strong>Description</strong></p><p>An unlinked element was found.<strong><br /></strong></p><p><strong>Severity</strong></p><p>warning<strong><br /></strong></p><p><strong>Context element</strong></p><p>Abstract Requirement<strong><br /></strong></p><p><strong>Solvers</strong></p><p><strong>Example</strong></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720102 space=CRMP2024x version=1 -->
## PAGE 00103: Switching between multiple projects

- page_id: `136720102`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720102/Switching+between+multiple+projects
- version_number: 1
- version_date: `2023-09-21T10:22:35.094+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Working with multiple projects' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="13d05c40-d38a-49e2-b69e-9eafdbed54c0"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Working with multiple projects" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720298 space=CRMP2024x version=1 -->
## PAGE 00104: Test Case

- page_id: `136720298`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720298/Test+Case
- version_number: 1
- version_date: `2023-09-21T10:22:43.592+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Test Case (Activity / StateMachine / Interaction) is a method for verifying a requirement.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="a924f1fc-9ac3-4a58-af31-569e61be0a93"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Test Case (Activity / StateMachine / Interaction) is a method for verifying a requirement.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720076 space=CRMP2024x version=2 -->
## PAGE 00105: Toolbars

- page_id: `136720076`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720076/Toolbars
- version_number: 2
- version_date: `2024-01-29T14:31:45.473+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Toolbars' space='MD2024x']

#### PANEL: On this page

On this page

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="ca1ef367-9922-470c-8c6e-981d09c0d662"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Toolbars" /></ac:link></ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="a94676ce-3885-4a49-b26a-d92cbdb1f569"><ac:parameter ac:name="title">
       On this page
      </ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="4d9411b7-50c2-40e9-b174-c140b877629e" /></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=136720299 space=CRMP2024x version=1 -->
## PAGE 00106: Trace

- page_id: `136720299`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720299/Trace
- version_number: 1
- version_date: `2023-09-21T10:22:43.614+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A 'Trace' relationship is a dependency between a requirement and an arbitrary model element traced by this requirement.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="749bb55f-4391-48f8-a3c2-9794c1416959"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A 'Trace' relationship is a dependency between a requirement and an arbitrary model element traced by this requirement.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720185 space=CRMP2024x version=1 -->
## PAGE 00107: Tracing requirements

- page_id: `136720185`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720185/Tracing+requirements
- version_number: 1
- version_date: `2023-09-21T10:22:37.348+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements
- labels: []

### NORMALIZED CONTENT

831113593

831113595

831113591

**On this page**

43

831113594

The traceability solution is available in Architect and Enterprise editions.

The traceability relations help determine how your requirements or other model artifacts are satisfied. As they change, you can use traceability relations to monitor the impact of these changes. You can visualize traceability relations using MagicDraw features, such as the Dependency Matrix or Relation Map. Requirements tracing is a background for analysis and is concerned with recovering the sources of requirements and predicting the effects of requirements. Tracing is fundamental to performing impact analysis when requirements change. A requirement should be traceable backwards to the criteria and stakeholders which motivated it (from functional requirements to business requirements). A requirement should also be traceable forwards into the design entities that satisfy it.

Traceability makes it easier for you to:

- Find, navigate and define the realization and specification of elements from different levels of abstraction:
- Understand why an element exists, how the element is realized, and clarify the purpose of the element.
- Validate the system functionality (to see if it meets customer requirements and if any superfluous functionality has been implemented).
- Improve a customer's understanding of the system and thus his/her acceptance of the system.
- Have single places for relations analysis used in traceability.
- Check artifact coverage and completeness.
- Bridge the gap between levels of abstraction.
- Trace elements by using out-of-the-box predefined traceability suites.

For detailed instructions on how to use the traceability solution, see [CONFLUENCE_PAGE title='Traceability' space='MD2024x'].

##### Traceability relations in Specification window

In the selected element's Specification window, you can see traceability relations as properties. You can also create your own specific properties and edit them here. 
 
 To trace element relations in the Specification window

1. Open the Specification window of the selected element.
2. Scroll through the general requirement's properties to get to the Traceability properties list.

###### [IMAGE alt='' src='']Traceability property group in element's specification window

For more information about using a Specification window, see [CONFLUENCE_PAGE title='Specification window' space='MD2024x'].

##### Traceability relations in Properties panel

The same traceability properties are displayed in a Properties panel. 
 
 To trace element relations in the Properties panel

1. Select the element in the [CONFLUENCE_PAGE title='Model Browser' space='MD2024x'] or the shape on the diagram pane.
2. In the Model Browser, click the Properties panel > Element tab and scroll through the properties to get to the Traceability properties list.

###### [IMAGE alt='' src='']Traceability property group in element's properties panel.

For more information about using the Properties panel, see [CONFLUENCE_PAGE title='Properties tab' space='MD2024x'].

##### Representing traceability on Notes

To trace element relations in a Note

1. Select the element's shape on the diagram pane.
2. Connect a note to the selected shape.
3. Right-click the note and click Edit Compartments on the shortcut menu,or select a note and click the Edit Element Properties button appearing on the right side of the note. [ATTACHMENT filename='edit_element_properties.png']
4. In the Compartment Edit dialog, click the Element Properties tab, select the traceability properties you want to represent on a note and move them from the Hidden to Selected list.
5. Click OK when you are done. Selected traceability properties are presented on a note.

###### [IMAGE alt='' src=''] 
Traceability properties on a note

##### Tracing relations using Go To command

The Go To command allows you to easily find and navigate to the related elements through the traceability relations. 
 
To trace element relations using the Go To command

1. Select the Requirement in the Containment tree or the shape on the diagram pane.
2. Right-click the selected Requirement. On the shortcut menu, click Go To > Traceability > Specification / Realization / Owner / Other and select the desired element. This element is selected in the Containment tree.

For more information about traceability, see [CONFLUENCE_PAGE title='Traceability' space='MD2024x'].

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c9689e84-5db8-45ce-ad6b-d770ab6cd2ee"><ac:parameter ac:name="id">831113593</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="42349e9d-21fb-4ed8-bed9-8a04da94d608"><ac:parameter ac:name="id">831113595</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c4fafd8b-78a5-4a6b-960c-069898e00759"><ac:parameter ac:name="id">831113591</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="a793b12a-d7e5-45df-9902-81f842fc0c8c"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6665ee71-1ce6-41ce-a3ad-c409d1ee4348"><ac:parameter ac:name="id">831113594</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="894f41fa-ff48-487e-aadf-836b9ce18e0e"><ac:rich-text-body><p>The traceability solution is available in Architect and Enterprise editions.</p></ac:rich-text-body></ac:structured-macro><p>The traceability relations help determine how your requirements or other model artifacts are satisfied. As they change, you can use traceability relations to monitor the impact of these changes. You can visualize traceability relations using MagicDraw features, such as the Dependency Matrix or Relation Map. Requirements tracing is a background for analysis and is concerned with recovering the sources of requirements and predicting the effects of requirements. Tracing is fundamental to performing impact analysis when requirements change. A requirement should be traceable backwards to the criteria and stakeholders which motivated it (from functional requirements to business requirements). A requirement should also be traceable forwards into the design entities that satisfy it.</p><p>Traceability makes it easier for you to:</p><ul><li>Find, navigate and define the realization and specification of elements from different levels of abstraction:</li><li>Understand why an element exists, how the element is realized, and clarify the purpose of the element.</li><li>Validate the system functionality (to see if it meets customer requirements and if any superfluous functionality has been implemented).</li><li>Improve a customer's understanding of the system and thus his/her acceptance of the system.</li><li>Have single places for relations analysis used in traceability.</li><li>Check artifact coverage and completeness.</li><li>Bridge the gap between levels of abstraction.</li><li>Trace elements by using out-of-the-box predefined traceability suites.</li></ul><p>For detailed instructions on how to use the traceability solution, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Traceability" /></ac:link>.</p><h3>Traceability relations in Specification window</h3><p>In the selected element's Specification window, you can see traceability relations as properties. You can also create your own specific properties and edit them here. <br class="atl-forced-newline" /><br class="atl-forced-newline" /> To trace element relations in the Specification window</p><hr /><ol><li>Open the Specification window of the selected element.</li><li>Scroll through the general requirement's properties to get to the <strong>Traceability</strong> properties list.</li></ol><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="traceability_property_group_in_element_specification_window.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Tracing requirements" /></ri:attachment></ac:image>Traceability property group in element's specification window</h6><p>For more information about using a Specification window, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Specification window" /></ac:link>.</p><h3>Traceability relations in Properties panel</h3><p>The same traceability properties are displayed in a Properties panel. <br class="atl-forced-newline" /><br class="atl-forced-newline" /> To trace element relations in the Properties panel</p><hr /><ol><li>Select the element in the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Browser" /></ac:link> or the shape on the diagram pane.</li><li>In the Model Browser, click the <strong>Properties</strong> panel &gt; <strong>Element</strong> tab and scroll through the properties to get to the <strong>Traceability</strong> properties list.</li></ol><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="Traceability_property_group_in_element_properties_panel.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Tracing requirements" /></ri:attachment></ac:image>Traceability property group in element's properties panel.</h6><p><br class="atl-forced-newline" /> For more information about using the Properties panel, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Properties tab" /></ac:link>.</p><h3>Representing traceability on Notes</h3><p><br /></p><p><br class="atl-forced-newline" /> To trace element relations in a Note</p><hr /><ol><li>Select the element's shape on the diagram pane.</li><li>Connect a note to the selected shape.</li><li>Right-click the note and click <strong>Edit Compartments</strong> on the shortcut menu,or select a note and click the <strong>Edit Element Properties</strong> button appearing on the right side of the note.<br /><ac:image ac:thumbnail="true" ac:height="80"><ri:attachment ri:filename="edit_element_properties.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Tracing requirements" /></ri:attachment></ac:image></li><li>In the <strong>Compartment Edit</strong> dialog, click the <strong>Element</strong><strong> Properties</strong> tab, select the traceability properties you want to represent on a note and move them from the <strong>Hidden</strong> to <strong>Selected</strong> list.</li><li>Click <strong>OK</strong> when you are done.<br />Selected traceability properties are presented on a note.</li></ol><h6 style="text-align: center;"><ac:image><ri:attachment ri:filename="traceability_properties_on_note.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Tracing requirements" /></ri:attachment></ac:image><br class="atl-forced-newline" />Traceability properties on a note</h6><h3><br class="atl-forced-newline" />Tracing relations using Go To command</h3><p><br class="atl-forced-newline" /> The Go To command allows you to easily find and navigate to the related elements through the traceability relations. <br class="atl-forced-newline" /><br class="atl-forced-newline" />To trace element relations using the Go To command</p><hr /><ol><li>Select the Requirement in the Containment tree or the shape on the diagram pane.</li><li>Right-click the selected Requirement. On the shortcut menu, click <strong>Go To</strong> &gt; <strong>Traceability</strong> &gt; <strong>Specification / Realization / Owner / Other</strong> and select the desired element.<br />This element is selected in the Containment tree.</li></ol><p><br /></p><p>For more information about traceability, see <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Traceability" /></ac:link>.</p><p><br /></p><p class="auto-cursor-target"><br /></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720074 space=CRMP2024x version=2 -->
## PAGE 00108: Understanding the user interface

- page_id: `136720074`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720074/Understanding+the+user+interface
- version_number: 2
- version_date: `2024-01-29T14:51:07.008+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started
- labels: []

### NORMALIZED CONTENT

732931906

732931917

732931907

true[CONFLUENCE_PAGE title='Understanding the user interface' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="c9159744-7f6a-4a7f-904b-1d4c69904413"><ac:parameter ac:name="id">732931906</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="fc4c15af-bbe8-4c8a-836b-599e2dfeb1b1"><ac:parameter ac:name="id">732931917</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c3802fda-8254-4557-a188-70a5b02d4bdc"><ac:parameter ac:name="id">732931907</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="b7513ec6-84ba-4b6e-99e4-9be942ae98e7"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Understanding the user interface" /></ac:link></ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720292 space=CRMP2024x version=1 -->
## PAGE 00109: Usability Requirement

- page_id: `136720292`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720292/Usability+Requirement
- version_number: 1
- version_date: `2023-09-21T10:22:43.502+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A Usability Requirement specifies the fitness for use of a system for its users and other actors.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="589f9f85-0f5b-4807-b4f2-55356a02c423"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A Usability Requirement specifies the fitness for use of a system for its users and other actors.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720072 space=CRMP2024x version=1 -->
## PAGE 00110: User Guide

- page_id: `136720072`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720072/User+Guide
- version_number: 1
- version_date: `2023-09-21T10:22:34.158+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation
- labels: []

### NORMALIZED CONTENT

**Welcome to the Cameo Requirements Modeler Plugin user guide!** It is intended to assist you with using this plugin. Please read the sections below or use the **Quick Search** box to find a specific topic.

- [Getting started.](https://docs.nomagic.com/display/CRMP2024x/Getting+started) This section presents the basic procedures for using the tool, such as:
  - creating a new Requirement project
  - specifying options and properties
  - customizing the environment, understand the concepts in the user interface
  - using the search and filter features
  - using the most common shortcut keys
  - and others.

- [Creating requirements.](https://docs.nomagic.com/display/CRMP2024x/Creating+requirements) This section shows how to create Requirements in the Requirement Diagram and Requirement Table.
- [Importing requirements.](https://docs.nomagic.com/display/CRMP2024x/Importing+requirements) This section describes how to import Requirements from ReqIF, CSV, Excel files, and how to use Cameo DataHub to interchange them.
- **Relating requirements.** This section explains how to create specific relationships between Requirements (including Derive, Refine, Satisfy, or Verify) directly on the Requirement Diagram pane or in the Requirement Matrices.
- [Creating Requirement Diagram for sub-requirements.](https://docs.nomagic.com/display/CRMP2024x/Creating+Requirement+Diagram+for+sub-requirements) This section demonstrates how to create a new Requirements Diagram for the sub-requirement that becomes the owner of a new diagram and is marked with the diagram sign.
- [Modifying requirement text.](https://docs.nomagic.com/display/CRMP2024x/Modifying+requirement+text) This section presents all procedures for editing and modifying the Requirement text by using the rich text formatting toolbar, Glossary terms, hyperlinks, and images. It also shows how to switch the requirement text to HTML or a Plain text format.
- [Customizing requirement properties.](https://docs.nomagic.com/display/CRMP2024x/Customizing+requirement+properties) This section shows how to create custom properties for the Requirements. It is closely related to the UML Profiling and DSL Guide when trying to extend Requirements with custom properties.
- [CONFLUENCE_PAGE title='Converting requirements' space='CRMP2024x'] This section shows how to use the Refactor command to convert one Requirement to another type of Requirement or any other element.
- [Replacing requirements.](https://docs.nomagic.com/display/CRMP2024x/Replacing+requirements) This section shows how to use the Refactor command to replace one Requirement with another one.
- [CONFLUENCE_PAGE title='Requirements numbering' space='CRMP2024x'] This section presents and explains how to number Requirements by automatically or manually setting their IDs.
- [Analyzing Requirements.](https://docs.nomagic.com/display/CRMP2024x/Analyzing+Requirements) This section offers mechanisms (such as Dependency Matrices, Relation Maps, validation, traceability, metrics, and others) allowing you to analyze Requirements in various formats and ways.
- [Extracting Constraint from Requirement.](https://docs.nomagic.com/display/CRMP2024x/Extracting+Constraint+from+Requirement) This section shows how to use the Extract Constraint From Requirement command for automatic constraint creation directly from the Requirement text.
- [Exporting requirements.](https://docs.nomagic.com/display/CRMP2024x/Exporting+requirements) This section describes how to export Requirements to ReqIF files manually, from the command-line interface, or automatically by applying an automated pre-processing script before ReqIF file export.
- [CONFLUENCE_PAGE title='Exchanging requirements with ReqIf' space='CRMP2024x']. The Requirement Interchange Format (ReqIF) standard is an XML based international standard adopted by Object Management Group (OMG) as a formal specification for exchanging requirements between software tools from different vendors.
- [Generating requirement reports.](https://docs.nomagic.com/display/CRMP2024x/Generating+requirement+reports) This section explains how to generate Requirement reports in the .docx and .html/.htm formats directly from your model.
- [Basic requirement concepts.](https://docs.nomagic.com/display/CRMP2024x/Basic+requirement+concepts) This section contains all specific requirement concepts and their descriptions.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><strong>Welcome to the Cameo Requirements Modeler Plugin user guide!</strong> It is intended to assist you with using this plugin. Please read the sections below or use the <strong>Quick Search</strong> box to find a specific topic.</p><ul><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Getting+started">Getting started.</a></strong><br />This section presents the basic procedures for using the tool, such as: <br /><ul><li>creating a new Requirement project</li><li>specifying options and properties</li><li>customizing the environment, understand the concepts in the user interface</li><li>using the search and filter features</li><li>using the most common shortcut keys</li><li>and others.</li></ul></li></ul><ul class="childpages-macro"><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Creating+requirements">Creating requirements.</a></strong><br />This section shows how to create Requirements in the Requirement Diagram and Requirement Table.<br /><br class="confluence-link" /></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Importing+requirements">Importing requirements.</a></strong><br />This section describes how to import Requirements from ReqIF, CSV, Excel files, and how to use Cameo DataHub to interchange them.<br /><br /></li><li><a href="https://docs.nomagic.com/display/CRMP2024x/Relating+requirements"><strong>Relating requirements.</strong><br /></a>This section explains how to create specific relationships between Requirements (including Derive, Refine, Satisfy, or Verify) directly on the Requirement Diagram pane or in the Requirement Matrices.<br /><br /></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Creating+Requirement+Diagram+for+sub-requirements">Creating Requirement Diagram for sub-requirements.</a></strong><br />This section demonstrates how to create a new Requirements Diagram for the sub-requirement that becomes the owner of a new diagram and is marked with the diagram sign.<br /><span class="confluence-link"><br /></span></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Modifying+requirement+text">Modifying requirement text.</a></strong><br />This section presents all procedures for editing and modifying the Requirement text by using the rich text formatting toolbar, Glossary terms, hyperlinks, and images. It also shows how to switch the requirement text to HTML or a Plain text format.<br /><br /></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Customizing+requirement+properties">Customizing requirement properties.</a></strong><br />This section shows how to create custom properties for the Requirements. It is closely related to the <a href="https://docs.nomagic.com/display/MD2024x/UML+Profiling+and+DSL+Guide">UML Profiling and DSL Guide</a> when trying to extend Requirements with custom properties.<br /><br /></li><li><strong><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Converting requirements" /><ac:plain-text-link-body><![CDATA[Converting requirements.]]></ac:plain-text-link-body></ac:link></strong><br />This section shows how to use the <strong>Refactor</strong> command to convert one Requirement to another type of Requirement or any other element.<br /><br /></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Replacing+requirements">Replacing requirements.</a></strong><br />This section shows how to use the <strong>Refactor</strong> command to replace one Requirement with another one.<br /><span class="confluence-link"><br /></span></li><li><strong><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirements numbering" /><ac:plain-text-link-body><![CDATA[Numbering Requirements.]]></ac:plain-text-link-body></ac:link></strong><br />This section presents and explains how to number Requirements by automatically or manually setting their IDs.<span class="confluence-link"><br class="confluence-link" /><br /></span></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Analyzing+Requirements">Analyzing Requirements.</a></strong><br />This section offers mechanisms (such as Dependency Matrices, Relation Maps, validation, traceability, metrics, and others) allowing you to analyze Requirements in various formats and ways.<br /><span class="confluence-link"><br /></span></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Extracting+Constraint+from+Requirement">Extracting Constraint from Requirement. </a></strong><br />This section shows how to use the <strong>Extract Constraint From Requirement</strong> command for automatic constraint creation directly from the Requirement text.<br /><span class="confluence-link"><br /></span></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Exporting+requirements">Exporting requirements.</a></strong><br />This section describes how to export Requirements to ReqIF files manually, from the command-line interface, or automatically by applying an automated pre-processing script before ReqIF file export.<br /><br /></li><li><strong><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Exchanging requirements with ReqIf" /></ac:link>.</strong><br /><span style="color: rgb(62,63,64);">The Requirement Interchange Format (ReqIF) standard is an XML based international standard adopted by Object Management Group (OMG) as a formal specification for exchanging requirements between software tools from different vendors.</span><br /><span class="confluence-link"><span class="confluence-link"><br /></span></span></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Generating+requirement+reports">Generating requirement reports.</a></strong><br />This section explains how to generate Requirement reports in the .docx and .html/.htm formats directly from your model.<br /><br /></li><li><strong><a href="https://docs.nomagic.com/display/CRMP2024x/Basic+requirement+concepts">Basic requirement concepts.</a></strong><br />This section contains all specific requirement concepts and their descriptions.<br /><br /></li></ul></ac:layout-cell><ac:layout-cell><p> </p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720246 space=CRMP2024x version=2 -->
## PAGE 00111: Using Requirement patterns glossary

- page_id: `136720246`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720246/Using+Requirement+patterns+glossary
- version_number: 2
- version_date: `2024-02-19T16:16:43.680+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Warning

759888368

INLINE

#### CONTENT-COLUMN: Warning

759888370

INLINE

759896385

INLINE

**On this page**

43

#### CONTENT-BLOCK: Warning

759888369

INLINE

#### EXCERPT: Warning

INLINE

You can use the specific condition patterns in Requirement texts if you want to [CONFLUENCE_PAGE title='Extracting Constraint from Requirement' space=''].

##### Enabling/disabling the Requirement patterns underlining in Requirement text

Before using this feature, make sure the **Underline Patterns in Requirement Text**option is enabled.

To enable/disable Requirement patterns underlining

1. From the main menu, click Options > Project .
2. In the Project Options dialog, under the General group, click Requirements and select the Underline Patterns in Requirement Text option.
3. Set its value to *true* to underline the Requirement text that matches the defined pattern, or *false* - to disable it. The default value of the **Underline Patterns in Requirement Text**option is *true*. [IMAGE alt='' src='']

##### Defining custom condition patterns

If you can't find an appropriate condition pattern from the predefined glossary table, you can define a custom glossary. For this, you have to create a new Glossary Table with the <<requirementTerms>> stereotype applied.

define_new

To create a new glossary table with the [CONFLUENCE_PAGE title='Stereotype' space='MD2024x']<<requirementTerms>>

1. From the [CONFLUENCE_PAGE title='Toolbars' space='MD2024x'] , click the Create Diagram button.
2. Double-click the glossary table icon.
3. Open the Specification window of the newly created Glossary table.
4. Change the Applied Stereotype property value to <<requirementTerms>>.
5. Click Close . The new glossary table with the stereotype <<requirementTerms>> is created. You can now define your own condition patterns by adding them in the [CONFLUENCE_PAGE title='Glossary table' space='MD2024x'] .

##### Opening the predefined requirements glossary table

You can use condition patterns from the already created glossary table. If you want to check the most frequently used patterns, open the predefined glossary table.

defined termsTo open the predefined glossary table

1. In the [CONFLUENCE_PAGE title='Model Browser' space='MD2024x'] , click [ATTACHMENT filename='options_button_in_model_browser.png'] and select Show Auxiliary Resources .
2. Expand MD Customization for Requirements Package > requirement verification Package .
3. Double-click the requirement verification to open the table (see the figure below).

[IMAGE alt='' src='']

The glossary table with the stored frequently used condition patterns opens (see the following figure).

[IMAGE alt='' src='']

#### WARNING: Warning

Warning

You cannot extend the list of custom condition patterns in this Glossary Table.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="aa6f13b1-dc59-4ec9-bb23-030f42637c44"><ac:parameter ac:name="id">759888368</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="5b12fa97-3f68-4756-9abe-bb3440fd65e8"><ac:parameter ac:name="id">759888370</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="30094275-e499-468b-894c-97d3618a910d"><ac:parameter ac:name="id">759896385</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="44e0d020-6b61-420f-9831-f561ae63c099"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="28d9c0e0-28fd-4161-abd5-d373714c938f"><ac:parameter ac:name="id">759888369</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="c089f3b6-f71f-4cab-b299-cd5b511ab71e"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>You can use the specific condition patterns in Requirement texts if you want to <ac:link><ri:page ri:content-title="Extracting Constraint from Requirement" /><ac:plain-text-link-body><![CDATA[extract Constraint from Requirement automatically]]></ac:plain-text-link-body></ac:link>.</p><h3>Enabling/disabling the Requirement patterns underlining in Requirement text</h3><p>Before using this feature, make sure the <strong>Underline Patterns in Requirement Text</strong><span class="confluence-link"> option</span> is enabled.</p><p><br />To enable/disable Requirement patterns underlining</p><hr /><ol><li>From the main menu, click <strong>Options</strong> &gt; <strong>Project</strong>.</li><li>In the <strong>Project Options</strong> dialog, under the <strong>General</strong> group, click <strong>Requirements</strong> and select the <strong>Underline Patterns in Requirement Text</strong> option.</li><li><p class="auto-cursor-target">Set its value to <em>true</em> to underline the Requirement text that matches the defined pattern, or <em>false</em> - to disable it.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="bbe94568-549e-476c-980c-a0caac0cbed3"><ac:rich-text-body><p>The default value of the <strong>Underline Patterns in Requirement Text</strong><span> option is <em>true</em>.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Underline_Patterns_in_Requirement_Text.png" /></ac:image></p></li></ol><h3><span class="confluence-link">Defining custom condition patterns</span></h3><p><span class="confluence-link">If you can't find an appropriate condition pattern from the predefined glossary table, you can define a custom glossary. For this, you have <span class="confluence-link">to create a new Glossary Table with the &lt;&lt;requirementTerms&gt;&gt; stereotype applied</span>.</span></p><p><span class="confluence-link"><br /></span></p><p class="auto-cursor-target"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9df8259f-7862-49f3-8dfc-59bf0e29668e"><ac:parameter ac:name="">define_new</ac:parameter></ac:structured-macro></p><p>To create a new glossary table with the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Stereotype" /><ac:plain-text-link-body><![CDATA[stereotype ]]></ac:plain-text-link-body></ac:link>&lt;&lt;requirementTerms&gt;&gt;</p><hr /><ol><li>From the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Toolbars" /><ac:plain-text-link-body><![CDATA[main toolbar]]></ac:plain-text-link-body></ac:link>, click the <strong>Create Diagram</strong> button.</li><li>Double-click the glossary table icon.</li><li>Open the Specification window of the newly created Glossary table.</li><li>Change the <strong>Applied Stereotype</strong> property value to &lt;&lt;requirementTerms&gt;&gt;.</li><li>Click <strong>Close</strong>.<br />The new glossary table with the stereotype &lt;&lt;requirementTerms&gt;&gt; is created. You can now define your own condition patterns by adding them in the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Glossary table" /><ac:plain-text-link-body><![CDATA[Glossary Table]]></ac:plain-text-link-body></ac:link>.</li></ol><h3>Opening the predefined requirements glossary table</h3><p>You can use condition patterns from the already created glossary table. If you want to check the most frequently used patterns, open the predefined glossary table.</p><p><br /></p><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="937cd269-5c73-4f85-9a2b-1216d827684f"><ac:parameter ac:name="">defined terms</ac:parameter></ac:structured-macro>To open the predefined glossary table</p><hr /><ol><li>In the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Browser" /></ac:link>, click <ac:image ac:title="Options" ac:alt="Options"><ri:attachment ri:filename="options_button_in_model_browser.png" /></ac:image> and select <strong>Show Auxiliary Resources</strong>.</li><li>Expand <em>MD Customization for Requirements</em> Package &gt; <em><ac:inline-comment-marker ac:ref="acee9479-f4ae-43ec-8d0d-32c50647827a">requirement verification</ac:inline-comment-marker> </em>Package<em>.</em></li><li>Double-click the <em>requirement verification</em> to open the table (see the figure below).</li></ol><p><ac:image><ri:attachment ri:filename="requirement_verification_package.png" /></ac:image></p><p>The glossary table with the stored frequently used condition patterns opens (see the following figure).</p><p><ac:image><ri:attachment ri:filename="requirement_verification_patterns.png" /></ac:image></p><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="e360d443-e809-4497-bc90-58e7afc39754"><ac:parameter ac:name="title">Warning</ac:parameter><ac:rich-text-body><p>You cannot extend the list of custom condition patterns in this Glossary Table.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=136720078 space=CRMP2024x version=2 -->
## PAGE 00112: Using the Model Browser

- page_id: `136720078`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720078/Using+the+Model+Browser
- version_number: 2
- version_date: `2024-01-29T14:30:32.505+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

729316187

729316202

729316188

true[CONFLUENCE_PAGE title='Using the Model Browser' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d7ad47e9-ccfd-45c0-8c2e-a959821aa9a8"><ac:parameter ac:name="id">729316187</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="c1ec7e69-a666-41b0-8a3a-8958d8bf32b9"><ac:parameter ac:name="id">729316202</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="857f89fe-eccd-4d43-a21b-a9c960eb97bb"><ac:parameter ac:name="id">729316188</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="c0a3467d-5c92-4278-862a-7441cd4b1602"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /></ac:link></ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720190 space=CRMP2024x version=2 -->
## PAGE 00113: Validation

- page_id: `136720190`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720190/Validation
- version_number: 2
- version_date: `2024-01-29T14:58:40.879+01:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: Solvers of invalid elements

831175078

#### CONTENT-COLUMN: Solvers of invalid elements

831175080

227684947

**On this page**

43

#### CONTENT-BLOCK: Solvers of invalid elements

831175079

##### Purpose

Validation checks the accuracy, completeness, and correctness of a model, marks invalid elements in the model, and suggests solutions.

##### Validation suites

Models are validated against a set of validation rules. Each validation rule captures an imperative condition that must be checked against the model. Validation rules are grouped into meaningful groups called validation suites. There are predefined validation suites that you can customize. You can also create your own rules and group them into suites. Some validation rules are active; that is, they run all the time. Validation rules and suites can be exported into a separate project in order to reuse them. They are stored in the Teamwork Server or Teamwork Cloud server for exchange.

- [CONFLUENCE_PAGE title='Predefined validation suites' space='MD2024x']>]]>
- Learn more about SysML validation suites >>
- [CONFLUENCE_PAGE title='Active validation suites' space='MD2024x']>]]>
- Learn more about SysML active validation suites >>
- [CONFLUENCE_PAGE title='Requirements validation suites' space='CRMP2024x']>]]>
- [CONFLUENCE_PAGE title='Creating validation suites' space='CRMP2024x']>]]>
- [CONFLUENCE_PAGE title='Creating new validation rules' space='CRMP2024x']>]]>
- [CONFLUENCE_PAGE title='Global validation rules' space='CRMP2024x']>]]>

##### Validating your model

The validation can run on the entire model or on a selected part of it. All the elements in that scope are checked against relevant validation rules, and elements that violate these rules are reported in the [CONFLUENCE_PAGE title='Validation Results panel' space='CRMP2024x']**Validation Results** panel. They are also marked in the [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x'], and their symbols are highlighted. Diagrams, tables, matrices, and relation maps displaying these highlighted symbols have the validation results marker bar.

- [CONFLUENCE_PAGE title='Starting the validation' space='CRMP2024x']>]]>
- [CONFLUENCE_PAGE title='Validation results marker bar' space='CRMP2024x']Learn more about validation results marker bar >>
- [CONFLUENCE_PAGE title='Validation Results panel' space='CRMP2024x']Learn more about Validation Results panel >>
- [CONFLUENCE_PAGE title='Validation dialog' space='CRMP2024x']>]]>

##### Invalid elements representation

The invalid elements are marked as follows:

- [ATTACHMENT filename='error_icon.png'] - error or fatal error.
- [ATTACHMENT filename='warning_icon.png'] - warning.
- [ATTACHMENT filename='info_icon.png'] - debug or info.

[CONFLUENCE_PAGE title='Customizing severity levels' space='CRMP2024x']>]]>

You can see invalid elements in the following areas:

- In the [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x'] an invalid element is marked with a small symbol that depends on the failure severity. [ATTACHMENT filename='invalid_element_in_model_brower.png']
- On the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'] an invalid symbol is highlighted. [ATTACHMENT filename='invalid_symbol_on_diagram_pane.png']
- In the [CONFLUENCE_PAGE title='Validation results marker bar' space='CRMP2024x'] every marker of an invalid symbol is colored according to the violation severity. [ATTACHMENT filename='invalid_symbol_in_validation_results_marker_bar.png']
- On the [CONFLUENCE_PAGE title='Understanding the user interface' space='CRMP2024x'] the failure indicator displays the severity icon, number of errors, and the first letter of the error severity (F - fatal error; E - error; W - warning; D - debug; I - info). 
[IMAGE alt='' src='']

#### NOTE: Solvers of invalid elements

Solvers of invalid elements

You can analyze invalid elements and solve problems by selecting appropriate commands from the invalid element or symbol shortcut menu or in the [CONFLUENCE_PAGE title='Validation Results panel' space='CRMP2024x']**Validation Results** panel.

800700

831175077

**Related pages**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="e1d12125-aedb-455d-8d37-1defcea84c0a"><ac:parameter ac:name="id">831175078</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="31c18fd8-7e8f-4ea6-865a-bbc8bd73b6ca"><ac:parameter ac:name="id">831175080</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1c765dc7-2f75-439a-ab5b-0d99383e364d"><ac:parameter ac:name="id">227684947</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="e83e47e3-c77b-4594-a3ad-1ec6dec8f7ac"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0153bab8-104a-4369-9c58-dcd8f752dd54"><ac:parameter ac:name="id">831175079</ac:parameter><ac:rich-text-body><h3>Purpose</h3><p>Validation checks the accuracy, completeness, and correctness of a model, marks invalid elements in the model, and suggests solutions.</p><h3>Validation suites</h3><p>Models are validated against a set of validation rules. Each validation rule captures an imperative condition that must be checked against the model. Validation rules are grouped into meaningful groups called validation suites. There are predefined validation suites that you can customize. You can also create your own rules and group them into suites. Some validation rules are active; that is, they run all the time. Validation rules and suites can be exported into a separate project in order to reuse them. They are stored in the Teamwork Server or Teamwork Cloud server for exchange.</p><ul><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Predefined validation suites" /><ac:plain-text-link-body><![CDATA[Learn more about MagicDraw predefined validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><a href="https://docs.nomagic.com/display/SYSMLP2024x/SysML+validation+suites">Learn more about SysML validation suites &gt;&gt;</a></li><li><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Active validation suites" /><ac:plain-text-link-body><![CDATA[Learn more about MagicDraw active validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><a href="https://docs.nomagic.com/display/SYSMLP2024x/SysML+active+validation+suites">Learn more about SysML active validation suites &gt;&gt;</a></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirements validation suites" /><ac:plain-text-link-body><![CDATA[Learn more about Requirements validation suites >>]]></ac:plain-text-link-body></ac:link></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating validation suites" /><ac:plain-text-link-body><![CDATA[Learn how to create new validation suites >>]]></ac:plain-text-link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Creating new validation rules" /><ac:plain-text-link-body><![CDATA[Learn how to create new validation rule >>]]></ac:plain-text-link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Global validation rules" /><ac:plain-text-link-body><![CDATA[Learn more about global validation rules >>]]></ac:plain-text-link-body></ac:link></span></li></ul><h3>Validating your model</h3><p>The validation can run on the entire model or on a selected part of it. All the elements in that scope are checked against relevant validation rules, and elements that violate these rules are reported in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation Results panel" /><ac:link-body><strong>Validation Results</strong> panel</ac:link-body></ac:link>. They are also marked in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link>, and their symbols are highlighted. Diagrams, tables, matrices, and relation maps displaying these highlighted symbols have <span class="confluence-link">the validation results marker bar</span>.</p><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Starting the validation" /><ac:plain-text-link-body><![CDATA[Learn how to start the validation >>]]></ac:plain-text-link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation results marker bar" /><ac:link-body>Learn more about <span class="current">validation results marker bar &gt;&gt;</span></ac:link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation Results panel" /><ac:link-body>Learn more about <span class="current">Validation Results panel &gt;&gt;</span></ac:link-body></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation dialog" /><ac:plain-text-link-body><![CDATA[Learn more about Validation dialog >>]]></ac:plain-text-link-body></ac:link></span></li></ul><h3>Invalid elements representation</h3><p>The invalid elements are marked as follows:</p><ul><li><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="error_icon.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation" /></ri:attachment></ac:image> - error or fatal error.</li><li><ac:image ac:thumbnail="true" ac:height="17"><ri:attachment ri:filename="warning_icon.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation" /></ri:attachment></ac:image> - warning.</li><li><ac:image ac:thumbnail="true" ac:height="18"><ri:attachment ri:filename="info_icon.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation" /></ri:attachment></ac:image> - debug or info.<br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d02a399a-e347-4ed9-a562-d89caa67449f"><ac:rich-text-body><p><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Customizing severity levels" /><ac:plain-text-link-body><![CDATA[Learn how to customize severity levels >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p>You can see invalid elements in the following areas:</p><ul><li>In the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link> an invalid element is marked with a small symbol that depends on the failure severity.<br /><ac:image><ri:attachment ri:filename="invalid_element_in_model_brower.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation" /></ri:attachment></ac:image></li><li>On the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[diagram pane]]></ac:plain-text-link-body></ac:link> an invalid symbol is highlighted.<br /><ac:image><ri:attachment ri:filename="invalid_symbol_on_diagram_pane.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation" /></ri:attachment></ac:image></li><li>In the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation results marker bar" /><ac:plain-text-link-body><![CDATA[validation results marker bar]]></ac:plain-text-link-body></ac:link> every marker of an invalid symbol is colored according to the violation severity.<br /><ac:image><ri:attachment ri:filename="invalid_symbol_in_validation_results_marker_bar.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation" /></ri:attachment></ac:image></li><li><p class="auto-cursor-target">On the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Understanding the user interface" /><ac:plain-text-link-body><![CDATA[status bar]]></ac:plain-text-link-body></ac:link> the failure indicator displays the severity icon, number of errors, and the first letter of the error severity (F - fatal error; E - error; W - warning; D - debug; I - info).<br /><ac:image ac:thumbnail="true" ac:height="81"><ri:attachment ri:filename="example_of_error.png"><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation" /></ri:attachment></ac:image></p></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4b6e9bd0-8afb-4361-9b9f-432a6b38dbdb"><ac:parameter ac:name="title">Solvers of invalid elements</ac:parameter><ac:rich-text-body><p>You can analyze invalid elements and solve problems by selecting appropriate commands from the invalid element or symbol shortcut menu or in the <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Validation Results panel" /><ac:link-body><strong>Validation Results</strong> panel</ac:link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="7938a485-fa7c-4969-98b9-356d824aff35"><ac:parameter ac:name="width">800</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=YgyeNgpR7TA" /></ac:parameter><ac:parameter ac:name="height">700</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e8928258-5995-4b55-b636-c9e9d1851c22"><ac:parameter ac:name="id">831175077</ac:parameter><ac:rich-text-body><p><strong>Related pages</strong></p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="f8a589f4-ae6e-49c1-9160-a60a566d9428" /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720215 space=CRMP2024x version=1 -->
## PAGE 00114: Validation dialog

- page_id: `136720215`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720215/Validation+dialog
- version_number: 1
- version_date: `2023-09-21T10:22:39.231+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation
- labels: []

### NORMALIZED CONTENT

227890949

227890951

227890948

**On this page**

43

227890950

[CONFLUENCE_PAGE title='Validation dialog' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="eafeeac0-ca04-475b-9067-72af469f6d93"><ac:parameter ac:name="id">227890949</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="15560bbe-1e01-41e0-850d-33ca3aac1231"><ac:parameter ac:name="id">227890951</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="18074c76-ce18-4f96-9ddd-5c6810e4f3fd"><ac:parameter ac:name="id">227890948</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="caa2ccee-e80b-4dce-a000-f043f853cbf1"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8da4aeb2-caea-4476-a0b2-01ea187e6d0a"><ac:parameter ac:name="id">227890950</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="8e224012-9c5d-4e0b-b826-39b97f9643b2"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Validation dialog" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720213 space=CRMP2024x version=1 -->
## PAGE 00115: Validation results marker bar

- page_id: `136720213`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720213/Validation+results+marker+bar
- version_number: 1
- version_date: `2023-09-21T10:22:39.075+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Validation results marker bar' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="77020805-7ebe-4e25-9d66-b5220f778fda"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Validation results marker bar" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=136720214 space=CRMP2024x version=1 -->
## PAGE 00116: Validation Results panel

- page_id: `136720214`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720214/Validation+Results+panel
- version_number: 1
- version_date: `2023-09-21T10:22:39.152+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation
- labels: []

### NORMALIZED CONTENT

227839096

227839098

227839095

**On this page**

43

227839097

[CONFLUENCE_PAGE title='Validation Results panel' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="72cc4f2d-c55b-41f4-b829-b703d4db17af"><ac:parameter ac:name="id">227839096</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="79444717-5860-472a-af38-7a6bfaac1ae8"><ac:parameter ac:name="id">227839098</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="71d8826c-0fc7-437c-bda0-c6d55e7028c9"><ac:parameter ac:name="id">227839095</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="b8a9db7c-35dd-4f73-b7cc-2830ee5c8d60"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="2cd1549a-bf2f-436c-9b6c-e9e027a945ea"><ac:parameter ac:name="id">227839097</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="29ac21e6-fdc2-4941-91cd-5d8b61da6ced"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Validation Results panel" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720218 space=CRMP2024x version=1 -->
## PAGE 00117: Validation Suites dialog

- page_id: `136720218`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720218/Validation+Suites+dialog
- version_number: 1
- version_date: `2023-09-21T10:22:39.480+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Analyzing Requirements > Validation > Custom validation > Creating validation suites
- labels: []

### NORMALIZED CONTENT

227994665

227994668

227994664

**On this page**

43

227994667

[CONFLUENCE_PAGE title='Validation Suites dialog' space='MD2024x']true

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="165bcf2d-2f0f-4a84-9cf0-1e224e4af536"><ac:parameter ac:name="id">227994665</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="162924a4-fe29-4478-9a78-c2564e4f112d"><ac:parameter ac:name="id">227994668</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="16dd889e-19d4-4908-9ca1-679e0321d377"><ac:parameter ac:name="id">227994664</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fbcc11f3-f357-4036-810f-1e02ade13b79"><ac:parameter ac:name="maxLevel">4</ac:parameter><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a0c137c3-1e71-4657-84a6-78cf09623280"><ac:parameter ac:name="id">227994667</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="40b60c61-3461-48a9-bda5-36bc65919198"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Validation Suites dialog" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p><p><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136720300 space=CRMP2024x version=1 -->
## PAGE 00118: Verify

- page_id: `136720300`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720300/Verify
- version_number: 1
- version_date: `2023-09-21T10:22:43.640+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Basic requirement concepts > Element descriptions
- labels: []

### NORMALIZED CONTENT

INLINE

A 'Verify' relationship is a dependency between a requirement and a test case or a model element that can determine whether the system fulfills the requirement. As with other dependencies, the arrow direction points from the (client) test case to the (supplier) requirement.

#### PANEL: Related diagrams

Related diagrams

- [CONFLUENCE_PAGE title='Requirement Diagram' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Requirement Table' space='CRMP2024x']
- [CONFLUENCE_PAGE title='Verify Requirement Matrix' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="d12c185f-ebd4-4870-837e-e0b3d96fa1e2"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p>A 'Verify' relationship is a dependency between a requirement and a test case or a model element that can determine whether the system fulfills the requirement. As with other dependencies, the arrow direction points from the (client) test case to the (supplier) requirement.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="e7c2a5a7-b54d-4095-9d7c-1c6389263d6e"><ac:parameter ac:name="title">Related diagrams</ac:parameter><ac:rich-text-body><ul><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Diagram" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Requirement Table" /></ac:link></span></li><li><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Verify Requirement Matrix" /></ac:link><br /></span></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720093 space=CRMP2024x version=1 -->
## PAGE 00119: Working with model elements in the Model Browser

- page_id: `136720093`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720093/Working+with+model+elements+in+the+Model+Browser
- version_number: 1
- version_date: `2023-09-21T10:22:34.822+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='MD2024x']true

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Zoom tab' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="1799d16c-5d3f-4437-90e5-a7f09fe53239"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f66a763c-1625-4208-9fa1-67e984e84365"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Zoom tab" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=136720090 space=CRMP2024x version=1 -->
## PAGE 00120: Zoom tab

- page_id: `136720090`
- space_key: `CRMP2024x`
- source_url: https://docs.nomagic.com/spaces/CRMP2024x/pages/136720090/Zoom+tab
- version_number: 1
- version_date: `2023-09-21T10:22:34.703+02:00`
- ancestors: Cameo Requirements Modeler Plugin Documentation > User Guide > Getting started > Understanding the user interface > Model Browser
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Zoom tab' space='MD2024x']true

#### PANEL: Related pages

Related pages

- [CONFLUENCE_PAGE title='Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Using the Model Browser' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Containment tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Structure tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Diagrams tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Documentation tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Inheritance tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Lock View tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Model Extensions tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Properties tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Search Results tab' space='CRMP2024x']
  - [CONFLUENCE_PAGE title='Working with model elements in the Model Browser' space='CRMP2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="two_right_sidebar"><ac:layout-cell><p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="04ffc3df-b58f-4c84-828c-90a8fced79d5"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Zoom tab" /></ac:link></ac:parameter><ac:parameter ac:name="nopanel">true</ac:parameter></ac:structured-macro></p></ac:layout-cell><ac:layout-cell><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="panel" ac:schema-version="1" ac:macro-id="f66a763c-1625-4208-9fa1-67e984e84365"><ac:parameter ac:name="title">
       Related pages
      </ac:parameter><ac:rich-text-body><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Browser" /></ac:link><ul class="childpages-macro"><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Using the Model Browser" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Containment tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Structure tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Diagrams tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Documentation tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Inheritance tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Lock View tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Model Extensions tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Properties tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Search Results tab" /></ac:link></li><li><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Working with model elements in the Model Browser" /></ac:link></li></ul></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````
