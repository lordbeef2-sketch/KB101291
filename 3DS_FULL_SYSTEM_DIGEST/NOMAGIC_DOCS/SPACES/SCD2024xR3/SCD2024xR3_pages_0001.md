# NOMAGIC DOCUMENTATION SPACE: Systems Cybersecurity Designer 2024x Refresh3

<!--NOMAGIC_SPACE key=SCD2024xR3 chunk=1 -->

<!--NOMAGIC_PAGE id=227164556 space=SCD2024xR3 version=1 -->
## PAGE 00001: 2024x Refresh1 Version News

- page_id: `227164556`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164556/2024x+Refresh1+Version+News
- version_number: 1
- version_date: `2024-06-18T11:42:55.195+02:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

### Systems Cybersecurity Designer

Released on: July 5, 2024

In version 2024x Refresh1,[CONFLUENCE_PAGE title='Systems Cybersecurity Designer' space='']introduces many new features and enhancements for Threat Analysis and Risk Assessment analysis as per[ISO/SAE 21434:2021](https://www.iso.org/standard/70918.html). This release presents new enhancements, including the introduction of attack path modeling, the number of new libraries to add, customizing threat types to your requirements, generating reports, and automatic generation of cybersecurity goals.

****

- 
- 

****

****

****

****

****

****

- 
- 
- 

### Attack Path modeling

##### Attack Graphs

You can now generate a new kind of diagram (i.e.,****Cybersecurity Attack Graph***)*to ease the creation of Simple Attack Paths, also known as Manual Attack Paths. With this diagram, you can easily createAttack Path Steps, define potentialCausalityrelations between the steps, and automatically compute all possible Attack Paths (Manual Attack Paths) between the two steps. To learn more refer to[CONFLUENCE_PAGE title='Cyber Security Attack Graph' space=''].

[IMAGE alt='' src='']

###### Attack Graph showing possible Simple Attack Paths.

[IMAGE alt='' src='']

###### Manual Attack Paths table.

##### Attack Potential Based Attack Paths

In addition to Manual Attack Paths, a new flavor of Attack Path (potential-based) is available.

With these **Attack Potential-based Attack Paths**, **Attack Feasibility Rating** is automatically computed, based on the following core factors:

- Elapsed Time
- Specialist Expertise
- Knowledge of the Item/Component
- Window of Opportunity
- Equipment

To learn more, refer to [CONFLUENCE_PAGE title='Attack Potential Based Attack Path' space=''].

[IMAGE alt='' src='']

###### Attack Potential Based Attack Paths table along with the available core parameters.

### OOTB Model Libraries

You can now add new model libraries introduced in this release, and can add them to any TARA project.

Following is a list of newly added libraries:

- MITRE ATT&CK Enterprise Technique Library
- MITRE ATT&CK ICS Technique Library
- NIST Control Library

MITRE ATT&CK Technique Libraries describe specific methods or approaches used by attackers to achieve their objectives. Those represent 'how' an adversary achieves a given step of an attack, by performing a specific action. When one of those techniques is used as a step of an Attack Path, the recommended requirements for that technique will be automatically proposed by the **Recommend Control** command on any Threat Scenario associated to that Attack Path. To learn more, refer to[CONFLUENCE_PAGE title='Libraries' space=''].

[IMAGE alt='' src='']

###### MITRE ATT&CK Enterprise Technique Library.

[IMAGE alt='' src='']

###### MITRE ATT&CK ICS Technique Library.

[IMAGE alt='' src='']

###### NIST Control Library.

### Customizable Threat Types

In addition to the STRIDE classification for Threat Types, UNECE classification is now directly available in the tool.Moreover, theseThreat Typesare now customizable by users. A custom hierarchy of threat types can be created, and will be automatically used in the selection dialog of threat type, in addition to STRIDE and UNECE. To learn more, refer to [CONFLUENCE_PAGE title='Threat scenario' space=''].

[IMAGE alt='' src='']

###### Select Threat Type dialog showing customized threat types in the custom folder along with STRIDE and UNECE classification.

### Assets creation

New commands have been added to simplify Assets creation, and to ease the selection of Asset’s Underlying Elements. To learn more, refer to [CONFLUENCE_PAGE title='Asset' space=''].

From a SysML Block Definition Diagram or from a SysML Internal Block Diagram, you can now directly:

- Create new Assets.
- Add an Underlying Element to an existing Asset.

From an Item Table, you can now select a set of Members and:

- Create a new Asset with those Members as Underlying Element.
- Add those Members as Underlying Elements of an existing Asset.

### Reports

It is now possible to export your ISO 21434 project using Report Wizard capability, with a provided TARA Report Template. To learn more, refer to [CONFLUENCE_PAGE title='Generating Cybersecurity Reports' space=''].

### Automatic generation of Cybersecurity Goals

In the TARA table, you may want to auto-generate the cybersecurity goals associated with a given Threat Scenario, without needing to create them one by one. We provide a dedicated command,**Generate /Synchronize Cybersecurity goals,**in the TARA table for the same purpose. When the command runs on a Threat Scenario, it will create a set of Cybersecurity goals, and associate those goals with the Threat Scenario. The names of the auto-generated Cybersecurity Goals will be: “[Asset Name] of the [Item Name] shall be protected against [Threat type]”.

### Other improvements

##### Final Item with Cybersecurity Concept

ISO21424 project now provides an additional table, which gathers all Items, with associated Assets, Goals and Requirements.

[IMAGE alt='' src='']

###### Functional Cybersecurity Concept table with the item and its associated assets, goals and requirements.

##### ISO 21434 & 26262 convergence

Safety goals defined in a HARA analysis can be reused in a TARA analysis, and a validation rule validates that the ASIL Value & Safety Risk**Value are aligned.

##### Enhanced Recommend control command

The**Recommend control** command now recursively searches for recommended requirements associated to Attack Path Steps. For example, if anAttack Pathhas a step, which is anotherAttack Path, then the steps of the secondAttack Pathwill be considered by thisRecommend controlcommand.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;"><span style="color: rgb(23,43,77);">Systems Cybersecurity Designer</span></h1><p style="text-align: center;"><span style="color: rgb(62,63,64);"><span style="color: rgb(128,128,128);">Released on: July 5, 2024</span></span></p><p style="text-align: left;"><span style="letter-spacing: 0.0px;"><span style="color: rgb(62,63,64);">In version 2024x Refresh1,</span> </span><ac:link><ri:page ri:content-title="Systems Cybersecurity Designer" /></ac:link><span style="letter-spacing: 0.0px;"> </span><span style="letter-spacing: 0.0px;">introduces many new features and enhancements for Threat Analysis and Risk Assessment analysis as per </span><a href="https://www.iso.org/standard/70918.html" style="letter-spacing: 0.0px;">ISO/SAE 21434:2021</a><span style="letter-spacing: 0.0px;">. This release presents new enhancements, including the introduction of attack path modeling, the number of new libraries to add, customizing threat types to your requirements, generating reports, and automatic generation of cybersecurity goals.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="two_equal"><ac:layout-cell><p><strong><ac:link ac:anchor="Attack Path modeling" /></strong></p><ul><li><ac:link ac:anchor="Attack Graphs" /></li><li><ac:link ac:anchor="Attack Potential Based Attack Paths" /></li></ul><p><strong><ac:link ac:anchor="OOTB Model Libraries" /></strong></p><p><strong><ac:link ac:anchor="Customizable Threat Types" /></strong></p><p><strong> <ac:link ac:anchor="Assets creation" /></strong></p></ac:layout-cell><ac:layout-cell><p><strong style="letter-spacing: 0.0px;"><ac:link ac:anchor="Reports" /></strong></p><p><strong><ac:link ac:anchor="Automatic generation of Cybersecurity Goals" /></strong></p><p><strong><span style="letter-spacing: 0.0px;"><ac:link ac:anchor="Other improvements" /></span></strong></p><ul><li><ac:link ac:anchor="Final Item with Cybersecurity Concept" /></li><li><ac:link ac:anchor="ISO 21434 &amp; 26262 convergence" /></li><li><ac:link ac:anchor="Enhanced Recommend control command" /></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Attack Path modeling</h1><h3>Attack Graphs</h3><p>You can now generate a new kind of diagram (i.e.,<em> </em><strong><ac:inline-comment-marker ac:ref="9515cb63-5598-44f0-ace2-520d9162972d">Cybersecurity</ac:inline-comment-marker> Attack Graph</strong><em>) </em>to ease the creation of Simple Attack Paths, also known as Manual Attack Paths. <span style="letter-spacing: 0.0px;">With this diagram, you can easily create </span><span style="letter-spacing: 0.0px;">Attack Path Steps</span><span style="letter-spacing: 0.0px;">, define potential </span><span style="letter-spacing: 0.0px;">Causality</span><span style="letter-spacing: 0.0px;"> relations between the steps, and automatically compute all possible Attack Paths (</span><span style="letter-spacing: 0.0px;">Manual Attack Paths</span><span style="letter-spacing: 0.0px;">) between the two steps. To learn more refer to </span><ac:link><ri:page ri:content-title="Cyber Security Attack Graph" /></ac:link><span style="letter-spacing: 0.0px;">.</span></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Attack Graph.png" /></ac:image></p><h6 style="text-align: center;">Attack Graph showing possible Simple Attack Paths.</h6><p><ac:image ac:align="center"><ri:attachment ri:filename="Manual Attack Path.png" /></ac:image></p><h6 style="text-align: center;">Manual Attack Paths table.</h6><h3>Attack Potential Based Attack Paths</h3><p>In addition to Manual Attack Paths, a new flavor of Attack Path (potential-based) is available.</p><p>With these <strong>Attack Potential-based Attack Paths</strong>, <strong>Attack Feasibility Rating</strong> is automatically computed, based on the following core factors:</p><ul><li>Elapsed Time</li><li>Specialist Expertise</li><li>Knowledge of the Item/Component</li><li>Window of Opportunity</li><li>Equipment</li></ul><p>To learn more, refer to <ac:link><ri:page ri:content-title="Attack Potential Based Attack Path" /></ac:link><span>.</span></p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Attack Potential Based Attack Path.png" /></ac:image></p><h6 style="text-align: center;">Attack Potential Based Attack Paths table along with the available core parameters.</h6><h1>OOTB Model Libraries</h1><p>You can now add new model libraries introduced in this release, and can add them to any TARA project.</p><p>Following is a list of newly added libraries:</p><ul><li><ac:inline-comment-marker ac:ref="4e70d8ed-05f3-452b-b720-931246fab6cc">MITRE ATT&amp;CK Enterprise Technique Library</ac:inline-comment-marker></li><li><ac:inline-comment-marker ac:ref="92f68a9c-97ac-417c-8277-1a9460291eab">MITRE ATT&amp;CK ICS Technique Library</ac:inline-comment-marker></li><li>NIST Control Library</li></ul><p>MITRE ATT&amp;CK Technique Libraries describe specific methods or approaches used by attackers to achieve their objectives. Those represent 'how' an adversary achieves a given step of an attack, by performing a specific action. <span style="letter-spacing: 0.0px;">When one of those techniques is used as a step of an Attack Path, the recommended requirements for that technique will be automatically proposed by the <strong>Recommend Control</strong> command on any Threat Scenario associated to that Attack Path. To learn more, refer to </span><ac:link><ri:page ri:content-title="Libraries" /></ac:link>.</p><p><br /></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Enterprise Technique.png" /></ac:image></p><h6 style="text-align: center;"><span style="letter-spacing: 0.0px;">MITRE ATT&amp;CK Enterprise Technique Library.</span></h6><p><ac:image ac:align="center"><ri:attachment ri:filename="ICS Technique.png" /></ac:image></p><h6 style="text-align: center;">MITRE ATT&amp;CK ICS Technique Library.</h6><p style="text-align: center;"><ac:image><ri:attachment ri:filename="NIST Control.png" /></ac:image></p><h6 style="text-align: center;"><span style="letter-spacing: 0.0px;color: rgb(94,108,132);font-size: 12.0px;font-weight: 600;">NIST Control Library.</span></h6><h1><span style="font-size: 24.0px;letter-spacing: -0.01em;">Customizable Threat Types</span></h1><p style="text-align: left;"><span style="text-align: center;letter-spacing: 0.0px;">In addition to the STRIDE classification for Threat Types, UNECE classification is now directly available in the tool. </span><span style="text-align: center;letter-spacing: 0.0px;">Moreover, these </span><span style="letter-spacing: 0.0px;text-align: center;">Threat Types</span><span style="letter-spacing: 0.0px;text-align: center;"> are now customizable by users. A custom hierarchy of threat types can be created, and will be automatically used in the selection dialog of threat type, in addition to STRIDE and UNECE. To learn more, refer to <ac:link><ri:page ri:content-title="Threat  scenario" /><ac:plain-text-link-body><![CDATA[Threat scenario]]></ac:plain-text-link-body></ac:link>.</span></p><p><span style="letter-spacing: 0.0px;"> </span></p><p style="text-align: center;"><ac:image><ri:attachment ri:filename="Nesting Effect.png" /></ac:image></p><h6 style="text-align: center;"><span style="letter-spacing: 0.0px;">Select Threat Type dialog showing customized threat types in <ac:inline-comment-marker ac:ref="6c3d6ecd-6060-4cfd-a709-e8c50e08229a">the custom folder along</ac:inline-comment-marker> with STRIDE and UNECE classification.</span></h6><h1>Assets creation</h1><p>New commands have been added to simplify Assets creation, and to ease the selection of Asset’s Underlying Elements. To learn more, refer to <ac:link><ri:page ri:content-title="Asset" /></ac:link>.</p><p>From a SysML Block Definition Diagram or from a SysML Internal Block Diagram, you can now directly:</p><ul><li>Create new Assets.</li><li>Add an Underlying Element to an existing Asset.</li></ul><p>From an Item Table, you can now select a set of Members and:</p><ul><li>Create a new Asset with those Members as Underlying Element.</li><li>Add those Members as Underlying Elements of an existing Asset.</li></ul><h1>Reports</h1><p>It is now possible to export your ISO 21434 project using Report Wizard capability, with a provided TARA Report Template. To learn more, refer to <ac:link><ri:page ri:content-title="Generating  Cybersecurity Reports" /><ac:plain-text-link-body><![CDATA[Generating Cybersecurity Reports]]></ac:plain-text-link-body></ac:link>.<span style="font-size: 24.0px;letter-spacing: -0.01em;"> </span></p><h1>Automatic generation of Cybersecurity Goals</h1><p>In the TARA table, you may want to auto-generate the cybersecurity goals associated with a given Threat Scenario, without needing to create them one by one. <span style="letter-spacing: 0.0px;">We provide a dedicated command, </span><strong style="letter-spacing: 0.0px;">Generate /Synchronize Cybersecurity goals, </strong><span style="letter-spacing: 0.0px;">in the TARA table for the same purpose. When the command runs on a Threat Scenario, it will create a set of Cybersecurity goals, and associate those goals with the Threat Scenario. The names of the auto-generated Cybersecurity Goals will be: “</span><span style="letter-spacing: 0.0px;">[Asset Name] of the [Item Name] shall be protected against [Threat type]</span><span style="letter-spacing: 0.0px;">”.</span></p><h1>Other improvements</h1><h3>Final Item with Cybersecurity Concept</h3><p>ISO21424 project now provides an additional table, which gathers all Items, with associated Assets, Goals and Requirements.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Functional Cybersecurity.png" /></ac:image></p><h6 style="text-align: center;">Functional Cybersecurity Concept table with the item and its associated assets, goals and requirements.</h6><h3>ISO 21434 &amp; 26262 convergence</h3><p>Safety goals defined in a HARA analysis can be reused in a TARA analysis, and a validation rule validates that the ASIL Value &amp; Safety Risk<em> </em>Value are aligned.</p><h3>Enhanced Recommend control command</h3><p>The<strong> Recommend control</strong> command now recursively searches for recommended requirements associated to Attack Path Steps. <span style="letter-spacing: 0.0px;">For example, if an </span>Attack Path<span style="letter-spacing: 0.0px;"> has a step, which is another </span>Attack Path<span style="letter-spacing: 0.0px;">, then the steps of the second </span>Attack Path<span style="letter-spacing: 0.0px;"> will be considered by this </span>Recommend control<span style="letter-spacing: 0.0px;"> command.</span></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164547 space=SCD2024xR3 version=1 -->
## PAGE 00002: 2024x Refresh2 Version News

- page_id: `227164547`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164547/2024x+Refresh2+Version+News
- version_number: 1
- version_date: `2025-03-11T07:40:40.046+01:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

### Systems Cybersecurity Designer

Released on: November 8, 2024

