# NOMAGIC DOCUMENTATION SPACE: Magic Software Architect 2024x Refresh1

<!--NOMAGIC_SPACE key=MSA2024xR1 chunk=1 -->

<!--NOMAGIC_PAGE id=169682234 space=MSA2024xR1 version=1 -->
## PAGE 00001: 2024x News for Developers

- page_id: `169682234`
- space_key: `MSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSA2024xR1/pages/169682234/2024x+News+for+Developers
- version_number: 1
- version_date: `2023-11-09T13:02:47.885+01:00`
- ancestors: Magic Software Architect Documentation
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

<!--NOMAGIC_PAGE id=178159691 space=MSA2024xR1 version=6 -->
## PAGE 00002: 2024x Refresh1 Version News

- page_id: `178159691`
- space_key: `MSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSA2024xR1/pages/178159691/2024x+Refresh1+Version+News
- version_number: 6
- version_date: `2024-12-16T14:56:21.606+01:00`
- ancestors: Magic Software Architect Documentation
- labels: []

### NORMALIZED CONTENT

top

###### Magic Software Architect

Released on: July 5, 2024

The 2024x Refresh1 release introduces performance improvements, as well as general modeling and collaborative modeling enhancements.

The client-side performance enhancements include improvements in Diagram Export as SVG, optimizing the efficiency of exporting matrices and tables in the SVG format. This results in significantly reduced file sizes.

For general modeling, this release presents Information Flow management improvements. Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. You can also specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. Additionally, you can now choose whether you want to hide the arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified using the 'Hide Information Flow If Conveyed Information Is Missing' project option that controls the arrow visibility. Furthermore, the Conveyed Information in the 'New Conveyed Information' dialog is represented with icons to help you identify the Conveyed Information. Finally, new validation rules have been implemented to highlight Information Flows that do not have any Conveyed Information.

Additional enhancements include the improved samples access and navigation in the modeling tool, as now you can review the list of available samples any time by invoking the Samples tab. Also, a new 'Letter Spacing Reduction in SVG' environment option is introduced to control the spacing between letters when exporting diagram images in SVG format, allowing you to maintain text alignment within shape boundaries upon export.

Additionally, collaborative modeling brings several enhancements tothe Model Patch functionality, which is now out of the technology preview phase. The Model Patch UI has been improved with a new panel that identifies and explains issues related to model patch application. Project commit processes are now more efficient with a First-In-First-Out (FIFO) queue system for simultaneous commits. Finally, you can save time by skipping the migration of archived branches when migrating Teamwork Cloud projects and more.

Collaboration powered by the 3DEXPERIENCE platform introduces significant improvements as well. You can now move Teamwork Cloud projects to the 3DEXPERIENCE platform and then update these projects using the .szip file format. In addition, the History and Edit Branches dialogs now indicate if and from which iteration a project was merged.

To download the latest version of the modeling tool, see [CONFLUENCE_PAGE title='Downloading installation files' space='IL2024xR1']. For further information, check the [CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024xR1'].

#### NOTE: 2024x Refresh1 Hot Fix 1 available

2024x Refresh1 Hot Fix 1 available

2024x Refresh1 Hot Fix 1 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Refresh1 Hot Fix 1 Version News' space='CATIA']>]]>

****

- 

****

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

### Client side performance improvementsClient-side Performance Improvements

#### Improvements in Diagram Export as SVG

Exporting diagrams in Scalable Vector Graphics (*.svg) format now features significant optimizations, with the most notable improvements in matrix and table exports:

- 
  - Reduction in the file size of exported SVG files.
  - Export now requires up to 10 times less RAM resources.
  - Decreased duration of the export process.

These optimizations enhance the efficiency of exporting matrices and tables in SVG format, resulting in significantly reduced file sizes. The improvements impact various functionalities that utilize SVG image generation, such as image export via the MDZipX plugin or the 'Save as Image' command.

[IMAGE alt='' src='']

###### A chart comparing the file size of a Dependency Matrix exported as a SVG image in 2024x and 2024x Refresh1.

### miModeling and Infrastructure

#### Information Flow Management Improvements

- 
  - Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. [CONFLUENCE_PAGE title='Element usage in diagrams' space='MD2024xR1']>]]> [ATTACHMENT filename='Navigate_to_diagram_UML.png']
  - Specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. [CONFLUENCE_PAGE title='Information Flow' space='MD2024xR1']>]]> [IMAGE alt='' src='']
  - You can no w choose whether you want to hide the arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified . The **Hide Information Flow If Conveyed Information Is Missing** [CONFLUENCE_PAGE title='Setting project options' space='MD2024xR1'] controls the arrow visibility. [CONFLUENCE_PAGE title='Information Flow' space='MD2024xR1']>]]> 
[IMAGE alt='' src='']
  - Now the Conveyed Information in the New Conveyed Information dialog is represented with icons to help you identify the Conveyed Information. [IMAGE alt='' src='']
  - New validation rules ( [CONFLUENCE_PAGE title='Information Flow has no Conveyed Information' space='MD2024xR1'] and [CONFLUENCE_PAGE title='Realized Information Flow has no Conveyed Information' space='MD2024xR1'] ) have been implemented to highlight Information Flows that do not have any Conveyed Information. Learn more on the [CONFLUENCE_PAGE title='Information Flow has no Conveyed Information' space='MD2024xR1'] and [CONFLUENCE_PAGE title='Realized Information Flow has no Conveyed Information' space='MD2024xR1'] pages.

#### Improved Samples Access and Navigation

From now on, you can review the list of available samplesanytime by invoking theSamples tab. The tab displays all the samplesprovided with the modeling tool installation, providing a convenient way to review and access the needed samples.Additionally, you can use the search bar to navigate the available content efficiently both in the Samples and Welcome tabs.

[CONFLUENCE_PAGE title='Editor Tabs' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

#### Other Improvements

- 
  - A new Letter Spacing Reduction in SVG environment option is introduced to control the spacing between letters when exporting diagram images in SVG format . Adjusting letter spacing enables you to maintain text alignment within shape boundaries when exporting, ensuring it does not exceed their borders. [CONFLUENCE_PAGE title='Diagram image export' space='MD2024xR1']>]]>

