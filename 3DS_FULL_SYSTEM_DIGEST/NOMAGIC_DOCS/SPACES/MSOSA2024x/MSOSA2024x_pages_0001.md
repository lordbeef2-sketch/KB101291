# NOMAGIC DOCUMENTATION SPACE: Magic Systems of Systems Architect 2024x

<!--NOMAGIC_SPACE key=MSOSA2024x chunk=1 -->

<!--NOMAGIC_PAGE id=137989986 space=MSOSA2024x version=2 -->
## PAGE 00001: 2022x News for Developers

- page_id: `137989986`
- space_key: `MSOSA2024x`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024x/pages/137989986/2022x+News+for+Developers
- version_number: 2
- version_date: `2024-01-31T11:24:25.550+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='2022x News for Developers' space='MD2022x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="7bca5887-f302-4e35-9131-f75eea6694e5"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2022x" ri:content-title="2022x News for Developers" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=137989959 space=MSOSA2024x version=1 -->
## PAGE 00002: 2022x Version News

- page_id: `137989959`
- space_key: `MSOSA2024x`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024x/pages/137989959/2022x+Version+News
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

<!--NOMAGIC_PAGE id=142934839 space=MSOSA2024x version=20 -->
## PAGE 00003: 2024x Version News

- page_id: `142934839`
- space_key: `MSOSA2024x`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024x/pages/142934839/2024x+Version+News
- version_number: 20
- version_date: `2025-11-27T13:45:20.098+01:00`
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

#### CONTENT-BLOCK: 2024x Hot Fix 2 available

243271308

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

#### NOTE: 2024x Hot Fix 3 available

2024x Hot Fix 3 available

2024x Hot Fix 3 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 3 Version News' space='CATIA']>]]>

#### NOTE: 2024x Hot Fix 2 available

2024x Hot Fix 2 available

2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 2 Version News' space='CATIA']>]]>

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
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ac060d11-24bb-43ee-828b-bfae5b72f6eb"><ac:parameter ac:name="id">753686899</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d04429d1-af39-4fcc-95f9-34e91a0b1fb5"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">753686902</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><br /><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="c7e26ed7-b7c9-4b37-8bde-4953e68aaa48"><ac:parameter ac:name="id">243271308</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5 style="text-align: center;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fd7d672f-fb01-4e70-8982-8ff70256549a"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro>Magic Systems of Systems Architect</h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released: November 10, 2023 </span></p><p><br /></p><p>In the 2024x version of UAF, significant enhancements have been introduced. Behavior to Structure Synchronization has been enriched, allowing the automatic construction of structure models from defined activities and enabling one-click generation of Internal Connectivity diagrams.</p><p>Diagramming improvements include specialized Security Process Flow diagrams aligned with Operational and Resource viewpoints and new NAFv4 Structure diagrams for Logical, Service, and Physical Resource Specification Viewpoints.</p><p>Additionally, the Strategic Viewpoint now offers simplified assembly tools, such as the Strategic Motivation Table and the Impact Matrix, enhancing analysis and traceability. Exchange management has been refined for better visibility control, and various dialogs have been optimized for efficient review and management. These enhancements, along with improved library support and renamed perspectives, provide you with a more intuitive and efficient modeling experience.</p><p><span style="color: rgb(62,63,64);">In SysML modeling, the 2024x release introduces several improvements to Item Flow creation and editing. The<span> </span> <strong>Create / Edit Item Flow<span> </span> </strong>dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition,<span> </span> <strong style="text-align: left;">Autowire Parts</strong> <span> </span>and<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>command functionality regarding nested ports is now improved to treat each displayed nested port individually.</span></p><p><span>For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</span></p><p><span>Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.</span></p><p><span>We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.</span></p><p>To download the latest version, see <a href="https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files">Downloading installation files</a>. For further information, check the product documentation.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a672b7b3-8ef4-458a-b61f-9c4fafd6dc87"><ac:parameter ac:name="title">2024x Hot Fix 3 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 3 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Hot Fix 3 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="5a9d3003-fadd-4a35-b8e1-c0e247955c61"><ac:parameter ac:name="title">2024x Hot Fix 2 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Hot Fix 2 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong> <ac:link ac:anchor="UAF 1.2 Features" /> </strong></p><ul><li><ac:link ac:anchor="UAF Behavior to Structure Synchronization" /></li><li><ac:link ac:anchor="Diagramming" /><ul><li><ac:link ac:anchor="New Security Process Flow diagrams" /></li><li><ac:link ac:anchor="New NAFv4 Structure diagrams" /></li><li><ac:link ac:anchor="New views in Strategic Viewpoint" /></li></ul></li><li><ac:link ac:anchor="Exchange management improvements" /><ul><li><ac:link ac:anchor="Exchange visibility management" /></li><li><ac:link ac:anchor="Realized Exchange wizard improvements" /></li><li><ac:link ac:anchor="Exchange Manager improvements" /></li><li><ac:link ac:anchor="Producing and Consuming Functions dialog improvements" /></li></ul></li><li><ac:link ac:anchor="Library Support" /></li><li><ac:link ac:anchor="Templates and Perspectives" /></li><li><ac:link ac:anchor="Other Enhancements" /></li></ul><p><strong> <ac:link ac:anchor="SysML Features" /> </strong></p><ul><li><ac:link ac:anchor="Improved Item Flow Creation and Editing" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Discontinued Features" /> </strong></p><ul><li><ac:link ac:anchor="JavaScript Nashorn Scripting" /></li><li><ac:link ac:anchor="Record Macro Functionality" /></li><li><ac:link ac:anchor="SPEM Plugin" /></li></ul><p><strong> <ac:link ac:anchor="Known Migration Issues" /> </strong></p><p><strong> <ac:link ac:anchor="Modeling and Infrastructure" /> </strong></p><ul><li><ac:link ac:anchor="DSLS Licensing" /></li><li><ac:link ac:anchor="Zoom in Model Browser" /></li><li><ac:link ac:anchor="Advanced Legend Adornments in Tables" /></li><li><ac:link ac:anchor="MIother"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"> <ac:link ac:anchor="Collaboration" /> </strong></p><ul><li><ac:link ac:anchor="Teamwork Cloud" /><ul><li><ac:link ac:anchor="New File Exchange Format for Server Projects" /></li><li><ac:link ac:anchor="Model Patch Mechanism (Technology Preview)" /></li></ul></li><li><ac:link ac:anchor="Power"><ac:plain-text-link-body><![CDATA[Power'By]]></ac:plain-text-link-body></ac:link><ul><li><ac:link ac:anchor="New Features to Manage Used Projects" /></li><li><ac:link ac:anchor="Opening Projects in Read-Only Mode" /></li></ul></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8b326b1a-84ea-4b7a-97b9-fd2d178c5b46"><ac:parameter ac:name="id">753686901</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5>UAF 1.2 Features</h5><h3>UAF Behavior to Structure Synchronization</h3><p>In the 2024x version, the UAF Behavior to Structure Synchronization has been enhanced. Now, you can automatically build the structure model according to defined Activities and generate an Internal Connectivity diagram by executing a single-click command. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Creating structure models by behavior models" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="internal_connectivity_diagram_by_begavior_model_news.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Diagramming</h3><h4>New Security Process Flow diagrams</h4><p>With version 2024x, the Security Process flow diagram has been specialized to align with two distinct Operational and Resource viewpoints, which led to the creation of two new diagrams: Security Process Flow (Operational) and Security Process Flow (Resource).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Security Process Flow diagrams.png" /></ac:image></p><h4>New NAFv4 Structure diagrams</h4><p>New structure diagrams have been implemented in the Logical, Service, and Physical Resource Specification Viewpoints:</p><ul><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="L2 Logical Scenario" /></ac:link> </li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="S2 Service Structure" /></ac:link></li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="P2 Resource Structure" /></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><h4>         </h4><h4>New views in Strategic Viewpoint</h4><p>Beginning with this version, the following new views related to the Strategic Viewpoint are introduced:</p><ul><li><strong>Strategic Motivation Table</strong>, which you can find under the UAF Strategy Diagrams category, is designed to simplify the assembly of UAF Strategic requirements, such as Enterprise Goals and Enterprise Objectives, in a tabular format. </li><li><strong>Impact Matrix</strong>, which you can find under the UAF Analysis Diagrams category, illustrates the mapping between the Strategic, Operational, Resource, Service Viewpoint Elements and Strategic Viewpoint Elements using the Impacted By relationship.</li></ul></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="3fa4aaf2-b093-4c8b-92e0-86d9bfccc5fd"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=ngOqW2UVOSI&amp;ab_channel=CATIAMBSE" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Exchange management improvements</h3><p style="text-align: left;">This version adds significant enhancements to working with exchanges, including the ability to control their visibility on diagrams. Improved exchange creation wizards and management dialogs provide greater clarity.</p><h4 style="text-align: left;">Exchange visibility management</h4><p style="text-align: left;">Now, you can easily manage the visibility of realized exchanges in the diagrams. The dedicated button in the smart manipulator toolbar allows you to choose whether you want to show or hide required Exchange Items.</p><p style="text-align: left;"><ac:image ac:align="center"><ri:attachment ri:filename="show_operational_exchanges.png" /></ac:image></p><h6 style="text-align: center;">This is an example of managing the visibility of Operational Exchange Items in an Operational Internal Connectivity diagram.</h6><h4><span>Realized Exchange wizard improvements </span></h4><p><span>Additionally, 2024x brings a more focused approach to reviewing Activity pairs connected with existing Activity Edges in the </span> <strong>Realized Exchange wizards,</strong> <span> improving overall usability and clarity.</span></p><ul><li>In the second step, our focus has shifted solely to reviewing existing Activity Pairs connected by existing Activity Edges. This means that creating new Activity pairs or editing existing ones is no longer possible. As a result, the tool will no longer trigger the automatic generation of new elements or diagrams.</li><li>We've introduced a new step called <strong>Affected Diagrams</strong>. This step lets you see where changes will occur after realizing elements or editing existing exchanges.</li></ul><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="Exchange management changes.png" /></ac:image> </span> <span>An example of changes in the Realized Resource Exchange creation wizard.</span></h6><h4><span>Exchange Manager improvements</span></h4><p>In this release, we've made improvements to the <strong>Exchange Managers</strong>. Now, you'll find a handy <strong>Affected Diagrams</strong> button that opens a dialog listing all the diagrams containing elements that already realize the selected exchange.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="echanges_exchange_manager.png" /></ac:image> </span> <span>An example of changes in the Operational Exchange Manager. </span></h6><h4><span>Producing and Consuming Functions dialog improvements</span></h4><p>We've made some changes in the Producing and Consuming Activities/Functions dialogs as well. They now serve as tools for reviewing Activity pairs and easily removing any unnecessary ones.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="changes_producing_consuming_activities.png" /></ac:image>An example of changes in the Producing and Consuming Activities dialog.</span></h6><h3>Library Support</h3><p>New DISR and UJTL library versions are now available:</p><ul><li>UJTL (20230616)</li><li>DISR (<span style="color: rgb(23,43,77);">20230523</span>)</li></ul><p><span style="color: rgb(62,63,64);">You can choose the library version when creating a new project. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Using libraries" /><ac:plain-text-link-body><![CDATA[Learn more about using libraries >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Templates and Perspectives</h3><h4>New template</h4><ul><li>A new <span style="color: rgb(23,43,77);"> <strong>EA Project Template with Process Guide</strong> is now available in UAF. This Enterprise Architecture (EA) Guide defines a workflow for creating EA views following the Unified Architecture Framework Modeling Language (UAFML). When using this template, you will receive a new UAF project enhanced with the EA Guide for UAF. This modeling guide aids in building architecture by providing nine steps of workflow.</span></li></ul><h4><span style="color: rgb(23,43,77);">Renamed </span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF Enterprise Architecture Project</strong> was renamed to <strong>EA with BPMN Project</strong>. Using the <strong>EA with BPMN Project</strong> template, you will get a simplified Enterprise Architecture project with BPMN, which is based on the UAF framework and designed for enterprise and IT architecture modeling. Creating an EA with the BPMN project will switch the modeling tool to the EA-BPMN Architect graphical user interface and use the EA with the BPMN model template.</span></li><li><span style="color: rgb(23,43,77);">The perspective <strong style="text-align: left;">UAF Enterprise Architect</strong> <span> was renamed </span>to<span> </span> <strong style="text-align: left;">EA-BPMN Architect. </strong> <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Select Perspective dialog" /><ac:plain-text-link-body><![CDATA[Learn more about the perspectives >>>]]></ac:plain-text-link-body></ac:link> </span></li></ul><h4><span style="color: rgb(23,43,77);">Removed</span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF EA Project Template with Process Guide</strong> was removed.</span></li></ul><h3>Other Enhancements</h3><ul><li><span style="color: rgb(23,43,77);">The nested ports in all relevant viewpoints are now supported.</span></li><li>The options for <strong>Information Flows</strong> in the <strong>Environment Options</strong> dialog under the <strong>UAF </strong>options group are no longer available.</li><li>The<span> </span> <strong>Tools</strong> <span> </span>option group containing the<span> </span> <strong>Autowire Parts</strong> <span> </span>action is removed from the UAF Parametric Diagram toolbar.</li><li>The <strong>Delegate Port(s)</strong> <span> </span>action is now implemented in the Internal Connectivity Diagrams and is available from the <span style="color: rgb(23,43,77);">diagrams toolbar and context menu of roles, connectors, and ports</span>.</li><li><span style="color: rgb(23,43,77);">You can now create the Vision Statement in the <strong>Specification </strong>window of the Vision element.</span></li><li><span style="color: rgb(23,43,77);">New correctness validation rules regarding the Motivated By relationship are now available. These rules check if the Motivated By relationship is created between correct pairs.</span></li><li><span style="color: rgb(23,43,77);">A new passive validation rule COR2361 is implemented. This rule checks if an Operation Port Class Property type is correct.</span></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="90bd7b1e-43b6-43f5-8025-5097e80fab78"><ac:parameter ac:name="id">244508097</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>SysML Features</h5><h3>Improved Item Flow Creation and Editing</h3><p><span>SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the </span> <strong>Create / Edit Item Flow </strong> <span>dialog, improving overall usability and clarity.</span></p><ul><li><span>Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:</span><ul><li><span>New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams. </span></li><li>The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in <span>a well-organized diagram list in the third step, accurately representing selected options.</span></li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Improved_Item_Flow.png" /></ac:image></p><h6 style="text-align: center;">A comparison of some of the changes in the second step of the <strong>Create / Edit Item Flow</strong> dialog between versions 2024x and 2022x Refresh2.</h6><p><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more about Item Flow creation and editing >>]]></ac:plain-text-link-body></ac:link> </p><h3>Other Improvements</h3><ul><li>The <strong>Tools</strong> option group containing <strong>Autowire Parts</strong> and <strong>Delegate Port(s)</strong> commands has been removed from the SysML Parametric Diagram toolbar. Both <strong>Delegate Port(s)</strong> and <strong>Autowire Parts</strong> commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.</li><li>Improved <strong>Delegate Port(s)</strong> command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. <ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Automatic delegation" /><ac:plain-text-link-body><![CDATA[Learn more about automatic delegation >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="76d426b3-d26b-4be9-8310-6bc9193da35c"><ac:parameter ac:name="id">256630726</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Discontinued Features</h5><p>The following features have been discontinued with the 2024x version release.</p><h3>JavaScript Nashorn Scripting</h3><p><span style="color: rgb(62,63,64);">The JavaScript<span> </span> </span>Nashorn <span style="color: rgb(62,63,64);">language usage has been removed from the modeling tool. Please use JavaScript<span> </span> <em>Rhino</em> instead<em>. </em>This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Deprecated JavaScript Nashorn" /><ac:plain-text-link-body><![CDATA[Learn more about the deprecated JavaScript Nashorn >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Record Macro Functionality </h3><p>The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.</p><h3>SPEM Plugin</h3><p>The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.</p><h5>Known Migration Issues</h5><p>Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.</p><p>To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the &lt;modeling_tool_install_dir&gt;\bin\&lt;modeling_tool&gt;.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="79ae8693-d2ab-4747-accb-c1b9c1c7b0bd"><ac:parameter ac:name="id">272319258</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Modeling and Infrastructure</h5><h3>DSLS Licensing</h3><p>Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:</p><ul><li>License usage statistics, debugging, and simple UI to administer and view statistics.</li><li>Licenses are bound to their expiration date rather than the product version.</li><li>Nodelock (seat), floating, and managed licensing options.</li></ul><p>Thus, now you can choose to use either FlexNet or DSLS for product licensing. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f49ff8d-45a1-456c-a2a0-a919be8c1f02"><ac:rich-text-body><p>The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version <span>R2024x with modeling tool version 2024x</span>).</p></ac:rich-text-body></ac:structured-macro><p><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS Licensing >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9484f639-acef-4728-8acc-d1e2338719d2"><ac:parameter ac:name="">Zoom in Model Browser</ac:parameter></ac:structured-macro>Zoom in Model Browser</h3><p>From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking. </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Zoom in Model Browser.png" /></ac:image></p><h6 style="text-align: center;">Zooming in the Model Browser using keyboard shortcuts.</h6><p><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /><ac:plain-text-link-body><![CDATA[Learn more about zooming in the Model Browser>>]]></ac:plain-text-link-body></ac:link></p><h3>Advanced Legend Adornments in Tables</h3><p>In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Advanced Legend Adornments in Tables Example.png" /></ac:image></p><h6 style="text-align: center;">Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item <em>In Progress</em>.</h6><p style="text-align: right;"><br /></p><h3 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6c8c8907-e1fd-4c63-9547-aff205bb1046"><ac:parameter ac:name="">MIother</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li><strong>OpenJDK version update. </strong>Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version. </li><li><strong> <span style="color: rgb(62,63,64);">Supported operating system changes for Linux. </span> </strong> <span style="color: rgb(62,63,64);">CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support. </span></li><li><strong>JavaScript Rhino version update.</strong> The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</li><li>It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.</li></ul><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9de59458-bf62-4484-8bac-bf7d69a0b745"><ac:parameter ac:name="id">243174490</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h5><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="82578d71-581b-42b4-bfdc-d5dcd49ff7cd"><ac:parameter ac:name="">TWC</ac:parameter></ac:structured-macro> </span>Teamwork Cloud</h3><h4 style="text-align: left;">New File Exchange Format for Server Projects</h4><p>In version 2022x Refresh2, we introduced <strong>.szip</strong> – a new <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using server project file format" /><ac:plain-text-link-body><![CDATA[server project exchange format]]></ac:plain-text-link-body></ac:link>. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.</p><p>In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="600"><ri:attachment ri:filename="project_exchange_options.png" /></ac:image></h6><p style="margin-left: 0.0in;"><span style="color: rgb(0,0,0);">The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.</span></p><p style="margin-left: 0.0in;"><br /></p><p style="margin-left: 0.0in;text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image><ri:attachment ri:filename="szip_project_import_performance.png" /></ac:image> <ac:image><ri:attachment ri:filename="szip_project_export_performance.png" /></ac:image> </span></p><h6 style="text-align: center;">Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).</h6><p><br /></p><h4>Model Patch Mechanism (Technology Preview)</h4><p><span style="color: rgb(0,0,0);">We introduce the technology preview of the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Patch - Technology preview" /><ac:plain-text-link-body><![CDATA[Model Patch mechanism]]></ac:plain-text-link-body></ac:link>, a more lightweight way to move model changes. Model Patch can help you:</span></p><ul><li><span style="color: rgb(0,0,0);">Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;</span></li><li><span style="color: rgb(0,0,0);">Transfer only a specific scope of model changes between disconnected teams instead of the entire model;</span></li><li>Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.</li></ul><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="model_patch_mechanism.jpg" /></ac:image></h6><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfdd0694-20ca-468f-858e-b8118a0d2206"><ac:parameter ac:name="">Power</ac:parameter></ac:structured-macro> </span>Power’By</h3><h4>New Features to Manage Used Projects</h4><p><span style="color: rgb(0,0,0);">We added new features that provide you with better capabilities to manage used projects in <strong>3D</strong>EXPERIENCE:</span></p><ul><li><span style="color: rgb(0,0,0);">Export packages as a new server project;</span></li><li><span style="color: rgb(0,0,0);">Move elements to/from used projects;</span></li><li><span style="color: rgb(0,0,0);">Import used projects.</span></li></ul><h4><span style="color: rgb(0,0,0);">Opening Projects in Read-Only Mode</span></h4><p><span style="color: rgb(0,0,0);">Beginning with version 2024x, you can open <strong>3D</strong>EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.</span></p><p style="text-align: center;"><ac:image ac:height="96"><ri:attachment ri:filename="3DEXPERIENCE_project_editing_disabled.jpg" /></ac:image></p><h6 style="text-align: center;">Notification informing the user that the <strong>3D</strong>EXPERIENCE project is read-only.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to Top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="da45258d-6386-4b80-af5a-54f24ceca0df"><ac:parameter ac:name="id">430554266</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong> <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link> </strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=137989847 space=MSOSA2024x version=1 -->
## PAGE 00004: Magic Systems of Systems Architect Documentation

- page_id: `137989847`
- space_key: `MSOSA2024x`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024x/pages/137989847/Magic+Systems+of+Systems+Architect+Documentation
- version_number: 1
- version_date: `2023-09-22T13:04:11.720+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

