# NOMAGIC DOCUMENTATION SPACE: Cameo Enterprise Architecture 2024x Refresh2

<!--NOMAGIC_SPACE key=CEA2024xR2 chunk=1 -->

<!--NOMAGIC_PAGE id=187334780 space=CEA2024xR2 version=1 -->
## PAGE 00001: 2022x News for Developers

- page_id: `187334780`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/187334780/2022x+News+for+Developers
- version_number: 1
- version_date: `2024-01-26T14:56:39.895+01:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

To learn more, follow the link: [CONFLUENCE_PAGE title='2022x News for Developers' space='MD2022x']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To learn more, follow the link: <ac:link><ri:page ri:space-key="MD2022x" ri:content-title="2022x News for Developers" /></ac:link></p>
````

<!--NOMAGIC_PAGE id=187334783 space=CEA2024xR2 version=4 -->
## PAGE 00002: 2024x Refresh1 Version News

- page_id: `187334783`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/187334783/2024x+Refresh1+Version+News
- version_number: 4
- version_date: `2024-12-16T15:10:59.974+01:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

top

[IMAGE alt='' src='']

Released on: July 5, 2024

Beginning with version 2024x Refresh1, significant enhancements have been made to various diagramming tools and tables. The**Security Connectivity**and**Security Role-based Connectivity**tables have been restructured into dedicated diagrams for better clarity on Operational and Resource viewpoints. The**Strategic Driver Map**now visually connects Drivers, Enterprise Goals, and Strategic Phases, while the new**Strategic Drivers Table**organizes elements, such as Drivers, Challenges, Opportunities, and Capabilities, in a structured format. The**Preview Affected Diagrams**dialog has been introduced for easier management and preview of affected diagrams, with new options for updating diagram elements. Enhancements to**Gantt Charts**include better project and milestone management and display options for projects. Measurement management has been improved with features for reusing default values and auto-populating measurements in Property Sets. Additionally, model conversion between frameworks and new validation rules have been implemented to streamline processes and ensure data integrity.

SysML features introduce several improvements to Item Flow management. You can now navigate from a selected Item Flow in the Containment tree to the diagrams where it is realized, specify Conveyed Items from the Diagram Palette, and hide arrow notations on realizing elements when the Conveyed Item is hidden or unspecified. Conveyed Items are now represented with icons in the 'Create / Edit Item Flow' dialog. Item Flow creation between Activity Parameter Nodes and Actions has been enhanced. Two new validation rules highlight Item Flows without Conveyed Items. The 'Preview Affected Diagrams' dialog further enhances the Item Flow management experience by presenting all affected diagrams.

Furthermore, the 2024x Refresh1 release contains new validation solvers for the 'Invalid Connector' validation rule, allowing for an easy connector redefinition. The new release also introduces the MagicGrid perspective.

Simulation features introduce several significant enhancements. One of the key updates is the ability toanimate behavioral diagrams during server-side simulationby embedding theminto HTML-generated user interfaces. The latest product version also supports model data export to the SSP file format,allowing you transfer models between different simulation tools, such as Dymola. Furthermore, you can now load and play external simulation results from CSV files using the Results Player.Additionally, a new project option allows you to display runtime values on Port labels during simulation, providing immediate insights into model behavior. The new release also supports Matlab integration for Apple Silicon,allows enabling and disabling simulation annotations in diagrams, offers improvements to the ALH.callOperation method and built-in math functions, and more.

Client-side performance enhancements include optimized efficiency for exporting matrices and tables in SVG format. For general modeling, this release improves Information Flow management. You can now easily navigate from a selected Information Flow in the Containment tree to the diagrams where it is realized and specify Conveyed Information directly in the diagram. You can choose to hide arrow notations on realizing elements when the Conveyed Information is hidden or unspecified. Conveyed Information is now represented with icons in the 'New Conveyed Information' dialog. New validation rules highlight Information Flows that do not have any Conveyed Information.

Additional enhancements include the improved samples access and navigation in the modeling tool. Also, a new 'Letter Spacing Reduction in SVG' environment option is introduced to control the spacing between letters when exporting diagram images in SVG format.

Additionally, collaborative modeling brings several enhancements tothe Model Patch functionality, which is now out of the technology preview phase. The Model Patch UI has been improved with a new panel that identifies and explains issues related to model patch application. Project commit processes are now more efficient with a First-In-First-Out (FIFO) queue system for simultaneous commits. Finally, you can save time by skipping the migration of archived branches when migrating Teamwork Cloud projects and more.

Collaboration powered by the **3D**EXPERIENCE platform introduces significant improvements as well. You can now move Teamwork Cloud projects to the 3DEXPERIENCE platform and then update these projects using the .szip file format. In addition, the History and Edit Branches dialogs now indicate if and from which iteration a project was merged.

To download the latest version of the modeling tool, see [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']. For further information, check the [CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024xR1'].

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

