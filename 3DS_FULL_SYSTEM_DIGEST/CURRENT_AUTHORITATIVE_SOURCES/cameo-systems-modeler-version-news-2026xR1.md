# CURRENT AUTHORITATIVE SOURCE: Magic Cyber Systems Engineer / Cameo Systems Modeler

- source_url: https://docs.nomagic.com/VN/2026x-refresh1/magic-cyber-systems-engineer-cameo-systems-modeler-314179731.html
- source_bytes: 94035
- source_sha256: `ac77dd65dba6576e9ddf2c919156c3477fd89c261a66ae87f788726daa9e02df`
- captured_utc: `2026-07-14T16:49:06.448280+00:00`

## NORMALIZED CONTENT

Magic Cyber Systems Engineer / Cameo Systems Modeler
Released on: June 26, 2026
The 2026x Refresh1 release introduces multiple improvements to SysML v1 modeling, simulation, and client-side collaborative modeling capabilities.
SysML v1 modeling now offers enhanced import from Excel files, supporting nested connectors.
Model simulation improvements include instance selection for behavioral diagrams, allowing you to filter animation for a single object in State Machine, Activity, and Sequence diagrams. In addition, UI mockups now support unit symbols, and a new
Show Units
property lets you control whether units are displayed in diagrams and mockups.
In client-side collaborative modeling, Partial Project Usages is now out of the technology preview phase and offers a smoother user experience for defining usage scope. Additionally, the feature for saving projects to an earlier version has been improved so that all used projects are saved together with the open project, and Teamwork Cloud projects can now be saved to an earlier version as .mdzip files.
SysML v1 Features
Nested Connector Import
Import from Excel files has been enhanced to support nested connectors. You can now define connectors between elements located at different levels of the model structure, and the tool will automatically construct the corresponding nested connector paths during import.
This improvement enables accurate reconstruction of complex internal structures directly from external data sources, reducing manual adjustments and improving modeling efficiency.
Learn more >>
Simulation Features
Instance Selection in Behavioral Diagrams
The 2026x Refresh1 version of the plugin allows you to filter animation for one specific object in State Machine, Activity, and Sequence diagrams.
If several instances of the same behavior exist, the diagram automatically shows animation only for the first instance annotated in the diagram. This prevents the diagram from merging events from multiple concurrent instances and improves clarity during simulation analysis. You can switch the displayed instance from the contextual menu.
Selecting the Instance to be animated in a State Machine Diagram.
UI Mockup Improvements
This release introduces the ability to display the unit symbol in UI mockups. In addition, a new Simulation Configuration property —
Show Units
— allows you to control whether units are displayed in diagrams and UI mockups.
Displaying units in UI mockups
Other Improvements
Time Series and Timeline Charts now support negative time values.
UI mockups, graphs, and other elements generated during model execution are displayed with an automatic offset, making them easier to rearrange. In addition, the adjusted layout is now preserved between execution runs.
Collaboration in Teamwork Cloud
Partial Project Usages
We are excited to announce that Partial Project Usages is now out of the technology preview phase, featuring a significantly improved overall user experience. As in previous releases, the feature allows you to define the usage scope by selecting a specific part of a project, and enables seamless switching between full and partial usages as well as easy adjustment of the usage scope at any time.
Learn more >>
Partial project usage
Saving Projects to an Earlier Version
The previous release introduced the ability to save projects to an earlier major version—for example, from version 2026x to 2024x—making it easier to collaborate with teams using older versions of the modeling tool.
In version 2026x Refresh1, this functionality brings the following improvements:
If your project uses other projects, all used projects are saved together with the open project.
You can now save Teamwork Cloud projects to an older version as .mdzip files without first saving them locally.
SysML v2 Project Migration to Version 2026x Refresh1
The new release supports several options for migrating
SysML v2 projects
to version 2026x Refresh1. You can migrate all or selected projects on the Teamwork Cloud server in bulk via the
Collaborate
menu, or migrate standalone Teamwork Cloud or local repository projects by opening them and agreeing to update standard libraries.
Back to top
Documentation
Magic Cyber Systems Engineer / Cameo Systems Modeler 2026x Refresh1
×

## EXACT MAIN HTML

