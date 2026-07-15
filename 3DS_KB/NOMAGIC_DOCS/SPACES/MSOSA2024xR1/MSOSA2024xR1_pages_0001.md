# NOMAGIC DOCUMENTATION SPACE: Magic Systems of Systems Architect 2024x Refresh1

<!--NOMAGIC_SPACE key=MSOSA2024xR1 chunk=1 -->

<!--NOMAGIC_PAGE id=170463040 space=MSOSA2024xR1 version=1 -->
## PAGE 00001: 2022x News for Developers

- page_id: `170463040`
- space_key: `MSOSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024xR1/pages/170463040/2022x+News+for+Developers
- version_number: 1
- version_date: `2024-01-31T11:24:25.550+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='2022x News for Developers' space='MD2022x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="7bca5887-f302-4e35-9131-f75eea6694e5"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="2022x News for Developers" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=170463041 space=MSOSA2024xR1 version=1 -->
## PAGE 00002: 2022x Version News

- page_id: `170463041`
- space_key: `MSOSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024xR1/pages/170463041/2022x+Version+News
- version_number: 1
- version_date: `2023-09-22T13:04:13.523+02:00`
- ancestors: 
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

753686899

INLINE

100.00002%

753686902

INLINE

753686898

INLINE

###### topMagic Systems of Systems Architect

Released: July 1,2022

In the 2022x release, we implemented the UAF 1.2 standard changes making the UAF 1.2 Profile fully supported in UAF, UAF Enterprise Architect, DoDAF, DoDAF 2.0, MODAF, NAF, and NAF 4.0 frameworks. Therefore, UAF 1.1 is no longer supported. Moreover, we adapted the partial import of the ArchiMate model from the open exchange file into the UAF 1.2 project. Finally, new DISR and UJTL library versions are now available.

This version alsointroduces several Instantiation Wizard improvements that will allow you to customize Instance Specifications before creating them, e.g., define their names and apply custom stereotypes. In addition, the plugin now supports the upcoming SysML 1.7 specification and provides an easier way to perform requirement verification in Requirement Tables.

The 2022x release launches the Data Markings and Classification Plugin for working with classified or sensitive data. This plugin allows system and software engineers, enterprise architects, and others to mark model elements to indicate different levels of classification or sensitivity.

For general modeling, this release presents diagram banner creation, improvements to Structured Expressions, extended filtering by Legend items functionality, an easier and safer way to manage secure connections, pre-bundled plugins, Product Line Engineering Plugin, and Project Merge Plugin improvements.

Beginning with this version, Reader is introduced as a modeling tool mode.

Additionally, collaborative modeling has been further enhanced with production-ready Global Element Usage Search functionality, allowing you to effectively analyze element modification impact in decomposed, highly interlinked models.

To download the latest version, see [Downloading installation files](https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files). For further information, check the product documentation.

243271308

INLINE

****

- 
- 
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

****

- 
- 
- 
- 
- 
- 

****

****

****

- 

753686901

INLINE

###### UAF 1.2 Features

##### Methods and Standards

Beginning with this version, the UAF 1.2 Plugin is available for use in production. The UAF 1.2 Profile is fully supported in UAF, UAF Enterprise Architect, DoDAF, DoDAF 2.0, MODAF, NAF, and NAF 4.0 frameworks. The following migration will be **necessary**:

- UPDM 2.1 to UAF 1.2. [CONFLUENCE_PAGE title='UPDM 2.1 migration to UAF 1.2' space='UAF12P2021xR2']>]]>
- UAF 1.0 to UAF 1.2. [CONFLUENCE_PAGE title='Migration from UAF 1.0 to UAF 1.2' space='UAF12P2022x']>]]>
- UAF 1.1 to UAF 1.2. [CONFLUENCE_PAGE title='Migration from UAF 1.1 to UAF 1.2' space='UAF12P2022x']>]]>

[CONFLUENCE_PAGE title='Migration from UAF 1.1 to UAF 1.2' space='UAF12P2022x']>]]>

**[IMAGE alt='' src='']**

**IMPORTANT!** The UAF 1.1 Plugin is no longer available.

###### [IMAGE alt='' src='']

###### Evolution of standards

##### UAF 1.2 support

Together with the UAF 1.2 Profile, the following changes (such as new aspects*, viewpoints**, diagrams, and tables) are implemented:

- Interaction Scenarios Aspect is renamed to Sequences Aspect.
- New Architecture Management Viewpoint:
  - New Architecture Management diagram.
  - Dictionary is a part of Architecture Management Viewpoint.
- New Motivation Aspect:
  - New Strategic Motivation diagram.
  - Requirements view specification is a part of Motivation Aspect for operational, personnel, resources viewpoints.
  - New Security Controls diagram.
- Improvements in Strategic Viewpoint:
  - Support of Value Streams.
  - Introduced Strategic Constraints, new Strategic Constraint table in UAF Framework, and new C8 Planning Assumption table in NAF 4.0 Framework.
  - Introduced Strategic Exchanges.
  - New Strategic Processes diagram.
- Improvements in Services Viewpoint:
  - Introduced Service Contract constraints.
  - Introduced Service Exchanges.
  - Service Association stereotype is introduced and applied to associations between Services.
  - Resource Service introduced to model technical services, such as web services.
- Improvements in Security Viewpoint:
  - Risks as a cross-cutting construct bringing new Risks diagram available in most viewpoints, under Parameters Aspect.
  - New Security Constraints table.
- Implementation Matrix enhanced and adapted to UAF 1.2 Profile.
- Support Personnel Traceability.
  - Functions to Operational Activities and Actual Responsible Resources to Actual Project Mapping matrices are available in Personnel Traceability View Specification.
- Improvements in Information Aspect:
  - Dictionary is a part of Information Aspect.
  - Introduced Strategic Information element and new Strategic Information diagram.

***Aspects** were previously known as model kinds.

****Viewpoints** were previously known as domains.

###### [IMAGE alt='' src='']

###### UAF 1.2 grid. 
(Click the image to enlarge)

##### Library Support

New DISR and UJTL library versions are now available:

- UJTL (20220215)
- DISR (20211110)

You can choose the library version when creating a new project. [CONFLUENCE_PAGE title='Using libraries' space='UAF12P2022x']>]]>

##### ArchiMate Import (Technology preview)

In this version, we continued developing the import of the ArchiMate model from the open exchange file into the UAF project. The imported element mapping is still only partial, but adapted to the UAF 1.2 profile. The mapping of ArchiMate 3.1 to UAF 1.2 approach is based on the NATO Architecture Framework.[CONFLUENCE_PAGE title='Importing from ArchiMate' space='UAF12P2022x']>]]>

[IMAGE alt='' src='']

244508097

INLINE

###### SysML Features

##### Instantiation Wizard Improvements

SysML Plugin 2022x brings several improvements in automatic instance creation using the Instantiation Wizard. You can now save time by specifying the names and custom stereotypes of Instance Specifications while creating them. We have also introduced new UI options that will help you select the elements to be instantiated quicker than before. Last but not least, the Instantiation Wizard performance has been improved for even better user experience.

[IMAGE alt='' src='']

###### Instantiation Wizard improvements.

##### SysML 1.7 Support

As of version 2022x, the SysML Plugin supports the upcoming SysML 1.7 specification which brings the following changes:

- The QUDV model library for owned operations has been updated. The *dependsOnUnits* owned operation has been redefined with the *dependsOnUnits*operation owned by *Unit* for the following blocks: *SimpleUnit*, *DerivedUnit*, and *ConversionBasedUnit.* The *dependsOnQuantityKinds*owned operation for the *SimpleQuanitityKind* block has been redefined with the *dependsOnQuantityKinds* operation owned by *QuantityKind*.
- In the QUDV model library, the multiplicity of Prefix::Symbol has been changed from [1] to [0..1] .
- A new symbol property allows renaming allocation compartments according to the SysML 1.7 standard. The "allocatedTo" compartment will be renamed to "allocatedToElements", and the "allocatedFrom" compartment to"allocatedElements".

##### Easier Requirement Verification

Performing automated Requirements verification in Requirement Tables is now easier as verification-specific columns and Legend are auto-displayed once the verification context - block or instance - is assigned.

256630726

INLINE

###### Data Markings and Classification Plugin

The 2022x version introduces a new product: **Data Markings and Classification Plugin**. This plugin is designed for system and software engineers, enterprise architects, business analysts, and others who work with classified or sensitive data. It provides compatibility with the DoD Manual 5200.01 Volume 2 specification. Using the **Data Markings and Classification Plugin**, you can specifically mark your model elements to indicate different levels of classification or sensitivity. The plugin allows you to:

- Use predefined DoD data markings and/or create custom ones. [ATTACHMENT filename='create_use_dod.png']
- Access data markings via diagram (also symbol, table row, etc.) and element shortcut menus, as well as their specification windows. [ATTACHMENT filename='access_data_markings.png']
- Add data markings to various elements (relationships, blocks, packages, ports, operations, properties, comments, etc.) of your project. [ATTACHMENT filename='diagrams_elements_and_containment_tree.png']

To see it in action, watch the following demo.

700349

[CONFLUENCE_PAGE title='Data Markings and Classification Plugin' space='DMP2022x']>]]>

272319258

INLINE

###### Performance Improvements

##### Client-side Performance Improvements

- **Refactoring Elements**. Converting an element from one type to another is two to four times faster than in 2021x Refresh2. 
[IMAGE alt='' src=''] A chart comparing the conversion of the Block to Signal operation in Refresh2 and 2022x.
- **Element Auto-Numbering**. Every time the diagram is opened, the active validation for numbering is triggered to maintain the uniqueness of displayed model elements that are numbered (e.g., requirements). The uniqueness check is now significantly faster when opening diagrams (including tables, matrices, etc.) containing up to 1000 numbered elements. 
 
[IMAGE alt='' src=''] A chart comparing the time it takes to execute element number uniqueness check in a SysML (0.5M) project with 60k requirements in 2021x Refresh2 and 2022x.

- Dependency Matrices . Further performance improvements have been introduced to matrix building; it is up to twice as fast compared to 2021x Refresh2.

###### [IMAGE alt='' src='']A chart comparing the SysML Allocation Matrix building time in 2021x Refresh2 and 2022x projects.

##### Limits of Diagram Export as Image

You can now specify dimension limits to prevent extremely large diagrams from being exported as images. Additionally, you can set a time limit for table and matrix building to skip image export. This is especially handy when exporting hundreds of diagrams, including large ones, i.e., generating reports and publishing models to Cameo Collaborator is significantly faster and smoother as the diagrams exceeding the limits are exported as cropped.

[IMAGE alt='' src='']

###### The diagram is cropped upon export based on Image Export options.

[CONFLUENCE_PAGE title='Diagram image export' space='MD2022x']> ]]>

##### Teamwork Cloud-related Performance Improvements

- Element History and Content History performance improvements. In version 2022x, we present major performance improvements of Element History and Content History, two of the most widely used features related to project history. Depending on the size and type of a project, the initial history results should now appear 3 to 10 times faster compared to our latest 2021x Refresh2 release.

[IMAGE alt='' src='']

###### A chart representing the improved Element History performance in version 2022x as compared to 2021x Refresh2.

[IMAGE alt='' src='']

###### A chart representing the improved Content History performance in version 2022x as compared to 2021x Refresh2.

243174490

INLINE

###### Modeling and Infrastructure

##### Diagram Banners

From now on, you can create diagram banners, such as headers and/or footers, to display important information on the diagram. The diagram banners can be created for all diagram types, such as tables, matrices, or maps. Upon diagram image export, the diagram banners are also included in the exported image.

[IMAGE alt='' src='']

###### A diagram with a diagram banner displayed at the bottom of the diagram pane.

[CONFLUENCE_PAGE title='Diagram banners' space='MD2022x']>]]>

##### Using Structured Expressions in a More Intuitive Way

Modelers rely on Structured Expressions to perform one of the basic tasks: querying the model. Building Structured Expressions is now easier and more efficient:

- The smart result type update lets you forget about manually adjusting the type for columns or derived properties:

[IMAGE alt='' src='']

- The Unique check box allows you to control whether value duplicates should be taken into account using Simple and Metachain Navigation operations: 
 
[IMAGE alt='' src='']

Additionally, there is enriched learning material that includes detailed steps for completing the most common model querying tasks. [CONFLUENCE_PAGE title='Case Studies for Querying the Model' space='MD2022x']>]]>

[CONFLUENCE_PAGE title='Specifying criteria for querying model' space='MD2022x']Learn more about Structured Expressions >>

##### Pre-bundled Plugins

Installing plugins has now become easier. All available plugins, both commercial and no-cost, are now pre-bundled together with the installation files and automatically added to the **Resource/Plugin Manager**.

[IMAGE alt='' src='']

###### All available plugins are accessible via the pre-bundled *core.rdzip* file in the Resource/Plugin Manager.

Learn more about plugin installation for CATIA Magic portfolio products >>

[CONFLUENCE_PAGE title='Installing plugins' space='MD2022x']>]]>

##### Hide Results of Legend Items

You can now select the filtering preference (show or hide) to either display or hide the results of a Legend item.

[IMAGE alt='' src='']

###### Filtering a diagram by the selected Legend item *Comment* with the filtering preference set to *Hide*.

[CONFLUENCE_PAGE title='Filtering by Legend items' space='MD2022x']>]]>

##### Easier and Safer Way to Manage Secure Connections

With the release of version 2022x, we have consolidated server certificate management for all secure network connections made on the client-side. Now a new Server Certificates Management tool handles all secure connections supported by the client. In addition to automatically adding existing certificates from the operating system, the tool allows you to add or remove certificates without running complex commands via the command-line interface. You can simply use the Environment Options dialog in your modeling tool to:

- See the list of all currently added certificates and their details.
- Add new certificates or certificate storage trusted by the current user or by all users.
- Manage all added certificates.

[IMAGE alt='' src='']

###### Managing secure connections.

##### Other Improvements

- The Product Line Engineering Plugin is now split into two plugins: the Variability Core Plugin , which provides technical mechanisms and functions for various PLE and Data Marking activities, and the Product Line Engineering Plugin , which provides Model-Based Product Line Engineering method support for the user.
- The Project Merge Plugin is no longer pre-installed, so you will not be receiving license expiration notifications if the plugin is not used. In addition, you no longer need the Project Merge Plugin to execute project comparison, element and content history review, as this functionality is now part of the built-in Merge Core Plugin . The Project Merge Plugin is now only required for project merging functionality.
- A new UML Invalid Redefinition validation rule has been introduced to the UML correctness constraints validation suite. It checks whether a property redefines the inherited property of the owner classifier. [CONFLUENCE_PAGE title='UML validation rules' space='MD2022x']>]]>
- You now have the option to use a custom encryption algorithm instead of the default one with the **Model Obfuscation Plugin**. [CONFLUENCE_PAGE title='Model Obfuscation' space='MD2022x']>]]>
- Now you can choose whether or not to display the Presentation Mode icon in the status bar.
- From now on, when you create an Enumeration Literal, a Slot is created for it with the default value if the Slot's Defining Feature has one. [ATTACHMENT filename='slot_with_value_for_enumeration_literal.png']
- Now there is an easy way of selecting model elements in the Containment tree from the Criteria area of a Table, Matrix, and Map. [ATTACHMENT filename='select_model_elements_in_the_Containment_tree.png']

1292342252

INLINE

###### Discontinued Products

Beginning with the 2022x version, support of the following products is discontinued:

- CSV Import Plugin . [CONFLUENCE_PAGE title='Sync with Excel or CSV files' space='MD2022x'] or [CONFLUENCE_PAGE title='Importing data from Excel or CSV files' space='MD2022x'] features will be replacing the CSV Import Plugin.
- MagicDraw Professional Java Edition Floating License and MagicDraw Professional Java Edition Seat License. Java Code Engineering will be available in the modeling tool Enterprise editions. For customers with active software assurance (ALC), the upgrade to the Enterprise edition will come at no cost.
- JRuby scripting language . Any previously used scripts written in JRuby need to be rewritten in a different built-in scripting language. Otherwise, you can [CONFLUENCE_PAGE title='Adding JRuby and installing Gems' space='MD2022x'] to continue using the existing JRuby scripts.
- Magic Teamcenter Connector . Starting with version 2022x, Magic Teamcenter Connector is no longer available. You may continue to use your perpetual license of the product in accordance with the terms of your license agreement. The support for the product will be provided until the end of your current maintenance support subscription.

1292358024

INLINE

###### Reader Mode

Starting with this version, **Reader**is introduced as the modeling tool mode. [CONFLUENCE_PAGE title='Reader Mode activation' space='NMDOC']>]]>

243713866

INLINE

###### Collaboration

##### Global Element Usage Search

The 2022x version includes the release of production-ready **Global Element Usage Search** functionality. It allows you to search for usages of an element that you want to modify or delete. Depending on the [CONFLUENCE_PAGE title='Creating indexing configurations' space='TWCloud2022x'], projects that use the element in question can be returned either from the entire Teamwork Cloud repository or the selected custom indexed scope. This minimizes the probability of unexpected Recovered Elements appearing when updating the Used Project versions.

[IMAGE alt='' src='']

###### Searching for element usages within the Teamwork Cloud repository.

[CONFLUENCE_PAGE title='Global element usage search' space='MD2022x']>]]>

430554266

INLINE

**[CONFLUENCE_PAGE title='2022x Version News' space='NMDOC']>]]>**

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ac060d11-24bb-43ee-828b-bfae5b72f6eb"><ac:parameter ac:name="id">753686899</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d04429d1-af39-4fcc-95f9-34e91a0b1fb5"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">753686902</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="52ee565b-7c7f-4b63-9021-994a0965d636"><ac:parameter ac:name="id">753686898</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5 style="text-align: center;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fd7d672f-fb01-4e70-8982-8ff70256549a"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro>Magic Systems of Systems Architect</h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released: July 1<span style="color: rgb(128,128,128);">,</span><span style="color: rgb(128,128,128);"> 2022</span> </span></p><p><br /></p><p><span style="color: rgb(62,63,64);">In the 2022x release, <span>we implemented the UAF 1.2 standard changes making the UAF 1.2 Profile fully supported in UAF, UAF Enterprise Architect, DoDAF, DoDAF 2.0, MODAF, NAF, and NAF 4.0 frameworks. Therefore, UAF 1.1 is no longer supported. Moreover, we adapted the partial import of the ArchiMate model from the open exchange file into the UAF 1.2 project. Finally, new DISR and UJTL library versions are now available</span>.</span></p><p><span style="color: rgb(62,63,64);">This version also </span><span>introduces several Instantiation Wizard improvements that will allow you to customize Instance Specifications before creating them, e.g., define their names and apply custom stereotypes. In addition, the plugin now supports the upcoming SysML 1.7 specification and provides an easier way to perform requirement verification in Requirement Tables.</span></p><p>The 2022x release launches the Data Markings and Classification Plugin for working with classified or sensitive data. This plugin allows system and software engineers, enterprise architects, and others to mark model elements to indicate different levels of classification or sensitivity.</p><p>For general modeling, this release presents diagram banner creation, improvements to Structured Expressions, extended filtering by Legend items functionality, an easier and safer way to manage secure connections, pre-bundled plugins, Product Line Engineering Plugin, and Project Merge Plugin improvements.</p><p>Beginning with this version, Reader is introduced as a modeling tool mode.</p><p>Additionally, collaborative modeling has been further enhanced with production-ready Global Element Usage Search functionality, allowing you to effectively analyze element modification impact in decomposed, highly interlinked models.</p><p>To download the latest version, see <a href="https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files">Downloading installation files</a>. For further information, check the product documentation.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="3416750c-69ed-479b-b795-b595a8c79a21"><ac:parameter ac:name="id">243271308</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong><ac:link ac:anchor="UAF Features" /></strong></p><ul><li><ac:link ac:anchor="Methods and Standards" /></li><li><ac:link ac:anchor="UAF 1.2 support" /></li><li><ac:link ac:anchor="Library Support" /></li><li><ac:link ac:anchor="ArchiMate Import (Technology preview)" /></li></ul><p><strong><ac:link ac:anchor="SysML Features" /></strong></p><ul><li><ac:link ac:anchor="Instantiation Wizard Improvements" /></li><li><ac:link ac:anchor="SysML 1.7 Support" /></li><li><ac:link ac:anchor="Easier Requirement Verification" /></li></ul><p><strong><ac:link ac:anchor="Data Markings and Classification Plugin" /></strong></p></ac:layout-cell><ac:layout-cell><p><strong><ac:link ac:anchor="Performance Improvements" /></strong></p><ul><li><ac:link ac:anchor="Client-side Performance Improvements" /></li><li><ac:link ac:anchor="Limits of Diagram Export as Image" /></li><li><ac:link ac:anchor="Teamwork Cloud-related Performance Improvements" /><strong><br class="_mce_tagged_br" /></strong></li></ul><p><strong><ac:link ac:anchor="Modeling and Infrastructure" /></strong></p><ul><li><ac:link ac:anchor="Diagram Banners" /></li><li><ac:link ac:anchor="Using Structured Expressions in a More Intuitive Way" /></li><li><ac:link ac:anchor="Pre-bundled Plugins" /></li><li><ac:link ac:anchor="Hide Results of Legend Items" /></li><li><ac:link ac:anchor="Easier and Safer Way to Manage Secure Connections" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul></ac:layout-cell><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Discontinued Products" /></strong></p><p><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Reader Mode" /></strong></p><p><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Collaboration" /></strong></p><ul><li><ac:link ac:anchor="Global Element Usage Search" /></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="219ce1f1-83f8-4bff-aec2-7c3b84a1a780"><ac:parameter ac:name="id">753686901</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5>UAF 1.2 Features</h5><h3>Methods and Standards</h3><p><span style="color: rgb(62,63,64);">Beginning with this version, the UAF 1.2 Plugin is available for use in production. The UAF 1.2 Profile is fully supported in UAF, UAF Enterprise Architect, DoDAF, DoDAF 2.0, MODAF, NAF, and NAF 4.0 frameworks</span>. The following migration will be <strong><span style="color: rgb(255,0,0);">necessary</span></strong>:</p><ul><li>UPDM 2.1 to UAF 1.2. <ac:link><ri:page ri:space-key="UAF12P2021xR2" ri:content-title="UPDM 2.1 migration to UAF 1.2" /><ac:plain-text-link-body><![CDATA[Learn more about the changes >>]]></ac:plain-text-link-body></ac:link></li><li>UAF 1.0 to UAF 1.2. <ac:link><ri:page ri:space-key="UAF12P2022x" ri:content-title="Migration from UAF 1.0 to UAF 1.2" /><ac:plain-text-link-body><![CDATA[Learn more about the changes >>]]></ac:plain-text-link-body></ac:link></li><li><span style="color: rgb(62,63,64);">UAF 1.1 to UAF 1.2. <ac:link><ri:page ri:space-key="UAF12P2022x" ri:content-title="Migration from UAF 1.1 to UAF 1.2" /><ac:plain-text-link-body><![CDATA[Learn more about the changes >>]]></ac:plain-text-link-body></ac:link></span></li></ul><p><ac:link><ri:page ri:space-key="UAF12P2022x" ri:content-title="Migration from UAF 1.1 to UAF 1.2" /><ac:plain-text-link-body><![CDATA[Learn more about the duration of project migration >>]]></ac:plain-text-link-body></ac:link></p><p><span style="color: rgb(255,0,0);"><strong><ac:image ac:align="center" ac:width="1003"><ri:attachment ri:filename="migration_duration.png" /></ac:image><br /></strong></span></p><p><span style="color: rgb(255,0,0);"><strong>IMPORTANT!</strong></span> The UAF 1.1 Plugin is no longer available.</p><h6 style="text-align: center;"><ac:image ac:width="800"><ri:attachment ri:filename="cea-evo-19-22x - plugin.png" /></ac:image></h6><h6 style="text-align: center;"><span style="color: rgb(128,128,128);">Evolution of standards</span></h6><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><h3>UAF 1.2 support</h3><p>Together with the UAF 1.2 Profile, the following changes (such as new aspects*, viewpoints**, diagrams, and tables) are implemented:</p><ul><li>Interaction Scenarios Aspect is renamed to Sequences Aspect.</li><li>New Architecture Management Viewpoint:<ul><li>New Architecture Management diagram.</li><li>Dictionary is a part of Architecture Management Viewpoint.</li></ul></li><li>New Motivation Aspect:<ul><li>New Strategic Motivation diagram.</li><li>Requirements view specification is a part of Motivation Aspect for operational, personnel, resources viewpoints.</li><li>New Security Controls diagram.</li></ul></li><li>Improvements in Strategic Viewpoint:<ul><li>Support of Value Streams.</li><li>Introduced Strategic Constraints, new Strategic Constraint table in UAF Framework, and new C8 Planning Assumption table in NAF 4.0 Framework.</li><li>Introduced Strategic Exchanges.</li><li>New Strategic Processes diagram.</li></ul></li><li>Improvements in Services Viewpoint:<ul><li>Introduced Service Contract constraints.</li><li>Introduced Service Exchanges.</li><li>Service Association stereotype is introduced and applied to associations between Services.</li><li>Resource Service introduced to model technical services, such as web services. </li></ul></li><li>Improvements in Security Viewpoint:<br /><ul><li>Risks as a cross-cutting construct bringing new Risks diagram available in most viewpoints, under Parameters Aspect.</li><li>New Security Constraints table.</li></ul></li><li>Implementation Matrix enhanced and adapted to UAF 1.2 Profile.</li><li>Support Personnel Traceability.<ul><li>Functions to Operational Activities and Actual Responsible  Resources to Actual Project Mapping matrices are available in Personnel Traceability View Specification.</li></ul></li><li>Improvements in Information Aspect:<ul><li>Dictionary is a part of Information Aspect.</li><li>Introduced Strategic Information element and new Strategic Information diagram.</li></ul></li></ul><hr /><p><strong>*Aspects</strong> were previously known as model kinds.</p><p><strong>**Viewpoints</strong> were previously known as domains.</p></ac:layout-cell><ac:layout-cell><h6 style="text-align: center;"><ac:image ac:align="center" ac:height="250"><ri:attachment ri:filename="UAF _1_2 grid Last.png" /></ac:image></h6><h6 style="text-align: center;">UAF 1.2 grid.<br />(Click the image to enlarge)</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Library Support</h3><p>New DISR and UJTL library versions are now available:</p><ul><li>UJTL (20220215)</li><li>DISR (20211110)</li></ul><p><span style="color: rgb(62,63,64);">You can choose the library version when creating a new project. <ac:link><ri:page ri:space-key="UAF12P2022x" ri:content-title="Using libraries" /><ac:plain-text-link-body><![CDATA[Learn more about using libraries >>]]></ac:plain-text-link-body></ac:link></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>ArchiMate Import (Technology preview)</h3><p>In this version, we continued developing the <span style="color: rgb(62,63,64);">import of the ArchiMate model from the open exchange file into the UAF project. The imported element mapping is still only partial, but adapted to the UAF 1.2 profile. The mapping of ArchiMate 3.1 to UAF 1.2 approach is based on the NATO Architecture Framework. </span><ac:link><ri:page ri:space-key="UAF12P2022x" ri:content-title="Importing from ArchiMate" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center" ac:width="1040"><ri:attachment ri:filename="ArchiMate 3.1 to UAF 1.2 horizontal-white-background.jpg" /></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="a672970d-0b10-4a72-a92c-25e7fccc5e0d"><ac:parameter ac:name="id">244508097</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>SysML Features</h5><h3>Instantiation Wizard Improvements</h3><p>SysML Plugin 2022x brings several improvements in automatic instance creation using the Instantiation Wizard. You can now save time by specifying the names and custom stereotypes of Instance Specifications while creating them. We have also introduced new UI options that will help you select the elements to be instantiated quicker than before. Last but not least, the Instantiation Wizard performance has been improved for even better user experience.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="automatic_instanciation_wizard.png" /></ac:image></p><h6 style="text-align: center;">Instantiation Wizard improvements.</h6><h3>SysML 1.7 Support</h3><p><span style="color: rgb(62,63,64);">As of version 2022x, the SysML Plugin supports the upcoming SysML 1.7 specification which brings the following changes:</span></p><ul><li><p>The QUDV model library for owned operations has been updated. The <em>dependsOnUnits</em> owned operation has been redefined with the <em>dependsOnUnits </em>operation owned by <em>Unit</em> for the following blocks: <em>SimpleUnit</em>, <em>DerivedUnit</em>, and <em>ConversionBasedUnit.</em> The <em>dependsOnQuantityKinds </em>owned operation for the <em>SimpleQuanitityKind</em> block has been redefined with the <em>dependsOnQuantityKinds</em> operation owned by <em>QuantityKind</em>.</p></li><li>In the QUDV model library, the multiplicity of <em>Prefix::Symbol</em> has been changed from <span class="error">[1]</span> to <span class="error">[0..1]</span>.</li><li>A new symbol property allows renaming allocation compartments according to the SysML 1.7 standard. The &quot;allocatedTo&quot; compartment will be renamed to &quot;allocatedToElements&quot;, and the &quot;allocatedFrom&quot; compartment to&quot;allocatedElements&quot;.</li></ul><h3><br />Easier Requirement Verification</h3><p>Performing automated Requirements verification in Requirement Tables is now easier as verification-specific columns and Legend are auto-displayed once the verification context - block or instance - is assigned.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="7bd9a9a5-ef07-41f4-a700-149d04080047"><ac:parameter ac:name="id">256630726</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Data Markings and Classification Plugin</h5><p>The 2022x version introduces a new product: <strong>Data Markings and Classification Plugin</strong>. This plugin is designed for system and software engineers, enterprise architects, business analysts, and others who work with classified or sensitive data. It provides compatibility with the DoD Manual 5200.01 Volume 2 specification. Using the <strong>Data Markings and Classification Plugin</strong>, you can specifically mark your model elements to indicate different levels of classification <span style="color: rgb(62,63,64);">or sensitivity</span>. The plugin allows you to:</p><ul><li><p>Use predefined DoD data markings and/or create custom ones.</p><ac:image ac:align="center"><ri:attachment ri:filename="create_use_dod.png" /></ac:image></li><li><p>Access data markings via diagram (also symbol, table row, etc.) and element shortcut menus, as well as their specification windows.</p><ac:image ac:align="center"><ri:attachment ri:filename="access_data_markings.png" /></ac:image></li><li><p>Add data markings to various elements (relationships, blocks, packages, ports, operations, properties, comments, etc.) of your project.</p><ac:image ac:align="center"><ri:attachment ri:filename="diagrams_elements_and_containment_tree.png" /></ac:image></li></ul><p><br /></p><p>To see it in action, watch the following demo.</p><p style="text-align: center;"><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="f9cdd251-fd0c-47f0-9e42-f9683383490e"><ac:parameter ac:name="width">700</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=OBvX40zgbqc&amp;t=1s" /></ac:parameter><ac:parameter ac:name="height">349</ac:parameter></ac:structured-macro></p><p><br /></p><p><ac:link><ri:page ri:space-key="DMP2022x" ri:content-title="Data Markings and Classification Plugin" /><ac:plain-text-link-body><![CDATA[Learn more about the Data Markings and Classification Plugin >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="77c02728-d48d-4941-bb36-35af3cdb8a0f"><ac:parameter ac:name="id">272319258</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5 style="margin-left: 0.0in;">Performance Improvements</h5><h3>Client-side Performance Improvements</h3><ul><li><p><strong>Refactoring Elements</strong>. Converting an element from one type to another is two to four times faster than in 2021x Refresh2.<br /><ac:image ac:align="center"><ri:attachment ri:filename="converting_block_to_signal_chart.png" /></ac:image></p><h6 style="text-align: center;"><span>A chart comparing the conversion of the Block to Signal operation in Refresh2 and 2022x.</span></h6></li><li><p><strong>Element Auto-Numbering</strong>. Every time the diagram is opened, the active validation for numbering is triggered to maintain the uniqueness of displayed model elements that are numbered (e.g., requirements). The uniqueness check is now significantly faster when opening diagrams (including tables, matrices, etc.) containing up to 1000 numbered elements.<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="element_number_uniqueness_check_chart.png" /></ac:image></p><h6 style="text-align: center;">A chart comparing the time it takes to execute element number uniqueness check in a SysML (0.5M) project with 60k requirements in 2021x Refresh2 and 2022x.</h6></li></ul><ul><li><strong>Dependency Matrices</strong>. <span>Further performance improvements have been introduced to matrix building; it is up to twice as fast compared to 2021x Refresh2.</span></li></ul><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="matrix_building_time.png" /></ac:image>A chart comparing the SysML Allocation Matrix building time in 2021x Refresh2 and 2022x projects.</h6><h3>Limits of Diagram Export as Image</h3><p>You can now specify dimension limits to prevent extremely large diagrams from being exported as images. Additionally, you can set a time limit for table and matrix building to skip image export. This is especially handy when exporting hundreds of diagrams, including large ones, i.e., generating reports and publishing models to Cameo Collaborator is significantly faster and smoother as the diagrams exceeding the limits are exported as cropped.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="diagram_export_options_example.png" /></ac:image></p><h6 style="text-align: center;">The diagram is cropped upon export based on Image Export options.</h6><p><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Diagram image export" /><ac:plain-text-link-body><![CDATA[Learn more about diagram export options >> ]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Teamwork Cloud-related Performance Improvements</h3><ul><li><strong>Element History</strong> and <strong>Content History</strong> performance improvements. In version 2022x, we present major performance improvements of Element History and Content History, two of the most widely used features related to project history. Depending on the size and type of a project, the initial history results should now appear 3 to 10 times faster compared to our latest 2021x Refresh2 release.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="element_history_chart.png" /></ac:image></p><h6 style="text-align: center;">A chart representing the improved Element History performance in version 2022x as compared to 2021x Refresh2.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="content_history_chart.png" /></ac:image></p><h6 style="text-align: center;"><span>A chart representing the improved Content History performance in version 2022x as compared to 2021x Refresh2.</span></h6><p style="text-align: right;"><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9e3c4365-9014-4b61-a338-ea7eabec915c"><ac:parameter ac:name="id">243174490</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5>Modeling and Infrastructure</h5><h3>Diagram Banners</h3><p>From now on, you can create diagram banners, such as headers and/or footers, to display important information on the diagram. The diagram banners can be created for all diagram types, such as tables, matrices, or maps. Upon diagram image export, the diagram banners are also included in the exported image. </p><p><ac:image ac:align="center"><ri:attachment ri:filename="diagram_banner_example_2.png" /></ac:image></p><h6 style="text-align: center;">A diagram with a diagram banner displayed at the bottom of the diagram pane.</h6><p><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Diagram banners" /><ac:plain-text-link-body><![CDATA[Learn more about diagram banners >>]]></ac:plain-text-link-body></ac:link></p><h3><span>Using Structured Expressions in a More Intuitive Way</span></h3><p>Modelers rely on Structured Expressions to perform one of the basic tasks: querying the model. Building Structured Expressions is now easier and more efficient:</p><ul><li class="p1">The smart result type update lets you forget about manually adjusting the type for columns or derived properties:</li></ul><p class="p1"><ac:image ac:align="center"><ri:attachment ri:filename="smart_result_type.png" /></ac:image></p><p><br /></p><ul><ul><li><p class="p1">The Property Test operation now supports more testing properties. In addition to checking properties' primitive values (e.g., string, boolean, integer), you can also test properties whose values are model elements:<span> <br /><ac:image ac:align="center"><ri:attachment ri:filename="property_test_operation.png" /></ac:image> <br /></span></p></li><li><p class="p1">Apply the same type relation criterion with different properties multiple times: <br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="same_type_relation_criterion.png" /></ac:image></p></li></ul></ul><p><br /></p><ul><li><p>The Unique check box allows you to control whether value duplicates should be taken into account using Simple and Metachain Navigation operations:<br /><br /><ac:image ac:align="center"><ri:attachment ri:filename="Manipulating_with_non-unique_values.png" /></ac:image></p></li></ul><p><br /></p><p class="p1">Additionally, there is enriched learning material that includes detailed steps for completing the most common model querying tasks. <ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Case Studies for Querying the Model" /><ac:plain-text-link-body><![CDATA[Learn more on the Case Studies for Querying the Model page >>]]></ac:plain-text-link-body></ac:link></p><p><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Specifying criteria for querying model" /><ac:link-body> <br />Learn more about Structured Expressions &gt;&gt;</ac:link-body></ac:link></p><h3>Pre-bundled Plugins</h3><p>Installing plugins has now become easier. All available plugins, both commercial and no-cost, are now pre-bundled together with the installation files and automatically added to the <strong>Resource/Plugin Manager</strong>.</p><p style="text-align: center;"><span class="confluence-embedded-file-wrapper"> <ac:image><ri:attachment ri:filename="resource_manager_core_file.png" /></ac:image> </span></p><h6 style="text-align: center;">All available plugins are accessible via the pre-bundled <em>core.rdzip</em> file in the Resource/Plugin Manager.</h6><p>Learn more about plugin installation for CATIA Magic portfolio products &gt;&gt;</p><p><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Installing plugins" /><ac:plain-text-link-body><![CDATA[Learn more about plugin installation for No Magic portfolio products >>]]></ac:plain-text-link-body></ac:link></p><h3>Hide Results of Legend Items </h3><p>You can now select the filtering preference (show or hide) to either display or hide the results of a Legend item.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="filtering_preference_hide.png" /></ac:image></p><h6 style="text-align: center;">Filtering a diagram by the selected Legend item <em> Comment </em> with the filtering preference set to <em> Hide</em>.</h6><p><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Filtering by Legend items" /><ac:plain-text-link-body><![CDATA[Learn more about filtering by Legend items >>]]></ac:plain-text-link-body></ac:link></p><h3>Easier and Safer Way to Manage Secure Connections</h3><p>With the release of version 2022x, we have consolidated server certificate management for all secure network connections made on the client-side. Now a new Server Certificates Management tool handles all secure connections supported by the client. In addition to automatically adding existing certificates from the operating system, the tool allows you to add or remove certificates without running complex commands via the command-line interface. You can simply use the Environment Options dialog in your modeling tool to:</p><ul><li>See the list of all currently added certificates and their details.</li><li>Add new certificates or certificate storage trusted by the current user or by all users.</li><li>Manage all added certificates.</li></ul><p style="text-align: center;"><ac:image><ri:attachment ri:filename="certificate_manager.jpg" /></ac:image></p><h6 style="text-align: center;">Managing secure connections.</h6><h3>Other Improvements</h3><ul><li>The <strong>Product Line Engineering Plugin</strong> is now split into two plugins: the <strong>Variability Core Plugin</strong>, which provides technical mechanisms and functions for various PLE and Data Marking activities, and the <strong>Product Line Engineering Plugin</strong>, which provides Model-Based Product Line Engineering method support for the user.</li><li>The <strong>Project Merge Plugin</strong> is no longer pre-installed, so you will not be receiving license expiration notifications if the plugin is not used. In addition, you no longer need the <strong>Project Merge Plugin</strong> to execute project comparison, element and content history review, as this functionality is now part of the built-in <strong>Merge Core Plugin</strong>. The <strong>Project Merge Plugin</strong> is now only required for project merging functionality.</li><li>A new UML <strong>Invalid Redefinition</strong> validation rule has been introduced to the UML correctness constraints validation suite. It checks whether a property redefines the inherited property of the owner classifier. <ac:link><ri:page ri:space-key="MD2022x" ri:content-title="UML validation rules" /><ac:plain-text-link-body><![CDATA[Learn more about UML validation rules >>]]></ac:plain-text-link-body></ac:link></li><li><p>You now have the option to use a custom encryption algorithm instead of the default one with the <strong>Model Obfuscation Plugin</strong>. <ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Model Obfuscation" /><ac:plain-text-link-body><![CDATA[Learn more about Model Obfuscation >>]]></ac:plain-text-link-body></ac:link></p></li><li><p>Now you can choose whether or not to display the Presentation Mode icon in the status bar.</p></li><li>From now on, when you create an Enumeration Literal, a Slot is created for it with the default value if the Slot's Defining Feature has one.<br /><ac:image><ri:attachment ri:filename="slot_with_value_for_enumeration_literal.png" /></ac:image></li><li>Now there is an easy way of selecting model elements in the Containment tree from the Criteria area of a Table, Matrix, and Map.<br /><ac:image><ri:attachment ri:filename="select_model_elements_in_the_Containment_tree.png" /></ac:image></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to Top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f88898b1-de9e-429c-9e96-2a9541797a7c"><ac:parameter ac:name="id">1292342252</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Discontinued Products</h5><p>Beginning with the 2022x version, support of the following products is discontinued:</p><ul><li><strong>CSV Import Plugin</strong>. <ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Sync with Excel or CSV files" /><ac:plain-text-link-body><![CDATA[Excel/CSV Sync]]></ac:plain-text-link-body></ac:link> or<ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Importing data from Excel or CSV files" /><ac:plain-text-link-body><![CDATA[ Excel/CSV Import]]></ac:plain-text-link-body></ac:link> features will be replacing the CSV Import Plugin.<strong><br /></strong></li><li><strong>MagicDraw Professional Java Edition Floating License</strong> and <strong>MagicDraw Professional Java Edition Seat License.</strong> Java Code Engineering will be available in the modeling tool Enterprise editions. For customers with active software assurance (ALC), the upgrade to the Enterprise edition will come at no cost.</li><li><strong>JRuby scripting language</strong>. Any previously used scripts written in JRuby need to be rewritten in a different built-in scripting language. Otherwise, you can <ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Adding JRuby and installing Gems" /><ac:plain-text-link-body><![CDATA[manually add JRuby to the modeling tool]]></ac:plain-text-link-body></ac:link> to continue using the existing JRuby scripts.</li><li><strong>Magic Teamcenter Connector</strong>. Starting with version 2022x, Magic Teamcenter Connector is no longer available. You may continue to use your perpetual license of the product in accordance with the terms of your license agreement. The support for the product will be provided until the end of your current maintenance support subscription.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6d29a81c-76d8-4412-8e3c-38170ac63ca1"><ac:parameter ac:name="id">1292358024</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Reader Mode</h5><p>Starting with this version, <strong>Reader </strong>is introduced as the modeling tool mode. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Reader Mode activation" /><ac:plain-text-link-body><![CDATA[Learn more about how to activate the Reader Mode >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="6069d3a5-2669-47b8-bfcb-8be56cf750dc"><ac:parameter ac:name="id">243713866</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Collaboration</h5><h3><span>Global Element Usage Search</span></h3><p>The 2022x version includes the release of production-ready <strong>Global Element Usage Search</strong> functionality. It allows you to search for usages of an element that you want to modify or delete. Depending on the <ac:link><ri:page ri:space-key="TWCloud2022x" ri:content-title="Creating indexing configurations" /><ac:plain-text-link-body><![CDATA[server-side configuration]]></ac:plain-text-link-body></ac:link>, projects that use the element in question can be returned either from the entire Teamwork Cloud repository or the selected custom indexed scope. This <span style="color: rgb(62,63,64);">minimizes the probability of unexpected Recovered Elements appearing</span> when updating the Used Project versions.</p><p><span class="confluence-embedded-file-wrapper image-center-wrapper"> <ac:image ac:align="center"><ri:attachment ri:filename="global_element_usage_search.png" /></ac:image> </span></p><h6 style="text-align: center;">Searching for element usages within the Teamwork Cloud repository.</h6><p><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="Global element usage search" /><ac:plain-text-link-body><![CDATA[Learn more about the Global Element Usage Search feature >>]]></ac:plain-text-link-body></ac:link></p><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to Top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="34f0ca67-0bd7-4e60-ab36-156ec5dcf663"><ac:parameter ac:name="id">430554266</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong><ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2022x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=178160436 space=MSOSA2024xR1 version=4 -->
## PAGE 00003: 2024x Refresh1 Version News

- page_id: `178160436`
- space_key: `MSOSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024xR1/pages/178160436/2024x+Refresh1+Version+News
- version_number: 4
- version_date: `2024-12-16T15:00:18.134+01:00`
- ancestors: Magic Systems of Systems Architect Documentation
- labels: []