### UAF Features

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
- With this version, when you hide the realized exchanges, you can choose to hide the arrow notation on the realizing elements as well. The **Hide Information Flow If Conveyed Information Is Missing**[Project option](https://docs.nomagic.com/display/UAF12P2024xR2/Setting+project+options)controls the arrow visibility.
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

### SysML Features

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

### Simulation Features

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

### Client side performance improvementsClient-side Performance Improvements

##### Improvements in Diagram Export as SVG

Exporting diagrams in Scalable Vector Graphics (*.svg) format now features significant optimizations, with the most notable improvements in matrix and table exports:

- Reduction in the file size of exported SVG files.
- Export now requires up to 10 times less RAM resources.
- Decreased duration of the export process.

These optimizations enhance the efficiency of exporting matrices and tables in SVG format, resulting in significantly reduced file sizes. The improvements impact various functionalities that utilize SVG image generation, such as image export via the MDZipX plugin or the 'Save as Image' command.

[IMAGE alt='' src='']

###### A chart comparing the file size of a Dependency Matrix exported as a SVG image in 2024x and 2024x Refresh1.

### miModeling and Infrastructure

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

### CollaborationCollaboration

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

### Collaboration Powered by **3D**EXPERIENCE Platform

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7dc7bee2-3797-466f-982b-5a1e0d78e7c5"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><p><span class="confluence-embedded-file-wrapper image-center-wrapper"><ac:image ac:align="center" ac:width="465"><ri:attachment ri:filename="CEA.png" /></ac:image></span></p><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: July 5, 2024</span></p><p><br /></p><p><span><span style="color: rgb(23,43,77);">Beginning with version 2024x Refresh1, significant enhancements have been made to various diagramming tools and tables. The </span><strong>Security Connectivity</strong><span style="color: rgb(23,43,77);"> and </span><strong>Security Role-based Connectivity</strong><span style="color: rgb(23,43,77);"> tables have been restructured into dedicated diagrams for better clarity on Operational and Resource viewpoints. The </span><strong>Strategic Driver Map</strong><span style="color: rgb(23,43,77);"> now visually connects Drivers, Enterprise Goals, and Strategic Phases, while the new </span><strong>Strategic Drivers Table</strong><span style="color: rgb(23,43,77);"> organizes elements, such as Drivers, Challenges, Opportunities, and Capabilities, in a structured format. The </span><strong>Preview Affected Diagrams</strong><span style="color: rgb(23,43,77);"> dialog has been introduced for easier management and preview of affected diagrams, with new options for updating diagram elements. Enhancements to </span><strong>Gantt Charts</strong><span style="color: rgb(23,43,77);"> include better project and milestone management and display options for projects. Measurement management has been improved with features for reusing default values and auto-populating measurements in Property Sets. Additionally, model conversion between frameworks and new validation rules have been implemented to streamline processes and ensure data integrity.</span></span></p><p><span>SysML features introduce several improvements to Item Flow management. You can now navigate from a selected Item Flow in the Containment tree to the diagrams where it is realized, specify Conveyed Items from the Diagram Palette, and hide arrow notations on realizing elements when the Conveyed Item is hidden or unspecified. Conveyed Items are now represented with icons in the 'Create / Edit Item Flow' dialog. Item Flow creation between Activity Parameter Nodes and Actions has been enhanced. Two new validation rules highlight Item Flows without Conveyed Items. The 'Preview Affected Diagrams' dialog further enhances the Item Flow management experience by presenting all affected diagrams.</span></p><p><span>Furthermore, the 2024x Refresh1 release contains <span style="color: rgb(14,16,26);">new validation solvers for the 'Invalid Connector' validation rule, allowing for an easy connector redefinition. T</span></span><span style="color: rgb(14,16,26);">he new release also introduces the MagicGrid perspective. </span></p><p><span>Simulation features introduce several significant enhancements. One of the key updates is the ability to</span><span> </span><span>animate behavioral diagrams during server-side simulation </span><span>by embedding them</span><span> </span><span>into HTML-generated user interfaces</span><span>. The latest product version also supports model data export to the SSP file format, </span><span style="color: rgb(33,37,41);"><span style="color: rgb(13,13,13);">allowing you transfer models between different simulation tools, such as Dymola</span></span><span>. Furthermore, you can now load and play external simulation results from CSV files using the Results Player. </span><span>Additionally, a new project option allows you to display runtime values on Port labels during simulation, providing immediate insights into model behavior. The new release also supports Matlab integration for Apple Silicon, </span><span>allows enabling and disabling simulation annotations in diagrams, offers improvements to the ALH.callOperation method and built-in math functions, and more.</span></p><p><span>Client-side performance enhancements include optimized efficiency for exporting matrices and tables in SVG format. For general modeling, this release improves Information Flow management. You can now easily navigate from a selected Information Flow in the Containment tree to the diagrams where it is realized and specify Conveyed Information directly in the diagram. You can choose to hide arrow notations on realizing elements when the Conveyed Information is hidden or unspecified. Conveyed Information is now represented with icons in the 'New Conveyed Information' dialog. New validation rules highlight Information Flows that do not have any Conveyed Information.</span></p><p><span>Additional enhancements include the improved samples access and navigation in the modeling tool. Also, a new 'Letter Spacing Reduction in SVG' environment option is introduced to control the spacing between letters when exporting diagram images in SVG format.</span></p><p>Additionally, collaborative modeling brings several enhancements to<span> the Model Patch functionality, which is now out of the technology preview phase. The Model Patch UI has been improved with a new panel that identifies and explains issues related to model patch application. Project commit processes are now more efficient with a First-In-First-Out (FIFO) queue system for simultaneous commits. Finally, you can save time by skipping the migration of archived branches when migrating Teamwork Cloud projects and more.</span></p><p><span>Collaboration powered by the <strong>3D</strong>EXPERIENCE platform introduces significant improvements as well. You can now move Teamwork Cloud projects to the 3DEXPERIENCE platform and then update these projects using the .szip file format. In addition, the History and Edit Branches dialogs now indicate if and from which iteration a project was merged.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[product documentation]]></ac:plain-text-link-body></ac:link>.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong><ac:link ac:anchor="UAF Features" /></strong></p><ul><li><ac:link ac:anchor="Diagraming" /></li><li><ac:link ac:anchor="Report templates" /></li><li><ac:link ac:anchor="Gantt Chart Enhancements" /></li><li><ac:link ac:anchor="Exchange Management" /></li><li><ac:link ac:anchor="Measurement Management Enhancements" /></li><li><ac:link ac:anchor="Model Conversion Between Frameworks Improvements" /></li><li><ac:link ac:anchor="Validation" /></li><li><ac:link ac:anchor="Discontinued Features" /></li><li><ac:link ac:anchor="Other Enhancements" /></li></ul><p><strong><ac:link ac:anchor="SysML Features" /></strong></p><ul><li><ac:link ac:anchor="Affected Diagrams Preview Dialog" /></li><li><ac:link ac:anchor="Item Flows Management" /></li><li><ac:link ac:anchor="Connector Redefinition" /></li><li><ac:link ac:anchor="MagicGrid Perspective" /></li></ul></ac:layout-cell><ac:layout-cell><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Client side performance improvements"><ac:plain-text-link-body><![CDATA[Client-side Performance Improvements]]></ac:plain-text-link-body></ac:link></strong><ul><li><ac:link ac:anchor="Improvements in Diagram Export as SVG" /></li></ul><p><strong><ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link></strong></p><ul><li><ac:link ac:anchor="Information Flow Management Improvements" /></li><li><ac:link ac:anchor="Improved Samples Access and Navigation" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul><p><strong><ac:link ac:anchor="Simulation Features" /></strong></p><ul><li><ac:link ac:anchor="What's New in Server-Side Simulation" /><ul><li><ac:link ac:anchor="Diagram Animation Support" /></li><li><ac:link ac:anchor="Other" /></li></ul></li><li><p><ac:link ac:anchor="SSP Export Support" /></p></li><li><p><ac:link ac:anchor="Results Player" /></p></li><li><p><ac:link ac:anchor="Displaying Runtime Values on Port Labels" /></p></li><li><p><ac:link ac:anchor="Easier Access to Nested Properties" /></p></li><li><p><ac:link ac:anchor="Other Improvements" /></p></li></ul></ac:layout-cell><ac:layout-cell><p><strong><ac:link ac:anchor="Collaboration" /></strong></p><ul><li><ac:link ac:anchor="Model Patch Functionality Improvements" /></li><li><ac:link ac:anchor="Commit Queues" /></li><li><ac:link ac:anchor="Other" /></li></ul><p><strong><ac:link ac:anchor="Collaboration Powered by 3DEXPERIENCE Platform" /></strong></p><ul><li><ac:link ac:anchor="Moving Projects to the 3DEXPERIENCE Platform" /></li><li><ac:link ac:anchor="Iteration Merge Information" /></li><li><ac:link ac:anchor="Performance Improvements" /></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>UAF Features</h1></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Diagraming</h3></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><h4 style="text-align: left;margin-left: 40.0px;">Security Connectivity and Role-Based Connectivity Tables</h4><p style="text-align: left;">Beginning with version 2024x Refresh1, the Security Connectivity and Security Role-based Connectivity tables have been redesigned into dedicated diagrams focusing on the Operational and Resource viewpoints:</p><ul style="text-align: left;"><li>Security Connectivity (Resource) Table</li><li>Security Role-based Connectivity (Resource) Table</li><li>Security Connectivity (Operational) Table</li><li>Security Role-based Connectivity (Operational) Table</li></ul></ac:layout-cell><ac:layout-cell><p><ac:image ac:align="center" ac:height="241"><ri:attachment ri:filename="role_based_table_evolution.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h4 style="text-align: left;margin-left: 40.0px;">Strategic Driver Map</h4><p style="text-align: left;"><span style="color: rgb(23,43,77);">This predefined map includes the Driver, Enterprise Goals, and/or Enterprise Objectives that are related to a Driver using the Motivated By relationship, and Actual Strategic Phases that are related to the Enterprise Goals or Enterprise Objectives using the Phases relationship.<span>  </span></span></p><p style="text-align: left;"><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="strategic_driver_map.png" /></ac:image></span></p><h4 style="margin-left: 40.0px;">Strategic Driver Table</h4><p><span>The new Strategic Drivers Table allows you to assemble Drivers, Challenges, Opportunities, and Capabilities in a tabular form in strict order:  the Driver presenting Challenges, the Challenges motivating Opportunities, and the Opportunities impacting Capabilities.</span></p><p style="text-align: left;"><span style="color: rgb(23,43,77);">In this table, you can also define relationships between Drivers and Challenges, Challenges and Opportunities, Opportunities and Capabilities. This table captures the Driver, Challenge, Opportunity, and Capability elements.</span></p><p style="text-align: left;"><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="strategic_driver_table.png" /></ac:image></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h4 style="margin-left: 40.0px;">Affected Diagrams Preview Dialog</h4><p>To enhance the exchange creation and management experience in Resource, Service, and Operational viewpoints, we have introduced the <strong>Preview Affected Diagrams</strong> dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements, where the created Exchanges will be realized, are prominently marked in the diagram preview pane.</p><p>During the preview process, you can select the <strong>Update Diagram</strong> check box for diagrams in which you wish to display the Conveyed Items of the selected exchange.</p><p><span style="color: rgb(23,43,77);">The new<span> </span></span><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[Project option]]></ac:plain-text-link-body></ac:link><strong><span> </span>Show Item Flows on Affected Diagrams</strong><span style="color: rgb(23,43,77);"><span> </span>controls how the diagrams will be updated for newly created or modified exchanges. Set the option to true to update all affected diagrams and show the Conveyed Items of exchanges whenever a new exchange is created or an existing one is modified. </span><span> </span></p><p><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Preview Affected Diagrams dialog" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link><span> </span></p><p><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="preview_affected_v2.png" /></ac:image></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Report templates</h3><ul><li>The new report templates have been implemented for <span style="color: rgb(23,43,77);">Service Connectivity Table and Service Role-based Connectivity Table. The reports are available through the Report Wizard.</span></li></ul><p><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="service_reports.png" /></ac:image></span></p><ul><li><span style="color: rgb(23,43,77);">A new Strategic Driver Table also makes a new report available. You can create the report through the Report Wizard, directly from the table toolbar, or using a quick report option from the Containment tree.</span></li></ul><p><span style="color: rgb(23,43,77);"><ac:image ac:align="center"><ri:attachment ri:filename="strategic_driver_table_report.png" /></ac:image></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Gantt Chart Enhancements</h3><h4 style="margin-left: 40.0px;">Project Roadmap Enhancements</h4><ul><li><span>The new Actual Project Assignment wizard will help you add new Actual Projects to the chart more conveniently. </span><span>With this wizard, you will:</span><ul><li>Have the ability to reuse existing Projects as created Actual Project types<br /><ac:image><ri:attachment ri:filename="actual_project_assignmnet_wizard.png" /></ac:image></li><li>Control Actual Projects hierarchy creation based on the existing Project structure. </li></ul></li><li><p style="text-align: left;">Two additional steps were added to the Actual Project Milestone Creation wizard. With these steps, you can specify the Actual Project Milestone Version Released and Version Withdrawn properties during milestone creation.<br /><ac:image><ri:attachment ri:filename="actual_project_milestone_creation_wizard.png" /></ac:image></p></li><li><p><span style="color: rgb(23,43,77);">The new<span> </span></span><strong style="text-align: left;">Display Actual Projects as Grouping Elements</strong><span style="color: rgb(23,43,77);"><span> </span>option (located in the Gantt chart options area) is introduced. This option controls how the Actual Project is displayed:</span></p><ul><li><span style="color: rgb(23,43,77);">Turn the option on to display the Actual Project only as a grouping element.</span></li><li><span style="color: rgb(23,43,77);">Turn the option off to display the grouping Actual Project bars with Actual Project Milestones and completion progress.</span></li></ul><span style="color: rgb(23,43,77);"><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Customizing Gantt chart properties" /><ac:plain-text-link-body><![CDATA[Learn more about customizing Gantt chart >>>]]></ac:plain-text-link-body></ac:link> <br /><ac:image><ri:attachment ri:filename="actual_project_as_grouping_element.png" /></ac:image></span></li></ul><h4 style="margin-left: 40.0px;"><span>Strategic Phasing Gantt Chart Enhancements</span></h4><ul><li><span>You can now choose whether you want to show or hide selected Capability's Provisions in the Capability Provisions area in the </span>Strategic Phasing Gantt Chart.<span> </span><ac:image><ri:attachment ri:filename="show_hide_capability_provisions_area_strategic_phasing.png" /></ac:image></li><li>Now, when creating a Strategic Phasing Gantt Chart, you can choose to add Capabilities and Resources from the used projects. These elements will be displayed in gray to indicate that they come from a used project. </li></ul><h4 style="margin-left: 40.0px;">Other</h4><ul><li><span style="color: rgb(23,43,77);">The Gantt charts were enhanced to indicate when an element is used from another project and/or is read-only, with the element name displayed in gray to signify this status. </span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Exchange Management</h3><ul><li><p>The functionality when reconnecting connectors between elements was improved, offering options for managing exchanges. Now, the modeling tool checks the flow properties of source and target ports (if defined), recommending suitable exchanges for realization. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Working with exchanges" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link> </p></li><li>You can now specify a Conveyed Item directly in the diagram, picking the needed Conveyed Item element from the diagram palette and dragging it on to the exchange. <br /><ac:image><ri:attachment ri:filename="set_conveyed_item_palette_personnel.png" /></ac:image></li><li>Now the Conveyed Items in the Realized Exchange wizards are represented with icons to help you identify the Conveyed Items. </li><li><span style="color: rgb(23,43,77);">With this version, when you hide the realized exchanges, you can choose to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements as well. The<span> </span></span><span style="color: rgb(23,43,77);"><strong>Hide Information Flow If Conveyed Information Is Missing</strong><span> </span><a href="https://docs.nomagic.com/display/UAF12P2024xR2/Setting+project+options">Project option</a><span> </span>controls the arrow visibility. </span></li><li><span style="color: rgb(23,43,77);">You can now easily navigate from the selected exchange in Containment tree to the diagrams where that exchange is realized. <br /><ac:image><ri:attachment ri:filename="Navigation to realizing elements in symbolic diagrams.png" /></ac:image></span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Measurement Management Enhancements</h3><p style="text-align: left;"><span>With this version, we have enhanced measurements management for Property Sets and Measurable Elements.</span></p><ul><li>Before the 2024xR1 release, you had the ability to define actual values for all measurements within Measurement Sets or Property Sets. Now, with the introduction of the 2024xR1 release, you can effortlessly reuse default actual values to define the entire structure of Actual Property Sets. This enhancement includes the implementation of the <strong>Default value</strong> button, conveniently accessible within the Specification window. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Applying Actual Measurements" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link></li></ul><p style="margin-left: 40.0px;"><span><ac:image><ri:attachment ri:filename="measurements_1.png" /></ac:image></span></p><ul><li><span><span style="color: rgb(23,43,77);">Prior to the 2024xR1 release, automatic population of measurements was limited to Measurable Elements only, with no capability for Property Sets. With the introduction of the 2024xR1 release, you now have the ability to automatically populate measurements on Property Sets as well. Measurements are created for elements with the <strong>Applies for</strong> tag values (stereotyped with «DoDAFProperties») applied, and the newly created measurements are typed by the elements with the «DoDAFProperties» stereotype applied. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Setting up Automatic Population of Measurement Sets" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link><br /></span></span></li></ul><p style="margin-left: 40.0px;"><span><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="measurements_applyFor_tag.png" /></ac:image><br /></span></span></p><ul><li>Before the 2024x R1 release, reusing and synchronization of Measurement structures was not feasible in UAF. With the release of the 2024x R1, you can now leverage this functionality for Property Set usages, including Assets and Roles, as well as Measurement Sets and Measurements. This enhancement enables the creation of an Actual Property Set structure suggested based on the structure of the Property Set typing the Measurable Element, with default values also suggested.</li></ul><p style="margin-left: 40.0px;"><span>Existing Actual Property Sets of the Measurable Element type are recommended, and this allows you to review and adjust them as needed. Additionally, the newly created Actual Property Set is applied as a default value of the Measurable Element.</span></p><p style="margin-left: 40.0px;"><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Reusing Measurement Sets for Actual Property Set creation" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link></p><p style="margin-left: 40.0px;"><ac:image><ri:attachment ri:filename="Reusing measurements structure owned by roles type.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Model Conversion Between Frameworks Improvements</h3><p>The project conversion between different Enterprise Architecture Frameworks has undergone some improvements and now adds more clarity. The framework packages are seamlessly mapped during conversion, with package names adjusted accordingly. Custom-named packages remain unchanged, while multiple packages with identical names are merged into one.</p><p><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Converting model between Enterprise Architecture Frameworks" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="converting_frameworks_wn.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Validation</h3><ul><li><span style="color: rgb(23,43,77);">The COR2185 validation rule was improved to synchronize Measurement Sets of the validated element, located in the Measurement Set property, with Measurement Sets of the associated element: extending beyond Measurable Elements to include Property sets that own the measurements typed by Measurement Sets. </span></li><li><span style="color: rgb(23,43,77);">New completeness validation rules (COM2028, COM2029, COM2030) have been implemented for Operational, Resource, and Service viewpoints to highlight exchanges that are not realized by any realizing element. </span></li><li><span style="color: rgb(23,43,77);">The new correctness validation rule COR2184 was implemented to check whether the Actual Project Start and End dates enclose the dates of its owned Actual Projects. </span></li><li><span style="color: rgb(23,43,77);">The COR2196 correctness validation rule was implemented to check whether the date of the Actual Project Milestone does not precede the date of its referenced Actual Project Milestones. </span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Discontinued Features</h3><ul><li><span>The PES export functionality is no longer available. </span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Other Enhancements</h3><ul><li><span>One more way to model conjugated ports is to create the Conjugated Operational/Resource/Resource Service/Service/ Interface, which has the same features as its original Interface except that its Flow Properties are reversed (conjugated). </span><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Working with conjugated Interfaces" /><ac:plain-text-link-body><![CDATA[Learn more>>>]]></ac:plain-text-link-body></ac:link><span> </span></li><li><span><span style="color: rgb(23,43,77);">You can now create a Definition and Comment for any UAF element in their <strong>Specification </strong>window &gt; <strong>Documentation/Comment</strong> property group.<br /><ac:image><ri:attachment ri:filename="definition_creation.png" /></ac:image><br /></span></span></li><li><span style="color: rgb(23,43,77);">The new Project option <strong style="text-align: left;">Show Diagram Abbreviations </strong>has been<span> introduced. Set this option to true to show diagram abbreviation in the Containment tree. <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Show diagram abbreviation in Containment tree" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link> <br /><ac:image><ri:attachment ri:filename="diagram_abbreviations_sample.png" /></ac:image></span></span></li><li><p><span>With the new Project Option <strong style="text-align: left;">Show default documentation for UAF Packages</strong>, y</span>ou can<span> </span>choose to show the default UAF Package<span> </span>documentation. Turning the option on will display the documentation<span> </span>in:</p><ul><li>The viewpoint package element's Specification window, Documentation/Comment property</li><li>The selected viewpoint package element's Documentation tab, which is located in the<span> </span>Model Browser.<br /><ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Show default documentation for UAF packages" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="default_package_documentation.png" /></ac:image></li></ul></li><li><span style="color: rgb(23,43,77);"><span>The Strategic Motivation Table has been improved. Now when you click the <strong>Add New</strong> or <strong>Add Nested</strong> button, the SysML Requirements are collapsed and you can focus only on UAF requirements - Enterprise Goal and Enterprise Objective. </span></span></li><li><span style="color: rgb(23,43,77);"><span>The creation process of UAF Instance Specifications was enhanced by enabling the creation of slots when one instance specification is dragged and dropped onto another from the diagram, diagram palette, or Containment tree when the structure of Instance Specification types is predefined.</span></span></li><li>The role-based connectivity diagrams have been enhanced by adding a <span>Context column to show the context of the element realizing the exchange</span>.  </li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>SysML Features</h1><h3>Affected Diagrams Preview Dialog</h3><p><span>To enhance the Item Flow creation and management experience, we have introduced the </span><strong>Preview Affected Diagrams</strong><span> dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements are prominently marked in the diagram preview pane conveying where the created Item Flows will be realized.</span></p><p>During the preview process, you can select the <strong>Update Diagram</strong> check box for diagrams in which you wish to display the Conveyed Items of the selected flows.</p><p><span style="color: rgb(23,43,77);">The new<span> </span></span><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link><strong><span> </span>Show Item Flows on Affected Diagrams</strong><span style="color: rgb(23,43,77);"><span> </span>controls how the diagrams will be updated for newly created or modified flows. Set the option to <em>true </em>to update all affected diagrams and show the Conveyed Items of flows whenever a new flow is created or an existing one is modified. </span></p><p><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Preview Affected Diagrams dialog" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p><span><ac:image ac:align="center" ac:alt="preview_affected_diagrams_dialog.png"><ri:url ri:value="https://docs.nomagic.com/download/attachments/146407510/preview_affected_diagrams_dialog.png?version=1&amp;modificationDate=1710870010652&amp;api=v2" /></ac:image></span></p><h4>Item Flows Management</h4><ul><li><span style="color: rgb(23,43,77);">Interactions can be modeled across various diagrams in both behavior and structure models, creating difficulties in locating diagrams representing Item Flow realizations and hindering transparency in their identification. Now you can easily navigate from the selected Item Flow in the Containment tree to the diagrams where the Item Flow is realized. <ac:link ac:anchor="Navigating to diagrams where Item Flow is realized"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image ac:align="center"><ri:attachment ri:filename="Navigate_to_diagram_SYSML.png" /></ac:image><br /></span></li><li><span>Specify the Conveyed Item directly in the diagram, picking the needed Conveyed Item element from the diagram palette and dragging it on to the Item Flow. </span><ac:link ac:anchor="Specifying the Conveyed Item directly on the diagram pane"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Specifying Conveyed Item via Diagram Palette.png" /></ac:image><br /></span></li><li><span style="color: rgb(23,43,77);">You can now choose whether you want to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements when the Conveyed Item is hidden or unspecified in case you would need to conceal such approximate interactions, and vice versa</span>. The <span><strong>Hide Information Flow If Conveyed Information Is Missing</strong> <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link> controls the arrow visibility. <ac:link ac:anchor="Showing/hiding the Conveyed Item"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image ac:align="center"><ri:attachment ri:filename="hide_information_flow.png" /></ac:image><br /></span></li><li><span>Now the Conveyed Items in the </span><strong>Create / Edit Item Flow</strong><span> dialog are represented with icons to help you identify the Conveyed Items.</span><span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Conveyed Item Element Icon.png" /></ac:image><br /></span></li><li><span>Item Flow creation between Activity Parameter Nodes and Actions has been enhanced to facilitate the creation of Item Flows when interactions are modeled between Part Properties. Typically, the 'Usage' allocation mode is used for this, which does not create an allocation relation on the end of the Activity Parameter Node, thereby not providing a possible sender or receiver on this end. Now, the tool checks action allocations to typed parts for Activity Parameter Nodes. Consequently, the Direction field in the <strong>Create / Edit Item Flow</strong> dialog displays suggested sender and receiver elements based on the element typing the parts to which actions are allocated.</span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Item Flow between Activity Parameter Node and Action.png" /></ac:image><h6 style="text-align: center;">On the end of the<em> input : Audio data </em>Activity Parameter Node there are no Actions, only the<em> Read and transmit the sound </em>Activity. Thus, the tool checks the model to find Actions that invoke this Activity, locating the<em> : Read and transmit the sound</em> Action in the <em>Listen the audio</em> Activity diagram. <br />Then the tool checks the allocation relationships for this action and an allocation to the <em>: Wireless Earbuds</em> Part Property is found. <br />Using this information the <strong>Create/Edit Item Flow</strong> dialog identifies the <em>Wireless Earbuds</em> Block as a possible sender of the flow, displaying<em> Wireless Earbuds </em>and <em>Processing </em>Blocks as a suggestion for the sender/receiver in the <strong>Direction </strong>field of the dialog.<br /><br /></h6></li><li><span>New validation rules (</span><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Item Flow has no Conveyed Items" /><ac:plain-text-link-body><![CDATA[IFHNCI[2]]]></ac:plain-text-link-body></ac:link><span><span class="error"> and <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Realized Item Flow has no Conveyed Items" /><ac:plain-text-link-body><![CDATA[RIFHNCI[2]]]></ac:plain-text-link-body></ac:link></span></span><span>) have been implemented to highlight Item Flows that do not have any Conveyed Items. This helps to declutter the model and identify potentially unused flows. Learn more on the <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Item Flow has no Conveyed Items" /></ac:link> and <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Realized Item Flow has no Conveyed Items" /></ac:link> pages.</span></li></ul><h3>Connector Redefinition</h3><p><span style="color: rgb(14,16,26);">New validation solvers are available for the <strong>Invalid Connector</strong> validation rule, allowing for an easy connector redefinition:</span></p><ul><li style="list-style-type: disc;"><span style="color: rgb(14,16,26);">Use the <strong>Redefine and Replace Connector</strong> solver to have a new redefining connector created if the selected connector is inherited and at least one of its ends is redefined.</span></li><li style="list-style-type: disc;"><span style="color: rgb(14,16,26);">Use the <strong>Replace with Redefining</strong> solver to replace the failed connector with the redefining one if the failed connector is already redefined in the same context.</span></li></ul><p><span style="color: rgb(14,16,26);"><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Invalid Connector (UML Correctness)" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="image-2024-4-12_8-33-47.png" /></ac:image></p><h6 style="text-align: center;">The image displays how to resolve the <span style="color: rgb(14,16,26);"><strong>Invalid Connector </strong>validation error via the <strong>Redefine and Replace Connector </strong>solver.<strong> </strong></span></h6><h3>MagicGrid Perspective</h3><p>The MagicGrid perspective has been introduced, supplementing existing perspectives, such as Full Featured or System Engineer. This perspective simplifies the modeling tool by providing only the MagicGrid-required subset of SysML elements and diagrams, making it easier to understand and navigate for users new to MagicGrid. You can manually switch perspectives via the <strong>Select Perspective</strong> dialog. Furthermore, a dialog prompting you to switch to this perspective appears whenever you create a MagicGrid project.</p><p><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Selecting perspective" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="MagicGrid_perspective.png" /></ac:image>The MagicGrid perspective available via the <strong>Select Perspective</strong> dialog.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Simulation Features</h1><h3>What's New in Server-Side Simulation</h3><h4 style="margin-left: 40.0px;">Diagram Animation Support</h4><p style="margin-left: 40.0px;"><span style="color: rgb(23,43,77);">The new release supports diagram animation when executing projects on the server. Now behavioral (Activity, State Machine, and Sequence) diagrams can be embedded into HTML-generated user interfaces and are animated during server-side simulation. </span><span><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation with UI" /><ac:plain-text-link-body><![CDATA[Learn more about simulation with UI >>]]></ac:plain-text-link-body></ac:link></span></p><p style="margin-left: 40.0px;"><br /></p><p style="margin-left: 40.0px;text-align: center;"><ac:image><ri:attachment ri:filename="diagram_animation_support.png" /></ac:image></p><h6 style="text-align: center;margin-left: 40.0px;">Diagram animation support in server-side simulation.</h6><h4 style="margin-left: 40.0px;"><br />Other</h4><ul><li style="list-style-type: none;"><ul><li><p><span style="color: rgb(23,43,77);">Now UI titles are displayed in a UI index window and you can use them to open a specific UI in a separate window.</span></p></li><li><span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">Upon successful installation, the Simulation application card is displayed on the Web Application Platform <span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">welcome page</span></span>.<span> </span></span>Opening the application will redirect you to the Server-side Simulation Swagger page.</span></li><li><span style="color: rgb(23,43,77);">The RUN endpoint has a new 'timeout' query parameter which allows you to specify the timeout duration in minutes.</span></li><li><span style="color: rgb(23,43,77);">The 'sync' query parameter has been added to the RUN, STEP, and TERMINATE endpoints. You can use them to initiate a synchronous API call in server-side simulation using Jupyter Notebook.</span></li></ul></li></ul><p style="margin-left: 40.0px;"><br /></p><h3>SSP Export Support</h3><p><span style="color: rgb(33,37,41);"><span style="color: rgb(13,13,13);">This release introduces a powerful new feature - the ability to export model data to the SSP (System Structure and Parameterization) file format. </span>SSP is a tool-independent standard used to define complete systems consisting of one or more FMUs (Functional Mockup Interfaces). <span style="color: rgb(13,13,13);">With this enhancement, you can transfer models between different simulation tools, such as Dymola, facilitating greater interoperability and collaboration. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="SSP Export - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></span></p><p><br /></p><h3>Results Player</h3><p><span style="color: rgb(13,13,13);">Now, the tool can read and play external simulation results from CSV files. You can load CSV files generated either locally or by external tools into the Results Player and then play back the simulation results in your modeling tool. The Results Player offers enhanced playback controls, allowing users to pause playback, navigate through different simulation times using a slider, and adjust playback speed according to their preferences. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Results Player - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="results_player.png" /></ac:image></p><h6 style="text-align: center;">Using the Results Player to play back simulation results from an imported CSV file.</h6><h3><br />Displaying Runtime Values on Port Labels</h3><p>A new<strong> </strong><span style="color: rgb(23,43,77);"><strong>Show Runtime Values on Port Labels</strong> </span>project option and Simulation Configuration property allows you to see runtime values on Port labels during simulation as displayed below. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Manipulating simulation information" /><ac:plain-text-link-body><![CDATA[Learn more about manipulating simulation information >>]]></ac:plain-text-link-body></ac:link></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="showing_runtime_values_on_port_labels.png" /></ac:image></p><h6 style="text-align: center;">Displaying runtime values on Port labels during simulation.</h6><h3><br />Easier Access to Nested Properties</h3><p>You no longer need complex <span style="color: rgb(23,43,77);">ALH (Action Language Helper) scripts to access deeply nested properties. With the Groovy language, you can use &quot;dot notation&quot; directly in any expression.</span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="dot_notation_in_groovy.png" /></ac:image><br /></span></p><h6 style="text-align: center;">Using &quot;dot notation&quot; in the Groovy language.</h6><h3><br />Other Improvements</h3><ul><li><span style="color: rgb(23,43,77);">The new <strong>Show Annotations</strong> project option and Simulation Configuration property allows enabling and disabling simulation annotations in diagrams. Simulation annotations include flowing information, possibility to change animation speed, and annotation tooltips. <ac:link ac:anchor="Enabling and disabling animation options"><ri:page ri:space-key="CST2024xR1" ri:content-title="Displaying simulation information" /><ac:plain-text-link-body><![CDATA[Learn more about animation options >>]]></ac:plain-text-link-body></ac:link></span></li><li><span style="color: rgb(23,43,77);">Matlab integration is now supported for Apple Silicone.</span></li><li><span style="color: rgb(23,43,77);">The ALH.callOperation method has been enhanced and now supports calling operations through ports.</span></li><li>This release introduces several new methods of the built-in math functions.</li><li>Now you can specify the simulation license for SIMULIA when logging in to the <strong>3D</strong>EXPERIENCE platform.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="815c4f41-7b9a-4abd-a370-16ecd19fe713"><ac:parameter ac:name="">Client side performance improvements</ac:parameter></ac:structured-macro>Client-side Performance Improvements</h1><h3>Improvements in Diagram Export as SVG</h3><p>Exporting diagrams in Scalable Vector Graphics (*.svg) format now features significant optimizations, with the most notable improvements in matrix and table exports:</p><ul><li>Reduction in the file size of exported SVG files.</li><li>Export now requires up to 10 times less RAM resources.</li><li>Decreased duration of the export process.</li></ul><p>These optimizations enhance the efficiency of exporting matrices and tables in SVG format, resulting in significantly reduced file sizes. The improvements impact various functionalities that utilize SVG image generation, such as image export via the MDZipX plugin or the 'Save as Image' command.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="File Size of Dependency Matrix Exported as SVG.png" /></ac:image></p><h6 style="text-align: center;">A chart comparing the file size of a Dependency Matrix exported as a SVG image in 2024x and 2024x Refresh1.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h1><h3>Information Flow Management Improvements</h3><ul><li>Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Element usage in diagrams" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="Navigate_to_diagram_UML.png" /></ac:image></li><li>Specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><span><br /><ac:image><ri:attachment ri:filename="Specifying Conveyed Information via Diagram Palette.png" /></ac:image><br /></span></li><li>You can no<span style="color: rgb(23,43,77);">w choose whether you want to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified</span>. The <span><strong>Hide Information Flow If Conveyed Information Is Missing</strong> <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link> controls the arrow visibility. <ac:link ac:anchor="Changing the arrow notation visibility"><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="hide_information_flow_UML.png" /></ac:image><br /></span></li><li>Now the Conveyed Information in the New Conveyed Information <span>dialog is represented with icons to help you identify the Conveyed Information. </span><span><br /><ac:image><ri:attachment ri:filename="Conveyed Information Element Icon.png" /></ac:image><br /></span></li><li>New validation rules (<ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[IFHNCI[1]]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[RIFHNCI[1]]]></ac:plain-text-link-body></ac:link>)<span> have been implemented to highlight Information Flows that do not have any Conveyed Information. Learn more on the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /></ac:link> pages.</span></li></ul><h3 style="text-align: left;">Improved Samples Access and Navigation</h3><p><span>From now on, you can review the list of available samples</span><span> anytime by invoking the </span><span>Samples tab. The tab displays all the samples </span><span>provided with the modeling tool installation, providing a convenient way to review and access the needed samples. </span><span>Additionally, you can use the search bar to navigate the available content efficiently both in the Samples and Welcome tabs.</span></p><p><span><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Editor Tabs" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Improved Samples Access and Navigation.png" /></ac:image></p><h3>Other Improvements</h3><ul><li><span>A new </span><strong><span>Letter Spacing Reduction in SVG</span></strong><span> environment option is introduced to control the spacing between letters when exporting diagram images in SVG format</span>. Adjusting letter spacing enables you to maintain text alignment within shape boundaries when exporting, ensuring it does not exceed their borders. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Diagram image export" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h1><h3>Model Patch Functionality Improvements</h3><p><span style="color: rgb(0,0,0);">We are happy to announce that in this release the Model Patch functionality is coming out of the technology preview phase with several enhancements. </span><span style="color: rgb(0,0,0);">M</span><span style="color: rgb(0,0,0);">odel Patch is a more convenient alternative to a </span>full Model merge or disconnected team collaboration because it <span style="color: rgb(0,0,0);">allows you to move the selected elements or element changes from one model branch to another and transfer only a specific scope of model modifications.</span></p><p><span style="color: rgb(0,0,0);">In this version, we improved the Model Patch UI and introduced a new panel that will help you solve any problems related to model patch application</span><span style="color: rgb(0,0,0);">. This panel lists all the changes that could not be applied and describes the underlying issue for each change. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Model Patch" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="model_patch.png" /></ac:image></p><h6 style="text-align: center;">Model Patch mechanism.</h6><p><br /></p><p style="text-align: center;"><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="changes_that_are_not_applied.png" /></ac:image></span></p><h6 style="text-align: center;">A panel listing the model patch changes that could not be applied.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p><h3>Commit Queues</h3><p><span style="color: rgb(13,13,13);">You now have access to a quicker and more predictable project commit execution at the end of a long working day: simultaneous commits are processed by putting all users in a First-In-First-Out (FIFO) line, ensuring fairness and efficiency in project commits. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(13,13,13);"><ac:image><ri:attachment ri:filename="commit_queues.png" /></ac:image></span></p><h6 style="text-align: center;">The dialog showing your position in the project commit queue.</h6><h3><br />Other</h3><ul><li>Starting with version 2024x Refresh1, <span style="color: rgb(13,13,13);">you won't need to manually</span> specify the Web Application Platform URL to access specific Teamwork Cloud features like Resource Usage Map or global element usage search. Teamwork Cloud will now retrieve the URL automatically.</li><li>Now it will be possible to skip the migration of archived branches when migrating Teamwork Cloud projects, which will significantly reduce the migration time.</li><li>The project comparing functionality no longer requires the Read Resources permission for used projects. However, you still need the Read Resources permission for the main projects you want to compare.</li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Collaboration Powered by <strong>3D</strong>EXPERIENCE Platform</h1><h3>Moving Projects to the <strong>3D</strong>EXPERIENCE Platform</h3><p>We're thrilled to announce a significant step towards collaboration between Teamwork Cloud and the <strong>3D</strong>EXPERIENCE platform. With this release<span>, you will have the ability to move Teamwork Cloud projects to the <strong>3D</strong>EXPERIENCE platform using the server project file format (.szip). </span><span>Previously, the .szip file format facilitated collaboration solely between different Teamwork Cloud servers. However, with version 2024x Refresh1, we have extended its functionality to allow importing projects from .szip files to the </span><strong>3D</strong><span>EXPERIENCE platform as well and <span style="color: rgb(23,43,77);">updating them if a project already exists on the platform.</span></span></p><p><span style="color: rgb(13,13,13);">We hope that you will benefit from this new functionality and stay tuned for further improvements in future releases</span>. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Importing Teamwork Cloud projects to the 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="moving_projects_to_platform.png" /></ac:image></p><h6 style="text-align: center;"><span>Moving projects to the <strong>3D</strong>EXPERIENCE platform by using the server project file format.</span></h6><h3><span><br />Iteration Merge Information</span></h3><p style="text-align: left;">Now the <strong>History</strong> and <strong>Edit Branches</strong> dialogs show <span>if a specific project iteration was merged, as well as the iteration it was merged from.</span></p><p style="text-align: left;"><br /></p><p style="text-align: center;"><span><ac:image><ri:attachment ri:filename="project_history.png" /></ac:image></span></p><h6 style="text-align: center;"><span>The Iteration column of the History dialog displays the project merge information.</span></h6><h3><span>Performance Improvements</span></h3><p><span><span style="color: rgb(23,43,77);">The performance for various basic server operations, especially project opening, has been significantly improved. As you can see in the charts below, now projects on the <strong>3D</strong>EXPERIENCE platform open at least five times faster compared to version 2024x.</span></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="project_opening_performance.png" /></ac:image></p><h6 style="text-align: center;">The charts comparing project opening performance for projects with 2 million elements.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Refresh1 Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=194643498 space=CEA2024xR2 version=9 -->
## PAGE 00003: 2024x Refresh2 Version News

- page_id: `194643498`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/194643498/2024x+Refresh2+Version+News
- version_number: 9
- version_date: `2025-05-02T09:56:26.768+02:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

top

[IMAGE alt='' src='']

Released on: November 8, 2024

The **2024x Refresh2** release introduces key enhancements to Gantt charts, diagramming, and other capabilities, aimed at improving clarity and usability. The **Strategic Phasing Gantt Chart**now includes domain-based color-coding, and a new hierarchical view has been added to the Strategic **Actual Strategic Phase Taxonomy Table**. Other updates include enhanced element creation in UAF maps and a consistent approach to descriptions across matrices and tables.

SysML features introduce anew 'Properties to Ignore for Status Update'project option. This new project option allows you to specify the properties that, when modified, will not change the elements' status to 'updated' when importing requirements from ReqIF files.

Simulation features introduce several significant enhancements. One of the key updates is the ability toanimate behavioral diagrams during server-side simulationby embedding theminto HTML-generated user interfaces. The latest product version also supports model data export to the SSP file format, allowing you transfer models between different simulation tools, such as Dymola. Furthermore, you can now load and play external simulation results from CSV files using the Results Player.

Additionally, a new project option allows you to display runtime values on Port labels during simulation, providing immediate insights into model behavior. The new version also supports Matlab integration for Apple Silicon, allows enabling and disabling simulation annotations in diagrams, offers improvements to the ALH.callOperation method and built-in math functions, and more.

For general modeling, this release presents improvements to the Excel/CSV Sync and Excel/CSV Import functionalities, which you can now use to import connectors into your model. The model patch functionality has been enhanced as well. It now allows you to preview the specific changes that will be made to the model when applying a model patch.Additionally, thenew version allows derived properties in DSL to be customized more flexibly, enabling a specialized customization's derived property to override that of the base customization, which is ideal for user-specific needs in fields like safety and security.

Collaborative modeling introduces the ability to transfer projects between various **3D**EXPERIENCE platform instances using .szip files and improved project migration from Teamwork Cloud to the **3D**EXPERIENCE platform. Additionally, you can now create branches from any model iteration, and use a newembedded browser with**3D**Search capabilities to select and open projects.

To download the latest version of the modeling tool, see [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR2']. For further information, check the product documentation.

#### NOTE: 2024x Refresh2 Hot Fix 1 available

2024x Refresh2 Hot Fix 1 available

2024x Refresh2 Hot Fix 1 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Refresh2 Hot Fix 1 Version News' space='NMDOC']>]]>

****

****

- 
- 
- 

****

- 

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

- 
- 
- 

Starting with the 2024x Refresh2 version, the Concept Modeler plugin is no longer pre-installed with Cameo Enterprise Architecture. Key changes include:

- Separate Installation : The Concept Modeler plugin is now available for installation through the Resource/Plugin Manager as a standalone plugin. For detailed instructions, visit Installing Plugins .
- Separate Licensing : The Concept Modeler plugin now requires its own license key. To obtain the license key, contact your Dassault Systèmes Sales Contact or Distributor with the necessary technical details. More information is available at Obtaining License Keys .

### Discover CATIA SysML v2 Early Experience Program

Through the **Early Experience Program**, participants gain early access to the implementation of the **OMG SysML v2**standard across the CATIA Magic and No Magic (Cameo) product lines and alongside SysML v1.

- 100% Standard Conformance to the OMG SysML v2 specification metamodel
- Synchronized Textual and Graphical Authoring
- Extensibility and Customization adaptable to meet unique user needs
- SysML v2 REST API Integration to enhance interoperability
- Model evaluation

To**join the CATIA SysML v2 Early Experience Program**

- Install CATIA Magic/No Magic 2024x Refresh2 Desktop Client
- The designated Point of Contact (POC) from your organization should contact CATIA.EMEAR.sysml2-eep@3ds.com

[IMAGE alt='' src='']

### UAF Features

Gantt Chart Improvements

- Now, in the Strategic Phasing Gantt Chart, Capability Provision area, the bars color is shown according to the domain. [ATTACHMENT filename='strategic_phasing_colors.png']
- In the 2024x Refresh2 version, the Strategic Phasing Gantt Chart has been improved. If there are duplicate Exhibit relationships connecting the same element pairs, they will now be displayed as a single bar in the Gantt Chart. [ATTACHMENT filename='Entry aggregation.png']
- You can now adjust the visible part of the Gantt chart bars. You can either shift the bars to the left based on the selected bar's start date and marking options, or keep the default view, determined by the earliest bar date and marking options. 
[IMAGE alt='' src='']

- Beginning with this version, you can view and resolve failing validation(s) directly in the Project Roadmap Gantt charts. Actual Project Milestones are now highlighted when at least one validation rule fails. [ATTACHMENT filename='validation_gantt_chart.png']
- The Personnel Availability Gantt Chart has been enhanced. Now, the Actual Persons that were removed from a chart (Remove from Chart action) are no longer displayed, regardless of whether the **Display Actual Persons in Different Lines** option is enabled or disabled.

### Diagramming

- Several improvements have been added to the [CONFLUENCE_PAGE title='Working with Strategic Actual Strategic Phase Taxonomy Table' space='UAF12P2024xR2'] , including:
  - Implementation of a hierarchical view of instances in both Compact and Complete tree display modes.
  - Updates to the functionality for adding new or existing items.
  - Enhancements to the All View report.

[IMAGE alt='' src='']

### Other Enhancements

- UAF requirement refactoring has been enhanced to improve identifier prefix updates. Now, when you refactor UAF requirements, the identifier prefixes are also updated. For example, refactoring an Enterprise Goal to an Enterprise Objective changes the prefix from EG to EO, and vice versa.
- The process for creating elements in the UAF predefined map has been enhanced. When the scope is set in the relation map, the owner of the created elements will now be the same as the diagram owner.
- The owning package selection in Gantt Charts, Forecast Tables, and Strategic Drivers Table wizards has been improved. You can now filter to display only packages or both types and packages to be selected as owners.
- The description area for matrices now displays the information in the same way as t he description areas of the tables and maps. [Lear more >>>](https://docs.nomagic.com/display/UAF12P2024xR2/Working+with+matrices#Workingwithmatrices-Descriptionarea)

### SysML Features

##### Improvements

- A new Properties to Ignore for Status Update project option has been introduced that allows you to specify those properties that, when modified, will not change the elements' status to 'updated' when importing requirements from ReqIF files. It enables more efficient requirement management by preventing unnecessary status updates when specified properties are modified during ReqIF imports. [CONFLUENCE_PAGE title='Setting project options' space='SYSMLP2024xR2']>]]>

### Simulation Features

##### Results Player Improvements

The latest release adds several improvements to the Results Player aimed at enhancing data analysis and usability:

- The Results Player can generate a Time Series Chart for the selected properties using data from a CSV file. This feature provides an easier way to visualize results, making data analysis more seamless. [CONFLUENCE_PAGE title='Results Player - Technology Preview' space='CST2024xR2']>]]> [ATTACHMENT filename='time_series_chart_from_results_player.png']
- You can now export the current time step data from the Results Player to an Instance Specification. This allows you to save data from a CSV file back to the model and use it for simulation if required. [CONFLUENCE_PAGE title='Results Player - Technology Preview' space='CST2024xR2']>]]> [ATTACHMENT filename='exporting_time_stamp_data.png']
- The Results Player now supports the drag-and-drop functionality for files, both from the file system and the containment tree. You can drag files directly into the results panel to load them. [CONFLUENCE_PAGE title='Results Player - Technology Preview' space='CST2024xR2']>]]> [ATTACHMENT filename='drag_and_drop.png']

##### SIMULIA Process Composer Integration

We are thrilled to announce that the SIMULIA Process Composer integration has officially moved out of the technology preview phase, introducing several key improvements. You can now execute SIMULIA simulation templates on both on-premise and cloud deployments of the **3D**EXPERIENCE platform, including execution on private stations, provided you are using platform version 2024x FD01 or later. Additionally, simulation templates now support Array parameters.

[CONFLUENCE_PAGE title='SIMULIA Process Composer Integration' space='CST2024xR2']>]]>

##### Automated Simulation in Dymola

In the previous release, simulation features introduced the ability to export model data to the SSP (System Structure and Parameterization) file format, which you could use to transfer models to other simulation tools. In version 2024x Refresh2, we have enhanced the SSP export functionality, allowing you to export model data to SSP, simulate it in Dymola, and then load the results to the Results Playerwith just one click.

[IMAGE alt='' src='']

###### Automated simulation in Dymola.

##### Other Improvements

- Now simulation features include an Image Library offering a variety of icons that can be displayed on diagram shapes. [ATTACHMENT filename='image_library.png']
- The SIMULIA Process Composer properties have been moved from the login dialog the Project Options. In addition, the available execution license is chosen automatically when executing a SIMULIA template.

### miModeling and Infrastructure

##### Connectors Import via Excel/CSV Sync and Excel/CSV Import

You can now import connectors from Excel and CSV files into your model in addition to other elements. Specify the needed connectors in the Excel/CSV file and import the data from the file into your model via[CONFLUENCE_PAGE title='Sync with Excel or CSV files' space='MD2024xR2']or[CONFLUENCE_PAGE title='Importing data from Excel or CSV files' space='MD2024xR2'].

[IMAGE alt='' src='']An example of importing connectors from an Excel file into a model via[CONFLUENCE_PAGE title='Sync with Excel or CSV files' space='MD2024xR2'].

##### Model Patch Improvements

Before applying a patch, you can now preview the specific changes that will be made to the model. This enhancement allows you to better understand the impact the patch will have on the model. Additionally,tag modification is now treated as one changerather tracking individual tag values, ensuring more consistent and predictable outcomes during patch application.

[IMAGE alt='' src='']

###### The Apply Patch dialog allowing you to review the patch contents and related model changes before the patch application.

#### Other Improvements2Other Improvements

- The new version introduces greater flexibility for customizing derived properties in DSL: when a base customization generalizes another and the inherited derived property is redefined, the specialized customization’s derived property overrides that of the base customization. This allows flexible customization, where the specialized derived property takes precedence over the base, enabling further customization of derived properties, which is particularly useful in domains like safety, reliability, and security, where user-specific modifications are common.

### Collaboration Powered by **3D**EXPERIENCE Platform

##### Collaboration Between Disconnected **3D**EXPERIENCE Platforms

We are excited to announce that with the 2024x Refresh2 release, you can now transfer projects between various **3D**EXPERIENCE platforms using the server project file format (.szip). Previously, .szip files could only be generated from Teamwork Cloud projects and imported into either another the Teamwork Cloud server or a **3D**EXPERIENCE platform. Now, the .szip format can also be used to back up projects directly from the **3D**EXPERIENCE platform, enabling seamless collaboration between disconnected platform instances.

We have also improved the workflow for migrating projects from Teamwork Cloud to the **3D**EXPERIENCE platform. When importing .szip files, you can now upgrade used projects to a newer standard profile version, thus ensuring compatibility and consistency.

##### More Flexible Model Branching

In previous versions, model branches could only be created from the latest iteration of a selected revision. From version 2024x Refresh2, you can create branches from any model iteration, which provides greater control over model development process.

##### Embedded **3D**Search

If you use the **3D**EXPERIENCE platform version 2025x or later, you can now enjoy a new and improved user interface when selecting and opening projects. You can now browse projects in the embedded browser and use **3D**Search capabilities to filter them.

[IMAGE alt='' src='']

###### The **Open Server Project** dialog with an embedded browser and **3D**Serach capabilities.

[CONFLUENCE_PAGE title='2024x Refresh2 Version News' space='NMDOC']>]]>

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7dc7bee2-3797-466f-982b-5a1e0d78e7c5"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><p><span class="confluence-embedded-file-wrapper image-center-wrapper"><ac:image ac:align="center" ac:width="465"><ri:attachment ri:filename="CEA.png" /></ac:image></span></p><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: <span style="color: rgb(128,128,128);">November 8</span>, 2024</span></p><p><br /></p><p><span style="color: rgb(62,63,64);">The <strong>2024x Refresh2</strong> release introduces key enhancements to Gantt charts, diagramming, and other capabilities, aimed at improving clarity and usability. The <strong>Strategic Phasing Gantt Chart </strong>now includes domain-based color-coding, and a new hierarchical view has been added to the Strategic <strong>Actual Strategic Phase Taxonomy Table</strong>. Other updates include enhanced element creation in UAF maps and a consistent approach to descriptions across matrices and tables.</span></p><p><span style="color: rgb(62,63,64);">SysML features introduce a</span><span style="letter-spacing: 0.0px;"> new '</span><span style="letter-spacing: 0.0px;">Properties to Ignore for Status Update'</span><span style="letter-spacing: 0.0px;"> project option. This new project option allows you to specify the properties that, when modified, will not change the elements' status to 'updated' when importing requirements from ReqIF files.</span></p><p>Simulation features introduce several significant enhancements. One of the key updates is the ability to<span> </span><span style="color: rgb(23,43,77);">animate behavioral diagrams during server-side simulation<span> </span></span>by embedding them<span> </span><span style="color: rgb(23,43,77);">into HTML-generated user interfaces</span>. The latest product version also supports model data export to the SSP file format, <span style="color: rgb(33,37,41);"><span style="color: rgb(13,13,13);">allowing you transfer models between different simulation tools, such as Dymola</span></span>. Furthermore, you can now load and play external simulation results from CSV files using the Results Player.</p><p>Additionally, a new project option allows you to display runtime values on Port labels during simulation, providing immediate insights into model behavior. The new version also supports Matlab integration for Apple Silicon, <span style="color: rgb(23,43,77);">allows enabling and disabling simulation annotations in diagrams, offers improvements to the ALH.callOperation method and built-in math functions, and more.</span></p><p><span style="color: rgb(23,43,77);">For general modeling, this release presents improvements to the Excel/CSV Sync and Excel/CSV Import functionalities, which you can now use to import connectors into your model. The model patch functionality has been enhanced as well. It now allows you to preview the specific changes that will be made to the model when applying a model patch.<span> </span>Additionally, the<span> </span></span><span>new version allows derived properties in DSL to be customized more flexibly, enabling a specialized customization's derived property to override that of the base customization, which is ideal for user-specific needs in fields like safety and security.</span></p><p><span>Collaborative modeling introduces the ability to transfer projects between various <strong>3D</strong>EXPERIENCE platform instances using .szip files and improved project migration from Teamwork Cloud to the <strong>3D</strong>EXPERIENCE platform. Additionally, you can now create branches from any model iteration, and use a new</span><span> embedded browser with </span><strong>3D</strong><span>Search capabilities to select and open projects.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="IL2024xR2" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the product documentation.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8a330e2f-a370-4cf1-b280-b2518ae4b772"><ac:parameter ac:name="title">2024x Refresh2 Hot Fix 1 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Refresh2 Hot Fix 1 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Refresh2 Hot Fix 1 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong><ac:link ac:anchor="Discover CATIA SysML v2 Early Experience Program" /></strong></p><p><strong><ac:link ac:anchor="UAF Features" /></strong></p><ul><li><ac:link ac:anchor="Gantt Chart Improvements" /></li><li><ac:link ac:anchor="Diagramming" /></li><li><ac:link ac:anchor="Other Enhancements" /></li></ul><p><strong><ac:link ac:anchor="SysML Features" /></strong></p><ul><li><ac:link ac:anchor="Improvements" /></li></ul></ac:layout-cell><ac:layout-cell><p><strong><ac:link ac:anchor="Simulation Features" /></strong></p><ul><li><p><ac:link ac:anchor="Results Player Improvements" /></p></li><li><p><ac:link ac:anchor="SIMULIA Process Composer Integration" /></p></li><li><p><ac:link ac:anchor="Automated Simulation in Dymola" /></p></li><li><p><ac:link ac:anchor="Other Improvements" /></p></li></ul><p><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link></strong></p><ul><li><ac:link ac:anchor="Connectors Import via Excel/CSV Sync and Excel/CSV Import" /></li><li><ac:link ac:anchor="Model Patch Improvements" /></li><li><ac:link ac:anchor="Other Improvements2"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Collaboration Powered by 3DEXPERIENCE Platform" /></strong></p><ul><li><ac:link ac:anchor="Collaboration Between Disconnected 3DEXPERIENCE Platforms" /></li><li><ac:link ac:anchor="More Flexible Model Branching" /></li><li><ac:link ac:anchor="Embedded 3DSearch" /></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><ac:structured-macro ac:name="warning" ac:schema-version="1" ac:macro-id="ecb01d05-262b-473a-bdab-6dee26bcda60"><ac:rich-text-body><p style="text-align: left;">Starting with the 2024x Refresh2 version, the Concept Modeler plugin is no longer pre-installed with Cameo Enterprise Architecture. Key changes include:</p><ul style="text-align: left;"><li><strong>Separate Installation</strong>: The Concept Modeler plugin is now available for installation through the <strong>Resource/Plugin Manager</strong> as a standalone plugin. For detailed instructions, visit<span> </span><a class="external-link" href="https://docs.nomagic.com/display/IL2024xR2/Installing+plugins">Installing Plugins</a>.</li><li><strong>Separate Licensing</strong>: The Concept Modeler plugin now requires its own license key. To obtain the license key, contact your Dassault Systèmes Sales Contact or Distributor with the necessary technical details. More information is available at<span> </span><a href="https://docs.nomagic.com/display/IL2024xR2/Obtaining+License+Keys">Obtaining License Keys</a>.</li></ul></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Discover CATIA SysML v2 Early Experience Program</h1><p>Through the <strong>Early Experience Program</strong>, participants gain early access to the implementation of the <strong>OMG SysML v2 </strong>standard across the CATIA Magic and No Magic (Cameo) product lines and alongside SysML v1.</p><ul><li>100% Standard Conformance to the OMG SysML v2 specification metamodel</li><li>Synchronized Textual and Graphical Authoring</li><li>Extensibility and Customization adaptable to meet unique user needs</li><li>SysML v2 REST API Integration to enhance interoperability</li><li>Model evaluation </li></ul><p>To<strong> join the CATIA SysML v2 Early Experience Program</strong></p><ul><li>Install CATIA Magic/No Magic 2024x Refresh2 Desktop Client</li><li>The designated Point of Contact (POC) from your organization should contact <a href="mailto:CATIA.EMEAR.sysml2-eep@3ds.com">CATIA.EMEAR.sysml2-eep@3ds.com</a></li></ul><p><br /></p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="sysml-v2-image.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>UAF Features</h1></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="font-size: 24.0px;letter-spacing: -0.01em;">Gantt Chart Improvements</span></p><ul><li><span class="ghx-inner">Now, in the Strategic Phasing Gantt Chart, Capability Provision area, the bars color is shown according to the domain. <br /></span><ac:image><ri:attachment ri:filename="strategic_phasing_colors.png" /></ac:image></li><li>In the 2024x Refresh2 version, the Strategic Phasing Gantt Chart has been improved. If there are duplicate Exhibit relationships connecting the same element pairs, they will now be displayed as a single bar in the Gantt Chart.<br /><ac:image ac:height="400"><ri:attachment ri:filename="Entry aggregation.png" /></ac:image></li><li><span style="color: rgb(23,43,77);">You can now adjust the visible part of the Gantt chart bars. You can either shift the bars to the left based on the selected bar's start date and marking options, or keep the default view, determined by the earliest bar date and marking options.<br /><ac:image><ri:attachment ri:filename="bar_align.png" /></ac:image></span></li></ul><ul><li>Beginning with this version, you can view and resolve failing validation(s) directly in the Project Roadmap Gantt charts. Actual Project Milestones are now highlighted when at least one validation rule fails.<br /><ac:image><ri:attachment ri:filename="validation_gantt_chart.png" /></ac:image></li><li><span style="color: rgb(23,43,77);">The Personnel Availability Gantt Chart has been enhanced. Now, the Actual Persons that were removed from a chart (Remove from Chart action) are no longer displayed, regardless of whether the <strong>Display Actual Persons in Different Lines</strong> option is enabled or disabled.</span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Diagramming</h1><ul><li>Several improvements have been added to the <span style="color: rgb(23,43,77);"><ac:link><ri:page ri:space-key="UAF12P2024xR2" ri:content-title="Working with Strategic Actual Strategic Phase Taxonomy Table" /><ac:plain-text-link-body><![CDATA[Strategic Actual Strategic Phase Taxonomy Table]]></ac:plain-text-link-body></ac:link></span>, including:<ul><li>Implementation of a hierarchical view of instances in both Compact and Complete tree display modes.</li><li>Updates to the functionality for adding new or existing items.</li><li>Enhancements to the All View report.</li></ul></li></ul><p style="margin-left: 40.0px;"><ac:image><ri:attachment ri:filename="strategic_actual_strategic_phase_taxonomy_table_views.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Other Enhancements</h1><ul><li>UAF requirement refactoring has been enhanced to improve identifier prefix updates. Now, when you refactor UAF requirements, the identifier prefixes are also updated. For example, refactoring an Enterprise Goal to an Enterprise Objective changes the prefix from EG to EO, and vice versa.</li><li>The process for creating elements in the UAF predefined map has been enhanced. When the scope is set in the relation map, the owner of the created elements will now be the same as the diagram owner.</li><li>The owning package selection in Gantt Charts, Forecast Tables, and Strategic Drivers Table wizards has been improved. You can now filter to display only packages or both types and packages to be selected as owners.</li><li>The description area for matrices now displays the information in the same way as t<span class="ghx-inner">he description areas of the tables and maps. <a href="https://docs.nomagic.com/display/UAF12P2024xR2/Working+with+matrices#Workingwithmatrices-Descriptionarea">Lear more &gt;&gt;&gt;</a></span></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>SysML Features</h1><h3>Improvements</h3><ul><li>A new <strong>Properties to Ignore for Status Update</strong> project option has been introduced that allows you to specify those properties that, when modified, will not change the elements' status to 'updated' when importing requirements from ReqIF files. It enables more efficient requirement management by preventing unnecessary status updates when specified properties are modified during ReqIF imports. <ac:link><ri:page ri:space-key="SYSMLP2024xR2" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Simulation Features</h1><h3>Results Player Improvements</h3><p>The latest release adds several improvements to the Results Player aimed at enhancing data analysis and usability:</p><ul><li>The Results Player can generate a Time Series Chart for the selected properties using data from a CSV file. This feature provides an easier way to visualize results, making data analysis more seamless.<br /><ac:link ac:anchor="Generating a Time Series Chart"><ri:page ri:space-key="CST2024xR2" ri:content-title="Results Player - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn how to generate a Time Series Chart >>]]></ac:plain-text-link-body></ac:link><br /><br /><ac:image><ri:attachment ri:filename="time_series_chart_from_results_player.png" /></ac:image><br /><br /></li><li>You can now export the current time step data from the Results Player to an Instance Specification. This allows you to save data from a CSV file back to the model and use it for simulation if required.<br /><ac:link ac:anchor="Exporting the current step to an Instance Specification"><ri:page ri:space-key="CST2024xR2" ri:content-title="Results Player - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn how to export the current step to an Instance Specification >>]]></ac:plain-text-link-body></ac:link><br /><br /><ac:image><ri:attachment ri:filename="exporting_time_stamp_data.png" /></ac:image><br /><br /></li><li>The Results Player now supports the drag-and-drop functionality for files, both from the file system and the containment tree. You can drag files directly into the results panel to load them.<br /><ac:link ac:anchor="Loading CSV export file"><ri:page ri:space-key="CST2024xR2" ri:content-title="Results Player - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn how to load CSV files to the Results Player >>]]></ac:plain-text-link-body></ac:link><br /><br /><ac:image><ri:attachment ri:filename="drag_and_drop.png" /></ac:image></li></ul><h3>SIMULIA Process Composer Integration</h3><p>We are thrilled to announce that the SIMULIA Process Composer integration has officially moved out of the technology preview phase, introducing several key improvements. You can now execute SIMULIA simulation templates on both on-premise and cloud deployments of the <strong>3D</strong>EXPERIENCE platform, including execution on private stations, provided you are using platform version 2024x FD01 or later. Additionally, simulation templates now support Array parameters.</p><p><ac:link><ri:page ri:space-key="CST2024xR2" ri:content-title="SIMULIA Process Composer Integration" /><ac:plain-text-link-body><![CDATA[Learn more about SIMILIA Process Composer integration >>]]></ac:plain-text-link-body></ac:link></p><h3>Automated Simulation in Dymola</h3><p>In the previous release, simulation features introduced the ability to export model data to the SSP (System Structure and Parameterization) file format, which you could use to transfer models to other simulation tools. In version 2024x Refresh2, we have enhanced the SSP export functionality, allowing you to export model data to SSP, simulate it in Dymola, and <span style="color: rgb(23,43,77);">then load the results to the Results Player </span>with just one click.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="automated_simulation_in_dymola.png" /></ac:image></p><h6 style="text-align: center;">Automated simulation in Dymola.</h6><h3>Other Improvements</h3><ul><li>Now simulation features include an Image Library offering a variety of icons that can be displayed on diagram shapes.<br /><br /><ac:image><ri:attachment ri:filename="image_library.png" /></ac:image><br /><br /></li><li>The SIMULIA Process Composer properties have been moved from the login dialog the Project Options. In addition, the <span style="color: rgb(23,43,77);">available execution license is chosen automatically when executing a SIMULIA template.</span></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h1><h3>Connectors Import via Excel/CSV Sync and Excel/CSV Import</h3><p>You can now import connectors from Excel and CSV files <span>into your model in addition to other elements. Specify the needed connectors in the Excel/CSV file and import the data from the file into your model via </span><ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Sync with Excel or CSV files" /><ac:plain-text-link-body><![CDATA[Excel/CSV Sync]]></ac:plain-text-link-body></ac:link><span> or</span><ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Importing data from Excel or CSV files" /><ac:plain-text-link-body><![CDATA[ Excel/CSV Import]]></ac:plain-text-link-body></ac:link>.</p><p style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="importing_connectors_via_excel_csv_sync.png" /></ac:image><span style="color: rgb(94,108,132);">An example of importing connectors from an Excel file into a model via </span><ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Sync with Excel or CSV files" /><ac:plain-text-link-body><![CDATA[Excel/CSV Sync]]></ac:plain-text-link-body></ac:link><span style="color: rgb(94,108,132);">.</span></p><h3>Model Patch Improvements</h3><p><span>Before applying a patch, you can now preview the specific changes that will be made to the model. This enhancement allows you to better understand the impact the patch will have on the model. Additionally, </span><span style="color: rgb(23,43,77);">tag modification is now treated as one change </span><span>rather tracking individual tag values, ensuring more consistent and predictable outcomes during patch application.</span></p><p><br /></p><p style="text-align: center;"><span><ac:image><ri:attachment ri:filename="apply_patch_dialog.png" /></ac:image></span></p><h6 style="text-align: center;"><span>The Apply Patch dialog allowing you to review the patch contents and related model changes before the patch application.</span></h6><h2 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="16acec53-e369-4445-bd64-1cf04dc9fa59"><ac:parameter ac:name="">Other Improvements2</ac:parameter></ac:structured-macro>Other Improvements</h2><ul><li>The new version introduces greater flexibility for customizing derived properties in DSL: when a base customization generalizes another and the inherited derived property is redefined, the specialized customization’s derived property overrides that of the base customization. This allows flexible customization, where the specialized derived property takes precedence over the base, enabling further customization of derived properties, which is particularly useful in domains like safety, reliability, and security, where user-specific modifications are common. </li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Collaboration Powered by <strong>3D</strong>EXPERIENCE Platform</h1><h3 style="text-align: left;">Collaboration Between Disconnected <strong>3D</strong>EXPERIENCE Platforms</h3><p>We are excited to announce that with the 2024x Refresh2 release, you can now transfer projects between various <strong>3D</strong>EXPERIENCE platforms using the server project file format (.szip). Previously, .szip files could only be generated from Teamwork Cloud projects and imported into either another the Teamwork Cloud server or a <strong>3D</strong>EXPERIENCE platform. Now, the .szip format can also be used to back up projects directly from the <strong>3D</strong>EXPERIENCE platform, enabling seamless collaboration between disconnected platform instances.</p><p>We have also improved the workflow for migrating projects from Teamwork Cloud to the <strong>3D</strong>EXPERIENCE platform. When importing .szip files, you can now upgrade used projects to a newer standard profile version, thus ensuring compatibility and consistency.</p><h3>More Flexible Model Branching</h3><p>In previous versions, model branches could only be created from the latest iteration of a selected revision. From version 2024x Refresh2, you can create branches from any model iteration, which provides greater control over model development process.</p><h3>Embedded <strong>3D</strong>Search</h3><p style="text-align: left;">If you use the <strong>3D</strong>EXPERIENCE platform version 2025x or later, you can now enjoy a new and improved user interface when selecting and opening projects. You can now <span>browse projects in the embedded browser and use <strong>3D</strong>Search capabilities to filter them.</span></p><p style="text-align: left;"><br /></p><p style="text-align: center;"><span><ac:image><ri:attachment ri:filename="embedded_3dsearch.png" /></ac:image></span></p><h6 style="text-align: center;"><span>The <strong>Open Server Project</strong> dialog with an embedded browser and <strong>3D</strong>Serach capabilities.</span></h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Refresh2 Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=187334829 space=CEA2024xR2 version=1 -->
## PAGE 00004: 2024x Version News

- page_id: `187334829`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/187334829/2024x+Version+News
- version_number: 1
- version_date: `2024-04-19T13:54:42.664+02:00`
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

753686898

INLINE

top [IMAGE alt='' src='']

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
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ac060d11-24bb-43ee-828b-bfae5b72f6eb"><ac:parameter ac:name="id">753686899</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d04429d1-af39-4fcc-95f9-34e91a0b1fb5"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">753686902</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="81a963dd-d8b4-45a0-a0cc-ae8aaefef06f"><ac:parameter ac:name="id">753686898</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p style="text-align: center;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fd7d672f-fb01-4e70-8982-8ff70256549a"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro> <ac:image ac:width="465"><ri:attachment ri:filename="CEA.png" /></ac:image></p><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released: November 10<span style="color: rgb(128,128,128);">,</span> <span style="color: rgb(128,128,128);"> 2023</span> </span></p><p><br /></p><p>In the 2024x version of UAF, significant enhancements have been introduced. Behavior to Structure Synchronization has been enriched, allowing the automatic construction of structure models from defined activities and enabling one-click generation of Internal Connectivity diagrams.</p><p>Diagramming improvements include specialized Security Process Flow diagrams aligned with Operational and Resource viewpoints and new NAFv4 Structure diagrams for Logical, Service, and Physical Resource Specification Viewpoints.</p><p>Additionally, the Strategic Viewpoint now offers simplified assembly tools, such as the Strategic Motivation Table and the Impact Matrix, enhancing analysis and traceability. Exchange management has been refined for better visibility control, and various dialogs have been optimized for efficient review and management. These enhancements, along with improved library support and renamed perspectives, provide you with a more intuitive and efficient modeling experience.</p><p><span style="color: rgb(62,63,64);">In SysML modeling, the 2024x release introduces several improvements to Item Flow creation and editing. The<span> </span> <strong>Create / Edit Item Flow<span> </span> </strong>dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition,<span> </span> <strong style="text-align: left;">Autowire Parts</strong> <span> </span>and<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>command functionality regarding nested ports is now improved to treat each displayed nested port individually.</span></p><p><span>For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</span></p><p><span>Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.</span></p><p><span>We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.</span></p><p>To download the latest version, see <a href="https://docs.nomagic.com/display/IL2022xR2/Downloading+installation+files">Downloading installation files</a>. For further information, check the product documentation.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d7532128-51a7-45ef-87bc-961374545d5f"><ac:parameter ac:name="title">2024x Hot Fix 2 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Hot Fix 2 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="30610e88-4291-44f1-a1ed-49684a2d0cc5"><ac:parameter ac:name="id">243271308</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong> <ac:link ac:anchor="UAF 1.2 Features" /> </strong></p><ul><li><ac:link ac:anchor="UAF Behavior to Structure Synchronization" /></li><li><ac:link ac:anchor="Diagramming" /><ul><li><ac:link ac:anchor="New Security Process Flow diagrams" /></li><li><ac:link ac:anchor="New NAFv4 Structure diagrams" /></li><li><ac:link ac:anchor="New views in Strategic Viewpoint" /></li></ul></li><li><ac:link ac:anchor="Exchange management improvements" /><ul><li><ac:link ac:anchor="Exchange visibility management" /></li><li><ac:link ac:anchor="Realized Exchange wizard improvements" /></li><li><ac:link ac:anchor="Exchange Manager improvements" /></li><li><ac:link ac:anchor="Producing and Consuming Functions dialog improvements" /></li></ul></li><li><ac:link ac:anchor="Library Support" /></li><li><ac:link ac:anchor="Templates and Perspectives" /></li><li><ac:link ac:anchor="Other Enhancements" /></li></ul><p><strong> <ac:link ac:anchor="SysML Features" /> </strong></p><ul><li><ac:link ac:anchor="Improved Item Flow Creation and Editing" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Discontinued Features" /> </strong></p><ul><li><ac:link ac:anchor="JavaScript Nashorn Scripting" /></li><li><ac:link ac:anchor="Record Macro Functionality" /></li><li><ac:link ac:anchor="SPEM Plugin" /></li></ul><p><strong> <ac:link ac:anchor="Known Migration Issues" /> </strong></p><p><strong> <ac:link ac:anchor="Modeling and Infrastructure" /> </strong></p><ul><li><ac:link ac:anchor="DSLS Licensing" /></li><li><ac:link ac:anchor="Zoom in Model Browser" /></li><li><ac:link ac:anchor="Advanced Legend Adornments in Tables" /></li><li><ac:link ac:anchor="MIother"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"> <ac:link ac:anchor="Collaboration" /> </strong></p><ul><li><ac:link ac:anchor="Teamwork Cloud" /><ul><li><ac:link ac:anchor="New File Exchange Format for Server Projects" /></li><li><ac:link ac:anchor="Model Patch Mechanism (Technology Preview)" /></li></ul></li><li><ac:link ac:anchor="Power"><ac:plain-text-link-body><![CDATA[Power'By]]></ac:plain-text-link-body></ac:link><ul><li><ac:link ac:anchor="New Features to Manage Used Projects" /></li><li><ac:link ac:anchor="Opening Projects in Read-Only Mode" /></li></ul></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="165032c6-162e-4b91-ac3b-64ad3ac32452"><ac:parameter ac:name="id">753686901</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h5>UAF 1.2 Features</h5><h3>UAF Behavior to Structure Synchronization</h3><p>In the 2024x version, the UAF Behavior to Structure Synchronization has been enhanced. Now, you can automatically build the structure model according to defined Activities and generate an Internal Connectivity diagram by executing a single-click command. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Creating structure models by behavior models" /><ac:plain-text-link-body><![CDATA[Learn more >>>]]></ac:plain-text-link-body></ac:link></p><p><ac:image ac:align="center"><ri:attachment ri:filename="internal_connectivity_diagram_by_begavior_model_news.png" /></ac:image></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Diagramming</h3><h4>New Security Process Flow diagrams</h4><p>With version 2024x, the Security Process flow diagram has been specialized to align with two distinct Operational and Resource viewpoints, which led to the creation of two new diagrams: Security Process Flow (Operational) and Security Process Flow (Resource).</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Security Process Flow diagrams.png" /></ac:image></p><h4>New NAFv4 Structure diagrams</h4><p>New structure diagrams have been implemented in the Logical, Service, and Physical Resource Specification Viewpoints:</p><ul><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="L2 Logical Scenario" /></ac:link> </li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="S2 Service Structure" /></ac:link></li><li><ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="P2 Resource Structure" /></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><h4>       </h4><h4>New views in Strategic Viewpoint</h4><p>Beginning with this version, the following new views related to the Strategic Viewpoint are introduced:</p><ul><li><strong>Strategic Motivation Table</strong>, which you can find under the UAF Strategy Diagrams category, is designed to simplify the assembly of UAF Strategic requirements, such as Enterprise Goals and Enterprise Objectives, in a tabular format. </li><li><strong>Impact Matrix</strong>, which you can find under the UAF Analysis Diagrams category, illustrates the mapping between the Strategic, Operational, Resource, Service Viewpoint Elements and Strategic Viewpoint Elements using the Impacted By relationship.</li></ul></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="widget" ac:schema-version="1" ac:macro-id="0b19ebb0-c9d5-4fa4-abc5-1f15cb7c26eb"><ac:parameter ac:name="width">600</ac:parameter><ac:parameter ac:name="url"><ri:url ri:value="https://www.youtube.com/watch?v=ngOqW2UVOSI&amp;ab_channel=CATIAMBSE" /></ac:parameter><ac:parameter ac:name="height">400</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Exchange management improvements</h3><p style="text-align: left;">This version adds significant enhancements to working with exchanges, including the ability to control their visibility on diagrams. Improved exchange creation wizards and management dialogs provide greater clarity.</p><h4 style="text-align: left;">Exchange visibility management</h4><p style="text-align: left;">Now, you can easily manage the visibility of realized exchanges in the diagrams. The dedicated button in the smart manipulator toolbar allows you to choose whether you want to show or hide required Exchange Items.</p><p style="text-align: left;"><ac:image ac:align="center"><ri:attachment ri:filename="show_operational_exchanges.png" /></ac:image></p><h6 style="text-align: center;">This is an example of managing the visibility of Operational Exchange Items in an Operational Internal Connectivity diagram.</h6><h4><span>Realized Exchange wizard improvements </span></h4><p><span>Additionally, 2024x brings a more focused approach to reviewing Activity pairs connected with existing Activity Edges in the </span> <strong>Realized Exchange wizards,</strong> <span> improving overall usability and clarity.</span></p><ul><li>In the second step, our focus has shifted solely to reviewing existing Activity Pairs connected by existing Activity Edges. This means that creating new Activity pairs or editing existing ones is no longer possible. As a result, the tool will no longer trigger the automatic generation of new elements or diagrams.</li><li>We've introduced a new step called <strong>Affected Diagrams</strong>. This step lets you see where changes will occur after realizing elements or editing existing exchanges.</li></ul><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="Exchange management changes.png" /></ac:image> </span> <span>An example of changes in the Realized Resource Exchange creation wizard.</span></h6><h4><span>Exchange Manager improvements</span></h4><p>In this release, we've made improvements to the <strong>Exchange Managers</strong>. Now, you'll find a handy <strong>Affected Diagrams</strong> button that opens a dialog listing all the diagrams containing elements that already realize the selected exchange.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="echanges_exchange_manager.png" /></ac:image> </span> <span>An example of changes in the Operational Exchange Manager. </span></h6><h4><span>Producing and Consuming Functions dialog improvements</span></h4><p>We've made some changes in the Producing and Consuming Activities/Functions dialogs as well. They now serve as tools for reviewing Activity pairs and easily removing any unnecessary ones.</p><h6 style="text-align: center;"><span> <ac:image ac:align="center"><ri:attachment ri:filename="changes_producing_consuming_activities.png" /></ac:image>An example of changes in the Producing and Consuming Activities dialog.</span></h6><h3>Library Support</h3><p>New DISR and UJTL library versions are now available:</p><ul><li>UJTL (20230616)</li><li>DISR (<span style="color: rgb(23,43,77);">20230523</span>)</li></ul><p><span style="color: rgb(62,63,64);">You can choose the library version when creating a new project. <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Using libraries" /><ac:plain-text-link-body><![CDATA[Learn more about using libraries >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Templates and Perspectives</h3><h4>New template</h4><ul><li>A new <span style="color: rgb(23,43,77);"> <strong>EA Project Template with Process Guide</strong> is now available in UAF. This Enterprise Architecture (EA) Guide defines a workflow for creating EA views following the Unified Architecture Framework Modeling Language (UAFML). When using this template, you will receive a new UAF project enhanced with the EA Guide for UAF. This modeling guide aids in building architecture by providing nine steps of workflow.</span></li></ul><h4><span style="color: rgb(23,43,77);">Renamed </span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF Enterprise Architecture Project</strong> was renamed to <strong>EA with BPMN Project</strong>. Using the <strong>EA with BPMN Project</strong> template, you will get a simplified Enterprise Architecture project with BPMN, which is based on the UAF framework and designed for enterprise and IT architecture modeling. Creating an EA with the BPMN project will switch the modeling tool to the EA-BPMN Architect graphical user interface and use the EA with the BPMN model template.</span></li><li><span style="color: rgb(23,43,77);">The perspective <strong style="text-align: left;">UAF Enterprise Architect</strong> <span> was renamed </span>to<span> </span> <strong style="text-align: left;">EA-BPMN Architect. </strong> <ac:link><ri:page ri:space-key="UAF12P2024x" ri:content-title="Select Perspective dialog" /><ac:plain-text-link-body><![CDATA[Learn more about the perspectives >>>]]></ac:plain-text-link-body></ac:link> </span></li></ul><h4><span style="color: rgb(23,43,77);">Removed</span></h4><ul><li><span style="color: rgb(23,43,77);">The <strong>UAF EA Project Template with Process Guide</strong> was removed.</span></li></ul><h3>Other Enhancements</h3><ul><li><span style="color: rgb(23,43,77);">The nested ports in all relevant viewpoints are now supported.</span></li><li>The options for <strong>Information Flows</strong> in the <strong>Environment Options</strong> dialog under the <strong>UAF </strong>options group are no longer available.</li><li>The<span> </span> <strong>Tools</strong> <span> </span>option group containing the<span> </span> <strong>Autowire Parts</strong> <span> </span>action is removed from the UAF Parametric Diagram toolbar.</li><li>The <strong>Delegate Port(s)</strong> <span> </span>action is now implemented in the Internal Connectivity Diagrams and is available from the <span style="color: rgb(23,43,77);">diagrams toolbar and context menu of roles, connectors, and ports</span>.</li><li><span style="color: rgb(23,43,77);">You can now create the Vision Statement in the <strong>Specification </strong>window of the Vision element.</span></li><li><span style="color: rgb(23,43,77);">New correctness validation rules regarding the Motivated By relationship are now available. These rules check if the Motivated By relationship is created between correct pairs.</span></li><li><span style="color: rgb(23,43,77);">A new passive validation rule COR2361 is implemented. This rule checks if an Operation Port Class Property type is correct.</span></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="90bd7b1e-43b6-43f5-8025-5097e80fab78"><ac:parameter ac:name="id">244508097</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>SysML Features</h5><h3>Improved Item Flow Creation and Editing</h3><p><span>SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the </span> <strong>Create / Edit Item Flow </strong> <span>dialog, improving overall usability and clarity.</span></p><ul><li><span>Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:</span><ul><li><span>New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams. </span></li><li>The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in <span>a well-organized diagram list in the third step, accurately representing selected options.</span></li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Improved_Item_Flow.png" /></ac:image></p><h6 style="text-align: center;">A comparison of some of the changes in the second step of the <strong>Create / Edit Item Flow</strong> dialog between versions 2024x and 2022x Refresh2.</h6><p><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more about Item Flow creation and editing >>]]></ac:plain-text-link-body></ac:link> </p><h3>Other Improvements</h3><ul><li>The <strong>Tools</strong> option group containing <strong>Autowire Parts</strong> and <strong>Delegate Port(s)</strong> commands has been removed from the SysML Parametric Diagram toolbar. Both <strong>Delegate Port(s)</strong> and <strong>Autowire Parts</strong> commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.</li><li>Improved <strong>Delegate Port(s)</strong> command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. <ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Automatic delegation" /><ac:plain-text-link-body><![CDATA[Learn more about automatic delegation >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d2134088-4966-4566-9a72-e0d0d9dd9d47"><ac:parameter ac:name="id">256630726</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Discontinued Features</h5><p>The following features have been discontinued with the 2024x version release.</p><h3>JavaScript Nashorn Scripting</h3><p><span style="color: rgb(62,63,64);">The JavaScript<span> </span> </span>Nashorn <span style="color: rgb(62,63,64);">language usage has been removed from the modeling tool. Please use JavaScript<span> </span> <em>Rhino</em> instead<em>. </em>This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Deprecated JavaScript Nashorn" /><ac:plain-text-link-body><![CDATA[Learn more about the deprecated JavaScript Nashorn >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Record Macro Functionality </h3><p>The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.</p><h3>SPEM Plugin</h3><p>The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.</p><h5>Known Migration Issues</h5><p>Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.</p><p>To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the &lt;modeling_tool_install_dir&gt;\bin\&lt;modeling_tool&gt;.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="eb46d24f-3281-4de3-b6b2-1ecb89f93d0c"><ac:parameter ac:name="id">272319258</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Modeling and Infrastructure</h5><h3>DSLS Licensing</h3><p>Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:</p><ul><li>License usage statistics, debugging, and simple UI to administer and view statistics.</li><li>Licenses are bound to their expiration date rather than the product version.</li><li>Nodelock (seat), floating, and managed licensing options.</li></ul><p>Thus, now you can choose to use either FlexNet or DSLS for product licensing. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f49ff8d-45a1-456c-a2a0-a919be8c1f02"><ac:rich-text-body><p>The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version <span>R2024x with modeling tool version 2024x</span>).</p></ac:rich-text-body></ac:structured-macro><p><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS Licensing >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9484f639-acef-4728-8acc-d1e2338719d2"><ac:parameter ac:name="">Zoom in Model Browser</ac:parameter></ac:structured-macro>Zoom in Model Browser</h3><p>From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking. </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Zoom in Model Browser.png" /></ac:image></p><h6 style="text-align: center;">Zooming in the Model Browser using keyboard shortcuts.</h6><p><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /><ac:plain-text-link-body><![CDATA[Learn more about zooming in the Model Browser>>]]></ac:plain-text-link-body></ac:link></p><h3>Advanced Legend Adornments in Tables</h3><p>In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Advanced Legend Adornments in Tables Example.png" /></ac:image></p><h6 style="text-align: center;">Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item <em>In Progress</em>.</h6><p style="text-align: right;"><br /></p><h3 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="6c8c8907-e1fd-4c63-9547-aff205bb1046"><ac:parameter ac:name="">MIother</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li><strong>OpenJDK version update. </strong>Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version. </li><li><strong> <span style="color: rgb(62,63,64);">Supported operating system changes for Linux. </span> </strong> <span style="color: rgb(62,63,64);">CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support. </span></li><li><strong>JavaScript Rhino version update.</strong> The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</li><li>It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.</li></ul><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="f7e102f2-3db2-4461-a12e-4ff53e738c59"><ac:parameter ac:name="id">243174490</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h5><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="82578d71-581b-42b4-bfdc-d5dcd49ff7cd"><ac:parameter ac:name="">TWC</ac:parameter></ac:structured-macro> </span>Teamwork Cloud</h3><h4 style="text-align: left;">New File Exchange Format for Server Projects</h4><p>In version 2022x Refresh2, we introduced <strong>.szip</strong> – a new <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using server project file format" /><ac:plain-text-link-body><![CDATA[server project exchange format]]></ac:plain-text-link-body></ac:link>. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.</p><p>In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.</p><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="600"><ri:attachment ri:filename="project_exchange_options.png" /></ac:image></h6><p style="margin-left: 0.0in;"><span style="color: rgb(0,0,0);">The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.</span></p><p style="margin-left: 0.0in;"><br /></p><p style="margin-left: 0.0in;text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image><ri:attachment ri:filename="szip_project_import_performance.png" /></ac:image> <ac:image><ri:attachment ri:filename="szip_project_export_performance.png" /></ac:image> </span></p><h6 style="text-align: center;">Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).</h6><p><br /></p><h4>Model Patch Mechanism (Technology Preview)</h4><p><span style="color: rgb(0,0,0);">We introduce the technology preview of the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Patch - Technology preview" /><ac:plain-text-link-body><![CDATA[Model Patch mechanism]]></ac:plain-text-link-body></ac:link>, a more lightweight way to move model changes. Model Patch can help you:</span></p><ul><li><span style="color: rgb(0,0,0);">Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;</span></li><li><span style="color: rgb(0,0,0);">Transfer only a specific scope of model changes between disconnected teams instead of the entire model;</span></li><li>Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.</li></ul><p><br /></p><h6 style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="model_patch_mechanism.jpg" /></ac:image></h6><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfdd0694-20ca-468f-858e-b8118a0d2206"><ac:parameter ac:name="">Power</ac:parameter></ac:structured-macro> </span>Power’By</h3><h4>New Features to Manage Used Projects</h4><p><span style="color: rgb(0,0,0);">We added new features that provide you with better capabilities to manage used projects in <strong>3D</strong>EXPERIENCE:</span></p><ul><li><span style="color: rgb(0,0,0);">Export packages as a new server project;</span></li><li><span style="color: rgb(0,0,0);">Move elements to/from used projects;</span></li><li><span style="color: rgb(0,0,0);">Import used projects.</span></li></ul><h4><span style="color: rgb(0,0,0);">Opening Projects in Read-Only Mode</span></h4><p><span style="color: rgb(0,0,0);">Beginning with version 2024x, you can open <strong>3D</strong>EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.</span></p><p style="text-align: center;"><ac:image ac:height="96"><ri:attachment ri:filename="3DEXPERIENCE_project_editing_disabled.jpg" /></ac:image></p><h6 style="text-align: center;">Notification informing the user that the <strong>3D</strong>EXPERIENCE project is read-only.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to Top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="da45258d-6386-4b80-af5a-54f24ceca0df"><ac:parameter ac:name="id">430554266</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><strong> <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link> </strong></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=187334782 space=CEA2024xR2 version=7 -->
## PAGE 00005: Cameo Enterprise Architecture Documentation

- page_id: `187334782`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/187334782/Cameo+Enterprise+Architecture+Documentation
- version_number: 7
- version_date: `2025-05-30T07:30:37.002+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

**Docs of other versions**

- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2024xR1']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2024x']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2022xR2']
- 
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2022x']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2021xR2']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2021xR1']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA2021x']
- [CONFLUENCE_PAGE title='Cameo Enterprise Architecture Documentation' space='CEA190SP4']

