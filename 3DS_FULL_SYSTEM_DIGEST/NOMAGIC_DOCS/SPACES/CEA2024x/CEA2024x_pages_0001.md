# NOMAGIC DOCUMENTATION SPACE: Cameo Enterprise Architecture 2024x

<!--NOMAGIC_SPACE key=CEA2024x chunk=1 -->

<!--NOMAGIC_PAGE id=137988303 space=CEA2024x version=2 -->
## PAGE 00001: 2022x News for Developers

- page_id: `137988303`
- space_key: `CEA2024x`
- source_url: https://docs.nomagic.com/spaces/CEA2024x/pages/137988303/2022x+News+for+Developers
- version_number: 2
- version_date: `2024-01-26T14:56:39.895+01:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

To learn more, follow the link: [CONFLUENCE_PAGE title='2022x News for Developers' space='MD2022x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To learn more, follow the link: <ac:link><ri:page ri:space-key="MD2022x" ri:content-title="2022x News for Developers" /></ac:link></p>
````

<!--NOMAGIC_PAGE id=137988276 space=CEA2024x version=37 -->
## PAGE 00002: 2024x Version News

- page_id: `137988276`
- space_key: `CEA2024x`
- source_url: https://docs.nomagic.com/spaces/CEA2024x/pages/137988276/2024x+Version+News
- version_number: 37
- version_date: `2024-11-29T13:52:30.530+01:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

#### CONTENT-LAYER: 2024x Hot Fix 2 available

753686899

INLINE

#### CONTENT-COLUMN: 2024x Hot Fix 2 available

100.00002%

753686902

INLINE

#### CONTENT-BLOCK: 2024x Hot Fix 2 available

243271308

INLINE

top [IMAGE alt='' src='']

Released: November 10, 2023

Diagramming improvements include specialized Security Process Flow diagrams aligned with Operational and Resource viewpoints and new NAFv4 Structure diagrams for Logical, Service, and Physical Resource Specification Viewpoints.

Additionally, the Strategic Viewpoint now offers simplified assembly tools, such as the Strategic Motivation Table and the Impact Matrix, enhancing analysis and traceability. Exchange management has been refined for better visibility control, and various dialogs have been optimized for efficient review and management. These enhancements, along with improved library support and renamed perspectives, provide you with a more intuitive and efficient modeling experience.

In SysML modeling, the 2024x release introduces several improvements to Item Flow creation and editing. The **Create / Edit Item Flow**dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition, **Autowire Parts** and **Delegate Port(s)** commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the **Delegate Port(s)** command functionality regarding nested ports is now improved to treat each displayed nested port individually.

For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.

Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.

We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.

To download the latest version, see [Downloading installation files](https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files). For further information, check the product documentation.

#### NOTE: 2024x Hot Fix 3 available

2024x Hot Fix 3 available

2024x Hot Fix 3 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 3 Version News' space='NMDOC']>]]>

#### NOTE: 2024x Hot Fix 2 available

2024x Hot Fix 2 available

2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 2 Version News' space='NMDOC']>]]>

****

- 
- 
  - 
  - 
  - 
- 
  - 
  - 
  - 
  - 
- 
- 
- 

****

- 
- 

****

- 
- 
- 

****

****

- 
- 
- 
- 

****

- 
  - 
  - 
- 
  - 
  - 

753686901

INLINE

###### UAF 1.2 Features

##### UAF Behavior to Structure Synchronization

In the 2024x version, the UAF Behavior to Structure Synchronization has been enhanced. Now, you can automatically build the structure model according to defined Activities and generate an Internal Connectivity diagram by executing a single-click command. [CONFLUENCE_PAGE title='Creating structure models by behavior models' space='UAF12P2024x']>>]]>

[IMAGE alt='' src='']

##### Diagramming

###### New Security Process Flow diagrams

With version 2024x, the Security Process flow diagram has been specialized to align with two distinct Operational and Resource viewpoints, which led to the creation of two new diagrams: Security Process Flow (Operational) and Security Process Flow (Resource).

[IMAGE alt='' src='']

###### New NAFv4 Structure diagrams

New structure diagrams have been implemented in the Logical, Service, and Physical Resource Specification Viewpoints:

- [CONFLUENCE_PAGE title='L2 Logical Scenario' space='UAF12P2024x']
- [CONFLUENCE_PAGE title='S2 Service Structure' space='UAF12P2024x']
- [CONFLUENCE_PAGE title='P2 Resource Structure' space='UAF12P2024x']

###### New views in Strategic Viewpoint

Beginning with this version, the following new views related to the Strategic Viewpoint are introduced:

- Strategic Motivation Table , which you can find under the UAF Strategy Diagrams category, is designed to simplify the assembly of UAF Strategic requirements, such as Enterprise Goals and Enterprise Objectives, in a tabular format.
- Impact Matrix , which you can find under the UAF Analysis Diagrams category, illustrates the mapping between the Strategic, Operational, Resource, Service Viewpoint Elements and Strategic Viewpoint Elements using the Impacted By relationship.

600400

##### Exchange management improvements

This version adds significant enhancements to working with exchanges, including the ability to control their visibility on diagrams. Improved exchange creation wizards and management dialogs provide greater clarity.

###### Exchange visibility management

Now, you can easily manage the visibility of realized exchanges in the diagrams. The dedicated button in the smart manipulator toolbar allows you to choose whether you want to show or hide required Exchange Items.