The 2024x Refresh2 release introduces a set of new features and enhancements for Threat Analysis and Risk Assessment analysis as per [ISO/SAE 21434:2021](https://www.iso.org/standard/70918.html).

- 
- 

- 
- 

### Cybersecurity Assurance Level

##### Cybersecurity Assurance Level Property

A Cybersecurity Goal contains a new property **Cybersecurity Assurance Level**(CAL)****depicting the cybersecurity assurance level that has been assigned to the goal either directly or via a derivation of another Cybersecurity Goal.

[IMAGE alt='' src='']

###### **Cybersecurity Assurance Level**property displayed in the Specification dialog.

The ISO 21434 Profile project contains a default set of 4 CAL values. You can also create and use the custom set of CAL values.

[IMAGE alt='' src='']

###### **CAL**package containing four CAL values in the Containment Tree.

##### Cybersecurity Goal Assurance Table

Cybersecurity Goal Assurance Table helps you to specify the CAL value for each Cybersecurity Goal. Only one CAL value can be assigned for one Cybersecurity Goal.

[IMAGE alt='' src='']

###### Cybersecurity Goal Assurance Table

### Global Risk Map in the TARA Report

A Global Risk Map spreadsheet is now available as part of the TARA Report provided with the Report Wizard capability. The spreadsheet displays the mapping of Threat Scenarios corresponding a given Impact Rating and a given Attack Feasibility Rating.

[IMAGE alt='' src='']

###### Global Risk Map in the TARA Report

### Threat Scenario Residual Risk

Similar to the four SFOP Risk Values and the subsequent Global Risk Value, properties for representing corresponding Residual Risk Values for a Threat Scenario can be specified. The values can be specified through the TARA table or the specification window of a Threat Scenario by selecting a number from the drop down or typing in any number between 0.0 and 5.0.

[IMAGE alt='' src='']

###### Residual Risk Values present in TARA table.

[IMAGE alt='' src='']

###### Residual Risk Values present in the Specification dialog.

### Other Improvements

##### OOTB Model Library Version

The provided model libraries are tagged with the version number corresponding to the data set from which the library was created/updated.

[IMAGE alt='' src='']

###### OOTB Model Library Version

##### NIST Control Library Families

The NIST Control Library’s package structure properly reflects the names of the NIST Families.

[IMAGE alt='' src='']

###### NIST Families names displayed in the library structure.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;">Systems Cybersecurity Designer</h1><p style="text-align: center;"><span style="color: rgb(122,134,154);">Released on: November 8, 2024</span></p><p>The 2024x Refresh2 release introduces a set of new features and enhancements for Threat Analysis and Risk Assessment analysis as per <a href="https://www.iso.org/standard/70918.html">ISO/SAE 21434:2021</a>.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><ac:link ac:anchor="Cybersecurity Assurance Level" /></p><ul><li><ac:link ac:anchor="Cybersecurity Assurance Level Property" /></li><li><ac:link ac:anchor="Cybersecurity Goal Assurance Table" /></li></ul></ac:layout-cell><ac:layout-cell><p><ac:link ac:anchor="Global Risk Map in the TARA Report" /></p><p><ac:link ac:anchor="Threat Scenario Residual Risk" /></p></ac:layout-cell><ac:layout-cell><p><ac:link ac:anchor="Other Improvements" /></p><ul><li><ac:link ac:anchor="OOTB Model Library Version" /></li><li><ac:link ac:anchor="NIST Control Library Families" /></li></ul></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1>Cybersecurity Assurance Level</h1><h3>Cybersecurity Assurance Level Property</h3><p>A Cybersecurity Goal contains a new property <strong>Cybersecurity Assurance Level</strong>(CAL)<strong> </strong>depicting the cybersecurity assurance level that has been assigned to the goal either directly or via a derivation of another Cybersecurity Goal.</p><p><br /></p><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="image 1.png" /></ac:image></p><h6 style="text-align: center;"><strong>Cybersecurity Assurance Level </strong>property displayed in the Specification dialog.</h6><p>The ISO 21434 Profile project contains a default set of 4 CAL values. You can also create and use the custom set of CAL values.</p><p><br /></p><p style="text-align: center;"><ac:image ac:height="250"><ri:attachment ri:filename="image 2.png" /></ac:image></p><h6 style="text-align: center;"><strong>CAL </strong>package containing four CAL values in the Containment Tree.</h6><h3>Cybersecurity Goal Assurance Table</h3><p><br /></p><span style="letter-spacing: 0.0px;">Cybersecurity Goal Assurance Table helps you to specify the CAL value for each Cybersecurity Goal. Only one CAL value can be assigned for one Cybersecurity Goal.</span><p><br /></p><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="image 3.png" /></ac:image></p><h6 style="text-align: center;">Cybersecurity Goal Assurance Table</h6><h1>Global Risk Map in the TARA Report</h1><p> <span style="letter-spacing: 0.0px;">A Global Risk Map spreadsheet is now available as part of the TARA Report provided with the Report Wizard capability.  The spreadsheet displays the mapping of Threat Scenarios corresponding a given Impact Rating and a given Attack Feasibility Rating.</span></p><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="image 4.png" /></ac:image></p><h6 style="text-align: center;">Global Risk Map in the TARA Report</h6><h1>Threat Scenario Residual Risk</h1><p>Similar to the four SFOP Risk Values and the subsequent Global Risk Value, properties for representing corresponding Residual Risk Values for a Threat Scenario can be specified.  The values can be specified through the TARA table or the specification window of a Threat Scenario by selecting a number from the drop down or typing in any number between 0.0 and 5.0.</p><p><br /></p><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="image 5.png" /></ac:image></p><h6 style="text-align: center;">Residual Risk Values present in TARA table.</h6><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="image 6.png" /></ac:image></p><h6 style="text-align: center;">Residual Risk Values present in the Specification dialog.</h6><h1>Other Improvements</h1><h3><span style="font-size: 20.0px;letter-spacing: -0.008em;">OOTB Model Library Version</span></h3><p>The provided model libraries are tagged with the version number corresponding to the data set from which the library was created/updated.</p><p><br /></p><p style="text-align: center;"><ac:image ac:width="700"><ri:attachment ri:filename="image 7.png" /></ac:image></p><h6 style="text-align: center;">OOTB Model Library Version</h6><h3><span style="letter-spacing: -0.008em;font-size: 20.0px;">NIST Control Library Families</span></h3><p>The NIST Control Library’s package structure properly reflects the names of the NIST Families.</p><p><br /></p><p><ac:image ac:align="center" ac:height="400"><ri:attachment ri:filename="image 8.png" /></ac:image></p><h6 style="text-align: center;">NIST Families names displayed in the library structure.</h6><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164544 space=SCD2024xR3 version=4 -->
## PAGE 00003: 2024x Refresh3 Version News

- page_id: `227164544`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164544/2024x+Refresh3+Version+News
- version_number: 4
- version_date: `2025-11-27T17:16:48.812+01:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

### Systems Cybersecurity Designer

Released on: July 11, 2025

The 2024x Refresh3 release adds enhanced usability and improved standard compliance. Drag and drop support now allows seamless assignment of elements in ISO 21434 Element tables. Multi-selection of Threat Scenarios is now supported while generating or synchronizing the cybersecurity goals.Additionally,MITRE librarieshave been updated to the latest versions, and other improvements ensure accurate risk ratings and clearer notifications messages while working withTWC.

### Multi-selection support of Threat Scenarios

Multi-selection of Threat Scenarios in TARA table and in the Containment tree is now supported while using the **Generate/Synchronize Cybersecurity Goals** Command.

[IMAGE alt='' src='']

###### Multi-selection of Threat Scenarios in TARA table is now supported while using the **Generate/Synchronize Cybersecurity Goals**Command.

MITRE Libraries

The following standard libraries provided with the ISO 21434 Plugin have been upgraded to reflect the latest versions of the corresponding dataset:

- MITRE CWE Library has been updated to version 4.16 .
- MITRE ATT&CK Enterprise Technique Library has been updated to version 16.1 .
- MITRE ATT&CK ICS Technique Library has been updated to version 16.1 .
- MITRE ATT&CK Platforms Library has been updated to version 16.1 .

### Other Improvements

- The new improvement now ensures that you can assign the relevant elements only to the corresponding properties. For example, the Failure Mode element can only be assigned to the Failure property of any Damage Scenario.
- The new improvement now ensures that the Threat Scenario has a risk rating before specifying a corresponding residual risk rating.
- The new improvement now ensures that the appropriate content is now displayed in the notification message while working with TWC.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;">Systems Cybersecurity Designer</h1><p style="text-align: center;"><span style="color:var(--ds-chart-gray-bold,#8590a2);">Released on: July 11, 2025</span></p><p style="text-align: center;"><br /></p><p>The 2024x Refresh3 release adds enhanced usability and improved standard compliance. Drag and drop support now allows seamless assignment of elements in ISO 21434 Element tables. Multi-selection of Threat Scenarios is now supported while generating or synchronizing the cybersecurity goals.<span style="letter-spacing: 0.0px;"> Additionally, </span>MITRE libraries<span style="letter-spacing: 0.0px;"> have been updated to the latest versions, and other improvements ensure accurate risk ratings and clearer <span>notifications messages while working with </span>TWC.</span></p><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="three_equal"><ac:layout-cell><p><ac:link ac:anchor="Multi-selection support of Threat Scenarios" /></p></ac:layout-cell><ac:layout-cell><p><ac:link ac:anchor="MITRE Libraries" /></p></ac:layout-cell><ac:layout-cell><p><span><ac:link ac:anchor="Other Improvements" /></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p><br /></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h1><span>Multi-selection support of Threat Scenarios</span></h1><p>Multi-selection of Threat Scenarios in TARA table and in the Containment tree is now supported while using the <strong>Generate/Synchronize Cybersecurity Goals</strong> Command.</p><p><span><br /><ac:image ac:align="center"><ri:attachment ri:filename="Multi_selection.png" /></ac:image></span></p><h6 style="text-align: center;"><span>Multi-selection of Threat Scenarios in TARA table is now supported while using the <strong>Generate/Synchronize Cybersecurity Goals </strong>Command.</span></h6><p><span style="font-size: 24.0px;letter-spacing: -0.01em;">MITRE Libraries </span></p><p style="text-align: left;"><span style="letter-spacing: 0.0px;">The following standard libraries provided with the ISO 21434 Plugin have been upgraded to reflect the latest versions of the corresponding dataset:</span></p><ul><li>MITRE CWE Library has been updated to version <strong>4.16</strong>.</li><li>MITRE ATT&amp;CK Enterprise Technique Library has been updated to version <strong>16.1</strong>.</li><li>MITRE ATT&amp;CK ICS Technique Library has been updated to version <strong>16.1</strong>.</li><li>MITRE ATT&amp;CK Platforms Library has been updated to version <strong>16.1</strong>.</li></ul><h1 style="text-align: left;">Other Improvements</h1><ul style="text-align: left;"><li><span style="letter-spacing: 0.0px;">The new improvement now ensures that you can assign the relevant elements only to the corresponding properties. For example, the Failure Mode element can only be assigned to the Failure property of any Damage Scenario.</span></li><li><span style="letter-spacing: 0.0px;">The new improvement now ensures that the Threat Scenario has a risk rating before specifying a corresponding residual risk rating.</span></li><li>The new improvement now ensures that the appropriate content is now displayed in the notification message while working with TWC.</li></ul></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164570 space=SCD2024xR3 version=1 -->
## PAGE 00004: 2024x Version News

- page_id: `227164570`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164570/2024x+Version+News
- version_number: 1
- version_date: `2024-06-18T11:42:39.499+02:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

### Systems Cybersecurity Designer

Released on: November 10, 2023

In this release, a new plugin: [CONFLUENCE_PAGE title='Systems Cybersecurity Designer' space=''] has been introduced. The Systems Cybersecurity Designer plugin enables security assessments on systems architecture as per ISO 21434:2021.

###### Systems Cybersecurity Designer

Cybersecurity engineering is a critical discipline thatensures safe and secure human experiences using cyber physical systems. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events. The[CONFLUENCE_PAGE title='Systems Cybersecurity Designer' space='']Systems CybersecurityDesigner supports the[ISO/SAE 21434 standard](https://www.iso.org/standard/70918.html). Itenables a proactive and continuous security assessment in the initial design phase to reduce product development costs and time. Systems cybersecurity designers are able to create a Threat Analysis and Risk Assessment (TARA) project template to comply with the ISO/SAE 21434:2021. TheSystemsCybersecurity Designer is based in [SysML](https://www.omgsysml.org/what-is-sysml.htm)and [RAAML](https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML).

TheSystemsCybersecurity Designerallows a cybersecurity designer to:

- Design a safe and secure system through a built-in scalable cyber system model, which includes assets, weaknesses, threats, attack paths, and security requirements.
- Perform continuous threat assessments and hazard analyses to enhance design through real world scenarios.
- Support certification needs with consistent safety and cybersecurity compliance views.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;">Systems Cybersecurity Designer</h1><p style="text-align: center;"><span style="color: rgb(62,63,64);"><span style="color: rgb(128,128,128);">Released on: November 10, 2023</span></span></p><p style="text-align: left;">In this release, a new plugin: <ac:link><ri:page ri:content-title="Systems Cybersecurity Designer" /></ac:link> has been introduced. The <span style="color: rgb(62,63,64);">Systems Cybersecurity Designer plugin enables security assessments on systems architecture as per ISO 21434:2021.</span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h5>Systems Cybersecurity Designer</h5><p><span style="color: rgb(62,63,64);">Cybersecurity engineering is a critical discipline that<span> </span></span><span style="color: rgb(62,63,64);">ensures safe and secure human experiences using cyber physical systems</span><span style="color: rgb(62,63,64);">. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events. The<span> </span><ac:link><ri:page ri:content-title="Systems Cybersecurity Designer" /><ac:link-body>Systems Cybersecurity<span> </span>Designer</ac:link-body></ac:link> supports the<a class="external-link" href="https://www.iso.org/standard/70918.html" style="text-decoration: none;"><span> </span>ISO/SAE 21434 standard</a>. It<span> </span>enables a proactive and continuous security assessment in the initial design phase to reduce product development costs and time. Systems cybersecurity designers are able to create a Threat Analysis and Risk Assessment (TARA) project template to comply with the ISO/SAE 21434:2021. The<span> </span>Systems<span> </span>Cybersecurity Designer is based in <a href="https://www.omgsysml.org/what-is-sysml.htm"> SysML </a>and <a href="https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML">RAAML</a>.</span></p><p>The<span> </span>Systems<span> </span><span style="color: rgb(62,63,64);">Cybersecurity Designer<span> </span></span>allows a cybersecurity designer to:</p><ul><li>Design a safe and secure system through a built-in scalable cyber system model, which includes assets, weaknesses, threats, attack paths, and security requirements.</li><li>Perform continuous threat assessments and hazard analyses to enhance design through real world scenarios.</li><li>Support certification needs with consistent safety and cybersecurity compliance views.</li></ul><p><br /></p><p><ac:image><ri:attachment ri:filename="Index.png" /></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=242780701 space=SCD2024xR3 version=2 -->
## PAGE 00005: 2026x Version News

- page_id: `242780701`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/242780701/2026x+Version+News
- version_number: 2
- version_date: `2025-07-18T13:48:22.355+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

### Systems Cybersecurity Designer

Released on: November 28, 2025

In this release, a new Cybersecurity Template: [CONFLUENCE_PAGE title='DO-326A Preliminary Security Risk Assessment' space='SCDTWRT']has been introduced, which is based on the [DO-326A](https://products.rtca.org/21dja1f/)standard. TheDO-326Astandard, titled*Airworthiness Security Process Specification*, provides guidance for the implementation of an airworthiness cybersecurity process.

##### DO-326A Preliminary Security Risk Assessment

Cybersecurity engineering is a critical discipline that ensures the safe and secure operation of connected and complex airborne systems. The increasing integration of digital and networked technologies in aviation demands a robust, lifecycle-oriented approach to manage cybersecurity risks. This update implements the[DO-326A](https://products.rtca.org/21dja1f/)methodology within the Systems Cybersecurity Designer to enable compliance assessments during the development of avionics systems.

DO-326A, published by RTCA and EUROCAE, defines the process framework for airworthiness security — that is, ensuring that cybersecurity threats do not compromise the safety and continued airworthiness of an aircraft. Its main principles include:

- A risk-based approach to managing cybersecurity threats to aircraft systems.
- Lifecycle integration, requiring threat and mitigation analysis from system concept through decommissioning.

The Systems Cybersecurity Designer now enables users to:

- Model avionics systems for cybersecurity risk assessment , incorporating assets, vulnerabilities, threat scenarios, attack paths, and mitigations in line with DO-326A guidance.
- Perform a Security Risk Assessment (SRA) and Aircraft System Security Assessment (ASSA) using structured, iterative methodologies.
- Link safety and cybersecurity analyses , helping teams ensure consistency between security measures and system safety objectives.
- Produce certification-ready artifacts that demonstrate compliance with DO-326A, and support alignment with DO-355 (Information Security Guidance for Continuing Airworthiness) and DO-356A (Security Methods and Considerations).

By embedding DO-326A methodology into the design workflow, this update empowers aerospace engineers to reduce certification risk, identify security issues early in development, and streamline the path toward regulatory approval.

[IMAGE alt='' src='']

###### DO-326A Index.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><h1 style="text-align: center;">Systems Cybersecurity Designer</h1><p style="text-align: center;"><span style="color:var(--ds-chart-gray-bold,#8590a2);">Released on: November 28, 2025</span></p><p>In this release, a new Cybersecurity Template: <span style="letter-spacing: 0.0px;"><ac:link><ri:page ri:space-key="SCDTWRT" ri:content-title="DO-326A Preliminary Security Risk Assessment" /></ac:link> </span><span style="letter-spacing: 0.0px;">has been introduced, which is based on the <a href="https://products.rtca.org/21dja1f/">DO-326A</a><span> standard. <span style="color:var(--ds-text,#172b4d);">The </span>DO-326A<span style="color:var(--ds-text,#172b4d);"> standard, titled </span><em style="text-align: left;">Airworthiness Security Process Specification</em><span style="color:var(--ds-text,#172b4d);">, provides guidance for the implementation of an airworthiness cybersecurity process.</span></span></span></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>DO-326A Preliminary Security Risk Assessment</h3><p><span style="letter-spacing: 0.0px;">Cybersecurity engineering is a critical discipline that ensures the safe and secure operation of connected and complex airborne systems. The increasing integration of digital and networked technologies in aviation demands a robust, lifecycle-oriented approach to manage cybersecurity risks. This update implements the </span><a style="letter-spacing: 0.0px;" href="https://products.rtca.org/21dja1f/">DO-326A</a><span style="letter-spacing: 0.0px;"> methodology within the Systems Cybersecurity Designer to enable compliance assessments during the development of avionics systems.</span></p><p>DO-326A, published by RTCA and EUROCAE, defines the process framework for airworthiness security — that is, ensuring that cybersecurity threats do not compromise the safety and continued airworthiness of an aircraft. Its main principles include:</p><ul><li data-uuid="0b3da48a-2e64-407b-9f8a-57eb1acd7974">A risk-based approach to managing cybersecurity threats to aircraft systems.</li><li data-uuid="8cb79a36-8634-4e28-aafb-45bef9f05447">Lifecycle integration, requiring threat and mitigation analysis from system concept through decommissioning.</li></ul><p>The Systems Cybersecurity Designer now enables users to:</p><ul><li data-uuid="7904beea-c260-4523-8c2e-c03a6ed59d72"><strong>Model avionics systems for cybersecurity risk assessment</strong>, incorporating assets, vulnerabilities, threat scenarios, attack paths, and mitigations in line with DO-326A guidance.</li><li data-uuid="55c036f2-ad7c-4bc8-b448-b8e3e792d8be"><strong>Perform a Security Risk Assessment (SRA)</strong> and <strong>Aircraft System Security Assessment (ASSA)</strong> using structured, iterative methodologies.</li><li data-uuid="21ae15ff-e239-48ed-ac3c-486e0b9ddfe6"><strong>Link safety and cybersecurity analyses</strong>, helping teams ensure consistency between security measures and system safety objectives.</li><li data-uuid="ade792dd-fb74-468e-ba2a-7dbcb118a021"><strong>Produce certification-ready artifacts</strong> that demonstrate compliance with DO-326A, and support alignment with DO-355 (Information Security Guidance for Continuing Airworthiness) and DO-356A (Security Methods and Considerations).</li></ul><p>By embedding DO-326A methodology into the design workflow, this update empowers aerospace engineers to reduce certification risk, identify security issues early in development, and streamline the path toward regulatory approval.</p><p style="text-align: center;"><ac:image ac:border="true" ac:height="828" ac:width="1440"><ri:attachment ri:filename="DO326A_Index.png" /></ac:image></p><h6 style="text-align: center;">DO-326A Index.</h6></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164639 space=SCD2024xR3 version=2 -->
## PAGE 00006: Asset

- page_id: `227164639`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164639/Asset
- version_number: 2
- version_date: `2025-11-18T11:04:20.359+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

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

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Asset</strong></p><p>Asset is an object that has value or contributes to value. <span style="color:var(--ds-text,#172b4d);">It has has one or more cybersecurity properties whose compromise can lead to one or</span><br /><span style="color:var(--ds-text,#172b4d);">more damage scenarios.</span></p><p><strong>Confidentiality</strong></p><p>A property that contains sensitive information <span style="color:var(--ds-text,#172b4d);">that should not be disclosed</span> to unauthorized entities.</p><p><strong>Integrity</strong></p><p>Guarding against improper information modification or destruction. It includes ensuring information non-repudiation and authenticity. Quality of being complete and unaltered.</p><p><strong>Availability</strong></p><p>Property of being accessible and usable on demand by an authorized entity.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="4ee9e7c3-f470-4cb4-8e64-0673e1b9ca71">Creating an Asset</ac:inline-comment-marker></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4e545fa2-bd88-48e6-b89a-d462301947ac"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);"> An Asset must be created in the context of an Item.</span></p></ac:rich-text-body></ac:structured-macro><p>To create an asset do one of the following:</p><ul><li>To create an Asset using an Item</li></ul><hr /><ol><li>In the Containment tree, right-click an Item and select <strong>Create Element</strong>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png" /></ac:image><br /><strong><br /><br /></strong></li><li class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Asset</strong>.<br /></span><br /><ac:image><ri:attachment ri:filename="Create Asset_Menu.png" /></ac:image><br /><br /></li><li class="auto-cursor-target">Name the created Asset in the Containment tree and press Enter. The Asset has the prefix <span><strong>AS</strong>,</span><span> </span>which denotes that the created element is an Asset; the number<span> </span><strong>1</strong><span> </span>indicates that it is the first Asset created.<br /><br /><ac:image><ri:attachment ri:filename="2 BreakingRequestAssetCreated.png" /></ac:image><br /><br /></li></ol><ul><li>To create an Asset using the Item Table</li></ul><hr /><ol><li>In the Item Table, double-click to select a Member(s) or Boundary Member(s).</li><li>Right-click and select <strong>Security&gt;Add an Asset to the Item.</strong><br /><br /><ac:image><ri:attachment ri:filename="Adding asset to the item.png" /></ac:image><br /><br /></li><li><p>Name the created Asset in the Containment tree and press Enter. The Asset has the prefix<span> <strong>AS</strong>,</span><span> </span><span>which denotes that the created element is an Asset; the number</span><span> <strong>5</strong></span><span> </span><span>indicates that it is the fifth Asset created.<br /><br /><ac:image><ri:attachment ri:filename="Containment Tree-New Asset.png" /></ac:image><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="05e3955a-d037-438f-bf78-d0bd0b609e7e"><ac:rich-text-body><ul><li>If you select an already added Member(s) or Boundary Member(s) <ac:inline-comment-marker ac:ref="5473c06e-3b6f-46ca-bf52-2fae0b99108b">to add as an underlying element</ac:inline-comment-marker>, the <strong>Add as an Asset to the Item</strong> command will be unavailable.<br /><br /><ac:image><ri:attachment ri:filename="Add asset command- unavailable.png" /></ac:image><br /><br /></li><li>The following notification message appears at the bottom right corner of the modeling tool once the asset is created. The message also provides a hyperlink to the item under which the asset is created.<br /><br /><ac:image><ri:attachment ri:filename="New Asset Added-Message.png" /></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="500928e5-b5aa-4deb-9f12-f5f3dccc4ed1"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">After creating an asset, it is beneficial to find its location in the model tree by performing one of the following:</span></p><ul><li><span style="color:var(--ds-text,#333333);">Right-click the asset, and, from the shortcut menu, choose the<span> </span></span><strong>Select in Containment Tree</strong><span style="color:var(--ds-text,#333333);"><span> </span>command.</span></li><li><span style="color:var(--ds-text,#333333);">Select the asset and press Alt+B.</span></li></ul></ac:rich-text-body></ac:structured-macro></li></ol><h3><span>Creating </span><span>an Asset from a System Diagram</span></h3><p>To create an asset from a system diagram</p><hr /><ol><li><p class="auto-cursor-target">In the system diagram, right-click an element(s) and select <strong>Security&gt;Add as an Asset.<br /><br /><ac:image><ri:attachment ri:filename="Add an Asset-Sys Diagram.png" /></ac:image><br /></strong></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6f92a462-f533-4238-b4cd-c4eee2c90a93"><ac:rich-text-body><p>Once you add <ac:inline-comment-marker ac:ref="8aa738cc-f1ab-4d55-84c7-9af64ed6f66a">a</ac:inline-comment-marker> system diagram element as an asset, a legend appears at the top right corner of the element.<br /><br /><ac:image><ri:attachment ri:filename="Asset_Legend.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>From the <strong>Select Elements</strong> dialog, select the item you want to add an asset under and click <strong>OK</strong>.<br /><br /><strong><ac:image><ri:attachment ri:filename="Select Elements-Sys Diagram.png" /></ac:image><br /></strong></li><li><p>Name the created Asset in the Containment tree and press Enter. The Asset has the suffix <strong>AS</strong>, which denotes that the created element is an Asset; the number <strong>6 </strong>indicates that it is the sixth Asset created.<br /><br /><ac:image><ri:attachment ri:filename="Containment Tree-New Asset-Sys Diagram.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="50906262-b8ec-443d-a002-779e4dfa12ad"><ac:rich-text-body><ul><li>If you select an already added system diagram element(s) to <ac:inline-comment-marker ac:ref="00f367b6-68e9-4af0-a40a-f882046a7c7d">add as an asset,</ac:inline-comment-marker> the Select Elements dialog will exclude the item to which the selected element was linked earlier.</li><li>The following notification message appears at the bottom right corner of the modeling tool once the asset is created. The message also provides a hyperlink to the item under which the asset is created.<br /><br /><ac:image ac:thumbnail="true" ac:height="105"><ri:attachment ri:filename="New Asset Added-Message-Sys Diagram.png" /></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><p><strong><span> </span></strong></p></li></ol><h3>Creating an Asset Table</h3><p>An Asset Table is automatically created while creating an Item. An Asset Table should always be linked to an Item to be compliant with the standard. You can also manually create an Asset Table.</p><p><ac:image><ri:attachment ri:filename="Automatically created Asset Table.png" /></ac:image><br /><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="17d8aa92-df27-4391-9f75-ae822300267f"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color:var(--ds-text,#172b4d);">, then an<span> </span><strong>Asset Table<span> </span></strong>already exists in the<span> </span><strong>2.1 Items &amp; Assets Definition</strong><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><span style="letter-spacing: 0.0px;">To create an Asset Table</span></p><hr /><ol><li><p>In the Containment tree, right-click <strong style="text-align: left;">Items &amp; Assets Definition</strong> and select<strong><span> </span>Create Diagram.<br /></strong></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ef7e122f-9fc2-4ffa-9dbd-87e176e3ef6a"><ac:rich-text-body><p>An Asset Table can be created under both Package and Item.</p></ac:rich-text-body></ac:structured-macro><p><strong><ac:image><ri:attachment ri:filename="Create Diagram.png" /></ac:image><br /></strong><strong><br /></strong></p></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Asset Table</strong>.</span><br /><strong><br /><ac:image><ri:attachment ri:filename="Asset Table_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword asset and then select<span> </span><strong>Asset Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="174"><ri:attachment ri:filename="Asset Table_Menu_Search.png" /></ac:image><br /><br /></strong> The Asset Table is displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="2 ContainmentTreeAssetsTable.png" /></ac:image></li></ul></li></ol><h3>Adding an Asset to the Asset Table</h3><p>To add a new Asset to the Asset Table</p><hr /><ol><li>In the Asset Table, click<span> </span><strong>Add New. </strong>A row is added in the Asset table, which shows the new Asset.<strong><br /><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png" /></ac:image><br /><br /></strong></li><li>In the newly created Asset's row and in the <strong>Name </strong>column, double-click the designated cell to name the Asset.<br /><br /><ac:image><ri:attachment ri:filename="2 AddingBreakingRequestAsset.png" /></ac:image></li></ol><h3>Adding an Underlying Element</h3><p>To add an underlying element for the asset do one of the following:</p><ul><li>To add an Underlying Element from the Asset Table</li></ul><hr /><ul><li><p>From the Containment tree, drag the Underlying Element and drop it in the designated cell of the <strong>Underlying Element </strong>column and the required Asset's row.<br /><br /><ac:image><ri:attachment ri:filename="1 DragAndDropUnderlyingElement.png" /></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1eb723ed-fb21-4e78-9c8f-fa7037b55b2f"><ac:rich-text-body><ul><li>You can also drag and drop SysML Elements (such as Connector, port, etc.) from the Containment tree to the Asset Table.</li><li>To add multiple Underlying Elements in the Asset Table, hold the Ctrl key on the keyboard to select multiple Underlying Elements from the Containment tree. Drag and drop the selected Underlying Elements into the required cell.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li><li>To add an Underlying Element from the Item Table<hr /><ol><li>In the Item Table, double-click to select a Member(s) or Boundary Member(s).</li><li>Right-click and select <strong>Security&gt;Add to an existing asset.<br /><br /><ac:image><ri:attachment ri:filename="Add to an existing asset.png" /></ac:image><br /><br /></strong></li><li>From the <strong>Select Elements</strong> dialog, select the Asset you want to add the underlying element to and click <strong>OK</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog.png" /></ac:image></li></ol></li></ul><h3>Adding an Underlying Element from a System Diagram</h3><p>To add an Underlying Element for the asset in a system diagram</p><hr /><ol><li>In the system diagram, right-click an element(s) and select <strong>Security&gt;Add to an existing Asset.<br /><br /><ac:image><ri:attachment ri:filename="Add to an existing asset-Sys Diagram.png" /></ac:image><br /><br /></strong></li><li>From the <strong>Select Elements</strong> dialog, select the Asset you want to add the element to and click <strong>OK</strong>.<strong><br /><br /><ac:image><ri:attachment ri:filename="Select Elements-add existing-Sys Diagram.png" /></ac:image></strong></li></ol><h3><ac:inline-comment-marker ac:ref="dc55f102-972a-4620-8a54-36f519bb7a76">Assigning CIA properties</ac:inline-comment-marker></h3><p>To assign CIA properties in the Asset Table</p><hr /><ul><li>  Double-click each cell<span style="color:var(--ds-text,#000000);">, namely </span><strong>Confidentiality</strong>, <strong>Integrity, </strong>and <strong>Availability </strong>in the Asset row. From the drop-down list, select the CIA properties.<br /><br /><ac:image><ri:attachment ri:filename="CIA property selection.png" /></ac:image><br /><br /><ac:image><ri:attachment ri:filename="CIA property selected.png" /></ac:image></li></ul><h3>Asset Table Example<br /><br /><ac:image><ri:attachment ri:filename="Asset Table Example.png" /></ac:image><br /><br /></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="82562ffd-ad3e-4312-b7bb-e489b1d03ed8"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a href="https://csrc.nist.gov/glossary/term/confidentiality#:~:text=Confidentiality%20covers%20data%20in%20storage%2C%20during%20processing%2C%20and,to%20the%20authors%20of%20the%20linked%20Source%20publication">NIST-Confidentiality</a>.</li><li><a class="external-link" href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf">Security and Privacy Controls for Information Systems and Organizations</a></li><li><a class="external-link" href="https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-160v1r1.pdf">Engineering Trustworthy Secure Systems</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164958 space=SCD2024xR3 version=2 -->
## PAGE 00007: Attack Path Step

- page_id: `227164958`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164958/Attack+Path+Step
- version_number: 2
- version_date: `2025-11-18T11:04:51.252+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
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
<p>An Attack Path Step is elementary action performed on the system component and could be reused in several threat scenarios.</p><h3>Creating an Attack Path Step</h3><p>To create an Attack Path Step</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<strong> Attack Paths and Feasibility Ratings</strong> and select</span> <strong>Create Element</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.jpg" /></ac:image><br /><strong style="text-align: left;"><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong><ac:inline-comment-marker ac:ref="20ef5502-d9cb-436b-a1f8-c4bc7c4853b1">Attack Path</ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="20ef5502-d9cb-436b-a1f8-c4bc7c4853b1"> </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="20ef5502-d9cb-436b-a1f8-c4bc7c4853b1">Step</ac:inline-comment-marker></strong>.</span><br /><strong><br /></strong><ac:image><ri:attachment ri:filename="Attack Path Step Menu.png" /></ac:image><br /><strong><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword <span style="color:var(--ds-text,#333333);">attack<span> and </span></span>then select<span> </span><strong><ac:inline-comment-marker ac:ref="5b8c43fd-07fe-4f56-943d-16f221f1b7c8">Attack Path Step</ac:inline-comment-marker>.<br /><br /></strong><strong><ac:image><ri:attachment ri:filename="Attack Path Step Search Menu.png" /></ac:image><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Attack Path Step in the Containment tree and press Enter.<br /><br /></span><ac:image><ri:attachment ri:filename="4 AttackPathStepCreated.png" /></ac:image></li></ol><h3><span style="color:var(--ds-text,#333333);"> </span></h3>
````

<!--NOMAGIC_PAGE id=227164921 space=SCD2024xR3 version=2 -->
## PAGE 00008: Attack Potential Based Attack Path

- page_id: `227164921`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164921/Attack+Potential+Based+Attack+Path
- version_number: 2
- version_date: `2025-11-18T11:04:45.950+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
- labels: []

### NORMALIZED CONTENT

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

Adding a new or existing Attack Potential Based Attack Path to the Attack Potential Based Attack Path Table is the same as adding a new or existing Manual Attack Path to the Manual Attack Path Table. To learn more about adding a Manual Attack Path to the Manual Attack Path Table, refer to [CONFLUENCE_PAGE title='Manual Attack Path' space=''].

##### Adding Attack Path Steps

Attack path steps in an Attack Based Potential Attack Path table are added in the same as they are added in a Simple Attack Path table. To learn more about adding attack path steps in a Simple Attack Path table, refer to [CONFLUENCE_PAGE title='Manual Attack Path' space=''].

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>Attack Potential based method is supported by the ISO/IEC 18045 standard.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating an Attack Potential Based Attack Path</h3><p>To create an <span style="color:var(--ds-text,#333333);">Attack Potential Based Attack Path </span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<span> </span><strong>Attack Paths and Feasibility Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Attack Potential Based Attack Path</strong>.<br /><br /></span><strong><ac:image><ri:attachment ri:filename="AP_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong>Attack Potential Based Attack Path</strong></span><strong>.<br /><br /><ac:image><ri:attachment ri:filename="AP_Menu_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Attack Potential Based Attack Path in the Containment tree and press Enter. The Attack Potential Based Attack Path has the prefix <span><strong>AP</strong>, </span>which denotes that the created element <ac:inline-comment-marker ac:ref="e2ccbbe1-1d06-4ff2-b453-088e481a1261">is an <span style="color:var(--ds-text,#172b4d);">an Attack Path (Manual or Potential-Based)</span></ac:inline-comment-marker>; the number<span> </span><strong style="text-align: left;">1</strong> indicates that it is the <ac:inline-comment-marker ac:ref="04adb341-47be-4092-8e66-59b49a92c088">first <span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">Attack Path (Manual or Potential-Based)</span></span></ac:inline-comment-marker> created.<br /><br /><strong><ac:image><ri:attachment ri:filename="AP_Created_Containment Tree.png" /></ac:image></strong><br /></span></li></ol><h3>Creating an Attack Potential Based Attack Path Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="fa731bd7-f3e3-4691-8670-2f2ab9a94c52"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color:var(--ds-text,#172b4d);">, then a<span> <span style="color:var(--ds-text,#333333);"><strong>Attack Potential Based Attack Path </strong></span></span>table<span> </span>already exists in the<span> <strong>1.3 Attack Paths and Feasibility Ratings</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create an<span> Attack Potential Based Attack Path </span>Table</p><hr /><ol><li><ac:inline-comment-marker ac:ref="d3d2d78f-ade4-4c8d-862a-f017c198a2ea">In the Containment tree</ac:inline-comment-marker>, right-click<span> <span style="color:var(--ds-text,#333333);"><strong>Attack Paths and Feasibility Ratings</strong></span></span><span style="color:var(--ds-text,#333333);"> </span>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png" /></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Attack Potential Based Attack Path Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="AP_Table_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong>Attack Potential Based Attack Path </strong></span><strong>Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="196"><ri:attachment ri:filename="AP_Table_Menu_Search.png" /></ac:image><br /><br /></strong>The Attack Potential Based Attack Path Table is displayed in the diagram pane of the modeling tool.<br /><br /><strong><ac:image><ri:attachment ri:filename="AP_Table_Created.png" /></ac:image></strong></li></ul></li></ol><h3>Adding an Attack Potential Based Attack Path to the Attack Potential Based Attack Path Table</h3><p>Adding a new or existing Attack Potential Based Attack Path to the Attack Potential Based Attack Path Table is the same as adding a new or existing Manual Attack Path to the Manual Attack Path Table. To learn more about adding a Manual <ac:inline-comment-marker ac:ref="093c246e-d7ef-483e-a8a4-364cff6ae8f1">Attack Path</ac:inline-comment-marker> to the Manual Attack Path Table, refer to <ac:link><ri:page ri:content-title="Manual Attack Path" /></ac:link>.</p><h3>Adding Attack Path Steps</h3><p>Attack path steps in an Attack Based Potential Attack Path table are added in the same as they are added in a Simple Attack Path table. To learn more about adding attack path steps in a Simple Attack Path table, refer to <ac:link><ri:page ri:content-title="Manual Attack Path" /></ac:link>.</p><h3>Rating the Potential Attack core parameters</h3><p>To rate the Potential Attack core parameters</p><hr /><ul><li><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="54784e0f-7c81-4b6b-a155-6e73ca26b34d">Double-click each cell's</ac:inline-comment-marker> column</span><span style="color:var(--ds-text,#000000);"><span> namely <strong>Elapsed Time, Specialist Expertise, Knowledge of Item/Component, Window of Opportunity, </strong>and <strong>Equipment</strong> in the Attack Based Potential Attack Path's </span></span><span style="color:var(--ds-text,#333333);">row and select the required option from the drop-down list.<br /><br /><ac:image><ri:attachment ri:filename="Rating the Potential Attack core parameters.png" /></ac:image><br /></span></li></ul><p><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8bde7915-02a8-4097-a418-ea8eff9333d1"><ac:rich-text-body><p>The Attack Feasibility Rating is calculated with help of core parameters viz. <span style="color:var(--ds-text,#000000);">Elapsed Time, Specialist Expertise, Knowledge of Item/Component, Window of Opportunity, and Equipment. Each parameter has different grading system which has a numerical value assigned to it. These numerical values are based on the ISO/IEC 18045 standard. </span></p><p><span style="color:var(--ds-text,#000000);">The following table shows the assigned numerical values to each parameter.<br /><br /><ac:image><ri:attachment ri:filename="Attack Feasibility Rating _Parameters_Table.png" /></ac:image><br /><br /></span></p><p><span style="color:var(--ds-text,#000000);">The numerical values are added together to calculate the  Attack Feasibility Rating. Following is the formula used to calculate the Attack Feasibility Rating.</span></p><ul><li><span>Attack Feasibility Rating = Elapsed Time + <span style="color:var(--ds-text,#000000);">Specialist Expertise</span>+ <span style="color:var(--ds-text,#000000);">Knowledge of Item/Component</span>+ <span style="color:var(--ds-text,#000000);">Window of Opportunity</span>+ <span style="color:var(--ds-text,#000000);">Equipment</span></span></li></ul><p>The <ac:inline-comment-marker ac:ref="17f1a584-e363-405b-aea7-2dbc939069ac">following table</ac:inline-comment-marker> shows the numerical values assigned to the Attack Feasibility Rating.</p><p><ac:image ac:thumbnail="true" ac:height="101"><ri:attachment ri:filename="Attack Feasibility Rating values.png" /></ac:image></p></ac:rich-text-body></ac:structured-macro><p><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227165078 space=SCD2024xR3 version=2 -->
## PAGE 00009: Collaborative modeling

- page_id: `227165078`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227165078/Collaborative+modeling
- version_number: 2
- version_date: `2025-05-05T08:30:15.336+02:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Collaborative modeling' space='MD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="75de1aab-6655-4037-a71b-7e37f9a3b76b"><ac:parameter ac:name=""><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Collaborative modeling" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227164970 space=SCD2024xR3 version=3 -->
## PAGE 00010: Cyber Security Attack Graph

- page_id: `227164970`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164970/Cyber+Security+Attack+Graph
- version_number: 3
- version_date: `2025-11-18T11:04:56.907+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
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
  - Click the attack path step to open the [CONFLUENCE_PAGE title='Smart manipulator toolbar' space='MD2024xR3'] , select the Causality relationship, and create a relationship. To learn more about creating relationships, refer to [CONFLUENCE_PAGE title='Creating a relationship' space='MD2024xR3'] [ATTACHMENT filename='Causality Relation_Smart Manipulator.png']
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
<h3><ac:inline-comment-marker ac:ref="da1d3de1-7fe0-4f45-b5ba-f59f1e700918">Creating a Cyber Security Attack Graph</ac:inline-comment-marker> Diagram</h3><p>To create a<span> Cyber Security Attack Graph Diagram</span></p><hr /><ol><li>In the Containment tree, right-click<span> </span>any required package<span style="color:var(--ds-text,#333333);"> </span>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png" /></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand<span> </span><strong>ISO 21434<span> </span></strong>and select <strong>Cyber</strong><span><strong> Security Attack Graph Diagram</strong></span>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Cyber Security Attack Graph Diagram_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword graph and then select<span> <strong>Cyber Security Attack Graph Diagram</strong></span><strong>.<br /><br /><ac:image><ri:attachment ri:filename="Cyber Security Attack Graph Diagram_Search.png" /></ac:image><br /><br /></strong>The <span>Cyber Security Attack Graph Diagram<strong> </strong></span>is displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Cyber Security Attack Graph Diagram.png" /></ac:image></li></ul></li></ol><h3>Adding an Attack Path Step in the Attack Graph</h3><p>To add a new Attack Path Step in the Attack Graph</p><hr /><ul><li>From the diagram palette, select <strong>Attack Path Step</strong> and c<span style="color:var(--ds-text,#172b4d);">lick on the diagram pane. Name the created Attack Path Step.<br /><br /><ac:image><ri:attachment ri:filename="Attack Path step_Diagram Pallete.png" /></ac:image><br /></span></li></ul><p><br /></p><p><span style="color:var(--ds-text,#172b4d);">To add an existing Attack Path Step, CWE Element, or any Situation in the Attack Graph</span></p><hr /><ul><li><ac:inline-comment-marker ac:ref="975d17d3-ec2c-4d2d-8111-7bee0c82aa15">Drag the required <span style="color:var(--ds-text,#172b4d);">Attack Path Step, CWE Element, or any Situation</span></ac:inline-comment-marker> from the Containment tree and drop it in the diagram pane.<br /><br /><ac:image><ri:attachment ri:filename="Attack Steps_Drag and Drop.png" /></ac:image></li></ul><h3>Creating a Causality Relation between Attack Path Steps</h3><p>To create a Causality Relation between Attack Path Steps</p><hr /><ul><li>Do one of the following:<br /><br /><ul><li>Click the attack path step to open the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Smart manipulator toolbar" /><ac:plain-text-link-body><![CDATA[Smart Manipulator toolbar]]></ac:plain-text-link-body></ac:link>, select the Causality relationship, and create a relationship. To learn more about creating relationships, refer to <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating a relationship" /></ac:link><br /><br /><ac:image><ri:attachment ri:filename="Causality Relation_Smart Manipulator.png" /></ac:image><br /><br /></li><li>From the diagram palette, select the Causality command and then select the <ac:inline-comment-marker ac:ref="10887742-853d-4e1c-96f3-3f31fdf9f597">required attack path steps</ac:inline-comment-marker>.<br /><br /><ac:image><ri:attachment ri:filename="Causality_Diagram Palette.png" /></ac:image></li></ul></li></ul><p>An arrow icon is displayed in the graph which denotes that causality relation is created.<span style="color:var(--ds-text,#172b4d);"><br /><br /><ac:image><ri:attachment ri:filename="Causality Relation created.png" /></ac:image><br /></span></p><h3>Generating an Attack Path from the Attack Graph</h3><p>To generate an Attack Path from the Attack Graph</p><hr /><ol><li><p class="auto-cursor-target">In the attack graph, select the two required attack steps by holding down the Shift key. The selected attack paths are considered as two ends of an attack path.</p></li><li>Right-click and select the Generate Attack Paths command.<br /><br /><ac:image><ri:attachment ri:filename="Generate Attack Paths.png" /></ac:image><br /><br /></li><li><p class="auto-cursor-target">In the Select Attack Paths dialog, select the required attack path from the list of available attack paths and click OK.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="d0907153-873c-43f4-9f47-b725a1f54485"><ac:rich-text-body><p>Loops present in the attack graph are eliminated while calculating the attack path(s).</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="Select Attack Path_Dialog.png" /></ac:image><br /><br /></p></li><li><p class="auto-cursor-target">In the Select Destination Package dialog, select the package to save the generated attack path(s).<br /><br /><ac:image><ri:attachment ri:filename="Select Destination Package_Dialog.png" /></ac:image><br /><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="4f1e46a7-c6bb-4d05-a42d-1b4a4967644a"><ac:rich-text-body><ul><li>After generation of an Attack Path, if Attack Graph changes in such a way that the path is not valid anymore, a validation rule is triggered and an error occurs. You can fix the error from the Attack Path, but in such case, the path will not be linked to the graph anymore. Also, no further errors will be reported on that Attack Path if the graph is further modified.</li><li>The generated attack path(s) are manual attack paths.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol>
````

<!--NOMAGIC_PAGE id=227164686 space=SCD2024xR3 version=3 -->
## PAGE 00011: Damage scenario

- page_id: `227164686`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164686/Damage+scenario
- version_number: 3
- version_date: `2025-11-18T11:04:23.868+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Damage Scenario</strong></p><p>Adverse consequence involving a vehicle or vehicle function and affecting a road user.</p><p><strong>Effect</strong></p><p>Allows you to define and manage system and vehicle level effects that can result in harm.</p><p><strong>Failure</strong></p><p>Termination of an intended behavior of an element or an item due to a fault manifestation.</p><p><strong>Operational Situation </strong></p><p>A scenario that can occur during a vehicle's life.</p><p><strong>Impact category</strong></p><p>Impact rating is done for four categories: Safety, Financial, Operational, and Privacy.  The assessment should be done according to the definition given in ISO/SAE 21434:2021(annex F).</p><p><strong><ac:inline-comment-marker ac:ref="f9331154-8121-4939-80cf-3a54ebb5a194">Impact scale</ac:inline-comment-marker></strong></p><p>By default, the plugin adopts the scale provided in the ISO/SAE 21434:2021 <ac:inline-comment-marker ac:ref="f55a94f1-8539-4dda-8a8d-eee0cacf6d5e">standard: <span style="color:var(--ds-text,#172b4d);">Negligible / Moderate / Major or Severe.</span></ac:inline-comment-marker></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Damage Scenario</h3><p>To create a Damage Scenario</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click <strong>Damage Scenario and Impact Ratings</strong> and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Damage</strong> <strong>Scenario</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="3 DirectlySelectDamageScenario.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword damage and then select<span> </span><strong>Damage Scenario.<br /><br /><ac:image><ri:attachment ri:filename="2 WriteDamage.png" /></ac:image><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Damage Scenario in the Containment tree and press Enter. The Damage Scenario has the prefix <span><strong>D</strong></span><strong>S</strong> which denotes the created element is a Damage Scenario; the number <strong style="text-align: left;">1</strong> indicates that it is the first Damage Scenario created.<br /><br /><ac:image><ri:attachment ri:filename="4 DamageScenarioCreated.png" /></ac:image><br /></span></li></ol><h3><span style="color:var(--ds-text,#333333);">Creating a Damage Scenarios Table<br /></span></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="d04b1ff4-bbca-47f1-9e94-886674d33795"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color:var(--ds-text,#172b4d);">, then an<span> </span><strong>Damage Scenarios Table<span> </span></strong>already exists in the<span> <strong>1.1 Damage Scenarios and Impact Ratings</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create a <span style="color:var(--ds-text,#333333);">Damage Scenario </span>Table</p><hr /><ol><li><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">In the Containment tree, right-click </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">Damage Scenario and Impact Ratings</ac:inline-comment-marker></strong><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">and select</ac:inline-comment-marker><strong><span><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="2ec52fd6-e367-469e-a416-fe772b20ab13">Create Diagram.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Create Diagram_Command.png" /></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Damage Scenario Table</strong>.</span><strong><br /><br /><ac:image><ri:attachment ri:filename="Damage Scenario Table Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword damage and then select<span> </span><strong>Damage Scenarios Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="198"><ri:attachment ri:filename="Damage Scenario Table_Seach.png" /></ac:image><br /><br /></strong>The Damage Scenarios Table is displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="1 ContainmentTreeDamageScenariosTable.png" /></ac:image></li></ul></li></ol><h3>Adding a Damage Scenario to the Damage Scenarios Table</h3><p>To add a new Damage Scenario to the Damage Scenarios Table</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Damage Scenario Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New. </strong><span style="color:var(--ds-text,#333333);">A row is added in the Damage Scenarios Table, which shows the new Damage Scenario.</span><br /><strong style="text-align: left;"><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">In the newly created Damage Scenario's row and the <strong>Name </strong>column, double-click the designated cell to name the Damage Scenario.<br /><br /><ac:image ac:height="210"><ri:attachment ri:filename="2 AfterAddingDamageScenario.png" /></ac:image><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color:var(--ds-text,#333333);">To add an existing Damage Scenario to the Damage Scenarios Table</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Damage Scenarios Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="3 ClickAddExisting.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Damage Scenario </strong>dialog, select the required Damage Scenario. A row is added to the Damage Scenarios Table, which shows the existing Damage Scenario. <br /><br /><ac:image><ri:attachment ri:filename="4 SelectExistingDamageScenario_v2.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">In the existing Damage Scenario's row and the <strong>Name </strong>column, double-click the designated cell to rename the Damage Scenario.<br /><br /><ac:image><ri:attachment ri:filename="5 AfterAddingExistingDamageScenario.png" /></ac:image><br style="text-align: left;" /></span></li></ol><h3>Adding a Failure</h3><p>To add a Failure to the Damage Scenarios Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Failure </strong>column and the required Damage Scenario's row and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickThreeDots_Failure.png" /></ac:image><br /><br /></li><li>From the <strong>Select Class</strong><strong> </strong>dialog, select Failure.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectFailureWindow_v2.png" /></ac:image><br /><br />The Failure is shown in the Damage Scenarios Table.<br /><br /><ac:image ac:height="223"><ri:attachment ri:filename="3 AfterAddingFailure.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2a741443-4456-43c3-9b41-ecd0582595e3"><ac:rich-text-body><p>You can also drag and drop the Failure modes from the Containment tree to the Damage Scenarios Table.</p></ac:rich-text-body></ac:structured-macro><p><br /></p><h3>Adding an Effect</h3><p>To add an Effect in the Damage Scenarios Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Effect </strong>column and the required Damage Scenario's row and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickThreeDots_Effect.png" /></ac:image><br /><br /></li><li>From the <strong>Select Class</strong><strong> </strong>dialog, select Effect.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectEffectWindow_v2.png" /></ac:image><br /><br />The Effect is shown in the Damage Scenarios Table.<br /><br /><ac:image><ri:attachment ri:filename="3 AfterAddingEffect.png" /></ac:image><br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="71709c22-7e35-46d3-b43f-89e912b6a30b"><ac:rich-text-body><p>You can also drag and drop the Effects such as Vehicle Level Effects and System Level Effects from the Containment tree to the Damage Scenarios Table.</p></ac:rich-text-body></ac:structured-macro><h3>Adding an Operational Situation</h3><p>To add an Operational Situation in the Damage Scenarios Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Operational Situation </strong>column and the required Damage Scenario's row and click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image>.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickThreeDots_Operation Situation.png" /></ac:image><br /><br /></li><li>From the <strong>Select Class </strong>dialog, select Operational Situation.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectOpSituation_v2.png" /></ac:image><br /><br />The Operational Situation is added in the Damage Scenarios Table.<br /><br /><ac:image><ri:attachment ri:filename="3 AfterAddingOpSituation.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b5b6c59c-57af-4ec2-8384-d1a99f663c5d"><ac:rich-text-body><p>You can also drag and drop the Operation Situations from the Containment tree to the Damage Scenarios Table.</p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="516ed4d0-1fc9-40ad-948c-245338bcaeb1">Rating SFOP Impact</ac:inline-comment-marker></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c30dc5fb-c3ec-4666-a078-efae78e20973"><ac:rich-text-body><ul><li>The Damage Scenario cannot be rated if there is no Effect associated to it.</li><li>All the Damage Scenarios sharing the same Effect get the same impact ratings. In such case, if you update any impact rating(s) for one Damage Scenario, the impact rating(s) for other Damage Scenarios are updated.</li></ul></ac:rich-text-body></ac:structured-macro><br /><p><span style="letter-spacing: 0.0px;">To rate the SFOP Impact</span></p><hr /><ul><li><span style="color:var(--ds-text,#333333);">  Double-click each cell,<span> </span></span><span style="color:var(--ds-text,#000000);">namely<span> <strong>Safety Impact</strong>, <strong>Financial Impact</strong>, <strong>Operational Impact</strong>, and <strong>Privacy Impact </strong>in the Damage Scenario </span></span><span style="color:var(--ds-text,#333333);">row. From the drop-down list, select the impact rating.<br /><br /><ac:image><ri:attachment ri:filename="Impact Rating selection.png" /></ac:image><br />The Impact rating is done in the Damage Scenarios Table.<br /><br /><ac:image><ri:attachment ri:filename="Impact Rating selected.png" /></ac:image><br /></span></li></ul><p><br /></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="2c0ad3e4-67f2-44fa-ba80-78757c382bd7"><ac:rich-text-body><p>The plugin behavior when you use the Effect element from the used project in your local project:</p><ul><li>When you update the SFOP Impact ratings of the damage scenario, a cloned Effect element is created in your local project and is visible in the Containment tree. The following notification message is displayed with the cloned Effect element link at the bottom right corner of the modeling tool.<br /><br /><ac:image ac:height="121"><ri:attachment ri:filename="Cloned_Notification.png" /></ac:image></li></ul><p>The plugin behavior when you use the Effect element from the used project in the TWC server project:</p><ul><li>When you update the SFOP Impact ratings of the damage scenario, a cloned Effect element is created in your server project and is visible in the Containment tree. The following notification message is displayed with the cloned Effect element link at the bottom right corner of the modeling tool.<br /><br /><ac:image ac:height="121"><ri:attachment ri:filename="Cloned_Notification.png" /></ac:image></li></ul><p>The plugin behavior when you use the Effect element from your own TWC server project:</p><ul><li>When you update the SFOP ratings of the damage scenario and the Effect element is in a read-only state, the Effect element gets locked automatically by you.</li><li>When you update the SFOP ratings of the damage scenario and the Effect element is locked by another user, the following notification is displayed with the locked Effect element link at the bottom right corner of the modeling tool.<br /><br /><ac:image ac:height="154"><ri:attachment ri:filename="Locked_Notification.PNG" /></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target"><ac:inline-comment-marker ac:ref="7eba9344-79dc-4ea0-a9f1-d01cabdc6bf2">Damage Scenarios Table Example</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Damage Scenarios Example.png" /></ac:image></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b327f344-eb80-4f95-8e82-df85cdda6744"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a class="external-link" href="https://www.iso.org/obp/ui">ISO 26262-1:2018 Road vehicles-Functional safety</a></li><li><a href="https://docs.nomagic.com/display/CSRA2024xR3/Tables+and+diagrams">Tables and diagrams</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164764 space=SCD2024xR3 version=2 -->
## PAGE 00012: Effect

- page_id: `227164764`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164764/Effect
- version_number: 2
- version_date: `2025-11-18T11:04:30.826+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Damage scenario
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
<h3><ac:inline-comment-marker ac:ref="c0001038-dc02-4862-8b55-0ea3f529a632">Creating an Effect</ac:inline-comment-marker></h3><p>To create an Effect</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<span> <strong>Damage Scenario </strong></span><strong>and Impact Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Vehicle Level Effect </strong>or <strong>System Level Effect</strong>.<br /></span><strong><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Effect.jpg" /></ac:image></strong><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword effect and then select<span> </span><strong>Vehicle Level Effect<span> </span></strong>or <strong><span>System Level Effect.</span></strong><strong><br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Effect_Search.jpg" /></ac:image></strong><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Effect in the Containment tree and press Enter.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="4 EffectCreated.png" /></ac:image></strong></span></li></ol><h3>Adding Effects to the Effects Table</h3><p>Using the Effects Table you can only add nested Effects.</p><p>To add an Effects</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Effects Table, select an Effect and then click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Nested.<span> </span></strong><span style="color:var(--ds-text,#333333);">A row is added in the Effects Table, which shows the nested Effect.<br /><br /><ac:image><ri:attachment ri:filename="Add Nested_Effect.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">In the newly created Effect's row and the <strong style="text-align: left;">Name<span> </span></strong>column, double-click the designated cell to name the Effect.<br style="text-align: left;" /><br /><ac:image><ri:attachment ri:filename="Nested Effect added.png" /></ac:image><br /></span></li></ol><h3>Adding Relevant Element in the Effects Table</h3><p><span style="color:var(--ds-text,#172b4d);">To add Relevant To</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Double-click the designated cell in the<span> </span><strong>Relevant Element </strong></span><span style="color:var(--ds-text,#333333);">column and the required Effect's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.<br /><br /><ac:image><ri:attachment ri:filename="Relevant To_Three Dot_Effect.png" /></ac:image><br /><br /></span></span></li><li><span style="color:var(--ds-text,#333333);"><span>From the <strong style="text-align: left;">Select Elements</strong><strong style="text-align: left;"> </strong>dialog, select Relevant Element.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog_Effect.png" /></ac:image><br /><br style="text-align: left;" /></span></span><span style="color:var(--ds-text,#333333);"><span>The Relevant Element is added to the Effects Table.<br /><br /><ac:image><ri:attachment ri:filename="Relevant To added_Effect.png" /></ac:image><br /></span></span></li></ol>
````

<!--NOMAGIC_PAGE id=227164740 space=SCD2024xR3 version=2 -->
## PAGE 00013: Failure Mode

- page_id: `227164740`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164740/Failure+Mode
- version_number: 2
- version_date: `2025-11-18T11:04:26.685+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Damage scenario
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
<h3>Creating a Failure Mode</h3><p>To create a Failure Mode</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<span> <strong>Damage Scenario </strong></span><strong>and Impact Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Failure Mode</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Failure Mode.jpg" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword failure and then select<span> </span><strong>Failure Mode.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode_Search.jpg" /></ac:image><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Failure Mode in the Containment tree and press Enter.<br /><br /><ac:image><ri:attachment ri:filename="4 FailureModeCreated.png" /></ac:image><br /></span></li></ol><h3>Adding Failure Mode to the Failure Modes Table</h3><p>To add a new Failure Mode to the Failure Modes Table</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Failure Modes Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New.<span> </span></strong><span style="color:var(--ds-text,#333333);">A row is added in the Failure Modes Table, which shows the new Failure Mode.</span><br /><strong style="text-align: left;"><br /><ac:image><ri:attachment ri:filename="Add New_Failure Mode.png" /></ac:image><br /><br /></strong></li><li>Select between the <strong>FailureMode</strong> and <strong>MalfucntioningBehavior</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Select the failure mode or Malfunction Behavior.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">In the newly created Failure Mode's row and the<span> </span><strong>Name<span> </span></strong>column, double-click the designated cell to name the Failure Mode.<br /><br /><ac:image><ri:attachment ri:filename="Failure Mode added.png" /></ac:image><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color:var(--ds-text,#333333);">To add an existing Failure Mode to the Failure Modes Table</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Failure Modes Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="Add Existing_Failure Mode.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">From the<span> </span><strong>Select Failure Mode </strong>dialog, select the required Failure Mode. A row is added to the Failure Modes Table, which shows the existing Failure Mode.<br /><br /><ac:image><ri:attachment ri:filename="Select Failure Mode dialog.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">In the existing Failure Mode's row and the<span> </span><strong>Name<span> </span></strong>column, double-click the designated cell to rename the Failure Mode.<br /><br /><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="Failure Mode added.png" /></ac:image></span><br /></span></li></ol><h3>Adding Relevant To in the Failure Modes Table</h3><p>To add Relevant To</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Double-click the designated cell in the <strong>Relevant To</strong> </span><span style="color:var(--ds-text,#333333);">column and the required Failure Mode's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Relevant To_Three Dot.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From<span> </span>the<span> </span><strong>Select Elements</strong><strong><span> </span></strong>dialog, select Relevant To.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements dialog.png" /></ac:image><br /></span><span style="color:var(--ds-text,#333333);"><br />The Relevant To is added to the Failure Modes Table.<br /><br /><ac:image><ri:attachment ri:filename="Relevant To added.png" /></ac:image><br /></span></li></ol>
````

<!--NOMAGIC_PAGE id=227165030 space=SCD2024xR3 version=2 -->
## PAGE 00014: Functional Cybersecurity Concept

- page_id: `227165030`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227165030/Functional+Cybersecurity+Concept
- version_number: 2
- version_date: `2025-05-05T08:30:15.152+02:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
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

##### Cybersecurity Assurance Level

TheCybersecurity Assurance Level (CAL) classification scheme is used to specify a set of assurance requirements for components/items in terms of levels of rigor. These levels of rigor provide confidence that assets of an item are developed with adequate protection. A CAL value is specified on a Cybersecurity Goal and is inherited by all derived requirements. This value specifies the amount of rigor required to address relevant threat scenarios during product development. By default, there are four CAL levels CAL1 to CAL4 representing Low to High Cybersecurity assurance.

To assign a Cybersecurity Assurance Level

1. In the Containment tree, double- click the Cybersecurity Assurance dependency matrix. [ATTACHMENT filename='CAL_Containment tree.png']
2. In the Cybersecurity Assurance dependency matrix, double click the designated cell in the desired cybersecurity goal's row and the CAL value's column. You can modify the dependency matrix based on your requirements. To learn more about modifying dependency matrix, refer to[CONFLUENCE_PAGE title='Using Dependency Matrix' space='MD2024xR3']. [ATTACHMENT filename='CAL matrix.png']

You can also create custom CAL values and assign the custom created CAL value to any cybersecurity goal.

To create custom CAL value and assign it to the cybersecurity goal

1. In the Containment tree, right-click the desired package , select Create Element and select Class.
2. Assign CybersecurityAssuraneLevel [Class] stereotype to the created element. [ATTACHMENT filename='Assiging stereotype.png']
3. Assign AbstractCybersecurityAssuranceLevel as Base Classifier to the created element. [ATTACHMENT filename='Applying Base Classifier.png']
4. Drag and drop the package containing the custom CAL value onto the column scope. [ATTACHMENT filename='Column scope change.png']
5. Double-click the designated cell in the cybersecurity goal's row and custom CAL value's column.

##### Functional Cybersecurity Concept Table

The Functional Cybersecurity Concept Table provides an overview of goals & requirements to be implemented to secure assets.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><ac:structured-macro ac:name="toc" ac:schema-version="1" ac:macro-id="fa760972-d553-481d-9841-f7390fbfff7f"><ac:parameter ac:name="minLevel">3</ac:parameter></ac:structured-macro></p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><p>A Cybersecurity Requirement Diagram displays cybersecurity goals, cybersecurity requirements, and their relations. The main purpose of this diagram is to create requirements that cover the goals defined in TARA. </p><h3>Deriving Cybersecurity Requirements</h3><p>Cybersecurity Requirements are derived from Cybersecurity Goals defined in a TARA table. You can use the Cybersecurity  Requirement Diagram to derive four types of Cybersecurity Requirements: Functional, Technical, Software, and Hardware.</p><p>To derive a Cybersecurity Requirement</p><hr /><ol><li><span style="color: rgb(62,63,64);">From the Index page, open the Functional Cybersecurity Concept.</span></li><li>Find the Cybersecurity Goal you want to derive the C<span style="color: rgb(62,63,64);">ybersecurity </span>Requirement from and drag it to the diagram.</li><li>Create the Cybersecurity Requirement you want to derive by clicking it in the diagram palette and clicking an empty space on the diagram pane.</li><li>Name the created C<span style="color: rgb(62,63,64);">ybersecurity </span>Requirement and write the required text.</li><li>Create a derived relationship from the C<span style="color: rgb(62,63,64);">ybersecurity </span>Requirement to the Safety Goal as displayed below.<br /><br /><ac:image><ri:attachment ri:filename="Cybersecurity GoalsAndRequirements.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></li></ol><h3>Creating a Cybersecurity Goal</h3><p>To create a Cybersecurity Goal</p><hr /><ol><li>In the Containment tree, right-click <strong>Functional Cybersecurity Concept </strong>and select<strong><span> </span>Create Element.</strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Create Element.jpg"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">Do one of the following:<ul><li class="auto-cursor-target"><span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="8e2d61f6-324f-4d14-a611-205ffa444e5b">In the dialog</ac:inline-comment-marker>, expand <strong>ISO</strong> <strong>21434</strong> and select <strong>Cybersecurity Goal</strong>.</span><br /><strong><br /></strong><ac:image><ri:attachment ri:filename="Cybersecurity Goal Menu.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li><li class="auto-cursor-target">In the search tab, type the keyword goals and then select<span> <strong>Cybersecurity Goal</strong></span><strong>.<br /></strong><br /><strong><ac:image><ri:attachment ri:filename="Cybersecurity Goal_Search.jpg"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></strong><br /><br /></li></ul></li><li class="auto-cursor-target">Name the created Cybersecurity Goal in the Containment tree. The cybersecurity goal has the prefix <strong>CG, </strong>which denotes that the created element is c<span>ybersecurity goals; </span>the number <strong>1</strong> indicates that it is the first c<span>ybersecurity goal<strong> </strong></span>created.<br /><br /><strong><ac:image><ri:attachment ri:filename="Cybersecurity Goal_Created.jpg"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></strong></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="095dae29-e483-4570-8157-e73c2f75ecf9"><ac:rich-text-body><p>You can also create a Cybersecurity Goal in the Cybersecurity Goal Table or by using the diagram panel.</p></ac:rich-text-body></ac:structured-macro><h3>Creating a Cybersecurity Requirement</h3><p>To create a Cybersecurity Requirement</p><hr /><ol><li>In the Containment tree, right-click <strong>Functional Cybersecurity Concept </strong>and select<strong><span> </span>Create Element.</strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Create Element.jpg"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></strong></li><li class="auto-cursor-target">Do one of the following:<ul><li><p>In the dialog, expand <strong>ISO 21434</strong>. From the drop-down list, choose one of the following:</p><ul><li>Functional Cybersecurity Requirement</li><li>Hardware Cybersecurity Requirement </li><li>Software Cybersecurity Requirement</li><li>Technical Cybersecurity Requirement<strong><br /><br /></strong><ac:image><ri:attachment ri:filename="Cybersecurity Requirement_Menu.jpg"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li></ul></li><li class="auto-cursor-target">In the search tab, type the keyword goals and then select<span> the required Cybersecurity Requirement</span><strong>.<br /><br /></strong><ac:image><ri:attachment ri:filename="Cybersecurity Requirement_Search.jpg"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li></ul></li><li class="auto-cursor-target"><p class="auto-cursor-target">Name the created Cybersecurity Requirement in the Containment tree.<br /><br /><ac:image><ri:attachment ri:filename="Cybersecurity Requirement_Created.jpg"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="27d4e3c8-4ffa-4234-b9c7-5e53ac4dbe8c"><ac:rich-text-body><p>You can also create a cybersecurity requirement in the cybersecurity requirement tables.</p></ac:rich-text-body></ac:structured-macro><h3>Cybersecurity Assurance Level</h3><p><span style="color: rgb(23,43,77);">The </span><span style="letter-spacing: 0.0px;">Cybersecurity Assurance Level (</span><span style="letter-spacing: 0.0px;">CAL) classification scheme is used to specify a set of assurance requirements for components/items in terms of levels of rigor.  These levels of rigor provide confidence that assets of an item are developed with adequate protection. A CAL value is specified on a Cybersecurity Goal and is inherited by all derived requirements.  This value specifies the amount of rigor required to address relevant threat scenarios during product development. B</span><span style="letter-spacing: 0.0px;">y default, there are four CAL levels CAL1 to CAL4 representing Low to High Cybersecurity assurance.</span></p><p>To assign a <span>Cybersecurity Assurance Level</span></p><hr /><ol><li>In the Containment tree, double- click the <strong>Cybersecurity Assurance </strong>dependency matrix.<br /><br /><ac:image><ri:attachment ri:filename="CAL_Containment tree.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>In the <strong>Cybersecurity Assurance </strong>dependency matrix, double click the designated cell in the desired cybersecurity goal's row and the CAL value's column.<br /><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="bc7d47e0-09f2-4c10-8cac-42a62176bc18"><ac:rich-text-body><p><span style="color: rgb(23,43,77);">You can modify the dependency matrix based on your requirements. To learn more about modifying dependency matrix, refer to </span><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Using Dependency Matrix" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro><br /><ac:image><ri:attachment ri:filename="CAL matrix.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></li></ol><p><br /></p><p>You can also create custom CAL values and assign the custom created CAL value to any cybersecurity goal.</p><p>To create custom CAL value and assign it to the cybersecurity goal</p><hr /><ol><li>In the Containment tree, right-click the desired package<strong>, </strong>select<strong><span> </span>Create Element</strong> and select <strong>Class.</strong></li><li>Assign <strong>CybersecurityAssuraneLevel [Class]</strong> stereotype to the created element.<br /><br /><ac:image><ri:attachment ri:filename="Assiging stereotype.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>Assign <strong>AbstractCybersecurityAssuranceLevel </strong>as Base Classifier to the created element.<br /><br /><ac:image><ri:attachment ri:filename="Applying Base Classifier.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>Drag and drop the package containing the custom CAL value onto the column scope.<br /><br /><ac:image><ri:attachment ri:filename="Column scope change.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>Double-click the designated cell in the cybersecurity goal's row and custom CAL value's column.</li></ol><h3>Functional Cybersecurity Concept Table</h3><p>The Functional Cybersecurity Concept Table provides an overview of goals &amp; requirements to be implemented to secure assets.</p><p><ac:image><ri:attachment ri:filename="Functional cybersecurity concept table.png"><ri:page ri:content-title="Functional Cybersecurity Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227165079 space=SCD2024xR3 version=2 -->
## PAGE 00015: Generating  Cybersecurity Reports

- page_id: `227165079`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227165079/Generating+Cybersecurity+Reports
- version_number: 2
- version_date: `2025-05-05T08:30:15.527+02:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

The[CONFLUENCE_PAGE title='Report Wizard' space='MD2024xR3']can generate reports that include data on TARA(Threat Analysis and Risk Assessment).The TARA report presents a comprehensive overview of identified potential threats and their associated risks. It categorizes these threats and provides an analysis of the risks involved.

To generate a report

1. In the main menu of your modeling tool, select**Tools**>**Report Wizard**.
2. Select the TARA Report Template to generate a report containing TARA data and click Next . [ATTACHMENT filename='TARA_Report.png']
3. To include built-in data in the report, select Built-in and click Next.
4. To generate the TARA report, select the packages containing TARA elements and then click Next . 
 
[IMAGE alt='' src=''] To learn more about selecting report data, refer to the [CONFLUENCE_PAGE title='Select Element Scope pane' space='MD2024xR3'].
5. Configure the report file by specifying the report file location and image format. Then Click **Generate**. To learn more about configuring output options, refer to the [CONFLUENCE_PAGE title='Generate Output pane' space='MD2024xR3'].

Following is the example of the **TARA**report.

[IMAGE alt='' src='']

###### Example of the **TARA**report.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><span style="color: rgb(23,43,77);">The<span> </span></span><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Report Wizard" /></ac:link><span style="color: rgb(23,43,77);"><span> can generate</span> reports that include data on TARA(</span><span style="color: rgb(23,43,77);">Threat Analysis and Risk Assessment</span><span style="color: rgb(23,43,77);">).<span> </span></span><span style="color: rgb(23,43,77);">The TARA report presents a comprehensive overview of identified potential threats and their associated risks. It categorizes these threats and provides an analysis of the risks involved.</span></p><p>To generate a r<span style="color: rgb(23,43,77);">eport</span></p><hr /><ol><li><p>In the main menu of your modeling tool, select<span> </span><strong>Tools<span> </span></strong>&gt;<span> </span><strong>Report Wizard</strong>.</p></li><li><span style="color: rgb(23,43,77);">Select the<span> </span></span><strong style="text-align: left;">TARA Report Template</strong><span style="color: rgb(23,43,77);"><span> </span>to generate a report containing TARA data and click<span> </span></span><strong style="text-align: left;">Next</strong><span style="color: rgb(23,43,77);">.</span><strong style="text-align: left;"><br /></strong><br /><ac:image><ri:attachment ri:filename="TARA_Report.png"><ri:page ri:content-title="Generating  Cybersecurity Reports" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li><li>To include built-in data in the report, select<span> </span><strong>Built-in<span> </span></strong>and click<span> </span><strong>Next.</strong></li><li><span style="color: rgb(23,43,77);">To generate the<span> </span></span><strong style="text-align: left;">TARA<span> </span></strong><span style="color: rgb(23,43,77);">report, select the packages containing TARA elements and then click<span> </span></span><strong style="text-align: left;">Next</strong><span style="color: rgb(23,43,77);">.<br /><br /><ac:image><ri:attachment ri:filename="Select Element Scope_Dialog.png"><ri:page ri:content-title="Generating  Cybersecurity Reports" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /></span><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a7e0c1cf-1761-4df4-b506-f0833aac2be4"><ac:rich-text-body><p>To learn more about selecting report data, refer to the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Select Element Scope pane" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li><li><span style="color: rgb(23,43,77);"><span style="color: rgb(62,63,64);"><span> C</span>onfigure the report file by specifying the report file location and image format. Then C</span>lick <strong>Generate</strong>.<br /></span><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="1e09bc38-d021-45a9-bb8b-8a8ee1b252fb"><ac:rich-text-body><p>To learn more about configuring output options, refer to the <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Generate Output pane" /></ac:link>.</p></ac:rich-text-body></ac:structured-macro></li></ol><p><span style="color: rgb(23,43,77);">Following is the example of the <strong>TARA </strong>report.<br /><br /></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="TARA report example.png"><ri:page ri:content-title="Generating  Cybersecurity Reports" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Example of the <strong>TARA </strong>report.</h6>
````

<!--NOMAGIC_PAGE id=227164573 space=SCD2024xR3 version=2 -->
## PAGE 00016: Installation, licensing, and system requirements

- page_id: `227164573`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164573/Installation+licensing+and+system+requirements
- version_number: 2
- version_date: `2025-05-05T08:30:14.436+02:00`
- ancestors: Systems Cybersecurity Designer
- labels: []

### NORMALIZED CONTENT

For information regarding installation, licensing, and system requirements, visit the[CONFLUENCE_PAGE title='Installation, licensing, and system requirements' space='IL2024xR3']page.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p class="with-breadcrumbs conf-macro output-block">For information regarding installation, licensing, and system requirements, visit the<span> </span><ac:link><ri:page ri:space-key="IL2024xR3" ri:content-title="Installation, licensing, and system requirements" /></ac:link><span> </span>page.</p>
````

<!--NOMAGIC_PAGE id=227164572 space=SCD2024xR3 version=3 -->
## PAGE 00017: Introduction to Systems Cybersecurity Designer

- page_id: `227164572`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164572/Introduction+to+Systems+Cybersecurity+Designer
- version_number: 3
- version_date: `2025-08-20T11:10:58.595+02:00`
- ancestors: Systems Cybersecurity Designer
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

- [CONFLUENCE_PAGE title='ISO 21434 Functional Cybersecurity' space='']
- [CONFLUENCE_PAGE title='Collaborative modeling' space='']
- [CONFLUENCE_PAGE title='Generating Cybersecurity Reports' space='']
- [CONFLUENCE_PAGE title='Libraries' space='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>Cybersecurity engineering is a critical discipline to ensure safe and secure human experiences using cyber-physical systems. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events.</p><p>Based on a system architecture, the Systems Cybersecurity Designer enables:</p><ul><li data-uuid="42511957-d214-45ce-943c-7d97c28a3041">Selection of Assets for protection</li><li data-uuid="d773b6ac-8c7b-4334-8085-0edc836c4b91">Threat and Cyberattack Modeling</li><li data-uuid="6ab3324c-1f0e-4da6-9cfe-59d21a76aec7">Risk Evaluation</li><li data-uuid="772b49c8-b958-48b7-92db-050624c84cd7">Cybersecurity requirements creation to mitigate identified risks</li></ul><p>The Systems Cybersecurity Designer supports the following risk assessment methodologies :</p><ul><li data-uuid="50bc1f97-3055-4848-a8c0-4ffb2f16803f">Threat Analysis and Risk Assessment as per ISO/SAE 21434:2021</li></ul><p>To learn more about Systems Cybersecurity Designer, refer to:</p><ul><li><ac:link><ri:page ri:content-title="ISO 21434 Functional Cybersecurity" /></ac:link></li><li><ac:link><ri:page ri:content-title="Collaborative modeling" /></ac:link></li><li><ac:link><ri:page ri:content-title="Generating  Cybersecurity Reports" /><ac:plain-text-link-body><![CDATA[Generating Cybersecurity Reports]]></ac:plain-text-link-body></ac:link></li><li><ac:link><ri:page ri:content-title="Libraries" /></ac:link></li></ul>
````

<!--NOMAGIC_PAGE id=227164578 space=SCD2024xR3 version=1 -->
## PAGE 00018: ISO 21434 Concept

- page_id: `227164578`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164578/ISO+21434+Concept
- version_number: 1
- version_date: `2025-04-17T11:02:36.090+02:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity
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
<h3>T<ac:inline-comment-marker ac:ref="bf287acc-bf9b-439c-9577-f57d30a2a79c">ARA process</ac:inline-comment-marker></h3><p style="text-align: center;"><ac:image><ri:attachment ri:filename="TARA_Process_Image.png"><ri:page ri:content-title="ISO 21434 Concept" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">TARA process</h6><p>The TARA (Threat <span style="color: rgb(23,43,77);">Analysis </span>and Risk Assessment) process is described in Chapter 15 of ISO/SAE 21434:2021. It is a methodology used to identify and assess cyber security threats and vulnerabilities beginning with the design phase of a product.</p><p>The following is the standard procedure followed in TARA:</p><ol style="text-align: left;"><li>Define the items you want to study. These items are components or sets of components of the considered system.</li><li>For each item identify t<ac:inline-comment-marker ac:ref="af0ba61b-9718-49e9-a668-3aa8aeead8c3"><ac:inline-comment-marker ac:ref="c05e0205-3381-4c26-8d3b-1c549d91a8fd">he assets</ac:inline-comment-marker></ac:inline-comment-marker> to be protected and allocate CIA (Confidentiality, Integrity, and Availability) properties for each asset.</li><li><ac:inline-comment-marker ac:ref="3052ec32-3de2-449c-bfd4-0a2305aae43e"><ac:inline-comment-marker ac:ref="2c6a74a6-ec8c-4b17-9c7f-c36e00ca043c">Define any dama</ac:inline-comment-marker>ge scenarios</ac:inline-comment-marker> that can affect a vehicle system/function or a road user. After identifying those damage scenarios, you need to rate their impact in terms of Safety, Financial, Operational, and Privacy.</li><li>Create threat scenarios that can lead to the identified damage scenarios and rate them in terms of feasibility. Threat scenarios that lead to an asset compromise can be described by one or several attack paths. Each attack path is rated with an attack feasibility value.</li><li>Assess the risks. The risk is the probability that the threat will occur and entails the damage scenario impact. The risk valu<ac:inline-comment-marker ac:ref="17f8e5a8-8899-4fa5-a8e1-c7971384ff30">e is <span style="color: rgb(62,63,64);">automatically </span>computed</ac:inline-comment-marker> based on this formula from ISO/SAE 21434:2021,<span> </span><em>Annex H: Risk = 1 + Impact x Feasibility.</em></li><li> According to the computed risk value,<ac:inline-comment-marker ac:ref="f77ed7e0-6738-4276-95e2-b33854c5d6e2"> decide</ac:inline-comment-marker> the risk treatment for each threat scenario: Retain, Reduce, Share, or Avoid. Depending on the risk treatment decision, <ac:inline-comment-marker ac:ref="b18dd0f5-50da-48e5-a536-d3e96f0b1e8c">determine</ac:inline-comment-marker> cybersecurity claims or goals that will eventually be detailed in the cybersecurity requirements (functional, technical, hardware, or software type).</li></ol><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="faa93582-b57b-4b49-bd25-28be3230adea"><ac:rich-text-body><p><span style="color: rgb(62,63,64);">An Item is a part of the system architecture to be protected. An Item with a Functional Cybersecurity Concept (output of the study) is the system architecture with additional requirements and claims that <ac:inline-comment-marker ac:ref="eb7839d2-148c-42c6-9a64-784c8e8da763">ensures</ac:inline-comment-marker> a secure system.</span></p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227164574 space=SCD2024xR3 version=1 -->
## PAGE 00019: ISO 21434 Functional Cybersecurity

- page_id: `227164574`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164574/ISO+21434+Functional+Cybersecurity
- version_number: 1
- version_date: `2023-08-25T07:53:48.152+02:00`
- ancestors: Systems Cybersecurity Designer
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
<p>Cybersecurity engineering is a critical discipline to <span style="color: rgb(62,63,64);">ensure safe and secure human experiences using cyber physical systems</span>. The main challenge is to preserve trust for connected cyber systems in an evolving digital economy increasingly threatened by unpredictable events.</p><p>Systems Cybersecurity Designer <span style="color: rgb(62,63,64);">allows you to identify assets to be protected, threats and attacks to be tackled, and cybersecurity requirements to mitigate identified risks</span>. <span style="color: rgb(62,63,64);"><ac:inline-comment-marker ac:ref="5aa9f7b7-f09d-4e88-9c6c-564d4e1ae5e3">The <ac:inline-comment-marker ac:ref="aa078253-f98a-42c8-851b-60551bb5183d">Systems Cybersecurity</ac:inline-comment-marker> Designer supports t</ac:inline-comment-marker>he<a href="https://www.iso.org/standard/70918.html"> ISO/SAE 21434 standard</a>. It </span>enables a proactive and continuous security assessment in the initial design phase to reduce product development cost and time. Systems cybersecurity designers are able to create a Threat Analysis and Risk Assessment (TARA) project template to comply with the ISO/SAE 21434:2021.</p><p>The<strong> </strong>ISO/SAE 21434:2021 standard specifies engineering requirements for cybersecurity risk management regarding the Concept, Product development, Production, Operations, and maintenance and decommissioning of electrical and electronic (E/E) systems in road vehicles. This standard includes the integral components and interfaces of the road vehicles. A framework includes requirements for cybersecurity processes and a common language for communicating and managing cybersecurity risk. It is applicable to electrical and electronic (E/E) systems of production road vehicles whose development or modification began after the publication of ISO/SAE 21434:2021. ISO/SAE 21434:2021 does not prescribe specific technology or solutions related to cybersecurity.</p><p>The <ac:inline-comment-marker ac:ref="895e8af4-0a2f-4aea-b5ef-49e70b4ac1ec">Systems</ac:inline-comment-marker> <span style="color: rgb(62,63,64);">Cybersecurity Designer </span>allows a cybersecurity designer to:</p><ul><li>Design a safe and secure system through a built-in scalable cyber system model, which includes assets, weaknesses, threats, attack paths, and security requirements.</li><li>Perform continuous threat assessment and hazard analyses to enhance design through real world scenarios.</li><li>Support certification needs with consistent safety and cybersecurity compliance views.</li></ul><p>The Systems <span style="color: rgb(62,63,64);">Cybersecurity Designer </span>directly covers the following parts of the standard:</p><p><strong>9. Concept</strong> </p><p>This chapter specifies the item with its cybersecurity goals and claims. It is composed of cybersecurity requirements and the operational environment requirements of an item.</p><p><strong>15. Threat analysis and risk assessment methods</strong></p><p>This chapter specifies the methods to determine the extent to which a threat scenario can impact a road user. These methods and their work products are known as Threat Analysis and Risk Assessment (TARA) and are performed from the viewpoint of affected road users. The TARA steps are generic modules that can be invoked systematically from any point in the lifecycle of an item or component.</p><p><br /></p><p><ac:image ac:align="center"><ri:attachment ri:filename="ISOFramework.png"><ri:page ri:content-title="ISO 21434 Functional Cybersecurity" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></p><h6 style="text-align: center;">Overview of ISO/SAE 21434:2021 standard</h6><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6f459f96-4d19-47a8-8187-d08bea2c157e"><ac:parameter ac:name="title">Prerequisites</ac:parameter><ac:rich-text-body><p><span style="color: rgb(62,63,64);">To install and use the Sy<ac:inline-comment-marker ac:ref="5a62dbbe-3f21-4ffe-a890-35f81a113da1">stem</ac:inline-comment-marker>s Cybersecurity Designer, ensure that one of the following modeling tools is installed:</span></p><ul><li><p>Magic Cyber Systems Engineer</p></li><li><p>Magic Cyber Systems of Systems Architect</p></li><li><p>Cameo Systems Modeler - Architect Edition</p></li><li><p>Cameo Systems Modeler - Enterprise Edition</p></li><li><p><ac:inline-comment-marker ac:ref="61d83bad-579d-4a05-86ed-b4075f1788b9">Cameo Enterprise Architecture</ac:inline-comment-marker></p></li><li><ac:inline-comment-marker ac:ref="61d83bad-579d-4a05-86ed-b4075f1788b9"><span style="color: rgb(62,63,64);">Magic Draw (any version) with SysML plugin installed</span></ac:inline-comment-marker></li></ul><p>To learn more about how to download the installation files, refer <ac:link><ri:page ri:space-key="NMDOC" ri:content-title="Downloading installation files" /></ac:link>.</p><p><span style="color: rgb(62,63,64);">To install and use the Sy<ac:inline-comment-marker ac:ref="5b0a6940-6649-4125-b4e0-a03cb02cd91f">stems</ac:inline-comment-marker> Cybersecurity Designer, ensure that the following plugins are installed in your modeling tool:</span></p><ul><li>Cameo Safety and Reliability Analyzer</li><li>ISO 26262 plugin</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="e9fbfa8c-d2e1-4821-998e-868b1d97f93e"><ac:rich-text-body><p>The cybersecurity plugin is compliant to <a href="https://www.omg.org/spec/RAAML/1.0/Beta2/About-RAAML">RAAML standard</a>.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p>
````

<!--NOMAGIC_PAGE id=227164584 space=SCD2024xR3 version=2 -->
## PAGE 00020: ISO 21434 Project

- page_id: `227164584`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164584/ISO+21434+Project
- version_number: 2
- version_date: `2025-11-18T11:03:40.109+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity
- labels: []

### NORMALIZED CONTENT

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

If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling.

##### ISO 21434 Project Template

A default ISO 21434 project template is displayed once you open the project. This template is provided to help you initiate the process.

**Containment Tree**

The Containment tree displays the default packages. One package, one table, and one element of each type is provided in the Containment tree. You can add, modify or delete any element or package from the Containment tree.

**Index**

The Index displays the default tables and information related to it. It also displays other elements, such as Operational Conditions, Operation Situations, etc.. You can navigate to the tables and elements by clicking the icons. Only the default tables and elements are displayed in the Index. The Index will not display any table or element created later.

If you press the CTRL key and double-click any table's icon, the table opens in a new tab.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<h3>Creating ISO 21434 project</h3><p>To create a new ISO 21434 project</p><hr /><ol><li>Do one of the following:<ul><li class="atl-forced-newline">From the<span> </span><strong>File</strong><span> </span>menu, select <strong>New Project </strong>from the drop-down list.<br /><em><br /><ac:image><ri:attachment ri:filename="New Project_command.jpg" /></ac:image><br /><br /></em></li><li>Click <strong>Create New Project </strong>on the welcome screen.<br /><br /><ac:image><ri:attachment ri:filename="Create New Project_Command.png" /></ac:image><br /><br /></li><li>Press Ctrl + Shift + N.</li></ul></li><li><p class="auto-cursor-target">In the New Project dialog, select <strong>ISO 21434 Project.<br /></strong><br /><ac:image><ri:attachment ri:filename="New Project_Window.jpg" /></ac:image><br /><br /></p></li><li><p class="auto-cursor-target">Specify the file name in the Name box.</p></li><li><p class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">Click the</span><span style="color:var(--ds-text,#333333);"><span> <ac:image><ri:attachment ri:filename="Three Dot Icon.png" /></ac:image> </span>button to select the location to store the project in a folder.</span></p></li><li><p class="auto-cursor-target">Select the checkbox to automatically create a folder for the project in the specified location.</p></li><li><p class="auto-cursor-target">Click <strong>OK</strong>.</p></li></ol><p>A new ISO 21434 project is displayed with the default packages in the Containment tree and the Index.</p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="df13aefb-d300-4916-8e58-5927a3285c35"><ac:rich-text-body><p><ac:inline-comment-marker ac:ref="3104bf7f-9aeb-412a-8d92-79623c88ba4c">If any dependent plugin(s) is not installed, a notification message is displayed which lists the required plugin(s) while launching the modeling.</ac:inline-comment-marker></p></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">ISO 21434 Project Template</h3><p>A default ISO 21434 project template is displayed once you open the project. This template is provided to help you initiate the process.</p><p><strong>Containment Tree</strong></p><p>The Containment tree displays the default packages. One package, one table, and one element of each type is  provided in the Containment tree. You can add, modify or delete any element or package from the Containment tree.</p><p><strong>Index</strong></p><p>The Index displays the default tables and information related to it. It also displays other elements, such as Operational Conditions, Operation Situations, etc.. You can navigate to the tables and elements by <ac:inline-comment-marker ac:ref="e3889777-fca1-4399-926c-39b8be2b8e53">clicking the icons</ac:inline-comment-marker>. Only the default tables and elements are displayed in the Index. The Index will not display any table or element created later.</p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="99614ef4-6697-44ce-a28f-8369f17b828d"><ac:rich-text-body><p>If you press the CTRL key and double-click any table's icon, the table opens in a new tab.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /><ac:image><ri:attachment ri:filename="Index.png" /></ac:image></p>
````

<!--NOMAGIC_PAGE id=227164596 space=SCD2024xR3 version=2 -->
## PAGE 00021: Item

- page_id: `227164596`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164596/Item
- version_number: 2
- version_date: `2025-11-18T11:04:16.963+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Item</strong></p><p>Component or set of components that implements a function at the vehicle level.</p><p><strong>Item Block</strong></p><p>An Item Block is a part of the system that needs to be assessed with a TARA process. <span style="letter-spacing: 0.0px;">An Item Block is a SysML Block.</span></p><p><strong>Members</strong></p><p>Elements that are within the item block.</p><p><strong>Boundary Members</strong></p><p>Elements and/or ports that connect the item with other elements.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3><ac:inline-comment-marker ac:ref="4d7400a9-4746-4fc9-b733-09d729e7585d">Creating an Item</ac:inline-comment-marker></h3><p>To create an Item</p><hr /><ol><li>In the Containment tree, right-click <strong>Items &amp; Assets Definition </strong>and select<strong> Create Element.</strong><strong><br /><br /><ac:image><ri:attachment ri:filename="Create Element.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">Do one of the following:<ul><li class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">I</span><span style="color:var(--ds-text,#333333);">n the dialog, expand <strong>ISO 21434 </strong>and select <strong>Single Block Item.</strong></span><strong><br /><br /></strong><ac:image><ri:attachment ri:filename="Single Block Item.png" /></ac:image><br /><br /></li><li class="auto-cursor-target">In the search tab, type the keyword item and then select <strong>Single Block Item.<br /></strong><br /><ac:image ac:thumbnail="true" ac:height="187"><ri:attachment ri:filename="Create Item_Search.png" /></ac:image><br /><br /></li></ul></li><li class="auto-cursor-target">Name the created Item in the Containment tree. The Item has the prefix <strong>IT</strong>, which denotes that the created element is an Item; the number <strong>1</strong> indicates that it is the first Item created.<br /><br /><ac:image><ri:attachment ri:filename="1 ContainmentTreeAEBS.png" /></ac:image></li></ol><ac:structured-macro ac:name="tip" ac:schema-version="1" ac:macro-id="500928e5-b5aa-4deb-9f12-f5f3dccc4ed1"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">After creating an asset, it is beneficial to find its location in the model tree by performing one of the following:</span></p><ul><li><span style="color:var(--ds-text,#333333);">Right-click the asset, and, from the shortcut menu, choose the<span> </span></span><strong>Select in Containment Tree</strong><span style="color:var(--ds-text,#333333);"><span> </span>command.</span></li><li><span style="color:var(--ds-text,#333333);">Select the asset and press Alt+B.</span></li></ul></ac:rich-text-body></ac:structured-macro><h3>Creating an Item Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="b731e3bf-11d8-4757-a15e-afa992b85247"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project </strong>template<span style="color:var(--ds-text,#172b4d);">, then an <strong>Item Table </strong>already exists in the <strong>2.1 Items &amp; Assets Definition</strong> package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:inline-comment-marker ac:ref="799bf929-1740-4ea7-a937-3f76c0165a6e">To create an Item Table</ac:inline-comment-marker></p><hr /><ol><li>In the Containment tree, right-click <strong>Items &amp; Assets Definition </strong>and select<strong> Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram_Containment tree.png" /></ac:image><br /></strong><strong><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Item Table.</strong></span><strong><br /><br /><ac:image><ri:attachment ri:filename="Item Table_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword item and then select <strong>Item Table.<br /><br /><ac:image><ri:attachment ri:filename="Item Table_Search.png" /></ac:image><br /><br /></strong>The Item Table is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="1 ContainmentTreeItemsTable.png" /></ac:image></li></ul></li></ol><h3>Adding an Item to the Item Table</h3><p>To add a new Item to the Item Table</p><hr /><ol><li>In the Item Table, click <strong>Add New. </strong>A row is added to the Item table, which shows the new Item.<strong><br /><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png" /></ac:image><br /><br /></strong></li><li> In the newly created Item's row and in the <strong>Name </strong>column, double-click the designated cell to name the Item.<br /><br /><ac:image><ri:attachment ri:filename="2 AfterAddingAEBSasItem.png" /></ac:image><br /><br /></li></ol><p>To add an existing Item in the Item Table</p><hr /><ol><li>In the Item Table, click <strong>Add Existing.<br /><br /><ac:image ac:height="194"><ri:attachment ri:filename="3 ClickAddExisting.png" /></ac:image><br /><br /></strong></li><li>From the <strong>Select Single Block Item</strong><strong> </strong>dialog, select the required Item. A row is added to the Item table, which shows the existing Item.<br /><br /><ac:image><ri:attachment ri:filename="4 SelectSingleItemBlockWindow_v2.png" /></ac:image><br /><br /></li><li>In the existing Item's row and in the <strong>Name </strong>column, double-click the designated cell to rename the Item.<br /><br /><ac:image><ri:attachment ri:filename="5 AfterAddingExistingHeadlampAsItem.png" /></ac:image></li></ol><h3>Assigning SysML Block as an Item Block</h3><p>To assign SysML Block as an Item Block</p><hr /><ul><li>Double-click the designated cell in the Item's row and the <strong>Item Block column</strong>. I<span style="color:var(--ds-text,#333333);">n the drop-down list, select the Item Block.</span><br /><br /><ac:image><ri:attachment ri:filename="2 DoubleClickItemBlockCell_v2.png" /></ac:image><br /><br />The added Item Block is now displayed in the Item Table.<br /><br /><ac:image><ri:attachment ri:filename="5 AfterAssigningAnItemBlock.png" /></ac:image></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8954b67c-823f-4ac9-9998-8f53065b77ae"><ac:rich-text-body><ul><li>You can also drag and drop the SysML Block from the Containment tree to the Item Table.</li><li>Once you declare a SysML Block as an Item Block, a legend appears at the top left corner of the element.<br /><br /><ac:image><ri:attachment ri:filename="Item_Legend.png" /></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><h3>Item Table Example</h3><p><span style="color:var(--ds-text,#333333);">In an Item Table, <strong>Members </strong>and <strong>Boundary</strong> <strong>Members </strong>columns are automatically filled based on the Item Block definition.</span></p><p class="auto-cursor-target"><ac:image><ri:attachment ri:filename="5 AfterAssigningAnItemBlock.png" /></ac:image></p><p class="auto-cursor-target"><br /></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ecb29b23-9bba-4d3c-b9c0-8d100bee465f"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a href="https://www.iso.org/obp/ui/fr/#iso:std:iso-sae:21434:ed-1:v1:en">ISO/SAE 21434:2021 Road vehicles-Cybersecurity engineering</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227165083 space=SCD2024xR3 version=1 -->
## PAGE 00022: Libraries

- page_id: `227165083`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227165083/Libraries
- version_number: 1
- version_date: `2024-06-18T11:57:24.962+02:00`
- ancestors: Systems Cybersecurity Designer
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
<p>You can import multiple libraries in the Systems Cybersecurity Designer plugin instead of creating elements. All imported libraries are treated as used projects in your current project. </p><h3>Adding a library to the project</h3><p>To add a library to the project </p><hr /><ul><li>In the Containment tree, right-click <strong>Model&gt; Security </strong>and then select the required library.<br /><br /><ac:image><ri:attachment ri:filename="Add Library.png"><ri:page ri:content-title="Libraries" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image><br /><br /></li></ul><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="28d0d24c-3743-4be7-85c9-4bf6856b9cdd"><ac:rich-text-body><p>If you click on any element in the library, you will be redirected to the web page of the respective element.</p></ac:rich-text-body></ac:structured-macro><h3>MITRE CWE Library</h3><p><span style="color: rgb(62,63,64);">The addition of the MITRE CWE Library <span style="color: rgb(23,43,77);">adds a package to the Containment tree. The <span style="color: rgb(62,63,64);">MITRE CWE Library </span></span>contains two sub-packages: Common Weakness Enumeration and Functional Cybersecurity Requirements.  The Common Weakness Enumeration package contains a list of weaknesses. Each weakness contains a hyperlink that redirects you to the CWE definition web page. The Functional Cybersecurity Requirements package contains the requirements to mitigate the weakness. These requirements are segregated with the help of sub-packages based on the type of requirement.</span></p><p><br /></p><h6 style="text-align: center;"><ac:image ac:align="center"><ri:attachment ri:filename="MITRE CWE Library.png"><ri:page ri:content-title="Libraries" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image>MITRE Library present in the Containment tree.</h6><h3><span style="color: rgb(23,43,77);">MITRE ATT&amp;CK Enterprise </span><span style="color: rgb(23,43,77);">Technique Library</span></h3><p><span style="color: rgb(23,43,77);">The addition of MITRE ATT&amp;CK Enterprise Technique Library adds two packages to the Containment tree: MITRE ATT&amp;CK Enterprise Technique Library and MITRE ATT&amp;CK Platforms Library. The MITRE ATT&amp;CK Enterprise Technique Library package contains sub-packages which contain enterprise mitigation, tactics and techniques. The MITRE ATT&amp;CK Platforms Library contains the platforms through which the attacks can take place.<br /><br /></span></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="Enterprise_Library.png"><ri:page ri:content-title="Libraries" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">MITRE ATT&amp;CK Enterprise Technique Library present in the Containment tree.</h6><h3><span style="color: rgb(23,43,77);">MITRE ATT&amp;CK ICS </span><span style="color: rgb(23,43,77);">Technique Library</span></h3><p><span style="color: rgb(23,43,77);">The addition of MITRE ATT&amp;CK ICS Technique Library adds a package to the Containment tree. The MITRE ATT&amp;CK ICS Technique Library package contains sub-packages which contain ICS mitigation, tactics and techniques.<br /><br /></span></p><p style="text-align: center;"><span style="color: rgb(23,43,77);"><ac:image><ri:attachment ri:filename="ICS_Library.png"><ri:page ri:content-title="Libraries" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">MITRE ATT&amp;CK ICSTechnique Library present in the Containment tree.</h6><h3><span style="color: rgb(23,43,77);">NIST Control Library</span></h3><p style="text-align: left;"><span style="color: rgb(23,43,77);">The addition of the NIST Control Library adds a package to the Containment tree. The NIST Control Library package contains a sub-package that lists the c</span><span style="color: rgb(23,43,77);">yber security requirements.<br /></span><span style="color: rgb(23,43,77);"><br /><ac:image ac:align="center"><ri:attachment ri:filename="NIST Library.png"><ri:page ri:content-title="Libraries" ri:space-key="SCD2024xR3" /></ri:attachment></ac:image></span></p><h6 style="text-align: center;">NIST Control Library present in the Containment tree.</h6>
````

<!--NOMAGIC_PAGE id=227164868 space=SCD2024xR3 version=2 -->
## PAGE 00023: Manual Attack Path

- page_id: `227164868`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164868/Manual+Attack+Path
- version_number: 2
- version_date: `2025-11-18T11:04:42.019+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Threat  scenario
- labels: []

### NORMALIZED CONTENT

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Attack Path</strong></p><p>Set of deliberate actions to realize a threat scenario.</p><p><strong>Attack Path Steps</strong></p><p>Enumerate each step needed to perform the threat scenario.</p><p><strong>Attack Feasibility Rating</strong></p><p>An attribute of an attack path describes the ease of successfully carrying out the corresponding set of actions. By default, the ISO/SAE 21434:2021 rating scale is used.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Manual <span>Attack Path</span></h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="33960afa-9338-4985-843d-537893e4b919"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">A <span style="color:var(--ds-text,#172b4d);">Manual </span>Attack Path refers to the manual way of describing and rating the feasibility of attack paths. It does not refer to potential based attacks or CVSS methodologies.</span></p></ac:rich-text-body></ac:structured-macro><p>To create a <span style="color:var(--ds-text,#172b4d);">Manual </span><span style="color:var(--ds-text,#333333);">Attack Path</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<span> </span><strong>Attack Paths and Feasibility Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="Create Element.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong><span style="color:var(--ds-text,#172b4d);">Manual </span>Attack Path</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Manual Attack Path_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong><span style="color:var(--ds-text,#172b4d);">Manual </span></strong></span><strong>Attack Path.<br /><br /><ac:image><ri:attachment ri:filename="Manual Attack Path_Menu_Search.png" /></ac:image><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Manual Attack Path in the Containment tree and press Enter. The <span style="color:var(--ds-text,#172b4d);">Manual </span>Attack Path has the prefix <span><strong><ac:inline-comment-marker ac:ref="36c001cf-dca2-40db-87f2-dd5774b62d1d">AP</ac:inline-comment-marker></strong>, </span>which denotes that the created element is a Manual Attack Path; the number<span> </span><strong style="text-align: left;">1</strong> indicates that it is the first Manual Attack Path created.<br /><br /><strong><ac:image><ri:attachment ri:filename="Containment Tree.png" /></ac:image></strong><br /></span></li></ol><h3>Creating a Manual Attack Path Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="ac3fdcfd-bb62-48d6-a13a-b462ed970031"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color:var(--ds-text,#172b4d);">, then a<span> </span><strong>Manual Attack Paths </strong>table<span> </span>already exists in the<span> <strong>1.3 Attack Paths and Feasibility Ratings</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:inline-comment-marker ac:ref="bc6650c9-7c62-42c5-8f4d-246e2a504771">To create a</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="bc6650c9-7c62-42c5-8f4d-246e2a504771"> Manual Attack Path </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="bc6650c9-7c62-42c5-8f4d-246e2a504771">Table</ac:inline-comment-marker></p><hr /><ol><li>In the Containment tree, right-click<span> <span style="color:var(--ds-text,#333333);"><strong>Attack Paths and Feasibility Ratings</strong></span></span><span style="color:var(--ds-text,#333333);"> </span>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png" /></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Manual Attack</strong> <strong>Path Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Manual Attack Path Table_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword attack and then select<span> <strong>Manual Attack Path </strong></span><strong>Table.<br /><br /><ac:image><ri:attachment ri:filename="Manual Attack Path Table_Menu_Search.png" /></ac:image><br /><br /></strong>The Manual Attack Table is displayed in the diagram pane of the modeling tool.<br /><br /><strong><ac:image><ri:attachment ri:filename="Manual Attack Path Table_Created.png" /></ac:image></strong></li></ul></li></ol><h3>Adding a Manual Attack Path to Manual Attack Path Table</h3><p>To add a new Manual Attack Path to the Manual Attack Path Table</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Manual Attack Path Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New. </strong><span style="color:var(--ds-text,#333333);">A row is added in the Manual Attack Path Table, which shows the new Manual Attack Path.</span><strong style="text-align: left;"><span style="color:var(--ds-text,#333333);"> </span><br /><br /><ac:image><ri:attachment ri:filename="Add New.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">In the newly created Manual Attack Path's row and the<span> </span><strong>Name<span> </span></strong>column, double-click the designated cell to name the Manual Attack Path.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="New added.png" /></ac:image></strong><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color:var(--ds-text,#333333);">To add an existing Manual Attack Path to the Manual Attack Path Table</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Manual Attack Path Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="Add Existing.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Attack Path</strong> dialog, select the required Manual Attack Path. A row is added to the Manual Attack Path Table, which shows the existing Manual Attack Path. <br /><br /><ac:image><ri:attachment ri:filename="Select Attack Path dialog box.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">In the existing Manual Attack Path's row and the<span> </span><strong style="text-align: left;">Name<span> </span></strong>column, double-click the designated cell to rename the Manual Attack Path.<br style="text-align: left;" /><br /><span style="color:var(--ds-text,#333333);"><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="New added.png" /></ac:image></strong></span><br style="text-align: left;" /></span></li></ol><h3>Adding Attack Path Steps</h3><p>To add Attack Path Steps to the Manual Attack Path Table</p><hr /><ol><li>Double-click the designated cell in the<span> <strong>Attack Path Steps </strong></span>column and the required Manual Attack Path's row and click<span> </span><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Adding attack path_Three dot.png" /></ac:image><br /><br /></li><li><p><span style="color:var(--ds-text,#333333);">From the <strong>Select Situation</strong><strong> </strong>dialog, <ac:inline-comment-marker ac:ref="0095b215-7b06-4c59-b208-bd489cf1c532">select Attack Path Steps.</ac:inline-comment-marker></span><br style="text-align: left;" /><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="Select Element Dialog.png" /></ac:image><br style="text-align: left;" /><br style="text-align: left;" /><span style="color:var(--ds-text,#333333);">The Attack Path Steps now shown in the Manual Attack Path Table.<br /><br /><ac:image><ri:attachment ri:filename="Attack Path Steps added.png" /></ac:image><br /></span></p></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="a20036fc-d84f-496a-8521-30c4fd021e0b"><ac:rich-text-body><ul><li>You can also drag and drop the Attack Path Step from the Containment tree to the Threat Scenario Table.</li><li>You can move the Attack Path Steps in the <strong>Select Situation</strong><strong> </strong>dialog by clicking <strong>Up </strong>or <strong>Down</strong>.<br /><br /><ac:image><ri:attachment ri:filename="Movement of attack paths.png" /></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);"> </span></p><h3>Adding an Attack Feasibility Rating</h3><p>To rate the Attack Feasibility</p><hr /><ul><li><span style="color:var(--ds-text,#333333);">Double-click the cell </span><span style="color:var(--ds-text,#000000);"><span>in the <ac:inline-comment-marker ac:ref="3cdd3203-a6de-44a0-ac78-27acd9233c8b">Manual Attack Path's </ac:inline-comment-marker></span></span><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="3cdd3203-a6de-44a0-ac78-27acd9233c8b">row</ac:inline-comment-marker> and from the drop-down list, select Attack Feasibility Rating.<br /><br /><ac:image><ri:attachment ri:filename="Attack Feasibility Rating_Selection.png" /></ac:image><br /><br style="text-align: left;" /><ac:inline-comment-marker ac:ref="1ad0fcee-334d-488f-af31-80b41680fef6">The Attack Feasibility</ac:inline-comment-marker> Rating is now shown in the Manual Attack Path Table.<br /><br /><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="Attack Feasibility Rating_Selected.png" /></ac:image></span><br /></span></li></ul><h3><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="5e0c1889-ac92-4cf1-88fe-58a76a8a21b0">Manual Attack Path Table Example</ac:inline-comment-marker><br /><br /></span></h3><p><span style="color:var(--ds-text,#333333);"><ac:image><ri:attachment ri:filename="Example_Manual Attack Path.png" /></ac:image></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="45a1ec35-b666-48f8-a3c3-7f8c169ccbc8"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><p><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO/SAE 21434:2021 Road vehicles-Cybersecurity enginee</a>r</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164784 space=SCD2024xR3 version=2 -->
## PAGE 00024: Operational Situation

- page_id: `227164784`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164784/Operational+Situation
- version_number: 2
- version_date: `2025-11-18T11:04:34.849+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > Damage scenario
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
<h3><ac:inline-comment-marker ac:ref="84cf21db-815d-4ff0-9ede-465c908157bf">Creating an Operational Situation</ac:inline-comment-marker></h3><p>To create an Operational Situation</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<span> <strong>Damage Scenario </strong></span><strong>and Impact Ratings</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Operational Situation</strong>.</span><br /><strong><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Operational Situation.jpg" /></ac:image></strong><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword operational and then select<span> </span><strong>Operational Situation.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="Operational Situation_Search.jpg" /></ac:image></strong><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Operational Situation in the Containment tree and press Enter.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="4 OpSituationCreated.png" /></ac:image></strong></span></li></ol><h3>Adding Operational Situation to the Operational Situations Table</h3><p>Using the <span style="letter-spacing: 0.0px;">Operational Situations </span><span style="letter-spacing: 0.0px;">Table you can only add nested <span>Operational Situations.</span></span></p><p>To add an <span style="letter-spacing: 0.0px;">Operational Situation</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the <span>Operational Situations </span>Table, select an <span>Operational Situation </span>and then click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Nested.<span> </span></strong><span style="color:var(--ds-text,#333333);">A row is added in the <span>Operational Situations </span>Table, which shows the nested <span>Operational Situation</span>.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Add Nested.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">In the newly created <span>Operational Situation's </span>row and the <strong style="text-align: left;">Name<span> </span></strong>column, double-click the designated cell to name the Effect.<br style="text-align: left;" /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Added.png" /></ac:image><br /></span></li></ol><h3>Adding Operational Situation's parameters to the Operational Situations Table</h3><p><span style="color:var(--ds-text,#333333);">To add Operational Situation's parameters to the Operational Situations Table</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Double-click the designated cell in the<span> </span><strong>Vehicle Usage </strong></span><span style="color:var(--ds-text,#333333);">column and the required Operational Situation's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span></span>.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Parameters_Three Dot.png" /></ac:image><br /><br /></span></span></li><li><span style="color:var(--ds-text,#333333);"><span>From the <strong style="text-align: left;">Select Elements</strong><strong style="text-align: left;"> </strong>dialog, select the Vehicle Usage.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Select Elements dialog.png" /></ac:image><br /><br />The Vehicle Usage is added to the Operational Situations Table.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Parameters_added.png" /></ac:image><br /><br style="text-align: left;" />All other Operational Situation parameters are added to the Operational Situations Table using the same procedure.<br /><br /><ac:image><ri:attachment ri:filename="Operational Situation_Parameters_added_all.png" /></ac:image><br /></span></span></li></ol>
````

<!--NOMAGIC_PAGE id=227165029 space=SCD2024xR3 version=3 -->
## PAGE 00025: Risk Computation Customization

- page_id: `227165029`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227165029/Risk+Computation+Customization
- version_number: 3
- version_date: `2025-11-18T11:05:06.275+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table > TARA
- labels: []

### NORMALIZED CONTENT

To customize the Risk Computation

1. Create a new project and profile:
  1. Create a [CONFLUENCE_PAGE title='Creating a new project' space='MD2024xR3'] .
  2. Select Options>Project Usages , and add the ISO 21434 Profile.mdzip file to it.
  3. Create a [CONFLUENCE_PAGE title='Creating Profiles' space='MD2024xR3'] under the root package.
  4. Provide the required name, for example, My Customized ISO21434 Profile .
  5. Create a [CONFLUENCE_PAGE title='Profile diagram' space='MD2024xR3'] in the My Customized ISO21434 Profile.
  6. Provide the required name, for example, My Customized Threat Scenario .
2. Create a new customization:
  1. Search for ThreatScenarioCustomization available in the ISO 21434 Profile, and drag and drop it into the profile diagram.
  2. Create a [CONFLUENCE_PAGE title='Creating your First Customization' space='MD2024xR3'] .
  3. Provide the required name, for example, MyThreatScenarioCustomization .
  4. Create a [CONFLUENCE_PAGE title='Generalization' space='MD2024xR3'] relationship between the newly created customization element and ThreatScenarioCustomization .
  5. Using the Specification window of MyThreatScenarioCustomization, assign the value to the Customization Target property as ThreatScenario.
3. Create Customization Element Properties:
  1. Select the customization element, open the smart manipulator, and select the [CONFLUENCE_PAGE title='Creating and specifying derived properties' space='MD2024xR2'] Specification.
  2. Provide the required name for example SafetyRiskValue.
  3. Using the Specification window, assign:
    1. Type: Real [UML Primitive Types]
    2. Multiplicity: [0.1]
    3. Redefined Property: +SafetyRiskValue (From the ISO 21434 profile)
4. Create an [CONFLUENCE_PAGE title='Defining expressions' space='MD2024xR3'] for the Derived property:
  1. In the Specification window of the derived property (SafetyRiskValue), launch the editor for the Expression property.
  2. Select Create operation and then select the Real value.
  3. Provide the required Name and Value.
  4. Share the created profile and save the project.

Using the same steps, create other required derived properties and create required expressions for them (Operational, Financial, and Privacy Risk Value).

Once you add the created project containing the customized profile, the customized risk values are visible in any TARA project containing the threat scenario elements.

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p>To customize the Risk Computation</p><hr /><ol><li>Create a new project and profile:<ol><li>Create a <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating a new project" /><ac:plain-text-link-body><![CDATA[new UML project]]></ac:plain-text-link-body></ac:link>.</li><li>Select <strong>Options&gt;Project Usages</strong>, and add the <strong>ISO 21434 Profile.mdzip</strong> file to it.</li><li>Create a <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating Profiles" /><ac:plain-text-link-body><![CDATA[new profile]]></ac:plain-text-link-body></ac:link> under the root package.</li><li>Provide the required name, for example, <strong>My Customized ISO21434 Profile</strong>.</li><li>Create a <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Profile diagram" /><ac:plain-text-link-body><![CDATA[new profile diagram]]></ac:plain-text-link-body></ac:link> in the My Customized ISO21434 Profile.</li><li>Provide the required name, for example, <strong>My Customized Threat Scenario</strong>.</li></ol></li><li>Create a new customization:<ol><li>Search for <strong>ThreatScenarioCustomization </strong>available in the ISO 21434 Profile, and drag and drop it into the profile diagram.</li><li>Create a <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Creating your First Customization" /><ac:plain-text-link-body><![CDATA[new customization element]]></ac:plain-text-link-body></ac:link>.</li><li>Provide the required name, for example, <strong>MyThreatScenarioCustomization</strong>.</li><li>Create a <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Generalization" /><ac:plain-text-link-body><![CDATA[generalization ]]></ac:plain-text-link-body></ac:link>relationship between the newly created customization element and <strong>ThreatScenarioCustomization</strong>.</li><li>Using the Specification window of MyThreatScenarioCustomization, assign the value to the Customization Target property as ThreatScenario.</li></ol></li><li>Create Customization Element Properties:<ol><li>Select the customization element, open the smart manipulator, and select the <ac:link><ri:page ri:space-key="MD2024xR2" ri:content-title="Creating and specifying derived properties" /><ac:plain-text-link-body><![CDATA[Derived Property]]></ac:plain-text-link-body></ac:link> Specification.</li><li>Provide the required name for example SafetyRiskValue.</li><li>Using the Specification window, assign:<ol><li><p>Type: Real [UML Primitive Types]</p></li><li>Multiplicity: [0.1]</li><li>Redefined Property: +SafetyRiskValue (From the ISO 21434 profile)</li></ol></li></ol></li><li>Create an <ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Defining expressions" /><ac:plain-text-link-body><![CDATA[expression]]></ac:plain-text-link-body></ac:link> for the Derived property:<ol><li>In the Specification window of the derived property (SafetyRiskValue), launch the editor for the Expression property.</li><li>Select Create operation and then select the <strong>Real </strong>value.</li><li>Provide the required Name and Value.</li><li>Share the created profile and save the project.</li></ol></li></ol><p>Using the same steps, create other required derived properties and create required expressions for them (Operational, Financial, and Privacy Risk Value).</p><p>Once you add the created project containing the customized profile, the customized risk values are visible in any TARA project containing the threat scenario elements.</p>
````

<!--NOMAGIC_PAGE id=227164543 space=SCD2024xR3 version=1 -->
## PAGE 00026: Systems Cybersecurity Designer

- page_id: `227164543`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164543/Systems+Cybersecurity+Designer
- version_number: 1
- version_date: `2024-06-18T12:33:52.758+02:00`
- ancestors: 
- labels: []

### NORMALIZED CONTENT

[CONFLUENCE_PAGE title='Introduction to Systems Cybersecurity Designer' space='SCD2024xR3']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:structured-macro ac:name="include" ac:schema-version="1" ac:macro-id="b92733c1-717a-454d-ba77-ba8ada1ae303"><ac:parameter ac:name=""><ac:link><ri:page ri:content-title="Introduction to Systems Cybersecurity Designer" ri:space-key="SCD2024xR3" /></ac:link></ac:parameter></ac:structured-macro></p>
````

<!--NOMAGIC_PAGE id=227164595 space=SCD2024xR3 version=1 -->
## PAGE 00027: Table

- page_id: `227164595`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164595/Table
- version_number: 1
- version_date: `2024-01-31T07:30:01.476+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity
- labels: []

### NORMALIZED CONTENT

Learn more about tables and diagrams of the ISO 21434 project template from the following chapters:

### EXACT CONFLUENCE STORAGE SOURCE

````html
<p><ac:inline-comment-marker ac:ref="2b195a29-57e4-432b-98b8-4c02aeb8a869">Learn more a</ac:inline-comment-marker>bout tables and diagrams of the ISO 21434 project template from the following chapters: </p><p><ac:structured-macro ac:name="children" ac:schema-version="2" ac:macro-id="e53f8925-cb18-4682-9fb1-5a9ac41082e0" /></p>
````

<!--NOMAGIC_PAGE id=227164989 space=SCD2024xR3 version=2 -->
## PAGE 00028: TARA

- page_id: `227164989`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164989/TARA
- version_number: 2
- version_date: `2025-11-18T11:05:00.713+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

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
- You can also select multiple Threat Scenarios and generate/synchronize cybersecurity goals for all the selected Threat Scenarios at once.

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

##### Assigning Residual Risk Value

To assign the Residual Risk value in the TARA Table

- Double-click Residual Safety Risk value cell in the Threat Scenario row. From the drop-down list, select the R esidual Safety R isk Value . Follow the same procedure to assign Financial, Operational and Privacy Residual Risk Values. 
 
[IMAGE alt='' src='']

- You can add custom residual risk value in between the given range of 1.0 to 5.0, such as 1.2, 3.7 or 0.3.
- You can also assign the residual risk value with help of the Specification dialog of the Threat Scenario.
- The maximum value among all the residual risk values viz. Safety, Financial, Operational, and Privacy is considered as the Residual Global Risk Value.

##### TARA Table Example

- The Safety, Financial, Operational, Privacy risk values are calculated automatically by using following formula:
  - Risk Value = 1 + Maximum(Impact) * Aggregated Attack Feasibility Rating [ATTACHMENT filename='Impact Rating.png']
- The maximum value among all the risk values viz. Safety, Financial, Operational, and Privacy is considered as the Global Risk Value.

[IMAGE alt='' src='']

### EXACT CONFLUENCE STORAGE SOURCE

````html
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p>The TARA table gathers all elements that have been modeled in the previous steps and gives a global overview of the threat scenario that has to be mitigated, retained, shared, or avoided. The risk value is automatically calculated according to the ISO/SAE 21434:2021 standard.</p><p><strong>Cybersecurity Risk</strong></p><p>An effect of uncertainty on road vehicle cybersecurity expressed in terms of attack feasibility and impact.</p><p><strong>Cybersecurity Control</strong></p><p>A measure that is modifying risk.</p><p><strong>Cybersecurity Claim</strong></p><p>A statement about a risk.</p><p><strong>Cybersecurity Goal</strong></p><p>A concept-level cybersecurity requirement associated with one or more threat scenarios.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a TARA Table</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7e648328-edd6-4bc0-9aed-66cdf7a757f4"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color:var(--ds-text,#172b4d);">, then a<span> <span style="color:var(--ds-text,#333333);"><strong>TARA</strong> </span></span>table<span> </span>already exists in the<span> <strong>1.4 Risk Treatment and Cybersecurity Control</strong> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec">To create a</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec"> </ac:inline-comment-marker></span><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec">TARA</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec"> </ac:inline-comment-marker></span></span><ac:inline-comment-marker ac:ref="ed4f1fdf-8139-4559-839b-08f24dd4adec">Table</ac:inline-comment-marker></p><hr /><ol><li>In the Containment tree, right-click<span> </span><strong>Risk Treatment and Cybersecurity Control </strong>and select<strong><span> </span>Create Diagram.<br /><br /><ac:image><ri:attachment ri:filename="1 SelectCreateDiagram.png" /></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>TARA</strong> <strong>Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="2 DirectlySelectTARAtable.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target"><span style="color:var(--ds-text,#333333);">In the search tab, type the keyword TARA and then select</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">TARA Table.<br /><br /><strong><ac:image><ri:attachment ri:filename="3 WriteTARAtable.png" /></ac:image></strong><br /><br /></strong><span style="color:var(--ds-text,#333333);">The TARA Table is displayed in the diagram pane of the modeling tool.<br /></span><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="TARA Table created.png" /></ac:image></li></ul></li></ol><h3>Adding Threat Scenarios</h3><p>To add Threat Scenarios to the TARA Table</p><hr /><ol><li>In the TARA Table, click Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="Add Existing.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Threat Scenario</strong><strong> </strong>dialog, select the required Threat Scenario.<br /><br /></span><ac:image><ri:attachment ri:filename="Select TS-Dialog.jpg" /></ac:image><br /><br /><p><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="7b589376-fb3c-43cb-b74d-d3ec594130f7">A row is added to the TARA</ac:inline-comment-marker> Table, which shows the existing Threat Scenario.</span><br /><br /><ac:image><ri:attachment ri:filename="Existing TS added.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="77e20d62-232c-4810-8df2-d4c1d4888c49"><ac:rich-text-body><ul><li>Threat Type, Impacted Asset, and <ac:inline-comment-marker ac:ref="a7612104-f5f2-450b-973f-517cbe6aaab5">Damage Scenarios</ac:inline-comment-marker> are automatically added to the TARA Table based on the Damage Scenario Table and Threat Scenarios Table. <span style="color:var(--ds-text,#172b4d);">The association between Threat Scenarios and Damage Scenarios tables is done through failure. The Damage Scenarios which have the same Failure Modes as a given Threat Scenario are taken into account for Risk Values computation.</span></li><li>The risk values are automatically computed according to ISO/SAE 21434:2021 standard. Risk values are read-only values.</li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><h3><span>Assigning Risk Treatment Decision</span></h3><p>To assign Risk Treatment Decision</p><hr /><ul><li><p><span style="color:var(--ds-text,#333333);">  Double-click the cell </span><span style="color:var(--ds-text,#000000);"><span>in the<strong> Risk Treatment Decision</strong> column and the <span style="color:var(--ds-text,#333333);">required </span><ac:inline-comment-marker ac:ref="6f5a9180-4325-47b6-bd76-846e832408b2">Threat Scenario's</ac:inline-comment-marker> </span></span><span style="color:var(--ds-text,#333333);">row. From the drop-down list, assign Risk Treatment Decision.<br /><br /><ac:image><ri:attachment ri:filename="Assigning Risk Treatment Decision.png" /></ac:image><br />The Risk Treatment Decision is assigned in the <ac:inline-comment-marker ac:ref="7acc8642-88b3-462f-8d34-ca4f06afe485">TARA Table</ac:inline-comment-marker>.<br style="text-align: left;" /><br /><ac:image><ri:attachment ri:filename="Risk Treatment Decision assigned.png" /></ac:image><br /></span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="8f7913eb-62eb-4cac-ada5-8e0f0922b472"><ac:rich-text-body><p>If the risk treatment decision is Retain, adding a claim is mandatory. In those cases, the cybersecurity goals and controls are not<span> </span>required.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ul><h3><ac:inline-comment-marker ac:ref="96f9d859-049c-465c-aa24-64e270a761ed">Adding Cybersecurity Goal</ac:inline-comment-marker></h3><p>To add a Cybersecurity Goal to the TARA Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Cybersecurity Goals </strong>column and the required Threat Scenario's row and click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Goal creation_Three dots.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Element</strong><strong> </strong>dialog, select Cybersecurity Goal.</span><br style="text-align: left;" /><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="Select Element dialog_Goal creation.png" /></ac:image><br style="text-align: left;" /><br style="text-align: left;" /><span style="color:var(--ds-text,#333333);">The Cybersecurity Goal is added to the TARA Table.</span><br style="text-align: left;" /><br /></li><li><ac:image><ri:attachment ri:filename="Goal creation_Done.png" /></ac:image></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="1f707f02-74e9-452f-be65-7ab470f0cb77"><ac:rich-text-body><ul><li>You can also add a safety goal from another project (HARA analysis) as a cybersecurity goal. Doing this will create a clone of the safety goal in your project. To add a safety goal as a cybersecurity goal, follow the same procedure as defined above.</li><li>If the ASIL value of the safety goal is inconsistent with the Safety Risk Value of the threat scenario, a validation rule is triggered and the particular row is displayed in red. You can view the error message in the Active Validation Results pane.</li><li>You can mitigate the error by making the ASIL value and the Safety Risk Value consistent with each other.<br /><br /><ac:image><ri:attachment ri:filename="Error.jpg" /></ac:image></li></ul></ac:rich-text-body></ac:structured-macro><p>To Generate/Synchronize the Cybersecurity Goals to the TARA Table</p><hr /><ul><li>Right-click  the threat scenario in the TARA table and select <strong>Generate/Synchronize Cybersecurity Goals.<br /><br /><ac:image><ri:attachment ri:filename="Generate or Synchronize Cybersecurity Goals.png" /></ac:image><br /><br /></strong></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="482534e4-e6ea-48be-8952-8297ceae1473"><ac:rich-text-body><ul><li>The cybersecurity goal is autogenerated based on the following formula:<ul><li><p style="text-align: left;"><span> </span><span style="letter-spacing: 0.0px;"><span class="error" style="color:var(--ds-text,#172b4d);">[Asset Name]</span><span style="color:var(--ds-text,#172b4d);"> of the </span><span class="error" style="color:var(--ds-text,#172b4d);">[Item]</span><span style="color:var(--ds-text,#172b4d);"> shall be protected against </span><span class="error" style="color:var(--ds-text,#172b4d);">[Threat type]</span></span></p></li></ul></li><li>If you add an item, asset or a threat type for a threat scenario, the command <ac:inline-comment-marker ac:ref="8bd65be0-1e49-4d25-9844-40347193bece">autogenerates</ac:inline-comment-marker> a cybersecurity goal.</li><li>If you update an item, asset or a threat type for a threat scenario, the command synchronizes the autogenerated cybersecurity goal. Following are the two scenarios in which synchronization happens:<ul><li>If you rename an item, asset or a threat type, then the existing autogenerated cybersecurity goal is renamed.</li><li>If you add/remove an item, asset or a threat type, then <ac:inline-comment-marker ac:ref="2ac9f00b-da95-40e2-ac69-0550d05bedbe">an </ac:inline-comment-marker>autogenerated cybersecurity goal is added/removed.</li></ul></li><li>You can also select multiple Threat Scenarios and generate/synchronize cybersecurity goals for all the selected Threat Scenarios at once.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Adding Controls</h3><p>To add Controls to the TARA Table</p><hr /><ol><li>Double-click the designated cell in the <strong>Controls </strong>column and the required Threat Scenario's row and click <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Adding control_three dots.png" /></ac:image><br /><br /></li><li><p><span style="color:var(--ds-text,#333333);">From the <strong>Select Elements</strong><strong> </strong>dialog, select Controls.<br /></span><br style="text-align: left;" /><ac:image><ri:attachment ri:filename="Select Element dialog.png" /></ac:image></p><p><br style="text-align: left;" /><span style="color:var(--ds-text,#333333);">The Controls are added to the TARA Table.<br /><br /><ac:image><ri:attachment ri:filename="Controls added.png" /></ac:image><br /></span></p><p><span style="color:var(--ds-text,#333333);"> </span></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="134e66d9-b566-4d6b-a8f1-a28a54abcc70"><ac:rich-text-body><p>Controls are a list of Cybersecurity Requirements. There are 4 types of Cybersecurity Requirements: Functional, Technical, Hardware, and Software.</p></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></li></ol><p>To ease the process of adding controls, the plugin provides a feature to add the controls with the aid of the Recommend Control command. The controls are recommended on the basis of assigned cybersecurity goals and CWE elements used as attack path steps.</p><p>To add controls using the Recommend Control command to the TARA Table</p><hr /><ol><li>Right-click the threat scenario in the TARA table and select <strong>Recommended Control,</strong> as follows:<br /><br /><ac:image><ri:attachment ri:filename="Recommended Controls.png" /></ac:image><br /><br /></li><li><p><span style="color:var(--ds-text,#333333);">From the <strong>Select Elements </strong>dialog, select or remove the recommended controls.<br /><br /><ac:image><ri:attachment ri:filename="Select Elements Dialog.png" /></ac:image><br /></span></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="14a75f63-82fb-4424-b1e2-de4fba1e9d60"><ac:rich-text-body><p>For requirements to be reflected as recommended controls in the Select Elements dialog, either of these conditions should be satisfied:</p><ul><li>A Threat scenario should have assigned cybersecurity goals with all the derived requirements.<br /><br /><ac:image ac:height="400"><ri:attachment ri:filename="Dreived Requirements.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#172b4d);">A Threat Scenario should have an Attack Path, which itself has a step, which is either a CWE or a Technique. In such case, if the CWE or Technique has a Recommendation from a Cybersecurity Requirement, then that requirement will be automatically proposed by <strong>Recommend control </strong>command.</span></li></ul></ac:rich-text-body></ac:structured-macro><p><span style="color:var(--ds-text,#333333);"> </span></p><span style="color:var(--ds-text,#333333);">The recommended controls are added to the TARA Table.<br /><br /><ac:image><ri:attachment ri:filename="Recommended Controls_Added.png" /></ac:image><br /></span></li></ol><h3><span>Adding Claim</span></h3><p>To add a Claim to the TARA Table</p><hr /><ul><li><p>Double-click the cell in the <strong>Claims </strong>column and the required Threat Scenario's row and type in the necessary Claim. <br /><br /><ac:image><ri:attachment ri:filename="Adding claim.png" /></ac:image></p><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="fbac0599-a233-4659-a473-5460133a0011"><ac:rich-text-body><p>If the risk treatment decision is Retain, adding a claim is mandatory. In those cases, the cybersecurity goals and controls are not required <span style="color:var(--ds-text,#333333);">and cannot be specified.</span></p></ac:rich-text-body></ac:structured-macro><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7a794356-545a-4198-8751-3c2a1fb2df47"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">Due to some performance reason, the claim does not appear in the containment tree directly after specifying it in the claim's cell. You must save the project to see the claims in the containment tree under the smart package <strong>2.3 Cybersecurity Claims</strong>.</span></p></ac:rich-text-body></ac:structured-macro></li></ul><h3>Assigning Residual Risk Value</h3><p>To assign the Residual Risk value in the TARA Table</p><hr /><ul><li><span style="color:var(--ds-text,#333333);">Double-click Residual </span><span style="color:var(--ds-text,#000000);"><span>Safety Risk value cell in the Threat Scenario </span></span><span style="color:var(--ds-text,#333333);">row. From the drop-down list, select the R</span>esidual Safety R<span style="letter-spacing: 0.0px;color:var(--ds-text,#000000);">isk Value</span><span style="letter-spacing: 0.0px;">. <span>Follow the same procedure to assign Financial, Operational and Privacy Residual Risk Values.</span> <br /><br /><ac:image><ri:attachment ri:filename="Residual Risk Value.png" /></ac:image><br /></span></li></ul><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="31b9396c-f9c0-4833-9f01-ad1aa50158d4"><ac:rich-text-body><ul><li><span>You can add custom residual risk value in between the given range of 1.0 to 5.0, such as 1.2, 3.7 or 0.3.</span></li><li><span>You can also assign the residual risk value with help of the Specification dialog of the Threat Scenario.</span></li><li><span style="color:var(--ds-text,#333333);">The maximum value among all the residual risk values viz. Safety, Financial, Operational, and Privacy is considered as the Residual Global Risk Value.</span></li></ul></ac:rich-text-body></ac:structured-macro><h3 class="auto-cursor-target">TARA Table Example</h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="7c53fe9f-4eba-4f52-9c80-3bdd2b2a14c4"><ac:rich-text-body><ul><li>The Safety, Financial, Operational, Privacy risk values are calculated automatically by using following formula:<ul><li>Risk Value =  1 + Maximum(Impact) * Aggregated Attack Feasibility Rating<br /><br /><ac:image><ri:attachment ri:filename="Impact Rating.png" /></ac:image><br /><br /></li></ul></li><li><span style="color:var(--ds-text,#333333);">The maximum value among all the risk values viz. Safety, Financial, Operational, and Privacy is considered as the Global Risk Value.</span></li></ul></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="1 TARA_illustration.png" /></ac:image></p></ac:layout-cell></ac:layout-section></ac:layout>
````

<!--NOMAGIC_PAGE id=227164799 space=SCD2024xR3 version=3 -->
## PAGE 00029: Threat  scenario

- page_id: `227164799`
- space_key: `SCD2024xR3`
- source_url: https://docs.nomagic.com/spaces/SCD2024xR3/pages/227164799/Threat+scenario
- version_number: 3
- version_date: `2025-11-18T11:04:38.276+01:00`
- ancestors: Systems Cybersecurity Designer > ISO 21434 Functional Cybersecurity > Table
- labels: []

### NORMALIZED CONTENT

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

You can group the custom-created threat types by creating custom packages and placing them under the custom packages. To create a new package, you must create a generalization set of the required custom threat types.To learn more about creating a generalization set, refer to[CONFLUENCE_PAGE title='Generalization set' space='MD2024xR3'].

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
<ac:layout><ac:layout-section ac:type="single"><ac:layout-cell><p><strong>Threat Scenario</strong></p><p><span style="color:var(--ds-text,#333333);">Potential cause of compromise of cybersecurity properties of one or more assets  in order to realize a damage scenario.</span></p><p><strong>Attack Path</strong></p><p>Set of deliberate actions to realize a threat scenario.</p><p><strong>Failure</strong></p><p>Termination of an intended behavior of an element or an item due to a fault manifestation.</p></ac:layout-cell></ac:layout-section><ac:layout-section ac:type="single"><ac:layout-cell><h3>Creating a Threat Scenario</h3><p>To create a Threat Scenario</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Containment tree, right-click<span> </span><strong>Threat Scenario</strong><span> </span>and select</span><strong style="text-align: left;"><span> </span>Create Element.<br /><br /><ac:image><ri:attachment ri:filename="1 ClickCreateElement.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">Do one of the following:</span><ul style="text-align: left;"><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO 21434 </strong>and select <strong>Threat Scenario</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="3 DirectlySelectThreatScenario.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword <strong>threat</strong> and then select<span> </span><strong>Threat Scenario.<br /><br /><ac:image><ri:attachment ri:filename="2 WriteThreat.png" /></ac:image><br /><br /></strong></li></ul></li><li><span style="color:var(--ds-text,#333333);">Name the created Threat Scenario in the Containment tree and press Enter. The Threat Scenario has the prefix <span><strong>D</strong></span><strong>S</strong>,<span> </span>which denotes that the created element is a Threat Scenario; the number<span> </span><strong style="text-align: left;">1</strong> indicates that it is the first Threat Scenario created.<br /><br /><ac:image><ri:attachment ri:filename="4 ThreatScenarioCreated.png" /></ac:image><br /></span></li></ol><h3><span style="color:var(--ds-text,#333333);">Creating a Threat Scenario Table<br /></span></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="8bfaf83d-4424-4723-83be-76cbbc167205"><ac:rich-text-body><p><span style="color:var(--ds-text,#172b4d);">If you create a new project using the </span><strong style="text-align: left;">ISO 21434 Project<span> </span></strong>template<span style="color:var(--ds-text,#172b4d);">, then a<span> </span><strong>Threat Scenario Table<span> </span></strong>already exists in the<span> <strong>1.2 Threat Scenarios</strong></span><span> </span>package.</span></p></ac:rich-text-body></ac:structured-macro><p><br /></p><p>To create a<span> </span><span style="color:var(--ds-text,#333333);">Threat Scenario<span> </span></span>Table</p><hr /><ol><li><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">In the Containment tree, right-click</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><strong><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">Threat Scenario</ac:inline-comment-marker></strong><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">and select</ac:inline-comment-marker><strong><span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83"> </ac:inline-comment-marker></span><ac:inline-comment-marker ac:ref="520a36b8-3d14-4a04-a353-74c1682c8c83">Create Diagram.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Create Diagram.png" /></ac:image><br /><br /></strong></li><li>Do one of the following:<ul><li><span style="color:var(--ds-text,#333333);">In the dialog, expand <strong>ISO</strong> <strong>21434 </strong>and select <strong>Threat Scenario Table</strong>.<br /></span><strong><br /><ac:image><ri:attachment ri:filename="Threat Scenario Table_Menu.png" /></ac:image><br /><br /></strong></li><li class="auto-cursor-target">In the search tab, type the keyword threat and then select<span> </span><strong>Threat Scenario Table.<br /><br /><ac:image ac:thumbnail="true" ac:height="196"><ri:attachment ri:filename="Threat Scenario Table_Search.png" /></ac:image><br /><br /></strong>The Threat Scenario Table is now displayed in the diagram pane of the modeling tool.<br /><br /><ac:image><ri:attachment ri:filename="Threat Scenario Table.png" /></ac:image></li></ul></li></ol><h3>Adding a Threat Scenario to the Threat Scenario Table</h3><p>To add a new Threat Scenario to the Threat Scenario Table</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Threat Scenario Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add New. </strong><span style="color:var(--ds-text,#333333);">A row is added in the Threat Scenario Table, which shows the new Threat Scenario.</span><strong style="text-align: left;"><br /><br /><ac:image><ri:attachment ri:filename="1 ClickAddNew.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">In the newly created Threat Scenario's row and the <strong>Name </strong>column, double-click the designated cell to name the Threat Scenario.<br /><br /><strong style="text-align: left;"><ac:image><ri:attachment ri:filename="2 AfterAddingThreatScenario.png" /></ac:image></strong><br /></span><strong style="text-align: left;"><br style="text-align: left;" /></strong></li></ol><p><span style="color:var(--ds-text,#333333);">To add an existing Threat Scenario to the Threat Scenario Table</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">In the Threat Scenario Table, click</span><span style="color:var(--ds-text,#333333);"> </span><strong style="text-align: left;">Add Existing.<br /><br /><ac:image><ri:attachment ri:filename="3 ClickAddExisting.png" /></ac:image><br /><br /></strong></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Threat Scenario</strong> dialog, select the required Threat Scenario. A row is added to the Threat Scenario Table, showing the existing Threat Scenario.<br /><br /><ac:image><ri:attachment ri:filename="Threat Scenario Dialog.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);"> In the existing Threat Scenario's row and the <strong>Name </strong>column, double-click the designated cell to rename the Threat Scenario.<br /><br /><strong style="text-align: left;"><ac:image ac:height="249"><ri:attachment ri:filename="2 AfterAddingThreatScenario.png" /></ac:image></strong><br /></span></li></ol><h3><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="668ed2cf-1efb-41ff-8f28-6c23538b037a">Creating a custom threat type</ac:inline-comment-marker></span></h3><p><span style="color:var(--ds-text,#333333);">To create a custom threat type</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Create a general threat scenario as defined in the <ac:link ac:anchor="Creating a Threat Scenario" /> section.</span></li><li><span style="color:var(--ds-text,#333333);">Open the Specification dialog of the newly created threat scenario in the <strong>Expert</strong> mode.</span></li><li><span style="color:var(--ds-text,#333333);">Set the <strong>Is Abstract</strong> property to <em>True</em>.<br /><br /><ac:image><ri:attachment ri:filename="Specification Dialog.png" /></ac:image><br /><br />The newly created threat scenario will now be displayed in italics in the Containment tree and will be available under the <strong>custom </strong>package in the Select Threat Type dialog. <br /><br /></span><ac:image><ri:attachment ri:filename="Custom Threat Type.png" /></ac:image><br /><br /></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="6844d142-575d-4c9d-be5f-b2833b703c80"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);"><span style="color:var(--ds-text,#172b4d);">Threat Types are displayed by default in the TARA analysis as Threat Scenarios. To prevent that, you must create the Threat Types in a dedicated package or library.</span></span></p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="86496062-e728-4cc2-a157-ff38237b101e">Creating custom packages for custom-created threat types</ac:inline-comment-marker></h3><p>You can group the custom-created threat types by creating custom packages and placing them under the custom packages. <span>To create a new package, you must create a generalization set of the required custom threat types. </span><span>To learn more about creating a generalization set, refer to </span><ac:link><ri:page ri:space-key="MD2024xR3" ri:content-title="Generalization set" /></ac:link><span>.<br /><br /></span></p><p><ac:image ac:align="center"><ri:attachment ri:filename="Generalization set_Threat Type.png" /></ac:image></p><h6 style="text-align: center;">Select Threat Type dialog showing the custom threat types places under the custom created packages.<br /><br /></h6><p>The following example displays a typical scenario in which a generalization set can be created.</p><p><ac:image ac:align="center"><ri:attachment ri:filename="Generalizarion Example.png" /></ac:image></p><h6 style="text-align: center;">Generalization set example.</h6><h3><ac:inline-comment-marker ac:ref="b2a3beea-cf3f-4e8e-877a-7e54200c78ee">Creating subcategory for the custom-created threat type</ac:inline-comment-marker></h3><p><span style="letter-spacing: 0.0px;">You can also create subcategories of the custom-created threat types. Doing so will create a nesting effect in the Select Threat Type dialog.<br /><br /></span></p><p style="text-align: center;"><span style="letter-spacing: 0.0px;"><ac:image><ri:attachment ri:filename="Nesting Effect.png" /></ac:image></span></p><h6 style="text-align: center;">Select Threat Type dialog showing the nesting effect due to subcategorization of the threat types.</h6><p><br /></p><p>To create subcategories of the custom-created threat type</p><hr /><ol><li>In the <span style="color:var(--ds-text,#333333);">Specification dialog of the newly created threat Type, click <ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image> in the<strong style="text-align: left;"> <span style="color:var(--ds-text,#172b4d);">Base Classifier</span></strong> property.<br /><br /><ac:image><ri:attachment ri:filename="Custom Subcategory for threat type.png" /></ac:image><br /><br /></span></li><li><span style="color:var(--ds-text,#333333);">Select any parent threat type under which you want to place the newly created custom threat type.<br /><br /><ac:image><ri:attachment ri:filename="Select Class dialog.png" /></ac:image><br /></span></li></ol><h3>Adding a Threat Type</h3><p><span style="color:var(--ds-text,#333333);">To add a Threat Type</span></p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Double-click the designated cell in the <strong>Threat Type </strong></span><span style="color:var(--ds-text,#333333);">column <ac:inline-comment-marker ac:ref="c03df453-8eef-4927-9271-99fd6a3835b7">and</ac:inline-comment-marker> the required Threat Scenario's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.<br /><br /><ac:image><ri:attachment ri:filename="Edit_Button_Three_Dots.png" /></ac:image><br /><br /></span></span></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Threat Type </strong>dialog, <ac:inline-comment-marker ac:ref="2d78d067-b411-4118-8db0-7620df8624af">select a threat type(s)</ac:inline-comment-marker> from either the <strong><a href="https://en.wikipedia.org/wiki/STRIDE_%28security%29"> STRIDE </a></strong>or <strong><a href="https://unece.org/sites/default/files/2023-02/R155e%20%282%29.pdf"> UNECE </a></strong>package. You can also select a custom-created threat type.<br /><br /><ac:image><ri:attachment ri:filename="Nesting Effect.png" /></ac:image><br /></span><br /><span style="color:var(--ds-text,#333333);">The Threat Type will be added to the Threat Scenarios Table.</span><br /><br /><ac:image><ri:attachment ri:filename="Threat Type Applied.png" /></ac:image></li></ol><h3>Adding an Attack Path</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="c581d357-c34b-43b7-a2cb-efc6411e9256"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">You can add multiple attack paths for a given Threat Scenario.</span></p></ac:rich-text-body></ac:structured-macro><p>To add an Attack Path</p><hr /><ol><li><span style="color:var(--ds-text,#333333);">Double-click the designated cell in the <strong>Attack Path </strong></span><span style="color:var(--ds-text,#333333);">column and the required Threat Scenario's row and cl<span>ick <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Three dot-Attack Path Steps.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From <ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">Select Elements</ac:inline-comment-marker></strong><strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85"> </ac:inline-comment-marker></strong><ac:inline-comment-marker ac:ref="179657e3-77c6-4b8c-8658-e11c1da6ac85">dialog, select Attack</ac:inline-comment-marker> Path.<br /><br /><ac:image><ri:attachment ri:filename="Select Element_Attack Path.png" /></ac:image><br /></span><span style="color:var(--ds-text,#333333);"><br /><ac:inline-comment-marker ac:ref="ed16e46c-9c6e-4aea-8b13-97eab5097f69">The Attack Path is added to the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Attack Path added.png" /></ac:image><br style="text-align: left;" /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="7a5f66ac-ca84-4422-a7e4-11e5ddccf5bb"><ac:rich-text-body><ul><li>You can also drag and drop the Attack Paths from the Containment tree to the Threat Scenario Table.</li><li>The Aggregated Attack Feasibility Rating is added automatically after you add the Attack Path.</li></ul></ac:rich-text-body></ac:structured-macro><h3>Adding a Failure</h3><p>To add a Failure</p><hr /><ol><li><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">Double-click the designated cell in the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">Failure </ac:inline-comment-marker></strong></span><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">column and the required Threat Scenario's row and cl</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="c6598fc0-d4e2-4946-b5a4-ea1e5bf0d8f9">ick</ac:inline-comment-marker> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Adding Failure_Three dot.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Class</strong><strong> </strong>dialog, select Failure.<br /><br /><ac:image><ri:attachment ri:filename="2 SelectFailureWindow_v2.png" /></ac:image><br /></span><span style="color:var(--ds-text,#333333);"><br /><ac:inline-comment-marker ac:ref="40a0d885-7391-4f2a-9357-e7d0abf552bf">The Failure is now shown in the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Failure added.png" /></ac:image><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="88ded4ef-a5bc-47f5-96bf-2d2829c714ab"><ac:rich-text-body><p>You can also drag and drop the Failure modes from the Containment tree to the Threat Scenario Table.</p></ac:rich-text-body></ac:structured-macro><h3>Adding an Impacted Asset</h3><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="415c82df-db8d-4115-a637-19735c45920e"><ac:rich-text-body><p><span style="color:var(--ds-text,#333333);">You can add multiple Impacted Assets for a given Threat Scenario.</span></p></ac:rich-text-body></ac:structured-macro><p>To add an Impacted Asset</p><hr /><ol><li><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">Double-click the designated cell in the </ac:inline-comment-marker><strong><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">Impacted Asset </ac:inline-comment-marker></strong></span><span style="color:var(--ds-text,#333333);"><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">column and the required Threat Scenario's row and cl</ac:inline-comment-marker><span><ac:inline-comment-marker ac:ref="510969eb-54e6-41ab-8b3b-1816fa656bfc">ick</ac:inline-comment-marker> <span class="confluence-embedded-file-wrapper confluence-embedded-manual-size" style="color:var(--ds-text,#333333);"><ac:image ac:thumbnail="true" ac:height="15"><ri:attachment ri:filename="Three Dot _Icon.png" /></ac:image></span>.</span></span><br /><br /><ac:image><ri:attachment ri:filename="Adding Impacted Assets.png" /></ac:image><br /><br /></li><li><span style="color:var(--ds-text,#333333);">From the <strong>Select Element</strong><strong> </strong>dialog, select Impacted Asset.<br /><br /><ac:image><ri:attachment ri:filename="1 SelectAssetWindow_v2.png" /></ac:image><br /></span><span style="color:var(--ds-text,#333333);"><br /><ac:inline-comment-marker ac:ref="e96f5570-448a-43bc-8157-2a3e4b973c59">The Impacted Asset is added to the Threat Scenario Table.</ac:inline-comment-marker><br /><br /><ac:image><ri:attachment ri:filename="Impacted Asset added.png" /></ac:image><br /></span></li></ol><ac:structured-macro ac:name="note" ac:schema-version="1" ac:macro-id="b020098c-6c00-47ee-b5df-0adb690f9033"><ac:rich-text-body><p>You can also drag and drop the Impacted Assets from the Containment tree to the Threat Scenario Table.</p></ac:rich-text-body></ac:structured-macro><h3><ac:inline-comment-marker ac:ref="4c718e6a-c1af-4784-8d55-2e7af05d5dfa">Threat Scenario Table Example</ac:inline-comment-marker></h3><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="a22e06b7-0a8c-4b90-a2da-d78dd453ed8d"><ac:rich-text-body><p>The maximum value among all the attacks paths for the given threat scenario is considered as the Aggregated Attack Feasibility Rating.</p></ac:rich-text-body></ac:structured-macro><p><ac:image><ri:attachment ri:filename="Threat Scenario Example.png" /></ac:image></p><ac:structured-macro ac:name="info" ac:schema-version="1" ac:macro-id="913c17ef-41fc-4abc-9236-e55fcf09aa7a"><ac:parameter ac:name="title">References</ac:parameter><ac:rich-text-body><ul><li><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO/SAE 21434:2021 Road vehicles-Cybersecurity engineering</a></li><li><a class="external-link" href="https://www.iso.org/obp/ui/fr/">ISO 26262-1:2018 Road vehicles-Functional safety</a></li></ul></ac:rich-text-body></ac:structured-macro><p class="auto-cursor-target"><br /></p></ac:layout-cell></ac:layout-section></ac:layout>
````
