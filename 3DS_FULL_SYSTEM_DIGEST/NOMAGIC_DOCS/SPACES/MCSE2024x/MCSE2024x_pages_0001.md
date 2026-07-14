# NOMAGIC DOCUMENTATION SPACE: Magic Cyber Systems Engineer 2024x

<!--NOMAGIC_SPACE key=MCSE2024x chunk=1 -->

<!--NOMAGIC_PAGE id=142934666 space=MCSE2024x version=1 -->
## PAGE 00001: 2024x News for Developers

- page_id: `142934666`
- space_key: `MCSE2024x`
- source_url: https://docs.nomagic.com/spaces/MCSE2024x/pages/142934666/2024x+News+for+Developers
- version_number: 1
- version_date: `2023-11-09T13:02:03.943+01:00`
- ancestors: Magic Cyber Systems Engineer Documentation
- labels: []

### NORMALIZED CONTENT

###### OpenJDK Version Update

Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 versioninstead of the OpenJDK 11.0.18+10* version.

###### Identifying Plugin Dependencies by Class Name

A new functionality is introduced that allows you to identify plugin dependencies by class name. For more information, see the [CONFLUENCE_PAGE title='Identifying plugin dependencies' space='MD2024x'] page.

###### Revised Value of the Constants

The values of the constants for SimulationProfile, SimulationOptions, and SysMLConstants are updated. For more information, see the[CONFLUENCE_PAGE title='API Changes' space='MSI2024x'] page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h5><span>OpenJDK Version Update</span></h5><p><span style="color: rgb(62,63,64);">Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version </span><span>instead of the OpenJDK 11.0.18+10* version. </span></p><h5><span>Identifying Plugin Dependencies by Class Name</span></h5><p class="auto-cursor-target" style="text-align: left;">A new functionality is introduced that allows you to identify plugin dependencies by class name. For more information, see the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Identifying plugin dependencies" /></ac:link> page.</p><h5><span>Revised Value of the Constants </span></h5><p><span>The values of the constants for SimulationProfile, SimulationOptions, and SysMLConstants are updated. For more information, see the </span><ac:link><ri:page ri:space-key="MSI2024x" ri:content-title="API Changes" /></ac:link> page.</p>
````

<!--NOMAGIC_PAGE id=136726681 space=MCSE2024x version=37 -->
## PAGE 00002: 2024x Version News

- page_id: `136726681`
- space_key: `MCSE2024x`
- source_url: https://docs.nomagic.com/spaces/MCSE2024x/pages/136726681/2024x+Version+News
- version_number: 37
- version_date: `2024-12-06T10:56:59.020+01:00`
- ancestors: Magic Cyber Systems Engineer Documentation
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

top

###### Magic Cyber Systems Engineer

Released on: November 10, 2023

2024x release introduces several improvements to Item Flow creation and editing. The **Create / Edit Item Flow**dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition, **Autowire Parts** and **Delegate Port(s)** commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the **Delegate Port(s)** command functionality regarding nested ports is now improved to treat each displayed nested port individually.

Simulation features introduce a number of powerful functionalities. The new product version allows you to run server-side simulation with modified Simulation Configuration properties and even employ a virtual Simulation Configuration without modifying the Teamwork Cloud project. The product also enables live unit conversion to simplify model analysis and reduce the likelihood of errors. Beyond these enhancements, you can customize the Histogram appearance, control the simulation termination logic with the help of a new Auto Terminate property, and benefit from other smaller improvements.

The 2024x release also introduces general modeling and infrastructure, as well as collaborative modeling enhancements.

For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.

Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.

We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.

To download the latest version of the modeling tool, see [CONFLUENCE_PAGE title='Downloading installation files' space='ILTWRT']. For further information, check the .

#### NOTE: 2024x Hot Fix 3 available

2024x Hot Fix 3 available

2024x Hot Fix 3 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 3 Version News' space='CATIA']>]]>

#### NOTE: 2024x Hot Fix 2 available

2024x Hot Fix 2 available

2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 2 Version News' space='CATIA']>]]>

****

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

244508097

INLINE

###### SysML Features

##### Improved Item Flow Creation and EditingImproved Item Flow Creation and Editing

SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the **Create / Edit Item Flow** dialog, improving overall usability and clarity.

- Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:
  - New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams.
  - The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in a well-organized diagram list in the third step, accurately representing selected options.

[IMAGE alt='' src='']