1430502845

1430502848

1430502847

This is the home page of Magic Systems of Systems Architect documentation.

Magic Systems of Systems Architect is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to **enterprise architecture** needs.

The documentation of Magic Systems of Systems Architect is a package that includes the documentation of these capabilities:

**[CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024x']**

Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.

Type a search phrase...

**[CONFLUENCE_PAGE title='UAF 1.2 Plugin Documentation' space='UAF12P2024x']**

Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='UPDM 2 Plugin Documentation' space='UPDM2P2024x']**

Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024x']**

Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.

Type a search phrase...

**[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024x']**

Guides you through the import, export, and management of SysML requirements.

Type a search phrase...

**[CONFLUENCE_PAGE title='Magic Concept Modeler Documentation' space='MCM2024x']**

Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain.

Type a search phrase...

1302769756

##### Additional information

**[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024x']**

Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation.

****

Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.

Type a search phrase...

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="49da89cf-930a-42d6-93ee-2f9e7644bd43"><ac:parameter ac:name="id">1430502845</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="30c2055f-6f1d-4a38-baef-0c400c8a8d15"><ac:parameter ac:name="id">1430502848</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="af7f9153-5c44-4383-9ba9-772e6f6b9b8d"><ac:parameter ac:name="id">1430502847</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>This is the home page of Magic Systems of Systems Architect documentation.</p><p>Magic Systems of Systems Architect is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to <strong>enterprise architecture</strong> needs.</p><p>The documentation of Magic Systems of Systems Architect is a package that includes the documentation of these capabilities:</p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[General Capabilities]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="a03877fa-9149-454b-8ae8-d0bf52a98ec4"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MD2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><span class="confluence-link"><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="UAF 1.2 Plugin Documentation" /><ac:plain-text-link-body><![CDATA[UAF 1.2 modeling]]></ac:plain-text-link-body></ac:link></span></span></strong></p><p>Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="5dadf551-69b2-42ba-a244-5eaed808fd26"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UAF12P2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="UPDM2P2024x" ri:content-title="UPDM 2 Plugin Documentation" /><ac:plain-text-link-body><![CDATA[UPDM 2 modeling]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="a1c8a376-ee87-4565-be6d-a1efdd50e9f5"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UPDM2P2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML modeling]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="8c480077-d377-4348-98b2-403c0f3caf02"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="SYSMLP2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Requirements modeling]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Guides you through the import, export, and management of SysML requirements.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="a64a5a3c-b1b5-4a83-b779-e680cf71cb3f"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CRMP2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"><ac:link><ri:page ri:space-key="MCM2024x" ri:content-title="Magic Concept Modeler Documentation" /><ac:plain-text-link-body><![CDATA[Concept modeling]]></ac:plain-text-link-body></ac:link></strong></p><p><span style="color: rgb(62,63,64);">Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain. </span></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="224d903c-842c-489e-af74-df13189825ed"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MCM2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="652c9857-7149-4821-87a6-a108bbd88f32"><ac:parameter ac:name="id">1302769756</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><h3>Additional information</h3></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installation and licensing]]></ac:plain-text-link-body></ac:link></strong></p><p>Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation. </p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><span class="confluence-link"><ac:link><ri:space ri:space-key="MSI2024x" /><ac:plain-text-link-body><![CDATA[Simulation]]></ac:plain-text-link-body></ac:link></span></strong></p><p>Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.</p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="fb6a39a4-f4ff-449e-b45c-63db2a620788"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MSI2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=137989848 space=MSOSA2024x version=2 -->
## PAGE 00005: Magic Systems of Systems Architect Home Page