### Collaboration

#### Model Patch Functionality Improvements

We are happy to announce that in this release the Model Patch functionality is coming out of the technology preview phase with several enhancements.Model Patch is a more convenient alternative to afull Model merge or disconnected team collaboration because itallows you to move the selected elements or element changes from one model branch to another and transfer only a specific scope of model modifications.

In this version, we improved the Model Patch UI and introduced a new panel that will help you solve any problems related to model patch application. This panel lists all the changes that could not be applied and describes the underlying issue for each change. [CONFLUENCE_PAGE title='Using Model Patch' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

###### Model Patch mechanism.

[IMAGE alt='' src='']

###### A panel listing the model patch changes that could not be applied.

#### Commit Queues

You now have access to a quicker and more predictable project commit execution at the end of a long working day: simultaneous commits are processed by putting all users in a First-In-First-Out (FIFO) line, ensuring fairness and efficiency in project commits. [CONFLUENCE_PAGE title='Committing changes to Teamwork Cloud' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

###### The dialog showing your position in the project commit queue.

#### Other

- 
  - Starting with version 2024x Refresh1, you won't need to manually specify the Web Application Platform URL to access specific Teamwork Cloud features like Resource Usage Map or global element usage search. Teamwork Cloud will now retrieve the URL automatically.
  - Now it will be possible to skip the migration of archived branches when migrating Teamwork Cloud projects, which will significantly reduce the migration time.
  - The project comparing functionality no longer requires the Read Resources permission for used projects. However, you still need the Read Resources permission for the main projects you want to compare.

### Collaboration Powered by **3D**EXPERIENCE Platform

#### Moving Projects to the **3D**EXPERIENCE Platform

We're thrilled to announce a significant step towards collaboration between Teamwork Cloud and the **3D**EXPERIENCE platform. With this release, you will have the ability to move Teamwork Cloud projects to the **3D**EXPERIENCEplatform using the server project file format (.szip).Previously, the .szip file format facilitated collaboration solely between different Teamwork Cloud servers. However, with version 2024x Refresh1, we have extended its functionality to allow importing projects from .szip files to the**3D**EXPERIENCE platform as well and updating them if a project already exists on the platform.

We hope that you will benefit from this new functionality and stay tuned for further improvements in future releases. [CONFLUENCE_PAGE title='Importing Teamwork Cloud projects to the 3DEXPERIENCE platform' space='MD2024xR1']>]]>

[IMAGE alt='' src='']

###### Moving projects to the **3D**EXPERIENCE platform by using the server project file format.

