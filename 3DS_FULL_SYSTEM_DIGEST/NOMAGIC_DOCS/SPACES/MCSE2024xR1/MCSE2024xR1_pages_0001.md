# NOMAGIC DOCUMENTATION SPACE: Magic Cyber Systems Engineer 2024x Refresh1

<!--NOMAGIC_SPACE key=MCSE2024xR1 chunk=1 -->

<!--NOMAGIC_PAGE id=170487713 space=MCSE2024xR1 version=1 -->
## PAGE 00001: 2024x News for Developers

- page_id: `170487713`
- space_key: `MCSE2024xR1`
- source_url: https://docs.nomagic.com/spaces/MCSE2024xR1/pages/170487713/2024x+News+for+Developers
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

<!--NOMAGIC_PAGE id=178159884 space=MCSE2024xR1 version=5 -->
## PAGE 00002: 2024x Refresh1 Version News

- page_id: `178159884`
- space_key: `MCSE2024xR1`
- source_url: https://docs.nomagic.com/spaces/MCSE2024xR1/pages/178159884/2024x+Refresh1+Version+News
- version_number: 5
- version_date: `2024-12-16T14:57:14.474+01:00`
- ancestors: Magic Cyber Systems Engineer Documentation
- labels: []

### NORMALIZED CONTENT

top

### Magic Cyber Systems Engineer

Released on: July 5, 2024

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

****

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

### SysML Features

##### Affected Diagrams Preview Dialog

To enhance the Item Flow creation and management experience, we have introduced the**Preview Affected Diagrams**dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements are prominently marked in the diagram preview pane conveying where the created Item Flows will be realized.

During the preview process, you can select the **Update Diagram** check box for diagrams in which you wish to display the Conveyed Items of the selected flows.

The new[CONFLUENCE_PAGE title='Setting project options' space='SYSMLP2024xR1']**Show Item Flows on Affected Diagrams**controls how the diagrams will be updated for newly created or modified flows. Set the option to *true*to update all affected diagrams and show the Conveyed Items of flows whenever a new flow is created or an existing one is modified.

[CONFLUENCE_PAGE title='Preview Affected Diagrams dialog' space='SYSMLP2024xR1']>]]>

[IMAGE alt='' src='']

##### Item Flows Management

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