[IMAGE alt='' src='']

###### This is an example of managing the visibility of Operational Exchange Items in an Operational Internal Connectivity diagram.

###### Realized Exchange wizard improvements

Additionally, 2024x brings a more focused approach to reviewing Activity pairs connected with existing Activity Edges in the **Realized Exchange wizards,** improving overall usability and clarity.

- In the second step, our focus has shifted solely to reviewing existing Activity Pairs connected by existing Activity Edges. This means that creating new Activity pairs or editing existing ones is no longer possible. As a result, the tool will no longer trigger the automatic generation of new elements or diagrams.
- We've introduced a new step called Affected Diagrams . This step lets you see where changes will occur after realizing elements or editing existing exchanges.

###### [IMAGE alt='' src=''] An example of changes in the Realized Resource Exchange creation wizard.

###### Exchange Manager improvements

In this release, we've made improvements to the **Exchange Managers**. Now, you'll find a handy **Affected Diagrams** button that opens a dialog listing all the diagrams containing elements that already realize the selected exchange.

###### [IMAGE alt='' src=''] An example of changes in the Operational Exchange Manager.

###### Producing and Consuming Functions dialog improvements

We've made some changes in the Producing and Consuming Activities/Functions dialogs as well. They now serve as tools for reviewing Activity pairs and easily removing any unnecessary ones.

###### [IMAGE alt='' src='']An example of changes in the Producing and Consuming Activities dialog.

##### Library Support

New DISR and UJTL library versions are now available:

- UJTL (20230616)
- DISR ( 20230523 )

You can choose the library version when creating a new project. [CONFLUENCE_PAGE title='Using libraries' space='UAF12P2024x']>]]>

##### Templates and Perspectives

###### New template

- A new **EA Project Template with Process Guide** is now available in UAF. This Enterprise Architecture (EA) Guide defines a workflow for creating EA views following the Unified Architecture Framework Modeling Language (UAFML). When using this template, you will receive a new UAF project enhanced with the EA Guide for UAF. This modeling guide aids in building architecture by providing nine steps of workflow.

###### Renamed

- The **UAF Enterprise Architecture Project** was renamed to **EA with BPMN Project**. Using the **EA with BPMN Project** template, you will get a simplified Enterprise Architecture project with BPMN, which is based on the UAF framework and designed for enterprise and IT architecture modeling. Creating an EA with the BPMN project will switch the modeling tool to the EA-BPMN Architect graphical user interface and use the EA with the BPMN model template.
- The perspective **UAF Enterprise Architect** was renamedto **EA-BPMN Architect.** [CONFLUENCE_PAGE title='Select Perspective dialog' space='UAF12P2024x']>>]]>

###### Removed

- The **UAF EA Project Template with Process Guide** was removed.

##### Other Enhancements

- The nested ports in all relevant viewpoints are now supported.
- The options for Information Flows in the Environment Options dialog under the UAF options group are no longer available.
- The Tools option group containing the Autowire Parts action is removed from the UAF Parametric Diagram toolbar.
- The Delegate Port(s) action is now implemented in the Internal Connectivity Diagrams and is available from the diagrams toolbar and context menu of roles, connectors, and ports .
- You can now create the Vision Statement in the **Specification**window of the Vision element.
- New correctness validation rules regarding the Motivated By relationship are now available. These rules check if the Motivated By relationship is created between correct pairs.
- A new passive validation rule COR2361 is implemented. This rule checks if an Operation Port Class Property type is correct.

244508097

INLINE

###### SysML Features

##### Improved Item Flow Creation and Editing

SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the **Create / Edit Item Flow** dialog, improving overall usability and clarity.

- Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:
  - New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams.
  - The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in a well-organized diagram list in the third step, accurately representing selected options.

[IMAGE alt='' src='']

###### A comparison of some of the changes in the second step of the **Create / Edit Item Flow** dialog between versions 2024x and 2022x Refresh2.

[CONFLUENCE_PAGE title='Creating Item Flow' space='SYSMLP2024x']>]]>

##### Other Improvements

- The Tools option group containing Autowire Parts and Delegate Port(s) commands has been removed from the SysML Parametric Diagram toolbar. Both Delegate Port(s) and Autowire Parts commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.
- Improved Delegate Port(s) command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. [CONFLUENCE_PAGE title='Automatic delegation' space='SYSMLP2024x']>]]>

256630726

INLINE

###### Discontinued Features

The following features have been discontinued with the 2024x version release.

##### JavaScript Nashorn Scripting

The JavaScriptNashorn language usage has been removed from the modeling tool. Please use JavaScript *Rhino* instead*.*This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.

[CONFLUENCE_PAGE title='Deprecated JavaScript Nashorn' space='MD2024x']>]]>

##### Record Macro Functionality

The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.

##### SPEM Plugin

The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.

###### Known Migration Issues

Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.

To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the <modeling_tool_install_dir>\bin\<modeling_tool>.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.

272319258

INLINE

###### Modeling and Infrastructure

##### DSLS Licensing

Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:

- License usage statistics, debugging, and simple UI to administer and view statistics.
- Licenses are bound to their expiration date rather than the product version.
- Nodelock (seat), floating, and managed licensing options.

Thus, now you can choose to use either FlexNet or DSLS for product licensing.

