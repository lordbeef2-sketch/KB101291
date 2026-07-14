# JAVA OPENAPI: ProjectPartListenerAdapter (2024x API)

- source_url: https://jdocs.nomagic.com/2024xRefresh1/com/nomagic/magicdraw/core/project/ProjectPartListenerAdapter.html
- source_path: `com/nomagic/magicdraw/core/project/ProjectPartListenerAdapter.html`
- source_sha256: `12ee088d0663c18266ab9093b3546b215475acd68c4ac2dbedc3812d72250d7d`
- captured_utc: `2026-07-14T16:51:16.273137+00:00`

## NORMALIZED JAVADOC CONTENT

======== START OF CLASS DATA ========

Package [com.nomagic.magicdraw.core.project](package-summary.html)

## Class ProjectPartListenerAdapter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter](ProjectEventListenerAdapter.html)
com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter
com.nomagic.magicdraw.core.project.ProjectPartListenerAdapter

All Implemented Interfaces:
`[ProjectEventListener](ProjectEventListener.html)`, `[ProjectPartListener](ProjectPartListener.html)`, `[ProjectPartLoadedListener](ProjectPartLoadedListener.html)`

@OpenApiAllpublic classProjectPartListenerAdapter
extends com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter
implements [ProjectPartListener](ProjectPartListener.html)

======== CONSTRUCTOR SUMMARY ======== 
Constructor Summary
Constructors
Constructor
Description
`[ProjectPartListenerAdapter](#%3Cinit%3E())()`
 ========== METHOD SUMMARY =========== 