````html
<main>
<span id="admin-menu-link" style="display: none; position: absolute; top:-5000px;"></span>
<div class="grid-container article full">
<div class="grid-x article__content" data-sticky-container="">
<div class="cell large-2 article__navigation show-for-large">
<div data-options="marginTop:8;" data-sticky="">
<div class="page-tree-collapser"></div>
</div>
<div data-btm-anchor="article-content:bottom" data-options="marginTop:8;" data-sticky="" data-top-anchor="article-content" id="js-desktop-pageTree">
<ul aria-hidden="false" class="vertical menu js-loading accordion-menu renderPageTree scroll-y" data-accordion-menu="" data-current="/VN/2026x-refresh1/magic-cyber-systems-engineer-cameo-systems-modeler-314179731.html" data-root="/VN/2026x-refresh1/2026x-refresh1-version-news-314179593.html" data-submenu-toggle="true" data-viewport-id="AC1032020199C466FD24A2C8640CCE1F">
<li class="js-loading js-loading__stacked js-loading__stacked--listItem"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem js-loading__stacked--listItem--short"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem js-loading__stacked--listItem--short"></li>
<li class="js-loading js-loading__stacked js-loading__stacked--listItem"></li>
</ul>
</div>
</div>
<div class="cell medium-auto grid-container full js-loading" id="article-content">
<article class="grid-x" role="article">
<header class="cell grid-x">
<nav aria-label="You are here:" class="cell medium-11" role="navigation">
<ul class="breadcrumbs js-loading js-loading__stacked js-loading__stacked--breadcrumb">
<li class="js-hide-until-loaded"><a href="/VN/2026x-refresh1/2026x-refresh1-version-news-314179593.html" rel="prev" target="_self">Version News</a></li>
<li class="breadcrumbs--active js-hide-until-loaded"><span class="show-for-sr">Current: </span>Magic Cyber Systems Engineer / Cameo Systems Modeler</li>
</ul>
</nav>
<h1 class="cell article__heading js-loading js-loading__stacked js-loading__stacked--heading" role="heading"><span class="js-hide-until-loaded">Magic Cyber Systems Engineer / Cameo Systems Modeler</span></h1>
</header>
<section class="cell page" id="content" role="main">
<div class="cell wiki-content js-tocBot-content js-hide-until-loaded hc-content-width--wide" id="main-content">
<div class="conf-macro output-block" data-hasbody="true" data-macro-name="sp-pagelayout"><div class="sp-grid-section">
<div class="sp-grid-cell sp-grid-100">
<h6 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-top" style="text-align: center;"><span class="conf-macro output-inline" data-hasbody="false" data-macro-name="sp-anchor"><span class="confluence-anchor-link" id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-top"></span><span id="top"></span></span></h6><h6 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-Releasedon:June26,2026" style="text-align: center;">Released on: June 26, 2026</h6><p><br/></p><p class="isSelectedEnd"><span>The 2026x Refresh1 release introduces multiple improvements to SysML v1 modeling, simulation, and client-side collaborative modeling capabilities.</span></p><p class="isSelectedEnd"><span>SysML v1 modeling now offers enhanced import from Excel files, supporting nested connectors.</span></p><p class="isSelectedEnd"><span>Model simulation improvements include instance selection for behavioral diagrams, allowing you to filter animation for a single object in State Machine, Activity, and Sequence diagrams. In addition, UI mockups now support unit symbols, and a new </span><strong><span>Show Units</span></strong><span> property lets you control whether units are displayed in diagrams and mockups.</span></p><p><span>In client-side collaborative modeling, Partial Project Usages is now out of the technology preview phase and offers a smoother user experience for defining usage scope. Additionally, the feature for saving projects to an earlier version has been improved so that all used projects are saved together with the open project, and Teamwork Cloud projects can now be saved to an earlier version as .mdzip files.</span></p>
</div>
</div>
<div class="sp-grid-section">
<div class="sp-grid-cell sp-grid-100">
<p><br/></p>
</div>
</div>
<div class="sp-grid-section">
<div class="sp-grid-cell sp-grid-100">
<h2 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-SysMLv1Features">SysML v1 Features</h2><h3 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-NestedConnectorImport">Nested Connector Import</h3><p>Import from Excel files has been enhanced to support nested connectors. You can now define connectors between elements located at different levels of the model structure, and the tool will automatically construct the corresponding nested connector paths during import. <span>This improvement enables accurate reconstruction of complex internal structures directly from external data sources, reducing manual adjustments and improving modeling efficiency. <a href="https://docs.nomagic.com/MT/?contextKey=Importing-data-from-Excel-and-CSV-files&amp;version=2026x Refresh1&amp;variant=default" rel="nofollow">Learn more &gt;&gt;</a></span></p><p style="text-align: center;"><span class="confluence-embedded-file-wrapper image-center-wrapper conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image image-center" src="/VN/files/2026x-refresh1/314179731/314179737/1/1781598630682/Nested+Connector+Import.png"/></span></p><h2 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-SimulationFeatures">Simulation Features</h2><h3 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-InstanceSelectioninBehavioralDiagrams">Instance Selection in Behavioral Diagrams</h3><p><span style="color:var(--ds-text,#172b4d);">The 2026x Refresh1 version of the plugin allows you to filter animation for one specific object in State Machine, Activity, and Sequence diagrams.<span> </span></span>If several instances of the same behavior exist, the diagram automatically shows animation only for the first instance annotated in the diagram. This prevents the diagram from merging events from multiple concurrent instances and improves clarity during simulation analysis. You can switch the displayed instance from the contextual menu.</p><h6 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-instance_selection.pngSelectingtheInstancetobeanimatedinaStateMachineDiagram." style="text-align: center;"><span class="confluence-embedded-file-wrapper conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image" src="/VN/files/2026x-refresh1/314179731/314179736/1/1781598630659/instance_selection.png"/></span><br/> Selecting the Instance to be animated in a State Machine Diagram.</h6><h3 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-UIMockupImprovements">UI Mockup Improvements</h3><p>This release introduces the ability to display the unit symbol in UI mockups. In addition, a new Simulation Configuration property — <strong>Show Units</strong> — allows you to control whether units are displayed in diagrams and UI mockups.</p><p style="text-align: center;"><span class="confluence-embedded-file-wrapper conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image" src="/VN/files/2026x-refresh1/314179731/314179733/1/1781598630580/units_in_ui_mockups.png"/></span></p><h6 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-DisplayingunitsinUImockups" style="text-align: center;"><span>Displaying units in UI mockups</span></h6><h3 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-OtherImprovements">Other Improvements</h3><ul><li data-uuid="aa1d0f4d-671e-469e-a1a1-885eeed09383">Time Series and Timeline Charts now support negative time values.</li><li data-uuid="f137ce23-7245-4c04-b009-911762469bb5">UI mockups, graphs, and other elements generated during model execution are displayed with an automatic offset, making them easier to rearrange. In addition, the adjusted layout is now preserved between execution runs.</li></ul><h2 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-CollaborationinTeamworkCloud"><span>Collaboration in Teamwork Cloud</span></h2><h3 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-PartialProjectUsages">Partial Project Usages</h3><p><span>We are excited to announce that Partial Project Usages is now out of the technology preview phase, featuring a significantly improved overall user experience. As in previous releases, the feature allows you to define the usage scope by selecting a specific part of a project, and enables seamless switching between full and partial usages as well as easy adjustment of the usage scope at any time.</span></p><p><span><a href="https://docs.nomagic.com/CM/?contextKey=using-server-projects&amp;version=2026x%20Refresh1" rel="nofollow">Learn more &gt;&gt;</a></span></p><p style="text-align: center;"><span class="confluence-embedded-file-wrapper conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image" src="/VN/files/2026x-refresh1/314179731/314179734/1/1781598630614/partial_project_usage_GA.png"/></span></p><h6 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-Partialprojectusage" style="text-align: center;">Partial project usage</h6><h3 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-SavingProjectstoanEarlierVersion">Saving Projects to an Earlier Version</h3><p><span>The previous release introduced the ability to save projects to an earlier major version—for example, from version 2026x to 2024x—making it easier to collaborate with teams using older versions of the modeling tool.</span></p><p>In version 2026x Refresh1, this functionality brings the following improvements:</p><ul style="text-align: left;"><li data-uuid="cdc977aa-22cc-42e1-b731-e58ca074d0e9">If your project uses other projects, all used projects are saved together with the open project.</li><li data-uuid="7881c179-2db3-492e-91ea-730004e255fe">You can now save Teamwork Cloud projects to an older version as .mdzip files without first saving them locally.</li></ul><h3 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-SysMLv2ProjectMigrationtoVersion2026xRefresh1">SysML v2 Project Migration to Version 2026x Refresh1</h3><p>The new release supports several options for migrating <strong>SysML v2 projects</strong> to version 2026x Refresh1. You can migrate all or selected projects on the Teamwork Cloud server in bulk via the <strong>Collaborate</strong> menu, or migrate standalone Teamwork Cloud or local repository projects by opening them and agreeing to update standard libraries.</p><p style="text-align: right;"><span><a class="conf-macro output-inline" data-hasbody="true" data-macro-name="sp-plaintextbody-link" href="#id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-top">Back to top</a></span></p>
</div>
</div>
<div class="sp-grid-section">
<div class="sp-grid-cell sp-grid-100">
<h2 id="id-(2026xRefresh1)MagicCyberSystemsEngineer/CameoSystemsModeler-Documentation">Documentation</h2><ul><li data-uuid="7beca90e-fd8e-4406-b617-e8bde65f5dc7"><a href="https://docs.nomagic.com/MT/?contextKey=modeling-tools-documentation&amp;version=2026x%20Refresh1&amp;variant=Magic%20Cyber%20Systems%20Engineer%20%2F%20Cameo%20Systems%20Modeler" rel="nofollow">Magic Cyber Systems Engineer / Cameo Systems Modeler 2026x Refresh1</a></li></ul>
</div>
</div>
</div>
<div class="table-overlay full reveal" data-reveal="" id="tableOverlay">
<button aria-label="Close modal" class="close-button table-overlay__close" data-close="" type="button">
<span aria-hidden="true">×</span>
</button>
<div class="article__content table-overlay__content"></div>
</div>
</div>
</section>
</article>
</div>
<div class="cell xlarge-2 article__toc show-for-xlarge">
<div class="scroll-y padding-bottom-3" data-btm-anchor="article-content:bottom" data-options="marginTop:8;" data-sticky="" data-top-anchor="article-content">
<div class="js-tocBot">
</div>
</div>
</div>
</div>
</div>
</main>
````