###### A comparison of some of the changes in the second step of the **Create / Edit Item Flow** dialog between versions 2024x and 2022x Refresh2.

[CONFLUENCE_PAGE title='Creating Item Flow' space='SYSMLP2024x']>]]>

##### Other ImprovementsOther Improvements

- The Tools option group containing Autowire Parts and Delegate Port(s) commands has been removed from the SysML Parametric Diagram toolbar. Both Delegate Port(s) and Autowire Parts commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.
- Improved Delegate Port(s) command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. [CONFLUENCE_PAGE title='Automatic delegation' space='SYSMLP2024x']>]]>

1298061950

INLINE

###### Simulation Features

##### Server-Side Simulation

###### Modifying Simulation Configuration Properties

Now, you can run server-side simulations with modified properties of a Simulation Configuration without having to change the Teamwork Cloud project. This approach provides a more convenient method to modify simulation properties without a modeling tool. 
It's even feasible to run a simulation without explicitly specifying a Simulation Configuration; instead, a virtual Simulation Configuration can be employed. This gives you the possibility to quickly choose a different execution target and define its simulation properties.

[IMAGE alt='' src='']

###### The REST API request body with the 'simconfig' parameter which allows specifying simulation properties.

[IMAGE alt='' src='']

###### Enablingthe autocompletion option for the simulation using Jupyter Notebook.

[CONFLUENCE_PAGE title='Simulation using REST API' space='CST2024x']>]]>

[CONFLUENCE_PAGE title='Simulation using Jupyter Notebook' space='CST2024x']>]]>

###### DSLS Licensing Server Support

From version 2024x, in addition to FlexNet, server-side simulation supports the DSLS licensing server.

[CONFLUENCE_PAGE title='DSLS installation and licensing' space='IL2024x']>]]>

##### Live Unit Conversion for Runtime Objects

Cameo Simulation Toolkit 2024x introduces live unit conversion for simulation runtime objects. When Value Properties are connected using a Binding Connector, their runtime values will be automatically converted if they have compatible Value Types (like grams and kilograms). This feature simplifies model analysis, especially when combining elements from various sources, and reduces the possibility of errors.

[IMAGE alt='' src='']

###### A Parametric Diagram with runtime values of Value Properties being automatically converted according to their Value Types during simulation.

[CONFLUENCE_PAGE title='Unit Conversion' space='CST2024x']>]]>

##### Histogram Improvements

We're happy to present a new functionality that will allow you to tailor the Histogram appearance. With this improvement, you can define a custom number of data bins in which the results will be distributed and achieve the desired Histogram shape and precision. Furthermore, the edge of the last data bin will now match the maximum value of the value array, ensuring accurate representation.

[IMAGE alt='' src='']

###### A sample Histogram with the custom number of data bins. Here, the **Number Of Bins** property is set to 50.

[CONFLUENCE_PAGE title='Histogram' space='CST2024x']>]]>

##### Auto-Terminating Simulation Configurations

Simulation Configurations now have a new **Auto Terminate** property, allowing you to manage the simulation termination logic. If you set this property to *true*, the simulation is terminated when it completes or after the initialization phase if it does not start automatically. When the property is set to *false*, the simulation continues to run without termination, hanging at the end or after the initialization phase if it does not start automatically.

[IMAGE alt='' src='']

###### A new **Auto Terminate** property of a Simulation Configuration.

[CONFLUENCE_PAGE title='SimulationConfig stereotype' space='CST2024x']>]]>

##### Other Improvements1Other Improvements

- Generating HTML has become easier, thanks to the availability of the **Generate HTML** and **Generate and Attach HTML** actions in new, convenient locations. These actions can now be accessed from the context menu of a User Interface Modeling Diagram or a UI element in the Containment tree. Additionally, you can invoke the actions by right-clicking a property symbol, provided its type is a Widget. [IMAGE alt='' src='']
- The simulation now considers the Decimal Places project option.
- The Parametric Execution Profile has been eliminated. The constraints for parametric execution have been moved to the Simulation Profile .

272319258

INLINE

###### Discontinued FeaturesDiscontinued Features

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

243174490

INLINE

###### miModeling and Infrastructure

##### DSLS LicensingDSLS Licensing

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

##### Advanced Legend Adornments in TablesAdvanced Legend Adornments in Tables

In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.

[IMAGE alt='' src='']

###### Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item *In Progress*.

##### Other Improvements2Other Improvements

- OpenJDK version update. Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version.
- Supported operating system changes for Linux. CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support.
- JavaScript Rhino version update. The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.
- It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.