- page_id: `137989848`
- space_key: `MSOSA2024x`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024x/pages/137989848/Magic+Systems+of+Systems+Architect+Home+Page
- version_number: 2
- version_date: `2024-01-31T12:23:19.718+01:00`
- ancestors: Magic Systems of Systems Architect Documentation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Magic Systems of Systems Architect Documentation' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="6f6de204-e5e4-4f00-abf4-f05b04847656"><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Magic Systems of Systems Architect Documentation" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=137989989 space=MSOSA2024x version=1 -->
## PAGE 00006: Support

- page_id: `137989989`
- space_key: `MSOSA2024x`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024x/pages/137989989/Support
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
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f491134c-1f31-440c-b0cd-49219bca45e2"><ac:parameter ac:name="id">1906792292</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="92d28415-56a9-4da3-bb95-f0f1d439792a"><ac:parameter ac:name="id">1906792294</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b02bd87b-9182-47bc-8dbd-8936e128fbf2"><ac:parameter ac:name="id">1906792293</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2602c0ae-4d92-45ef-b3a9-b208e2028088"><ac:rich-text-body><p>For information about the support, please visit: <a href="https://www.3ds.com/support/">https://www.3ds.com/support/</a></p></ac:rich-text-body></ac:structured-macro><h3>Reporting an Issue</h3><p><span style="color: rgb(0,0,0);">If you encounter an issue or the modeling tool becomes unresponsive, a separately executable tool is provided for analyzing the status of the process to aid in bug submission. </span><span style="color: rgb(0,0,0);">In these situations, manually start the <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em> file (located in the <em>&lt;modeling tool installation directory&gt;\bin folder</em>). </span><span style="color: rgb(0,0,0);">After you start <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em>, the </span><strong>Report an Issue</strong> dialog <span style="color: rgb(0,0,0);">opens. </span></p><p><span style="color: rgb(0,0,0);">In this dialog, you can easily dump threads or memory heap into files and provide those files when reporting an issue to the support team.</span></p><p><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="report_issue.png"><ri:page ri:space-key="MSOSA2024x" ri:content-title="Support" /></ri:attachment></ac:image><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=137989987 space=MSOSA2024x version=1 -->
## PAGE 00007: Using UAF and UPDM2 plugins in Magic Systems of Systems Architect