The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version R2024x with modeling tool version 2024x).

[CONFLUENCE_PAGE title='DSLS installation and licensing' space='IL2024x']>]]>

##### Zoom in Model BrowserZoom in Model Browser

From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking.

[IMAGE alt='' src='']

###### Zooming in the Model Browser using keyboard shortcuts.

[CONFLUENCE_PAGE title='Using the Model Browser' space='MD2024x']>]]>

##### Advanced Legend Adornments in Tables

In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.

[IMAGE alt='' src='']

###### Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item *In Progress*.

##### MIotherOther Improvements

- OpenJDK version update. Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version.
- Supported operating system changes for Linux. CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support.
- JavaScript Rhino version update. The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.
- It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.

243174490

INLINE

###### CollaborationCollaboration

##### TWCTeamwork Cloud

###### New File Exchange Format for Server Projects

In version 2022x Refresh2, we introduced **.szip** – a new [CONFLUENCE_PAGE title='Using server project file format' space='MD2024x']. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.

In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.

###### [IMAGE alt='' src='']

The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.

[IMAGE alt='' src=''] [IMAGE alt='' src='']

###### Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).

###### Model Patch Mechanism (Technology Preview)

We introduce the technology preview of the [CONFLUENCE_PAGE title='Model Patch - Technology preview' space='MD2024x'], a more lightweight way to move model changes. Model Patch can help you:

- Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;
- Transfer only a specific scope of model changes between disconnected teams instead of the entire model;
- Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.

###### [IMAGE alt='' src='']

##### PowerPower’By

###### New Features to Manage Used Projects

We added new features that provide you with better capabilities to manage used projects in **3D**EXPERIENCE:

- Export packages as a new server project;
- Move elements to/from used projects;
- Import used projects.

###### Opening Projects in Read-Only Mode

Beginning with version 2024x, you can open **3D**EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.

[IMAGE alt='' src='']

###### Notification informing the user that the **3D**EXPERIENCE project is read-only.

430554266

INLINE