[CONFLUENCE_PAGE title='2024x Refresh1 Version News' space='CATIA']>]]>

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7dc7bee2-3797-466f-982b-5a1e0d78e7c5"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><h1 style="text-align: center;">Magic Cyber Systems Engineer</h1><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: July 5, 2024</span></p><p><br /></p><p><span style="letter-spacing: 0.0px;">SysML features introduce several improvements to Item Flow management. You can now navigate from a selected Item Flow in the Containment tree to the diagrams where it is realized, specify Conveyed Items from the Diagram Palette, and hide arrow notations on realizing elements when the Conveyed Item is hidden or unspecified. Conveyed Items are now represented with icons in the 'Create / Edit Item Flow' dialog. Item Flow creation between Activity Parameter Nodes and Actions has been enhanced. Two new validation rules highlight Item Flows without Conveyed Items. The 'Preview Affected Diagrams' dialog further enhances the Item Flow management experience by presenting all affected diagrams.</span></p><p><span style="letter-spacing: 0.0px;">Furthermore, the 2024x Refresh1 release contains <span style="color: rgb(14,16,26);">new validation solvers for the 'Invalid Connector' validation rule, allowing for an easy connector redefinition. T</span></span><span style="letter-spacing: 0.0px;color: rgb(14,16,26);">he new release also introduces the MagicGrid perspective. </span></p><p><span>Simulation features introduce several significant enhancements. One of the key updates is the ability to</span><span> </span><span>animate behavioral diagrams during server-side simulation </span><span>by embedding them</span><span> </span><span>into HTML-generated user interfaces</span><span>. The latest product version also supports model data export to the SSP file format, </span><span style="color: rgb(33,37,41);"><span style="color: rgb(13,13,13);">allowing you transfer models between different simulation tools, such as Dymola</span></span><span>. Furthermore, you can now load and play external simulation results from CSV files using the Results Player. </span><span style="letter-spacing: 0.0px;">Additionally, a new project option allows you to display runtime values on Port labels during simulation, providing immediate insights into model behavior. The new release also supports Matlab integration for Apple Silicon, </span><span style="letter-spacing: 0.0px;">allows enabling and disabling simulation annotations in diagrams, offers improvements to the ALH.callOperation method and built-in math functions, and more.</span></p><p><span style="letter-spacing: 0.0px;">Client-side performance enhancements include optimized efficiency for exporting matrices and tables in SVG format. For general modeling, this release improves Information Flow management. You can now easily navigate from a selected Information Flow in the Containment tree to the diagrams where it is realized and specify Conveyed Information directly in the diagram. You can choose to hide arrow notations on realizing elements when the Conveyed Information is hidden or unspecified. Conveyed Information is now represented with icons in the 'New Conveyed Information' dialog. New validation rules highlight Information Flows that do not have any Conveyed Information.</span></p><p><span style="letter-spacing: 0.0px;">Additional enhancements include the improved samples access and navigation in the modeling tool. Also, a new 'Letter Spacing Reduction in SVG' environment option is introduced to control the spacing between letters when exporting diagram images in SVG format.</span></p><p>Additionally, collaborative modeling brings several enhancements to<span> the Model Patch functionality, which is now out of the technology preview phase. The Model Patch UI has been improved with a new panel that identifies and explains issues related to model patch application. Project commit processes are now more efficient with a First-In-First-Out (FIFO) queue system for simultaneous commits. Finally, you can save time by skipping the migration of archived branches when migrating Teamwork Cloud projects and more.</span></p><p><span>Collaboration powered by the 3DEXPERIENCE platform introduces significant improvements as well. You can now move Teamwork Cloud projects to the 3DEXPERIENCE platform and then update these projects using the .szip file format. In addition, the History and Edit Branches dialogs now indicate if and from which iteration a project was merged.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[product documentation]]></ac:plain-text-link-body></ac:link>.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="569e25e5-7042-4e37-bc33-e76dbcdf057e"><ac:parameter ac:name="title">2024x Refresh1 Hot Fix 1 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Refresh1 Hot Fix 1 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Refresh1 Hot Fix 1 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong><ac:link ac:anchor="SysML Features" /></strong></p><ul><li><ac:link ac:anchor="Affected Diagrams Preview Dialog" /></li><li><ac:link ac:anchor="Item Flows Management" /></li><li><ac:link ac:anchor="Connector Redefinition" /></li><li><ac:link ac:anchor="MagicGrid Perspective" /></li></ul><p> <strong><ac:link ac:anchor="Simulation Features" /></strong></p><ul><li><ac:link ac:anchor="What's New in Server-Side Simulation" /><ul><li><ac:link ac:anchor="Diagram Animation Support" /></li><li><ac:link ac:anchor="Other" /></li></ul></li><li><p><ac:link ac:anchor="SSP Export Support" /></p></li><li><p><ac:link ac:anchor="Results Player" /></p></li><li><p><ac:link ac:anchor="Displaying Runtime Values on Port Labels" /></p></li><li><p><ac:link ac:anchor="Easier Access to Nested Properties" /></p></li><li><p><ac:link ac:anchor="Other Improvements" /></p></li></ul></ac:layout-cell><ac:layout-cell><p> <strong><ac:link ac:anchor="Client side performance improvements"><ac:plain-text-link-body><![CDATA[Client-side Performance Improvements]]></ac:plain-text-link-body></ac:link></strong></p><ul><li><ac:link ac:anchor="Improvements in Diagram Export as SVG" /></li></ul><p><strong><ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link></strong></p><ul><li><ac:link ac:anchor="Information Flow Management Improvements" /></li><li><ac:link ac:anchor="Improved Samples Access and Navigation" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul></ac:layout-cell><ac:layout-cell><p> <strong><ac:link ac:anchor="Collaboration" /></strong></p><ul><li><ac:link ac:anchor="Model Patch Functionality Improvements" /></li><li><ac:link ac:anchor="Commit Queues" /></li><li><ac:link ac:anchor="Other" /></li></ul><p><strong><ac:link ac:anchor="Collaboration Powered by 3DEXPERIENCE Platform" /></strong></p><ul><li><ac:link ac:anchor="Moving Projects to the 3DEXPERIENCE Platform" /></li><li><ac:link ac:anchor="Iteration Merge Information" /></li><li><ac:link ac:anchor="Performance Improvements" /></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>SysML Features</h1><h3>Affected Diagrams Preview Dialog</h3><p><span>To enhance the Item Flow creation and management experience, we have introduced the </span><strong>Preview Affected Diagrams</strong><span> dialog. This dialog conveniently presents all affected diagrams, allowing you to preview them individually. Furthermore, the affected elements are prominently marked in the diagram preview pane conveying where the created Item Flows will be realized.</span></p><p>During the preview process, you can select the <strong>Update Diagram</strong> check box for diagrams in which you wish to display the Conveyed Items of the selected flows.</p><p><span style="color: rgb(23,43,77);">The new<span> </span></span><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link><strong><span> </span>Show Item Flows on Affected Diagrams</strong><span style="color: rgb(23,43,77);"><span> </span>controls how the diagrams will be updated for newly created or modified flows. Set the option to <em>true </em>to update all affected diagrams and show the Conveyed Items of flows whenever a new flow is created or an existing one is modified. </span></p><p><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Preview Affected Diagrams dialog" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p><span><ac:image ac:align="center" ac:alt="preview_affected_diagrams_dialog.png"><ri:url ri:value="https://docs.nomagic.com/download/attachments/146407510/preview_affected_diagrams_dialog.png?version=1&amp;modificationDate=1710870010652&amp;api=v2" /></ac:image></span></p><h3>Item Flows Management</h3><ul><li><span style="color: rgb(23,43,77);">Interactions can be modeled across various diagrams in both behavior and structure models, creating difficulties in locating diagrams representing Item Flow realizations and hindering transparency in their identification. Now you can easily navigate from the selected Item Flow in the Containment tree to the diagrams where the Item Flow is realized. <ac:link ac:anchor="Navigating to diagrams where Item Flow is realized"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image ac:align="center"><ri:attachment ri:filename="Navigate_to_diagram_SYSML.png" /></ac:image><br /></span></li><li><span>Specify the Conveyed Item directly in the diagram, picking the needed Conveyed Item element from the diagram palette and dragging it on to the Item Flow. </span><ac:link ac:anchor="Specifying the Conveyed Item directly on the diagram pane"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Specifying Conveyed Item via Diagram Palette.png" /></ac:image><br /></span></li><li><span style="color: rgb(23,43,77);">You can now choose whether you want to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements when the Conveyed Item is hidden or unspecified in case you would need to conceal such approximate interactions, and vice versa</span>. The <span><strong>Hide Information Flow If Conveyed Information Is Missing</strong> <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link> controls the arrow visibility. <ac:link ac:anchor="Showing/hiding the Conveyed Item"><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image ac:align="center"><ri:attachment ri:filename="hide_information_flow.png" /></ac:image><br /></span></li><li><span>Now the Conveyed Items in the </span><strong>Create / Edit Item Flow</strong><span> dialog are represented with icons to help you identify the Conveyed Items.</span><span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Conveyed Item Element Icon.png" /></ac:image><br /></span></li><li><span>Item Flow creation between Activity Parameter Nodes and Actions has been enhanced to facilitate the creation of Item Flows when interactions are modeled between Part Properties. Typically, the 'Usage' allocation mode is used for this, which does not create an allocation relation on the end of the Activity Parameter Node, thereby not providing a possible sender or receiver on this end. Now, the tool checks action allocations to typed parts for Activity Parameter Nodes. Consequently, the Direction field in the <strong>Create / Edit Item Flow</strong> dialog displays suggested sender and receiver elements based on the element typing the parts to which actions are allocated.</span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Item Flow between Activity Parameter Node and Action.png" /></ac:image><h6 style="text-align: center;">On the end of the<em> input : Audio data </em>Activity Parameter Node there are no Actions, only the<em> Read and transmit the sound </em>Activity. Thus, the tool checks the model to find Actions that invoke this Activity, locating the<em> : Read and transmit the sound</em> Action in the <em>Listen the audio</em> Activity diagram. <br />Then the tool checks the allocation relationships for this action and an allocation to the <em>: Wireless Earbuds</em> Part Property is found. <br />Using this information the <strong>Create/Edit Item Flow</strong> dialog identifies the <em>Wireless Earbuds</em> Block as a possible sender of the flow, displaying<em> Wireless Earbuds </em>and <em>Processing </em>Blocks as a suggestion for the sender/receiver in the <strong>Direction </strong>field of the dialog.<br /><br /></h6></li><li><span>New validation rules (</span><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Item Flow has no Conveyed Items" /><ac:plain-text-link-body><![CDATA[IFHNCI[2]]]></ac:plain-text-link-body></ac:link><span><span class="error"> and <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Realized Item Flow has no Conveyed Items" /><ac:plain-text-link-body><![CDATA[RIFHNCI[2]]]></ac:plain-text-link-body></ac:link></span></span><span>) have been implemented to highlight Item Flows that do not have any Conveyed Items. This helps to declutter the model and identify potentially unused flows. Learn more on the <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Item Flow has no Conveyed Items" /></ac:link> and <ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Realized Item Flow has no Conveyed Items" /></ac:link> pages.</span></li></ul><h3>Connector Redefinition</h3><p><span style="color: rgb(14,16,26);">New validation solvers are available for the <strong>Invalid Connector</strong> validation rule, allowing for an easy connector redefinition:</span></p><ul><li style="list-style-type: disc;"><span style="color: rgb(14,16,26);">Use the <strong>Redefine and Replace Connector</strong> solver to have a new redefining connector created if the selected connector is inherited and at least one of its ends is redefined.</span></li><li style="list-style-type: disc;"><span style="color: rgb(14,16,26);">Use the <strong>Replace with Redefining</strong> solver to replace the failed connector with the redefining one if the failed connector is already redefined in the same context.</span></li></ul><p><span style="color: rgb(14,16,26);"><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Invalid Connector (UML Correctness)" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="image-2024-4-12_8-33-47.png" /></ac:image></p><h6 style="text-align: center;">The image displays how to resolve the <span style="color: rgb(14,16,26);"><strong>Invalid Connector </strong>validation error via the <strong>Redefine and Replace Connector </strong>solver.<strong> </strong></span></h6><h3>MagicGrid Perspective</h3><p>The MagicGrid perspective has been introduced, supplementing existing perspectives, such as Full Featured or System Engineer. This perspective simplifies the modeling tool by providing only the MagicGrid-required subset of SysML elements and diagrams, making it easier to understand and navigate for users new to MagicGrid. You can manually switch perspectives via the <strong>Select Perspective</strong> dialog. Furthermore, a dialog prompting you to switch to this perspective appears whenever you create a MagicGrid project.</p><p><ac:link><ri:page ri:space-key="SYSMLP2024xR1" ri:content-title="Selecting perspective" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="MagicGrid_perspective.png" /></ac:image>The MagicGrid perspective available via the <strong>Select Perspective</strong> dialog.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Simulation Features</h1><h3>What's New in Server-Side Simulation</h3><h4 style="margin-left: 40.0px;">Diagram Animation Support</h4><p style="margin-left: 40.0px;"><span style="color: rgb(23,43,77);">The new release supports diagram animation when executing projects on the server. Now behavioral (Activity, State Machine, and Sequence) diagrams can be embedded into HTML-generated user interfaces and are animated during server-side simulation. </span><span><ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Simulation with UI" /><ac:plain-text-link-body><![CDATA[Learn more about simulation with UI >>]]></ac:plain-text-link-body></ac:link></span></p><p style="margin-left: 40.0px;"><br /></p><p style="margin-left: 40.0px;text-align: center;"><ac:image><ri:attachment ri:filename="diagram_animation_support.png" /></ac:image></p><h6 style="text-align: center;margin-left: 40.0px;">Diagram animation support in server-side simulation.</h6><h4 style="margin-left: 40.0px;"><br />Other</h4><ul><li style="list-style-type: none;"><ul><li><p><span style="color: rgb(23,43,77);">Now UI titles are displayed in a UI index window and you can use them to open a specific UI in a separate window.</span></p></li><li><span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">Upon successful installation, the Simulation application card is displayed on the Web Application Platform <span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);">welcome page</span></span>.<span> </span></span>Opening the application will redirect you to the Server-side Simulation Swagger page.</span></li><li><span style="color: rgb(23,43,77);">The RUN endpoint has a new 'timeout' query parameter which allows you to specify the timeout duration in minutes.</span></li><li><span style="color: rgb(23,43,77);">The 'sync' query parameter has been added to the RUN, STEP, and TERMINATE endpoints. You can use them to initiate a synchronous API call in server-side simulation using Jupyter Notebook.</span></li></ul></li></ul><p style="margin-left: 40.0px;"><br /></p><h3>SSP Export Support</h3><p><span style="color: rgb(33,37,41);"><span style="color: rgb(13,13,13);">This release introduces a powerful new feature - the ability to export model data to the SSP (System Structure and Parameterization) file format. </span>SSP is a tool-independent standard used to define complete systems consisting of one or more FMUs (Functional Mockup Interfaces). <span style="color: rgb(13,13,13);">With this enhancement, you can transfer models between different simulation tools, such as Dymola, facilitating greater interoperability and collaboration. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="SSP Export - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></span></p><p><br /></p><h3>Results Player</h3><p><span style="color: rgb(13,13,13);">Now, the tool can read and play external simulation results from CSV files. You can load CSV files generated either locally or by external tools into the Results Player and then play back the simulation results in your modeling tool. The Results Player offers enhanced playback controls, allowing users to pause playback, navigate through different simulation times using a slider, and adjust playback speed according to their preferences. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Results Player - Technology Preview" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="results_player.png" /></ac:image></p><h6 style="text-align: center;">Using the Results Player to play back simulation results from an imported CSV file.</h6><h3><br />Displaying Runtime Values on Port Labels</h3><p>A new<strong> </strong><span style="color: rgb(23,43,77);"><strong>Show Runtime Values on Port Labels</strong> </span>project option and Simulation Configuration property allows you to see runtime values on Port labels during simulation as displayed below. <ac:link><ri:page ri:space-key="CST2024xR1" ri:content-title="Manipulating simulation information" /><ac:plain-text-link-body><![CDATA[Learn more about manipulating simulation information >>]]></ac:plain-text-link-body></ac:link></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="showing_runtime_values_on_port_labels.png" /></ac:image></p><h6 style="text-align: center;">Displaying runtime values on Port labels during simulation.</h6><h3><br />Easier Access to Nested Properties</h3><p>You no longer need complex <span style="color: rgb(23,43,77);">ALH (Action Language Helper) scripts to access deeply nested properties. With the Groovy language, you can use &quot;dot notation&quot; directly in any expression.</span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="dot_notation_in_groovy.png" /></ac:image><br /></span></p><h6 style="text-align: center;">Using &quot;dot notation&quot; in the Groovy language.</h6><h3><br />Other Improvements</h3><ul><li><span style="color: rgb(23,43,77);">The new <strong>Show Annotations</strong> project option and Simulation Configuration property allows enabling and disabling simulation annotations in diagrams. Simulation annotations include flowing information, possibility to change animation speed, and annotation tooltips. <ac:link ac:anchor="Enabling and disabling animation options"><ri:page ri:space-key="CST2024xR1" ri:content-title="Displaying simulation information" /><ac:plain-text-link-body><![CDATA[Learn more about animation options >>]]></ac:plain-text-link-body></ac:link></span></li><li><span style="color: rgb(23,43,77);">Matlab integration is now supported for Apple Silicone.</span></li><li><span style="color: rgb(23,43,77);">The ALH.callOperation method has been enhanced and now supports calling operations through ports.</span></li><li>This release introduces several new methods of the built-in math functions.</li><li>Now you can specify the simulation license for SIMULIA when logging in to the <strong>3D</strong>EXPERIENCE platform.</li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="815c4f41-7b9a-4abd-a370-16ecd19fe713"><ac:parameter ac:name="">Client side performance improvements</ac:parameter></ac:structured-macro>Client-side Performance Improvements</h1><h3>Improvements in Diagram Export as SVG</h3><p>Exporting diagrams in Scalable Vector Graphics (*.svg) format now features significant optimizations, with the most notable improvements in matrix and table exports:</p><ul><li>Reduction in the file size of exported SVG files.</li><li>Export now requires up to 10 times less RAM resources.</li><li>Decreased duration of the export process.</li></ul><p>These optimizations enhance the efficiency of exporting matrices and tables in SVG format, resulting in significantly reduced file sizes. The improvements impact various functionalities that utilize SVG image generation, such as image export via the MDZipX plugin or the 'Save as Image' command.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="File Size of Dependency Matrix Exported as SVG.png" /></ac:image></p><h6 style="text-align: center;">A chart comparing the file size of a Dependency Matrix exported as a SVG image in 2024x and 2024x Refresh1.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h1><h3>Information Flow Management Improvements</h3><ul><li>Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Element usage in diagrams" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="Navigate_to_diagram_UML.png" /></ac:image></li><li>Specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><span><br /><ac:image><ri:attachment ri:filename="Specifying Conveyed Information via Diagram Palette.png" /></ac:image><br /></span></li><li>You can no<span style="color: rgb(23,43,77);">w choose whether you want to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified</span>. The <span><strong>Hide Information Flow If Conveyed Information Is Missing</strong> <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link> controls the arrow visibility. <ac:link ac:anchor="Changing the arrow notation visibility"><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="hide_information_flow_UML.png" /></ac:image><br /></span></li><li>Now the Conveyed Information in the New Conveyed Information <span>dialog is represented with icons to help you identify the Conveyed Information. </span><span><br /><ac:image><ri:attachment ri:filename="Conveyed Information Element Icon.png" /></ac:image><br /></span></li><li>New validation rules (<ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[IFHNCI[1]]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[RIFHNCI[1]]]></ac:plain-text-link-body></ac:link>)<span> have been implemented to highlight Information Flows that do not have any Conveyed Information. Learn more on the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /></ac:link> pages.</span></li></ul><h3 style="text-align: left;">Improved Samples Access and Navigation</h3><p><span>From now on, you can review the list of available samples</span><span> anytime by invoking the </span><span>Samples tab. The tab displays all the samples </span><span>provided with the modeling tool installation, providing a convenient way to review and access the needed samples. </span><span>Additionally, you can use the search bar to navigate the available content efficiently both in the Samples and Welcome tabs.</span></p><p><span><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Editor Tabs" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Improved Samples Access and Navigation.png" /></ac:image></p><h3>Other Improvements</h3><ul><li><span>A new </span><strong><span>Letter Spacing Reduction in SVG</span></strong><span> environment option is introduced to control the spacing between letters when exporting diagram images in SVG format</span>. Adjusting letter spacing enables you to maintain text alignment within shape boundaries when exporting, ensuring it does not exceed their borders. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Diagram image export" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h1><h3>Model Patch Functionality Improvements</h3><p><span style="color: rgb(0,0,0);">We are happy to announce that in this release the Model Patch functionality is coming out of the technology preview phase with several enhancements. </span><span style="color: rgb(0,0,0);">M</span><span style="color: rgb(0,0,0);">odel Patch is a more convenient alternative to a </span>full Model merge or disconnected team collaboration because it <span style="color: rgb(0,0,0);">allows you to move the selected elements or element changes from one model branch to another and transfer only a specific scope of model modifications.</span></p><p><span style="color: rgb(0,0,0);">In this version, we improved the Model Patch UI and introduced a new panel that will help you solve any problems related to model patch application</span><span style="color: rgb(0,0,0);">. This panel lists all the changes that could not be applied and describes the underlying issue for each change. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Model Patch" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="model_patch.png" /></ac:image></p><h6 style="text-align: center;">Model Patch mechanism.</h6><p><br /></p><p style="text-align: center;"><span style="color: rgb(0,0,0);"><ac:image><ri:attachment ri:filename="changes_that_are_not_applied.png" /></ac:image></span></p><h6 style="text-align: center;">A panel listing the model patch changes that could not be applied.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p><h3>Commit Queues</h3><p><span style="color: rgb(13,13,13);">You now have access to a quicker and more predictable project commit execution at the end of a long working day: simultaneous commits are processed by putting all users in a First-In-First-Out (FIFO) line, ensuring fairness and efficiency in project commits. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(13,13,13);"><ac:image><ri:attachment ri:filename="commit_queues.png" /></ac:image></span></p><h6 style="text-align: center;">The dialog showing your position in the project commit queue.</h6><h3><br />Other</h3><ul><li>Starting with version 2024x Refresh1, <span style="color: rgb(13,13,13);">you won't need to manually</span> specify the Web Application Platform URL to access specific Teamwork Cloud features like Resource Usage Map or global element usage search. Teamwork Cloud will now retrieve the URL automatically.</li><li>Now it will be possible to skip the migration of archived branches when migrating Teamwork Cloud projects, which will significantly reduce the migration time.</li><li>The project comparing functionality no longer requires the Read Resources permission for used projects. However, you still need the Read Resources permission for the main projects you want to compare.</li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Collaboration Powered by <strong>3D</strong>EXPERIENCE Platform</h1><h3>Moving Projects to the <strong>3D</strong>EXPERIENCE Platform</h3><p>We're thrilled to announce a significant step towards collaboration between Teamwork Cloud and the <strong>3D</strong>EXPERIENCE platform. With this release<span>, you will have the ability to move Teamwork Cloud projects to the <strong>3D</strong>EXPERIENCE platform using the server project file format (.szip). </span><span>Previously, the .szip file format facilitated collaboration solely between different Teamwork Cloud servers. However, with version 2024x Refresh1, we have extended its functionality to allow importing projects from .szip files to the </span><strong>3D</strong><span>EXPERIENCE platform as well and <span style="color: rgb(23,43,77);">updating them if a project already exists on the platform.</span></span></p><p><span style="color: rgb(13,13,13);">We hope that you will benefit from this new functionality and stay tuned for further improvements in future releases</span>. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Importing Teamwork Cloud projects to the 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="moving_projects_to_platform.png" /></ac:image></p><h6 style="text-align: center;"><span>Moving projects to the <strong>3D</strong>EXPERIENCE platform by using the server project file format.</span></h6><h3><span><br />Iteration Merge Information</span></h3><p style="text-align: left;">Now the <strong>History</strong> and <strong>Edit Branches</strong> dialogs show <span>if a specific project iteration was merged, as well as the iteration it was merged from.</span></p><p style="text-align: left;"><br /></p><p style="text-align: center;"><span><ac:image><ri:attachment ri:filename="project_history.png" /></ac:image></span></p><h6 style="text-align: center;"><span>The Iteration column of the History dialog displays the project merge information.</span></h6><h3><span>Performance Improvements</span></h3><p><span><span style="color: rgb(23,43,77);">The performance for various basic server operations, especially project opening, has been significantly improved. As you can see in the charts below, now projects on the <strong>3D</strong>EXPERIENCE platform open at least five times faster compared to version 2024x.</span></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="project_opening_performance.png" /></ac:image></p><h6 style="text-align: center;">The charts comparing project opening performance for projects with 2 million elements.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Refresh1 Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170487623 space=MCSE2024xR1 version=1 -->
## PAGE 00003: 2024x Version News

