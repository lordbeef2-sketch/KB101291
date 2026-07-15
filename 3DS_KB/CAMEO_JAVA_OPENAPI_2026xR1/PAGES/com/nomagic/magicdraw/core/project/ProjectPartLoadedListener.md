# JAVA OPENAPI: ProjectPartLoadedListener (2026x Refresh1 API)

- source_url: https://jdocs.nomagic.com/2026xRefresh1/com/nomagic/magicdraw/core/project/ProjectPartLoadedListener.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectPartLoadedListener.html`
- source_sha256: `83f4c0b2ce2ab1f56708209be18d33ed7e534e94ecbc13cf8c1b171ae39c5bf6`
- captured_utc: `2026-07-14T16:45:31.547423+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Interface ProjectPartLoadedListener

All Superinterfaces:
`[ProjectEventListener](ProjectEventListener.html)`

All Known Subinterfaces:
`[ProjectPartListener](ProjectPartListener.html)`

All Known Implementing Classes:
`[ProjectPartListenerAdapter](ProjectPartListenerAdapter.html)`, `com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter`

@OpenApiAllpublic interfaceProjectPartLoadedListenerextends [ProjectEventListener](ProjectEventListener.html)

Listener witch listen project part load. Event is fired when model or project is loaded. Diagram
 are loaded also. On teamwork or module update event will be fired only after removing element. It
 is necessary to fire after elements remove because some updated elements can be deleted from part
 during element remove process.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[projectPartLoaded](#projectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject))([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject storage)`
Method called during project load process, when project part and diagrams are loaded.
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectEventListener](ProjectEventListener.html)
`[projectActivated](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)), [projectActivatedFromGUI](ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectDeActivated](ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)), [projectOpened](ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosed](ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreOpenedFromGUI](ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreSaved](ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectUsedFromGUI](ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))`

============ METHOD DETAIL ========== 
Method Details
projectPartLoaded
void projectPartLoaded([Project](../Project.html) project,
 com.nomagic.ci.persistence.IProject storage)
Method called during project load process, when project part and diagrams are loaded.
Parameters:
`project` - project in which part is loaded.
`storage` - module or primary project which is loaded.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Interface ProjectPartLoadedListener">Interface ProjectPartLoadedListener</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Subinterfaces:</dt>
<dd><code><a href="ProjectPartListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartListener</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ProjectPartListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectPartListenerAdapter</a></code>, <code>com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter</code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectPartLoadedListener</span><span class="extends-implements">
extends <a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></span></div>
<div class="block">Listener witch listen project part load. Event is fired when model or project is loaded. Diagram
 are loaded also. On teamwork or module update event will be fired only after removing element. It
 is necessary to fire after elements remove because some updated elements can be deleted from part
 during element remove process.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject)">projectPartLoaded</a><wbr/>(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject storage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Method called during project load process, when project part and diagrams are loaded.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListener">Methods inherited from interface com.nomagic.magicdraw.core.project.<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></h3>
<code><a href="ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a>, <a href="ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a>, <a href="ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a>, <a href="ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a>, <a href="ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a>, <a href="ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a>, <a href="ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a>, <a href="ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a>, <a href="ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a>, <a href="ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a>, <a href="ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a>, <a href="ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectPreOpenedFromGUI</a>, <a href="ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a>, <a href="ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a>, <a href="ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a>, <a href="ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">projectUsedFromGUI</a></code></div>
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
<section class="detail" id="projectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject)">
<h3>projectPartLoaded</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPartLoaded</span><wbr/><span class="parameters">(<a href="../Project.html" title="class in com.nomagic.magicdraw.core">Project</a> project,
 com.nomagic.ci.persistence.IProject storage)</span></div>
<div class="block">Method called during project load process, when project part and diagrams are loaded.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project in which part is loaded.</dd>
<dd><code>storage</code> - module or primary project which is loaded.</dd>
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