**[CONFLUENCE_PAGE title='2024x Version News' space='NMDOC']>]]>**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ac060d11-24bb-43ee-828b-bfae5b72f6eb"><ac:parameter ac:name="id">753686899</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d04429d1-af39-4fcc-95f9-34e91a0b1fb5"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">753686902</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><br /><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="30610e88-4291-44f1-a1ed-49684a2d0cc5"><ac:parameter ac:name="id">243271308</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p style="text-align: center;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fd7d672f-fb01-4e70-8982-8ff70256549a"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro> <ac:image ac:width="465"><ri:attachment ri:filename="CEA.png" /></ac:image></p><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released: November 10, 2023 </span></p><p><br /></p>In the 2024x version of UAF, significant enhancements have been introduced. Behavior to Structure Synchronization has been enriched, allowing the automatic construction of structure models from defined activities and enabling one-click generation of Internal Connectivity diagrams.<p>Diagramming improvements include specialized Security Process Flow diagrams aligned with Operational and Resource viewpoints and new NAFv4 Structure diagrams for Logical, Service, and Physical Resource Specification Viewpoints.</p><p>Additionally, the Strategic Viewpoint now offers simplified assembly tools, such as the Strategic Motivation Table and the Impact Matrix, enhancing analysis and traceability. Exchange management has been refined for better visibility control, and various dialogs have been optimized for efficient review and management. These enhancements, along with improved library support and renamed perspectives, provide you with a more intuitive and efficient modeling experience.</p><p><span style="color: rgb(62,63,64);">In SysML modeling, the 2024x release introduces several improvements to Item Flow creation and editing. The<span> </span> <strong>Create / Edit Item Flow<span> </span> </strong>dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition,<span> </span> <strong style="text-align: left;">Autowire Parts</strong> <span> </span>and<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>command functionality regarding nested ports is now improved to treat each displayed nested port individually.</span></p><p><span>For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</span></p><p><span>Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.</span></p><p><span>We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.</span></p><p>To download the latest version, see <a href="https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files">Downloading installation files</a>. For further information, check the product documentation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a672b7b3-8ef4-458a-b61f-9c4fafd6dc87"><ac:parameter ac:name="title">2024x Hot Fix 3 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 3 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Hot Fix 3 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d7532128-51a7-45ef-87bc-961374545d5f"><ac:parameter ac:name="title">2024x Hot Fix 2 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Hot Fix 2 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong> <ac:link ac:anchor="UAF 1.2 Features" /> </strong></p><ul><li><ac:link ac:anchor="UAF Behavior to Structure Synchronization" /></li><li><ac:link ac:anchor="Diagramming" /><ul><li><ac:link ac:anchor="New Security Process Flow diagrams" /></li><li><ac:link ac:anchor="New NAFv4 Structure diagrams" /></li><li><ac:link ac:anchor="New views in Strategic Viewpoint" /></li></ul></li><li><ac:link ac:anchor="Exchange management improvements" /><ul><li><ac:link ac:anchor="Exchange visibility management" /></li><li><ac:link ac:anchor="Realized Exchange wizard improvements" /></li><li><ac:link ac:anchor="Exchange Manager improvements" /></li><li><ac:link ac:anchor="Producing and Consuming Functions dialog improvements" /></li></ul></li><li><ac:link ac:anchor="Library Support" /></li><li><ac:link ac:anchor="Templates and Perspectives" /></li><li><ac:link ac:anchor="Other Enhancements" /></li></ul><p><strong> <ac:link ac:anchor="SysML Features" /> </strong></p><ul><li><ac:link ac:anchor="Improved Item Flow Creation and Editing" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Discontinued Features" /> </strong></p><ul><li><ac:link ac:anchor="JavaScript Nashorn Scripting" /></li><li><ac:link ac:anchor="Record Macro Functionality" /></li><li><ac:link ac:anchor="SPEM Plugin" /></li></ul><p><strong> <ac:link ac:anchor="Known Migration Issues" /> </strong></p><p><strong> <ac:link ac:anchor="Modeling and Infrastructure" /> </strong></p><ul><li><ac:link ac:anchor="DSLS Licensing" /></li><li><ac:link ac:anchor="Zoom in Model Browser" /></li><li><ac:link ac:anchor="Advanced Legend Adornments in Tables" /></li><li><ac:link ac:anchor="MIother"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"> <ac:link ac:anchor="Collaboration" /> </strong></p><ul><li><ac:link ac:anchor="Teamwork Cloud" /><ul><li><ac:link ac:anchor="New File Exchange Format for Server Projects" /></li><li><ac:link ac:anchor="Model Patch Mechanism (Technology Preview)" /></li></ul></li><li><ac:link ac:anchor="Power"><ac:plain-text-link-body><![CDATA[Power'By]]></ac:plain-text-link-body></ac:link><ul><li><ac:link ac:anchor="New Features to Manage Used Projects" /></li><li><ac:link ac:anchor="Opening Projects in Read-Only Mode" /></li></ul></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="165032c6-162e-4b91-ac3b-64ad3ac32452"><ac:parameter ac:name="id">753686901</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5>UAF 1.2 Features</h5><h3>UAF Behavior to Structure Synchronization</h3><p>In the 2024x version, the UAF Behavior to Structure Synchronization has been enhanced. Now, you can automatically build the structure model according to defined Activities and generate an Internal Connectivity diagram by executing a single-click command. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Creating structure models by behavior models" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="internal_connectivity_diagram_by_begavior_model_news.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Diagramming</h3><h4>New Security Process Flow diagrams</h4><p>With version 2024x, the Security Process flow diagram has been specialized to align with two distinct Operational and Resource viewpoints, which led to the creation of two new diagrams: Security Process Flow (Operational) and Security Process Flow (Resource).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Security Process Flow diagrams.png" /></ac:image></p><h4>New NAFv4 Structure diagrams</h4><p>New structure diagrams have been implemented in the Logical, Service, and Physical Resource Specification Viewpoints:</p><ul><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="L2 Logical Scenario" /></ac:link> </li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="S2 Service Structure" /></ac:link></li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="P2 Resource Structure" /></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><h4>       </h4><h4>New views in Strategic Viewpoint</h4><p>Beginning with this version, the following new views related to the Strategic Viewpoint are introduced:</p><ul><li><strong>Strategic Motivation Table</strong>, which you can find under the UAF Strategy Diagrams category, is designed to simplify the assembly of UAF Strategic requirements, such as Enterprise Goals and Enterprise Objectives, in a tabular format. </li><li><strong>Impact Matrix</strong>, which you can find under the UAF Analysis Diagrams category, illustrates the mapping between the Strategic, Operational, Resource, Service Viewpoint Elements and Strategic Viewpoint Elements using the Impacted By relationship.</li></ul></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="0b19ebb0-c9d5-4fa4-abc5-1f15cb7c26eb"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=ngOqW2UVOSI&amp;ab_channel=CATIAMBSE" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Exchange management improvements</h3><p style="text-align: left;">This version adds significant enhancements to working with exchanges, including the ability to control their visibility on diagrams. Improved exchange creation wizards and management dialogs provide greater clarity.</p><h4 style="text-align: left;">Exchange visibility management</h4><p style="text-align: left;">Now, you can easily manage the visibility of realized exchanges in the diagrams. The dedicated button in the smart manipulator toolbar allows you to choose whether you want to show or hide required Exchange Items.</p><p style="text-align: left;"><ac:image ac:align="center"><ri:attachment ri:filename="show_operational_exchanges.png" /></ac:image></p><h6 style="text-align: center;">This is an example of managing the visibility of Operational Exchange Items in an Operational Internal Connectivity diagram.</h6><h4><span>Realized Exchange wizard improvements </span></h4><p><span>Additionally, 2024x brings a more focused approach to reviewing Activity pairs connected with existing Activity Edges in the </span> <strong>Realized Exchange wizards,</strong> <span> improving overall usability and clarity.</span></p><ul><li>In the second step, our focus has shifted solely to reviewing existing Activity Pairs connected by existing Activity Edges. This means that creating new Activity pairs or editing existing ones is no longer possible. As a result, the tool will no longer trigger the automatic generation of new elements or diagrams.</li><li>We've introduced a new step called <strong>Affected Diagrams</strong>. This step lets you see where changes will occur after realizing elements or editing existing exchanges.</li></ul><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="Exchange management changes.png" /></ac:image> </span> <span>An example of changes in the Realized Resource Exchange creation wizard.</span></h6><h4><span>Exchange Manager improvements</span></h4><p>In this release, we've made improvements to the <strong>Exchange Managers</strong>. Now, you'll find a handy <strong>Affected Diagrams</strong> button that opens a dialog listing all the diagrams containing elements that already realize the selected exchange.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="echanges_exchange_manager.png" /></ac:image> </span> <span>An example of changes in the Operational Exchange Manager. </span></h6><h4><span>Producing and Consuming Functions dialog improvements</span></h4><p>We've made some changes in the Producing and Consuming Activities/Functions dialogs as well. They now serve as tools for reviewing Activity pairs and easily removing any unnecessary ones.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="changes_producing_consuming_activities.png" /></ac:image>An example of changes in the Producing and Consuming Activities dialog.</span></h6><h3>Library Support</h3><p>New DISR and UJTL library versions are now available:</p><ul><li>UJTL (20230616)</li><li>DISR (<span style="color: rgb(23,43,77);">20230523</span>)</li></ul><p><span style="color: rgb(62,63,64);">You can choose the library version when creating a new project. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Using libraries" /><ac:plain-text-link-body><![CDATA[Learn more about using libraries >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Templates and Perspectives</h3><h4>New template</h4><ul><li>A new <span style="color: rgb(23,43,77);"> <strong>EA Project Template with Process Guide</strong> is now available in UAF. This Enterprise Architecture (EA) Guide defines a workflow for creating EA views following the Unified Architecture Framework Modeling Language (UAFML). When using this template, you will receive a new UAF project enhanced with the EA Guide for UAF. This modeling guide aids in building architecture by providing nine steps of workflow.</span></li></ul><h4><span style="color: rgb(23,43,77);">Renamed </span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF Enterprise Architecture Project</strong> was renamed to <strong>EA with BPMN Project</strong>. Using the <strong>EA with BPMN Project</strong> template, you will get a simplified Enterprise Architecture project with BPMN, which is based on the UAF framework and designed for enterprise and IT architecture modeling. Creating an EA with the BPMN project will switch the modeling tool to the EA-BPMN Architect graphical user interface and use the EA with the BPMN model template.</span></li><li><span style="color: rgb(23,43,77);">The perspective <strong style="text-align: left;">UAF Enterprise Architect</strong> <span> was renamed </span>to<span> </span> <strong style="text-align: left;">EA-BPMN Architect. </strong> <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Select Perspective dialog" /><ac:plain-text-link-body><![CDATA[Learn more about the perspectives >>>]]></ac:plain-text-link-body></ac:link> </span></li></ul><h4><span style="color: rgb(23,43,77);">Removed</span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF EA Project Template with Process Guide</strong> was removed.</span></li></ul><h3>Other Enhancements</h3><ul><li><span style="color: rgb(23,43,77);">The nested ports in all relevant viewpoints are now supported.</span></li><li>The options for <strong>Information Flows</strong> in the <strong>Environment Options</strong> dialog under the <strong>UAF </strong>options group are no longer available.</li><li>The<span> </span> <strong>Tools</strong> <span> </span>option group containing the<span> </span> <strong>Autowire Parts</strong> <span> </span>action is removed from the UAF Parametric Diagram toolbar.</li><li>The <strong>Delegate Port(s)</strong> <span> </span>action is now implemented in the Internal Connectivity Diagrams and is available from the <span style="color: rgb(23,43,77);">diagrams toolbar and context menu of roles, connectors, and ports</span>.</li><li><span style="color: rgb(23,43,77);">You can now create the Vision Statement in the <strong>Specification </strong>window of the Vision element.</span></li><li><span style="color: rgb(23,43,77);">New correctness validation rules regarding the Motivated By relationship are now available. These rules check if the Motivated By relationship is created between correct pairs.</span></li><li><span style="color: rgb(23,43,77);">A new passive validation rule COR2361 is implemented. This rule checks if an Operation Port Class Property type is correct.</span></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="90bd7b1e-43b6-43f5-8025-5097e80fab78"><ac:parameter ac:name="id">244508097</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>SysML Features</h5><h3>Improved Item Flow Creation and Editing</h3><p><span>SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the </span> <strong>Create / Edit Item Flow </strong> <span>dialog, improving overall usability and clarity.</span></p><ul><li><span>Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:</span><ul><li><span>New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams. </span></li><li>The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in <span>a well-organized diagram list in the third step, accurately representing selected options.</span></li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Improved_Item_Flow.png" /></ac:image></p><h6 style="text-align: center;">A comparison of some of the changes in the second step of the <strong>Create / Edit Item Flow</strong> dialog between versions 2024x and 2022x Refresh2.</h6><p><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more about Item Flow creation and editing >>]]></ac:plain-text-link-body></ac:link> </p><h3>Other Improvements</h3><ul><li>The <strong>Tools</strong> option group containing <strong>Autowire Parts</strong> and <strong>Delegate Port(s)</strong> commands has been removed from the SysML Parametric Diagram toolbar. Both <strong>Delegate Port(s)</strong> and <strong>Autowire Parts</strong> commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.</li><li>Improved <strong>Delegate Port(s)</strong> command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. <ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Automatic delegation" /><ac:plain-text-link-body><![CDATA[Learn more about automatic delegation >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d2134088-4966-4566-9a72-e0d0d9dd9d47"><ac:parameter ac:name="id">256630726</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Discontinued Features</h5><p>The following features have been discontinued with the 2024x version release.</p><h3>JavaScript Nashorn Scripting</h3><p><span style="color: rgb(62,63,64);">The JavaScript<span> </span> </span>Nashorn <span style="color: rgb(62,63,64);">language usage has been removed from the modeling tool. Please use JavaScript<span> </span> <em>Rhino</em> instead<em>. </em>This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Deprecated JavaScript Nashorn" /><ac:plain-text-link-body><![CDATA[Learn more about the deprecated JavaScript Nashorn >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Record Macro Functionality </h3><p>The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.</p><h3>SPEM Plugin</h3><p>The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.</p><h5>Known Migration Issues</h5><p>Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.</p><p>To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the &lt;modeling_tool_install_dir&gt;\bin\&lt;modeling_tool&gt;.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="eb46d24f-3281-4de3-b6b2-1ecb89f93d0c"><ac:parameter ac:name="id">272319258</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Modeling and Infrastructure</h5><h3>DSLS Licensing</h3><p>Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:</p><ul><li>License usage statistics, debugging, and simple UI to administer and view statistics.</li><li>Licenses are bound to their expiration date rather than the product version.</li><li>Nodelock (seat), floating, and managed licensing options.</li></ul><p>Thus, now you can choose to use either FlexNet or DSLS for product licensing. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f49ff8d-45a1-456c-a2a0-a919be8c1f02"><ac:rich-text-body><p>The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version <span>R2024x with modeling tool version 2024x</span>).</p></ac:rich-text-body></ac:structured-macro><p><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS Licensing >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9484f639-acef-4728-8acc-d1e2338719d2"><ac:parameter ac:name="">Zoom in Model Browser</ac:parameter></ac:structured-macro>Zoom in Model Browser</h3><p>From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking. </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Zoom in Model Browser.png" /></ac:image></p><h6 style="text-align: center;">Zooming in the Model Browser using keyboard shortcuts.</h6><p><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /><ac:plain-text-link-body><![CDATA[Learn more about zooming in the Model Browser>>]]></ac:plain-text-link-body></ac:link></p><h3>Advanced Legend Adornments in Tables</h3><p>In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Advanced Legend Adornments in Tables Example.png" /></ac:image></p><h6 style="text-align: center;">Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item <em>In Progress</em>.</h6><p style="text-align: right;"><br /></p><h3 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6c8c8907-e1fd-4c63-9547-aff205bb1046"><ac:parameter ac:name="">MIother</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li><strong>OpenJDK version update. </strong>Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version. </li><li><strong> <span style="color: rgb(62,63,64);">Supported operating system changes for Linux. </span> </strong> <span style="color: rgb(62,63,64);">CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support. </span></li><li><strong>JavaScript Rhino version update.</strong> The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</li><li>It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.</li></ul><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f7e102f2-3db2-4461-a12e-4ff53e738c59"><ac:parameter ac:name="id">243174490</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h5><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="82578d71-581b-42b4-bfdc-d5dcd49ff7cd"><ac:parameter ac:name="">TWC</ac:parameter></ac:structured-macro> </span>Teamwork Cloud</h3><h4 style="text-align: left;">New File Exchange Format for Server Projects</h4><p>In version 2022x Refresh2, we introduced <strong>.szip</strong> – a new <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using server project file format" /><ac:plain-text-link-body><![CDATA[server project exchange format]]></ac:plain-text-link-body></ac:link>. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.</p><p>In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="600"><ri:attachment ri:filename="project_exchange_options.png" /></ac:image></h6><p style="margin-left: 0.0in;"><span style="color: rgb(0,0,0);">The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.</span></p><p style="margin-left: 0.0in;"><br /></p><p style="margin-left: 0.0in;text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image><ri:attachment ri:filename="szip_project_import_performance.png" /></ac:image> <ac:image><ri:attachment ri:filename="szip_project_export_performance.png" /></ac:image> </span></p><h6 style="text-align: center;">Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).</h6><p><br /></p><h4>Model Patch Mechanism (Technology Preview)</h4><p><span style="color: rgb(0,0,0);">We introduce the technology preview of the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Patch - Technology preview" /><ac:plain-text-link-body><![CDATA[Model Patch mechanism]]></ac:plain-text-link-body></ac:link>, a more lightweight way to move model changes. Model Patch can help you:</span></p><ul><li><span style="color: rgb(0,0,0);">Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;</span></li><li><span style="color: rgb(0,0,0);">Transfer only a specific scope of model changes between disconnected teams instead of the entire model;</span></li><li>Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.</li></ul><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="model_patch_mechanism.jpg" /></ac:image></h6><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfdd0694-20ca-468f-858e-b8118a0d2206"><ac:parameter ac:name="">Power</ac:parameter></ac:structured-macro> </span>Power’By</h3><h4>New Features to Manage Used Projects</h4><p><span style="color: rgb(0,0,0);">We added new features that provide you with better capabilities to manage used projects in <strong>3D</strong>EXPERIENCE:</span></p><ul><li><span style="color: rgb(0,0,0);">Export packages as a new server project;</span></li><li><span style="color: rgb(0,0,0);">Move elements to/from used projects;</span></li><li><span style="color: rgb(0,0,0);">Import used projects.</span></li></ul><h4><span style="color: rgb(0,0,0);">Opening Projects in Read-Only Mode</span></h4><p><span style="color: rgb(0,0,0);">Beginning with version 2024x, you can open <strong>3D</strong>EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.</span></p><p style="text-align: center;"><ac:image ac:height="96"><ri:attachment ri:filename="3DEXPERIENCE_project_editing_disabled.jpg" /></ac:image></p><h6 style="text-align: center;">Notification informing the user that the <strong>3D</strong>EXPERIENCE project is read-only.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to Top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="da45258d-6386-4b80-af5a-54f24ceca0df"><ac:parameter ac:name="id">430554266</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong> <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link> </strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=137988166 space=CEA2024x version=4 -->
## PAGE 00003: Cameo Enterprise Architecture Documentation