### NORMALIZED CONTENT

top

### Magic Systems of Systems Architect

Released on: July 5, 2024

Beginning with version 2024x Refresh1, significant enhancements have been made to various diagramming tools and tables. The**Security Connectivity**and**Security Role-based Connectivity**tables have been restructured into dedicated diagrams for better clarity on Operational and Resource viewpoints. The**Strategic Driver Map**now visually connects Drivers, Enterprise Goals, and Strategic Phases, while the new**Strategic Drivers Table**organizes elements, such as Drivers, Challenges, Opportunities, and Capabilities, in a structured format. The**Preview Affected Diagrams**dialog has been introduced for easier management and preview of affected diagrams, with new options for updating diagram elements. Enhancements to**Gantt Charts**include better project and milestone management and display options for projects. Measurement management has been improved with features for reusing default values and auto-populating measurements in Property Sets. Additionally, model conversion between frameworks and new validation rules have been implemented to streamline processes and ensure data integrity.

SysML features introduce several improvements to Item Flow management. You can now navigate from a selected Item Flow in the Containment tree to the diagrams where it is realized, specify Conveyed Items from the Diagram Palette, and hide arrow notations on realizing elements when the Conveyed Item is hidden or unspecified. Conveyed Items are now represented with icons in the 'Create / Edit Item Flow' dialog. Item Flow creation between Activity Parameter Nodes and Actions has been enhanced. Two new validation rules highlight Item Flows without Conveyed Items. The 'Preview Affected Diagrams' dialog further enhances the Item Flow management experience by presenting all affected diagrams.

