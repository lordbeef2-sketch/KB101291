# CURRENT AUTHORITATIVE SOURCE: Magic Collaboration Studio / Teamwork Cloud and Services

- source_url: https://docs.nomagic.com/VN/2026x-refresh1/magic-collaboration-studio-teamwork-cloud-and-services-314179937.html
- source_bytes: 100570
- source_sha256: `948ae60c0fada1fc5a5e1361705046a0e7b0cc749eb3ef7194da1f08a158c636`
- captured_utc: `2026-07-14T16:49:07.570293+00:00`

## NORMALIZED CONTENT

Magic Collaboration Studio / Teamwork Cloud and Services
Released on: June 26, 2026
One of the most important additions in 2026x Refresh1 is
MagicLab Collaborator, introduced to enable collaborative work on SysML v2 projects with branch-based feedback, commenting, and multi-branch review capabilities.
2026x Refresh1 release also delivers a brand
new Resource Usage Map for SysML v2 resources that enhances impact analysis and a
modernized Web Application Platform home page with a cleaner design and improved usability
. Additional improvements include automatic SAML login redirection and configurable parallel execution of synchronization jobs.
Cameo Collaborator introduces a new Reader mode for distraction-free viewing, text comparison directly within tables, enhanced PDF export options with automatic tables of figures, diagrams, and tables, smoother zooming, and the ability to edit the To Do property.
MagicLab Collaborator
We introduce MagicLab Collaborator, a service that enables teams to collaborate on SysML v2 projects. Building on the capabilities of MagicLab, which is a read-only viewer, MagicLab Collaborator includes flexible collaboration features such as branch-specific feedback, commenting with search and editing, and support for working across multiple branches. Users can also open and review both current and historical branches, improving traceability and team coordination.
Commenting
Commenting features, available with a Cameo Collaborator license, provide flexible ways to collaborate on specific elements and to view all comments of the project with easy navigation.
Viewing comments for a specific element in the element Specification panel.
Commenting features of MagicLab Collaborator.
Teamwork Cloud
Resource Usage Map for
SysML v2
Resources
Support for SysML v2 resources has been enhanced with the implementation of a dedicated Resource Usage Map. When selecting a SysML v2 resource in the Resources application, users can now access the new “Open in Resource Usage Map” action. The generated map visualizes all dependencies of the selected SysML v2 resource, providing improved transparency and impact analysis.
Displaying SysML v2 project usages in the Resource Usage Map.
Teamwork Cloud SysML v2 REST API extensions
This release introduces two additional SysML v2-focused API extensions for Teamwork Cloud, enabling powerful CI/CD workflows for MBSE models.
Textual API Services
The textual API provides services for retrieving the textual representation of a SysML v2 model from a specified namespace. Additionally, the textual representation can be used in the payload to update a namespace of an existing SysML v2 model.
Graphical API Services
The graphical API provides a service to retrieve the visual representation of a SysML v2 diagram by its View ID. The service returns an SVG image that preserves the original diagram layout and the content of the elements used to build it.
These services are available to Magic Collaboration Studio and Teamwork Cloud Enterprise edition users.
Multi-Threaded Cross-Cluster Synchronization
A new mechanism has been implemented to allow multiple synchronization configurations to run simultaneously, with the number of concurrent executors now fully configurable. This allows for a considerably faster synchronization process.
Synchronizing multiple resources.
Modernized Web Application Platform Home Page
The Web Application Platform home page has been refreshed with a cleaner, more modern design to enhance the overall user experience. The updated interface features a visually polished appearance, making it easier for users to access the apps and information. This modernization improves usability, performance, and provides a more intuitive digital experience.
Modernized Web Application Platform home page.
Other
A new improvement introduces automatic redirection to the configured Identity Provider’s login page when SAML is the only authentication option available on the authentication server login page. This addresses a common customer request for a more streamlined login experience.
Cameo Collaborator
New Reading Mode in Collaborator
A new Reading mode has been introduced in Cameo Collaborator to provide a focused, distraction-free viewing experience.
When the Reading mode is enabled, c
ommenting, editing, and simulation tabs are hidden, and e
xisting comments are no longer displayed within the content. This allows
users to review documents in a clean, read-only format, making it easier to concentrate on the content without interactive elements.
Enabling Reading mode in Cameo Collaborator.
Text Comparer in Tables
When comparing tables in Cameo Collaborator, a new “Compare texts” option is now available, enabling users to view differences directly in plain text within the table for added convenience and clarity.
Comparing texts in a table in Cameo Collaborator.
Additional Table Export Options in Document Exporter
PDF export has been enhanced with the ability to automatically generate a Table of Figures, Table of Diagrams, and Table of Tables, providing improved document structure and navigation.
New Document Exporter options.
Authentication Using Personal Access Token
When publishing documents from the command line, you now have the option to use your personal access token instead of your username and password. This increases security as you do not have to input your data in plain text and eliminates the need to update the properties file in case your password changes.
Other
Zooming in Cameo Collaborator is now smoother for a better viewing experience.
It is now possible to edit the To Do property directly in Cameo Collaborator.
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
<ul aria-hidden="false" class="vertical menu js-loading accordion-menu renderPageTree scroll-y" data-accordion-menu="" data-current="/VN/2026x-refresh1/magic-collaboration-studio-teamwork-cloud-and-services-314179937.html" data-root="/VN/2026x-refresh1/2026x-refresh1-version-news-314179593.html" data-submenu-toggle="true" data-viewport-id="AC1032020199C466FD24A2C8640CCE1F">
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
<li class="breadcrumbs--active js-hide-until-loaded"><span class="show-for-sr">Current: </span>Magic Collaboration Studio / Teamwork Cloud and Services</li>
</ul>
</nav>
<h1 class="cell article__heading js-loading js-loading__stacked js-loading__stacked--heading" role="heading"><span class="js-hide-until-loaded">Magic Collaboration Studio / Teamwork Cloud and Services</span></h1>
</header>
<section class="cell page" id="content" role="main">
<div class="cell wiki-content js-tocBot-content js-hide-until-loaded hc-content-width--wide" id="main-content">
<div class="conf-macro output-block" data-hasbody="true" data-macro-name="sp-pagelayout"><div class="sp-grid-section">
<div class="sp-grid-cell sp-grid-100">
<h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-Releasedon:June26,2026" style="text-align: center;">Released on: June 26, 2026</h6><p><br/></p><p><span style="letter-spacing: 0.0px;">One of the most important additions in 2026x Refresh1 is </span><span class="inline-comment-marker" data-ref="e7c56320-035e-4fe6-8601-8a99bcda26b1">MagicLab Collaborator, introduced to enable collaborative work on SysML v2 projects with branch-based feedback, commenting, and multi-branch review capabilities.</span></p><p>2026x Refresh1 release also delivers a brand <span data-ref="c33df0be-aaaa-4773-a303-46fba4c7ca43">new Resource Usage Map for SysML v2 resources that enhances impact analysis and a</span> <span data-ref="650b56f5-fa8f-412c-802a-bc23f4c74512">modernized Web Application Platform home page with a cleaner design and improved usability</span>. Additional improvements include automatic SAML login redirection and configurable parallel execution of synchronization jobs.</p><p>Cameo Collaborator introduces a new Reader mode for distraction-free viewing, text comparison directly within tables, enhanced PDF export options with automatic tables of figures, diagrams, and tables, smoother zooming, and the ability to edit the To Do property. </p>
</div>
</div>
<div class="sp-grid-section">
<div class="sp-grid-cell sp-grid-100">
<p><br/></p>
</div>
</div>
<div class="sp-grid-section">
<div class="sp-grid-cell sp-grid-100">
<h2 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-MagicLabCollaborator">MagicLab Collaborator</h2><p><span style="color:var(--ds-text,#172b4d);">We introduce MagicLab Collaborator, a service that enables teams to collaborate on SysML v2 projects. Building on the capabilities of MagicLab, which is a read-only viewer, MagicLab Collaborator includes flexible collaboration features such as branch-specific feedback, commenting with search and editing, and support for working across multiple branches. Users can also open and review both current and historical branches, improving traceability and team coordination.</span></p><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-Commenting"><span style="color:var(--ds-text,#172b4d);">Commenting</span></h3><p><span style="color:var(--ds-text,#172b4d);">Commenting features, available with a Cameo Collaborator license, provide flexible ways to collaborate on specific elements and to view all comments of the project with easy navigation.</span></p><p><span style="color:var(--ds-text,#172b4d);"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image image-center" src="/VN/files/2026x-refresh1/314179937/314181592/1/1782384599078/magiclab_individual_element_comments.png" width="1400"/></span><br/></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-ViewingcommentsforaspecificelementintheelementSpecificationpanel." style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">Viewing comments for a specific element in the element Specification panel.</span></h6><p><span style="color:var(--ds-text,#172b4d);"><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image confluence-content-image-border image-center" height="856" src="/VN/files/2026x-refresh1/314179937/314181590/2/1782384544825/magiclab_collaborator_comments.png" width="1400"/></span></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-CommentingfeaturesofMagicLabCollaborator." style="text-align: center;"><span style="color:var(--ds-text,#172b4d);">Commenting features of MagicLab Collaborator.</span></h6><h2 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-TeamworkCloud">Teamwork Cloud</h2><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-ResourceUsageMapforSysMLv2Resources"><span style="letter-spacing: -0.006em;">Resource Usage Map for <span class="inline-comment-marker" data-ref="4afb749c-13c4-449f-88bf-e78fb21179b4">SysML v2</span> Resources</span></h3><p><span>Support for SysML v2 resources has been enhanced with the implementation of a dedicated Resource Usage Map. When selecting a SysML v2 resource in the Resources application, users can now access the new “Open in Resource Usage Map” action. The generated map visualizes all dependencies of the selected SysML v2 resource, providing improved transparency and impact analysis.</span></p><p><span><span class="confluence-embedded-file-wrapper image-center-wrapper conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image image-center" src="/VN/files/2026x-refresh1/314179937/314179941/1/1781598636094/sysmlv2_project_usages.png"/></span></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-DisplayingSysMLv2projectusagesintheResourceUsageMap." style="text-align: center;"><span>Displaying SysML v2 project usages in the Resource Usage Map.</span></h6><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-TeamworkCloudSysMLv2RESTAPIextensions" style="color:var(--ds-text,#172b4d);"><span style="letter-spacing: -0.006em;">Teamwork Cloud SysML v2 REST API extensions</span></h3><p style="font-size: 14.0px;font-weight: 400;letter-spacing: normal;"><span style="letter-spacing: -0.006em;"><span>This release introduces two additional SysML v2-focused API extensions for Teamwork Cloud, enabling powerful CI/CD workflows for MBSE models.</span></span></p><h4 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-TextualAPIServices" style="line-height: 1.42857;color:var(--ds-text,#172b4d);"><span style="letter-spacing: -0.006em;"><span><strong>Textual API Services</strong></span></span></h4><p>The textual API provides services for retrieving the textual representation of a SysML v2 model from a specified namespace. Additionally, the textual representation can be used in the payload to update a namespace of an existing SysML v2 model.</p><h4 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-GraphicalAPIServices" style="line-height: 1.42857;color:var(--ds-text,#172b4d);"><span style="letter-spacing: -0.006em;"><span><strong>Graphical API Services</strong></span></span></h4><p style="font-size: 14.0px;font-weight: 400;letter-spacing: normal;"><span style="letter-spacing: -0.006em;"><span>The graphical API provides a service to retrieve the visual representation of a SysML v2 diagram by its View ID. The service returns an SVG image that preserves the original diagram layout and the content of the elements used to build it.</span></span></p><p style="font-size: 14.0px;font-weight: 400;letter-spacing: normal;"><span style="letter-spacing: -0.006em;"><span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image image-center" src="/VN/files/2026x-refresh1/314179937/314182191/4/1782730053011/teamwork_cloud_sysml2_api.png" width="1400"/></span></span></span></p><p style="font-size: 14.0px;font-weight: 400;letter-spacing: normal;"><br/></p><p style="font-size: 14.0px;font-weight: 400;letter-spacing: normal;"><span style="letter-spacing: -0.006em;"><span>These services are available to Magic Collaboration Studio and Teamwork Cloud Enterprise edition users.</span></span></p><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-Multi-ThreadedCross-ClusterSynchronization">Multi-Threaded Cross-Cluster Synchronization</h3><p><span>A new mechanism has been implemented to allow multiple synchronization configurations to run simultaneously, with the number of concurrent executors now fully configurable. This allows for a considerably faster synchronization process.</span></p><p><span><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image confluence-content-image-border image-center" height="667" src="/VN/files/2026x-refresh1/314179937/314179939/1/1781598636020/multi_threaded_sync.png" width="1000"/></span></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-Synchronizingmultipleresources." style="text-align: center;">Synchronizing multiple resources.</h6><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-ModernizedWebApplicationPlatformHomePage"><span style="letter-spacing: -0.006em;">Modernized Web Application Platform Home Page</span></h3><p><span class="inline-comment-marker" data-ref="27d99c58-398d-4478-a04e-d4742a1e0707">The Web Application Platform home page has been refreshed with a cleaner, more modern design to enhance the overall user experience. The updated interface features a visually polished appearance, making it easier for users to access the apps and information. This modernization improves usability, performance, and provides a more intuitive digital experience.</span></p><p style="text-align: center;"><span class="confluence-embedded-file-wrapper confluence-embedded-manual-size conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image" src="/VN/files/2026x-refresh1/314179937/314179944/1/1781598636189/webapp_home_page.png" width="1000"/></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-ModernizedWebApplicationPlatformhomepage." style="text-align: center;">Modernized Web Application Platform home page.</h6><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-Other"><span style="letter-spacing: 0.0px;">Other</span></h3><ul><li><span style="letter-spacing: 0.0px;">A new improvement introduces automatic redirection to the configured Identity Provider’s login page when SAML is the only authentication option available on the authentication server login page. This addresses a common customer request for a more streamlined login experience.</span></li></ul><h2 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-CameoCollaborator">Cameo Collaborator</h2><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-NewReadingModeinCollaborator"><span style="letter-spacing: -0.006em;">New Reading Mode in Collaborator</span></h3><p><span class="inline-comment-marker" data-ref="a12e0f65-f237-4ebc-a5d6-000d09a94126">A new Reading mode has been introduced in Cameo Collaborator to provide a focused, distraction-free viewing experience. </span><span style="letter-spacing: 0.0px;"><span class="inline-comment-marker" data-ref="a12e0f65-f237-4ebc-a5d6-000d09a94126">When the Reading mode is enabled, c</span></span><span style="letter-spacing: 0.0px;"><span class="inline-comment-marker" data-ref="a12e0f65-f237-4ebc-a5d6-000d09a94126">ommenting, editing, and simulation tabs are hidden, and e</span></span><span style="letter-spacing: 0.0px;"><span class="inline-comment-marker" data-ref="a12e0f65-f237-4ebc-a5d6-000d09a94126">xisting comments are no longer displayed within the content. This allows </span></span><span style="letter-spacing: 0.0px;"><span class="inline-comment-marker" data-ref="a12e0f65-f237-4ebc-a5d6-000d09a94126">users to review documents in a clean, read-only format, making it easier to concentrate on the content without interactive elements.</span></span></p><p><span style="letter-spacing: 0.0px;"><span class="inline-comment-marker" data-ref="a12e0f65-f237-4ebc-a5d6-000d09a94126"><span class="confluence-embedded-file-wrapper image-center-wrapper conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image image-center" src="/VN/files/2026x-refresh1/314179937/314179942/1/1781598636125/reading_mode.png"/></span></span></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-EnablingReadingmodeinCameoCollaborator." style="text-align: center;"><span style="letter-spacing: 0.0px;"><span class="inline-comment-marker" data-ref="a12e0f65-f237-4ebc-a5d6-000d09a94126">Enabling Reading mode in Cameo Collaborator.</span></span></h6><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-TextComparerinTables"><span style="letter-spacing: -0.006em;">Text Comparer in Tables</span></h3><p><span style="color:var(--ds-text,#172b4d);"><span class="inline-comment-marker" data-ref="0f0dac8e-d23f-4196-9d5f-9cd72034732e">When comparing tables in Cameo Collaborator, a new “Compare texts” option is now available, enabling users to view differences directly in plain text within the table for added convenience and clarity.</span></span></p><p><span style="color:var(--ds-text,#172b4d);"><span class="inline-comment-marker" data-ref="0f0dac8e-d23f-4196-9d5f-9cd72034732e"><span class="confluence-embedded-file-wrapper image-center-wrapper conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image image-center" src="/VN/files/2026x-refresh1/314179937/314179943/1/1781598636157/compare_texts.png"/></span></span></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-ComparingtextsinatableinCameoCollaborator." style="text-align: center;"><span style="color:var(--ds-text,#172b4d);"><span class="inline-comment-marker" data-ref="0f0dac8e-d23f-4196-9d5f-9cd72034732e">Comparing texts in a table in Cameo Collaborator.</span></span></h6><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-AdditionalTableExportOptionsinDocumentExporter"><span style="color:var(--ds-text,#172b4d);">Additional Table Export Options in Document Exporter</span></h3><p>PDF export has been enhanced with the ability to automatically generate a Table of Figures, Table of Diagrams, and Table of Tables, providing improved document structure and navigation.</p><p><span class="confluence-embedded-file-wrapper image-center-wrapper confluence-embedded-manual-size conf-macro output-inline" data-hasbody="false" data-macro-name="sp-image"><img class="confluence-embedded-image confluence-content-image-border image-center" height="782" src="/VN/files/2026x-refresh1/314179937/314179945/1/1781598636219/new_table_options_in_collaborator_export.png" width="493"/></span></p><h6 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-NewDocumentExporteroptions." style="text-align: center;">New Document Exporter options.</h6><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-AuthenticationUsingPersonalAccessToken">Authentication Using Personal Access Token</h3><p>When publishing documents from the command line, you now have the option to use your personal access token instead of your username and password. This increases security as you do not have to input your data in plain text and eliminates the need to update the properties file in case your password changes.</p><h3 id="id-(2026xRefresh1)MagicCollaborationStudio/TeamworkCloudandServices-Other.1">Other</h3><ul><li data-uuid="9b3fb775-4f5d-496f-a6d5-20d1dbf3f61f"><p>Zooming in Cameo Collaborator is now smoother for a better viewing experience.</p></li><li data-uuid="a2715b21-7ae7-44a9-8a3c-57981d03ab8b">It is now possible to edit the To Do property directly in Cameo Collaborator.</li></ul>
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