- page_id: `137988166`
- space_key: `CEA2024x`
- source_url: https://docs.nomagic.com/spaces/CEA2024x/pages/137988166/Cameo+Enterprise+Architecture+Documentation
- version_number: 4
- version_date: `2023-09-22T12:58:38.084+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

1430502845

1430502848

1430502843

**Docs of other versions**

- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2022xR2']
- 
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2022x']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2021xR2']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2021xR1']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2021x']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA190SP4']

1430502847

This is the home page of Cameo Enterprise Architecture documentation.

Cameo Enterprise Architecture is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to **enterprise architecture** needs.

The documentation of Cameo Enterprise Architecture is a package that includes the documentation of these products and plugins:

**[CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024x']**

Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.

Type a search phrase...

**[CONFLUENCE_PAGE title='UPDM 2 Plugin Documentation' space='UPDM2P2024x']**

Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='UAF 1.2 Plugin Documentation' space='UAF12P2024x']**

Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024x']**

Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.

Type a search phrase...

**[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024x']**

Guides you through the import, export, and management of SysML requirements.

Type a search phrase...

**[CONFLUENCE_PAGE title='Concept Modeler Documentation' space='CCMP2024x']**

Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain.

Type a search phrase...

1302769756

##### Additional plugin

**[CONFLUENCE_PAGE title='Introduction to Cameo Simulation Toolkit' space='CST2024x']**

Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.

Type a search phrase...

##### Additional information

**[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024x']**

Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation.

Type a search phrase...

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="49da89cf-930a-42d6-93ee-2f9e7644bd43"><ac:parameter ac:name="id">1430502845</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="30c2055f-6f1d-4a38-baef-0c400c8a8d15"><ac:parameter ac:name="id">1430502848</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c3ddf0da-ce08-45b0-a86a-8a6e175a2265"><ac:parameter ac:name="id">1430502843</ac:parameter><ac:rich-text-body><p><strong>Docs of other versions</strong></p><ul><li><ac:link><ri:page ri:space-key="CEA2022xR2" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2022x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2022x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2022x" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2022x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2021xR2" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2021x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2021xR1" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2021x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2021x" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2021x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA190SP4" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 19.0 SP4]]></ac:plain-text-link-body></ac:link></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cf077ff2-3025-490c-8ac5-04131af9ca11"><ac:parameter ac:name="id">1430502847</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>This is the home page of Cameo Enterprise Architecture documentation.</p><p>Cameo Enterprise Architecture is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to <strong>enterprise architecture</strong> needs.</p><p>The documentation of Cameo Enterprise Architecture is a package that includes the documentation of these products and plugins:</p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="MagicDraw Documentation" /></ac:link></strong></p><p>Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="f967936d-9967-4d03-acfb-3bbda25ff786"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MD2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="UPDM2P2024x" ri:content-title="UPDM 2 Plugin Documentation" /></ac:link></strong></p><p>Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="cda62ca0-1a01-4b5e-af34-c99fae5e856d"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UPDM2P2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="UAF 1.2 Plugin Documentation" /></ac:link></strong></p><p>Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.</p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="4b6b3e8d-fee6-49cc-a7f9-3cef7259ed0c"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UAF12P2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="SysML Plugin Documentation" /></ac:link></strong></p><p>Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="6dcb808d-0e08-4204-9283-fbfab1d1c63a"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="SYSMLP2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /></ac:link></strong></p><p>Guides you through the import, export, and management of SysML requirements.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="6ce34cf5-e82b-4a63-8887-405dce315521"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CRMP2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="CCMP2024x" ri:content-title="Concept Modeler Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Concept Modeler Documentation]]></ac:plain-text-link-body></ac:link></strong></p><p><span style="color: rgb(62,63,64);">Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain. </span></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="7b7d7ac1-9d59-4d83-a4ff-b9bbfa8555dd"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CCMP2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b9ed7c1e-923f-499f-a271-c2585cbb6d8b"><ac:parameter ac:name="id">1302769756</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h3>Additional plugin</h3></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="CST2024x" ri:content-title="Introduction to Cameo Simulation Toolkit" /><ac:plain-text-link-body><![CDATA[Cameo Simulation Toolkit Documentation]]></ac:plain-text-link-body></ac:link></strong></p><p>Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.</p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="4d29e6ec-8db6-4cf7-952b-3776d53b1181"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CST2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><h3>Additional information</h3></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installation and licensing]]></ac:plain-text-link-body></ac:link></strong></p><p>Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation. </p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="5a5db465-c8bf-4bc9-8856-f296a23aaa35"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="IL2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=137988167 space=CEA2024x version=2 -->
## PAGE 00004: Cameo Enterprise Architecture Home Page

- page_id: `137988167`
- space_key: `CEA2024x`
- source_url: https://docs.nomagic.com/spaces/CEA2024x/pages/137988167/Cameo+Enterprise+Architecture+Home+Page
- version_number: 2
- version_date: `2024-01-26T14:54:39.986+01:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="6f6de204-e5e4-4f00-abf4-f05b04847656"><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Cameo Enterprise Architecture Documentation" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=137988307 space=CEA2024x version=4 -->
## PAGE 00005: Legal Notices