- page_id: `137989987`
- space_key: `MSOSA2024x`
- source_url: https://docs.nomagic.com/spaces/MSOSA2024x/pages/137989987/Using+UAF+and+UPDM2+plugins+in+Magic+Systems+of+Systems+Architect
- version_number: 1
- version_date: `2023-09-22T13:04:14.217+02:00`
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

In case you will decide to change the plugin later, see chapter [CONFLUENCE_PAGE title='Changing between UAF and UPDM 2 plugins' space='UAF12P2024x'] for information about how to do that.

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
<h3>Choosing the default plugin</h3><p>Before the first startup of the Magic Systems of Systems Architect, you can set which plugin - UAF or UPDM2 - will be installed by default. If no changes are made, by default UAF plugin is installed.</p><p><br /></p><p>To change the default plugin before the first startup</p><hr /><ol><li>Go to the &lt;msosa_install_dir&gt;\bin\ and open for editing the <em>msosa.properties</em> file.</li><li>In the file, find the system property <em>-Dstart.application.with.updm2.or.uaf.plugin=uaf</em></li><li>Change the <em>uaf</em> value to <em>updm2</em>.</li><li>Save the file and start the Magic Systems of Systems Architect modeling tool.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c93f7330-b046-4e85-be90-7075c3f9d206"><ac:rich-text-body><p>In case you will decide to change the plugin later, see chapter <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Changing between UAF and UPDM 2 plugins" /></ac:link> for information about how to do that.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Displaying which plugin is installed</h3><p>You can choose to display the plugin name in brackets next to the Magic Systems of Systems Architect title in the modeling tool's title bar. </p><p><br /></p><p>To display the installed plugin name near the modeling tool title</p><hr /><ol><li>Go to the &lt;msosa_install_dir&gt;\bin\ and open for editing the <em>msosa.properties</em> file.</li><li>In the file, find the system property <em>-Dadd.plugin.name.to.application.title\=false</em></li><li>Change the <em>property </em>value to <em>true</em>.</li><li>Save the file and start the Magic Systems of Systems Architect modeling tool.</li></ol><p><ac:image><ri:attachment ri:filename="plugin_name_in_title.png"><ri:page ri:space-key="MSOSA2024x" ri:content-title="Using UAF and UPDM2 plugins in Magic Systems of Systems Architect" /></ri:attachment></ac:image></p>
````