- page_id: `170487623`
- space_key: `MCSE2024xR1`
- source_url: https://docs.nomagic.com/spaces/MCSE2024xR1/pages/170487623/2024x+Version+News
- version_number: 1
- version_date: `2024-04-19T13:54:32.478+02:00`
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

753686898

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

#### NOTE: 2024x Hot Fix 2 available

2024x Hot Fix 2 available

2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 2 Version News' space='NMDOC']>]]>

243271308

INLINE

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
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="ac060d11-24bb-43ee-828b-bfae5b72f6eb"><ac:parameter ac:name="id">753686899</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="d04429d1-af39-4fcc-95f9-34e91a0b1fb5"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">753686902</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="ce579dbe-f9d4-4d57-9f8f-444d4f75bd7c"><ac:parameter ac:name="id">753686898</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p style="text-align: center;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="fd7d672f-fb01-4e70-8982-8ff70256549a"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><h5 style="text-align: center;">Magic Cyber Systems Engineer</h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: November 10, 2023</span></p><p><br /></p><p><span style="color: rgb(62,63,64);">2024x release introduces several improvements to Item Flow creation and editing. The<span> </span> <strong>Create / Edit Item Flow<span> </span> </strong>dialog now provides greater clarity and usability, providing a more focused approach to reviewing Activity Pairs connected with existing Activity Edges. In addition, <strong style="text-align: left;">Autowire Parts</strong> <span> </span>and<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>commands' availability is changed in the SysML Internal Block Diagram and the SysML Parametric Diagram. Also, the<span> </span> <strong style="text-align: left;">Delegate Port(s)</strong> <span> </span>command functionality regarding nested ports is now improved to treat each displayed nested port individually.</span></p><p><span style="color: rgb(62,63,64);"> <span style="color: rgb(128,128,128);"> <span style="color: rgb(55,65,81);">Simulation features introduce a number of powerful functionalities. The new </span> </span> <span style="color: rgb(55,65,81);">product</span> <span style="color: rgb(55,65,81);"> </span> <span style="color: rgb(55,65,81);">version allows you to run server-side simulation with modified Simulation Configuration properties and even employ a virtual Simulation Configuration <span style="color: rgb(62,63,64);">without modifying the Teamwork Cloud project</span>.</span> <span style="color: rgb(55,65,81);"> The product also enables live unit conversion <span style="color: rgb(55,65,81);text-decoration: none;">to </span> <span style="color: rgb(55,65,81);text-decoration: none;">simplify</span> <span style="color: rgb(55,65,81);text-decoration: none;"> model analysis and reduce the likelihood of errors. Beyond these enhancements, you can customize</span> the Histogram appearance, control the simulation termination logic with the help of a new Auto Terminate property, and benefit from other smaller improvements.</span> </span></p><p><span>The 2024x release also introduces general modeling and infrastructure, as well as collaborative modeling enhancements.</span></p><p><span>For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</span></p><p><span>Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.</span></p><p><span>We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="ILTWRT" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the <ac:link><ri:space ri:space-key="MD2022xR1" /><ac:plain-text-link-body><![CDATA[product documentation]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="f9b23f4f-2dd2-42fb-9662-2ccc8dafb914"><ac:parameter ac:name="title">2024x Hot Fix 2 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Hot Fix 2 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fb82fc80-35bc-42cf-ab13-51cc01e20dfc"><ac:parameter ac:name="id">243271308</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong> <ac:link ac:anchor="SysML Features" /> </strong></p><ul><li><ac:link ac:anchor="Improved Item Flow Creation and Editing" /></li><li><ac:link ac:anchor="Other Improvements" />  </li></ul><p><strong> <ac:link ac:anchor="Simulation Features" /> </strong></p><ul><li><ac:link ac:anchor="Server-Side Simulation" /><ul><li><ac:link ac:anchor="Modifying Simulation Configuration Properties" /></li><li><ac:link ac:anchor="DSLS License Server Support" /></li></ul></li><li><ac:link ac:anchor="Live Unit Conversion for Runtime Objects" /></li><li><ac:link ac:anchor="Histogram Improvements" /></li><li><ac:link ac:anchor="Auto-Terminating Simulation Configurations" /></li><li><ac:link ac:anchor="Other Improvements1"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Discontinued Features" /> </strong></p><ul><li><span style="color: rgb(255,0,0);"> <ac:link ac:anchor="JavaScript Nashorn Scripting" /> </span></li><li><ac:link ac:anchor="Record Macro Functionality" /></li><li><ac:link ac:anchor="SPEM Plugin" /></li></ul><p><strong> <ac:link ac:anchor="Known Migration Issues" /> </strong></p><p><strong> <ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link> </strong></p><ul><li><span style="color: rgb(255,0,0);"> <ac:link ac:anchor="DSLS Licensing" /> </span></li><li><ac:link ac:anchor="Zoom in Model Browser" /></li><li><span style="color: rgb(23,43,77);"> <ac:link ac:anchor="Advanced Legend Adornments in Tables" /> </span></li><li><p style="text-align: left;"><ac:link ac:anchor="Other Improvements2"><ac:plain-text-link-body><![CDATA[Other Improvements]]></ac:plain-text-link-body></ac:link></p></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Collaboration" /> </strong></p><p><ac:link ac:anchor="TWC"><ac:plain-text-link-body><![CDATA[Teamwork Cloud]]></ac:plain-text-link-body></ac:link></p><ul><li><ac:link ac:anchor="New File Exchange Format for Server Projects" /></li><li><ac:link ac:anchor="Model Patch Mechanism (Technology Preview)" /></li></ul><p><ac:link ac:anchor="Power"><ac:plain-text-link-body><![CDATA[Power'By]]></ac:plain-text-link-body></ac:link></p><ul><li><ac:link ac:anchor="New Features to Manage Used Projects" /></li><li><ac:link ac:anchor="Opening Projects in Read-Only Mode" /></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1b77567e-eabc-4a51-b858-9f25a0643a8f"><ac:parameter ac:name="id">244508097</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>SysML Features</h5><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="f513c0f4-8ec4-4734-9196-44187491e529"><ac:parameter ac:name="">Improved Item Flow Creation and Editing</ac:parameter></ac:structured-macro>Improved Item Flow Creation and Editing</h3><p><span>SysML Plugin 2024x brings a more focused approach to reviewing Activity Pairs connected with existing Activity Edges in the </span> <strong>Create / Edit Item Flow </strong> <span>dialog, improving overall usability and clarity.</span></p><ul><li><span>Now, the second step centers exclusively on reviewing existing Activity Pairs connected by existing Activity Edges, thus:</span><ul><li><span>New Activity Pairs cannot be created, and existing Activity Pairs cannot be edited. Because of this, the tool will no longer initiate the automatic generation of new elements or diagrams. </span></li><li>The overall synchronization of the dialog's steps is now improved to ensure that all relevant Activity Pairs are systematically gathered based on specified preferences. This results in <span>a well-organized diagram list in the third step, accurately representing selected options.</span></li></ul></li></ul><p><ac:image ac:align="center"><ri:attachment ri:filename="Improved_Item_Flow.png" /></ac:image></p><h6 style="text-align: center;">A comparison of some of the changes in the second step of the <strong>Create / Edit Item Flow</strong> dialog between versions 2024x and 2022x Refresh2.</h6><p><ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Creating Item Flow" /><ac:plain-text-link-body><![CDATA[Learn more about Item Flow creation and editing >>]]></ac:plain-text-link-body></ac:link> </p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9c001aa7-667d-4750-b4db-cc7e6ffc4392"><ac:parameter ac:name="">Other Improvements</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li>The <strong>Tools</strong> option group containing <strong>Autowire Parts</strong> and <strong>Delegate Port(s)</strong> commands has been removed from the SysML Parametric Diagram toolbar. Both <strong>Delegate Port(s)</strong> and <strong>Autowire Parts</strong> commands are no longer available for Constraint Properties and Constraint Parameters in the SysML Internal Block Diagram and the SysML Parametric Diagram.</li><li>Improved <strong>Delegate Port(s)</strong> command functionality regarding nested ports. Now if the command is called from a part or a port enclosing a nested ports structure, each displayed nested port is treated individually to create delegated connectors and ports. <ac:link><ri:page ri:space-key="SYSMLP2024x" ri:content-title="Automatic delegation" /><ac:plain-text-link-body><![CDATA[Learn more about automatic delegation >>]]></ac:plain-text-link-body></ac:link></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="e3ec648a-2337-479b-af36-c178d5f75e7b"><ac:parameter ac:name="id">1298061950</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5>Simulation Features</h5><h3 style="text-align: left;">Server-Side Simulation</h3><h4>Modifying Simulation Configuration Properties</h4><p>Now, you can run server-side simulations with modified properties of a Simulation Configuration without having to change the Teamwork Cloud project. This approach provides a more convenient method to modify simulation properties without a modeling tool. <br />It's even feasible to run a simulation without explicitly specifying a Simulation Configuration; instead, a virtual Simulation Configuration can be employed. This gives you the possibility to quickly choose a different execution target and define its simulation properties.</p><p><br /></p><p style="text-align: center;"><span style="color: rgb(62,63,64);"> <ac:image><ri:attachment ri:filename="simconfig_parameter.png" /></ac:image> </span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">The REST API request body with the 'simconfig' parameter which allows specifying simulation properties.</span></h6><p style="text-align: center;"><span style="color: rgb(62,63,64);"> <ac:image ac:queryparams="effects=border-simple,blur-border"><ri:attachment ri:filename="autocomletion_jupyter.png" /></ac:image> </span></p><h6 style="text-align: center;"><span style="color: rgb(62,63,64);">Enabling<span style="color: rgb(23,43,77);"> the autocompletion option for the simulation using Jupyter Notebook.</span> </span></h6><p><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="Run simulation"><ri:page ri:space-key="CST2024x" ri:content-title="Simulation using REST API" /><ac:plain-text-link-body><![CDATA[Learn more about modifying Simulation Configuration properties using REST API >>]]></ac:plain-text-link-body></ac:link> </span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="CST2024x" ri:content-title="Simulation using Jupyter Notebook" /><ac:plain-text-link-body><![CDATA[Learn more about modifying Simulation Configuration properties using Jupyter Notebook >>]]></ac:plain-text-link-body></ac:link> </span></p><h4><span style="color: rgb(62,63,64);"> <br />DSLS Licensing Server Support</span></h4><p><span style="color: rgb(62,63,64);">From version 2024x, in addition to FlexNet, server-side simulation supports the DSLS licensing server.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS licensing >>]]></ac:plain-text-link-body></ac:link> </span></p><p style="text-align: right;"><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span></p><h3>Live Unit Conversion for Runtime Objects</h3><p><span style="color: rgb(55,65,81);">Cameo Simulation Toolkit 2024x introduces live unit conversion for simulation runtime objects. When Value Properties are connected using a Binding Connector, their runtime values will be automatically converted if they have compatible Value Types (like grams and kilograms). This feature simplifies model analysis, especially when combining elements from various sources, <span style="color: rgb(62,63,64);">and reduces the possibility of errors.</span> </span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(55,65,81);"> <ac:image><ri:attachment ri:filename="live_unit_conversion.png" /></ac:image> </span></p><h6 style="text-align: center;"><span style="color: rgb(55,65,81);">A Parametric Diagram with runtime values of Value Properties being automatically converted according to their Value Types during simulation.</span></h6><p><span style="color: rgb(55,65,81);"> <ac:link><ri:page ri:space-key="CST2024x" ri:content-title="Unit Conversion" /><ac:plain-text-link-body><![CDATA[Learn more about unit conversion for runtime objects >>]]></ac:plain-text-link-body></ac:link> </span></p><p style="text-align: right;"><span style="color: rgb(55,65,81);"> <span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span> </span></p><h3>Histogram Improvements</h3><p><span style="color: rgb(55,65,81);"> <span style="color: rgb(23,43,77);">We're happy to present a new functionality that will allow you to tailor the Histogram appearance. With this improvement, you can define a custom number of data bins in which the results will be distributed and achieve the desired Histogram shape and precision. Furthermore, the edge of the last data bin will now match the maximum value of the value array, ensuring accurate representation.</span> </span></p><p><br /></p><p style="text-align: center;"><span style="color: rgb(55,65,81);"> <span style="color: rgb(23,43,77);"> <ac:image><ri:attachment ri:filename="histogram_improvements.png" /></ac:image> </span> </span></p><h6 style="text-align: center;">A sample Histogram with the custom number of data bins. Here, the <strong>Number Of Bins</strong> property is set to 50.</h6><p><ac:link><ri:page ri:space-key="CST2024x" ri:content-title="Histogram" /><ac:plain-text-link-body><![CDATA[Learn more about working with Histograms >>]]></ac:plain-text-link-body></ac:link></p><h3>Auto-Terminating Simulation Configurations</h3><p><span style="color: rgb(23,43,77);">Simulation Configurations now have a new <strong>Auto Terminate</strong> property, allowing you to manage the simulation termination logic. If you set this property to <em>true</em>, the simulation is terminated when it completes or after the initialization phase if it does not start automatically. When the property is set to <em>false</em>, the simulation continues to run without termination, hanging at the end or after the initialization phase if it does not start automatically.</span></p><p style="text-align: left;"><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="auto_terminate_property.png" /></ac:image></p><h6 style="text-align: center;">A new <strong>Auto Terminate</strong> property of a Simulation Configuration.</h6><p><ac:link><ri:page ri:space-key="CST2024x" ri:content-title="SimulationConfig stereotype" /><ac:plain-text-link-body><![CDATA[Learn more about Simulation Configuration properties >>]]></ac:plain-text-link-body></ac:link></p><p style="text-align: right;"><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="17e6ae39-43e4-436c-a486-664e5e22a58c"><ac:parameter ac:name="">Other Improvements1</ac:parameter></ac:structured-macro>Other Improvements</h3><ul style="text-align: left;"><li><span style="color: rgb(55,65,81);">Generating HTML has become easier, thanks to the availability of the <strong>Generate HTML</strong> and <strong>Generate and Attach HTML</strong> actions in new, convenient locations. These actions can now be accessed from the context menu of a User Interface Modeling Diagram or a UI element in the Containment tree. Additionally, you can invoke the actions by right-clicking a property symbol, provided its type is a Widget.</span> <br /><span> <br /><ac:image><ri:attachment ri:filename="generating_and_attaching_html.png" /></ac:image> <br /><br /></span></li><li>The simulation now considers the <strong>Decimal Places</strong> project option.</li><li>The <em>Parametric Execution Profile</em> has been eliminated. The constraints for parametric execution have been moved to the <em>Simulation Profile</em>.</li></ul><p style="text-align: right;"><span style="color: rgb(62,63,64);"> <ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="30ac573a-9647-46db-9970-34218fdb29a6"><ac:parameter ac:name="id">272319258</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="22763b20-4732-4783-a4d2-7e1f4d09824a"><ac:parameter ac:name="">Discontinued Features</ac:parameter></ac:structured-macro>Discontinued Features</h5><p>The following features have been discontinued with the 2024x version release.</p><h3>JavaScript Nashorn Scripting</h3><p><span style="color: rgb(62,63,64);">The JavaScript<span> </span> </span>Nashorn <span style="color: rgb(62,63,64);">language usage has been removed from the modeling tool. Please use JavaScript<span> </span> <em>Rhino</em> instead<em>. </em>This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Deprecated JavaScript Nashorn" /><ac:plain-text-link-body><![CDATA[Learn more about the deprecated JavaScript Nashorn >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Record Macro Functionality </h3><p>The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.</p><h3>SPEM Plugin</h3><p>The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.</p><h5>Known Migration Issues</h5><p>Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.</p><p>To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the &lt;modeling_tool_install_dir&gt;\bin\&lt;modeling_tool&gt;.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="19265554-ddd8-4aac-b349-e17ad50aaf56"><ac:parameter ac:name="id">243174490</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h5><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="d9658866-47d8-4652-bd44-57d618a5c6d6"><ac:parameter ac:name="">DSLS Licensing</ac:parameter></ac:structured-macro>DSLS Licensing</h3><p>Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:</p><ul><li>License usage statistics, debugging, and simple UI to administer and view statistics.</li><li>Licenses are bound to their expiration date rather than the product version.</li><li>Nodelock (seat), floating, and managed licensing options.</li></ul><p>Thus, now you can choose to use either FlexNet or DSLS for product licensing. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f49ff8d-45a1-456c-a2a0-a919be8c1f02"><ac:rich-text-body><p>The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version <span>R2024x with modeling tool version 2024x</span>).</p></ac:rich-text-body></ac:structured-macro><p><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS Licensing >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9484f639-acef-4728-8acc-d1e2338719d2"><ac:parameter ac:name="">Zoom in Model Browser</ac:parameter></ac:structured-macro>Zoom in Model Browser</h3><p>From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking. </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Zoom in Model Browser.png" /></ac:image></p><h6 style="text-align: center;">Zooming in the Model Browser using keyboard shortcuts.</h6><p><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /><ac:plain-text-link-body><![CDATA[Learn more about zooming in the Model Browser>>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="24661fa1-5ddb-4481-a09b-e7ad23369751"><ac:parameter ac:name="">Advanced Legend Adornments in Tables</ac:parameter></ac:structured-macro>Advanced Legend Adornments in Tables</h3><p>In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Advanced Legend Adornments in Tables Example.png" /></ac:image></p><h6 style="text-align: center;">Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item <em>In Progress</em>.</h6><p style="text-align: right;"><br /></p><h3 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="90856e33-8181-4fc8-8fe9-caeeed943312"><ac:parameter ac:name="">Other Improvements2</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li><strong>OpenJDK version update. </strong>Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version. </li><li><strong> <span style="color: rgb(62,63,64);">Supported operating system changes for Linux. </span> </strong> <span style="color: rgb(62,63,64);">CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support. </span></li><li><strong>JavaScript Rhino version update.</strong> The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</li><li>It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.</li></ul><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="dcc5ff79-6a80-4582-9dc2-bb34ce0a429b"><ac:parameter ac:name="id">243713866</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h5><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="82578d71-581b-42b4-bfdc-d5dcd49ff7cd"><ac:parameter ac:name="">TWC</ac:parameter></ac:structured-macro> </span>Teamwork Cloud</h3><h4 style="text-align: left;">New File Exchange Format for Server Projects</h4><p>In version 2022x Refresh2, we introduced <strong>.szip</strong> – a new <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using server project file format" /><ac:plain-text-link-body><![CDATA[server project exchange format]]></ac:plain-text-link-body></ac:link>. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.</p><p>In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.</p><p style="text-align: center;"><ac:image ac:width="600"><ri:attachment ri:filename="project_exchange_options.png" /></ac:image></p><p style="margin-left: 0.0in;"><span style="color: rgb(0,0,0);">The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.</span></p><p style="margin-left: 0.0in;"><br /></p><p style="margin-left: 0.0in;text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image><ri:attachment ri:filename="szip_project_import_performance.png" /></ac:image> <ac:image><ri:attachment ri:filename="szip_project_export_performance.png" /></ac:image> </span></p><h6 style="text-align: center;">Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).</h6><p><br /></p><h4>Model Patch Mechanism (Technology Preview)</h4><p><span style="color: rgb(0,0,0);">We introduce the technology preview of the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Patch - Technology preview" /><ac:plain-text-link-body><![CDATA[Model Patch mechanism]]></ac:plain-text-link-body></ac:link>, a more lightweight way to move model changes. Model Patch can help you:</span></p><ul><li><span style="color: rgb(0,0,0);">Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;</span></li><li><span style="color: rgb(0,0,0);">Transfer only a specific scope of model changes between disconnected teams instead of the entire model;</span></li><li>Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.</li></ul><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="model_patch_mechanism.jpg" /></ac:image></p><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfdd0694-20ca-468f-858e-b8118a0d2206"><ac:parameter ac:name="">Power</ac:parameter></ac:structured-macro> </span>Power’By</h3><h4>New Features to Manage Used Projects</h4><p><span style="color: rgb(0,0,0);">We added new features that provide you with better capabilities to manage used projects in <strong>3D</strong>EXPERIENCE:</span></p><ul><li><span style="color: rgb(0,0,0);">Export packages as a new server project;</span></li><li><span style="color: rgb(0,0,0);">Move elements to/from used projects;</span></li><li><span style="color: rgb(0,0,0);">Import used projects.</span></li></ul><h4><span style="color: rgb(0,0,0);">Opening Projects in Read-Only Mode</span></h4><p><span style="color: rgb(0,0,0);">Beginning with version 2024x, you can open <strong>3D</strong>EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.</span></p><p style="text-align: center;"><ac:image ac:height="96"><ri:attachment ri:filename="3DEXPERIENCE_project_editing_disabled.jpg" /></ac:image></p><h6 style="text-align: center;">Notification informing the user that the <strong>3D</strong>EXPERIENCE project is read-only.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="0529d28e-ccbb-400b-8ef2-23229cc103a8"><ac:parameter ac:name="id">430554266</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=170487621 space=MCSE2024xR1 version=9 -->
## PAGE 00004: Magic Cyber Systems Engineer Documentation

- page_id: `170487621`
- space_key: `MCSE2024xR1`
- source_url: https://docs.nomagic.com/spaces/MCSE2024xR1/pages/170487621/Magic+Cyber+Systems+Engineer+Documentation
- version_number: 9
- version_date: `2024-10-08T10:19:56.415+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

**Docs of other versions**

- [CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='MCSE2024x']
- [CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='MCSE2022xR2']
- [CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='MCSE2022xR1']
- [CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='MCSE2022x']
- [CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='MCSE2021xR2']
- [CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='MCSE2021xR1']
- [CONFLUENCE_PAGE title='Magic Cyber Systems Engineer Documentation' space='MCSE2021x']

This is the home page of Magic Cyber Systems Engineer documentation.

Magic Cyber Systems Engineer is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to **systems engineering** needs.

The documentation of Magic Cyber Systems Engineer is a package that includes the documentation of these capabilities:

**[CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024xR1']**

Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.

Type a search phrase...

**[SysML modeling](https://docs.nomagic.com/display/SYSMLP2024xR1/SysML+Plugin+Documentation)**

Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.

Type a search phrase...

**[CONFLUENCE_PAGE title='Cameo Requirements Modeler Plugin Documentation' space='CRMP2024xR1']**

Guides you through the import, export, and management of SysML requirements.

Type a search phrase...

**[CONFLUENCE_PAGE title='Magic Model Analyst Documentation' space='MSI2024xR1']**

Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.

Type a search phrase...

**[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024xR1']**

Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation.

Type a search phrase...

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Docs of other versions</strong></p><ul><li><ac:link><ri:page ri:space-key="MCSE2024x" ri:content-title="Magic Cyber Systems Engineer Documentation" /><ac:plain-text-link-body><![CDATA[Magic Cyber Systems Engineer 2024x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MCSE2022xR2" ri:content-title="Magic Cyber Systems Engineer Documentation" /><ac:plain-text-link-body><![CDATA[Magic Cyber Systems Engineer 2022x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MCSE2022xR1" ri:content-title="Magic Cyber Systems Engineer Documentation" /><ac:plain-text-link-body><![CDATA[Magic Cyber Systems Engineer 2022x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MCSE2022x" ri:content-title="Magic Cyber Systems Engineer Documentation" /><ac:plain-text-link-body><![CDATA[Magic Cyber Systems Engineer 2022x]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MCSE2021xR2" ri:content-title="Magic Cyber Systems Engineer Documentation" /><ac:plain-text-link-body><![CDATA[Magic Cyber Systems Engineer 2021x Refresh2]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MCSE2021xR1" ri:content-title="Magic Cyber Systems Engineer Documentation" /><ac:plain-text-link-body><![CDATA[Magic Cyber Systems Engineer 2021x Refresh1]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:space-key="MCSE2021x" ri:content-title="Magic Cyber Systems Engineer Documentation" /><ac:plain-text-link-body><![CDATA[Magic Cyber Systems Engineer 2021x]]></ac:plain-text-link-body></ac:link></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>This is the home page of Magic Cyber Systems Engineer documentation.</p><p>Magic Cyber Systems Engineer is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to <strong>systems engineering</strong> needs.</p><p>The documentation of Magic Cyber Systems Engineer is a package that includes the documentation of these capabilities:</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"><strong><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[General capabilities]]></ac:plain-text-link-body></ac:link> </strong> <br /></span></p><p style="margin-left: 30.0px;">Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="a19a15e6-6d9c-4fe3-acfd-816196a1293c"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MD2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"><strong><a href="https://docs.nomagic.com/display/SYSMLP2024xR1/SysML+Plugin+Documentation">SysML modeling</a> </strong> <br /></span></p><p style="margin-left: 30.0px;">Provides descriptions of SysML diagrams and elements, plus introduces SysML specific features as well as gives guidelines for building systems.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="69c8d25a-03df-4212-8101-45b0d5e9b665"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="SYSMLP2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"><strong><ac:link><ri:page ri:space-key="CRMP2024xR1" ri:content-title="Cameo Requirements Modeler Plugin Documentation" /><ac:plain-text-link-body><![CDATA[Requirements modeling]]></ac:plain-text-link-body></ac:link> </strong> <br /></span></p><p style="margin-left: 30.0px;">Guides you through the import, export, and management of SysML requirements.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="2722c7c0-1772-4ad3-ada3-92a9891db8c7"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CRMP2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p style="margin-left: 30.0px;"><strong><ac:link><ri:page ri:space-key="MSI2024xR1" ri:content-title="Magic Model Analyst Documentation" /><ac:plain-text-link-body><![CDATA[Simulation]]></ac:plain-text-link-body></ac:link></strong></p><p style="margin-left: 30.0px;">Provides instructions on how to test the system reactions to user interaction or predefined testing data and execution scenarios.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="53fec610-94a2-4ec9-82de-907e2f11535a"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MSI2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p style="margin-left: 30.0px;"><strong><ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installation and licensing]]></ac:plain-text-link-body></ac:link> </strong></p><p style="margin-left: 30.0px;">Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation. </p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="b8ff725f-5178-4f97-9acb-182c5d9df593"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="IL2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=170487714 space=MCSE2024xR1 version=3 -->
## PAGE 00005: Support

- page_id: `170487714`
- space_key: `MCSE2024xR1`
- source_url: https://docs.nomagic.com/spaces/MCSE2024xR1/pages/170487714/Support
- version_number: 3
- version_date: `2024-05-08T16:59:44.850+02:00`
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
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f491134c-1f31-440c-b0cd-49219bca45e2"><ac:parameter ac:name="id">1906792292</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="92d28415-56a9-4da3-bb95-f0f1d439792a"><ac:parameter ac:name="id">1906792294</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="9bb8e93b-a585-44e2-909a-96290dfd3b3a"><ac:parameter ac:name="id">1906792293</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2602c0ae-4d92-45ef-b3a9-b208e2028088"><ac:rich-text-body><p>For information about the support, please visit: <a href="https://www.3ds.com/support/">https://www.3ds.com/support/</a></p></ac:rich-text-body></ac:structured-macro><h3>Reporting an Issue</h3><p><span style="color: rgb(0,0,0);">If you encounter an issue or the modeling tool becomes unresponsive, a separately executable tool is provided for analyzing the status of the process to aid in bug submission. </span><span style="color: rgb(0,0,0);">In these situations, manually start the <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em> file (located in the <em>&lt;modeling tool installation directory&gt;\bin folder</em>). </span><span style="color: rgb(0,0,0);">After you start <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em>, the </span><strong>Report an Issue</strong> dialog <span style="color: rgb(0,0,0);">opens. </span></p><p><span style="color: rgb(0,0,0);">In this dialog, you can easily dump threads or memory heap into files and provide those files when reporting an issue to the support team.</span></p><p><span style="color: rgb(0,0,0);"><ac:image ac:height="250"><ri:attachment ri:filename="report_issue.png" /></ac:image><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