This is the home page of Cameo Enterprise Architecture documentation.

Cameo Enterprise Architecture is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to **enterprise architecture** needs.

The documentation of Cameo Enterprise Architecture is a package that includes the documentation of these products and plugins:

**[CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024xR2']**

Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.

Type a search phrase...

**[CONFLUENCE_PAGE title='UPDM 2 Plugin Documentation' space='UPDM2P2024xR2']**

Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='UAF 1.2 Plugin Documentation' space='UAF12P2024xR2']**

Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.

Type a search phrase...

**[CONFLUENCE_PAGE title='SysML Plugin Documentation' space='SYSMLP2024xR2']**

Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.

Type a search phrase...

**[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024xR2']**

Guides you through the import, export, and management of SysML requirements.

Type a search phrase...

**[CONFLUENCE_PAGE title='Concept Modeler Documentation' space='CCMP2024xR2']**

Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain.

Type a search phrase...

##### Additional plugin

**[CONFLUENCE_PAGE title='Cameo Simulation Toolkit Documentation' space='CST2024xR2']**

Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.

Type a search phrase...

##### Additional information

**[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024xR2']**

Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation.

Type a search phrase...

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Docs of other versions</strong></p><ul><li><ac:link><ri:page ri:space-key="CEA2024xR1" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2024x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2024x" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2024x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2022xR2" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2022x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2022x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2022x" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2022x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2021xR2" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2021x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2021xR1" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2021x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA2021x" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 2021x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="CEA190SP4" ri:content-title="Cameo Enterprise Architecture Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Enterprise Architecture 19.0 SP4]]></ac:plain-text-link-body></ac:link></li></ul><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span>This is the home page of Cameo Enterprise Architecture documentation.</span></p><p>Cameo Enterprise Architecture is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to <strong>enterprise architecture</strong> needs.</p><p>The documentation of Cameo Enterprise Architecture is a package that includes the documentation of these products and plugins:</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"><ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="MagicDraw Documentation" /></ac:link></strong></p><p>Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="089042d3-3846-48b0-a4c8-84c5200800dc"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MD2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="UPDM2P2024xR2" ri:content-title="UPDM 2 Plugin Documentation" /></ac:link></strong></p><p>Provides descriptions of UPDM 2 diagrams and elements, plus introduces UPDM 2 specific features as well as gives guidelines for building enterprises.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="9be80c7d-2a62-4a9a-a5b0-36f765ca27f8"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UPDM2P2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="UAF12P2024xR2" ri:content-title="UAF 1.2 Plugin Documentation" /></ac:link></strong></p><p>Provides descriptions of UAF diagrams and elements, plus introduces UAF specific features as well as gives guidelines for building enterprises.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="2c36a58c-caea-4e2a-b8c2-475f4809c913"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="UAF12P2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="SYSMLP2024xR2" ri:content-title="SysML Plugin Documentation" /></ac:link></strong></p><p>Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="ec3bdbb7-2e15-4fea-9da6-404b06e9863d"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="SYSMLP2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="CRMP2024xR2" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /></ac:link></strong></p><p>Guides you through the import, export, and management of SysML requirements.</p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="dc7900b6-4d82-4476-9f6f-6359bb6f90e6"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CRMP2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="CCMP2024xR2" ri:content-title="Concept Modeler Documentation" /><ac:plain-text-link-body><![CDATA[Cameo Concept Modeler Documentation]]></ac:plain-text-link-body></ac:link></strong></p><p><span style="color:var(--ds-text,#333333);">Provides instructions about how to model real-world concepts, import/export a model from/to an OWL ontology, and generate glossaries in plain English for clearer and more informative source of knowledge for any domain. </span></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="0ea811e0-01b5-4ca1-bd0a-6240488d5788"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CCMP2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><h3>Additional plugin</h3></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="CST2024xR2" ri:content-title="Cameo Simulation Toolkit Documentation" /></ac:link></strong></p><p>Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.</p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="61c2d572-2cd0-492e-bcd1-b199634dee75"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CST2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><h3>Additional information</h3></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p><strong><ac:link><ri:page ri:space-key="IL2024xR2" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installation and licensing]]></ac:plain-text-link-body></ac:link></strong></p><p>Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation. </p><p><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="8839bce4-5422-4d98-b0ce-c47d17497649"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="IL2024xR2" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=187334781 space=CEA2024xR2 version=2 -->
## PAGE 00006: Legal Notices

