# JAVA OPENAPI: ProjectWindowsConfigurator (2024x API)

- source_url: https://jdocs.nomagic.com/2024x/com/nomagic/magicdraw/ui/ProjectWindowsConfigurator.html
- source_path: `com/nomagic/magicdraw/ui/ProjectWindowsConfigurator.html`
- source_sha256: `554c76bac4976fc800f334ca9bcf2333aa3d9cbe9c2fb782f55e47672dbaed1b`
- captured_utc: `2026-07-14T16:52:02.811757+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.ui](package-summary.html)

## Interface ProjectWindowsConfigurator

@OpenApiAllpublic interfaceProjectWindowsConfigurator

Project window configurator. It should add/remove project window to manager.
 Use [`ProjectWindowsManager.ConfiguratorRegistry`](ProjectWindowsManager.ConfiguratorRegistry.html) to register this configurator.
 Use configurator if you want to have persistence docking state for your ProjectWindows.

See Also:
[`ProjectWindowsManager.ConfiguratorRegistry`](ProjectWindowsManager.ConfiguratorRegistry.html)

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[configure](#configure(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindowsManager))([Project](../core/Project.html) project,
 [ProjectWindowsManager](ProjectWindowsManager.html) projectWindowsManager)`
Configure project windows

============ METHOD DETAIL ========== 
Method Details
configure
void configure([Project](../core/Project.html) project,
 [ProjectWindowsManager](ProjectWindowsManager.html) projectWindowsManager)
Configure project windows
Parameters:
`project` - project
`projectWindowsManager` - manager
See Also:
[`ProjectWindowsManager.addWindow(Project, ProjectWindow)`](ProjectWindowsManager.html#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow))
[`ProjectWindowsManager.removeWindow(Project, String)`](ProjectWindowsManager.html#removeWindow(com.nomagic.magicdraw.core.Project,java.lang.String))

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.ui</a></div>
<h1 class="title" title="Interface ProjectWindowsConfigurator">Interface ProjectWindowsConfigurator</h1>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectWindowsConfigurator</span></div>
<div class="block">Project window configurator. It should add/remove project window to manager.
 Use <a href="ProjectWindowsManager.ConfiguratorRegistry.html" title="class in com.nomagic.magicdraw.ui"><code>ProjectWindowsManager.ConfiguratorRegistry</code></a> to register this configurator.
 Use configurator if you want to have persistence docking state for your ProjectWindows.</div>
<dl class="notes">
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="ProjectWindowsManager.ConfiguratorRegistry.html" title="class in com.nomagic.magicdraw.ui"><code>ProjectWindowsManager.ConfiguratorRegistry</code></a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#configure(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindowsManager)">configure</a><wbr/>(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindowsManager.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowsManager</a> projectWindowsManager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Configure project windows</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="configure(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindowsManager)">
<h3>configure</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">configure</span><wbr/><span class="parameters">(<a href="../core/Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 <a href="ProjectWindowsManager.html" title="interface in com.nomagic.magicdraw.ui">ProjectWindowsManager</a> projectWindowsManager)</span></div>
<div class="block">Configure project windows</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project</dd>
<dd><code>projectWindowsManager</code> - manager</dd>
<dt>See Also:</dt>
<dd>
<ul class="see-list-long">
<li><a href="ProjectWindowsManager.html#addWindow(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.ui.ProjectWindow)"><code>ProjectWindowsManager.addWindow(Project, ProjectWindow)</code></a></li>
<li><a href="ProjectWindowsManager.html#removeWindow(com.nomagic.magicdraw.core.Project,java.lang.String)"><code>ProjectWindowsManager.removeWindow(Project, String)</code></a></li>
</ul>
</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>
````