243713866

INLINE

###### CollaborationCollaboration

##### TWCTeamwork Cloud

###### New File Exchange Format for Server Projects

In version 2022x Refresh2, we introduced **.szip** – a new [CONFLUENCE_PAGE title='Using server project file format' space='MD2024x']. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.

In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.

[IMAGE alt='' src='']

The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.

[IMAGE alt='' src=''] [IMAGE alt='' src='']

###### Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).

###### Model Patch Mechanism (Technology Preview)

We introduce the technology preview of the [CONFLUENCE_PAGE title='Model Patch - Technology preview' space='MD2024x'], a more lightweight way to move model changes. Model Patch can help you:

- Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;
- Transfer only a specific scope of model changes between disconnected teams instead of the entire model;
- Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.

[IMAGE alt='' src='']

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

[CONFLUENCE_PAGE title='2024x Version News' space='CATIA']>]]>

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ac060d11-24bb-43ee-828b-bfae5b72f6eb"><ac:parameter ac:name="id">753686899</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d04429d1-af39-4fcc-95f9-34e91a0b1fb5"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">753686902</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><br /><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fb82fc80-35bc-42cf-ab13-51cc01e20dfc"><ac:parameter ac:name="id">243271308</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p style="text-align: center;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fd7d672f-fb01-4e70-8982-8ff70256549a"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><h5 style="text-align: center;">Magic Cyber Systems Engineer</h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: November 10, 2023</span></p><p><br /></p><p><span style="color: rgb(62,63,64);">2024x release introduces several improvements to Item Flow creation and editing. The<span> </span> <strong>Create / Edit Item Flow<span> </span> </strong>dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition, <strong style="text-align: left;">Autowire Parts</strong> <span> </span>and<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>command functionality regarding nested ports is now improved to treat each displayed nested port individually.</span></p><p><span style="color: rgb(62,63,64);"> <span style="color: rgb(128,128,128);"> <span style="color: rgb(55,65,81);">Simulation features introduce a number of powerful functionalities. The new </span> </span> <span style="color: rgb(55,65,81);">product</span> <span style="color: rgb(55,65,81);"> </span> <span style="color: rgb(55,65,81);">version allows you to run server-side simulation with modified Simulation Configuration properties and even employ a virtual Simulation Configuration <span style="color: rgb(62,63,64);">without modifying the Teamwork Cloud project</span>.</span> <span style="color: rgb(55,65,81);"> The product also enables live unit conversion <span style="color: rgb(55,65,81);text-decoration: none;">to </span> <span style="color: rgb(55,65,81);text-decoration: none;">simplify</span> <span style="color: rgb(55,65,81);text-decoration: none;"> model analysis and reduce the likelihood of errors. Beyond these enhancements, you can customize</span> the Histogram appearance, control the simulation termination logic with the help of a new Auto Terminate property, and benefit from other smaller improvements.</span> </span></p><p><span>The 2024x release also introduces general modeling and infrastructure, as well as collaborative modeling enhancements.</span></p><p><span>For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</span></p><p><span>Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.</span></p><p><span>We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="ILTWRT" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the <ac:link><ri:space ri:space-key="MD2022xR1" /><ac:plain-text-link-body><![CDATA[product documentation]]></ac:plain-text-link-body></ac:link>.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a672b7b3-8ef4-458a-b61f-9c4fafd6dc87"><ac:parameter ac:name="title">2024x Hot Fix 3 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 3 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Hot Fix 3 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f9b23f4f-2dd2-42fb-9662-2ccc8dafb914"><ac:parameter ac:name="title">2024x Hot Fix 2 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Hot Fix 2 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong> <ac:link ac:anchor="SysML Features" /> </strong></p><ul><li><ac:link ac:anchor="Improved Item Flow Creation and Editing" /></li><li><ac:link ac:anchor="Other Improvements" />  </li></ul><p><strong> <ac:link ac:anchor="Simulation Features" /> </strong></p><ul><li><ac:link ac:anchor="Server-Side Simulation" /><ul><li><ac:link ac:anchor="Modifying Simulation Configuration Properties" /></li><li><ac:link ac:anchor="DSLS License Server Support" /></li></ul></li><li><ac:link ac:anchor="Live Unit Conversion for Runtime Objects" /></li><li><ac:link ac:anchor="Histogram Improvements" /></li><li><ac:link ac:anchor="Auto-Terminating Simulation Configurations" /></li><li><ac:link ac:anchor="Other Improvements1"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Discontinued Features" /> </strong></p><ul><li><span style="color: rgb(255,0,0);"> <ac:link ac:anchor="JavaScript Nashorn Scripting" /> </span></li><li><ac:link ac:anchor="Record Macro Functionality" /></li><li><ac:link ac:anchor="SPEM Plugin" /></li></ul><p><strong> <ac:link ac:anchor="Known Migration Issues" /> </strong></p><p><strong> <ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link> </strong></p><ul><li><span style="color: rgb(255,0,0);"> <ac:link ac:anchor="DSLS Licensing" /> </span></li><li><ac:link ac:anchor="Zoom in Model Browser" /></li><li><span style="color: rgb(23,43,77);"> <ac:link ac:anchor="Advanced Legend Adornments in Tables" /> </span></li><li><p style="text-align: left;"><ac:link ac:anchor="Other Improvements2"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></p></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Collaboration" /> </strong></p><p><ac:link ac:anchor="TWC"><ac:plain-text-link-body><![CDATA[Teamwork Cloud]]></ac:plain-text-link-body></ac:link></p><ul><li><ac:link ac:anchor="New File Exchange Format for Server Projects" /></li><li><ac:link ac:anchor="Model Patch Mechanism (Technology Preview)" /></li></ul><p><ac:link ac:anchor="Power"><ac:plain-text-link-body><![CDATA[Power'By]]></ac:plain-text-link-body></ac:link></p><ul><li><ac:link ac:anchor="New Features to Manage Used Projects" /></li><li><ac:link ac:anchor="Opening Projects in Read-Only Mode" /></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1b77567e-eabc-4a51-b858-9f25a0643a8f"><ac:parameter ac:name="id">244508097</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>SysML Features</h5><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="f513c0f4-8ec4-4734-9196-44187491e529"><ac:parameter ac:name="">Improved Item Flow Creation and Editing</ac:parameter></ac:structured-macro>Improved Item Flow Creation and Editing</h3><p><span>SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the </span> <strong>Create / Edit Item Flow </strong> <span>dialog, improving overall usability and clarity.</span></p><ul><li><span>Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:</span><ul><li><span>New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams. </span></li><li>The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in <span>a well-organized diagram list in the third step, accurately representing selected options.</span></li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Improved_Item_Flow.png" /></ac:image></p><h6 style="text-align: center;">A comparison of some of the changes in the second step of the <strong>Create / Edit Item Flow</strong> dialog between versions 2024x and 2022x Refresh2.</h6><p><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more about Item Flow creation and editing >>]]></ac:plain-text-link-body></ac:link> </p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9c001aa7-667d-4750-b4db-cc7e6ffc4392"><ac:parameter ac:name="">Other Improvements</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li>The <strong>Tools</strong> option group containing <strong>Autowire Parts</strong> and <strong>Delegate Port(s)</strong> commands has been removed from the SysML Parametric Diagram toolbar. Both <strong>Delegate Port(s)</strong> and <strong>Autowire Parts</strong> commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.</li><li>Improved <strong>Delegate Port(s)</strong> command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. <ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Automatic delegation" /><ac:plain-text-link-body><![CDATA[Learn more about automatic delegation >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e3ec648a-2337-479b-af36-c178d5f75e7b"><ac:parameter ac:name="id">1298061950</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Simulation Features</h5><h3 style="text-align: left;">Server-Side Simulation</h3><h4>Modifying Simulation Configuration Properties</h4><p>Now, you can run server-side simulations with modified properties of a Simulation Configuration without having to change the Teamwork Cloud project. This approach provides a more convenient method to modify simulation properties without a modeling tool. <br />It's even feasible to run a simulation without explicitly specifying a Simulation Configuration; instead, a virtual Simulation Configuration can be employed. This gives you the possibility to quickly choose a different execution target and define its simulation properties.</p><p><br /></p><p style="text-align: center;"><span style="color: rgb(62,63,64);"> <ac:image><ri:attachment ri:filename="simconfig_parameter.png" /></ac:image> </span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The REST API request body with the 'simconfig' parameter which allows specifying simulation properties.</span></h6><p style="text-align: center;"><span style="color: rgb(62,63,64);"> <ac:image ac:queryparams="effects=border-simple,blur-border"><ri:attachment ri:filename="autocomletion_jupyter.png" /></ac:image> </span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">Enabling<span style="color: rgb(23,43,77);"> the autocompletion option for the simulation using Jupyter Notebook.</span> </span></h6><p><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="Run simulation"><ri:page ri:space-key="CST2024x" ri:content-title="Simulation using REST API" /><ac:plain-text-link-body><![CDATA[Learn more about modifying Simulation Configuration properties using REST API >>]]></ac:plain-text-link-body></ac:link> </span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="CST2024x" ri:content-title="Simulation using Jupyter Notebook" /><ac:plain-text-link-body><![CDATA[Learn more about modifying Simulation Configuration properties using Jupyter Notebook >>]]></ac:plain-text-link-body></ac:link> </span></p><h4><span style="color: rgb(62,63,64);"> <br />DSLS Licensing Server Support</span></h4><p><span style="color: rgb(62,63,64);">From version 2024x, in addition to FlexNet, server-side simulation supports the DSLS licensing server.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS licensing >>]]></ac:plain-text-link-body></ac:link> </span></p><p style="text-align: right;"><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span></p><h3>Live Unit Conversion for Runtime Objects</h3><p><span style="color: rgb(55,65,81);">Cameo Simulation Toolkit 2024x introduces live unit conversion for simulation runtime objects. When Value Properties are connected using a Binding Connector, their runtime values will be automatically converted if they have compatible Value Types (like grams and kilograms). This feature simplifies model analysis, especially when combining elements from various sources, <span style="color: rgb(62,63,64);">and reduces the possibility of errors.</span> </span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(55,65,81);"> <ac:image><ri:attachment ri:filename="live_unit_conversion.png" /></ac:image> </span></p><h6 style="text-align: center;"><span style="color: rgb(55,65,81);">A Parametric Diagram with runtime values of Value Properties being automatically converted according to their Value Types during simulation.</span></h6><p><span style="color: rgb(55,65,81);"> <ac:link><ri:page ri:space-key="CST2024x" ri:content-title="Unit Conversion" /><ac:plain-text-link-body><![CDATA[Learn more about unit conversion for runtime objects >>]]></ac:plain-text-link-body></ac:link> </span></p><p style="text-align: right;"><span style="color: rgb(55,65,81);"> <span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span> </span></p><h3>Histogram Improvements</h3><p><span style="color: rgb(55,65,81);"> <span style="color: rgb(23,43,77);">We're happy to present a new functionality that will allow you to tailor the Histogram appearance. With this improvement, you can define a custom number of data bins in which the results will be distributed and achieve the desired Histogram shape and precision. Furthermore, the edge of the last data bin will now match the maximum value of the value array, ensuring accurate representation.</span> </span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(55,65,81);"> <span style="color: rgb(23,43,77);"> <ac:image><ri:attachment ri:filename="histogram_improvements.png" /></ac:image> </span> </span></p><h6 style="text-align: center;">A sample Histogram with the custom number of data bins. Here, the <strong>Number Of Bins</strong> property is set to 50.</h6><p><ac:link><ri:page ri:space-key="CST2024x" ri:content-title="Histogram" /><ac:plain-text-link-body><![CDATA[Learn more about working with Histograms >>]]></ac:plain-text-link-body></ac:link></p><h3>Auto-Terminating Simulation Configurations</h3><p><span style="color: rgb(23,43,77);">Simulation Configurations now have a new <strong>Auto Terminate</strong> property, allowing you to manage the simulation termination logic. If you set this property to <em>true</em>, the simulation is terminated when it completes or after the initialization phase if it does not start automatically. When the property is set to <em>false</em>, the simulation continues to run without termination, hanging at the end or after the initialization phase if it does not start automatically.</span></p><p style="text-align: left;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="auto_terminate_property.png" /></ac:image></p><h6 style="text-align: center;">A new <strong>Auto Terminate</strong> property of a Simulation Configuration.</h6><p><ac:link><ri:page ri:space-key="CST2024x" ri:content-title="SimulationConfig stereotype" /><ac:plain-text-link-body><![CDATA[Learn more about Simulation Configuration properties >>]]></ac:plain-text-link-body></ac:link></p><p style="text-align: right;"><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="17e6ae39-43e4-436c-a486-664e5e22a58c"><ac:parameter ac:name="">Other Improvements1</ac:parameter></ac:structured-macro>Other Improvements</h3><ul style="text-align: left;"><li><span style="color: rgb(55,65,81);">Generating HTML has become easier, thanks to the availability of the <strong>Generate HTML</strong> and <strong>Generate and Attach HTML</strong> actions in new, convenient locations. These actions can now be accessed from the context menu of a User Interface Modeling Diagram or a UI element in the Containment tree. Additionally, you can invoke the actions by right-clicking a property symbol, provided its type is a Widget.</span> <br /><span> <br /><ac:image><ri:attachment ri:filename="generating_and_attaching_html.png" /></ac:image> <br /><br /></span></li><li>The simulation now considers the <strong>Decimal Places</strong> project option.</li><li>The <em>Parametric Execution Profile</em> has been eliminated. The constraints for parametric execution have been moved to the <em>Simulation Profile</em>.</li></ul><p style="text-align: right;"><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="30ac573a-9647-46db-9970-34218fdb29a6"><ac:parameter ac:name="id">272319258</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="22763b20-4732-4783-a4d2-7e1f4d09824a"><ac:parameter ac:name="">Discontinued Features</ac:parameter></ac:structured-macro>Discontinued Features</h5><p>The following features have been discontinued with the 2024x version release.</p><h3>JavaScript Nashorn Scripting</h3><p><span style="color: rgb(62,63,64);">The JavaScript<span> </span> </span>Nashorn <span style="color: rgb(62,63,64);">language usage has been removed from the modeling tool. Please use JavaScript<span> </span> <em>Rhino</em> instead<em>. </em>This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Deprecated JavaScript Nashorn" /><ac:plain-text-link-body><![CDATA[Learn more about the deprecated JavaScript Nashorn >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Record Macro Functionality </h3><p>The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.</p><h3>SPEM Plugin</h3><p>The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.</p><h5>Known Migration Issues</h5><p>Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.</p><p>To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the &lt;modeling_tool_install_dir&gt;\bin\&lt;modeling_tool&gt;.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="19265554-ddd8-4aac-b349-e17ad50aaf56"><ac:parameter ac:name="id">243174490</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h5><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="d9658866-47d8-4652-bd44-57d618a5c6d6"><ac:parameter ac:name="">DSLS Licensing</ac:parameter></ac:structured-macro>DSLS Licensing</h3><p>Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:</p><ul><li>License usage statistics, debugging, and simple UI to administer and view statistics.</li><li>Licenses are bound to their expiration date rather than the product version.</li><li>Nodelock (seat), floating, and managed licensing options.</li></ul><p>Thus, now you can choose to use either FlexNet or DSLS for product licensing. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f49ff8d-45a1-456c-a2a0-a919be8c1f02"><ac:rich-text-body><p>The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version <span>R2024x with modeling tool version 2024x</span>).</p></ac:rich-text-body></ac:structured-macro><p><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS Licensing >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9484f639-acef-4728-8acc-d1e2338719d2"><ac:parameter ac:name="">Zoom in Model Browser</ac:parameter></ac:structured-macro>Zoom in Model Browser</h3><p>From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking. </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Zoom in Model Browser.png" /></ac:image></p><h6 style="text-align: center;">Zooming in the Model Browser using keyboard shortcuts.</h6><p><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /><ac:plain-text-link-body><![CDATA[Learn more about zooming in the Model Browser>>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="24661fa1-5ddb-4481-a09b-e7ad23369751"><ac:parameter ac:name="">Advanced Legend Adornments in Tables</ac:parameter></ac:structured-macro>Advanced Legend Adornments in Tables</h3><p>In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Advanced Legend Adornments in Tables Example.png" /></ac:image></p><h6 style="text-align: center;">Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item <em>In Progress</em>.</h6><p style="text-align: right;"><br /></p><h3 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="90856e33-8181-4fc8-8fe9-caeeed943312"><ac:parameter ac:name="">Other Improvements2</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li><strong>OpenJDK version update. </strong>Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version. </li><li><strong> <span style="color: rgb(62,63,64);">Supported operating system changes for Linux. </span> </strong> <span style="color: rgb(62,63,64);">CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support. </span></li><li><strong>JavaScript Rhino version update.</strong> The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</li><li>It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.</li></ul><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dcc5ff79-6a80-4582-9dc2-bb34ce0a429b"><ac:parameter ac:name="id">243713866</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h5><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="82578d71-581b-42b4-bfdc-d5dcd49ff7cd"><ac:parameter ac:name="">TWC</ac:parameter></ac:structured-macro> </span>Teamwork Cloud</h3><h4 style="text-align: left;">New File Exchange Format for Server Projects</h4><p>In version 2022x Refresh2, we introduced <strong>.szip</strong> – a new <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using server project file format" /><ac:plain-text-link-body><![CDATA[server project exchange format]]></ac:plain-text-link-body></ac:link>. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.</p><p>In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.</p><p style="text-align: center;"><ac:image ac:width="600"><ri:attachment ri:filename="project_exchange_options.png" /></ac:image></p><p style="margin-left: 0.0in;"><span style="color: rgb(0,0,0);">The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.</span></p><p style="margin-left: 0.0in;"><br /></p><p style="margin-left: 0.0in;text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image><ri:attachment ri:filename="szip_project_import_performance.png" /></ac:image> <ac:image><ri:attachment ri:filename="szip_project_export_performance.png" /></ac:image> </span></p><h6 style="text-align: center;">Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).</h6><p><br /></p><h4>Model Patch Mechanism (Technology Preview)</h4><p><span style="color: rgb(0,0,0);">We introduce the technology preview of the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Patch - Technology preview" /><ac:plain-text-link-body><![CDATA[Model Patch mechanism]]></ac:plain-text-link-body></ac:link>, a more lightweight way to move model changes. Model Patch can help you:</span></p><ul><li><span style="color: rgb(0,0,0);">Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;</span></li><li><span style="color: rgb(0,0,0);">Transfer only a specific scope of model changes between disconnected teams instead of the entire model;</span></li><li>Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.</li></ul><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="model_patch_mechanism.jpg" /></ac:image></p><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfdd0694-20ca-468f-858e-b8118a0d2206"><ac:parameter ac:name="">Power</ac:parameter></ac:structured-macro> </span>Power’By</h3><h4>New Features to Manage Used Projects</h4><p><span style="color: rgb(0,0,0);">We added new features that provide you with better capabilities to manage used projects in <strong>3D</strong>EXPERIENCE:</span></p><ul><li><span style="color: rgb(0,0,0);">Export packages as a new server project;</span></li><li><span style="color: rgb(0,0,0);">Move elements to/from used projects;</span></li><li><span style="color: rgb(0,0,0);">Import used projects.</span></li></ul><h4><span style="color: rgb(0,0,0);">Opening Projects in Read-Only Mode</span></h4><p><span style="color: rgb(0,0,0);">Beginning with version 2024x, you can open <strong>3D</strong>EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.</span></p><p style="text-align: center;"><ac:image ac:height="96"><ri:attachment ri:filename="3DEXPERIENCE_project_editing_disabled.jpg" /></ac:image></p><h6 style="text-align: center;">Notification informing the user that the <strong>3D</strong>EXPERIENCE project is read-only.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0529d28e-ccbb-400b-8ef2-23229cc103a8"><ac:parameter ac:name="id">430554266</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=136726679 space=MCSE2024x version=2 -->
## PAGE 00003: Magic Cyber Systems Engineer Documentation

- page_id: `136726679`
- space_key: `MCSE2024x`
- source_url: https://docs.nomagic.com/spaces/MCSE2024x/pages/136726679/Magic+Cyber+Systems+Engineer+Documentation
- version_number: 2
- version_date: `2024-02-01T10:24:06.458+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

564776767

564776769

564776768

INLINE

This is the home page of Magic Cyber Systems Engineer documentation.

Magic Cyber Systems Engineer is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to **systems engineering** needs.

The documentation of Magic Cyber Systems Engineer is a package that includes the documentation of these capabilities:

**[CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024x']**

Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.

Type a search phrase...

**[CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024x']**

Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.

Type a search phrase...

**[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024x']**

Guides you through the import, export, and management of SysML requirements.

Type a search phrase...

**[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024x']**

Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation.

798213816

##### Additional information

**[CONFLUENCE_PAGE title='Magic Model Analyst Documentation' space='MSI2024x']**

Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.

Type a search phrase...

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d516dbf5-4ea4-4e56-a38a-2c61f18af7be"><ac:parameter ac:name="id">564776767</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="44f03ae1-e5ba-44d1-ae13-9dbd20224243"><ac:parameter ac:name="id">564776769</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cace0e58-3588-4ca8-97d3-aec17a220c9d"><ac:parameter ac:name="id">564776768</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="06e751a1-0bf7-4bf6-8901-22b44fe37360"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>This is the home page of Magic Cyber Systems Engineer documentation.</p><p>Magic Cyber Systems Engineer is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to <strong>systems engineering</strong> needs.</p><p>The documentation of Magic Cyber Systems Engineer is a package that includes the documentation of these capabilities:</p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"> <strong> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[General capabilities]]></ac:plain-text-link-body></ac:link> </strong> <br /></span></p><p style="margin-left: 30.0px;">Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="7fdee566-5950-48b8-b4db-d2ca91399b05"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MD2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"> <span class="confluence-link"> <strong> <ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="SysML Plugin Documentation" /><ac:plain-text-link-body><![CDATA[SysML modeling]]></ac:plain-text-link-body></ac:link> </strong> <br /></span> </span></p><p style="margin-left: 30.0px;">Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="4d640133-3ecf-483c-b64a-4673fbd5fb6b"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="SYSMLP2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"> <span class="confluence-link"> <strong> <ac:link><ri:page ri:space-key="CRMP2024x" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Requirements modeling]]></ac:plain-text-link-body></ac:link> </strong> <br /></span> </span></p><p style="margin-left: 30.0px;">Guides you through the import, export, and management of SysML requirements.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="7c458b64-7c95-4ccd-a021-c14195f68206"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CRMP2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><strong> <ac:link><ri:page ri:space-key="IL2024x" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installation and licensing]]></ac:plain-text-link-body></ac:link> </strong></p><p style="margin-left: 30.0px;">Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation. </p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="db7a20a3-ed3d-4b34-8948-dcb9e446c942"><ac:parameter ac:name="id">798213816</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><h3>Additional information</h3></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><strong style="letter-spacing: 0.0px;"><ac:link><ri:page ri:space-key="MSI2024x" ri:content-title="Magic Model Analyst Documentation" /><ac:plain-text-link-body><![CDATA[Simulation]]></ac:plain-text-link-body></ac:link></strong></p><p style="margin-left: 30.0px;">Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.</p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="9de3b2f1-1884-4d77-a05a-ce5a8080a962"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MSI2024x" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````

<!--NOMAGIC_PAGE id=136726680 space=MCSE2024x version=3 -->
## PAGE 00004: Magic Cyber Systems Engineer Home Page

- page_id: `136726680`
- space_key: `MCSE2024x`
- source_url: https://docs.nomagic.com/spaces/MCSE2024x/pages/136726680/Magic+Cyber+Systems+Engineer+Home+Page
- version_number: 3
- version_date: `2024-02-01T10:22:56.809+01:00`
- ancestors: Magic Cyber Systems Engineer Documentation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="excerpt-include" ac:schema-version="1" ac:macro-id="a5ea0454-93f7-4545-af1e-359f8a8ed922"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Magic Cyber Systems Engineer Documentation" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=136726840 space=MCSE2024x version=1 -->
## PAGE 00005: Support

- page_id: `136726840`
- space_key: `MCSE2024x`
- source_url: https://docs.nomagic.com/spaces/MCSE2024x/pages/136726840/Support
- version_number: 1
- version_date: `2023-09-21T14:04:01.710+02:00`
- ancestors: Magic Cyber Systems Engineer Documentation
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
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f491134c-1f31-440c-b0cd-49219bca45e2"><ac:parameter ac:name="id">1906792292</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="92d28415-56a9-4da3-bb95-f0f1d439792a"><ac:parameter ac:name="id">1906792294</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9bb8e93b-a585-44e2-909a-96290dfd3b3a"><ac:parameter ac:name="id">1906792293</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2602c0ae-4d92-45ef-b3a9-b208e2028088"><ac:rich-text-body><p>For information about the support, please visit: <a href="https://www.3ds.com/support/">https://www.3ds.com/support/</a></p></ac:rich-text-body></ac:structured-macro><h3>Reporting an Issue</h3><p><span style="color: rgb(0,0,0);">If you encounter an issue or the modeling tool becomes unresponsive, a separately executable tool is provided for analyzing the status of the process to aid in bug submission. </span><span style="color: rgb(0,0,0);">In these situations, manually start the <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em> file (located in the <em>&lt;modeling tool installation directory&gt;\bin folder</em>). </span><span style="color: rgb(0,0,0);">After you start <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em>, the </span><strong>Report an Issue</strong> dialog <span style="color: rgb(0,0,0);">opens. </span></p><p><span style="color: rgb(0,0,0);">In this dialog, you can easily dump threads or memory heap into files and provide those files when reporting an issue to the support team.</span></p><p><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="report_issue.png"><ri:page ri:space-key="MCSE2024x" ri:content-title="Support" /></ri:attachment></ac:image><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