Furthermore, the 2024x Refresh1 release contains new validation solvers for the 'Invalid Connector' validation rule, allowing for an easy connector redefinition. The new release also introduces the MagicGrid perspective.

Simulation features introduce several significant enhancements. One of the key updates is the ability toanimate behavioral diagrams during server-side simulationby embedding theminto HTML-generated user interfaces. The latest product version also supports model data export to the SSP file format,allowing you transfer models between different simulation tools, such as Dymola. Furthermore, you can now load and play external simulation results from CSV files using the Results Player.Additionally, a new project option allows you to display runtime values on Port labels during simulation, providing immediate insights into model behavior. The new release also supports Matlab integration for Apple Silicon,allows enabling and disabling simulation annotations in diagrams, offers improvements to the ALH.callOperation method and built-in math functions, and more.

Client-side performance enhancements include optimized efficiency for exporting matrices and tables in SVG format. For general modeling, this release improves Information Flow management. You can now easily navigate from a selected Information Flow in the Containment tree to the diagrams where it is realized and specify Conveyed Information directly in the diagram. You can choose to hide arrow notations on realizing elements when the Conveyed Information is hidden or unspecified. Conveyed Information is now represented with icons in the 'New Conveyed Information' dialog. New validation rules highlight Information Flows that do not have any Conveyed Information.

Additional enhancements include the improved samples access and navigation in the modeling tool. Also, a new 'Letter Spacing Reduction in SVG' environment option is introduced to control the spacing between letters when exporting diagram images in SVG format.

Additionally, collaborative modeling brings several enhancements tothe Model Patch functionality, which is now out of the technology preview phase. The Model Patch UI has been improved with a new panel that identifies and explains issues related to model patch application. Project commit processes are now more efficient with a First-In-First-Out (FIFO) queue system for simultaneous commits. Finally, you can save time by skipping the migration of archived branches when migrating Teamwork Cloud projects and more.

Collaboration powered by the 3DEXPERIENCE platform introduces significant improvements as well. You can now move Teamwork Cloud projects to the 3DEXPERIENCE platform and then update these projects using the .szip file format. In addition, the History and Edit Branches dialogs now indicate if and from which iteration a project was merged.

To download the latest version of the modeling tool, see [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']. For further information, check the [CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024xR1'].

#### NOTE: 2024x Refresh1 Hot Fix 1 available

2024x Refresh1 Hot Fix 1 available

2024x Refresh1 Hot Fix 1 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Refresh1 Hot Fix 1 Version News' space='CATIA']>]]>

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

****

- 
- 
- 
- 

- 

****

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
- 
- 

****

- 
- 
- 

****

- 
- 
- 

#### UAF Features

##### Diagraming

###### Security Connectivity and Role-Based Connectivity Tables

Beginning with version 2024x Refresh1, the Security Connectivity and Security Role-based Connectivity tables have been redesigned into dedicated diagrams focusing on the Operational and Resource viewpoints:

- Security Connectivity (Resource) Table
- Security Role-based Connectivity (Resource) Table
- Security Connectivity (Operational) Table
- Security Role-based Connectivity (Operational) Table

[IMAGE alt='' src='']

###### Strategic Driver Map

This predefined map includes the Driver, Enterprise Goals, and/or Enterprise Objectives that are related to a Driver using the Motivated By relationship, and Actual Strategic Phases that are related to the Enterprise Goals or Enterprise Objectives using the Phases relationship.

[IMAGE alt='' src='']

###### Strategic Driver Table

The new Strategic Drivers Table allows you to assemble Drivers, Challenges, Opportunities, and Capabilities in a tabular form in strict order: the Driver presenting Challenges, the Challenges motivating Opportunities, and the Opportunities impacting Capabilities.

In this table, you can also define relationships between Drivers and Challenges, Challenges and Opportunities, Opportunities and Capabilities. This table captures the Driver, Challenge, Opportunity, and Capability elements.

[IMAGE alt='' src='']

###### Affected Diagrams Preview Dialog

To enhance the exchange creation and management experience in Resource, Service, and Operational viewpoints, we have introduced the **Preview Affected Diagrams** dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements, where the created Exchanges will be realized, are prominently marked in the diagram preview pane.

During the preview process, you can select the **Update Diagram** check box for diagrams in which you wish to display the Conveyed Items of the selected exchange.

The new[CONFLUENCE_PAGE title='Setting project options' space='UAF12P2024xR1']**Show Item Flows on Affected Diagrams**controls how the diagrams will be updated for newly created or modified exchanges. Set the option to true to update all affected diagrams and show the Conveyed Items of exchanges whenever a new exchange is created or an existing one is modified.

[CONFLUENCE_PAGE title='Preview Affected Diagrams dialog' space='UAF12P2024xR1']>>]]>

[IMAGE alt='' src='']

##### Report templates

- The new report templates have been implemented for Service Connectivity Table and Service Role-based Connectivity Table. The reports are available through the Report Wizard.

[IMAGE alt='' src='']

- A new Strategic Driver Table also makes a new report available. You can create the report through the Report Wizard, directly from the table toolbar, or using a quick report option from the Containment tree.

[IMAGE alt='' src='']

##### Gantt Chart Enhancements

###### Project Roadmap Enhancements

- The new Actual Project Assignment wizard will help you add new Actual Projects to the chart more conveniently. With this wizard, you will:
  - Have the ability to reuse existing Projects as created Actual Project types [ATTACHMENT filename='actual_project_assignmnet_wizard.png']
  - Control Actual Projects hierarchy creation based on the existing Project structure.
- Two additional steps were added to the Actual Project Milestone Creation wizard. With these steps, you can specify the Actual Project Milestone Version Released and Version Withdrawn properties during milestone creation. 
[IMAGE alt='' src='']
- The new**Display Actual Projects as Grouping Elements**option (located in the Gantt chart options area) is introduced. This option controls how the Actual Project is displayed: [CONFLUENCE_PAGE title='Customizing Gantt chart properties' space='UAF12P2024xR1']>>]]> 
[IMAGE alt='' src='']
  - Turn the option on to display the Actual Project only as a grouping element.
  - Turn the option off to display the grouping Actual Project bars with Actual Project Milestones and completion progress.

###### Strategic Phasing Gantt Chart Enhancements

- You can now choose whether you want to show or hide selected Capability's Provisions in the Capability Provisions area in the Strategic Phasing Gantt Chart. [ATTACHMENT filename='show_hide_capability_provisions_area_strategic_phasing.png']
- Now, when creating a Strategic Phasing Gantt Chart, you can choose to add Capabilities and Resources from the used projects. These elements will be displayed in gray to indicate that they come from a used project.

###### Other

- The Gantt charts were enhanced to indicate when an element is used from another project and/or is read-only, with the element name displayed in gray to signify this status.

##### Exchange Management

- The functionality when reconnecting connectors between elements was improved, offering options for managing exchanges. Now, the modeling tool checks the flow properties of source and target ports (if defined), recommending suitable exchanges for realization. [CONFLUENCE_PAGE title='Working with exchanges' space='UAF12P2024xR1']>>]]>
- You can now specify a Conveyed Item directly in the diagram, picking the needed Conveyed Item element from the diagram palette and dragging it on to the exchange. [ATTACHMENT filename='set_conveyed_item_palette_personnel.png']
- Now the Conveyed Items in the Realized Exchange wizards are represented with icons to help you identify the Conveyed Items.
- With this version, when you hide the realized exchanges, you can choose to hide the arrow notation on the realizing elements as well. The **Hide Information Flow If Conveyed Information Is Missing**[Project option](https://docs.nomagic.com/display/UAF12P2024xR1/Setting+project+options)controls the arrow visibility.
- You can now easily navigate from the selected exchange in Containment tree to the diagrams where that exchange is realized. 
[IMAGE alt='' src='']

##### Measurement Management Enhancements

With this version, we have enhanced measurements management for Property Sets and Measurable Elements.

- Before the 2024xR1 release, you had the ability to define actual values for all measurements within Measurement Sets or Property Sets. Now, with the introduction of the 2024xR1 release, you can effortlessly reuse default actual values to define the entire structure of Actual Property Sets. This enhancement includes the implementation of the Default value button, conveniently accessible within the Specification window. [CONFLUENCE_PAGE title='Applying Actual Measurements' space='UAF12P2024xR1']>>]]>