#### Iteration Merge Information

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7dc7bee2-3797-466f-982b-5a1e0d78e7c5"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><p><span class="confluence-embedded-file-wrapper image-center-wrapper"> </span></p><h5 style="text-align: center;"><span class="confluence-embedded-file-wrapper image-center-wrapper">Magic Software Architect</span></h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: July 5, 2024</span></p><p><br /></p><p>The 2024x Refresh1 release introduces performance improvements, as well as general modeling and collaborative modeling enhancements.</p><p>The client-side performance enhancements include improvements in Diagram Export as SVG, optimizing the efficiency of exporting matrices and tables in the SVG format. This results in significantly reduced file sizes.</p><p>For general modeling, this release presents Information Flow management improvements. Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. You can also specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. Additionally, you can now choose whether you want to hide the arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified using the 'Hide Information Flow If Conveyed Information Is Missing' project option that controls the arrow visibility. Furthermore, the Conveyed Information in the 'New Conveyed Information' dialog is represented with icons to help you identify the Conveyed Information. Finally, new validation rules have been implemented to highlight Information Flows that do not have any Conveyed Information.</p><p>Additional enhancements include the improved samples access and navigation in the modeling tool, as now you can review the list of available samples any time by invoking the Samples tab. Also, a new 'Letter Spacing Reduction in SVG' environment option is introduced to control the spacing between letters when exporting diagram images in SVG format, allowing you to maintain text alignment within shape boundaries upon export.</p><p>Additionally, collaborative modeling brings several enhancements to<span style="letter-spacing: 0.0px;"> the Model Patch functionality, which is now out of the technology preview phase. The Model Patch UI has been improved with a new panel that identifies and explains issues related to model patch application. Project commit processes are now more efficient with a First-In-First-Out (FIFO) queue system for simultaneous commits. Finally, you can save time by skipping the migration of archived branches when migrating Teamwork Cloud projects and more.</span></p><p><span style="letter-spacing: 0.0px;">Collaboration powered by the 3DEXPERIENCE platform introduces significant improvements as well. You can now move Teamwork Cloud projects to the 3DEXPERIENCE platform and then update these projects using the .szip file format. In addition, the History and Edit Branches dialogs now indicate if and from which iteration a project was merged.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[product documentation]]></ac:plain-text-link-body></ac:link>.</p><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="569e25e5-7042-4e37-bc33-e76dbcdf057e"><ac:parameter ac:name="title">2024x Refresh1 Hot Fix 1 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Refresh1 Hot Fix 1 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Refresh1 Hot Fix 1 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Client side performance improvements"><ac:plain-text-link-body><![CDATA[Client-side Performance Improvements]]></ac:plain-text-link-body></ac:link></strong></p><ul><li><ac:link ac:anchor="Improvements in Diagram Export as SVG" /></li></ul><p><strong><ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link></strong></p><ul><li><ac:link ac:anchor="Information Flow Management Improvements" /></li><li><ac:link ac:anchor="Improved Samples Access and Navigation" /></li><li><ac:link ac:anchor="Other Improvements" /></li></ul></ac:layout-cell><ac:layout-cell> <strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Collaboration" /></strong><ul><li><ac:link ac:anchor="Model Patch Functionality Improvements" /></li><li><ac:link ac:anchor="Commit Queues" /></li><li><ac:link ac:anchor="Other" /></li></ul><p><strong><ac:link ac:anchor="Collaboration Powered by 3DEXPERIENCE Platform" /></strong></p><ul><li><ac:link ac:anchor="Moving Projects to the 3DEXPERIENCE Platform" /></li><li><ac:link ac:anchor="Iteration Merge Information" /></li><li><ac:link ac:anchor="Performance Improvements" /></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="815c4f41-7b9a-4abd-a370-16ecd19fe713"><ac:parameter ac:name="">Client side performance improvements</ac:parameter></ac:structured-macro>Client-side Performance Improvements</h1><h2 style="margin-left: 40.0px;">Improvements in Diagram Export as SVG</h2><p style="margin-left: 40.0px;"><ac:inline-comment-marker ac:ref="2acf5364-4c4e-456b-99c8-49f367373f14">Exporting diagrams in Scalable Vector Graphics (*.svg) format now features significant optimizations, with the most notable improvements in matrix and table exports:</ac:inline-comment-marker></p><ul><li style="list-style-type: none;"><ul><li>Reduction in the file size of exported SVG files.</li><li>Export now requires up to 10 times less RAM resources.</li><li>Decreased duration of the export process.</li></ul></li></ul><p style="margin-left: 40.0px;">These optimizations enhance the efficiency of exporting matrices and tables in SVG format, resulting in significantly reduced file sizes. The improvements impact various functionalities that utilize SVG image generation, such as image export via the MDZipX plugin or the 'Save as Image' command.</p><p style="margin-left: 40.0px;"><ac:image ac:align="center"><ri:attachment ri:filename="File Size of Dependency Matrix Exported as SVG.png" /></ac:image></p><h6 style="text-align: center;margin-left: 40.0px;">A chart comparing the file size of a Dependency Matrix exported as a SVG image in 2024x and 2024x Refresh1.</h6></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h1><h2 style="margin-left: 40.0px;">Information Flow Management Improvements</h2><ul><li style="list-style-type: none;"><ul><li>Now you can easily navigate from the selected Information Flow in the Containment tree to the diagrams where that flow is realized. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Element usage in diagrams" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="Navigate_to_diagram_UML.png" /></ac:image></li><li>Specify the Conveyed Information directly in the diagram, picking the necessary Conveyed Information element from the diagram palette and dragging it on to the Information Flow. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><span><br /><ac:image><ri:attachment ri:filename="Specifying Conveyed Information via Diagram Palette.png" /></ac:image><br /></span></li><li>You can no<span style="color: rgb(23,43,77);">w choose whether you want to hide the</span><span style="color: rgb(23,43,77);"><span> </span>arrow notation on the realizing elements when the Conveyed Information is hidden or unspecified</span>. The <span><strong>Hide Information Flow If Conveyed Information Is Missing</strong> <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Setting project options" /><ac:plain-text-link-body><![CDATA[project option]]></ac:plain-text-link-body></ac:link> controls the arrow visibility. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link><br /><ac:image><ri:attachment ri:filename="hide_information_flow_UML.png" /></ac:image><br /></span></li><li>Now the Conveyed Information in the New Conveyed Information <span>dialog is represented with icons to help you identify the Conveyed Information. </span><span><br /><ac:image><ri:attachment ri:filename="Conveyed Information Element Icon.png" /></ac:image><br /></span></li><li>New validation rules (<ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[IFHNCI[1]]]></ac:plain-text-link-body></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /><ac:plain-text-link-body><![CDATA[RIFHNCI[1]]]></ac:plain-text-link-body></ac:link>)<span> have been implemented to highlight Information Flows that do not have any Conveyed Information. Learn more on the <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Information Flow has no Conveyed Information" /></ac:link> and <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Realized Information Flow has no Conveyed Information" /></ac:link> pages.</span></li></ul></li></ul><h2 style="text-align: left;margin-left: 40.0px;">Improved Samples Access and Navigation</h2><p style="margin-left: 40.0px;"><span style="letter-spacing: 0.0px;">From now on, you can review the list of available samples</span><span style="letter-spacing: 0.0px;"> anytime by invoking the </span><span style="letter-spacing: 0.0px;">Samples tab. The tab displays all the samples </span><span style="letter-spacing: 0.0px;">provided with the modeling tool installation, providing a convenient way to review and access the needed samples. </span><span style="letter-spacing: 0.0px;">Additionally, you can use the search bar to navigate the available content efficiently both in the Samples and Welcome tabs.</span></p><p style="margin-left: 40.0px;"><span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Editor Tabs" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p style="text-align: center;margin-left: 40.0px;"><ac:image><ri:attachment ri:filename="Improved Samples Access and Navigation.png" /></ac:image></p><h2 style="margin-left: 40.0px;">Other Improvements</h2><ul><li style="list-style-type: none;"><ul><li><span>A new </span><strong><span>Letter Spacing Reduction in SVG</span></strong><span> environment option is introduced to control the spacing between letters when exporting diagram images in SVG format</span>. Adjusting letter spacing enables you to maintain text alignment within shape boundaries when exporting, ensuring it does not exceed their borders. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Diagram image export" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></li></ul></li></ul><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Collaboration</h1><h2 style="margin-left: 40.0px;">Model Patch Functionality Improvements</h2><p style="margin-left: 40.0px;"><span style="color: rgb(0,0,0);"><span style="color: rgb(0,0,0);">We are happy to announce that in this release the Model Patch functionality is coming out of the technology preview phase with several enhancements. </span></span><span style="color: rgb(0,0,0);letter-spacing: 0.0px;">M</span><span style="color: rgb(0,0,0);letter-spacing: 0.0px;">odel Patch is a more convenient alternative to a </span><ac:inline-comment-marker ac:ref="61218513-e1f9-4191-94c6-eb3430d3c143">full Model merge or disconnected team collaboration because it </ac:inline-comment-marker><span style="color: rgb(0,0,0);letter-spacing: 0.0px;">allows you to move the selected elements or element changes from one model branch to another and transfer only a specific scope of model <ac:inline-comment-marker ac:ref="006e31a6-c4a9-4a7a-8a40-36fe5b8cbc3f">modifications</ac:inline-comment-marker>.</span></p><p style="margin-left: 40.0px;"><span style="color: rgb(0,0,0);">In this version, we improved the Model Patch UI and introduced a new panel that will help you solve any problems related to model patch application</span><span style="color: rgb(0,0,0);letter-spacing: 0.0px;">. This panel lists all the changes that could not be applied and describes the underlying issue for each change. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Using Model Patch" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p style="margin-left: 40.0px;"><br /></p><p style="margin-left: 40.0px;text-align: center;"><ac:image><ri:attachment ri:filename="model_patch.png" /></ac:image></p><h6 style="margin-left: 40.0px;text-align: center;">Model Patch mechanism.</h6><p><br /></p><p style="text-align: center;margin-left: 40.0px;"><span style="color: rgb(0,0,0);letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="changes_that_are_not_applied.png" /></ac:image></span></p><h6 style="text-align: center;">A panel listing the model patch changes that could not be applied.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p><h2 style="margin-left: 40.0px;"><ac:inline-comment-marker ac:ref="66cf7bf9-ba1d-48a0-bf2d-ea668db20188">Commit Queues</ac:inline-comment-marker></h2><p style="margin-left: 40.0px;"><span style="color: rgb(13,13,13);">You now have access to a quicker and more predictable project commit execution at the end of a long working day: simultaneous commits are processed by putting all users in a First-In-First-Out (FIFO) line, ensuring fairness and efficiency in project commits. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Committing changes to Teamwork Cloud" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></span></p><p style="margin-left: 40.0px;"><br /></p><p style="text-align: center;margin-left: 40.0px;"><span style="color: rgb(13,13,13);"><ac:image><ri:attachment ri:filename="commit_queues.png" /></ac:image></span></p><h6 style="text-align: center;">The dialog showing your position in the project commit queue.</h6><h2 style="margin-left: 40.0px;"><br />Other</h2><ul><li style="list-style-type: none;"><ul><li>Starting with version 2024x Refresh1, <span style="color: rgb(13,13,13);">you won't need to manually</span> specify the Web Application Platform URL to access specific Teamwork Cloud features like Resource Usage Map or global element usage search. Teamwork Cloud will now retrieve the URL automatically.</li><li>Now it will be possible to skip the migration of archived branches when migrating Teamwork Cloud projects, which will significantly reduce the migration time.</li><li>The project comparing functionality no longer requires the Read Resources permission for used projects. <ac:inline-comment-marker ac:ref="6f3679a1-c38f-4103-8c7b-64d725a284b1">However, you still need the Read Resources permission for the main projects you want to compare.</ac:inline-comment-marker></li></ul></li></ul><p style="text-align: right;"><ac:inline-comment-marker ac:ref="6f3679a1-c38f-4103-8c7b-64d725a284b1"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></ac:inline-comment-marker></p><h1>Collaboration Powered by <strong>3D</strong>EXPERIENCE Platform</h1><h2 style="margin-left: 40.0px;">Moving Projects to the <strong>3D</strong>EXPERIENCE Platform</h2><p style="margin-left: 40.0px;">We're thrilled to announce a significant step towards collaboration between Teamwork Cloud and the <strong>3D</strong>EXPERIENCE platform. With this release<span style="letter-spacing: 0.0px;">, you will have the ability to move Teamwork Cloud projects to the <strong>3D</strong><span>EXPERIENCE </span>platform using the server project file format (.szip). </span><span style="letter-spacing: 0.0px;">Previously, the .szip file format facilitated collaboration solely between different Teamwork Cloud servers. However, with version 2024x Refresh1, we have extended its functionality to allow importing projects from <ac:inline-comment-marker ac:ref="3086ffbe-d6b3-486d-a74f-5f7914cf938c">.szip files</ac:inline-comment-marker> to the </span><strong style="letter-spacing: 0.0px;">3D</strong><span style="letter-spacing: 0.0px;">EXPERIENCE platform as well and <span style="color: rgb(23,43,77);">updating them if a project already exists on the platform.</span></span></p><p style="margin-left: 40.0px;"><span style="color: rgb(13,13,13);">We hope that you will benefit from this new functionality and stay tuned for further improvements in future releases</span>. <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="Importing Teamwork Cloud projects to the 3DEXPERIENCE platform" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link></p><p style="margin-left: 40.0px;"><br /></p><p style="margin-left: 40.0px;text-align: center;"><ac:image><ri:attachment ri:filename="moving_projects_to_platform.png" /></ac:image></p><h6 style="margin-left: 40.0px;text-align: center;"><span style="letter-spacing: 0.0px;">Moving projects to the <strong>3D</strong>EXPERIENCE platform by using the server project file format.</span></h6><h2 style="margin-left: 40.0px;"><span style="letter-spacing: 0.0px;"><br />Iteration Merge Information</span></h2><p style="text-align: left;margin-left: 40.0px;">Now the <strong>History</strong> and <strong>Edit Branches</strong> dialogs show <span style="letter-spacing: 0.0px;">if a specific project iteration was merged, as well as the iteration it was merged from.</span></p><p style="text-align: left;margin-left: 40.0px;"><br /></p><p style="text-align: center;margin-left: 40.0px;"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="project_history.png" /></ac:image></span></p><h6 style="margin-left: 40.0px;text-align: center;"><span style="letter-spacing: 0.0px;">The Iteration column of the History dialog displays the project merge information.</span></h6><h3><span>Performance Improvements</span></h3><p><span><span style="color: rgb(23,43,77);">The performance for various basic server operations, especially project opening, has been significantly improved. As you can see in the charts below, now projects on the <strong>3D</strong>EXPERIENCE platform open at least five times faster compared to version 2024x.</span></span></p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="project_opening_performance.png" /></ac:image></p><h6 style="text-align: center;">The charts comparing project opening performance for projects with 2 million elements.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p><hr /></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><span style="color: rgb(255,0,0);"><ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Refresh1 Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></span></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=169682150 space=MSA2024xR1 version=1 -->
## PAGE 00003: 2024x Version News