- page_id: `187334781`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/187334781/Legal+Notices
- version_number: 2
- version_date: `2024-10-08T09:02:27.379+02:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

true[CONFLUENCE_PAGE title='Legal Notices' space='MD2024xR2']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="b4c9a95e-f983-4dcb-8211-306757af9e20"><ac:parameter ac:name="nopanel">true</ac:parameter><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Legal Notices" /></ac:link></ac:parameter></ac:structured-macro></p><p><br /></p>
````

<!--NOMAGIC_PAGE id=187334849 space=CEA2024xR2 version=2 -->
## PAGE 00007: Support

- page_id: `187334849`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/187334849/Support
- version_number: 2
- version_date: `2024-10-04T14:29:18.402+02:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Support' space='NMDOC']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="eeb7bfc0-8e9d-44c3-855a-0f28b2d7c20d"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Support" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=187334847 space=CEA2024xR2 version=1 -->
## PAGE 00008: Using UAF and UPDM2 plugins in Cameo Enterprise Architecture

- page_id: `187334847`
- space_key: `CEA2024xR2`
- source_url: https://docs.nomagic.com/spaces/CEA2024xR2/pages/187334847/Using+UAF+and+UPDM2+plugins+in+Cameo+Enterprise+Architecture
- version_number: 1
- version_date: `2024-05-09T10:05:03.068+02:00`
- ancestors: Cameo Enterprise Architecture Documentation
- labels: []