[IMAGE alt='' src='']

- Prior to the 2024xR1 release, automatic population of measurements was limited to Measurable Elements only, with no capability for Property Sets. With the introduction of the 2024xR1 release, you now have the ability to automatically populate measurements on Property Sets as well. Measurements are created for elements with the **Applies for** tag values (stereotyped with «DoDAFProperties») applied, and the newly created measurements are typed by the elements with the «DoDAFProperties» stereotype applied. [CONFLUENCE_PAGE title='Setting up Automatic Population of Measurement Sets' space='UAF12P2024xR1']>>]]>

[IMAGE alt='' src='']

- Before the 2024x R1 release, reusing and synchronization of Measurement structures was not feasible in UAF. With the release of the 2024x R1, you can now leverage this functionality for Property Set usages, including Assets and Roles, as well as Measurement Sets and Measurements. This enhancement enables the creation of an Actual Property Set structure suggested based on the structure of the Property Set typing the Measurable Element, with default values also suggested.

Existing Actual Property Sets of the Measurable Element type are recommended, and this allows you to review and adjust them as needed. Additionally, the newly created Actual Property Set is applied as a default value of the Measurable Element.

[CONFLUENCE_PAGE title='Reusing Measurement Sets for Actual Property Set creation' space='UAF12P2024xR1']>>]]>

[IMAGE alt='' src='']

##### Model Conversion Between Frameworks Improvements

The project conversion between different Enterprise Architecture Frameworks has undergone some improvements and now adds more clarity. The framework packages are seamlessly mapped during conversion, with package names adjusted accordingly. Custom-named packages remain unchanged, while multiple packages with identical names are merged into one.

[CONFLUENCE_PAGE title='Converting model between Enterprise Architecture Frameworks' space='UAF12P2024xR1']>>]]>

[IMAGE alt='' src='']

##### Validation

- The COR2185 validation rule was improved to synchronize Measurement Sets of the validated element, located in the Measurement Set property, with Measurement Sets of the associated element: extending beyond Measurable Elements to include Property sets that own the measurements typed by Measurement Sets.
- New completeness validation rules (COM2028, COM2029, COM2030) have been implemented for Operational, Resource, and Service viewpoints to highlight exchanges that are not realized by any realizing element.
- The new correctness validation rule COR2184 was implemented to check whether the Actual Project Start and End dates enclose the dates of its owned Actual Projects.
- The COR2196 correctness validation rule was implemented to check whether the date of the Actual Project Milestone does not precede the date of its referenced Actual Project Milestones.

##### Discontinued Features

- The PES export functionality is no longer available.

##### Other Enhancements

- One more way to model conjugated ports is to create the Conjugated Operational/Resource/Resource Service/Service/ Interface, which has the same features as its original Interface except that its Flow Properties are reversed (conjugated). [CONFLUENCE_PAGE title='Working with conjugated Interfaces' space='UAF12P2024xR1']>>]]>
- You can now create a Definition and Comment for any UAF element in their **Specification**window > **Documentation/Comment** property group. 
[IMAGE alt='' src='']
- The new Project option **Show Diagram Abbreviations**has beenintroduced. Set this option to true to show diagram abbreviation in the Containment tree. [CONFLUENCE_PAGE title='Show diagram abbreviation in Containment tree' space='UAF12P2024xR1']>>]]> 
[IMAGE alt='' src='']
- With the new Project Option **Show default documentation for UAF Packages**, you canchoose to show the default UAF Packagedocumentation. Turning the option on will display the documentationin:
  - The viewpoint package element's Specification window, Documentation/Comment property
  - The selected viewpoint package element's Documentation tab, which is located in the Model Browser. [CONFLUENCE_PAGE title='Show default documentation for UAF packages' space='UAF12P2024xR1']>>]]> [ATTACHMENT filename='default_package_documentation.png']
- The Strategic Motivation Table has been improved. Now when you click the **Add New** or **Add Nested** button, the SysML Requirements are collapsed and you can focus only on UAF requirements - Enterprise Goal and Enterprise Objective.
- The creation process of UAF Instance Specifications was enhanced by enabling the creation of slots when one instance specification is dragged and dropped onto another from the diagram, diagram palette, or Containment tree when the structure of Instance Specification types is predefined.
- The role-based connectivity diagrams have been enhanced by adding a Context column to show the context of the element realizing the exchange .

#### SysML Features

##### Affected Diagrams Preview Dialog

To enhance the Item Flow creation and management experience, we have introduced the**Preview Affected Diagrams**dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements are prominently marked in the diagram preview pane conveying where the created Item Flows will be realized.

During the preview process, you can select the **Update Diagram** check box for diagrams in which you wish to display the Conveyed Items of the selected flows.

The new[CONFLUENCE_PAGE title='Setting project options' space='SYSMLP2024xR1']**Show Item Flows on Affected Diagrams**controls how the diagrams will be updated for newly created or modified flows. Set the option to *true*to update all affected diagrams and show the Conveyed Items of flows whenever a new flow is created or an existing one is modified.

[CONFLUENCE_PAGE title='Preview Affected Diagrams dialog' space='SYSMLP2024xR1']>]]>

[IMAGE alt='' src='']

###### Item Flows Management

- Interactions can be modeled across various diagrams in both behavior and structure models, creating difficulties in locating diagrams representing Item Flow realizations and hindering transparency in their identification. Now you can easily navigate from the selected Item Flow in the Containment tree to the diagrams where the Item Flow is realized. [CONFLUENCE_PAGE title='Creating Item Flow' space='SYSMLP2024xR1']>]]> 
[IMAGE alt='' src='']
- Specify the Conveyed Item directly in the diagram, picking the needed Conveyed Item element from the diagram palette and dragging it on to the Item Flow. [CONFLUENCE_PAGE title='Creating Item Flow' space='SYSMLP2024xR1']>]]> [IMAGE alt='' src='']
- You can now choose whether you want to hide the arrow notation on the realizing elements when the Conveyed Item is hidden or unspecified in case you would need to conceal such approximate interactions, and vice versa . The **Hide Information Flow If Conveyed Information Is Missing** [CONFLUENCE_PAGE title='Setting project options' space='SYSMLP2024xR1'] controls the arrow visibility. [CONFLUENCE_PAGE title='Creating Item Flow' space='SYSMLP2024xR1']>]]> 
[IMAGE alt='' src='']
- Now the Conveyed Items in the Create / Edit Item Flow dialog are represented with icons to help you identify the Conveyed Items. [IMAGE alt='' src='']
- Item Flow creation between Activity Parameter Nodes and Actions has been enhanced to facilitate the creation of Item Flows when interactions are modeled between Part Properties. Typically, the 'Usage' allocation mode is used for this, which does not create an allocation relation on the end of the Activity Parameter Node, thereby not providing a possible sender or receiver on this end. Now, the tool checks action allocations to typed parts for Activity Parameter Nodes. Consequently, the Direction field in the **Create / Edit Item Flow** dialog displays suggested sender and receiver elements based on the element typing the parts to which actions are allocated. [ATTACHMENT filename='Item Flow between Activity Parameter Node and Action.png'] On the end of the*input : Audio data*Activity Parameter Node there are no Actions, only the*Read and transmit the sound*Activity. Thus, the tool checks the model to find Actions that invoke this Activity, locating the*: Read and transmit the sound* Action in the *Listen the audio* Activity diagram. 
Then the tool checks the allocation relationships for this action and an allocation to the *: Wireless Earbuds* Part Property is found. 
Using this information the **Create/Edit Item Flow** dialog identifies the *Wireless Earbuds* Block as a possible sender of the flow, displaying*Wireless Earbuds*and *Processing*Blocks as a suggestion for the sender/receiver in the **Direction**field of the dialog.
- New validation rules ( [CONFLUENCE_PAGE title='Item Flow has no Conveyed Items' space='SYSMLP2024xR1'] and [CONFLUENCE_PAGE title='Realized Item Flow has no Conveyed Items' space='SYSMLP2024xR1'] ) have been implemented to highlight Item Flows that do not have any Conveyed Items. This helps to declutter the model and identify potentially unused flows. Learn more on the [CONFLUENCE_PAGE title='Item Flow has no Conveyed Items' space='SYSMLP2024xR1'] and [CONFLUENCE_PAGE title='Realized Item Flow has no Conveyed Items' space='SYSMLP2024xR1'] pages.

##### Connector Redefinition

New validation solvers are available for the **Invalid Connector** validation rule, allowing for an easy connector redefinition:

- Use the **Redefine and Replace Connector** solver to have a new redefining connector created if the selected connector is inherited and at least one of its ends is redefined.
- Use the **Replace with Redefining** solver to replace the failed connector with the redefining one if the failed connector is already redefined in the same context.

[CONFLUENCE_PAGE title='Invalid Connector (UML Correctness)' space='SYSMLP2024xR1']>]]>

[IMAGE alt='' src='']

###### The image displays how to resolve the **Invalid Connector**validation error via the **Redefine and Replace Connector**solver.****

##### MagicGrid Perspective

The MagicGrid perspective has been introduced, supplementing existing perspectives, such as Full Featured or System Engineer. This perspective simplifies the modeling tool by providing only the MagicGrid-required subset of SysML elements and diagrams, making it easier to understand and navigate for users new to MagicGrid. You can manually switch perspectives via the **Select Perspective** dialog. Furthermore, a dialog prompting you to switch to this perspective appears whenever you create a MagicGrid project.

[CONFLUENCE_PAGE title='Selecting perspective' space='SYSMLP2024xR1']>]]>

###### [IMAGE alt='' src='']The MagicGrid perspective available via the **Select Perspective** dialog.

#### Simulation Features

##### What's New in Server-Side Simulation

###### Diagram Animation Support

The new release supports diagram animation when executing projects on the server. Now behavioral (Activity, State Machine, and Sequence) diagrams can be embedded into HTML-generated user interfaces and are animated during server-side simulation.[CONFLUENCE_PAGE title='Simulation with UI' space='CST2024xR1']>]]>

[IMAGE alt='' src='']

###### Diagram animation support in server-side simulation.

###### Other

- 
  - Now UI titles are displayed in a UI index window and you can use them to open a specific UI in a separate window.
  - Upon successful installation, the Simulation application card is displayed on the Web Application Platform welcome page.Opening the application will redirect you to the Server-side Simulation Swagger page.
  - The RUN endpoint has a new 'timeout' query parameter which allows you to specify the timeout duration in minutes.
  - The 'sync' query parameter has been added to the RUN, STEP, and TERMINATE endpoints. You can use them to initiate a synchronous API call in server-side simulation using Jupyter Notebook.

##### SSP Export Support

This release introduces a powerful new feature - the ability to export model data to the SSP (System Structure and Parameterization) file format.SSP is a tool-independent standard used to define complete systems consisting of one or more FMUs (Functional Mockup Interfaces). With this enhancement, you can transfer models between different simulation tools, such as Dymola, facilitating greater interoperability and collaboration. [CONFLUENCE_PAGE title='SSP Export - Technology Preview' space='CST2024xR1']>]]>

##### Results Player

Now, the tool can read and play external simulation results from CSV files. You can load CSV files generated either locally or by external tools into the Results Player and then play back the simulation results in your modeling tool. The Results Player offers enhanced playback controls, allowing users to pause playback, navigate through different simulation times using a slider, and adjust playback speed according to their preferences. [CONFLUENCE_PAGE title='Results Player - Technology Preview' space='CST2024xR1']>]]>

[IMAGE alt='' src='']

###### Using the Results Player to play back simulation results from an imported CSV file.

##### Displaying Runtime Values on Port Labels

A new******Show Runtime Values on Port Labels**project option and Simulation Configuration property allows you to see runtime values on Port labels during simulation as displayed below. [CONFLUENCE_PAGE title='Manipulating simulation information' space='CST2024xR1']>]]>

[IMAGE alt='' src='']

###### Displaying runtime values on Port labels during simulation.

##### Easier Access to Nested Properties

You no longer need complex ALH (Action Language Helper) scripts to access deeply nested properties. With the Groovy language, you can use "dot notation" directly in any expression.

[IMAGE alt='' src='']

###### Using "dot notation" in the Groovy language.

##### Other Improvements

- The new **Show Annotations** project option and Simulation Configuration property allows enabling and disabling simulation annotations in diagrams. Simulation annotations include flowing information, possibility to change animation speed, and annotation tooltips. [CONFLUENCE_PAGE title='Displaying simulation information' space='CST2024xR1']>]]>
- Matlab integration is now supported for Apple Silicone.
- The ALH.callOperation method has been enhanced and now supports calling operations through ports.
- This release introduces several new methods of the built-in math functions.
- Now you can specify the simulation license for SIMULIA when logging in to the 3D EXPERIENCE platform.

#### Client side performance improvementsClient-side Performance Improvements

##### Improvements in Diagram Export as SVG

Exporting diagrams in Scalable Vector Graphics (*.svg) format now features significant optimizations, with the most notable improvements in matrix and table exports:

- Reduction in the file size of exported SVG files.
- Export now requires up to 10 times less RAM resources.
- Decreased duration of the export process.

These optimizations enhance the efficiency of exporting matrices and tables in SVG format, resulting in significantly reduced file sizes. The improvements impact various functionalities that utilize SVG image generation, such as image export via the MDZipX plugin or the 'Save as Image' command.

[IMAGE alt='' src='']

###### A chart comparing the file size of a Dependency Matrix exported as a SVG image in 2024x and 2024x Refresh1.

#### miModeling and Infrastructure

##### Information Flow Management Improvements

- Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. [CONFLUENCE_PAGE title='Element usage in diagrams' space='MD2024xR1']>]]> [ATTACHMENT filename='Navigate_to_diagram_UML.png']
- Specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. [CONFLUENCE_PAGE title='Information Flow' space='MD2024xR1']>]]> [IMAGE alt='' src='']
- You can no w choose whether you want to hide the arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified . The **Hide Information Flow If Conveyed Information Is Missing** [CONFLUENCE_PAGE title='Setting project options' space='MD2024xR1'] controls the arrow visibility. [CONFLUENCE_PAGE title='Information Flow' space='MD2024xR1']>]]> 
[IMAGE alt='' src='']
- Now the Conveyed Information in the New Conveyed Information dialog is represented with icons to help you identify the Conveyed Information. [IMAGE alt='' src='']
- New validation rules ( [CONFLUENCE_PAGE title='Information Flow has no Conveyed Information' space='MD2024xR1'] and [CONFLUENCE_PAGE title='Realized Information Flow has no Conveyed Information' space='MD2024xR1'] ) have been implemented to highlight Information Flows that do not have any Conveyed Information. Learn more on the [CONFLUENCE_PAGE title='Information Flow has no Conveyed Information' space='MD2024xR1'] and [CONFLUENCE_PAGE title='Realized Information Flow has no Conveyed Information' space='MD2024xR1'] pages.

##### Improved Samples Access and Navigation

From now on, you can review the list of available samplesanytime by invoking theSamples tab. The tab displays all the samplesprovided with the modeling tool installation, providing a convenient way to review and access the needed samples.Additionally, you can use the search bar to navigate the available content efficiently both in the Samples and Welcome tabs.

[CONFLUENCE_PAGE title='Editor Tabs' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

##### Other Improvements

- A new Letter Spacing Reduction in SVG environment option is introduced to control the spacing between letters when exporting diagram images in SVG format . Adjusting letter spacing enables you to maintain text alignment within shape boundaries when exporting, ensuring it does not exceed their borders. [CONFLUENCE_PAGE title='Diagram image export' space='MD2024xR1']>]]>

#### CollaborationCollaboration

##### Model Patch Functionality Improvements

We are happy to announce that in this release the Model Patch functionality is coming out of the technology preview phase with several enhancements.Model Patch is a more convenient alternative to afull Model merge or disconnected team collaboration because it allows you to move the selected elements or element changes from one model branch to another and transfer only a specific scope of model modifications.