- page_id: `137988307`
- space_key: `CEA2024x`
- source_url: https://docs.nomagic.com/spaces/CEA2024x/pages/137988307/Legal+Notices
- version_number: 4
- version_date: `2024-04-19T13:34:44.311+02:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Legal Notices' space='MD2024x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="5883121e-bf11-4e22-95bc-1cf64cc48efa"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Legal Notices" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=137988306 space=CEA2024x version=3 -->
## PAGE 00006: Support

- page_id: `137988306`
- space_key: `CEA2024x`
- source_url: https://docs.nomagic.com/spaces/CEA2024x/pages/137988306/Support
- version_number: 3
- version_date: `2024-10-04T14:29:51.232+02:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Support' space='NMDOC']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="a8f81004-643a-4326-826c-13401bcb72df"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Support" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=137988304 space=CEA2024x version=1 -->
## PAGE 00007: Using UAF and UPDM2 plugins in Cameo Enterprise Architecture

- page_id: `137988304`
- space_key: `CEA2024x`
- source_url: https://docs.nomagic.com/spaces/CEA2024x/pages/137988304/Using+UAF+and+UPDM2+plugins+in+Cameo+Enterprise+Architecture
- version_number: 1
- version_date: `2023-09-22T12:48:35.664+02:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

1905569236

1905569247

1905569235

**On this page**

1905569237

##### Choosing the default plugin

Before the first startup of the Cameo Enterprise Architecture, you can set which plugin - UAF or UPDM2 - will be installed by default. If no changes are made, by default UAF plugin is installed.

To change the default plugin before the first startup

1. Go to the <cea_install_dir>\bin\ and open for editing the cameoea.properties file.
2. In the file, find the system property -Dstart.application.with.updm2.or.uaf.plugin=uaf
3. Change the uaf value to updm2 .
4. Save the file and start the Cameo Enterprise Architecture modeling tool.

In case you will decide to change the plugin later, see chapter [CONFLUENCE_PAGE title='Changing between UAF and UPDM 2 plugins' space='UAF12P2024x'] for information about how to do that.

##### Displaying which plugin is installed

You can choose to display the plugin name in brackets next to the Cameo Enterprise Architecture title in the modeling tool's title bar.

To display the installed plugin name near the modeling tool title

1. Go to the <cea_install_dir>\bin\ and open for editing the cameoea.properties file.
2. In the file, find the system property -Dadd.plugin.name.to.application.title\=false
3. Change the property value to true .
4. Save the file and start the Cameo Enterprise Architecture modeling tool.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="6e77571e-3d86-4467-bb90-939ee50b6890"><ac:parameter ac:name="id">1905569236</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d4476d95-eca4-40a4-a0b1-11e693e19e04"><ac:parameter ac:name="id">1905569247</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d081a48b-bb07-42c2-8a5c-22d8dd7f1861"><ac:parameter ac:name="id">1905569235</ac:parameter><ac:rich-text-body><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="45e56338-1c7d-4c50-a104-06124d9eae17" /></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8d554852-4e5e-4573-b6de-dc7f37703400"><ac:parameter ac:name="id">1905569237</ac:parameter><ac:rich-text-body><h3>Choosing the default plugin</h3><p>Before the first startup of the Cameo Enterprise Architecture, you can set which plugin - UAF or UPDM2 - will be installed by default. If no changes are made, by default UAF plugin is installed.</p><p><br /></p><p>To change the default plugin before the first startup</p><hr /><ol><li>Go to the &lt;cea_install_dir&gt;\bin\ and open for editing the <em>cameoea.properties</em> file.</li><li>In the file, find the system property <em>-Dstart.application.with.updm2.or.uaf.plugin=uaf</em></li><li>Change the <em>uaf</em> value to <em>updm2</em>.</li><li>Save the file and start the Cameo Enterprise Architecture modeling tool.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c93f7330-b046-4e85-be90-7075c3f9d206"><ac:rich-text-body><p>In case you will decide to change the plugin later, see chapter <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Changing between UAF and UPDM 2 plugins" /></ac:link> for information about how to do that.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Displaying which plugin is installed</h3><p>You can choose to display the plugin name in brackets next to the Cameo Enterprise Architecture title in the modeling tool's title bar. </p><p><br /></p><p>To display the installed plugin name near the modeling tool title</p><hr /><ol><li>Go to the &lt;cea_install_dir&gt;\bin\ and open for editing the <em>cameoea.properties</em> file.</li><li>In the file, find the system property <em>-Dadd.plugin.name.to.application.title\=false</em></li><li>Change the <em>property </em>value to <em>true</em>.</li><li>Save the file and start the Cameo Enterprise Architecture modeling tool.</li></ol><p><ac:image><ri:attachment ri:filename="plugin_name_in_title.png"><ri:page ri:space-key="CEA2024x" ri:content-title="Using UAF and UPDM2 plugins in Cameo Enterprise Architecture" /></ri:attachment></ac:image></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