Method Summary
All MethodsInstance MethodsConcrete Methods
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
Methods inherited from class com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter
`projectPartLoaded`
Methods inherited from class com.nomagic.magicdraw.core.project.[ProjectEventListenerAdapter](ProjectEventListenerAdapter.html)
`[projectActivated](ProjectEventListenerAdapter.html#projectActivated(com.nomagic.magicdraw.core.Project)), [projectActivatedFromGUI](ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectDeActivated](ProjectEventListenerAdapter.html#projectDeActivated(com.nomagic.magicdraw.core.Project)), [projectOpened](ProjectEventListenerAdapter.html#projectOpened(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosed](ProjectEventListenerAdapter.html#projectPreClosed(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreSaved](ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean))`
Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))`
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectEventListener](ProjectEventListener.html)
`[projectActivated](ProjectEventListener.html#projectActivated(com.nomagic.magicdraw.core.Project)), [projectActivatedFromGUI](ProjectEventListener.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)), [projectClosed](ProjectEventListener.html#projectClosed(com.nomagic.magicdraw.core.Project)), [projectCreated](ProjectEventListener.html#projectCreated(com.nomagic.magicdraw.core.Project)), [projectDeActivated](ProjectEventListener.html#projectDeActivated(com.nomagic.magicdraw.core.Project)), [projectOpened](ProjectEventListener.html#projectOpened(com.nomagic.magicdraw.core.Project)), [projectOpenedFromGUI](ProjectEventListener.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreActivated](ProjectEventListener.html#projectPreActivated(com.nomagic.magicdraw.core.Project)), [projectPreClosed](ProjectEventListener.html#projectPreClosed(com.nomagic.magicdraw.core.Project)), [projectPreClosedFinal](ProjectEventListener.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)), [projectPreDeActivated](ProjectEventListener.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)), [projectPreOpenedFromGUI](ProjectEventListener.html#projectPreOpenedFromGUI(com.nomagic.magicdraw.core.Project)), [projectPreSaved](ProjectEventListener.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectReplaced](ProjectEventListener.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)), [projectSaved](ProjectEventListener.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)), [projectUsedFromGUI](ProjectEventListener.html#projectUsedFromGUI(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject,com.nomagic.ci.persistence.IAttachedProject))`
Methods inherited from interface com.nomagic.magicdraw.core.project.[ProjectPartLoadedListener](ProjectPartLoadedListener.html)
`[projectPartLoaded](ProjectPartLoadedListener.html#projectPartLoaded(com.nomagic.magicdraw.core.Project,com.nomagic.ci.persistence.IProject))`

========= CONSTRUCTOR DETAIL ======== 
Constructor Details
ProjectPartListenerAdapter
public ProjectPartListenerAdapter()
 ============ METHOD DETAIL ========== 
Method Details
projectPartAttached
public void projectPartAttached([ModuleUsage](../modules/ModuleUsage.html) usage)
Description copied from interface: `[ProjectPartListener](ProjectPartListener.html#projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage))`
Project is attached to another project or module.
Specified by:
`[projectPartAttached](ProjectPartListener.html#projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage))` in interface `[ProjectPartListener](ProjectPartListener.html)`
Parameters:
`usage` - information about attached project part.
projectPartDetached
public void projectPartDetached([ModuleUsage](../modules/ModuleUsage.html) usage)
Description copied from interface: `[ProjectPartListener](ProjectPartListener.html#projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage))`
Project is detached from project or module. Detached project may still be attached to another project.
Specified by:
`[projectPartDetached](ProjectPartListener.html#projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage))` in interface `[ProjectPartListener](ProjectPartListener.html)`
Parameters:
`usage` - information about removed project part.
projectPartRemoved
public void projectPartRemoved(com.nomagic.ci.persistence.IProject project)
Description copied from interface: `[ProjectPartListener](ProjectPartListener.html#projectPartRemoved(com.nomagic.ci.persistence.IProject))`
Previously attached project is removed and is no longer available.
Specified by:
`[projectPartRemoved](ProjectPartListener.html#projectPartRemoved(com.nomagic.ci.persistence.IProject))` in interface `[ProjectPartListener](ProjectPartListener.html)`
Parameters:
`project` - project which is removed.

========= END OF CLASS DATA =========

## EXACT JAVADOC MAIN HTML

````html
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.nomagic.magicdraw.core.project</a></div>
<h1 class="title" title="Class ProjectPartListenerAdapter">Class ProjectPartListenerAdapter</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter</a>
<div class="inheritance">com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter
<div class="inheritance">com.nomagic.magicdraw.core.project.ProjectPartListenerAdapter</div>
</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="ProjectEventListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectEventListener</a></code>, <code><a href="ProjectPartListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartListener</a></code>, <code><a href="ProjectPartLoadedListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartLoadedListener</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations">@OpenApiAll
</span><span class="modifiers">public class </span><span class="element-name type-name-label">ProjectPartListenerAdapter</span>
<span class="extends-implements">extends com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter
implements <a href="ProjectPartListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartListener</a></span></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">
<h2>Constructor Summary</h2>
<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">ProjectPartListenerAdapter</a>()</code></div>
<div class="col-last even-row-color"> </div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div id="method-summary-table.tabpanel" role="tabpanel">
<div aria-labelledby="method-summary-table-tab0" class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">projectPartAttached</a><wbr/>(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Project is attached to another project or module.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">projectPartDetached</a><wbr/>(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Project is detached from  project or module.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#projectPartRemoved(com.nomagic.ci.persistence.IProject)">projectPartRemoved</a><wbr/>(com.nomagic.ci.persistence.IProject project)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Previously attached project is removed and is no longer available.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter">Methods inherited from class com.nomagic.magicdraw.core.project.ProjectPartLoadedListenerAdapter</h3>
<code>projectPartLoaded</code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-com.nomagic.magicdraw.core.project.ProjectEventListenerAdapter">Methods inherited from class com.nomagic.magicdraw.core.project.<a href="ProjectEventListenerAdapter.html" title="class in com.nomagic.magicdraw.core.project">ProjectEventListenerAdapter</a></h3>
<code><a href="ProjectEventListenerAdapter.html#projectActivated(com.nomagic.magicdraw.core.Project)">projectActivated</a>, <a href="ProjectEventListenerAdapter.html#projectActivatedFromGUI(com.nomagic.magicdraw.core.Project)">projectActivatedFromGUI</a>, <a href="ProjectEventListenerAdapter.html#projectClosed(com.nomagic.magicdraw.core.Project)">projectClosed</a>, <a href="ProjectEventListenerAdapter.html#projectCreated(com.nomagic.magicdraw.core.Project)">projectCreated</a>, <a href="ProjectEventListenerAdapter.html#projectDeActivated(com.nomagic.magicdraw.core.Project)">projectDeActivated</a>, <a href="ProjectEventListenerAdapter.html#projectOpened(com.nomagic.magicdraw.core.Project)">projectOpened</a>, <a href="ProjectEventListenerAdapter.html#projectOpenedFromGUI(com.nomagic.magicdraw.core.Project)">projectOpenedFromGUI</a>, <a href="ProjectEventListenerAdapter.html#projectPreActivated(com.nomagic.magicdraw.core.Project)">projectPreActivated</a>, <a href="ProjectEventListenerAdapter.html#projectPreClosed(com.nomagic.magicdraw.core.Project)">projectPreClosed</a>, <a href="ProjectEventListenerAdapter.html#projectPreClosedFinal(com.nomagic.magicdraw.core.Project)">projectPreClosedFinal</a>, <a href="ProjectEventListenerAdapter.html#projectPreDeActivated(com.nomagic.magicdraw.core.Project)">projectPreDeActivated</a>, <a href="ProjectEventListenerAdapter.html#projectPreSaved(com.nomagic.magicdraw.core.Project,boolean)">projectPreSaved</a>, <a href="ProjectEventListenerAdapter.html#projectReplaced(com.nomagic.magicdraw.core.Project,com.nomagic.magicdraw.core.Project)">projectReplaced</a>, <a href="ProjectEventListenerAdapter.html#projectSaved(com.nomagic.magicdraw.core.Project,boolean)">projectSaved</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">
<h2>Constructor Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>ProjectPartListenerAdapter</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProjectPartListenerAdapter</span>()</div>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>projectPartAttached</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPartAttached</span><wbr/><span class="parameters">(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProjectPartListener.html#projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">ProjectPartListener</a></code></span></div>
<div class="block">Project is attached to another project or module.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPartListener.html#projectPartAttached(com.nomagic.magicdraw.core.modules.ModuleUsage)">projectPartAttached</a></code> in interface <code><a href="ProjectPartListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>usage</code> - information about attached project part.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">
<h3>projectPartDetached</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPartDetached</span><wbr/><span class="parameters">(<a href="../modules/ModuleUsage.html" title="class in com.nomagic.magicdraw.core.modules">ModuleUsage</a> usage)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProjectPartListener.html#projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">ProjectPartListener</a></code></span></div>
<div class="block">Project is detached from  project or module. Detached project may still be attached to another project.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPartListener.html#projectPartDetached(com.nomagic.magicdraw.core.modules.ModuleUsage)">projectPartDetached</a></code> in interface <code><a href="ProjectPartListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartListener</a></code></dd>
<dt>Parameters:</dt>
<dd><code>usage</code> - information about removed project part.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="projectPartRemoved(com.nomagic.ci.persistence.IProject)">
<h3>projectPartRemoved</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">projectPartRemoved</span><wbr/><span class="parameters">(com.nomagic.ci.persistence.IProject project)</span></div>
<div class="block"><span class="descfrm-type-label">Description copied from interface: <code><a href="ProjectPartListener.html#projectPartRemoved(com.nomagic.ci.persistence.IProject)">ProjectPartListener</a></code></span></div>
<div class="block">Previously attached project is removed and is no longer available.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="ProjectPartListener.html#projectPartRemoved(com.nomagic.ci.persistence.IProject)">projectPartRemoved</a></code> in interface <code><a href="ProjectPartListener.html" title="interface in com.nomagic.magicdraw.core.project">ProjectPartListener</a></code></dd>
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