In this version, we improved the Model Patch UI and introduced a new panel that will help you solve any problems related to model patch application. This panel lists all the changes that could not be applied and describes the underlying issue for each change. [CONFLUENCE_PAGE title='Using Model Patch' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

###### Model Patch mechanism.

[IMAGE alt='' src='']

###### A panel listing the model patch changes that could not be applied.

##### Commit Queues

You now have access to a quicker and more predictable project commit execution at the end of a long working day: simultaneous commits are processed by putting all users in a First-In-First-Out (FIFO) line, ensuring fairness and efficiency in project commits. [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

###### The dialog showing your position in the project commit queue.

##### Other

- Starting with version 2024x Refresh1, you won't need to manually specify the Web Application Platform URL to access specific Teamwork Cloud features like Resource Usage Map or global element usage search. Teamwork Cloud will now retrieve the URL automatically.
- Now it will be possible to skip the migration of archived branches when migrating Teamwork Cloud projects, which will significantly reduce the migration time.
- The project comparing functionality no longer requires the Read Resources permission for used projects. However, you still need the Read Resources permission for the main projects you want to compare.

#### Collaboration Powered by **3D**EXPERIENCE Platform

##### Moving Projects to the **3D**EXPERIENCE Platform

We're thrilled to announce a significant step towards collaboration between Teamwork Cloud and the **3D**EXPERIENCE platform. With this release, you will have the ability to move Teamwork Cloud projects to the **3D**EXPERIENCE platform using the server project file format (.szip).Previously, the .szip file format facilitated collaboration solely between different Teamwork Cloud servers. However, with version 2024x Refresh1, we have extended its functionality to allow importing projects from .szip files to the**3D**EXPERIENCE platform as well and updating them if a project already exists on the platform.

We hope that you will benefit from this new functionality and stay tuned for further improvements in future releases. [CONFLUENCE_PAGE title='Importing Teamwork Cloud projects to the 3DEXPERIENCE platform' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

###### Moving projects to the **3D**EXPERIENCE platform by using the server project file format.

##### Iteration Merge Information

Now the **History** and **Edit Branches** dialogs show if a specific project iteration was merged, as well as the iteration it was merged from.

[IMAGE alt='' src='']

###### The Iteration column of the History dialog displays the project merge information.

##### Performance Improvements

The performance for various basic server operations, especially project opening, has been significantly improved. As you can see in the charts below, now projects on the **3D**EXPERIENCE platform open at least five times faster compared to version 2024x.

[IMAGE alt='' src='']

###### The charts comparing project opening performance for projects with 2 million elements.

[CONFLUENCE_PAGE title='2024x Refresh1 Version News' space='NMDOC']>]]>

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7dc7bee2-3797-466f-982b-5a1e0d78e7c5"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><h1 style="text-align: center;">Magic Systems of Systems Architect</h1><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: July 5, 2024</span></p><p><br /></p><p><span><span style="color: rgb(23,43,77);">Beginning with version 2024x Refresh1, significant enhancements have been made to various diagramming tools and tables. The </span><strong>Security Connectivity</strong><span style="color: rgb(23,43,77);"> and </span><strong>Security Role-based Connectivity</strong><span style="color: rgb(23,43,77);"> tables have been restructured into dedicated diagrams for better clarity on Operational and Resource viewpoints. The </span><strong>Strategic Driver Map</strong><span style="color: rgb(23,43,77);"> now visually connects Drivers, Enterprise Goals, and Strategic Phases, while the new </span><strong>Strategic Drivers Table</strong><span style="color: rgb(23,43,77);"> organizes elements, such as Drivers, Challenges, Opportunities, and Capabilities, in a structured format. The </span><strong>Preview Affected Diagrams</strong><span style="color: rgb(23,43,77);"> dialog has been introduced for easier management and preview of affected diagrams, with new options for updating diagram elements. Enhancements to </span><strong>Gantt Charts</strong><span style="color: rgb(23,43,77);"> include better project and milestone management and display options for projects. Measurement management has been improved with features for reusing default values and auto-populating measurements in Property Sets. Additionally, model conversion between frameworks and new validation rules have been implemented to streamline processes and ensure data integrity.</span></span></p><p><span>SysML features introduce several improvements to Item Flow management. You can now navigate from a selected Item Flow in the Containment tree to the diagrams where it is realized, specify Conveyed Items from the Diagram Palette, and hide arrow notations on realizing elements when the Conveyed Item is hidden or unspecified. Conveyed Items are now represented with icons in the 'Create / Edit Item Flow' dialog. Item Flow creation between Activity Parameter Nodes and Actions has been enhanced. Two new validation rules highlight Item Flows without Conveyed Items. The 'Preview Affected Diagrams' dialog further enhances the Item Flow management experience by presenting all affected diagrams.</span></p><p><span>Furthermore, the 2024x Refresh1 release contains <span style="color: rgb(14,16,26);">new validation solvers for the 'Invalid Connector' validation rule, allowing for an easy connector redefinition. T</span></span><span style="color: rgb(14,16,26);">he new release also introduces the MagicGrid perspective. </span></p><p><span>Simulation features introduce several significant enhancements. One of the key updates is the ability to</span><span> </span><span>animate behavioral diagrams during server-side simulation </span><span>by embedding them</span><span> </span><span>into HTML-generated user interfaces</span><span>. The latest product version also supports model data export to the SSP file format, </span><span style="color: rgb(33,37,41);"><span style="color: rgb(13,13,13);">allowing you transfer models between different simulation tools, such as Dymola</span></span><span>. Furthermore, you can now load and play external simulation results from CSV files using the Results Player. </span><span>Additionally, a new project option allows you to display runtime values on Port labels during simulation, providing immediate insights into model behavior. The new release also supports Matlab integration for Apple Silicon, </span><span>allows enabling and disabling simulation annotations in diagrams, offers improvements to the ALH.callOperation method and built-in math functions, and more.</span></p><p><span>Client-side performance enhancements include optimized efficiency for exporting matrices and tables in SVG format. For general modeling, this release improves Information Flow management. You can now easily navigate from a selected Information Flow in the Containment tree to the diagrams where it is realized and specify Conveyed Information directly in the diagram. You can choose to hide arrow notations on realizing elements when the Conveyed Information is hidden or unspecified. Conveyed Information is now represented with icons in the 'New Conveyed Information' dialog. New validation rules highlight Information Flows that do not have any Conveyed Information.</span></p><p><span>Additional enhancements include the improved samples access and navigation in the modeling tool. Also, a new 'Letter Spacing Reduction in SVG' environment option is introduced to control the spacing between letters when exporting diagram images in SVG format.</span></p><p>Additionally, collaborative modeling brings several enhancements to<span> the Model Patch functionality, which is now out of the technology preview phase. The Model Patch UI has been improved with a new panel that identifies and explains issues related to model patch application. Project commit processes are now more efficient with a First-In-First-Out (FIFO) queue system for simultaneous commits. Finally, you can save time by skipping the migration of archived branches when migrating Teamwork Cloud projects and more.</span></p><p><span>Collaboration powered by the 3DEXPERIENCE platform introduces significant improvements as well. You can now move Teamwork Cloud projects to the 3DEXPERIENCE platform and then update these projects using the .szip file format. In addition, the History and Edit Branches dialogs now indicate if and from which iteration a project was merged.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[product documentation]]></ac:plain-text-link-body></ac:link>.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="569e25e5-7042-4e37-bc33-e76dbcdf057e"><ac:parameter ac:name="title">2024x Refresh1 Hot Fix 1 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Refresh1 Hot Fix 1 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Refresh1 Hot Fix 1 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong><ac:link ac:anchor="UAF Features" /></strong></p><ul><li><ac:link ac:anchor="Diagraming" /></li><li><ac:link ac:anchor="Report templates" /></li><li><ac:link ac:anchor="Gantt Chart Enhancements" /></li><li><ac:link ac:anchor="Exchange Management" /></li><li><ac:link ac:anchor="Measurement Management Enhancements" /></li><li><ac:link ac:anchor="Model Conversion Between Frameworks Improvements" /></li><li><ac:link ac:anchor="Validation" /></li><li><ac:link ac:anchor="Discontinued Features" /></li><li><ac:link ac:anchor="Other Enhancements" /></li></ul><p><strong><ac:link ac:anchor="SysML Features" /></strong></p><ul><li><ac:link ac:anchor="Affected Diagrams Preview Dialog" /></li><li><ac:link ac:anchor="Item Flows Management" /></li><li><ac:link ac:anchor="Connector Redefinition" /></li><li><ac:link ac:anchor="MagicGrid Perspective" /></li></ul></ac:layout-cell><ac:layout-cell> <strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Client side performance improvements"><ac:plain-text-link-body><![CDATA[Client-side Performance Improvements]]></ac:plain-text-link-body></ac:link></strong><ul><li><ac:link ac:anchor="Improvements in Diagram Export as SVG" /></li></ul><p><strong><ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link></strong></p><ul><li><ac:link ac:anchor="Information Flow Management Improvements" /></li><li><ac:link ac:anchor="Improved Samples Access and Navigation" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul><p> <strong><ac:link ac:anchor="Simulation Features" /></strong></p><ul><li><ac:link ac:anchor="What's New in Server-Side Simulation" /><ul><li><ac:link ac:anchor="Diagram Animation Support" /></li><li><ac:link ac:anchor="Other" /></li></ul></li><li><p><ac:link ac:anchor="SSP Export Support" /></p></li><li><p><ac:link ac:anchor="Results Player" /></p></li><li><p><ac:link ac:anchor="Displaying Runtime Values on Port Labels" /></p></li><li><p><ac:link ac:anchor="Easier Access to Nested Properties" /></p></li><li><p><ac:link ac:anchor="Other Improvements" /></p></li></ul></ac:layout-cell><ac:layout-cell><p> <strong><ac:link ac:anchor="Collaboration" /></strong></p><ul><li><ac:link ac:anchor="Model Patch Functionality Improvements" /></li><li><ac:link ac:anchor="Commit Queues" /></li><li><ac:link ac:anchor="Other" /></li></ul><p><strong><ac:link ac:anchor="Collaboration Powered by 3DEXPERIENCE Platform" /></strong></p><ul><li><ac:link ac:anchor="Moving Projects to the 3DEXPERIENCE Platform" /></li><li><ac:link ac:anchor="Iteration Merge Information" /></li><li><ac:link ac:anchor="Performance Improvements" /></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h2>UAF Features</h2></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Diagraming</h3></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><h4 style="text-align: left;margin-left: 40.0px;">Security Connectivity and Role-Based Connectivity Tables</h4><p style="text-align: left;">Beginning with version 2024x Refresh1, the Security Connectivity and Security Role-based Connectivity tables have been redesigned into dedicated diagrams focusing on the Operational and Resource viewpoints:</p><ul style="text-align: left;"><li>Security Connectivity (Resource) Table</li><li>Security Role-based Connectivity (Resource) Table</li><li>Security Connectivity (Operational) Table</li><li>Security Role-based Connectivity (Operational) Table</li></ul></ac:layout-cell><ac:layout-cell><p><ac:image ac:align="center" ac:height="241"><ri:attachment ri:filename="role_based_table_evolution.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h4 style="text-align: left;margin-left: 40.0px;">Strategic Driver Map</h4><p style="text-align: left;"><span style="color: rgb(23,43,77);">This predefined map includes the Driver, Enterprise Goals, and/or Enterprise Objectives that are related to a Driver using the Motivated By relationship, and Actual Strategic Phases that are related to the Enterprise Goals or Enterprise Objectives using the Phases relationship.<span>  </span></span></p><p style="text-align: left;"><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="strategic_driver_map.png" /></ac:image></span></p><h4 style="margin-left: 40.0px;">Strategic Driver Table</h4><p><span>The new Strategic Drivers Table allows you to assemble Drivers, Challenges, Opportunities, and Capabilities in a tabular form in strict order:  the Driver presenting Challenges, the Challenges motivating Opportunities, and the Opportunities impacting Capabilities.</span></p><p style="text-align: left;"><span style="color: rgb(23,43,77);">In this table, you can also define relationships between Drivers and Challenges, Challenges and Opportunities, Opportunities and Capabilities. This table captures the Driver, Challenge, Opportunity, and Capability elements.</span></p><p style="text-align: left;"><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="strategic_driver_table.png" /></ac:image></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h4 style="margin-left: 40.0px;">Affected Diagrams Preview Dialog</h4><p>To enhance the exchange creation and management experience in Resource, Service, and Operational viewpoints, we have introduced the <strong>Preview Affected Diagrams</strong> dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements, where the created Exchanges will be realized, are prominently marked in the diagram preview pane.</p><p>During the preview process, you can select the <strong>Update Diagram</strong> check box for diagrams in which you wish to display the Conveyed Items of the selected exchange.</p><p><span style="color: rgb(23,43,77);">The new<span> </span></span><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[Project option]]></ac:plain-text-link-body></ac:link><strong><span> </span>Show Item Flows on Affected Diagrams</strong><span style="color: rgb(23,43,77);"><span> </span>controls how the diagrams will be updated for newly created or modified exchanges. Set the option to true to update all affected diagrams and show the Conveyed Items of exchanges whenever a new exchange is created or an existing one is modified. </span><span> </span></p><p><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Preview Affected Diagrams dialog" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link><span> </span></p><p><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="preview_affected_v2.png" /></ac:image></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Report templates</h3><ul><li>The new report templates have been implemented for <span style="color: rgb(23,43,77);">Service Connectivity Table and Service Role-based Connectivity Table. The reports are available through the Report Wizard.</span></li></ul><p><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="service_reports.png" /></ac:image></span></p><ul><li><span style="color: rgb(23,43,77);">A new Strategic Driver Table also makes a new report available. You can create the report through the Report Wizard, directly from the table toolbar, or using a quick report option from the Containment tree.</span></li></ul><p><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="strategic_driver_table_report.png" /></ac:image></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Gantt Chart Enhancements</h3><h4 style="margin-left: 40.0px;">Project Roadmap Enhancements</h4><ul><li><span>The new Actual Project Assignment wizard will help you add new Actual Projects to the chart more conveniently. </span><span>With this wizard, you will:</span><ul><li>Have the ability to reuse existing Projects as created Actual Project types<br /><ac:image><ri:attachment ri:filename="actual_project_assignmnet_wizard.png" /></ac:image></li><li>Control Actual Projects hierarchy creation based on the existing Project structure. </li></ul></li><li><p style="text-align: left;">Two additional steps were added to the Actual Project Milestone Creation wizard. With these steps, you can specify the Actual Project Milestone Version Released and Version Withdrawn properties during milestone creation.<br /><ac:image><ri:attachment ri:filename="actual_project_milestone_creation_wizard.png" /></ac:image></p></li><li><p><span style="color: rgb(23,43,77);">The new<span> </span></span><strong style="text-align: left;">Display Actual Projects as Grouping Elements</strong><span style="color: rgb(23,43,77);"><span> </span>option (located in the Gantt chart options area) is introduced. This option controls how the Actual Project is displayed:</span></p><ul><li><span style="color: rgb(23,43,77);">Turn the option on to display the Actual Project only as a grouping element.</span></li><li><span style="color: rgb(23,43,77);">Turn the option off to display the grouping Actual Project bars with Actual Project Milestones and completion progress.</span></li></ul><span style="color: rgb(23,43,77);"><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Customizing Gantt chart properties" /><ac:plain-text-link-body><![CDATA[Learn more about customizing Gantt chart >>>]]></ac:plain-text-link-body></ac:link> <br /><ac:image><ri:attachment ri:filename="actual_project_as_grouping_element.png" /></ac:image></span></li></ul><h4 style="margin-left: 40.0px;"><span>Strategic Phasing Gantt Chart Enhancements</span></h4><ul><li><span>You can now choose whether you want to show or hide selected Capability's Provisions in the Capability Provisions area in the </span>Strategic Phasing Gantt Chart.<span> </span><ac:image><ri:attachment ri:filename="show_hide_capability_provisions_area_strategic_phasing.png" /></ac:image></li><li>Now, when creating a Strategic Phasing Gantt Chart, you can choose to add Capabilities and Resources from the used projects. These elements will be displayed in gray to indicate that they come from a used project. </li></ul><h4 style="margin-left: 40.0px;">Other</h4><ul><li><span style="color: rgb(23,43,77);">The Gantt charts were enhanced to indicate when an element is used from another project and/or is read-only, with the element name displayed in gray to signify this status. </span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Exchange Management</h3><ul><li><p>The functionality when reconnecting connectors between elements was improved, offering options for managing exchanges. Now, the modeling tool checks the flow properties of source and target ports (if defined), recommending suitable exchanges for realization. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Working with exchanges" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link> </p></li><li>You can now specify a Conveyed Item directly in the diagram, picking the needed Conveyed Item element from the diagram palette and dragging it on to the exchange. <br /><ac:image><ri:attachment ri:filename="set_conveyed_item_palette_personnel.png" /></ac:image></li><li>Now the Conveyed Items in the Realized Exchange wizards are represented with icons to help you identify the Conveyed Items. </li><li><span style="color: rgb(23,43,77);">With this version, when you hide the realized exchanges, you can choose to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements as well. The<span> </span></span><span style="color: rgb(23,43,77);"><strong>Hide Information Flow If Conveyed Information Is Missing</strong><span> </span><a href="https://docs.nomagic.com/display/UAF12P2024xR1/Setting+project+options">Project option</a><span> </span>controls the arrow visibility. </span></li><li><span style="color: rgb(23,43,77);">You can now easily navigate from the selected exchange in Containment tree to the diagrams where that exchange is realized. <br /><ac:image><ri:attachment ri:filename="Navigation to realizing elements in symbolic diagrams.png" /></ac:image></span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Measurement Management Enhancements</h3><p style="text-align: left;"><span>With this version, we have enhanced measurements management for Property Sets and Measurable Elements.</span></p><ul><li>Before the 2024xR1 release, you had the ability to define actual values for all measurements within Measurement Sets or Property Sets. Now, with the introduction of the 2024xR1 release, you can effortlessly reuse default actual values to define the entire structure of Actual Property Sets. This enhancement includes the implementation of the <strong>Default value</strong> button, conveniently accessible within the Specification window. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Applying Actual Measurements" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link></li></ul><p style="margin-left: 40.0px;"><span><ac:image><ri:attachment ri:filename="measurements_1.png" /></ac:image></span></p><ul><li><span><span style="color: rgb(23,43,77);">Prior to the 2024xR1 release, automatic population of measurements was limited to Measurable Elements only, with no capability for Property Sets. With the introduction of the 2024xR1 release, you now have the ability to automatically populate measurements on Property Sets as well. Measurements are created for elements with the <strong>Applies for</strong> tag values (stereotyped with «DoDAFProperties») applied, and the newly created measurements are typed by the elements with the «DoDAFProperties» stereotype applied. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Setting up Automatic Population of Measurement Sets" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link><br /></span></span></li></ul><p style="margin-left: 40.0px;"><span><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="measurements_applyFor_tag.png" /></ac:image><br /></span></span></p><ul><li>Before the 2024x R1 release, reusing and synchronization of Measurement structures was not feasible in UAF. With the release of the 2024x R1, you can now leverage this functionality for Property Set usages, including Assets and Roles, as well as Measurement Sets and Measurements. This enhancement enables the creation of an Actual Property Set structure suggested based on the structure of the Property Set typing the Measurable Element, with default values also suggested.</li></ul><p style="margin-left: 40.0px;"><span>Existing Actual Property Sets of the Measurable Element type are recommended, and this allows you to review and adjust them as needed. Additionally, the newly created Actual Property Set is applied as a default value of the Measurable Element.</span></p><p style="margin-left: 40.0px;"><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Reusing Measurement Sets for Actual Property Set creation" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link></p><p style="margin-left: 40.0px;"><ac:image><ri:attachment ri:filename="Reusing measurements structure owned by roles type.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Model Conversion Between Frameworks Improvements</h3><p>The project conversion between different Enterprise Architecture Frameworks has undergone some improvements and now adds more clarity. The framework packages are seamlessly mapped during conversion, with package names adjusted accordingly. Custom-named packages remain unchanged, while multiple packages with identical names are merged into one.</p><p><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Converting model between Enterprise Architecture Frameworks" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="converting_frameworks_wn.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Validation</h3><ul><li><span style="color: rgb(23,43,77);">The COR2185 validation rule was improved to synchronize Measurement Sets of the validated element, located in the Measurement Set property, with Measurement Sets of the associated element: extending beyond Measurable Elements to include Property sets that own the measurements typed by Measurement Sets. </span></li><li><span style="color: rgb(23,43,77);">New completeness validation rules (COM2028, COM2029, COM2030) have been implemented for Operational, Resource, and Service viewpoints to highlight exchanges that are not realized by any realizing element. </span></li><li><span style="color: rgb(23,43,77);">The new correctness validation rule COR2184 was implemented to check whether the Actual Project Start and End dates enclose the dates of its owned Actual Projects. </span></li><li><span style="color: rgb(23,43,77);">The COR2196 correctness validation rule was implemented to check whether the date of the Actual Project Milestone does not precede the date of its referenced Actual Project Milestones. </span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Discontinued Features</h3><ul><li><span>The PES export functionality is no longer available. </span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Other Enhancements</h3><ul><li><span>One more way to model conjugated ports is to create the Conjugated Operational/Resource/Resource Service/Service/ Interface, which has the same features as its original Interface except that its Flow Properties are reversed (conjugated). </span><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Working with conjugated Interfaces" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link><span> </span></li><li><span><span style="color: rgb(23,43,77);">You can now create a Definition and Comment for any UAF element in their <strong>Specification </strong>window &gt; <strong>Documentation/Comment</strong> property group.<br /><ac:image><ri:attachment ri:filename="definition_creation.png" /></ac:image><br /></span></span></li><li><span style="color: rgb(23,43,77);">The new Project option <strong style="text-align: left;">Show Diagram Abbreviations </strong>has been<span> introduced. Set this option to true to show diagram abbreviation in the Containment tree. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Show diagram abbreviation in Containment tree" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link> <br /><ac:image><ri:attachment ri:filename="diagram_abbreviations_sample.png" /></ac:image></span></span></li><li><p><span>With the new Project Option <strong style="text-align: left;">Show default documentation for UAF Packages</strong>, y</span>ou can<span> </span>choose to show the default UAF Package<span> </span>documentation. Turning the option on will display the documentation<span> </span>in:</p><ul><li>The viewpoint package element's Specification window, Documentation/Comment property</li><li>The selected viewpoint package element's Documentation tab, which is located in the<span> </span>Model Browser.<br /><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Show default documentation for UAF packages" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="default_package_documentation.png" /></ac:image></li></ul></li><li><span style="color: rgb(23,43,77);"><span>The Strategic Motivation Table has been improved. Now when you click the <strong>Add New</strong> or <strong>Add Nested</strong> button, the SysML Requirements are collapsed and you can focus only on UAF requirements - Enterprise Goal and Enterprise Objective. </span></span></li><li><span style="color: rgb(23,43,77);"><span>The creation process of UAF Instance Specifications was enhanced by enabling the creation of slots when one instance specification is dragged and dropped onto another from the diagram, diagram palette, or Containment tree when the structure of Instance Specification types is predefined.</span></span></li><li>The role-based connectivity diagrams have been enhanced by adding a <span>Context column to show the context of the element realizing the exchange</span>.  </li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h2>SysML Features</h2><h3>Affected Diagrams Preview Dialog</h3><p><span>To enhance the Item Flow creation and management experience, we have introduced the </span><strong>Preview Affected Diagrams</strong><span> dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements are prominently marked in the diagram preview pane conveying where the created Item Flows will be realized.</span></p><p>During the preview process, you can select the <strong>Update Diagram</strong> check box for diagrams in which you wish to display the Conveyed Items of the selected flows.</p><p><span style="color: rgb(23,43,77);">The new<span> </span></span><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link><strong><span> </span>Show Item Flows on Affected Diagrams</strong><span style="color: rgb(23,43,77);"><span> </span>controls how the diagrams will be updated for newly created or modified flows. Set the option to <em>true </em>to update all affected diagrams and show the Conveyed Items of flows whenever a new flow is created or an existing one is modified. </span></p><p><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Preview Affected Diagrams dialog" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p><span><ac:image ac:align="center" ac:alt="preview_affected_diagrams_dialog.png"><ri:url ri:value="https://docs.nomagic.com/download/attachments/146407510/preview_affected_diagrams_dialog.png?version=1&amp;modificationDate=1710870010652&amp;api=v2" /></ac:image></span></p><h4>Item Flows Management</h4><ul><li><span style="color: rgb(23,43,77);">Interactions can be modeled across various diagrams in both behavior and structure models, creating difficulties in locating diagrams representing Item Flow realizations and hindering transparency in their identification. Now you can easily navigate from the selected Item Flow in the Containment tree to the diagrams where the Item Flow is realized. <ac:link ac:anchor="Navigating to diagrams where Item Flow is realized"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image ac:align="center"><ri:attachment ri:filename="Navigate_to_diagram_SYSML.png" /></ac:image><br /></span></li><li><span>Specify the Conveyed Item directly in the diagram, picking the needed Conveyed Item element from the diagram palette and dragging it on to the Item Flow. </span><ac:link ac:anchor="Specifying the Conveyed Item directly on the diagram pane"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Specifying Conveyed Item via Diagram Palette.png" /></ac:image><br /></span></li><li><span style="color: rgb(23,43,77);">You can now choose whether you want to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements when the Conveyed Item is hidden or unspecified in case you would need to conceal such approximate interactions, and vice versa</span>. The <span><strong>Hide Information Flow If Conveyed Information Is Missing</strong> <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link> controls the arrow visibility. <ac:link ac:anchor="Showing/hiding the Conveyed Item"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image ac:align="center"><ri:attachment ri:filename="hide_information_flow.png" /></ac:image><br /></span></li><li><span>Now the Conveyed Items in the </span><strong>Create / Edit Item Flow</strong><span> dialog are represented with icons to help you identify the Conveyed Items.</span><span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Conveyed Item Element Icon.png" /></ac:image><br /></span></li><li><span>Item Flow creation between Activity Parameter Nodes and Actions has been enhanced to facilitate the creation of Item Flows when interactions are modeled between Part Properties. Typically, the 'Usage' allocation mode is used for this, which does not create an allocation relation on the end of the Activity Parameter Node, thereby not providing a possible sender or receiver on this end. Now, the tool checks action allocations to typed parts for Activity Parameter Nodes. Consequently, the Direction field in the <strong>Create / Edit Item Flow</strong> dialog displays suggested sender and receiver elements based on the element typing the parts to which actions are allocated.</span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Item Flow between Activity Parameter Node and Action.png" /></ac:image><h6 style="text-align: center;">On the end of the<em> input : Audio data </em>Activity Parameter Node there are no Actions, only the<em> Read and transmit the sound </em>Activity. Thus, the tool checks the model to find Actions that invoke this Activity, locating the<em> : Read and transmit the sound</em> Action in the <em>Listen the audio</em> Activity diagram. <br />Then the tool checks the allocation relationships for this action and an allocation to the <em>: Wireless Earbuds</em> Part Property is found. <br />Using this information the <strong>Create/Edit Item Flow</strong> dialog identifies the <em>Wireless Earbuds</em> Block as a possible sender of the flow, displaying<em> Wireless Earbuds </em>and <em>Processing </em>Blocks as a suggestion for the sender/receiver in the <strong>Direction </strong>field of the dialog.<br /><br /></h6></li><li><span>New validation rules (</span><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Item Flow has no Conveyed Items" /><ac:plain-text-link-body><![CDATA[IFHNCI[2]]]></ac:plain-text-link-body></ac:link><span><span class="error"> and <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Realized Item Flow has no Conveyed Items" /><ac:plain-text-link-body><![CDATA[RIFHNCI[2]]]></ac:plain-text-link-body></ac:link></span></span><span>) have been implemented to highlight Item Flows that do not have any Conveyed Items. This helps to declutter the model and identify potentially unused flows. Learn more on the <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Item Flow has no Conveyed Items" /></ac:link> and <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Realized Item Flow has no Conveyed Items" /></ac:link> pages.</span></li></ul><h3>Connector Redefinition</h3><p><span style="color: rgb(14,16,26);">New validation solvers are available for the <strong>Invalid Connector</strong> validation rule, allowing for an easy connector redefinition:</span></p><ul><li style="list-style-type: disc;"><span style="color: rgb(14,16,26);">Use the <strong>Redefine and Replace Connector</strong> solver to have a new redefining connector created if the selected connector is inherited and at least one of its ends is redefined.</span></li><li style="list-style-type: disc;"><span style="color: rgb(14,16,26);">Use the <strong>Replace with Redefining</strong> solver to replace the failed connector with the redefining one if the failed connector is already redefined in the same context.</span></li></ul><p><span style="color: rgb(14,16,26);"><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Invalid Connector (UML Correctness)" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="image-2024-4-12_8-33-47.png" /></ac:image></p><h6 style="text-align: center;">The image displays how to resolve the <span style="color: rgb(14,16,26);"><strong>Invalid Connector </strong>validation error via the <strong>Redefine and Replace Connector </strong>solver.<strong> </strong></span></h6><h3>MagicGrid Perspective</h3><p>The MagicGrid perspective has been introduced, supplementing existing perspectives, such as Full Featured or System Engineer. This perspective simplifies the modeling tool by providing only the MagicGrid-required subset of SysML elements and diagrams, making it easier to understand and navigate for users new to MagicGrid. You can manually switch perspectives via the <strong>Select Perspective</strong> dialog. Furthermore, a dialog prompting you to switch to this perspective appears whenever you create a MagicGrid project.</p><p><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Selecting perspective" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="MagicGrid_perspective.png" /></ac:image>The MagicGrid perspective available via the <strong>Select Perspective</strong> dialog.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h2>Simulation Features</h2><h3>What's New in Server-Side Simulation</h3><h4 style="margin-left: 40.0px;">Diagram Animation Support</h4><p style="margin-left: 40.0px;"><span style="color: rgb(23,43,77);">The new release supports diagram animation when executing projects on the server. Now behavioral (Activity, State Machine, and Sequence) diagrams can be embedded into HTML-generated user interfaces and are animated during server-side simulation. </span><span><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation with UI" /><ac:plain-text-link-body><![CDATA[Learn more about simulation with UI >>]]></ac:plain-text-link-body></ac:link></span></p><p style="margin-left: 40.0px;"><br /></p><p style="margin-left: 40.0px;text-align: center;"><ac:image><ri:attachment ri:filename="diagram_animation_support.png" /></ac:image></p><h6 style="text-align: center;margin-left: 40.0px;">Diagram animation support in server-side simulation.</h6><h4 style="margin-left: 40.0px;"><br />Other</h4><ul><li style="list-style-type: none;"><ul><li><p><span style="color: rgb(23,43,77);">Now UI titles are displayed in a UI index window and you can use them to open a specific UI in a separate window.</span></p></li><li><span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">Upon successful installation, the Simulation application card is displayed on the Web Application Platform <span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">welcome page</span></span>.<span> </span></span>Opening the application will redirect you to the Server-side Simulation Swagger page.</span></li><li><span style="color: rgb(23,43,77);">The RUN endpoint has a new 'timeout' query parameter which allows you to specify the timeout duration in minutes.</span></li><li><span style="color: rgb(23,43,77);">The 'sync' query parameter has been added to the RUN, STEP, and TERMINATE endpoints. You can use them to initiate a synchronous API call in server-side simulation using Jupyter Notebook.</span></li></ul></li></ul><p style="margin-left: 40.0px;"><br /></p><h3>SSP Export Support</h3><p><span style="color: rgb(33,37,41);"><span style="color: rgb(13,13,13);">This release introduces a powerful new feature - the ability to export model data to the SSP (System Structure and Parameterization) file format. </span>SSP is a tool-independent standard used to define complete systems consisting of one or more FMUs (Functional Mockup Interfaces). <span style="color: rgb(13,13,13);">With this enhancement, you can transfer models between different simulation tools, such as Dymola, facilitating greater interoperability and collaboration. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="SSP Export - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></span></p><p><br /></p><h3>Results Player</h3><p><span style="color: rgb(13,13,13);">Now, the tool can read and play external simulation results from CSV files. You can load CSV files generated either locally or by external tools into the Results Player and then play back the simulation results in your modeling tool. The Results Player offers enhanced playback controls, allowing users to pause playback, navigate through different simulation times using a slider, and adjust playback speed according to their preferences. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Results Player - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="results_player.png" /></ac:image></p><h6 style="text-align: center;">Using the Results Player to play back simulation results from an imported CSV file.</h6><h3><br />Displaying Runtime Values on Port Labels</h3><p>A new<strong> </strong><span style="color: rgb(23,43,77);"><strong>Show Runtime Values on Port Labels</strong> </span>project option and Simulation Configuration property allows you to see runtime values on Port labels during simulation as displayed below. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Manipulating simulation information" /><ac:plain-text-link-body><![CDATA[Learn more about manipulating simulation information >>]]></ac:plain-text-link-body></ac:link></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="showing_runtime_values_on_port_labels.png" /></ac:image></p><h6 style="text-align: center;">Displaying runtime values on Port labels during simulation.</h6><h3><br />Easier Access to Nested Properties</h3><p>You no longer need complex <span style="color: rgb(23,43,77);">ALH (Action Language Helper) scripts to access deeply nested properties. With the Groovy language, you can use &quot;dot notation&quot; directly in any expression.</span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="dot_notation_in_groovy.png" /></ac:image><br /></span></p><h6 style="text-align: center;">Using &quot;dot notation&quot; in the Groovy language.</h6><h3><br />Other Improvements</h3><ul><li><span style="color: rgb(23,43,77);">The new <strong>Show Annotations</strong> project option and Simulation Configuration property allows enabling and disabling simulation annotations in diagrams. Simulation annotations include flowing information, possibility to change animation speed, and annotation tooltips. <ac:link ac:anchor="Enabling and disabling animation options"><ri:page ri:space-key="CST2024xR1" ri:content-title="Displaying simulation information" /><ac:plain-text-link-body><![CDATA[Learn more about animation options >>]]></ac:plain-text-link-body></ac:link></span></li><li><span style="color: rgb(23,43,77);">Matlab integration is now supported for Apple Silicone.</span></li><li><span style="color: rgb(23,43,77);">The ALH.callOperation method has been enhanced and now supports calling operations through ports.</span></li><li>This release introduces several new methods of the built-in math functions.</li><li>Now you can specify the simulation license for SIMULIA when logging in to the <strong>3D</strong>EXPERIENCE platform.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h2><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="815c4f41-7b9a-4abd-a370-16ecd19fe713"><ac:parameter ac:name="">Client side performance improvements</ac:parameter></ac:structured-macro>Client-side Performance Improvements</h2><h3>Improvements in Diagram Export as SVG</h3><p>Exporting diagrams in Scalable Vector Graphics (*.svg) format now features significant optimizations, with the most notable improvements in matrix and table exports:</p><ul><li>Reduction in the file size of exported SVG files.</li><li>Export now requires up to 10 times less RAM resources.</li><li>Decreased duration of the export process.</li></ul><p>These optimizations enhance the efficiency of exporting matrices and tables in SVG format, resulting in significantly reduced file sizes. The improvements impact various functionalities that utilize SVG image generation, such as image export via the MDZipX plugin or the 'Save as Image' command.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="File Size of Dependency Matrix Exported as SVG.png" /></ac:image></p><h6 style="text-align: center;">A chart comparing the file size of a Dependency Matrix exported as a SVG image in 2024x and 2024x Refresh1.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h2><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h2><h3>Information Flow Management Improvements</h3><ul><li>Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Element usage in diagrams" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="Navigate_to_diagram_UML.png" /></ac:image></li><li>Specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><span><br /><ac:image><ri:attachment ri:filename="Specifying Conveyed Information via Diagram Palette.png" /></ac:image><br /></span></li><li>You can no<span style="color: rgb(23,43,77);">w choose whether you want to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified</span>. The <span><strong>Hide Information Flow If Conveyed Information Is Missing</strong> <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link> controls the arrow visibility. <ac:link ac:anchor="Changing the arrow notation visibility"><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="hide_information_flow_UML.png" /></ac:image><br /></span></li><li>Now the Conveyed Information in the New Conveyed Information <span>dialog is represented with icons to help you identify the Conveyed Information. </span><span><br /><ac:image><ri:attachment ri:filename="Conveyed Information Element Icon.png" /></ac:image><br /></span></li><li>New validation rules (<ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[IFHNCI[1]]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[RIFHNCI[1]]]></ac:plain-text-link-body></ac:link>)<span> have been implemented to highlight Information Flows that do not have any Conveyed Information. Learn more on the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /></ac:link> pages.</span></li></ul><h3 style="text-align: left;">Improved Samples Access and Navigation</h3><p><span>From now on, you can review the list of available samples</span><span> anytime by invoking the </span><span>Samples tab. The tab displays all the samples </span><span>provided with the modeling tool installation, providing a convenient way to review and access the needed samples. </span><span>Additionally, you can use the search bar to navigate the available content efficiently both in the Samples and Welcome tabs.</span></p><p><span><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Editor Tabs" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Improved Samples Access and Navigation.png" /></ac:image></p><h3>Other Improvements</h3><ul><li><span>A new </span><strong><span>Letter Spacing Reduction in SVG</span></strong><span> environment option is introduced to control the spacing between letters when exporting diagram images in SVG format</span>. Adjusting letter spacing enables you to maintain text alignment within shape boundaries when exporting, ensuring it does not exceed their borders. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Diagram image export" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h2><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h2><h3>Model Patch Functionality Improvements</h3><p><span style="color: rgb(0,0,0);">We are happy to announce that in this release the Model Patch functionality is coming out of the technology preview phase with several enhancements. </span><span style="color: rgb(0,0,0);">M</span><span style="color: rgb(0,0,0);">odel Patch is a more convenient alternative to a </span>full Model merge or disconnected team collaboration because it <span style="color: rgb(0,0,0);">allows you to move the selected elements or element changes from one model branch to another and transfer only a specific scope of model modifications.</span></p><p><span style="color: rgb(0,0,0);">In this version, we improved the Model Patch UI and introduced a new panel that will help you solve any problems related to model patch application</span><span style="color: rgb(0,0,0);">. This panel lists all the changes that could not be applied and describes the underlying issue for each change. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Model Patch" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="model_patch.png" /></ac:image></p><h6 style="text-align: center;">Model Patch mechanism.</h6><p><br /></p><p style="text-align: center;"><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="changes_that_are_not_applied.png" /></ac:image></span></p><h6 style="text-align: center;">A panel listing the model patch changes that could not be applied.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p><h3>Commit Queues</h3><p><span style="color: rgb(13,13,13);">You now have access to a quicker and more predictable project commit execution at the end of a long working day: simultaneous commits are processed by putting all users in a First-In-First-Out (FIFO) line, ensuring fairness and efficiency in project commits. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(13,13,13);"><ac:image><ri:attachment ri:filename="commit_queues.png" /></ac:image></span></p><h6 style="text-align: center;">The dialog showing your position in the project commit queue.</h6><h3><br />Other</h3><ul><li>Starting with version 2024x Refresh1, <span style="color: rgb(13,13,13);">you won't need to manually</span> specify the Web Application Platform URL to access specific Teamwork Cloud features like Resource Usage Map or global element usage search. Teamwork Cloud will now retrieve the URL automatically.</li><li>Now it will be possible to skip the migration of archived branches when migrating Teamwork Cloud projects, which will significantly reduce the migration time.</li><li>The project comparing functionality no longer requires the Read Resources permission for used projects. However, you still need the Read Resources permission for the main projects you want to compare.</li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h2>Collaboration Powered by <strong>3D</strong>EXPERIENCE Platform</h2><h3>Moving Projects to the <strong>3D</strong>EXPERIENCE Platform</h3><p>We're thrilled to announce a significant step towards collaboration between Teamwork Cloud and the <strong>3D</strong>EXPERIENCE platform. With this release<span>, you will have the ability to move Teamwork Cloud projects to the <strong>3D</strong>EXPERIENCE platform using the server project file format (.szip). </span><span>Previously, the .szip file format facilitated collaboration solely between different Teamwork Cloud servers. However, with version 2024x Refresh1, we have extended its functionality to allow importing projects from .szip files to the </span><strong>3D</strong><span>EXPERIENCE platform as well and <span style="color: rgb(23,43,77);">updating them if a project already exists on the platform.</span></span></p><p><span style="color: rgb(13,13,13);">We hope that you will benefit from this new functionality and stay tuned for further improvements in future releases</span>. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Importing Teamwork Cloud projects to the 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="moving_projects_to_platform.png" /></ac:image></p><h6 style="text-align: center;"><span>Moving projects to the <strong>3D</strong>EXPERIENCE platform by using the server project file format.</span></h6><h3><span><br />Iteration Merge Information</span></h3><p style="text-align: left;">Now the <strong>History</strong> and <strong>Edit Branches</strong> dialogs show <span>if a specific project iteration was merged, as well as the iteration it was merged from.</span></p><p style="text-align: left;"><br /></p><p style="text-align: center;"><span><ac:image><ri:attachment ri:filename="project_history.png" /></ac:image></span></p><h6 style="text-align: center;"><span>The Iteration column of the History dialog displays the project merge information.</span></h6><h3><span>Performance Improvements</span></h3><p><span><span style="color: rgb(23,43,77);">The performance for various basic server operations, especially project opening, has been significantly improved. As you can see in the charts below, now projects on the <strong>3D</strong>EXPERIENCE platform open at least five times faster compared to version 2024x.</span></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="project_opening_performance.png" /></ac:image></p><h6 style="text-align: center;">The charts comparing project opening performance for projects with 2 million elements.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Refresh1 Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170463070 space=MSOSA2024xR1 version=1 -->
## PAGE 00004: 2024x Version News

- page_id: `170463070`
- space_key: `MSOSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024xR1/pages/170463070/2024x+Version+News
- version_number: 1
- version_date: `2024-04-19T13:55:12.895+02:00`
- ancestors: Magic Systems of Systems Architect Documentation
- labels: ['unrestored-unknown-attachment']

### NORMALIZED CONTENT

#### CONTENT-LAYER: 2024x Hot Fix 2 available

753686899

INLINE

#### CONTENT-COLUMN: 2024x Hot Fix 2 available

100.00002%

753686902

INLINE

753686898

INLINE

###### topMagic Systems of Systems Architect

Released: November 10, 2023

In the 2024x version of UAF, significant enhancements have been introduced. Behavior to Structure Synchronization has been enriched, allowing the automatic construction of structure models from defined activities and enabling one-click generation of Internal Connectivity diagrams.

Diagramming improvements include specialized Security Process Flow diagrams aligned with Operational and Resource viewpoints and new NAFv4 Structure diagrams for Logical, Service, and Physical Resource Specification Viewpoints.

Additionally, the Strategic Viewpoint now offers simplified assembly tools, such as the Strategic Motivation Table and the Impact Matrix, enhancing analysis and traceability. Exchange management has been refined for better visibility control, and various dialogs have been optimized for efficient review and management. These enhancements, along with improved library support and renamed perspectives, provide you with a more intuitive and efficient modeling experience.

In SysML modeling, the 2024x release introduces several improvements to Item Flow creation and editing. The **Create / Edit Item Flow**dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition, **Autowire Parts** and **Delegate Port(s)** commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the **Delegate Port(s)** command functionality regarding nested ports is now improved to treat each displayed nested port individually.

For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.

Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.

We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.

To download the latest version, see [Downloading installation files](https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files). For further information, check the product documentation.

#### NOTE: 2024x Hot Fix 2 available

2024x Hot Fix 2 available

2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 2 Version News' space='NMDOC']>]]>

243271308

INLINE

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
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ac060d11-24bb-43ee-828b-bfae5b72f6eb"><ac:parameter ac:name="id">753686899</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d04429d1-af39-4fcc-95f9-34e91a0b1fb5"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">753686902</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b48c2588-a107-48c6-a871-e57a5ff43535"><ac:parameter ac:name="id">753686898</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5 style="text-align: center;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fd7d672f-fb01-4e70-8982-8ff70256549a"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro>Magic Systems of Systems Architect</h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released: November 10<span style="color: rgb(128,128,128);">,</span> <span style="color: rgb(128,128,128);"> 2023</span> </span></p><p><br /></p><p>In the 2024x version of UAF, significant enhancements have been introduced. Behavior to Structure Synchronization has been enriched, allowing the automatic construction of structure models from defined activities and enabling one-click generation of Internal Connectivity diagrams.</p><p>Diagramming improvements include specialized Security Process Flow diagrams aligned with Operational and Resource viewpoints and new NAFv4 Structure diagrams for Logical, Service, and Physical Resource Specification Viewpoints.</p><p>Additionally, the Strategic Viewpoint now offers simplified assembly tools, such as the Strategic Motivation Table and the Impact Matrix, enhancing analysis and traceability. Exchange management has been refined for better visibility control, and various dialogs have been optimized for efficient review and management. These enhancements, along with improved library support and renamed perspectives, provide you with a more intuitive and efficient modeling experience.</p><p><span style="color: rgb(62,63,64);">In SysML modeling, the 2024x release introduces several improvements to Item Flow creation and editing. The<span> </span> <strong>Create / Edit Item Flow<span> </span> </strong>dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition,<span> </span> <strong style="text-align: left;">Autowire Parts</strong> <span> </span>and<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>command functionality regarding nested ports is now improved to treat each displayed nested port individually.</span></p><p><span>For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</span></p><p><span>Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.</span></p><p><span>We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.</span></p><p>To download the latest version, see <a href="https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files">Downloading installation files</a>. For further information, check the product documentation.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5a9d3003-fadd-4a35-b8e1-c0e247955c61"><ac:parameter ac:name="title">2024x Hot Fix 2 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Hot Fix 2 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c7e26ed7-b7c9-4b37-8bde-4953e68aaa48"><ac:parameter ac:name="id">243271308</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong> <ac:link ac:anchor="UAF 1.2 Features" /> </strong></p><ul><li><ac:link ac:anchor="UAF Behavior to Structure Synchronization" /></li><li><ac:link ac:anchor="Diagramming" /><ul><li><ac:link ac:anchor="New Security Process Flow diagrams" /></li><li><ac:link ac:anchor="New NAFv4 Structure diagrams" /></li><li><ac:link ac:anchor="New views in Strategic Viewpoint" /></li></ul></li><li><ac:link ac:anchor="Exchange management improvements" /><ul><li><ac:link ac:anchor="Exchange visibility management" /></li><li><ac:link ac:anchor="Realized Exchange wizard improvements" /></li><li><ac:link ac:anchor="Exchange Manager improvements" /></li><li><ac:link ac:anchor="Producing and Consuming Functions dialog improvements" /></li></ul></li><li><ac:link ac:anchor="Library Support" /></li><li><ac:link ac:anchor="Templates and Perspectives" /></li><li><ac:link ac:anchor="Other Enhancements" /></li></ul><p><strong> <ac:link ac:anchor="SysML Features" /> </strong></p><ul><li><ac:link ac:anchor="Improved Item Flow Creation and Editing" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Discontinued Features" /> </strong></p><ul><li><ac:link ac:anchor="JavaScript Nashorn Scripting" /></li><li><ac:link ac:anchor="Record Macro Functionality" /></li><li><ac:link ac:anchor="SPEM Plugin" /></li></ul><p><strong> <ac:link ac:anchor="Known Migration Issues" /> </strong></p><p><strong> <ac:link ac:anchor="Modeling and Infrastructure" /> </strong></p><ul><li><ac:link ac:anchor="DSLS Licensing" /></li><li><ac:link ac:anchor="Zoom in Model Browser" /></li><li><ac:link ac:anchor="Advanced Legend Adornments in Tables" /></li><li><ac:link ac:anchor="MIother"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"> <ac:link ac:anchor="Collaboration" /> </strong></p><ul><li><ac:link ac:anchor="Teamwork Cloud" /><ul><li><ac:link ac:anchor="New File Exchange Format for Server Projects" /></li><li><ac:link ac:anchor="Model Patch Mechanism (Technology Preview)" /></li></ul></li><li><ac:link ac:anchor="Power"><ac:plain-text-link-body><![CDATA[Power'By]]></ac:plain-text-link-body></ac:link><ul><li><ac:link ac:anchor="New Features to Manage Used Projects" /></li><li><ac:link ac:anchor="Opening Projects in Read-Only Mode" /></li></ul></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8b326b1a-84ea-4b7a-97b9-fd2d178c5b46"><ac:parameter ac:name="id">753686901</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5>UAF 1.2 Features</h5><h3>UAF Behavior to Structure Synchronization</h3><p>In the 2024x version, the UAF Behavior to Structure Synchronization has been enhanced. Now, you can automatically build the structure model according to defined Activities and generate an Internal Connectivity diagram by executing a single-click command. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Creating structure models by behavior models" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="internal_connectivity_diagram_by_begavior_model_news.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Diagramming</h3><h4>New Security Process Flow diagrams</h4><p>With version 2024x, the Security Process flow diagram has been specialized to align with two distinct Operational and Resource viewpoints, which led to the creation of two new diagrams: Security Process Flow (Operational) and Security Process Flow (Resource).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Security Process Flow diagrams.png" /></ac:image></p><h4>New NAFv4 Structure diagrams</h4><p>New structure diagrams have been implemented in the Logical, Service, and Physical Resource Specification Viewpoints:</p><ul><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="L2 Logical Scenario" /></ac:link> </li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="S2 Service Structure" /></ac:link></li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="P2 Resource Structure" /></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><h4>         </h4><h4>New views in Strategic Viewpoint</h4><p>Beginning with this version, the following new views related to the Strategic Viewpoint are introduced:</p><ul><li><strong>Strategic Motivation Table</strong>, which you can find under the UAF Strategy Diagrams category, is designed to simplify the assembly of UAF Strategic requirements, such as Enterprise Goals and Enterprise Objectives, in a tabular format. </li><li><strong>Impact Matrix</strong>, which you can find under the UAF Analysis Diagrams category, illustrates the mapping between the Strategic, Operational, Resource, Service Viewpoint Elements and Strategic Viewpoint Elements using the Impacted By relationship.</li></ul></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="3fa4aaf2-b093-4c8b-92e0-86d9bfccc5fd"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=ngOqW2UVOSI&amp;ab_channel=CATIAMBSE" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Exchange management improvements</h3><p style="text-align: left;">This version adds significant enhancements to working with exchanges, including the ability to control their visibility on diagrams. Improved exchange creation wizards and management dialogs provide greater clarity.</p><h4 style="text-align: left;">Exchange visibility management</h4><p style="text-align: left;">Now, you can easily manage the visibility of realized exchanges in the diagrams. The dedicated button in the smart manipulator toolbar allows you to choose whether you want to show or hide required Exchange Items.</p><p style="text-align: left;"><ac:image ac:align="center"><ri:attachment ri:filename="show_operational_exchanges.png" /></ac:image></p><h6 style="text-align: center;">This is an example of managing the visibility of Operational Exchange Items in an Operational Internal Connectivity diagram.</h6><h4><span>Realized Exchange wizard improvements </span></h4><p><span>Additionally, 2024x brings a more focused approach to reviewing Activity pairs connected with existing Activity Edges in the </span> <strong>Realized Exchange wizards,</strong> <span> improving overall usability and clarity.</span></p><ul><li>In the second step, our focus has shifted solely to reviewing existing Activity Pairs connected by existing Activity Edges. This means that creating new Activity pairs or editing existing ones is no longer possible. As a result, the tool will no longer trigger the automatic generation of new elements or diagrams.</li><li>We've introduced a new step called <strong>Affected Diagrams</strong>. This step lets you see where changes will occur after realizing elements or editing existing exchanges.</li></ul><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="Exchange management changes.png" /></ac:image> </span> <span>An example of changes in the Realized Resource Exchange creation wizard.</span></h6><h4><span>Exchange Manager improvements</span></h4><p>In this release, we've made improvements to the <strong>Exchange Managers</strong>. Now, you'll find a handy <strong>Affected Diagrams</strong> button that opens a dialog listing all the diagrams containing elements that already realize the selected exchange.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="echanges_exchange_manager.png" /></ac:image> </span> <span>An example of changes in the Operational Exchange Manager. </span></h6><h4><span>Producing and Consuming Functions dialog improvements</span></h4><p>We've made some changes in the Producing and Consuming Activities/Functions dialogs as well. They now serve as tools for reviewing Activity pairs and easily removing any unnecessary ones.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="changes_producing_consuming_activities.png" /></ac:image>An example of changes in the Producing and Consuming Activities dialog.</span></h6><h3>Library Support</h3><p>New DISR and UJTL library versions are now available:</p><ul><li>UJTL (20230616)</li><li>DISR (<span style="color: rgb(23,43,77);">20230523</span>)</li></ul><p><span style="color: rgb(62,63,64);">You can choose the library version when creating a new project. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Using libraries" /><ac:plain-text-link-body><![CDATA[Learn more about using libraries >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Templates and Perspectives</h3><h4>New template</h4><ul><li>A new <span style="color: rgb(23,43,77);"> <strong>EA Project Template with Process Guide</strong> is now available in UAF. This Enterprise Architecture (EA) Guide defines a workflow for creating EA views following the Unified Architecture Framework Modeling Language (UAFML). When using this template, you will receive a new UAF project enhanced with the EA Guide for UAF. This modeling guide aids in building architecture by providing nine steps of workflow.</span></li></ul><h4><span style="color: rgb(23,43,77);">Renamed </span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF Enterprise Architecture Project</strong> was renamed to <strong>EA with BPMN Project</strong>. Using the <strong>EA with BPMN Project</strong> template, you will get a simplified Enterprise Architecture project with BPMN, which is based on the UAF framework and designed for enterprise and IT architecture modeling. Creating an EA with the BPMN project will switch the modeling tool to the EA-BPMN Architect graphical user interface and use the EA with the BPMN model template.</span></li><li><span style="color: rgb(23,43,77);">The perspective <strong style="text-align: left;">UAF Enterprise Architect</strong> <span> was renamed </span>to<span> </span> <strong style="text-align: left;">EA-BPMN Architect. </strong> <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Select Perspective dialog" /><ac:plain-text-link-body><![CDATA[Learn more about the perspectives >>>]]></ac:plain-text-link-body></ac:link> </span></li></ul><h4><span style="color: rgb(23,43,77);">Removed</span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF EA Project Template with Process Guide</strong> was removed.</span></li></ul><h3>Other Enhancements</h3><ul><li><span style="color: rgb(23,43,77);">The nested ports in all relevant viewpoints are now supported.</span></li><li>The options for <strong>Information Flows</strong> in the <strong>Environment Options</strong> dialog under the <strong>UAF </strong>options group are no longer available.</li><li>The<span> </span> <strong>Tools</strong> <span> </span>option group containing the<span> </span> <strong>Autowire Parts</strong> <span> </span>action is removed from the UAF Parametric Diagram toolbar.</li><li>The <strong>Delegate Port(s)</strong> <span> </span>action is now implemented in the Internal Connectivity Diagrams and is available from the <span style="color: rgb(23,43,77);">diagrams toolbar and context menu of roles, connectors, and ports</span>.</li><li><span style="color: rgb(23,43,77);">You can now create the Vision Statement in the <strong>Specification </strong>window of the Vision element.</span></li><li><span style="color: rgb(23,43,77);">New correctness validation rules regarding the Motivated By relationship are now available. These rules check if the Motivated By relationship is created between correct pairs.</span></li><li><span style="color: rgb(23,43,77);">A new passive validation rule COR2361 is implemented. This rule checks if an Operation Port Class Property type is correct.</span></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="90bd7b1e-43b6-43f5-8025-5097e80fab78"><ac:parameter ac:name="id">244508097</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>SysML Features</h5><h3>Improved Item Flow Creation and Editing</h3><p><span>SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the </span> <strong>Create / Edit Item Flow </strong> <span>dialog, improving overall usability and clarity.</span></p><ul><li><span>Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:</span><ul><li><span>New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams. </span></li><li>The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in <span>a well-organized diagram list in the third step, accurately representing selected options.</span></li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Improved_Item_Flow.png" /></ac:image></p><h6 style="text-align: center;">A comparison of some of the changes in the second step of the <strong>Create / Edit Item Flow</strong> dialog between versions 2024x and 2022x Refresh2.</h6><p><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more about Item Flow creation and editing >>]]></ac:plain-text-link-body></ac:link> </p><h3>Other Improvements</h3><ul><li>The <strong>Tools</strong> option group containing <strong>Autowire Parts</strong> and <strong>Delegate Port(s)</strong> commands has been removed from the SysML Parametric Diagram toolbar. Both <strong>Delegate Port(s)</strong> and <strong>Autowire Parts</strong> commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.</li><li>Improved <strong>Delegate Port(s)</strong> command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. <ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Automatic delegation" /><ac:plain-text-link-body><![CDATA[Learn more about automatic delegation >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="76d426b3-d26b-4be9-8310-6bc9193da35c"><ac:parameter ac:name="id">256630726</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Discontinued Features</h5><p>The following features have been discontinued with the 2024x version release.</p><h3>JavaScript Nashorn Scripting</h3><p><span style="color: rgb(62,63,64);">The JavaScript<span> </span> </span>Nashorn <span style="color: rgb(62,63,64);">language usage has been removed from the modeling tool. Please use JavaScript<span> </span> <em>Rhino</em> instead<em>. </em>This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Deprecated JavaScript Nashorn" /><ac:plain-text-link-body><![CDATA[Learn more about the deprecated JavaScript Nashorn >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Record Macro Functionality </h3><p>The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.</p><h3>SPEM Plugin</h3><p>The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.</p><h5>Known Migration Issues</h5><p>Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.</p><p>To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the &lt;modeling_tool_install_dir&gt;\bin\&lt;modeling_tool&gt;.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="79ae8693-d2ab-4747-accb-c1b9c1c7b0bd"><ac:parameter ac:name="id">272319258</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Modeling and Infrastructure</h5><h3>DSLS Licensing</h3><p>Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:</p><ul><li>License usage statistics, debugging, and simple UI to administer and view statistics.</li><li>Licenses are bound to their expiration date rather than the product version.</li><li>Nodelock (seat), floating, and managed licensing options.</li></ul><p>Thus, now you can choose to use either FlexNet or DSLS for product licensing. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f49ff8d-45a1-456c-a2a0-a919be8c1f02"><ac:rich-text-body><p>The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version <span>R2024x with modeling tool version 2024x</span>).</p></ac:rich-text-body></ac:structured-macro><p><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS Licensing >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9484f639-acef-4728-8acc-d1e2338719d2"><ac:parameter ac:name="">Zoom in Model Browser</ac:parameter></ac:structured-macro>Zoom in Model Browser</h3><p>From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking. </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Zoom in Model Browser.png" /></ac:image></p><h6 style="text-align: center;">Zooming in the Model Browser using keyboard shortcuts.</h6><p><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /><ac:plain-text-link-body><![CDATA[Learn more about zooming in the Model Browser>>]]></ac:plain-text-link-body></ac:link></p><h3>Advanced Legend Adornments in Tables</h3><p>In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Advanced Legend Adornments in Tables Example.png" /></ac:image></p><h6 style="text-align: center;">Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item <em>In Progress</em>.</h6><p style="text-align: right;"><br /></p><h3 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6c8c8907-e1fd-4c63-9547-aff205bb1046"><ac:parameter ac:name="">MIother</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li><strong>OpenJDK version update. </strong>Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version. </li><li><strong> <span style="color: rgb(62,63,64);">Supported operating system changes for Linux. </span> </strong> <span style="color: rgb(62,63,64);">CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support. </span></li><li><strong>JavaScript Rhino version update.</strong> The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</li><li>It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.</li></ul><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9de59458-bf62-4484-8bac-bf7d69a0b745"><ac:parameter ac:name="id">243174490</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h5><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="82578d71-581b-42b4-bfdc-d5dcd49ff7cd"><ac:parameter ac:name="">TWC</ac:parameter></ac:structured-macro> </span>Teamwork Cloud</h3><h4 style="text-align: left;">New File Exchange Format for Server Projects</h4><p>In version 2022x Refresh2, we introduced <strong>.szip</strong> – a new <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using server project file format" /><ac:plain-text-link-body><![CDATA[server project exchange format]]></ac:plain-text-link-body></ac:link>. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.</p><p>In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="600"><ri:attachment ri:filename="project_exchange_options.png" /></ac:image></h6><p style="margin-left: 0.0in;"><span style="color: rgb(0,0,0);">The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.</span></p><p style="margin-left: 0.0in;"><br /></p><p style="margin-left: 0.0in;text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image><ri:attachment ri:filename="szip_project_import_performance.png" /></ac:image> <ac:image><ri:attachment ri:filename="szip_project_export_performance.png" /></ac:image> </span></p><h6 style="text-align: center;">Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).</h6><p><br /></p><h4>Model Patch Mechanism (Technology Preview)</h4><p><span style="color: rgb(0,0,0);">We introduce the technology preview of the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Patch - Technology preview" /><ac:plain-text-link-body><![CDATA[Model Patch mechanism]]></ac:plain-text-link-body></ac:link>, a more lightweight way to move model changes. Model Patch can help you:</span></p><ul><li><span style="color: rgb(0,0,0);">Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;</span></li><li><span style="color: rgb(0,0,0);">Transfer only a specific scope of model changes between disconnected teams instead of the entire model;</span></li><li>Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.</li></ul><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="model_patch_mechanism.jpg" /></ac:image></h6><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfdd0694-20ca-468f-858e-b8118a0d2206"><ac:parameter ac:name="">Power</ac:parameter></ac:structured-macro> </span>Power’By</h3><h4>New Features to Manage Used Projects</h4><p><span style="color: rgb(0,0,0);">We added new features that provide you with better capabilities to manage used projects in <strong>3D</strong>EXPERIENCE:</span></p><ul><li><span style="color: rgb(0,0,0);">Export packages as a new server project;</span></li><li><span style="color: rgb(0,0,0);">Move elements to/from used projects;</span></li><li><span style="color: rgb(0,0,0);">Import used projects.</span></li></ul><h4><span style="color: rgb(0,0,0);">Opening Projects in Read-Only Mode</span></h4><p><span style="color: rgb(0,0,0);">Beginning with version 2024x, you can open <strong>3D</strong>EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.</span></p><p style="text-align: center;"><ac:image ac:height="96"><ri:attachment ri:filename="3DEXPERIENCE_project_editing_disabled.jpg" /></ac:image></p><h6 style="text-align: center;">Notification informing the user that the <strong>3D</strong>EXPERIENCE project is read-only.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to Top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="da45258d-6386-4b80-af5a-54f24ceca0df"><ac:parameter ac:name="id">430554266</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong> <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link> </strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170463068 space=MSOSA2024xR1 version=2 -->
## PAGE 00005: Magic Systems of Systems Architect Documentation

- page_id: `170463068`
- space_key: `MSOSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024xR1/pages/170463068/Magic+Systems+of+Systems+Architect+Documentation
- version_number: 2
- version_date: `2024-05-09T10:31:40.691+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

1430502845

1430502848

1430502847

This is the home page of Magic Systems of Systems Architect documentation.

Magic Systems of Systems Architect is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to **enterprise architecture** needs.

The documentation of Magic Systems of Systems Architect is a package that includes the documentation of these capabilities:

**[CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024xR1']**

Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.

Type a search phrase...

**[CONFLUENCE_PAGE title='UAF 1.2 Plugin Documentation' space='UAF12P2024xR1']**

Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='UPDM 2 Plugin Documentation' space='UPDM2P2024xR1']**

Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR1']**

Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.

Type a search phrase...

**[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024xR1']**

Guides you through the import, export, and management of SysML requirements.

Type a search phrase...

**[CONFLUENCE_PAGE title='Magic Concept Modeler Documentation' space='MCM2024xR1']**

Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain.

Type a search phrase...

1302769756

##### Additional information

**[CONFLUENCE_PAGE title='Installation, Licensing, and System Requirements Documentation' space='IL2024xR1']**

Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation.

**[CONFLUENCE_PAGE title='Magic Model Analyst Documentation' space='MSI2024xR1']**

Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.

Type a search phrase...

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="49da89cf-930a-42d6-93ee-2f9e7644bd43"><ac:parameter ac:name="id">1430502845</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="30c2055f-6f1d-4a38-baef-0c400c8a8d15"><ac:parameter ac:name="id">1430502848</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="af7f9153-5c44-4383-9ba9-772e6f6b9b8d"><ac:parameter ac:name="id">1430502847</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>This is the home page of Magic Systems of Systems Architect documentation.</p><p>Magic Systems of Systems Architect is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to <strong>enterprise architecture</strong> needs.</p><p>The documentation of Magic Systems of Systems Architect is a package that includes the documentation of these capabilities:</p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[General Capabilities]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="5bc3601d-dfda-423a-a1f9-5fad722b3da5"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MD2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><span class="confluence-link"><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="UAF 1.2 Plugin Documentation" /><ac:plain-text-link-body><![CDATA[UAF 1.2 modeling]]></ac:plain-text-link-body></ac:link></span></span></strong></p><p>Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="bb9cd62a-0132-4e5c-be61-9e16054d2897"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UAF12P2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="UPDM2P2024xR1" ri:content-title="UPDM 2 Plugin Documentation" /><ac:plain-text-link-body><![CDATA[UPDM 2 modeling]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="e187fc76-cd3c-4740-8beb-d9d0f852e55b"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UPDM2P2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML modeling]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="3fc35616-300a-42dd-92da-2e6df0cdf95a"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="SYSMLP2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024xR1" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Requirements modeling]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Guides you through the import, export, and management of SysML requirements.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="f848973d-7582-4859-82e3-3b18632cb75b"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CRMP2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"><ac:link><ri:page ri:space-key="MCM2024xR1" ri:content-title="Magic Concept Modeler Documentation" /><ac:plain-text-link-body><![CDATA[Concept modeling]]></ac:plain-text-link-body></ac:link></strong></p><p><span style="color: rgb(62,63,64);">Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain. </span></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="992ea157-ee69-4f67-b011-552563f98523"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MCM2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="652c9857-7149-4821-87a6-a108bbd88f32"><ac:parameter ac:name="id">1302769756</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><h3>Additional information</h3></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installation, Licensing, and System Requirements Documentation" /><ac:plain-text-link-body><![CDATA[Installation and licensing]]></ac:plain-text-link-body></ac:link></strong></p><p>Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation. </p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="MSI2024xR1" ri:content-title="Magic Model Analyst Documentation" /><ac:plain-text-link-body><![CDATA[Simulation]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.</p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="3384cd9a-b724-4729-82d9-70f810a549ee"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MSI2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170463090 space=MSOSA2024xR1 version=1 -->
## PAGE 00006: Support

- page_id: `170463090`
- space_key: `MSOSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024xR1/pages/170463090/Support
- version_number: 1
- version_date: `2023-09-22T13:04:14.309+02:00`
- ancestors: Magic Systems of Systems Architect Documentation
- labels: []

### NORMALIZED CONTENT

1906792292

1906792294

1906792293

For information about the support, please visit: [https://www.3ds.com/support/](https://www.3ds.com/support/)

##### Reporting an Issue

If you encounter an issue or the modeling tool becomes unresponsive, a separately executable tool is provided for analyzing the status of the process to aid in bug submission.In these situations, manually start the *submit_issue.exe* file (located in the *<modeling tool installation directory>\bin folder*).After you start *submit_issue.exe*, the**Report an Issue** dialog opens.

In this dialog, you can easily dump threads or memory heap into files and provide those files when reporting an issue to the support team.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f491134c-1f31-440c-b0cd-49219bca45e2"><ac:parameter ac:name="id">1906792292</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="92d28415-56a9-4da3-bb95-f0f1d439792a"><ac:parameter ac:name="id">1906792294</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b02bd87b-9182-47bc-8dbd-8936e128fbf2"><ac:parameter ac:name="id">1906792293</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2602c0ae-4d92-45ef-b3a9-b208e2028088"><ac:rich-text-body><p>For information about the support, please visit: <a href="https://www.3ds.com/support/">https://www.3ds.com/support/</a></p></ac:rich-text-body></ac:structured-macro><h3>Reporting an Issue</h3><p><span style="color: rgb(0,0,0);">If you encounter an issue or the modeling tool becomes unresponsive, a separately executable tool is provided for analyzing the status of the process to aid in bug submission. </span><span style="color: rgb(0,0,0);">In these situations, manually start the <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em> file (located in the <em>&lt;modeling tool installation directory&gt;\bin folder</em>). </span><span style="color: rgb(0,0,0);">After you start <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em>, the </span><strong>Report an Issue</strong> dialog <span style="color: rgb(0,0,0);">opens. </span></p><p><span style="color: rgb(0,0,0);">In this dialog, you can easily dump threads or memory heap into files and provide those files when reporting an issue to the support team.</span></p><p><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="report_issue.png"><ri:page ri:space-key="MSOSA2024xR1" ri:content-title="Support" /></ri:attachment></ac:image><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=170463088 space=MSOSA2024xR1 version=2 -->
## PAGE 00007: Using UAF and UPDM2 plugins in Magic Systems of Systems Architect

- page_id: `170463088`
- space_key: `MSOSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024xR1/pages/170463088/Using+UAF+and+UPDM2+plugins+in+Magic+Systems+of+Systems+Architect
- version_number: 2
- version_date: `2024-05-09T10:32:33.899+02:00`
- ancestors: Magic Systems of Systems Architect Documentation
- labels: []

### NORMALIZED CONTENT

##### Choosing the default plugin

Before the first startup of the Magic Systems of Systems Architect, you can set which plugin - UAF or UPDM2 - will be installed by default. If no changes are made, by default UAF plugin is installed.

To change the default plugin before the first startup

1. Go to the <msosa_install_dir>\bin\ and open for editing the msosa.properties file.
2. In the file, find the system property -Dstart.application.with.updm2.or.uaf.plugin=uaf
3. Change the uaf value to updm2 .
4. Save the file and start the Magic Systems of Systems Architect modeling tool.

In case you will decide to change the plugin later, see chapter [CONFLUENCE_PAGE title='Changing between UAF and UPDM 2 plugins' space='UAF12P2024xR1'] for information about how to do that.

##### Displaying which plugin is installed

You can choose to display the plugin name in brackets next to the Magic Systems of Systems Architect title in the modeling tool's title bar.

To display the installed plugin name near the modeling tool title

1. Go to the <msosa_install_dir>\bin\ and open for editing the msosa.properties file.
2. In the file, find the system property -Dadd.plugin.name.to.application.title\=false
3. Change the property value to true .
4. Save the file and start the Magic Systems of Systems Architect modeling tool.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Choosing the default plugin</h3><p>Before the first startup of the Magic Systems of Systems Architect, you can set which plugin - UAF or UPDM2 - will be installed by default. If no changes are made, by default UAF plugin is installed.</p><p><br /></p><p>To change the default plugin before the first startup</p><hr /><ol><li>Go to the &lt;msosa_install_dir&gt;\bin\ and open for editing the <em>msosa.properties</em> file.</li><li>In the file, find the system property <em>-Dstart.application.with.updm2.or.uaf.plugin=uaf</em></li><li>Change the <em>uaf</em> value to <em>updm2</em>.</li><li>Save the file and start the Magic Systems of Systems Architect modeling tool.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c93f7330-b046-4e85-be90-7075c3f9d206"><ac:rich-text-body><p>In case you will decide to change the plugin later, see chapter <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Changing between UAF and UPDM 2 plugins" /></ac:link> for information about how to do that.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Displaying which plugin is installed</h3><p>You can choose to display the plugin name in brackets next to the Magic Systems of Systems Architect title in the modeling tool's title bar. </p><p><br /></p><p>To display the installed plugin name near the modeling tool title</p><hr /><ol><li>Go to the &lt;msosa_install_dir&gt;\bin\ and open for editing the <em>msosa.properties</em> file.</li><li>In the file, find the system property <em>-Dadd.plugin.name.to.application.title\=false</em></li><li>Change the <em>property </em>value to <em>true</em>.</li><li>Save the file and start the Magic Systems of Systems Architect modeling tool.</li></ol><p><ac:image><ri:attachment ri:filename="plugin_name_in_title.png" /></ac:image></p>
````
