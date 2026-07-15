# JAVA OPENAPI: ProjectPartListener (2024x Refresh3 API)

- source_url: https://jdocs.nomagic.com/2024xRefresh3/com/nomagic/magicdraw/core/project/ProjectPartListener.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectPartListener.html`
- source_sha256: `7834eeee13f56660e5abd857f5515fc17c1a50749a17b57995e5aa6f99d5ee12`
- captured_utc: `2026-07-14T16:55:13.341987+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Interface ProjectPartListener

All Superinterfaces:
`[ProjectEventListener](ProjectEventListener.html)`, `[ProjectPartLoadedListener](ProjectPartLoadedListener.html)`

All Known Implementing Classes:
`[ProjectPartListenerAdapter](ProjectPartListenerAdapter.html)`

@OpenApiAllpublic interfaceProjectPartListenerextends [ProjectPartLoadedListener](ProjectPartLoadedListener.html)

Listener which informs about modules attach, detach, load and remove.

========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsAbstract Methods
Modifier and Type
Method
Description
`void`
`[projectPartAttached](#projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../modules/ModuleUsage.html) usage)`
Project is attached to another project or module.
`void`
`[projectPartDetached](#projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage))([ModuleUsage](../modules/ModuleUsage.html) usage)`
Project is detached from project or module.
`void`
`[projectPartRemoved](#projectPartRemoved(com.nomagic.ci.persistence.IProject))(com.nomagic.ci.persistence.IProject project)`
Previously attached project is removed and is no longer available.
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectEventListener](ProjectEventListener.html)
`[projectActivated](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)), [projectActivatedFromGUI](ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectDeActivated](ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)), [projectOpened](ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosed](ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreOpenedFromGUI](ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreSaved](ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectUsedFromGUI](ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))`
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectPartLoadedListener](ProjectPartLoadedListener.html)
`[projectPartLoaded](ProjectPartLoadedListener.html#projectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject))`

============ METHOD DETAIL ========== 
Method Details
projectPartAttached
void projectPartAttached([ModuleUsage](../modules/ModuleUsage.html) usage)
Project is attached to another project or module.
Parameters:
`usage` - information about attached project part.
projectPartDetached
void projectPartDetached([ModuleUsage](../modules/ModuleUsage.html) usage)
Project is detached from project or module. Detached project may still be attached to another project.
Parameters:
`usage` - information about removed project part.
projectPartRemoved
void projectPartRemoved(com.nomagic.ci.persistence.IProject project)
Previously attached project is removed and is no longer available.
Parameters:
`project` - project which is removed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Interface ProjectPartListener">Interface ProjectPartListener</h1>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Superinterfaces:</dt>
<dd><code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code>, <code><a href="ProjectPartLoadedListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartLoadedListener</a></code></dd>
</dl>
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="ProjectPartListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectPartListenerAdapter</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">ProjectPartListener</span><span class="extends-implements">
extends <a href="ProjectPartLoadedListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartLoadedListener</a></span></div>
<div class="block">Listener which informs about modules attach, detach, load and remove.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">projectPartAttached</a><wbr/>(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Project is attached to another project or module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">projectPartDetached</a><wbr/>(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Project is detached from  project or module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#projectPartRemoved(com.nomagic.ci.persistence.IProject)">projectPartRemoved</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Previously attached project is removed and is no longer available.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListener">Methods inherited from interface com.nomagic.magicdraw.core.project.<a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></h3>
<code><a href="ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a>, <a href="ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a>, <a href="ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a>, <a href="ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a>, <a href="ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a>, <a href="ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a>, <a href="ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a>, <a href="ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a>, <a href="ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a>, <a href="ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a>, <a href="ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a>, <a href="ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectPreOpenedFromGUI</a>, <a href="ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a>, <a href="ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a>, <a href="ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a>, <a href="ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject)">projectUsedFromGUI</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectPartLoadedListener">Methods inherited from interface com.nomagic.magicdraw.core.project.<a href="ProjectPartLoadedListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartLoadedListener</a></h3>
<code><a href="ProjectPartLoadedListener.html#projectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject)">projectPartLoaded</a></code></div>
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
<section class="detail" id="projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>projectPartAttached</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPartAttached</span><wbr/><span class="parameters">(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</span></div>
<div class="block">Project is attached to another project or module.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usage</code> - information about attached project part.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>projectPartDetached</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPartDetached</span><wbr/><span class="parameters">(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</span></div>
<div class="block">Project is detached from  project or module. Detached project may still be attached to another project.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>usage</code> - information about removed project part.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPartRemoved(com.nomagic.ci.persistence.IProject)">
<h3>projectPartRemoved</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">projectPartRemoved</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block">Previously attached project is removed and is no longer available.</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>project</code> - project which is removed.</dd>
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