- page_id: `169682150`
- space_key: `MSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSA2024xR1/pages/169682150/2024x+Version+News
- version_number: 1
- version_date: `2024-04-19T13:54:05.001+02:00`
- ancestors: Magic Software Architect Documentation
- labels: []

### NORMALIZED CONTENT

#### CONTENT-LAYER: 2024x Hot Fix 2 available

648293284

INLINE

#### CONTENT-COLUMN: 2024x Hot Fix 2 available

100.00002%

648293298

INLINE

648293285

INLINE

top

###### Magic Software Architect

Released on: November 10, 2023

The 2024x release introduces general modeling and infrastructure, as well as collaborative modeling enhancements.

For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.

Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.

We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.

To download the latest version of the modeling tool, see [CONFLUENCE_PAGE title='Downloading installation files' space='ILTWRT']. For further information, check the .

#### NOTE: 2024x Hot Fix 2 available

2024x Hot Fix 2 available

2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products . [CONFLUENCE_PAGE title='2024x Hot Fix 2 Version News' space='NMDOC']>]]>

648293283

INLINE

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

1994146009

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

649041710

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

##### Other ImprovementsOther Improvements

- OpenJDK version update. Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version.
- Supported operating system changes for Linux. CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support.
- JavaScript Rhino version update. The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.
- It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.

2139947249

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

###### [IMAGE alt='' src='']

##### PowerPower’By

###### New Features to Manage Used Projects

We added new features that provide you with better capabilities to manage used projects in **3D**EXPERIENCE:

- Export packages as a new server project;
- Move elements to/from used projects;
- Import used projects.

###### Opening Projects in Read-Only Mode

Beginning with version 2024x, you can open **3D** EXPERIENCE projects in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.

[IMAGE alt='' src='']

###### Notification informing the user that the **3D**EXPERIENCE project is read-only.

649599800

INLINE

[CONFLUENCE_PAGE title='2024x Version News' space='CATIA']>]]>

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="8e724017-c71b-4e7e-9b4e-9ca0e1e5ee22"><ac:parameter ac:name="id">648293284</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="3f9cbf16-dd87-4dad-bf2f-5d78c95e0dbf"><ac:parameter ac:name="width">100.00002%</ac:parameter><ac:parameter ac:name="id">648293298</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="d276ac27-09e4-4002-b02c-eb9b84b5c288"><ac:parameter ac:name="id">648293285</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="7dc7bee2-3797-466f-982b-5a1e0d78e7c5"><ac:parameter ac:name="">top</ac:parameter></ac:structured-macro></p><h5 style="text-align: center;"><span class="confluence-embedded-file-wrapper image-center-wrapper">Magic Software Architect</span></h5><p style="text-align: center;"><span style="color: rgb(128,128,128);">Released on: November 10<span style="color: rgb(128,128,128);">, 2023</span> </span></p><p><br /></p><p><span>The 2024x release introduces general modeling and infrastructure, as well as collaborative modeling enhancements.</span></p><p><span>For general modeling and infrastructure, this release presents the DSLS licensing option, the ability to zoom the Modeling Browser using keyboard shortcuts, and additional Legend adornment properties in Tables. Additionally, OpenJDK is now updated to version 17.0.8+7, CentOS Linux 7 is now replaced with Oracle Linux 8.8 support, and the JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</span></p><p><span>Several features have been discontinued with the 2024x version, such as the JavaScript Nashorn language usage, Record Macro functionality, and the SPEM plugin.</span></p><p><span>We have exciting news for collaborative modeling, as well. The new file exchange format .szip is now out of technology preview and was improved with a UI dialog for ease of use. Also, we introduce a major new feature: the Model Patch mechanism, a significantly lighter solution to move project changes. There are enhancements for 3DEXPERIENCE projects, too; you can now manage used projects more easily and open certain projects in a read-only mode.</span></p><p>To download the latest version of the modeling tool, see <ac:link><ri:page ri:space-key="ILTWRT" ri:content-title="Downloading installation files" /></ac:link>. For further information, check the <ac:link><ri:space ri:space-key="MD2022xR1" /><ac:plain-text-link-body><![CDATA[product documentation]]></ac:plain-text-link-body></ac:link>.</p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="468d1704-538c-4656-afb0-93884232873d"><ac:parameter ac:name="title">2024x Hot Fix 2 available</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">2024x Hot Fix 2 is now available for CATIA Magic and No Magic portfolios. <span style="color: rgb(23,43,77);">It includes a number of improvements and bug fixes, and vulnerability fixes in our modeling tools, plugins, and server products</span> </span> <span style="color: rgb(62,63,64);">. <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="2024x Hot Fix 2 Version News" /><ac:plain-text-link-body><![CDATA[Learn more >>]]></ac:plain-text-link-body></ac:link> </span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="5210811c-98a3-461c-9dd4-db84b4937cf8"><ac:parameter ac:name="id">648293283</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><strong> <ac:link ac:anchor="Discontinued Features" /> </strong></p><ul><li><span style="color: rgb(255,0,0);"> <ac:link ac:anchor="JavaScript Nashorn Scripting" /> </span></li><li><ac:link ac:anchor="Record Macro Functionality" /></li><li><ac:link ac:anchor="SPEM Plugin" /></li></ul><p><strong> <ac:link ac:anchor="Known Migration Issues" /> </strong></p></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="mi"><ac:plain-text-link-body><![CDATA[Modeling and Infrastructure]]></ac:plain-text-link-body></ac:link> </strong></p><ul><li><span style="color: rgb(255,0,0);"> <ac:link ac:anchor="DSLS Licensing" /> </span></li><li><ac:link ac:anchor="Zoom in Model Browser" /></li><li><span style="color: rgb(23,43,77);"> <ac:link ac:anchor="Advanced Legend Adornments in Tables" /> </span></li><li><p style="text-align: left;"><ac:link ac:anchor="Other Improvements" /></p></li></ul></ac:layout-cell><ac:layout-cell><p><strong> <ac:link ac:anchor="Collaboration" /> </strong></p><p><ac:link ac:anchor="TWC"><ac:plain-text-link-body><![CDATA[Teamwork Cloud]]></ac:plain-text-link-body></ac:link></p><ul><li><ac:link ac:anchor="New File Exchange Format for Server Projects" /></li><li><ac:link ac:anchor="Model Patch Mechanism (Technology Preview)" /></li></ul><p><ac:link ac:anchor="Power"><ac:plain-text-link-body><![CDATA[Power'By]]></ac:plain-text-link-body></ac:link></p><ul><li><ac:link ac:anchor="New Features to Manage Used Projects" /></li><li><ac:link ac:anchor="Opening Projects in Read-Only Mode" /></li></ul></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="b8a6a106-9ea4-4bbb-9ac4-169d31dffac0"><ac:parameter ac:name="id">1994146009</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="22763b20-4732-4783-a4d2-7e1f4d09824a"><ac:parameter ac:name="">Discontinued Features</ac:parameter></ac:structured-macro>Discontinued Features</h5><p>The following features have been discontinued with the 2024x version release.</p><h3>JavaScript Nashorn Scripting</h3><p><span style="color: rgb(62,63,64);">The JavaScript<span> </span> </span>Nashorn <span style="color: rgb(62,63,64);">language usage has been removed from the modeling tool. Please use JavaScript<span> </span> <em>Rhino</em> instead<em>. </em>This affects expression-related functionality, e.g., custom validation rules, derived properties, smart packages, tables, and macros.</span></p><p><span style="color: rgb(62,63,64);"> <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Deprecated JavaScript Nashorn" /><ac:plain-text-link-body><![CDATA[Learn more about the deprecated JavaScript Nashorn >>]]></ac:plain-text-link-body></ac:link> </span></p><h3>Record Macro Functionality </h3><p>The Record Macro functionality has been discontinued. However, any previously recorded macros can still be used in the modeling tool.</p><h3>SPEM Plugin</h3><p>The SPEM 2.0 Plugin (16.8 and 16.9 versions) has been discontinued.</p><h5>Known Migration Issues</h5><p>Projects created using modeling tools of version 19.x, may get corrupted after migration to version 2024x.</p><p>To avoid project corruption, before migrating or opening projects for the first time, close the modeling tool, open the &lt;modeling_tool_install_dir&gt;\bin\&lt;modeling_tool&gt;.properties file, find the JAVA_ARGS line, and add the -Dskip.ProjectCleanup=true (for MAC OS: -Dskip.ProjectCleanup\=true) argument as one of its values.</p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="1f99a462-0053-4696-86a7-908ad793ef7b"><ac:parameter ac:name="id">649041710</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="86c1e37a-6f77-4e5e-aa46-ea5b738c8c41"><ac:parameter ac:name="">mi</ac:parameter></ac:structured-macro>Modeling and Infrastructure</h5><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="d9658866-47d8-4652-bd44-57d618a5c6d6"><ac:parameter ac:name="">DSLS Licensing</ac:parameter></ac:structured-macro>DSLS Licensing</h3><p>Starting with the 2024x release, we are introducing a new licensing option - DSLS (Dassault Systèmes License Server). DSLS is a licensing system developed by Dassault Systèmes that provides these benefits:</p><ul><li>License usage statistics, debugging, and simple UI to administer and view statistics.</li><li>Licenses are bound to their expiration date rather than the product version.</li><li>Nodelock (seat), floating, and managed licensing options.</li></ul><p>Thus, now you can choose to use either FlexNet or DSLS for product licensing. </p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="9f49ff8d-45a1-456c-a2a0-a919be8c1f02"><ac:rich-text-body><p>The DSLS version must be compatible with the modeling tool version you use (currently, DSLS version <span>R2024x with modeling tool version 2024x</span>).</p></ac:rich-text-body></ac:structured-macro><p><ac:link><ri:page ri:space-key="IL2024x" ri:content-title="DSLS installation and licensing" /><ac:plain-text-link-body><![CDATA[Learn more about DSLS Licensing >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="9484f639-acef-4728-8acc-d1e2338719d2"><ac:parameter ac:name="">Zoom in Model Browser</ac:parameter></ac:structured-macro>Zoom in Model Browser</h3><p>From now on, you can easily increase the size of the displayed data in the Model Browser tabs. Zoom in and out using keyboard shortcuts to modify the view to your liking. </p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Zoom in Model Browser.png" /></ac:image></p><h6 style="text-align: center;">Zooming in the Model Browser using keyboard shortcuts.</h6><p><ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using the Model Browser" /><ac:plain-text-link-body><![CDATA[Learn more about zooming in the Model Browser >>]]></ac:plain-text-link-body></ac:link></p><h3><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="24661fa1-5ddb-4481-a09b-e7ad23369751"><ac:parameter ac:name="">Advanced Legend Adornments in Tables</ac:parameter></ac:structured-macro>Advanced Legend Adornments in Tables</h3><p>In addition to using Legend Items' Fill Color property to color table cells, now you can also add and color cell borders via the Pen Color and Line Width properties, as well as change the color of the text via the Text Color property, allowing you more options to emphasize specific data rows in tables.</p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Advanced Legend Adornments in Tables Example.png" /></ac:image></p><h6 style="text-align: center;">Text Color, Pen Color, and Line Width adornment properties are specified for the Legend Item <em>In Progress</em>.</h6><p style="text-align: right;"><br /></p><h3 style="text-align: left;"><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="672ef41c-9f3f-4bde-add8-61dd2944ee47"><ac:parameter ac:name="">Other Improvements</ac:parameter></ac:structured-macro>Other Improvements</h3><ul><li style="text-align: left;"><strong> <ac:inline-comment-marker ac:ref="5a26372f-78b5-4ce6-bf52-87d848d0d122">OpenJDK version update.</ac:inline-comment-marker> </strong>Desktop applications (MagicDraw, Cameo Systems Modeler, Cameo Enterprise Architecture, Magic Software Architect, Magic Cyber Systems Engineer, Magic Systems of Systems Architect) and Teamwork Cloud are now only run using OpenJDK 17.0.8+7 version. </li><li style="text-align: left;"><strong> <span style="color: rgb(62,63,64);">Supported operating system changes for Linux. </span> </strong> <span style="color: rgb(62,63,64);">CentOS Linux 7 has reached End of Life; thus, it is no longer supported. It is now replaced with Oracle Linux 8.8 support. </span></li><li style="text-align: left;"><strong>JavaScript Rhino version update.</strong> The JavaScript Rhino engine is now upgraded from 1.7R4 to the 1.7.13 version.</li><li>It is no longer necessary to display the pin's type when displaying its multiplicity due to the newly introduced Show Multiplicity symbol property.</li></ul><p style="text-align: right;"><br /></p><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="cc5705c1-a93d-4ba2-9c86-50d309c61eee"><ac:parameter ac:name="id">2139947249</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><h5><ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="c2a3e277-67ff-49eb-8666-39ed7c6d17c8"><ac:parameter ac:name="">Collaboration</ac:parameter></ac:structured-macro>Collaboration</h5><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="82578d71-581b-42b4-bfdc-d5dcd49ff7cd"><ac:parameter ac:name="">TWC</ac:parameter></ac:structured-macro> </span>Teamwork Cloud</h3><h4 style="text-align: left;"><ac:inline-comment-marker ac:ref="7c2ca0cb-2ea5-4912-bec7-86429a10563a">New File Exchange Format for Server Projects</ac:inline-comment-marker></h4><p>In version 2022x Refresh2, we introduced <strong>.szip</strong> – a new <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Using server project file format" /><ac:plain-text-link-body><![CDATA[server project exchange format]]></ac:plain-text-link-body></ac:link>. It addresses the issues of slow performance and project structural changes associated with the .mdzip format. Using .szip, you can export and import projects more quickly without altering the project structure.</p><p>In version 2024x, we further improved the .szip format by introducing a new UI dialog that allows you to select which projects you want to import to the server and which to skip. This gives you greater control over the file exchange process.</p><p style="text-align: center;"><ac:image ac:align="center" ac:width="600"><ri:attachment ri:filename="project_exchange_options.png" /></ac:image></p><p style="margin-left: 0.0in;"><span style="color: rgb(0,0,0);">The charts below depict how the .szip project format increases the performance of project export and import operations when compared to .mdzip. Depending on the project size element and used project count-wise, the performance gain for export can vary between 2-20 times, while the project import speed has been increased by roughly 40%.</span></p><p style="margin-left: 0.0in;"><br /></p><p style="margin-left: 0.0in;text-align: center;"><span style="color: rgb(51,51,51);"> <ac:image><ri:attachment ri:filename="szip_project_import_performance.png" /></ac:image> <ac:image><ri:attachment ri:filename="szip_project_export_performance.png" /></ac:image> </span></p><h6 style="text-align: center;">Comparing the import and export performance of Project #1 (1M elements, 57 Used Projects), Project #2 (2M elements, 7 Used Projects), and Project #3 (2M+ elements, 3 Used Projects).</h6><p><br /></p><h4>Model Patch Mechanism (Technology Preview)</h4><p><span style="color: rgb(0,0,0);">We introduce the technology preview of the <ac:link><ri:page ri:space-key="MD2024x" ri:content-title="Model Patch - Technology preview" /><ac:plain-text-link-body><![CDATA[Model Patch mechanism]]></ac:plain-text-link-body></ac:link>, a more lightweight way to move model changes. Model Patch can help you:</span></p><ul><li><span style="color: rgb(0,0,0);">Move changes from one branch to another without the need to perform a full Merge operation, which can be slow and cumbersome;</span></li><li><span style="color: rgb(0,0,0);">Transfer only a specific scope of model changes between disconnected teams instead of the entire model;</span></li><li>Reuse only the necessary subset of an external model as an alternative to bringing in the whole model as a Used Project.</li></ul><h6 style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="model_patch_mechanism.jpg" /></ac:image></h6><h3><span style="color: rgb(0,0,0);"> <ac:structured-macro ac:name="anchor" ac:schema-version="1" ac:macro-id="bfdd0694-20ca-468f-858e-b8118a0d2206"><ac:parameter ac:name="">Power</ac:parameter></ac:structured-macro> </span>Power’By</h3><h4>New Features to Manage Used Projects</h4><p><span style="color: rgb(0,0,0);">We added new features that provide you with better capabilities to manage used projects in <strong>3D</strong>EXPERIENCE:</span></p><ul><li><span style="color: rgb(0,0,0);">Export packages as a new server project;</span></li><li><span style="color: rgb(0,0,0);">Move elements to/from used projects;</span></li><li><span style="color: rgb(0,0,0);">Import used projects.</span></li></ul><h4><span style="color: rgb(0,0,0);">Opening Projects in Read-Only Mode</span></h4><p><span style="color: rgb(0,0,0);">Beginning with version 2024x, you can open <strong> <ac:inline-comment-marker ac:ref="c7319731-fdab-4bb0-85c6-0548eef6b250">3D</ac:inline-comment-marker> </strong> <ac:inline-comment-marker ac:ref="c7319731-fdab-4bb0-85c6-0548eef6b250">EXPERIENCE projects</ac:inline-comment-marker> in Read-Only mode. Projects open in this mode with a balloon notification if you do not have the necessary access rights or if the project is in Read-Only mode because of its maturity state.</span></p><p style="text-align: center;"><ac:image ac:height="96"><ri:attachment ri:filename="3DEXPERIENCE_project_editing_disabled.jpg" /></ac:image></p><h6 style="text-align: center;">Notification informing the user that the <strong>3D</strong>EXPERIENCE project is read-only.</h6><p style="text-align: right;"><ac:link ac:anchor="top"><ac:plain-text-link-body><![CDATA[Back to top]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="8885ba51-e5f3-4e8f-bf38-a3179c393beb"><ac:parameter ac:name="id">649599800</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><ac:link><ri:page ri:space-key="CATIA" ri:content-title="2024x Version News" /><ac:plain-text-link-body><![CDATA[Version news of servers and plugins >>]]></ac:plain-text-link-body></ac:link></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=169682148 space=MSA2024xR1 version=2 -->
## PAGE 00004: Magic Software Architect Documentation

- page_id: `169682148`
- space_key: `MSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSA2024xR1/pages/169682148/Magic+Software+Architect+Documentation
- version_number: 2
- version_date: `2024-05-08T16:38:26.385+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

564776767

INLINE

564776769

INLINE

564776768

INLINE

INLINE

This is the home page of Magic Software Architect documentation.

Magic Software Architect is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to **software engineering** needs.

The documentation of Magic Software Architect is a package that includes the documentation of these capabilities:

**[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024xR1']**

Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation.

**[CONFLUENCE_PAGE title='MagicDraw Documentation' space='MD2024xR1']**

Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.

Type a search phrase...

[CONFLUENCE_PAGE title='Cameo Data Modeler Plugin' space='CDMP2024xR1']**Data modeling**

Provides data-related modeling, it includes entity-relationship, database and XML schema modeling features. Data modeling is enabled/disable by the user.

Type a search phrase...

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="d516dbf5-4ea4-4e56-a38a-2c61f18af7be"><ac:parameter ac:name="id">564776767</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="44f03ae1-e5ba-44d1-ae13-9dbd20224243"><ac:parameter ac:name="id">564776769</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="fbdaba4d-bb14-4162-84f0-78e175cad82e"><ac:parameter ac:name="id">564776768</ac:parameter><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="excerpt" ac:schema-version="1" ac:macro-id="af240ef5-4a37-4427-ad60-32bf12c83123"><ac:parameter ac:name="atlassian-macro-output-type">INLINE</ac:parameter><ac:rich-text-body><ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>This is the home page of Magic Software Architect documentation.</p><p>Magic Software Architect is based on the award-winning MagicDraw modeling platform. The solution retains all the best diagramming, collaboration, persistence, and documentation capabilities while offering more customized capabilities tailored to <strong>software engineering</strong> needs.</p><p>The documentation of Magic Software Architect is a package that includes the documentation of these capabilities:</p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><strong> <ac:link><ri:page ri:space-key="IL2024xR1" ri:content-title="Installation, licensing, and system requirements" /><ac:plain-text-link-body><![CDATA[Installation and licensing]]></ac:plain-text-link-body></ac:link> </strong></p><p style="margin-left: 30.0px;">Provides the instructions about how to install modeling tool and plugins, add or remove licenses, perform activation. </p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"> <strong> <ac:link><ri:page ri:space-key="MD2024xR1" ri:content-title="MagicDraw Documentation" /><ac:plain-text-link-body><![CDATA[General capabilities]]></ac:plain-text-link-body></ac:link> </strong> <br /></span></p><p style="margin-left: 30.0px;">Introduces the main features of modeling tool: working with projects, UML 2 modeling and diagramming, collaboration capabilities, and many more core features.</p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="6209a95a-cd1c-4afd-9a1f-658f38c81657"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="MD2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_left_sidebar"><ac:layout-cell><p style="margin-left: 30.0px;"><span class="confluence-link"> <ac:link><ri:page ri:space-key="CDMP2024xR1" ri:content-title="Cameo Data Modeler Plugin" /><ac:link-body> <strong>Data modeling</strong> </ac:link-body></ac:link> <br /></span></p><p style="margin-left: 30.0px;">Provides data-related modeling, it includes <span style="color: rgb(62,63,64);">entity-relationship, database and XML schema modeling features. Data modeling is enabled/disable by the user.</span></p><p style="margin-left: 30.0px;"><br /></p></ac:layout-cell><ac:layout-cell><p><ac:structured-macro ac:name="livesearch" ac:schema-version="1" ac:macro-id="9d22b45f-87d5-496e-b65c-ae69b9674cf5"><ac:parameter ac:name="spaceKey"><ri:space ri:space-key="CDM2024xR1" /></ac:parameter><ac:parameter ac:name="placeholder">Type a search phrase...</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section></ac:layout></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=169682235 space=MSA2024xR1 version=3 -->
## PAGE 00005: Support

- page_id: `169682235`
- space_key: `MSA2024xR1`
- source_url: https://docs.nomagic.com/spaces/MSA2024xR1/pages/169682235/Support
- version_number: 3
- version_date: `2024-05-08T17:00:40.535+02:00`
- ancestors: Magic Software Architect Documentation
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
<ac:structured-macro ac:name="content-layer" ac:schema-version="1" ac:macro-id="f491134c-1f31-440c-b0cd-49219bca45e2"><ac:parameter ac:name="id">1906792292</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-column" ac:schema-version="1" ac:macro-id="92d28415-56a9-4da3-bb95-f0f1d439792a"><ac:parameter ac:name="id">1906792294</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="content-block" ac:schema-version="1" ac:macro-id="afcf3ca4-8e78-455a-b459-1132e6be5227"><ac:parameter ac:name="id">1906792293</ac:parameter><ac:rich-text-body><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="2602c0ae-4d92-45ef-b3a9-b208e2028088"><ac:rich-text-body><p>For information about the support, please visit: <a href="https://www.3ds.com/support/" style="letter-spacing: 0.0px;">https://www.3ds.com/support/</a></p></ac:rich-text-body></ac:structured-macro><h3>Reporting an Issue</h3><p><span style="color: rgb(0,0,0);">If you encounter an issue or the modeling tool becomes unresponsive, a separately executable tool is provided for analyzing the status of the process to aid in bug submission. </span><span style="color: rgb(0,0,0);">In these situations, manually start the <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em> file (located in the <em>&lt;modeling tool installation directory&gt;\bin folder</em>). </span><span style="color: rgb(0,0,0);">After you start <em><span style="color: rgb(62,63,64);">submit_issue.exe</span></em>, the </span><strong>Report an Issue</strong> dialog <span style="color: rgb(0,0,0);">opens. </span></p><p><span style="color: rgb(0,0,0);">In this dialog, you can easily dump threads or memory heap into files and provide those files when reporting an issue to the support team.</span></p><p><span style="color: rgb(0,0,0);"><ac:image ac:height="250"><ri:attachment ri:filename="report_issue.png" /></ac:image><br /></span></p></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro></ac:rich-text-body></ac:structured-macro>
````