### NORMALIZED CONTENT

**On this page**

##### Choosing the default plugin

Before the first startup of the Cameo Enterprise Architecture, you can set which plugin - UAF or UPDM2 - will be installed by default. If no changes are made, by default UAF plugin is installed.

To change the default plugin before the first startup

1. Go to the <cea_install_dir>\bin\ and open for editing the cameoea.properties file.
2. In the file, find the system property -Dstart.application.with.updm2.or.uaf.plugin=uaf
3. Change the uaf value to updm2 .
4. Save the file and start the Cameo Enterprise Architecture modeling tool.

In case you will decide to change the plugin later, see chapter [CONFLUENCE_PAGE title='Changing between UAF and UPDM 2 plugins' space='UAF12P2024xR1'] for information about how to do that.

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>On this page</strong></p><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="45e56338-1c7d-4c50-a104-06124d9eae17" /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Choosing the default plugin</h3><p>Before the first startup of the Cameo Enterprise Architecture, you can set which plugin - UAF or UPDM2 - will be installed by default. If no changes are made, by default UAF plugin is installed.</p><p><br /></p><p>To change the default plugin before the first startup</p><hr /><ol><li>Go to the &lt;cea_install_dir&gt;\bin\ and open for editing the <em>cameoea.properties</em> file.</li><li>In the file, find the system property <em>-Dstart.application.with.updm2.or.uaf.plugin=uaf</em></li><li>Change the <em>uaf</em> value to <em>updm2</em>.</li><li>Save the file and start the Cameo Enterprise Architecture modeling tool.</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="c93f7330-b046-4e85-be90-7075c3f9d206"><ac:rich-text-body><p>In case you will decide to change the plugin later, see chapter <ac:link><ri:page ri:space-key="UAF12P2024xR1" ri:content-title="Changing between UAF and UPDM 2 plugins" /></ac:link> for information about how to do that.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Displaying which plugin is installed</h3><p>You can choose to display the plugin name in brackets next to the Cameo Enterprise Architecture title in the modeling tool's title bar. </p><p><br /></p><p>To display the installed plugin name near the modeling tool title</p><hr /><ol><li>Go to the &lt;cea_install_dir&gt;\bin\ and open for editing the <em>cameoea.properties</em> file.</li><li>In the file, find the system property <em>-Dadd.plugin.name.to.application.title\=false</em></li><li>Change the <em>property </em>value to <em>true</em>.</li><li>Save the file and start the Cameo Enterprise Architecture modeling tool.</li></ol><p><ac:image><ri:attachment ri:filename="plugin_name_in_title.png"><ri:page ri:content-title="Using UAF and UPDM2 plugins in Cameo Enterprise Architecture" ri:space-key="CEA2024xR2" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````
